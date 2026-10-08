# Task 3 report: check script reads only what may be read

## Step 2 (RED): tests against the prototype script

Command: `python -B gate/run_tests.py instruction-files` (full output kept at `.runs/task-cycles/instruction-files-part/reports/check_3_red_full.txt`).

Result: `Ran 45 tests`, `FAILED (failures=11, errors=7, skipped=1)`.

- ERRORs (7): `test_a_broken_link_is_reported`, `test_a_character_cut_at_the_limit_does_not_make_the_text_invalid`, `test_a_file_gone_mid_run_is_reported_and_the_run_goes_on`, `test_a_file_that_is_not_a_readable_regular_file_exits_with_2` (2 subtests), `test_a_file_without_permission_is_reported`, `test_only_the_first_mebibyte_is_read`.
- FAILs (11): `test_a_directory_link_or_junction_is_not_followed`, `test_a_directory_named_agents_md_is_reported_and_the_run_goes_on`, `test_a_directory_that_cannot_be_listed_is_reported`, `test_a_file_link_out_of_the_repository_is_neither_read_nor_listed`, `test_a_file_that_is_not_regular_is_not_opened`, `test_a_root_that_is_not_a_directory_exits_with_2`, `test_a_utf8_byte_order_mark_is_stripped_before_every_check`, `test_control_and_bidirectional_characters_are_escaped_and_long_values_cut`, `test_text_that_is_not_utf8_is_reported_and_its_content_not_checked` (3 subtests).
- Skipped (1): the FIFO test on Windows.

Why expected: these are exactly the rows the brief lists for the prototype; the prototype reads files with `open(..., errors="replace")`, follows no guards, prints values unescaped and has no `read`/`walk` findings, so the crafted-input tests fail or error there.

## Step 4 (GREEN): implementation

Command: `python -B gate/run_tests.py instruction-files` (output at `.runs/task-cycles/instruction-files-part/reports/check_3_tests_instruction_files.txt`). Exit 0.

Result: `Ran 45 tests`, `OK (skipped=1)`. The skip is the FIFO test on Windows (per the brief; I did not print the skip reason).

Script run on the-way (`python -B instruction-files/check_instructions.py .`):

```text
WARN  dead-path AGENTS.md:20 `_zadania\` does not exist
INFO  skill-dir .claude/skills:0 12 skills in .claude/skills have no pointer in AGENTS.md; Codex does not read .claude/skills, so point to the SKILL.md of each one Codex needs
INFO  size AGENTS.md:0 21 lines, 187 words
INFO  size CLAUDE.md:0 1 lines, 1 words
0 error, 1 warn, 3 info
```

exit 0. Matches the brief's expected output exactly.

`python -B instruction-files/check_instructions.py instruction-files/SKILL.md` gives `Error: ROOT is not a directory: instruction-files/SKILL.md` and exit 2, as the brief expects.

## Files changed

- `instruction-files/check_instructions.py` (replaced whole, verbatim from the brief)
- `instruction-files/test_check_instructions.py` (replaced whole, verbatim from the brief)

Commit: `295e154` on `task/instruction-files-part`, subject `fix(instruction-files): Read only regular UTF-8 files inside the root, and report what cannot be read`, committed by explicit paths.

## Step 5: crafted-input rows and the test that pins each

- Directory link or junction, and a loop: `test_a_directory_link_or_junction_is_not_followed`.
- File link out of the repository: `test_a_file_link_out_of_the_repository_is_neither_read_nor_listed`; `--file` read through its link: `test_a_file_given_with_file_is_read_through_its_link`.
- Huge file (1 MiB cut): `test_only_the_first_mebibyte_is_read`.
- Non-regular file: `test_a_file_that_is_not_regular_is_not_opened`; FIFO: `test_a_fifo_named_like_an_instruction_file_does_not_stop_the_run`.
- UTF-8 BOM: `test_a_utf8_byte_order_mark_is_stripped_before_every_check`.
- Other encodings (UTF-16, UTF-32, invalid UTF-8): `test_text_that_is_not_utf8_is_reported_and_its_content_not_checked`.
- Printed values (control and bidi characters, long values cut): `test_control_and_bidirectional_characters_are_escaped_and_long_values_cut`.
- Unreadable files: `UnreadableFiles` class (directory named like an instruction file, broken link, permission denied, file gone mid-run).
- Unlistable directory: `test_a_directory_that_cannot_be_listed_is_reported`.
- Bad arguments: `CommandLine` class.
- Not owned by this task: the network row and the 1 MiB paragraph row (Task 4), the pointed-file row (Task 5).

## Concerns

- None blocking. The Windows FIFO skip is expected; a POSIX run would exercise that test.
- The script uses `os.path.isjunction`, which needs Python 3.12 or later. The brief targets Python 3.14, so this is fine there.

---

# Task 3 fix round 1 report: network paths, link walk, split characters

Brief: `task-3-fix-1.md`. Commit `c06b237` on `task/instruction-files-part`, subject `fix(instruction-files): Never pass a network path to the file system, and walk without following links`. Files: `instruction-files/check_instructions.py`, `instruction-files/test_check_instructions.py` only.

## RED (tests first, against the committed script `295e154`)

The new tests were written first. The non-network tests were run with a scratch runner that skips the `NetworkPaths` class (saved at `.runs/task-cycles/instruction-files-part/reports/check_3_fix1_red_nonnetwork.txt`):

```text
Ran 47 tests in 0.505s
FAILED (failures=3, skipped=1)
FAIL: test_a_network_path_given_as_root_or_file_exits_with_2_without_a_lookup (arguments=['--file', '\\\\192.0.2.1\\share\\x.md'])
FAIL: test_a_network_path_given_as_root_or_file_exits_with_2_without_a_lookup (arguments=['\\\\192.0.2.1\\share\\x.md'])
FAIL: test_an_invalid_byte_near_the_limit_is_not_taken_for_a_split_character
```

Why expected: `main` passed the network path to `os.stat`/`os.path.isdir` (the guard fired: "stat received a network path", "isdir received a network path"), and the committed `read_text` accepted `\xff` in the last bytes of a cut file as a split character.

The full command `python -B gate/run_tests.py instruction-files` did not finish on the committed script: `test_a_chain_that_reaches_a_network_path_through_a_link_is_not_followed` (and the network tests after it) stalled for minutes, and the run was stopped. Cause: the committed walk used `os.walk`, whose `DirEntry.is_dir()` follows links, so a file link to a UNC path was looked up through the network. The guard could not catch this, since the network path is reached inside the OS call, not passed as an argument. This is the Critical finding of the review.

## GREEN

Full suite (`.runs/task-cycles/instruction-files-part/reports/check_3_fix1_green_tests.txt`), run with `python -B gate/run_tests.py instruction-files`:

```text
Ran 53 tests in 91.491s
OK (skipped=1)
instruction-files 0
```

The skip is the Windows FIFO test. The `NetworkPaths` class alone: `Ran 6 tests in 83.077s, OK` (`check_3_fix1_class_trace.txt`).

Script on the-way (`python -B instruction-files/check_instructions.py .`): unchanged from Task 3, `0 error, 1 warn, 3 info`, exit 0. Refusals, run through PowerShell so the arguments reach Python unchanged:

```text
Error: --file is a network path: \\192.0.2.1\share\x.md        exit 2
Error: ROOT is a network path: \\192.0.2.1\share               exit 2
```

Git Bash rewrote a `\\` argument to a single backslash, so the same check run from Bash showed the older "cannot be read" message. The unit tests pass the path as a Python string and are not affected.

## What changed

- `instruction_files`: rewritten over `os.scandir` with `follow_symlinks=False`, `is_junction()` and `is_symlink()`. Directory links and junctions are reported as `walk` "a link to a directory, not followed" and not entered. Nested repositories are detected with `os.path.lexists`, so a `.git` link still counts. A directory that cannot be listed is reported as before. Non-instruction file links are never touched.
- New `leads_out(path, root, hops)`: follows a link chain with `os.readlink`, at most `LINK_HOPS = 8`. Each link target is normalised and checked before anything else is done with it; a network path, a path outside the root, a junction on the way, or a chain longer than the limit counts as "leads out". Only the parts of the path inside the root are checked with `os.path.islink`, one prefix at a time, so no target is ever followed. A file leading out is reported as the existing `read` INFO "a link out of the repository, not read".
- New `directory_link(entry, root)`: on Windows the link's own `st_file_attributes` says whether it is a directory; otherwise `entry.is_dir()` is called only when `leads_out` is False.
- `network_shaped(path)` with `local_form(path)`: `/` becomes `\`, and the local-drive extended prefix (`\\?\C:\`, `\??\C:\`) is removed, since `os.readlink` returns that form for absolute targets. `\\?\UNC\`, `\\.\` and `\??\UNC\` stay network paths.
- `main`: a network-shaped ROOT or `--file` is a usage error (exit 2) before any file-system call. ROOT is refused too, although the ruling named only `--file`: `os.path.isdir` on a network ROOT would reach the network, which §4.6 forbids.
- `read_text`: a decode error counts as a split character only when its reason is "unexpected end of data" and it lies in the last three bytes of a cut file. An `\xff` there stays "not UTF-8 text".
- Test file: literal U+FEFF and U+202E are now `\N{ZERO WIDTH NO-BREAK SPACE}` and `\N{RIGHT-TO-LEFT OVERRIDE}` escapes (the Minor item).

## Covering tests

- Network link (`AGENTS.md` and `notes.txt` to `\\192.0.2.1\share\x.md`), no call receiving a network path, exit 0: `test_a_link_to_a_network_path_is_never_looked_up`.
- Chain reaching a network path through an in-repository link: `test_a_chain_that_reaches_a_network_path_through_a_link_is_not_followed`.
- Nested repository whose `.git` is a network link: `test_a_nested_repository_whose_git_is_a_link_is_skipped_without_a_lookup`.
- Two-link chain leaving the repository: `test_a_chain_of_two_links_that_leaves_the_repository_is_not_read`.
- Chain longer than `LINK_HOPS`: `test_a_chain_longer_than_the_hop_limit_is_not_read`.
- Chain ending inside the repository is still read: `test_a_chain_that_ends_inside_the_repository_is_read`.
- Network path as ROOT or `--file`: `test_a_network_path_given_as_root_or_file_exits_with_2_without_a_lookup`.
- `\xff` in the last bytes of a file over 1 MiB: `test_an_invalid_byte_near_the_limit_is_not_taken_for_a_split_character`.
- Existing tests kept: `test_a_directory_link_or_junction_is_not_followed`, `test_a_file_link_out_of_the_repository_is_neither_read_nor_listed`, `test_a_broken_link_is_reported`, `test_a_file_given_with_file_is_read_through_its_link`.

## Concerns

- Test time: each UNC link the tests create takes about 12 to 20 seconds on this machine (the OS resolves the target), so the `NetworkPaths` class takes about 80 seconds and the whole suite about 90 seconds. Some runs took much longer; the suite has no timeout.
- Not verified on POSIX. On a non-Windows system a directory symlink outside the root is not recognised as a directory (its target is not followed), so `test_a_directory_link_or_junction_is_not_followed` would see a `read`-less, `walk`-less result for the outside link `linked`. Windows, where the tests were run, reports it through its junction.
- The guard in the network tests wraps `os` and `open` calls only; calls the OS makes inside `DirEntry` methods are not wrapped. The walk avoids those calls on network-shaped targets by design, and the tests check the outcome instead.

---

# Task 3 fix round 2 report: platform split, iterative walk, offline tests

Ruling: `task-3-fix-2.md`. Files: `instruction-files/check_instructions.py`, `instruction-files/test_check_instructions.py` only.

## RED (tests first, against c06b237's script)

`python -B gate/run_tests.py instruction-files`: `Ran 58 tests in 2.491s`, `FAILED (errors=1, skipped=4)`.

- ERROR `DeepTree.test_a_tree_deeper_than_the_recursion_limit_does_not_stop_the_run`: `RecursionError` in `visit` (one call per directory level), as the review found. Only this test fails on Windows.
- The offline network tests and the POSIX tests do not fail on c06b237 here: the Windows code path of c06b237 is correct (the new network tests pass at once, now in well under a second, where they took ~90 s); the POSIX tests (`LinkChains` dot-dot, absolute link, every directory link) are skipped on Windows and could not be run red. They are unchecked until a POSIX run.

## GREEN

`python -B gate/run_tests.py instruction-files`: `Ran 58 tests in 3.305s`, `OK (skipped=4)` (wall time 3.5 s; skips: FIFO and the 3 POSIX tests, each with its reason). Script on the-way: `0 error, 1 warn, 3 info`, exit 0.

## What changed

- `WINDOWS = os.name == "nt"` constant. `network_shaped` is false off Windows (a share is a mounted directory there), so the ROOT/`--file` refusal and the UNC logic are Windows-only.
- `leads_out`: off Windows, `not inside(os.path.realpath(path), os.path.realpath(root))`, no `local_form`, no text `normpath` (fixes finding 1 and the `dirlink/../x` case). Windows keeps the `os.readlink` chain.
- `directory_link`: off Windows, `entry.is_dir()`; every directory link or junction is reported "a link to a directory, not followed", wherever it points (finding 4). Windows unchanged.
- `instruction_files`: explicit stack of (directory, entry iterator), same order and findings as the recursive walk (finding 2).
- Tests: network tests (class `NetworkPaths`, Windows only) now link to a local file with a marker and patch `os.readlink` via `pretend_target` to return the network path for that link; no link to a network path is created (finding 3). The `guard_network_paths` guard is kept. New `DeepTree` test (depth = recursion limit + 100, built by `mkdir`/`chdir` one level at a time, skip with reason if it cannot be built). New class `LinkChains` holds the chain tests (two-hop out, ends inside; hop-limit test is Windows only) and three POSIX-only tests: `..` after a directory link, absolute link out, every directory link reported.

## Concerns

- POSIX branch is not run here (unchecked, as the ruling records).
- Off Windows a chain longer than `LINK_HOPS` is not cut; `realpath` decides (a loop makes `read_text` report "cannot be read").

---

# Task 3 fix round 3 report: tests that catch a following walk

Ruling: `task-3-fix-3.md`. Files: `instruction-files/check_instructions.py` (one docstring), `instruction-files/test_check_instructions.py`.

## RED (planted regression, never committed)

Temporarily replaced `directory_link(entry, root)` in the walk's classification with `entry.is_dir()` (a walk that follows a link to classify it), then ran `python -B gate/run_tests.py instruction-files`:

```text
FAIL: test_a_chain_that_reaches_a_network_path_through_a_link_is_not_followed
FAIL: test_a_link_to_a_network_path_is_never_looked_up
Ran 59 tests in 0.850s
FAILED (failures=2, skipped=5)
```

The plant was reverted (script restored from a copy; `directory_link(entry, root)` is back in place).

## GREEN

`python -B gate/run_tests.py instruction-files`: `Ran 59 tests in 0.948s`, `OK (skipped=5)` (1.3 s wall). Script on the-way: `0 error, 1 warn, 3 info`.

## What changed

1. New helper `make_bait_link`: the link is made while its local target does not exist (so it is a file link), then a directory is created at the target. The network tests (link, chain, nested `.git`) use it; they assert no `walk` finding / "a link to a directory" output, so a walk that follows a link to classify it fails offline.
2. `DeepTree`: recursion limit lowered to 200 (restored by `addCleanup`), 300 levels, so the deepest path stays far below 1,024 characters.
3. New POSIX-only `test_a_link_loop_is_reported_as_unreadable_and_the_run_goes_on` (self-link `AGENTS.md`; expects a `read` WARN "cannot be read: ..." and the run going on). Skipped on Windows; unchecked.
4. `directory_link` docstring: following a link off Windows "reaches only what the system has mounted".

## Concerns

- The POSIX tests (now 4) are unrun here.

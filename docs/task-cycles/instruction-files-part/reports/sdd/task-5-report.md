# Task 5 report

Status: DONE.

## RED
Tests added: brief's 2 RootLayout, 2 Skills, 8 PointedFiles, plus 2 (Windows) PointedFiles tests: a pointed network path (plain and `/` form; INFO "network path, not checked", nothing looked up, guarded by `guard_network_paths`) and a pointed file that is a link whose `os.readlink` reports a network target (`pretend_target`, bait link). `WINDOWS_ONLY` moved up beside `NETWORK` so classes before `NetworkPaths` can use it.
Result: `Ran 85 tests`, `FAILED (failures=5)` - the same 5 the brief names. The count is 85, not 69, because Tasks 3-4 and their fixes added tests to the base; the 5 failures match because only the new behaviours fail.

## GREEN
`Ran 85 tests in 1.7s`, `OK (skipped=5)` (skips are link/POSIX-only tests that need privileges or another OS; both new Windows tests and the link test ran and passed).

## Reconciliation
- Docstring, `POINTED_SUFFIXES`, `check_layout` (root layout for every CLAUDE.md beside an AGENTS.md; `CLAUDE.local.md` stays root-only; skill twin in `.agents/skills`) and the `check` call to `pointed_files` applied as in the brief; `check` otherwise untouched, so it keeps `agents_beside`, link/unreadable findings and the ROOT network refusal (that is in `main`).
- `pointed_files` differs from the brief (fix D under the Task 3 rule): no `realpath`/`exists`/`stat`/`open` on a network-shaped path. Order: `is_network(token)` skipped; candidate = `normpath(join(root, expanduser(token)))`; skipped if `network_shaped(candidate)` or `leads_out(candidate, root)` (link chains by `os.readlink` only on Windows) or it is the root; skip-dir and nested-`.git` checks on the lexical relative path; only then `realpath` (for deduplication against `known`) and `stat` (regular file). Returns (real path, path from root).
- A pointed network token is not followed; `check_file` of the pointing file already gives the INFO line.

## Runs
- the-way: `WARN dead-path AGENTS.md:20 `_zadania\` does not exist`; INFO size AGENTS.md 21/187, CLAUDE.md 1/1, agent-instructions/README.md 49 lines, 471 words; `0 error, 1 warn, 3 info`, exit 0. Differs from the brief only in README.md word count (471 vs 475): the file changed during the cycle. (The brief said global user file changed too; not part of this run.)
- loop2: `0 error, 0 warn, 2 info`, no skill-dir line, exit 0.
- Test log: `.runs/task-cycles/instruction-files-part/reports/check_5_tests_instruction_files.txt`.

## Files changed
`instruction-files/check_instructions.py`, `instruction-files/test_check_instructions.py`.

## Concerns
- A nested CLAUDE.md beside an AGENTS.md now gets the root-layout warning too (R18/A20, as intended).
- `leads_out` on POSIX uses `realpath` on the vetted candidate; network paths cannot occur there by the `is_network` rule.

## Fix round 1
RED on 0683617 (7 new tests, 92 total): 5 failed + 1 error. NUL: ERROR (ValueError); `.git` link spy; link into a skipped directory; link into a nested repository; token naming a network link (Windows); token through a directory link. The test "token naming nothing is still a dead path" passed already (guard against over-reach).
Fix: `excluded()` uses `os.path.lexists` for `.git` and is applied to the path as written and to the real path relative to the real root (finding 3); tokens holding NUL are dropped before a path is built and `ValueError` is caught beside `OSError` around `stat` (2); new `names_something` replaces `os.path.exists` in `resolve`: on Windows a component walk with `lstat` that stops at the first link/junction/reparse point (the token counts as existing, nothing looked up through it), elsewhere `lexists` (4).
GREEN: 92 tests, OK (skipped=5). the-way: 0 error, 1 warn, 3 info; loop2: 0 error, 0 warn, 2 info.
Note: a dangling link now counts as existing for a token (by the ruling).

## Fix round 2
RED on 5fe6ed1 (3 new tests, 95 total): all 3 failed - every spelling of a path through a link to a network path (`via/x.md`, `via\x.md`, absolute with `/`; spies on lstat, stat, exists), a repository reached through a directory link above its root, a `--file` reached through such a link.
Fix: `names_something(path, base)` normalises with `normpath` first. On Windows a relative path below its base is walked from the base (`walk_exists`, `lstat` per part, a link/junction/reparse point ends the walk as existing); an absolute path, or one climbing above the base, is walked from its root following links with `os.readlink` only (hop limit; network-shaped target, unreadable link or limit ends it as existing). POSIX: `lexists` of the normalised path. `resolve` passes the base it joined onto.
GREEN: 95 tests, OK (skipped=5). the-way: 0 error, 1 warn, 3 info; loop2: 0 error, 0 warn, 2 info.

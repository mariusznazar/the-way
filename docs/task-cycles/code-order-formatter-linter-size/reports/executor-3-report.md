# Executor-3 report — slice 3, the formatter's test, rule and documents

**Status:** `done with concerns`

**Concern in one line:** `agent-instructions/test_script_invariants.py` was outside the slice's Change list, but its gate test failed on the new `.git-blame-ignore-revs` file, so I added that one name to its `NAMES` list (see Reaches).

## Commits (branch `task/code-order-formatter-linter-size`, worktree root)

| Commit | Subject | Files |
|---|---|---|
| `5e8fa379` | Add the formatter's test of invariant formatter-layout and the blame-ignore file | `agent-instructions/test_linter_invariant.py` +82 −4; `agent-instructions/test_script_invariants.py` +1; `.git-blame-ignore-revs` +2 (new) |
| `037f6c93` | Document the formatter in the coding guidelines, the README and the part map | `README.md` +22 −3; `guidelines/coding.md` +11 −1; `installation/README.md` +6 −2; `foundations/part_map.md` +2 −1 |

Each commit was made by path. The branch's base for this slice is `015ce05c` (slice 2).

## Checks

Each command was run from the worktree root. Exit codes are as observed.

| Check | Command | Exit |
|---|---|---|
| Agent-instructions gate, final tree | `python -B gate/run_tests.py agent-instructions` | 0 (`Ran 52 tests`, `OK (expected failures=2)`) |
| New formatter tests by name, unbroken code | `cd agent-instructions && python -B -m unittest -v test_linter_invariant` | 0 (both `Formatter` tests `ok`; `Linter.test_no_file_of_a_part_breaks_a_blocking_rule` stays `expected failure`) |
| Layout break, run 1 (failing) | `python -B gate/run_tests.py agent-instructions` with `printf 'BROKEN_LAYOUT = [1,2]\n' >> gate/run_tests.py` | 1 — `FAIL: test_every_python_file_of_the_parts_stands_as_the_formatter_leaves_it`; the message names `gate\run_tests.py:222`, `1 file would be reformatted` |
| Layout break, restore | `cp` back from a copy, `git diff --quiet -- gate/run_tests.py` | 0 (file clean) |
| Skip-comment break, run 2 (failing) | same gate command with `printf '# fmt: skip\n' >> gate/run_tests.py` | 1 — `FAIL: test_no_python_file_of_the_parts_holds_a_comment_that_switches_the_formatter_off` |
| Skip-comment break, restore | as above | 0 (file clean) |
| Formatter check, changed `.py` files | `<ruff> format --check --config ruff.toml --no-cache agent-instructions/test_linter_invariant.py` and `…/test_script_invariants.py` | 0, 0 |
| Ruff check, changed `.py` files | `<ruff> check --config ruff.toml --ignore-noqa` on the same two files | 0, 0 |
| Hash names slice 2 | `git log -1 --format='%H %s' 015ce05c2a7209af7db05873775f561acdae408f` | 0 — `015ce05c… Reformat the Python files of the named parts with ruff format and nothing else` |
| Foundation check | `python -B elements/common/foundation_check.py --skip-test-citations` | 0 (`0 errors`); the first run before staging the blame file gave exit 1 (`/.git-blame-ignore-revs ... matches no file git tracks`), and it passed once the file was staged |

`<ruff>` is `the Ruff of the quality environment of the main checkout`, version 0.17.1.

Not run, by design: the full gate (`python -B gate/run_tests.py` with no directory), which the handoff reserves for the orchestrator or CI.

Pre-change state: all 79 tracked `.py` files in the ten parts were already formatter-clean at `015ce05c` (`ruff format --check` gave `79 files already formatted`, exit 0).

## The two breaks (WAY-08)

The formatter test was added to code that already has the behaviour, so each break was applied to `gate/run_tests.py` for a moment and the file was restored from a copy afterwards.

1. Layout break: `BROKEN_LAYOUT = [1,2]` appended. The formatter test failed with `unformatted: File would be reformatted --> gate\run_tests.py:222:20`, `1 != 0`. Its run is kept at `.runs/task-cycles/code-order-formatter-linter-size/reports/executor-3-break-layout-failing-run.txt`.
2. Comment break: `# fmt: skip` appended. The comment test failed and named the switch in its message. Ruff's check would have passed this file (it honours the skip), so only the comment test catches it. Its run is kept at `.runs/task-cycles/code-order-formatter-linter-size/reports/executor-3-break-skip-failing-run.txt`.

Both files were restored, and `git status` was clean for them before each commit.

## What the slice changed

- **`agent-instructions/test_linter_invariant.py`:** a new class `Formatter` with two tests, both citing `invariant: formatter-layout`.
  - The first runs the pinned formatter in check mode (`format --check --config ruff.toml --no-cache`) over the tracked `.py` files of `PARTS`, passed as file arguments so no Markdown file enters, and asserts exit 0. A missing Ruff or a Ruff that cannot run fails the test.
  - The second reads each such file's comments with `tokenize`, and fails on any comment matching `\bfmt:\s*(?:off|on|skip)\b`. Strings, including the test's own, are not comments and do not count.
  - The Ruff lookup moved into a shared helper `installed_ruff()` used by both `run_ruff` and the formatter run. The linter's behaviour and its missing-Ruff message are unchanged.
  - The module docstring now covers the formatter.
- **`guidelines/coding.md`:** `### Formatter` now reads Decision WAY-382 · WAY-381, Invariant `formatter-layout`, Good, Bad, and a paragraph. The paragraph names no command, per WAY-16.
- **`README.md`, "Installing the linter":** says the same Ruff formats the code at width 100 and that a test checks it; that only `.py` files are formatted; how to format a file with the installed Ruff (Windows and Linux/macOS commands, run from the root); and names `.git-blame-ignore-revs` with `git blame --ignore-revs-file`.
- **`installation/README.md`:** the `TrackedFilesTest` block is re-laid out by the formatter at width 100, extracted and dedented, formatted with `ruff format --config ruff.toml`, and re-indented back into the list item. Own-work check: `ast.dump` of the block before and after is identical, so only the layout changed; the surrounding text is unchanged.
- **`.git-blame-ignore-revs`** (new, root): a comment line, then `015ce05c2a7209af7db05873775f561acdae408f`.
- **`foundations/part_map.md`:** the `repository` part's *Files* lists `/.git-blame-ignore-revs` first.

## Own-work check (WAY-164)

- **Requirement most likely missed:** that the formatter test fails on the two break kinds it names, and not only on a clean tree.
  **Check:** the two breaks above, each run through the gate on the directory that holds the test.
  **Showed:** each break failed the matching test, with the expected message. Both runs are kept as files.
- **Requirement:** the new test does not count its own text. **Check:** the module passed on the final tree, and the test file contains no comment with `fmt:`; the module's `fmt:` words live in a docstring and a string, which `tokenize` does not return as comments.
- **Requirement:** the installation example still means the same code. **Check:** the `ast.dump` comparison above.

## Choices made

- **Two commits, not one:** the test and its blame-ignore file together; the documents together. Rejected: one commit. Cost if wrong: none that I can see; the split only groups by what each commit does.
- **Comment regex is a search within the comment text, not anchored at its start:** this makes the check stricter, so a comment that mentions `fmt: skip` in prose would fail the test. Rejected: anchoring at the comment's start, which would let `# note: fmt: skip` pass. No such comment exists in the tracked tree now.
- **Invariant citation in each of the two test methods:** rejected: one citation at class level. Cost: none; the citation check looks for the line anywhere in the file.
- **The `Good` and `Bad` lines of `### Formatter`:** written by me in the form of the Linter rule. Please check the wording against the template at review.
- **Refactor of the Ruff lookup into `installed_ruff()`:** rejected: a second copy of the lookup in the new class. Cost: the linter's code path changed (not its behaviour), so it is in the diff for review.

## Reaches beyond the handoff

- **`agent-instructions/test_script_invariants.py`** (not in the Change list): the test `test_every_file_git_tracks_is_a_python_file_or_of_a_kind_that_is_no_script` failed on the new `.git-blame-ignore-revs` file. Its own failure message says a file that is no script gets its kind added to `NAMES` with a reason. I added `".git-blame-ignore-revs",  # the commits \`git blame\` passes over, one hash to a line` (commit `5e8fa379`). Alternatives: add the file to this slice's Change list and let the executor make the line (what I did), or put it under a different list. Please confirm the change is wanted.
- **`README.md`, the paragraph about the tests and the `ruff.toml` settings** (around line 106: "the settings of the linter"): now also holds the formatter's settings. I did not change it, as it is outside my named section. Observed only.

## Unread material

- `foundations/decisions.md:10579-10628` (WAY-379, F5): not read; I read only the WAY-379 *Verification* quoted in the cycle's `task.md` (its settlements section).
- Everything else the handoff names was read whole or in the cited ranges: the `task.md` passages, WAY-205, WAY-16, WAY-08, WAY-03, WAY-381, WAY-382, F4 (`formatter-layout`), `ruff-blocking-rules`, `test-method-citation`, `repository-file-location`, the part map's `repository` and `agent-instructions` parts, the glossary's `standing check`, the template's `Required form`, `What each section carries` and `The tools of the standing checks`, `guidelines/testing.md`, and `ruff.toml`.

## Searches not found or unclear

- None that changed the work. The `.git-blame-ignore-revs` path was not yet tracked when the foundation check first ran; the fix was to stage it before the check, as described above.

## Working copies

- `.runs/executor-3/` held the test-run outputs, the `run_tests.py` backup, the block extraction script and its intermediate files. Its needed outputs were kept beside this report as the two `executor-3-break-*-failing-run.txt` files. The directory itself was removed (`rm -rf` of that one path, then checked absent); it is no git worktree, so no `git worktree remove` or `prune` applied. No other copy was made.

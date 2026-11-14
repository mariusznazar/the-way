# Report - executor of slice 2 (the state the branch left, and the listed items)

## Status

`done`

## Commits

- `269fecc` Read the commit the branch left in the foundation check (range `6440ca9..269fecc`)

## Files changed

- `elements/common/foundation_check.py` (+78 -4 lines, docstring included)
- `elements/common/test_foundation_check.py` (+130 -4)
- `elements/common/rules.md` (+2)

Totals from `git diff --stat HEAD~1`: 214 insertions, 4 deletions.

## What was made

- `fork_point(root)`: takes the first of `refs/remotes/origin/HEAD`, `refs/heads/main`, `refs/heads/master` that resolves
  to a commit (`git rev-parse --verify --quiet <ref>^{commit}`) and returns `git merge-base HEAD <that commit>`, or `None`
  where no branch resolves or there is no merge base.
- `at_commit(root, commit, path)`: the lines of a file at a commit through `git show`, or `None` where the commit lacks the
  file or git gives it as no UTF-8 text. It decodes the bytes itself (see choices).
- `Foundation.read_base()` sets `self.base` and `self.base_files` (for `foundations/decisions.md` and
  `foundations/invariants.md`). Slices 3 and 4 use these and the two functions.
- `Foundation.list_unknown_base()` writes the listed lines, only where `self.numbers` (the decisions of the working tree's
  log) is not empty: one line naming `foundations/decisions.md` for an unknown base, else one line for each of the two
  files the base lacks, naming that file.
- `Report.note(path, line, message)` makes `<path>: listed: <message>` (or `path:line:`); `run` writes the errors, the listed
  lines, then the count line, which counts errors only. No listed message holds `N error`.
- The docstring states the listed lines and the base. `elements/common/rules.md` has the one bullet under `{fork-point}`.
- No new argument, switch or exit code; a failure to read the base is never exit 2.

## Checks

| Check | Command | Exit |
|---|---|---|
| Red run of the new tests, before the code | `python -B elements/common/test_foundation_check.py -v -k unknown_base -k listed_line -k empty_log -k no_main_branch -k base_on_ -k remote_head -k base_lacking -k base_holding -k good_product_passes` | 1 (13 ran, 10 failed) |
| Green run of the same tests, after the code | the same command (without `-v`) | 0 (13 ran), after two fixes below |
| Slice check | `python -B gate/run_tests.py elements/common` | 0 (171 tests) |
| Slice check | `python -B gate/run_tests.py elements/part-map` | 0 (39 tests) |
| Slice check | `python -B gate/run_tests.py installation` | 0 (56 tests; includes `test_empty_foundations_have_valid_form`) |
| Slice check | `python -B elements/common/foundation_check.py` on this repository | 0 (`0 errors`, no listed line: the repository has a base) |
| Gate (`python -B gate/run_tests.py` with no directory) | not run, the orchestrator's alone | - |

Red run: each of the ten failing tests fails at its assertion on the report: the expected `listed:` line is missing
(`['0 errors'] != ['foundations/decisions.md: listed: ...', '0 errors']`). Failing: `test_no_commit_and_a_log_with_a_decision_lists_the_unknown_base`,
`test_listed_line_stands_after_the_errors_and_before_the_count`, `test_no_commit_and_an_empty_log_writes_no_such_line` (its positive half),
`test_commits_on_no_main_branch_leave_the_base_unknown`, `test_base_on_main`, `test_remote_head_naming_another_branch_is_preferred_over_main`,
`test_base_lacking_the_decisions_is_unknown_for_them`, `test_base_lacking_the_invariants_is_unknown_for_them`,
`test_base_lacking_both_files_writes_a_line_for_each`, `test_base_holding_a_file_git_cannot_read_as_text_is_no_exit_2`.

Tests that passed before the code only by what the old script already did (named as such):

- `test_base_lacking_the_files_and_an_empty_log_writes_no_line`: asserts no `listed:` line, which the old script never wrote.
  It guards the rule that an empty log writes no line.
- `test_base_on_master_where_there_is_no_main` passed in the red run; I then gave it a positive first step (unknown base, then
  `git branch master`), as `test_base_on_main` has, so it now fails before the code. The red run listed above is of the earlier form
  of this one test; I did not re-run the red run after that edit.
- `test_good_product_passes`: a control that was in the red run's pattern; it passed before and after.
- `test_remote_head_naming_a_branch_that_does_not_exist_leaves_main` was added after the red run; not seen failing (before the code it expects
  `0 errors` alone and the old script writes just that, so it would pass; it guards the dangling remote HEAD).

Two fixes between the red and the green run, both in my work: (1) the first form of `at_commit` used the script's `git` helper
with `text=True`; a non-UTF-8 file at the base made `subprocess` print a thread traceback and return `None` output, and the script
then crashed on `.split` (exit 1). The test `test_base_holding_a_file_git_cannot_read_as_text_is_no_exit_2` caught it; `at_commit`
now reads bytes and decodes itself. (2) In the remote-HEAD test, an orphan branch whose commit has the same tree, message,
author and second as the root commit of `main` gets the same hash, so it was `main`; the test now changes `notes.txt` first.

## Own-work check (WAY-164)

- Requirement most likely not met: "a failure to read the base is never exit code 2" and "a base that lacks a file is never read as an empty
  file / nothing is a crash". Check: `test_base_holding_a_file_git_cannot_read_as_text_is_no_exit_2` (a base file of bytes that are no UTF-8)
  and the two tests of a base lacking one file, one lacking both. First run: failed in the way fix (1) names (exit 1, traceback). After
  the fix: passed (exit 0 of `python -B gate/run_tests.py elements/common`).
- Second requirement at risk: the existing tests, the installation test and the-way's own foundation test pass unchanged. Check: the
  three slice checks above (exit 0 each); no existing test was edited, only `Product.__init__` writes bytes where a test gives bytes, and
  `Product` gained `on_branch`, `write`, `commit`.
- A manual check beyond the tests: a remote HEAD that names a branch that does not exist gives `main`; added as a test.

## Choices (with the way rejected and the cost if wrong)

- First existing branch decides: if `refs/remotes/origin/HEAD` resolves but shares no history with HEAD, the base is unknown; the script
  does not go on to `main`. Rejected: falling through to `main` and `master` when the merge base fails. D1 says "no such branch or no
  merge base exists" -> unknown, and the order is of branches, not of merge bases. Cost if wrong: a product whose remote HEAD is a stale
  branch gets the one listed line instead of a base from `main`; the gate keeps its old strength and says so.
- The unknown-base line names `foundations/decisions.md`; the line for a missing file names the missing file. Message for a file the base
  lacks says "holds no readable <file>", so one message covers a missing file and a file that is no UTF-8 text.
- `at_commit` starts `git show` with `subprocess.run` directly (bytes) and not through the `git` helper; the invariant
  `script-subprocesses` allows git. Rejected: making the `git` helper tolerant of decode errors, which changes how every existing git call fails.
- `git show` output has `\r\n` made `\n`, as `read` does for the working tree through universal newlines.
- No move-out of code was needed (the product's rule of size is not in this slice's *Read*; the file grew by 82 lines).

## Reaches beyond the dispatch

none

## Unread material

none: WAY-60, WAY-65, WAY-38, WAY-344 (whole entries, as shown in the section's notes ranges), WAY-321 (read whole), the spec ranges 27-38, 42-58 and 151-153,
the task range 94-98, the invariants `script-imports`, `script-subprocesses` and `cross-part-imports`, the part-map entries `elements-common` and
`foundation-check-command`, and `installation/test_install.py:665-700` were read. I did not read `elements/part-map/test_cross_part_imports.py`
(I ran it as part of `elements/part-map`, which passed); the script keeps all the names it imports (no name removed or renamed).

## Searches not found or unclear

- The slice names "the installation test of an empty foundation" by file and line (`installation/test_install.py:665-700`): found at that range.
- Whether the line for a base that lacks a file stands under the file's own path or under `foundations/decisions.md`: D1 says "naming the file"
  and gives `foundations/decisions.md` for the unknown base only; I used the missing file as the path. Unclear in the spec, settled by my choice above.
- Wall time: the runs of `gate/run_tests.py installation` took 825 s in one pipeline; nothing failed.

## Problems observed

- A background run of the test files by the harness made progress only while other tool calls ran; the red and green runs were repeated in the foreground.
  Not a problem of the code.

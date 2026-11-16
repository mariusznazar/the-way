# Author fix 2 report — the first CI run of the Windows check

**Status:** done

**Commit** (not pushed): `c645221`, on top of `33426d5`. Four test files changed, no code of a script, no CI file, no decision.

## Findings, one by one

**F-1 — 25 tests of `task-cycle/test_remove_merged_worktrees.py`: the test was wrong; fixed.** The fixture took its root from `tempfile.TemporaryDirectory`, which on the runner is given by a short name (`RUNNER~1`), and then built the paths it passes to the script from it. Git and the script (`git rev-parse --show-toplevel`, `git worktree list`) print the long name (`runneradmin`). The tests then compared the printed path with the root by `os.path.relpath`, which between the two spellings of one directory climbs five levels and goes down again: that is the `../../../../../runneradmin/...` of the log and the `KeyError: 'wt/merged'`. The script is right: it prints the directory as git names it, and `holds`/`same` compare by `os.path.samefile`. The fix: `Fixture.root = Path(os.path.realpath(...))`, so that every expected path is below the root in the spelling the system resolves it to. No assertion changed or weakened.

**F-2 — 5 tests of `project-level`: the test was wrong; fixed.** `plan_state.py` prints `repository: ` followed by `Path(args.product_repository).resolve()`, so the long spelling; the two tests built their expected string from the temporary directory as given (short). The script is right (it resolves what it is given, as it should). The fix: in `test_plan_state.py` (`Command.setUp`) and `test_plan_state_invariant.py` (`PlanStateEvidence.setUp`) the root is `Path(...).resolve()`, the same call the script makes. No assertion changed.

**F-3 — `test_a_bar_in_a_name_is_escaped_so_that_the_row_keeps_its_cells`: the subject cannot exist on Windows; skipped there.** `@unittest.skipIf(os.name == "nt", "a bar cannot stand in a file name on Windows")` with a comment that names the cause and the evidence (the first run of `tests-windows` on the request), as `guidelines/testing.md` "Changing an existing test" asks, and `import os` added. The check of the escape stays on Linux, where the name can exist. Cost: the work machine's Windows also skips it, though its git accepted the path; the Linux check carries it.

## What I reproduced of the runner's short-name spelling, and what stayed unchecked

- Reproduced: on the work machine the 8.3 names exist, so a directory with a long name (`a_long_directory_name`, under the ignored `.runs/` of the worktree) has a short spelling (its short path comes from `GetShortPathNameW`; the script that prints it is kept as `reports/author-fix-2-shorttmp.py`). With `TMP` and `TEMP` set to that short path I ran the tests before the fix: `test_remove_merged_worktrees` and `test_change_file_sizes` gave 28 failures, 26 of them the same names as in the CI log, and `project-level` gave exactly the 5 failures of the log (`test_plan_state` three, `test_plan_state_invariant` two). After the fix, with the same `TMP`: `task-cycle` tests of the two files 62 pass and 2 fail, `project-level` (`test_plan_state`, `test_plan_state_invariant`) 71 tests OK. The two that still failed there (`test_a_directory_that_is_no_repository_exits_two_with_an_error` and `test_a_directory_that_holds_no_repository_ends_with_exit_two`) are an effect of my reproduction: its temporary directory lay inside the repository of the worktree, so the "directory that is no repository" was inside one; they passed in the run with the default temporary directory (below) and in the CI log.
- Not reproduced, so unchecked: the bar test's refusal by git on the runner (the work machine's git accepts the path, so the skip rests on the CI log's `exit status 128` and the orchestrator's reading); the runner's own spelling, which I only imitated; that no other test of the runner's 1601 depends on the spelling (the nine passing directories passed in the log, and the next CI run on the request is the check). The three groups were the only failures of the log.

## Checks (command, exit code)

| Check | Exit code |
|---|---|
| `python -B gate/run_tests.py task-cycle` (534 tests, 2 skipped: the bar test and the Windows signal test) | 0 |
| `python -B gate/run_tests.py project-level` (279 tests) | 0 |
| The same directory runs before one wording of a comment: a first `task-cycle` run exited 1 on `test_tracked_files_private_paths` (a comment of mine named a drive path, `<the runner's user directory>`, which the check of private paths lists); I removed the path from the comment and ran again, exit 0 | 1, then 0 |
| Reproduction with `TMP`/`TEMP` at a short name, before the fix | failures as above (not a gate run) |

The full gate was not run.

## Own-work check (WAY-164)

Requirement most likely not met: the tests pass on the runner, where the temporary directory has a short name. Check: the short-name reproduction above, run before and after the fix on the same files; before: the failures of the log (26 of 26 names the files hold, and the 5 of `project-level`), after: none but the two of my reproduction's location. It does not show a pass on the runner itself.

## Choices (with the way rejected and its cost if wrong)

1. Resolve the root in the tests (`realpath` / `resolve`), not change the scripts to print the spelling they were given. Rejected: making the scripts keep the given spelling — git prints long names, so the script would have to reconstruct a short one, and WAY-392's rule (test behaviour, not the spelling of a path) says the test is the one to take both sides to one form. Cost if wrong: none for the scripts.
2. `os.path.realpath` in one file and `Path.resolve()` in the others: each matches what its script does (the cleanup script reads git's paths; the plan-state script calls `.resolve()`). Cost if wrong: a spelling that differs on another system; the next run shows.
3. The bar test skipped by `os.name == "nt"`, not by a try of staging the path. Rejected: a capability check — more code in a test; the ruling asks for the repository's way of skipping POSIX tests. Cost if wrong: coverage of the bar's escape on a Windows git that accepts the path.

## Unread material

- The whole log `.runs/ci-logs/windows-run-1.log`: read the lines of the failing tests and their tracebacks (about 110 lines), not the passing output; the path of the runner in it is not copied here.
- `guidelines/coding-repository-changer.md`: not read; `remove_merged_worktrees.py` was not changed. `guidelines/testing.md` and `guidelines/coding.md`: read earlier in this cycle, not again.
- The test files were read in the parts that build the fixture and the failing tests, not the whole of each.

## Searches not found or unclear

- None unclear. I did not search for other tests that build an expected path from the temporary directory; the CI log lists every failure on the runner, and no other test failed there.

## Working copies

`.runs/author-fix-2/` held the long-named directory used as the temporary directory of the reproduction, the logs and the script that prints a short name; the script was copied to `reports/author-fix-2-shorttmp.py` and the directory removed. Nothing remains.

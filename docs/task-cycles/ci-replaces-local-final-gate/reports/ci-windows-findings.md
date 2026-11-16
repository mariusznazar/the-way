# Findings of the first CI run of the Windows check — the failures the fix is given

Source: the run 43809475737 of the check `tests-windows` on the head `33426d58864cdfa78630d5da2bf4a21540f7e9a7` of the request (the check `tests` on Linux passed in 1 m 11 s). The Windows run took 9 m 41 s and ended `1601 tests in 11 directories; failed: project-level (exit code 1), task-cycle (exit code 1)`; the other nine directories passed, `installation` (62 tests) and `instruction-files` (105 tests) among them. The log of the failed job stands at `.runs/ci-logs/windows-run-1.log` of the worktree (it holds absolute paths of the runner; read it, never copy it into a report).

All these tests passed on the Windows machine of the work (the orchestrator's full gate on the same code, exit 0, 1601 tests), and they fail on every run on the runner, so they are no flaky tests and the exception of WAY-261 does not apply: the red result is a failed gate, fixed in this request. They show where the machine of GitHub differs from the machine of the work. The reading below is the orchestrator's from the log; the cause is the author's to establish.

## Important

### F-1. 25 tests of `task-cycle/test_remove_merged_worktrees.py` fail on the runner

- `ApplyTest` (`KeyError: 'wt/merged'`, `'wt/late'`, `'main'` and an `AssertionError: Lists differ: ['main'] != ['../../../../../runneradmin/AppData/Local/Temp/<dir>/main']`) and `ClassificationTest` (`AssertionError: 'wt/fresh' not found in {'../../../../../runneradmin/AppData/Local/Temp/<dir>/main': ...}`): the paths of the script's output come out as relative paths that climb five levels and go down through `runneradmin`, where the tests expect `main`, `wt/merged` and the like under the temporary directory.
- Reading: the runner's temporary directory is reached by a short name (`<the runner's user directory>`) in one place and by the long name (`runneradmin`) in another, so a relative path between the two forms of one directory goes up and down instead of staying below; the repository itself stands on the drive `D:` and the temporary directory on `C:`.
- The failing tests of `ApplyTest` named in the log: `test_a_change_in_a_submodule_that_the_configuration_hides_keeps_the_directory`, `test_a_listed_path_that_is_a_junction_is_kept`, `test_a_listed_path_that_is_a_link_is_kept`, `test_a_nested_checkout_with_uncommitted_work_keeps_its_task_directory`, `test_the_directory_the_script_runs_in_is_not_removed`, `test_the_main_checkout_stays_where_it_stands_on_a_merged_branch`, `test_the_merge_pushed_by_another_clone_is_seen_after_the_fetch_only`, `test_the_target_branch_comes_from_the_remote_head_or_from_the_option`, `test_apply_removes_a_nested_base_copy_with_its_task_directory`; the others are in the log (count: 31 names of `ERROR:`/`FAIL:` lines in all).

### F-2. 5 tests of `project-level` fail on the runner for the same short and long names

- `test_plan_state.Command`: `test_ansi_stdout_preserves_non_ascii_paths_and_completion_evidence`, `test_crafted_non_ascii_repository_paths_are_data`, `test_worktree_trace_is_exact_and_only_from_git_inventory`; `test_plan_state_invariant.PlanStateEvidence`: `test_git_listed_worktree_proves_start_without_completion` and one more of the log. Each expects a path containing `RUNNER~1` and gets the output with `runneradmin` (`AssertionError: 'repository: <the runner's user directory>\Local\Temp\plan state ...' not found in 'repository: <the runner's user directory>'`).
- Reading: the test builds its expected string from the temporary directory as the system names it, and the script under test prints the path as git or the file system returns it (the long name). Whether the code or the test is wrong is for the author to settle: a script that prints a path in another spelling than it was given is no defect when both name one directory.

### F-3. `task-cycle/test_change_file_sizes.py::test_a_bar_in_a_name_is_escaped_so_that_the_row_keeps_its_cells` fails on the runner

- `subprocess.CalledProcessError: Command '['git', ..., 'update-index', '--add', '--cacheinfo', '100644,<sha>,a|b.txt']' returned non-zero exit status 128.`
- Reading: a `|` cannot stand in a file name on Windows, and git on the runner refuses the path (the Windows machine of the work accepted it).

## Rulings of the orchestrator that bind the fix

1. Fix the tests where the test is wrong (the expected value or the temporary directory taken in one spelling, the other compared), and the code only where the code is wrong, and say which in the report for each group. Keep what the tests check on POSIX; do not weaken an assertion to make it pass.
2. A test whose subject cannot exist on Windows (a `|` in a file name) is skipped on Windows with the reason, the way the repository skips POSIX-only tests (WAY-393's levels and `guidelines/testing.md` say how).
3. Nobody can run the runner. Reproduce the short-name spelling on the machine of the work if you can (a temporary directory reached by its 8.3 name, e.g. via `cmd /c for %I in ("<dir>") do @echo %~sI`) and say in the report what you reproduced and what stayed unchecked; the next CI run on the request is the check.
4. Do not change the CI file or the decisions for this; if the cause needs it, return `questions`.
5. The directories you change, `task-cycle` and `project-level`, are run with `python -B gate/run_tests.py <directory>`; the full gate is the orchestrator's alone.

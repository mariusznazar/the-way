PASS c6452215e40a32da2a9b65d79412e9fb2ec4e4b6

# Review of fix 2: the first CI run's Windows failures

- Range: `33426d58864cdfa78630d5da2bf4a21540f7e9a7..c6452215e40a32da2a9b65d79412e9fb2ec4e4b6`, one commit, `c645221`. It changes four test files and nothing else: no script, no CI file, no decision. `git rev-parse HEAD` gives the head named.
- Bounds: `reports/ci-windows-findings.md` (F-1 to F-3, with the orchestrator's rulings) and the fix diff (`task-cycle/review/fix.md`).
- Counts: no new Critical or Important finding. F-1, F-2 and F-3 are fixed as far as can be checked without the runner. 2 new Minor notes.

## The findings, one by one

The CI log has 31 lines `ERROR:` or `FAIL:`: 25 in `test_remove_merged_worktrees` (16 in `ClassificationTest`, 9 in `ApplyTest`), 3 in `test_plan_state.Command`, 2 in `test_plan_state_invariant.PlanStateEvidence`, and 1 in `test_change_file_sizes`. Every one lies in the three groups the fix answers.

### F-1: fixed. The test was wrong, not the script

- Where the failures came from:
  - The fixture's helper `relative` (`task-cycle/test_remove_merged_worktrees.py:147-148`) turns each path the script prints into a key with `os.path.relpath(path, self.root)`.
  - The fixture took `self.root` from `tempfile.TemporaryDirectory` as given, which on the runner is the short 8.3 spelling. Git and the script print the long spelling.
  - The two spellings make `relpath` climb and come down again, which gives the `../../../../../runneradmin/...` keys and the `KeyError`s of the log.
- Why the script is right: it compares directories with `os.path.samefile`, in `same` and `holds` (`task-cycle/remove_merged_worktrees.py:175-191`), so the spelling does not matter to its judgement.
- The fix: `self.root = Path(os.path.realpath(self.holder.name))`. Every expected path is now built from the long spelling that git prints. Every assertion is unchanged.

### F-2: fixed. The test was wrong, not the script

- `project-level/plan_state.py:496,502` resolves the repository (`Path(args.product_repository).resolve()`) and prints the result. The two `setUp`s built their expected string from the temporary directory as given.
- The fix: they now take `Path(...).resolve()`, the same call the script makes. No assertion changed.

### F-3: fixed, as ruling 2 gives

- `@unittest.skipIf(os.name == "nt", "a bar cannot stand in a file name on Windows")`, with a comment that names the cause and the evidence, the first run of `tests-windows`. That is what `guidelines/testing.md`, "Changing an existing test", asks of a skip.
- The check of the escape stays on Linux, where the CI check `tests` runs it.
- The reason the skip gives is narrower than the cause; see N-1.

### No assertion weakened

The diff touches only the root of each fixture and adds one skip; every assertion is unchanged. Resolving the root changes no expected value of the code under test. It only puts the side the test builds and the side the script prints into one spelling, which `guidelines/testing.md`, "Behaviour, not implementation", supports: the spelling of a path is no part of the required behaviour.

### Did `realpath` and `resolve()` match each script?

Yes. The cleanup script prints git's paths, which git gives in the long spelling, and the test takes `os.path.realpath`. The plan-state script calls `.resolve()`, and the test takes the same call. On Windows both turn an 8.3 name into the long one; I checked that on this machine (check 3). On Linux they change nothing for a temporary directory that has no links, so the coverage on POSIX stays as it was.

## New Minor notes

- **N-1** (within the task). `task-cycle/test_change_file_sizes.py:161-164`: the skip's reason, "a bar cannot stand in a file name on Windows", is narrower than the cause.
  - The test makes no file. `stage_entry` (`:140-145`) only puts an entry into git's index ("whatever the file system allows"). What refused the path on the runner is git's own check of path names (`exit status 128`), and the work machine's git accepted the same path.
  - A path with a bar can still reach a repository that the-way reads on Windows, through a commit made on Linux.
  - The escaping is plain string handling and the Linux check covers it, so nothing is lost today. A more exact reason would name git's refusal on Windows.
- **N-2** (within the task). With both roots resolved, no test now hands the scripts a short-spelled path, so their handling of short names (`samefile` in the cleanup script, `.resolve()` in the plan-state script) has no test on Windows. Before this fix the runner exercised it only by accident, and Linux never did. A test that passes a short-spelled directory on purpose would keep it. This is broader coverage, not a fault of the fix.

## Declined to judge

none

## Checks run

1. `git diff 33426d5..c645221`: read whole.
2. The `ERROR:`/`FAIL:` lines of `.runs/ci-logs/windows-run-1.log`, counted by test file: 31, all in the three groups of the findings file. I read the log only for these lines and copy none of the runner's paths here.
3. A script of mine in `.runs/review-fix-2/` made a directory `a_long_directory_name`, took its 8.3 name with `GetShortPathNameW`, and compared it with `Path(short).resolve()` and `os.path.realpath(short)` (`python -B -I short.py a_long_directory_name`), exit 0. The short name differs and holds `~`, and both calls give back the long path.
4. In a worktree of the head: `python -B gate/run_tests.py task-cycle`, exit 0 (534 tests, 2 skipped: the bar test and the Windows signal test).
5. In a worktree of the head: `python -B gate/run_tests.py project-level`, exit 0 (279 tests).
- Not run:
  - the runner itself: nobody can run it, and the next CI run on the request is the check;
  - a run of the two test files with `TMP` set to a short path: the author made that reproduction and reports the 5 failures of `project-level` and 26 of the task-cycle files before the fix, and none after save two caused by its location, and I did not repeat it;
  - the full gate: the orchestrator's alone.

## Reaches beyond the dispatch

- `task-cycle/remove_merged_worktrees.py:170-191, 505-525`: `same`, `holds` and the places the script keeps, to judge whether the script or the test was wrong.
- `project-level/plan_state.py:496,502`: what the script prints.
- `task-cycle/test_change_file_sizes.py:140-148`: `stage_entry`, for N-1.
- `task-cycle/test_remove_merged_worktrees.py:130-170`: the fixture's `run`, `relative` and `decisions`.

## Working copies

- `.runs/review-fix-2/head` (a worktree of `c645221`): removed with `git worktree remove --force`, then `git worktree prune`.
- `.runs/review-fix-2/`, which held the test logs, `short.py` and the directory `a_long_directory_name`: removed.
- `git worktree list` shows nothing under `.runs/review-fix-2/`. Nothing remains.

## Unread material

- `guidelines/testing.md` and `guidelines/coding.md`: read whole earlier in this cycle's review and not re-read. Their rules on changing a test and on where an expected value comes from were checked against the diff.
- `.runs/ci-logs/windows-run-1.log`: only the `ERROR:`/`FAIL:` lines were read, not the whole log.
- The four changed test files: read in the diff and the passages named above, not whole.
- `reports/author-fix-2-shorttmp.py`: not read, since its effect was checked with my own script.

## Searches not found or unclear

- Why the work machine's git accepts a path with `|` while the runner's refuses it: unclear. It may be a setting of git on Windows, but I did not check this further. It does not change the judgement of the fix.

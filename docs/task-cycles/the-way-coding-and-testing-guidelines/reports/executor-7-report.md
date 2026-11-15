# Report — executor of slice 7 (the tests of the gate wait for events, not for constant pauses)

**Status:** done with concerns

**Commits:** `8ef214d` on branch `task/the-way-coding-and-testing-guidelines` (base `0905337`).

**Files changed:** `gate/test_run_tests.py`, 8 insertions and 6 deletions. No script changed.

**Check result:** `python -B gate/test_run_tests.py` did not exit 0 three times in a row: 2 of 9 full-file runs passed, 7 failed on a pre-existing flake in `DirectoriesAtOnce` (`test_by_default_every_directory_runs_at_the_same_time`, `test_a_number_of_jobs_limits_the_directories_that_run_at_once`); ruff and the foundation check passed.

**Report path:** `.runs/task-cycles/the-way-coding-and-testing-guidelines/reports/executor-7-report.md`

## What the slice changed

1. **Test of the order in which directories end** (`test_each_report_stands_whole_under_its_own_line_in_the_order_directories_end`): removed `pause=2.0`. The module of `a` still waits for the line `end b` in the log, with the helper's limit of 120 seconds (the existing event, no new event added). The comment now names the wait and its limit.
2. **Test of `--slowest`** (`test_the_option_names_the_slowest_tests_with_their_time`): the regex was `^0\.\d{3}s`, which needs a time under 1 second, so a slow machine could turn it red. Now the regex is `^\d+\.\d{3}s +test_slow ` and the time must be at least 0.25 seconds. The slow test sleeps 0.3 seconds, so its time is at least that; the bound lies 0.05 seconds lower for clock resolution. There is no upper bound, since a slow machine only adds time.

## Pauses and limits left in the file, and why

- `timed_module` (helper): the 120-second deadline of its wait loop is kept as the limit the slice asks for; the 0.02-second poll interval is kept (it only sets how fast the wait notices the event).
- `timed_module` keeps its `pause` parameter because other tests still use it:
  - interrupt test, `pause=0.3`: not named by cause 4; left as it was.
  - `test_one_job_runs_the_directories_one_after_another`, `pause=0.3`: not named; with `--jobs 1` the order comes from the runner, not the pause.
  - `test_failed_directories_are_named_in_sorted_order_whatever_the_order_they_ended_in`, `pause=1.0`: not named; the test asserts sorted names, not an order, so the pause does not decide it.
- `SLOW_AND_FAST`, `time.sleep(0.3)` in `test_slow`: this is the work being timed, not a wait for ordering; kept, and the bound above checks it.

## Own-work check (section 3)

Requirement: the two named tests must not depend on a constant pause or on machine speed, and must still catch a broken behaviour.

- Mutant 1, runner made to print directories in name order (`for done in list(pending):` in a copy of `run_tests.py`): `python -B -m unittest test_run_tests.DirectoriesAtOnce.test_each_report_stands_whole_under_its_own_line_in_the_order_directories_end` gave exit 1. The unmutated copy gave exit 0.
- Mutant 2, slow test sleeping 0.1 seconds instead of 0.3 (in a copy): `python -B -m unittest test_run_tests.SlowestTests.test_the_option_names_the_slowest_tests_with_their_time` gave exit 1 with `0.101 not greater than or equal to 0.25`. The unmutated copy gave exit 0.
- Weakest point: the report-order test no longer orders the runner's printing by a pause. The runner prints a directory's report only after its process exits, and the test's `a` only waits for the log line `end b`, which `b` writes before it exits. So a narrow race remains: if `a` exits before the runner has printed `b`, the order flips. In the full-file runs below, `test_each_report...` did not appear in any failure list I read (the first three runs and run 1 of the batch; I did not read the failure lists of batch runs 2 and 4, which I had deleted before I could check them again), but the race is not closed by construction. Check made: the mutant above and the full-file runs.

## Checks run (commands and exit codes)

| Check | Command | Exit | Note |
|---|---|---|---|
| Baseline before edits | `python -B gate/test_run_tests.py` (worktree) | 0 | 34 tests, 13.4 s |
| Edited file, run 1 | `python -B gate/test_run_tests.py` | 1 | fails `test_a_number_of_jobs...`, 131 s |
| Edited file, runs 2 and 3 | same | 1, 1 | fail `test_by_default...`, 131 s each |
| Edited file, run 4 | same | 0 | 34 tests, 11.3 s |
| Edited file, batch of 5 | same | 1, 1, 1, 1, 0 | run 3 had 2 failures, 251 s |
| Base file, 3 runs (copy at `0905337`) | `python -B test_run_tests.py` from a copy of its `gate/` | 0, 1, 1 | run 2 failed `test_by_default...`, run 3 failed `test_a_number_of_jobs...` |
| Focused, `DirectoriesAtOnce`, base copy | `python -B -m unittest test_run_tests.DirectoriesAtOnce` | 0 | 11 tests, 8.0 s |
| Focused, `DirectoriesAtOnce`, edited copy | same | 0 | 11 tests, 6.0 s |
| Mutant 1 and restored | see above | 1 and 0 | |
| Mutant 2 and restored | see above | 1 and 0 | |
| Linter | `<main checkout>/.runs/quality-venv/Scripts/ruff.exe check --config ruff.toml --no-cache --ignore-noqa gate/test_run_tests.py` | 0 | "All checks passed!" |
| Foundation check | `python -B elements/common/foundation_check.py --skip-test-citations` | 0 | "0 errors" |

The gate's full suite (`python -B gate/run_tests.py` without a directory) was not run, per WAY-160.

The test file was not changed to add a new invariant test; its own `invariant:` citations are unchanged.

## Concerns and questions

1. **Pre-existing flake in `DirectoriesAtOnce`.** At the base commit, the full file failed in 2 of 3 runs; the failing tests (`test_by_default_every_directory_runs_at_the_same_time`, `test_a_number_of_jobs_limits_the_directories_that_run_at_once`) wait 120 seconds for the other directories' `start` lines and never see them, although the same tests pass when the class runs alone. I did not find the root cause. The slice does not name these tests, so I did not change them.
   - Recommended answer: a separate slice (or a fix) that investigates these two tests under the full-file run, since the slice's own check "exits 0 three times in a row" cannot be met reliably until they stop failing.
   - Cost if left: the gate of the-way is red at random, and this slice's check cannot be satisfied.
   - Caveat: the edited file failed in 7 of 9 runs and the base in 2 of 3. The samples are small, so I cannot say the edit does not change the rate; the edit does not touch the failing tests.
2. **Residual race in the report-order test.** Recommended answer: add an event the helper writes when its process is ending (an `atexit` line such as `exit <name>` written by `timed_module`) and wait for `exit b` in place of `end b` in that one test. Cost: a small change to the helper; the race shrinks but is not closed. The alternative that closes it fully is a driver-side wait that releases `a` after the runner has printed `b`, which is a larger change. I kept the wait on `end b` as the slice asks, and I did not add the event.
3. The slice's check "exits 0 three times in a row" was not met (see concern 1).

## Choices

- Removed the pause instead of replacing it with a new event (the slice names the existing `end b` line); way rejected: the `atexit` event; cost if wrong: see concern 2.
- The `--slowest` lower bound is 0.25 seconds for a 0.3-second sleep; way rejected: exactly 0.3, which can fail on clock resolution; cost if wrong: a spurious red run on a machine whose clock reads a little early.

## Adaptations of section 4

None; the plan matched the code.

## Reaches beyond the handoff

- `gate/run_tests.py`: read whole (the handoff named lines 1-60); needed to see how the runner prints reports.
- `.ai/rules/scripts.md` and `.ai/rules/git.md` (the user's global rules): read because a hook blocked my Bash calls until I read them.
- `task-cycle/change/slice.md`: read (the method's variant names it).

## Unread material

- `ruff.toml`: I printed it but only the tail of the rules list was visible; I did not read its line-length or other settings whole.
- `project-level/technology/reserved_choices.md`: not read; section 5 applies only where the work needs a technology the task does not settle, which did not arise.
- Everything else the handoff names was read whole: the slice section, the task passages at `task.md:41`, `:161-163`, `:253-259`, E12 (WAY-395 at `foundations/decisions.md:10140`), WAY-243 (`:9522`), WAY-232 (`:9019`), the gate part-map lines (`foundations/part_map.md:136-143`), the invariants `script-language`, `script-imports`, `script-subprocesses`, `cross-part-imports`, `test-method-citation` and the plan's *Choices* and "Orchestrator's additions"; `gate/test_run_tests.py` whole.

## Searches not found or unclear

- The source of the flake in `DirectoriesAtOnce`: looked for a mechanism that would stop directories from seeing each other's log lines and found none; the log path is the same in every process and the writes return without error. Unclear.
- `ruff.toml` line-length: not checked; ruff passed on the file, so the long comment line I wrote is accepted by the configuration.

## Working copies

All working copies I made are removed; none remained and none were git worktrees:
- a copy of the base `gate/` (`test_run_tests.py` and `run_tests.py` from `0905337`) under `.runs/executor-7/base-check/`: removed;
- a copy of the edited `gate/` under `.runs/executor-7/edited-check/`: removed;
- mutant copies under `.runs/executor-7/mutant/`: removed;
- run outputs under `.runs/executor-7/`: removed (their results are in the tables above).
The directory `.runs/executor-7/` itself is removed.

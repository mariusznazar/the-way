# Report — executor-9 (slice 9: the worktree test no longer depends on git's background maintenance)

**Status:** done

## Commits

- `0ccdc807` — Turn git's automatic maintenance and garbage collection off in the worktree test
  (branch `task/code-order-formatter-linter-size`, range base `222c5a7b`).

## Files changed

- `task-cycle/test_remove_merged_worktrees.py`: +11 lines, −0 lines.
  - `ENVIRONMENT` gets `GIT_CONFIG_COUNT=2` with `gc.auto=0` and `maintenance.auto=false`, given by
    the git environment settings `GIT_CONFIG_KEY_n` / `GIT_CONFIG_VALUE_n`, and a comment naming the
    cause (the first CI run of pull request #144 on Linux, `FileNotFoundError` on `maintenance.lock`).
  - `ApplyTest.test_a_dry_run_removes_nothing_and_apply_removes_only_what_is_marked` gets a comment
    naming the same cause and pointing at `ENVIRONMENT`.
  - The snapshot `state`, the assertions and the test's logic are unchanged.

## Choices made

- **Two settings, not a removed lock file.** The slice allowed either turning maintenance off through
  the environment or leaving out the lock file from the snapshot (task question carried to the cycle).
  I chose the environment: it covers every git process of the test, the bare `origin.git` included,
  and the git run by the script under test (it merges `os.environ` with its own `ENVIRONMENT`, so it
  inherits the test's settings). Rejected: excluding `maintenance.lock` in `state` — it would hide the
  cause and leave git's other background files in the snapshot. Cost if wrong: git versions older than
  2.31 ignore `GIT_CONFIG_COUNT`; the local git is 2.55, and the CI git version was not checked.
- **Edge of the override.** `ENVIRONMENT` starts from `os.environ`, and `GIT_CONFIG_COUNT=2` replaces
  any count the outer environment sets, so entries beyond the two keys of the outer environment would
  be dropped. The test already overrides `GIT_CONFIG_GLOBAL` and `GIT_CONFIG_NOSYSTEM`, so the test's
  git reads no outside configuration anyway; cost is nil on the current machines.

## Checks

| Check | Command | Exit code | Result |
|---|---|---|---|
| Baseline, before the change: format | `the Ruff of the quality environment of the main checkout format --check --config ruff.toml task-cycle/test_remove_merged_worktrees.py` | 0 | 1 file already formatted |
| Baseline: lint | `ruff.exe check --config ruff.toml --ignore-noqa task-cycle/test_remove_merged_worktrees.py` | 0 | All checks passed |
| Baseline: the whole test file | `python -B -m unittest task-cycle.test_remove_merged_worktrees` | 0 | Ran 46 tests, OK (57.7 s) |
| Once, the test's environment: git reads the settings | `python -B -c` importing `ENVIRONMENT` from the test module and running `git config --get gc.auto` and `git config --get maintenance.auto` with it | 0 and 0 | `gc.auto` = `0`; `maintenance.auto` = `false` |
| Format after the change | `ruff.exe format --check --config ruff.toml task-cycle/test_remove_merged_worktrees.py` | 0 | 1 file already formatted |
| Lint after the change (slice's Check) | `ruff.exe check --config ruff.toml --ignore-noqa task-cycle/test_remove_merged_worktrees.py` | 0 | All checks passed |
| The changed test after the comment edit | `python -B -m unittest task-cycle.test_remove_merged_worktrees.ApplyTest.test_a_dry_run_removes_nothing_and_apply_removes_only_what_is_marked` | 0 | Ran 1 test, OK |
| Focused gate (slice's Check) | `python -B gate/run_tests.py task-cycle` | 0 | Ran 534 tests, OK (skipped=2: two Windows-only skips, unrelated) |

Log of the gate: `.runs/task-cycles/code-order-formatter-linter-size/reports/executor-9-gate-task-cycle.log`.

Not run, by design: the full gate (`python -B gate/run_tests.py` without a directory), per the handoff.

## Own-work check (WAY-164)

- **Requirement:** the dry-run test gives the same verdict every time; its snapshot must not see
  `maintenance.lock` come or go; every git process of the test, the bare `origin.git` included, and
  the script's git inherits the setting; the snapshot and the assertions unchanged.
- **Check:** the one-time environment check above (both settings read as off through `ENVIRONMENT`),
  plus the single test and the directory gate passing. The script's git inheritance was checked by
  reading `task-cycle/remove_merged_worktrees.py` (`env={**os.environ, **ENVIRONMENT}`).
- **What it showed:** the settings are in effect for the test's git processes, and the test passes.
- **Weakest point:** I did not reproduce the flake, so the test passing shows no more than that it
  passes. The claim that the lock file cannot appear while the snapshot is taken rests on git's
  documented behaviour of `gc.auto=0` and `maintenance.auto=false`, not on a run of the failing case.
  No run of the test was repeated many times for the stability claim. A repeated run on Linux in CI
  is the only real evidence; the orchestrator may want it.

## Observed, outside the slice (not changed)

- Lines 592 and 626 of `task-cycle/test_remove_merged_worktrees.py` read `except OSError, NotImplementedError:`
  without parentheses. Python 3.14.3 parses it locally and `ruff check` passes with `target-version = "py314"`,
  but that form is only valid from Python 3.14 (PEP 758); on an older interpreter the whole test module
  fails to load. Evidence: the file as it stands; the local interpreter. Whether CI runs 3.14 was not checked.
  The intended form is probably `except (OSError, NotImplementedError):`. Not changed here: a different slice's decision.

## Reaches beyond the handoff

- `a private rule file of the author` and `.ai/rules/git.md`: read because the
  private hooks blocked the `python -c` check and the commit until the rules were read; the commit
  message is in English and the change is committed by path.
- `task-cycle/change/SKILL.md` and `task-cycle/change/slice.md` of the worktree: read whole, as the
  handoff's method names them.

## Working copies

- No worktree or clone was made. The only file I wrote under `.runs/executor-9/` was the gate log;
  it was moved to `reports/executor-9-gate-task-cycle.log` and the directory `.runs/executor-9/`
  was removed. Nothing remains there.

## Unread material

- The handoff's `plan.md` was not opened; the slice text was taken from the handoff, which copies it.
- `guidelines/coding-*.md` (the kind files) were not read: the changed file is a test, and the
  guideline's table asks for them only for a check, a report, a generator, a changer, a command runner
  or a shared module.
- Everything else the handoff names was read whole: `task-cycle/change/SKILL.md`, `slice.md`,
  `task-cycle/test_remove_merged_worktrees.py`, `guidelines/testing.md`, `guidelines/coding.md`;
  `task.md` lines 30–41, 93–110; `foundations/invariants.md` 476–489 (current range of
  `repository-changer-acts-only-when-told`); `foundations/decisions.md` 9933–9978 (WAY-233);
  `foundations/glossary.md` 209–216 (`git test`).

## Searches not found or unclear

- none

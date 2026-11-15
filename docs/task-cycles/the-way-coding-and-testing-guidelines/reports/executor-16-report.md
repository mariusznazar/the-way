# Report of executor 16 (slice 16, the test of the linter's invariant)

**Status:** done with concerns (one listed check, `foundation_check.py` exits 0, does not hold at this
slice: see Problems).

## Commits and files

- `fc9244f` Test the linter's invariant: the pinned Ruff runs, and no file of a part breaks a blocking rule, marked as an expected failure
- Added `agent-instructions/test_linter_invariant.py`: +76 / -0. No other file changed.

## What the file does

- `main_checkout()` finds the main checkout through `git rev-parse --git-common-dir` run from the root of the
  worktree (relative `.git` in a main checkout, absolute in a worktree; `ROOT / output` handles both).
- `ruff_program()` is `<main checkout>/.runs/quality-venv/Scripts/ruff.exe` (Windows) or `bin/ruff`.
- `run_ruff()` raises an assertion error naming the path and the README section where the program is
  missing; otherwise runs `ruff check --config <ROOT>/ruff.toml --no-cache --output-format concise ...`.
  No version check of its own.
- Test 1 (`test_the_pinned_ruff_runs_and_passes_a_clean_file`, not marked): a clean file in a temporary
  directory, exit code 0 required.
- Test 2 (`test_no_file_of_a_part_breaks_a_blocking_rule`, `@unittest.expectedFailure`, cites
  `# invariant: ruff-blocking-rules`): `--ignore-noqa` over the ten directories, exit code 0 required.
- Imports the standard library only; no file of another part.

## Checks (command, exit code)

| Check | Command | Exit |
|---|---|---|
| Slice check: reports one expected failure | `python -B agent-instructions/test_linter_invariant.py` | 0 (`OK (expected failures=1)`, 2 tests) |
| Focused run of the directory | `python -B gate/run_tests.py agent-instructions` | 0 (32 tests, `OK (expected failures=1)`) |
| Test 2 unmarked, on the base | `python -B agent-instructions/test_linter_invariant.py` with the `@unittest.expectedFailure` line deleted for a moment | 1: `FAILED (failures=1)`, `AssertionError: 1 != 0`, the output holds the 25 places (`Found 25 errors.`), the same 25 as the direct ruff run on the ten directories (FURB188, PERF102, RUF059, UP022, UP037, F541, PIE810, TRY004, PYI034, PLR1704 ...). Marking restored. |
| Test 1 seen failing, environment path made wrong | the same command with `quality-venv` changed to `quality-venv-wrong` in the file for a moment | 1: test 1 fails with `Ruff is not installed at ...\quality-venv-wrong\Scripts\ruff.exe; install it as the README ...`; test 2 shows `x` (expected failure), the run is red. Undone. |
| Test 1 seen failing, version mismatch (extra check of the weakest point) | the same command with `required-version = "==0.17.2"` in `ruff.toml` for a moment | 1: test 1 fails with `Required version ==0.17.2 does not match the running version 0.17.1`, exit 2 of ruff in the message. `ruff.toml` restored (`git status` clean for it). |
| Linter on the new file | `ruff.exe check --config ruff.toml --no-cache --ignore-noqa agent-instructions/test_linter_invariant.py` | 0 (`All checks passed!`) |
| `python -B elements/common/foundation_check.py` | as in *Checks* | 1: one error left, see Problems; the error for `ruff-blocking-rules` (no test cites it) is gone after the commit (it was there while the file was untracked) |

Test 1 shown passing: the passing runs above (before and after the failing runs) run it on the clean file.

## Own-work check (WAY-164)

Requirement most likely not met: "a missing ruff cannot pass as the expected failure and leave the gate
green" (item of the slice's goal). Check: with the environment path wrong, the whole run exits 1
because test 1 fails while test 2 reports `x` (above). Second: that test 1 really reads `ruff.toml` so
that the pinned version is enforced (a version mismatch turns it red; above, exit 1).

Mutations in my head: ruff run without `--ignore-noqa` in test 2 (no test sees it: a file of the ten
parts with a `noqa` comment hiding a break would pass; the test is itself the check of the invariant, and
the flag is read in the file; not protected by another test); a clean file with a break in it (test 1
would fail, seen by the unmarked variant of the same mechanism); `PARTS` missing a directory (not
caught by a test; the list is the ten directories the handoff names).

## Places the linter reports that no slice of this plan cleans

At the base 25 places stay (the report of the unmarked run, concise format):

- agent-instructions/test_instruction_files.py:161:18 FURB188
- elements/common/foundation_check.py:599:30 and :608:30 PERF102
- elements/common/migrate_foundation.py:398:17 and :679:17 RUF059
- elements/common/test_migrate_foundation.py:680:9 RUF059
- gate/test_skills_reach_the_way_sessions.py:62:21 PIE810
- installation/install.py:83:14 UP022, :467:27 PERF102
- installation/test_agent_types_installation.py:24:12, test_coding_guidelines_installation.py:20:12,
  test_installed_guidance.py:15:12, test_lead_installation.py:19:12, test_styleguide_installation.py:25:12,
  test_testing_guidelines_installation.py:20:12 UP022
- instruction-files/check_instructions.py:296:5 FURB188
- process-audit/audit_count.py:1259:19 RUF059, :2293:25, :2506:19, :2580:36 UP037
- process-audit/test_audit_count.py:2388:38 F541
- product-guidelines/test_skill_references.py:209:8 PIE810
- task-cycle/cycle_stages.py:598:13 TRY004
- task-cycle/test_cycle_measures.py:867:17 PYI034
- task-cycle/test_remarks_check.py:365:13 PLR1704

This is the 25 the plan names ("25 at the plan's base after the slices that clean 18 of the 43"); the slices
that clean the 18 are already in the base, so I could not tell which of the 25 a later slice cleans; the
orchestrator has the plan, I list all 25 as seen at the base.

## Problems as observed

- `python -B elements/common/foundation_check.py` exits 1 after my commit: `foundations/invariants.md:442:
  function-and-file-size reads test and no test cites it`. That invariant belongs to no test written up to
  this slice (the entry `function-and-file-size`, E23); I take it that a later slice cites it. Verified:
  the error for `ruff-blocking-rules` cleared after the file was tracked, the one for
  `function-and-file-size` stands. This is a mismatch with the slice's *Checks* ("exits 0"), not caused by
  my change.

## Choices (with the way rejected)

- The two tests share one helper `run_ruff` that raises `AssertionError` where Ruff is not installed;
  test 2 in that case ends as an expected failure but test 1 fails (the separation the slice names).
  Rejected: a skip of test 2 where Ruff is missing: a skipped test is easy to overlook, and the slice wants
  the red from test 1. Cost if wrong: none for the gate.
- `--output-format concise` so the failure message is one line per place. Rejected: the default full
  format (a screen per place). Cost: none.
- `--no-cache` so no `.ruff_cache` is written in the repository or the temporary directory.
- The clean file stands as a module constant; the test writes it to a temporary directory.
- Used `unittest.expectedFailure`, the gate's runner is `unittest`; an unexpected success ends the run red
  (checked reading: `wasSuccessful()` is false on an unexpected success in Python 3.12+ — not run here, as
  no clean tree exists to run on).

## Reach beyond the handoff

- Read `task-cycle/change/slice.md` (named by `SKILL.md` for the slice variant) and `gate/run_tests.py`
  (whole, to confirm the runner and what an expected failure does). Read
  `agent-instructions/test_agent_type_copies.py` lines 1-60 as the model of style of a test of this
  directory. Read `README.md:155-185` and `foundations/part_map.md:155-173` (in the handoff's range).
  Ran `git log --oneline` to confirm the base.

## Working copies

`.runs/executor-16/` held a copy of the test file, a backup of `ruff.toml` and the outputs of the failing
runs. Removed with `rm -rf` before returning (`ls .runs` shows `review-8`, `task-cycles` only). No worktree
made.

## Unread material

- `foundations/decisions.md` WAY-61 (1866-1914), WAY-203, WAY-204, WAY-205: not read (the invariant and
  WAY-380/WAY-381 restate what the slice needs).
- WAY-08 and WAY-51: read whole. WAY-38: read whole. WAY-380 and WAY-381: read whole.
- `foundations/invariants.md`: read whole `script-subprocesses`, `script-imports`, `test-method-citation`,
  `cross-part-imports` (header and sentence in part: the output was truncated and I read the sentence, method
  and *Part* lines), `ruff-blocking-rules`, `function-and-file-size` (the first lines); not read:
  `script-language` beyond its sentence, `repository-file-location`, `ci-checking-commands`,
  `tracked-file-private-paths`, `guidelines-file-place`, `map-reference-target`, `derived-file-content`
  (the slice adds no file at the root or under `guidelines/`).
- `foundations/environment_facts.md`: `ruff-required-version` read whole; `ruff-default-rules` read in part
  (the first lines; the list of 407 rules was not needed).
- `plan.md` (the end, "Orchestrator's additions") and its *Choices*: not read; the handoff carries the slice.
- Task passages: lines 31, 35, 77-97, 197-202, 516-523 read; `README.md:163-177` read (155-185).

## Searches not found or unclear

- The plan's remark that 18 of the 43 places are cleaned by earlier slices: I could not tell from the code
  which of the 25 left a later slice cleans; none of them is cleaned by this slice.

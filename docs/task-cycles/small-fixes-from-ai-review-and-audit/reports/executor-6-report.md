# Report of executor 6 (slice 6)

**Status:** done with concerns (the concerns are two texts outside my *Change* list that still say Q1 is a word; see *Problems*).

## Commits (task branch `task/small-fixes-from-ai-review-and-audit`, base `3b34de03`)

- `0ee90d8e` Give the audit's result an image of each series and Q1 as numbers of cycles
- the second commit (message "Test that a version has no reason of its own for its Q1 and each cycle keeps its reason"; `git log -2` names its hash): one added test in `process-audit/test_process_versions.py`.

The worktree is clean.

## Files changed

- `process-audit/series_summary.py` new, 186 lines (shared module: `median_of`, `median_text`, `money`, `measure_number`, `gate_values(cycles)`, `q1_text`, `plan_sums`, `cost_image`, `count_image`, `mechanism_image`, `gate_image`).
- `process-audit/version_analysis.py` 1056 -> 1001 lines: the moved functions are gone, it imports the new module (not the other way round), `Series` gains `image` and `cycles()`, the four `*_rows` functions set the image, `count_rows` writes Q1 as numbers, `contradiction_of` and `too_large_of` are removed (their callers use `q1_text` and `plan_sums`), the docstring says what is now true.
- `process-audit/audit_report.py`: the new image headers, `series_lines` (heading, reason, image, "By version:", table), the explanatory text (Q1 is no longer `yes`, `no` or `unknown`; it is the numbers), `money` imported from the new module.
- `process-audit/test_process_versions.py`: base class `VersionsCase` (reads the two tables of a series), the old Q1 assertions changed, class `SeriesImages` with 6 new tests.
- `process-audit/test_series_summary.py` new: 32 unit tests.

## Checks (command, exit code)

Failing runs first:
- `python -B -m unittest discover -s process-audit -p "test_series_summary.py"` against an empty stub of the module (the functions return empty values): exit 1, 24 failures and 7 errors, on assertions and on the missing rows of the stub.
- `python -B -m unittest test_process_versions.ProcessVersions` from `process-audit/` of a worktree at the base `3b34de03` (working copy `.runs/executor-6/base`, removed) with the new test file copied in and its helper loosened to read the last table, since the base writes no image: exit 1, 15 failures, each on a Q1 cell (`'yes 0 · no 1 · unknown 0' != 'no'` and the like), plus `'yes 2 · no 0 · unknown 4' != 'yes'` for the crafted items. The same file unloosened fails 44 of 44 tests on the base, because a series there holds one table, not two.

Passing runs on the final tree:
- `python -B -m unittest discover -s process-audit -p "test_series_summary.py"`: exit 0, 32 tests.
- `python -B -m unittest discover -s process-audit -p "test_process_versions.py"`: exit 0, 45 tests.
- `python -B gate/run_tests.py process-audit`: exit 0, 314 tests, before the last added test (the one test was run in `test_process_versions.py` above); the invariant `audit-series-script-paths` is among them.
- `python -B gate/run_tests.py agent-instructions`: exit 0, 53 tests (run after the new files were tracked, and again after the last commit); it holds the linter, the formatter and the size checks.
- Ruff, the pinned one at `the pinned Ruff in the main checkout's ignored directory`, `format` and `check --ignore-noqa` over the five files: clean.

## Own-work check

Requirement most likely unmet: "a version has no Q1 answer of its own: the line of *Unknown values* that gave a reason for a version's Q1 is no longer written, and what each cycle gives as unknown stays with its reason". My first set of tests had no check of it. I added `SeriesImages.test_a_version_has_no_reason_for_its_q1_and_each_cycle_keeps_its_own`: it runs a series with one cycle whose Q1 is unknown, asserts that no row of *Unknown values* starts with `contradiction only after code` and that the cycle's own `Discarded attempt` reason is still there. It passes; against the old `count_rows` it would fail. A second weak point: the expected value I guessed for the crafted-items test (`yes 2 · no 0 · unknown 4`) came from reading the rules, not from the run; the run agreed.

Mutations considered: Q1 as a word taken from the cycles (`test_one_cycle_that_answers_yes_does_not_make_the_group_yes` and the version rows fail); the median of a gate taken over all runs (the failed-run test); the image over the last version only (the split-series test); a lost `%` of the share (the image test reads `12.5%`); the Q2 answer from the sums over all cycles instead of the read ones (the "not read" unit test).

## Choices (with the way rejected and the cost if wrong)

- Image rows for the mechanism measures: always one row per measure, with `0` and `unknown` where no cycle gives a value. Rejected: the single `—` row that a version has. Cost if wrong: a reader who wants the `—` form gets 15 rows of zeros for a series with no measures; the change is local to `mechanism_image`.
- Image of the count of remarks has six columns: Cycles, Q1, Plans read, Slices planned, Slices returned too large, Q2. The sums stand as cells because the plan says "Q2 as the sums ... with the answer"; a version's row still shows only the answer, as before.
- `gate_values` takes the list of cycles (not a `Version`) so that it depends on cycles alone; `version_analysis.gate_rows` calls it with `version.cycles`. Behaviour is the same.
- `too_large_of` became `plan_sums` over a list of cycles, returning a small dataclass; it now also computes the sums when an answer is unknown (they were not computed then before). The answer and the reasons are the same as before.
- `money`/`MONEY` and `median_text` moved too (the image needs them); `audit_report.py` imports `money` from the new module.
- The tests' helper `section` is overridden in a new base class `VersionsCase` inside `test_process_versions.py` (it returns the table of versions, the second table). Rejected: changing `section` in `process-audit/test_audit_count.py`, which is not in my *Change* list.

## Differences between the Goal and the foundation entries

None found: WAY-417 and the sentences of WAY-339 say what the Goal says. WAY-417 puts the Q1 numbers also on "each side of a comparison before and after a fix": that comparison is another slice, not made here.

## Reaches beyond the handoff

- Read `foundations/decisions.md:8995-9038` (WAY-417) and the whole of WAY-339/WAY-350 range as named; no reach beyond them.
- Searched `process-audit/*.py` and the repository for users of the moved names (`median_of`, `gate_values`, `money`, `contradiction_of`, `too_large_of`, `section`) to be sure nothing else broke: only `audit_report.py` and `version_analysis.py` used them.
- `.runs/` of the main checkout holds the Ruff the linter test uses; I ran it directly for format and lint (read only).

## Working copies

- `.runs/executor-6/base` (worktree of the base commit): removed with `git worktree remove --force` and `git worktree prune`.
- `.runs/executor-6/agent-instructions.out`, `process-audit.out`, `versions.out`: logs of the runs above, in an ignored directory, removed before returning (if one remains, it is under `.runs/executor-6/`).

## Unread material

- `.runs/task-cycles/.../task.md` passages: read as the handoff copied them, not opened in the file.
- `foundations/decisions.md:11087-11134` (WAY-385) and `6820-6857` (WAY-365), `foundations/invariants.md`, `foundations/part_map.md`: read the ranges. `guidelines/coding-measuring-report.md`, `coding-shared-module.md`, `coding.md`, `testing.md`: read whole.
- `process-audit/record_reading.py:166-232`, `process-audit/problem_register.py:60-100`: record_reading read; `problem_register.py:60-100` not read (the Register is untouched by my code).
- `process-audit/audit_shared.py`: read the first 60 lines.
- `process-audit/test_audit_count.py:1-355`: read the lines 1-120 and 195-360; I did not read the middle (120-195, the `Repository` class body).
- `process-audit/test_process_versions.py`: read whole, except lines 1-140 which I read as a head only (they are fixtures).

## Searches not found or unclear

- WAY-417 verification names "on each side of a comparison before and after a fix" for Q1 as numbers; that comparison does not exist yet in the code (another slice), so nothing here makes it true. Not unclear for this slice.
- `guidelines/coding-shared-module.md` lists only `relation-model/fingerprint.py` as a file of that kind; I did not add `process-audit/series_summary.py` to its table (the file is not in my *Change* list and the invariant test reads only the exemplar).

## Problems as observed

- Two texts still say Q1 is a word per version and are outside my *Change* list: the docstring of `process-audit/audit_count.py` (lines about 146-148: "Each answer is `yes`, `no` or `unknown`" and Q1's rule "yes where ... no where every ...") and `process-audit/SKILL.md` (lines 223-225: "Each answer is `yes`, `no` or `unknown` inside its series"). They are now untrue for Q1 of a version. The orchestrator should give them to a slice.
- `process-audit/test_audit_count.py`'s helper `AuditCountCase.section` reads all table lines under a series heading, so it is wrong for a series that has an image; only `test_process_versions.py` uses it, and its subclass overrides it. Evidence: grep for `.section(` shows no other user. A later change may remove or correct the base helper.
- A run of `test_process_versions.py` takes about 105 s, of `process-audit` about 325 s; run them in the background.

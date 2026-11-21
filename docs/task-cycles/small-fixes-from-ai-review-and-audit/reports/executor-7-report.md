# Report of executor 7 — slice 7, the audit's comparison before and after a fix, inside each series

**Status:** done with concerns (the concerns are observations in *Problems as observed*, none blocks the slice)

## Commits

- `ca55d4e8` Compare the cycles before and after each fixed issue's fix inside each series of the audit (on base `29a1c6ae`); the worktree is clean.

## Files changed (added / removed lines, `git diff --stat HEAD~1`)

| File | Lines |
|---|---|
| `process-audit/series_summary.py` | +151 / -few (the four comparison functions, `Comparison`, `falls_between`, `side_rows`, `measure_values`) |
| `process-audit/version_analysis.py` | +72 (the field `Versions.fixes`, `Series.comparison`, `fix_sides`, `compare_series`, the wiring in `process_versions` and `measure_versions`, the grouping of the new unknown values in `unknown_field`) |
| `process-audit/audit_report.py` | +74 (the four comparison headers, the table in `series_lines`, two paragraphs of prose) |
| `process-audit/test_series_summary.py` | +207 (unit tests of the four comparisons) |
| `process-audit/test_process_versions.py` | +372 (the class `SeriesComparisons`, 12 tests; the helper `tables` now reads two or three tables, `section` reads the last, new `comparison`) |

Total: 854 added, 22 removed. `process-audit/audit_count.py`, the signature of `measure_versions` and the files of the trust boundary are not changed.

## What was made

- `Versions.fixes`: the register's issues whose *Fate* is `fixed`, as (issue, fix commit), in the order of the register, filled by `process_versions` from `register.issues` (the register already refuses a fixed issue whose *Fix* is no commit, so such an issue never reaches the field). `measure_versions(versions, ancestry)` reads it; its signature is unchanged.
- `fix_sides` (`process-audit/version_analysis.py`): per series, per fix, per version the answer of `Ancestry.holds(version.commit, fix)`: `True` puts the version's cycles after, `False` before, `None` on neither side with the reason in *Unknown values*. A fix that `Ancestry.commit` does not resolve gives no sides and one value for the issue (not one per version or series).
- `compare_series` calls the comparison of the series' kind once for each fixed issue and appends its rows to `Series.comparison` and its unknown answers to the unknown values.
- `series_summary.py`: `cost_comparison`, `count_comparison`, `mechanism_comparison`, `gate_comparison`, pure functions of (issue, fix, cycles before, cycles after). A comparison stands where cycles stand on both sides; the gate times where runs compared stand on both sides of the total. Each side reuses the image of its kind (`cost_image`, `count_image`, the medians of `measure_values` and `gate_values`). Q3 / the fall: `yes` where the median after is lower than before, `no` where not (equal is `no`), `unknown` with the reason where a median is not known; it stands in the row of the side after, the side before has `—`; the count of remarks has no verdict column.
- `audit_report.py`: under the image of a series that has comparisons, the table "Before and after a fix, inside the series, ..." (columns: Issue, Fix, Side, then the columns of the image, then Q3 or Falls); the table of the versions stays after it. Two paragraphs of prose added to *Process versions* and *Measure versions*.
- New unknown values (grouped by `unknown_field` as `... after the fix of an issue`): `comparison before and after the fix of issue ...` (fix not in the checkout; or, with `, version <commit>`, a version whose answer is unknown), `cost falls after the fix of issue ...`, `Measure falls after the fix of issue ...: <measure>`, `Gate time falls after the fix of issue ...: <measure>`.

## Checks (command and exit code)

| Check | Command | Exit |
|---|---|---|
| New unit tests fail on the base | with the three source files at `HEAD` and stubs of the new functions (see below): `python -B -m unittest test_series_summary.CostComparison test_series_summary.CountComparison test_series_summary.MechanismComparison test_series_summary.GateComparison` (from `process-audit/`) | 1 (3 failures, 8 errors; the 4 negative cases pass on the stub, see *Problems*) |
| New integration tests fail on the base | same stubs: `python -B -m unittest test_process_versions.SeriesComparisons` | 1 (8 failures, 2 errors; the 2 negative cases pass on the base) |
| Focused tests pass | `python -B -m unittest discover -s process-audit -p "test_series_summary.py"` | 0 (47 tests) |
| | `python -B -m unittest discover -s process-audit -p "test_process_versions.py"` (run after the commit; 57 tests) | 0 |
| The gate of the part | `python -B gate/run_tests.py process-audit` | 0 (342 tests, 367 s) |
| Linter, formatter, size | `python -B gate/run_tests.py agent-instructions` (run after the commit) | 0 (53 tests) |

The failing run on the base: the base (`HEAD` versions of `series_summary.py`, `version_analysis.py`, `audit_report.py`) plus a stub of `Comparison`, the four comparison functions (returning an empty `Comparison`) and `fix_sides` (returning two empty lists), so that the tests reach their assertions instead of stopping on an import. My three files were copied to `.runs/executor-7/mine/` before, and copied back after; the diff of the commit is the tree I tested.

## Own-work check

- Requirement most likely not met: "whether a version holds the fix is the answer of `Ancestry.holds` for the version's full commit and the fix, never a date" (task point 5, WAY-339), and that an unknown answer puts the version on neither side.
- Checks: `SeriesComparisons.test_a_version_that_is_later_by_date_but_lacks_the_fix_lands_before_it` (a version on a branch beside the fix, dated after the version that holds it: before = median 3.000000 from 4 and 2 dollars, a date reading would give 4.000000 before); `test_a_version_whose_answer_is_unknown_stands_on_neither_side` (`fix_sides` over three versions with the answers no, yes, unknown, with a double of the ancestry because a shallow clone with the fix in it is costly to build; the double only answers `commit` and `holds`); `test_a_fix_that_the_checkout_lacks_...` on a real git history with a fix hash `1 * 40`.
- Showed: all pass; the date-versus-commit one fails on the base as it must. Mutations I made in my head and the test that catches each: `<` to `<=` in `falls_between` (the equal cases of `CostComparison` and `MechanismComparison`, gate/a "no"), `holds` true to before (every integration test), the check of the runs compared of the total dropped (`GateComparison.test_a_side_with_no_run_compared_of_the_total_...`), the register order lost (`test_two_issues_with_the_same_fix_...`), the one-side rule dropped (`test_a_series_with_cycles_on_one_side_...` and the split-count test).

## Where the Goal and the foundation entries differ

No difference found. WAY-339's sentences, WAY-417 and the Goal agree on: the sides by the version, the group of the series, Q3 and the fall only in the comparison, the count of remarks without a verdict, the gate times over the runs WAY-350 compares. The Goal says "for the gate times, runs compared on both sides, of the total"; I read it, as written, as the total of the runs compared on each side (not each directory), and then every measure is shown for that issue.

## Choices (with the way rejected and its cost if wrong)

- Where the sides are worked out: `fix_sides` in `version_analysis.py` (it needs `Ancestry`), the rows in `series_summary.py` (pure, takes two lists of cycles). Rejected: giving `Ancestry` to `series_summary.py` — that module reads no git, by its description. Cost if wrong: a later move of one function.
- `Series.comparison` as a new field of the series and `Versions.fixes` as the carrier of the register's fixed issues, as the Goal says; `count_rows` and `cost_rows` keep their signatures.
- A unit of the verdict cell: `—` on the side before and the verdict on the side after (rejected: the verdict on both rows, which repeats it, and an own column with a blank). Cost if wrong: the column holds a dash in half of the rows.
- The fix the checkout lacks is one value of the issue (`comparison before and after the fix of issue ...`) and not one per version; it is added once and the lists are deduplicated by `render` (identical tuples). The reason is the same as `fixed_issue_row`'s for the same fix, but under another field, so the two do not merge.
- `unknown_field` got a second pattern (`FIX_ISSUE`) so that the names of the issues leave the field and the values of one kind make one pair, as the existing pattern does for `the fix of issue ...`. Rejected: a pair for each issue. Cost if wrong: one more regular expression.
- The helper `VersionsCase.tables` of `test_process_versions.py` now accepts two or three tables, `section` takes the last, `comparison` the middle one. `process-audit/test_audit_count.py` is not changed. Changed existing test code: only this helper, because a series with a comparison has a third table; no expected value of an existing test changed.

## Reaches beyond the handoff

- `.ai/rules/scripts.md` and `.ai/rules/git.md` (the user's own rules, which the harness hook put in front of the first script and commit) — read, no change.
- `guidelines/coding.md`, `coding-measuring-report.md`, `coding-shared-module.md`, `testing.md` (named by the handoff) read whole. `foundations/decisions.md` WAY-339, WAY-350, WAY-330, WAY-416, WAY-365, WAY-417, `foundations/invariants.md` and `part_map.md` ranges named by the handoff read. I did not read `foundations/decisions.md` WAY-385 (the thresholds): I took "no function over 110 lines, no file over 1200" from the handoff's *Checks*; the invariant's test passed.
- I used the linter and formatter of the main checkout (`the pinned Ruff in the main checkout's ignored directory`, version 0.17.1) to format and check my files; the gate's own test does the same.

## Working copies

- `.runs/executor-7/` (the base-check copies `mine/series_summary.py`, `mine/version_analysis.py`, `mine/audit_report.py`, the helper edit scripts and the outputs of the two gate runs): stood under `.runs/executor-7/`; removed with `rm -rf` and its full path. A stray empty file `.runs/executor-7-edit.py`, made by a command that hung on `cat >`, also removed.
- No worktree, clone or screenshot was made.

## Unread material

- `foundations/decisions.md` WAY-385 (the thresholds of the rule of size) — not opened; the handoff gives the numbers, and the size invariant test passed.
- The passages of `task.md` and the entries named by the handoff were read from the handoff's own copy (the passages word for word) and from `foundations/decisions.md`; I did not open `task.md` itself.
- `process-audit/problem_register.py` lines outside 60-100 I read only around `check_issue` and the issue part of the reader (lines 135-160, 300-340), as needed to see that a fixed issue with a *Fix* that is no commit is refused; `process-audit/record_reading.py` I read through its use (`Cycle`, `GateRun`, `gate_values`), not lines 166-232 whole; `process-audit/audit_shared.py` was not read beyond its names (`THE_WAY`, `Git`).
- `process-audit/test_audit_count.py` read to line 360 and the helper blocks near 2320-2385 (`MEASURE_VALUES`, `gate_file`); the rest not.

## Searches not found or unclear

- none

## Problems as observed

1. A mechanism comparison stands wherever cycles stand on both sides, as the Goal and the task say, also where no cycle on either side gives a value of mechanism measures (copies without `mechanism_measures.md`): then it gives 15 pairs of rows with `unknown` and 15 pairs in *Unknown values*. Evidence: `GateComparison`/`MechanismComparison` units with empty `measures`; `test_a_version_that_is_later_by_date_but_lacks_the_fix_lands_before_it` builds such cycles and the result renders. Not changed, since the Goal and the entries say "cycles". If the report grows noisy, a one-line rule "a mechanism comparison stands where a value stands on both sides" would cut it; the orchestrator decides.
2. The number of git calls grows with the number of fixed issues times the number of versions (each pair `(version, fix)` is asked once and cached in `Ancestry.holdings`, shared by the four kinds). On the real register I did not measure it (no run on the real data, which this slice does not require). Guess, not measured: a register of dozens of fixed issues and a hundred versions is thousands of `merge-base --is-ancestor` calls.
3. The negative tests (`a series with cycles on one side only`, `a fixed issue whose fix is not a commit`, the one-side unit cases) pass on the base too, as any test of an absence does; the positive tests of the same code paths are what fail on the base.
4. The tool of this session turned a doubled backslash in a heredoc into a single one in some of my edit scripts, so a few scripted edits failed on a mismatch and I made them with the edit tool or with the line editor; no file was left half-edited (each failing script stopped before writing).

# Slice 6 fix report: the findings of the review

**Status:** done

**Commits** (fix range `0964b52..9209ecb`, branch `task/audit-numbers-mechanism-measures`):
- `9209ecb` Count a row of the wrong number of cells in the run limit of the gate times

**Files changed:** `process-audit/audit_count.py` (+10 / -8), `process-audit/test_audit_count.py` (+9).

**One-line check result:** the new flood test failed before the fix (500 != 600) and passes after; the whole `test_audit_count.py` passes with 164 of 164, exit 0; the private-paths test passes, exit 0.

## Findings

**I1 (blocking): fixed.** The run limit did not count rows of the wrong number of cells. In `read_gate`, the wrong-width branch appended a run and continued before the cap check.

- Fix: the wrong-width test now runs before the branch, so a wrong-width row is a new run too. The cap check runs for it first; when the cap is reached, the loop stops and the "more than 500 runs" reason is written. The width reason is only added for rows still inside the cap.
- Check that shows it: `test_a_flood_of_wrong_width_rows_after_a_valid_header_is_capped_too` (600 rows `| a | b |` after a valid header) asserts 500 rows in *Gate runs* and the cut reason in *Unknown values*.
  - Failing run before the fix: `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k test_a_flood_of_wrong_width` gave `AssertionError: 500 != 600`, exit 1.
  - After the fix: `-k Measures` gives `Ran 16 tests ... OK`, exit 0.
  - Whole file: `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` gave `Ran 164 tests in 221.422s ... OK`, exit 0. Run in the background and waited for before committing.

No other findings were in the file, so none were contested.

## Other checks

- `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` after the commit: `Ran 1 test ... OK`, exit 0.
- `git diff 2292f334d5499f45b68b00c477cd76a2effd7537 HEAD -- process-audit/audit_count.py | grep -c TREE_PATHS`: 0.
- The product's gate was not run.

## Own-work check

- Requirement most likely unmet: a flood of wrong-width rows, the case the reviewer named, still unbounded.
- Check: the flood test above, which failed before the fix and passes after.
- Mutation thought: if the wrong-width branch skipped the cap again, the flood test would fail at 600 rows; if the cap were off by one, the test's exact count of 500 would fail.

## Unread material

- `reports/slice-6-review-report.md`: read only the finding as copied into the findings file; not read whole.
- `task-cycle/change/fix.md`: read whole after the fix (I had not opened it before making the fix; the fix matches its rules: one blocking finding, fixed with its check).
- Everything else in the handoff was read.

## Searches not found or unclear

- none

## Reaches beyond the handoff

- none

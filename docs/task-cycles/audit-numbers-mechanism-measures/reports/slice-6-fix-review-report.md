PASS 9209ecb7cfa22575e44208e7c711df8abe8d04a1

# Review of the fix of slice 6, range `0964b521610f2f7a73d19c6a99f9477e537e8dd9..9209ecb7cfa22575e44208e7c711df8abe8d04a1`

Method: `review-change`, the fix variant (`task-cycle/review/fix.md` read whole). `git rev-parse HEAD` is
`9209ecb7cfa22575e44208e7c711df8abe8d04a1`, the head given. One commit in the range: `9209ecb` "Count a row of the wrong number of
cells in the run limit of the gate times". Counts: 0 blocking, 0 new Minor of the fix (the four Minor findings of the earlier
review are unchanged and not part of this fix), 0 out of scope.

Changed files (`git diff --stat 0964b52..9209ecb`):
- `process-audit/audit_count.py`: +10 / -8 lines
- `process-audit/test_audit_count.py`: +9 lines

## The finding the fix answers

**I1 (the run limit does not hold for rows of the wrong number of cells): fixed.** In `read_gate`
(`process-audit/audit_count.py:1473-1491`) a row of the wrong width is now a new run, so it goes through the same test
`len(runs) >= MAX_RUNS` as a row with a new key; at the limit the loop stops and the reason "holds more than 500 runs" is written. The
width reason is added only for a row still inside the limit, and the row then appends `(None, [])` and sets `last = None` as before, so the
earlier behaviour for rows inside the limit is kept (`test_a_row_of_the_wrong_number_of_cells_is_its_own_unknown_run` still passes).

Evidence, from `read_gate` called on crafted text cut at `MAX_BYTES` (4 MiB) after a valid header, scratch probe
`a scratch script in the session's scratchpad`:

| Input | Runs | Time | Cut reason |
|---|---|---|---|
| 500,000 rows `\| a \| b \|` (the case of the finding; was 419,412 runs) | 500 | 0.15 s | yes |
| 40,000 pairs of a wrong-width row and a right-width row with the same key | 500 | 0.04 s | yes |
| 2,000 distinct right-width runs, each followed by a wrong-width row | 500 | under 0.01 s | yes |
| 3,000 wrong-width rows with distinct cell counts | 500 | 0.06 s | yes; 505 reasons in all, bounded by the limit |
| 80,000 right-width rows of one run | 2 (the second is the row cut by the size limit) | 0.47 s | no; the directories stay at 50 |
| one row of 800,000 cells | 1 | 0.25 s | no |
| 500 wrong-width rows exactly | 500 | under 0.01 s | no (nothing was cut) |
| 501 wrong-width rows | 500 | under 0.01 s | yes |
| 500 right-width runs, then one more row of the 500th run's key | 500, the last holds both directories | under 0.01 s | no |
| 3 wrong-width rows, a blank line, 1,000 more | 3 | under 0.01 s | no (the reading stops at the blank line; the earlier Minor M2 stands) |

The limit holds at the exact boundary (500 read, the 501st cut with the reason), a right-width row that continues the last run is
not counted as a run, and no input made the work more than linear.

## Inspection of the fix diff for what it broke

Nothing new found. The only change in behaviour for rows inside the limit is the order of two statements; `last = None` after a
wrong-width row is kept, so the next right-width row opens a run of its own as before. The new test
`test_a_flood_of_wrong_width_rows_after_a_valid_header_is_capped_too` (`process-audit/test_audit_count.py`, after
`test_runs_beyond_the_limit_are_not_read_and_say_so`) gives 600 rows `| a | b |` and asserts 500 rows in *Gate runs* and the cut reason;
by the probe above it fails if the cap is skipped again (the earlier code gave all 600). The 500-exact boundary is covered by the
neighbouring test of well-formed rows and by my probe, not by a test of wrong-width rows.

## Minor (not blocking)

The earlier review's M1 (exit codes of four or more digits), M2 (rows after a blank line dropped without a reason), M3 (module
docstring) and M4 (git failure on an optional file) are outside the findings file of this fix and remain as written in
`reports/slice-6-review-report.md`; none is made worse by the fix.

## Declined to judge

none

## Checks run

- `git rev-parse HEAD`: `9209ecb7cfa22575e44208e7c711df8abe8d04a1`.
- `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k Measures`: exit 0, 16 tests OK in 13.8 s.
- Scratch probe `probe3.py` (read-only, imports `audit_count` from the worktree): the table above; nothing written in the worktree
  (`git status --short` empty).
- Not run: the whole `test_audit_count.py` (the fix report claims 164 of 164, exit 0; unverified by me), the product's gate, as the
  handoff says, and the private-paths test (the fix touches no tracked path rule; the fix report gives exit 0).

## Reaches beyond the handoff

none

## Unread material

- `reports/slice-6-fix-review-handoff.md`'s own "same selection as the earlier review": not reread; I used my earlier review's reading.
- The foundation entries were not reopened for this review; the fix touches one condition in `read_gate` and a test.

## Searches not found or unclear

none

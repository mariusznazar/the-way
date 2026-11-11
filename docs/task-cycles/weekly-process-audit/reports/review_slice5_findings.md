# Findings of the review of slice 5 (`9cf2633..c2a0169`) — the reviewer's words

Full review: `.runs/task-cycles/weekly-process-audit/reports/review_slice5_report.md`

## Blocking finding

### 1. Important — a refused row of the register is invisible in the figures it belongs to: the cycle shows `0`, an open issue shows `—` ("no problem yet")

Place: `process-audit/audit_count.py` `analyse` (the lines that build `cycle_rows`, `members` and `open_rows`; counts are taken from `register.problems` only, refused rows go to `unknown` only)
and `read_register` (a row refused for its class, weight or issue is dropped from `register.problems`).

What is wrong. Binding choice 1 says a refused row gives "`unknown` for what depends on it, never an abort"; the slice says a problem that cannot be placed "gives `unknown` with its reason". The code lists the refused row in *Unknown values*
and leaves every count it belongs to as if the row did not exist:
- Scratch A: one cycle, one open issue `open-one`, one problem row for that cycle and issue with the weight `Blocker`. The row is refused (listed in *Unknown values*), and the result gives
  *Problems by cycle* `none 0 0 0 0` for the cycle and *Open issues* `open-one 0 0 0 —` — "`—` where the issue has no problem yet", in the table's own wording. The issue has a problem; the days of waiting, which the human weighs, are not "none".
- The executor's own tests pin this: `test_a_class_named_in_two_rows_refuses_both_and_its_problems_with_it` asserts `none 0 0 0 0` for a cycle whose only problem was refused, and `test_crafted_rows...` asserts a count of 1 for a cycle with seven problem rows of which six are refused.
- The same holds for a fixed issue: a refused problem of a fixed issue is in neither "holds" nor "lacks" nor any `unknown` column.
A row refused for a cause that still names its cycle (valid Repository and Record, bad class or weight or issue) is a known cycle with an incomplete count.

Why it matters. WAY-335 asks that the weighing of an issue be the human's, on material the audit gives; slice 6 and the weekly session read these tables. A zero that means "unreadable" and `—` that means "none yet" are figures that look measured, the class of defect the
reviews of slices 3 and 4 failed on ("`unknown`, never zero"). A typo in a user's register (one weight, one class) silently shortens a cycle's count and can shorten an issue's waiting. The listing in *Unknown values* is there, but the tables a reader and the next slice use do not point to it.

Direction (the author's choice): give each cycle row, each fixed issue row and each open or dropped issue row a count of refused rows that belong to it (known by Repository + Record, or by Issue name), and write the cycle's count as `unknown`, or "at least n", where that count is above zero; an open issue whose
rows are refused gets `unknown` days, not `—`. Rows with no usable Record or issue name stay in *Unknown values* only.

Evidence: scratch `scratch6.py` scenario A (`a scratch file outside the repository`), and the two tests named.

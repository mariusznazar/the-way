# Handoff — the review of correction 1, `review-structure-form-class`

## Delegation

You are the reviewer of the whole change, resumed to review a correction the human asked for on the open request, once, as an agent that did not make it.
Read-only. The orchestrator is the one you ask; no human answers during the cycle.

## Where

- Worktree (read-only for you): `the worktree's root`; range of the correction `24cbe61..c04d9cc` (one commit,
  five files: `foundations/decisions.md`, `product-guidelines/coding/settle.md`, `product-guidelines/coding/template.md`, `task-cycle/review/SKILL.md`,
  `task-cycle/review/whole_change.md`). Confirm `git rev-parse HEAD` is `c04d9cc`. The tree before it is the tree you reviewed (`0f35395`).
- The human's remarks, word for word, which take the place of a findings file: `docs/task-cycles/review-structure-form-class/reports/correction-1-remarks.md`.
  Item 1 asks for a fix in this request; item 2 is explicitly not fixed here.
- The correction's report: `docs/task-cycles/review-structure-form-class/reports/correction-1-author-report.md`; its handoff: `reports/correction-1-handoff.md`.
- Report path (write your full report there): `docs/task-cycles/review-structure-form-class/reports/review-correction-1-report.md`; its first line is
  `PASS c04d9cc`, `FAIL c04d9cc` or `questions`.

## Method

Read `task-cycle/review/fix.md` and follow it for "a correction for the human's remarks": each remark as made or not made, and what the correction itself broke or
widened beyond the remark. Judge in particular: that every sentence about this grade (the review skill, the binding sentence of the entry on the structure of
code, `whole_change.md`, the coding template and its question list, and any other place that says "below the threshold" about it) now says the same about a
product with no rule of size; that the entry's *Rejected* names the way not taken with its price; that no other grade or rule changed; that the entry still
reads as a decision of the foundation (WAY-263, WAY-297 grade a mismatch of an entry with the files). Search once for any sentence of the branch the correction
missed. Run, each with command and exit code, `python -B elements/common/foundation_check.py`, `python -B gate/run_tests.py task-cycle`; do not run the whole
gate. Only a new Critical or Important finding fails this review; a Minor finding goes to the request's list.
Your report holds **Unread material** and **Searches not found or unclear** (each `none` where there is nothing). Return the first line, the counts of
blocking, Minor and out-of-scope findings, a one-line check result and the report path.

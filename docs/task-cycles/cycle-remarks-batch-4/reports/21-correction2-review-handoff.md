# Handoff — review of the second correction, cycle `cycle-remarks-batch-4`

You are the reviewer of the whole change, resumed, to review a correction made for the human's
remarks, once. The orchestrator acts on the user's delegation; nothing here is the human's approval.
Read-only.

- Worktree (from its root): `.runs/worktrees/cycle-remarks-batch-4`.
- Method: `task-cycle/review/SKILL.md`, variant **a correction made for the human's remarks**:
  `task-cycle/review/fix.md` (what you read, what bounds the review). The remarks stand in the place
  of a findings file.
- Range: `98e2d86..1c1e8c8` (compute it yourself; confirm `git rev-parse HEAD`). `98e2d86`'s tree
  equals the tree you passed at `10d443f`.
- The human's remarks, binding: `docs/task-cycles/cycle-remarks-batch-4/reports/18-correction2-remarks.md`
  (S1, S2). They answer your finding N-1 of `…\reports\15-correction-review-report.md`. The handoff
  the author got: `…\reports\19-correction2-handoff.md` (where it goes beyond the remarks, judge it
  against the remarks).
- The author's report: `docs/task-cycles/cycle-remarks-batch-4/reports/20-correction2-report.md`
  (claims to verify, not evidence).
- Entries the correction changes, whole: WAY-71, WAY-287; also whole: WAY-17, WAY-160 (unchanged here),
  `elements/common/rules.md`, `elements/decisions/template.md`, `elements/invariants/template.md`,
  `task-cycle/skill/request_template.md` item 15. Beyond that you select as the method gives; name each reach.
- Judge besides your usual criteria: (1) that the script now does what route 1 says in all three fields
  and rejects nothing the rule allows: run `foundation_check.py` on scratch copies with the values of
  your own N-1 (`python-stdlib-modules · TODO`, `python-stdlib-modules · TODO — a second fact, from the
  vendor`, `WAY-38 · TODO — …`, quoted *Based on* sources with ` · ` and `TODO` inside quotation marks,
  `TODO` first then more items), on the-way and read-only on `<the loop2 checkout>`; (2) that every
  place that states the form of the three fields agrees (WAY-71, `rules.md`, the two templates, WAY-287,
  item 15); (3) the author's note that `clock-tick, TODO — x` (a comma before the `TODO` item) is still
  split on the comma and reported as before — judge whether that leaves a trap for the rule as written;
  (4) that the first round's and the first correction's decisions stand.
- The orchestrator runs the full gate; you do not.

## Report

Write it to `docs/task-cycles/cycle-remarks-batch-4/reports/22-correction2-review-report.md`
(first line `PASS <sha>` or `FAIL <sha>`; findings with grade, `file:line` and scope; the checks you ran
with command and exit code, installation tests included if you run them and wait for them to finish
before you return; **Unread material**; **Searches not found or unclear**). Return the first line,
the findings by grade and the report path.

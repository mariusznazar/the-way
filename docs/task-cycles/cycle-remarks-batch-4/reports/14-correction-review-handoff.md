# Handoff — review of the correction, cycle `cycle-remarks-batch-4`

You are the reviewer of the whole change, resumed, to review a correction made for the human's
remarks, once. The orchestrator acts on the user's delegation; nothing here is the human's approval.
Read-only.

- Worktree (from its root): `.runs/worktrees/cycle-remarks-batch-4`.
- Method: `task-cycle/review/SKILL.md`; variant **a correction made for the human's remarks**, so read
  `task-cycle/review/fix.md` whole and follow it (what you read and what bounds the review). The
  remarks stand in the place of a findings file.
- Range: `14b7680750c48e0c173291fec8223dd7c30b0655..10d443f` (compute it yourself; confirm
  `git rev-parse HEAD`). `14b7680`'s tree equals the tree you passed at `5841ed7`.
- The human's remarks, binding: `docs/task-cycles/cycle-remarks-batch-4/reports/11-correction-remarks.md`
  (R1–R3). The handoff the author got: `…\reports\12-correction-handoff.md` (it adds orchestrator
  detail; where it goes beyond the remarks, judge it against the remarks).
- The author's report: `docs/task-cycles/cycle-remarks-batch-4/reports/13-correction-report.md`
  (claims to verify, not evidence).
- Entries the correction writes or changes, whole: WAY-71, WAY-160, WAY-287; also whole, for the
  judgment of consistency: WAY-17, WAY-58, WAY-05, WAY-33, WAY-263; `elements/common/rules.md`,
  `elements/decisions/template.md`, `elements/invariants/template.md`, and the parts of the part map
  `decisions`, `elements-common`, `task-cycle`. Beyond that you select as the method gives; name each
  reach.
- Things to judge besides your usual criteria: (1) that the script now says what the rule says and
  rejects no entry the rule allows — run `foundation_check.py` on the-way and read-only on
  `<the loop2 checkout>`; (2) that each form of `TODO` in WAY-71, `rules.md`, the two templates, WAY-287
  and item 15 of `task-cycle/skill/request_template.md` agrees; (3) the sentence in WAY-71's *Rationale*
  that gives the reason *Relations* and *Origin* take no `TODO` (the remarks gave the rejection, not
  the reason; the reason is the author's: judge whether it is true and necessary); (4) the earlier
  decisions of the first round stand (item 15 covers the whole tree after the change).
- The orchestrator runs the full gate; you do not.

## Report

Write it to `docs/task-cycles/cycle-remarks-batch-4/reports/15-correction-review-report.md`
(first line `PASS <sha>` or `FAIL <sha>`; findings with grade, `file:line` and scope; the checks you
ran with command and exit code; **Unread material**; **Searches not found or unclear**). Return the
first line, the findings by grade and the report path.

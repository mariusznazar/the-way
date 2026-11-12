# Handoff — review of the whole change

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator. You have
no contact with the human: questions go to the orchestrator in your report (status `questions`).
You did not make the change. Your grades and scope are yours; this handoff names no finding wrong,
Minor or outside the scope.

## Where and what

- Worktree (read-only for you; write nothing but your report): `the root of the task's worktree`
- Method: `task-cycle/review/SKILL.md` of the worktree (project skill `the-way-review-change`); read
  it whole, and `task-cycle/review/whole_change.md` when it tells you to. Your variant: **the review
  of the whole change**.
- Range: base `55afa8e57aa1b83c77108576a36642722e0dda15` to head `172bc71c41b81cca6b6f31261550e64f121b4570`
  (verify with `git rev-parse HEAD`; on a mismatch, ask).
  Two commits: `0f34dc1`, `172bc71`. This is the one-author route: no plan, no spec, no slices, no
  slice reviews; the author's change is the whole range.
- Frozen task (read whole): `.runs/task-cycles/report-file-names-remarks-items/task.md`.
- Author's report (claims to verify, not evidence):
  `.runs/task-cycles/report-file-names-remarks-items/reports/author-report.md`.
- Answers of the cycle's start: trust boundary touched: no; irreversible operation: no; open design
  choice: none; the task did not move a pin (the-way itself).
- Settlement to check against the foundation change: *Settlements to record* row 1 of the task
  (WAY-294 states that a report without the section gives no item and no error, as the exception to
  WAY-344, with its reason; its *Verification* example `report-planner.md` becomes `planner-report.md`).
- Checks failing on the base: not yet known; the orchestrator's gate run on the base is still being
  collected. Do not assume any.
- You select your own foundation and guidelines (WAY-150). The task's *Decisions in play* are
  WAY-148, WAY-260, WAY-294, WAY-295, WAY-344. The author reports that these stayed unread or partly
  read, so judge them yourself: `elements/common/rules.md` and the glossary (`foundations/glossary.md`)
  were not read; WAY-148, WAY-30, WAY-260 and WAY-328 only in part. Check the WAY-294 edit against the
  decision element's template and rules, and check the new skill sentence of
  `task-cycle/skill/SKILL.md` against the wording the task's To do item 1 gives, word for word.
- Also check, among the rest: every task item (1–5) and the two questions' answers are carried out; the
  four cases of item 5 exist; the script's reading of `cycle.md` and of other files is as it was
  (the task's *Out of scope*); WAY-344's duty for the reading the change reworked (the task settles
  the no-section exception, nothing else); the docstring of `task-cycle/remarks_check.py` against the
  code (the author flagged its line on a report with no section).
- You may run the focused tests: `python -B gate/run_tests.py task-cycle` or one test file. Do not run
  the full gate.

## Report

Write your full report to `.runs/task-cycles/report-file-names-remarks-items/reports/review-whole-report.md`
(first line `PASS <sha>` or `FAIL <sha>`, as the method gives). Return its first line, a one-line check
result, and the path. Include **Unread material**, **Searches not found or unclear**, the count of
decisions read whole and by title, each reach beyond this handoff, and for each finding its grade, scope
and place in the code. List the Minor findings within the task's scope as the method asks.

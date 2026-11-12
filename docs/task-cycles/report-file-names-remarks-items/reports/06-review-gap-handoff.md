# Handoff — review of what the whole-change review left unread

## Delegation

The orchestrator holds the user's delegation; no contact with the human. Questions go to the
orchestrator in your report. You did not make the change and did not review it before. Grade and scope
are yours.

## Where and what

- Worktree (read-only for you, write only your report): `the root of the task's worktree`.
- Method: `task-cycle/review/SKILL.md` (project skill `the-way-review-change`), section 2 on how to review
  and section 4 on how to report. This is a narrow dispatch: not a second review of the whole change.
- Range: base `55afa8e57aa1b83c77108576a36642722e0dda15` to head
  `8dae4be92c7869e708ff66025b58b4b235878e4d` (verify with `git rev-parse HEAD`). Compute the diff yourself.
- Frozen task: `.runs/task-cycles/report-file-names-remarks-items/task.md` (read whole).
- Why you: the reviewer of the whole change (`reports/review-whole-report.md`, `PASS`) named these decisions of
  `foundations/decisions.md` as bearing on the change's topic and left unopened: WAY-38, WAY-125,
  WAY-296, WAY-308, WAY-309, WAY-326, and WAY-157 (named in the task's *Context*; the reviewer did not
  find it by title — search `foundations/decisions.md` for its heading, and if it is absent say so).
- Your job: read each of those decisions whole (heading to the next `###`, with Rationale and Rejected),
  and judge whether the change in the range contradicts, or leaves out something that, any of them
  requires. Report only what you find in the range's files: `foundations/decisions.md` (WAY-294),
  `task-cycle/remarks_check.py`, `task-cycle/test_remarks_check.py`, `task-cycle/skill/SKILL.md`.
  Findings carry grade, scope and place in the code as the method gives.
- You may run focused tests (`python -B gate/run_tests.py task-cycle`). Not the full gate.

## Report

Write `.runs/task-cycles/report-file-names-remarks-items/reports/review-gap-report.md`, first line
`PASS <sha>` or `FAIL <sha>`; then each decision read (whole or part), findings, checks with command and
exit code, **Unread material**, **Searches not found or unclear**. Return the first line, a one-line check
result and the path.

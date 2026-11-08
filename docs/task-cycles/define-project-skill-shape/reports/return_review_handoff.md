# Handoff — review of the return step, `define-project` in the shape of WAY-256

## Delegation

Mariusz asked the orchestrator to take this task through its cycle; the orchestrator dispatches
this review. You did not make the change. You ask no human; questions go back to the orchestrator
(first line `questions`).

## Where you work

- Process root and worktree: `.`
  (branch `task/define-project-skill-shape`). Read every file from it. Read-only: write only your
  report.
- Record directory (ignored by git): `.runs/task-cycles/define-project-skill-shape/`.

## Stage

Your method: `task-cycle/review/SKILL.md`, read whole, and a file it names when its step comes.
Your review: **the return step's commit**, a later change on the branch whose whole change
(`2754675..eeca32c`) already passed its review and the review of its fix.

Range: `eeca32c..09b0dd0` (one commit, "Name define-project's step 7 file readiness_gate.md, since
the glossary's gate is the test command"): `project-level/skill/gate.md` renamed to
`readiness_gate.md`, its three pointers in `SKILL.md` and `existing_definition.md` updated.

## What is reviewed against

- The frozen task: `.runs/task-cycles/define-project-skill-shape/task.md` (in Polish) — the
  requirement; in particular To do 2–3 and the acceptance criteria on pointers and on nothing
  changing outside `project-level/skill/`.
- The return step's method: `task-cycle/skill/return_step.md` and `task-cycle/skill/foundation_step.md`
  — what the return step compares and may correct.
- The entries the return step writes or corrects: none are written; the correction is the file
  name, made against the glossary entry of "gate" (`foundations/glossary.md`).
- The return step's report: `.runs/task-cycles/define-project-skill-shape/reports/return_report.md`
  — claims to verify, not evidence. It also says the figures of `reports/word-counts.md`,
  `reports/assessment.md` and the earlier reports were brought to the new name; check that no
  pointer, figure or route walk still names the old file where it should name the new one, and
  that every file of the-way that cites the skill's step numbers still points right.

Answers of step 4: no trust boundary, no irreversible operation.

The product's gate is the orchestrator's; run focused checks you need, each with command and exit
code.

## Report

Write the full report to `.runs/task-cycles/define-project-skill-shape/reports/return_review_report.md`
as your method gives it; first line `PASS <sha>`, `FAIL <sha>` or `questions`; include
**Searches not found or unclear**. Return only: the first line, the report path, a one-line check
result, and each blocking finding in one line.

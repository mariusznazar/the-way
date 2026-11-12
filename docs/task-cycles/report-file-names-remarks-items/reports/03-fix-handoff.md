# Handoff — the fix of a review's findings (Minor findings of the whole-change review)

## Delegation

The orchestrator holds the user's delegation. No contact with the human; questions to the
orchestrator in your report. Nothing here is the human's approval.

## Where and what

- Worktree: `the root of the task's worktree`, branch
  `task/report-file-names-remarks-items`, head before the fix `172bc71c41b81cca6b6f31261550e64f121b4570`.
- Method: `task-cycle/change/SKILL.md`, variant **the fix of a review's findings** (read `task-cycle/change/fix.md`
  when the method says).
- Findings file: `reports/findings-whole-minor.md` (in `.runs/task-cycles/report-file-names-remarks-items/`).
  Five Minor findings of the review of the whole change (`reports/review-whole-report.md`, `PASS`), all
  within the task. The reviewer alone graded and scoped them; fix all five, or answer with evidence a
  finding you hold wrong.
- Frozen task: `.runs/task-cycles/report-file-names-remarks-items/task.md`.
- Run the affected checks again (`python -B gate/run_tests.py task-cycle`, and
  `python -B elements/common/foundation_check.py foundations` after the WAY-294 edit). Not the full gate.
- Commit by explicit paths, messages in English.

## Report

Write your full report to `.runs/task-cycles/report-file-names-remarks-items/reports/fix-report.md`, with
**Unread material**, **Searches not found or unclear**, each check with command and exit code, and the
own-work check. Return status, commits, a one-line check result and the path.

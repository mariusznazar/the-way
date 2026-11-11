# Handoff — review of the fix of the whole-change review's findings

You are the reviewer of the whole change, resumed to review the fix once. The orchestrator's
delegation stands; nothing here is a human's approval.

- Method: `task-cycle/review/SKILL.md`, and `fix.md` beside it for the review of a fix — read it
  and follow it.
- Worktree (read-only): `the task's worktree root`,
  branch `task/backlog-line-for-plan-tasks`.
- Fix range: from the head you reviewed, `9eb2bd637697fd5f3cccdb891091110054f9d292`, to
  `9d5743d7648b4a5095fba28a7d6ab100cd078c3b` (one commit, `9d5743d`). Compute the diff yourself and
  confirm `git rev-parse HEAD`.
- Findings file: `docs/task-cycles/backlog-line-for-plan-tasks/reports/fix-findings.md` — your own
  words, lines 22-124 of your report, copied without change: B1 and Minor 1-6.
- The author's fix report, claims to verify: `docs/task-cycles/backlog-line-for-plan-tasks/reports/fix-report.md`.
  It names two reaches beyond the findings: WAY-154's binding sentence reworded for B1 (not only
  for Minor 5) and the orchestrator's making of a missing line at acceptance added to the entry;
  `project-level/lead/skill/SKILL.md` step 3.1 with the moment taken out. Judge each as the fix of a
  finding or as a new defect.
- Judge each finding as fixed or remains, and a new Critical or Important finding in the fix as one
  that remains. A Minor finding that remains or that the fix introduces does not block.
- The full suite and the 12-minute `project-level` directory run are the orchestrator's; do not run
  them.
- Report: `docs/task-cycles/backlog-line-for-plan-tasks/reports/fix-review-report.md`,
  first line `PASS <head sha>` or `FAIL <head sha>`, each finding as fixed or remains, **Declined to
  judge**, each check with command and exit code, each reach beyond this dispatch, **Unread material**
  and **Searches not found or unclear**. Return the first line, the counts of blocking, Minor and
  out-of-scope findings, a one-line check result and the report path.

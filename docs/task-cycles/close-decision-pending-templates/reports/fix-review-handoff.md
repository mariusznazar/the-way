# Handoff — review of the fix of the Minor findings

You reviewed the whole change (head `2c27260`, PASS with three Minor findings within the task). The author fixed them once.
Review the fix range once, as `task-cycle/review/fix.md` of `review-change` gives it (read it when the method names it).

- Worktree: `the root of the task's worktree`.
- Fix range: `2c27260`..`faee0f8`.
- Findings file the fix was given: `reports/whole-review-findings.md` (in the record directory, `docs/task-cycles/close-decision-pending-templates/` of the worktree).
- Fix report: `reports/fix-report.md` there. Your new report: `reports/fix-review-report.md` there, first line `PASS <sha>`, `FAIL <sha>` or `questions`.
- Only a new Critical or Important finding in the fix fails this review; a Minor finding that remains or is new does not block.
- The orchestrator runs the product's gate; you do not run it whole.

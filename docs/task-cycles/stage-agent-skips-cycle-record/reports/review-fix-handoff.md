# Handoff — review of the fix of the review's findings

Stage: the review of the fix, by the reviewer of the whole change, resumed; `task-cycle/review/SKILL.md`, which names `fix.md` for this review (read it when it tells you to).

- Range of the fix: from the reviewed head `de24e5b8d03893f53cee4f8083b8f4ef2d102028` to the head `91e1fa99`. Compute the diff yourself and confirm that `git rev-parse HEAD` is `91e1fa99`.
- Findings the fix answers: `.runs/task-cycles/stage-agent-skips-cycle-record/reports/review-whole-findings.md` (your own findings, in your words: one Important, two Minor within the task).
- The fix report (claims to verify, not evidence): `.runs/task-cycles/stage-agent-skips-cycle-record/reports/author-fix-report.md`.
- The frozen task as before: `.runs/task-cycles/stage-agent-skips-cycle-record/task.md`.
- Review the fix once: does it fix each finding, and does it bring a new Critical or Important finding? A new Minor finding does not block.
- Files of the cycle's record directory other than those named here are not yours to read.
- Your directory for working copies: `.runs/review-whole-2/`; the rule on working copies is as in your first handoff. Your report path: `.runs/task-cycles/stage-agent-skips-cycle-record/reports/review-fix-report.md`; its first line is `PASS <sha>` or `FAIL <sha>`, with **Unread material**, **Searches not found or unclear** and the working copies line. Run the foundation check and the checks the fix calls for, each with command and exit code; no full gate.
- Return the first line of the report, a one-line check result and the report's path.

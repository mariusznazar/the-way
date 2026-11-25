# Handoff — review of the fix of the whole-change review's findings, `review-change`

## Where you work

- The same worktree and branch: `the task's worktree`; read-only. Your directory for working copies: `.runs/review-fix-1/`.
- Your report: `.runs/task-cycles/ai-review-fixes-from-24-11/reports/review-fix-1-report.md`; its first line is `PASS <sha>` or `FAIL <sha>`. The report file is the input of the cycle's scripts.

## Your stage

The review of the fix, as `task-cycle/review/SKILL.md` and `task-cycle/review/fix.md` give it, by the same reviewer as the review of the whole change. Range: `225bf1c5..2dca6873` (one commit by the author, resumed).

- The findings the fix answers: `.runs/task-cycles/ai-review-fixes-from-24-11/reports/review-whole-findings.md` (no blocking finding; one Minor finding within the task, the two long wrapped lines in `README.md` and `agent-instructions/README.md`).
- The fix report: `.runs/task-cycles/ai-review-fixes-from-24-11/reports/author-fix-1-report.md`.
- Check that the fix answers the finding, that the text of the two paragraphs is unchanged word for word, and that it brings no new Critical or Important finding. A Minor finding that remains or is new does not block.

## What to return

The report with its **Unread material**, **Searches not found or unclear** and each check with its command and exit code; the working copy removed by its full path and named in the report.

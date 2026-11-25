# Handoff — review of the fix of the second review's findings, `review-change`

## Where you work

- The same worktree and branch: `the task's worktree`; read-only. Your directory for working copies: `.runs/review-fix-2/`.
- Your report: `.runs/task-cycles/ai-review-fixes-from-24-11/reports/review-fix-2-report.md`; its first line is `PASS <sha>` or `FAIL <sha>`. The report file is the input of the cycle's scripts.

## Your stage

The review of the fix, as `task-cycle/review/SKILL.md` and `task-cycle/review/fix.md` give it, by the same reviewer as the review of the whole change. Range: `2dca6873..b87125b6` (one commit by the one author, resumed).

- The findings the fix answers: `.runs/task-cycles/ai-review-fixes-from-24-11/reports/review-whole-2-findings.md` (I-1 and I-2, blocking; M-1 and M-2, Minor within the task).
- The fix report: `.runs/task-cycles/ai-review-fixes-from-24-11/reports/author-fix-2-report.md`.
- The orchestrator's rulings that the fix followed (binding for it, yours to judge where you hold one wrong): I-2 — WAY-12's *Rejected* keeps only Question 2's way not chosen (the field that carries the link) and WAY-30's *Rejected* keeps only the way of Question 1 that is a way of the product's rule (approval before the code); the other options are dropped, so no way a row's source does not keep, and none that is a way of how an answer is recorded, stands; the *Rationale* sentences stay where they still read true. M-2 — "asks that human no question about it".
- Check that each finding is answered, that no binding sentence of a decision changed beyond M-2's wording, that WAY-12's *Verification* tests clause and WAY-30's pair of examples stand as they were, and that the fix brings no new Critical or Important finding (a new Minor finding does not block).

## What to return

The report with its **Unread material**, **Searches not found or unclear** and each check with its command and exit code; the working copy removed by its full path and named in the report.

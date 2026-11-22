# Handoff — the review of the fix of the review's findings, `review-change`

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator; no answer here is that person's approval.

## Where you work

- The same worktree (`the task's worktree`). Your directory for working copies: `.runs/review-fix-1/` (directly under `.runs/`).
- Your report: `.runs/task-cycles/installer-foundation-check-full-path/reports/review-fix-1-report.md`, first line `PASS <sha>` or `FAIL <sha>` (the file is the input of the cycle's scripts; the rule against a subagent writing a file whose name starts with `report` does not apply to it; if refused, return the report whole as your answer). Keep the rule of working copies of your first handoff (`reports/review-whole-handoff.md`): remove your copies, state where each stood and that it was removed.

## Your stage

Review the fix of your own findings once, with `review-change`: read `task-cycle/review/fix.md` as the method names it and follow it. The range: from the reviewed head `1c222ce238c2194900ec246de5f8cc6cfa7faa5b` to the fix's head `674c93fe` (confirm `git rev-parse HEAD` is the full SHA that begins `674c93fe`); one commit.

- The findings the fix answers: `reports/review-whole-findings.md` (the blocking finding and the two Minor findings, copied in your words).
- The author's report of the fix: `reports/author-fix-1-report.md`. It is claims to verify. Where it says the sentence of the invariant says "warning" while the test also refuses an error, judge it as you would any gap between an invariant's sentence and its test.
- A new Critical or Important finding in the fix fails this review; a Minor finding that remains, or that you find new, does not block. Grade and scope are yours alone.
- Run the checks the method gives on the fix's head; run no full gate.

## What to return

The report with its first line, findings graded and scoped by you, each check with its command and exit code, **Unread material** and **Searches not found or unclear** (`none` where there is none), and the line on working copies. Return the status, the first line, one line on the checks and the report's path.

# Handoff — review of the fix of the whole-change review's findings

Stage: the review of the fix, by the reviewer of the whole change (resumed). Variant of `review-change`:
the review of the fix of earlier findings. Read-only; you grade and scope.

## Where and what

- Worktree: `the worktree root`, branch
  `task/precedence-between-decisions`.
- Range of the fix: base `9b44856c6b8bda6ea17f22808e3332694b026601` (the head you reviewed), head
  `baa07f44472de3d3c86cc61cb681c43ecb1bfd41`. Confirm `git rev-parse HEAD` and compute
  `git diff 9b44856..baa07f4` and `git log 9b44856..baa07f4` yourself.
- Method: `task-cycle/review/SKILL.md` and, for a fix, `task-cycle/review/fix.md`, which bounds this review.
- Findings fixed: `docs/task-cycles/precedence-between-decisions/reports/findings_whole_1.md` (one
  blocking, I1, then Minor M1-M3, cut from your report in your words).
- The author's fix report, a set of claims to verify:
  `docs/task-cycles/precedence-between-decisions/reports/fix_report.md`.
- Your own earlier report: `docs/task-cycles/precedence-between-decisions/reports/review_whole_report.md`.
- Frozen task: `docs/task-cycles/precedence-between-decisions/task.md`.
- Your O1 (out of scope) was not given to the author, as it is outside the task's scope; it goes to the
  request's list.

## Report

Write the full report to `docs/task-cycles/precedence-between-decisions/reports/review_fix_report.md`
with the first line `PASS <sha>` or `FAIL <sha>` (or `questions`), the checks you ran with command and
exit code, your reaches and **Searches not found or unclear**. Do not run the whole gate. Return the
first line, the checks and the report path.

# Handoff — review of the whole change (`review-change`)

You are a fresh reviewer that made none of this change. Read `.claude/skills/the-way-review-change/SKILL.md`
whole in the worktree and follow it; open a file it names only when its step comes. Review the
whole change as one author's change without a plan (no slices, no spec).

Worktree (work from its root, read-only): `the root of the task's worktree`
Range: base `e1726b78ad357791c5f84dd946f0edd26cdc3fe8` .. head `8fa6bac` (one commit).
Frozen task (read whole): `.runs/task-cycles/posix-class-not-a-link/task.md` (Polish).
Author's report: `.runs/task-cycles/posix-class-not-a-link/reports/author_report.md`.
Answers of step 4: touches a trust boundary: no; irreversible operation: no.
Check coverage of every item of "To do", the answers of "Questions to settle", and settlement row 1
(the change edits WAY-323 in place; the return step comes after your review). You select your own
foundation entries and guidelines (WAY-328: the-way departs from coding/testing guidelines in part
`task-cycle`; nothing to wait for). Run focused checks only (`python -B gate/run_tests.py task-cycle`;
the orchestrator runs the full gate). Report path: `.runs/task-cycles/posix-class-not-a-link/reports/review_report.md`.
The report's first line is `PASS <sha>` or `FAIL <sha>`; it holds graded findings, the checks you ran with
command and exit code, **Unread material**, **Searches not found or unclear** (`none` if so).
Return: the first line, changed files with line counts, the report path.

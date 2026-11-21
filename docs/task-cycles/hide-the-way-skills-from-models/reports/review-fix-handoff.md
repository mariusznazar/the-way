# Handoff to the reviewer of the fix

You reviewed the whole change (`reports/review-whole-report.md`, `PASS 7d063ef278748884de28577f582b2ab0767d068d`, six Minor findings within the task). The author fixed them once. You review the fix range once.

- Your variant: the review of a fix. Read `task-cycle/review/SKILL.md` again as it tells you and `task-cycle/review/fix.md` whole.
- Worktree: `the root of the task's worktree`. Range of the fix: base `7d063ef278748884de28577f582b2ab0767d068d`, head `f1efc257e7d2810d4072b0a82d2a98a78e889a3d` (confirm `git rev-parse HEAD`). Three commits: `90ac8500`, `2bd0efde`, `f1efc257`.
- Findings file the fix was given, in your words: `reports/review-whole-findings.md`. The author's report of the fix: `reports/author-fix-report.md` (claims to verify; it also corrects its first report's "46" to 23).
- Per `fix.md` and WAY-161/162: only a new Critical or Important finding fails this review; a Minor finding that remains or a new Minor one does not block and goes to the request's list.
- Directory for working copies: `.runs/review-fix/`; first paragraph of "Working copies" in `reports/review-whole-handoff.md` binds you again word for word. Report: `reports/review-fix-report.md`, first line `PASS <sha>` / `FAIL <sha>` / `questions`. Do not run the whole gate.

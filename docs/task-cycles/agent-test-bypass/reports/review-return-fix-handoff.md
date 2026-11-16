# Handoff — the review of the fix of the return step's finding

You are resumed as the reviewer of the return step. The author made the one fix of your blocking finding; you review it once (WAY-162).

- Stage: the review of a fix, method `task-cycle/review/fix.md` (named by section 1 of `task-cycle/review/SKILL.md`); read it whole and follow it.
- Worktree (read-only for you): `the root of the task's worktree`, branch `task/agent-test-bypass`. Range of the fix: base `91f6c884` (the head you reviewed) to head `b91fe896`; compute `git diff 91f6c884..b91fe896` and `git log 91f6c884..b91fe896` yourself and confirm `git rev-parse HEAD` is `b91fe896`.
- The findings file the fix was given: `reports/fix-findings-return.md` (in `.runs/task-cycles/agent-test-bypass/`): your blocking finding 1, in your words. Your finding 2 (outside the task) is not part of the fix; the cycle puts it before the human in the request.
- The fix report: `.runs/task-cycles/agent-test-bypass/reports/author-return-fix-report.md`: a claim to verify. The author says the fix is `git revert 91f6c884` and that `git diff 1a17406a b91fe896` is empty; check both yourself.
- Judge: whether finding 1 is met (both entries stand as at `1a17406a`, the head the whole change and its fix passed); whether the fix brings a new Critical or Important finding (it counts as one that remains); and whether the repository state at `b91fe896` is the state the earlier reviews accepted. Run `python -B elements/common/foundation_check.py`. You do not run the full gate.
- Your directory for working copies, if you need one: `.runs/review-return-fix/` of the worktree; remove it before you return and say where each copy stood.
- Your report: `.runs/task-cycles/agent-test-bypass/reports/review-return-fix-report.md`, first line `PASS <sha>` or `FAIL <sha>`; findings graded and scoped; checks with command and exit code; **Unread material**; **Searches not found or unclear** (or `none`).

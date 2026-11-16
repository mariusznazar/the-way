# Handoff — the fix of the return step's finding (the one author, resumed)

The review of the return step (your commit `91f6c884`) returned `FAIL`: one blocking finding (Important, `Contradiction: yes`) and one finding outside the task's scope, which is not yours to fix. This is the one fix a code review allows; a reviewer that did not make the change reviews it once.

- Worktree and branch as before: `the root of the task's worktree`, `task/agent-test-bypass`; the reviewed head is `91f6c884`; the fix's range runs from it.
- You make: **the fix of a review's findings**. Method: `task-cycle/change/fix.md` (you read it for the first fix), as `task-cycle/change/SKILL.md` section 1 gives.
- The findings file: `reports/fix-findings-return.md` (in `.runs/task-cycles/agent-test-bypass/`): the blocking finding, in the reviewer's words. The reviewer's report is `reports/review-return-report.md`; you may read it whole.
- What the reviewer says must come out: the two clauses the return step added to the end of the *Rejected* of WAY-410 and WAY-409 — both entries restored to their *Rejected* as at `1a17406a` (in effect the revert of `91f6c884`). Make it as a revert commit on the branch so that the history keeps the attempt (`git revert 91f6c884`, then check the diff against `git diff 1a17406a HEAD`, which must be empty for `foundations/decisions.md` and every other file). The question of the collision between WAY-100 and WAY-134 is the reviewer's finding 2, outside the task: it goes before the human in the request, and you write nothing of it into any entry. If you hold the finding wrong, answer with evidence instead of reverting, and say which evidence.
- Run again the checks the fix affects: `python -B elements/common/foundation_check.py`. You never run the product's full gate.
- Your directory for working copies, if you need one: `.runs/author-return-fix/` of the worktree; remove it before you return and say in the report where each copy stood.
- Your report: `.runs/task-cycles/agent-test-bypass/reports/author-return-fix-report.md`: how the fix meets the finding, your checks with command and exit code, your own-work check as the method gives it for a fix, **Unread material**, **Searches not found or unclear** (or `none`), working copies.
- Commit by path or by `git revert`, never `git add -A`, `git add .` or `git commit -a`; messages in English; no push.
- Return: status, commits, a one-line check result, the report's path.

# Handoff — review of the fix of the review of correction 1 (task slug `small-fixes-after-prs-117-121`)

You are resumed to review once the fix of your blocking finding I1 of the review of correction 1. The
orchestrator dispatches you; nothing here is the human's approval; ask the human nothing.

- Worktree: `the task's worktree`, head `5cb2e1f` (confirm `git rev-parse HEAD`). **The fix range is empty**: the findings said the fix needs no commit, and the author changed no file (`git rev-list 5cb2e1f..HEAD` is empty; confirm). The fix is a corrected account.
- Method: `task-cycle/review/SKILL.md`, the review of a fix; `task-cycle/review/fix.md`.
- Findings you gave: `docs/task-cycles/small-fixes-after-prs-117-121/reports/review-correction-findings.md` (I1). The fix report: `docs/task-cycles/small-fixes-after-prs-117-121/reports/correction-1-fix-report.md`.
- Judge: whether the corrected account removes I1 — WAY-114 marked `the cycle's`, the two clauses quoted word for word as `foundations/decisions.md` holds them at `5cb2e1f`, meaning sentences in English and Polish true of what the correction changed in WAY-114 — and whether the report's claim that no entry other than WAY-139, WAY-60 and WAY-114 carries an added pair is right (the report treats the two examples clauses of WAY-229 as changes of existing examples; the orchestrator will quote WAY-229's added *violates* clause under it in any case). The orchestrator carries the account into the request's section 6 and *Foundation entries*; judge the account, not a description that does not exist yet. A new Critical or Important finding fails this review; a Minor one goes to the request's list.
- No full gate. Report path: `docs/task-cycles/small-fixes-after-prs-117-121/reports/review-correction-fix-report.md`, first line `PASS <sha>` or `FAIL <sha>`. Your directory for working copies: `.runs/review-correction/` as before.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed,
except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
says, to the place the product's foundation settles for screenshots, and into the agent's directory
only where no such place is settled. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
`git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed.

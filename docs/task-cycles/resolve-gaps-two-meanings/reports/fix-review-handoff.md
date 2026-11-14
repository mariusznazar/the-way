# Handoff: review of the fix (task `resolve-gaps-two-meanings`)

You are the reviewer of the whole change, resumed, to review the fix of your findings once. The person who requested the cycle has delegated intermediate choices to the orchestrator; nothing here is that person's approval.

- Worktree: the task's worktree, branch `task/resolve-gaps-two-meanings`. Range of the fix: `9c66ee1179d0a84f41dec2c6c19d1d87de36d7dd..187bbde` (one commit; files `foundations/decisions.md` +20 −18, `project-level/task/skill/SKILL.md` +5 −4, `project-level/task/skill/resolve_gaps.md` +19 −16).
- Method: `task-cycle/review/SKILL.md`, the review of the fix of earlier findings. Findings file the fix was given: `reports/fix-findings.md`; your earlier report `reports/whole-change-review-report.md`; the fix report `reports/fix-report.md`, all in `.runs/task-cycles/resolve-gaps-two-meanings/`.
- Judge: whether I-1 and M-1..M-5 are fixed as you described them; whether the fix introduces a new finding; whether WAY-374 and the check of `resolve_gaps.md` now say the same thing, and the new wording of M-4 ("which step 5 finds and WAY-95 judges there") is true to what `project-level/task/skill/find_settlements.md` does — you did not read that file in the first review; read it whole now, with `project-level/task/skill/SKILL.md` section 5. Only a new Critical or Important finding fails this review; a Minor finding that remains or is new does not block and goes to the request's list.
- First line of the report: `PASS <sha>` or `FAIL <sha>`.
- Your directory for working copies: `.runs/review-fix/`.
- Report path: `.runs/task-cycles/resolve-gaps-two-meanings/reports/fix-review-report.md`, with checks (command, exit code), **Unread material**, **Searches not found or unclear** and working copies. Return the first line and the report's path.

Working copies, word for word from `task-cycle/skill/SKILL.md`:

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed.
The files that a product's own tools and tests make by themselves are no working copy of the agent
and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a
worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside
its report what the report needs, and states in the report where each copy stood and that it was
removed. Where a removal fails, the agent finishes all the same and names in the report the
remainder, with its full path and the reason it stayed.

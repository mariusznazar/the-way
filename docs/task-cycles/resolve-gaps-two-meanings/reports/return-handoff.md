# Handoff: the return step (task `resolve-gaps-two-meanings`)

You are the one author, resumed, for the return step of the cycle. The person who requested the cycle has delegated intermediate choices to the orchestrator; nothing here is that person's approval.

- Worktree: the task's worktree, branch `task/resolve-gaps-two-meanings`, head `187bbde` (the change: `f4af75d..187bbde`; the fix is reviewed `PASS 187bbde`).
- Method: read `task-cycle/skill/return_step.md` whole, and `task-cycle/skill/foundation_step.md` whole, since the return step writes as the foundation step writes; read the `SKILL.md` of an element when you write an entry of that element. Your stage is the return step, not a row of `make-change`'s table.
- Frozen task: `.runs/task-cycles/resolve-gaps-two-meanings/task.md`. Row 1 of *Settlements to record* is written as WAY-374.
- Compare the foundation entries the change writes or edits (WAY-374), those the task names (WAY-100, 113, 95, 99, 118) and those your search of the foundation found, and the part map of the touched parts, with the files of the repository, and correct in the same change whatever no longer matches. Write an invariant only for a rule the task, a decision or the human sets; none is set here. Where a correction would change the meaning of an approved decision beyond what the task settles (WAY-114), return it as a question instead of changing it.
- Run the affected checks again where you commit (`python -B elements/common/foundation_check.py`, and the `gate/run_tests.py` directories your edit touches). Do not run the whole gate: the orchestrator runs it.
- Your directory for working copies: `.runs/author/`.
- Report path: `.runs/task-cycles/resolve-gaps-two-meanings/reports/return-report.md`, with the sections the return step gives plus **Unread material**, **Searches not found or unclear** and working copies. Return status, commits (none if nothing needed correcting), a one-line check result and the report's path.

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

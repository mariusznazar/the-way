# Handoff: review of the whole change (task `resolve-gaps-two-meanings`)

You review the whole change of a task cycle of the-way as an agent that did not make it. The person who requested the cycle has delegated intermediate choices to the orchestrator; nothing here is that person's approval.

- Worktree (work only here, from its root; read-only for the repository): the task's worktree, branch `task/resolve-gaps-two-meanings`.
- Method: read `task-cycle/review/SKILL.md` of this worktree whole; your review is "the whole change", so read `task-cycle/review/whole_change.md` as the method says, and any other file the method names only when its step comes.
- Range: base `f4af75d85c7850696e5716d0c9678878559549d6` to head `9c66ee1` (one commit; `git diff f4af75d..9c66ee1`). Files: `foundations/decisions.md` +64, `project-level/task/skill/resolve_gaps.md` +17, `project-level/task/skill/SKILL.md` +2 −2.
- Frozen task, read whole: `.runs/task-cycles/resolve-gaps-two-meanings/task.md` (Polish; `Status: ready for cycle`; settlement row 1 accepted 2026-11-14). Check every item of *To do* (1–5), the five answers of *Questions to settle* with their ways not chosen, *Out of scope* and row 1 of *Settlements to record*, and the fidelity of the change to these sources.
- No spec, no plan (one author, no open design choice). Two questions at start: trust boundary — no; operation that cannot be undone — no. The author: report `.runs/task-cycles/resolve-gaps-two-meanings/reports/author-report.md` (read it as the author's account; judge the code, not the report).
- The task did not move the pin; there is no checks-carried list. The checks already failing on the base: none (the base's final gate passed).
- Selection: you select your own foundation and guidelines by "Reading the foundation" in `elements/common/way_of_working.md`; the-way has no `guidelines/` directory. The author's report names what it left unread: the decisions whose *Scope* names `project-level` (beyond those it read) and the invariants whose *Part* names `project-level` or `every`, and the full part map; those gaps are yours to cover, besides the tail of WAY-134 and WAY-150. Check specially that the new entry WAY-374 contradicts no existing decision or invariant, that WAY-95, WAY-99, WAY-100, WAY-113 and WAY-118 keep their meaning, and that the new wording of `resolve_gaps.md` does not invite the invented edge cases the task's answer 2 guards against.
- Your directory for working copies: `.runs/review-whole/`.
- Report path: `.runs/task-cycles/resolve-gaps-two-meanings/reports/whole-change-review-report.md`. First line `PASS <sha>` or `FAIL <sha>`. Include **Unread material**, **Searches not found or unclear**, the count of decisions read whole and by title, each check with command and exit code, the Minor findings within the task and those outside its scope marked as such. Return the first line, the changed files with line counts, and the report's path.

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

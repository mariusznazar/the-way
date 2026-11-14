# Handoff: the fix of the review's findings (task `resolve-gaps-two-meanings`)

You are the one author, resumed, fixing the findings of the review of the whole change. The person who requested the cycle has delegated intermediate choices to the orchestrator; nothing here is that person's approval.

- Worktree: the task's worktree, branch `task/resolve-gaps-two-meanings`, head reviewed `9c66ee1179d0a84f41dec2c6c19d1d87de36d7dd`; your fix's range runs from it.
- Method: `task-cycle/change/SKILL.md`, variant "the fix of a review's findings"; read the file it names for the variant when that step comes.
- Findings file: `reports/fix-findings.md` in `.runs/task-cycles/resolve-gaps-two-meanings/` (the reviewer's words: one blocking finding I-1, Important, and the Minor findings M-1..M-5 within the task, which are fixed in the same round, WAY-161). The full review: `reports/whole-change-review-report.md` beside it.
- Fix each finding; where you hold one wrong, answer with evidence in the report instead of changing it. For I-1 the reviewer proposes bringing the entry to the skill's condition ("whose resolution changes the definition"); bring the two to one wording. For M-4 and M-5 the wording is yours within the task's answers (Q4: a reader-of-the-field meaning goes as a candidate by WAY-95's road; To do 3: "as a question of decision according to How a skill asks"); do not widen the task and change no meaning of WAY-95, WAY-99, WAY-113 or WAY-118.
- Run again the affected checks: `python -B elements/common/foundation_check.py` and the `gate/run_tests.py` directories your edit touches (`project-level`, `instruction-files`; others only if touched). Do not run the whole gate.
- Your directory for working copies: `.runs/author/` (the one you used; it needs recreating only if you make a copy).
- Report path: `.runs/task-cycles/resolve-gaps-two-meanings/reports/fix-report.md`, with the sections your method gives (checks with command and exit code, own-work check, **Unread material**, **Searches not found or unclear**, working copies, and for each finding what you did). Return status, commits, a one-line check result and the report's path.

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

# Handoff — the return step

You are the one author, resumed, for the return step of the task cycle (step 11 of
`implement-task`). The person who requested the cycle has delegated the intermediate choices to the
orchestrator; nothing you or the orchestrator say is that person's approval.

- Worktree: `.`, branch
  `task/cycle-after-foundation-review`, head `cfda61e` (the review of the whole change and the review
  of its Minor findings' fix both returned `PASS`). The range of the change: base
  `739c8139bc7f2e74ef0f4c2f0a76a4352614cfd6` to `cfda61e`.
- Stage: the return step. It is no variant of `make-change`'s table; read
  `task-cycle/skill/foundation_step.md` whole and `task-cycle/skill/return_step.md` whole, each by its
  path in this worktree, and, when you write an entry of an element, that element's `SKILL.md` at
  the path `foundation_step.md` gives.
- The frozen task: `.runs/task-cycles/cycle-after-foundation-review/task.md`; its *Decisions in play*
  name the entries to compare (WAY-13, WAY-25, WAY-375, WAY-376, WAY-261, WAY-243, WAY-289), and
  its *Settlements to record* (7 rows) are what the foundation step wrote or placed in a skill.
- What to compare with the code: the entries the change wrote or changed (the decisions of your
  foundation step: WAY-13's *Verification*, WAY-375, WAY-376, WAY-261, WAY-289), those the task
  names, those the search of the foundation found, and the part map of the touched parts
  (`decisions`, `task-cycle`, `agent-instructions`), each with the files of the repository
  (`task-cycle/remove_merged_worktrees.py` and its tests, `task-cycle/skill/SKILL.md`,
  `task-cycle/skill/correction.md`, `task-cycle/skill/request_template.md`,
  `agent-instructions/README.md`, `task-cycle/request_check.py`). Correct in the same change whatever
  no longer matches. The review reports of the cycle are no source of entries, and no entry is
  deferred.
- Do not run the whole gate (the orchestrator's run). Run the checks of the directories your
  corrections reach, and `python -B elements/common/foundation_check.py` (full) if you change any
  entry.
- If the return step commits nothing, say so and leave the worktree as it is, clean.
- Agent directory for working copies: `.runs/author/`.
- Report path: `.runs/task-cycles/cycle-after-foundation-review/reports/return-step-report.md`. Its
  content, as the record's *Return step* gives it: the foundation compared with code (what no
  longer matched and its correction, or none); decisions written or changed; invariants written or
  changed, each with what sets its rule; environment facts; glossary terms; part-map changes;
  projected entries written; rows of *Settlements to record* written, each by its row number and
  where it went. Also the checks with command and exit code, reaches, **Unread material**,
  **Searches not found or unclear**, working copies.

## Working copies

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

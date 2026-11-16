# Handoff — review of the commits of the return step

## Delegation

The person who requested this cycle delegated the intermediate choices to the orchestrator. You review as an agent that made none of the
change; grade and scope of every finding are yours; you ask no human anything.

## What you review

- Method: `task-cycle/review/SKILL.md`, read whole. Your variant: the return step's commits, "reviewed as section 2 gives, against the task
  and the foundation entries the return step writes or corrects". Where the skill names a file for that variant, read it when that step comes.
- Worktree `the root of the task's worktree`, branch `task/script-invariants-by-test`. You change nothing in it.
- Range: base `540aed04` to head `3043e760` (one commit by the author in its return step; it changes `foundations/part_map.md` only). Compute
  the diff yourself (`git diff 540aed04..3043e760`, `git log 540aed04..3043e760`) and confirm `git rev-parse HEAD`.
- The task, word for word the passages that bear on it, in `docs/task-cycles/script-invariants-by-test/task.md`: *To do* items 1-5,
  *Settlements to record* rows 1-3, *Decisions in play*, *Out of scope*. The change before the return step: base `604907c8` to `540aed04`,
  reviewed and passed twice; you review only the return step's commit against it.
- The author's return report: `docs/task-cycles/script-invariants-by-test/reports/author-return-report.md` — claims to verify, not evidence.
- Foundation entries, by identifier, each whole: the part-map entries `agent-instructions`, `elements-common`, `part-map` and `repository` in
  `foundations/part_map.md` (read the whole file, it is short); decisions WAY-44, WAY-09, WAY-11, WAY-33, WAY-38, WAY-89, WAY-08, WAY-61; the
  invariants `python-version-declared`, `script-language`, `script-imports`, `element-directory-contents`, `cross-part-imports`
  (`foundations/invariants.md`). The form of a part-map entry: `elements/part-map/template.md` and `elements/part-map/skill/SKILL.md`.
- What to judge: whether the two changed sentences of the part map are true of the files of the repository and say what the files
  `agent-instructions/test_script_invariants.py` and `elements/common/test_element_directory_contents.py` hold; whether any other entry
  names the old sentences or a place the moved file left (the search of the foundation, WAY-33); whether the return step missed a
  correction the change calls for; whether it wrote something the rule of the return step (`task-cycle/skill/return_step.md`) forbids.
- Working copies in `.runs/review-return/` of the worktree; remove them before you return. Report:
  `docs/task-cycles/script-invariants-by-test/reports/review-return-report.md`, first line `PASS <sha>` or `FAIL <sha>`.
- You run no full gate (WAY-160); you may run `python -B elements/common/foundation_check.py` and a focused directory.

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

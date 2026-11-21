# Handoff — executor of slice 4

You make slice 4 of a planned change in a task cycle of the-way. The person who requested the cycle has delegated every intermediate choice to the orchestrator; no answer you get is that person's approval. You never ask the human; questions go back to the orchestrator in your report.

- Worktree (your working directory for everything): `the worktree root`, task branch `task/small-fixes-from-ai-review-and-audit`. Slice 4's base: `5160a7b9` (`git rev-parse HEAD` now). Start from the worktree's root.
- Method: `task-cycle/change/SKILL.md` (`make-change`) in the worktree, read whole. Your variant, in the words of its table's row: "a slice, or the retry of a slice". Read `task-cycle/change/slice.md` beside it. The skill tool is not yours: a skill a file names is the `SKILL.md` whose frontmatter `name:` is that name, read as a file under the same root.
- Stage and boundary: slice 4 only. You do not start slice 5.
- Report path: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/reports/executor-4-report.md`.
- Your directory for working copies: `.runs/executor-4/`.
- Answers of the cycle's step 4: trust boundary yes for the change as a whole (not for this slice, whose risk is `none`); irreversible operation no.
- Frozen task: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md` (open only the lines the slice's *Read* names).

## Your slice, word for word from the plan

### Slice 4 — the hand-over of a skill to another stands once: the other nine skills

- **Goal:** each of the nine skills `foundation-review/SKILL.md`, `product-guidelines/coding/SKILL.md`, `product-guidelines/styleguide/SKILL.md`, `product-guidelines/testing/SKILL.md`, `project-level/lead/skill/SKILL.md`, `project-level/plan/skill/SKILL.md`, `project-level/skill/SKILL.md`, `project-level/task/skill/SKILL.md` and `project-level/technology/SKILL.md` has the sentences that say how a named skill is handed on to (the-way itself: its `SKILL.md` read as a file and never called; a product: the project skill with the `the-way-` prefix) replaced by the one instruction that slice 3 wrote in the six skills of the elements, adapted to the words of the skill (a skill named "below", "here" or in the files beside it); the file `elements/common/hand_over.md`, made by slice 3, is read whole first, and its wording of the instruction is the model. The rest of each paragraph and of each skill stays as it is; in `project-level/lead/skill/SKILL.md` the instruction that the brief of an agent the skill dispatches for such a skill gives the path of that file stays, as the one instruction only sessions on the-way itself use. No description of a skill changes, so no entry point changes; after the slice `elements/common/hand_over.md` is the only file that holds the sentences.
- **Change:** `foundation-review/SKILL.md` · `product-guidelines/coding/SKILL.md` · `product-guidelines/styleguide/SKILL.md` · `product-guidelines/testing/SKILL.md` · `project-level/lead/skill/SKILL.md` · `project-level/plan/skill/SKILL.md` · `project-level/skill/SKILL.md` · `project-level/task/skill/SKILL.md` · `project-level/technology/SKILL.md`
- **Read:** `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md:40-40` *To do* point 9 · `foundations/decisions.md:3329-3422` WAY-127 · `foundations/decisions.md:1492-1522` WAY-35 · `foundations/decisions.md:3423-3538` WAY-256 · `foundations/part_map.md:65-81` elements-common · `foundations/part_map.md:82-103` project-level · `foundations/part_map.md:117-127` foundation-review · `foundations/part_map.md:214-225` product-guidelines
- **Model:** cheaper
- **Risk:** none
- **Checks:** `git grep -n "read as a file, not called"` finds `elements/common/hand_over.md` alone among the files git tracks outside `foundations/`, `.claude/` and `.agents/`; `python -B agent-instructions/skill_entry_points.py` reports nothing to create or change; `python -B gate/run_tests.py product-guidelines` passes (it finds a pointer to a file that is not there); `python -B elements/common/foundation_check.py` reports nothing.
- **Depends on:** Slice 3


## Notes of the orchestrator for this slice

- Slice 3 (commit `5160a7b9`, the head of the branch now) wrote `elements/common/hand_over.md` and, in the six skills of the elements, replaced the hand-over sentences by one instruction. Read `elements/common/hand_over.md` whole first, then one of the six (`elements/decisions/skill/SKILL.md`, the paragraph "This skill lives in …") as the model of the instruction; adapt its words to each of your nine skills (a skill named "below", "here" or in the files beside it). The old sentences wrap at different points in each skill, so find them by reading the paragraph of each skill that tells where the skill lives, not by a one-line search.
- `project-level/lead/skill/SKILL.md` carries a second instruction (the brief of an agent it dispatches for such a skill gives the path of the file): it stays, as the plan's Goal says.
- After the slice no skill outside `elements/common/hand_over.md` (and `foundations/`, `.claude/`, `.agents/`) holds the sentence "read as a file, not called": check it with `git grep` and by reading, and report what you see.

## What you return and keep (WAY-148, WAY-164, WAY-260)

- Make the slice from its section above and the *Read* it names; do not open the plan. Where the plan and the code disagree, `slice.md` says what to do.
- Write the failing test first where the slice changes behaviour, and keep the failing run's command and exit code for your report. A check you report carries its command and its exit code; run only the focused checks the slice's *Checks* names, never the product's gate (`python -B gate/run_tests.py` with no directory), which the orchestrator or CI runs.
- Commit your work on the task branch, by path (`git add <path> <path>`, never `git add -A`, `git add .` or `git commit -a`), with commit messages in English; leave the worktree clean. Name your commits in the report. Do not push.
- Your report holds: the status (`done`, `done with concerns`, `questions`, `returned` or `blocked`, as the method gives), your commits, each check with its command and exit code, the own-work check the method asks for (the weakest point of your work, how you tested it, what it showed), each reach beyond this handoff (what, where, why), each working copy (where it stood and that you removed it, or the remainder with its full path), **Unread material:** each file, entry or passage this handoff names that you did not read whole or read in part, or `none`, and **Searches not found or unclear:** each thing you looked for and did not find or that was unclear, or `none`. Return the status, your commits, a one-line check result naming what failed or did not run, and the report's path.
- Do not read `cycle.md` or any file of `.runs/task-cycles/small-fixes-from-ai-review-and-audit/` that this handoff does not name.
- The report file is the input of the cycle's scripts (`task-cycle/remarks_check.py` reads it), so write it at the path above although its name could look like one Claude Code refuses a subagent to write; if the write is refused all the same, return the report whole as your answer.

## Working copies (word for word from the process of the cycle)

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
all the same and names in the report the remainder, with its full path and the reason it stayed. It
removes a copy, as any directory, by its path written out in full in the command, never through a
shell variable: an empty variable turns the removal on the directory the shell stands in.

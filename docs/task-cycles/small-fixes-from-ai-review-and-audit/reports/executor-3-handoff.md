# Handoff — executor of slice 3

You make slice 3 of a planned change in a task cycle of the-way. The person who requested the cycle has delegated every intermediate choice to the orchestrator; no answer you get is that person's approval. You never ask the human; questions go back to the orchestrator in your report.

- Worktree (your working directory for everything): `the worktree root`, task branch `task/small-fixes-from-ai-review-and-audit`. Slice 3's base: `bcd8e55167b7ad60aa4c3fafa7da7e978858b0f0` (`git rev-parse HEAD` now). Start from the worktree's root.
- Method: `task-cycle/change/SKILL.md` (`make-change`) in the worktree, read whole. Your variant, in the words of its table's row: "a slice, or the retry of a slice". Read `task-cycle/change/slice.md` beside it. The skill tool is not yours: a skill a file names is the `SKILL.md` whose frontmatter `name:` is that name, read as a file under the same root.
- Stage and boundary: slice 3 only. You do not start slice 4.
- Report path: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/reports/executor-3-report.md`.
- Your directory for working copies: `.runs/executor-3/`.
- Answers of the cycle's step 4: trust boundary yes for the change as a whole (not for this slice, whose risk is `none`); irreversible operation no.
- Frozen task: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md` (open only the lines the slice's *Read* names).

## Your slice, word for word from the plan

### Slice 3 — the hand-over of a skill to another stands once: the shared file and the skills of the elements

- **Goal:** the file `elements/common/hand_over.md` is new and holds, once, the way a skill of the-way hands work on to another skill of the-way: in the-way itself the other skill's `SKILL.md` is read as a file from the checkout or worktree the session works in and never called, since Claude Code does not offer the entry points of the-way's skills to the model; its path is the one the list of skills in the entry point the session started with gives, or, where the session started without one, the file under that root whose frontmatter has the line `name: <that name>`, found by a search of the files git lists as `SKILL.md`; the skill is read in full and followed; in a product it is the project skill of that name with the `the-way-` prefix. It says no more and no less than the sentences it replaces. In each of the six skills `elements/common/skill/SKILL.md`, `elements/decisions/skill/SKILL.md`, `elements/environment-facts/skill/SKILL.md`, `elements/glossary/skill/SKILL.md`, `elements/invariants/skill/SKILL.md` and `elements/part-map/skill/SKILL.md`, the sentences that say this (from "In the-way itself, a skill named below …" to "… the project skill of that name with the `the-way-` prefix") are replaced by one instruction that names `elements/common/hand_over.md`, says that a skill named in this skill or in the files beside it is handed on to as that file gives, and has the file read when the first hand-over comes; the rest of the paragraph (where this skill lives, where the-way lies, the element's directory) and the rest of the skill stay as they are. The Verification of WAY-127, in `foundations/decisions.md`, has its line on "the paragraphs of the skills that say where the-way lies" reworded in place, and nothing else of that entry changes: its binding paragraphs, its other lines of Verification, its *Rationale* and *Rejected*. The reworded line says that a skill's paragraph names the checkout or worktree the session works in as the place of the-way for the-way itself and the pinned `.the-way` for a product, and that the shared file the paragraph points to names the other the-way skill a skill hands work on to as the file `SKILL.md` read from that checkout or worktree for the-way itself and as the project skill with the `the-way-` prefix for a product; its *violates* line stays. No description of a skill changes, so no entry point changes.
- **Change:** `elements/common/hand_over.md` · `elements/common/skill/SKILL.md` · `elements/decisions/skill/SKILL.md` · `elements/environment-facts/skill/SKILL.md` · `elements/glossary/skill/SKILL.md` · `elements/invariants/skill/SKILL.md` · `elements/part-map/skill/SKILL.md` · `foundations/decisions.md`
- **Read:** `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md:40-40` *To do* point 9 · `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md:86-86` *Context*, the way of working file stays unchanged · `elements/common/way_of_working.md` · `.claude/skills/the-way-record-glossary-term/SKILL.md` · `foundations/decisions.md:3329-3422` WAY-127 · `foundations/decisions.md:1492-1522` WAY-35 · `foundations/decisions.md:3423-3538` WAY-256 · `foundations/decisions.md:2178-2213` WAY-84 · `foundations/invariants.md:96-105` skill-rule-source · `foundations/invariants.md:284-293` skill-entry-points · `foundations/part_map.md:65-81` elements-common
- **Model:** cheaper
- **Risk:** none
- **Checks:** `git grep -n "read as a file, not called" -- elements` finds the new file alone; `python -B agent-instructions/skill_entry_points.py` reports nothing to create or change; `python -B elements/common/foundation_check.py` reports nothing; `python -B gate/run_tests.py elements/common` passes.
- **Depends on:** none


## Notes of the orchestrator for this slice

- Source of the paragraph: the request https://github.com/mariusznazar/the-way/pull/154 (merged) rewrote the hand-over sentences in 15 skill files; its *Technical changes* list them. Slice 3 moves them out of the six skills of the elements into `elements/common/hand_over.md`; slice 4, which follows, does the other nine from your file as the model, so word the file and the one instruction that names it so that a skill outside the elements can use them (the skill names the other skill "below", "here" or "in the files beside it").
- Find the sentences by reading the six skills (they wrap lines, so a one-line search for "read as a file, not called" may miss them: look at the paragraph that begins "This skill lives in …" in each). The new file says what the sentences say, no more and no less; the skill keeps what it says of where the skill lives, where the-way lies and the element's directory.
- The line to reword in WAY-127's *Verification* is the one on "the paragraphs of the skills that say where the-way lies". Reword that one line in place; change nothing else of WAY-127. The ranges of the decisions in *Read* are current at your base.
- No description of a skill changes, so no entry point changes; the generator, run without `--write`, must report nothing to create or change.
- Your *Checks* name `git grep -n "read as a file, not called" -- elements`: where a sentence wraps, the search finds the file only where the phrase stands on one line; look at the paragraph of each of the six skills by eye as well and report what you see.

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

# Handoff — executor of slice 5

You make slice 5 of a planned change in a task cycle of the-way. The person who requested the cycle has delegated every intermediate choice to the orchestrator; no answer you get is that person's approval. You never ask the human; questions go back to the orchestrator in your report.

- Worktree (your working directory for everything): `the worktree root`, task branch `task/small-fixes-from-ai-review-and-audit`. Slice 5's base: `5bdef59f` (`git rev-parse HEAD` now). Start from the worktree's root.
- Method: `task-cycle/change/SKILL.md` (`make-change`) in the worktree, read whole. Your variant, in the words of its table's row: "a slice, or the retry of a slice". Read `task-cycle/change/slice.md` beside it. The skill tool is not yours: a skill a file names is the `SKILL.md` whose frontmatter `name:` is that name, read as a file under the same root.
- Stage and boundary: slice 5 only. You do not start slice 6.
- Report path: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/reports/executor-5-report.md`.
- Your directory for working copies: `.runs/executor-5/`.
- Answers of the cycle's step 4: trust boundary yes for the change as a whole (not for this slice, whose risk is `none`); irreversible operation no.
- Frozen task: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md` (open only the lines the slice's *Read* names).

## Your slice, word for word from the plan

### Slice 5 — three wordings: the source of a fact without an archived copy, and the own search of the return step

- **Goal:** the three wordings that points 1 to 3 of *To do* give stand in the files: in `elements/environment-facts/template.md`, section `## Source`, the second form of a source (the page without editions) reads as point 1 gives it, the line of its other bullets and every other line of the file unchanged; in `task-cycle/skill/return_step.md` the list of entries the return step compares with the code reads as point 2 gives it; in `task-cycle/record_template.md`, section `## Return step`, the item *Foundation compared with code* reads as point 3 gives it. The text of each is the one of the task, character for character. No other line of the three files changes, `elements/common/way_of_working.md` stays as it is, and the form line of `**Source:**` at the top of the template stays as it is.
- **Change:** `elements/environment-facts/template.md` · `task-cycle/skill/return_step.md` · `task-cycle/record_template.md`
- **Read:** `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md:27-34` *To do* points 1 to 3 · `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md:44-55` *Questions to settle*, the first two · `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md:78-86` *Context*, the lines on points 1 to 3 · `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md:108-110` *Decisions in play*, WAY-84, WAY-11 and WAY-33 · `foundations/decisions.md:2178-2213` WAY-84 · `foundations/decisions.md:6053-6099` WAY-11 · `foundations/decisions.md:1459-1491` WAY-33 · `foundations/invariants.md:46-55` return-step-record · `foundations/part_map.md:56-64` environment-facts · `foundations/part_map.md:104-116` task-cycle
- **Model:** cheaper
- **Risk:** none
- **Checks:** `git diff --stat` of the slice names the three files and no more; `python -B elements/common/foundation_check.py` reports nothing; `python -B gate/run_tests.py elements/common` and `python -B gate/run_tests.py task-cycle` pass.
- **Depends on:** none


## Notes of the orchestrator for this slice

- The text of each of the three wordings is in the task, character for character: points 1, 2 and 3 of *To do* (lines 27-34 of the frozen task, in *Read* above). Where the task gives "jest:" (what is there now) compare it with the file at your base: it must match, and if it does not, say so in your report and do not guess. The new text replaces the "jest" text, and the words around it in the same sentence stay.
- Do not change the form line of `**Source:**` at the top of `elements/environment-facts/template.md` and no other line of the three files. `elements/common/way_of_working.md` stays unchanged.
- Point 1: the new text contains backticks and a placeholder `<date>`; keep them exactly. Write nothing Polish into these files; they are English.
- Check, besides the checks of the slice: `git diff --stat` names exactly the three files, and the added and removed lines are the ones of the three wordings.

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

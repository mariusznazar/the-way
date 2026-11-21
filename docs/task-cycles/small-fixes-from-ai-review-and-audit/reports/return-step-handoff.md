# Handoff — the return step

You take the return step of a task in a task cycle of the-way, step 11 of `implement-task`, as a fresh agent with `make-change`. The person who requested the cycle has delegated every intermediate choice to the orchestrator; no answer you get is that person's approval. You never ask the human; questions go back to the orchestrator in your report.

- Worktree (your working directory for everything): `the worktree root`, task branch `task/small-fixes-from-ai-review-and-audit`, head `5d160f9d75f25c26092815ba98df43c6cc4aa2f6` (`git rev-parse HEAD` now): the change as the review of the whole change and the review of its fix passed it. The range of the whole change: `268b2b07..5d160f9d`.
- Method: `task-cycle/skill/return_step.md`, read whole, and `task-cycle/skill/foundation_step.md`, read whole (the return step writes as the foundation step writes); and `task-cycle/change/SKILL.md` (`make-change`) for how a change is made and reported; the `SKILL.md` of an element, at the path `foundation_step.md` gives, when you write an entry of that element, read whole. You take none of the rows of the table of variants of `make-change`: your handoff names your stage. The skill tool is not yours: a skill a file names is the `SKILL.md` whose frontmatter `name:` is that name, read as a file under the same root.
- Stage and boundary: the return step only. You write no new feature and no test beyond what the step asks; you correct, in the same change, whatever no longer matches between the foundation entries and the code, and write the entries the step gives. Commit what you change, by path, with messages in English; leave the worktree clean; do not push. If nothing no longer matches, commit nothing and say so.
- Report path: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/reports/return-step-report.md`. The report file is the input of the cycle's scripts (`task-cycle/remarks_check.py` reads it); write it there although its name could look like one Claude Code refuses a subagent to write; if the write is refused all the same, return it whole as your answer. The report's form follows the record's *Return step* of `task-cycle/record_template.md` (read that section): the eight items, each with its answer or `none`.
- Your directory for working copies: `.runs/return-step/`.
- Frozen task, whole: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md`. Plan: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/plan.md` (its *Foundation entries* and *Choices*). Answers of step 4: trust boundary yes (`task-cycle/gate_times.py`, the docstring of `process-audit/audit_count.py`); irreversible operation no; open design choice none.
- Do not read `cycle.md` or any file of `.runs/task-cycles/small-fixes-from-ai-review-and-audit/` that this handoff does not name.

## What the change wrote and changed (to compare with the code)

- The foundation entries of the change (the plan's *Foundation entries*, commit `a946862b`, narrowed by the fix `f358aa42`): WAY-339 (two sentences added and a clause of its *Verification*: `foundations/decisions.md`, heading "WAY-339"), the new decision WAY-417 (Q1 to Q3 of a group of cycles), and the line of WAY-127's *Verification* about the paragraphs of the skills (`5160a7b9`, `5bdef59f`). Read each whole.
- The code: `task-cycle/gate_times.py` (the lines of a nested runner output), `process-audit/series_summary.py` (new), `process-audit/version_analysis.py`, `process-audit/audit_report.py`, `process-audit/audit_count.py` (docstring only), `process-audit/SKILL.md`, the tests `process-audit/test_series_summary.py`, `process-audit/test_process_versions.py` (the tests of the versions moved out of `process-audit/test_audit_count.py`), `task-cycle/test_gate_times.py`; the file `elements/common/reaching_another_skill.md` (new) and the 15 skills that point to it; the three wordings of `elements/environment-facts/template.md`, `task-cycle/skill/return_step.md` (the sentence you are reading) and `task-cycle/record_template.md`.
- The entries the task names (*Decisions in play*): WAY-84, WAY-11, WAY-33, WAY-339, WAY-350 — compare each with the code and files above.
- The part map of the touched parts: `foundations/part_map.md` entries `task-cycle`, `process-audit`, `elements-common`, `project-level`, `product-guidelines`, `foundation-review`, `environment-facts`. The review of the whole change noticed (its Minor 10, left to you): the sentence of the entry `elements-common` names "the way of working shared by foundation-entry skills", while `elements/common/reaching_another_skill.md` now serves the nine skills of `project-level`, `product-guidelines` and `foundation-review` as well; compare and correct the map if it no longer matches (WAY-11).
- Your own search (the sentence of `return_step.md` this change added): one search of the foundation by the names and words that the change's code adds — for instance `series_summary`, `reaching_another_skill`, `PIECES_KEPT`, the image of a series, "before and after", `yes n · no n · unknown n` and the like — for the entries, outside those above, that name them or that no link joins to them; compare what you find with the code, and say in the report what you searched by and what you found.
- Pairs of examples and tests: WAY-339 and WAY-417 carry pairs of examples in their *Verification* that the foundation step wrote until tests of the same change hold the sentences. The tests of `process-audit/test_series_summary.py` and `process-audit/test_process_versions.py` now carry lines `decision:` for them. Do as `return_step.md` says: where a test holds part of a sentence, remove that part from the pair, name the test by the clause `tests:` of the decision's *Verification*, and leave a pair only for a part no test holds. Then run `python -B elements/common/foundation_check.py` (it must end with exit 0 and `0 errors`) and `python -B gate/run_tests.py elements/common`.
- The invariant `skill-entry-points` and the generator, whose entry points were not changed by the change: run `python -B agent-instructions/skill_entry_points.py` once and report its result.

## What the return step must not do

It writes an invariant only for a rule the task, a decision or the human sets, never for behaviour merely because no invariant covers it. No entry is deferred. The review findings of the request are no foundation entries. The task's *Out of scope* binds: WAY-84 and `elements/common/way_of_working.md` stay as they are.

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

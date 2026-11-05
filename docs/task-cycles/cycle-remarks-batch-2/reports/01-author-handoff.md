# Handoff 01 — the one author of the whole change

## Delegation

You are the one author of this change, dispatched by the orchestrator of `implement-task`. The
person who requested the cycle delegated every intermediate choice to the orchestrator; ask no
human. Send a question to the orchestrator in your report (status `questions`); never start the
next stage, never ask for approval.

## Where you work

- Worktree (work only here, from its root): `C:\Storage\repos\the-way\.runs\worktrees\cycle-remarks-batch-2`
- Branch: `task/cycle-remarks-batch-2`, base `61c72fb6347649a9bd61a71f0d2695f2e91e8b6a` (`foundations`)
- Commit on this branch only. No push, no merge, no other branch. Touch nothing outside the worktree
  except your report.

## Your method and your variant

- Method: `task-cycle/change/SKILL.md` in the worktree — read it whole.
- Your variant, in the words of its row: **the whole change as the one author**.
- Read a file that method names only when the step or variant that names it comes.
- The foundation step is yours: read `task-cycle/skill/foundation_step.md` whole when you write the
  entries (rows 1–3 of *Settlements to record*), and the skill of the element, `elements/decisions/skill/SKILL.md`
  (and the files it names, as its steps come), when you write or change a decision.
- Do not take the return step; the orchestrator dispatches it after the review.

## The task

- Frozen task, read whole: `C:\Storage\repos\the-way\.runs\task-cycles\cycle-remarks-batch-2\task.md`
  (original: `C:\Storage\The Brain\The Brain\Notes\Projects\(P) Proces pracy nad produktem\_zadania\zadanie_the_way_poprawki_z_uwag_cykli_2026_11_05.md`, ready for cycle, answers of 2026-11-05).
- No spec and no plan: the task leaves no open design choice. The *To do* items give the wording of
  each edit; copy it exactly where it gives a sentence. Where a quoted line number no longer matches
  the file, find the passage by its text and name the correction in your report.
- Rows 1–3 of *Settlements to record* are entries you write (WAY-134): row 1 a **new** decision
  (narrows WAY-22 and WAY-18, as the row and WAY-25 give); row 2 is the change to WAY-05 and row 3 the
  change to WAY-148, each edited in place, in the wording of *To do* 2 and 4. The two changes were
  approved with the task document (WAY-30).
- Answers to the questions at start: trust boundary — no; irreversible operation — no; open design
  choice — none; route — one author without a plan.

## What the orchestrator selected for you to read

Foundation entries, each whole, by identifier in `foundations/decisions.md`: WAY-05, WAY-18, WAY-22,
WAY-25, WAY-30, WAY-35, WAY-36, WAY-60, WAY-148, WAY-159, WAY-164, WAY-260; also the entries the
search of the foundation (WAY-33) finds, as `elements/common/way_of_working.md` "2. Search the foundation" gives it.
Parts touched: `decisions` and `task-cycle` (`foundations/part_map.md`). Templates and examples:
`elements/decisions/template.md` and `elements/decisions/examples.md`. The product's guidelines: none
(the-way has no `guidelines/` directory; the change is Markdown instructions only).

## Boundaries

- Do not change any skill's description; entry points (`agent-instructions/skill_entry_points.py`)
  need no regeneration.
- Out of scope: removing the counts of findings from the reviewer's message (task, *Out of scope*).
- Do not run the product's gate (`python -B gate/run_tests.py` with no argument) — that run is the
  orchestrator's. Run focused checks of the directories your edits touch
  (`python -B gate/run_tests.py <directory>`, for example `elements/decisions`, `elements/common`,
  `task-cycle`, `relation-model`) and the foundation form check,
  `elements/common/foundation_check.py`, as its usage gives. A full gate is running elsewhere on the
  base; do not start another.

## Your report

Write it to `C:\Storage\repos\the-way\.runs\task-cycles\cycle-remarks-batch-2\reports\02-author-report.md`
as the method gives it, with the commits, every check with its command and exit code, the own-work
check of the weakest point (WAY-164), the reaches beyond this handoff, the foundation entries marked
`row <n>` with their two meaning sentences, and the section **Searches not found or unclear**
(WAY-260; `none` is an answer, a missing section is not). Return the status, the commits, a one-line
check result naming what failed or did not run, and the report path.

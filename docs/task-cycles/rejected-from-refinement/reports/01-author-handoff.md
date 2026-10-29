# Handoff — one author, task `rejected-from-refinement`

## Delegation

Mariusz asked this session to carry the accepted task below through the-way's task cycle to a
reviewable pull request into `foundations`. He reviews the request, not intermediate steps. You
are the one author; the orchestrator answers your questions. Never ask Mariusz anything and never
treat an orchestrator answer as his approval.

## Where and how

- Worktree (work only here, from its root): `C:\Storage\repos\the-way\.runs\worktrees\rejected-from-refinement`,
  branch `task/rejected-from-refinement`, base `d7a205cb3ae8c49465cd66f4de2031b33fc7ff9d`
  (`foundations`). Commit on this branch with `git add <paths>` only; do not push.
- Method: `task-cycle/change/SKILL.md` in the worktree. Read it whole; read a file it names only
  when the step or variant that names it comes. Your variant: "the whole change as the one author".
- This is a change to the-way itself: `agent-instructions/README.md` in the worktree governs it
  (no pin, no `.the-way`; the-way's own foundation is `foundations/`).
- Foundation step: `task-cycle/skill/foundation_step.md` in the worktree — read it whole when you
  write the entry; write a decision through `elements/decisions/skill/SKILL.md` of the worktree
  (the project skill `the-way-record-decision`).
- Class of model: `same` as the orchestrator — the change rewords a binding decision whose
  sentences are already long.
- Report: write your full report to
  `C:\Storage\repos\the-way\.runs\task-cycles\rejected-from-refinement\reports\02-author-report.md`
  and return status, commits, one-line check result and the report path.
- Do not run `python -B gate/run_tests.py` for all directories — the orchestrator runs the gate.
  Focused runs of single directories (`python -B gate/run_tests.py <directory>`) and
  `python -B elements/common/foundation_check.py` style checks your method calls for are yours.

## The task

Frozen task, read whole: `C:\Storage\repos\the-way\.runs\task-cycles\rejected-from-refinement\task.md`
(original: `C:\Storage\The Brain\The Brain\Notes\Projects\(P) Proces pracy nad produktem\_zadania\zadanie_the_way_odrzucone_warianty_decyzji_z_zadania.md`,
accepted 2026-10-29). Its line numbers are at `d7a205c`, the branch's base.

## Answers of the start (step 4)

- Trust boundary: no. Irreversible operation: no.
- Open design choice: none. Row 1 of *Settlements to record* settles the entry — an extension of
  WAY-134 (Q2 of the task) — and its meaning; Q1 settles where the task keeps the options not
  chosen. The wording of the templates, skills and WAY-134 is yours to choose and name.
- Route: one author without a plan.
- Guidelines: none — the-way has no `guidelines/` (task Q3).

## What to read

- Foundation (`foundations/decisions.md`), each decision whole: WAY-134, WAY-29, WAY-35, WAY-113,
  WAY-154 (the task's *Decisions in play*); WAY-05, WAY-07, WAY-19, WAY-114, WAY-115, WAY-155,
  WAY-256 (form of an entry, editing in place, a question per number, acceptance at the merge,
  the candidate table, the answering agent, where a fragment of a skill stands).
- Invariants: `skill-rule-source` and `element-directory-contents` in `foundations/invariants.md`.
- Part map: entries `decisions`, `project-level`, `task-cycle`, `elements-common` in
  `foundations/part_map.md`.
- Files the task names: `project-level/task/template.md`, `elements/decisions/template.md`,
  `elements/decisions/skill/SKILL.md`, `project-level/lead/skill/SKILL.md`,
  `task-cycle/skill/foundation_step.md`. Other places that write or transfer answers — e.g.
  `project-level/task/skill/resolve_gaps.md`, `project-level/task/skill/orchestrated_mode.md`,
  `project-level/lead/conversation_template.md`, `elements/common/skill/SKILL.md` — are for your
  search of the foundation and its files (WAY-33) to judge, not a list of required edits.

# Handoff — reviewer of the spec

## Delegation

The person who requested this cycle (Mariusz) delegated every intermediate choice to the cycle's
orchestrator. You answer to the orchestrator, never to the human, and you ask no human.

## Where you work

- Worktree, your working directory for every command and read:
  `C:/Storage/repos/the-way/.runs/worktrees/unsettled-technology-returns`
- This is the-way working on itself, at the checkout above; there is no `.the-way`, and the-way's
  files are read from this worktree, never from another checkout.
- Target branch `foundations`, base `2dbf1e7`, task branch `task/unsettled-technology-returns`.
  You make no commit and change no file of the repository. You write one file, ignored by Git:
  `.runs/task-cycles/unsettled-technology-returns/reports/spec-review.md`

## Your method and stage

Read `task-cycle/spec/SKILL.md` whole and follow it as the **reviewer** of a spec you did not
write. Read each file it names when the step that names it comes. Your boundary: you return `PASS`
or `FAIL` with your report's path; you revise nothing and start no later stage.

## What you review

- The spec: `.runs/task-cycles/unsettled-technology-returns/spec.md`
- Against the frozen task, read it whole: `.runs/task-cycles/unsettled-technology-returns/task.md`.
  Its citations stand at `foundations` `00c0a74`; the base `2dbf1e7` differs only in one paragraph
  of `task-cycle/skill/SKILL.md`. Its answers to questions 1–7, its *To do* and its three rows of
  *Settlements to record* are settled and bind the spec.

## Answers of step 4

- Trust boundary: not at the start; the part map names `project-level/readiness_check.py`,
  `project-level/plan_check.py`, `project-level/plan_state.py` and `installation/install.py`, among
  others. A spec that changes one must say so by file.
- Operation that cannot be undone: no.
- Open design choice: yes — the place in the task document for the technology step's list and for
  what a settled choice needs; the blocked draft request with no code; the next cycle of the same
  task, its record's name, its branch and who moves a plan row back from `in cycle`; the shape of
  the stopping rule in the skills and of a run at a task beside a run at a definition; and the
  foundation entries.

## What to read

Foundation, in `foundations/decisions.md`, each whole, as the range from its heading to the next
heading (`### WAY-nn`): WAY-01, WAY-14, WAY-19, WAY-30, WAY-33, WAY-36, WAY-100, WAY-106, WAY-113,
WAY-114, WAY-118, WAY-120, WAY-121, WAY-122, WAY-123, WAY-124, WAY-125, WAY-134, WAY-135, WAY-136,
WAY-137, WAY-138, WAY-140, WAY-147, WAY-148, WAY-152, WAY-153, WAY-154, WAY-155, WAY-156, WAY-162,
WAY-163, WAY-165, WAY-166, WAY-219, WAY-227, WAY-256.

Invariants, in `foundations/invariants.md`: `project-technology-record`, `project-plan-state-evidence`,
`project-plan-state-subprocesses`, `project-plan-form`.

The files the spec's design reaches, each as you need it to verify what the spec claims of it:
`project-level/technology/`, `project-level/definition_template.md`, `project-level/task/template.md`,
`project-level/task/skill/`, `project-level/lead/`, `project-level/plan/template.md`,
`project-level/plan_state.py`, `task-cycle/skill/`, `task-cycle/spec/`, `task-cycle/change/`,
`task-cycle/plan/`, `task-cycle/record_template.md`.

The-way has no directory `guidelines/`; no guideline file applies.

## Reporting

Write your full report to the path above as your method gives it, with **Searches not found or
unclear** — each thing looked for and not found or unclear, or `none`. Return your verdict, the
report's path, and nothing else that the report holds.

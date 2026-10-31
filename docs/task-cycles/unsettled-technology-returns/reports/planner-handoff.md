# Handoff — planner

## Delegation

The person who requested this cycle (Mariusz) delegated every intermediate choice to the cycle's
orchestrator. You answer to the orchestrator, never to the human, and you ask no human.

## Where you work

- Worktree, your working directory for every command and read:
  `C:/Storage/repos/the-way/.runs/worktrees/unsettled-technology-returns`
- This is the-way working on itself, at the checkout above; there is no `.the-way`, and the-way's
  files are read from this worktree, never from another checkout.
- Target branch `foundations`, base `2dbf1e7`, task branch `task/unsettled-technology-returns`.
  You make no commit and change no file of the repository. You write three files, all ignored by
  Git:
  - the plan: `.runs/task-cycles/unsettled-technology-returns/plan.md`
  - its size report: `.runs/task-cycles/unsettled-technology-returns/plan-size.md`
  - your report: `.runs/task-cycles/unsettled-technology-returns/reports/planner.md`

## Your method and stage

Read `task-cycle/plan/SKILL.md` whole and follow it. Read each file it names when the step that
names it comes. Your boundary: you return before any slice is made.

## The task and the spec

- Frozen task, read it whole: `.runs/task-cycles/unsettled-technology-returns/task.md`. Its
  citations stand at `foundations` `00c0a74`; the base `2dbf1e7` differs only in one paragraph of
  `task-cycle/skill/SKILL.md`.
- Reviewed spec, read it whole: `.runs/task-cycles/unsettled-technology-returns/spec.md`. Its review
  reached the end of its rounds: nine findings resolved in one revision, and finding 10, left after
  it, settled by the orchestrator in the spec under decision 4, "One choice in two members of a
  round". The spec binds the plan. Its *Left to the maker* stays with the makers; the wording of
  every text is theirs.

## Answers of step 4

- Trust boundary: no. The spec changes no file the part map names as one, and reaches
  `project-level/test_plan_state.py` only by a test of behaviour that stands.
- Operation that cannot be undone: no.
- Both answers are no, so no slice is marked with a risk.

## The route's reason, for the division

The orchestrator judged that the change needs division: about 28 files across `project-level`,
`task-cycle`, `decisions`, `glossary` and `elements`, with three new decisions, six changed ones and
one glossary term. The natural seams of the spec are the technology step with the task template,
refinement, leading a project, and the cycle; that is what the orchestrator saw and not a division
you must keep. The plan's *Foundation entries* written first let the slices cite them.

A change to `project-level/technology/SKILL.md`'s description is followed by
`python -B agent-instructions/skill_entry_points.py --write`, its output committed by that slice.
The whole gate is the orchestrator's; a slice's *Checks* name focused checks only, such as
`python -B gate/run_tests.py project-level`, `python -B gate/run_tests.py agent-instructions` and
`python -B elements/common/foundation_check.py .`, each as it can actually run.

## Class of model

The default class for a slice is `cheaper`; a slice that writes across many parts or needs judgment
of wording against decisions carries its reason for `same`.

## What to read

- `agent-instructions/README.md`, which governs changes to the-way itself, and `AGENTS.md`.
- The files the spec names as changing, enough to size each slice.
- Foundation, in `foundations/decisions.md`, each whole, from its heading to the next: WAY-121,
  WAY-122, WAY-123, WAY-135, WAY-136, WAY-137, WAY-138, WAY-30, WAY-33, WAY-134, WAY-147, WAY-153,
  WAY-155, WAY-229, WAY-256, WAY-264. For each slice's *Read* name the entries of the parts it
  touches, by identifier.
- The-way has no directory `guidelines/`; no guideline file applies.

## Reporting

Write your full report to the path above as your method gives it, with **Searches not found or
unclear** — each thing looked for and not found or unclear, or `none`. Return your status, the
report's path, and a one-line check result naming what failed or did not run.

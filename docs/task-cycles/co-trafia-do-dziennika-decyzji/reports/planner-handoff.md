# Handoff — planner

## Delegation

The person who requested this cycle delegated intermediate choices to the orchestrator. You have no human to ask: return `questions` to the orchestrator. Never label an answer as the human's approval.

## Worktree and branch

Work from the root of `the root of the task's worktree`, branch `task/co-trafia-do-dziennika-decyzji`, base `ac753401de0bfaae0b9b8175c10c17387736f8d8` (the-way itself; no pin, so no check carried by a move of the pin). You write no code and no commit; you write `plan.md` and `plan-size.md` in the record's directory and your report.

## Method

Read whole `task-cycle/plan/SKILL.md` of the worktree (`plan-task`); read `task-cycle/plan/too_large.md` and any other file it names only when its step comes. Read no skill by calling it.

## Stage and boundary

Stage: the plan of slices, before any slice is made. Write `.runs/task-cycles/co-trafia-do-dziennika-decyzji/plan.md` and `plan-size.md` there. Return `done`, `done with concerns`, `questions`, `returned` or `reserved` as the method gives.

## Inputs

- Frozen task (read whole): `.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md`. Its 12 rows of *Settlements to record* are accepted and the plan covers every one; its *To do* points 1–9 each have a slice that makes them.
- The reviewed spec (read whole): `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md` (the spec before its one revision is `spec-reviewed.md`; do not plan from it). Its decisions D1–D9 are binding on the plan: the orchestrator's rulings of Q1–Q6 stand in it (switch `--skip-test-citations` skips only what WAY-321 names and WAY-321 stays; "changed" means the binding sentences; rows 11 and 12 become paragraphs of WAY-12 and WAY-03; the unknown-base line only where the log holds a decision; the pair-then-trim rule in step 3 of `elements/decisions/skill/SKILL.md` and in `task-cycle/skill/return_step.md`; a file missing at the base makes the base unknown). The spec names the foundation entries the change writes; the plan lists them in its *Foundation entries* where the method gives that section.
- Two wording notes of the spec's reviewer for the maker: keep the two bullets of step 3 of `elements/decisions/skill/SKILL.md` side by side with the reason D2 gives, and use WAY-268's own wording for "entered in the cycle record's questions table".
- The foundation: select by "Reading the foundation" in `elements/common/way_of_working.md` the entries each slice reads: the decisions of the task's *Decisions in play*, those the spec lists under "Other decisions of the log the change reaches", the invariants of the touched parts, the part map's entries of `decisions`, `elements-common`, `project-level`, `task-cycle`, `product-guidelines`, `agent-instructions`; the touched files whole. The orchestrator adds to each slice's *Read* what it finds missing.
- The product has no `guidelines/` directory; the-way's own checks are in `gate/run_tests.py` (the gate is the orchestrator's alone; a slice's *Checks* name focused checks such as `python -B gate/run_tests.py elements/common` and `python -B elements/common/foundation_check.py`, never a run of the whole gate).

## What the plan has to respect

- The foundation step's order: where the plan lists *Foundation entries*, they are written by one agent before slice 1, and slice 1's range starts at its base; a slice that writes a script's code and its tests keeps both in one slice.
- The slices are made one after another in the plan's order; a slice whose files the part map names as a trust boundary or that holds an operation that cannot be undone is marked so: the orchestrator found neither (`elements/common/foundation_check.py` is a surface, not a trust boundary; no trust-boundary file of `task-cycle/` or `project-level/` is among the files the spec names). If you find that a slice reaches a file the part map names as a boundary, say so.
- A change to a skill or a description runs `python -B agent-instructions/skill_entry_points.py --write` (see `AGENTS.md` of the worktree); the spec says whether a description changes; check it.

## Report

Write your full report to `.runs/task-cycles/co-trafia-do-dziennika-decyzji/reports/planner-report.md` as your method gives it, with the sections **Unread material** and **Searches not found or unclear** (each `none` where there is nothing). Return your status, a one-line result, the report path and your questions.

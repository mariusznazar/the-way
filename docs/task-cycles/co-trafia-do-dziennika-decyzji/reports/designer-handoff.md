# Handoff — designer of the spec

## Delegation

The person who requested this cycle delegated intermediate choices to the orchestrator of the cycle. You get no human to ask: put every question to the orchestrator by returning `questions`. Never label an answer as the human's approval.

## Worktree and branch

- Worktree (work from its root): `the root of the task's worktree`
- Branch `task/co-trafia-do-dziennika-decyzji`, base `ac753401de0bfaae0b9b8175c10c17387736f8d8` (the-way itself; no pin). You write no commit and no code; you write `spec.md` and your report only.

## Method

Read whole `task-cycle/spec/SKILL.md` of the worktree (`write-spec`), your variant: the designer of a spec. Read a file the method names, one beside that `SKILL.md` included, only when the step or variant that names it comes. Read no skill by calling it.

## Stage and boundary

Stage: the design of the spec of this task. The boundary: before any plan or code. Write the spec to `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md` (ignored directory of the record). Return `questions`, `done` or `reserved`.

## The task and its open design choices

- Frozen task (read whole): `.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md`. It carries 12 accepted rows of *Settlements to record* and six answered *Questions to settle*; these settle their entries and are not open: do not redesign them and never widen the task.
- The open design choices this spec settles are the three of *Questions carried to cycle*:
  1. How `elements/common/foundation_check.py` learns the state the branch left (points 7 and 8 of *To do*), without changing the path, the argument or the exit codes that the part map's `foundation-check-command` promises. Read how the-way already ties an invariant test to "the commit the branch left the main branch from" (WAY-65) and how the checker and its tests are written today.
  2. Which script lists an invariant whose sentence changed while its test did not (point 8), and where the request's description names it (`task-cycle/skill/request_template.md`, `task-cycle/request_check.py`).
  3. Whether the new column "dokąd idzie" replaces the column *Kind* of the table *Settlements to record* or stands beside it (`project-level/task/template.md`, `elements/common/skill/task_variant.md`, `elements/common/skill/build_table.md`), and the exact form of that column.
- Also settle whatever else the spec needs so that a planner and executors do not have to guess: the exact words of the five questions "dokąd to idzie", where each of points 1–9 of *To do* lands (file and section), the exact form of the line `decision: <number> "<quote>"`, how the checker reads it (which files count as tests, how a quote is compared to a sentence), and how points 7 and 8 are tested. Keep the-way's choice of question 1 (WAY-293 changed in part) as the task gives it.

## What to read

Foundation entries (read each whole, in `foundations/decisions.md`; locate by the heading `### WAY-NN`): WAY-36, WAY-293, WAY-11, WAY-134, WAY-19, WAY-05, WAY-12, WAY-22, WAY-03, WAY-02, WAY-65, WAY-168, WAY-167, WAY-171, WAY-172, WAY-173, WAY-26, and the decisions they link to as far as you need; plus the decisions whose *Scope* names `decisions`, `elements-common`, `project-level`, `task-cycle` or `product-guidelines` that bear on the log's form or on the task's table (search *Scope* lines). Part map: `foundations/part_map.md` (whole). Invariants whose *Part* names those parts or `every`, and the invariants that test cites by `invariant:` lines (`foundations/invariants.md`). Glossary: `foundations/glossary.md`.

Files the task names, each whole: `elements/decisions/template.md`, `elements/decisions/skill/decide_entry.md`, `elements/common/foundation_check.py` and `elements/common/test_foundation_check.py`, `project-level/task/template.md`, `elements/common/skill/task_variant.md`, `elements/common/skill/build_table.md`, `task-cycle/skill/return_step.md`, `task-cycle/skill/request_template.md`, `product-guidelines/template.md`, `elements/common/rules.md`.

The `.runs/` directory of other worktrees and the earlier cycles' records under `docs/task-cycles/` are not sources.

## Report

Write your full report to `.runs/task-cycles/co-trafia-do-dziennika-decyzji/reports/designer-report.md` as your method gives it, with the sections **Unread material** and **Searches not found or unclear** (each `none` where there is nothing). Return your status, a one-line result, the report path and your questions.

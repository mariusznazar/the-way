# Handoff — planner (stage: plan-task)

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator, and the
orchestrator answers your questions. Nothing here is that person's approval. Your questions go to the
orchestrator, never to the human.

## Where you work

- Worktree (work from its root, read every file from it, never from another checkout):
  `the worktree of the task`, branch `task/weekly-process-audit`,
  base commit `e3825a82386a61930a86f8517fc0c5f422fc2833`.
- The product is the-way itself, so there is no `.the-way` submodule: the method lives in the worktree.

## Method and stage

- Method: `task-cycle/plan/SKILL.md` of the worktree. Read it whole, and a file it names only when the
  step that names it comes.
- Stage: write the plan of slices for the change the task requires, and its size report. Write
  `plan.md` and `plan-size.md` in `docs/task-cycles/weekly-process-audit/`.
  You write no code and no foundation entry text; you return before any slice is made.
- Route: planning was selected at the start of the cycle (no spec: the task's rows of *Settlements to
  record* settle every decision; the shapes of the register template, of the command's output and of
  the keys in the locations file are ways of making what the task settles — leave each to the slice that
  makes it and have the slice name its choice in its report).

## Inputs

- Frozen task (whole): `.runs/task-cycles/weekly-process-audit/task.md`
  (copy of the task document, approved 2026-11-11). Its original path is in `cycle.md`, which you do not read.
- No spec. The move of the pin does not apply (the-way itself).

## Answers of the start

- Trust boundary: **yes**. The new part's counting command reads files from outside the repository
  (cycle records of repositories the user names, the register of problems, the price list, the locations
  file). The part-map entry of the new part names that command as a trust boundary. A slice that touches
  it is marked with this risk, so that it gets a review of its own that checks crafted input.
- Irreversible operation: **no**. Scheduling the command and adding the weekly backlog task are human
  actions the task places in the cycle; no slice performs them.
- Open design choice: none. Reserved choice: none.

## What to read of the foundation (selected by the orchestrator)

Decisions of `foundations/decisions.md` (range = heading to the next heading):
- the task's *Decisions in play*: WAY-09 (line 222), WAY-103 (2309), WAY-140 (3843), WAY-260 (7967),
  WAY-296 (9411), WAY-320 (10321);
- the part map and its assignment of files: WAY-40 (1044), WAY-41 (1070), WAY-42 (1092), WAY-44 (1116),
  WAY-48 (1192), WAY-49 (1222), WAY-21 (564);
- scripts and skills: WAY-38 (1018), WAY-89 (1991), WAY-127 (3177), WAY-125 (3094), WAY-148 (4141),
  WAY-150 (4209), WAY-229 (6711), WAY-255 (7743), WAY-256 (7776), WAY-265 (8114);
- backlog: WAY-101 (2263), WAY-107 (2410);
- planning: WAY-13 (403), WAY-134 (3449), WAY-135 (3558), WAY-136 (3601).

Invariants of `foundations/invariants.md`: `script-language` (106), `script-imports` (116),
`script-subprocesses` (126), `cross-part-imports` (328), `skill-entry-points` (261),
`repository-file-location` (26), `element-directory-contents` (36), `tracked-file-private-paths` (86),
`test-method-citation` (156), `map-reference-target` (146), `foundation-file-kinds` (6).

Whole short files: `foundations/part_map.md`, `foundations/glossary.md`.

Code the change touches or sits beside: `task-cycle/cycle_stages.py` and `task-cycle/test_cycle_stages.py`
(item 7 of the task), `task-cycle/record_template.md` (what an audit reads from a cycle record),
`task-cycle/remarks_check.py` (a command that reads records), `project-level/plan_state.py` (a command
of the same kind: reads a user's files, a trust boundary), `foundation-review/SKILL.md` (the existing
part the task says the new one resembles), `agent-instructions/skill_entry_points.py`, `gate/run_tests.py`.

Product guidelines: the-way has none (task *Questions to settle*: its missing guidelines do not hold
the task, WAY-215).

## Boundary and report

- Do not start a slice, edit a tracked file or commit.
- Report path: `docs/task-cycles/weekly-process-audit/reports\planner-report.md`.
- Return: your status, the report path, questions, concerns, each reach beyond this handoff, the
  **Unread material** (what this handoff names that stayed unread or was read in part, or `none`) and
  **Searches not found or unclear** (or `none`), all as your method gives them.

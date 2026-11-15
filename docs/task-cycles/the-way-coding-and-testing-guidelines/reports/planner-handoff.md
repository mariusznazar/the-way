# Handoff — planner of the task "the way: coding and testing guidelines of the-way itself"

You are the planner of this task cycle. The person who requested the cycle has delegated
intermediate choices to the orchestrator; nothing you or the orchestrator answers is that person's
approval. You do not write code. You write the plan and return before any slice is made.

## Where you work

- Worktree (work from its root): `the root of the worktree`,
  branch `task/the-way-coding-and-testing-guidelines`, base `2d593214e4ce11676880b1f3ac3aa75884e023ab`.
  This repository is the-way itself; there is no `.the-way` and no pin.
- Method of your stage: read `task-cycle/plan/SKILL.md` whole; read `task-cycle/plan/too_large.md`
  and any other file it names only when the step or variant that names it comes. Your variant:
  the plan of a ready task's change, before any slice is made.
- Your directory for working copies: `.runs/planner/` (create it only if you need a working copy).
- Write the plan to `.runs/task-cycles/the-way-coding-and-testing-guidelines/plan.md` and its size
  report to `.runs/task-cycles/the-way-coding-and-testing-guidelines/plan-size.md`, and your full
  report to `.runs/task-cycles/the-way-coding-and-testing-guidelines/reports/planner-report.md`.

## Working copies (word for word from the orchestrator's skill)

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
all the same and names in the report the remainder, with its full path and the reason it stayed.

## The task

The frozen task: `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md` (task document,
status `ready for cycle`, `Project relation: independent`, approved 2026-11-15, last commit of the
note `a05edac6`). Read it whole: its *To do* (20 items), its *Questions to settle* with answers
1–26, *Context*, *Human actions*, *Decisions in play*, *Settlements to record* (34 accepted rows)
and the list of causes of the audit (numbered 1–34) the *To do* items 12–20 take.

Answers of step 4 of the cycle (they bind the plan):

- Trust boundary: **yes**. The part map names `task-cycle/cycle_stages.py`,
  `task-cycle/cycle_measures.py`, `task-cycle/gate_times.py`, `process-audit/audit_count.py`,
  `project-level/readiness_check.py`, `project-level/plan_check.py`, `project-level/plan_state.py`,
  `instruction-files/check_instructions.py` and `installation/install.py` as trust boundaries. The
  change edits `task-cycle/cycle_stages.py` and `task-cycle/cycle_measures.py` and edits the tests
  of the refusals of the others. A slice whose files include a boundary file is marked with that
  risk, and so is a slice that adds the six invariants of the boundaries.
- Irreversible operation: **no**.
- Open design choice: **none** (every choice is settled by the task's answers and settlement rows).
- Reserved choice: **none** (Python, ruff 0.17.1 and its pin are settled in the task).
- Route: the orchestrator judged **planning** from the task: the change spans ten parts and is more
  than one agent can hold (WAY-136).

## What to read (the orchestrator's selection, WAY-150, WAY-213)

- Foundation entries by identifier, from `foundations/decisions.md`. The orchestrator's index of
  its selection (51 decisions in full) is `.runs/task-cycles/the-way-coding-and-testing-guidelines/decision_index_orchestrator.md`;
  read it, and open whole those the plan depends on. The decisions the task changes or withdraws
  and must be opened whole with *Rationale* and *Rejected*: WAY-328, WAY-09, WAY-38, WAY-344,
  WAY-363. The decisions the task's *Decisions in play* binds: WAY-14, WAY-16, WAY-48, WAY-51,
  WAY-167, WAY-168, WAY-172, WAY-173, WAY-198, WAY-199, WAY-202–WAY-206, WAY-212, WAY-215, WAY-216,
  WAY-231, WAY-232, WAY-235, WAY-240–WAY-242, WAY-247, WAY-252, WAY-253, WAY-312, WAY-360, WAY-361,
  WAY-365, WAY-372. Also relevant: WAY-55, WAY-63, WAY-89, WAY-160, WAY-228, WAY-233, WAY-234,
  WAY-238, WAY-243, WAY-244, WAY-254.
- `foundations/part_map.md` (whole), `foundations/glossary.md` (whole), `foundations/invariants.md`
  (the invariants of the parts the change touches and those it cites; the rest by identifier),
  `foundations/environment_facts.md` (the entries written in the form the element's skill gives,
  and `script-subprocesses` among the invariants, which rows 9 and 10 change).
- The templates the guidelines of the task are written from, whole: `product-guidelines/coding/template.md`,
  `product-guidelines/testing/template.md`, and the skills that lead those matters,
  `product-guidelines/coding/SKILL.md` and `product-guidelines/testing/SKILL.md` with the files they
  name where the step that names them comes. `product-guidelines/reading.md`, `product-guidelines/template.md`.
- The skills of the elements, read when a slice writes an entry of that element: `elements/decisions/`,
  `elements/invariants/`, `elements/glossary/`, `elements/environment-facts/`, `elements/part-map/`
  — each `SKILL.md`, template and `elements/common/rules.md`. The foundation step of the cycle
  is `task-cycle/skill/foundation_step.md`; read it, since the plan's *Foundation entries* are
  written by the agent it governs.
- Code and tests the task names: every file in its *To do* and in its list of causes. Read each
  place the task cites; line numbers are at `21ecb62`, and the base is later — find them again.
- The-way has no guidelines of its own yet (that is this task's output): no guideline file to read.
  `agent-instructions/README.md` is the instruction of the repository for this change.
- No trial of the full gate: the plan's slices name focused checks and no run of the gate
  (WAY-160). The gate is run by the orchestrator, once, on the finished change.

## Facts the orchestrator found while reading, for the plan

- The record of the orchestrator's cycle names the rule of the day advisor about the full gate; it
  is the orchestrator's and no slice runs the full gate.
- The checkout holds `.runs/` ignored; the quality environment `.runs/quality-venv` with
  `ruff 0.17.1` exists in the main checkout `<main checkout>` only (a human action done
  before the cycle). The tests of the linter invariant find it through `git rev-parse --git-common-dir`
  (answer 25); a slice that runs that test runs it from this worktree and relies on that lookup.
- The base's test of foundation (`elements/common/test_foundation_check.py`) and
  `python -B elements/common/foundation_check.py` check the form of the foundation; a slice that
  writes foundation entries runs the latter.
- Open requests may change the same files; this branch merges the target branch at step 12.

## What the plan must give

As `task-cycle/plan/SKILL.md` gives: slices in order, each with its *Change*, *Read*, *Checks*,
*Model*, *Risk* and *Choices*; the plan's *Foundation entries* (the entries of decisions,
invariants, glossary terms, environment facts and part-map lines the 34 settlement rows and the
changes of WAY-09, WAY-38, WAY-328, WAY-344, WAY-363 call for, with the invariant tests the
invariants cite) and the size report by the script of the method. The 34 rows of *Settlements to
record* must each be covered by a slice or by *Foundation entries*; the 20 items of *To do* each by
a slice; every cause of the audit that the task takes (1–6, 23, the cut of 17, and 26, 27, 30, 33)
by its slice. Divide by the order a reviewer can follow: the foundation entries before the files
that cite them, the linter's configuration before the invariant that runs it, the fixes of
existing code before the tests of the invariants that need them clean or marked violated, the six
guidelines of kinds after the exemplars they name are corrected. Keep an item of the task that the
plan cannot place as a stated gap, never as a silent omission.

## What you return

Your status, the plan's and the size report's paths, questions, and the report path, as the method
gives. Your report holds **Unread material** and **Searches not found or unclear** (`none` is an
answer). Return `reserved` or an open design choice only as the method gives; the orchestrator
does not expect either.

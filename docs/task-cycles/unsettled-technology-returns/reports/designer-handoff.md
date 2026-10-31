# Handoff — designer of the spec

## Delegation

The person who requested this cycle (Mariusz) delegated every intermediate choice to the cycle's
orchestrator. You answer to the orchestrator, never to the human, and you ask no human.

## Where you work

- Worktree, your working directory for every command and read:
  `C:/Storage/repos/the-way/.runs/worktrees/unsettled-technology-returns`
- This is the-way working on itself, at the checkout above; there is no `.the-way`, and the-way's
  files are read from this worktree, never from another checkout. Skills named below are this
  repository's files, listed here by path.
- Target branch `foundations`, base `2dbf1e7`, task branch `task/unsettled-technology-returns`.
  You make no commit and change no file of the repository. You write two files only, both ignored
  by Git:
  - the spec: `.runs/task-cycles/unsettled-technology-returns/spec.md`
  - your report: `.runs/task-cycles/unsettled-technology-returns/reports/designer.md`

## Your method and stage

Read `task-cycle/spec/SKILL.md` whole and follow it as the **designer**. Read each file it names
when the step that names it comes. Your boundary: you return with `questions` or `done`, before
any plan or code; you start no later stage.

## The task

Frozen task, read it whole: `.runs/task-cycles/unsettled-technology-returns/task.md`. It was copied
from the author's private notes on 2026-10-31, accepted there with `Status: ready for cycle`,
`Project relation: independent`. Its citations stand at `foundations` `00c0a74`; the current base
`2dbf1e7` differs from that commit only in `task-cycle/skill/SKILL.md` (a paragraph on where the
base checks run, step 4), so the line numbers it cites in that file moved by a few lines.

The task's answers to questions 1–7, its *To do* and its three rows of *Settlements to record* are
settled. They bind you; your spec does not reopen them.

## Answers of step 4

- Trust boundary: not at the start. The part map names `project-level/readiness_check.py`,
  `project-level/plan_check.py`, `project-level/plan_state.py` and `installation/install.py`,
  among others, as trust boundaries; the task names none of them. Where your design changes one of
  these, say so in the spec, by file, because the route and the reviews are judged again from it.
- Operation that cannot be undone: no.
- Open design choice: yes, the choices below.

## The choices this spec settles

The task leaves these open. Settle each, with the ways weighed.

1. **The place in the task document (To do 2 and 4).** The task's template
   `project-level/task/template.md` has no place for the technology step's list of choices and its
   progress, nor for what a settled choice needs: the options not chosen, the source of each
   difference between options, the lacks of the option chosen and the risks taken. Question 1's
   answer names *Questions to settle* and a row of *Settlements to record* as where the choice and
   the options not chosen go, and To do 4 says the template gets a place because none exists.
   Settle the form, how a resumed step finds its state in it, and how the cycle's writer of the
   decision reads it, under the rule of WAY-134 for a decision's rejected options. Reports under
   `.runs/technology/` are outside Git, so what must survive has to stand in the document.
2. **The blocked draft request with no code (carried question 1).** What it looks like when the
   discarded attempt leaves no code and the task branch holds only the pair of commits of the
   cycle's record: what the branch holds, how the request can open on it at all, and what the
   request states, against step 13 of `task-cycle/skill/SKILL.md`.
3. **The next cycle of the same task (carried question 2).** How the new cycle names its record
   given that the earlier one stands in history under that name (WAY-147, `docs/task-cycles/<name>/`,
   `task-cycle/skill/SKILL.md` step 5 and 12), what happens to its branch, and who moves a project
   plan's row back from `in cycle`. Read how `project-level/plan_state.py` reads a cycle trace and
   `project-level/lead/skill/SKILL.md` step 1: a row moved back while a trace of the earlier cycle
   stands in a ref may read as a conflict.
4. **The shape of the rule in the skills.** Where the stopping rule stands in `refine-task`, in the
   cycle and in the agents' methods (`task-cycle/spec/design.md`, `task-cycle/change/`,
   `task-cycle/plan/`), so that an agent that meets a reserved choice in any stage returns it, and
   the orchestrator's "smallest reversible reading" (`task-cycle/spec/design.md:15-16`,
   `task-cycle/skill/SKILL.md` around 184-186 and 211-213) no longer settles it; how the status of
   that return differs from an open design choice (WAY-135, row 3); and how the technology step's
   files (`project-level/technology/`) carry a run at a task beside a run at a definition, the
   skill's description included, without a second copy of the steps.
5. **The foundation entries.** Which rows become new decisions and which edit existing ones; each
   entry the change writes or changes, by kind and one sentence of meaning. Row 3 names the edits
   of WAY-121, WAY-122, WAY-123, WAY-137, WAY-138 and WAY-135. Where your search finds another entry
   the change makes untrue, name it.

Where a design would change the meaning of an approved decision beyond what the task document
carries (WAY-30), that is not yours or the orchestrator's to settle: name it as such, in your
questions, with a design that avoids it where one exists.

## What to read

Read whole, from the worktree:

- `task-cycle/spec/SKILL.md` and what it names when its step comes;
- `agent-instructions/README.md`, which governs changes to the-way itself, and `AGENTS.md`;
- `project-level/technology/` — every file; `project-level/definition_template.md`, section
  Technology;
- `project-level/task/template.md`, and of `project-level/task/skill/`: `SKILL.md`,
  `read_sources.md`, `resolve_gaps.md`, `carry_foundation.md`, `final_review.md`,
  `orchestrated_mode.md`, `project_plan_task.md`;
- `project-level/lead/skill/SKILL.md`, `project-level/lead/conversation_template.md`,
  `project-level/plan/template.md` (states), and `project-level/plan_state.py` as the choice 3 needs;
- `task-cycle/skill/SKILL.md`, `foundation_step.md`, `return_step.md`, `blocked_finding.md`,
  `correction.md`, `task-cycle/record_template.md`, `task-cycle/spec/design.md`, and the methods in
  `task-cycle/change/` and `task-cycle/plan/` as the choice 4 needs.

Foundation, in `foundations/decisions.md`, each whole, as the range from its heading to the next
heading (`### WAY-nn`): WAY-01, WAY-14, WAY-30, WAY-33, WAY-36, WAY-100, WAY-106, WAY-113, WAY-114,
WAY-118, WAY-120, WAY-121, WAY-122, WAY-123, WAY-124, WAY-125, WAY-134, WAY-135, WAY-136, WAY-137,
WAY-138, WAY-140, WAY-147, WAY-148, WAY-152, WAY-153, WAY-154, WAY-155, WAY-156, WAY-162, WAY-163,
WAY-165, WAY-166, WAY-219, WAY-227, WAY-256. The task's *Decisions in play* quotes what binds of
WAY-185, WAY-186, WAY-210, WAY-211, WAY-248 and WAY-249; read them where your design comes near them.

Invariants, in `foundations/invariants.md`: `project-technology-record`, `project-plan-state-evidence`,
`project-plan-state-subprocesses`, `project-plan-form`, and the invariant of a skill's entry points.

The-way has no directory `guidelines/`; no guideline file applies.

## Reporting

Write your full report to the path above as your method gives it, with **Searches not found or
unclear** — each thing looked for and not found or unclear, or `none`. Return your status, the
report's path, and nothing else that the report holds.

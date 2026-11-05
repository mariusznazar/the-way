# Handoff — reviewer of the spec

## Delegation

The person who requested this cycle (Mariusz) delegated every intermediate choice to the cycle's
orchestrator. You answer to the orchestrator, never to the human, and you ask no human. You did not
write the spec.

## Where you work

- Worktree, your working directory for every command and read:
  `C:/Storage/repos/the-way/.runs/worktrees/pr-description-schema`
- This is the-way working on itself; there is no `.the-way`, and the-way's files are read from this
  worktree, never from another checkout.
- Target branch `foundations`, base `f45ca40`, task branch `task/pr-description-schema`. You make no
  commit and change no file of the repository. You write one file, ignored by Git:
  `docs/task-cycles/pr-description-schema/reports/spec-review.md`.

## Your method and stage

Read `task-cycle/spec/SKILL.md` whole and follow it as the **reviewer** of the spec; read each file
it names when the step that names it comes. Your boundary: you return the first line of your report,
`PASS` or `FAIL`; you change no file but your report and start no later stage.

## What you review

- The spec: `docs/task-cycles/pr-description-schema/spec.md`, written by a designer of this cycle.
  The designer's report, for context on how it read its handoff:
  `docs/task-cycles/pr-description-schema/reports/designer.md`.
- Against the frozen task, read whole: `docs/task-cycles/pr-description-schema/task.md` (Polish;
  copied 2026-11-05, `Status: ready for cycle`, `Project relation: independent`, citations at
  `f45ca40`). Its *To do* 1–9, its answers under *Questions to settle* and its six rows of
  *Settlements to record* bind the spec; *Out of scope* holds screenshots' place and the weekly
  review of the archives' findings.
- The handoff the designer worked from, which names the choices the spec settles:
  `docs/task-cycles/pr-description-schema/reports/designer-handoff.md`.

## Answers of step 4

- Trust boundary: no at the start; the part map names none in `task-cycle`, `agent-instructions`
  or `decisions`.
- Operation that cannot be undone: no.
- Open design choice: yes, the choices of the designer's handoff.

## Foundation entries to review against

Read each whole in `foundations/decisions.md`, from its `###` heading to the next, with its rationale
and *Rejected*: WAY-03, WAY-10, WAY-14, WAY-35, WAY-36, WAY-49, WAY-51, WAY-114, WAY-134, WAY-135,
WAY-140, WAY-148, WAY-160, WAY-161, WAY-162, WAY-163, WAY-164, WAY-219, WAY-227, WAY-256, WAY-260,
WAY-261, WAY-268, WAY-269. Also `foundations/part_map.md` and `foundations/glossary.md`, whole (both
short), and `elements/decisions/template.md` for the form of a decision.

The files the spec changes or names, as far as you need them to judge it: `task-cycle/skill/SKILL.md`
(step 13, lines 390–425), `task-cycle/record_template.md` (*Request handoff*, 163–191),
`task-cycle/skill/correction.md`, `task-cycle/skill/foundation_step.md`,
`task-cycle/skill/reserved_return.md`, `task-cycle/skill/blocked_finding.md`,
`agent-instructions/README.md`, `project-level/test_plan_state_invariant.py:186`, and the nightly
digest `C:\Storage\The Brain\The Brain\Notes\Areas\(A) Claude code\scripts\cycle_remarks_digest.py`
(`extract_remark_blocks`, around line 240), whose cutting of "Process remarks" blocks the change must
not break.

## Your report

Write `reports/spec-review.md` as your method gives it, with each reach beyond this handoff and
**Searches not found or unclear** — each thing looked for and not found or unclear, or `none`.
Return its first line and its path.

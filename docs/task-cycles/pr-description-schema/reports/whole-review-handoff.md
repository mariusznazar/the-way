# Handoff — reviewer of the whole change

## Delegation

The person who requested this cycle (Mariusz) delegated every intermediate choice to the cycle's
orchestrator. You answer to the orchestrator, never to the human, and you ask no human. You made
none of this change.

## Where you work

- Worktree, your working directory for every command and read:
  `C:/Storage/repos/the-way/.runs/worktrees/pr-description-schema`
- This is the-way working on itself; there is no `.the-way`, and the-way's files are read from this
  worktree, never from another checkout. `agent-instructions/README.md` governs changes to the-way
  before `main`.
- Read-only: you commit nothing and change no tracked file. You write one file, ignored by Git:
  `docs/task-cycles/pr-description-schema/reports/whole-review.md`.
- The orchestrator runs the full test run (`python -B gate/run_tests.py`) in this worktree while you
  review; do not run it yourself, and do not move HEAD. Focused runs of one directory
  (`python -B gate/run_tests.py task-cycle`, `elements/common`, `project-level`,
  `agent-instructions`) and `python -B elements/common/foundation_check.py .` are yours where your
  review needs them.

## Your method and stage

Read `task-cycle/review/SKILL.md` whole and follow it, for **the whole change**; read each file it
names when the step that names it comes. You select your own foundation entries by the parts the
change touches, as your method gives. Your boundary: your report's first line, `PASS <sha>`,
`FAIL <sha>` or `questions`.

## What you review

- Range: `f45ca40..5b685df` on `task/pr-description-schema` — three commits, `609a92f`
  (foundation), `d1d57db` (template, script, tests), `5b685df` (the cycle's files and
  `agent-instructions/README.md`). One author without a plan; no slice.
- The frozen task, read whole: `docs/task-cycles/pr-description-schema/task.md` (Polish; copied
  2026-11-05, `Status: ready for cycle`, `Project relation: independent`, citations at `f45ca40`).
  Its *To do* 1–9, its answers, its six rows of *Settlements to record* and its one *Questions
  carried to cycle* bind the change; *Out of scope*: the place of screenshots and test artifacts,
  the weekly review of the archives' findings.
- The reviewed spec: `docs/task-cycles/pr-description-schema/spec.md`. Its D10 was settled by the
  orchestrator after the spec's review left two findings
  (`docs/task-cycles/pr-description-schema/reports/spec-review-2.md`); where the spec and D10
  differ, D10 holds.
- The author's report: `docs/task-cycles/pr-description-schema/reports/author.md`.

## Answers of step 4

- Trust boundary: no. The part map names none in the parts this change touches; the new script
  reads only the description file and the task document the cycle gives it.
- Operation that cannot be undone: no.
- No user interface.

## Outside the repository

The nightly digest
`C:\Storage\The Brain\The Brain\Notes\Areas\(A) Claude code\scripts\cycle_remarks_digest.py`
(`extract_remark_blocks`, around line 240) cuts every "Process remarks" block out of committed
cycle records; the task's *Context* requires that the change to the record template not lose it.
Read it to judge that; it is not part of the change.

## Your report

Write `reports/whole-review.md` as your method gives it — graded findings with their places in the
code, coverage of every *To do* item, settlement row and carried question, source fidelity, the
checks you ran with command and exit code, what you declined to judge, each reach beyond this
handoff, and **Searches not found or unclear**, or `none`. Return its first line and its path.

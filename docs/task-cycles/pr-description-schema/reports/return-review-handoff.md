# Handoff — reviewer of the return step

## Delegation

The person who requested this cycle (Mariusz) delegated every intermediate choice to the cycle's
orchestrator. You answer to the orchestrator, never to the human, and you ask no human. You made
none of this change.

## Where you work

- Worktree, your working directory for every command and read:
  `C:/Storage/repos/the-way/.runs/worktrees/pr-description-schema`
- This is the-way working on itself; there is no `.the-way`, and the-way's files are read from this
  worktree, never from another checkout.
- Read-only: you commit nothing and change no tracked file. You write one file, ignored by Git:
  `docs/task-cycles/pr-description-schema/reports/return-review.md`. Do not run the full gate
  (`python -B gate/run_tests.py` with no argument); focused runs of one directory and
  `python -B elements/common/foundation_check.py .` are yours where your review needs them.

## Your method and stage

Read `task-cycle/review/SKILL.md` whole and follow it, for **the return step's commits**; read each
file it names when the step that names it comes. Your boundary: your report's first line,
`PASS <sha>`, `FAIL <sha>` or `questions`.

## What you review

- Range: `4327974..e6f24b0`, one commit, the return step of the one author, against the task and the
  entries the return step writes or corrects: a new environment fact `github-collapsed-section`
  with WAY-288's *Based on* naming it; WAY-292 narrowed to "wherever it reads the task document as
  English"; the 9.4 stop and step 12 of `task-cycle/skill/SKILL.md` and
  `task-cycle/skill/blocked_finding.md` naming `task-cycle/skill/request_template.md`.
- The return step's report: `docs/task-cycles/pr-description-schema/reports/return-step.md`.
- What the return step does: `task-cycle/skill/return_step.md`.
- The change it follows: `f45ca40..4327974`, reviewed `PASS 4327974`
  (`docs/task-cycles/pr-description-schema/reports/whole-review.md`, then `whole-review-2.md`).
  Its unfixed Minor findings M-1 to M-5 stand; you judge only this range.
- The frozen task, as far as you need it: `docs/task-cycles/pr-description-schema/task.md`
  (Polish; *To do* 1–9, six rows of *Settlements to record*). The reviewed spec, as far as you need
  it: `docs/task-cycles/pr-description-schema/spec.md`.

## Answers of step 4

- Trust boundary: no. Operation that cannot be undone: no. No user interface.

## Your report

Write `reports/return-review.md` as your method gives it — graded findings with their places, the
checks you ran with command and exit code, what you declined to judge, each reach beyond this
handoff, and **Searches not found or unclear**, or `none`. Return its first line and its path.

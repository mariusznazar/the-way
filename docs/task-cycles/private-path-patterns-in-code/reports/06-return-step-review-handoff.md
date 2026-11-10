# Handoff 06 — review of the return step's commits

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator. You did
not make this change. You are read-only: you write only your report. Questions go to the
orchestrator as a report with first line `questions`.

## Where you work

- Worktree (your working directory, the process root): `the task's worktree root`
- Branch `task/private-path-patterns-in-code`; target branch `foundations`.
- The method of your stage is `task-cycle/review/SKILL.md` in this worktree: read it whole and follow
  it. Your variant is "the return step's commits": section 2 of the method gives how they are
  reviewed, against the task and the foundation entries the return step writes or corrects.

## What you review

- Range: base `578a8bd` (the head of the fix, already reviewed `PASS`), head `3057f16`; compute the
  diff yourself. It holds two edits of `foundations/`: one sentence added to WAY-324 and a new
  surface entry `tracked-private-paths-command` in `foundations/part_map.md`.
- The return step's method (what it compares and writes): `task-cycle/skill/return_step.md`; the
  agent's report, a set of claims to verify: `.runs/task-cycles/private-path-patterns-in-code/reports/05-return-step-report.md`.
- The task (frozen): `.runs/task-cycles/private-path-patterns-in-code/task.md`. Pass to read in it:
  *To do* 4–6, question 4 and the third row of *Settlements to record*.
- Foundation entries, each whole: `foundations/decisions.md` WAY-324 (from its `###` heading to the
  next), WAY-49 and WAY-37 (what a surface entry is and what entries wait for), WAY-44 (assignment of
  files to parts); `foundations/part_map.md` entries `test-runner-command`, `installation-command`
  and the new `tracked-private-paths-command`; the command itself,
  `task-cycle/tracked_private_paths_check.py`, whole, to compare the two sentences and the surface
  entry with the code.
- The cycle's recorded reading of the entry: the orchestrator chose to write the surface entry (a
  product relies on the command's path, argument, exit codes). You may find that choice wrong.

## Checks you may run

Focused only: `python -B elements/common/foundation_check.py`,
`python -B gate/run_tests.py elements/part-map` and the new command on this repository. Not the
whole gate (the orchestrator runs it). Do not change a tracked file.

## Report

Write the full report to `.runs/task-cycles/private-path-patterns-in-code/reports/06-return-step-review-report.md`
as the method gives it, with the first line `PASS <sha>` or `FAIL <sha>`, graded findings with
`file:line`, the checks with command and exit code, and **Searches not found or unclear** (`none` is
an answer). Return the first line, your checks in one line and the report's path.

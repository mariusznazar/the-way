# Handoff — review of the whole change, task `rejected-from-refinement`

## Delegation

Mariusz asked this session to carry the accepted task below through the-way's task cycle to a
reviewable pull request into `foundations`; he reviews the request, not intermediate steps. You
review the whole change as an agent that made none of it. Never ask Mariusz anything; questions go
to the orchestrator.

## Where and how

- Worktree (read only, from its root): `C:\Storage\repos\the-way\.runs\worktrees\rejected-from-refinement`,
  branch `task/rejected-from-refinement`.
- Method: `task-cycle/review/SKILL.md` in the worktree. Read it whole; read a file it names only
  when the step or variant that names it comes. You review the whole change.
- This is a change to the-way itself: `agent-instructions/README.md` in the worktree governs it
  (no pin; the-way's own foundation is `foundations/`). The review checks the change against the
  task, the foundation entries it touches, and the rules of the element templates.
- Range: `d7a205cb3ae8c49465cd66f4de2031b33fc7ff9d..1267e73` (one commit, one author, no plan, no
  spec, no slices).
- Changed files (added/removed lines): `foundations/decisions.md` 45/22 (WAY-134, WAY-154),
  `elements/decisions/template.md` 9/1, `project-level/task/template.md` 15/5,
  `project-level/lead/conversation_template.md` 8/5, `project-level/lead/skill/SKILL.md` 5/3,
  `elements/common/skill/SKILL.md` 4/2, `task-cycle/skill/foundation_step.md` 4/2,
  `project-level/task/skill/resolve_gaps.md` 3/1, `project-level/task/skill/final_review.md` 2/1,
  `project-level/task/skill/orchestrated_mode.md` 2/1.
- Report: write your full report to
  `C:\Storage\repos\the-way\.runs\task-cycles\rejected-from-refinement\reports\04-review-report.md`;
  its first line is `PASS <sha>`, `FAIL <sha>` or `questions`. Return that first line, the report
  path and a one-line check result.
- Do not run the full gate (`python -B gate/run_tests.py` with no directory) — the orchestrator
  runs it. Focused checks your method calls for are yours.

## Answers of the start (step 4)

- Trust boundary: no. Irreversible operation: no.
- Open design choice: none — row 1 of *Settlements to record* settles the entry (an extension of
  WAY-134, the task's Q2) and its meaning; Q1 settles where the task keeps the ways not chosen.
- Route: one author without a plan, class `same`.
- Guidelines: none — the-way has no `guidelines/` (task Q3).

## Inputs

- Frozen task, read whole: `C:\Storage\repos\the-way\.runs\task-cycles\rejected-from-refinement\task.md`
  (line numbers in it are at the base `d7a205c`).
- Author's report: `C:\Storage\repos\the-way\.runs\task-cycles\rejected-from-refinement\reports\02-author-report.md`.
- You select your own foundation reading for the parts of the change, by "Reading the foundation"
  in `elements/common/way_of_working.md`. The task's *Decisions in play* are WAY-134, WAY-29,
  WAY-35, WAY-113 and WAY-154.

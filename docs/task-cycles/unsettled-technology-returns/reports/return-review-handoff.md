# Handoff — reviewer of the return step

## Delegation

The person who requested this cycle (Mariusz) delegated every intermediate choice to the cycle's
orchestrator. You answer to the orchestrator, never to the human, and you ask no human. You made
none of this change.

## Where you work

- Worktree, your working directory for every command and read:
  `C:/Storage/repos/the-way/.runs/worktrees/unsettled-technology-returns`
- This is the-way working on itself; the-way's files are read from this worktree.
- Review is read-only: you change no file of the repository and make no commit. You run no gate;
  that run is the orchestrator's, and it runs on this head while you read. Your report:
  `.runs/task-cycles/unsettled-technology-returns/reports/return-review.md`

## Your method

Read `task-cycle/review/SKILL.md` whole and follow it, as the review of the return step, and read a
file it names when the step that names it comes. Your report's first line is `PASS <sha>`, `FAIL
<sha>` or `questions`.

## What you review

The range `9849f4b..6f34b64` on `task/unsettled-technology-returns`, one commit by the agent of the
return step. Its report: `.runs/task-cycles/unsettled-technology-returns/reports/return.md`.

Review it against the frozen task,
`.runs/task-cycles/unsettled-technology-returns/task.md`, and the entries the return step writes or
corrects: the new environment fact `github-closed-pull-request-branch` in
`foundations/environment_facts.md`, and WAY-267 in `foundations/decisions.md`. The form of a fact
stands in `elements/environment-facts/`, and WAY-90 and WAY-84 say what enters as a fact. The return
step's rules stand in `task-cycle/skill/return_step.md` and `task-cycle/skill/foundation_step.md`.

Earlier reviews of this change passed `2dbf1e7..9849f4b`; you do not review that range again.

## Answers of step 4

- Trust boundary: no.
- Operation that cannot be undone: no.

## Reporting

Write your full report to the path above as your method gives it, with each check's command and exit
code, and **Searches not found or unclear** — each thing looked for and not found or unclear, or
`none`. Return your report's first line, a one-line check result naming what failed or did not run,
and the report's path.

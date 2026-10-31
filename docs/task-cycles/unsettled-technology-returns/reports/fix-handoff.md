# Handoff — the fix of the review's findings

## Delegation

The person who requested this cycle (Mariusz) delegated every intermediate choice to the cycle's
orchestrator. You answer to the orchestrator, never to the human, and you ask no human.

## Where you work

- Worktree, your working directory for every command and read:
  `C:/Storage/repos/the-way/.runs/worktrees/unsettled-technology-returns`
- This is the-way working on itself; there is no `.the-way`, and the-way's files are read from this
  worktree, never from another checkout.
- Task branch `task/unsettled-technology-returns`, reviewed head `e21d286`, the current head; your
  range runs from it. Nothing else writes in this worktree while you work.
- Commit on the task branch by explicit paths (`git add <path>`, never `git add -A`, `git add .` or
  `git commit -a`), in English, in the form of the repository's log (`docs: ...`). Do not push.
- Your report: `.runs/task-cycles/unsettled-technology-returns/reports/fix.md`

## Your method and variant

Read `task-cycle/change/SKILL.md` whole and follow it, in the variant **the fix of a review's
findings**. Read a file it names when the step that names it comes. Your boundary: you fix these
findings, run the affected checks and return. You run no gate; that run is the orchestrator's.

The session's global rule on knowledge artifacts applies: a skill or entry says how things are, with
no history of attempts and no dates of events.

## What you fix

The findings file, read it whole:
`.runs/task-cycles/unsettled-technology-returns/reports/whole-review-findings.md`. It holds the three
blocking findings in the reviewer's words. You fix these three, finding 2's *Also* included, and no
Minor finding. Where you hold a finding wrong, answer it with evidence in your report.

The whole frozen task and spec are there for what the findings cite:
`.runs/task-cycles/unsettled-technology-returns/task.md` and
`.runs/task-cycles/unsettled-technology-returns/spec.md`. The spec's decisions 1, 3 and 5 are the
ones the findings touch. Finding 3 changes only WAY-267, an entry this change writes: use the skill
`the-way-record-decision` in `.claude/skills/` for it, and keep it to what the finding names. An edit
that would change the meaning the spec gives beyond this returns as `blocked`, as
`task-cycle/skill/foundation_step.md` gives.

The-way has no directory `guidelines/`; no guideline file applies.

## Reporting

Write your full report to the path above as your method gives it, each check with its command and
exit code, run with no pipe, and **Searches not found or unclear** — each thing looked for and not
found or unclear, or `none`. At least run `python -B elements/common/foundation_check.py .`,
`python -B gate/run_tests.py project-level`, `python -B gate/run_tests.py task-cycle` and
`python -B instruction-files/check_instructions.py . --file project-level/technology/task_run.md`.
Return your status, your commits, a one-line check result naming what failed or did not run, and
the report's path.

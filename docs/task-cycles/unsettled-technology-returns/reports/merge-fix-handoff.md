# Handoff — the fix of the reconciliation's findings

## Delegation

The person who requested this cycle (Mariusz) delegated every intermediate choice to the cycle's
orchestrator. You answer to the orchestrator, never to the human, and you ask no human.

## Where you work

- Worktree, your working directory for every command and read:
  `C:/Storage/repos/the-way/.runs/worktrees/unsettled-technology-returns`
- This is the-way working on itself; there is no `.the-way`, and the-way's files are read from this
  worktree, never from another checkout.
- Task branch `task/unsettled-technology-returns`, reviewed head `c69e355`, the current head; your
  range runs from it. Nothing else writes in this worktree while you work.
- Commit on the task branch by explicit paths (`git add <path>`, never `git add -A`, `git add .` or
  `git commit -a`), in English, in the form of the repository's log (`docs: ...`). Do not push.
- Your report: `.runs/task-cycles/unsettled-technology-returns/reports/merge-fix.md`

## Your method and variant

Read `task-cycle/change/SKILL.md` whole and follow it, in the variant **the fix of a review's
findings**. Read a file it names when the step that names it comes. Your boundary: you fix these
findings, run the affected checks and return. You run no gate; that run is the orchestrator's.

The session's global rule on knowledge artifacts applies: a skill says how things are, with no history
of attempts and no dates of events.

## What you fix

The findings file, read it whole:
`.runs/task-cycles/unsettled-technology-returns/reports/merge-review-findings.md`. It holds the three
blocking findings in the reviewer's words, with their shared ground. You fix these three and no Minor
finding: `project-level/task/skill/SKILL.md`, `task-cycle/spec/SKILL.md` and
`task-cycle/skill/SKILL.md`. Where you hold a finding wrong, answer it with evidence in your report.

Read WAY-265, WAY-256 and WAY-268 whole in `foundations/decisions.md`. A condition named in a
`SKILL.md` reads as the condition in the step's file, since the file stands in two places that must
be kept equal. Do not move a check or a rule out of its file; WAY-256 keeps the fragments where they
stand, and the pointer is all that is added. No frontmatter changes, so no entry point changes.

The task, for what the findings cite:
`.runs/task-cycles/unsettled-technology-returns/task.md`. The-way has no directory `guidelines/`.

## Reporting

Write your full report to the path above as your method gives it, each check with its command and exit
code, run with no pipe, and **Searches not found or unclear** — each thing looked for and not found or
unclear, or `none`. At least run `python -B elements/common/foundation_check.py .`,
`python -B agent-instructions/skill_entry_points.py`,
`python -B gate/run_tests.py task-cycle` and `python -B gate/run_tests.py project-level`.
Return your status, your commits, a one-line check result naming what failed or did not run, and
the report's path.

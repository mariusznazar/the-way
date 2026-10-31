# Handoff — the agent of the return step

## Delegation

The person who requested this cycle (Mariusz) delegated every intermediate choice to the cycle's
orchestrator. You answer to the orchestrator, never to the human, and you ask no human.

## Where you work

- Worktree, your working directory for every command and read:
  `C:/Storage/repos/the-way/.runs/worktrees/unsettled-technology-returns`
- This is the-way working on itself; there is no `.the-way`, and the-way's files are read from this
  worktree, never from another checkout.
- Task branch `task/unsettled-technology-returns`, base `2dbf1e7`, reviewed head `9849f4b`, the
  current head. Nothing else writes in this worktree while you work.
- Commit on the task branch by explicit paths (`git add <path>`, never `git add -A`, `git add .` or
  `git commit -a`), in English, in the form of the repository's log (`docs: ...`). Do not push.
- Your report: `.runs/task-cycles/unsettled-technology-returns/reports/return.md`

## Your stage

You take the return step, as a fresh agent; you take none of the rows of the table of variants in
`make-change`. Read whole, in the worktree:

- `task-cycle/change/SKILL.md`, the method for how you read, commit and report;
- `task-cycle/skill/return_step.md`, what you compare and write;
- `task-cycle/skill/foundation_step.md`, since the return step writes as the foundation step writes.

Read the skill of an element when you write an entry of that element, each in `.claude/skills/`:
`the-way-record-decision`, `the-way-record-glossary-term`, `the-way-record-environment-fact`,
`the-way-update-part-map`. `agent-instructions/README.md` adds its own account of the return step for
a change to the-way itself. You run no gate; that run is the orchestrator's.

The session's global rule on knowledge artifacts applies to what you write.

## What you compare

- The frozen task: `.runs/task-cycles/unsettled-technology-returns/task.md`, its *Decisions in play*,
  its rows of *Settlements to record* and its *Questions carried to cycle*.
- The entries this change writes or changes: WAY-121, WAY-122, WAY-123, WAY-135, WAY-137, WAY-138,
  WAY-265, WAY-266, WAY-267 and the glossary term `reserved choice`. The search of the whole
  foundation found WAY-114, by `narrows WAY-114` on WAY-266, and WAY-160, by a clause of WAY-267's
  *Rationale*; `reports/foundation.md` gives what it searched and found.
- The part map's entries of the touched parts: `project-level`, `task-cycle`, `decisions`, `glossary`,
  `agent-instructions` and `elements-common` where a file of it changed.
- The files of the change, `git diff --name-only 2dbf1e7..9849f4b`, with the skills the entries
  describe: `project-level/technology/`, `project-level/task/`, `project-level/lead/`,
  `task-cycle/skill/`, `task-cycle/change/`, `task-cycle/plan/`, `task-cycle/spec/`,
  `task-cycle/review/`, `task-cycle/record_template.md`.
- `task-cycle/record_template.md` and `.runs/task-cycles/unsettled-technology-returns/spec.md` for
  the choices that bind after the merge.

WAY-267 cites a page of GitHub's documentation in *Based on*; judge whether that source is held as
the foundation requires.

The review's Minor findings are not fixed here: they go to the request, and they are no foundation
entries. A correction of an entry that would change the meaning of an approved decision beyond what
the task and the spec carry returns as `blocked`, as `foundation_step.md` gives.

## Reporting

Write your full report to the path above, by the fields of the record's *Return step*: foundation
compared with code, decisions written or changed, invariants, environment facts, glossary terms,
part-map changes, projected entries, rows written, each row by its number and identifier. Where you
write or change an entry, keep one sentence of its meaning in Polish, the task document's language.
Add each check's command and exit code, run with no pipe, at least
`python -B elements/common/foundation_check.py .`, and **Searches not found or unclear** — each thing
looked for and not found or unclear, or `none`. Return your status, your commits or that there are
none, a one-line check result naming what failed or did not run, and the report's path.

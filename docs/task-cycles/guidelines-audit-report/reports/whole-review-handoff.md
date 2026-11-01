# Handoff — reviewer of the whole change

## Delegation

The person who requested this cycle (Mariusz) delegated every intermediate choice to the cycle's
orchestrator. You answer to the orchestrator, never to the human, and you ask no human.

## Where you work

- Worktree, your working directory for every command and read:
  `C:/Storage/repos/the-way/.runs/worktrees/guidelines-audit-report`
- This is the-way working on itself, at the checkout above; there is no `.the-way`, and the-way's
  files are read from this worktree, never from another checkout.
- Target branch `foundations`, task branch `task/guidelines-audit-report`. You change no tracked file
  and make no commit. Your report: `.runs/task-cycles/guidelines-audit-report/reports/whole-review.md`,
  ignored by Git.

## Your method and stage

Read `task-cycle/review/SKILL.md` whole and follow it for the review of **the whole change**: read
`task-cycle/review/whole_change.md` when it names it, and each other file when the step that names
it comes. You made none of this change. You alone select your own foundation and guidelines.
Your boundary: you return your report's first line, `PASS <sha>`, `FAIL <sha>` or `questions`.

## What you review

- Range: base `2f51e6c`, head `0ee0cd9`. One author, no plan, so this is the review of the whole
  change and no slice stands apart.
- Frozen task, read it whole: `.runs/task-cycles/guidelines-audit-report/task.md`. Its citations stand
  at `foundations` `2f51e6c`, the base. Read no skill of the course it names.
- Reviewed spec: `.runs/task-cycles/guidelines-audit-report/spec.md`, which passed its review in
  `reports/spec-review-2.md` in the same directory. It settles the choices the task left open under
  its decisions 1 to 14, and names six new entries with WAY-187, WAY-201 and WAY-250 changed.
- Author's report: `.runs/task-cycles/guidelines-audit-report/reports/author.md`.

Coverage to check: every item of the task's *To do*, each of its six rows of *Settlements to record*,
its four *Questions carried to cycle*, and its answers to questions 1 to 9. The task carries no
projected entry.

The change is prose and foundation entries. Its readers are agents following them: a session leading
a product's guidelines through an audit at setting up, refreshing and extending, in each of the three
skills, alone and in a task joining code and tests, and in orchestrated mode, and the session of
`refine-task` it hands back to. Read them as those agents would, following each step's pointer to the
file it names. An agent's way of acting on this text was not tried by anyone in this cycle.

The review of the spec judged the words `grave`, `heavy`, `medium` and `light`, `finding` and `cause`
and the reading of WAY-247; they are the spec's, and they stand as evidence, not as a limit on what
you judge.

## Answers of step 4

- Trust boundary: no. No file the part map names as one changes.
- Operation that cannot be undone: no.

The-way has no `guidelines/` directory of its own, so no guideline file applies.

## Your return

Write the report as the method gives, its first line `PASS 0ee0cd9` or `FAIL 0ee0cd9`, with
**Searches not found or unclear**, and return only that first line, the counts of blocking, Minor and
out-of-scope findings, and the report's path.

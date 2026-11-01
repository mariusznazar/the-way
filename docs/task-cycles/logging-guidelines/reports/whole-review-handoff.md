# Handoff — reviewer of the whole change

## Delegation

The person who requested this cycle (Mariusz) delegated every intermediate choice to the cycle's
orchestrator. You answer to the orchestrator, never to the human, and you ask no human.

## Where you work

- Worktree, your working directory for every command and read:
  `C:/Storage/repos/the-way/.runs/worktrees/logging-guidelines`
- This is the-way working on itself, at the checkout above; there is no `.the-way`, and the-way's
  files are read from this worktree, never from another checkout.
- Target branch `foundations`, task branch `task/logging-guidelines`. You change no tracked file and
  make no commit. Your report: `.runs/task-cycles/logging-guidelines/reports/whole-review.md`,
  ignored by Git.

## Your method and stage

Read `task-cycle/review/SKILL.md` whole and follow it for the review of **the whole change**: read
`task-cycle/review/whole_change.md` when it names it, and each other file when the step that names
it comes. You made none of this change. You alone select your own foundation and guidelines.
Your boundary: you return your report's first line, `PASS <sha>`, `FAIL <sha>` or `questions`.

## What you review

- Range: base `ea4694e`, head `1740c02`. One author, no plan, so this is the review of the whole
  change and no slice stands apart.
- Frozen task, read it whole: `.runs/task-cycles/logging-guidelines/task.md`. Its citations stand at
  `foundations` `ea4694e`, the base.
- Reviewed spec: `.runs/task-cycles/logging-guidelines/spec.md`, which passed its review in
  `reports/spec-review-2.md` in the same directory. It settles the choices the task left open, under
  its D1 to D9, and names nine entries, E1 to E9.
- Author's report: `.runs/task-cycles/logging-guidelines/reports/author.md`.

Coverage to check: every item of the task's *To do*, each of its eight rows of *Settlements to
record*, its *Questions carried to cycle*, and its answers 1 to 12 with the marks of which answer
replaces which. The task carries no projected entry.

The change is prose and foundation entries. Its readers are agents following them: the author of a
product's coding guidelines reading the template, the skill leading a human at the first guidelines,
at an extension and at a refresh that finds the rules missing, and a reviewer of a product's change.
Read them as those agents would. An agent's way of acting on this text was not tried by anyone in this
cycle; the author says so in its report.

## Answers of step 4

- Trust boundary: no. No file the part map names as one changes.
- Operation that cannot be undone: no.

**One restriction stands in the task's Context and binds you:** apart from that document, read no
note of any product and no repository of any product. Stay in this worktree's tracked files and the
cycle's directory. A text of the change that names a product is something to look for.

The-way has no `guidelines/` directory of its own, so no guideline file applies.

## Your return

Write the report as the method gives, its first line `PASS 1740c02` or `FAIL 1740c02`, with
**Searches not found or unclear**, and return only that first line, the counts of blocking, Minor and
out-of-scope findings, and the report's path.

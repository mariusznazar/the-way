# Handoff — reviewer of the whole change

## Delegation

The person who requested this cycle (Mariusz) delegated every intermediate choice to the cycle's
orchestrator. You answer to the orchestrator, never to the human, and you ask no human.

## Where you work

- Worktree, your working directory for every command and read:
  `C:/Storage/repos/the-way/.runs/worktrees/logs-life-and-failure-notice`
- This is the-way working on itself, at the checkout above; there is no `.the-way`, and the-way's
  files are read from this worktree, never from another checkout.
- Target branch `foundations`, task branch `task/logs-life-and-failure-notice`. You change no
  tracked file and make no commit. Your report:
  `.runs/task-cycles/logs-life-and-failure-notice/reports/whole-review.md`, ignored by Git.

## Your method and stage

Read `task-cycle/review/SKILL.md` whole and follow it for the review of **the whole change**: read
`task-cycle/review/whole_change.md` when it names it, and each other file when the step that names
it comes. You made none of this change. You alone select your own foundation and guidelines.
Your boundary: you return your report's first line, `PASS <sha>`, `FAIL <sha>` or `questions`.

## What you review

- Range: base `5d66387`, head `4a3ee37`. One author, no plan, so this is the review of the whole
  change and no slice stands apart.
- Frozen task, read it whole: `.runs/task-cycles/logs-life-and-failure-notice/task.md`. Its
  citations stand at `foundations` `f86fd71`; the base differs from that commit only in
  `product-guidelines/coding/**` and in two passages of `foundations/decisions.md` outside the
  entries in play.
- Reviewed spec: `.runs/task-cycles/logs-life-and-failure-notice/spec.md`, which passed its review
  in `reports/spec-review-2.md` in the same directory. It settles the choices the task left open,
  under its D1 to D9. Its D6 reads row 4 and its D4 reads row 3, each named there; the rows' words
  stand in the task.
- Author's report: `.runs/task-cycles/logs-life-and-failure-notice/reports/author.md`.

Coverage to check: every item of the task's *To do*, each of its four rows of *Settlements to
record*, its *Questions carried to cycle*, and its answers 1 to 6 with the two marks of what answer
5 replaced. The task carries no projected entry.

The change is prose and foundation entries; the reader of the step's files is an agent following
them, so read them as that agent would, resuming a definition as well as starting one, and at a
definition as well as at a task.

## Answers of step 4

- Trust boundary: no. No file the part map names as one changes.
- Operation that cannot be undone: no.

**One restriction stands in the task's Context and binds you:** do not open
`C:\Storage\repos\loop2-10x`, the branch `10x/m3l5`, the tag `archive/10x-m3l5` of the repository
`loop2`, or the map of m3l5. A text of the change that names a product, or a tool, in the step's
files is something to look for.

The-way has no `guidelines/` directory of its own, so no guideline file applies.

## Your return

Write the report as the method gives, its first line `PASS 4a3ee37` or `FAIL 4a3ee37`, with
**Searches not found or unclear**, and return only that first line and the report's path.

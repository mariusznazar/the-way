# Handoff — the one author

## Delegation

The person who requested this cycle (Mariusz) delegated every intermediate choice to the cycle's
orchestrator. You answer to the orchestrator, never to the human, and you ask no human.

## Where you work

- Worktree, your working directory for every command and read:
  `C:/Storage/repos/the-way/.runs/worktrees/logging-guidelines`
- This is the-way working on itself, at the checkout above; there is no `.the-way`, and the-way's
  files are read from this worktree, never from another checkout. Each skill of the-way named by a
  file you read is this repository's file: `record-decision` is `elements/decisions/skill/SKILL.md`.
- Target branch `foundations`, base `ea4694e`, task branch `task/logging-guidelines`. No upstream is
  set; do not push.
- Your report: `.runs/task-cycles/logging-guidelines/reports/author.md`, ignored by Git.

## Your method and stage

Read `task-cycle/change/SKILL.md` whole and follow it for **the whole change as the one author**.
Read each file it names when the step or variant that names it comes. For the foundation step, read
`task-cycle/skill/foundation_step.md`, and the skill of an element when you write an entry of that
element. Your boundary: you return before review; you start no later stage.

Do not run the full gate (`python -B gate/run_tests.py`): that run is the orchestrator's. Run the
focused checks that bear on what you change, such as
`python -B elements/common/foundation_check.py .` and `python -B gate/run_tests.py <directory>` for
one directory. Report each with its command and exit code. A check that goes through a pipe does
not report the exit code of the check.

Commit by path (`git add <file> <file>`, never `git add -A`, `git add .` or `git commit -a`), commit
messages in English in the form the repository's recent commits use. Leave a clean tree.

## The task and the spec

- Frozen task, read it whole: `.runs/task-cycles/logging-guidelines/task.md`, accepted with
  `Status: ready for cycle`, `Project relation: independent`. Its citations stand at `foundations`
  `ea4694e`, the base.
- Reviewed spec, read it whole: `.runs/task-cycles/logging-guidelines/spec.md`, which passed its
  review in `reports/spec-review-2.md` in the same directory. Its *Decisions*, its *Units* and its
  *Foundation entries* bind you; *Left to the maker* is yours. A change the spec does not name and
  the task needs is a reach: name it in your report.
- The eight rows of *Settlements to record* are the foundation entries' meaning, as the spec divides
  them. *Rejected* of an entry written from a row holds only the ways the row's source keeps.

Two points the review of the spec left to you:

- The line `Personal data: none — <PREFIX-NN>` of D3: settle in the template's bullet for that rule
  whether its label stays in English in a product that writes its guidelines in another language.
- E7's *Rejected* stays as the spec gives it.

**One restriction stands in the task's Context and binds you:** apart from that document, read no
note of the author and no repository of any product. A later step measures whether the process
reaches its conclusions on a product's logs by itself. No text of the change names any product, and
no text of the change names the private notes.

The texts the change writes are in English, as the files they stand in are.

## Answers of step 4

- Trust boundary: no. No file the part map names as one changes; where your work needs one to, stop
  and return.
- Operation that cannot be undone: no.
- Open design choice: settled by the reviewed spec. One you meet that it does not settle returns
  `returned` with a report and no code.
- Route: one author without a plan.

## What to read

Of the foundation, each whole, from `foundations/decisions.md`: WAY-05, WAY-07, WAY-19, WAY-25,
WAY-27, WAY-30, WAY-33, WAY-86, WAY-100, WAY-104, WAY-134, WAY-165, WAY-167, WAY-168, WAY-170,
WAY-171, WAY-172, WAY-173, WAY-174, WAY-202, WAY-203, WAY-210, WAY-211, WAY-225, WAY-251, WAY-268,
WAY-270; each opens at its heading `### WAY-<n> — `. Read the log by those ranges, not whole.

Every file of the spec's *Units* table, whole, before you change it, `foundations/decisions.md`
apart, whose end and the form of its last entries you read. `product-guidelines/template.md`, whole.
`agent-instructions/README.md` sets how work on the-way goes: the search of the whole foundation once
an entry is settled (WAY-33) stands there, and a finding you cannot settle by correcting an entry
returns to me.

The-way has no `guidelines/` directory of its own, so no guideline file applies.

## Your return

Keep the one sentence of each entry's meaning for the request, in the task document's language,
Polish, in your report, with the row each entry carries. Write the report as the method gives, with
**Searches not found or unclear**, and return only your status, your commits, a one-line check
result naming what failed or did not run, and the report's path.

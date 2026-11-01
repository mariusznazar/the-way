# Handoff — the one author

## Delegation

The person who requested this cycle (Mariusz) delegated every intermediate choice to the cycle's
orchestrator. You answer to the orchestrator, never to the human, and you ask no human.

## Where you work

- Worktree, your working directory for every command and read:
  `C:/Storage/repos/the-way/.runs/worktrees/guidelines-audit-report`
- This is the-way working on itself, at the checkout above; there is no `.the-way`, and the-way's
  files are read from this worktree, never from another checkout. Each skill of the-way named by a
  file you read is this repository's file: `record-decision` is `elements/decisions/skill/SKILL.md`.
- Target branch `foundations`, base `2f51e6c`, task branch `task/guidelines-audit-report`. No
  upstream is set; do not push.
- Your report: `.runs/task-cycles/guidelines-audit-report/reports/author.md`, ignored by Git.

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

- Frozen task, read it whole: `.runs/task-cycles/guidelines-audit-report/task.md`, accepted with
  `Status: ready for cycle`, `Project relation: independent`. Its citations stand at `foundations`
  `2f51e6c`, the base. It holds the scale and the order whole: read no skill of the course it names
  and no note of the author beyond it.
- Reviewed spec, read it whole: `.runs/task-cycles/guidelines-audit-report/spec.md`, which passed its
  review in `reports/spec-review-2.md` in the same directory. Its *Decisions* and its *Foundation
  entries* bind you; *Left to the maker* is yours, and it lists the files to change. A change the
  spec does not name and the task needs is a reach: name it in your report.
- The six rows of *Settlements to record* are the foundation entries' meaning, as the spec divides
  them. *Rejected* of an entry written from a row holds only the ways the row's source keeps, and
  each row's weak point goes into its entry's *Rationale*.

Three points the review of the spec left to you, from `reports/spec-review-2.md`:

- `refine-task` step 3 names no discipline skill, so the hand-back of an audit that stopped works
  only by what `hand_back.md` itself says of the other skill. Write it there, and correct "hands
  back to its step 4" at `product-guidelines/coding/SKILL.md:31` and
  `product-guidelines/testing/SKILL.md:30`.
- Step 3 of the coding and the testing skill names the other skill's `recognize.md`, with its
  condition, under WAY-256 and WAY-265; `recognize.md` itself does not change.
- Word the condition of an audit that stops by the audit that runs, never by what the product has.

The texts the change writes are in English, as the files they stand in are. No text of the change
names the private notes or any product. Entry A names the course and lesson with no address, as
`foundations/decisions.md:7960` and `:8074` do.

The order of the commits: the foundation first, so that the files' citations stand on existing
entries, unless your own reading gives a reason against it.

## Answers of step 4

- Trust boundary: no. No file the part map names as one changes; where your work needs one to, stop
  and return.
- Operation that cannot be undone: no.
- Open design choice: settled by the reviewed spec. One you meet that it does not settle returns
  `returned` with a report and no code.
- Route: one author without a plan.

## What to read

Of the foundation, each whole, from `foundations/decisions.md`: WAY-05, WAY-07, WAY-14, WAY-19,
WAY-22, WAY-24, WAY-25, WAY-27, WAY-30, WAY-33, WAY-36, WAY-100, WAY-114, WAY-120, WAY-134, WAY-161,
WAY-173, WAY-174, WAY-187, WAY-200, WAY-201, WAY-204, WAY-205, WAY-215, WAY-216, WAY-235, WAY-247,
WAY-250, WAY-251, WAY-256, WAY-265, WAY-266; each opens at its heading `### WAY-<n> — `. Read the log
by those ranges, not whole.

Every file of the spec's *Left to the maker*, whole, before you change it, `foundations/decisions.md`
apart, whose end and the form of its last entries you read. Also `product-guidelines/reading.md`,
`product-guidelines/coding/recognize.md`, `product-guidelines/testing/recognize.md`,
`product-guidelines/testing/new_level.md`, `project-level/task/template.md` and
`elements/decisions/template.md`. `agent-instructions/README.md` sets how work on the-way goes: the
search of the whole foundation once an entry is settled (WAY-33) stands there, and a finding you
cannot settle by correcting an entry returns to me.

The-way has no `guidelines/` directory of its own, so no guideline file applies.

## Your return

Keep the one sentence of each entry's meaning for the request, in the task document's language,
Polish, in your report, with the row each entry carries, for new and changed entries alike. Write
the report as the method gives, with **Searches not found or unclear**, and return only your status,
your commits, a one-line check result naming what failed or did not run, and the report's path.

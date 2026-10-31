# Handoff — the one author

## Delegation

The person who requested this cycle (Mariusz) delegated every intermediate choice to the cycle's
orchestrator. You answer to the orchestrator, never to the human, and you ask no human.

## Where you work

- Worktree, your working directory for every command and read:
  `C:/Storage/repos/the-way/.runs/worktrees/logs-life-and-failure-notice`
- This is the-way working on itself, at the checkout above; there is no `.the-way`, and the-way's
  files are read from this worktree, never from another checkout. Each skill of the-way named by a
  file you read is this repository's file: `record-decision` is `elements/decisions/skill/SKILL.md`.
- Target branch `foundations`, base `5d66387`, task branch `task/logs-life-and-failure-notice`. No
  upstream is set; do not push.
- Your report: `.runs/task-cycles/logs-life-and-failure-notice/reports/author.md`, ignored by Git.

## Your method and stage

Read `task-cycle/change/SKILL.md` whole and follow it for **the whole change as the one author**.
Read each file it names when the step or variant that names it comes. For the foundation step, read
`task-cycle/skill/foundation_step.md`, and the skill of an element when you write an entry of that
element. Your boundary: you return before review; you start no later stage.

Do not run the full gate (`python -B gate/run_tests.py`): that run is the orchestrator's. Run the
focused checks that bear on what you change, such as
`python -B elements/common/foundation_check.py <the argument its usage gives>` and
`python -B gate/run_tests.py project-level` for one directory. Report each with its command and
exit code. A check that goes through a pipe does not report the exit code of the check.

Commit by path (`git add <file> <file>`, never `git add -A`, `git add .` or `git commit -a`),
commit messages in English in the form the repository's recent commits use. Leave a clean tree.

## The task and the spec

- Frozen task, read it whole: `.runs/task-cycles/logs-life-and-failure-notice/task.md`, accepted with
  `Status: ready for cycle`, `Project relation: independent`. Its citations stand at `foundations`
  `f86fd71`; the base `5d66387` differs from that commit only in `product-guidelines/coding/**` and
  in two passages of `foundations/decisions.md` outside the entries in play, so its line numbers in
  that file from WAY-219 on moved by about eleven lines.
- Reviewed spec, read it whole: `.runs/task-cycles/logs-life-and-failure-notice/spec.md`, which
  passed its review in `reports/spec-review-2.md` in the same directory. Its *Decisions*, its
  *Files* and its *Foundation entries* bind you, D6's three readings and D4's condition included;
  *Left to the maker* is yours. A change the spec does not name and the task needs is a reach:
  name it in your report.
- The four rows of *Settlements to record* are the foundation entries' meaning, as the spec divides
  them. *Rejected* of an entry written from a row holds only the ways the row's source keeps.

**One restriction stands in the task's Context and binds you:** do not open
`C:\Storage\repos\loop2-10x`, the branch `10x/m3l5`, the tag `archive/10x-m3l5` of the repository
`loop2`, or the map of m3l5. The change must not know what lies there, and no text of the change
names `loop2` or any product.

The step's text names no tool and no product (To do 5). The texts the change writes are in English,
as the files they stand in are.

## Answers of step 4

- Trust boundary: no. `project-level/readiness_check.py`, `plan_check.py` and `plan_state.py` do not
  change. Where your work needs one of them to change, stop and return.
- Operation that cannot be undone: no.
- Open design choice: settled by the reviewed spec. One you meet that it does not settle returns
  `returned` with a report and no code.
- Route: one author without a plan.

## What to read

Of the foundation, each whole, from `foundations/decisions.md`: WAY-05, WAY-07, WAY-19, WAY-25,
WAY-33, WAY-100, WAY-106, WAY-118, WAY-121, WAY-122, WAY-123, WAY-134, WAY-138, WAY-139, WAY-165,
WAY-166, WAY-267, WAY-268; each opens at its heading `### WAY-<n> — `. From
`foundations/invariants.md`, the invariant `project-technology-record`. From
`foundations/glossary.md`, `agent's way to the running product`.

Every file of the spec's *Files* table, whole, before you change it. `agent-instructions/README.md`
sets how work on the-way goes: the search of the whole foundation once an entry is settled (WAY-33)
stands there, and a finding it cannot settle by correcting an entry returns to me.

The-way has no `guidelines/` directory of its own, so no guideline file applies.

## Your return

Keep the one sentence of each entry's meaning for the request, in the task document's language,
Polish, in your report, with the row each entry carries. Write the report as the method gives, with
**Searches not found or unclear**, and return only your status, your commits, a one-line check
result naming what failed or did not run, and the report's path.

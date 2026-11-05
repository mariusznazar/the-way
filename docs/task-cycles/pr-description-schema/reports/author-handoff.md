# Handoff — the one author

## Delegation

The person who requested this cycle (Mariusz) delegated every intermediate choice to the cycle's
orchestrator. You answer to the orchestrator, never to the human, and you ask no human. A question
goes into your report and your short return, with the status `questions`.

## Where you work

- Worktree, your working directory for every command and read:
  `C:/Storage/repos/the-way/.runs/worktrees/pr-description-schema`
- This is the-way working on itself; there is no `.the-way`, and the-way's files are read from this
  worktree, never from another checkout. `agent-instructions/README.md` governs changes to the-way
  before `main`: read its "Make the change" section.
- Target branch `foundations`, base `f45ca40`, task branch `task/pr-description-schema`, no
  upstream. You commit on the task branch; you never push, never merge, never touch another branch
  or worktree. No other agent writes in this worktree while you work.
- Never commit anything under `.runs/` (ignored by Git). Your report goes to
  `docs/task-cycles/pr-description-schema/reports/author.md`.

## Your method and stage

Read `task-cycle/change/SKILL.md` whole and follow it, in its variant **"the whole change as the
one author"**. Read each file it names when the step that names it comes. Your stage includes the
foundation step: read `task-cycle/skill/foundation_step.md` whole and write the entries it and the
spec give, each through its element's skill (`elements/decisions/skill/` for a decision), which
selects the reading the entry needs. Your boundary: you return before review — `done`, `done with
concerns`, `questions`, `returned`, `reserved` or `blocked` — and start no later stage.

## The task and the spec

- Frozen task, read whole: `docs/task-cycles/pr-description-schema/task.md` (Polish; copied
  2026-11-05, `Status: ready for cycle`, `Project relation: independent`, citations at `f45ca40`).
  Its *To do* 1–9, its answers and its six rows of *Settlements to record* bind you; *Out of scope*
  holds the place of screenshots and the weekly review of the archives' findings.
- Reviewed spec, read whole: `docs/task-cycles/pr-description-schema/spec.md`. Its *Decisions*
  D1–D10 and *Foundation entries* bind you; *Left to the maker* is yours. D10 was settled by the
  orchestrator after the spec's review left two findings
  (`docs/task-cycles/pr-description-schema/reports/spec-review-2.md`): it moves the exception for
  a form error held wrong out of the row-6 entry into a decision of its own, and narrows the plan
  case of the language measure. Where the spec and D10 differ, D10 holds.
- The spec gives WAY-114, WAY-134 and WAY-10 and the new entries as meanings; their wording is
  yours, keeping each meaning (WAY-114, WAY-134).

## Answers of step 4

- Trust boundary: no. The spec changes no file the part map names as one.
- Operation that cannot be undone: no.
- No user interface: WAY-219's screenshot does not apply.

## What you read

Foundation entries, each whole in `foundations/decisions.md`, from its `###` heading to the next,
with rationale and *Rejected*: WAY-03, WAY-10, WAY-14, WAY-19, WAY-33, WAY-35, WAY-36, WAY-49,
WAY-51, WAY-114, WAY-134, WAY-140, WAY-148, WAY-160, WAY-161, WAY-162, WAY-163, WAY-164, WAY-219,
WAY-227, WAY-256, WAY-260, WAY-261, WAY-268, WAY-269. The part map and the glossary, both short,
whole. The-way has no product guidelines directory; for the script, follow the house style of
`task-cycle/cycle_stages.py` and `task-cycle/test_cycle_stages.py`, and the invariants of
`foundations/invariants.md` whose *Part* names `task-cycle` or `every` — the spec's reviewer reached
`script-language`, `script-imports`, `script-subprocesses`, `return-step-record` and
`outbound-link-reach`.

The nightly digest outside the repository,
`C:\Storage\The Brain\The Brain\Notes\Areas\(A) Claude code\scripts\cycle_remarks_digest.py`
(`extract_remark_blocks`, around line 240), cuts "Process remarks" blocks out of committed records;
the record template you change must keep such a block where it cuts it (spec D3). Read it; change
nothing outside the repository.

## Checks

- Run the focused tests of each directory you change, e.g. `python -B gate/run_tests.py task-cycle`,
  `python -B gate/run_tests.py elements`, `python -B gate/run_tests.py project-level`,
  `python -B gate/run_tests.py agent-instructions`, and `python -B elements/common/foundation_check.py .`.
  A new test file runs only once `git add` has it. Do not run the full gate
  (`python -B gate/run_tests.py` with no argument): the orchestrator runs it.
- Never commit while one of your own test runs is still going: a test of `installation/` reads the
  current commit twice and fails if HEAD moves during the run.
- Each check in your report carries its command and exit code (WAY-159).

## Your report

Write `reports/author.md` as your method gives it: what changed and why, by commit; each foundation
entry written or changed with its identifier and one sentence of its meaning in Polish (for the
request's decision section and its collapsed block); each kept row tied to its entry; the choices
you made under *Left to the maker*; your own-work check (WAY-164); your checks with command and exit
code; each reach beyond this handoff; and **Searches not found or unclear**, or `none`. Return your
status, your commits, a one-line check result naming what failed or did not run, and the report's
path.

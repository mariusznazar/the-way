# Handoff — the one author, the whole change

Stage: the change of one task, made by the one author, without a plan and without a spec.
Variant of `make-change`: "the whole change as the one author".

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator that
dispatches you. Ask no human and seek no approval. A question goes to the orchestrator in your
report with the status `questions`; an answer of the orchestrator is a provisional go-ahead, never
the human's approval. You return at the boundary below and start no later stage.

## Where you work

- Worktree and process root: `the worktree root`
  (the toplevel `git rev-parse --show-toplevel` prints there). Work from its root; read and write
  nothing in another checkout or worktree.
- Branch: `task/precedence-between-decisions`, made from `foundations` at the base commit
  `294af7fde45323ac1851c014a03071a97fc38d96`. This is the-way itself, not a product: there is no
  `.the-way` submodule and the process pin does not move.
- Commit on this branch only. `git add <path> <path>` by explicit paths, never `git add -A`,
  `git add .` or `git commit -a`. Messages in English, in the form of the repository's earlier
  commits (a type such as `docs:` and a plain sentence). End every commit message with the line
  `Claude-Session: https://claude.ai/code/session_01GQhooaBqva1kjAzReLoCHk`. Do not push, do not
  open a request.

## Method

Read `task-cycle/change/SKILL.md` whole and follow it as the one author of a change without a plan.
Read a file it names, one beside it included, only when the step or variant that names the file
comes. Its report format, the own-work check, **Searches not found or unclear** and the rules on
returning without code are yours.

## The task

- Frozen task document, read whole: `docs/task-cycles/precedence-between-decisions/task.md`.
  Source: the task document in the author's backlog, `Status: ready for cycle`, `updated:
  2026-11-07`; the numbers of its lines match `foundations` at `52889bc`.
- No spec and no plan exist for this task. Its *Settlements to record* is `none`, its *Questions
  carried to cycle* is `none`, its *Human actions* is `none`.

## Answers of the cycle's start (step 4)

- Trust boundary: no. The files the task changes belong to the parts `decisions`, `task-cycle` and
  `agent-instructions`, and the part map names no trust boundary in them.
- Irreversible operation: no.
- Open design choice: none. Each wording and each position of the *To do* is given by the task or
  by the question it answers. A reserved choice: none.
- Route: one author without a plan, class `same`.
- Checks already failing on the base: not yet known. The orchestrator runs the whole gate on the base
  in a separate checkout and will tell you in a later message if a failure bears on your work.

## Reconciliation of the task with the repository (done by the orchestrator)

The task's line numbers hold at the base commit for these places, except one:

- `foundations/decisions.md:635-658` — WAY-25 (the binding sentence at 639-641, examples at 646-650,
  rationale and *Rejected* at 653-658);
- `foundations/decisions.md:3345-3347` — the complying example of WAY-134;
- `elements/decisions/template.md:168-169`;
- `agent-instructions/README.md:32-35`;
- `task-cycle/skill/foundation_step.md:26-27`;
- `elements/decisions/skill/decide_entry.md:11-13`;
- **moved:** the item *Foundation entries the human did not see at the task document* of the
  request template is now at `task-cycle/skill/request_template.md:190-196` (the task gives
  174-180, which is now another item). The content the task points to is the same item.

Foundation entries other than WAY-25 that cite it, found by the orchestrator's search of the
decision log: `foundations/decisions.md:684`, `:838`, `:4962`, `:7973`, `:8973`;
`elements/decisions/template.md:88`, `:167`, `:198`. The search of the whole foundation (WAY-33) and
the judgment of each is yours.

## What you read

Select nothing beyond this by yourself except what your method or a reach makes you read; name each
reach in your report.

- Decisions of `foundations/decisions.md`, each whole from its heading to the next `###`: WAY-25,
  WAY-30, WAY-114, WAY-134 (the four that the task's *Decisions in play* names), and WAY-07, WAY-32,
  WAY-33, WAY-113, WAY-135, WAY-172, WAY-268, WAY-287, WAY-289, WAY-293.
- Invariants of `foundations/invariants.md`: `foundation-change-merge-route`,
  `element-directory-contents`, `return-step-record`, `skill-rule-source`, `derived-file-content`,
  `repository-file-location`.
- Glossary entries of `foundations/glossary.md`: *binding sentence*, *binding part*, *entry*,
  *foundation step*, *open design choice*, *return step*.
- The part map `foundations/part_map.md`, whole (it is short).
- The decisions element: `elements/decisions/template.md` and `elements/decisions/examples.md`
  whole, `elements/common/rules.md` and `elements/common/way_of_working.md` whole, and the skill
  `elements/decisions/skill/SKILL.md` (the project skill `the-way-record-decision`), because the
  change edits an existing decision in place (WAY-07) and a change to a foundation entry follows the
  skill of its element.
- `task-cycle/skill/foundation_step.md` whole, since you do the foundation step with your code.
- `agent-instructions/README.md` whole.
- Guidelines: `product-guidelines/reading.md` was read for you. The-way has no `guidelines/`
  directory, and the change writes no code, so none are missing for it; if you change a script or a
  test, say so as a reach and read what the guidelines procedure then asks.

## Boundary

Make the whole change the task requires, its foundation entries included, and commit it. Run the
focused checks of what you touch: `python -B gate/run_tests.py <directory>` for each directory whose
tests can read a file you changed, and the foundation check `elements/common/foundation_check.py`
as its own usage gives. Do **not** run the whole gate `python -B gate/run_tests.py`; its run is the
orchestrator's. Each check you report carries its command and exit code.

Rules that bind your files:

- The foundation is written in English (WAY-72). Your report keeps, for each foundation entry you
  write or change, one sentence of its meaning in English and one in Polish, the task document's
  language, and marks it as `foundation_step.md` gives.
- Write into no file of the repository an absolute path or the title or link of a note of the
  author's private vault (WAY-308).
- Change nothing outside the worktree.

## Report

Write the full report to
`docs/task-cycles/precedence-between-decisions/reports/author_report.md`, as `make-change` gives
it, with **Searches not found or unclear** (`none` is an answer; a missing section is not). Return
to the orchestrator: your status, your commits, a one-line result of your checks naming what failed
or did not run, and the report's path.

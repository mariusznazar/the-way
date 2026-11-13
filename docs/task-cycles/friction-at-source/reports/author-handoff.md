# Handoff — the one author of the change `friction-at-source`

## Delegation

You make the whole change of one the-way task as the one author, with no plan. The human who asked for this
cycle has delegated intermediate choices to the orchestrator, who is the one you ask; there is no human to ask
during the cycle. Your work is reviewed afterwards by an agent that did not make it.

## Where

- Worktree (work from its root, and nowhere else): `the worktree's root`
- Branch `task/friction-at-source`, base commit `6814c6f6c9ff2b29d34612fa5cc86945ec3a2812` (the target branch `foundations`).
- This is the-way itself, so the process root is that worktree. No other the-way checkout is read.
- Report path (write your full report there): `docs/task-cycles/friction-at-source/reports/author-report.md`

## Method

Read `task-cycle/change/SKILL.md` in the worktree whole, and follow it, in its variant "the whole change as the one author".
Read a file it names only when the step or variant that names it comes. Where it, or the task, names another skill of the-way —
`record-decision`, `record-glossary-term` — use the project skill with the `the-way-` prefix, whose entry point leads to
`elements/decisions/` and `elements/glossary/` of the worktree. The change includes the foundation step: read
`task-cycle/skill/foundation_step.md` whole and follow it for the entries below; it also tells how the foundation step
chooses the entries' wording and when it asks. The return step comes later, as a separate resumption; do not take it now.

## The task

The frozen task document is
`docs/task-cycles/friction-at-source/task.md`.
Read it whole. It is in Polish; the entries and files you write are in English, as the-way's files are.

What it asks, in one line each (the document governs):

1. In `task-cycle/skill/request_template.md`, the item of kind 4 (a check an agent did not run, which the human can do by hand)
   gets a fifth part: three to six steps for the human — where to go, what to do, what the human should see. The three answers
   of the item stay the same; the human writes a remark after checking, as today. This changes WAY-327 in place (a decision is
   edited in place, WAY-07), adding the fifth part to it. The skeleton of the description (WAY-286) and the form-check script
   (WAY-290) stay as they are.
2. In the template of the task document (`project-level/task/template.md`) and in the skill that refines a task
   (`project-level/task/skill/`, the file or files where the rule belongs), the place to change in a file is pointed at by a heading
   or a quotation, and a line number is only a hint; the *Source* under a question stays as it is today, with the line and the revision.
3. The skill of the foundation review (`foundation-review/`) lists the decisions that describe a transitional state of the product
   and asks the human, at each, whether a task exists that ends that state; where none exists, it proposes creating one, as it does
   for its other proposals (WAY-302). The decision entry carries no field for the task.

Settlements to record (rows of the task's *Settlements to record*, all accepted, all to be written whole by you in the foundation step):

- Row 1 — a new decision: the rule of point 2, with the rejected script that checks references before the cycle (from question 2's *Not chosen*).
- Row 2 — a new decision: the rule of point 3, with the rejected field in a decision's entry and the rejected question at refinement (question 3's *Not chosen*).
- Row 3 — the change to WAY-327 of point 1 (question 4's *Not chosen*: the separate section of the description).
- Row 4 — a glossary entry for "transitional state" (Polish "stan przejściowy"): the state of a product that a decision describes until work later than
  the change that brings the decision ends it — like the two forms of a shared control until the last screen moves to React. Check with
  `record-glossary-term` whether the term earns an entry (WAY-95) and the form of the entry; where the row's own wording conflicts with that skill, say so in the report instead of settling it silently.

The next free decision number is WAY-353. Write nothing beyond the task: the script that runs a check and writes its proof, the counting
of unrun checks by cause, and the list-of-tasks field in a decision are out of scope (the task's *Out of scope* and questions 1, 5).

## Answers of the cycle's start (step 4)

- Trust boundary: no. Irreversible operation: no. Open design choice: none. Reserved choice: none.
- The change touches the parts `task-cycle`, `project-level`, `foundation-review`, `decisions`, `glossary` of the part map.
  Check the part map after the change: where a file you add or move needs an assignment, the return step handles it; tell the orchestrator in the report.
- Product guidelines: the-way has none.

## What you read

Foundation entries, each whole (a decision is the lines from its `###` heading to the next heading in `foundations/decisions.md`):

- the task's *Decisions in play*: WAY-327, WAY-286, WAY-287, WAY-289, WAY-290, WAY-24, WAY-302, WAY-305, WAY-36, WAY-37, WAY-01;
- selected by the orchestrator as bearing on the files you change: WAY-282, WAY-301, WAY-303, WAY-310, WAY-311, WAY-312 (the foundation review),
  WAY-113, WAY-114, WAY-124, WAY-134, WAY-308, WAY-309, WAY-320 (the task document and the privacy of paths);
- `foundations/part_map.md` whole, `foundations/glossary.md` whole, the invariants whose *Part* names a touched part or `every`
  (find them by a search of `foundations/invariants.md`).

Beyond that, the foundation step selects as `task-cycle/skill/foundation_step.md` and the skills of the elements give. Search the whole
foundation once for the entries your new entries touch (WAY-33), and correct them in the same change. Every file you change, read whole first.

## Boundaries

- Commit on the branch, naming files by path (`git add <file> ...`), never `git add -A`. Commit messages in English, the form of the existing log.
  Do not push. Do not touch the checkout `the main checkout of the repository` or other worktrees.
- Do not run the product's whole gate (`python -B gate/run_tests.py` without a directory): the orchestrator runs it. Run the focused checks that
  your change calls for: `python -B gate/run_tests.py <directory>` for the directories whose files you changed
  (the part's tests; `elements/common/foundation_check.py` on the foundation; `python -B agent-instructions/skill_entry_points.py --check`
  if a description of a skill changes — and `--write` with a commit if so). Record each check's command and exit code in the report.
- Do not start the next stage; return at your boundary with the report. Questions go to the orchestrator as `questions`, not to a human.
- The report holds, as `make-change` gives it: status, commits, checks with command and exit code, the own-work check, your meaning sentences
  for each foundation entry written, **Unread material** and **Searches not found or unclear** (each `none` where there is nothing).
- Write the report to the path above only: a subagent's report file whose name starts with `report`, `summary`, `findings` or `analysis` is refused; `author-report.md` is fine.

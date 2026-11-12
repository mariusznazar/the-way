# Handoff — the one author, `make-change`

Delegation: the person who requested this cycle (Mariusz) has delegated intermediate choices to the
orchestrator and, through it, to you for choices of how to make what the task settles. Your answers
are never his approval. Do not ask him anything; send questions to the orchestrator.

## Where you work

- Worktree (the process root; work from its root, edit only inside it):
  `the task's worktree`
- Branch `task/problem-cost-in-register`, base `55afa8e57aa1b83c77108576a36642722e0dda15`
  (target branch `foundations`). The worktree is clean at the base. Commit on this branch only.
- Git rules: `agent-instructions/README.md` ("Make the change", "Check the change"); `git add` by
  path, never `-A`/`.`; commit messages in English; no force-push; do not push.
- Do not edit anything outside the worktree. In particular do not touch the user's register or any
  file in the user's notes: that is a human action the task places in the cycle (the orchestrator
  lists it in the request).

## Stage and variant

Stage: make the whole change as the one author (`make-change` variant "the whole change as the one
author"), foundation step included. Method: the project skill `the-way-make-change`; its entry
point sends you to `task-cycle/change/SKILL.md` in the worktree. Read that `SKILL.md` whole, and a
file it names only when the step that names it comes. The foundation step: read
`task-cycle/skill/foundation_step.md` whole when you reach it; it names the skill of each element
you write an entry of (decision, glossary term); read that skill's `SKILL.md` when you write an
entry of that element. You return before any review.

## The task

- Frozen task, read whole: `.runs/task-cycles/problem-cost-in-register/task.md`
  (approved `Status: ready for cycle`, document dated 2026-11-12; `Project relation: independent`).
- No spec, no plan: none was written; the task leaves no open design choice. What stays for you are
  choices of how to make what is settled (the header word of the column, the name of the table of
  levels, column order, layout of the output). Make them, name each in your report.
- *Settlements to record* rows 1, 2 and 3 are the entries you write in the foundation step
  (rows 1 and 2 decisions, row 3 a glossary term), as the task's table gives them; the
  report of *Candidates: 6 shown, 3 accepted* means only those three are accepted.
- Settled by the task and not yours to reopen: five fixed levels `nothing`, `steps`, `stage`,
  `round`, `human`, each dearer than the one before, a problem takes the highest level its actual
  cost reached; the user adapts only their meanings; the count shows cost per matter (issue) —
  for each issue fixed, open and dropped, how many of its problems stand on each level — and not per
  cycle. Read the task's "To do" items 1–4 and "Questions to settle" for the exact words.

## Answers of the orchestrator at start

- Trust boundary: yes. `process-audit/audit_count.py` is a trust boundary of the part map and the
  change edits it. Craft-input cases to cover with tests: a cost cell that is not a level of the
  table, a table of levels missing a level, with a doubled or an extra level, a register lacking the
  new column or the new table (WAY-344: an error that names the missing field; never an empty value),
  a cell holding `|` or a line break.
- Irreversible operation: no.
- Open design choice: none. Reserved choice: none.
- No move of the process pin: this is the-way itself.
- Checks already failing on the base: the orchestrator is running the whole gate on the base in a
  separate checkout; its result is not available to you yet. Run focused checks only.

## Foundation entries to read (by identifier, each whole, in `foundations/`)

- Decisions: WAY-330, WAY-333, WAY-334, WAY-335, WAY-336, WAY-337, WAY-339, WAY-344 (the task's
  *Decisions in play* and their neighbours in the audit), and WAY-328, WAY-38, WAY-89 (how the-way
  writes its own code and tests, and the Python version).
- Part map: the entry `process-audit` and the entries of the parts it depends on that you touch.
- Invariants whose *Part* is `process-audit` or `every`.
- Glossary: read it whole (short); the term row 3 asks for must not collide with an entry.
- Guidelines: none apply; WAY-328 departs from the general coding and testing guidelines for the
  code and tests of the-way itself.

## What to change (the task's To do, for your orientation; the frozen task is the authority)

1. `process-audit/problem_register.md`: a column for the cost of one occurrence in the table
   *Problems*, and, beside the table *Weights*, a table of the five fixed levels with meanings the
   user may adapt, without changing the levels.
2. `process-audit/audit_count.py`: read each problem's cost; refuse a row whose cost is not a level
   of the table as an unknown weight is refused today; treat a levels table that lacks exactly these
   five levels as a weights table without its four levels is treated today. WAY-344 governs every
   new field (a table, a column).
3. The result of the count, for each issue fixed, open and dropped, gives how many of its problems
   stand on each level of cost. (The task says "sprawa" for issue.)
4. `process-audit/SKILL.md`: show the human the cost beside issues as material to weigh, setting no
   priority or order from it (WAY-336).
5. Tests in `process-audit/test_audit_count.py` for each of the above, including the failing run of
   each new test before the code makes it pass, as `make-change` gives.
6. Foundation entries: the three rows of *Settlements to record*. A new decision for the scale and
   one for the place of cost in the result, or an edit of WAY-333 / WAY-330 where that is how the
   decision log should hold them — judge by the decisions skill and `rules.md`; name the choice in
   the report. Part-map and other foundation entries only as the change requires. `foundation_check`
   must pass.

Keep the term "cost of an occurrence" distinct from the existing *Cost* section of the count (cost
of a cycle at constant prices, WAY-337): that is the point of glossary row 3.

## Report

Write your full report to
`.runs/task-cycles/problem-cost-in-register/reports/author-report.md`
as `make-change` gives, including **Unread material**, **Searches not found or unclear** and the
own-work check, and every check with its command and exit code. Return status, commits, a one-line
check result and the report's path. Do not run the whole gate (`python -B gate/run_tests.py` with no
argument); run the tests of `process-audit` and the foundation check, and any directory your change
touches.

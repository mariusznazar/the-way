# Handoff — the one author of the whole change

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator. You have
no contact with the human: send questions to the orchestrator in your report (status `questions`),
never seek approval. Nothing here is the human's approval.

## Where you work

- Worktree (work only here, from its root): `the root of the task's worktree`
- Branch `task/report-file-names-remarks-items`, base commit `55afa8e57aa1b83c77108576a36642722e0dda15`
  (branch `foundations`). This is the-way itself; there is no pinned `.the-way`.
- Git: commit messages in English, in the style of the existing log; stage by explicit paths
  (`git add <path> ...`), never `git add -A`, `git add .` or `git commit -a`.

## Method and variant

- Method: `task-cycle/change/SKILL.md` of the worktree (project skill `the-way-make-change`). Read it
  whole; read a file it names only when the step or variant that names it comes.
- Your variant, in the words of its row: **the whole change as the one author**.
- Foundation step: `task-cycle/skill/foundation_step.md` (read it whole when you reach the entries
  the task carries); read the skill of an element when you write an entry of that element
  (`the-way-record-decision` for the decision).
- Stage boundary: make the whole change with its foundation entry, commit, and return before any
  review. Do not run the product's full gate (`python -B gate/run_tests.py` with no argument) — the
  orchestrator runs it. Focused checks are yours: `python -B gate/run_tests.py task-cycle` runs the
  tests of the `task-cycle` directory; you may also run a single test file.

## The task

Frozen task (read it whole): `.runs/task-cycles/report-file-names-remarks-items/task.md`
(original: the human's backlog document, status `ready for cycle`, updated 2026-11-12).

Answers of the cycle's start:

- Trust boundary touched: no. Irreversible operation: no.
- Open design choice: none. Reserved choice: none. Route: one author without a plan, class `cheaper`.
- Checks failing on the base: not known yet (the orchestrator is measuring the gate on the base in a
  separate checkout); do not assume any.
- *Settlements to record*, row 1 (the one entry you write): the remarks script reads a report without
  the section **Searches not found or unclear** as giving no item and does not end with an error;
  the exception to WAY-344 stands in WAY-294, with its reason, and WAY-294's *Verification* example
  `report-planner.md` becomes `planner-report.md` at the same meaning (see *Decisions in play* of the
  task, WAY-294).

## What to read (foundation, selected by the orchestrator)

Decisions, each whole: WAY-148, WAY-260, WAY-294, WAY-295, WAY-344 (the task's *Decisions in play*),
and WAY-328 (the-way departs from product guidelines for its own code and tests), in
`foundations/decisions.md`.
Invariants of `foundations/invariants.md`: `script-language`, `script-imports`,
`script-subprocesses`, `tracked-file-private-paths`, `test-method-citation`, and any other whose
*Part* is `task-cycle` or `every` that the files you change reach.
Part map entry `task-cycle` in `foundations/part_map.md`. Glossary terms in
`foundations/glossary.md` for the words you use.
Code and tests you change: `task-cycle/remarks_check.py` (docstring lines 1–48, `split_items`,
`label_end`, `section_items`) and `task-cycle/test_remarks_check.py`; the skill sentence goes into
`task-cycle/skill/SKILL.md`, immediately after the sentence in the paragraph beginning "Write each
dispatch's full handoff to a file in `reports/` whose name holds `handoff`; …(WAY-148).".

## Name your report

Write your full report to `.runs/task-cycles/report-file-names-remarks-items/reports/author-report.md`
(the name starts with the role and `report` comes after it — Claude Code refuses a subagent's write
of a file whose name starts with `report`, `summary`, `findings` or `analysis`; this is the very rule
the task adds). If a write is refused anyway, say so in **Searches not found or unclear**.

## Return

Return status, commits, a one-line check result naming what failed or did not run, and the report's
path. The report holds your questions and concerns, each reach beyond this handoff, its **Unread
material** (what this handoff names that stayed unread or was read in part, or `none`), its
**Searches not found or unclear** (or `none`), and the own-work check the method asks for, each check
with its command and exit code.

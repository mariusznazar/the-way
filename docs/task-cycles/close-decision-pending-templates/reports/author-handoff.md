# Handoff — the one author

You are the one author of this change, dispatched by the orchestrator of the task cycle `implement-task`.
The person who requested the cycle has delegated intermediate choices to the orchestrator; no answer
you get is that person's approval.

- Variant of `make-change`: "the whole change as the one author".
- Method: read `task-cycle/change/SKILL.md` whole, from the worktree below, and a file it names (one
  beside it included) only when the step or variant that names it comes.
- Worktree (your working directory; never edit another checkout):
  `the root of the task's worktree`
- Branch: `task/close-decision-pending-templates`, base commit `fca8491` (`foundations`).
- Frozen task, read it whole:
  `docs/task-cycles/close-decision-pending-templates/task.md`
  (it is the task document `zadanie_the_way_zamkniecie_dopiskow_w_szablonach.md`, approved 2026-11-13).
- Your report: `docs/task-cycles/close-decision-pending-templates/reports/author-report.md`

## Boundary

Make the whole change the task requires, with the foundation step, and return before any review. The
orchestrator runs the product's gate (`python -B gate/run_tests.py`, about 16 minutes) — you do not. You may run
the focused checks you need: `python -B gate/run_tests.py <directory>` for the directories of the files
you change, and the foundation check named in `elements/common/foundation_check.py` for this repository.

## Answers of the start (step 4)

- Trust boundary touched: no. The files are templates and a skill file of the elements; the part map gives
  those parts (`elements-common`, `environment-facts`, `glossary`, `invariants`, `part-map`) none.
- Irreversible operation: no.
- Open design choice: none. Every question of the task's *Questions to settle* is answered there; do not
  reopen one. Where you meet an open design choice, return `returned` with no code.
- Reserved choice: none.
- Settlements to record: none (0 accepted). *Decisions in play* are cited, not written; the decision log
  `foundations/decisions.md` does not change (task, *Out of scope*).

## Things the orchestrator checked on the base

- All 32 `TODO — decision pending` lines of `elements/` stand on `fca8491` at the places the task gives
  (`grep -rn "decision pending" elements`); the cases S26 (`elements/environment-facts/template.md:138`) and
  S28 (`elements/invariants/template.md:94`) stay and are out of scope.
- The task's table gives the line of each dopisek; a line moves as you edit a file, so locate by the quoted
  text of the dopisek, not by number alone.

## What to read (selected by "Reading the foundation" in `elements/common/way_of_working.md`)

Parts touched: `elements-common`, `environment-facts`, `glossary`, `invariants`, `part-map`.

- `agent-instructions/README.md` — the way the-way's own changes are made before `main` (WAY-33 search and
  return step of the change included).
- Decisions in `foundations/decisions.md`, each whole, from its heading to the next heading: the fifteen of the
  task's *Decisions in play* — WAY-05, WAY-22, WAY-29, WAY-36, WAY-41, WAY-44, WAY-48, WAY-61, WAY-62,
  WAY-64, WAY-71, WAY-72, WAY-73, WAY-90, WAY-99, WAY-113, WAY-114 — and besides them WAY-01, WAY-28, WAY-33,
  WAY-35, WAY-76, WAY-85, WAY-89, WAY-150, WAY-134.
  Check each citation you write against the whole entry, not against the sentence the task quotes.
- Invariants in `foundations/invariants.md`: `element-directory-contents`, `skill-rule-source`,
  `tracked-file-private-paths`, `return-step-record`.
- Part map `foundations/part_map.md`: the entries of the five parts above.
- Glossary: the entries for the words you use in the rewritten rules — read the terms in
  `foundations/glossary.md` that the rewritten sentences use.
- The element templates and files you change (listed in the task) and, for the search of the foundation for
  entries your change touches, the whole foundation once.
- `task-cycle/skill/foundation_step.md` — name of the foundation step of the cycle; read it whole and follow it
  (it is likely that it writes nothing here, because the task carries no entry to write; say so in the report).
- The product-guidelines of the-way itself: there are none for this repository; `product-guidelines/` holds
  the method for products. Report the reading as `none apply`.

## Reminders from the orchestrator

- Edit only what the task requires: the 19 cases S1–S19 (23 lines) by the table, S20–S25 and S27 by the
  task's *To do* items 2–9 in the words the task gives. The only change of the *sense* of a rule is the
  ending of S5 (the words "it belongs to the foundation of the product whose commits decide it" go) and the
  items 2–9.
- Every citation in S1–S12 is written only after you checked the decision's whole entry. Where you cannot
  confirm a citation — especially S4, S5, S7, S10, S11, where the task's source rates the confidence as medium —
  do not guess: put that case in the report under concerns with the quoted decision text, and write the
  rule as plain text without the citation, so the reviewer can decide.
- The citations are made the way the rest of the file cites: `(WAY-nn)` style, as the neighbouring lines do.
- The rewritten text of the template stays correct English of the template's register; keep lines wrapped as
  the file wraps them.
- After the edit, `grep -rn "decision pending" elements` must list exactly the two lines S26 and S28.
- Own-work check, commits and the report: as the method gives them. Commits message and language: follow
  `agent-instructions/README.md` and the git history of the repository.

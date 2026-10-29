A decision that a task's cycle writes from a row of *Settlements to record* had a *Rejected* field with no source: the task document kept the human's choice but not the ways shown and not chosen, and the refinement conversation that held them is deleted after acceptance. In loop2 the cycle `odkrywanie` filled *Rejected* of D-121–D-126 from the task's text, and its author wrote "Reasons in D-126's and D-124's *Rejected* are my own reading, not quoted." This change keeps the ways not chosen in the task document and has the cycle write *Rejected* only from them, from `none considered` where the human said so, or as `unknown`.

Independent task, refined and accepted on 2026-10-29 (AIR-533). Base and process revision: `d7a205cb3ae8c49465cd66f4de2031b33fc7ff9d`. No spec: the task's one row settles the entry (an extension of WAY-134) and its meaning, and the task's questions settle where the ways are kept. Route: one author without a plan; one review of the whole change (PASS), the return step and its review (PASS), and a correction for the human's remarks on this request, reviewed PASS. The process pin is unchanged — this is the-way itself.

## What changed

- `project-level/task/template.md`: an answer under *Questions to settle* gains `- Not chosen:`, one line per way shown and not chosen, with the cost the question gave it or the human's reason; a row's *Source* points to that question, or holds the ways itself for a choice made outside *Questions to settle*.
- `elements/decisions/template.md`: `*Rejected:* <…> | none considered | unknown`; what `none considered` and `unknown` each state; the rule for the *Rejected* of a decision written from a task row, which a derived way never enters.
- `task-cycle/skill/foundation_step.md`: a decision's *Rejected* no longer raises a question to the human; the step names its three values.
- `elements/decisions/skill/SKILL.md`: the line restating that `none considered` is the human's statement is gone; the rule stands in the template alone.
- Refinement writes and transfers the ways with the answer: `project-level/task/skill/resolve_gaps.md`, `final_review.md`, `orchestrated_mode.md`, `elements/common/skill/SKILL.md` (step 4, task variant), `project-level/lead/skill/SKILL.md`, `project-level/lead/conversation_template.md`, `project-level/lead/answering.md`, and the three guideline skills `product-guidelines/coding|styleguide|testing/SKILL.md`.

## What this request settles

- **WAY-134** (changed; written from row 1 of the task's *Settlements to record*): „Zadanie trzyma warianty pokazane człowiekowi i niewybrane — pod odpowiedzią w *Questions to settle* albo, gdy wybór padł poza tą sekcją, w *Source* wiersza — a cykl wpisuje do *Rejected* decyzji zapisanej z wiersza tylko te warianty, `none considered`, gdy człowiek tak powiedział, albo `unknown`, bez pytania człowieka i nigdy wariantu wywiedzionego przez piszącego.”
- **WAY-154** (changed by the search of the foundation, within the task's To do 4): „Plik rozmowy doprecyzowania prowadzonego przez lidera projektu kasuje się dopiero, gdy w dokumencie zadania przetrwały też warianty niewybrane przez człowieka, a refiner przenosi je razem z odpowiedzią.”

No invariant test, surface or *Violated* mark changes.

## Checks

- `python -B gate/run_tests.py` on the final tree `03411a5`: exit **0** — 613 tests in 8 directories, every directory passed; 5 skipped in `instruction-files` (four need POSIX, one a FIFO), not counted as passed. A first run on that tree was stopped by the harness for low system memory and is not counted.
- Before the correction, the same command on `c6ee066`: exit 0, 613 tests.
- On the base `d7a205c` every directory passes.
- Own-work check (author): a decision with `*Rejected:* unknown` passes `elements/common/foundation_check.py` (exit 0), and removing the field fails it (exit 1) — the check reaches the field.
- Not checked: no test reads the prose changed here; the change is checked by the reviews, not by a test.

## Review findings not fixed

Minor, from the review of the whole change (`04-review-report.md`): "The own-work check aimed at the strongest point, not the weakest. The author checked that a decision with `*Rejected:* unknown` passes `foundation_check.py` — something the task's *Context* already established and the script's presence-only check makes near-certain. The weaker points of this change are coverage (every place that writes, transfers or checks an answer carries the ways — Minors 3 and 4 show two it missed) and the fidelity of WAY-134's extended sentences to row 1." No place in the code.

The other four Minor findings of that review are fixed: the two on `project-level/lead/answering.md` and the guideline skills by the return step (`c6ee066`), and the two on `elements/decisions/skill/SKILL.md:36` and `task-cycle/skill/foundation_step.md:22–24` by the correction on the human's remarks (`03411a5`, review `13-correction-review-report.md`: PASS, no findings).

Outside the task's scope: none.

## Questions

None.

Other choices made in the cycle: 3, in the record's questions table. Human actions: none.

Cycle record: `cycle.md` in the commit that adds this record. Please merge with a merge commit so that the record's link survives.

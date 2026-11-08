# Handoff — the one author

Delegation: the person who requested this cycle delegated every intermediate choice to the
orchestrator; nothing below is that person's approval. The human reviews the pull request only.

Worktree (work only here, from its root): `the root of the worktree`
Branch: `task/guidelines-no-inventory`, base `deded3fd297a862e0160611827c564f95bb9037a` (target `foundations`).
Do not touch the main checkout or any other worktree. Commit your work on this branch.

Method: read `task-cycle/change/SKILL.md` whole, variant **"the whole change as the one author"**.
Read any file it names only when the step that names it comes. The foundation step is
`task-cycle/skill/foundation_step.md` (read whole); the return step is taken later by you on resumption,
with its own handoff. Write entries through the pinned skills of their elements:
`elements/decisions/SKILL.md`, `elements/environment-facts/SKILL.md` (each read whole, with the element's
`template.md`, `elements/common/rules.md` and `elements/common/way_of_working.md`, as those skills give).

Frozen task (read whole): `.runs/task-cycles/guidelines-no-inventory/task.md`
(original: the task's note in the author's private backlog; `Status: ready for cycle`, updated 2026-11-08).

Answers of step 4:
- Trust boundary: no. Irreversible operation: no.
- Open design choice: none. Rows 1, 2 and 3 of *Settlements to record* are accepted and settle their
  entries; their meaning is the row's, their wording yours (WAY-134). Row 2 is carried by the task's
  *To do* 2 / question 5: a sentence in the shared template `product-guidelines/template.md` saying
  that a rule of a product's guidelines neither lists the state of the code or the product nor repeats
  a decision or a value taken from a configuration file. Skills of the guidelines get no new search
  step (row 2).
- Route: one author without a plan. Your class: same as the orchestrator's.

What to produce (the task's *To do*):
1. A decision of the-way's log `foundations/decisions.md` (new identifier, next free number) for row 1
   (and the part of row 2 that says the product's own task cleans existing guidelines), with the
   *Based on* / *Rests on* link the environment fact of row 3 supports where its template gives it.
2. The sentence/rule of row 2 in `product-guidelines/template.md`, citing that decision.
3. The environment fact of row 3 in `foundations/environment_facts.md`, through
   `elements/environment-facts` (its template decides the form, the source and what counts as a
   citation; take values from the sources only — the task cites request #68 of the product `loop2`;
   if the template needs a source you cannot read, return `blocked` with the question instead of
   inventing a value).
4. The search of the whole foundation that `way_of_working.md` step 2 gives, and the corrections it
   finds (e.g. entries naming WAY-168/171 or the template, `Where guidelines go` etc.), in the same
   change. Check WAY-130's *Scope* wording against the new decision as the task says.
5. `python -B elements/common/foundation_check.py` from the worktree root passes. Do not run the
   product's gate (`gate/run_tests.py`); the orchestrator runs it. Run focused tests of any directory
   you touch with `python -B gate/run_tests.py <directory>` only if you change a file with tests.

Foundation entries to read by identifier (selected by "Reading the foundation"): the task's
*Decisions in play* — WAY-168, WAY-169, WAY-171, WAY-172, WAY-173, WAY-213, WAY-130, WAY-100, WAY-271
(and WAY-272–276 for the six rules on failures and logs, `product-guidelines/coding/template.md`) —
plus the decisions whose *Scope* names `decisions`, `environment-facts` or `product-guidelines` that
your search finds, the parts' entries of `foundations/part_map.md`, invariants whose *Part* names them,
and the glossary terms you use. The-way has no `guidelines/` of its own, so no guidelines file is read.
The task's sources are inside the task document; the product `loop2` is not open to this cycle.

Report: write the full report to
`.runs/task-cycles/guidelines-no-inventory/reports/author-report.md`
as your method gives it. It must hold, for each entry, one sentence of its meaning in English and one in
Polish (the task document's language), marked `row <n>`, `projected` or `the cycle's`; checks with command
and exit code; your own-work check; **Searches not found or unclear** (`none` is an answer). Return
status, commits, one-line check result and the report path.

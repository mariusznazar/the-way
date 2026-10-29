# Author report — task `rejected-from-refinement`

**Status:** done with concerns (concerns: see "Choices" 2 and 5 — WAY-154 reworded by the search,
and the `none considered` / `unknown` meaning bullet added to the decision template).

Worktree: `C:\Storage\repos\the-way\.runs\worktrees\rejected-from-refinement`, branch
`task/rejected-from-refinement`, base `d7a205c`. Variant: the whole change as the one author.

## Commits

- `1267e73` feat: keep the ways not chosen in refinement and source a decision's Rejected from them

## Files changed (added / removed lines)

| File | + | − |
|---|---|---|
| `foundations/decisions.md` (WAY-134, WAY-154) | 45 | 22 |
| `elements/decisions/template.md` | 9 | 1 |
| `project-level/task/template.md` | 15 | 5 |
| `project-level/lead/conversation_template.md` | 8 | 5 |
| `project-level/lead/skill/SKILL.md` | 5 | 3 |
| `elements/common/skill/SKILL.md` | 4 | 2 |
| `task-cycle/skill/foundation_step.md` | 4 | 2 |
| `project-level/task/skill/resolve_gaps.md` | 3 | 1 |
| `project-level/task/skill/final_review.md` | 2 | 1 |
| `project-level/task/skill/orchestrated_mode.md` | 2 | 1 |

## What each item of the task became

- **Row 1 / Q2 — WAY-134 extended** (still three binding sentences, WAY-05):
  - sentence 1: the task document keeps, where the human chose among ways shown, each way not
    chosen — under the answer to its question, or, for a choice made outside the task's questions,
    in the source of the row it settles (Q1);
  - sentence 3: the cycle gives a decision written from a row as its rejected options only the ways
    not chosen that the row's source keeps, `none considered` where the human said so, or
    `unknown`; the blocked-draft-request question now covers only "any other value" the row and
    the work do not give;
  - *Verification*: one complies example (two ways kept → two rejected options; none kept →
    `unknown`, no question) and three violates examples (choice kept without its ways; options
    derived from the guess column; request blocked to ask for them);
  - *Rationale*: why the ways must outlive the conversation and why a derived option is worse than
    `unknown` (from the task's *Need*);
  - *Rejected*: added the ways not chosen of Q1 and Q2, translated from their *Not chosen* lines
    with the costs those lines give — the row's *Source* for every choice; the templates alone;
    part of WAY-29; a decision of its own. Nothing was added from the row's guess column (the new
    rule applied to its own entry). Earlier rejected options kept unchanged.
  - Meaning, one sentence in Polish for the request: „Zadanie trzyma warianty pokazane człowiekowi
    i niewybrane (pod odpowiedzią w *Questions to settle* albo, gdy wybór padł poza tą sekcją,
    w *Source* wiersza), a cykl wpisuje do *Rejected* decyzji zapisanej z wiersza tylko te warianty,
    `none considered`, gdy człowiek tak powiedział, albo `unknown` — bez pytania człowieka
    i nigdy wariantu wywiedzionego przez piszącego.”
- **To do 1** — `project-level/task/template.md`: the *Questions to settle* form gains
  `- Not chosen:` with one sub-line per way (`<way> — <cost the question gave it, or the human's
  reason>`); the section rule says when it appears, that a transferred or canonical answer brings
  its ways along, and the *Settlements to record* rule says *Source* points to that question, or
  holds the ways itself for a choice made outside *Questions to settle* (e.g. the question against a
  choice while candidates are cut), and that a decision's *Rejected* is taken from them; the
  "survive removal of a conversation" sentence now includes the ways.
  `project-level/task/skill/resolve_gaps.md` (manual refinement writes answers there) and
  `elements/common/skill/SKILL.md` step 4, task variant (the question against a choice writes its
  ways into the row's *Source*) point to the template rule. `final_review.md` checks it.
- **To do 2 and 3** — `elements/decisions/template.md`: syntax `*Rejected:* <…> | none considered
  | unknown`; a bullet saying what `none considered` and `unknown` each state; a bullet with the
  rule for a decision written from a task row, its exclusion of derived ways (guess column, cost of
  the chosen way, foundation) and "written with no question to the human" (WAY-35: the rule stands
  in the template, the skill unchanged). `task-cycle/skill/foundation_step.md`: the "value neither
  the row nor the work gives" question now excepts a decision's *Rejected*, pointing to the
  template.
- **To do 4** — `project-level/task/skill/orchestrated_mode.md` (refiner transfers the ways with
  the answer), `project-level/lead/skill/SKILL.md` step 3.6 (transfer) and step 4 (check before
  deleting the conversation file), `project-level/lead/conversation_template.md` (refiner duty,
  canonical answer copy, *Transferred:* field, check before removal).

## Search of the whole foundation (WAY-33) and return step

Searched `foundations/` for `Rejected`, `none considered`, rejected options, `unknown`, blocked
draft request, conversation removal, and every reference to WAY-134; read whole each hit that could
be touched: WAY-05, WAY-11, WAY-29, WAY-118, WAY-124, WAY-154, WAY-155, WAY-172, WAY-227, WAY-242.

- **WAY-154 corrected** (binding + one violates example): the refiner transfers answers "with their
  sources and the ways the human did not choose (WAY-134)", and the conversation is removed only
  after "all settled answers, their sources and the ways not chosen survive". Without it, WAY-154's
  deletion condition would still allow removing the conversation while the ways live only there.
  Meaning for the request: „Plik rozmowy doprecyzowania kasuje się dopiero, gdy w dokumencie zadania
  przetrwały też warianty niewybrane przez człowieka.” This is within To do 4; I judged it not a
  meaning change beyond the task (README: such goes to Mariusz) — the orchestrator may judge
  otherwise.
- WAY-29 untouched (recovered decisions; consistent: its `unknown` and its refusal of inferred
  rejected options are the same family). WAY-124, WAY-155, WAY-118 (projected decisions —
  out of the task's reach), WAY-172, WAY-227, WAY-242: no collision, no edit.
- No invariant, glossary term, environment fact or part-map entry touched; no file added, so the
  part map needs no change. Return step: WAY-134 and WAY-154 now match the templates and skills
  that carry them.
- `project-level/definition_template.md:323` (projected decisions: `none considered` is the human's
  statement) left as is — projects are outside this task.

## Checks

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` (after edits, and after commit-ready state) | 0 (0 errors) |
| `python -B gate/run_tests.py elements/common` | 0 (109 tests OK) |
| `python -B gate/run_tests.py agent-instructions` | 0 (18 tests OK) |
| line-width check of added lines (`git diff -U0` filtered for > 100 columns) | none left |

Not run: the full gate `python -B gate/run_tests.py` (the orchestrator's, per handoff);
`project-level`, `installation`, `instruction-files`, `gate` directories — no test there reads the
changed passages (searched test files for the edited files' names and phrases; none found), so I
left them to the full gate. No test was written: the change is prose for agents and templates;
`foundation_check.py` needed no change (the task's *Context* says so; confirmed below).

## Own-work check (WAY-164)

Requirement most likely not met: To do 3 — a decision whose *Rejected* reads `unknown` must pass
the foundation's form check, since the cycle will now write it without asking.
Check: in the worktree, temporarily set WAY-154's *Rejected* to `*Rejected:* unknown` and ran
`python -B elements/common/foundation_check.py` → exit 0, 0 errors; then removed the line →
exit 1, `foundations/decisions.md:4022: the entry lacks *Rejected*` (the check reaches the field);
restored the file from a copy → `git diff --stat` identical to before (45/22), check exit 0.
Result: `unknown` passes without a script change.

## Reaches beyond the dispatch

- `elements/common/way_of_working.md`, `elements/common/rules.md`, `elements/decisions/skill/read.md`,
  `decide_entry.md`, `examples.md` — step 1 of the record-decision skill requires them.
- `project-level/task/skill/SKILL.md`, `draft.md`, `final_review.md`, `find_settlements.md`,
  `project-level/lead/answering.md`, `task-cycle/skill/SKILL.md` (lines 86–100),
  `task-cycle/skill/return_step.md` — to find every place that writes, transfers or checks answers.
- `elements/common/foundation_check.py:415–444` and its docstring — to confirm `unknown` passes.

## Choices, with the way rejected and its cost if wrong

1. **Placement in WAY-134**: folded into sentences 1 and 3 rather than adding a fourth sentence
   (WAY-05 caps at three). Cost if wrong: sentences 1 and 3 are now longer (the weak point named in
   Q2); a reader may find sentence 3 hard to parse.
2. **WAY-154 edited** rather than left for WAY-134 to carry alone. Rejected: leave WAY-154 —
   its deletion condition would contradict the lead skill's new check. Cost if wrong: a meaning
   change to an approved decision the orchestrator may want shown to Mariusz as such.
3. **Format of *Not chosen***: a sub-list, one way per line, as To do 1 says ("każdy w jednej
   linii"), not one line joined by semicolons as the task document itself uses. Cost if wrong: one
   more indentation level in the template.
4. **`final_review.md` gets a check** of the ways, mirroring the lead's check in orchestrated mode.
   Rejected: no check in manual mode. Cost if wrong: one clause more in that step.
5. **New template bullet on the meaning of `none considered` and `unknown`**. The record-decision
   skill already says `none considered` is the human's statement; I left that line (pre-existing,
   WAY-35 question not mine). Cost if wrong: a slight duplication between skill and template.
6. WAY-134 *Relations* and WAY-154 *Relations* unchanged; WAY-154 names WAY-134 inline only.

## Problems observed

- `elements/decisions/skill/SKILL.md:54–55` — the line "In projected mode, read `projected.md`
  beside this skill …" stands inside the bullet list of projected mode, between two step bullets
  (pre-existing at `d7a205c`, not touched).

# Plan — the way: wpisać przejęcia z lekcji m1l5 kursu 10xDEVS

- Task: `.runs/task-cycles/m1l5-adoptions/frozen_task.md`
- Spec: none
- Base: 7335b5f (`foundations`)

## Foundation entries

| Entry | Kind | From | What depends on it |
|---|---|---|---|
| WAY-137 — agent-friendliness (terminal operation, scriptable deployment, documentation an agent can read) as the last tie-breaker for a place to run, after WAY-123's simplest-and-cheapest rule still leaves a tie; never a filter or a weight; `narrows WAY-123`, WAY-123 unchanged; names the borrowed practice and why (WAY-100) | decision (new) | row 1; orchestrator Q2 | Slice 1 |
| WAY-138 — "what will this break" tests (devil's advocate, pre-mortem, unknown unknowns) on the recommended option, only for choices this project settles, those taken from a constraint included, never on `held by` choices and never backfilled; risks are hypotheses without a source, not claimed differences between options, shown before the choice beside the recommended option; the option chosen takes its risks, which reach its decision through the lacks of the chosen option, marked as hypotheses; *Review when* from row 2's scope condition with a check-by date of 2026-12-31 (WAY-24); names the borrowed practice and why (WAY-100) | decision (new) | row 2; orchestrator Q3 | Slice 1 |
| WAY-139 — the-way holds no product skills, only the list of what a product's deployment skill has (preview of deployments; where secrets lie and how they are rotated; rollback — how many steps, what happens to data; what the agent does and what the human does; how to read logs), in its binding sentence; `refine-task`, for a task whose outcome deploys the product or changes how and where it runs, checks that the product has a deployment skill covering the list, and where none does or an element is missing, the task gets that item or the human splits it into a task of its own | decision (new) | row 3; orchestrator settlement on row 3 | Slice 2 |
| WAY-140 — an effect of a task outside the repository (server, DNS, keys, an external account) is a human action the task document names, placed before the cycle (the task is not ready until it is done) or in the cycle (the cycle does what the repository allows and returns a blocked draft request listing the actions, which the human performs at the request); reads outside the repository stay with the agent; the human places each action at refinement, the agent proposing "before" when the cycle's code needs the action's effect and "in the cycle" when the action uses code the cycle writes | decision (new) | rows 4 and 5; orchestrator Q4 | Slices 2, 3 · WAY-124 edit |
| WAY-124/1 edited in place — readiness gains the condition that every human action the task document places before the cycle is done, citing WAY-140 as it cites WAY-134, with `derives from WAY-140@<fingerprint>` added to *Relations* and its verification examples extended; binding part changes, so its fingerprint changes: today no decision relation and no invariant carries `WAY-124@` (grep of `foundations/`), which the foundation step confirms after the edit (WAY-31); shown for renewed acceptance at the merge (WAY-07) | decision (edit, change of meaning) | row 4 (To do 4, first sub-item); orchestrator Q4 | Slices 2, 3 |

Order of writing: WAY-137, WAY-138, WAY-139, WAY-140, then the WAY-124 edit (it carries WAY-140's
fingerprint). Each new entry and the edit take *Approved by* `Mariusz, merge of <request link>` and
*Based on* `none`; fingerprints for *Relations* come from `relation-model/fingerprint.py`. Checks of
the foundation step: `python -B elements/decisions/format_guard.py --base none --merge-onto none`,
`python -B gate/run_tests.py elements/decisions`, `python -B gate/run_tests.py gate`, and a grep
of `foundations/` for `WAY-124@`. WAY-123 and WAY-125 stay unchanged. No invariant, glossary term,
environment fact or part-map change is written (see *Choices*).

## Slices

### Slice 1 — technology step carries the tie-breaker and the "what will this break" tests

- **Goal:** the Technology section's rules in `definition_template.md` state WAY-137 and WAY-138
  beside the WAY-123 bullet; `settle-technology` step 5 forms each recommendation, applies the
  tie-breaker of WAY-137 to a place to run, has one fresh agent per wave run the three tests on
  every recommended option of a choice settled in this project (never a `held by` choice), passes
  the table's contradiction critique the risks marked as hypotheses rather than claimed
  differences, and shows the risks beside the recommended option; step 6 says that choosing an
  option takes its risks; step 7 hands the accepted risks to `record-decision` with the lacks of the
  chosen option, marked as hypotheses; `record-decision`'s projected mode says in which field the
  lacks and the accepted risks of a chosen option stand (*Rationale*, a risk marked as a
  hypothesis, never in *Based on*).
- **Change:** `project-level/definition_template.md` · `project-level/technology/SKILL.md` ·
  `elements/decisions/skill/SKILL.md`
- **Read:** `foundations/decisions.md:2769-2794` · `foundations/decisions.md:3158-3193` ·
  `foundations/decisions.md:3371-3537` · `elements/decisions/template.md` ·
  `elements/common/way_of_working.md:1-60` · `elements/common/critique/SKILL.md`, and the entries
  WAY-137 and WAY-138 the foundation step appends at the end of the decision log
- **Checks:** `python -B gate/run_tests.py project-level` · `python -B gate/run_tests.py
  elements/decisions` · `python -B gate/run_tests.py gate` · `python -B
  agent-instructions/skill_entry_points.py` (entry points still current: no description changes);
  no script's behaviour changes, so no test is written first
- **Depends on:** WAY-137 · WAY-138

### Slice 2 — task refinement names human actions and checks the deployment skill

- **Goal:** `project-level/task/template.md` gives the task document a section, always present
  (`none` where the task has no effect outside the repository), that names each human action with
  its placement — before the cycle, with whether it is done, or in the cycle — and its rule under
  "What each section carries" (WAY-140, WAY-124), and says that a document written before the
  section existed names none; `refine-task` names each effect outside the repository as a human
  action, proposes its placement by WAY-140's rule and has the human place each; for a task whose
  outcome deploys the product or changes how and where it runs, checks the product's deployment
  skill against WAY-139's list and adds the item or offers the split; and its step 6 check requires
  every action placed and every action before the cycle done before `Status: ready for cycle`.
- **Change:** `project-level/task/template.md` · `project-level/task/skill/SKILL.md`
- **Read:** `foundations/decisions.md:3538-3622` · `foundations/decisions.md:3942-3989` ·
  `elements/common/way_of_working.md:1-60` · `.runs/task-cycles/m1l5-adoptions/frozen_task.md`,
  and the entries WAY-139 and WAY-140 the foundation step appends at the end of the decision log
- **Checks:** `python -B gate/run_tests.py project-level` · `python -B gate/run_tests.py gate` ·
  `python -B agent-instructions/skill_entry_points.py`; no script's behaviour changes, so no test
  is written first
- **Depends on:** WAY-139 · WAY-140 · WAY-124 edit

### Slice 3 — task cycle never makes an effect outside the repository itself

- **Goal:** `implement-task` states WAY-140: lines 15–21 add the human action in the cycle beside
  the decision reserved to a human; step 1 requires every human action the task document places
  before the cycle to be done (WAY-124); the paragraph at line 46 keeps writes to the repository
  and allows reads outside it; step 4 (lines 63–69) replaces "when the product's rules reserve its
  authorization" with WAY-140's rule — the cycle prepares what the repository allows and returns a
  blocked draft request listing the actions in the cycle, and an effect the document does not name
  goes into that list for the human to place; steps 12–13 keep that request a draft and list the
  actions in it; `task-cycle/record_template.md`'s *Request handoff* gains the line for the human
  actions the request waits for.
- **Change:** `task-cycle/skill/SKILL.md` · `task-cycle/record_template.md`
- **Read:** `project-level/task/template.md` · `foundations/decisions.md:3538-3622` ·
  `foundations/decisions.md:3942-3989`, and the entry WAY-140 the foundation step appends at the
  end of the decision log
- **Checks:** `python -B gate/run_tests.py task-cycle` · `python -B gate/run_tests.py gate` ·
  `python -B agent-instructions/skill_entry_points.py`; no script's behaviour changes, so no test
  is written first
- **Depends on:** Slice 2 · WAY-140 · WAY-124 edit

## Coverage

| What the task requires | Slices or entries |
|---|---|
| To do 1 — agent-friendliness as the last tie-breaker for a place to run, WAY-123 unchanged | WAY-137 · Slice 1 |
| To do 2 — "what will this break" tests on the recommended option, scope, `held by` untouched, risks before the choice, accepted risks through the lacks channel as hypotheses | WAY-138 · Slice 1 |
| To do 3 — list of a product deployment skill's elements in a binding sentence; `refine-task` checks it | WAY-139 · Slice 2 |
| To do 4 — effect outside the repository as a human action before or in the cycle; readiness; blocked request with the list; placement by the human with the agent's proposal; reads stay with the agent | WAY-140 · WAY-124 edit · Slices 2, 3 |
| To do 5 — each adoption in the decision log with the skills and templates that carry it | WAY-137–WAY-140 · WAY-124 edit · Slices 1–3 |
| To do 6 — vault map update after the merge | out of the cycle (human action after the merge, orchestrator's dispatch) |
| Question 0 — one task | the plan covers all four adoptions in one change |
| Question 1 — list in a binding sentence, read by refinement | WAY-139 · Slice 2 |
| Question 3 — no pause in the cycle; blocked request; placement by the human | WAY-140 · Slices 2, 3 |
| Row 1 | WAY-137 |
| Row 2 | WAY-138 |
| Row 3 | WAY-139 |
| Row 4 | WAY-140 · WAY-124 edit |
| Row 5 | WAY-140 |

## Choices

| Choice | Way rejected | Cost if wrong |
|---|---|---|
| Identifiers in task order: WAY-137 row 1, WAY-138 row 2, WAY-139 row 3, WAY-140 rows 4–5 | another order | none; numbers only |
| The rules of rows 1–2 go into the Technology section of `definition_template.md`, the order of the work into `settle-technology` steps 5–7, as the skill divides them today | rules in the skill alone | the template and skill drift; caught by slice review |
| One fresh agent per wave runs the three tests on every recommended option of the wave, after the recommendations and before the table's contradiction critique | the step's own agent runs them; one agent per choice | own agent: a weaker devil's advocate attached to its recommendation; per choice: more agents for no gain |
| The table's contradiction critique is told the risks are hypotheses, so it does not strike them for lacking a source; `critique/SKILL.md` unchanged | a rule in the critique skill | none beyond one sentence in step 5; the critique skill stays general |
| `record-decision` projected mode names *Rationale* as the field for the lacks and accepted risks of a chosen option, each risk marked as a hypothesis | leaving the field unnamed, as for lacks today; *Review when* | unnamed: a risk could land in *Based on* and read as a sourced fact; *Review when* is for a prediction the decision rests on, which a risk is not |
| The task template's human-action section always appears, `none` included | a section only when it has content | one line in every task; without it the reader cannot tell "no effect outside" from "not looked at" |
| An effect outside the repository the task document does not name, found by the cycle, joins the blocked request's list for the human to place | stopping the cycle as not ready | the human meets it at the request rather than before the cycle |
| No glossary term: "human action", "deployment skill" and "place to run" carry the meaning a reader of the field gives them, and WAY-95 counts only binding parts, element templates and the elements' common part (WAY-95) | entries for them | a second meaning later goes unnoticed until a search of the foundation |
| No part-map change: no file is added, and failure modes are written by a human (`elements/part-map/template.md:184`); the request may propose one | the cycle writes a failure mode | a known failure stays unrecorded until the human writes it |
| WAY-122 unchanged: its *Rationale* speaks of weighing, and the tie-breaker acts only once weighing leaves a tie | an edit of WAY-122's rationale | the independent assessment may flag the sentence; then an unchanged-sentences edit |
| Entry points not regenerated: no skill description changes | running `--write` | none; the check confirms them current |
| *Origin* `none` for WAY-137–WAY-140: the vault map is outside the repository | *Origin* pointing to the vault map | a product reader cannot follow the reasoning beyond the entry |

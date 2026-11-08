PASS 3cf2a09b9dca6ed46eba30800e69863a7d010006

# Review of the whole change — decisions as material at refinement

Reviewer: `review-change`, review of the whole change. Range `354d37d56403b6f898155cb706efcb74f316c97a..3cf2a09b9dca6ed46eba30800e69863a7d010006` (commits `8316d28`, `3cf2a09`). `git rev-parse HEAD` returned `3cf2a09b9dca6ed46eba30800e69863a7d010006`, the head of the handoff. No file of the repository was changed by this review; `git status --short` was empty after the checks.

Counts: blocking 0, Minor 4 (all within the task), out of scope 0.

## Findings

### Critical

none

### Important

none

### Minor

All four lie within the task's scope; none lies outside it.

1. **A step at the start of a definition still asks whether the decision changes.**
   Place: `project-level/skill/read_foundation.md:8-10` ("For a decision, ask whether the decision changes or the project fits it (WAY-30)") and its source decision WAY-111 in `foundations/decisions.md` (the sentence "asks whether the project changes an existing decision or fits it", and the *Verification* line "shows the touched decision and boundary and asks whether the project changes or fits it").
   What is wrong: acceptance criterion 2 says that where refinement changes one decision of the foundation, the human consents once and no step asks again before the acceptance of the whole document. In a definition the human is first asked at this step whether the decision changes; later the option that changes it is shown and chosen (WAY-314), and a decision row of the candidate table follows. The author judged the first question a scoping question (author report, "Weakest points" 2). It is asked before any concrete option exists, so it may be read as direction, not consent; but the text neither says so nor drops the question.
   Why it matters: this is the pattern the task set out to remove (several asks on one change), and the wording leaves a reader free to count this ask as one.
   Evidence: the file read in full; `grep -rn "fits it" project-level foundations` finds only these two places; the change touches neither.
   Grade reasoning: Minor, because the question does not name an option or take a consent, and the task's *To do* names no such place. It would be Important if the orchestrator reads criterion 2 to cover it. Suggested fix: one clause in both places saying the question only frames the conversation and the consent is the choice of the option (WAY-314), or turn it into the shown-option form.

2. **The rule of the question against an answer is ambiguous for a definition's entry writing.**
   Place: `elements/common/way_of_working.md:36-40` and WAY-113 in `foundations/decisions.md` (the added sentence: "...in a task's cycle and where an entry is written it is asked as above, the looser rule holding only before the cycle starts").
   What is wrong: "while a project definition ... is refined, the technology step included, the question is asked only where the answer contradicts a sentence the human said earlier" and "where an entry is written the question stands as the bullet above gives it" can both apply to step 4 of `definition_variant.md`, where entries of a definition are written (handed to `record-decision` and the other element skills in projected mode) during the definition's refinement. A reader cannot tell which wins. Task point 3 itself asks for exactly this pair ("w definicji projektu ... zostaje tylko dla dwóch zdań człowieka" and "przy zapisie wpisów fundamentu zostaje jak dziś"), so the ambiguity is inherited, but the change writes it into the binding sentence without settling it.
   Why it matters: the agent writing a definition's entry may ask the full question where the task wanted none, which is the repeated question the task complains of; or the reverse.
   Evidence: reading of the three places together; `definition_variant.md` step 4 item 3 hands rows to the element skills, which read "How a skill asks".
   Suggested fix: say in WAY-113 and `way_of_working.md` which wins at a definition's step 4 (for example "where an entry is written outside the refinement of a definition or a task").

3. **WAY-165 makes opening mandatory where WAY-313 only permits it.**
   Place: WAY-165 in `foundations/decisions.md` (the sentence "in a run at a task (WAY-267) the step opens a decision of the foundation that leaves part of it unanswered as it opens any such decision (WAY-313)" and the *Verification* clause "an agent leaves, in a run at a task, a logs decision silent on the record's life `— held by` until the human says a word"); `project-level/technology/task_run.md:50-58` ("...is such a reason: its item stands `— open` here as at a definition").
   What is wrong: the task asks to drop the reservation "opens only on the human's word" from WAY-165 and WAY-267. WAY-313 and WAY-267 say the step opens a held choice "where it sees a reason" (permissive). For a decision silent on a matter of the logs, interface or development data, WAY-165 and `task_run.md` go further: the item must stand `— open`, and keeping it `— held by` is a violation. Files and entry agree with each other, so there is no WAY-263 mismatch; but the strengthening is the author's choice (author report, "Choices I made"), not a row of the task. It also contradicts nothing in the task, since a silent decision settles nothing at a definition either.
   Why it matters: a run at a task that touches the logs now always adds an item over a silent decision, which grows the human's list; the human can strike it from the list (the added one-sentence reason), so the cost is one strike.
   Evidence: reading WAY-165, WAY-267, WAY-313 and `task_run.md`; `git diff 354d37d..3cf2a09 -- foundations/decisions.md`.
   Suggested fix: either keep it and name the choice in WAY-165's *Rationale* as a deliberate step beyond WAY-313, or word the clause as "may open" and drop the *Verification* violation.

4. **Wrapping and line-length polish in the added text.**
   Places: `project-level/technology/running_product.md:40` (152 characters, a sentence of the added clause glued into one line); `project-level/task/skill/orchestrated_mode.md:48` (146 characters, "Likewise, only the human places Human actions and confirms completion." appended to a long line); `project-level/task/skill/resolve_gaps.md:18-19` (a line break after "All this" leaves a one-clause line); `foundations/decisions.md` WAY-165 *Verification* and WAY-267 added lines over 100 characters (the lines at 3399, 4739-4744 and 8040 of the head).
   What is wrong: the neighbouring text is wrapped at 100 characters; these lines are not. `git diff --check` is clean, so this is polish only.
   Evidence: `awk 'length($0)>100'` over the changed files.

## Against the task (the whole)

Method: each item of *To do*, each acceptance criterion, each answer of *Questions to settle* and each row of *Settlements to record* was checked against the commits.

- To do 1 (technology step: the agent may open a held choice, the present answer stands as one option, the changing option says so in its line, the human's choice is the only consent): met in `project-level/technology/task_run.md` (*List*), `list.md` ("find what settles it"), `running_product.md` ("The agent opens no decision..." replaced), `settle.md` sub-steps 5 and 6, `SKILL.md`, `project-level/definition_template.md`. The reason sentence the list shows for an item opened over a decision is a strike-able list line, not a leave asked before the comparison.
- To do 2 (options that change a decision shown like any other, with the decision named, a recommendation allowed, the choice as consent; the document carries the change per WAY-30; a definition makes a projected change; a projected decision of an approved definition stays outside): met in `resolve_gaps.md`, `carry_foundation.md`, `find_settlements.md`, `task/template.md`; the old "route that change to its own process" and "reopen the upstream settlement" for a foundation decision are gone; the projected-decision case still goes to the definition and WAY-118.
- To do 3 (question against an answer only for a quoted earlier sentence of the human; unchanged in the cycle and at entry writing; collision move narrowed): met in `way_of_working.md`, `task_variant.md` step 4, `settle.md` sub-step 6, `definition_variant.md` step 4, `lead/skill/SKILL.md`, `orchestrated_mode.md`; see Minor 2 for the one ambiguity.
- To do 4 (a row repeating a human's choice among shown options enters accepted, marked, strikeable; the human cuts only derived rows): met in `elements/common/skill/SKILL.md` step 3, `build_table.md`, `definition_variant.md`, `task_variant.md`, `find_settlements.md`, `orchestrated_mode.md`, `task_run.md` (the settled question as such a row). Note: `find_settlements.md` extends "a choice between shown ways" to "an answer under *Questions to settle* that keeps its *Not chosen*"; this follows the task's row 4 (the answer under a question that showed ways), so it stays within the task.
- To do 5 (decisions say the same): WAY-165 and WAY-267 without the reservation, with *Rationale* and *Verification* (Minor 3); WAY-113 per question 2; WAY-115, WAY-124, WAY-134 per question 3. All present in `8316d28`.
- To do 6 (binding stays in the cycle; the boundary is the cycle's start, the spec included; the files of points 1-4 say their looser rules hold only before it): WAY-315 and a short clause in each of the files of points 1-4 (`SKILL.md`, `build_table.md`, `task_run.md`, `list.md`, `settle.md`, `running_product.md`, `resolve_gaps.md`, `carry_foundation.md`, `find_settlements.md`, `way_of_working.md`, `definition_variant.md`, `task_variant.md`). No file of `task-cycle/` carries the old reservation; it is untouched and needs no change.
- Acceptance criterion 1: no skill file or decision keeps "an agent never opens one", "opens only", "route that change", "reopen the upstream settlement" (grep below). Criterion 2: see Minor 1 for the one step that still asks at a definition's start; otherwise one consent (the choice of the option; `final_review.md` unchanged and asks nothing about the change).
- Questions 1-5: the answers are carried as WAY-314 (q1), WAY-113 (q2), WAY-115, WAY-124, WAY-134 (q3), WAY-315 (q4) and the projected-decision carve-out in WAY-313, `resolve_gaps.md`, `carry_foundation.md`, `task_run.md` (q5). The weak points the answers accept appear in the *Rationale* of the entries as prices.
- Settlements 1-5: row 1 = WAY-313 (*Rejected: unknown*, the source of the row keeps no way not chosen, which `foundation_check.py` accepts); row 2 = WAY-314 (*Rejected* the one way of question 1); row 3 = WAY-113 (both ways of question 2 added to *Rejected*); row 4 = WAY-115, WAY-124, WAY-134 (both ways of question 3); row 5 = WAY-315 (the one way of question 4). Each entry's binding sentence says what its row says. WAY-314 adds "or the approval of the projected entries at the readiness gate of a definition" to row 2's "akceptacja dokumentu"; this follows To do 2 ("w definicji zmiana staje się rzutowaną zmianą decyzji") and is not a broader claim than the task. WAY-138 and the word "opened" in WAY-267 *Verification* were adjusted ("the human opened" to "the step opened") — a consequence of the changed rule, not an extra rule.
- Fidelity: no quotation or figure of the task was altered; the examples of WAY-313/314/315 *Verification* (a month against a week) are illustrations, not data claims.
- WAY-123 (options in one message, not a table): not undone. `settle.md` sub-step 5 adds only a sentence to the same message; `list.md` adds a sentence per opened item to the list message. No table of options was introduced.
- Nothing is added that nobody asked for beyond Minor 3 (mandatory opening over a silent decision) and the extension of the marked rows to the definition's table (WAY-115), which To do 5 names.

## Against the foundation and the invariants

Parts touched: `decisions`, `elements-common`, `project-level`. Entries read whole: WAY-14, WAY-30, WAY-111, WAY-113, WAY-115, WAY-124, WAY-134, WAY-138, WAY-165, WAY-267, WAY-313, WAY-314, WAY-315 (at head). Invariants of these parts, read whole: `skill-rule-source`, `project-definition-form`, `project-readiness-gate`, `project-technology-record` and the `every` ones; none is contradicted. No invariant test was changed. The Technology list form in `definition_template.md` (markers `— open`, `— held by`, `Changes:`) keeps the shape that `project-technology-record` checks (a choice item still names a decision as `<PREFIX>-<NN>` or a projected question); the tests of `project-level` pass.

The entries the change writes say what the files do: WAY-313 with `list.md`, `task_run.md`, `resolve_gaps.md`; WAY-314 with `settle.md` sub-step 6 and `task_run.md`; WAY-315 with the clauses of every file; WAY-113 with `way_of_working.md` (except the ambiguity of Minor 2); WAY-115/124/134 with `build_table.md` and `find_settlements.md`; WAY-165/267 with `task_run.md` (Minor 3). No file does what an entry forbids or restates it more broadly. Entries left unchanged that the change might make untrue were read by search: WAY-111 (Minor 1), WAY-139 (its *Rejected* line about rules on an agent opening a decision describes a rejected alternative and stays true), WAY-30 (stays true; its word "implementation" is fixed by WAY-315).

Guidelines: the-way has none of its own for coding, tests or a user interface; the change is Markdown only, with no script (none of the three `.py` boundary files of `project-level` touched), so nothing to compare. Reserved choices: none taken. Trust boundary: none touched. Irreversible operation: none. Tests: none were written and none of the-way reads the wording of the changed places (see the checks); the author's own-work check (grep for old reservations, a walk of the path of one decision change through the files) fits where the change is weakest, and I repeated the grep below, which would have caught an old reservation left in place. It could not catch the ambiguity of Minor 2 or the leftover ask of Minor 1, which the author named in the report.

## Declined to judge

- Whether the word "material" (a decision is "material for revision") should have a glossary entry, given that the same files use "the material" for source material: no sentence was found that a reader would read wrongly (the contexts differ), so at most a Minor, and the glossary is not part of this task.
- The collision of WAY-165 with the sibling task `the sibling task's note in the author's backlog` point 17 (not merged on this branch): the handoff says it is no finding of this change.
- The "implication" move of `definition_variant.md` step 4 (item 1): the task names only the collision move for narrowing and question 2 keeps "pytania o to, czego wpis potrzebuje"; left as the author left it.
- Whether the full gate passes: the orchestrator runs it.

## Checks run

All run in `the root of the task's worktree` on the head, no file changed (status empty afterwards).

- `git rev-parse HEAD` — `3cf2a09b9dca6ed46eba30800e69863a7d010006`, matches.
- `git diff 354d37d..3cf2a09 --stat` and `git log 354d37d..3cf2a09` — 19 files, +338/-122, two commits as the handoff says.
- `git diff 354d37d..3cf2a09 --check` — exit 0 (no whitespace error).
- `python -B elements/common/foundation_check.py` — exit 0, "0 errors".
- `python -B gate/run_tests.py project-level` — exit 0, 271 tests OK.
- `python -B gate/run_tests.py elements/common` — exit 0, 109 tests OK.
- `python -B agent-instructions/skill_entry_points.py` (check mode) — exit 0, "entry points are current".
- Grep (Grep/`grep -rniE` over `project-level elements product-guidelines task-cycle agent-instructions`, `*.md`) for `human's word|opens no decision|never opens|opens only|held by|reopen|on its own|the human opened|though a decision|human opened` — no remaining reservation of the old kind; the hits are unrelated uses (the human's words as a source, WAY-269's "human's word" for a returned task, "the language the human opened", the template's `held by` marker). One hit, `project-level/task/template.md:154`, "opened though a decision holds it", is a sentence the change rewrote to be about the option, not a leave, and is consistent.
- Grep for `WAY-113|question against|against the answer` over the repository's Markdown — every place that asks a question against an answer is one the change updated (`way_of_working.md`, `settle.md`, `task_variant.md`, `definition_variant.md`, `lead/skill/SKILL.md`, `orchestrated_mode.md`) or one that stays by the task (`audit_end.md:199`, the guidelines skills' "say in plain words", `conversation_template.md`).
- Grep of `foundations/decisions.md` for `human's word|opens only|human opens|opened though|stays the human's` — only unrelated or rewritten uses.
- Manual walk of one decision change at a task through the files in the order an agent meets them (`task_run.md` list, `settle.md` 5-6, `task_run.md` write, `find_settlements.md` row, `task_variant.md` step 4, `final_review.md`): one consent, at the choice; no second ask. At a definition, the same walk meets `read_foundation.md` step 2 first (Minor 1).
- Awk over changed files for lines over 100 characters — result in Minor 4.
- Not run: the full gate (the orchestrator runs it); `task-cycle` and `installation` and `agent-instructions` test directories (the author reports them OK; the change touches nothing they read besides `decisions.md`, which `foundation_check.py` covers), so unverified by me.

## Reach beyond the handoff

- `project-level/skill/read_foundation.md`, whole: to check whether a definition-start step asks about a decision change (Minor 1).
- `foundations/decisions.md`: WAY-111 (whole), WAY-30 (whole), WAY-165 and WAY-267 (whole, at head): to judge Minor 1 and 3.
- `project-level/technology/start.md`, `task_run.md` (whole), `project-level/task/skill/orchestrated_mode.md`, `project-level/skill/readiness_gate.md` (by search): to see whether any other place keeps the old reservation.
- `foundations/invariants.md` and `foundations/part_map.md` (by search of `Part` lines and the `task-cycle` entry): to name the invariants of the touched parts.
- `grep` over `task-cycle/` for "Decisions in play", "Changes:" and decision-change handling: to confirm that the cycle needs no change for point 6.

## Searches not found or unclear

- Not found: any test of the-way that reads the wording of the changed places (as the task said); none was expected to be added.
- Not found: a place in `task-cycle/` that carries the old reservation or needs the boundary clause.
- Unclear: whether "where an entry is written" in WAY-113 includes the entry writing of a definition's step 4 (Minor 2).
- Unclear: whether the definition-start question of `read_foundation.md` and WAY-111 counts as an ask about the change under acceptance criterion 2 (Minor 1).
- Unclear: whether the mandatory opening over a silent decision in WAY-165 at a task is intended or an outcome of "like any decision" (Minor 3).

# Author report — decisions as material at refinement

Status: `done with concerns` (concerns: section "Weakest points" and "Rulings that need the orchestrator's eye")

Branch `task/decisions-as-material-at-refinement`, base `354d37d`. Worktree clean after the commits.

## Commits

- `8316d28` Let refinement treat a decision of the foundation as material, binding from the cycle's start (`foundations/decisions.md`)
- `3cf2a09` Show options that change a decision of the foundation during refinement without asking leave (18 skill and template files)

## Files changed (added / removed lines, `git diff --numstat 354d37d HEAD`)

| File | + | - |
|---|---|---|
| foundations/decisions.md | 201 | 50 |
| elements/common/way_of_working.md | 5 | 0 |
| elements/common/skill/SKILL.md | 4 | 2 |
| elements/common/skill/build_table.md | 5 | 0 |
| elements/common/skill/definition_variant.md | 6 | 3 |
| elements/common/skill/task_variant.md | 7 | 4 |
| project-level/definition_template.md | 6 | 1 |
| project-level/lead/answering.md | 1 | 1 |
| project-level/lead/skill/SKILL.md | 3 | 1 |
| project-level/task/skill/carry_foundation.md | 7 | 5 |
| project-level/task/skill/find_settlements.md | 11 | 6 |
| project-level/task/skill/orchestrated_mode.md | 6 | 3 |
| project-level/task/skill/resolve_gaps.md | 20 | 9 |
| project-level/task/template.md | 7 | 4 |
| project-level/technology/SKILL.md | 5 | 2 |
| project-level/technology/list.md | 11 | 5 |
| project-level/technology/running_product.md | 4 | 4 |
| project-level/technology/settle.md | 13 | 9 |
| project-level/technology/task_run.md | 16 | 13 |

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — exit 0 ("0 errors"), after the foundation edits and again at the end.
- `python -B gate/run_tests.py elements/common` — exit 0, 109 tests OK.
- `python -B gate/run_tests.py project-level` — exit 0, 271 tests OK.
- `python -B gate/run_tests.py task-cycle` — exit 0, 187 tests OK (reads decisions/request files).
- `python -B gate/run_tests.py agent-instructions` — exit 0, 18 tests OK.
- `python -B agent-instructions/skill_entry_points.py` (check mode) — exit 0, "entry points are current". No `description` changed, so no `--write`.
- `python -B gate/run_tests.py installation` — exit 0, 44 tests OK.
- Not run: the full gate (`python -B gate/run_tests.py` with no argument), as the handoff says; the orchestrator runs it.
- No test written: the change is Markdown, and no test of the-way reads the wording of these places (the task's *Context*; I re-checked with a grep of `test_*.py` for the files and phrases I changed: only the directories above read them).

## Foundation entries (foundation step)

Searched the whole foundation (WAY-33) with greps for: "human's word", "opens", "opened", "held", "question against", "challenge", "reopen", "change of (that|a) decision", "on its own", and by reading each of the entries the handoff names. Entries written or changed, with the mark, one sentence of meaning in English and one in Polish:

New entries (each new, none of the five rows stood already in an existing entry):

1. **WAY-313** — What is a decision of the foundation to the refinement of a project or a task? Mark: `row 1`. Rejected: `unknown` (the row's source keeps no way not chosen).
   - EN: While a definition or a task is refined, a decision of the foundation is material for revision, not a limit: refinement shows an option that changes it like any other, may recommend it, and asks no leave first; a projected decision of an approved definition is outside.
   - PL: Przy doprecyzowaniu projektu albo zadania decyzja fundamentu jest materiałem do rewizji, nie granicą opcji: agent pokazuje opcję zmieniającą decyzję jak każdą inną, może ją polecić i nie pyta o pozwolenie; decyzja rzutowana zatwierdzonej definicji zostaje poza tym.
2. **WAY-314** — Which act of the human consents to a change of a decision that refinement shows? Mark: `row 2`. Rejected: the one way of question 1 (acceptance of the document as the consent, with the choice preliminary).
   - EN: The option that changes a decision names it in its line, and the human's choice of that option is the one consent; the acceptance of the whole document or the readiness gate asks nothing about the change again.
   - PL: Opcja zmieniająca decyzję mówi to w swoim wierszu, a wybór tej opcji przez człowieka jest jedyną zgodą na zmianę; akceptacja całego dokumentu albo bramka gotowości nie pyta o nią drugi raz.
3. **WAY-315** — From when does a decision of the foundation bind the work on a task? Mark: `row 5`. Rejected: the one way of question 4 (binding only from the writing of code).
   - EN: A decision binds from the start of a task's cycle, the spec in the cycle included; in the cycle no agent departs from a decision on its own and returns with the question (WAY-30), and the looser rules of refinement hold only before that point.
   - PL: Decyzja wiąże od startu cyklu zadania, z pisaniem specu w cyklu włącznie; w cyklu agent nie odchodzi od decyzji sam, tylko wraca z pytaniem (WAY-30), a luźniejsze reguły doprecyzowania obowiązują tylko przed tą granicą.

Existing entries edited in place:

4. **WAY-113** — Mark: `row 3`. Rejected gains the two ways of question 2 with their costs.
   - EN: At refinement (definition, task, technology step) the question against an answer is asked only where the answer contradicts a quoted earlier sentence of the human; in the cycle and where an entry is written it stays as before.
   - PL: Przy doprecyzowaniu pytanie przeciw odpowiedzi pada tylko wtedy, gdy odpowiedź przeczy zacytowanemu wcześniejszemu zdaniu człowieka; w cyklu i przy zapisie wpisu zostaje jak dotąd.
5. **WAY-115** (the definition's candidate table) — Mark: `row 4`. Rejected gains the two ways of question 3.
   - EN: A row repeating a choice the human made between ways shown enters the table accepted and marked, and stays unless the human strikes it; the human cuts only the rows the agent derived.
   - PL: Wiersz powtarzający wybór człowieka między pokazanymi opcjami wchodzi do tabeli przyjęty i oznaczony, zostaje, dopóki człowiek go nie skreśli; człowiek tnie tylko wiersze wyprowadzone przez agenta.
6. **WAY-124** — Mark: `row 4` (the readiness clause only).
   - EN: A task is ready once the human accepted the complete document and accepted or rejected every derived candidate; a row repeating the human's choice counts as accepted until struck.
   - PL: Zadanie jest gotowe, gdy człowiek przyjął cały dokument i przyjął albo odrzucił każdego kandydata wyprowadzonego przez agenta; wiersz powtarzający wybór człowieka liczy się jako przyjęty, dopóki nie zostanie skreślony.
7. **WAY-134** — Mark: `row 4`. Rejected gains the two ways of question 3.
   - EN: The task document keeps rows the human accepted and rows that repeat the human's choice between shown ways unless struck, so the cycle writes them whole.
   - PL: Dokument zadania trzyma wiersze przyjęte przez człowieka oraz wiersze powtarzające jego wybór między pokazanymi opcjami, o ile ich nie skreślił, więc cykl zapisuje je w całości.
8. **WAY-165** — Mark: `row 1` (task of point 5; the silent-decision reservation).
   - EN: In a run at a task a decision of the foundation that leaves part of a matter unanswered is opened by the step like any decision, and the list shown says in one sentence what it leaves unsaid; no word of the human is needed first.
   - PL: W przebiegu przy zadaniu decyzja fundamentu, która zostawia część sprawy bez odpowiedzi, jest otwierana przez krok jak każda decyzja, a pokazana lista mówi jednym zdaniem, czego decyzja nie mówi; wcześniejsze słowo człowieka nie jest potrzebne.
9. **WAY-267** — Mark: `row 1` (point 5).
   - EN: The step may open a choice a decision of the foundation holds when it sees a reason to change the decision; the human's choice among the options is the consent, and the result is a change of that decision.
   - PL: Krok może otworzyć wybór, który trzyma decyzja fundamentu, gdy widzi powód jej zmiany; zgodą jest wybór człowieka między opcjami, a wynikiem jest zmiana tej decyzji.
10. **WAY-138** — Mark: `the cycle's` (found by the WAY-33 search; wording only: "the human opened/opens" became "the step opened/opens", since the step, not only the human, now opens a held choice). No row carries it whole.
    - EN: A choice the step opened over a decision is no longer held, so its recommended option is tested; the rule of what is tested is unchanged.
    - PL: Wybór otwarty przez krok nad decyzją nie jest już trzymany przez decyzję, więc polecana opcja jest testowana; reguła tego, co się testuje, się nie zmienia.

Entries read in the search and left unchanged, with the ruling: WAY-14, WAY-30 (still true: approval with the document stands; WAY-315 and WAY-314 derive from it; its word "implementation" is now fixed by WAY-315 through the link), WAY-25, WAY-33, WAY-114, WAY-118 (question 5: unchanged), WAY-121, WAY-123 (still true; its option message is the carrier of "the option says it in its line", which WAY-314 requires), WAY-126, WAY-139 (its Rejected line "rules are needed on an agent opening a decision" describes a rejected alternative and stays true), WAY-140, WAY-154, WAY-155, WAY-166, WAY-270, WAY-111 (see rulings).

## Reaches beyond the handoff (section 1 of the skill)

- `foundations/decisions.md`: WAY-111, WAY-139, WAY-155, WAY-172, WAY-174, WAY-204/guidelines-decision neighbours, WAY-135 — read by search (grep for "reopen", "question against", "on its own", "challenge", "human's word") to judge whether the change makes them untrue; why: WAY-33 search. Only the passages found were read (not whole files).
- `elements/decisions/template.md` and `elements/decisions/skill/*.md`, `elements/common/rules.md`: read whole because the foundation step goes through `the-way-record-decision` (the handoff names the skill, not the files).
- `project-level/technology/start.md`, `close.md`, `failure_notice.md`, `research.md`, `reserved_choices.md`, `project-level/skill/read_foundation.md`, `project-level/lead/answering.md`, `project-level/lead/conversation_template.md`, `product-guidelines/audit_end.md`: read to judge the orchestrator's extra places.
- `the author's private rule file on knowledge artifacts` and `git.md`: read before writing decisions and committing (user instructions).

## Own-work check (WAY-164)

The requirement most likely not met: acceptance criterion 1, that no file of a skill and no decision of the-way any longer tells the refinement agent to treat a decision as the limit of its options before the cycle starts; and criterion 2, that no step asks the human about the change a second time before the acceptance of the whole document.

The check I ran: (a) a grep over `project-level`, `elements`, `product-guidelines`, `task-cycle`, `agent-instructions` and `foundations` for the old reservations ("human's word", "opens no decision", "never opens", "opens only", "opened though", "the human opened", "route that change", "reopen the upstream", "silently", "may not open") — after the edits the only remaining hits are unrelated uses (the human's words as a source, WAY-269's "human's word" for a returned task, a language the human opened in); (b) a walk of the path of one decision change at a task through the files in the order the agent meets them: technology list (the list shown, with the reason, may be struck — a list confirmation, no leave asked), comparison and choice (`settle.md` 6: the one consent; the question against only for a quoted contradiction), the settled question (`task_run.md` Write), the candidate row (`find_settlements.md`: enters accepted, marked), the question against a row (`task_variant.md` step 4: only for a contradiction), the acceptance of the complete document (`final_review.md`, unchanged) — one consent, no second ask; (c) `foundation_check.py` and the focused test directories above. The check showed: no leftover reservation, and one place that still asks at the definition about a decision change (see "Rulings", `read_foundation.md`).

## Weakest points

1. **Implication move of `definition_variant.md` step 4.1 left as it was.** The task names only the "collision" move for narrowing. The "implication" move ("you wrote X; from X follows Y — does Y hold?") is still a question against an answer, anchored in the human's words or the material. Question 2's answer, read widely, would limit it too. I did not touch it because the task's point 3 lists only the collision move; changing it is a one-line edit if the orchestrator reads question 2 widely.
2. **`project-level/skill/read_foundation.md` step 2 still has the agent ask "whether the decision changes or the project fits it" (WAY-30) at the start of a definition, and WAY-111 says the same.** I judged it a scoping question of the project's idea (what the project is), not the consent to a particular change, so criterion 2 holds: the consent to a concrete change is the choice (WAY-314). But a reader could count it as an extra ask for the same change. Left unchanged; named here.
3. **The list shown at the technology step** now carries, for each item the agent opened over a decision, one sentence of the reason, and the human "confirms, adds or strikes". I treat that as the list confirmation that already existed, not a leave. If the orchestrator reads "no separate word of the human before the comparison" as "no strike of the item either", `list.md` and `task_run.md` need one more clause.
4. WAY-165 at a task: a projected decision of an approved definition that is silent on a logs matter still stays `— projected` (no run reopens it), as before; I did not change that. WAY-165's old rule treated it together with foundation decisions ("any decision"), so its new wording covers foundation decisions only. If the task meant projected ones too, it contradicts question 5.

## Rulings on the places the orchestrator found beyond the task's list

- `project-level/task/skill/SKILL.md`: no change (it only routes to the files; it says no reservation).
- `project-level/task/template.md`: changed — the nested `Changes:` item and *Decisions in play* now speak of a change made by a chosen option; *Settlements to record* names the accepted-with-mark rows.
- `project-level/lead/skill/SKILL.md` (step 5): changed — the exception to the WAY-113 question at refinement. `project-level/lead/answering.md`: one phrase ("the human opened" became "opened over a decision"). `conversation_template.md`: no change ("or the applicable exception" there covers it).
- `product-guidelines/audit_end.md` (lines 197-199): no change; it says that answers on a backlog task are no rows and pass without the question against an answer, which stays true.
- `project-level/technology/start.md`: no change (it never holds the reservation; it already shows changed items with one sentence). `project-level/technology/SKILL.md`: one sentence added saying a held decision is material until the cycle starts.
- `project-level/task/skill/orchestrated_mode.md`: changed twice (the WAY-113 questions it asks the project orchestrator for; accepted-marked rows). It carried no other boundary.
- Also changed and not in the task's list: `project-level/definition_template.md` (Technology section: the nested `Changes:` item and a bullet that a held decision is material), `elements/common/skill/build_table.md` (the shared rule of the marked rows), `project-level/technology/settle.md` (sub-steps 5 and 6).
- Sibling task `the sibling task's note in the author's backlog` point 17: not merged here; I edited WAY-165's sentence as it stands on this branch, so the other task's cycle will have to reconcile that sentence.

## Choices I made (with the way rejected and the cost if wrong)

- Three new entries (WAY-313/314/315) instead of one: each row has its own source and its own *Rejected* (the writer may not derive one), and a single entry would have needed a mixed *Rejected*. Cost if wrong: three entries to merge into one.
- Rows 3 and 4 written as edits of WAY-113 and WAY-115/124/134, not as new entries: their questions are the ones those entries answer (WAY-19). Cost if wrong: a reader looks for the rule in a new entry.
- Row 4 applied to the definition's candidate table too (WAY-115, `definition_variant.md`, `build_table.md`), because point 5 names WAY-115 and the shared step 3 of `find-foundation-entries` serves both callers. Rejected: only the task variant — WAY-115 and WAY-134 would disagree. Cost if wrong: one clause of three files to remove.
- Row 5 (the boundary) stated also in the files of points 1-4 by one short clause each (point 6 wants it), not only in WAY-315.
- At a task, a held decision silent on part of a logs/interface/development-data matter is opened like at a definition (the item ends `— open` with `Changes:`); rejected: keeping `— held by` with a sentence and the agent opening it later — two states for one situation.
- Mark of a row repeating a human choice: the state `accepted` in the working table plus the note "the human's choice", not a new state value; no script reads the working table states.

## Searches not found or unclear

- The task's *Context* says "`resolve_gaps.md:10-11` ... route that change to its own process"; found there (now rewritten). Nothing in `task-cycle/` carries a reservation of the kind, so `task-cycle/` is untouched.
- Unclear: whether a "choice the human made between ways shown" includes an answer under *Questions to settle* with *Not chosen* but without a technology run (I read it so, in `find_settlements.md`).
- Not found: any test of the wording of these places (as the task said).
- Not found: a file named `technology_run.md` outside `project-level/lead/skill/`; that one has no reservation and I left it.

# Report — the plan's *Foundation entries*

**Status:** `done with concerns` — all ten entries are written and committed; two findings of the
search are for the orchestrator to carry into the request (see *Concerns*).

## Files and commits

| File | Added | Removed |
|---|---|---|
| `foundations/decisions.md` | 268 | 55 |
| `foundations/glossary.md` | 6 | 0 |

Commit: `443442f` `docs: settle how a technology choice no project settled reaches the human`, on
`task/unsettled-technology-returns`, base `2dbf1e7`. Not pushed. The 55 removed lines are the edited
sentences of the six changed decisions and the reflow of the paragraphs they stand in.

## The entries, with one sentence of meaning in Polish for the request

| Entry | Meaning |
|---|---|
| WAY-265 — How does the step that settles technology run outside a project definition? (new, row 1) | Krok technologii działa też przy dokumencie zadania, z dopiskiem, po co go uruchamiamy (bez dokumentu zaczyna się od `refine-task`), rozstrzyga tylko sprawy z dopisku i z zadania, wybór trzymany przez decyzję otwiera wyłącznie na słowo człowieka jako zmianę tej decyzji, nie rusza wyboru z zatwierdzonej definicji, a wynik zapisuje w dokumencie zadania, skąd cykl wpisuje decyzję razem z kodem. |
| WAY-266 — Who settles a technology choice that no decision or definition settles? (new, row 2) | Wybór, który mógłby zmienić podział pracy albo dokłada coś do uruchamiania, opłacania lub kopii zapasowej, a którego nic nie rozstrzyga, należy do człowieka: doprecyzowanie kieruje go do kroku technologii, a w cyklu agent oddaje raport bez kodu, próba przepada i cykl otwiera zablokowany szkic requestu; każdy inny wybór zostaje w cyklu, a narzędzia skilli wytycznych na ich drodze. |
| WAY-267 — How does a task leave a cycle that met a reserved choice, and how does it come back? (new, spec) | Gałąź trzyma tylko parę commitów zapisu cyklu, zablokowany szkic nazywa wybór i mówi, że nic więcej nie biegło; po zamknięciu przez człowieka zadanie wraca do doprecyzowania, nowy cykl idzie pod tą samą nazwą na nowej gałęzi, a orkiestrator projektu, na słowo człowieka, usuwa po nazwie ślad tego jednego cyklu i cofa wiersz planu. |
| reserved choice (new glossary term, spec) | Wybór zastrzeżony to wybór technologii, który WAY-266 zostawia człowiekowi: w odróżnieniu od innych decyzji zastrzeżonych cykl się na nim kończy, a w odróżnieniu od innych otwartych wyborów projektowych nie powstaje dla niego spec. |
| WAY-121 (changed, row 3) | Wybór podlegający regule, który definicja pominęła albo którego żadna definicja nie trzyma, rozstrzyga się przez uruchomienie kroku przy dokumencie zadania; reguła przynależności i kolejność przed bramką zostają. |
| WAY-122 (changed, row 3) | Badanie opcji idzie względem definicji albo, przy zadaniu, względem jego dokumentu i dopisku, a ograniczeniem może być też to, co podaje dokument zadania. |
| WAY-123 (changed, row 3) | Pokazywanie opcji przez konsekwencje dla produktu obowiązuje krok wszędzie, gdzie działa. |
| WAY-137 (changed, row 3) | Rozstrzyganie remisu między miejscami uruchomienia obowiązuje krok wszędzie, gdzie działa. |
| WAY-138 (changed, row 3) | Testy ryzyk obowiązują krok wszędzie, gdzie działa, także dla ograniczenia z dokumentu zadania; ryzyka idą do decyzji przez dokument zadania, a wybór otwarty przez człowieka nie jest trzymany przez decyzję, więc przechodzi testy. |
| WAY-135 (changed, row 3) | Przy wyborze zastrzeżonym raport bez kodu i odrzucenie próby są takie same, ale spec nie powstaje, a cykl się zatrzymuje. |

Numbers: the log's last entry was WAY-264 and its withdrawn list ends at WAY-224, so the next free
numbers were 265, 266 and 267. No row was tied to an existing entry: the search found none of the
settlements already stated. *Scope* of WAY-265 is `project-level, task-cycle, decisions`, since the
decisions' template changes with it; of WAY-266 and WAY-267 `project-level, task-cycle`. *Origin* is
`none` in all three: what the reasoning stands in does not outlive the task, and the task document is
private (WAY-27).

## Checks

| Check | Exit code | What it showed |
|---|---|---|
| `python -B elements/common/foundation_check.py .` (before the last two edits) | 0 | 0 errors |
| `python -B elements/common/foundation_check.py .` (on the committed text) | 0 | 0 errors |
| inline Python: binding sentences, forbidden words, *must* in prose for WAY-121, 122, 123, 135, 137, 138, 265, 266, 267 | 0 | one paragraph of 2 or 3 sentences in each; no forbidden word; no *must* in prose. Run before the last two edits, which touched only *Rationale* of WAY-267 and *Verification* of WAY-265. Seven lines stand 1–2 characters over 100; no check binds that width |
| inline Python: count of *Rejected* ways against the task | 0 | see the own-work check |
| `git grep -n -E "project's technology" -- foundations` | 1 | no match: no entry keeps the old phrase |
| `git grep -n -i -E "reserved[[:space:]]+choice" 2dbf1e7 -- .` | 1 | no match at the base: the term had no use in tracked files, so *Not* reads `none` |
| `git grep -n -i -w "reserved" -- installation` | 1 | no match: the earlier hits there are "preserved" |

Not run: the gate, which is the orchestrator's (handoff, WAY-160). No test was written: this stage
writes entries and no code, and no invariant changes. No critique of the set: `make-change` forbids
this stage a subagent, and WAY-120 takes a change to the foundation out of critique (WAY-10).

## Own-work check (section 3)

- **Requirement most likely unmet:** the *Rejected* of a decision written from a row takes exactly the
  ways not chosen that the row's source keeps, none added and none lost, and WAY-267's the ways of
  the spec's decisions 2 and 5.
- **Check:** a script counts the items under *Not chosen* of each question in `task.md` and the ways
  in each new entry's *Rejected*; then each way was compared by hand with its source.
- **Showed:** row 1 expects 4 (questions 1, 4, 7) and WAY-265 holds 4; row 2 expects 5 (questions 2,
  3, 5) and WAY-266 holds 5; WAY-267 holds 7 (3 of decision 2, 4 of decision 5). The spec's ways under
  decision 3, the rule on doubt among them, are in no *Rejected*, as the handoff gives.

## Search of the whole foundation (WAY-33)

Searched once the entries were settled: `technolog`, `stack`, `settle-technology`, `smallest
reversible`, `reserved`, `blocked draft`, `open design choice`, `without code`, `no code`, `returned`,
`closed-unmerged`, `to refine`, `reuse`, `new branch`, `` `blocked` ``, `cycle ends`, and every
reference to WAY-121, 122, 123, 135, 137, 138, over `foundations/`. Each entry below was read whole.

| Found | Outcome |
|---|---|
| WAY-114: a question goes to the human only where the agent has no recommendation, and the agent otherwise writes the entry. A reserved choice goes to the human whatever the agent recommends, and outside the step WAY-123's precedence does not reach it | Link: WAY-266 `narrows WAY-114`, its area in the binding sentence, as WAY-123, WAY-155, WAY-172 and WAY-174 do. **Not in the spec's list**; see *Concerns* |
| WAY-160: the orchestrator runs the gate on the tree that goes into the request. The spec's decision 2 runs no gate there | Read as not reaching this request: its question is the finished change's gate, and the tree equals the base. One clause in WAY-267's *Rationale* says so. **Not in the spec's list**; see *Concerns* |
| WAY-219: a missing way to the running product does not stop a cycle | No collision: stated in WAY-266's *Verification* |
| WAY-163: what runs before a blocked request | No collision: it binds a request a remaining finding blocked. Its shape, naming what did not run, is what WAY-267 follows |
| WAY-153, `project-plan-state-evidence`: the reader changes nothing; a closed-unmerged PR and a conflicting trace go to the human | No collision: WAY-267 removes and moves only on the human's word |
| WAY-152, WAY-154, WAY-155: what the project orchestrator, the refiner and the answering agent do | No collision. WAY-265's *Verification* gains the orchestrated route, so the rule that a refiner starts no child agent stays visible |
| WAY-140: a task's effect outside the repository is a human's | No collision read: removing a branch on the host is a leading session's cleanup, on the human's word, and no effect of a task |
| WAY-229, WAY-136, WAY-125: statuses, retries and methods | No collision: the retry binds `blocked` alone, and the planner's excluded status in WAY-136 concerns work it cannot divide |
| WAY-172, WAY-242: a blocked draft request carrying a proposed decision | No collision: another area, as the spec found |
| WAY-185, 186, 210, 211, 248, 249, WAY-165, WAY-166 | Stay true after the changes to WAY-121, 122 and 123, which derive them |
| WAY-01, WAY-14, WAY-30, WAY-36, WAY-106, WAY-118, WAY-124, WAY-126, WAY-134, WAY-147, WAY-156, WAY-227, WAY-263 | Unchanged and consistent; WAY-263 untouched as settled. WAY-36: all three new rules bind after the merge |
| `project-technology-record`, the only invariant deriving from a changed decision | Stays true; it speaks of a definition alone |
| `open design choice` | Unchanged; a reserved choice is one such choice, which the new term and WAY-135 say |
| `elements/decisions/template.md:65-67` still speaks of a choice "a project settles" | Slice 1 changes it, as the plan gives; a template is outside this stage's boundary |
| Words needing a glossary entry | None beyond `reserved choice`; "note" and "run" are used in their usual sense |

## Reaches beyond the handoff

- `foundations/decisions.md`, whole entries, because `the-way-record-decision` step 1 selects by
  *Scope* and the search found them: WAY-03 (the template's example), WAY-11, WAY-13, WAY-25, WAY-27,
  WAY-90, WAY-93 to WAY-97, WAY-99, WAY-115 to WAY-118, WAY-120, WAY-125, WAY-126, WAY-139, WAY-140,
  WAY-142, WAY-143, WAY-145, WAY-148, WAY-152, WAY-156, WAY-160, WAY-161, WAY-162, WAY-163, WAY-164,
  WAY-172, WAY-174, WAY-185, WAY-186, WAY-210, WAY-211, WAY-214, WAY-215, WAY-216, WAY-226, WAY-229,
  WAY-242, WAY-248, WAY-249, WAY-256, WAY-263, WAY-264.
- `foundations/invariants.md`: `outbound-link-reach`, `project-plan-form`,
  `project-plan-state-evidence`, for WAY-27's limit on sources and for the plan row's move.
- `foundations/part_map.md` lines 1–80, for the parts' identifiers.
- `task-cycle/record_template.md` by search, for the name "questions table";
  `project-level/plan/template.md` by search, for the states of a row.
- The GitHub page the spec quotes, fetched to give *Based on* the place in it, which the spec omits.

## Choices

| Choice | Way rejected | Cost if wrong |
|---|---|---|
| WAY-266 records `narrows WAY-114` | Leaving the link out as the spec's list does: WAY-25 would leave a cycle with two decisions and no precedence | The human strikes one clause and one link at the merge |
| WAY-160 read as not reaching the draft, with a clause in *Rationale* | `narrows WAY-160`, which records a precedence neither the task nor the spec names; or a return with a question, for a request that holds no change | A reader takes WAY-160 to require a gate on that draft; the spec's order would then need a line in WAY-160 |
| WAY-135 gains in *Rejected* the two ways of question 3, which row 3's source keeps, because they answer what follows the report. WAY-121, 122, 123, 137 and 138 keep their *Rejected* | Every way of questions 1, 3 and 4 in all six entries: five ways repeated to no reader. Row 3's ways all stand in WAY-265 and WAY-266 | A reviewer reads the template as asking for them in each entry; the fix is adding lines |
| WAY-267's *Based on* quotes the GitHub page rather than naming an environment fact | A fact entry: the spec's cost for this falls short of calling the decision into question (WAY-90), and no such entry is planned | If a reviewer judges otherwise, one fact entry and one changed field |
| *Based on* of WAY-266 is `none`, and the lesson m2l4 stands in *Rationale* and in a clause of the binding sentence, spelled `10xDevs` as WAY-237 does | A pointer to the private map of the course, against WAY-27 and `outbound-link-reach` | None seen; this follows WAY-121 and WAY-237 |
| WAY-266's binding sentence names `project-level/technology/reserved_choices.md` and the status `reserved`, as the handoff allows | The rule's examples left unnamed: an agent reading the decision would not reach them | Slice 2, 4 or 5 renames the file and has to edit the entry |
| WAY-267 also holds a correction's case, which the spec's table of meanings omits and its decision 2 settles | Leaving it out: the first sentence would be false of a correction | None seen |
| The spec's examples of the boundary stand in WAY-266's *Verification* | Only in the new file: the decision would show no boundary to an agent comparing a change with it | A second place to keep in step with `reserved_choices.md` |

## Concerns for the request

1. WAY-266's `narrows WAY-114` is a precedence the spec does not list. WAY-25 says a human records
   precedence; here row 2 settled the substance, and the human sees it at the merge. Name it under
   the entry in the request.
2. WAY-160 against WAY-267: a request with no gate run. Name it in the request so that the human sees
   the reading.

## Searches not found or unclear

- Question 2's second way not chosen reads "jak wyżej". Unclear whether it means the answer or the way
  before it; its cost, one more line in a request, fits only the answer, so WAY-266 writes "the same
  rule".
- Whether the template's rule on *Rejected* reaches a decision changed from a row, and how, when one
  row changes six decisions: not settled anywhere found; see *Choices*.
- The spec gives the GitHub passage with no place in the page. Found by fetching it: § "Restoring a
  deleted branch", passage as the spec quotes it, read 2026-10-31.
- `git grep` found "reserved" in `installation/` only as part of "preserved"; no other use.

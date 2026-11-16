# Author fix report — decision-sources-and-leftouts (fix of the review of the whole change)

**Status:** done

Fix range: `05b46486103be3db6ead33ffff5b53e3c9988331..01ab269`. One commit, `01ab269` — "Fix the
review's findings on the leftouts of the course practices" — `foundations/decisions.md`, 33 added,
23 removed lines. Not pushed.

## Findings

**I1 — fixed.** WAY-142 *Rejected*: "the milestones, the estimates and the interview on the order of
work …" now reads "the milestones and the interview on the order of work of the practice of a
roadmap of vertical slices — left out of what the step takes from it". I hold the finding right: the
lesson note m2l1, section "Czego skill świadomie nie robi", says the skill does not estimate the time
of the work, and the map of the course rejects the row "Bez estymat czasu" with "nic do przejęcia".
Check: `grep -n "the estimates" foundations/decisions.md` finds only an unrelated line of another
entry (`:3551`, a measurement in WAY-256's area), none in WAY-142.

**M1 — fixed** by the smaller of the two fixes the reviewer offered. WAY-143 *Rationale* now says the
practice's foundations stand "only with what it unlocks — a slice, a blocking unknown it reduces or a
way of verifying it enables" (the three the skill's line 344 and check 10 give), instead of "only
with the slice it unlocks". No *Rejected* item added.

**M2 — fixed for the four entries the finding names** (WAY-138, 142, 268, 270). I accept the
reviewer's judgment: the map of the course is the record where each of these choices was made, so
it is a source in the sense of the answer to question 1. Each reason below is taken in meaning from
the map's row, and no further:

| Entry | Item | Reason carried | Map row (lesson, element) |
|---|---|---|---|
| WAY-138 | known limitation recorded in a document of the infrastructure | such a document answers no question, and the decision of the choice carries it and its reasons | m1l5, "`infrastructure.md` jako trzeci kontrakt" (verdict: "`infrastructure.md` „nie odpowiada na żadne pytanie” … wybór i jego powody niosą decyzje the way") |
| WAY-138 | comparison of three alternatives in a table | the step already compares the options of each choice, and its decision keeps those not chosen in *Rejected* | m1l5, "Dwie techniki bez skilla" ("tabelę trzech alternatyw krok technologii już robi (porównanie opcji, *Rejected*)") |
| WAY-138 | change of roles | no decision of the-way has several roles on its other side | m1l5, same row ("w the way nie ma decyzji z kilkoma rolami po drugiej stronie"; the part about Mariusz's work elsewhere not carried) |
| WAY-142 | scored readiness check of the documents | the definition passes its stricter readiness gate before the breakdown (WAY-118) | m2l1, "Sprawdzenie gotowości PRD (0–4)…" ("the way ma ostrzejszą bramkę przed rozbiciem (… WAY-118 …)") |
| WAY-142 | fields feeding acceptance criteria, sentence of why an item stands where it does | the refinement of each task writes its acceptance criteria from its own analysis, and the order stands in the dependencies | m2l1, "Kryteria akceptacji wyprowadzane z pól roadmapy…" ("kryteria akceptacji pisze krok doprecyzowania w dokumencie zadania z niezależnej analizy zadania … kolejność niesie kolumna „zależy od”") |
| WAY-142 | list of parked items | it copies what the definition puts out of scope | m2l1, "Blokery zewnętrzne odróżnione od niewiadomych…" ("*Parked* w A to kopia „Out of scope”") |
| WAY-142 | state of an item blocked by an unknown | the plan has a state of waiting for the human and places each open question where it is resolved | m2l1, same row ("the way ma stan „czeka na człowieka” i „resolved in”"); the state `waiting for human` checked in `project-level/plan/template.md:95` |
| WAY-268 | search engine built for agents | it is a choice of a provider of search, not a step of the process | m2l4, row 4 ("wybór dostawcy wyszukiwania, nie krok procesu") |
| WAY-268 | library documentation put into context before the plan | an agent fetches the documentation when it needs it, rather than all of it ahead | m2l4, row 5 ("dociągać informacje z dokumentacji, gdy są potrzebne, a nie zaciągać całej z góry") |
| WAY-270 | a failure tool set up ahead of the choice | the step chooses the tool, with a deliberate absence among its options | m3l5, row 22 ("narzędzie monitoringu wybiera się kwestią observability … (z opcją „bez narzędzia”), nie z góry Sentry ścieżką kursu") |
| WAY-270 | agent reaching failures through the tool's server | how an agent reads the record of the running product is a matter the step already settles (WAY-121) | m3l5, row 6 ("agent czyta logi sam: WAY-121 (kwestia „logs” w kroku technologii)") |

Not given a reason: WAY-142's stock of the code by parallel agents — its map row is open
("otwarte", hypothesis untested), so the trace holds no reason. The new items of WAY-143, 144, 146,
147, 273 and 374 are outside the places M2 names and stay as they were.

## For the request's table

- WAY-138 *Rejected*: the three items now carry reasons (above).
- WAY-142 *Rejected*: "the estimates" removed from the existing item; reasons added to four items
  (readiness check, fields of acceptance criteria, parked list, blocked state).
- WAY-143 *Rationale*: foundations stand on a slice, a blocking unknown or a way of verifying.
- WAY-268 *Rejected*: both items carry reasons.
- WAY-270 *Rejected*: both items carry reasons.

## Checks

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B .runs/author/compare_binding.py . aba5ee92a0734c2e775cc69662af669bf6455795` | 0 | binding changed: `['WAY-100']` only; no decision added or removed |

Not run: the full gate (the orchestrator's). No test was written; no test cites the changed prose.

## Own-work check

- Requirement most likely missed: a reason that the trace does not hold, or a binding sentence moved
  by an edit next to it.
- Check: each reason compared with its map row (table above); the binding comparison against base.
- Result: every reason has its row; binding sentences changed only in WAY-100, as before.

## Working copies

`.runs/author/` recreated for the comparison script only; removed with `rm -rf` before returning
(`.runs/` holds only `task-cycles/`).

## Unread material

- The reviewer's full report `reports/review-whole-report.md`: not read — the findings file holds
  the evidence each fix needed.
- The map of the course: m1l5 rows read again by search of that section; m2l1, m2l4 and m3l5 rows
  as read in the first round.

## Searches not found or unclear

none

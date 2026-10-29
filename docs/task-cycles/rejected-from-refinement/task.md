---
title: "the way: decyzja zapisywana z zadania dostaje odrzucone warianty z doprecyzowania albo jawne „unknown”, zamiast domysłu agenta"
status: draft
created: 2026-10-28T14:51
updated: 2026-10-29
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# Decyzja zapisywana z wiersza zadania dostaje w *Rejected* warianty niewybrane przy doprecyzowaniu albo jawne `unknown`, zamiast wariantów dopowiedzianych przez autora wpisu

Status: ready for cycle
Project relation: independent

## Description

### Need

- Cykl zadania zapisuje każdy wiersz *Settlements to record* jako wpis fundamentu, a wpis decyzji ma pole *Rejected* — warianty rozważone i odrzucone (`elements/decisions/template.md:37`, `foundations` @ `d7a205c`).
- Dokument zadania nie trzyma wariantów, które człowiek zobaczył przy doprecyzowaniu i odrzucił: wiersz niesie rozstrzygnięcie i jego źródło (`project-level/task/template.md:129–146`), a odpowiedź pod *Questions to settle* — odpowiedź i jej pochodzenie (`project-level/task/template.md:92–102`).
- Rozmowa, w której te warianty padły, nie przeżywa zadania: w doprecyzowaniu prowadzonym przez lidera projektu plik rozmowy jest kasowany po sprawdzeniu, że w dokumencie zadania przetrwały „all resolved answers, original sources, accepted candidate meanings and required information” (`project-level/lead/skill/SKILL.md:156–157`), a warianty niewybrane do tej listy nie należą.
- Szablon decyzji dopuszcza w *Rejected* tylko warianty albo `none considered` (`elements/decisions/template.md:37`), a `none considered` jest wypowiedzią człowieka (`elements/decisions/skill/SKILL.md:36`) — autor wpisu bez źródła nie ma więc uczciwego wyjścia innego niż pytanie do człowieka przez zablokowany draft requestu (`task-cycle/skill/foundation_step.md:18–25`).
- W loop2 autor wpisów cyklu `odkrywanie` wypełnił *Rejected* decyzji D-121–D-126 z treści zadania i napisał: „Reasons in D-126's and D-124's *Rejected* are my own reading, not quoted.” (loop2 @ `ee96d7f`, `docs/task-cycles/odkrywanie/reports/04-foundation-entries-report.md:53`); sposób wziął z poprzedniego cyklu `grupy_regul_i_liczniki` (tamże, wiersz 62).
- Taki wpis wygląda, jakby człowiek te warianty rozważył i odrzucił, a agent, który zaproponuje jeden z nich później, ma według szablonu wyjaśnić, „what has changed since” (`elements/decisions/template.md:78`) — wariant, którego nikt nie odrzucił, staje się zamknięty.

### To do

1. Gdy człowiek przy doprecyzowaniu wybiera spośród pokazanych wariantów, dokument zadania trzyma warianty pokazane i niewybrane — każdy w jednej linii, z kosztem, jaki przypisało mu pytanie, albo z powodem w słowach człowieka — pod odpowiedzią na to pytanie w *Questions to settle*, a wiersz *Settlements to record* prowadzi do nich przez swoje *Source*; wybór dokonany poza *Questions to settle* trzyma swoje warianty w *Source* wiersza (Q1).
2. *Rejected* decyzji zapisywanej z wiersza zadania to warianty, które źródło wiersza trzyma, `none considered`, gdy człowiek tak powiedział, albo `unknown`; wariant, który piszący wywodzi z treści zadania — z kolumny „What the cycle would otherwise guess”, z kosztu wybranego wariantu albo z fundamentu — nie wchodzi do pola.
3. Składnia pola w szablonie decyzji dopuszcza `unknown`: `*Rejected:* <…> | none considered | unknown` (dziś bez `unknown`, choć sekcja „Recovered decisions” tego samego szablonu już go wymaga, `elements/decisions/template.md:204`).
4. W doprecyzowaniu prowadzonym przez lidera projektu refiner przenosi warianty niewybrane do dokumentu zadania razem z odpowiedzią, a lider przed skasowaniem pliku rozmowy sprawdza, że przetrwały (`project-level/lead/skill/SKILL.md:156–157`).

### Questions to settle

- Q1. Gdzie dokument zadania trzyma warianty pokazane człowiekowi i niewybrane?
  - Answer: pod odpowiedzią w *Questions to settle*, a *Source* wiersza *Settlements to record* wskazuje to pytanie; gdy wybór padł poza tą sekcją — np. przy pytaniu kontrolnym przy cięciu kandydatów — warianty stoją w *Source* wiersza.
  - Not chosen: w kolumnie *Source* wiersza — warianty trzeba donieść od pytania (krok 3) do budowy tabeli (krok 5), komórka tabeli nie znosi łamania linii, a refiner w doprecyzowaniu prowadzonym przez lidera przenosi odpowiedzi do *Questions to settle*, nie do tabeli.
  - Source: Mariusz, 2026-10-29, „B” — na pytanie z dwoma wariantami (A: *Source* wiersza, B: pod odpowiedzią w *Questions to settle*) i kosztem każdego.
- Q2. Gdzie w rejestrze decyzji the-way stoi reguła, skąd *Rejected* decyzji zapisywanej z wiersza zadania?
  - Answer: w WAY-134, rozszerzonej tak, że zadanie trzyma warianty niewybrane, a cykl bierze z nich *Rejected* albo wpisuje `unknown`, zamiast pytać człowieka przez zablokowany draft requestu.
  - Not chosen: bez wpisu w rejestrze, tylko w szablonach — WAY-134 dalej kazałaby pytać człowieka, a szablon wpisywać `unknown`, i agent porównujący zmianę z WAY-134 uznałby `unknown` za naruszenie; rozszerzenie WAY-29 — jej pytanie dotyczy decyzji odtworzonych z kodu (WAY-19: nowa reguła obok istniejącej to nowe pytanie), a WAY-134 dalej kazałaby pytać, więc potrzebna relacja pierwszeństwa; nowa decyzja — kolejny wpis, a WAY-134 i tak trzeba poprawić.
  - Source: Mariusz, 2026-10-29, „pójdźmy w A” — na pytanie z czterema wariantami (A: WAY-134, B: WAY-29, C: nowa decyzja, bez wpisu) i kosztem każdego; słaby punkt A nazwany w pytaniu: WAY-134 ma już trzy długie zdania wiążące, zdanie się wydłuży, a brzmienie wybiera cykl.
- Q3. Czy zadanie czeka na wytyczne samego the way, skoro the way nie ma katalogu `guidelines/`?
  - Answer: nie — zadanie idzie drogą z `agent-instructions/README.md`, jak zadania 1–3 serii skilli; wybór wytycznych jest pusty, a zadanie zmienia pliki Markdown szablonów i skilli.
  - Source: odpowiedź wspólna z `_zadania/zadanie_skille_the_way_3_fundament.md`, *Questions to settle*, pytanie 5: Mariusz, 2026-10-28, „tak” — na tę samą odpowiedź co w zadaniu 2 (`_zadania/zadanie_skille_the_way_2_refine_task.md`: Mariusz, 2026-10-28, „przyjmuję”), przeciw czekaniu na wytyczne samego the way.

## Context

- Źródło: sprawa AIR-533 z dziennego przeglądu warstwy AI (2026-10-28), z uwagi procesowej (1) w zapisie cyklu `odkrywanie` (loop2 @ `ee96d7f`, `docs/task-cycles/odkrywanie/cycle.md:179`, PR #33 w loop2).
- Zadanie w loop2 powoływało się na plik rozmowy `.runs/project-refinement/odkrywanie.md`, którego w chwili cyklu już nie było (raport, wiersz 53).
- Pytanie o decyzję pokazuje człowiekowi warianty i koszt każdego (WAY-113); w doprecyzowaniu prowadzonym przez lidera projektu stoją one w polu `Human question:` pliku rozmowy (`project-level/lead/conversation_template.md:86`).
- `elements/common/foundation_check.py:432` sprawdza tylko, czy pole *Rejected* istnieje, więc `unknown` przechodzi bez zmiany skryptu.
- Koszt po stronie doprecyzowania: linia na każdy niewybrany wariant; część nowych wpisów dostanie `unknown`.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

Brzmienie z `foundations/decisions.md` na `foundations` @ `d7a205c`.

- **WAY-134** — „How does a task carry what its refinement settles for the foundation?” — zmienia ją wiersz 1 *Settlements to record* (Q2): „Before a task is ready for its cycle, the human sees a table of candidates found in the task document and the conversation that refined it, in the form WAY-115 gives with each settlement in the human's words, and the task document keeps the rows the human accepts; the agent refining the task presents the table, or, in orchestrated refinement, the project orchestrator as WAY-154 and WAY-155 give. A candidate is a decision, an invariant, a glossary term, or an environment fact a candidate decision or invariant rests on, and a settlement that a current entry the refinement reads for the parts the task touches, or a projected entry the task carries, already states is no candidate. The task's cycle writes each kept row whole into the foundation in its foundation step, or in its return step where the foundation step missed it, one that no code makes true included, keeping its meaning and choosing its wording; where that meaning cannot hold, or the entry needs a value neither the row nor the cycle's work gives, the cycle asks the human through a blocked draft request rather than write another entry, and otherwise the human accepts the entry's meaning at the merge (WAY-114); a kept row whose settlement the cycle's search of the whole foundation (WAY-33) finds already stated becomes no second entry, the cycle tying the row to that entry and naming both in the request.”
- **WAY-29** — „How is a decision recovered from an existing product written?” — ta sama rodzina zakazu dla decyzji odtworzonych z kodu; zadanie jej nie zmienia: „A decision recovered from the code of an existing product says in *Origin*, in one sentence, that it was recovered from the code and where in the code it shows, and its rationale and rejected options are quoted from a source, given by a human who knows them, or written as `unknown`. A rationale an agent proposes for a human's decision goes to the human as a question, never into the entry; the rationale of a decision an agent takes in a task is the agent's to write.”
- **WAY-35** — „What does an element's skill hold?” — reguła pola *Rejected* trafia do szablonu decyzji, nie do skilla: „An element's skill holds only the way of working particular to its element: every rule of the element's entries stands in the element's template, or once in the part the elements share (WAY-09) where it is common to them; the way of working the skills share stands once in that part, and a skill reads the rules and that way of working from there instead of restating them.”
- **WAY-113** — „How does an agent of the-way ask a human decision?” — pytanie o decyzję jest źródłem wariantów pokazanych: „An agent asks in plain conversation text: a decision question gives the available ways, the cost of each and a recommendation, while a question of assessment stays open; neither opens a separate question panel. After a human choice enters an entry's binding part, the agent asks one question against that choice anchored in the human's words or supplied material, unless the choice ends with the work, or the human took one of the ways offered and the decision question named, anchored in the material, the weak point of that way.”
- **WAY-154** — „How do agents exchange a project task refinement and keep its result?” — przeniesienie odpowiedzi i skasowanie pliku rozmowy (To do 4); fragment: „Only a refiner changes the task document's body and transfers settled answers with their sources into Questions to settle […] final acceptance makes both document and plan ready for cycle and removes only that conversation after all settled answers and their sources survive in the task document”.

## Settlements to record

Candidates: 3 shown, 1 accepted — 2026-10-29

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Gdy człowiek przy doprecyzowaniu wybiera spośród pokazanych wariantów, zadanie trzyma warianty niewybrane pod odpowiedzią w *Questions to settle*, a gdy wybór padł poza tą sekcją — w *Source* wiersza; *Rejected* decyzji zapisanej z wiersza to te warianty, `none considered`, gdy człowiek tak powiedział, albo `unknown`, nigdy wariant wywiedziony przez piszącego — i stoi to w WAY-134, zamiast pytania człowieka o brakujące warianty. | decision | Q1, Q2; *To do* 1–2; przyjęty: Mariusz, 2026-10-29, „przyjmuję jak rekomendujesz” | czy dopisać regułę do WAY-134, do WAY-29, jako nową decyzję czy tylko w szablonach; czy przy braku wariantów blokować request pytaniem, jak dziś każe WAY-134 |

## Out of scope

- Decyzje zapisane przed tą zmianą, w the-way i w produktach, zostają, jakie są.
- Poprawa *Rejected* decyzji D-121–D-126 w loop2 — osobna sprawa produktu.

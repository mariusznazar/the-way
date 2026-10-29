---
title: "the way: planista ujmuje w liście wpisów fundamentu część ustalenia, którą kod zadania czyni prawdziwą, a linię mapy części dla nowego pliku daje do kawałka, który ten plik tworzy"
status: draft
created: 2026-10-29T10:30
updated: 2026-10-29
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# Planista cyklu ujmuje w *Foundation entries* część wpisu projektowanego, którą kod zadania czyni prawdziwą, a linię mapy części dla nowego pliku daje do kawałka, który ten plik dodaje

Status: ready for cycle
Project relation: independent

## Description

### Need

- Planista cyklu zadania spisuje w tabeli *Foundation entries* swojego planu wpisy, które krok fundamentu zapisuje przed kodem; z wpisów projektowanych instrukcja wymienia „each projected entry the task's code makes true or its plan item assigns” (`task-cycle/plan/SKILL.md:106-107`, `foundations` @ `d115159`).
- Zdanie nie mówi o części wpisu, którą kod zadania czyni prawdziwą, gdy plan projektu wskazuje do zapisu wpisu inne zadanie — a WAY-126, szablon planu projektu (`project-level/plan/template.md:121-123`) i instrukcja kroku fundamentu (`task-cycle/skill/foundation_step.md:9-10`) każą zadaniu zapisać tę część.
- To samo zdanie podaje jako przykład wpisu tabeli „a part-map change for a file the change adds” (`task-cycle/plan/SKILL.md:107-108`), a wpisy tabeli krok fundamentu zapisuje przed kodem.
- `elements/common/foundation_check.py` zgłasza błąd dla wzorca mapy części, który nie trafia w żaden plik śledzony przez git (`:550-553`), i dla śledzonego pliku, którego nie przypisuje żadna część (`:560-562`) — więc plik i jego linia mapy muszą wejść razem.

### To do

1. Opis tabeli *Foundation entries* w `task-cycle/plan/SKILL.md` każe ująć każdy wpis projektowany, który zadanie niesie, w całości albo tę jego część, którą kod zadania czyni prawdziwą, także gdy plan projektu wskazuje do zapisu wpisu inne zadanie (WAY-126), oraz każdy wpis, który pozycja planu zadaniu przydziela (Q1).
2. Z tego opisu znika przykład „a part-map change for a file the change adds”, a opis pola *Change* kawałka mówi, że zmiana mapy części potrzebna plikowi, który zmiana dodaje, stoi w *Change* kawałka, który ten plik dodaje — bo sprawdzenie fundamentu nie przyjmuje ani wzorca bez śledzonego pliku, ani śledzonego pliku bez części.

### Questions to settle

- Q1. Czy zdanie z *To do* 1 obejmuje każdy wpis projektowany, który kod zadania czyni prawdziwym, czy tylko wpis, który zadanie niesie w swoim dokumencie?
  - Answer: tylko wpis, który zadanie niesie w swoim dokumencie — przepisany w *Decisions in play* — w całości albo część, którą jego kod czyni prawdziwą, także gdy plan wskazuje do zapisu inne zadanie; do tego każdy wpis, który pozycja planu przydziela.
  - Not chosen:
    - każdy wpis projektowany, który kod zadania czyni prawdziwym (brzmienie z pierwotnej notatki) — obejmuje też zadanie planu, którego pozycja tego wpisu nie wymienia, a takie zadanie według WAY-126 i `task-cycle/skill/foundation_step.md:15-16` najpierw wraca do planu; planista wpisałby do tabeli wpis, którego krok fundamentu zapisać nie może.
  - Source: Mariusz, 2026-10-29, „B” — na pytanie z dwoma wariantami (A: każdy wpis, który kod czyni prawdziwym; B: tylko wpis, który zadanie niesie) i kosztem każdego; słaby punkt B nazwany w pytaniu: gdy doprecyzowanie nie przepisze wpisu do *Decisions in play*, mimo wymogu `project-level/plan/template.md:123-124`, planista go nie ujmie i złapie go dopiero krok powrotu.
- Q2. Czy zadanie czeka na wytyczne samego the way, skoro the way nie ma katalogu `guidelines/`?
  - Answer: nie — zadanie idzie drogą z `agent-instructions/README.md`, jak zadania 1–3 serii skilli; wybór wytycznych jest pusty, a zadanie zmienia plik Markdown skilla.
  - Source: odpowiedź wspólna z `_zadania/zadanie_skille_the_way_3_fundament.md`, *Questions to settle*, pytanie 5: Mariusz, 2026-10-28, „tak” — na tę samą odpowiedź co w zadaniu 2 (`_zadania/zadanie_skille_the_way_2_refine_task.md`: Mariusz, 2026-10-28, „przyjmuję”), przeciw czekaniu na wytyczne samego the way; skopiowana tu z `_zadania/zadanie_the_way_odrzucone_warianty_decyzji_z_zadania.md`, pytanie Q3.

## Context

- Źródło: sprawa AIR-540 z dziennego przeglądu warstwy AI (2026-10-29), z dwóch uwag procesowych zapisu cyklu `rozwiazanie-lasu` (loop2 PR #35, loop2 @ `c80cc51`, `docs/task-cycles/rozwiazanie-lasu/cycle.md:152`).
- W loop2 planista cyklu `rozwiazanie-lasu` (zadanie 7 planu projektu) odczytał „zapisuje zadanie 8” jako zostawienie zadaniu 8 całego projektowanego wpisu „How is a map solved, and what opens the next one?”, choć dokument zadania kazał zapisać część, którą kod czyni prawdziwą; brak wyszedł dopiero w kroku powrotu (`cycle.md:152`, uwaga procesowa 1).
- Spóźniony wpis zdublował istniejącą regułę — recenzja kroku powrotu zablokowała go znaleziskiem o liczeniu passy w D-71 i D-136 — i kosztował rundę poprawki przed PR-em (`cycle.md:24`).
- W tym samym cyklu linię mapy dla pliku testu, który pisał późniejszy kawałek, trzeba było przenieść z *Foundation entries* do kawałka 4 (`cycle.md:152`, uwaga procesowa 2).
- Częstość: pominięta część wpisu — raz na pięć przeczytanych zapisów cykli; linia mapy części na liście przed plikiem — raz.
- W planie projektu loop2 jeden wpis urzeczywistniają zadania 7, 8, 12 i 13 (`docs/task-cycles/rozwiazanie-lasu/task.md`, loop2 @ `c80cc51`, *Decisions in play*), więc każde zadanie realizujące część większego wpisu może zgubić swoją część.
- Pozycja planu projektu wymienia wpisy, które zadanie urzeczywistnia i które zapisuje, a każde zadanie urzeczywistniające niesie wpis w *Decisions in play* swojego dokumentu (`project-level/plan/template.md:119-124`); zadanie korzystające z projektu tylko jako ze źródła zaznacza tam wpisy i części, które jego kod czyni prawdziwymi (`project-level/task/template.md:131-133`).
- Ta sama instrukcja planisty mówi już o „the approved project definition's projected entries the task carries or its plan item assigns” (`task-cycle/plan/SKILL.md:36-37`).
- Krok wyboru drogi cyklu nazywa linię mapy części dla dodawanego pliku wpisem, który wynika ze zmiany bez otwartego wyboru (`task-cycle/skill/SKILL.md:92-94`); zadanie tego nie zmienia.
- Numery linii w pierwotnej notatce podano wg `origin/foundations` @ `745a6e5`; `task-cycle/plan/SKILL.md` i `foundation_check.py` nie zmieniły się do `d115159`, a zdanie o *Change* stoi w linii 119, nie 117-118.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

Brzmienie z `foundations/decisions.md` na `foundations` @ `d115159`.

- **WAY-126** — „How does a projected entry enter the foundation?” — reguła, którą *To do* 1 przenosi do instrukcji planisty: „A projected entry of an approved project definition enters the product's foundation in the change of the first task whose code makes it true — the task the plan assigns, or a task that uses the definition as a source only, even where the plan assigns the entry to another task — whole, in the wording the readiness gate approved, with the projected terms and environment facts it uses or rests on and with no record of approval copied from the gate, since the merge of the task's request brings it in; where the code makes only part of it true, the agent writes that part and the human accepts its meaning at the merge (WAY-114). The task the plan assigns writes what of the entry the foundation does not yet hold, and a projected entry no code makes true. The return step reads the projected entries of the task's sources as well as the foundation, writes one the code makes true that the foundation step missed — an invariant with its test run on that code — and writes a new entry only for a rule none of them states.” Z *Verification*: „a plan member whose code would make another item's entry true returns to the plan first”.
- **WAY-44** — „What assigns a file to a part?” — powód *To do* 2; fragment: „Every file git tracks belongs to exactly one part of the map, by path patterns that git itself matches […]; a file that no pattern matches, and a file that two parts claim, is an error of the check of the foundation, unless the map lists that file as left out on purpose, and so is a pattern of a part's *Files* or *Trust boundary* that matches no file git tracks.”
- **WAY-01** — „What state does the foundation describe?” — część zapisana w kawałku, a nie przed kodem, nadal wchodzi w tym samym merge'u; fragment: „A task that sets out to change the foundation makes that change on its branch in the product's repository, and the change reaches the main branch in the same merge as the code it describes; no entry the task calls for is left for a later task.”

## Settlements to record

Candidates: 4 shown, 0 accepted — 2026-10-29

none

## Out of scope

- `task-cycle/skill/foundation_step.md:15-16` („A plan member writes only the projected entries its plan item assigns…”) zostaje bez zmian: zdanie powtarza warunek WAY-126 — zadanie planu, którego kod uczyniłby prawdziwym wpis innej pozycji, wraca najpierw do planu — a zmiana pozwalałaby zapisywać części wpisów, których plan zadaniu nie przypisuje.

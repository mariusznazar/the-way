---
title: "the way: audyt procesu ma odpowiadać, czy sprzeczność z ustaleniami wyszła dopiero po napisaniu kodu"
status: draft
created: 2026-11-14T18:00
updated: 2026-11-15
tags: [zadanie]
related: "a note of the author's project in the private notes"
---

# Audyt procesu odpowiada, czy sprzeczność z ustaleniami wyszła dopiero po napisaniu kodu

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Cotygodniowy audyt procesu odpowiada przy każdej wersji procesu na pytanie Q1: czy sprzeczność z ustaleniami wyszła dopiero wtedy, gdy kod był już napisany.
- Odpowiedź mówi Mariuszowi, czy cykl bez specu (WAY-135) przepuszcza sprzeczności do przeglądu gotowego kodu, czy etap projektowania przed kodem je łapie.
- Dziś Q1 brzmi `unknown` we wszystkich 42 seriach liczenia z 2026-11-14, bo zapis cyklu nie mówi, czy runda przeglądu znalazła sprzeczność z ustaleniami.
- Mariusz wybrał na audycie 2026-11-14, że Q1 ma dostać odpowiedź, zamiast zniknąć z audytu.

### To do

1. Recenzent oznacza w raporcie każdą blokującą uwagę: czy jest sprzecznością z ustaleniami, a przy „tak” wskazuje wpis albo ustalenie, z którym kod się kłóci (metoda przeglądu, `task-cycle/review/SKILL.md`, sekcja „3. Grade”). Sprzeczność to uwaga, że zmiana robi coś wbrew wpisowi fundamentu albo wbrew ustaleniu z dokumentu zadania (pytanie 2); niedokończony punkt *To do* nią nie jest.
2. Prowadzący cykl przenosi oznaczenie razem z uwagami do pliku uwag (`task-cycle/skill/SKILL.md`, akapit zaczynający się od „For a fix, it gives the findings file”), a we wpisie rundy w pozycji *Review rounds* szablonu `task-cycle/record_template.md` zapisuje, czy runda miała sprzeczność z ustaleniami.
3. Liczenie audytu (`process-audit/audit_count.py`, funkcja `read_contradiction`) czyta tę odpowiedź z zapisu: Q1 cyklu to `yes`, gdy którakolwiek runda ma sprzeczność albo *Discarded attempt* ma znacznik `open design choice` (punkt 6); `no`, gdy żadna runda jej nie ma, a *Discarded attempt* czyta się jako `none` albo ma znacznik `reserved choice` lub `size`. Liczenie nie wnioskuje sprzeczności z treści uwag recenzenta ani z tekstu *Discarded attempt*.
4. Szablon zapisu dopuszcza w *Review rounds* wpis przeglądu bez poprawek we własnej formie: otwierany słowem `review`, z wynikiem `PASS` i ścieżką raportu, bez pliku uwag (pytanie 3). Liczenie nie dolicza takiego wpisu do kosztu rund poprawek (WAY-337), a dla Q1 czyta go jako brak sprzeczności; wpis w żadnej z dwóch form nadal daje `unknown` z powodem.
5. Wpis rundy poprawek bez oznaczenia — w zapisie sprzed zmiany i po niej — daje Q1 `unknown` z jednym powodem: „wpis rundy nie mówi, czy była sprzeczność” (pytanie 4), w miejsce dzisiejszego `a review round names findings, and their content is not in the record`.
6. Zapis cyklu daje powodowi porzuconej próby stałe miejsce w pozycji *Discarded attempt*, z jednym z trzech znaczników: `open design choice`, `reserved choice`, `size` (pytanie 5) — w szablonie `task-cycle/record_template.md` (pozycja „Discarded attempt”) i tam, gdzie prowadzący cykl zapisuje odrzucenie: `task-cycle/skill/SKILL.md`, akapity zaczynające się od „An agent that meets an open design choice while it makes the change” i „A one-author change that proves too large”, oraz `task-cycle/skill/reserved_return.md`, sekcja „Discard the attempt”. Liczenie czyta tylko znacznik: wpis bez niego — także każdy zapis sprzed zmiany — daje Q1 `unknown` z powodem, a wykrywanie zaprzeczeń w tekście pozycji (`denied_before` i słowa przeczące) znika. Test liczenia sprawdza, że cztery przykłady recenzenta #100 dają `unknown`: `open design choice not found`, `an open design choice did not apply`, `no sign whatsoever that this was an open design choice`, `No attempt was discarded for a reserved choice, an oversized change or an open design choice`.

### Questions to settle

- 1. Kto ocenia, czy uwagi rundy zawierały sprzeczność z ustaleniami?
  - Answer: recenzent, przy każdej blokującej uwadze; prowadzący cykl przenosi oznaczenie do pliku uwag i do wpisu rundy w zapisie. Przerwanie serii kosztu w audycie (WAY-339) przyjęte.
  - Not chosen:
    - prowadzący cykl przy pisaniu wpisu rundy — ocenia z drugiej ręki, bez lektury fundamentu, którą zrobił recenzent; uwaga o rozjeździe z odpowiedzią w zadaniu wymaga od niego sięgnięcia do źródeł, czyli dokłada kontekst w najdroższym miejscu cyklu
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „1 a — ocenia recenzent przy każdej blokującej uwadze; przerwanie serii kosztu przyjęte”
- 2. Co się liczy jako sprzeczność z ustaleniami?
  - Answer: blokująca uwaga, że zmiana robi coś wbrew wpisowi fundamentu (także wpisowi, który sama pisze) albo wbrew ustaleniu z dokumentu zadania — odpowiedzi pod *Questions to settle*, wierszowi *Settlements to record*, wpisowi z *Decisions in play*. Niedokończony punkt *To do* się nie liczy.
  - Not chosen:
    - tylko wpis fundamentu — Q1 pominie rozjazdy z ustaleniami zadania, choć spec przed kodem też by je wyłapał
    - każda blokująca uwaga o niespełnionym wymaganiu, także pominięty punkt *To do* — Q1 liczyłoby niedoróbki wykonawcy, których żaden spec by nie złapał, i „tak” przestałoby mówić coś o specu
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „2 b — wpis fundamentu albo ustalenie z dokumentu zadania; niedokończony punkt To do się nie liczy”
- 3. Co z rundami przeglądu bez poprawek, które cykle wpisują dziś w *Review rounds*?
  - Answer: dopuścić je w szablonie z własną formą — wpis otwierany słowem `review`, z wynikiem `PASS` i ścieżką raportu, bez pliku uwag; liczenie nie dolicza takiego wpisu do kosztu rund poprawek, a dla Q1 czyta go jako brak sprzeczności.
  - Not chosen:
    - zabronić ich w *Review rounds* (ślad zostaje w tabeli zdarzeń) — prowadzący chce te przeglądy gdzieś podsumować, więc bez innego miejsca dalej tu trafią, a każdy taki zapis da `unknown`
    - liczenie pomija po cichu każdy wpis nieotwierany słowem `findings` — runda poprawek z literówką w otwarciu zniknie bez śladu, dając fałszywe „nie” w Q1 i zaniżony udział kosztu poprawek
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „3 b — dopuścić przegląd bez poprawek z własną formą (review, wynik PASS, ścieżka raportu); skrypt nie dolicza go do kosztu poprawek, a dla Q1 czyta jako brak sprzeczności”
- 4. Czy liczenie ma odróżniać w powodzie `unknown` zapis w starej formie od zapisu w nowej formie bez odpowiedzi?
  - Answer: nie — jeden powód, „wpis rundy nie mówi, czy była sprzeczność”, dla zapisu starego i nowego.
  - Not chosen:
    - dwa powody, rozpoznane po wersji procesu, na której ruszył cykl — więcej kodu i testów w skrypcie i trzeci powód dla cyklu z nieznaną wersją, a tabela wersji już pokazuje Q1 osobno dla każdej wersji
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „4 b — jeden powód »wpis rundy nie mówi, czy była sprzeczność«”
- 5. Jak liczenie ma czytać *Discarded attempt*, żeby zaprzeczenie zapisane innymi słowami („open design choice not found”) nie dawało Q1 `yes`?
  - Answer: stały znacznik powodu — powód porzuconej próby stoi w *Discarded attempt* w stałym miejscu jako jedno z trzech słów: `open design choice`, `reserved choice`, `size`; liczenie czyta tylko znacznik, a wykrywanie zaprzeczeń w tekście pozycji znika. Test: cztery przykłady recenzenta #100 dają `unknown`.
  - Not chosen:
    - poszerzyć wykrywanie zaprzeczeń (zaprzeczenie po frazie, dalej niż cztery słowa, rządzące listą po przecinku → `unknown`) — zmienia tylko skrypt, ale kolejne nieprzewidziane sformułowanie znów da fałszywe „tak”, a zostaje wnioskowanie z tekstu, które wiersz 1 odrzuca dla rund
    - zostawić i dopisać test utrwalający obecne zachowanie jako znane ograniczenie — najtańsze, ale pierwszy porzucony cykl opisany takim zdaniem da fałszywe „tak”, na którym Mariusz waży, czy cykl potrzebował specu
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15: „pytanie 5 — a, stały znacznik powodu (open design choice / reserved choice / size), liczenie czyta tylko znacznik, test: cztery przykłady recenzenta dają unknown”; pytanie wyrosło z przeglądu fundamentu 2026-11-14, G7 (uwaga #100-6), decyzja Mariusza: „sprawdzić, czy zaprzeczenia z #100-6 w *Discarded attempt* wciąż dają »tak«, i dopisać test form zaprzeczenia”

## Context

- Cały dokument, z trzema wierszami *Settlements to record*, przyjął 2026-11-14 doradca dnia, powołując się na upoważnienie Mariusza z 18:05 do akceptacji w jego imieniu: „akceptuję cały dokument w obecnym brzmieniu, z trzema wierszami Settlements (z upoważnienia Mariusza z 18:05)”.
- Dokument po doprecyzowaniu z 2026-11-15 (pytanie 5, *To do* 6, wiersz 4) przyjął w całości 2026-11-15 doradca dnia z tego samego upoważnienia: „AKCEPTUJĘ cały dokument zadania […] w tym brzmieniu (przeczytany w całości, z czterema wierszami Settlements)”.
- Q1 wprowadził commit `260b650` („Count the process versions in series with their three answers”) jako jedno z trzech pytań o upraszczanie specu i planu.
- Liczenie daje dziś `no` tylko, gdy *Discarded attempt* to `none` i *Review rounds* nie ma żadnej rundy; przy rundzie z uwagami zwraca `unknown` z powodem `a review round names findings, and their content is not in the record` (`process-audit/audit_count.py`, funkcja `read_contradiction`, ok. linii 1131, rewizja `21ecb62`).
- Forma *Review rounds*, którą liczenie przyjmuje, stoi w funkcji `review_rounds` tego pliku (ok. linii 1045, rewizja `21ecb62`): `none` albo wpisy pod pozycją, każdy otwierany słowem `findings` i ścieżką `reports/<file>.md` w odwrotnych apostrofach. Tę samą formę czyta udział kosztu rund poprawek (WAY-337).
- Przykład zapisu, którego liczenie nie przyjmuje: `docs/task-cycles/worktrees-removed-after-merge/cycle.md` w commicie `53c5b24`, pozycja *Review rounds* — pierwszy wpis zaczyna się od `findings`, trzy kolejne (przegląd kroku powrotu, przegląd poprawki bramki, przegląd korekty 1) to przeglądy bez poprawek i od `findings` się nie zaczynają.
- Wiadomość rundy poprawek nazywa plik uwag po ścieżce w `reports/`, a prowadzący cykl pisze ten plik słowami recenzenta z jego blokujących uwag (`task-cycle/skill/SKILL.md`, akapit zaczynający się od „For a fix, it gives the findings file”).
- Zmiana plików pod `task-cycle/review` zaczyna nową serię kosztu w audycie (WAY-339); zmiana `task-cycle/record_template.md`, plików `task-cycle/skill/` i `process-audit/audit_count.py` — nie (lista `TREE_PATHS` w `audit_count.py`).
- Decyzja z audytu i zacytowane powody `unknown`: `the author's private note of the audit's decision of 2026-11-14`, sekcja *Weighed*, „Sprawa 4”.
- Skala: `the author's private note of the audit's count of 2026-11-14`, sekcja *Process versions* (kolumna Q1) i *Unknown values*.
- Przegląd fundamentu 2026-11-14 (G7, uwaga #100-6) przywrócił zadanie do doprecyzowania: dzisiejsza `read_contradiction` daje fałszywe „tak”, gdy zaprzeczenie stoi po frazie „open design choice”, dalej niż cztery słowa przed nią albo rządzi listą po przecinku; zadanie w brzmieniu z 2026-11-14 tej ścieżki nie zmieniało, stąd pytanie 5 i punkt 6.
- Żaden zapis cyklu the-way (252 commity zmieniające pliki `docs/task-cycles/*/cycle.md`, stan 2026-11-15) nie ma w *Discarded attempt* nic poza `none`; w zapisach Loop dwa wpisy mówią o odrzuceniu z powodu rozmiaru i dają dziś Q1 `unknown` — po zmianie, jako zapisy bez znacznika, nadal `unknown`.
- Plik danych przeglądu fundamentu 2026-11-14: `the author's private data file of the foundation review of 2026-11-14`, sekcja „Grupy uwag”, G7.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-337 — How is the cost of a cycle measured?: „A turn of an agent serves a fix round when the message that dispatches or resumes it names the round's findings file by its path in the cycle's `reports/`, which only the messages of that fix and of the review of that fix do, and the cycle's record names each round by that path. The share is `0.0%` only where the record says the cycle had no fix round, and unknown wherever the record and the stages cannot tie each round to the turns that served it.”
- WAY-339 — When do the measures of the audit stop being comparable?: „A new price list, or a change of the form of a stage report, of the list of classes or of the instructions of the reviewer, starts a new series of measures […]”
- WAY-135 — When does a task's cycle write a spec? (to, co Q1 mierzy): „A task's cycle writes a spec, reviewed by an agent other than its author, before implementation and any plan where the task leaves an open design choice and nowhere else […]”
- WAY-263 — Which foundation mismatches are Important findings? (oznaczenie z punktu 1 obejmuje te uwagi): „A reviewer grades as Important a finding that a change departs from a foundation entry it writes or changes: the change's files do what the entry forbids, fail to do what it requires, or restate it differently, including more broadly or without a qualification.”

## Settlements to record

Candidates: 4 shown, 4 accepted — 2026-11-15

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Recenzent oznacza przy każdej blokującej uwadze, czy jest sprzecznością z ustaleniami — z wpisem fundamentu albo ustaleniem z dokumentu zadania, nie niedokończonym punktem *To do* — a liczenie audytu bierze Q1 z tego oznaczenia w zapisie cyklu, nigdy z treści uwag. | decision | pytania 1 i 2 (ich *Not chosen*); kierunek z audytu 2026-11-14, `audit-2026-11-14.md`, „Sprawa 4” | kolejna zmiana metody przeglądu albo liczenia mogłaby przenieść ocenę na prowadzącego cykl, poszerzyć ją o pominięte punkty *To do* albo kazać liczeniu wnioskować z tekstu uwag, nie wiedząc, że to odrzucono |
| 2 | Pozycja *Review rounds* przyjmuje też przegląd bez poprawek we własnej formie (`review`, wynik `PASS`, ścieżka raportu); taki wpis nie jest rundą poprawek dla udziału kosztu, a dla Q1 znaczy brak sprzeczności. | sentence of WAY-337 | pytanie 3 (jego *Not chosen*) | kolejna zmiana szablonu zapisu mogłaby zabronić takich wpisów albo kazać liczeniu po cichu pomijać każdy wpis nieotwierany słowem `findings` |
| 3 | Runda bez oznaczenia daje jeden powód `unknown`, „wpis rundy nie mówi, czy była sprzeczność”, w zapisie starym i nowym. | data or code: `process-audit/audit_count.py`, funkcja `read_contradiction` | pytanie 4 (jego *Not chosen*) | cykl mógłby dorobić rozróżnienie starej i nowej formy po wersji procesu |
| 4 | Powód porzuconej próby stoi w *Discarded attempt* jako jeden z trzech znaczników — `open design choice`, `reserved choice`, `size` — a liczenie audytu bierze z tej pozycji Q1 tylko ze znacznika, nigdy z jej tekstu. | decision | pytanie 5 (jego *Not chosen*) | kolejna zmiana liczenia mogłaby wrócić do wykrywania zaprzeczeń w tekście albo je poszerzać, a zmiana szablonu zapisu — zdjąć znacznik jako zbędną formalność, nie wiedząc, że to odrzucono |

## Out of scope

none

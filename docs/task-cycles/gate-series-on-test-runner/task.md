---
title: the way: audyt procesu — nowa seria czasów bramki po równoległych katalogach
status: draft
created: 2026-11-13T22:00
updated: 2026-11-13
tags: [zadanie]
related: "the author's note of the project this task belongs to"
---

# the way: audyt procesu — nowa seria czasów bramki po równoległych katalogach

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Od scalenia prośby #111 skrypt testów the way (`gate/run_tests.py`) uruchamia katalogi testów jednocześnie, więc czas jednego katalogu w zapisie cyklu jest od tej pory czasem pod obciążeniem pozostałych katalogów, a czas całego przebiegu spada.
- Cotygodniowy audyt procesu zaczyna nową serię czasów bramki tylko przy zmianie skryptu, który je mierzy (`task-cycle/gate_times.py`), a #111 go nie zmieniła, tak jak kazało jej zadanie.
- Audyt wrzuca więc przebiegi sprzed #111 i po niej do jednej serii: mediana całego przebiegu spada, mediany pojedynczych katalogów rosną, a audyt porównuje je tak, jakby jedna wersja procesu była szybsza albo wolniejsza od drugiej.
- Odczuwa to Mariusz przy cotygodniowym audycie: dopóki to trwa, przy czytaniu wyników trzeba pamiętać, że porównanie miesza dwa sposoby uruchamiania bramki.
- Bez zmiany nic się nie psuje, a mieszanie słabnie dopiero, gdy przebiegów nowego rodzaju będzie więcej niż starych.

### To do

1. Audyt zaczyna nową serię czasów bramki także przy wersji procesu, w której `gate/run_tests.py` różni się od poprzedniej wersji, i podaje to jako powód podziału; pozostałych serii ta zmiana nie dzieli.
2. Reguła audytu (`process-audit/SKILL.md`, akapit „Measures are compared inside a series only”) i decyzja WAY-339 mówią to samo, z WAY-339 zmienioną tak, jak niesie to wybrana odpowiedź.

### Questions to settle

- Jak audyt ma oddzielić przebiegi bramki sprzed równoległych katalogów od przebiegów po nich?
  - Answer: Każda zmiana `gate/run_tests.py` zaczyna nową serię czasów bramki, tak jak dziś zmiana `task-cycle/gate_times.py`; zmienia to WAY-339.
  - Not chosen:
    - znacznik przy każdym przebiegu (ile katalogów biegnie naraz), zapisany przez `gate_times.py` w nowej kolumnie, i porównanie tylko przebiegów tego samego rodzaju — zmiany w skrypcie testów, w `gate_times.py` i w odczycie audytu, nowy kształt tabeli (zmiana WAY-349 i WAY-350), obsługa starych zapisów bez znacznika, a przebiegi od #111 do scalenia tego zadania zostają zmieszane ze starymi
    - zostawić jak jest i zamknąć zadanie — audyty przez kilka tygodni mieszają dwa rodzaje przebiegów i trzeba o tym pamiętać przy czytaniu, dopóki nowych nie będzie więcej niż starych
  - Source: Mariusz (przez doradcę dnia), 2026-11-13: „1 a, z listą To do jak proponujesz.”

## Context

- Źródło zadania: zapis cyklu `gate-parallel-directories` (commit `575f286` w historii the way), plik `reports/whole-review-report.md`, uwaga 6, oraz opis prośby #111, pozycja 1 sekcji „Fix or let through”, gdzie wybrano osobne zadanie zamiast poprawki w prośbie.
- Licznik audytu dzieli serie czasów bramki w funkcji `instrument_series` w `process-audit/audit_count.py`, porównując między wersjami procesu jeden plik — stałą `GATE_SCRIPT = "task-cycle/gate_times.py"` (ok. linii 404, revision `715ae20`).
- Licznik wylicza serie od nowa z historii gita przy każdym liczeniu, więc zmieniona reguła podziału obejmie też cykle, które przebiegły po #111 przed scaleniem tego zadania.
- Wersją procesu cyklu produktu jest przypięty commit the way, a bramka gry uruchamia przypięty `.the-way/gate/run_tests.py` (kontekst zadania #111), więc gra przejdzie na przebiegi równoległe z chwilą przesunięcia przypiętej wersji.
- Produkt może wpisać w swoje polecenie bramki `--jobs 1` i uruchamiać katalogi po kolei także na nowej wersji procesu; zmiany polecenia bramki produktu audyt nie widzi.
- Licznik innych przebiegów z WAY-350 liczy przebiegi skryptu bramki, nie katalogi wewnątrz jednego przebiegu, więc tych dwóch rodzajów nie rozdziela (uwaga 6 recenzji).
- `gate/run_tests.py` zmieniał się 9 razy w całej historii the way, 3 razy od września 2026: dwa commity #111 i `546eb52`, który dopisał nazwy pominiętych testów.
- Wytycznych kodu i testów część `process-audit` nie ma i ich nie potrzebuje: the way odstępuje od nich dla własnego kodu i testów (WAY-328), więc odczyt wytycznych nic tu nie znalazł.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-339 — When do the measures of the audit stop being comparable?** „A new price list, or a change of the form of a stage report, of the list of classes or of the instructions of the reviewer, starts a new series of measures, except for the measures of how a cycle's agents use context and the prompt cache (WAY-347) and the times of the gate (WAY-349): a new series of those starts only with a change of the script that counts them or of the script that records them, and no change of the instructions of the cycle, the reviewer's and the author's included, starts one.” Zadanie zmienia tę decyzję: nową serię czasów bramki zaczyna też zmiana skryptu testów procesu (`gate/run_tests.py`), który wypisuje czas każdego katalogu; jej *Verification* i uzasadnienie mówią to samo, z uzasadnieniem, że skrypt testów jest częścią pomiaru czasów. Zgoda Mariusza (przez doradcę dnia) z 2026-11-13: „1 a”.
- **WAY-349 — How does the orchestrator of a task cycle run the product's gate so that the gate times reach the cycle's record?** „The script runs the gate the product declares, measures the time of the whole run and, where the output of the process's test runner reports the time of a directory of tests, the time of each such directory, in whatever order they come, and adds the run to a file in the cycle's record.”
- **WAY-350 — Which runs of the gate does the audit compare between versions of the process?** „The audit compares the times of the gate between versions of the process — the median of each version and whether it falls against the previous version of the same series — only over the runs that passed and during which no other such run was going, and shows the other runs apart.”

## Settlements to record

Candidates: 2 shown, 1 accepted — 2026-11-13

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Każda zmiana `gate/run_tests.py` zaczyna nową serię czasów bramki, tak jak zmiana `task-cycle/gate_times.py`; zmienia to WAY-339. | decision | pytanie „Jak audyt ma oddzielić przebiegi bramki…”, odpowiedź Mariusza (przez doradcę dnia) z 2026-11-13 | czy zmienić tylko kod licznika i skill audytu, zostawiając WAY-339, z którą przegląd porówna zmianę, w starym brzmieniu

## Out of scope

- Polecenie bramki gry i przesunięcie jej przypiętej wersji procesu — osobne zadanie gry.

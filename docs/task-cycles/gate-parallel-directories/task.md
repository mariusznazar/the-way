---
title: "the way: krótsza bramka — katalogi testów równolegle i bez powtarzania przebiegu na stanie wyjściowym"
status: draft
created: 2026-11-12T17:54
updated: 2026-11-13
tags: [zadanie]
related: "the project note of the process"
---

# the way: krótsza bramka — katalogi testów równolegle i bez powtarzania przebiegu na stanie wyjściowym

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Pełny przebieg testów gry (bramka) trwa 23–24 minuty na wolnej maszynie (pomiar z 2026-11-12) i do 28 minut przy jednym cyklu obok, a cykl uruchamia go średnio trzy razy.
- Ok. 22 z tych minut to dwa katalogi testów Pythona gry, które skrypt bramki procesu uruchamia jeden po drugim.
- Pierwszy przebieg cyklu sprawdza stan, z którego cykl startuje, a w 94% cykli gry te same pliki sprawdziła chwilę wcześniej końcowa bramka poprzedniego cyklu.
- Na bramkę czeka Mariusz, bo czeka na cykl, i agent prowadzący cykl, kolejnymi turami, za które Mariusz płaci; przy kilku cyklach naraz bramki wydłużają się nawzajem i brakuje pamięci.
- Bramka rośnie razem z fundamentem: testów niezmienników gry przybyło w trzy tygodnie ze 152 do 259, a każdy cykl czeka na nią trzy razy.

### To do

1. Skrypt bramki procesu (`gate/run_tests.py`) uruchomiony bez katalogu uruchamia katalogi testów jednocześnie, każdy w osobnym procesie, jak dziś. Raport każdego katalogu wypisuje w całości po jego zakończeniu, pod jego linią `== <katalog>`, bez przeplatania z raportami innych katalogów; linia końcowa liczy testy i nazywa katalogi, które padły, jak dziś.
2. Skrypt bramki ma opcję, która ogranicza liczbę katalogów uruchamianych naraz; wartość 1 uruchamia je po kolei, jak dziś. Bez tej opcji biegną wszystkie naraz albo tyle, ile wybierze cykl.
3. Skrypt bramki ma opcję, która wypisuje najwolniejsze testy z ich czasem; bez tej opcji wynik wygląda jak w punkcie 1.
4. Na starcie cyklu agent prowadzący sprawdza w gicie, czy stan wyjściowy jest commitem scalenia o drzewie plików identycznym z drzewem głowy scalonej gałęzi. Jeśli tak, bramki na stanie wyjściowym nie uruchamia: listę testów padających przed zmianą bierze z końcowej bramki tamtego cyklu — także gdy była czerwona — i wpisuje do zapisu cyklu, skąd ją wziął. Listę bierze z zapisu tamtego cyklu w historii gita. Jeśli stan wyjściowy nie jest takim commitem albo scalona gałąź nie ma zapisu cyklu z wynikiem końcowej bramki, uruchamia bramkę na stanie wyjściowym jak dziś. Zmiana dotyczy kroku 4 instrukcji cyklu (`task-cycle/skill/SKILL.md`, akapit zaczynający się od „Create a task branch from the current target branch”, ok. linii 128).
5. Gdy końcowa bramka cyklu, który nie uruchamiał bramki na stanie wyjściowym, pada na teście spoza tej listy, agent prowadzący uruchamia padające testy na stanie wyjściowym, żeby odróżnić błąd zmiany od błędu zastanego, i wpisuje wynik do zapisu cyklu.

### Questions to settle

- Czy cykl uruchamia bramkę na stanie wyjściowym?
  - Answer: Pomija ją, gdy stan wyjściowy jest commitem scalenia o drzewie plików identycznym z głową scalonej gałęzi, i bierze listę padających testów z końcowej bramki tamtego cyklu — także gdy była czerwona; w przeciwnym razie działa jak dziś; gdy końcowa bramka pada na czymś spoza tej listy, padające testy uruchamia na stanie wyjściowym.
  - Not chosen:
    - zawsze, jak dziś — jeden pełny przebieg na cykl, w dwóch trzecich przypadków czerwony z powodu środowiska
    - nie robić wcale; przy porażce końcowej bramki sprawdzać padające testy na stanie wyjściowym — wariant pokazany i nie wybrany (raport nie podał przy nim kosztu)
  - Source: decyzja R3 w raporcie the author's report on process improvements, section 7, wybór wariantu (b) przez Mariusza zapisany w pierwotnym tekście tego zadania: „Decyzja z 12.11.2026: na starcie cyklu agent prowadzący sprawdza w gicie, czy stan wyjściowy jest commitem scalenia o drzewie plików identycznym z głową scalonej gałęzi.”
- Czy zmiany w repozytorium gry — przesunięcie przypiętej wersji procesu, ewentualne uruchamianie testów Node obok katalogów Pythona w `scripts/test.py` gry i trzy przebiegi pod rząd bez losowych porażek testów z Dockerem — należą do tego zadania, czy do osobnego zadania gry?
  - Answer: Do osobnego zadania gry. To zadanie obejmuje tylko repozytorium the way; zadanie gry — przesunięcie przypiętej wersji procesu, decyzja o testach Node obok katalogów Pythona w `scripts/test.py` i trzy przebiegi pod rząd bez losowych porażek testów z Dockerem — powstaje po zakończeniu tego doprecyzowania.
  - Not chosen:
    - jedno zadanie na oba repozytoria — cykl the way nie pisze poza swoim repozytorium, a the way nie ma testów z Dockerem, więc zadanie utknęłoby na punkcie, którego jego cykl nie umie zrobić ani sprawdzić
  - Source: Mariusz (przez doradcę dnia), 2026-11-13: „a) dzielimy — to zadanie obejmuje tylko the way; zadanie gry zaproponuj po skończeniu tego.”
- Czy równoległość katalogów da się wyłączyć bez zmiany procesu, np. gdy testy z Dockerem w grze padają pod obciążeniem?
  - Answer: Tak: domyślnie katalogi biegną równolegle, a opcja skryptu bramki ogranicza liczbę katalogów uruchamianych naraz; 1 uruchamia je po kolei, jak dziś. Produkt wpisuje ją w swoje polecenie bramki.
  - Not chosen:
    - zawsze równolegle, bez wyłącznika — gra nie przyjmie nowej wersji procesu, dopóki nie naprawi izolacji testów z Dockerem, jeśli te padną pod obciążeniem
    - domyślnie po kolei, równolegle tylko z opcją — zysk dopiero po zmianie polecenia bramki, także w samym the way, którego polecenie jest dziś jednym gołym poleceniem (WAY-16)
  - Source: Mariusz (przez doradcę dnia), 2026-11-13: „b) — domyślnie równolegle, z opcją limitu katalogów naraz.”

## Context

- Pomiar bramki gry: sekcja 1 notatki the author's note of measurements before changes of the process — `tests/invariants` 11,5–12,8 min, `tests/deploy` 9,6–10,2 min, testy Node ok. 1 min; przy jednym cyklu obok 24,0–28,0 min; pamięć bramki w szczycie 3–4 GB, maszyna przy jednym cyklu obok najwyżej 20,8 z 31,8 GB.
- Szacunek zysku z równoległych katalogów to przeliczenie, nie pomiar: ok. 15–16 minut zamiast 23–24, jeśli dwa ciężkie katalogi zwolnią się nawzajem tak jak dwie pełne bramki (+17%); dla trzech–pięciu cykli naraz liczby nie ma.
- Karty działań D1 i D2 oraz tabela konfliktów: card D1 of the author's report on process improvements, card D2 of the author's report on process improvements, its table of conflicts.
- W the way stan wyjściowy ma drzewo identyczne z głową scalonej gałęzi w 99 ze 111 scalonych gałęzi zadań, w grze w 65 z 69.
- Dziś pętla w `run_all` czeka na każdy proces katalogu, zanim uruchomi następny (`gate/run_tests.py`, pętla `for directory in directories:`, ok. linii 93, revision `fca8491`).
- Skrypt czasu bramki (`task-cycle/gate_times.py`) czyta czas katalogu z bloku, który otwiera linia `== <katalog>`, i z pierwszej linii `Ran <n> tests in <s>s` w tym bloku, w dowolnej kolejności katalogów; dlatego raport katalogu musi zostać jednym blokiem.
- Odrzucony wariant decyzji WAY-349 („the test runner of the process writing the times to a file itself”) wspomina, że kolidowałby z zadaniem uruchamiania katalogów równolegle — tamta decyzja przewidziała to zadanie.
- Umowa z produktami (wpis `test-runner-command` mapy części): polecenie zachowuje nazwę, argument i kody wyjścia; nowa opcja tego nie narusza.
- `unittest` w Pythonie 3.14 przyjmuje w `TextTestRunner` parametr `durations` (sprawdzone `inspect.signature` na Pythonie 3.14.3 tej maszyny).
- The way ma 10 katalogów testów i żaden nie używa Dockera; gra ma 4 katalogi, a Dockera używa 18 z 20 plików `tests/deploy` i 16 z 57 plików `tests/invariants` (karta D1).
- Gra przypina proces na `55afa8e`, a jej `scripts/test.py` uruchamia budowanie, testy Node, `.the-way/gate/run_tests.py` i kontrolę fundamentu po kolei i przerywa na pierwszym etapie, który padnie.
- Wynik końcowej bramki poprzedniego cyklu stoi w sekcji *Verification* jego zapisu, a kopię zapisu cykl dodaje do `docs/task-cycles/<task-slug>/` na gałęzi zadania i zaraz usuwa, więc jest w historii gita scalonej gałęzi; stoi też w sekcji *Checks* opisu prośby.
- Przebieg na stanie wyjściowym opisują też: krok 2 instrukcji cyklu (przesunięcie przypiętej wersji), krok 10 (lista przebiegów bramki), sekcja *Verification* szablonu zapisu (`task-cycle/record_template.md`), wariant prośby z wyborem zastrzeżonym w `task-cycle/skill/request_template.md` i decyzja WAY-349.
- `agent-instructions/README.md` podaje czas pełnego przebiegu testów the way: „The whole run takes about 16 minutes”.
- Ryzyko z karty D2: reguła z punktu 4 zakłada, że maszyna między cyklami się nie zmieniła; nową porażkę wyłapuje punkt 5, ale test z listy, który zmiana psuje naprawdę, zostanie wzięty za zastany — tak samo jak dziś, gdy pada na stanie wyjściowym z powodu środowiska.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-16 — How are the checks of invariants run?** „One command runs all of a product's tests, the tests of its invariants among them — the same command for an agent, for a human and for whatever runs it when a change is merged — and no list of checks written by hand stands beside it.” Opcja limitu katalogów jest częścią tego jednego polecenia, nie drugim poleceniem.
- **WAY-55 — Which part of the process holds the gate?** „In this repository, the gate is a part of the process of its own, and its directory is `gate/`: the gate's code and the test of every critical flow are files there. (…) Which checks a change calls for, when the gate runs and what follows from what it reports belong to the task cycle, not to this part.” Punkty 1–3 zmieniają część `gate`, punkty 4–5 — część `task-cycle`.
- **WAY-160 — How does the task-cycle orchestrator run the finished change's gate?** „The task-cycle orchestrator itself runs the product's gate on the tree that goes into the request, and the request gives its command and exit code and names each check that failed or did not run; a check that did not run is unchecked, never passed.” Lista z punktu 4 opiera się na tym wyniku poprzedniego cyklu.
- **WAY-243 — How is a flaky test treated?** „The template of the testing discipline requires the rule that running a flaky test again serves only the diagnosis of what makes it flaky, never making a run of the gate pass (…).” Uruchomienie padających testów na stanie wyjściowym (punkt 5) rozpoznaje, skąd porażka, i nie zmienia wyniku bramki.
- **WAY-349 — How does the orchestrator of a task cycle run the product's gate so that the gate times reach the cycle's record?** „The orchestrator of a task cycle runs the product's gate through a script of the process at every run, the run on the starting state included. The script runs the gate the product declares, measures the time of the whole run and, where the output of the process's test runner reports the time of a directory of tests, the time of each such directory, in whatever order they come, and adds the run to a file in the cycle's record.” Jej *Verification* („complies: the orchestrator runs the gate through the script on the starting state and on the finished tree”) zakłada, że przebieg na stanie wyjściowym jest zawsze. Zadanie zmienia tę decyzję: przebieg na stanie wyjściowym idzie przez skrypt wtedy, gdy cykl go robi (punkt 4), a *Verification* wymaga przebiegu na stanie wyjściowym tylko w takim cyklu — zgoda Mariusza (przez doradcę dnia) z 2026-11-13: „1 a (zadanie zmienia WAY-349 jednym zdaniem i sposób sprawdzania)”.

## Settlements to record

Candidates: 5 shown, 2 accepted — 2026-11-13

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Bramka uruchamia katalogi testów domyślnie równolegle, z opcją limitu katalogów naraz, gdzie 1 uruchamia je po kolei; produkt wpisuje opcję w swoje polecenie bramki. | decision | pytanie „Czy równoległość katalogów da się wyłączyć…”, odpowiedź Mariusza z 2026-11-13 | czy skrypt ma wyłącznik i czy domyślnie biegnie równolegle, czy po kolei |
| 2 | Cykl pomija bramkę na stanie wyjściowym, gdy stan wyjściowy jest commitem scalenia o drzewie plików identycznym z głową scalonej gałęzi, i bierze listę padających testów z końcowej bramki tamtego cyklu, także czerwonej; gdy końcowa bramka pada na czymś spoza tej listy, padające testy uruchamia na stanie wyjściowym. | decision | pytanie „Czy cykl uruchamia bramkę na stanie wyjściowym?”, decyzja Mariusza z 2026-11-12 | czy regułę zapisać tylko w kroku 4 instrukcji cyklu, bez decyzji w dzienniku, którą przegląd zmiany porówna z instrukcją |

## Out of scope

- Równoległość plików testów w obrębie jednego katalogu — osobny, późniejszy krok.
- Zmiany w repozytorium gry, z trzema przebiegami pod rząd bez losowych porażek testów z Dockerem — osobne zadanie gry.

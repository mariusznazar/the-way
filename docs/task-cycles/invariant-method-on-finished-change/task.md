---
title: "the way: reguła produktu może czytać „test”, gdy test powstaje później w tej samej zmianie, a pilnuje tego automat"
status: draft
created: 2026-11-01T09:00
updated: 2026-11-08
tags: [zadanie]
related: "the project note of the author's process work in his notes"
---

## Po co to

- **Jak jest dziś:** każda reguła produktu pilnowana w the way (niezmiennik) ma pole metody: `test` albo `review`. Zasada WAY-61 mówi, że dopóki testu nie ma, wpisuje się `review`. Agenci wpisują jednak od razu `test`, gdy test ma powstać kilka kroków dalej w tym samym PR-ze. W loop2 tak powstało 27 wpisów, a drogą z zasady 11, więc większość idzie wbrew zapisowi.
- **Kto to odczuwa:** agenci, którzy muszą sami rozstrzygać sprzeczność i zgłaszają ją w raportach. Mariusz odczułby to, gdyby test nie powstał, bo dokumentacja dalej mówiłaby, że regułę pilnuje test, a nikt by tego nie sprawdził.
- **Co jeśli nic:** dziś nic się nie psuje. Na `origin/main` w loop2 wszystkie 98 wpisów `test` i na `origin/foundations` w the-way wszystkie 15 mają test, który je cytuje. Sprzeczność zostaje, a zapomniany test nie da żadnego sygnału.

# the way: reguła produktu może czytać „test”, gdy test powstaje później w tej samej zmianie, a pilnuje tego automat

Status: ready for cycle
Project relation: independent

## Description

### Need

- Zasada WAY-61 każe wpisać metodzie niezmiennika `review`, dopóki żaden test go nie cytuje, a cykle zadań wpisują `test` od razu, gdy test ma powstać w późniejszym kawałku planu tej samej zmiany.
- Agenci cyklu muszą tę sprzeczność rozstrzygać sami i zgłaszają ją w raportach; w loop2 PR #43 agent wpisów fundamentu zapisał pięć niezmienników z metodą `test` wzorem dwóch wcześniejszych cykli, a o tym, czy testy powstały, przesądziło tylko to, że orkiestrator z własnej inicjatywy kazał to sprawdzić.
- Nic dziś nie sprawdza, czy wpis `test` ma test, który go cytuje: zapomniany test zostawiłby w fundamencie fałszywe `test`, a odbiorcą tej szkody jest Mariusz, który czyta fundament jako opis tego, co produkt naprawdę pilnuje.

### To do

1. WAY-61 dostaje po zdaniu kończącym się „it names no command and no script.” zdanie: „The method is held on the finished change: an invariant whose test a later slice of the same change writes may read `test` from its writing on.”; z tym zdaniem zgadzają się jej przykład zgodny, przykład niezgodny „an invariant reads `test` while no test cites it” i uzasadnienie „An invariant may be written before its test, and its method then says what keeps it meanwhile: the review.”
2. `elements/invariants/template.md` w sekcji „Method and test” mówi to samo co nowa WAY-61 zamiast „An invariant whose test is not written yet reads `review` (WAY-61).”
3. `elements/common/foundation_check.py` zgłasza każdy niezmiennik, którego metoda czyta `test`, a który nie ma ani jednej linii `invariant: <identyfikator>` w pliku śledzonym przez git innym niż Markdown, w każdym uruchomieniu poza tym, które wywołano z przełącznikiem pomijającym to sprawdzenie (pytanie 2).
4. Uruchomienie `foundation_check.py` zaraz po zapisaniu wpisu (`elements/common/way_of_working.md`, krok 4.3) używa tego przełącznika, więc wpis `test`, którego test powstanie później w tej samej zmianie, nie daje tam błędu (pytanie 2).

### Questions to settle

- Pytanie 1: którą drogą usunąć sprzeczność między WAY-61 a praktyką cykli?
  - Answer: zmienić WAY-61 tak, by metodę oceniać na gotowej zmianie, i dodać sprawdzenie automatyczne, że każdy wpis `test` ma test, który go cytuje.
  - Not chosen:
    - dopisać w `task-cycle/plan/SKILL.md`, że wpis czyta `review`, a kawałek planu piszący test zmienia go na `test` — czwarte miejsce tej samej reguły, którą agenci znali i świadomie omijali; kilka niezależnych kawałków planu musiałoby zmieniać ten sam plik niezmienników, czego zabrania `task-cycle/plan/SKILL.md:174` („Two slices change the same file only where one depends on the other.”).
  - Source: Mariusz, 2026-11-01 — dokument tego zadania, sekcja „Co zmienić”, po krytyce propozycji ze sprawy AIR-562.
- Pytanie 2: gdzie biegnie nowe sprawdzenie, skoro `foundation_check.py` uruchamia się także zaraz po zapisaniu wpisu, gdy testu jeszcze nie ma?
  - Answer: sprawdzenie biegnie w każdym uruchomieniu `foundation_check.py`, więc także w jednym poleceniu testów każdego produktu, bez zmiany tego polecenia; pomija je tylko uruchomienie zaraz po zapisaniu wpisu, które woła skrypt z przełącznikiem. Słaby punkt przyjęty z tą drogą: jeden przełącznik do pamiętania przy zapisie wpisu; agent, który go zapomni, zobaczy błąd i może cofnąć metodę na `review`, co jest kierunkiem bezpiecznym.
  - Not chosen:
    - osobny tryb skryptu, który produkt dopisuje do swojego polecenia testów — zmiana instalatora i jego testów oraz ręczna zmiana polecenia w loop2 i w każdym przyszłym produkcie; produkt, który tego nie dopisze, nie ma sprawdzenia i nic o tym nie mówi;
    - krok w cyklu, w którym orkiestrator sprawdza wpisy przed requestem — zmiany poza cyklem zostają bez sprawdzenia, cykl dostaje jeszcze jeden krok, a reguła żyje w tekście skilla, który agenci potrafią świadomie ominąć;
    - bez sprawdzenia, tylko zmiana WAY-61 — dziś nic nie kosztuje, ale zapomniany test zostawia w fundamencie fałszywe `test` bez żadnego sygnału.
  - Source: Mariusz, 2026-11-08: „A” — na pytanie „Którą drogę wybierasz: A, B, C czy bez sprawdzenia?”, przy drodze A, której słabość nazwano: przełącznik do pamiętania przy zapisie wpisu.
- Pytanie 3: czy zadanie czeka na własne wytyczne kodowania i testów the way, skoro zmienia skrypt i jego testy w repozytorium bez katalogu `guidelines/`?
  - Answer: nie czeka; zadanie idzie do cyklu drogą z `agent-instructions/README.md`, jak poprzednie zadania the way. Słaby punkt przyjęty z tą drogą: zmiana w skrypcie i jego testy powstają bez spisanych wytycznych, jak dotychczasowe skrypty the way.
  - Not chosen:
    - czekać na zadanie o wytycznych the way — sprzeczność w WAY-61 i brak sygnału o zapomnianym teście trwałyby do jego scalenia, a to zadanie nie ma jeszcze wybranego kierunku.
  - Source: Mariusz, 2026-11-08: „nie czeka” — na pytanie „Czeka czy nie czeka?”, przy drodze, której słabość nazwano: skrypt i testy bez spisanych wytycznych.
- Pytanie 4: czy zdanie trybu rzutowanego w `elements/invariants/skill/SKILL.md:57-58` („Step 3: *Method* reads `review`; the task that writes the invariant turns it to `test` with the test, where a cheap test can check the sentence”), uzasadnienie WAY-71 (`foundations/decisions.md:1675`) i przykład zgodny WAY-117 (`:2681`) zmieniają się razem z WAY-61?
  - Answer: nie, zostają bez zmian: zdanie skilla i przykład WAY-117 mówią o wpisie rzutowanym w definicji projektu, który jeszcze nie stoi w fundamencie, a uzasadnienie WAY-71 o niezmienniku, który testu nie dostanie; żadne nie przeczy nowemu zdaniu WAY-61. Słaby punkt przyjęty z tą drogą: zdanie skilla da się przeczytać tak, jakby `test` wolno było wpisać dopiero w kawałku piszącym test.
  - Not chosen:
    - dopisać doprecyzowanie we wszystkich trzech — trzy miejsca więcej w zmianie, dwa w innych decyzjach, i trzy powtórzenia reguły, która ma stać w jednym miejscu.
  - Source: Mariusz, 2026-11-08: „zostawmy” — na pytanie „Zostawiamy czy zmieniamy?”, przy drodze, której słabość nazwano: niejasność zdania skilla.

## Context

- Źródło zadania: sprawa AIR-562 z przeglądu warstwy AI, 2026-11-01, zapisana w prywatnym zeszycie przeglądu Mariusza; cytat z loop2 PR #43, `loop2@b37cc67:docs/task-cycles/zapis-stanu-na-serwerze/cycle.md:328`: „the invariants template says "An invariant whose test is not written yet reads `review` (WAY-61)", while the plan names each new invariant's check as a test of a later slice”.
- Numery linii poniżej zgadzają się ze stanem `foundations` @ a3206c1: WAY-61 stoi w `foundations/decisions.md:1461-1495`, zdanie z punktu 1 *To do* w `:1465`, przykład zgodny w `:1478-1479`, niezgodny w `:1482`, uzasadnienie w `:1488-1489`; zdanie szablonu z punktu 2 w `elements/invariants/template.md:59-60`.
- `foundation_check.py` sprawdza dziś tylko, czy metoda to `test` albo `review` (`elements/common/foundation_check.py:94`), i czy linia `invariant: <identyfikator>` w pliku innym niż Markdown nazywa istniejący wpis (`:473-483`); sprawdzenia w drugą stronę nie ma.
- `foundation_check.py` biegnie dziś w trzech miejscach: w jednym poleceniu, które uruchamia wszystkie testy produktu (`installation/README.md:71-74`, WAY-16); w the-way przez test `test_the_way_foundation_passes` (`elements/common/test_foundation_check.py:783-787`) uruchamiany przez `gate/run_tests.py`; i zaraz po zapisaniu każdego wpisu przez skill jego rodzaju (`elements/common/way_of_working.md:141-143`).
- W cyklu pełne testy produktu uruchamia tylko orkiestrator, raz na gotowej zmianie (WAY-160); kawałek planu uruchamia tylko swoje testy i testy tego, czego dotyka (`task-cycle/plan/SKILL.md:169-172`).
- W the-way test `test_the_way_foundation_passes` uruchamia skrypt bez przełącznika, więc sprawdzenie kawałka planu, które obejmuje ten test, zgłosi wpis `test` zapisany przed kawałkiem piszącym jego test.
- W the-way @ a3206c1 16 niezmienników czyta `test` i każdy ma linię `invariant:` w śledzonym pliku innym niż Markdown (`git grep`, 2026-11-08), więc nowe sprawdzenie przechodzi na dzisiejszym fundamencie the-way.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-61 — „An invariant's method of checking reads `test` once a test of the product's test suite, written in the product's language and run by the command that runs the product's tests, cites it, and `review` until then, and it names no command and no script. A test checks what its invariant's sentence is about, as it stands on the commit being checked, so a test fed input made up for it is the method of a sentence about the check it exercises, never of one about the data that check reads.” Zadanie zmienia jej zdanie, przykłady i uzasadnienie (punkt 1 *To do*).
- WAY-16 — „One command runs all of a product's tests, the tests of its invariants among them — the same command for an agent, for a human and for whatever runs it when a change is merged — and no list of checks written by hand stands beside it.”
- WAY-65 — „A test cites, at the test that checks it, each invariant it checks as `invariant: <identifier>`. A file is an invariant test of a change when it cites an invariant on the commit the branch left the main branch from or on the commit being checked.” Nowe sprawdzenie liczy cytat w tej postaci.
- WAY-63 — „An invariant's result on the commit being checked is `pass` where every test citing it ran on that commit and passed, and `fail` where one of them failed; a run in which no test citing it ran gives it no result, and nothing written by hand stands in for one. An invariant whose method is review takes no result from a run: the review of each change it reaches compares the change with its sentence. The command running the product's tests exits non-zero when a test fails.” Wpis `test` bez żadnego cytującego testu nie dostaje dziś wyniku po cichu; nowe sprawdzenie zamienia tę ciszę w błąd polecenia testów.
- WAY-160 — „The task-cycle orchestrator itself runs the product's gate on the tree that goes into the request, and the request gives its command and exit code and names each check that failed or did not run; a check that did not run is unchecked, never passed. The gate's run is the orchestrator's alone: no author, executor or reviewer runs it, and neither a plan's *Checks* nor a handoff names a run of it.”

## Settlements to record

Candidates: 6 shown, 3 accepted — 2026-11-08

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Metodę niezmiennika ocenia się na gotowej zmianie: niezmiennik, którego test pisze późniejszy kawałek tej samej zmiany, może czytać `test` od zapisania; zdania w `task-cycle/plan/SKILL.md` o przejściu z `review` na `test` nie ma. | decision | pytanie 1; pytanie przeciw odpowiedzi: Mariusz, 2026-11-08: „zostaje” — wobec zdania z pierwszej wersji propozycji AIR-562 „Przy proponowanym zdaniu zostaje prawdziwe `review`, więc błąd idzie w bezpieczną stronę.”; słaby punkt przyjęty: między zapisaniem wpisu a kawałkiem piszącym test gałąź zadania, także w zablokowanym drafcie requestu, mówi `test` bez testu, a na gałąź główną nie przejdzie dzięki sprawdzeniu z wiersza 2; droga nie wybrana stoi pod pytaniem 1 | czy odrzucona droga ze zdaniem w skillu planu trafia do *Rejected* WAY-61, czy zostaje tylko w historii zadania |
| 2 | Sprawdzenie, że każdy wpis `test` ma test, który go cytuje, biegnie w każdym uruchomieniu `foundation_check.py`, a pomija je tylko uruchomienie zaraz po zapisaniu wpisu, z przełącznikiem. | decision | pytanie 2 | czy sprawdzenie jest domyślne, a wyjątkiem uruchomienie po zapisie, czy odwrotnie — późniejsza zmiana skryptu mogłaby to odwrócić, nie wiedząc, że cisza była powodem wyboru |
| 3 | W fundamencie the-way każdy niezmiennik, którego metoda czyta `test`, ma w pliku śledzonym przez git innym niż Markdown linię `invariant: <identyfikator>`. | invariant | Mariusz, 2026-11-08: „przyjmuję tak jak rekomendujesz” — na propozycję agenta wzorowaną na niezmienniku `map-reference-target`, który cytuje `elements/common/test_foundation_check.py:785`; koszt nazwany: jeden wpis więcej i jedna linia cytatu w teście | czy cykl zapisuje dla nowego sprawdzenia niezmiennik the-way i cytuje go przy teście `test_the_way_foundation_passes` |

## Out of scope

none

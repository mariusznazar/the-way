---
title: "the way: drobne poprawki po PR-ze #155 — niestabilny test usuwania katalogów roboczych i testy nowej reguły zagnieżdżonego wyjścia w czasach bramki"
status: draft
created: 2026-11-21T19:00
updated: 2026-11-21
tags: [zadanie]
related: "the note of the project in the author's backlog"
---

# the way: drobne poprawki po PR-ze #155 — niestabilny test usuwania katalogów roboczych i testy nowej reguły zagnieżdżonego wyjścia w czasach bramki

Status: ready for cycle
Project relation: independent
Defect introduced by: https://github.com/mariusznazar/the-way/pull/125 · https://github.com/mariusznazar/the-way/pull/149

## Description

### Need

- Test `ApplyTest.test_a_dry_run_removes_nothing_and_apply_removes_only_what_is_marked` w `task-cycle/test_remove_merged_worktrees.py` czasem pada bez żadnej zmiany kodu.
- Pierwszy przebieg CI na ostatniej głowie PR-a #155 padł na nim na Linuksie z `AssertionError: Lists differ: [] != ['origin.git/objects/maintenance.lock']`, a ponowne uruchomienie nieudanego zadania przeszło.
- Każdy, kto otwiera PR do the way, może przez to dostać czerwoną bramkę do powtórzenia i dochodzenie, czy to jego zmiana.
- Testy klasy `NestedRunTest` w `task-cycle/test_gate_times.py` nie pilnują reguły, którą skrypt czasów bramki czyta zagnieżdżone wyjście bramki (wyjście kolejnego przebiegu bramki, które drukuje padający test samej bramki).
- Cztery uproszczenia tej reguły przechodzą dziś wszystkie testy, choć każde daje zły wynik na wejściu, które obecna reguła czyta dobrze.
- Kto kiedyś uprości regułę, przejdzie bramkę, a w czasach bramki zapisanych w zapisie cyklu i czytanych przez audyt procesu pojawi się wymyślony katalog z cudzym czasem.
- Opis na początku `task-cycle/gate_times.py` mówi o „ostatnich 100 liniach”, a skrypt trzyma ostatnie 100 różnych miejsc; ten opis jest źródłem wartości oczekiwanych przez testy (WAY-394), więc ma mówić to, co robi kod.

### To do

1. Fixture testów usuwania katalogów roboczych przestaje zostawiać pracujący w tle proces gita w swoim repozytorium zdalnym: po powrocie każdego `push` do `origin.git` żaden proces automatycznego porządkowania gita (`git maintenance`, `git gc`) nie pracuje już w `origin.git`, tak że test `ApplyTest.test_a_dry_run_removes_nothing_and_apply_removes_only_what_is_marked` porównuje stan przed suchym przebiegiem i po nim z asercją bez zmian.
   - Miejsce: klasa `Fixture` w `task-cycle/test_remove_merged_worktrees.py`, konstruktor, który zakłada repozytorium wierszem `git(self.root, "init", "--bare", "-b", target, str(self.origin))` (około linii 117).
   - Fakt, sprawdzony 2026-11-21 na git 2.55.0.windows.3 śledzeniem `GIT_TRACE`: przy `push` do repozytorium lokalnego git uruchamia `git-receive-pack` po `unset GIT_CONFIG_COUNT`, więc `gc.auto` i `maintenance.auto` podane zmiennymi środowiska w słowniku `ENVIRONMENT` do `origin.git` nie docierają; `receive-pack` uruchamia potem w `origin.git` `git maintenance run --auto --quiet --detach`, czyli w tle, po powrocie `push`.
   - Fakt z tego samego sprawdzenia: z `maintenance.auto` ustawionym na `false` w konfiguracji samego `origin.git` (`git -C origin.git config maintenance.auto false`) `receive-pack` tego procesu nie uruchamia.
   - Poprawić dwa komentarze, które dziś twierdzą, że zmienne środowiska wyłączają porządkowanie także w `origin.git`: przy `ENVIRONMENT` ten, który zaczyna się „Git's automatic maintenance and automatic collection of garbage stay off in every git process of the tests, the bare origin.git included”, i w samym teście ten, który zaczyna się „The snapshot must not see git's maintenance.lock come or go: ENVIRONMENT turns git's automatic maintenance off”.
2. Nowe testy w klasie `NestedRunTest` w `task-cycle/test_gate_times.py` sprawiają, że każda z czterech zmian kodu `task-cycle/gate_times.py` niżej daje co najmniej jeden czerwony test. Zmiany są zapisane jako zamiana wiersza `opened = any(self.count - mark == directories - 1 for mark in self.marks)` w metodzie `Times.summarise` albo warunku w metodzie `Times.line`; wynik reguły i każdej zmiany podany przy przypadku to wynik `Times.result()` z sondy z 2026-11-21 i z tabeli recenzji, dowód, że przypadek odróżnia zmianę — wartość oczekiwaną test bierze z opisu na początku skryptu, wyliczoną ręcznie (WAY-394).
   - (i) `opened = bool(self.marks)`. Przypadek „X z obcym znacznikiem gdzie indziej”: traceback wcześniejszego katalogu zawiera `assert x == y`, a zagnieżdżony przebieg zaczyna się na początku linii. Reguła: `[['other','0.002'],['gate','0.500']]`; zmiana (i): `[['other','0.002'],['gate',None],['x','0.500']]`.
   - (ii) `opened = bool(self.marks) and self.count - self.marks[-1] == directories - 1`, czyli tylko ostatni znacznik. Przypadek „N1 + A”: dwa katalogi drukują zagnieżdżone przebiegi, a środkowy katalog drugiego przebiegu drukuje `assert x == y`. Reguła: `[['other','0.002'],['gate1','0.500'],['gate2','0.600']]`; zmiana (ii): `[['other','0.002'],['gate1','0.001'],['y1','0.600']]`.
   - (iii) `opened = bool(self.marks) and self.count - self.marks[0] == directories - 1`, czyli tylko pierwszy znacznik. Przypadek z sondy: jak w teście `test_two_directories_that_each_print_a_nested_run_each_keep_their_own_time`, tylko `gate1` po swoim zagnieżdżonym przebiegu drukuje drugi padający test, którego traceback zawiera wiersz `    assert a == b`. Reguła: `[['other','0.002'],['gate1','0.500'],['gate2','0.600']]`; zmiana (iii): `[['other','0.002'],['gate1','0.001'],['y1','0.600']]`.
   - (v) warunek `if BLOCK in text and (not self.marks or self.marks[-1] != self.count):` w `Times.line` zamieniony na `if BLOCK in text:`, czyli bez usuwania powtórzeń znaczników. Przypadek z sondy: jak w tym samym teście, tylko katalog `y2` zagnieżdżonego przebiegu `gate2` drukuje ponad 100 wierszy z `== ` po tekście (np. padający test z długim porównaniem). Reguła: `[['other','0.002'],['gate1','0.500'],['gate2','0.600']]`; zmiana (v): `[['other','0.002'],['gate1','0.001'],['y1','0.600']]`.
   - Każdy nowy test nazywa w komentarzu przy wartości oczekiwanej zdanie opisu na początku `task-cycle/gate_times.py`, z którego ją wyliczono, bo nazwa testu źródła nie pokazuje (`guidelines/testing.md`, sekcja „Where the expected value comes from”).
   - Dotychczasowe testy `NestedRunTest` zostają bez zmian.
3. Z metody `Times.summarise` w `task-cycle/gate_times.py` znika wiersz `self.marks.clear()`, który nie zmienia żadnego wyniku (odpowiedź pod *Questions to settle*), a komentarz przy `self.marks` w `Times.__init__`, który zaczyna się „The number of piece lines when each of the last lines that holds `== ` after text was read in this segment”, przestaje mówić o bieżącym odcinku.
4. W opisie na początku `task-cycle/gate_times.py` zdanie o pamięci, które kończy się „and, in the lines since the last summary line, the places of the last 100 lines that hold `== ` after text”, mówi to, co kod robi po punkcie 3: skrypt trzyma, w całym wyjściu, ostatnie 100 różnych miejsc wierszy z `== ` po tekście, każde miejsce raz (`self.marks: deque[int] = deque(maxlen=SUMMARIES_KEPT)` i warunek przed `self.marks.append(self.count)` w `Times.line`). Granica pamięci się nie zmienia.

### Acceptance criteria

- Każda ze zmian (i), (ii), (iii) i (v), wpisana raz w kod `task-cycle/gate_times.py`, daje czerwony co najmniej jeden test `NestedRunTest`, a obecny kod przechodzi wszystkie; zapis cyklu pokazuje te przebiegi (sprawdzenie jednorazowe, bez narzędzia mutacji — WAY-402).
- Śledzenie `GIT_TRACE` przy `push` do `origin.git` z fixture'a nie pokazuje uruchomienia `git maintenance` ani `git gc` w `origin.git` — sprawdzone raz w cyklu i pokazane w jego zapisie.

### Questions to settle

- Zmiana (iv) — znaczniki niewyczyszczone przy linii podsumowania (wiersz `self.marks.clear()` w `Times.summarise` usunięty) — daje na każdym wejściu ten sam wynik co obecna reguła, więc żaden test nie może jej złapać, choć źródło zadania każe, by była czerwona. Co z nią?
  - Answer: usunąć `self.marks.clear()` z kodu i dopasować zdanie opisu o pamięci; wiersz, który nie zmienia żadnego wyniku, zostawiony w skrypcie czytającym wyjście bramki, jest zagadką dla następnego czytelnika, nie zabezpieczeniem. Wyjątek, gdyby czyszczenie ograniczało pamięć albo czas, nie zachodzi: `self.marks` ma `maxlen=SUMMARIES_KEPT` (100) z czyszczeniem i bez, więc pamięć i liczba znaczników sprawdzanych przy każdej linii podsumowania mają tę samą granicę (`task-cycle/gate_times.py`, `Times.__init__` i `Times.summarise`, rewizja `80006b25`).
  - Not chosen:
    - zostawić `self.marks.clear()` bez testu, z dowodem w zadaniu, że zmiana (iv) niczego nie psuje — koszt zero, ale wiersz bez wpływu na wynik zostaje w kodzie jako zagadka dla następnego czytelnika
  - Source: doradca dnia w imieniu Mariusza, 2026-11-21: „zmiana (iv) — b, usuń self.marks.clear() i dopasuj zdanie opisu o pamięci (to zdanie i tak poprawiacie w tym zadaniu). Linia, która nie zmienia żadnego wyniku, zostawiona w granicy zaufania to zagadka dla następnego czytelnika, a nie zabezpieczenie. Wyjątek: jeśli czyszczenie ma inny cel niż wynik (np. ogranicza pamięć albo czas przy długim wyjściu) — wtedy a, z tym celem i dowodem zapisanym w zadaniu.”

## Context

- Dlaczego wiersz `self.marks.clear()` nie zmienia żadnego wyniku (kod `task-cycle/gate_times.py`, metody `Times.line`, `Times.summarise` i `Times.nested`, rewizja `80006b25`): znacznik sprzed poprzedniej linii podsumowania leży co najmniej o tyle wierszy `== ` przed bieżącą linią podsumowania, ile wierszy ma bieżący odcinek, więc pasuje do niej tylko wtedy, gdy odcinek ma najwyżej `<m> - 1` wierszy, a wtedy `min(lines, <m> - 1, surplus)` i `min(lines, <m>, surplus)` dają to samo; sonda 2026-11-21 na 200 000 losowych wyjściach nie znalazła żadnego, na którym (iv) różni się od reguły (dla (i), (ii), (iii) znalazła odpowiednio 9012, 213 i 841).
- Źródło zadania: odpowiedź doradcy dnia w imieniu Mariusza na PR #155 (https://github.com/mariusznazar/the-way/pull/155), 2026-11-21: punkty 1 i 2 opisu PR-a idą do jednego zbiorczego zadania, oba z rekomendacją „zrobić zadanie”.
- Przebieg CI, który padł na teście z punktu 1: https://github.com/mariusznazar/the-way/actions/runs/44931971400 (pierwsze podejście, zadanie `tests`, Linux).
- Test z punktu 1 wszedł z PR-em #125 (commit `9fe7f66d`); słownik `ENVIRONMENT` z `gc.auto` i `maintenance.auto` dodał PR #149 (commit `0ccdc807`) po padnięciu pierwszego przebiegu CI PR-a #144 na tym samym pliku blokady — ta poprawka nie objęła `origin.git`, bo `receive-pack` nie dostaje tych zmiennych.
- Test z punktu 1 cytuje niezmiennik `repository-changer-acts-only-when-told`, więc jest testem niezmiennika w rozumieniu WAY-03.
- Dowody recenzji PR-a #155 leżą w historii gita the way i czyta się je przez `git show 399b46c7:docs/task-cycles/small-fixes-from-ai-review-and-audit/reports/<plik>`: `review-correction-1-report.md` (uwagi m1, m2, m3), `review-correction-1-cases.txt` i `review-correction-1-cases.py` (tabela przypadków i skrypt, który ją zbudował, z pomocnikami `passing`, `failing_dir`, `failing_with`), `review-correction-1-mutants.txt` i `review-correction-1-mutate.py` (zmiany kodu i ich wyniki na `NestedRunTest`).
- Przypadki dla zmian (iii) i (v) zbudowała sonda w tej refinacji na tych samych pomocnikach co `test_gate_times.py`; jej plik był tymczasowy i nie jest potrzebny, bo kształt każdego przypadku stoi w punkcie 2 *To do*.
- Inne testy z gołym repozytorium zdalnym (`project-level/test_plan_state.py`, `project-level/test_plan_state_invariant.py`, `project-level/test_plan_state_subprocesses_invariant.py`, `installation/test_install.py`) nie porównują stanu katalogu, w którym ono leży, więc blokada porządkowania ich nie dotyczy.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-03 — Who may change an invariant test, and when? „Any change may alter an invariant test, in any step of its task, implementation included. A change that alters an invariant test, or a test that holds a sentence of a decision by a line `decision:`, names that test in its request, so that the agent reviewing the change and the human merging it see it.”
- WAY-394 — Where does a test of the-way take its expected value from? „A test of the-way takes the value it expects from the entries of the-way's foundation, from its glossary, from the templates and skills that the script under test carries out, or from the description at the head of the script, which gives its exit codes and the form of its result, and from no other document (WAY-232).”
- WAY-402 — Does the-way adopt a mutation tool? „The-way adopts no mutation tool and departs from the rule of mutation testing of the template of the testing discipline, so `### Mutation testing` of its testing guidelines reads `none — WAY-402` and the author of a change checks its tests in every part by mutating the code in their head (WAY-253).”

## Settlements to record

Candidates: 3 shown, 2 accepted — 2026-11-21

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Test gita, który wyłącza automatyczne porządkowanie gita, ustawia to w konfiguracji każdego repozytorium, które buduje, także gołego repozytorium zdalnego, a nie tylko zmiennymi środowiska, bo git nie przekazuje ich stronie przyjmującej `push` do repozytorium lokalnego. | guidelines: testing | *To do* 1 (fakt sprawdzony śledzeniem `GIT_TRACE` 2026-11-21); przyjęte przez doradcę dnia w imieniu Mariusza, 2026-11-21: „wiersz 1 — przyjąć. Jedno zastrzeżenie: jeśli the way ma wspólny pomocnik, którym testy budują repozytoria gita (albo zmiana w tym zadaniu go naturalnie tworzy), ustawienie w konfiguracji idzie do pomocnika, a reguła brzmi krócej: repozytorium testowe, także gołe zdalne, buduj tym pomocnikiem — mechanizm zamiast pamiętania. Bez takiego pomocnika — reguła w obecnym brzmieniu, bez zakładania pomocnika w tym zadaniu.” Takiego pomocnika nie ma: każdy plik testów the way definiuje własną funkcję `git` (rewizja `80006b25`), a zadanie zmienia jeden fixture. | czy przyszły test gita z gołym repozytorium zdalnym może wyłączyć porządkowanie samymi zmiennymi środowiska, jak `ENVIRONMENT` dziś |
| 2 | W `task-cycle/gate_times.py` nie ma wiersza, który nie zmienia żadnego wyniku: `self.marks.clear()` znika, a opis mówi o ostatnich 100 różnych miejscach w całym wyjściu. | data or code: `task-cycle/gate_times.py` | odpowiedź pod *Questions to settle* (zmiana (iv)), wybór człowieka | czy zostawić `self.marks.clear()` bez testu |

## Out of scope

- Przypadek z uwagi m1 recenzji: zagnieżdżony przebieg zaczynający się od początku linii, którego pierwszy katalog drukuje `assert p == q`, nadal daje wymyślony katalog z cudzym czasem; Mariusz przepuścił go przez doradcę 2026-11-21 — bez testu, który przypinałby zły wynik, i bez szukania nowej reguły.
- Zmiana samej reguły czytania zagnieżdżonego wyjścia w `task-cycle/gate_times.py`: otwierałaby przypadek m1, który przepuszczono.
- Rozbicie na dwa zadania: odpowiedź doradcy każe jedno zbiorcze.

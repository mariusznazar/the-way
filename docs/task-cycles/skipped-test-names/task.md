---
title: "the way: runner testów nazywa pominięte testy"
status: draft
created: 2026-10-31T18:50
updated: 2026-11-01
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# Runner testów nazywa pominięte testy

Status: ready for cycle
Project relation: independent

## Description

### Need

- Proces wymaga, żeby PR nazywał każde sprawdzenie, które się nie wykonało (`task-cycle/skill/SKILL.md:395`, `task-cycle/record_template.md:126`).
- Runner testów `gate/run_tests.py` podaje tylko liczbę, na przykład `OK (skipped=5)`, bo uruchamia `unittest` z domyślną szczegółowością (`gate/run_tests.py:47`).
- Agent musi więc zdobywać nazwy sam albo zostawia samą liczbę: cykl `plomyk` w loop2 zapisał „The two tests skipped in the `tests/invariants` run: not identified.” (`docs/task-cycles/plomyk/cycle.md:136` na `31ac651`), a cykl PR-a #56 w the way puścił na to osobny przebieg (`docs/task-cycles/plan-partial-foundation/cycle.md:87` na `94adb60`).
- Traci na tym Mariusz, który przy PR-ze czyta, że pominięto dwa testy, i nie wie, czy chroniły coś ważnego, oraz agenci, którzy robią dodatkowy przebieg.
- Bez zmiany pominięte testy zostają anonimową liczbą, a nowy pominięty test trudno zauważyć wśród starych; nic się przez to nie wysypuje.

### To do

1. Raport `gate/run_tests.py` wymienia każdy pominięty test z nazwą i powodem, przed końcowymi liniami `unittest`, zarówno dla wskazanego katalogu, jak i w pełnym przebiegu.
2. W docstringu `gate/run_tests.py`, po zdaniu o raporcie `unittest` (`:10-12`), staje zdanie: „A skipped test is named there, with its reason, before the closing lines.”
3. `gate/test_run_tests.py` ma test pełnego przebiegu bez wskazanego katalogu, w którym katalog z pominiętym testem dalej przechodzi, a w raporcie stoją nazwa i powód tego testu.

### Questions to settle

- Czy to zadanie czeka na rozstrzygnięcie, czy the way ma własne wytyczne kodowania i testów, skoro w the way nie ma katalogu `guidelines/`, żadna decyzja od nich nie odchodzi, a WAY-215 trzyma w doprecyzowaniu zadanie piszące kod w produkcie bez wytycznych?
  - Answer: Nie czeka; to zadanie idzie do cyklu drogą z `agent-instructions/README.md`, a rozjazd reguły z praktyką zostaje w zadaniu [[wlasne_wytyczne_the_way]].
  - Not chosen:
    - Czekać, aż rozstrzygnie się zadanie o własnych wytycznych — drobna zmiana stoi za zadaniem z estymatą 5 bez wybranej drogi, a pominięte testy zostają do tego czasu anonimową liczbą.
    - Najpierw doprecyzować zadanie o własnych wytycznych w osobnej sesji — osobna sesja z Mariuszem przed drobną zmianą, która do jej końca czeka.
  - Source: Mariusz, 2026-11-01: „A”, na pytanie, czy zmiana w runnerze ma poczekać na to zadanie.

## Context

- Sprawdzony sposób, który wybiera lub zmienia cykl:

  ```python
  class NamingSkipsResult(unittest.TextTestResult):
      """A test result that names each skipped test and its reason before the closing lines."""

      def printErrors(self):
          super().printErrors()
          for test, reason in self.skipped:
              self.stream.writeln("skipped: %s: %s" % (test.id(), reason))
  ```

  ```python
  result = unittest.TextTestRunner(stream=stream, resultclass=NamingSkipsResult).run(suite)
  ```

- Nazwy muszą paść przed końcowymi liniami, bo `run_all` zalicza katalog tylko wtedy, gdy ostatnia niepusta linia zaczyna się od `OK` (`gate/run_tests.py:96-100`); dopisanie ich po `.run(suite)` zamieniłoby zielony katalog w „exit code 0 without unittest's OK”.
- Próba z 2026-11-01 na Pythonie 3.14.3 objęła `@skip`, `skipTest` w teście i w `subTest`, pominięcie całej klasy oraz `SkipTest` w `setUpClass` i `setUpModule`: każde pominięcie dostało linię, ostatnia linia to `OK (skipped=8)`, kod wyjścia 0.
- Dla `setUpClass` i `setUpModule` linia podaje `setUpClass (moduł.Klasa)` albo `setUpModule (moduł)`, a nie nazwy poszczególnych testów, bo tyle wie `unittest`.
- Powód złożony z kilku linii wypisze się w kilku liniach, a linia zaczynająca się od `Ran 99 tests in` podbiłaby sumę w ostatniej linii pełnego przebiegu; to samo potrafi już dziś `print` z testu, bo oba strumienie idą do tego samego odczytu (`gate/run_tests.py:87-95`).
- W the way na tym komputerze pomija się dziś 5 testów, wszystkie w `instruction-files` (przebieg z 2026-11-01).
- Pełna bramka loop2 idzie przez `.the-way/gate/run_tests.py` (`scripts/test.py:45`), więc nazwy dojdą tam po przesunięciu wersji the way; uruchamianie jednego pliku ma w loop2 własny runner (`scripts/test.py:31`) i się nie zmienia.
- Obietnica dla produktów `test-runner-command` w `foundations/part_map.md` obejmuje nazwę polecenia, argument i kody wyjścia, nie treść raportu, więc zmiana jej nie dotyka.
- Zmianę `gate/run_tests.py` sprawdza się dodatkowo poleceniem `python -B -m unittest discover -s gate -p "test_*.py"`, które nie opiera się na sprawdzanym runnerze (`agent-instructions/README.md:55-57`).
- Numery linii w the way ze stanu `foundations` @ `2f51e6c`; pliki `gate/` nie zmieniły się od `2dbf1e7`, na którym oparto notatkę.
- Źródło: sprawa AIR-556 z przeglądu warstwy AI, 2026-10-31.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-16: „One command runs all of a product's tests, the tests of its invariants among them — the same command for an agent, for a human and for whatever runs it when a change is merged — and no list of checks written by hand stands beside it.”
- WAY-63: „The command running the product's tests exits non-zero when a test fails.”
- WAY-215: „Unless a departure under WAY-217 applies, a task changing a user interface with no styleguide, writing code in a product with no general coding guidelines or writing or changing a test in a product with no testing guidelines, whether or not the product already has screens, code or tests, stays in refinement as `waiting for human` with a *Questions to settle* question awaiting the merge of a separate guidelines task”. Czytana dosłownie, reguła zatrzymywałaby to zadanie; Mariusz rozstrzygnął pod *Questions to settle*, że nie czeka.
- WAY-217: „The shared reading of product guidelines treats no absent discipline file as missing for the affected part where a current decision of the product's log departs from those guidelines for that part, and applies that departure only within the scope the decision gives it.” Dla the way takiej decyzji nie ma, a to zadanie jej nie zapisuje.

## Settlements to record

Candidates: 4 shown, 0 accepted — 2026-11-01

none

## Out of scope

- Ustawienie `verbosity=2`, które dołożyłoby do każdego logu the way po linii na każdy z 615 testów, choć potrzebne są tylko nazwy pominiętych.

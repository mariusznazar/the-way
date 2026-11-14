---
title: "the way: instalator odmawia zapisu przez junction Windows w folderze ustawień agentów produktu"
status: draft
created: 2026-11-14T00:28
updated: 2026-11-14
tags: [zadanie]
related: "the project's folder note in the author's notes"
---

## Po co to

- **Jak jest dziś:** Polecenie, które instaluje proces the way w cudzym produkcie (instalator), przed zapisem sprawdza, czy folder, do którego pisze, nie jest dowiązaniem symbolicznym, i takie dowiązanie odrzuca. Nie rozpoznaje jednak junction Windows, czyli skrótu do folderu, który system plików pokazuje jak zwykły katalog. Gdy folder `.claude` produktu (tam leżą ustawienia agentów) jest takim junction, instalator idzie za nim i zapisuje pliki procesu (definicje agentów i wejścia skilli) tam, dokąd junction prowadzi, czyli poza katalogiem produktu. Recenzent sprawdził to na próbnym produkcie: instalator zakończył się kodem 0, a pliki wylądowały w katalogu poza produktem.
- **Kto to odczuwa:** Ktoś, kto instaluje proces w produkcie z takim junction. Git nie przenosi junction przy klonowaniu, więc może go założyć tylko właściciel produktu u siebie, na przykład żeby dzielić ustawienia agentów między repozytoriami. Skutek to pliki zapisane poza produktem, bez ostrzeżenia.
- **Co jeśli nic:** Nic się dziś nie psuje i nie jest to nowa dziura: to samo sprawdzenie ścieżek działało tak już dla wejść skilli, zanim PR #112 dodał definicje agentów. Zostaje rzadka, cicha możliwość zapisu poza produktem u kogoś, kto sam ustawił junction. Możesz uznać to za zbyt rzadkie i zadanie wyrzucić.

# the way: instalator odmawia zapisu przez junction Windows w folderze ustawień agentów produktu

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Instalator (`installation/install.py`) odrzuca dowiązanie symboliczne w ścieżce, którą zapisuje, ale junction Windows przepuszcza jak zwykły katalog: dla junction Python 3.14 zwraca `is_symlink()` fałsz i `is_dir()` prawdę (sonda z 2026-11-14 na junction założonym w katalogu tymczasowym).
- Gdy folder `.claude` produktu jest junction do katalogu poza produktem, instalator kończy się kodem 0 i zapisuje definicje typów agentów i wejścia skilli poza produktem, bez ostrzeżenia (recenzent PR #112, punkt O1 raportu przeglądu całej zmiany).
- Ten sam brak dotyczy usuwania: gdy folder przestarzałego wejścia skilla, `.claude/skills/the-way-<nazwa>` albo `.agents/skills/the-way-<nazwa>`, jest junction, sprawdzenie `not entry.is_symlink()` w funkcji `stale_entry_points` go przepuszcza i instalator usuwa plik `SKILL.md` leżący poza produktem (z odczytu kodu na f04f046, nie sprawdzone uruchomieniem).
- Odczuwa to ktoś, kto instaluje the way w produkcie, w którym sam założył junction, na przykład żeby dzielić ustawienia agentów między repozytoriami; git nie przenosi junction przy klonowaniu.

### To do

1. Instalator odmawia, gdy którykolwiek katalog na drodze od korzenia produktu do pliku, który zapisuje, jest junction Windows — tak samo jak dziś odmawia przy dowiązaniu symbolicznym: przed zapisaniem czegokolwiek, z komunikatem i kodem wyjścia różnym od 0. Jedna poprawka obejmuje wejścia skilli, definicje typów agentów i pliki fundamentu, bo sprawdzenie rodziców ścieżki jest dla nich wspólne.
2. Instalator rozpoznaje junction także wszędzie poza drogą zapisu, gdzie dziś rozpoznaje dowiązanie symboliczne (pytanie 1): przy usuwaniu przestarzałych wejść skilli i definicji typów agentów — nie usuwa niczego, do czego prowadzi junction — i przy folderze `.the-way`.
3. Testy zakładają junction w próbnym produkcie i sprawdzają, że instalator nie zapisuje ani nie usuwa niczego ani w produkcie, ani w katalogu, do którego junction prowadzi: jeden z folderem `.claude` wskazującym katalog poza produktem, drugi z folderem przestarzałego wejścia skilla wskazującym katalog poza produktem, w którym leży plik `SKILL.md` instalatora; tam, gdzie junction nie da się założyć, test się pomija.
4. Testy z punktu 3 cytują niezmiennik z wiersza 1 sekcji *Settlements to record* (pytanie 2).

### Acceptance criteria

- Na Windows testy z punktu 3 nie są pomijane.

### Questions to settle

- 1. Czy instalator ma rozpoznawać junction tylko na drodze do pliku, który zapisuje, czy wszędzie, gdzie dziś rozpoznaje dowiązanie symboliczne, także przy usuwaniu przestarzałych wejść skilli i definicji typów agentów oraz przy folderze `.the-way`?
  - Answer: wszędzie, gdzie dziś rozpoznaje dowiązanie symboliczne; zamyka to także usuwanie cudzego pliku poza produktem, gorsze od zapisu, bo usuniętego pliku nie da się odzyskać.
  - Not chosen:
    - tylko na drodze zapisu, jak w notatce zadania — mniejsza zmiana, ale zostaje usuwanie pliku `SKILL.md` poza produktem, gdy folder porzuconego wejścia skilla jest junction.
  - Source: Mariusz przez doradcę dnia, 2026-11-14, „1 a”.
- 2. Czy zasada „instalator nie zapisuje ani nie usuwa niczego przez dowiązanie symboliczne ani junction” staje się niezmiennikiem fundamentu the way z testem, który go cytuje?
  - Answer: tak; granica zaufania instalatora nie ma dziś żadnego niezmiennika odmowy, a bez wpisu test można przy przepisaniu instalatora osłabić albo usunąć bez sygnału z fundamentu.
  - Not chosen:
    - sam test, bez wpisu — o jeden wpis taniej i nie łamie żadnej reguły, bo WAY-328 zwalnia the way z wymogu WAY-235, ale nic w fundamencie nie mówi, że odmowa jest wymagana.
  - Source: Mariusz przez doradcę dnia, 2026-11-14, „2 a”.

## Context

- Źródło: opis PR #112 (https://github.com/mariusznazar/the-way/pull/112), sekcja „Findings outside the task's scope”, pozycja 1; raport przeglądu w historii gita: `git show 72dc779bcc0776e7ff2c0ac97e1329281c8f9b3f:docs/task-cycles/cycle-subagent-types/reports/whole-review-report.md`, sekcja „Outside the task”, punkt O1.
- Repozytorium deklaruje Python 3.14 (`.python-version`); `os.path.isjunction` i `Path.is_junction` są w nim dostępne i dla junction zwracają prawdę (ta sama sonda z 2026-11-14).
- W tej sesji `New-Item -ItemType Junction` w PowerShellu założył junction w katalogu tymczasowym.
- Sprawdzenia `is_symlink()` w instalatorze na f04f046: funkcja `check_parents` (rodzice ścieżki zapisu), `stale_agent_definitions` (folder `.claude` i `.claude/agents`), `stale_entry_points` (folder `skills` i folder każdego wejścia), sprawdzenie folderu `.the-way` w funkcji `plan` (akapit, który zaczyna się od „if submodule_path.is_symlink()”) oraz `read_text_file`, `owned_entry_point` i `owned_agent_definition`, które sprawdzają pliki, a junction bywa tylko folderem.
- Sprawdzenie rodziców przyszło z commitem 3b2a0cb (2026-10-01, bez PR-a), które odrzucało dowiązanie symboliczne, a junction nie przewidziało; szablon zadania liczy rzecz nieprzewidzianą przez wcześniejszą zmianę jako `none` w linii `Defect introduced by:`.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-48 — How is a trust boundary recorded?** Bez zmiany; `installation/install.py` jest granicą zaufania części `installation` w mapie części, więc zmiana jest sprawdzana pod kątem spreparowanego wejścia.
  > A change that touches the files of a boundary is checked for crafted input, and its review is aimed at that risk.
- **WAY-13 — What sets the weight of a task's process?** Bez zmiany; zmiana dotyka plików granicy zaufania, więc dostaje przegląd wymierzony w to ryzyko.
  > At its start a task's cycle answers two questions — does the change touch the files of a trust boundary (WAY-48), and does it hold an operation that cannot be undone — and a change for which either answer is yes gets a review aimed at that risk;
- **WAY-38 — In what are the scripts of the-way written?** Bez zmiany; rozpoznanie junction korzysta tylko z biblioteki standardowej Pythona 3.14.
  > Every script of the-way runs on the version of Python the repository declares, with its standard library alone, and installs nothing.
- **WAY-328 — Does the-way hold its own code and tests to the general coding guidelines and the testing guidelines of a product?** Bez zmiany; zadanie zmienia kod i test części `installation` i nie czeka na wytyczne.
  > The-way departs, for its own code and its own tests, from the general coding guidelines and from the testing guidelines of a product, under WAY-217: in each part named in *Scope*, neither is missing, so a task of the-way that writes code, or writes or changes a test, in such a part waits for neither.
- **WAY-235 — How do a product's tests keep its trust boundaries?** Bez zmiany; wiąże produkty, a the way jest z niej zwolniony przez WAY-328, ale niezmiennik z wiersza 1 sekcji *Settlements to record* ma jej kształt: odmowa granicy zaufania sprawdzana stałym testem.
  > The template of the testing discipline requires, and the skill `maintain-testing-guidelines` proposes, for each trust boundary of the product's part map at least one invariant that the boundary refuses crafted input or unauthorised access, checked by a permanent test that checks the refusal directly, takes the expected refusal from the product's decisions on permissions and is seen failing once;

## Settlements to record

Candidates: 2 shown, 1 accepted — 2026-11-14

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Instalator nie zapisuje ani nie usuwa niczego przez dowiązanie symboliczne ani junction Windows w ścieżce, którą dotyka, i odmawia, zanim cokolwiek zapisze. | invariant | pytania 1 i 2 | czy pisać niezmiennik i czy obejmuje on także usuwanie, czy tylko zapis |

## Out of scope

none

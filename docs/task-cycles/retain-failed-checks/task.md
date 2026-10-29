---
title: "the way: test spoza zadania, który w cyklu pada, a przy powtórce przechodzi, trafia do PR-a do mojej decyzji zamiast znikać jako „niestabilny”"
status: draft
created: 2026-10-28T15:00
updated: 2026-10-29
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# Test spoza zadania, który w cyklu pada, a przy powtórce przechodzi, trafia do PR-a do decyzji człowieka

Status: ready for cycle
Project relation: independent

## Description

### Need

- Gdy w cyklu zadania pada sprawdzenie spoza części, których zadanie dotyka, a uruchomione drugi raz przechodzi, cykl nie ma dla niego drogi do PR-a poza „unchecked” — w cyklu `odkrywanie` w loop2 zapis wpisał, że nic nie zawiodło, bo zmiana nie dotykała tych plików (uwaga procesowa (2) w zapisie cyklu: „the gate's container tests were treated as flaky through the cycle although they exposed a product defect — the record of a failing check outside the task's parts has no route but "unchecked"”).
- Reguła o testach niestabilnych już istnieje w szablonie wytycznych testów (`product-guidelines/testing/template.md:220–223`, punkt *Flaky tests*, WAY-243): „Running a flaky test again serves only the diagnosis of what makes it flaky, never making a run of the gate pass” — ale cykl zadania jej nie przywołuje.
- Odbiorcą jest człowiek, który scala PR: o błędzie produktu, który taki test wyłapuje, dowiaduje się dziś tylko wtedy, gdy sam zapyta — w `odkrywanie` za trzema testami kontenera stał prawdziwy błąd bazy kont graczy, naprawiony osobnym PR-em (loop2 #34).

### To do

1. `task-cycle/record_template.md`, sekcja *Verification*, po zdaniu „Record the checks already failing on the base apart from the runs after the change.” (`:116` na `d7a205c`): sprawdzenie, które w uruchomieniu cyklu pada, a uruchomione ponownie przechodzi, idzie według reguły produktu o testach niestabilnych (wytyczne testów, *Flaky tests*), której źródło tekst podaje jako WAY-243, tak by obowiązywała także w produkcie bez tego punktu (pytanie 4) — każde padające uruchomienie zostaje w zapisie z wynikiem, a sprawdzenie spoza części zadania trafia do PR-a obok uwag spoza zakresu zadania. Punkt wyjścia brzmienia, z notatki źródłowej (sprzed pytań 1–5; brzmienie wybiera cykl): „A check that fails in a run of the cycle and passes when run again follows the product's rule on flaky tests (the testing guidelines, *Flaky tests*): each failing run stays in the record with its result, and a check outside the task's parts goes to the request beside the findings outside the task's scope.”
2. `task-cycle/skill/SKILL.md`, krok 13, pozycja z uwagami, które recenzenci oznaczyli jako spoza zakresu zadania (`:377–379` na `d7a205c`: „the findings their reviewers marked outside the task's scope in another, for the human to choose which become new tasks and to create them (WAY-161)”): ta sama pozycja wymienia sprawdzenia spoza części zadania, które w uruchomieniu padły, a ponownie przeszły — proponowany dopisek z notatki: „…and the checks outside the task's parts that failed in a run and passed again”; tę samą pozycję dostaje pole „Review findings listed” sekcji *Request handoff* `task-cycle/record_template.md` (`:168–170` na `d7a205c`), według którego krok 13 składa PR.
3. Każde sprawdzenie, które w uruchomieniu cyklu padło, a ponownie przeszło — z części zadania i spoza niej — PR wymienia w *Checks* jako padające, z wynikiem powtórki i z liczbą uruchomień cyklu, w których padło, wobec liczby tych, w których przeszło — np. „padło w 6 z 7 uruchomień, za każdym razem przechodziło uruchomione osobno”; tę samą liczbę podaje przy nim pozycja z uwagami spoza zakresu (To do 2): w kroku 13 `task-cycle/skill/SKILL.md` (*Checks*, `:373` na `d7a205c`) i w polu „Checks” sekcji *Request handoff* `task-cycle/record_template.md` (`:163` na `d7a205c`). Do pozycji z uwagami spoza zakresu zadania (To do 2) trafia ono dodatkowo tylko wtedy, gdy jego plik leży poza częściami, które orkiestrator wyznaczył zadaniu przy czytaniu fundamentu (krok 1 „Reading the foundation” w `elements/common/way_of_working.md`, WAY-150).
4. `task-cycle/change/SKILL.md`, raport autora albo wykonawcy (`:121–122` na `d7a205c`: „each check you ran as its command and exit code, the failing run of each test written first and of each invariant's test included”): sprawdzenie, które padło, a ponownie przeszło, raport podaje z obydwoma uruchomieniami.

### Questions to settle

- 1. Co ze sprawdzeniem w części, której zadanie dotyka, gdy w uruchomieniu cyklu pada, a ponownie przechodzi?
  - Answer: zostaje w zapisie cyklu jak każde (To do 1) i PR wymienia je w *Checks* jako padające, z wynikiem powtórki (To do 3); do pozycji z uwagami spoza zakresu, czyli kandydatów na nowe zadania, trafia tylko sprawdzenie spoza części zadania (To do 2).
  - Source: Mariusz, 2026-10-29: „C” — wybór spośród: A — tylko spoza części zadania, jak w notatce źródłowej (słaby punkt: w części zadania taki test dalej nie dociera do PR-a, a może za nim stać błąd samej zmiany); C — A i sprawdzenie z części zadania w *Checks* jako padające, z wynikiem powtórki (słaby punkt: więcej pozycji w PR-ze; jedna fraza w kroku 13 i w *Request handoff*). Pytanie 3 rozszerza to o sprawdzenia spoza części zadania w *Checks*.
- 2. Czy zadanie czeka na wytyczne samego the way, skoro the way nie ma katalogu `guidelines/`?
  - Answer: nie — zadanie idzie drogą z `agent-instructions/README.md`, jak zadania 1–3 serii skilli; wybór wytycznych jest pusty, a zadanie zmienia tylko pliki Markdown.
  - Source: Mariusz, 2026-10-29: „ok, tak jak rekomendujesz” — na rekomendację przeniesienia odpowiedzi z zadania 3 serii (`git -C C:/Storage/repos/the-way show 72b66de:docs/task-cycles/foundation-skills-shape/task.md`, *Questions to settle*, pytanie 5: Mariusz, 2026-10-28, „tak”), przeciw czekaniu na wytyczne samego the way (zadanie stoi bez zysku przy trzech dopiskach w Markdownie).
- 3. Kto rozstrzyga, czy padające i przechodzące sprawdzenie jest spoza części zadania, i co z tego wynika w PR-ze?
  - Answer: orkiestrator, według mapy części — sprawdzenie należy do części zadania, gdy jego plik leży w części, którą orkiestrator wyznaczył zadaniu przy czytaniu fundamentu (WAY-150); każde takie sprawdzenie stoi w *Checks*, a spoza części zadania dodatkowo w pozycji z uwagami spoza zakresu, więc przypisanie decyduje tylko o kandydaturze na nowe zadanie (To do 3).
  - Source: Mariusz, 2026-10-29: „ok, tak jak rekomendujesz” — na rekomendację B, przeciw A: orkiestrator sortuje według mapy części, a sprawdzenie spoza części stoi tylko w pozycji z uwagami (słaby punkt: złe przypisanie zdejmuje sprawdzenie z *Checks*; WAY-161: „The orchestrator moves no finding from one of these kinds to another”). Słaby punkt B: sprawdzenie spoza części zadania stoi w PR-ze dwa razy. B odpowiada WAY-160: „the request […] names each check that failed or did not run”.
- 4. Czy reguła cyklu działa w produkcie, którego wytyczne testów nie mają punktu *Flaky tests* (brak wytycznych albo wytyczne sprzed 2026-10-25)?
  - Answer: tak — w każdym produkcie; tekst cyklu podaje WAY-243 jako źródło reguły obok punktu *Flaky tests* wytycznych produktu.
  - Source: Mariusz, 2026-10-29: „odpowiedź na pytanie 4 brzmi A” — wybór spośród: A — w każdym produkcie, z WAY-243 jako źródłem (nic nie kosztuje); B — tylko w produkcie, którego wytyczne mają *Flaky tests* (słaby punkt: w produkcie bez tego punktu luka zostaje, a cykl musi sprawdzać, czy punkt istnieje).
- 5. Czy PR pokazuje, że sprawdzenie padało powtarzalnie, a nie raz?
  - Answer: tak — pozycja w PR-ze podaje, w ilu uruchomieniach cyklu sprawdzenie padło i w ilu przeszło (To do 3); cykl nie bada przyczyny sam, rozróżnienie kaprysu i błędu zostaje przy człowieku.
  - Source: Mariusz, 2026-10-29, na wątpliwość „problemem było to, że agent zauważył jakiś powtarzający się problem, nie pojedynczy test, który się wywalił i potem zadziałał, ale było to powtarzalne” — „ok tak zróbmy”, na propozycję liczby padających uruchomień w PR-ze (koszt: fraza w kroku 13 i w *Request handoff*); bez niej pojedynczy kaprys portu z `serwer-testowy` i błąd bazy z `odkrywanie` wyglądają w PR-ze tak samo. Cykl badający przyczynę sam nie był proponowany: WAY-243 odrzuca „every flaky test fixed before the next change — unrelated work stops for it”.

## Context

- Źródło: sprawa AIR-534 z dziennego przeglądu warstwy AI (2026-10-28), z uwagi procesowej w zapisie cyklu `odkrywanie` w loop2 (PR #33): `git -C C:/Storage/repos/loop2 show ee96d7f:docs/task-cycles/odkrywanie/cycle.md`, wiersze 110 (osobne badanie błędu bazy kont na prośbę człowieka), 151 i 172 (jak zapis opisuje padające testy), 179 (uwaga procesowa).
- W `odkrywanie` trzy testy kontenera (konta graczy, baza SQLite) padały pojedynczo w pięciu kawałkach planu i w sprawdzeniu przed PR-em (exit 137 / „database is locked”), a uruchomione same przechodziły; przyczyną było otwarcie bazy kont, które nie czekało, gdy inny proces ją blokował (`PRAGMA journal_mode = WAL` bez busy timeout).
- Historia loop2 ma 16 zapisów cykli (`docs/task-cycles/*/cycle.md` we wszystkich gałęziach); w trzech z nich sprawdzenie padło i przeszło przy powtórce — `mag-w-lesie` (`0ae1664`, `cycle.md:142`, port 3000), `serwer-testowy` (`4fce4f5`, `cycle.md:149,151`, EADDRINUSE na porcie 3000) i `odkrywanie` — a w `odkrywanie` stał za nim błąd produktu; notatka źródłowa podawała „4 z 18”.
- Reguła *Flaky tests* weszła do szablonu wytycznych 2026-10-25 (`083ab5d`), a `odkrywanie` (2026-10-27) i tak traktował porażki jako kaprys środowiska.
- W loop2 ta sama reguła stoi w `guidelines/testing.md`, „Flaky tests”, z decyzją D-73 i złym przykładem „Późniejszy sukces usuwa z raportu wcześniejszą porażkę”.
- WAY-243 odrzuca „every flaky test fixed before the next change — unrelated work stops for it”, więc zadanie nie każe cyklowi naprawiać takiego testu, tylko pokazać go człowiekowi.
- Spodziewany koszt: przy kapryśnym środowisku (Docker na Windows, mało pamięci) człowiek kilka razy odpowie w PR-ze „to środowisko, nie zadanie” — odróżnić kaprys od błędu potrafi ten, kto patrzy na całość.
- Numery linii w notatce źródłowej były z `foundations` @ `0b8c1bd`; na `d7a205c` zdanie z To do 1 stoi w `:116` bez zmian, a pozycja kroku 13 przesunęła się z ok. `:427–428` na `:377–379`.

## Questions carried to cycle

- Jak orkiestrator ustala w chwili pisania PR-a, czy plik sprawdzenia leży w części zadania (To do 3), skoro WAY-150 nie zapisuje wyboru części: „The selection is neither recorded nor compared with every *Scope* of the log”.

## Human actions

none

## Decisions in play

- **WAY-243** — „The template of the testing discipline requires the rule that running a flaky test again serves only the diagnosis of what makes it flaky, never making a run of the gate pass, and that disabling or deleting such a test is a change of an existing test under WAY-233.” — nie zmienia się; na nią wskazuje dopisek, jej słownika trzyma się jego brzmienie.
- **WAY-68** — „A test that cites an invariant and gives both `pass` and `fail` on one commit is fixed as any test of the product is, and the foundation records no quarantine for it.” — nie zmienia się; test niezmiennika spoza części zadania, który pada i przechodzi, naprawia osobne zadanie, które człowiek zakłada z PR-a.
- **WAY-161** (fragment) — „A finding the reviewer has marked as outside the task's scope […] is not fixed, whatever its grade, nor is a Minor finding, and the request lists those findings in an item of their own and the Minor findings in another, each with the reviewer's words and its place in the code, while the human decides which findings outside the scope become new tasks and creates them. The orchestrator moves no finding from one of these kinds to another.” — jej pozycja w PR-ze dostaje sprawdzenia spoza części zadania.
- **WAY-160** (fragment) — „The task-cycle orchestrator itself runs the product's gate on the tree that goes into the request, and the request gives its command and exit code and names each check that failed or did not run; a check that did not run is unchecked, never passed.”
- **WAY-150** (fragment) — „whoever selects names the parts the work touches from the files it changes through the part map's rules for assigning files […] in the task cycle the orchestrator selects for its own judgments and for each handoff […] The selection is neither recorded nor compared with every *Scope* of the log” — nie zmienia się; według niej orkiestrator wyznacza części zadania, do których To do 3 przypisuje sprawdzenie.
- **WAY-148** (fragment) — „only the orchestrator reads the cycle record” (`foundations/decisions.md:3796` na `d7a205c`) — nie zmienia się; dlatego liczba padających uruchomień idzie do PR-a, a nie zostaje tylko w zapisie.
- **WAY-159** (fragment) — „The author or executor runs the focused checks of its change or slice and reports each as its command and exit code; […] a change or a failure calls for its affected checks to run again.”

## Settlements to record

Candidates: 4 shown, 2 accepted — 2026-10-29

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Sprawdzenie, które w uruchomieniu cyklu pada, a uruchomione ponownie przechodzi, idzie według reguły produktu o testach niestabilnych (WAY-243): zostaje w zapisie cyklu z każdym padającym uruchomieniem i jego wynikiem, a PR wymienia je w *Checks* jako padające, z wynikiem powtórki i z liczbą uruchomień cyklu, w których padło, wobec tych, w których przeszło; to, którego plik leży poza częściami wyznaczonymi zadaniu przy czytaniu fundamentu, PR wymienia dodatkowo obok uwag spoza zakresu zadania, żeby człowiek wybrał, które staną się nowymi zadaniami; koszt odpowiadania w PR-ze „to środowisko, nie zadanie” jest przyjęty. | decision | notatka źródłowa, „Co zmienić”, punkty 1 i 2 oraz akapit o koszcie („Jest celowy — odróżnić kaprys od błędu potrafi ktoś, kto patrzy na całość, a cykl tego nie robi.”); *Questions to settle*, pytania 1, 3, 4 i 5 (Mariusz, 2026-10-29: „C”; „ok, tak jak rekomendujesz”; „odpowiedź na pytanie 4 brzmi A”; „ok tak zróbmy”); przyjęte: Mariusz, 2026-10-29, „teoretycznie przyjmuję oba” i „ok tak zróbmy” | czy kolumna „Failed or unchecked” zapisu ma `none` dla sprawdzenia, które przeszło uruchomione samo — tak zapisał `odkrywanie` (`cycle.md:149` w loop2) — i czy PR je pomija |
| 2 | Raport autora albo wykonawcy podaje sprawdzenie, które padło, a uruchomione ponownie przeszło, z obydwoma uruchomieniami. | decision | *To do* 4 (Mariusz, 2026-10-29: „ok, niech będą obie”, na propozycję frazy w `task-cycle/change/SKILL.md:121–122`); przyjęte: Mariusz, 2026-10-29, „teoretycznie przyjmuję oba” | czy WAY-159 („reports each as its command and exit code”) obejmuje oba uruchomienia, czy wystarczy ostatnie — dziś wykonawca może podać tylko to, które przeszło |

## Out of scope

- Naprawa testów kontenera w loop2 — poszła osobnym PR-em (loop2 #34, scalony).
- Sama reguła o testach niestabilnych w `product-guidelines/testing/template.md` i w wytycznych loop2 — zadanie na nią wskazuje, nie zmienia jej.

---
title: "the way: pliki zapisywane hurtem przez jeden generator stoją w planie jako jedno polecenie i jeden wzorzec, w jednym kawałku, zamiast być cięte po 10"
status: draft
created: 2026-10-29T10:50
updated: 2026-10-29
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# Pliki, które jedno polecenie zapisuje hurtem, stoją w *Change* kawałka jako wzorce liczone po jednym pliku, zamiast być cięte na kawałki po 10

Status: ready for cycle
Project relation: independent

## Description

### Need

- Plan cyklu dzieli pracę między agentów po najwyżej 10 zmienionych plików na kawałek (`task-cycle/slice_size.py:59`, `CHANGE_LIMIT = 10`, `foundations` @ `d115159`).
- Gdy jedno polecenie samo przepisuje kilkadziesiąt plików naraz — punkty wejścia skilli the-way, 21 w `.claude/skills/` i 21 w `.agents/skills/` — planista tnie jego wynik na kawałki, choć nie ma czego dzielić.
- Instrukcja planisty przeczy sama sobie: każe nie dzielić pracy nierozdzielnej (`task-cycle/plan/SKILL.md:117-118`), ale też ciąć każdy kawałek, który skrypt uzna za za duży, aż wszystkie się zmieszczą (`task-cycle/plan/SKILL.md:169-171`), a skoro *Change* wymienia każdy plik osobno (`:119`), 42 pliki generatora zawsze wychodzą za duże.
- W cyklu `task-cycle-skills-shape` 42 jednolinijkowe punkty wejścia zajęły pięć kawałków i cztery dodatkowe zlecenia, a test pilnujący punktów wejścia był celowo czerwony między kawałkami 2 i 6 (the-way @ `eeb5b34`, `docs/task-cycles/task-cycle-skills-shape/cycle.md:56`, `:100` C7, `:165`).
- Odczuwają to agenci cyklu w the-way przy każdej zmianie, która dodaje, usuwa albo przemianowuje skill lub zmienia wspólny tekst punktów wejścia; Mariusz pośrednio: dłuższy cykl, więcej zleceń i czerwony test, w którym prawdziwy błąd łatwo pomylić z zaplanowanym.
- Zdarzyło się to co najmniej trzy razy (18.10, 19.10, 28.10), a seria przebudowy skilli trwa; pieniężnie to mało, bo zlecenia idą na tańszym modelu, gorsze jest to, że czerwony test w środku planu przestaje cokolwiek sygnalizować.

### To do

1. `task-cycle/plan/SKILL.md`, po zdaniu „*Change* names every file the slice changes or creates.” (`:119`): pliki, które jedno deterministyczne polecenie zapisuje w jednym uruchomieniu — jak punkty wejścia skilli, które zapisuje `python -B agent-instructions/skill_entry_points.py --write` — stoją w *Change* jako jeden wzorzec ścieżek na każdy katalog, do którego polecenie pisze (dla punktów wejścia `.claude/skills/the-way-*/SKILL.md` i `.agents/skills/the-way-*/SKILL.md`), a `slice_size.py` liczy każdy wzorzec jako jeden plik; każdy kawałek, który zmienia to, z czego polecenie pisze, uruchamia je na koniec swojej pracy i commituje cały jego wynik, a wzorce stoją w *Change* każdego takiego kawałka (Q1); plik generatora stoi w *Change* tylko wtedy, gdy kawałek go zmienia, a *Goal* kawałka nazywa polecenie i to, że jego wyniku nie edytuje się ręcznie, bo wykonawca dostaje tylko swoją sekcję planu (Q2, wiersz 1 *Settlements to record*).
2. `task-cycle/skill/SKILL.md`, w sprawdzeniu mechanicznym po powrocie wykonawcy kawałka (`:264-266`, „the changed files against the slice's *Change*”): orkiestrator czyta wzorzec ścieżek w *Change* jako każdy plik, który do niego pasuje; skill planisty tego zdania nie powtarza (Q3).
3. `task-cycle/test_slice_size.py` ma przypadek, w którym kawałek z jednym istniejącym plikiem i dwoma wzorcami ścieżek w *Change* daje „3 files, fits”, a opis na początku `task-cycle/slice_size.py` (`:15-16`) mówi, że wzorzec w *Change* liczy się jako jeden plik; kod skryptu się nie zmienia (Q4).

### Questions to settle

- Q1. Gdy kilka kawałków planu zmienia to, z czego polecenie pisze (np. kawałek 2 zmienia opis jednego skilla, kawałek 5 dodaje nowy skill), który kawałek uruchamia polecenie i trzyma jego wynik?
  - Answer: każdy taki kawałek uruchamia polecenie na koniec swojej pracy i commituje cały jego wynik; wzorce stoją w *Change* każdego z nich, więc test punktów wejścia jest zielony po każdym kawałku.
  - Not chosen:
    - tylko ostatni kawałek zmieniający wejście polecenia uruchamia je raz — test czerwony od pierwszego takiego kawałka do ostatniego, czyli zostaje drugi objaw z *Need*
    - zdanie bez rozstrzygnięcia, wybór planisty — planista może pójść drogą „tylko ostatni”, a czerwony test wraca w kolejnym cyklu
  - Source: Mariusz, 2026-10-29, „A” — na pytanie z trzema wariantami (A: każdy kawałek, B: tylko ostatni, C: bez rozstrzygnięcia) i kosztem każdego; koszt A nazwany w pytaniu: kilka sekund na uruchomienie, a kawałki zmieniające te same pliki muszą być powiązane zależnością (`task-cycle/plan/SKILL.md:156-157`).
- Q2. Czy w zdaniu z notatki zmienić dwie rzeczy: „one pattern of its output” na jeden wzorzec na każdy katalog, do którego polecenie pisze, oraz „the command's source” na plik generatora tylko wtedy, gdy kawałek go zmienia?
  - Answer: tak, obie — jeden wzorzec na każdy katalog, do którego polecenie pisze; plik generatora w *Change* tylko wtedy, gdy kawałek go zmienia; samo polecenie (`… --write`) stoi w *Goal* kawałka, bo *Checks* to sprawdzenia, nie praca.
  - Not chosen:
    - brzmienie z notatki — przy przemianowaniu skilla planista dopisuje do *Change* niezmieniony generator wbrew `task-cycle/plan/SKILL.md:119` i orkiestrator za każdym razem zgłasza niezgodność; przy jednym wzorcu planista wymyśla wzorzec za szeroki (`.*/skills/the-way-*/SKILL.md`) albo wpisuje dwa wbrew instrukcji
    - tylko jedna z poprawek — zostaje drugi kłopot
  - Source: Mariusz, 2026-10-29, „A” — na pytanie z trzema wariantami (A: obie poprawki, B: brzmienie z notatki, C: jedna z nich) i kosztem każdego; koszt A nazwany w pytaniu: zdanie dłuższe o pół linii.
- Q3. Czy zdanie o sprawdzeniu mechanicznym orkiestratora stoi w skillu cyklu, przy tym sprawdzeniu (`task-cycle/skill/SKILL.md:264-266`), zamiast w skillu planisty?
  - Answer: tak — w skillu cyklu, przy sprawdzeniu mechanicznym; skill planisty trzyma tylko to, co dotyczy pisania planu.
  - Not chosen:
    - w skillu planisty, jak w notatce — orkiestrator go nie czyta (przegląd planu stoi w `task-cycle/skill/planning.md:6-23`), więc 21–42 punkty wejścia przy każdym takim kawałku szłyby do przeglądu jako pliki spoza *Change*
    - w obu miejscach — ta sama reguła w dwóch miejscach rozjeżdża się przy następnej zmianie
  - Source: Mariusz, 2026-10-29, „A” — na pytanie z trzema wariantami (A: skill cyklu, B: skill planisty, C: oba) i kosztem każdego; koszt A nazwany w pytaniu: drugi zmieniany plik, jedno zdanie albo jego fragment.
- Q4. Czy zadanie dodaje do `task-cycle/test_slice_size.py` przypadek, w którym wzorzec w *Change* liczy się jako jeden plik, a kawałek z generatorem i dwoma wzorcami się mieści?
  - Answer: tak, test i jedno zdanie w opisie skryptu (`task-cycle/slice_size.py:15-16`), że wzorzec w *Change* liczy się jako jeden plik; kod skryptu bez zmian.
  - Not chosen:
    - sam test — opis skryptu dalej nazywa wzorzec „a file the slice creates” i myli następnego czytelnika
    - bez testu — instrukcja wisi na przypadkowym zachowaniu skryptu (`task-cycle/slice_size.py:170-171`), którego nic nie pilnuje, i zmiana skryptu po cichu przywróciłaby cięcie po 10
  - Source: Mariusz, 2026-10-29, „B” — na pytanie z trzema wariantami (A: sam test, B: test i zdanie w opisie, C: bez testu) i kosztem każdego; słaby punkt B nazwany w pytaniu: dotyka pliku, o którym notatka mówi „nie zmieniaj”, choć tylko komentarza.
- Q5. Czy zadanie czeka na wytyczne samego the way, skoro the way nie ma katalogu `guidelines/`?
  - Answer: nie — zadanie idzie drogą z `agent-instructions/README.md`, jak zadania 1–3 serii skilli; wybór wytycznych jest pusty.
  - Source: odpowiedź wspólna z `_zadania/zadanie_skille_the_way_3_fundament.md`, *Questions to settle*, pytanie 5: Mariusz, 2026-10-28, „tak” — na tę samą odpowiedź co w zadaniu 2 (`_zadania/zadanie_skille_the_way_2_refine_task.md`: Mariusz, 2026-10-28, „przyjmuję”), przeciw czekaniu na wytyczne samego the way; przeniesiona też do `_zadania/zadanie_the_way_odrzucone_warianty_decyzji_z_zadania.md`, Q3.

## Context

- Źródło: sprawa AIR-541 z dziennego przeglądu warstwy AI (2026-10-29), z uwagi procesowej (1) zapisu cyklu `task-cycle-skills-shape` (the-way PR #50, the-way @ `eeb5b34`, `docs/task-cycles/task-cycle-skills-shape/cycle.md:165`).
- Wcześniejsza sprawa AIR-524 (przesunięcie wersji the-way pierwszym commitem cyklu, PR #45) obejmuje tylko instalator w produkcie, nie ten przypadek.
- `task-cycle/slice_size.py:170-171` liczy ścieżkę *Change*, która nie wskazuje istniejącego pliku, jako plik tworzony przez kawałek, bez niczego do czytania; wzorzec z gwiazdką jest dla skryptu taką ścieżką.
- Próbny plan z jednym kawałkiem, którego *Change* to `agent-instructions/skill_entry_points.py`, `.claude/skills/the-way-*/SKILL.md` i `.agents/skills/the-way-*/SKILL.md`, dał „3 files, fits”, kod wyjścia 0 (`foundations` @ `d115159`, 2026-10-29).
- Generator pisze do dwóch katalogów, `.claude/skills` i `.agents/skills` (`agent-instructions/skill_entry_points.py:37`, `ENTRY_DIRECTORIES`), a katalogów, których żaden skill nie tworzy, nie kasuje — wypisuje je do usunięcia przez `git rm -r` (`:17-19`).
- Orkiestrator sprawdza zmienione pliki względem *Change* w kroku cyklu (`task-cycle/skill/SKILL.md:264-266`), a planu nie czyta skillem planisty: jego przegląd planu stoi w `task-cycle/skill/planning.md:6-23`.
- Odrzucone przy przygotowaniu notatki: zmiana działania `task-cycle/slice_size.py` — skrypt już liczy wzorzec jako jeden plik, problem leży w instrukcji (zmienia się tylko opis skryptu, Q4).
- Odrzucone przy przygotowaniu notatki: instalator jako drugi przykład — w produkcie wynik instalatora wchodzi do commitu, który orkiestrator robi sam, poza kawałkami (`task-cycle/skill/SKILL.md:40-44`), więc przykład zapraszałby planistę do wstawienia go do kawałka.
- Odrzucone przy przygotowaniu notatki: generator puszczany przez orkiestratora jednym commitem po ostatnim kawałku — test byłby czerwony od zmiany źródła generatora aż do tego commitu, a przegląd kawałków nie widziałby wyniku generatora.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

Brzmienie z `foundations/decisions.md` i `foundations/invariants.md` na `foundations` @ `d115159`.

- **WAY-136** — „When does a task's change need a plan, and who makes and reviews it?” — kawałki, ich podział i sprawdzenie mechaniczne orkiestratora, które zadanie doprecyzowuje (To do 1–2); zadanie jej nie zmienia: „A change that, as the orchestrator judges before implementation from the task document and, where the task moves the pin, from the checks the move breaks (WAY-34), one agent can hold is made without a plan by one author, who writes its foundation entries, its code and its return step; the same judgment follows a reviewed spec, and an author that finds the change too large returns a report without code, its attempt is discarded with the foundation entries it wrote, and a planner divides the change. Every other change gets a plan written with the-way's skill `plan-task`, which divides it into slices and holds no code; the slices are made one after another in the plan's order, each by an agent of its own, and a slice that proves too large for it is discarded with its code and goes back to the planner to be split. A one-author change is reviewed by an agent that did not make it; of a plan's slices, only one that touches a trust boundary or holds an operation that cannot be undone, as the plan marks it, gets a review of its own by such an agent, and every other slice goes on after the orchestrator's mechanical check and its own checks; […]”. Jej *Rejected* odrzuca „a status by which the planner returns work it cannot divide into slices — the pin moved before the route keeps the installer's output out of every plan” — zadanie nie wprowadza takiego statusu, tylko liczy wynik polecenia jako wzorce.
- **WAY-148** — „How do task-cycle stages pass their work to the orchestrator?” — wykonawca kawałka dostaje tylko swoją sekcję planu, więc polecenie musi stać w niej, w *Goal* (Q2): „[…] it may carry a section of the plan, spec or task copied word for word, never restated in other words, with its file named as its address, so that a slice's executor gets its section of the plan and works without opening the plan […]”.
- **WAY-127** — „How does a session working on the-way itself reach the-way's skills?” — przykład w zdaniu planisty: „A session working on the-way itself reaches each skill of the-way as the project skill `the-way-<name>` through two identical tracked entry points, `.claude/skills/the-way-<name>/SKILL.md` and `.agents/skills/the-way-<name>/SKILL.md`, which a script of `agent-instructions` generates from the skill's `SKILL.md`. […]”; jej test to niezmiennik `skill-entry-points` — ten, który w cyklu `task-cycle-skills-shape` był czerwony między kawałkami.
- **WAY-53** — „How is a derived file compared with what its generator produces?” — powód, dla którego kawałek nie edytuje wyniku polecenia ręcznie: „A derived file is identical to what its generator produces on the same commit, except for values the file itself declares as varying between runs.”; jej test to niezmiennik `derived-file-content`.

## Settlements to record

Candidates: 3 shown, 1 accepted — 2026-10-29

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Pliki, które jedno deterministyczne polecenie zapisuje w jednym uruchomieniu, stoją w *Change* kawałka jako jeden wzorzec ścieżek na każdy katalog, do którego polecenie pisze, liczony jako jeden plik; każdy kawałek, który zmienia to, z czego polecenie pisze, uruchamia je na koniec swojej pracy i commituje cały jego wynik, a jego *Goal* nazywa polecenie i to, że wyniku nie edytuje się ręcznie; plik generatora stoi w *Change* tylko wtedy, gdy kawałek go zmienia; orkiestrator przy sprawdzeniu mechanicznym czyta wzorzec jako każdy plik, który do niego pasuje. | decision | Q1, Q2, Q3 z wariantami niewybranymi; *To do* 1–2; przyjęty: Mariusz, 2026-10-29, „zgodnie z rekomendacjami”; pytania kontrolne tego samego dnia, „tak jak proponujesz”: (K1) na WAY-148 „a slice's executor gets its section of the plan and works without opening the plan” — zakaz ręcznej edycji wchodzi do *Goal*, bo inaczej zna go tylko planista, a wykonawcy cyklu `task-cycle-skills-shape` generowali punkty wejścia na boku (`cycle.md:100`, C7); (K2) na zdanie z notatki „stand in *Change* as the command's source” — generator poza *Change*, gdy się nie zmienia, zostaje, bo polecenie widać w *Goal*, a przegląd nie porównuje plików z *Change* | czy reguła trafia do rejestru decyzji, czy tylko do skilli; czy przy kilku kawałkach zmieniających wejście polecenia uruchamia je każdy, czy ostatni; co wpisać w *Rejected* |

## Out of scope

- Limit 10 zmienianych plików (`task-cycle/slice_size.py:59`) i kod skryptu zostają, jakie są; zmienia się tylko jego opis na początku pliku.
- Plany i zapisy cykli zrobione przed tą zmianą zostają, jakie są.

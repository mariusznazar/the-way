---
title: "the way: lżejsza ścieżka cyklu dla małej zmiany bez zmiany fundamentu — jeden wykonawca z zadaniem w poleceniu, pełne sprawdzenia, jeden przegląd całości"
status: draft
created: 2026-10-08
updated: 2026-10-08
tags: []
related: "[[(P) Proces pracy nad produktem]]"
---

# the way: lżejsza ścieżka cyklu dla małej zmiany bez zmiany fundamentu — jeden wykonawca z zadaniem w poleceniu, pełne sprawdzenia, jeden przegląd całości

Status: ready for cycle
Project relation: independent

## Description

### Need

- Cykl `implement-task` trwa dziś długo, przykłady z `loop2`:
    - PR #6: 3 h 37 min
    - PR #8: 60 min i 11 agentów przy zmianie dwóch plików
- Do małej zmiany, np. zmiany copy, nie ma sensu rozpisywać specu i planu.

### To do

1. Dodać do cyklu `implement-task` lżejszą ścieżkę:
    - jeden wykonawca dostaje zadanie wprost w poleceniu, bez specu i planu, i robi całą zmianę
    - po implementacji te same sprawdzenia co na pełnej ścieżce: cała bramka produktu oraz kontrole, których wymaga to, czego zmiana dotyka (np. próby złośliwych danych przy pliku na granicy zaufania)
    - jeden przegląd całości
2. Wpuszczać zadanie na lżejszą ścieżkę według reguły kciuka:
    - zadanie nie zmienia fundamentu
    - implementacja zmieści się w 10 minut
    - nie wymaga wczytania do kontekstu bardzo dużych plików ani bardzo wielu plików
3. Gdy w trakcie lżejszej ścieżki zmiana okaże się dotykać fundamentu:
    - w prosty i oczywisty sposób — prowadzić dalej lżejszą ścieżką, a wpis fundamentu przepuścić przez skill swojego elementu i jedną niezależną ocenę (WAY-10)
    - w sposób nieoczywisty — przejść na pełną ścieżkę według punktu 6
4. Zmienić WAY-13 tak, żeby rozmiar zadania mógł odchudzić przygotowanie implementacji i samą implementację (spec, plan, liczbę agentów), ale nigdy sprawdzeń po zmianie.
5. Zmienić WAY-125 tak, żeby projekt, spec, plan i przeglądy każdego zadania planu obowiązywały na pełnej ścieżce, a lżejsza ścieżka miała własny zestaw kroków z punktu 1
    - reszta decyzji bez zmian: rola orkiestratora, zapis cyklu, niezależna ocena, krok zwrotu wiedzy i jeden kontakt z człowiekiem przy PR
6. Przechodzić z lżejszej ścieżki na pełną, gdy w trakcie implementacji zmiana okaże się większa, niż wynikało z oceny na starcie:
    - ocenę reguły kciuka robi orkiestrator na starcie, w tej samej analizie co ocenę zmiany fundamentu, i zapisuje jej powody w zapisie cyklu
    - wykonawca, który widzi, że zmiana przerasta regułę, wraca do orkiestratora
    - wykonawca oddaje raport bez kodu i bez diffu: dlaczego zmiana urosła, jakie pliki i przeszkody znalazł, co okazało się nieoczywiste
    - dotychczasową implementację odrzucić
    - świeży projektant dostaje ten raport razem z zadaniem i dalej idzie zwykła pełna ścieżka
    - zaimplementować zmianę od nowa według pełnej ścieżki

### Acceptance criteria

- Zadanie, które nie spełnia reguły kciuka, przechodzi pełną ścieżką tak samo jak przed zmianą.

### Questions to settle

- Czy wybór z punktu 4 trzyma się wobec uzasadnienia WAY-13: „size misleads both ways: a rename across many files is easy to undo, a one-line change to a stored format can destroy every user's data”?
  - Answer: trzyma się bez zmian — zmianę, której nie da się cofnąć, i tak zatrzymuje dla człowieka reszta WAY-13, a sprawdzenia po zmianie zostają pełne; dodatkowy warunek wykluczający zmiany nieodwracalne i pliki na granicy zaufania odrzucony, bo zabrałby lżejszą ścieżkę zadaniom takim jak PR #8.
- Jak pogodzić lżejszą ścieżkę z WAY-125, która przyjmuje projektowanie, spec, plan i przeglądy każdego zadania planu dla zadania prowadzonego przez `implement-task`?
  - Answer: zmienić WAY-125 (punkt 5) — lżejsza ścieżka zostaje wariantem `implement-task`; osobny skill odrzucony, bo dwa skille trzymałyby te same reguły zapisu, PR i kroku zwrotu wiedzy, a WAY-13 opisuje ścieżki jako warianty jednego procesu.
- Kto i kiedy ocenia, czy zadanie spełnia regułę kciuka z punktu 2, i co się dzieje, gdy w trakcie implementacji okaże się, że jej nie spełnia?
  - Answer: orkiestrator na starcie, a w razie przerostu powrót na pełną ścieżkę (punkt 6); implementację odrzucamy i robimy od nowa, żeby nie dopisywać specu i planu do częściowej implementacji; wariant „raz przyjęte zadanie kończy się lżejszą ścieżką” odrzucony.
- W jakiej formie wiedza wykonawcy z porzuconej próby trafia do specu i planu?
  - Answer: raport wykonawcy bez kodu i diffu dla świeżego projektanta (punkt 6); wariant „wykonawca sam pisze spec i plan” odrzucony, bo spec niósłby kształt porzuconej implementacji.

## Context

### Materiał

- PR #6: https://github.com/mariusznazar/loop2/pull/6
    - zmieniał fundament, więc na lżejszą ścieżkę by nie wszedł; tu służy tylko jako przykład dzisiejszego czasu cyklu
- PR #8: https://github.com/mariusznazar/loop2/pull/8
    - jego 11 agentów to orkiestrator, projektant, recenzent specu, planista, trzech wykonawców, trzech recenzentów zadań i recenzent całości

### Gdzie szukać

- Skill cyklu `task-cycle/skill/SKILL.md` w the-way wymaga specu i planu dla każdego gotowego zadania (krok 6) i pełnej pętli przeglądów przez subagentów nawet przy niskiej krytyczności (krok 4).
- Decyzja WAY-125 przyjmuje te metody Superpowers dla zadania prowadzonego przez `implement-task`.

### Sposób wykonania

- Zadanie idzie przez `implement-task` jako jednorazowy wyjątek od `agent-instructions/README.md` w the-way, który zmiany samego the-way prowadzi bez cyklu; przewodnik zostaje bez zmian.
- Wyjątek ma pokazać, czy cykl na samym the-way jest wart swojej ceny, zanim zapadnie decyzja o zmianie przewodnika.
- Dopasowania cyklu do the-way:
    - reguły procesu cykl czyta z commita bazowego `foundations`, a nie z przypiętego podmodułu `.the-way`, i według nich prowadzi zadanie, choć zadanie je zmienia
    - pełnej bramki nie ma: cykl uruchamia częściowe testy i strażników formatu z przewodnika i zapisuje resztę jako niesprawdzoną
    - PR idzie do `foundations`; tam, gdzie przewodnik różni się od skilla cyklu, rządzi przewodnik

## Questions carried to cycle

- Którymi metodami Superpowers przyjętymi w WAY-125 posługuje się lżejsza ścieżka (np. implementacja zaczynana od testów przy zmianie zachowania, przegląd całości, przygotowanie PR)?
- Jak odrzucić częściową implementację przy przejściu na pełną ścieżkę i co z porzuconej próby zostaje w zapisie cyklu?

## Decisions in play

- **WAY-13/1 — What sets the weight of a task's process?** (`foundations/decisions.md`; zadanie zmienia ją w punkcie 4)
  > What a task touches, never its size, sets its process: an agent's analysis at the start of the task settles whether it changes the foundation, which chooses among the paths that merge a change, while three things set how sharply it is checked — the criticality of the parts it touches, as the part map computes it, whether it touches the files of a trust boundary, and whether the change can be undone. Paths that merge a change differ in their steps, never in the outcome a task has to reach, and only a human sets a task to return knowledge instead of a change, which merges nothing. A task's size serves only as a signal to split it, an agent may check a change more sharply than the map computes, never less, and a human decides on every change that cannot be undone.
- **WAY-125/1 — Which Superpowers methods does the autonomous task cycle adopt?** (`foundations/decisions.md`)
  > The the-way task cycle adopts Superpowers 6.4.1 methods for brainstorming a design and written spec, writing an implementation plan, test-first implementation, subagent execution with independent task and final code reviews, and preparing a pull or merge request; they apply only to a ready task run through `implement-task`. The orchestrator answers workflow questions and gives provisional stage go-aheads under the task owner's delegation, never records these as human approval, controls the return between stages, keeps agent reports before a borrowed skill cleans its workspace, runs the independent assessment of its foundation change and its return step, and brings the request to the human for review. Decisions reserved to a human by the foundation remain reserved; when required code cannot proceed without one, the cycle opens a blocked draft request; a different Superpowers version requires a reviewed change to the-way before use.
- **WAY-10/1 — Who assesses a change to an invariant test or to the foundation?** (`foundations/decisions.md`; punkt 3 z niej korzysta)
  > A change to an invariant test or to the foundation is assessed by one independent agent, on a model other than its author's where one is available, which sees the diff and the files of the commit it assesses without the task's chronicle or the author's reasoning and names what of the change can be cut, or that nothing can. The author settles each of its remarks and records how, and a settlement that changes the assessed foundation entries or invariant tests is part of the assessed change and does not reopen its assessment. A human accepts the change, with the assessment and its settlement, when merging it.

## Out of scope

none

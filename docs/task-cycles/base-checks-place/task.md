---
title: "the way: pomiar testów przed zmianą idzie tam, gdzie żaden agent nie zmienia plików"
status: draft
created: 2026-10-30T19:30
updated: 2026-10-31
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# Pomiar testów przed zmianą idzie tam, gdzie żaden agent nie zmienia plików

Status: ready for cycle
Project relation: independent

## Description

### Need

- Na początku cyklu agent prowadzący sprawdza, które testy padają jeszcze przed zmianą, żeby potem odróżnić stare błędy od nowych, a instrukcja nie mówi, gdzie i kiedy ten pomiar puścić (`task-cycle/skill/SKILL.md:113`).
- W cyklu `rejected-from-refinement` pomiar szedł w tym samym katalogu, w którym autor commitował, więc zmierzył mieszankę starego i nowego kodu i trzeba go było odrzucić (`docs/task-cycles/rejected-from-refinement/cycle.md:41-47` na commicie `a2c1164`).
- Traci na tym agent cyklu, który marnuje przebieg testów, w the way około pół godziny, a pośrednio Mariusz, bo mieszanka, która przypadkiem wyjdzie poprawnie, niczym się nie zdradza.
- Bez zmiany agent rozstrzyga miejsce pomiaru sam przy każdym cyklu; zdarzyło się to raz w sześciu sprawdzonych zapisach cykli, ale gdy się zdarzy, zmianę porównuje się z pomiarem bez wartości.

### To do

1. W kroku 4 `task-cycle/skill/SKILL.md`, zaraz po „Record the base commit and the checks already failing on it”, staje zdanie: „Run those checks on the base alone: finish them before anything changes a tracked file of the worktree, or run them in a separate checkout of the base commit under the worktree's ignored `.runs/`, deleted when they end.”

### Questions to settle

- Gdzie stoi osobna kopia kodu z drugiej drogi, skoro `task-cycle/skill/SKILL.md:68` mówi „The cycle writes only in the task's worktree”?
  - Answer: W ignorowanym `.runs/` worktree zadania, skąd po pomiarze jest kasowana, jak klon z kroku 2 (`task-cycle/skill/SKILL.md:40-43`); wiersz 68 zostaje bez zmian i nie powstaje żaden wyjątek.
  - Not chosen:
    - Czekać na zadanie o plikach tymczasowych — to zadanie czeka bez terminu, bo tamto ma otwarte pytanie o nieudane kasowanie.
    - Wyjątek od wiersza 68 tylko dla tego pomiaru, z kopią poza worktree — zadanie przejmuje pytanie o nieudane kasowanie, a tamto musi ten wyjątek scalić.
  - Source: Mariusz, 2026-10-30: „C, bierzemy”, na propozycję zdania i trzy pokazane drogi.

## Context

- Pierwsza droga jest prostsza, ale przy cyklu z jednym autorem opóźnia start o czas testów, w the way 24–32 minuty.
- Druga droga niczego nie opóźnia i zadziałała w cyklu `rejected-from-refinement`, ale w `loop2` osobna kopia wymaga najpierw `node_modules` i zawartości `.the-way`, bo `scripts/test.py` uruchamia `.the-way/gate/run_tests.py`, więc tam zwykle wypadnie pierwsza.
- „Tracked file” zamiast „the first agent that changes code” obejmuje też commit przesunięcia wersji the way, który w kroku 2 robi sam agent prowadzący.
- Kopia w `.runs/` nie trafia do bramki: `gate/run_tests.py` bierze pliki z `git ls-files`, a `scripts/test.py` w `loop2` ma listę wzorców w `tests/`.
- Uwaga, z której wyszło zadanie: `docs/task-cycles/rejected-from-refinement/cycle.md:135` na commicie `a2c1164`.
- Zakaz dwóch pełnych przebiegów naraz padł, bo w tym samym cyklu dwa równoległe przebiegi urwały się jednocześnie, ale ich czas zakończenia zgadza się z poleceniem innego agenta, które ubiło wszystkie procesy Pythona na komputerze, więc równoległość nie była przyczyną.

## Questions carried to cycle

- Czy `task-cycle/record_template.md:116`, który mówi tylko, że wynik pomiaru notuje się osobno, wymaga dopisku, czy zmiana w jednym miejscu wystarczy.

## Human actions

none

## Decisions in play

- WAY-140: „A task's effect outside the product's repository — on a server, in DNS, on keys or on an external account — is made only by a human, through a human action the task document names and places before the cycle or in it, while reading outside the repository stays with the agent”. Zdanie z wiersza 68 powołuje się na tę decyzję, ale decyzja mówi o repozytorium, nie o worktree zadania.
- WAY-160: „The task-cycle orchestrator itself runs the product's gate on the tree that goes into the request”. Decyzja dotyczy pomiaru po zmianie; pomiar na bazie należy do tego samego agenta, bo krok 4 jest pisany do niego.
- WAY-256: „a fragment of one step or variant that is one instruction, which would otherwise stand in a file beside the skill, stays in `SKILL.md` where its pointer would stand”.

## Settlements to record

Candidates: 3 shown, 0 accepted — 2026-10-30

none

## Out of scope

- Zakaz dwóch pełnych przebiegów testów naraz.

---
title: Kopie robocze agentów cyklu stoją w katalogu zadania, każdy agent w swoim podkatalogu, i znikają przed oddaniem wyniku
status: draft
created: 2026-11-14T02:44
updated: 2026-11-14
tags: [zadanie]
related: "the author's note of the process project"
---

# Kopie robocze agentów cyklu stoją w katalogu zadania, każdy agent w swoim podkatalogu, i znikają przed oddaniem wyniku

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Agenci cyklu `implement-task` zostawiają kopie robocze — drzewa robocze do sprawdzenia, klony do przeglądu, skrypty, przygotowane wejścia testów, zrzuty ekranu — poza katalogiem zadania albo tam, skąd nie mogą ich potem usunąć.
- Mariusz sprząta je ręcznie; część raportów wymienia pliki tymczasowe bez informacji, czy zostały usunięte.
- Agenci jednego cyklu dzielą schowek sesji prowadzącego i nadpisują sobie nawzajem skrypty, więc przebieg jednego agenta potrafi uruchomić skrypt innego.
- Skill cyklu każe pisać tylko w worktree zadania, ale nie mówi, gdzie takie kopie mają stać ani co robić, gdy usunięcie się nie uda.

### To do

1. Agent cyklu, który robi kopię roboczą do sprawdzenia — drzewo robocze commita, klon, skrypt, zrzut ekranu, przygotowane wejście testu — robi ją we własnym podkatalogu w ignorowanym `.runs/` katalogu zadania, osobnym dla każdego agenta, nigdy w katalogu tymczasowym systemu, w schowku sesji ani w głównej kopii repozytorium. Miejsca do zmiany: w `task-cycle/review/SKILL.md` zdanie „Run them in a separate worktree of the head commit when they need files changed” (około linii 96), w `task-cycle/plan/SKILL.md` zdanie kończące się „run on the base in a separate worktree” (około linii 180), w `task-cycle/skill/SKILL.md` akapit zaczynający się „The cycle writes only in the task's worktree” i akapit zlecenia zaczynający się „The handoff gives the user's delegation, the worktree” (około linii 179).
2. Przed oddaniem wyniku agent usuwa swoją kopię, zachowuje w `reports/` to, czego potrzebuje jego raport, i podaje w raporcie, gdzie kopia stała i że została usunięta.
3. Gdy usunięcie się nie uda, agent kończy pracę, a w raporcie wymienia pozostałość z jej ścieżką; orkiestrator przenosi ją do zapisu cyklu i do opisu PR-a, żeby człowiek ją zobaczył. Ta sama zasada obejmuje osobne kopie bazy w `.runs/` z kroku 4 cyklu (akapit z „deleted when they end”, `task-cycle/skill/SKILL.md`, około linii 151).

### Questions to settle

- Gdzie stoi kopia robocza agenta cyklu, kto ją usuwa i co się dzieje, gdy usunięcie się nie uda?
  - Answer: każdy agent dostaje własny podkatalog w `.runs/` katalogu zadania; usuwa go przed oddaniem wyniku, a to, czego potrzebuje raport, zachowuje w `reports/`; gdy usunięcie się nie uda, agent kończy pracę, wymienia pozostałość w raporcie, a cykl przenosi ją do zapisu cyklu i do opisu PR-a; resztki znikają razem z katalogiem zadania.
  - Not chosen:
    - kopia może stać poza katalogiem zadania do powrotu agenta (szkic AIR-490) — kłóci się z twardą blokadą zapisu poza katalogiem zadania, którą ustala zadanie the abandoned task of a hard block on writing outside the task's directory.
    - nieudane usunięcie zatrzymuje cykl — cykl stanąłby przez rzecz, którą człowiek usuwa jednym poleceniem.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14, odpowiedź „5 a” w doprecyzowaniu zadania the abandoned task of a hard block on writing outside the task's directory.
- Czy ta reguła idzie osobnym zadaniem przed blokadą?
  - Answer: tak — ustalenia zostają razem w dokumencie blokady, a reguła kopii roboczych idzie od razu jako małe zadanie; blokada idzie po wyborze mechanizmu.
  - Not chosen:
    - jedno zadanie z blokadą — sprzątanie po agentach czekałoby na badanie mechanizmu i duży cykl.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14, odpowiedź „7 b”.

## Context

- Zadanie blokady porzucono 2026-11-14 (decyzja Mariusza: problem sztuczny, a kontener czy osobne konto na agenta kosztuje za dużo). Ta reguła stoi sama: tania reguła w instrukcjach cyklu, którą można dociągnąć hookiem albo skryptem; odwołania niżej do blokady są tłem, nie zależnością. Mariusz przeczytał zakres i puścił zadanie do cyklu 2026-11-14.
- Zadanie wydzielone 2026-11-14 z the abandoned task of a hard block on writing outside the task's directory, do którego wcześniej włączono sprawę AIR-490; tam stoi pełny materiał źródłowy.
- AIR-490 (`a private note of the author's on the reviews of agent sessions`, „### AIR-490”): kopie poza worktree w the-way PR #11 i #15 oraz `loop2` PR #24; recenzent PR #11 nie mógł usunąć katalogów z wrogimi danymi testowymi, a w PR #15 usunięcie klonu odrzuciła automatyczna ocena zgód Codexa.
- Powtórki w późniejszych cyklach (`a private note of the author's on the cycles read in those reviews`): `loop2` PR #41, #45 (nadpisany cudzy plik w schowku sesji), #46, #47 oraz the-way PR #77 (agenci dzielą schowek sesji prowadzącego i nadpisują sobie skrypty).
- Uwaga theway#061-3 z pierwszego przeglądu fundamentu: gdy usunięcie kopii bazy w `.runs/` się nie uda, skill nie mówi agentowi, co zgłosić (`a private note of the author's with the remarks of the first review of the foundation`, „Dopisek: twarda blokada i sprzątanie kopii”).
- `.runs/` jest już ignorowanym katalogiem roboczym cyklu w katalogu zadania: trzyma zapis cyklu (`.runs/task-cycles/<task-slug>/`) i kopie bazy z kroku 4.
- Gotowe brzmienie podobnej reguły jest w `product-guidelines/coding/SKILL.md` (narzędzie uruchamiane „in a scratch worktree of its commit or in a temporary environment … the scratch worktree is removed afterwards”).
- Usuwanie samych katalogów zadań po scaleniu PR-a to osobne zadanie (zaparkowane 2026-11-14), a „resztki znikają razem z katalogiem zadania” zależy od niego.

## Questions carried to cycle

- Dokładna ścieżka podkatalogu agenta w `.runs/` i to, jak zlecenie go nazywa.
- Zrzut ekranu, który serwer Playwright MCP sam zapisuje pod katalogiem sesji, która go uruchomiła (poza katalogiem zadania, AIR-490, `loop2` PR #24): czy agent przenosi go do swojego podkatalogu i usuwa oryginał, czy wskazuje serwerowi miejsce zapisu.

## Human actions

none

## Decisions in play

- WAY-140 — How does a task change something outside the product's repository?: „A task's effect outside the product's repository — on a server, in DNS, on keys or on an external account — is made only by a human, through a human action the task document names and places before the cycle or in it, while reading outside the repository stays with the agent and the cycle's record of the request and of the task's state in the backlog entry the product names (WAY-107) is no effect of the task.”
- WAY-316 — Where do the screenshots that a change shows the human lie, and how do they reach the request?: „[…] the screenshots that its author or reviewer shows the human are embedded as images in the description of the request, from a place that the foundation of the product settles outside the product's repository; the-way names no place. No file of a screenshot is committed to the product's repository […]” — zrzut pokazywany człowiekowi idzie tą drogą; to zadanie dotyczy tylko zrzutu jako kopii roboczej do sprawdzenia.

## Settlements to record

Candidates: 1 shown, 1 accepted — 2026-11-14

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Każdy agent cyklu robi kopię roboczą we własnym podkatalogu w `.runs/` katalogu zadania i usuwa ją przed oddaniem wyniku, a to, czego potrzebuje raport, zachowuje w `reports/`; gdy usunięcie się nie uda, agent kończy pracę, wymienia pozostałość w raporcie, a cykl przenosi ją do zapisu cyklu i do opisu PR-a. | decision | pytanie „Gdzie stoi kopia robocza agenta cyklu…” (wybór człowieka; drogi niewybrane pod pytaniem) | czy kopia idzie do katalogu tymczasowego systemu albo schowka sesji, i czy nieudane usunięcie zatrzymuje cykl |

## Out of scope

- Twarda blokada zapisu poza katalogiem zadania — zadanie the abandoned task of a hard block on writing outside the task's directory.
- Pliki tymczasowe, które narzędzia i testy produktu tworzą same w katalogu tymczasowym systemu — rozstrzyga je zadanie blokady.
- Usuwanie katalogów zadań po scaleniu PR-a i sprzątanie schowków sesji `%TEMP%\claude`.

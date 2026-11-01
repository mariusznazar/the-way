---
title: "the way: agenci szukają decyzji złym poziomem nagłówka"
status: draft
created: 2026-10-31T18:01
updated: 2026-11-01
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# the way: agenci szukają decyzji złym poziomem nagłówka

Status: ready for cycle
Project relation: independent

## Description

### Need

- Zanim agent zacznie pracę, wyszukuje i czyta wybrane decyzje z pliku `foundations/decisions.md`.
- W tym pliku każda decyzja stoi pod nagłówkiem `###`, a we wszystkich pozostałych plikach katalogu `foundations/` wpisy stoją pod `##`.
- Agenci przenoszą nawyk z tamtych plików: w październiku w sesjach Claude Code na repozytoriach the-way i loop2 147 razy szukali decyzji nagłówkiem `##`, a 85 z tych poleceń nie zwróciło żadnego wpisu.
- Odczuwają to agenci, którzy muszą wykonać kolejne polecenie, a pośrednio Mariusz, który płaci za te powtórki.
- Nic się nie psuje, bo puste wyszukiwanie agent od razu poprawia; zostaje około trzech zbędnych poleceń dziennie.
- Metoda czytania fundamentu ma mówić wprost, jaki poziom nagłówka ma który plik.

### To do

1. W `elements/common/way_of_working.md:73`, po słowach „Read each decision found whole, as the range of lines from its heading to the next heading”, dopisać:

   > (`###` in the decision log, `##` in the other foundation files)

2. W `task-cycle/change/SKILL.md:32`, po słowach „The foundation entries the dispatch names by identifier, each whole”, dopisać:

   > , an entry running to the next heading (`###` in the decision log, `##` in the other foundation files)

### Questions to settle

- Czy wstawka ma objąć też pliki, z których wpisy fundamentu czytają recenzent (`task-cycle/review/SKILL.md:32`), autor specyfikacji (`task-cycle/spec/SKILL.md:22`) i planista (`task-cycle/plan/SKILL.md:37`)?
  - Answer: Nie, zostają dwie wstawki z *To do*; obejmują 23 z 37 zmierzonych poleceń, a zostaje około 1,5 zbędnego polecenia dziennie.
  - Not chosen:
    - Trzecia wstawka u recenzenta — obejmuje 26 z 37 poleceń, ale to trzecia kopia zdania i zmiana układu nagłówków to trzy poprawki.
    - Wstawki we wszystkich pięciu plikach — pięć kopii, a w zmierzonym okresie autor specyfikacji i planista nie dali ani jednego dodatkowego polecenia, więc też 26 z 37.
  - Source: Mariusz, 2026-11-01: „A”. Pomiar: transkrypty Claude Code the-way i loop2, 24–31 października 2026: 37 poleceń szukających decyzji wyłącznie nagłówkiem `##`; przed 23 zdanie z `way_of_working.md:73` nie istniało, więc wcześniejszych poleceń nie liczono. Agent miał już wtedy w transkrypcie zdanie jednego z dwóch plików z *To do* w 23 poleceniach, tylko zdanie recenzenta w 3, a żadnego z pięciu zdań w 11.

## Context

- Źródło: sprawa AIR-554 z przeglądu warstwy AI, 2026-10-31, w `C:\Storage\The Brain\The Brain\Notes\Areas\(A) Claude code\ai_review_ledger.md:278`.
- Numery linii z *To do* zgadzają się ze stanem `foundations` @ 2f51e6c.
- Poziomów nagłówków pilnuje `elements/common/foundation_check.py:252` (`###`) oraz `:288` i `:313` (`##`), więc obowiązują też w produktach.
- W produktach wstawki zadziałają dopiero po przesunięciu wersji the-way, której używają.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-150: „reads each selected entry whole, reading more entries where relevance is uncertain and a whole file only where it is short”; „every other agent of the cycle reads what its handoff names and reaches for what is missing selectively — a search for an identifier or a word and a read of the passage found, never of a whole file of the foundation”.
- WAY-256: „a fragment of one step or variant that is one instruction, which would otherwise stand in a file beside the skill, stays in `SKILL.md` where its pointer would stand”.

## Settlements to record

Candidates: 3 shown, 0 accepted — 2026-11-01

none

## Out of scope

- Wstawki w `task-cycle/review/SKILL.md:32`, `task-cycle/spec/SKILL.md:22` i `task-cycle/plan/SKILL.md:37`, choć z tych plików wpisy fundamentu czytają recenzent, autor specyfikacji i planista.
- Skrypt do wyjmowania wpisów, który proponował nocny przegląd: rozwiązywał głównie ucinanie długich odczytów w Codexie (174 na 987 odczytów pliku decyzji), a z Codexa już nie korzystamy.
- W Claude Code na 1470 odczytów tego pliku odrzucone zostało 7, zawsze z jasnym komunikatem.
- Skrypt nie zmniejszyłby też liczby wpisów do przeczytania, a w produktach byłby dostępny dopiero po przesunięciu wersji the-way, której używają.

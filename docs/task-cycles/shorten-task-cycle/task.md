---
title: "the way: skrócić cykl implement-task — czas pracy agentów i zużycie tokenów"
status: draft
created: 2026-10-13
updated: 2026-10-14
tags: [the-way, zadanie]
related: ["[[(P) Proces pracy nad produktem]]"]
---

# the way: skrócić cykl implement-task — czas pracy agentów i zużycie tokenów

Status: ready for cycle
Project relation: independent

## Description

### Need

- Cykl `implement-task` dla zadania średniej wielkości (`mag-w-lesie` w `loop2`) pracował 3 h 51 min, a łańcuch kursu 10xDEVS dla tego samego zadania ok. 80 min.
- Cykl zużył 198 mln tokenów.
- Podczas pracy osiągnął limit użycia i czekał 1 h 48 min.
- Orkiestrator zjada dużą część tokenów: w PR #11 (cykl `instruction-files-part`) 153 mln z 364 mln (42%), w `mag-w-lesie` czytał od 0,5 do 3 mln tokenów na etap.
- Najdłuższy etap `mag-w-lesie` to krok powrotny z testami niezmienników, celowymi złamaniami i niezależną oceną — ok. 80 min, 35% czasu.

### To do

1. Skrócić kontekst orkiestratora i przekazywać pracę przez pliki.
2. Dopisywać w kroku powrotnym nowy niezmiennik dla zachowania, którego zmiana w następnym zadaniu naruszyłaby wymagania lub ustalenia produktu; szczegóły wykonania, które można zmienić bez takiego naruszenia, pozostawiać w zwykłych testach i opisie zmiany.
3. W kroku powrotnym przeprowadzać niezależną ocenę przed celowymi złamaniami testów dopisanych w tym kroku, żeby poprawki po ocenie nie wymuszały powtórki tych złamań; wcześniejsze złamania zachowują swoje miejsce w cyklu.
4. Rekomendować podział pracy na niezależne plasterki i wskazywać możliwość ich równoległego wykonania, niezależnie od ograniczeń obecnie używanego skilla.
    - orkiestrator ocenia, czy równoległość ma sens — na przykład czy plasterki nie dotykają tych samych plików i czy ich przegląd da się prowadzić osobno

### Questions to settle

- Czy podstawowa reguła ruchu może pozostać wyłącznie w zwykłych testach, bez osobnego niezmiennika?
  - Answer: Nie; zachować jako niezmiennik regułę, że każdy ruch kończy się na sąsiednim kafelku. Mariusz przyjął rekomendację zachowania tej podstawowej reguły działania produktu.
- Co rozstrzyga o potrzebie nowego niezmiennika dla pozostałych zachowań odkrytych w kroku powrotnym?
  - Answer: Czy następne zadanie mogłoby zmienić to zachowanie bez naruszenia wymagań lub ustaleń produktu? Jeśli tak, jest to szczegół wykonania; jeśli nie, jest to reguła wymagająca niezmiennika. Kryterium nie pozwala pomijać niezmienników wymaganych przez zapisane decyzje.
- Czy niezależna ocena ma poprzedzać celowe złamania tylko testów dopisanych w kroku powrotnym, czy również testów pisanych wcześniej w cyklu?
  - Answer: Tylko testów dopisanych w kroku powrotnym; wcześniejsze złamania zachowują swoje miejsce w cyklu.
- Czy zasadę podziału na niezależne części uzależniać od ograniczeń obecnie używanego skilla?
  - Answer: „the way powinno rekomendować podział niezależnych części, a to, że używany obecnie skill to wyklucza to osobna kwestia”. Rekomendacja obowiązuje również wtedy, gdy używany skill wykona części kolejno; realizacja przy użyciu obecnego skilla pozostaje pytaniem wykonawczym.

## Context

### Skąd to wiemy

- `mag-w-lesie`: sesja `cdeb45b6`, zestawienie etapów `docs/task-cycles/mag-w-lesie/stages.md` z commita `c9644b2` w `loop2`; porównanie z kursem w notatkach m2l2 w [[mapa_pakietu_10x]].
- PR #11: `docs/task-cycles/instruction-files-part/stages.md` z commita 58ee76e.
- Celowe złamania jedenastu nowych testów w `mag-w-lesie` wykonano w czterech turach: dwóch przed niezależną oceną i dwóch po niej.

### Granice porównania

- Łańcuch kursu nie pisał fundamentu ani testów niezmienników w tej skali, więc porównanie czasu nie jest jeden do jednego.

### Ryzyka wybranych wariantów

- Punkt 2: coś, co złapałby test niezmiennika, może przejść po cichu w następnym zadaniu.
- Punkt 4: konflikty w tych samych plikach i trudniejszy przegląd — stąd ocena orkiestratora przed równoległym startem.
- Zestawienie `mag-w-lesie` potwierdza 3:50:54 pracy i 198 549 901 tokenów; 191 057 172 z nich to wejście z pamięci podręcznej, więc suma nie oznacza tylu różnych tokenów tekstu ani nie jest miarą kosztu pieniężnego.
- Raport kroku powrotnego `mag-w-lesie` wymienia jedenaście nowych niezmienników; osobno pozostawia zwykłym testom szczegóły wykonania, m.in. geometrię heksów i kolejność losowania.
- Superpowers 6.4.1, `subagent-driven-development/SKILL.md:282`, zabrania równoległych wykonawców: „Never dispatch multiple implementation subagents in parallel (conflicts).”.
- Zakaz równoległych wykonawców w obecnym Superpowers jest ograniczeniem sposobu realizacji; nie określa zasady the-way dotyczącej rekomendowania podziału na niezależne części.

## Questions carried to cycle

- Jak ograniczyć kontekst orkiestratora i przekazywać pracę przez pliki?
- Jak zrealizować rekomendację niezależnych części i możliwości ich równoległego wykonania przy zakazie równoległych wykonawców w obecnym Superpowers, zachowując osobny przegląd każdego plasterka?

## Human actions

none

## Decisions in play

- WAY-11/1 — obowiązkowy krok powrotny; punkt 2 doprecyzowuje granicę między regułą produktu a szczegółem wykonania i wymaga uzgodnienia z obecnym szerokim brzmieniem:
  > A task ends with its return step before its branch is merged: an agent lists from the diff and the task's log new rules and decisions, code behaviour with no invariant over it, environment facts the change rests on that the foundation does not yet hold and words whose use the glossary does not yet settle, writes them into the foundation in the same change, which its independent assessment covers (WAY-10), and compares the foundation with the code in the parts the task touched. A periodic review of the foundation runs apart from tasks.
- WAY-12/1 — weryfikacja decyzji przez niezmienniki; punkt 2 zachowuje obowiązek niezmienników wymaganych przez zapisane decyzje:
  > A decision is checked through the invariants derived from it, which its *Verification* names by the identifiers of their entries, and tests live only with invariants. Where no invariant can be derived today, an agent compares a change with the decision using a pair of examples — one that complies and one that violates — and where an agent cannot judge, a human assesses it and leaves a trace of who and when. A decision can combine levels, each covering what it can check of its binding sentences.
- WAY-10/1 — jedna niezależna ocena zmiany fundamentu i testów niezmienników; punkt 3 zmienia jej miejsce względem celowych złamań:
  > A change to an invariant test or to the foundation is assessed by one independent agent, on a model other than its author's where one is available, which sees the diff and the files of the commit it assesses without the task's chronicle or the author's reasoning and names what of the change can be cut, or that nothing can. The author settles each of its remarks and records how, and a settlement that changes the assessed foundation entries or invariant tests is part of the assessed change and does not reopen its assessment. A human accepts the change, with the assessment and its settlement, when merging it.
- WAY-69/1 — rozdzielenie autorów zdania, testu i kodu; celowe złamanie pisze recenzent:
  > An invariant's sentence, the check that cites it and the code it covers come from three different agents, and the deliberate break the check is accepted on is written from the sentence by the reviewer of that code, who did not write the check. A check that cites an invariant takes the input it asserts on and the value it expects written out, wherever the code its invariant is about would otherwise compute either; only the side it compares against comes from the run.
- WAY-136/1 — plan, autor i przegląd każdego plasterka; punkt 4 musi zachować te obowiązki:
  > Every task's cycle writes a plan with the-way's skill `plan-task`, which divides the change into slices and holds no code. Each slice is made by an agent of its own and then reviewed by an agent that did not make it, and a change of more than one slice then gets one review of the whole change, while the review of a plan's only slice is the review of the whole change. A slice that proves too large for the agent making it is discarded with its code and goes back to the planner to be split.
- WAY-36/1 — do fundamentu trafia reguła obowiązująca po scaleniu; reguła kończąca się z pracą zostaje w jej planie:
  > A rule enters the decision log only when it still binds once the change that brings it has been merged; a rule that ends with a piece of work — an order of steps, a first merge, a transition between two states — stays in the plan of that work.
- WAY-125/1 — przyjęcie metod Superpowers 6.4.1; sposób realizacji zasady z punktu 4 trzeba uzgodnić z ograniczeniem zapożyczonej metody, bez podporządkowywania mu samej zasady the-way:
  > The the-way task cycle adopts Superpowers 6.4.1 methods for brainstorming a design and written spec, test-first implementation, subagent execution with independent task and final code reviews, and preparing a pull or merge request, only for a ready task run through `implement-task`. The orchestrator answers workflow questions and gives provisional stage go-aheads under the task owner's delegation, never records these as human approval, controls the return between stages, keeps agent reports before a borrowed skill cleans its workspace, runs the independent assessment of its foundation change and its return step, and brings the request to the human for review. Decisions reserved to a human by the foundation remain reserved; when required code cannot proceed without one, the cycle opens a blocked draft request; a different Superpowers version requires a reviewed change to the-way before use.

## Settlements to record

Candidates: 4 shown, 4 accepted — 2026-10-14

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Skrócić kontekst orkiestratora i przekazywać pracę przez pliki. | decision | To do, punkt 1; przyjęty zakres 1–4 | Czy pełne przekazania pracy i raporty mają nadal trafiać do kontekstu orkiestratora. |
| 2 | Nowy niezmiennik jest potrzebny dla zachowania, którego zmiana w następnym zadaniu naruszyłaby wymagania lub ustalenia produktu; szczegóły wykonania, które można zmienić bez takiego naruszenia, pozostają w zwykłych testach i opisie zmiany. | decision | Questions to settle — kryterium nowych niezmienników; odpowiedź „brzmi sensownie” | Czy każde odkryte zachowanie wymaga osobnego niezmiennika. |
| 3 | Niezależna ocena poprzedza celowe złamania tylko testów dopisanych w kroku powrotnym; wcześniejsze złamania zachowują swoje miejsce w cyklu. | decision | Questions to settle — kolejność oceny i złamań; odpowiedź „tak, przesuńmy tylko złamania z kroku powrotnego” | Czy odroczyć również złamania testów napisanych przed implementacją lub podczas niej. |
| 4 | The-way powinno rekomendować podział pracy na niezależne części i wskazywać możliwość ich równoległego wykonania, a ograniczenia obecnie używanego skilla pozostają osobną kwestią realizacji. | decision | To do, punkt 4; Questions to settle — niezależność zasady od narzędzia; odpowiedź autora własnymi słowami | Czy podporządkować rekomendację równoległej pracy zakazowi równoległych wykonawców w obecnym skillu. |

## Out of scope

- Ograniczenie odczytu dużych dokumentów przez `plan-project` jest osobnym zadaniem: [[ograniczyc_odczyt_dokumentow_plan_project]].
- Wprowadzanie dodatkowej kompakcji kontekstu orkiestratora sterowanej przez the-way.

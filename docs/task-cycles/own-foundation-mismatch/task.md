---
title: "the way: przegląd ocenia niezgodność zmiany z ustaleniem, które ta sama zmiana zapisuje, jako blokującą, a nie jako drobną uwagę"
status: draft
created: 2026-10-29T11:10
updated: 2026-10-29
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# Recenzent cyklu ocenia jako Important niezgodność zmiany z wpisem fundamentu, który ta sama zmiana zapisuje albo zmienia

Status: ready for cycle
Project relation: independent

## Description

### Need

- Recenzent cyklu ocenia uwagi jako Critical, Important albo Minor; uwaga Critical albo Important w zakresie zadania blokuje i dostaje jedną rundę poprawki, a Minor idzie do PR-a bez poprawki (WAY-161; `task-cycle/review/SKILL.md:84-97`, `foundations` @ `d115159`).
- Recenzent sprawdza, czy wpisy fundamentu, które zmiana sama zapisuje albo zmienia, mówią to, co robi kod (`task-cycle/review/SKILL.md:63-65`), ale sekcja ocen nie mówi, jak ocenić niezgodność z takim wpisem.
- W PR #49 zmiana zapisała WAY-258 („No rule stands in two of its files”), a krok powrotu, przenosząc tekst do nowych plików, stworzył powtórzenia reguł w dwóch plikach; przegląd kroku powrotu ocenił je jako Minor 2: „Today each pair says the same, so the effect is drift risk only” (the-way @ `fa5304f`, `docs/task-cycles/instruction-files-router/reports/return-review-report.md:73-75`).
- Poprawka przyszła dopiero po pytaniu Mariusza (uwaga R2, tamże, `reports/correction-remarks.md`) i kosztowała rundę poprawek z jednym przeglądem `FAIL 44475cf` po drodze (tamże, `cycle.md`, wiersz 2026-10-28T01:08Z).
- Bez zmiany PR może nieść fundament, któremu przeczy jego własna zmiana, a następne zadania czytają kod i wpisy, które sobie przeczą; WAY-01 każe, by po zamknięciu zadania fundament znów zgadzał się ze stanem obecnym.

### To do

1. Sekcja „3. Grade” w `task-cycle/review/SKILL.md`, po zdaniu „Something the plan or the task mandates is still a finding when it is a defect; name it so.” (`:94-95`), zyskuje zdanie, które każe ocenić jako Important uwagę, że zmiana odchodzi od wpisu fundamentu, który sama zapisuje albo zmienia (Q2) — gdy jej pliki robią coś, czego wpis zabrania, albo nie robią tego, czego wymaga, i gdy plik zmiany powtarza treść wpisu i mówi coś innego (Q1). Punktem wyjścia brzmienia jest zdanie z pierwszej wersji tej notatki, które mówi jeszcze tylko „writes”: „A finding that the change departs from an entry the same change writes into the foundation — in its code, or in a file that restates what the entry keeps in one place — is graded Important: the request would carry a foundation its own change contradicts.”

### Questions to settle

- Q1. Co liczy się jako niezgodność z wpisem: tylko kod, który robi coś, czego wpis zabrania albo nie robi tego, czego wymaga, czy także plik zmiany, który powtarza treść wpisu i mówi coś innego (szerzej, węziej, bez zastrzeżenia)?
  - Answer: obie sytuacje — pliki zmiany robią coś, czego wpis zabrania, albo nie robią tego, czego wymaga, oraz plik zmiany powtarza treść wpisu i mówi coś innego, szerzej albo bez zastrzeżenia; w PR #49 uwaga Minor 4 przeglądu kroku powrotu (przytoczenie faktu `single-rule-compliance` bez jego zakresu, `return-review-report.md:89-96` @ `fa5304f`) byłaby Important.
  - Not chosen:
    - tylko pliki, które robią inaczej niż wpis — powtórzenie mówiące inaczej niż wpis dalej może dostać Minor, a następny agent czyta skill, nie wpis, i robi to, co mówi wersja w skillu.
  - Source: Mariusz, 2026-10-29, „robimy A” — na pytanie z dwoma wariantami (A: obie sytuacje, B: tylko pierwsza) i kosztem każdego; słaby punkt A nazwany w pytaniu: zgubione zastrzeżenie blokuje tak samo jak sprzeczność.
- Q2. Które wpisy: tylko te, które zmiana zapisuje, czy te, które zapisuje albo zmienia?
  - Answer: te, które zmiana zapisuje albo zmienia — ten sam zakres, który recenzent sprawdza (`task-cycle/review/SKILL.md:64`) i który krok powrotu porównuje z kodem (WAY-11).
  - Not chosen:
    - tylko te, które zmiana zapisuje — przerobiony wpis, któremu zmiana przeczy, może dalej dostać Minor, a „writes” obok „writes or changes” dwa wiersze wyżej recenzent może czytać jako celowe wyłączenie wpisów zmienionych.
  - Source: Mariusz, 2026-10-29, „A” — na pytanie z dwoma wariantami (A: zapisuje albo zmienia, B: tylko zapisuje) i kosztem każdego; słaby punkt A nazwany w pytaniu: blokuje też stary rozjazd w nieruszonej części zmienionego wpisu, który krok powrotu i tak musi poprawić.
- Q3. Czy reguła oceniania dostaje wpis w rejestrze decyzji the-way, jak WAY-220 i WAY-221, i jaki?
  - Answer: nowa decyzja, jak WAY-220 i WAY-221, z *Relations* „derives from WAY-161”; WAY-161 zostaje bez zmiany.
  - Not chosen:
    - rozszerzenie WAY-161 — jej zdanie wiążące jest już długie, dopisanie zmienia znaczenie przyjętej decyzji i rozjeżdża się z tym, jak potraktowano WAY-220 i WAY-221.
    - bez wpisu, tylko zdanie w skillu — żaden wpis fundamentu go nie chroni: zmiana, która je wytnie, nie przeczy niczemu w rejestrze.
  - Source: Mariusz, 2026-10-29, „A” — na pytanie z trzema wariantami (A: nowa decyzja, B: rozszerzenie WAY-161, C: bez wpisu) i kosztem każdego; słaby punkt A nazwany w pytaniu: rejestr rośnie o wpis, którego treść to w praktyce jedno zdanie skilla z uzasadnieniem.
- Q4. Czy zadanie czeka na wytyczne samego the way, skoro the way nie ma katalogu `guidelines/`?
  - Answer: nie — zadanie idzie drogą z `agent-instructions/README.md`, jak zadania serii skilli; wybór wytycznych jest pusty, a zadanie zmienia jeden plik Markdown skilla.
  - Source: odpowiedź wspólna z `_zadania/zadanie_skille_the_way_3_fundament.md`, *Questions to settle*, pytanie 5: Mariusz, 2026-10-28, „tak” — na tę samą odpowiedź co w zadaniu 2 (`_zadania/zadanie_skille_the_way_2_refine_task.md`: Mariusz, 2026-10-28, „przyjmuję”), przeciw czekaniu na wytyczne samego the way.

## Context

- Źródło: sprawa AIR-542 z dziennego przeglądu warstwy AI (2026-10-29), z uwagi procesowej (1) zapisu cyklu `instruction-files-router` (the-way PR #49, @ `fa5304f`, `docs/task-cycles/instruction-files-router/cycle.md:137`).
- WAY-258 zapisał ten sam PR, w commicie `634fa3b`.
- Instrukcja recenzenta służy każdemu przeglądowi kodu w cyklu — odcinka planu, całej zmiany, commitów kroku powrotu, uzgodnienia z gałęzią docelową i poprawki po uwagach człowieka (WAY-162) — więc zdanie działa w każdym z nich.
- Ocena zostaje przy recenzencie: orkiestrator nie przesuwa uwagi między rodzajami (WAY-161, `task-cycle/skill/SKILL.md:326-328`).
- Rozjazdy, które krok powrotu znajduje sam, poprawia on niezależnie od tego, czy nazywa je też uwaga przeglądu; to zdanie stoi w zleceniu kroku powrotu cyklu `task-cycle-skills-shape` (the-way @ `eeb5b34`, `docs/task-cycles/task-cycle-skills-shape/reports/return-handoff.md:43`), nie w skillu.
- Zmiana `task-cycle/skill/return_step.md` odpadła: w PR #49 powtórzenia stworzył sam krok powrotu i znalazł je przegląd po nim, ocenił jako Minor, więc reguła kroku powrotu tego przypadku by nie domknęła.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

Brzmienie z `foundations/decisions.md` na `foundations` @ `d115159`.

- **WAY-161** — „Which findings of the review of the whole change are fixed, and how does the request carry the rest?” — nowa decyzja z niej wynika (Q3); zadanie jej nie zmienia: „In the review of the whole change on either route, a finding blocks when the reviewer grades it Critical or Important and has not itself marked it as outside the task's scope, and a review that leaves no blocking finding sends the change to its request without a fix. A finding the reviewer has marked as outside the task's scope — a line of its list of what it declined to judge, or a finding it describes as going beyond the task — is not fixed, whatever its grade, nor is a Minor finding, and the request lists those findings in an item of their own and the Minor findings in another, each with the reviewer's words and its place in the code, while the human decides which findings outside the scope become new tasks and creates them. The orchestrator moves no finding from one of these kinds to another.”
- **WAY-162** — „How does a code review of a task's change end when its findings block?” — zakres przeglądów, w których nowa ocena działa; fragment: „In every code review of a task's cycle — of a slice of its plan, of the whole change, of the return step's commits, of the reconciliation with the target branch and of a change made for the human's remarks on the request — the findings that block, as WAY-161 grades them, get one fix and one review of that fix”.
- **WAY-220** — „How does a code reviewer grade a finding about appearance?” — wzór reguły oceniania z własną decyzją: „A code reviewer grades a finding about appearance by its concrete effect on the user, within the review's existing severity scale, rather than treating it as Minor merely because it concerns appearance; the reviewer retains the grade and scope decisions WAY-161 assigns it.”
- **WAY-221** — „When can departure from a guideline example support a blocking finding?” — drugi wzór; zastrzega, że wiążące reguły zachowują moc: „Departure from an example in product guidelines or from the part of an exemplar no script checks is not by itself grounds for a blocking review finding: the reviewer names the consequence for the user or for code correctness that warrants the blocking grade under WAY-161. Binding rules and their invariants retain their force, and this criterion gives the orchestrator no authority to regrade or discard a reviewer's finding.”
- **WAY-01** — „What state does the foundation describe?” — uzasadnienie oceny; fragment: „On the main branch, the foundation describes the product as it is […] When a task closes, the foundation again matches the current state.”
- **WAY-11** — „How does a task end?” — zakres wpisów z Q2; fragment: „A task ends with its return step before its branch is merged: an agent compares with the code the foundation entries the change writes or changes, those its task names and those the search of the foundation found, and the part map of the parts the task touched, and corrects in the same change whatever no longer matches.”

## Settlements to record

Candidates: 2 shown, 1 accepted — 2026-10-29

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Uwagę, że zmiana odchodzi od wpisu fundamentu, który sama zapisuje albo zmienia — jej pliki robią coś, czego wpis zabrania, albo nie robią tego, czego wymaga, albo plik zmiany powtarza treść wpisu i mówi coś innego — recenzent ocenia jako Important; stoi to w nowej decyzji, wynikającej z WAY-161, a WAY-161 zostaje bez zmiany. | decision | Q1, Q2, Q3; *To do* 1; przyjęty: Mariusz, 2026-10-29, „Przyjmuję” | czy pisać decyzję, rozszerzać WAY-161, czy zostawić samo zdanie w skillu; czy blokuje powtórzenie, które mówi inaczej niż wpis; czy reguła obejmuje wpisy zmienione, czy tylko nowe |

## Out of scope

- Zmiana `task-cycle/skill/return_step.md`.
- Zmiana reguły, że uwag Minor się nie poprawia (WAY-161).

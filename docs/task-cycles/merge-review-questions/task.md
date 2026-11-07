---
title: "the way: zlecenie przeglądu scalenia pyta, czy obie strony nadal do siebie pasują, i nazywa decyzje przyniesione przez scalenie"
status: draft
created: 2026-11-02T13:20
updated: 2026-11-06
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# the way: zlecenie przeglądu scalenia pyta, czy obie strony nadal do siebie pasują, i nazywa decyzje przyniesione przez scalenie

Status: ready for cycle
Project relation: independent

## Description

### Need

- Tuż przed PR-em cykl zadania dociąga najnowszą gałąź główną; jeśli to zmienia przeglądany kod, świeży agent ogląda scalenie, ale instrukcja nie mówi, czego ma tam szukać, więc wszystko zależy od pytań, które postawi agent prowadzący cykl.
- Odczuwa to Mariusz przy PR-ze, gdy zmiana łamie ustalenie albo kod, które dopiero co weszły na gałąź główną z innego zadania.
- Prowadzący zwykle sami pytają o to dobrze, więc najczęściej nic się nie stanie; gdy nikt nie zapyta, PR będzie sprzeczny z tym, co właśnie stanęło na gałęzi głównej, a automat tego nie wykryje.
- Krok powrotu, czyli końcowe porównanie wpisów z kodem, odsyła termin użyty niezgodnie ze słownikiem do narzędzia `record-glossary-term`, które takiego przypadku nie zna; wpisu tu nie trzeba, wystarczy poprawić użycie.
- Po odrzuceniu specu projektant poprawia go w tym samym pliku poza gitem, więc recenzent poprawki nie ma starej wersji i porównuje z pamięci; kopia oszczędza mu pracę, choć nowych znalezisk nie daje, bo recenzenci wykrywali szkody poprawki także bez starej wersji.

### To do

Numery linii odpowiadają stanowi `origin/foundations` @ `dfd50e5`.

1. W kroku 12 cyklu zadania, `task-cycle/skill/SKILL.md:389-391`, zdanie o scaleniu ma brzmieć:
   > Otherwise merge the current target branch into the task branch; where that changes the reviewed code, have a fresh reviewer review the merge with `review-change`, with a dispatch that asks whether the two sides still hold together and names the foundation entries the merge brought in that bear on the parts the change touches (WAY-150), and have the agents that own the affected checks run them.
2. W kroku powrotu, `task-cycle/skill/return_step.md:10-11`, fragment „a word the change uses in a meaning for which WAY-95 gives it an entry, or a term used against its entry, through `record-glossary-term`;” ma brzmieć:
   > a word the change uses in a meaning for which WAY-95 gives it an entry, through `record-glossary-term`;

   a na końcu tego akapitu dochodzi zdanie:
   > A term used against its entry takes the use corrected and no entry.
3. W `task-cycle/skill/spec_review.md:6-7` zdanie „On `FAIL` the designer revises the spec once and the reviewer reviews the revision once.” ma brzmieć:
   > On `FAIL` keep the spec as `spec-reviewed.md` beside it; the designer revises the spec once and the reviewer reviews the revision once, comparing the two.
4. Metoda recenzenta specu wie o kopii z punktu 3:
   - w `task-cycle/spec/SKILL.md:18-19` punkt o zleceniu ma brzmieć:
     > The dispatch: whether you write or review, the open choice the cycle found, the spec path — normally `.runs/task-cycles/<task-slug>/spec.md` —, for the review of a revision also the spec as reviewed, `spec-reviewed.md` beside it, and the report path.
   - w `task-cycle/spec/review.md:18-20` zdanie o przeglądzie poprawionego specu ma brzmieć:
     > For the review of a revised spec, compare it with the spec as reviewed, say for each earlier finding whether it is resolved, and report only what the revision broke besides.

### Questions to settle

- Pytanie 1: jak ma brzmieć poprawka kroku powrotu, skoro PR #75 (`3177e10`) zmienił zdanie, które zadanie cytowało?
  - Answer: zostaje brzmienie z PR #75, a wypada z niego tylko wtrącenie „or a term used against its entry”; zdanie dopisywane na końcu akapitu bez zmian (*To do* 2). WAY-11 nie wymienia terminu użytego wbrew wpisowi i każe poprawić to, co nie zgadza się z kodem, więc poprawka wyrównuje skill do decyzji.
  - Not chosen:
    - podmiana dosłownie według pierwotnego zadania („in a meaning other than the usual one”) — cofa brzmienie z PR #75
  - Source: Mariusz, 2026-11-06, „zgadzam się na Twoje rekomendacje”; `task-cycle/skill/return_step.md:10-11` @ `dfd50e5`; WAY-11, `foundations/decisions.md` @ `dfd50e5`.
- Pytanie 2: co z akapitem o trzech pytaniach słownika, które „celowo zostały bez reguły”, skoro PR #75 rozstrzygnął część z nich?
  - Answer: akapit wypada z zadania. Po PR #75 WAY-104 dookreśla słowo procesu tam, gdzie zdanie fundamentu — także stare — da się przeczytać w drugim znaczeniu, a szablon słownika rozstrzyga dwa znaczenia testem zdania; o polu *Not* przy nowym słowie szablon mówił już wcześniej.
  - Not chosen:
    - akapit zostaje — cykl czyta, że pytania są celowo otwarte, i może przez to zgłosić uwagę albo potraktować je jak otwarte
  - Source: Mariusz, 2026-11-06, „zgadzam się na Twoje rekomendacje”; WAY-104 i `elements/glossary/template.md:59-61`, `:84-90` @ `dfd50e5`.
- Pytanie 3: czy metoda recenzenta specu ma wiedzieć o kopii `spec-reviewed.md`?
  - Answer: tak, dwa dopiski z *To do* 4. Zdanie z *To do* 3 stoi w pliku prowadzącego cykl, a recenzent czyta własną metodę; bez dopisków porównanie zależy od tego, czy prowadzący wpisze ścieżkę kopii w zlecenie.
  - Not chosen:
    - bez dopisków — świeży recenzent może czytać spec od nowa, jak w `logging-guidelines`; bez szkody, ale oszczędność pracy, dla której jest kopia, przestaje być pewna
  - Source: Mariusz, 2026-11-06, „zgadzam się na Twoje rekomendacje”; `task-cycle/spec/SKILL.md:18-19`, `task-cycle/spec/review.md:18-20` @ `dfd50e5`.

## Context

- Źródło: sprawy AIR-570 (przegląd scalenia), AIR-574 (krok powrotu) i AIR-575 (kopia specu) z przeglądu warstwy AI, 2026-11-02, w `C:\Storage\The Brain\The Brain\Notes\Areas\(A) Claude code\ai_review_ledger.md`; po 14 dniach od zamknięcia przechodzą do `ai_review_ledger_archive.md` w tym samym katalogu.
- W zapisach cykli jest 17 przeglądów scalenia w 14 cyklach, a 2 skończyły się oceną `FAIL`: w `unsettled-technology-returns` (the-way, PR #63) zmiana łamała decyzję WAY-265, która weszła ze scaleniem, a w `zapis-stanu-na-serwerze` (`loop2`) błąd leżał w kodzie, nie w dokumentach; dlatego zdanie z *To do* 1 ma dwie części: pytanie o to, czy obie strony do siebie pasują, i nazwanie wpisów.
- Wybór wpisów przez samego recenzenta scalenia odpadł: WAY-150 daje własny wybór lektury tylko recenzentowi całej zmiany, `task-cycle/review/SKILL.md:29-33` mówi to samo, a przy dużym scaleniu lista objęłaby też wpisy niedotyczące zmiany; dlatego `task-cycle/review/SKILL.md` zostaje bez zmian.
- Pytanie, czy scalenie zmieniło coś poza konfliktami, odpadło: przenumerowanie decyzji jest właśnie taką zmianą, a pada w 13 z 17 raportów tych przeglądów, więc dawałoby fałszywy alarm.
- Zdanie dla projektanta, żeby przy poprawce specu zmieniał tylko to, o co proszą uwagi, odpadło, bo gryzie się z obowiązkiem usuwania sprzeczności z `task-cycle/spec/design.md` (AIR-575).
- Zadanie powstało przy stanie `f45ca40`; od tego czasu krok 12 przesunął się z linii 373-375 na 389-391 bez zmiany treści, a zdanie kroku powrotu zmienił PR #75.
- Spec leży w `.runs/task-cycles/<task-slug>/spec.md` (`task-cycle/skill/SKILL.md:238`), a przy PR-ze cały ten katalog jest kopiowany do `docs/task-cycles/<task-slug>/` (`task-cycle/record_template.md:87-89`), więc kopia `spec-reviewed.md` trafi do zapisu cyklu bez osobnego kroku.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-150 — „[…] Outside the task cycle the agent doing the work selects its own reading, while in the task cycle the orchestrator selects for its own judgments and for each handoff, which names the foundation entries by identifier; the reviewer of the whole change selects for its own review, and an agent writing a foundation entry through an element's skill for the entry it writes; and every other agent of the cycle reads what its handoff names and reaches for what is missing selectively […]” (`foundations/decisions.md`, @ `dfd50e5`). *To do* 1 każe orkiestratorowi nazwać w zleceniu wpisy przyniesione przez scalenie, zgodnie z tym podziałem.
- WAY-162 — „In every code review of a task's cycle — of a slice of its plan, of the whole change, of the return step's commits, of the reconciliation with the target branch and of a change made for the human's remarks on the request — the findings that block, as WAY-161 grades them, get one fix and one review of that fix […]” — przegląd scalenia kończy się tak jak dotąd.
- WAY-11 — „A task ends with its return step before its branch is merged: an agent compares with the code the foundation entries the change writes or changes, those its task names and those the search of the foundation found, and the part map of the parts the task touched, and corrects in the same change whatever no longer matches. In the same change it writes the sources outside the product that the change rests on and the foundation does not yet hold, as environment facts, a word the change uses in a meaning for which WAY-95 gives it an entry, as a glossary term, and the accepted settlements (WAY-134) and projected entries (WAY-126) the task carries that are not yet written. […]” — decyzja nie wymienia terminu użytego wbrew wpisowi; poprawka *To do* 2 wyrównuje skill do niej.
- WAY-135 — „A task's cycle writes a spec, reviewed by an agent other than its author, before implementation and any plan where the task leaves an open design choice and nowhere else […]” — *To do* 3 dotyczy jednej rundy poprawki tego specu.

## Settlements to record

Candidates: 2 shown, 2 accepted — 2026-11-06

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Gdy scalenie gałęzi docelowej zmienia przeglądany kod, zlecenie przeglądu scalenia pyta, czy obie strony nadal do siebie pasują, i nazywa wpisy fundamentu przyniesione przez scalenie, które dotyczą części ruszanych przez zmianę; wpisy wybiera prowadzący cykl, nie recenzent. | decision | *To do* 1; odrzucone warianty: *Context* (wybór wpisów przez recenzenta, pytanie „poza konfliktami”). Pytanie przeciw odpowiedzi — zakotwiczenie w rachunku AIR-570: „Co może pęknąć: recenzent może zacząć oceniać całą zmianę od nowa; granicę trzyma „what the merge brought in””; czy szerokie pytanie zostaje mimo tego ryzyka: Mariusz, 2026-11-06, „to zostawmy”. Granicą przeglądu jest zakres commitów scalenia, który recenzent dostaje w zleceniu (`task-cycle/review/SKILL.md:20-22` @ `dfd50e5`) — do uzasadnienia decyzji. Odrzucone: węższe pytanie „whether the change still holds against what the merge brought in” — nie zmniejsza kodu do czytania, a słabiej obejmuje błąd na styku obu stron, jak I-1 w `loop2` `docs/task-cycles/zapis-stanu-na-serwerze/reports/37-reconcile-review-report.md` @ `b37cc67` (wczytywanie zapisu z gałęzi zadania odrzucało stan, który tworzył kod zadania 13 z gałęzi głównej); przegapiony błąd kosztuje korektę po PR-ze, a nadmiarowa uwaga najwyżej jedną rundę poprawki (WAY-162). | czy reguła zostaje tylko w tekście skilla, czy idzie do dziennika jako nowa decyzja albo dopisek do WAY-162, i co wpisać w jej *Rejected* |
| 2 | Po odrzuceniu specu jego przejrzana wersja zostaje obok jako `spec-reviewed.md`, a recenzent poprawki porównuje obie wersje. | decision | *To do* 3 i 4, pytanie 3; odrzucony wariant: *Context* (zdanie „zmieniaj tylko to, o co proszą uwagi”) | czy reguła zostaje tylko w tekście skilla, czy idzie do dziennika obok WAY-135, i co wpisać w jej *Rejected* |

## Out of scope

- Zmiana `task-cycle/review/SKILL.md` (zob. *Context*).

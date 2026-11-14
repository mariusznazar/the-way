---
title: "the way: uwaga o strukturze kodu w produkcie, którego wytyczne powstały przed regułą rozmiaru — domknąć zdanie skilla przeglądu i WAY-363"
status: draft
created: 2026-11-13T20:44
updated: 2026-11-13
tags: [the-way, zadanie]
related: "the project note in the author's vault"
---

# the way: uwaga o strukturze kodu w produkcie, którego wytyczne powstały przed regułą rozmiaru — domknąć zdanie skilla przeglądu i WAY-363

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Przegląd całej zmiany ocenia, co zmiana zostawia w strukturze kodu — na przykład czy funkcja urosła — a uwaga o strukturze ma być drobna (Minor) w każdym produkcie, który nie ma reguły rozmiaru funkcji i pliku (uwaga Mariusza do prośby o scalenie nr 109).
- Zdanie o stopniu takich uwag w sekcji 3 skilla recenzenta i zdanie wiążące WAY-363 wymieniają, między myślnikami, tylko dwa takie produkty: ten, który odstąpił od reguły decyzją z powodem, i ten, który nie ma wytycznych kodowania wcale (jak samo the way).
- Pomijają trzeci: produkt, który ma wytyczne kodowania napisane, zanim reguła rozmiaru istniała — tak stoi gra aż do własnego zadania przyjęcia reguły.
- Dłuższy zapis zasad przeglądu całej zmiany (`task-cycle/review/whole_change.md`) ten trzeci przypadek obejmuje, więc dwa miejsca mówią dziś nie to samo.
- Recenzent zmiany w takim produkcie może dać tej samej uwadze o rozroście funkcji stopień Minor (za dłuższym zapisem) albo Important (za krótkim zdaniem i decyzją) i zablokować zmianę, kosztując rundę poprawek i drugi przegląd — to ta losowość stopnia, którą WAY-363 miał usunąć.
- Dziś nic się nie psuje: zmian w grze według tej reguły nikt jeszcze nie przegląda; luka wyjdzie przy pierwszym przeglądzie zmiany w produkcie z wytycznymi sprzed reguły.

### To do

1. Zdanie o stopniu uwag o strukturze kodu w sekcji `## 3. Grade` pliku `task-cycle/review/SKILL.md` — to, które zaczyna się od „A finding about the structure of code that lies below the threshold of the rule of size” (około linii 126) — mówi, że uwaga o strukturze jest Minor wszędzie tam, gdzie produkt nie ma reguły rozmiaru, a wymienione przypadki podaje jako przykłady, nie zamkniętą listę; wśród przykładów stoi produkt, którego wytyczne kodowania nie mają jeszcze tej reguły.
2. Zdanie wiążące decyzji WAY-363 w `foundations/decisions.md` (pod nagłówkiem „### WAY-363 — How does a reviewer grade a finding about the structure of code?”, około linii 12095) mówi to samo co zdanie z punktu 1; decyzję zmienia się w miejscu (WAY-07).
3. *Verification*, *Rationale* i *Rejected* WAY-363 nie wskazują na stary, węższy zakres dwóch przypadków.
4. Linie wpisu WAY-363 są zawinięte jak reszta dziennika decyzji — także zdanie w *Rationale*, które zaczyna się od „The reviewer still judges the scope of each finding” i dziś stoi w linii o długości 163 znaków (uwaga C2 tego samego przeglądu).

### Acceptance criteria

- Zdanie z punktu 1, zdanie wiążące WAY-363 i ostatni punkt sekcji „## The structure of the code the change leaves” w `task-cycle/review/whole_change.md` (ten, który zaczyna się od „the functions and files over a threshold”) dają recenzentowi ten sam stopień w każdym z trzech przypadków produktu bez reguły rozmiaru.

## Context

- Lukę znalazł przegląd poprawki nr 1 w cyklu prośby nr 109, uwaga C1 w raporcie `reports/review-correction-1-report.md` rekordu cyklu `docs/task-cycles/review-structure-form-class/` w commicie `7965305`; katalogu nie ma w ostatecznym drzewie, czyta się go przez ten commit.
- Recenzent ocenił C1 jako Minor, bo ostatni punkt sekcji o strukturze w `whole_change.md` („Where that heading holds `none —`, or the product's guidelines hold no such rule, there is no such test, the first numbers and the diff are your material, and a finding of structure is Minor (WAY-363).”) już obejmuje trzeci przypadek i może posłużyć za wzór.
- Zdanie z myślnikami powtarza słowo w słowo uwagę Mariusza z poprawki nr 1 („one that departed from the rule with a reason, or one with no coding guidelines at all”), dlatego recenzent zostawił jej rozstrzygnięcie Mariuszowi.
- Produkt z wytycznymi bez nagłówka `### Size of a function and a file` i bez decyzji o odstąpieniu łamie WAY-360 („a product leaves the heading out with no decision”), więc trzeci przypadek to stan przejściowy do odświeżenia albo rozszerzenia wytycznych — ale realny, dopóki gra nie przyjmie reguły.
- Pozostałe miejsca, które mówią o produkcie bez reguły rozmiaru, już używają ogólnego sformułowania i nie wymagają zmiany: `task-cycle/plan/SKILL.md` (około linii 182), `task-cycle/change/SKILL.md` (około linii 56), `product-guidelines/coding/settle.md` (około linii 89).
- Zmiana dotyka tylko tekstu skilla i wpisu dziennika decyzji; nie zmienia kodu, testów ani interfejsu, więc nie ma wytycznych do przeczytania (the way nie ma wytycznych kodowania, WAY-328).

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-363** — zadanie zmienia jej zdanie wiążące tak, by obejmowało każdy produkt bez reguły rozmiaru, a wymienione przypadki podawało jako przykłady. Obecne brzmienie: „A reviewer grades as Minor a finding about the structure of code that lies below the threshold of the rule of size in the product's coding guidelines, and one in a product that has no rule of size — it departed from the rule by a decision, or has no coding guidelines at all — and judges its scope as for any finding (WAY-161). A finding about a function or a file over a threshold is graded as any other finding.”
- **WAY-362** — źródło brzmienia dłuższego zapisu w `whole_change.md`, z którym zdanie ma się zgadzać: „The reviewer of the whole change judges what the change leaves in the structure of the code: the growth of a function or a file, code that has no user after the change, and a name that stopped being true. It takes its numbers from a script of the-way that gives, for the range of the change, the lines of each changed file before the change and after it, and from the test of the product's rule of size (WAY-361), run on the state before the change and on the state after it.”
- **WAY-360** — określa, kiedy produkt nie ma reguły rozmiaru: „A product sets its thresholds after a trial run on its existing code and writes its exceptions in its decision on the rule, or departs from the rule only by a decision of its log that gives the reason (WAY-173), and a product that already has coding guidelines gets the rule by an ordinary extension, as WAY-278 gives it for the rules on failures and logs.”

## Settlements to record

Candidates: 2 shown, 0 accepted — 2026-11-13

none

## Out of scope

- Inne stopnie uwag i inne reguły przeglądu — zadanie tylko domyka listę przypadków produktu bez reguły rozmiaru.
- Zdanie w *Rejected* WAY-360 o „the same chance in the grade” — osobna uwaga z tego samego przeglądu.
- Przyjęcie reguły rozmiaru w grze — osobne zadanie w backlogu gry.

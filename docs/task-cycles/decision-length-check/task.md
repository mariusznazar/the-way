---
title: "the way: przywrócić skrypt pilnujący długości zapisanych decyzji"
status: draft
created: 2026-11-20T10:11
updated: 2026-11-20
tags: [zadanie]
related: "the author's project note"
---

# the way: przywrócić skrypt pilnujący długości zapisanych decyzji

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Każda zapisana decyzja — w the way i w produkcie, który z niego korzysta — ma odpowiadać na swoje pytanie najwyżej trzema zdaniami w akapicie; tak mówi szablon decyzji i decyzja WAY-05.
- Od 22.10.2026 nie sprawdza tego żaden skrypt: licznik zdań zniknął razem ze skryptami sprawdzającymi formę wpisów, a ograniczenie długości w słowach zdjęto wcześniej z założeniem, że licznik zostaje.
- Recenzenci liczą zdania ręcznie i przepuszczają: wpis WAY-344 urósł z 4 do 8 zdań w trzech kolejnych zmianach bez jednej uwagi, a WAY-405 powstał od razu z pięcioma.
- Odczuwają to Mariusz i agenci, którzy czytają dziennik decyzji, bo wpisy robią się coraz dłuższe; recenzenci, którzy liczą zdania ręcznie; autor zmiany, który dostaje uwagę za cudzy, starszy wpis.
- Bez zmiany wpisy rosną dalej, a pierwsza zmiana, która trafi na uważnego recenzenta, dostaje przy okazji przebudowę długiego wpisu, którego nie pisała.

### To do

1. `elements/common/foundation_check.py` sprawdza długość zdań wiążących każdej decyzji, którą zmiana dodaje albo której zdania wiążące zmienia, osobno w każdym akapicie zdań wiążących: akapit ma najwyżej 3 zdania i najwyżej 300 słów, a przekroczenie jest błędem, który nazywa decyzję, akapit i przekroczoną miarę z jej wartością; każdy inny wpis ponad limit skrypt wypisuje linią `listed:`. Dla tej kontroli decyzja liczy się jako zmieniona także wtedy, gdy zmiana inaczej dzieli jej zdania wiążące na akapity, bez zmiany słów.
2. Zdanie liczy się tak, jak skrypt już je wyznacza dla linii `decision:` testu: zaczyna się na początku akapitu albo po kropce i spacji, a kropka wewnątrz cudzysłowu zdania nie kończy; słowo to ciąg znaków między odstępami, tak jak skrypt liczy słowa cytatu w linii `decision:`.
3. Opis tego, co skrypt zgłasza, dostaje nową kontrolę wszędzie, gdzie stoi: w opisie na początku `foundation_check.py`, w `agent-instructions/README.md` w sekcji „The form of the foundation”, w `README.md` w zdaniu, które otwiera „`elements/common/foundation_check.py` checks that every identifier stands once”, i w `elements/decisions/template.md` w tabeli „Fields and their readers”, w wierszu „binding sentences”.
4. `elements/decisions/template.md` podaje limit słów obok liczby zdań: w sekcji „Binding sentences”, w punkcie, który otwiera „One to three sentences answer the question of the heading” (ok. linii 132–134), i w bloku wzoru wpisu w sekcji „Decision entry”, w wierszach „<1–3 binding sentences that answer the question>” i „<1–3 binding sentences for a part of another question this entry answers…>” (ok. linii 29–32).
5. Ta sama sekcja „Binding sentences” dostaje po tym punkcie zdanie, że oba limity liczy `foundation_check.py` w każdej decyzji, którą zmiana dodaje albo której zdania wiążące zmienia, więc starszy wpis ponad limit spełnia je, gdy zmiana go następnym razem zmieni, oraz że zdania liczy tak, jak punkt o linii `decision:` w sekcji „Verification” wyznacza początek zdania.
6. WAY-05 zmienia się tak, jak podaje „Decisions in play”; test nowej kontroli trzyma jej zdania linią `decision:`, a jej *Verification* dostaje klauzulę `tests:` i traci z pary przykładów „For the binding sentences” to, co test trzyma.

### Questions to settle

- Czym mierzyć długość: zdaniami, słowami czy jednym i drugim?
  - Answer: jednym i drugim — akapit zdań wiążących ma najwyżej 3 zdania i najwyżej 300 słów; zmienia to WAY-05, która dostaje limit słów obok liczby zdań.
  - Not chosen:
    - tylko zdania, najwyżej 3 w akapicie — wpis ponad limit najłatwiej naprawić sklejeniem zdań, więc długość w słowach rośnie dalej (WAY-134 mieści 478 słów w trzech zdaniach)
    - tylko słowa, limit słów zamiast liczby zdań — wypada reguła, której WAY-05 wprost broni, odrzucając wariant bez liczby zdań
    - jedno i drugie z progiem 200 słów — do przebudowy przy najbliższym dotknięciu jest 30 akapitów w the way i 45 w loop2, czyli co dziesiąty wpis staje się dokładką do cudzej zmiany
  - Source: Mariusz, 2026-11-20, „1. c z progiem 300 słów”
- Błąd czy linia `listed:`: czy przekroczenie w decyzji, którą zmiana dodaje albo zmienia, zatrzymuje zmianę, i co skrypt robi ze starszymi wpisami ponad limit?
  - Answer: przekroczenie w decyzji, którą zmiana dodaje albo której zdania wiążące zmienia, jest błędem; każdy inny wpis ponad limit skrypt wypisuje linią `listed:`, która niczego nie zatrzymuje. Na próbę: Mariusz wycofa się z błędu, jeśli będzie bardzo przeszkadzać.
  - Not chosen:
    - błąd tylko wtedy, gdy zmiana dodaje wpis ponad limit albo wydłuża wpis, który już był ponad — wpisy ponad limit mogą zostać długie na zawsze, reguła jest trudniejsza do wytłumaczenia, a skrypt bardziej złożony
    - tylko linie `listed:`, bez błędu — takie linie przeszły w requestach #132, #137 i #138 bez reakcji, więc długość dalej nie byłaby pilnowana
  - Source: Mariusz, 2026-11-20, „spróbujmy a, najwyżej się z tego wycofam jak będzie bardzo przeszkadzać”
- Gdzie poprawić 12 wpisów the way, które już dziś stoją ponad limit?
  - Answer: osobnym zadaniem the way, zaraz po tym; wpisy loop2 dostają własne zadanie w loop2.
  - Not chosen:
    - w tym zadaniu — jeden request miesza skrypt z przepisaniem zdań wiążących 12 zatwierdzonych decyzji, spór o jedno brzmienie blokuje całość, a pytania o podział wpisów takich jak WAY-344 weszłyby do tego doprecyzowania
    - wcale, każdy wpis poprawia ten, kto go dotknie — to dolegliwość, od której zadanie się zaczęło, tylko wymuszona przez skrypt
  - Source: Mariusz, 2026-11-20, „2. ok b, ale to od razu jak skończymy doprecyzowanie tego zadania to parkujemy dwa zadania, jedno dla the way, drugie dla loop2”
- Czy inny podział zdań wiążących na akapity, bez zmiany słów, liczy się przy kontroli długości jako zmiana decyzji?
  - Answer: tak — decyzja liczy się jako zmieniona także wtedy, gdy zmiana inaczej dzieli jej zdania wiążące na akapity.
  - Not chosen:
    - nie, zmianą jest tylko zmiana słów, jak przy sprawdzaniu, czy decyzję coś trzyma — sklejenie dwóch akapitów w jeden za długi, bez zmiany słów, daje tylko linię `listed:`, nie błąd
  - Source: Mariusz, 2026-11-20, „1. a”
- Jak kontrola wyznacza koniec zdania?
  - Answer: tak samo, jak szablon wyznacza początek zdania dla linii `decision:`, bez drugiej definicji.
  - Source: `elements/decisions/template.md:256-259` @ 1b6fe1c1 — „begins at the start of a sentence of the entry's binding sentences — the start of them, the start of one of their paragraphs, or the first word after a full stop and a space, the full stop not standing inside a passage between quotation marks, `"…"`, `“…”` or `„…”`, which is no end of a sentence”

## Context

- Źródłem zadania jest sprawa AIR-688 z nocnego przeglądu warstwy AI, przyjęta przez Mariusza 2026-11-20 w kształcie po krytyce; zeszyt `the author's notebook of the review of the AI layer`, po 14 dniach archiwum `ai_review_ledger_archive.md`.
- Stan sprawdzony 2026-11-20 na `foundations` @ 1b6fe1c1; numery linii są tylko podpowiedzią obok cytatu.
- Reguła stoi w `elements/decisions/template.md`, sekcja „Binding sentences”: „One to three sentences answer the question of the heading, in the first paragraph under it. A part of another question that the entry answers (WAY-19) has its own paragraph after that one, also of one to three sentences, one paragraph for each part (WAY-05).”
- `elements/common/foundation_check.py` nie liczy dziś zdań nigdzie; liczy tylko słowa cytatu w linii `decision:` testu („the quotation has fewer than three words”).
- Licznik zdań (`count_sentences`) i niezmiennik `binding-sentence-count/1` stały w `elements/decisions/format_guard.py`; widać je w `git show 80ba8c52^:elements/decisions/format_guard.py`.
- Commit 597edecc (2026-10-22, pozycja P12 planu odchudzania) usunął skrypty sprawdzające formę wpisów i wycofał ich niezmienniki, ale skrypt decyzji zostawił, bo `product-guidelines/form_check.py` ładował go jako bibliotekę.
- Commit 80ba8c52 (ten sam dzień) usunął `form_check.py`, a z nim trzy skrypty, które żyły już tylko jako jego biblioteka; liczenia zdań nikt nie przeniósł do `foundation_check.py`.
- Plan odchudzania zdjął budżet 600 słów na wpis i próg 80 słów zdań wiążących z zastrzeżeniem „liczbę zdań 1–3 pilnuje strażnik” — `the verdicts note of the author's plan of slimming the process:414` (wiersz F12).
- `Defect introduced by: none`: usunięcie skryptów sprawdzających formę było treścią pozycji P12 planu odchudzania, a niezmiennik liczby zdań wycofano w tym samym commicie jawnie; plan nie przewidział, że limit zostanie bez niczego, co go pilnuje, więc to luka tamtego zadania, nie defekt wobec tego, czego wymagało.
- Pomiar na the way @ 1b6fe1c1 (2026-11-20, licznik według definicji z punktu 2 „To do”): 236 wpisów, 281 akapitów zdań wiążących; ponad trzy zdania mają 2 akapity — WAY-344 (8 zdań, 743 słowa) i WAY-405 (5 zdań, 343 słowa); fałszywych alarmów nie ma.
- Długość zdań w the way: 638 zdań, mediana 46 słów, 201 zdań ponad 60 słów, 49 ponad 100, 10 ponad 150; akapit ma medianę 100 słów, 80 akapitów ma ponad 150 słów, 30 ponad 200, 17 ponad 250, 12 ponad 300, 3 ponad 400; WAY-134 mieści 478 słów w trzech zdaniach.
- Pomiar na loop2 @ 77a612cb, produkcie korzystającym z the way: 428 wpisów, 453 akapity; ponad trzy zdania ma 13 akapitów; 80 akapitów ma ponad 150 słów, 45 ponad 200, 23 ponad 250, 11 ponad 300, 3 ponad 400.
- Ponad limit 3 zdań albo 300 słów w akapicie stoi dziś 12 wpisów the way (WAY-134, 136, 139, 148, 150, 154, 256, 287, 289, 339, 344, 405) i 20 wpisów loop2.
- Limit dotyczy akapitu, a liczby akapitów skrypt nie ogranicza; to, czy akapit jest osobną częścią pytania, ocenia recenzent zmiany.
- Dawny licznik z `format_guard.py` uznawał koniec zdania tylko przed wielką literą, cudzysłowem `"` albo nawiasem; na loop2 różni się od definicji z punktu 2 w 32 akapitach i w sprawdzonych przypadkach to on się myli (zdanie zaczynające się od `*Purpose*` albo od „Zablokuj”).
- Kropka wewnątrz odwrotnych apostrofów (np. `template.md`) nie zmienia dziś liczby zdań w żadnym akapicie the way.
- WAY-344 rósł 4 → 6 → 7 → 8 zdań w requestach #132, #137 i #138 (15–16.11.2026), WAY-405 powstał z 5 zdaniami w #138; w opisach tych requestów nie ma uwagi o długości; w #151 dwa wpisy z chwilowymi 4 zdaniami złapano i poprawiono.
- Request #121: dwa wpisy z 5 i 4 zdaniami, poprawka rozbiła akapity na dwa bez zmiany zdań; request #120: recenzent liczył zdania ręcznie („It is enforced by review only”).
- Miejsca w kodzie: akapity zdań wiążących wybiera `binding()`, początek zdania wyznacza `begins_sentence()`, zdania wiążące z commitu, od którego gałąź odeszła, daje `base_sentences()`, a wzór „błąd dla decyzji dodanej albo zmienionej, linia `listed:` dla pozostałych” stoi w `check_held` — wszystko w `elements/common/foundation_check.py`.
- `check_held` porównuje zdania wiążące z bazą po sklejeniu akapitów w jeden tekst, więc sam inny podział na akapity nie jest dla niej zmianą; sprawdzanie, czy decyzję coś trzyma (WAY-12), zostaje przy tym porównaniu.
- Nazwy z `foundation_check.py` importują `elements/common/decision_index.py` i `elements/part-map/test_cross_part_imports.py`, a sam skrypt importuje moduł `elements/common/foundation_source.py`.
- Słowa w pomiarach wyżej liczone są jako ciągi znaków między odstępami; przy takim liczeniu WAY-256 ma 301 słów.
- Sprawdzenie fundamentu działa też w produkcie: produkt dostaje nową kontrolę, gdy przesunie przypiętą wersję the way.
- Rozważone przy przyjęciu sprawy i odrzucone: zadanie zbiorcze z innymi poprawkami skryptów the way (nie było czego dołożyć); request #75 jako trzecie wystąpienie (związku z długością nie potwierdzono).

## Questions carried to cycle

- `elements/common/foundation_check.py` ma 1141 linii przy limicie 1200 linii pliku skryptu (WAY-385); czy nowa kontrola mieści się w pliku, czy zmiana zaczyna od wydzielenia części do osobnego modułu.

## Human actions

none

## Decisions in play

- **WAY-05 — How is a decision entry written?** — zmieniana: „A decision entry opens with one to three binding sentences that answer its question — in the present tense, describing a state that is to be true, concrete enough to check — and one paragraph of one to three binding sentences for each part of another question that it answers, followed by fields a script or an agent reads, then rationale and rejected options in prose, which, where the entry's author writes it rather than quotes a source, names no file, script or count — a count being how many files, tests or entries of its foundation the product holds; a measurement the choice rests on may stand, with what was measured and under which conditions, never as a general bound — nor what the process's own tools do or lack today, and does not tell how the decision was reached. A field stays in the template only while someone or something reads it, and what a decision forces on later work stands in a binding sentence or a field, never in prose. An example in `elements/decisions/` names a decision of the log by its number instead of copying it.” Zmiana: (1) każdy akapit zdań wiążących ma też najwyżej 300 słów; (2) decyzja mówi, że sprawdzenie fundamentu zgłasza jako błąd akapit ponad limit zdań albo słów w decyzji, którą zmiana dodaje albo której zdania wiążące zmienia, także gdy zmienia tylko ich podział na akapity, a każdy inny wpis ponad limit tylko wypisuje; (3) *Verification* dostaje klauzulę `tests:` dla tego, co test trzyma, a para przykładów „For the binding sentences” zostaje tylko dla części, której test nie trzyma (czy część innego pytania ma własny akapit); (4) *Rejected* dostaje warianty odrzucone spod pytań „Czym mierzyć długość” i „Błąd czy linia `listed:`”, a jej dzisiejsze „a higher fixed limit — a number with no ground that breaks at the first topic with more parts than it allows” zostaje i mówi o liczbie zdań; (5) zmieniona WAY-05 sama mieści się w obu limitach, a zdanie o sprawdzeniu może stanąć we własnym akapicie jako część innego pytania, tak jak drugi akapit WAY-12.
- **WAY-12 — How is a decision checked?** — bez zmian; wzór, za którym idzie nowa kontrola: „The check of the foundation reports as an error a decision that a change adds, or whose binding sentences the change alters, and that nothing holds. Any other decision that nothing holds stands in a list the check prints, and the list stops no change.” Oraz o teście i parze przykładów: „A test that holds a sentence of a decision carries beside it a line `decision:` that gives the number of the decision and the start of that sentence, and the decision keeps its rationale and its rejected options whole. A decision may also carry a pair of examples — a change that complies and one that violates — only for the part of its sentences that no invariant and no test checks”.
- **WAY-02 — How does whatever depends on an entry refer to it?** — bez zmian: „The one reference that carries more than the identifier is the line `decision:` of a test that holds a sentence of a decision: it gives the number and, in straight double quotation marks, the start of that sentence — from where a sentence of the entry begins, three words or more, compared after every run of spaces and line breaks is replaced by a single space”.
- **WAY-22 — Is a rule a decision or an invariant?** — bez zmian; zdanie WAY-05 trzyma test, więc niezmiennika z niej nie wyprowadza się: „what of it a commit can make false is written as an invariant derived from it, unless a test holds that sentence by a line `decision:`, in which case the decision gets no derived invariant for it”.
- **WAY-385 — How large may a function and a file of a script of the-way be?** — bez zmian: „A function of a script of the-way has at most 110 lines, counted with the functions nested in it, and a file of a script has at most 1200 lines, in each part that WAY-379 names, both counted on the code as the formatter of WAY-382 leaves it; a test file stands outside the rule, and no function and no file is kept whole over a threshold as an exception.”

## Settlements to record

Candidates: 4 shown, 2 accepted — 2026-11-20

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Akapit zdań wiążących decyzji ma najwyżej 3 zdania i najwyżej 300 słów. | sentence of WAY-05 | pytanie „Czym mierzyć długość” (wybór Mariusza; odrzucone warianty pod pytaniem) | wpisze limit słów tylko do szablonu i skryptu, a WAY-05 dalej będzie mówić o samej liczbie zdań |
| 2 | Sprawdzenie fundamentu zgłasza jako błąd akapit ponad limit w decyzji, którą zmiana dodaje albo której zdania wiążące zmienia, także gdy zmienia tylko ich podział na akapity, a każdy inny wpis ponad limit tylko wypisuje. | sentence of WAY-05 | pytania „Błąd czy linia `listed:`” (wybór Mariusza, na próbę) i „Czy inny podział zdań wiążących na akapity…” (wybór Mariusza); odrzucone warianty pod pytaniami | zostawi regułę tylko w skrypcie i w szablonie albo dopisze ją do WAY-12, której pytanie dotyczy tego, co decyzję sprawdza, a nie jej długości |

## Out of scope

- Skracanie 12 wpisów the way, które już dziś stoją ponad limit, w tym WAY-344 i WAY-405: robi to osobne zadanie zaraz po tym.
- Wpisy loop2 ponad limit: loop2 dostaje kontrolę, gdy przesunie przypiętą wersję the way, i własne zadanie porządkowe.

---
title: "the way: wybory technologii docierają do mnie tekstem, wybór po wyborze, zamiast jedną gęstą tabelą"
status: draft
created: 2026-11-02T12:40
updated: 2026-11-07
tags: [zadanie]
related: "notatka projektu autora"
---

# the way: wybory technologii docierają do mnie tekstem, wybór po wyborze, zamiast jedną gęstą tabelą

Status: ready for cycle
Project relation: independent

## Description

### Need

- Gdy the way ustala technologię produktu, kilka wyborów zbadanych równolegle trafia do Mariusza razem, w jednej tabeli ze wszystkimi danymi naraz (`project-level/technology/settle.md:46-50`, WAY-123).
- Przy MVP2 były to cztery wybory w sześciu kolumnach, w jednej komórce stało 13 opcji oraz liczby pakietów i kilobajtów; Mariusz odpisał, że „te punkty są mało dla mnie zrozumiałe”, i nie wiedział, co zatwierdza, dopóki agent nie przepisał tego zwykłym tekstem.
- Sama zmiana formy nie wystarcza: po przepisaniu na tekst Mariusz nadal nie rozumiał zdania o kompilatorze.
- Liczby w tabeli łamały też obowiązującą decyzję WAY-123, która za naruszenie uznaje pokazanie opcji jako listy cech technicznych, a żaden krok tego nie sprawdza.
- Bez zmiany każdy następny krok technologii kosztuje dodatkowe tury, a przy szybkim „według rekomendacji” może przejść wybór, którego Mariusz by nie zrobił; zdarzyło się to raz, na jednym produkcie, i nic się nie zepsuło, bo Mariusz zatrzymał się przy tabeli.
- Osobno: przy doprecyzowaniu zadania pozycja listy technologii z dopiskiem `— held by` wygląda na rozstrzygniętą także wtedy, gdy wskazana decyzja nie odpowiada na część sprawy, więc Mariusz nie wie, że ma coś do dopowiedzenia; to przypadek z lektury reguły, bez ani jednego zdarzenia.

### To do

1. W `project-level/technology/settle.md:46-50` zdanie zaczynające się od „Then show the wave together, in one table:” zastąpić tekstem:

   > Then show the wave together, in one message, one choice after another: what the choice decides, in words a person who does not know the technology can follow; the options that decide it, each under its own name and by what it changes for the product; the other options, one line each, and the lines of the options left out; a recommendation, the weak point of the option recommended and beside it the risks the tests gave, each marked as a hypothesis (WAY-123, WAY-138, WAY-113).

2. W `settle.md:45-46`, gdzie świeży agent szuka przed pokazaniem sprzeczności między wyborami, po „what one choice of the table contradicts in another” dopisać: „and any option shown by figures or features instead of what it changes for the product, or a word a person who does not know the technology cannot follow without an explanation (WAY-123)” (pytanie 2).
3. W WAY-123 w `foundations/decisions.md` zmienić „in one table” na „in one message” (`:2883`), „in separate tables” na „in separate messages” (`:2897-2898`) i w *Rejected* „the tables come one choice at a time” na brzmienie bez tabeli (`:2912`). To zmiana sensu zaakceptowanej decyzji, więc Mariusz ma ją zobaczyć przy scaleniu.
4. Przejrzeć pozostałe miejsca, w których „table” nazywa to, co dostaje człowiek, i zmienić je na wiadomość. Stan @ 52889bc:
   - `project-level/technology/settle.md:43,46,55,59,67,75`, `project-level/technology/task_run.md:84`, `project-level/technology/SKILL.md:58`;
   - `project-level/definition_template.md:237` (powtórzenie zdania WAY-123) i `:255` (powtórzenie zdania WAY-138);
   - `project-level/task/template.md:42,134` („as the table gave them”);
   - `project-level/task/skill/orchestrated_mode.md:26`, `project-level/lead/conversation_template.md:101`, `project-level/lead/skill/SKILL.md:133` („the table of choices”);
   - w `foundations/decisions.md`: WAY-138 (`:3573,3583,3590`), WAY-267 (`:7886,7893`), WAY-268 (`:7967,7979`, „a table for the human”); WAY-137 (`:3547`, „the table of consequences”) — sprawdzić, czy mówi o tym, co dostaje człowiek, czy o porównaniu w raporcie.
   - Zwykłych tabel nie ruszać: tabeli pytań z `reserved_choices.md:22,42` i WAY-268 (`:7939,7953`), tabeli roboczej ze `start.md:7` i `definition_template.md:269,282`, tabeli znaczników z `definition_template.md:175`.
5. W `project-level/technology/task_run.md:55-57` zdanie o liście ma brzmieć:

   > A note that refinement derived from a reserved choice is not that word; the list shown to the human keeps the item `— held by`, with one sentence saying what that decision leaves unsaid, as `start.md` gives, and the human's change to the list is the word.

   W tym samym akapicie, w `task_run.md:52-54`, wtrącenie „whatever `list.md` says of the matter it settles” zastąpić przez „though at a definition `list.md` leaves such an item `— open`” (pytanie 3).

### Questions to settle

- Pytanie 1: w jakiej formie wybory jednej fali technologii docierają do Mariusza?
  - Answer: Jedną wiadomością, wybór po wyborze, zwykłym tekstem; pełny opis dostają tylko opcje rozstrzygające, z zachowanymi nazwami narzędzi, pozostałe po jednej linii, linie opcji odpadłych zostają; przed pokazaniem świeży agent sprawdza też, czy któraś opcja nie stoi liczbami albo cechami zamiast tym, co zmienia w produkcie. Cena: wiadomość jest dłuższa i traci porównanie opcji w poprzek; agent sprawdzający widzi tylko pierwszą wiadomość, więc żargon w dalszych dopytaniach zostaje.
  - Not chosen:
    - zdanie, że nazwa narzędzia stoi tylko tam, gdzie niesie konsekwencję — agent przy przepisywaniu zostawił samo „Playwrightem” i zgubił różnicę między CLI a serwerem MCP, o którą Mariusz musiał się upomnieć;
    - tabela z akapitem prostym językiem pod spodem — najmniej zmian, ale najdłuższa wiadomość, a tabela dalej nie jest czytana;
    - zostawić jak jest — nic nie psuje się od razu, ale tabela zachęca do „według rekomendacji”, a przy MVP2 dwie z czterech rekomendacji upadły.
  - Source: Mariusz, 2026-11-02, przyjęte brzmienie zadania w sesji przeglądu warstwy AI — rejestr przeglądu warstwy AI w prywatnych notatkach autora, AIR-564, *Propozycja*, *Rachunek* i *Historia* („przeredagowane (tekst z zachowanymi nazwami, pełny opis tylko dla opcji rozstrzygających, dopisek dla agenta sprawdzającego, linie opcji odrzuconych zostają, estymata 3)”).
- Pytanie 2: czy agent sprawdzający wiadomość przed pokazaniem łapie tylko liczby i cechy, czy także słowa, których człowiek nieznający technologii nie odczyta?
  - Answer: B. Łapie także słowo, którego osoba nieznająca technologii nie odczyta bez wyjaśnienia — bez tego nic nie sprawdza wymogu z punktu 1, by wybór był opisany słowami zrozumiałymi dla takiej osoby, a żargon w opisie konsekwencji (zdanie o kompilatorze, „bundler”) przechodzi. Cena: to ocena agenta, nie reguła mechaniczna, więc czasem zgłosi słowo, które Mariusz zna, i autor wiadomości dopisze zbędne wyjaśnienie.
  - Not chosen:
    - A. Tylko liczby i cechy, jak w pierwotnym brzmieniu zadania — nic nie kosztuje, ale żargon w opisie konsekwencji dalej dociera do Mariusza i kosztuje dodatkową turę, jak przy MVP2.
  - Source: Mariusz, 2026-11-07: „B”, na pytanie „Wybierasz A czy B?”, przy wariancie B, którego słabość nazwano: ocena agenta, czasem zgłosi słowo, które Mariusz zna.
- Pytanie 3: czy ta sama zmiana poprawia też zdanie dwie linie wyżej, `task_run.md:52-54`, które mówi odwrotnie niż `list.md`?
  - Answer: Tak. Wtrącenie „whatever `list.md` says of the matter it settles” nazywa sprawę rozstrzygniętą przez milczącą decyzję, a `list.md:23-26` mówi, że taka decyzja jej nie trzyma; reguła działa, sprzeczne jest tylko wtrącenie, więc zmienia się na „though at a definition `list.md` leaves such an item `— open`”.
  - Not chosen:
    - zostawić — dziś nic nie kosztuje, ale sprzeczność zostaje w akapicie, który zadanie właśnie poprawia, i wymaga osobnej łatki, a przegląd fundamentu przypisał ją temu zadaniu.
  - Source: Mariusz, 2026-11-07: „tak”, na pytanie „Dopisujemy?”, przy rekomendacji dopisania.

## Context

- Sesja, w której to się wydarzyło: zapis wcześniejszej sesji autora (poza repozytorium) — tabela w linii 1155, odpowiedź Mariusza w 1162, przepisanie „po ludzku” w 1166, dopytanie w 1176; wygasa około 2026-12-02.
- Zapis sprawy w przeglądzie warstwy AI: AIR-564 (tabela) i AIR-572 (pozycja `— held by`) w rejestr przeglądu warstwy AI w prywatnych notatkach autora; po 14 dniach od zamknięcia przechodzą do archiwum tego rejestru w tym samym katalogu.
- Przy MVP2 odpadły w tej wymianie dwie z czterech rekomendacji: Preact na rzecz Reacta (Mariusz wskazał go jeszcze przy tabeli) i Playwright MCP na rzecz Playwright CLI (z własnej wiedzy Mariusza, po przepisaniu).
- Przegląd fundamentu the way z 2026-11-07 znalazł w PR #65 dwie niezałatane uwagi dotyczące punktu 5: theway#065-8 (to samo, co punkt 5) i theway#065-9 (`task_run.md:53-54`: „whatever `list.md` says of the matter it settles” nazywa sprawę rozstrzygniętą przez milczącą decyzję, odwrotnie niż `list.md:23-26`) — notatka autora z uwagami z PR-ów (poza repozytorium), sekcja „Dopisek: wybory technologii tekstem”.
- Uwaga theway#065-8 wskazuje też `list.md:31`; przy definicji projektu takiej pozycji nie ma, bo milcząca decyzja zostawia ją `— open` (`list.md:23-26`), a przy zmianie listy zdanie o tym, czego decyzja nie mówi, każe dopisać `start.md:18-20`, więc `list.md` zmiany nie potrzebuje.
- Gdy Mariusz zostawi listę bez zmian, pozycja dalej stoi jako `— held by`, choć `reserved_choices.md:14-18` mówi, że taki wybór nie jest ustalony; po punkcie 5 Mariusz przynajmniej wie, co zostaje otwarte.
- Testy the way nie sprawdzają brzmienia tych zdań (`git grep` po „table” w plikach `*.py` @ 52889bc nie trafia w krok technologii).
- Numery linii w punktach 3 i 4 według `foundations` @ 52889bc; zadanie było pisane przy f45ca40, gdzie WAY-123 stało w `:2765-2787`.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-123: „The choices whose research started together reach the human together, in one table, once every one of their comparisons has passed the critique, each with its recommendation and the weak point of the option recommended” — w *Verification* jako naruszenie: „the options are shown as lists of technical features; […] two choices whose research started together reach the human in separate tables”; w *Rejected*: „every choice shown on its own, followed by a question against it — the human waits between choices, and each choice costs two exchanges; each comparison shown as soon as its critique passes — the tables come one choice at a time”. Zadanie zmienia tę decyzję (punkt 3).
- WAY-138: „The risks these tests give are hypotheses with no source, not differences claimed between options, so the critique of the comparison does not strike them, and they stand in the table beside the option recommended before the human chooses.”
- WAY-113: „a decision question gives the available ways, the cost of each and a recommendation […]. After a human choice enters an entry's binding part, the agent asks one question against that choice anchored in the human's words or supplied material, unless the choice ends with the work, or the human took one of the ways offered and the decision question named, anchored in the material, the weak point of that way.”
- WAY-120: „For a collectively reviewed set the critic checks form, fidelity to source and contradictions across entries before presentation.”
- WAY-165: „an entry […] that leaves part of what a matter asks unanswered does not settle that matter at a project definition, while in a run at a task (WAY-267) it holds the choice like any decision, which opens only on the human's word.”
- WAY-267: „a choice a decision of the foundation holds opens only on the human's word, the result then being a change of that decision.”

## Settlements to record

Candidates: 4 shown, 3 accepted — 2026-11-07

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Wybory jednej fali docierają do człowieka jedną wiadomością, wybór po wyborze, zwykłym tekstem: pełny opis pod własną nazwą dostają tylko opcje rozstrzygające, pozostałe po jednej linii, a linie opcji odpadłych zostają; tabela, tabela z akapitem pod spodem i zasada „nazwa narzędzia tylko tam, gdzie niesie konsekwencję” odpadły. | decision | pytanie 1 pod *Questions to settle*, z jego *Not chosen* | czy WAY-123 zmienia tylko słowo „table” na „message”, czy jego *Rationale* i *Rejected* dostają formę tekstu, odrzuconą tabelę i dwa odrzucone warianty |
| 2 | Zanim fala dotrze do człowieka, świeży agent sprawdza w wiadomości, czy któraś opcja nie stoi liczbami albo cechami zamiast tym, co zmienia w produkcie, i czy nie pada słowo, którego osoba nieznająca technologii nie odczyta bez wyjaśnienia; sprawdzenie widzi tylko pierwszą wiadomość. | decision | pytanie 2 (B) pod *Questions to settle*, z jego *Not chosen* | czy sprawdzenie zostaje tylko w `settle.md`, czy wchodzi do decyzji (WAY-123 albo WAY-120), i czy *Rejected* dostaje wariant A |
| 3 | W przebiegu przy zadaniu pozycja trzymana przez decyzję, która milczy o części sprawy, stoi na liście pokazanej człowiekowi z jednym zdaniem o tym, czego ta decyzja nie mówi. | decision | To do, punkt 5 (AIR-572, przyjęte z zadaniem 2026-11-02) | czy zmienia się tylko `task_run.md`, czy WAY-165 albo WAY-267 dostaje to zdanie, skoro dziś mówią tylko, że taka decyzja trzyma wybór do słowa człowieka |

## Out of scope

none

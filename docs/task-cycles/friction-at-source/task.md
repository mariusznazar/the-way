---
title: "the way: kroki „sprawdź sam” w prośbie, wskazywanie miejsc w zadaniu nagłówkiem, przegląd fundamentu pyta o koniec stanu przejściowego"
status: draft
created: 2026-11-12T17:54
updated: 2026-11-12
tags: [zadanie]
related: "the author's private note of the process project"
---

# the way: kroki „sprawdź sam” w prośbie, wskazywanie miejsc w zadaniu nagłówkiem, przegląd fundamentu pyta o koniec stanu przejściowego

Status: ready for cycle
Project relation: independent

## Description

### Need

- Człowiek, który dostaje prośbę o scalenie ze sprawdzeniem, którego agent nie mógł wykonać, nie wie z opisu prośby, co ma sprawdzić ręcznie.
- Agent cyklu zaczyna pracę od odwołania w dokumencie zadania do pliku, linii albo nazwy, która już nie istnieje.
- Decyzja o stanie przejściowym produktu („na razie obie wersje naraz”) nie mówi, co ten stan kończy, więc stan zostaje w kodzie na stałe.

### To do

Trzy niezależne punkty, w dowolnej kolejności.

1. Pozycja opisu prośby o sprawdzeniu, którego agent nie wykonał, a które człowiek może zrobić ręcznie, podaje trzy do sześciu kroków dla człowieka: gdzie wejść, co zrobić i co powinien zobaczyć; odpowiedzi pozycji zostają te same.
2. Szablon dokumentu zadania i skill doprecyzowania zadania mówią, że miejsce do zmiany w pliku wskazuje się nagłówkiem albo cytatem, a numer linii jest tylko podpowiedzią; źródło odpowiedzi pod pytaniem zostaje w dzisiejszej formie, z linią i rewizją.
3. Przegląd fundamentu wypisuje decyzje, które opisują stan przejściowy produktu, i przy każdej pyta człowieka, czy jest zadanie, które ten stan kończy; gdy nie ma, proponuje jego założenie tak, jak zakłada zadania z innych swoich propozycji.

### Questions to settle

- 1. Co to zadanie robi ze skryptem, który uruchamia sprawdzenie i sam zapisuje dowód?
  - Answer: Punkt wychodzi z tego zadania. Uruchamianie nowych testów na kodzie sprzed zmiany i po zmianie jest dopisane jako notatka do zadania the author's private task note about agents going around tests. Plik dowodu sprawdzenia jest odłożony, dopóki rejestr problemów nie pokaże więcej przypadków niż trzy wiersze o kodzie wyjścia w 83 cyklach.
  - Not chosen:
    - Cała karta w tym zadaniu, oba tryby — największy z czterech punktów: skrypt z testami, trzy skille, kontrola po każdym kawałku, spec i zmiana WAY-159; zadanie przestaje być zbiorem drobnych poprawek.
    - Sam plik dowodu (polecenie, kod wyjścia, commit), bez końcówki wyjścia i bez uruchamiania testów na kodzie sprzed zmiany — nadal zmienia WAY-159 i przepuszcza każde sprawdzenie każdego agenta przez pośrednika, a usuwa klasę, która dała trzy wiersze na 83 cykle.
    - Osobne zadanie na cały punkt — pełny koszt drugiego doprecyzowania i drugiego cyklu.
  - Source: Mariusz, 2026-11-12, „ok C”, w odpowiedzi na pytanie z czterema drogami A–D i rekomendacją C.
- 2. Czy kontrola odwołań dokumentu zadania przed cyklem zostaje w tym zadaniu, a jeśli tak, to jako skrypt czy jako reguła pisania odwołań?
  - Answer: Zostaje jako reguła u źródła, bez skryptu: miejsce do zmiany wskazuje się w dokumencie zadania nagłówkiem albo cytatem, a numer linii jest tylko podpowiedzią.
  - Not chosen:
    - Skrypt, który przed startem cyklu sprawdza pliki, linie i wpisy wskazane w zadaniu — łapie około 15 z 80 wystąpień, każde warte kilka kroków agenta, a kosztuje skrypt z testami i krok na starcie każdego cyklu; linia podana z rewizją jako źródło odpowiedzi przesuwa się z założenia, więc skrypt czytałby plik z tamtej rewizji albo zgłaszał fałszywe alarmy.
    - Punkt odpada — wiersze dalej przychodzą, mniej więcej jeden na cykl, każdy za zero albo kilka kroków agenta.
  - Source: Mariusz, 2026-11-12, „B”, w odpowiedzi na pytanie z trzema drogami A–C i rekomendacją B.
- 3. Jak decyzja o stanie przejściowym dostaje zadanie, które go kończy: polem we wpisie czy listą w przeglądzie fundamentu?
  - Answer: Listą w przeglądzie fundamentu, bez pola we wpisie: przegląd wypisuje decyzje o stanie przejściowym i przy każdej pyta człowieka, czy jest zadanie, które ten stan kończy; gdy nie ma, zakłada je za zgodą człowieka.
  - Not chosen:
    - Wskazanie zadania we wpisie decyzji, jak w karcie — zmienia WAY-24 i szablon decyzji, wchodzi w spór z WAY-01, wymaga sposobu, w jaki wpis nazywa zadanie z listy leżącej poza repozytorium, zadanie musi istnieć przed zapisem decyzji, a wskazania się starzeją.
    - Pytanie przy doprecyzowaniu zadania, co kończy ustalany stan przejściowy — stany przejściowe zapisane przez sam cykl przechodzą bokiem, a powiązanie decyzji z zadaniem nigdzie nie zostaje.
    - Punkt odpada — następne przejście może utknąć i nikt tego nie zauważy przed przeglądem fundamentu, o ile recenzent sam na to wpadnie.
  - Source: Mariusz, 2026-11-12, „B”, w odpowiedzi na pytanie z czterema drogami A–D i rekomendacją B.
- 4. Gdzie w opisie prośby stoją kroki „jak to sprawdzić samemu”: w pozycji o niewykonanym sprawdzeniu czy w osobnej sekcji?
  - Answer: Wewnątrz pozycji o niewykonanym sprawdzeniu: gdy sprawdzenie da się zrobić ręcznie, pozycja dostaje piątą część, trzy do sześciu kroków (gdzie wejść, co zrobić, co człowiek powinien zobaczyć). Odpowiedzi pozycji zostają te same trzy; po własnym sprawdzeniu człowiek pisze uwagę jak dziś. Zmienia WAY-327; szkielet opisu i skrypt formy zostają bez zmian.
  - Not chosen:
    - Osobna sekcja w górnej części opisu, jak w karcie źródłowej — zmienia szkielet (WAY-286), skrypt formy z testami (WAY-290) i blok w języku zadania; sekcja stoi w każdej prośbie i w większości ma `none`.
    - Punkt odpada — człowiek dalej dostaje pozycję z trzema odpowiedziami, a żeby sprawdzić samemu, dopytuje agenta albo czyta dolną część opisu.
  - Source: Mariusz, 2026-11-12, „B”, w odpowiedzi na pytanie z trzema drogami A–C i rekomendacją B.
- 5. Czy liczenie niewykonanych sprawdzeń według przyczyny zostaje w tym zadaniu?
  - Answer: Punkt wychodzi z zadania, bo nie zmienia niczego w repozytorium the way. Zgrubne policzenie z doprecyzowania zostaje w *Context* jako wynik. Z grupy „brak narzędzia na komputerze roboczym” wyłączony Docker dostał osobne zadanie w projekcie gry, the author's private task note in the game project about the test script starting Docker, w którym skrypt testów sam włącza Dockera; zadania o miejscu z Linuksem dla sprawdzeń agentów nie założono.
  - Not chosen:
    - Rozbicie klasy na stałe w szablonie rejestru i przeklasyfikowanie 292 wierszy — zmiana w repozytorium i w narzędziu w vaulcie, nowa seria pomiarów i jednorazowe przeklasyfikowanie dla jednej decyzji, którą liczby już w zarysie rozstrzygają.
    - Punkt odpada bez śladu — zgrubna tabela zostaje tylko w rozmowie.
  - Source: Mariusz, 2026-11-12, „niech będzie B”, w odpowiedzi na pytanie z trzema drogami A–C i rekomendacją B.

## Context

- Zadanie powstało z raportu o usprawnieniach procesu: the table of actions in the author's private report on improvements of the process, wiersze D13, D14, D16 i D19, pakiet „Mniej tarcia u źródła”.
- Karty źródłowe punktu o krokach dla człowieka i o liczeniu według przyczyny: card D4 in the author's private report on the AI Tech Leaders course i card D9 in the author's private report on the mega.dev course.
- Karty źródłowe punktu o odwołaniach: card D1 in the author's private report on the 10xDEVS course i card D4 in the author's second private report on the AI Tech Leaders course.
- Karta źródłowa punktu o stanie przejściowym: card D9 in the author's private report on the game's architecture.
- Zadania, z którymi punkty się łączą: the author's private task note on giving agents a working method of testing (kroki dla człowieka) i the author's private task note about agents going around tests (czerwony przebieg nowego testu; karta D4 z raportu o kursie mega.dev każe dopisać tę próbę właśnie do niego).
- Karty zostały porównane z dziennikiem decyzji the way w stanie `foundations` `2292f33` i z rejestrem problemów w dniu 2026-11-12; wynik stoi w punktach poniżej.
- Rejestr problemów 2026-11-12: 1306 wierszy z 83 cykli.
- Klasa „sprawdzenie niewykonane albo niepewne”: 292 wiersze w 57 cyklach; koszt jednego wystąpienia: 261 razy nic, 20 razy kilka kroków agenta, 2 razy etap, 4 razy runda, 5 razy czas człowieka; 29 wierszy należy do sprawy już naprawionej (agent oddaje etap bez części lektury).
- Klasa „nieaktualne odwołanie”: 80 wierszy w 45 cyklach; koszt jednego wystąpienia: 35 razy nic, 44 razy kilka kroków agenta, raz etap; ani razu runda ani czas człowieka.
- Z 80 wierszy „nieaktualnego odwołania”, według opisów wierszy czytanych przez agenta doprecyzowania: około 15 to numer linii, ścieżka albo cytat w dokumencie zadania, które skrypt mógłby sprawdzić; około 40 to odwołania w zleceniach dla agentów i w planach pisanych w trakcie cyklu; około 10 to nieaktualne liczby.
- Zgrubne policzenie klasy „sprawdzenie niewykonane albo niepewne” według przyczyny, po słowach kluczowych w opisach wierszy (nie klasyfikacja; 194 wiersze nie wpadły do żadnej grupy): brak Linuksa, Dockera albo narzędzia na komputerze roboczym — 17 wierszy w 6 cyklach, w tym 2 razy czas człowieka, raz runda, raz etap; stan serwera nieodczytany — 27 wierszy w 6 cyklach, 7 razy kilka kroków agenta, reszta nic; źródło nieotwarte — 50 wierszy w 33 cyklach, prawie zawsze nic.
- Opis prośby już dziś stawia niewykonane sprawdzenie przed człowiekiem: pozycja rodzaju 4 w grupie *Fix or let through* (`task-cycle/skill/request_template.md:225-233`), z czterema częściami pozycji według WAY-327; kroków do wykonania przez człowieka pozycja nie ma.
- Lista zadań the way i gry leży w prywatnych notatkach poza repozytorium, a ich ścieżki i linki nie wchodzą do plików repozytorium (WAY-320, WAY-308); zadanie spoza planu projektu nie ma identyfikatora, którym wpis mógłby je nazwać (WAY-329).
- Przegląd fundamentu już dziś wylicza słabe punkty, które nazywają uzasadnienia decyzji, i porównuje je ze stanem produktu (WAY-305), a propozycja przyjęta przez człowieka staje się zadaniem (WAY-302).
- Słowem nie da się wybrać decyzji o stanie przejściowym: „until” i pokrewne stoją w zdaniach wiążących 40 z 304 decyzji the way i 85 z 388 decyzji gry (`loop2` `eb7cf5d8`), w większości w zwykłych regułach („tempo zostaje, dopóki gracz nie wybierze innego”).
- Przypadek, z którego wyszedł punkt o stanie przejściowym: decyzja gry D-265 („Until its last screen in the browser's DOM APIs moves to React, a shared control that a React screen uses has two forms […]”).

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

Wybrane po częściach, których zadanie dotyka: cykl zadania (opis prośby), doprecyzowanie zadania (szablon i skill), przegląd fundamentu, dziennik decyzji. Cytowane zdania wiążące, w stanie `foundations` `2292f33`.

- **WAY-327 — zmieniana przez to zadanie (pytanie 4).** „An item of the section of a request's description for the human's decisions in which the human chooses — each item of the groups *Needed from you* and *Fix or let through* but one that asks for an action outside the repository — says concretely what happens and who feels it, when and in what situation; gives each way open with what follows from choosing it and what it costs, in time, a round of correction with its review and the risk that stays, and where it can show up later; gives a recommendation with its reason in one sentence; and asks a question with the answers to choose from. The agent that writes the description checks every such item against these four before the request opens, and fills in what is missing.” Zmiana: pozycja o sprawdzeniu, którego agent nie wykonał, a które człowiek może zrobić ręcznie, ma piątą część — trzy do sześciu kroków dla człowieka.
- **WAY-286** — stały szkielet opisu prośby: „The description of a request a task cycle opens follows one template whose headings stand in a fixed order and at a fixed level […] and a section with no content reads `none` rather than being left out.” Zadanie szkieletu nie zmienia.
- **WAY-287** — sekcja decyzji człowieka obejmuje m.in. „the steps skipped and the checks not run”, w trzech grupach *Needed from you*, *Fix or let through*, *You accept by merging*.
- **WAY-289** — odpowiedź „napraw w tej prośbie” dla pominiętego sprawdzenia: „the same answer is offered for a step or a check the cycle skipped […] and runs the step or the check”. Kroki dla człowieka nie dodają czwartej odpowiedzi.
- **WAY-290** — „The script judges no content.” Obecności kroków skrypt formy nie sprawdza; pilnuje jej agent piszący opis, jak czterech części WAY-327.
- **WAY-24** — „A decision names no date or condition for its review, the log holds no record of a review, and the review of the foundation against the product is a run of the skill `review-foundation`, which a human starts in a session with an agent when the reminder of a request asks for it (WAY-300), and no task of the product's backlog.”
- **WAY-302** — „A proposal on which the human decides a change becomes a task of the product's backlog; […] the review itself changes nothing in the foundation or the code.” Punkt 3 listy idzie tą drogą: brak zadania kończącego stan przejściowy jest propozycją przeglądu.
- **WAY-305** — „A review of the foundation lists the weak points, prices, gaps and accepted risks that the rationales of the decisions name, compares each with the product's state today, and runs the missing check wherever the check is cheap and by reading alone […]”.
- **WAY-36** — „A rule enters the decision log only when it still binds once the change that brings it has been merged; a rule that ends with a piece of work — an order of steps, a first merge, a transition between two states — stays in the plan of that work […]”. Stan przejściowy z punktu 3 to stan, który kończy praca późniejsza niż zmiana wnosząca decyzję; przejście kończące się razem z własną zmianą do dziennika nie trafia wcale.
- **WAY-37** — „A change that brings what entries of the foundation wait for […] also fixes every entry that waits for it, in the same change.” Punkt 3 nie zmienia tej reguły: ona działa, gdy to, na co wpis czeka, przychodzi; przegląd pilnuje, żeby ktoś to przyjście zaplanował.
- **WAY-01** — „On the main branch, the foundation describes the product as it is […] and roadmaps and plans do not change it.”

## Settlements to record

Candidates: 6 shown, 4 accepted — 2026-11-12

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Dokument zadania wskazuje miejsce do zmiany w pliku nagłówkiem albo cytatem, a numer linii jest tylko podpowiedzią; źródło odpowiedzi pod pytaniem zostaje z linią i rewizją. | decision | pytanie 2 (jego *Not chosen*) | czy reguła staje tylko w tekście szablonu, czy jako decyzja z odrzuconym skryptem sprawdzającym odwołania, i czy obejmuje też źródło odpowiedzi |
| 2 | Przegląd fundamentu wypisuje decyzje o stanie przejściowym produktu i przy każdej pyta człowieka, czy jest zadanie, które ten stan kończy; gdy nie ma, zakłada je za zgodą człowieka; wpis decyzji zadania nie wskazuje. | decision | pytanie 3 (jego *Not chosen*) | czy dać wpisowi decyzji pole na zadanie kończące, czy pytać o nie przy doprecyzowaniu zadania |
| 3 | Pozycja opisu prośby o sprawdzeniu, którego agent nie wykonał, a które człowiek może zrobić ręcznie, podaje trzy do sześciu kroków dla człowieka: gdzie wejść, co zrobić i co powinien zobaczyć; zmienia WAY-327. | decision | pytanie 4 (jego *Not chosen*) | czy kroki stoją w pozycji, czy w osobnej sekcji szkieletu, i czy zmiana idzie do WAY-327, czy do nowej decyzji |
| 4 | „Stan przejściowy” to stan produktu, który decyzja opisuje do czasu, aż skończy go praca późniejsza niż zmiana wnosząca tę decyzję — jak dwie formy wspólnej kontrolki, dopóki ostatni ekran nie przejdzie na React. | glossary term | punkt 3 listy zmian; WAY-36 („a transition between two states”); przyjęte przez Mariusza 2026-11-12 („1 i 2 tak jak rekomendujesz”) | czy przegląd wypisuje też zwykłe reguły ze słowem „dopóki” albo przejścia, które kończą się z własną zmianą, które WAY-36 trzyma poza dziennikiem |

## Out of scope

- Skrypt, który uruchamia sprawdzenie i sam zapisuje dowód (pytanie 1).
- Liczenie niewykonanych sprawdzeń według przyczyny i zmiana klas rejestru problemów (pytanie 5).

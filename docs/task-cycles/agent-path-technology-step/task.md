---
title: "the way: krok technologii — jak agent widzi działający produkt"
status: draft
created: 2026-10-17
updated: 2026-10-18
tags: [the-way, zadanie]
related: ["[[(P) Proces pracy nad produktem]]", "[[wznowienie_limen_zmiany_w_the_way]]"]
---

# Krok technologii: jak agent widzi działający produkt

Status: ready for cycle
Project relation: independent

## Description

### Need

- Cykl zadania każe sprawdzić zachowanie widoczne dla użytkownika także w uruchomionym produkcie, ale nic w procesie nie gwarantuje, że agent ma do działającego produktu drogę: do jego logów, do interfejsu i do danych deweloperskich.
- Krok technologii (WAY-121) ustala przed bramką gotowości wybory technologiczne projektu, ale o tę drogę nie pyta.
- Odbiorcą jest agent cyklu zadania, który ma sprawdzić zachowanie w uruchomionym produkcie, i Mariusz, który dostaje request z wynikiem tego sprawdzenia: bez drogi do produktu sprawdzenie albo się nie odbywa, albo agent improwizuje dostęp w trakcie cyklu.

### To do

1. Krok technologii, szukając wyborów potrzebnych projektowi, sprawdza trzy sprawy drogi agenta do działającego produktu — jak agent czyta jego logi, jak obsługuje jego interfejs, skąd bierze dane deweloperskie — i stawia każdą na liście jako osobny wybór, gdy projekt wnosi zachowanie, które użytkownik zobaczy w działającym produkcie, a fundament nie ma decyzji, jak agent do niego dotrze; taki wybór krok rozstrzyga jak każdy inny.
2. Definicja projektu nie ma obowiązkowych pozycji drogi agenta, a bramka gotowości ich nie sprawdza; definicja już zatwierdzona nie wraca z ich powodu do kroku technologii.

### Questions to settle

- Pytanie 1: czy zadanie obejmuje tylko drogę agenta do działającego produktu i technologię logów, czy także reguły tego, co produkt loguje i w jakiej postaci?
  - Answer: tylko drogę i technologię, jak mówi werdykt z wiersza A1; reguły treści logów idą osobnym zadaniem — wytycznymi do konstruowania obserwowalności produktu. Odrzucone: oba w tym zadaniu (reguła treści logów działa przy pisaniu kodu i w recenzji, czyli w cyklu zadania, a nie w definicji projektu, i nie była jeszcze ważona — weszłaby bez tego ważenia).
  - Source: Mariusz, 2026-10-17: „zróbmy a ale potem potrzebny będzie follow-up do wypracowania wytycznych do konstruowania dla produktu observability-guide czy czegoś podobnego” — na drogę a przedstawioną w rozmowie doprecyzowania.
- Pytanie 2: czy pozycja „jak agent widzi działający produkt” jest jednym z wyborów technologicznych listy, którą krok technologii prowadzi według WAY-121, czy osobnym wymaganiem kroku obok tej listy?
  - Answer: jednym z wyborów listy — zwykły wybór sekcji „Technology”, tylko obowiązkowy: WAY-121 dostaje zdanie, że lista zawsze ma tę pozycję, krok rozstrzyga ją jak każdy wybór (opcje z konsekwencjami, krytyka, test ryzyk, wybór człowieka, znacznik `held by` albo `projected`), a bramka gotowości sprawdza, że pozycja jest; wyjątek od reguły przynależności z WAY-121 (pozycja obowiązkowa także wtedy, gdy niczego nie dokłada do utrzymania) jest nazwany wprost. Odrzucone: osobne wymaganie kroku obok listy (nowe miejsce w formie definicji, nowy warunek bramki i nowa decyzja, a odpowiedź nie przechodzi sama do kolejnych projektów jako `held by`); miejsce poza krokiem technologii, np. lista skilla wdrożeniowego z WAY-139 (odchodzi od werdyktu A1, a WAY-139 sprawdza tylko zadania wdrażające produkt, więc produkt uruchamiany lokalnie zostaje bez gwarancji).
  - Source: Mariusz, 2026-10-17: „ok, a” — na drogę a przedstawioną w rozmowie doprecyzowania; WAY-121/1, `foundations/decisions.md:3432-3434`, `foundations` `e7f7c3a`.
  - Zastąpione w części odpowiedziami na pytania 7 i 8: pozycja nie jest obowiązkowa w każdej liście ani sprawdzana bramką; trafia na listę według kryterium z pytania 8.
- Pytanie 3: czy „logi, interfejs, dane deweloperskie” to jedna pozycja listy czy trzy osobne, i co z produktem, który któregoś z nich nie ma?
  - Answer: trzy osobne obowiązkowe pozycje — logi, interfejs, dane deweloperskie — każda ważona osobno, wszystkie w jednej fali, każda z własną decyzją albo `held by`; produkt bez którejś z tych rzeczy też dostaje odpowiedź (np. „interfejsem jest wyjście programu”, „produkt nie trzyma danych, agentowi wystarczą dane wejściowe z testów”). Odrzucone: jedna pozycja obejmująca wszystkie trzy (wiąże trzy niezależne wybory w jeden, co odrzuca WAY-122, a późniejsza zmiana jednej sprawy otwiera całą decyzję); jedna pozycja-hasło rozbijana na tyle wyborów, ile produkt potrzebuje (bramka nie sprawdzi kompletności skryptem, o pominięciu decyduje osąd agenta).
  - Source: Mariusz, 2026-10-17: „a” — na drogę a przedstawioną w rozmowie doprecyzowania; WAY-122/1 *Rejected*, `foundations/decisions.md:3512-3513`, `foundations` `e7f7c3a`.
  - Zastąpione w części odpowiedzią na pytanie 8: trzy sprawy zostają osobnymi wyborami, ale nie są obowiązkowe — każda staje na liście według kryterium z pytania 8.
- Pytanie 4: czy wymóg trzech pozycji obejmuje także definicję zatwierdzoną przed tą zmianą, gdy produkt przesunie przypięcie the way?
  - Answer: tak — po przesunięciu przypięcia najbliższe doprecyzowanie zadania z planu zatrzymuje się na bramce, definicja wraca do kroku technologii po trzy pozycje i przechodzi bramkę ponownie (WAY-118), a plan jest sprawdzany ponownie; dotyczy to definicji MVP loop2 (`C:\Storage\The Brain\The Brain\Notes\Projects\(P) Loop\definicja_mvp_loop2.md`, zatwierdzonej 2026-10-13). Odrzucone: wymóg tylko dla definicji zatwierdzanych po zmianie (do końca MVP agent bez zapewnionej drogi do gry, drugi tryb skryptu do utrzymania i usunięcia); to samo z ręcznym nadrobieniem w loop2 (drugi tryb skryptu, a gwarancja zależy od pamięci człowieka, czego WAY-102 nie dopuszcza).
  - Source: Mariusz, 2026-10-17: „a” — na drogę a przedstawioną w rozmowie doprecyzowania; `project-level/readiness_check.py:27-34` i `project-level/task/skill/SKILL.md:79-80`, `foundations` `e7f7c3a`.
  - Zastąpione odpowiedzią na pytanie 7: bramka nie sprawdza trzech pozycji, więc definicja zatwierdzona wcześniej (także MVP loop2) nie wraca z ich powodu do kroku technologii.
- Pytanie 5: o co dokładnie pyta każda z trzech pozycji?
  - Answer: logi — gdzie trafia zapis tego, co działający produkt robi, i jak agent go czyta; interfejs — jak agent obsługuje produkt tak, jak robi to jego użytkownik (ekran w przeglądarce, wywołanie API, polecenie w terminalu), i jak widzi, co produkt mu odpowiada; dane deweloperskie — skąd biorą się dane, na których agent sprawdza zachowanie produktu poza produkcją, i jak agent dochodzi do stanu danych, którego sprawdzenie potrzebuje; pozycja nie przesądza, czy to dane zakładane od zera, czy trwałe dedykowane środowisko testowe — oba są opcjami ważonymi przez konsekwencje (WAY-123). Odrzucone: interfejs bez dopisku „tak, jak robi to jego użytkownik” (interfejsem mógłby zostać dostęp do bazy z pominięciem aplikacji); dane z dopiskiem „i jak się je odtwarza od zera” (wyklucza trwałe dedykowane środowisko testowe, które w wielu przypadkach jest lepsze); dane bez żadnego dopisku (decyzja może nie powiedzieć, jak agent dochodzi do stanu, którego sprawdzenie potrzebuje, i agent cyklu improwizuje).
  - Source: Mariusz, 2026-10-17: „niech będzie a, ale nie jestem pewny czy rozumiem dobrze pojęcie danych developerskich i chyba chciałbym to doszczegółowić na jakiś przykładach” — na propozycję agenta (droga a); po przykładach: „wydaje mi się, że w wielu przypadkach dedykowane środowisko testowe, które nie powstaje od zera przy każdym PR jest dużo lepsze mimo, że przysparza też innych problemów”; „b jest spoko” — na nowe brzmienie pozycji danych (droga b) przedstawione w rozmowie doprecyzowania.
- Pytanie 6: czy w trzech pozycjach drogi agenta to, czy agent może z opcji korzystać, jest konsekwencją ważoną jak każda inna, skoro WAY-137 pozwala, by o tym, jak dobrze agent pracuje z opcją, decydowało tylko rozstrzygnięcie remisu przy miejscu uruchomienia?
  - Answer: tak — w trzech pozycjach drogi agenta to, czy agent może z opcji korzystać, jest konsekwencją dla produktu: opcja, z której agent nie skorzysta, zostaje w porównaniu (WAY-122) z brakiem opisanym jako „agent nie sprawdzi w ten sposób działającego produktu”, a rekomendacja ją omija; reguła remisu z WAY-137 zostaje przy miejscu uruchomienia. Odrzucone: nic nie dopisywać i zostawić zwykłe ważenie konsekwencji (agent może zarekomendować tańszą usługę bez drogi dla agenta, bo „wygoda agenta rozstrzyga tylko remis”, i pozycja przechodzi bramkę z odpowiedzią, która agentowi nic nie daje).
  - Source: Mariusz, 2026-10-17: „a” — na drogę a przedstawioną w rozmowie doprecyzowania; WAY-137/1, `foundations/decisions.md:4165-4170`, `foundations` `e7f7c3a`.
- Pytanie 7 (rewizja po przeglądzie PR #23): gdzie ma stać gwarancja, że agent ma drogę do działającego produktu — w każdej definicji projektu (trzy obowiązkowe pozycje i bramka, jak w PR #23), w doprecyzowaniu każdego zadania, czy w samym kroku technologii?
  - Answer: w samym kroku technologii — logi, interfejs i dane deweloperskie to trzy sprawy, które `settle-technology` sprawdza, szukając wyborów potrzebnych projektowi; na liście stają tylko wtedy, gdy projekt ich potrzebuje, a fundament ich nie rozstrzyga. Odrzucone: trzy obowiązkowe pozycje w każdej definicji ze sprawdzeniem bramką (powtarza w każdym projekcie fakt ustalany raz na produkt); pytanie w doprecyzowaniu każdego zadania (zapisywanie trzech informacji w każdym zadaniu „tylko dlatego, że bo tak”). Pytanie kontrolne: czy odpowiedź trzyma się, skoro krok technologii działa dziś tylko przy definicji projektu, a zadania niezależne i zatwierdzona definicja loop2 przez niego nie przechodzą? Trzyma się — gdy zadanie będzie potrzebować technologii (np. logów po wytycznych do obserwowalności), sięgnie po `settle-technology`; tę ścieżkę z zadań do kroku technologii niesie osobne zadanie z backlogu („wybór stacku, którego definicja projektu nie rozstrzygnęła […] wraca do `settle-technology`”), poza zakresem tego.
  - Source: Mariusz, 2026-10-18: „te 3 punkty powinny trafić aby do weryfikacji przez /the-way-settle-technology i tyle; w projekcie zadania nie widzę potrzeby zapisywać zawsze takich 3 informacji tylko dlatego, że bo tak” — po przeglądzie PR #23; na pytanie kontrolne: „jeśli pojawi się potrzeba zadbania o logi, a nie będzie do nich technologii, to wtedy sięgniemy po settle-technology tak jak już sięgamy przy zadaniach, które zahaczają o stack”, „a nie mam zapisanego w obsidianie zadania, żeby to settle-technology właśnie dopiąć do zadań?”, „tak, zapisz”; `project-level/technology/SKILL.md:2-3, 24-25`, `foundations` `77c8a8b`.
- Pytanie 8: według jakiej reguły któraś z trzech spraw trafia na listę, gdy krok technologii ją sprawdza — zwykłą regułą przynależności z WAY-121 czy własnym kryterium?
  - Answer: własnym kryterium — sprawa trafia na listę, gdy projekt wnosi zachowanie, które użytkownik zobaczy w działającym produkcie, a fundament nie ma decyzji, jak agent do niego dotrze; to wyjątek od reguły przynależności z WAY-121, nazwany wprost. Pierwszy projekt produktu ustala tak do trzech krótkich decyzji, kolejne znajdują je w fundamencie i nic nie wpisują. Odrzucone: zwykła reguła WAY-121 (tanie i najczęstsze odpowiedzi — przeglądarka na lokalnym adresie, logi z wyjścia kontenera — nie dokładają nic do utrzymania ani nie zmieniają podziału pracy, więc nigdy nie zostałyby zapisane i sprawdzenie nic by nie dawało).
  - Source: Mariusz, 2026-10-18: „a” — na drogę a przedstawioną w rozmowie doprecyzowania; WAY-121/1, `foundations/decisions.md:3432-3434`, `foundations` `77c8a8b`.

## Context

- Źródło: lekcja „Towards Autonomous Product Development” (Adam Gospodarczyk, harness Limen w wersji `e746877`), wiersz A1 w `C:\Storage\The Brain\The Brain\Notes\Areas\(A) Learning\mapa_artykulow.md`: „przejmuję (the way) — krok technologii (WAY-121) dostaje obowiązkową pozycję „jak agent widzi działający produkt: logi, interfejs, dane deweloperskie”; bez niej cykl wymaga sprawdzenia, do którego agent może nie mieć drogi”; stan wątku w `wznowienie_limen_zmiany_w_the_way.md` obok tego dokumentu, punkt 4. Po przeglądzie PR #23 pozycja nie jest obowiązkowa (pytania 7 i 8).
- Dziś w cyklu: „For visible behavior, verify it in the running product as well.” — `task-cycle/skill/SKILL.md:339-340`, `foundations` `77c8a8b`.
- Werdykt A1 przejmuje z elementu artykułu tylko pytanie o drogę agenta; „twarda granica (bez produkcyjnej bazy i roota)” z opisu elementu A1 nie jest przejęta.
- Pierwsza wersja zadania była wdrożona w PR https://github.com/mariusznazar/the-way/pull/23, zamkniętym bez scalenia po przeglądzie: obowiązkowe trzy pozycje ze znacznikami `logs:`, `interface:`, `development data:`, warunek bramki, zmieniony niezmiennik `project-technology-record`, powrót zatwierdzonych definicji, nowa WAY-165. Ta wersja idzie nowym cyklem od `foundations`; z PR #23 nic nie przechodzi.
- Przykłady odpowiedzi w trzech sprawach dla loop2: logi — agent czyta `docker compose logs api`; interfejs — agent obsługuje grę na `localhost:3000` w przeglądarce; dane — skrypt zakłada konta testowe ze świeżym zapisem, zapisem z połowy gry i oczekującym resetem hasła. Inne przykłady danych: narzędzie z linii poleceń bez danych — przykładowe pliki wejściowe w repozytorium; sklep z dużą bazą — dane generowane skryptem, kopia produkcji bez danych osobowych (sięgnięcie do produkcji to czynność człowieka, WAY-140) albo trwałe dedykowane środowisko testowe.
- Słowo „surface” ma w słowniku the way węższe znaczenie („something of a product that someone outside the product relies on and that the product promises to keep”, `foundations/glossary.md:196-198`), więc nie nazywa interfejsu z pozycji, którym jest droga użytkownika do obsługi produktu.
- Przed `main` istniejącą decyzję edytuje się w miejscu, a zmianę znaczenia pokazuje Mariuszowi (`agent-instructions/README.md:20-23`); od WAY-121 zależą WAY-122, WAY-123 i niezmiennik `project-technology-record`.

## Questions carried to cycle

- Gdzie w `settle-technology` stoi sprawdzenie trzech spraw (krok 1, w którym krok wylicza wybory potrzebne projektowi, `project-level/technology/SKILL.md`) i jak krok wznawia definicję w trakcie, której lista powstała przed tą zmianą.

## Human actions

none

## Decisions in play

Przeszukanie: decyzje z *Scope* `project-level` albo `task-cycle` w `foundations/decisions.md` na `foundations` `77c8a8b`, niezmienniki wyprowadzone z WAY-121–123 i WAY-137–139 oraz wyszukanie słów „log”, „logging”, „running product”, „interface”, „seed”, „test data”, „development data”, „browser”, „agent works with” we wszystkich pięciu plikach fundamentu. Żadna decyzja nie ustala, jak agent dociera do działającego produktu; zadanie nie koliduje z żadną decyzją, a zmienia WAY-121.

- WAY-121/1 — „A choice belongs on the list when settling it later could change how the work is cut into tasks, or when it adds something the product has to run, pay for or back up; a choice one task can make and change alone stays with that task.” Trzy sprawy trafiają na listę według własnego kryterium, także poza tą regułą (pytanie 8).
- `project-technology-record/1` — „Before approval, the project readiness check rejects a definition whose Technology section is missing or reads `none`, or holds a line that is no choice item, a choice still open, or a choice that names neither a decision as `<PREFIX>-<NN>/<version>` nor a question a heading of a projected decision holds.” Bez zmiany znaczenia (pytanie 7); odnawia się tylko odcisk relacji do WAY-121.
- WAY-122/1 — „every option is offered only after a critique that refutes every claimed difference between the options which no source supports”; z *Rationale*: „A place to run or a way of logging in has no types and no language family, so it is weighed by its consequences alone”. Trzy sprawy, gdy stoją na liście, przechodzą badanie i krytykę jak każdy wybór, a opcja bez drogi dla agenta zostaje w porównaniu z tym brakiem (pytanie 6).
- WAY-123/1 — „shows the options of each choice by their consequences for the product — what it costs, where it runs, what keeping it running takes and what changing it later costs”. Tu wychodzą problemy trwałego środowiska testowego (pytanie 5).
- WAY-137/1 — „For a place to run, how well an agent works with an option decides nothing else: it leaves no option out of the comparison and is weighed against no consequence for the product.” W trzech sprawach to, czy agent może z opcji korzystać, jest konsekwencją (pytanie 6); reguła dla miejsca uruchomienia zostaje.
- WAY-138/1 — „tests the option it recommends for each choice it settles […] with a devil's advocate, a pre-mortem and a search for unknown unknowns”. Obejmuje trzy sprawy, gdy krok je rozstrzyga.
- WAY-139/1 — skill wdrożeniowy produktu obejmuje m.in. „what the agent does and what the human does; and how to read the logs”, a sprawdza to tylko zadanie, które „deploys the product or changes how or where it runs”. Sprawa logów ustala, gdzie logi trafiają i jak agent je czyta; skill wdrożeniowy opisuje ich czytanie przy wdrożeniu — bez kolizji.
- WAY-140/1 — „reading outside the repository stays with the agent”, a każdy skutek poza repozytorium — konto usługi logów, dane na serwerze testowym — robi człowiek. Dotyczy zadań produktu, które budują wybraną drogę, nie tego zadania.
- WAY-143/1 — „A technical element enters the plan with the first task that uses it, or with a preparatory task that task depends on.” Drogę agenta buduje pierwsze zadanie planu, które z niej korzysta, nie zadanie stawiające logi na zapas.
- WAY-100/1 — „A method or practice borrowed from outside a product binds its way of working only through a decision that names what is adopted, where it applies, and why.” Zmiana WAY-121 nazywa, co przejmuje z lekcji „Towards Autonomous Product Development”, gdzie i dlaczego.
- WAY-106/1 — krok technologii zapisuje wyłącznie do definicji projektu (`project-level/technology/SKILL.md:24-25`); zadania dochodzą do niego osobnym zadaniem z backlogu (pytanie 7).
- WAY-04/1 — *Rejected*: „as elements of their own — […] the agent's environment and the return step (the task cycle)”. Trzy sprawy kończą się decyzjami produktu, nie nowym elementem fundamentu — bez kolizji.

## Settlements to record

Candidates: 6 shown, 4 accepted — 2026-10-18

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Krok technologii, szukając wyborów potrzebnych projektowi, sprawdza trzy osobne sprawy drogi agenta do działającego produktu — logi, interfejs, dane deweloperskie — i stawia każdą na liście jako osobny wybór, gdy projekt wnosi zachowanie, które użytkownik zobaczy w działającym produkcie, a fundament nie ma decyzji, jak agent do niego dotrze, także gdy niczego nie dokłada do utrzymania; produkt, który którejś z tych rzeczy nie ma, też dostaje odpowiedź (np. „interfejsem jest wyjście programu”). | decision | To do 1; odpowiedzi na pytania 3, 7 i 8 | czy krok w ogóle pyta o te trzy sprawy, czy stawia je na liście tylko według zwykłej reguły WAY-121, i czy trzy sprawy to jeden wybór, czy trzy |
| 2 | Pozycja logów pyta, gdzie trafia zapis tego, co działający produkt robi, i jak agent go czyta; pozycja interfejsu — jak agent obsługuje produkt tak, jak robi to jego użytkownik (ekran w przeglądarce, wywołanie API, polecenie w terminalu), i jak widzi, co produkt mu odpowiada. | decision | odpowiedź na pytanie 5 | o co pytają te pozycje — czy interfejsem może być dostęp do bazy z pominięciem aplikacji |
| 3 | Pozycja danych deweloperskich pyta, skąd biorą się dane, na których agent sprawdza zachowanie produktu poza produkcją, i jak agent dochodzi do stanu danych, którego sprawdzenie potrzebuje, bez przesądzania, czy to dane zakładane od zera, czy trwałe dedykowane środowisko testowe. | decision | odpowiedź na pytanie 5 | czy pozycja danych wymaga danych odtwarzanych od zera, czy wystarcza trwałe środowisko testowe |
| 4 | W każdej z trzech pozycji drogi agenta to, czy agent może z opcji korzystać, jest konsekwencją dla produktu: opcja, z której agent nie skorzysta, zostaje w porównaniu, z brakiem opisanym jako „agent nie sprawdzi w ten sposób działającego produktu”, a rekomendacja ją omija; reguła z WAY-137, w której przy remisie miejsc uruchomienia wygrywa to, z którym agent pracuje najlepiej, zostaje przy miejscu uruchomienia. | decision | odpowiedź na pytanie 6 | czy zarekomendować tańszą usługę logów z samym panelem w przeglądarce, bo według WAY-137 wygoda agenta rozstrzyga tylko remis |

## Out of scope

- Ścieżka z doprecyzowania zadania do kroku technologii — osobne zadanie w backlogu (pytanie 7).
- Skill do testowania zakresu, którego nie pokrywają skrypty (na wzór `test-run`) — osobne zadanie w backlogu.
- Okresowy przegląd fundamentu liczony scaleniami (zmiana 3) — osobne zadanie w backlogu.
- Reguły tego, co produkt loguje i w jakiej postaci (wytyczne do konstruowania obserwowalności produktu) — osobne zadanie w backlogu, odpowiedź na pytanie 1.

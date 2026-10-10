---
title: "the way: wpisać przejęcia z lekcji m1l5 kursu 10xDEVS"
status: draft
created: 2026-10-10
updated: 2026-10-10
tags: []
related: "[[(P) Proces pracy nad produktem]]"
---

# the way: wpisać przejęcia z lekcji m1l5 kursu 10xDEVS — remis przy miejscu uruchomienia, testy „co to zepsuje”, lista elementów skilla wdrożeniowego produktu, skutki zadania poza repozytorium

Status: ready for cycle
Project relation: independent

## Description

### Need

- Cztery wiersze „przejmuję w zmienionej postaci” z lekcji m1l5 (wiersze 2, 3, 6 i 10 w [[mapa_pakietu_10x]]) czekają na wpisy w dzienniku decyzji the way.
- Bez nich krok technologii nie ma reguły na remis przy miejscu uruchomienia ani testu skutków opcji zalecanej, the way nie mówi, co ma umieć skill wdrożeniowy produktu, a dokument zadania nie nazywa skutków zadania poza repozytorium.

### To do

1. Krok technologii (`settle-technology`): przy miejscu uruchomienia przyjazność dla agenta — obsługa z terminala, skryptowalne wdrożenie, dokumentacja czytelna dla agenta — jest ostatnim kryterium rozstrzygającym remis, nie filtrem ani główną wagą.
    - reguła WAY-123 zostaje bez zmian; przyjazność dla agenta rozstrzyga dopiero wtedy, gdy po niej nadal jest remis
2. Krok technologii: testy „co to zepsuje” — adwokat diabła, pre-mortem, nieznane niewiadome — na opcji zalecanej.
    - tylko dla wyborów rozstrzyganych w tym projekcie, także wziętych z ograniczenia
    - wyborów trzymanych przez zastane decyzje (`held by`) test nie dotyka i nie uzupełnia się ich wstecz
    - ryzyka z testów człowiek widzi przed wyborem, w tabeli przy opcji zalecanej; wybierając ją, przyjmuje jej ryzyka
    - przyjęte ryzyka idą do decyzji kanałem braków wybranej opcji (krok 7 `settle-technology`), oznaczone jako hipotezy
3. Spisać listę elementów, które skill wdrożeniowy produktu powinien mieć: podgląd wdrożeń; gdzie leżą sekrety i jak je obracać; cofanie (ile kroków, co z danymi); co robi agent, a co człowiek; jak czytać logi.
    - the way skilli produktu nie zawiera, tylko tę listę
    - lista stoi w zdaniu wiążącym decyzji; czyta ją doprecyzowanie zadania (`refine-task`): gdy wynik zadania wdraża produkt albo zmienia, jak i gdzie produkt działa, sprawdza, czy produkt ma skill wdrożeniowy pokrywający listę; jeśli nie ma albo czegoś brakuje, zadanie dostaje taki punkt albo człowiek wydziela go w osobne zadanie
4. Skutek zadania poza repozytorium (serwer, DNS, klucze, zewnętrzne konto) nie zapada w cyklu bez człowieka: dokument zadania nazywa każdy jako czynność człowieka — przed cyklem albo w cyklu.
    - przed cyklem: zadanie nie jest gotowe, dopóki człowiek jej nie zrobi (WAY-124)
    - w cyklu: cykl robi, co da się zrobić w repozytorium, i oddaje zablokowany PR z listą czynności; człowiek wykonuje je przy PR-ze (WAY-125)
    - czy czynność idzie przed cyklem, czy w cyklu, rozstrzyga człowiek przy doprecyzowaniu zadania, dla każdej czynności; agent proponuje: przed cyklem, gdy kod cyklu potrzebuje skutku czynności (konto, klucz, baza); w cyklu, gdy czynność korzysta z kodu, który cykl napisze (wdrożenie, DNS na nowy adres)
    - odczyty poza repozytorium zostają agentowi
5. Każde z przejęć 1–4 wpisać do dziennika decyzji the way (nowa decyzja albo zmiana obecnej) razem ze zmianą skilli i szablonów, które je wykonują.
6. Po scaleniu, poza cyklem (czynność człowieka albo sesji domykającej zadanie — mapa leży poza repozytorium): w wierszach 2, 3, 6 i 10 m1l5 w [[mapa_pakietu_10x]] wpisać w kolumnie nośnika numery decyzji WAY i zaktualizować wiersz stanu lekcji.

### Questions to settle

- 0. Jedno zadanie czy podział — przejęcia 1–2 zmieniają krok technologii (poziom projektu), 4 — dokument zadania i cykl, 3 — zależy od pytania 1.
  - Answer: jedno zadanie (Mariusz).
- 1. Gdzie stoi lista elementów skilla wdrożeniowego i który krok procesu ją czyta?
  - Answer: w zdaniu wiążącym decyzji; czyta ją doprecyzowanie zadania przy zadaniu, którego wynik wdraża produkt albo zmienia, jak i gdzie działa (Mariusz przyjął rekomendację; słaby punkt: pierwsze zadanie wdrożenia rośnie o skill wdrożeniowy).
- 3. Jak cykl „staje i czeka” na czynność człowieka w cyklu i kto rozstrzyga, czy czynność idzie przed cyklem, czy w cyklu?
  - Answer: cykl nie staje w środku — oddaje zablokowany PR z listą czynności, człowiek wykonuje je przy PR-ze; „przed” czy „w cyklu” rozstrzyga człowiek przy doprecyzowaniu, z propozycją agenta według reguły w punkcie 4 (Mariusz przyjął rekomendację; słaby punkt: sprawdzenie kodu po czynności wypada w rundzie poprawek po PR-ze).

## Context

- Werdykty, uzasadnienia i dowody z wypróbowań A (`10x-infra-research`) i B (Plan Mode): [[mapa_pakietu_10x]], sekcja „m1l5”, wiersze 2, 3, 6, 10 i Notatki.
- Dowód do przejęcia 1: w wypróbowaniu A trzy platformy z kompletem 24/24 punktów przyjazności odpadły na wymaganiach stacku, a wygrał Mikrus z 12/24 kosztem — kryteria same niczego nie rozstrzygnęły.
- Kolejność „najtańsza, skutki dla produktu, najprostsza, przyjazność dla agenta” z wiersza 2 mapy dotyczy tylko `loop2`; krok technologii o kolejność nie pyta (Mariusz).
- Dowód do przejęcia 2: testy na Mikrusie dały ryzyka nieobecne w definicji MVP `loop2` (brak pamięci przy budowie na serwerze zabija starą grę, nagłówki pośrednika HTTPS, klucz MCP o uprawnieniach roota); krytyka WAY-120 sprawdza prawdziwość porównania, nie skutki wyboru.
- Dowód do przejęcia 3: sekcja obsługi na co dzień w `infrastructure.md` z wypróbowania A była konkretna, ale w dokumencie, którego potem nic nie czyta; Mariusz: „jak to robić” żyje w skillach produktu.
- Dowód do przejęcia 4: plan z wypróbowania B wypisał ręczne kroki człowieka dopiero na żądanie promptu `m1l5-3`.
- Słaby punkt przejęcia 4 nazwany w wierszu 10: granica odczyt/zmiana nie zawsze jest ostra — moduł `/db` API Mikrusa nic nie zmienia, ale zwraca hasła.
- Skill cyklu już dziś mówi, że cykl „changes nothing outside the product repository”, a skutek zewnętrzny traktuje jak operację nieodwracalną tylko wtedy, gdy reguły produktu zastrzegają go człowiekowi: `task-cycle/skill/SKILL.md:46` i `:66–69`; żadna decyzja tego nie niesie.
- Skill cyklu ma jeden zwykły kontakt z człowiekiem — PR — i nie zatrzymuje się w trakcie; gdy kod nie może iść dalej bez decyzji zastrzeżonej człowiekowi, cykl przygotowuje zablokowany szkic PR z dowodami i kończy: `task-cycle/skill/SKILL.md:15–21`.
- Pierwszy użytkownik przejęć 3 i 4: zadanie wdrożenia szkieletu `loop2` w `(P) Loop`.
- Wzór zadania z przejęciami jednej lekcji: [[pliki_instrukcji_dla_agentow_w_the_way]] (m1l4, sześć wierszy w jednym zadaniu).
- Zmiana idzie trasą `agent-instructions/README.md`: gałąź zadania od `foundations`, sprawdzenia, przeszukanie fundamentu (WAY-33), jedna niezależna ocena (WAY-10), PR do `foundations`, scala Mariusz.

## Questions carried to cycle

none

## Decisions in play

- **WAY-100/1** — „When does a method or practice borrowed from elsewhere bind a product?”:
    > A method or practice borrowed from outside a product binds its way of working only through a decision that names what is adopted, where it applies, and why.
- **WAY-121/1** — „Where does a project settle the technology it needs?”, fragment:
    > … lists the technology and architecture choices the project needs — such as a language, a framework, a store of data or a place to run — and settles each one the foundation does not already hold as a projected decision of the definition.
- **WAY-122/1** — „How are the options of a technology choice found and checked before a human sees them?”, fragment:
    > … every option is offered only after a critique that refutes every claimed difference between the options which no source supports.
    - z *Rationale*: „A place to run or a way of logging in has no types and no language family, so it is weighed by its consequences alone and checked by the critique.” — przejęcie 1 dokłada miejscu uruchomienia kryterium spoza skutków.
- **WAY-123/1** — „How does a technology choice reach a human who cannot assess the technology?”, fragment:
    > A difference with no consequence for the product decides nothing, and where no difference with a consequence remains, the step recommends the simplest and cheapest option. The choices whose research started together reach the human together, in one table, once every one of their comparisons has passed the critique, each with its recommendation and the weak point of the option recommended.
    - przejęcie 1 dokłada po tej regule ostatni szczebel przy miejscu uruchomienia, samej reguły nie zmienia; przejęcie 2 dokłada test na opcji zalecanej — zmiana sensu, ponowna akceptacja Mariusza (WAY-07).
- **WAY-120/1** — „How does the-way critique an agent's proposal?” — ryzyka z testów przejęcia 2 to hipotezy bez źródła, a krytyka odrzuca twierdzenia bez źródła.
- **WAY-124/1** — „When is a task ready for its cycle?”, fragment:
    > It is ready when its required outcome is stated, every known question blocking that outcome is answered, the human has accepted or rejected every candidate settlement its refinement found, and implementation questions carried into the cycle are named.
    - przejęcie 4 dokłada warunek: czynność człowieka przed cyklem wykonana.
- **WAY-125/1** — „Which Superpowers methods does the autonomous task cycle adopt?”, fragment:
    > Decisions reserved to a human by the foundation remain reserved; when required code cannot proceed without one, the cycle opens a blocked draft request; …
    - przejęcie 4 dotyczy czynności, nie decyzji — reguła mówi dziś tylko o decyzjach.

## Settlements to record

Candidates: 10 shown, 5 accepted — 2026-10-10

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Przy miejscu uruchomienia przyjazność dla agenta — obsługa z terminala, skryptowalne wdrożenie, dokumentacja czytelna dla agenta — jest ostatnim kryterium rozstrzygającym remis, nie filtrem ani główną wagą: rozstrzyga dopiero, gdy po regule WAY-123 (najprostsza i najtańsza) nadal jest remis; zostaje, choć zwykle nie zadziała, bo chroni przed wejściem przyjazności dla agenta wyżej, jako filtr albo waga, jak robi to kurs. | decision | To do 1; odpowiedź na pytanie 2; odpowiedź Mariusza na pytanie kontrolne (reguła zostaje) | czy przyjazność dla agenta filtruje opcje, waży je, czy rozstrzyga remis, i czy przy tym przepisać regułę WAY-123 |
| 2 | Testy „co to zepsuje” — adwokat diabła, pre-mortem, nieznane niewiadome — idą na opcji zalecanej, tylko dla wyborów rozstrzyganych w tym projekcie, także wziętych z ograniczenia; wyborów trzymanych przez zastane decyzje test nie dotyka i nie uzupełnia się ich wstecz; ryzyka z testów człowiek widzi przed wyborem, w tabeli przy opcji zalecanej, a przyjęte idą do decyzji kanałem braków wybranej opcji, oznaczone jako hipotezy; zakres wraca do przeglądu, gdy testy na wyborze innym niż miejsce uruchomienia nie dadzą ryzyka, którego nie miało porównanie — wtedy zawęża się do miejsca uruchomienia. | decision | To do 2; odpowiedź Mariusza „przed wyborem, zakres niech na razie zostanie”; warunek przeglądu przyjęty na pytaniu kontrolnym | na których wyborach i opcjach robić testy, czy pokazać ryzyka przed wyborem, i gdzie zapisać te, których krytyka nie przepuści bez źródła |
| 3 | The way skilli produktu nie zawiera, tylko listę elementów, które skill wdrożeniowy produktu powinien mieć — podgląd wdrożeń; gdzie leżą sekrety i jak je obracać; cofanie (ile kroków, co z danymi); co robi agent, a co człowiek; jak czytać logi — w zdaniu wiążącym decyzji; doprecyzowanie zadania, którego wynik wdraża produkt albo zmienia, jak i gdzie działa, sprawdza, czy produkt ma skill wdrożeniowy pokrywający listę, i jeśli nie ma albo czegoś brakuje, zadanie dostaje taki punkt albo człowiek wydziela go w osobne zadanie. | decision | To do 3; odpowiedź na pytanie 1 | gdzie zapisać listę, kto i kiedy ją czyta, i czy the way ma dostarczyć gotowy skill wdrożeniowy |
| 4 | Skutek zadania poza repozytorium (serwer, DNS, klucze, zewnętrzne konto) nie zapada w cyklu bez człowieka: dokument zadania nazywa każdy jako czynność człowieka — przed cyklem (zadanie nie jest gotowe, dopóki człowiek jej nie zrobi) albo w cyklu (cykl robi, co da się zrobić w repozytorium, i oddaje zablokowany PR z listą czynności, a człowiek wykonuje je przy PR-ze); odczyty poza repozytorium zostają agentowi. | decision | To do 4; odpowiedź na pytanie 3 | czy cykl może sam zmienić coś poza repozytorium albo zatrzymać się w środku i czekać na człowieka |
| 5 | Czy czynność człowieka idzie przed cyklem, czy w cyklu, rozstrzyga człowiek przy doprecyzowaniu zadania, dla każdej czynności; agent proponuje „przed”, gdy kod cyklu potrzebuje skutku czynności, a „w cyklu”, gdy czynność korzysta z kodu, który cykl napisze. | decision | To do 4; odpowiedź na pytanie 3 | czy agent doprecyzowujący sam przydziela czynności i według jakiej reguły |

## Out of scope

- Skill wdrożeniowy `loop2` i samo wdrożenie szkieletu `loop2` — zadanie w `(P) Loop`.
- Zakres uprawnień agenta do serwera (wiersz 13 m1l5, otwarty z warunkiem powrotu).

---
title: "the way: limit lektury kawałka planu spada do 150 tys. tokenów"
status: draft
created: 2026-11-12T22:10
updated: 2026-11-13
tags: [zadanie]
related: "notatka projektu procesu pracy nad produktem"
---

# the way: limit lektury kawałka planu spada do 150 tys. tokenów

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Skrypt rozmiaru kawałka planu (`task-cycle/slice_size.py`) uznaje kawałek za za duży, gdy jego wykonawca ma do przeczytania ponad 250 tys. tokenów; z 220 kawałków gry z zachowanym szacunkiem lektury żaden tego limitu nie przekroczył.
- W grze kawałki z planowaną lekturą 150–250 tys. tokenów kończą ponad 100 wywołaniami modelu w 23–29% przypadków, kawałki poniżej 150 tys. — w 3–4%.
- Kawałki gry z planowaną lekturą powyżej 150 tys. zużywają przy pisaniu zmiany ok. 21 tys. tokenów wejścia na zmienioną linię, kawałki z lekturą 50–150 tys. — 13–16 tys.
- Limit 150 tys. objąłby 20 z 220 kawałków gry (9%), wśród nich 5 z 10 długich przebiegów wykonawców; te 20 kawałków zużyło 25% tokenów wejścia wszystkich wykonawców kawałków gry.
- Koszt długich przebiegów ponosi Mariusz, który płaci za cykle; nic się przy tym nie psuje — zmiany przechodzą przegląd i bramkę.
- Pomysł, by wybór między jednym autorem a planem na starcie cyklu dostał miarę rozmiaru (np. liczbę plików), odpadł przy doprecyzowaniu: przy podobnym rozmiarze zmiany cały cykl z planem kosztował więcej na linię niż cykl jednego autora; bez zapisu w decyzji ten sam pomysł wróci przy następnej analizie kosztów.

### To do

1. Limit lektury kawałka w skrypcie rozmiaru (`READ_LIMIT_TOKENS` w `task-cycle/slice_size.py`) wynosi 150 tys. tokenów zamiast ćwierci okna kontekstu (250 tys.).
2. Opis skryptu w akapicie o limitach (ten, który zaczyna się od „The limits start with a wide margin”) uzasadnia nową wartość pomiarem opisanym słowami i liczbami z *Need*, w miejsce zdania „READ_LIMIT_TOKENS is a quarter of that window”, i nie wskazuje źródła pomiaru, do którego czytelnik repozytorium nie sięgnie (WAY-27).
3. Decyzja WAY-136 dostaje w *Rejected* wariant: miara rozmiaru zmiany, taka jak liczba plików, rozstrzygająca na starcie cyklu o wyborze między jednym autorem a planem. Powód opisany słowami i liczbami (WAY-27): na zmianach gry o rozmiarze 1 500–3 000 linii, po 5 cykli na drogę, cały cykl z planem kosztował 0,0182 USD na zmienioną linię (mediana cyklu 39 USD), a cykl jednego autora 0,0157 USD (mediana 24 USD), bo plan dopłaca za planistę, przeglądy kawałków i krok zwrotny osobnym agentem.

### Questions to settle

- Czy pierwsza część zadania — miara rozmiaru przy wyborze między jednym autorem a planem — zostaje?
  - Answer: Część odpada; zadanie zostaje przy limicie lektury kawałka, a tytuł zmienia się na „the way: limit lektury kawałka planu spada do 150 tys. tokenów”.
  - Not chosen:
    - część czeka na więcej porównywalnych cykli, a obniżenie limitu idzie teraz — osobne zadanie wisi bez daty, a na dziś nie ma danych, że miara cokolwiek oszczędzi
  - Source: doradca dnia w imieniu Mariusza, 2026-11-13: „1 a”; wcześniej w opisie zadania (Mariusz, 2026-11-12): „Jeśli po doliczeniu różnica znika, pierwsza część odpada i zostaje druga.”
- Czy odrzucenie miary rozmiaru przy wyborze drogi zapisać w decyzji WAY-136, wśród odrzuconych wariantów?
  - Answer: Tak — *Rejected* decyzji WAY-136 dostaje ten wariant z powodem z porównania kosztu całych cykli (punkt 3).
  - Not chosen:
    - wniosek zostaje tylko w notatce z pomiarami — agent czytający WAY-136 go nie zna i może zaproponować to samo jeszcze raz
  - Source: doradca dnia w imieniu Mariusza, 2026-11-13: „2 a”
- Jaka wartość limitu lektury kawałka?
  - Answer: 150 tys. tokenów.
  - Not chosen:
    - 175 tys. — 10 kawałków gry do podziału (5%), 3 z 10 długich przebiegów, 12% tokenów wejścia wykonawców
    - 125 tys. — 34 kawałki do podziału (15%), te same 5 z 10 długich przebiegów co przy 150 tys., 34% tokenów wejścia wykonawców; o 14 kawałków więcej do podziału bez ani jednego długiego przebiegu więcej
  - Source: doradca dnia w imieniu Mariusza, 2026-11-13: „3 a”

## Context

- Pomiar długich przebiegów: sekcja 4 notatki prywatna notatka z pomiarami i sondami przed zmianami procesu; karta D28 w prywatna notatka z kartami usprawnień the way.
- Porównanie kosztu całych cykli na obu drogach (2026-11-13, przy doprecyzowaniu): koszt cyklu w dolarach według cennika z danych audytu (kolumna `cost` pliku cykli audytu, wszystkie etapy razem z agentem prowadzącym), rozmiar zmiany z gita jako linie dodane i usunięte bez zapisu cyklu; skrypty i wyniki `p5_*` w katalogu danych tej prywatnej notatki.
- Gra, zmiany 1 500–3 000 linii: jeden autor — 5 cykli, mediana 1 808 linii i 19 plików; plan — 5 cykli, mediana 1 934 linii i 24 plików.
- Gra, jeden autor przy zmianach ponad 10 plików: 0,018–0,020 USD na linię; cała droga z planem: 0,0145 USD na linię, ale przy medianie 5 400 linii, a koszt na linię spada z rozmiarem zmiany na obu drogach.
- Udział etapów w koszcie cykli gry: na drodze z planem planista 8%, przeglądy kawałków 7%, krok zwrotny osobnym agentem 14%, spec 5%; na drodze jednego autora krok zwrotny 8%, a pisanie zmiany 29% wobec 22% na drodze z planem.
- Szacunek, nie pomiar: gdyby kawałki z lekturą powyżej 150 tys. po podziale pisały jak kawałki 50–150 tys., zużyłyby przy pisaniu ok. 30% mniej tokenów wejścia.
- W the way kawałki z planowaną lekturą powyżej 150 tys. to 2 z 39; nowy limit prawie niczego tam nie zmienia.
- Limit 150 tys. pochodzi z jednego produktu: 220 kawałków gry.
- Źródło pomiaru leży w prywatnych notatkach, więc wpisy fundamentu z tego zadania opisują pomiar w sobie, jak uzasadnienie WAY-229 (WAY-27); ogólną zasadę dla takich pomiarów ustala osobne zadanie osobne zadanie o pomiarach z prywatnego źródła.
- Zmiana limitu nie zaczyna nowej serii miar audytu: WAY-339 wymienia jako początek serii nowy cennik, zmianę formy raportu etapu, listy klas i instrukcji recenzenta.
- Test skryptu (`task-cycle/test_slice_size.py`, asercja z `["250000", "fits"]`, ok. linii 83) sprawdza dziś granicę 250 000 i 250 001 tokenów.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-136 — When does a task's change need a plan, and who makes and reviews it?** „A change that, as the orchestrator judges before implementation from the task document and, where the task moves the pin, from the checks the move breaks (WAY-34), one agent can hold is made without a plan by one author (…); an author that finds the change too large returns a report without code, its attempt is discarded with the foundation entries it wrote, and a planner divides the change. Every other change gets a plan written with the-way's skill `plan-task`, which divides it into slices and holds no code; (…) a slice that proves too large for it is discarded with its code and goes back to the planner to be split.” Zadanie zmienia tę decyzję: jej *Rejected* dostaje wariant z punktu 3 — zgoda Mariusza (przez doradcę dnia) z 2026-11-13: „2 a”.
- **WAY-229 — On which class of model do the executor of a slice and the one author work?** „The executor of a slice, and the one author of a change without a plan, work on the class of model set for them (…): by default a class cheaper than the orchestrator's (…); the orchestrator's class, for a change across many parts; or the strongest class available, for one that needs design.” Zadanie jej nie zmienia.
- **WAY-27 — Where may this repository point for its reasoning?** „Nothing in this repository points to a source outside it that its readers cannot reach: every entry carries its whole reasoning, and what is seen only in such a source is described in the entry instead of being pointed to.” Dlatego opis skryptu i WAY-136 opisują pomiar zamiast do niego odsyłać (punkty 2 i 3).
- **WAY-328 — Does the-way hold its own code and tests to the general coding guidelines and the testing guidelines of a product?** „The-way departs, for its own code and its own tests, from the general coding guidelines and from the testing guidelines of a product, under WAY-217 (…).” Część `task-cycle` jest w jej zakresie, więc zadanie nie czeka na wytyczne.

## Settlements to record

Candidates: 3 shown, 2 accepted — 2026-11-13

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Wybór między jednym autorem a planem zostaje osądem z dokumentu zadania, bez miary rozmiaru; miara rozmiaru rozstrzygająca o drodze stoi wśród odrzuconych wariantów WAY-136, z kosztem całych cykli jako powodem (zmienia WAY-136). | decision | pytania 1 i 2 pod *Questions to settle* (wybór Mariusza) | czy WAY-136 dostaje odrzucony wariant i z jakim powodem, czy zostaje bez zmian |
| 2 | Limit lektury kawałka planu wynosi 150 tys. tokenów, nie 175 ani 125 tys. | decision | pytanie 3 pod *Questions to settle* (wybór Mariusza) | czy wartość wraz z odrzuconymi 175 i 125 tys. stoi tylko w opisie skryptu, czy jako decyzja w dzienniku |

## Out of scope

none

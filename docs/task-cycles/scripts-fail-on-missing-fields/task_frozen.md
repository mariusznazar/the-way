---
title: Skrypty the way sprawdzają swoje dane wejściowe i padają z nazwą brakującego pola, zamiast po cichu przepuszczać
status: draft
created: 2026-11-11T19:45
updated: 2026-11-11
tags: [zadanie]
related: "the author's project note for the process of work on a product"
---

## Po co to

- **Jak jest dziś:** Skrypty the way (dziś 18, m.in. kontrola formy requestu, uwag procesu, prywatnych ścieżek, planu i fundamentu) czytają pliki pisane przez agentów: raporty etapów, plany, opisy requestów. Żadna reguła nie wymaga, żeby skrypt sprawdzał, czy w czytanym pliku są pola, których oczekuje. Od 11.11 the way świadomie nie ma własnych wytycznych kodowania i testów (decyzja WAY-328), a ta decyzja sama nazywa cenę: nic z wytycznych produktu nie chroni kodu the way, a nowy kod kopiuje kod już istniejący.
- **Kto to odczuwa:** Mariusz i agenci cyklu — gdy agent zmieni format raportu albo planu, skrypt, który nie sprawdza pól, może przyjąć brak pola za „nic do zgłoszenia” i przepuścić zły wynik bez żadnego błędu. Nieustalone, czy to się już zdarzyło; Mariusz: „cały czas coś przepuszczamy, bo cały czas coś poprawiamy” — przy ciągłych zmianach nie da się tego ocenić jednoznacznie.
- **Co jeśli nic:** Nic nie psuje się dziś widocznie. Ryzyko: kontrola, która powinna zatrzymać cykl, po zmianie formatu przestaje cokolwiek łapać i nikt tego nie zauważa, dopóki Mariusz nie trafi na zły wynik sam.

## Po scaleniu

Przestawić nośnik w mapie lekcji the author's private map of the lessons of a course, lekcja s01e05, wiersz E5 — w kolumnie „nośnik” numer wpisu WAY zamiast linku do tego zadania.


# Skrypty the way sprawdzają dane wejściowe i padają z nazwą brakującego pola, zamiast po cichu przepuszczać

Status: ready for cycle
Project relation: independent

## Description

### Need

- the way ma 18 skryptów w Pythonie (bez plików testów), m.in. kontrolę formy opisu requestu, uwag procesu, prywatnych ścieżek, planu i fundamentu; część z nich czyta pliki pisane przez agentów albo człowieka: raporty etapów, plany, opisy requestów.
- Żadna decyzja ani niezmiennik the way nie wymaga, żeby skrypt sprawdzał, czy w czytanym pliku są pola, których potrzebuje.
- WAY-328 sama nazywa cenę odejścia od wytycznych kodowania i testów: nic z wytycznych produktu nie chroni kodu the way, a nowy kod kopiuje kod już istniejący.
- Gdy agent zmieni format raportu albo planu, skrypt, który nie sprawdza pól, może przyjąć brak pola za „nic do zgłoszenia” i przepuścić zły wynik bez błędu; kontrola, która miała zatrzymać cykl, przestaje cokolwiek łapać, dopóki Mariusz sam nie trafi na zły wynik.
- Nieustalone, czy to się już zdarzyło; Mariusz: „cały czas coś przepuszczamy, bo cały czas coś poprawiamy”.
- Odbiorcą jest Mariusz i agenci cyklu, którzy polegają na wyniku skryptów the way.

### To do

1. Dziennik decyzji the way (`foundations/decisions.md`) ma osobną decyzję, obok WAY-328, z regułą dla skryptów the way, która mówi:
   - skrypt, który czyta plik pisany przez agenta albo człowieka, sprawdza, czy są w nim pola, których potrzebuje; gdy którego brakuje albo stoi pod inną nazwą, kończy się błędem, który podaje nazwę tego pola; nie zgaduje i nie traktuje braku pola jak wartości pustej;
   - polem jest każda nazwana rzecz, po której skrypt szuka danych w pliku: nagłówek sekcji, etykieta wiersza, kolumna tabeli, klucz JSON;
   - reguła obowiązuje skrypt, który zmiana dodaje, a w skrypcie, który zmiana zmienia, cały odczyt pliku, którego sposób czytania zmiana przerabia — wszystkie pola tego pliku, nie pozostałe pliki i resztę skryptu;
   - przy brakującym polu skrypt kończy się kodem 2, a komunikat podaje plik i pole; w skrypcie, który istnieje po to, by sprawdzać formę pliku, brakujące pole, którego obecność sprawdza, zostaje ustaleniem jego listy z kodem 1;
   - każdy odczyt pliku objęty regułą ma jeden test, który podaje plik bez jednego z potrzebnych pól i sprawdza, że skrypt kończy się błędem z nazwą tego pola; za pozostałe pola odpowiada przegląd zmiany;
   - *Scope* decyzji wymienia wszystkie 16 części mapy części the way, a zmiana, która dodaje część do mapy, dopisuje ją do tego *Scope*.

### Questions to settle

- W jakiej formie reguła wchodzi do fundamentu the way?
  - Answer: (b) — osobna decyzja obok WAY-328, ze *Scope* wszystkich 16 części i zdaniem, że nowa część mapy dopisuje się do *Scope*; obejmuje tylko skrypty, które zmiana dodaje albo zmienia, i nie twierdzi niczego o istniejących; spokrewniona z WAY-38 jako reguła z tej samej rodziny.
  - Not chosen:
    - (a) wyjątek dopisany do WAY-328 — WAY-328 rozstrzyga, czy the way stosuje wytyczne produktu, a ta reguła jest wymogiem, nie odejściem; gdy WAY-328 zostanie wycofana po napisaniu własnych wytycznych, regułę trzeba przenosić, a do tego czasu agent piszący skrypt szuka zasad przy WAY-38 i niezmiennikach `script-*`, nie w decyzji o odejściu.
    - (c) osobna decyzja i niezmiennik z *Part:* `every`, jak `script-imports` — niezmiennik twierdzi coś o wszystkich śledzonych skryptach na każdym commicie, więc wymaga wpisu, czy dziś jest spełniony; bez przejrzenia 18 istniejących skryptów każdy wpis jest zgadywaniem, a przegląd zadanie wyklucza; wpis „naruszony” (WAY-51) dałby pilnowanie tylko nowych i zmienianych, ale twierdziłby naruszenie bez dowodu.
  - Source: Mariusz, 2026-11-11, „b” (odpowiedź na pytanie z drogami (a), (b), (c) i rekomendacją (b)).
- Co znaczy „zmieniany skrypt” — które odczyty pól istniejącego skryptu zmiana doprowadza do reguły?
  - Answer: (c) — cały odczyt danego pliku, gdy zmiana go dotyka: jeśli zmiana przerabia sposób, w jaki skrypt czyta jakiś plik, wszystkie pola tego pliku trafiają pod regułę; pozostałe pliki i reszta skryptu zostają, jak są.
  - Not chosen:
    - (a) cały skrypt — drobna poprawka puchnie do przeglądu wszystkich odczytów pól skryptu, a agent przeglądający musi czytać cały skrypt zamiast diffu.
    - (b) tylko odczyty pól, które zmiana dodaje albo przerabia — istniejący skrypt może na zawsze zostać sprawdzony w połowie, a bez ochrony zostają właśnie stare odczyty, którym zmiana formatu grozi najbardziej.
  - Source: Mariusz, 2026-11-11, „c” (odpowiedź na pytanie z drogami (a), (b), (c) i rekomendacją (c); kotwica w notatce: „Reguła obowiązuje nowe i zmieniane skrypty; przeglądania istniejących zadanie nie wymaga.”).
- Czym reguła jest sprawdzana — przeglądem zmiany czy testem?
  - Answer: (c) — przegląd zmiany i jeden test na odczyt pliku: test podaje plik bez jednego z potrzebnych pól i sprawdza, że skrypt kończy się błędem z nazwą tego pola; za to, że sprawdzane są wszystkie pola, odpowiada przegląd.
  - Not chosen:
    - (a) tylko przegląd, test zostawiony wyborowi cyklu — agent przeglądający łatwo przeoczy jedno niesprawdzane pole z wielu, a późniejsza zmiana, która po cichu usunie sprawdzanie, niczego nie wywraca.
    - (b) przegląd i test dla każdego pola — tyle testów, ile pól; przy plikach o kilkunastu polach test kosztuje więcej niż samo sprawdzanie, a ta praca spada na każdą zmianę, która przerabia odczyt pliku.
  - Source: Mariusz, 2026-11-11, „c” (odpowiedź na pytanie z drogami (a), (b), (c) i rekomendacją (c)).
- Jakim kodem wyjścia kończy się skrypt, gdy w czytanym pliku brakuje pola?
  - Answer: (a) — kodem 2: pliku nie dało się przeczytać, komunikat podaje plik i pole; w skrypcie, który istnieje po to, by sprawdzać formę pliku (np. kontrola opisu requestu albo fundamentu), brakujące pole, którego obecność sprawdza, zostaje ustaleniem jego listy z kodem 1, jak dziś.
  - Not chosen:
    - (b) zawsze kod 1, brak pola jako pozycja listy — orkiestrator wykonuje listę z kodem 1 jako ustalenia; przy skrypcie uwag procesu każda pozycja trafia słowo w słowo do uwag (WAY-294), więc „brakuje sekcji X w raporcie” stałoby się uwagą procesu, a raport zostałby niepoprawiony — to samo ciche przepuszczenie, któremu zadanie zapobiega.
    - (c) nowy kod, np. 3 — skille czytające kody wyjścia znają dziś tylko 0, 1 i 2, więc każdy trzeba uzupełnić, a do tego czasu nieznany kod każdy orkiestrator odczyta po swojemu; w zamian za sygnał, który kod 2 już daje.
  - Source: Mariusz, 2026-11-11, „a” (odpowiedź na pytanie z drogami (a), (b), (c) i rekomendacją (a)).

## Context

- Skąd pomysł: lekcja kursu Mega.DEV s01e05 („Building Workflows, Not Tool Stacks”) i jej przykład `skill-vs-saved-script` (https://github.com/MEGA-DOT-DEV/examples/tree/main/examples/skill-vs-saved-script).
- W tym przykładzie ten sam poranny raport liczono przez pięć dni raz skillem, raz zapisanym skryptem; czwartego dnia źródło zmieniło nazwę pola z `due` na `due_date`.
- Skrypt, który sprawdzał swoje pola, padł z błędem „Missing issues.due” i jedna poprawka go naprawiła; skrypt, który ich nie sprawdzał, przyjął brak pola za „brak terminu” i przez dwa dni dawał zły raport bez żadnego błędu.
- Z jakiego doprecyzowania wyszła WAY-328 i jakie drogi odrzucono: the author's private note on the refinement that led to that decision.
- Reguły dla skryptów the way stoją dziś jako niezmienniki z *Part:* `every` i *Method:* `review`, wyprowadzone z WAY-38: `script-language`, `script-imports`, `script-subprocesses` (`foundations/invariants.md`, `foundations` `52f8164`).
- Skrypty the way kończą się dziś kodem 0 (nic do zgłoszenia), 1 (lista ustaleń) albo 2 (brak listy); cykl czyta kod 2 tak: „Exit 2 is no listing: fix the call, or the file that could not be read.” (`task-cycle/skill/SKILL.md:502`, `foundations` `52f8164`).
- WAY-12 mówi, że testy żyją tylko przy niezmiennikach, ale chodzi tam o sprawdzanie samej decyzji; testy zachowania skryptów stoją w the way bez niezmiennika (np. `task-cycle/test_remarks_check.py` nie cytuje żadnego), więc test z *To do* nie wymaga niezmiennika, a to, że istnieje, sprawdza przegląd zmiany (`foundations` `52f8164`).
- Skryptów policzono 18: pliki `.py` śledzone przez git, bez plików `test_*` (`foundations` `52f8164`).

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-328 — Does the-way hold its own code and tests to the general coding guidelines and the testing guidelines of a product?: „The-way departs, for its own code and its own tests, from the general coding guidelines and from the testing guidelines of a product, under WAY-217 […]” *Rationale*, ostatnie zdanie: „The price: nothing of a product's guidelines protects the-way's code and tests, and new code copies the code already there.”
- WAY-38 — In what are the scripts of the-way written?: „[…] It calls git, the Python interpreter running it, and the commands a product declares in its own repository, reading their output through an adapter for the format. Where a product declares no such command, the script reports what it could not check, never agreement.” *Rationale*: „a check that quietly sees nothing would pass.”

## Settlements to record

Candidates: 5 shown, 4 accepted — 2026-11-11

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Skrypt the way, który czyta plik pisany przez agenta albo człowieka, sprawdza, czy są w nim pola, których potrzebuje, i gdy którego brakuje albo stoi pod inną nazwą, kończy się błędem z nazwą tego pola, nie zgaduje i nie bierze braku za wartość pustą; obowiązuje nowe skrypty, a w zmienianym cały odczyt pliku, którego sposób czytania zmiana przerabia; osobna decyzja obok WAY-328 ze *Scope* wszystkich 16 części, do którego nowa część mapy się dopisuje. | decision | *Questions to settle*: „W jakiej formie reguła wchodzi…” (b) i „Co znaczy »zmieniany skrypt«…” (c); drogi niewybrane w ich *Not chosen* | gdzie stoi reguła (WAY-328, WAY-38, niezmiennik), czy zmiana jednej linii skryptu wymaga sprawdzania wszystkich jego pól, które części obejmuje |
| 2 | Każdy odczyt pliku objęty regułą ma jeden test, który podaje plik bez jednego z potrzebnych pól i sprawdza błąd z nazwą tego pola; za pozostałe pola odpowiada przegląd zmiany. | decision | *Questions to settle*: „Czym reguła jest sprawdzana…” (c); drogi niewybrane w jej *Not chosen* | czy pisać test, ile testów (jeden czy na każde pole), czy tylko przegląd |
| 3 | Przy brakującym polu skrypt kończy się kodem 2 z plikiem i polem w komunikacie; w skrypcie, który sprawdza formę pliku, brakujące pole, którego obecność sprawdza, zostaje ustaleniem jego listy z kodem 1. | decision | *Questions to settle*: „Jakim kodem wyjścia…” (a); drogi niewybrane w jej *Not chosen* | kod wyjścia przy każdym skrypcie osobno: 1, 2 albo nowy |
| 4 | Polem w rozumieniu reguły jest każda nazwana rzecz, po której skrypt szuka danych w pliku: nagłówek sekcji, etykieta wiersza, kolumna tabeli, klucz JSON. | decision | wyprowadzone z materiału, przyjęte przez Mariusza 2026-11-11: „przyjmuję tak jak rekomendujesz”; w przykładzie Mega.DEV polem był klucz `due`; pliki pisane przez agentów the way to Markdown z sekcjami, etykietami i tabelami oraz JSON | czy nagłówek sekcji raportu albo kolumna tabeli planu podlega regule, czy tylko klucz w danych strukturalnych |

## Out of scope

- przegląd i poprawa istniejących skryptów the way pod nową regułę.

---
title: "the way: reguły słownika produktu — węższe znaczenie, słowa procesu w produkcie, pliki w innym języku, ocena uwag o słowach"
status: draft
created: 2026-11-05T12:10
updated: 2026-11-05
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# the way: reguły słownika produktu — węższe znaczenie, słowa procesu w produkcie, pliki w innym języku, ocena uwag o słowach

Status: ready for cycle
Project relation: independent

## Description

### Need

- Każdy produkt prowadzony przez the-way ma słownik (`foundations/glossary.md`), a reguły the-way pilnują, żeby jedno słowo miało w fundamencie produktu jedno znaczenie; te reguły nie mówią, co zrobić w trzech sytuacjach: słowo użyte węziej niż w branży, zwykłe angielskie słowo będące ostatnim słowem terminu z procesu („sentence” z „binding sentence”) i słowo w polskim pliku produktu.
- W trzech cyklach loop2 (PR #51, #52, #54) agenci zostawili o tym 12 uwag i rozstrzygali różnie; w PR #54 spór o słowo „secondary action” kosztował uwagę blokującą i dodatkową rundę poprawek.
- Agenci końca cyklu i recenzenci odczuwają to przy niemal każdej zmianie; Mariusz — bo w PR-ach dostaje wpisy słownika i zmiany nazw zależne od tego, który agent trafił na słowo.
- Bez zmiany to samo słowo będzie dookreślane w jednych decyzjach, a w innych nie, spory o słowa wrócą jako uwagi blokujące, a zastane użycia „sentence” w dzienniku decyzji loop2 dalej łamią regułę czytaną dosłownie.

### To do

1. Dopisać do decyzji WAY-95 i do szablonu słownika (`elements/glossary/template.md`, „Which words take an entry”) regułę, że słowo użyte węziej niż w branży dostaje wpis tylko tam, gdzie czytelnik biorący znaczenie branżowe przeczytałby zdanie błędnie (pytanie 1).
2. Przepisać WAY-104 na test zdania z pytania 2 — razem z jej *Rationale*, *Rejected* (w tym wariantem „reported as a warning rather than an error”, z powodem, dla którego jego koszt jest teraz do przyjęcia) i *Verification* — oraz akapit „Two glossaries” szablonu słownika.
3. Zawęzić WAY-99, WAY-97 (szukanie użyć słowa w „every file git tracks”) i szablon słownika do tekstu angielskiego: plik produktu w innym języku używa słów w ich znaczeniu w tym języku i reguły słownika go nie obejmują (pytanie 3).
4. Zastąpić w szablonie słownika (`elements/glossary/template.md`, zdanie z `TODO — decision pending: which decision sets when two uses of a word carry two meanings`) szkic oparty na definicji regułą opartą na zdaniu z pytania 1b; regułę niesie decyzja, na którą szablon się powołuje.
5. Zapisać w regułach przeglądu (nowa decyzja w zakresie `task-cycle` i zdanie w `task-cycle/review/SKILL.md`, sekcja 3) ocenę uwag o wpisie w słowniku i o brakującym dookreśleniu słowa procesu z pytań 1a i 2; zmiana nazwy słowa z dwoma znaczeniami (WAY-99) zostaje oceniana jak dotąd.

### Questions to settle

- Pytanie 1: czy słowo, które w produkcie znaczy węziej niż dla czytelnika znającego branżę, dostaje wpis w słowniku? (WAY-95 mówi o znaczeniu „something other than”; czy węższe jest „innym”, nie mówi.)
  - Answer: tak, ale tylko tam, gdzie czytelnik biorący znaczenie branżowe przeczytałby zdanie błędnie. Przykład: „secondary action” w loop2 to akcja pod formularzem narysowana jako podkreślony tekst bez ramki, a w branży to zwykle drugi, mniej wyróżniony przycisk, więc zdanie „the form „Załóż konto” holds no secondary action” czytane po branżowemu mówi co innego.
  - Not chosen:
    - każde węższe znaczenie dostaje wpis — pewniejsze, ale słownik rośnie o słowa, których nikt nie myli; zbliża się do wariantu odrzuconego w WAY-95 („every term relevant to the system — no bound”)
    - zostawić jak jest — spór z PR #54 wróci przy następnej zmianie; kosztował uwagę blokującą i rundę poprawek
  - Source: Mariusz, 2026-11-05, „A” — odpowiedź na pytanie z trzema drogami (A: wpis, gdy węższe znaczenie zmienia czytanie zdania; B: każde węższe znaczenie; C: zostawić); WAY-95, `foundations/decisions.md:2016-2043` @ `61c72fb`; loop2 `foundations/glossary.md`, wpis „secondary action”, @ `18fca47`.
- Pytanie 1a: czy uwaga recenzenta o tym, czy słowo powinno mieć wpis w słowniku, może blokować zmianę?
  - Answer: nie, chyba że recenzent wskaże zdanie, które pliki zawierają i które czytelnik przeczytałby przez brak wpisu błędnie — wtedy uwaga jest oceniana jak każda inna. Uwaga bez takiego zdania jest oceniana jako Minor, więc trafia na listę uwag niewstrzymujących w opisie PR-a, a Mariusz widzi ją przy scaleniu. Zmiana nazwy słowa z dwoma znaczeniami (WAY-99) nie należy do tej reguły i jest oceniana jak dotąd. Nie dotyczy to wpisu słownika, który zmiana sama pisze albo zmienia: uwaga, że taki wpis przeczy czemuś albo poszerza regułę, zostaje Important (WAY-263).
  - Not chosen:
    - zostawić ocenę recenzentowi bez ograniczenia — spór o słowo wraca jako uwaga blokująca i runda poprawek (PR #54)
    - każde węższe znaczenie dostaje wpis, więc nie ma sporu — słownik rośnie o słowa, których nikt nie myli; WAY-95 odrzuciła taki kierunek („no bound”)
    - skrypt wskazuje kandydatów na wpis — WAY-95 odrzuciła skrypt: nie odróżni definicji od zwykłego zdania
    - Minor zawsze, także ze wskazanym zdaniem (pierwsza odpowiedź, zmieniona po krytyce) — prawdziwa kolizja, pokazana na zdaniu, nie jest poprawiana w cyklu i dociera do scalenia
  - Source: Mariusz, 2026-11-05, „A” — odpowiedź na rekomendację „A razem z punktem 1” (uwaga o wpisie nie blokuje); WAY-161 i `task-cycle/review/SKILL.md:114` @ `61c72fb`. Odczytane jako zgoda na rekomendację, bo pytanie brzmiało „czy dołączyć punkt 1”. Pytanie przeciw odpowiedzi (cytat: „The reviewer alone grades and scopes”, `task-cycle/skill/SKILL.md:347`, czy odpowiedź obowiązuje mimo ograniczenia swobody recenzenta): Mariusz, 2026-11-05, „tak”. Po krytyce, na pytanie „Minor zawsze czy Minor bez wskazanego zdania?” z rekomendacją drugiej drogi: Mariusz, 2026-11-05, „tak” — odczytane jako zgoda na rekomendację. Zdanie o WAY-263 — propozycja przy akceptacji dokumentu: Mariusz, 2026-11-05, „akceptuję z tą propozycją zdania”.
- Pytanie 1b: kiedy dwa użycia słowa niosą dwa znaczenia (otwarte `TODO` w `elements/glossary/template.md:51-52` @ `61c72fb`)?
  - Answer: gdy zdanie, które zawiera tekst objęty regułami słownika (pytanie 3), jest prawdziwe dla jednego użycia i fałszywe dla drugiego — w obie strony i tylko na zdaniach, które pliki już zawierają, nie na zdaniu wymyślonym. Szkic: „Two uses of a word carry two meanings when a sentence the files hold is true of one use and false of the other.” Test opiera się na zdaniu, tak jak reguła z pytania 1 i uzasadnienie WAY-99 („a sentence a test cites carries its words as they stand”).
  - Not chosen:
    - test oparty na definicji (szkic zastany w szablonie: „a definition true of one is false of the other”) — żeby go zastosować, trzeba najpierw napisać definicję każdego użycia, co otwiera kolejny spór o to, jak ją sformułować
    - zostawić `TODO` — agenci dalej wymyślają kryterium sami
  - Source: Mariusz, 2026-11-05, „niech będzie oparty na zdaniu”; po krytyce, na pytanie „czy test z pytań 2 i 1b ma działać w obie strony i tylko na zdaniach, które pliki już zawierają?” — „tak”.
- Pytanie 2: czy WAY-104 obejmuje zwykłe angielskie użycie ostatniego słowa terminu procesu (np. „sentence” z „binding sentence”)?
  - Answer: WAY-104 zmienia się na test zdania — słowo procesu (słowo, które słownik the-way trzyma jako termin, albo ostatnie słowo jego terminu) dostaje w fundamencie produktu dookreślenie tylko tam, gdzie zdanie, które fundament produktu zawiera, dałoby się przeczytać w drugim znaczeniu — domenowe użycie w znaczeniu procesu albo użycie procesowe w znaczeniu domeny; uwaga recenzenta o brakującym dookreśleniu jest oceniana tak jak w pytaniu 1a. Przykład kolizji, którą reguła łapie: w loop2 gołe „sentence” znaczy zwykle komunikat dla gracza, więc zdanie decyzji w `foundations/decisions.md:2166` („leaving the sentence unchanged — its plain reading would admit…”) i w `:530` („a sentence naming what a kind of condition may take”), gdzie „sentence” znaczy zdanie decyzji, czytelnik może wziąć za komunikat. Przykład użycia, którego reguła nie rusza: gołe „map” w loop2 (mapa w grze; 79 użyć po przedimku albo zaimku, poza „map run”) — ostatnie słowo terminu „part map”, którego nikt nie weźmie za mapę części.
  - Not chosen:
    - zostawić WAY-104 dosłownie i osobnym zadaniem w loop2 dookreślić gołe użycia (pierwsza odpowiedź Mariusza, „A”, zmieniona po znalezisku „map”) — sprzątanie dziesiątek wierszy w loop2 („map”, „sentence”, „element” i inne) i stały koszt pisania, rosnący z każdym terminem słownika the-way; reguły nie sprawdza żaden skrypt, więc dalej byłaby stosowana wybiórczo (żaden z trzech cykli nie zgłosił gołego „map”)
    - usunąć WAY-104 całkiem — kolizje jak loop2 `:2166` zostają bez ochrony
    - zwolnić gołe ostatnie słowo z reguły (szkic z notatki: „A last word of a term written as plain English, in a phrase that bounds it […] is no use of the term”) — kolizje jak loop2 `:2166` zostają; szkic jest zresztą zbędny, bo fraza zawierająca słowo jest dookreśleniem już dziś
    - zostawić bez rozstrzygnięcia — kroki powrotu dalej dookreślają słowa po kawałku, niespójność rośnie z każdym cyklem
  - Source: Mariusz, 2026-11-05: najpierw „A” (WAY-104 dosłownie), potem — po pokazaniu gołych użyć „map” w loop2 (podanych jako ok. 240, liczba zawyżona, zob. *Context*) i wariantu „Słowo procesu […] dostaje w fundamencie produktu dookreślenie tylko tam, gdzie zdanie dałoby się przeczytać w znaczeniu procesu […] Uwaga o dookreśleniu nie blokuje, jak w 1a.” z pytaniem „czy otwieramy pytanie 2 na nowo i zmieniamy odpowiedź na test zdania?” — „tak”; po krytyce, na pytanie z poprawioną liczbą (79) „czy test zdania w pytaniu 2 zostaje mimo mniejszej liczby?” i na pytanie o test w obie strony — „tak”; WAY-104, `foundations/decisions.md:2214-2251` @ `61c72fb`; loop2 `foundations/decisions.md` (748 użyć „map”, 520 w „map run(s)”/„map-run”; `:530`, `:2166`) @ `18fca47`.
- Pytanie 3: czy reguły słownika (WAY-95, WAY-99, WAY-104) obejmują polskie pliki produktu, np. `guidelines/coding.md` w loop2?
  - Answer: nie — reguły słownika wiążą tekst angielski, a plik produktu w innym języku (np. polskie wytyczne) używa słów w ich znaczeniu w tym języku; produkt, który chce kontroli słów, pisze dany plik po angielsku, jak szablon styleguide'u już mówi o tłumaczeniach. WAY-99 („two meanings in the files git tracks”) zawęża się do tekstu angielskiego. WAY-104 polskich plików i tak nie obejmuje, bo dotyczy tylko `foundations/`, które są po angielsku (WAY-72).
  - Not chosen:
    - reguły obejmują polskie pliki, sprawdzane wobec angielskiego słownika (dosłowne czytanie WAY-99) — agent musi ustalać, które polskie słowo odpowiada któremu terminowi, bez listy i z polską odmianą; wraca osąd i spory
    - jedno znaczenie na słowo wewnątrz jednego języka, bez porównania ze słownikiem angielskim — nie ma polskiego słownika, w którym zapisać znaczenie; każda zmiana nazwy na osądzie agenta
    - zostawić — każdy cykl zgaduje jak PR #51, czasem zmieniając przy tym słowo w zatwierdzonej odpowiedzi
  - Source: Mariusz, 2026-11-05, na pytanie z drogami A (reguły obejmują polskie pliki), B (reguły wiążą tekst angielski), C (jedno znaczenie wewnątrz jednego języka), zostawić — „B, chociaż trochę się obawiam, że ten słownik jest zbyt sztywny i generuje sporo niepotrzebnych problemów”; WAY-99 `foundations/decisions.md:2097`, WAY-104 `:2216`, WAY-171 `:4755-4767`, `product-guidelines/styleguide/template.md:165-170` @ `61c72fb`; loop2 `guidelines/coding.md:170`, `guidelines/coding-saved-game.md:146` @ `18fca47`.

## Context

- Źródło: sprawa AIR-591 w zeszycie ai-review (`C:\Storage\The Brain\The Brain\Notes\Areas\(A) Claude code\ai_review_ledger.md`), wystąpienia w loop2 PR #51, #52, #54.
- Szkic poprawki WAY-99 z nocnego skanu (słowo ze znaczeniem węższym zachowuje nazwę) odpadł: WAY-99 każe zmienić nazwę tylko wtedy, gdy jedno ze znaczeń jest takie, którego czytelnik z branży by słowu nie dał, a znaczenie węższe mieści się w branżowym.
- „sentence” stoi w fundamencie loop2 (`main` @ `18fca47`) 93 razy w 86 wierszach — 85 wierszy w `foundations/decisions.md`, 1 w `foundations/invariants.md` — nie setki, jak podawał zeszyt.
- „map” stoi w `foundations/decisions.md` loop2 748 razy, z tego 520 w „map run(s)”/„map-run”; część pozostałych ma już dookreślenie („game map”, „solved map”, „manual map”); po przedimku albo zaimku („the map”, „each map”) i nie przed „run” — 79 razy (`18fca47`).
- Dwa otwarte miejsca `TODO` w `elements/glossary/template.md` ze stanu `61c72fb`: wiersze 51–52 (kiedy dwa użycia niosą dwa znaczenia) i wiersze 35–38 (słowo pokazywane użytkownikom w innym języku — to inna sprawa niż pytanie 3).

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-95 — „A word takes a glossary entry when it means, in the product, something other than a reader who knows the product's field takes it to mean; an agent that meets such a word in its work — writing an entry, searching the foundation, in a task's return step — writes its entry, no sweep of every binding sentence looks for candidates, and a human accepts the meaning (WAY-114).”
- WAY-99 — „Where a word carries two meanings in the files git tracks and one of them is a meaning a reader who knows the product's field would not give it, one of the two is renamed, and the glossary entry of the word names in *Not* each such meaning it no longer carries, with the term, identifier, closed-list value or quoted word — holding neither the term nor its forms — that carries it now. A meaning whose word a human has not yet chosen reads `TODO` in *Not*, which a task branch may hold and the main branch never does.”
- WAY-104 — „A word of a product's domain that the glossary of the-way holds at the commit the product pins, or the last word of a term it holds, in any of its forms, is written in the files of the product's `foundations/` with a qualifier — a phrase holding the word — and the bare word keeps there the meaning of the process; the qualified word takes a glossary entry only where WAY-95 gives a word one, and where the bare word itself has an entry in the glossary of the-way, that entry records no *Not* for its domain meaning. The product's code, its interface and talk about the product use the word of the domain unchanged.”
- WAY-161 — „A finding the reviewer has marked as outside the task's scope […] is not fixed, whatever its grade, nor is a Minor finding […]. The orchestrator moves no finding from one of these kinds to another.” (`foundations/decisions.md:4293`; ocenę i zakres ustala wyłącznie recenzent — `task-cycle/skill/SKILL.md:347`.) Pytanie 1a wprowadza wyjątek od swobody oceny recenzenta.
- WAY-263 — „A reviewer grades as Important a finding that a change departs from a foundation entry it writes or changes […]” (`foundations/decisions.md:7618`).
- WAY-97 — „A sentence relies on a glossary term by using its word. A glossary entry is edited in place, its meaning included, and the author of a change to a definition searches, in the same change, the texts that use the word and rewrites each use whose meaning the new definition moves.” (`foundations/decisions.md:2065`)
- WAY-226 — „The glossary of the-way holds the words of the process, and a product's glossary holds the words of its domain; a product takes the words of the process from the-way at the commit it pins and defines none of them again, and in the-way, whose product is the process, the two are one file.” (`foundations/decisions.md:6228`; WAY-104 z niej wynika.)
- WAY-72 — „A product's foundation is written in English, whatever language the product shows the people who use it and whatever language its team speaks.”
- WAY-171 — „The headings, header lines, field names, values of closed lists and the marker `none —` stay in English while the rest of the text is in the language the product writes its guidelines in.” (`foundations/decisions.md:4765-4767`)

## Settlements to record

Candidates: 6 shown, 5 accepted — 2026-11-05

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Słowo użyte w produkcie węziej niż w branży dostaje wpis w słowniku tylko tam, gdzie czytelnik biorący znaczenie branżowe przeczytałby zdanie błędnie. | decision | Questions to settle, pytanie 1 | czy „secondary action” (węższe niż w branży) dostaje wpis — recenzent i krok powrotu rozstrzygają różnie |
| 2 | Uwaga recenzenta o tym, czy słowo powinno mieć wpis w słowniku albo czy słowu procesu brakuje dookreślenia, jest oceniana jako Minor, chyba że recenzent wskaże zdanie, które pliki zawierają i które czytelnik przeczytałby przez ten brak błędnie; zmiana nazwy słowa z dwoma znaczeniami (WAY-99) jest oceniana jak dotąd, a uwaga, że wpis słownika, który zmiana sama pisze albo zmienia, przeczy czemuś albo poszerza regułę, zostaje Important (WAY-263). | decision | Questions to settle, pytania 1a i 2 | ocena uwagi bez wskazanego zdania jako Important i runda poprawek, jak w PR #54 |
| 3 | Dwa użycia słowa niosą dwa znaczenia, gdy zdanie, które pliki zawierają, jest prawdziwe dla jednego użycia i fałszywe dla drugiego. | decision | Questions to settle, pytanie 1b | test oparty na definicji (szkic w szablonie), na zdaniu wymyślonym albo kryterium wymyślone przez agenta |
| 4 | Słowo procesu — termin słownika the-way albo ostatnie słowo jego terminu — dostaje w fundamencie produktu dookreślenie tylko tam, gdzie zdanie, które ten fundament zawiera, dałoby się przeczytać w drugim znaczeniu, w którąkolwiek stronę. | decision | Questions to settle, pytanie 2 | dookreślenie każdego gołego „map”, „sentence”, „element” w loop2, jak każe dzisiejsza WAY-104 |
| 5 | Reguły słownika wiążą tekst angielski; plik produktu w innym języku używa słów w ich znaczeniu w tym języku. | decision | Questions to settle, pytanie 3 | zamiana „program” na „proces” w polskich wytycznych, jak w PR #51 |

## Out of scope

- Poprawienie w fundamencie loop2 zdań, które po zmianie WAY-104 dają się przeczytać w drugim znaczeniu (jak `foundations/decisions.md:2166` i `:530`) — osobne zadanie w loop2.

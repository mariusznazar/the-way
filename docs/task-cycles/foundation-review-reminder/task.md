---
title: "the way: przegląd fundamentu, którego nie da się pominąć — z partią porządków dziennika decyzji"
status: draft
created: 2026-11-12T17:54
updated: 2026-11-15
tags: [zadanie]
related: "a note of the author's"
---

## Po co to

- **Jak jest dziś:** Okresowy przegląd fundamentu produktu (dziennika decyzji, niezmienników, opisu części) jest jedynym krokiem procesu, który ogląda to, czego żadne zadanie nie dotyka. Proces o nim przypomina, ale przypomnienie da się przewinąć: w grze przegląd odbył się dopiero po 87 scaleniach, z zadania z terminem, a w the way przypomnienie stoi w kolejnych prośbach bez przeglądu. Porządki dziennika decyzji nie mają momentu, w którym się dzieją.
- **Kto to odczuwa:** Ja, gdy po wielu zadaniach okazuje się, że wpisy fundamentu rozjechały się z kodem. Agenci kolejnych cykli, którzy budują na wpisach, których nikt nie sprawdził.
- **Co jeśli nic:** Przegląd fundamentu dalej zależy od tego, czy o nim pamiętam. Dziennik decyzji rośnie o wpisy, które powinny stać gdzie indziej.

# Przegląd fundamentu, którego nie da się pominąć — z partią porządków dziennika decyzji

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Okresowy przegląd fundamentu produktu (dziennika decyzji, niezmienników, opisu części) jest jedynym krokiem procesu, który ogląda to, czego żadne zadanie nie dotyka.
- W grze pierwszy przegląd odbył się dopiero po 87 scaleniach, uruchomiony zadaniem w backlogu z terminem; w the way przypomnienie stało w opisie każdej prośby od 30. scalenia, w 19 prośbach z rzędu, zanim przegląd odbył się przy 49 scaleniach.
- Proces przypomina o przeglądzie zdaniem w opisie każdej prośby o scalenie, gdy od ostatniego przeglądu minęło 30 scaleń; zdanie niczego nie zatrzymuje, nie zostawia śladu poza opisem prośby i powtarza się w tym samym brzmieniu także wtedy, gdy przegląd jest zaplanowany na później.
- Porządki dziennika decyzji — wyprowadzanie wpisów, które decyzjami nie są, partiami — nie mają w procesie żadnego momentu, w którym się dzieją.
- Odczuwa to Mariusz, gdy po wielu zadaniach okazuje się, że wpisy fundamentu rozjechały się z kodem, oraz agenci kolejnych cykli, którzy budują na wpisach, których nikt nie sprawdził, i czytają dziennik pełen wpisów, które decyzjami nie są.
- Bez zmiany przegląd fundamentu dalej zależy od tego, czy Mariusz o nim pamięta, a dziennik decyzji rośnie o wpisy, które powinny stać gdzie indziej.

### To do

1. Na końcu cyklu, od progu przypomnienia (punkt 3) liczonego od ostatniego znacznika przeglądu, orkiestrator czyta backlog produktu (miejsce z sekcji `## Backlog`, odnalezione jak podaje `project-level/backlog_place.md`) i sprawdza, czy stoi w nim otwarta linia zadania przeglądu fundamentu tego repozytorium — linia, której nazwa zawiera nazwę skilla `review-foundation` i nazwę repozytorium, a co znaczy „otwarta”, mówią reguły miejsca zadań (WAY-107). Zdanie przypomnienia w opisie prośby: gdy takiej linii nie ma, mówi człowiekowi wprost, żeby dodał do backlogu zadanie przeglądu, podaje, co ma stać w jego nazwie, liczbę scaleń, znacznik ostatniego przeglądu i skill; gdy linia stoi — wskazuje ją i nie ponagla; gdy backlogu nie da się przeczytać (brak wpisu w pliku lokalizacji albo brak dostępu), mówi to wprost i brzmi jak przy braku linii. Cykl tej linii nie zakłada ani nie zmienia (WAY-140).
2. Przegląd fundamentu przy każdym przebiegu znajduje wszystkie wpisy dziennika decyzji, które decyzjami nie są — reguły wytycznych, pojedyncze teksty i liczby, opisy braku funkcji, części jednego pytania pod osobnymi numerami — według pytań „Where it goes” w `elements/decisions/template.md`, układa je w grupy według miejsca, do którego idą, z liczbą wpisów w każdej, i przedstawia człowiekowi grupy; człowiek decyduje, które grupy wchodzą w zadanie backlogu produktu tym razem (tak jak o grupach uwag w `foundation-review/with_the_human.md`), a reszta czeka do następnego przeglądu.
3. Próg przypomnienia wynosi 60 scaleń zamiast 30 i stoi w skrypcie `task-cycle/review_reminder.py` (dziś `THRESHOLD = 30`), z testem w `task-cycle/test_review_reminder.py`, który go trzyma, i komentarzem przy wartości z powodem — rytm przeglądów policzony dla 60 z tempa w *Context* i cena, którą Mariusz przyjął (pytania 5 i 6). WAY-300 przestaje podawać liczbę: zdanie mówi „od progu skryptu przypomnienia” i zatrzymuje regułę jednej liczby dla każdego produktu; *Verification* traci przykład „31 merges”, *Rationale* rytm liczony dla 30, a *Rejected* zdanie o 50 scaleniach („a review every 2–8 weeks in the-way”), które przy 60 przestaje być powodem odrzucenia. Zdanie „once the main branch holds 30 merges” w `foundation-review/SKILL.md` i „after 30 merges” w `README.md` przestają podawać 30.
4. Skrypt przypomnienia odróżnia brak znacznika przeglądu od błędu gita: dziś funkcja `last_review_tag` w `task-cycle/review_reminder.py` bierze każde niepowodzenie `git describe` za brak znacznika i liczy wtedy scalenia od początku historii; błąd gita ma kończyć skrypt kodem 2 z komunikatem, jak inne jego błędy. Krok 13 skilla cyklu (`task-cycle/skill/SKILL.md`, akapit zaczynający się od „Before you write the description, count the merges”) mówi „after a fetch” — ma mówić o fetchu, który przynosi znaczniki.
5. Wpis WAY-300 i krok 13 skilla cyklu mówią o przypomnieniu to, co cykl robi: przykład *Verification* mówi, że przypomnienie zamyka sekcję *How to merge* (dziś „opens its request with a reminder”, choć `task-cycle/skill/request_template.md` każe „*How to merge* ends with the reminder”); z *Rationale* znika zdanie „the history of the first product is not open to a reader of this repository”, bo repozytorium loop2 jest publiczne; krok 13 mówi wprost, że poniżej progu opis prośby nie mówi o przeglądzie nic (szablon prośby mówi to już zdaniem „Where the count reads `reminder: no`, nothing is written”, a prośby #82–#108 pisały tam trzy różne rzeczy).

### Questions to settle

- Czy agent przeglądu fundamentu czyta kod, zanim zobaczy wpisy fundamentu?
  - Answer: nie. Skill każe najpierw przeczytać cały fundament, plik po pliku, a potem każdy wpis zestawić z tym, co pokazuje repozytorium; agent, który dostaje do czytania kawałek dziennika decyzji, dostaje wpisy i reguły kroku, a kodu szuka dopiero pod wpis.
  - Source: `foundation-review/SKILL.md:46-51` i `:97-105`, `foundation-review/weak_points.md:9-13` @ 2292f33
- Pytanie 1. Które z czterech punktów zostają w tym zadaniu, a które czekają na pierwszy przegląd fundamentu gry jako osobne zadanie?
  - Answer (2026-11-12): żaden nie idzie teraz — całe zadanie czeka na wynik pierwszego przeglądu fundamentu gry, a partie porządków dziennika decyzji gry (dopisek Mariusza w *Context*) czekają także na zadanie the way o tym, co trafia do dziennika decyzji.
  - Not chosen:
    - samo przypomnienie teraz, punkty 2–4 osobnym zadaniem po przeglądzie gry — jeden cykl więcej, a zmiana WAY-300 i WAY-24 opiera się na pięciu dniach działania przypomnienia, w których przegląd gry był świadomie odłożony
    - punkty 1–3 teraz, sam skan osobno — część o strukturze kodu powstaje z raportu, zanim przegląd gry pokaże, czy zmieści się w jednej sesji
    - wszystko w jednym zadaniu teraz — kontrakt skanu i kształt części o strukturze z jednej próby w raportach, bez tego, co pokaże przegląd gry
  - Source: Mariusz, 2026-11-12: „trochę mi to brzmi tak, że nie powinniśmy teraz podejmować tego zadania wcale i po prostu poczekać na przeglad”; zależności dopisane w linii zadania na jego prośbę
  - Answer (2026-11-14, po przeglądzie gry): zostaje przypomnienie (punkt 1) i dochodzi nowy punkt — przegląd przy każdym przebiegu proponuje kolejną partię wpisów dziennika decyzji, które decyzjami nie są; część o strukturze kodu, kolejność lektury i tani skan „decyzje a kod” wypadają z zadania i nie idą do osobnego.
  - Not chosen:
    - przypomnienie bez zmian — przegląd dalej odbywa się tylko wtedy, gdy Mariusz o nim pamięta; w the way przypomnienie stało w każdej prośbie od 30. scalenia (#115: 37, #124: 46) bez przeglądu i bez zadania w backlogu, a przegląd gry odbył się z zadania z terminem
    - część o strukturze kodu w węższej postaci (przebieg narzędzia nieużywanego kodu, importy pod prąd wewnątrz części) — osobna konfiguracja dla każdego produktu; w grze knip bez konfiguracji zgłosił 229 plików, z konfiguracją jedną martwą funkcję; rozmiar pilnuje już test reguły rozmiaru w bramce produktu (WAY-360), a jej wyjątki stoją w decyzji, którą przegląd czyta wobec kodu
    - kolejność lektury jako lista części, których pliki zmieniły się od ostatniego znacznika, a wpisy nie — skrypt z testem, który przy 27 scaleniach na 8 części gry objąłby prawie wszystkie; przegląd gry nie pokazał niczego, co umknęło przez lekturę wpisów przed kodem
    - tani skan na tańszej klasie modelu przy przeglądzie — przegląd gry przeczytał wszystkie 389 decyzji wobec kodu, więc luka skanu zamyka się samym odbyciem przeglądu; zostaje oszczędność bez pomiaru kosztu przeglądu z 13.11, a tańszy model zawodził w próbie przy pytaniach ocennych (8 z 12 zgłoszeń chybionych)
    - partia porządków dziennika poza zadaniem — porządki dziennika nie mają żadnego momentu, w którym się dzieją
  - Source: Mariusz, 2026-11-14: „zgadzam się na rekomendacje” (rekomendacje: 1 a, 2 a, 3 a, 4 a, 5 a)
- Pytanie 2. Czym staje się przypomnienie o przeglądzie fundamentu: śladem w backlogu, zatrzymaniem prośby o scalenie, jednym i drugim?
  - Answer: ślad w backlogu, który zakłada człowiek, nie cykl — the way zostaje oddzielone od backlogu. Cykl na końcu, od 30 scaleń od ostatniego znacznika przeglądu, czyta backlog produktu i sprawdza, czy stoi w nim otwarta linia zadania przeglądu fundamentu tego repozytorium. Gdy nie stoi, zdanie przypomnienia w prośbie mówi wprost, żeby dodać takie zadanie do backlogu; gdy stoi, zdanie tylko je wskazuje i przestaje ponaglać. Część po stronie Mariusza — doradca dnia przy scalaniu prośby z takim zdaniem dopisuje linię albo pyta o nią — leży w jego setupie, poza the way.
  - Not chosen:
    - cykl sam dopisuje linię zadania przeglądu do backlogu (wariant wybrany najpierw) — Mariusz: „z tego co pamiętam to the way o backlogu jest oficjalnie odseparowane, więc to ja miałem pilnować, żeby zadanie się pojawiło na podstawie znacznika”; wymagałby zmiany WAY-140, wbrew uzasadnieniu WAY-161, a produkt z backlogiem w Jirze dawałby cyklowi prawo zapisu poza repozytorium
    - zatrzymanie prośby jako szkicu od 60 scaleń — zmiana WAY-300 („The reminder blocks nothing”); każda niezwiązana zmiana czeka na kliknięcie, które w the way przy kilkunastu scaleniach w tygodniu staje się odruchem
    - linia w backlogu i zatrzymanie prośby razem — suma obu kosztów
    - tylko setup Mariusza (doradca dnia codziennie uruchamia `review_reminder.py` i zakłada linię), w the way samo brzmienie WAY-24 — inny użytkownik the way zostaje ze zdaniem, które da się przewinąć
  - Source: Mariusz, 2026-11-14: „a, natomiast z tego co pamiętam to the way o backlogu jest oficjalnie odseparowane, więc to ja miałem pilnować, żeby zadanie się pojawiło na podstawie znacznika”, potem przy wariantach przepisanych pod oddzielenie: „b”
- Pytanie 3. Po czym cykl rozpoznaje w backlogu linię zadania przeglądu fundamentu?
  - Answer: po stałym znaczniku w nazwie linii — nazwie skilla `review-foundation` i nazwie repozytorium (np. „Przegląd fundamentu loop2 (`review-foundation`)”), którą podaje zdanie przypomnienia; cykl szuka otwartej linii z tym znacznikiem, a otwartość ocenia według reguł miejsca zadań. Gdy backlogu nie da się przeczytać, zdanie mówi to wprost i brzmi jak przy braku linii.
  - Not chosen:
    - identyfikator wyliczany przez the way (np. `loop2-foundation-review-after-2026-11-13`) w polu `🆔` — przeczy WAY-329 („A task that belongs to no plan has no identifier from the-way”), działa tylko w miejscu zadań z identyfikatorami, a każdy kolejny przegląd potrzebuje nowego, bo stary zostaje przy zrobionej linii
    - cykl nie czyta backlogu, zdanie zawsze prosi o zadanie „jeśli go nie ma” — przypomnienie nie milknie, gdy przegląd jest zaplanowany, czyli cofa część odpowiedzi na pytanie 2
  - Source: Mariusz, 2026-11-14: „a”; zdanie o nieczytelnym backlogu podane przy pytaniu jako uzupełnienie bez osobnego pytania, bez sprzeciwu; reguły zadań Mariusza: „Linię zadania znajduje po linku do jego notatki albo po nazwie” (`system_zadan.md`, akapit „Linia zadania agentowego z planu projektu”)
- Pytanie 4. Co znaczy „kolejna partia” wpisów dziennika, które decyzjami nie są?
  - Answer: przegląd znajduje wszystkie takie wpisy, układa je w grupy według miejsca, do którego idą, z liczbą wpisów w każdej; człowiek decyduje o całych grupach, które wchodzą w zadanie tym razem, a reszta czeka do następnego przeglądu.
  - Not chosen:
    - przegląd sam wybiera partię na jeden cykl (np. najtańsze wpisy do kilkunastu sztuk), o reszcie podaje liczbę — o tym, co wychodzi teraz, decyduje agent, a próg „ile na jeden cykl” trzeba wpisać na sztywno albo zostawić do zgadnięcia
  - Source: Mariusz, 2026-11-14: „a”; skala z raportu `odchudzenie_dziennika_decyzji.md`: „105 wpisów (24% bajtów), które decyzjami nie są”
- Pytanie 5. Od ilu scaleń od ostatniego przeglądu przypomnienie się pojawia?
  - Answer: od 60, nie od 30 — w the way i w loop2, nadal jedna liczba dla każdego produktu; przy dzisiejszym tempie (49 scaleń w 8 dniach, 6–14.11.2026) 30 daje przegląd mniej więcej co tydzień, a każdy czyta cały fundament od nowa. Przyjęta cena: rozjazdy fundamentu z kodem żyją dłużej, a jeden przegląd ma więcej uwag do przeczytania.
  - Source: Mariusz, 2026-11-15, po przeglądzie fundamentu the way: „żeby to było 60, nie 30”; tempo i cena z notatki tego dnia (*Context*)
- Pytanie 6. Gdzie stoi liczba 60 — w zdaniu decyzji WAY-300 czy w skrypcie przypomnienia z testem?
  - Answer: w skrypcie: `THRESHOLD = 60` w `task-cycle/review_reminder.py`, z testem, który ją trzyma, i komentarzem przy wartości z powodem (rytm przeglądów i przyjęta cena z pytania 5); WAY-300 mówi „od progu skryptu przypomnienia” i zatrzymuje regułę, że próg to jedna liczba dla każdego produktu i produkt nie ustala własnej. Powód: zadanie wprowadza regułę, że pojedyncze liczby nie stoją w dzienniku decyzji (pytanie 3 „Where it goes” w `elements/decisions/template.md`), więc samo nie dopisuje do niego liczby.
  - Not chosen:
    - liczba zostaje w zdaniu WAY-300 („from 60 merges on”), skrypt ją powtarza — wpis dalej trzyma pojedynczą liczbę, pierwszy przegląd po zmianie sam zgłosi WAY-300 do grupy „liczby do kodu”, a każda zmiana progu to zmiana decyzji; zysk: rachunek rytmu i odrzuconych liczb w jednym miejscu dziennika
  - Source: doradca dnia w imieniu Mariusza, z jego upoważnienia, 2026-11-15: „6 b — liczba do skryptu (THRESHOLD = 60) z testem i komentarzem z powodem; WAY-300 mówi „od progu skryptu przypomnienia” i trzyma regułę jednej liczby dla każdego produktu”

## Context

- Przypomnienie o przeglądzie istnieje od 2026-11-07 (commit `46ae3b9` w the way); z 82 scaleń gry 21 zaszło od tego dnia, wcześniejszym nic o przeglądzie nie przypominało.
- Przegląd fundamentu gry był w tym czasie odłożony świadomie, zadaniem w backlogu gry z terminem 2027-01-13; 12.11.2026 Mariusz przestawił go na „teraz”.
- Pierwszy przegląd fundamentu gry odbył się 2026-11-13, uruchomiony zadaniem w backlogu gry z terminem, nie przypomnieniem: znacznik `foundation-review/2026-11-13` na `1b0c8ad4` („389 decisions, 127 invariants, 126 environment facts, 39 glossary terms and the part map (8 parts) read whole; 305 remarks of 27 merged requests (#61-#87) checked; 40 proposals and 10 groups of remarks decided”); plik danych a note of the author's.
- Ten przegląd czytał fundament szesnastoma agentami, dał 40 propozycji i 11 zadań gry; decyzje podejmował doradca dnia z upoważnienia Mariusza (plik danych, „Stan kroków”, krok 6).
- Od napisania zadania the way dostało regułę rozmiaru funkcji i pliku w szablonie wytycznych kodu, z testem w bramce produktu (WAY-360), liczby rozmiarów dla recenzenta całej zmiany (WAY-361) i pytanie przeglądu o koniec stanu przejściowego (#108; dziś reguła w `foundation-review/proposals.md`).
- W the way przypomnienie stało w opisie każdej prośby od 30. scalenia po znaczniku `foundation-review/2026-11-06` — #107 i #109–#126, 19 próśb (np. #115: 37 scaleń, #120: 41, #124: 46); backlog the way nie miał zadania przeglądu fundamentu the way. Przegląd odbył się przy 49 scaleniach: znacznik `foundation-review/2026-11-15` na `21ecb62` (scalenie #126), „331 foundation entries and 329 remarks of 49 merged requests (#77, #79-#126) checked”; 2026-11-15 skrypt przypomnienia liczy od niego 0 scaleń.
- Reguły przeglądu fundamentu, na których zadanie stoi, #126 wyprowadził z dziennika decyzji do plików skilla (tabela „Withdrawn identifiers” w `foundations/decisions.md`): ostatni przegląd i przebieg przeglądu z człowiekiem (dawne WAY-301 i WAY-302) — `foundation-review/SKILL.md` i `foundation-review/with_the_human.md`; jeden skill dla każdego produktu (dawne WAY-304) — `foundation-review/remarks.md`; słabe punkty decyzji (dawne WAY-305) — `foundation-review/weak_points.md`; stan przejściowy (dawne WAY-354) — `foundation-review/proposals.md`.
- Źródła zadania leżą w notatkach Mariusza: raport o usprawnieniach procesu, tabela działań, wiersz D10b (punkt 1); raport o zgodności fundamentu gry z kodem, karta D7 i wzorzec W5; dopisek Mariusza niżej (punkt 2).
- Zmiana opisu skilla przeglądu wymaga odświeżenia punktów wejścia skilli poleceniem z głównego pliku instrukcji repozytorium.
- Dopisek Mariusza z 12.11.2026 (przegląd analizy dziennika decyzji): porządki dziennika decyzji gry idą tak, że teraz wychodzą najtańsze wpisy (a note of the author's), a reszta partiami przy kolejnych przeglądach fundamentu. Przegląd ma więc za każdym razem proponować kolejną partię wpisów, które decyzjami nie są — reguły wytycznych, pojedyncze napisy i liczby, opisy braku funkcji, części jednego pytania pod osobnymi numerami — według pytania „dokąd to idzie” z the way: co trafia do dziennika decyzji — pytanie „dokąd to idzie”, próg wejścia, reguły wytycznych bez wpisu, test wskazujący zdanie decyzji. Bez tego zaczepu te porządki nie mają żadnego momentu, w którym się dzieją.
- Punkty 4 i 5 *To do* pochodzą z przeglądu fundamentu the way 2026-11-14, na który Mariusz zdecydował notatkę do tego zadania: propozycja P12 (WAY-300, uwaga #80-24) i grupa uwag G10 (uwaga #80-8; #80-9 i #80-11, odłożone, dotyczą tego samego przypomnienia). Plik danych: `the data file of an earlier foundation review, in the author's notes`, sekcja „Fundament” → „Propozycje”, P12, i „Grupy uwag”, G10.
- Uwaga #80-8 w słowach recenzenta: „any non-zero exit of `git describe` is read as "no tag" … can read `reminder: yes` falsely (for instance in a clone where tags are not fetched)”; przegląd ocenił ją jako wąską, bo zwykły klon i fetch przynoszą znaczniki.
- P12 przeliczył tempo po krytyce: the-way 26, 20 i 36 scaleń w tygodniach ISO 44–46, loop2 21, 21 i 32; wpis WAY-300 podaje „6–26 merges a week in the-way, 4–21 in the product”, tydzień 46 wychodzi ponad te przedziały.
- Rytm dla 60 scaleń z notatki Mariusza z 2026-11-15: ok. 10 dni przy tempie 6–14.11.2026, a przy tempie, które podaje dziś *Rationale* WAY-300 (6–26 scaleń tygodniowo w the way, 4–21 w loop2), od 2,5 do 10 tygodni w the way i od 3 do 15 w loop2; dziś to samo *Rationale* liczy dla 30 „every 1–4 weeks” w the way i „every 1.5–7 weeks” w pierwszym produkcie.
- loop2 dostaje nową liczbę przez przesunięcie przypięcia the way, bez zmiany we własnym repozytorium: WAY-300 zabrania produktowi własnej liczby („violates: … a product sets a number of its own”).

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-24 — „A decision names no date or condition for its review, the log holds no record of a review, and the review of the foundation against the product is a run of the skill `review-foundation`, which a human starts in a session with an agent when the reminder of a request asks for it (WAY-300), and no task of the product's backlog.”
  - Zmiana w tym zadaniu (pytanie 2): przegląd może stać jako zadanie w backlogu produktu, które zakłada człowiek, a przypomnienie w prośbie prosi o nie, dopóki go nie ma — słowa „and no task of the product's backlog” i odrzucenie „the review set as a task of the backlog” przestają opisywać produkt; zostaje, że przegląd to przebieg skilla `review-foundation` w sesji z człowiekiem, a nie cykl zadania.
- WAY-300 — „At the end of every task cycle the orchestrator counts the merges to the main branch since the last review tag, and from 30 merges on the description of each request the cycle writes says, in its part for the human who merges, that the foundation waits for a review, with the number of merges, the tag of the last review and the skill that starts the review. The reminder blocks nothing, the number 30 is one for every product, and a repository with no review tag counts from the start of its history.”
  - Uzasadnienie nazywa słaby punkt, o który chodzi w punkcie 1: „the reminder repeats in each request until a review is made, also while the human puts it off on purpose”.
  - Odrzucone tam: „a check in the gate — the gate stops or lets through, a stop would block unrelated changes, and a warning that stops nothing is not read there”.
  - Zmiana w tym zadaniu (pytanie 2): od progu cykl czyta backlog produktu; zdanie przypomnienia ma dwie postaci — prośba o dodanie zadania przeglądu, gdy jego linii nie ma, i wskazanie linii bez ponaglania, gdy stoi; słaby punkt „repeats … also while the human puts it off on purpose” znika. „The reminder blocks nothing” zostaje.
  - Zmiana w tym zadaniu (pytania 5 i 6): próg 60 zamiast 30, liczba wychodzi ze zdania do skryptu przypomnienia, a zdanie mówi „od progu skryptu przypomnienia” i trzyma regułę jednej liczby dla każdego produktu (punkt 3 *To do*).
  - Zmiana w tym zadaniu (punkt 5 *To do*): przykład *Verification* o miejscu przypomnienia w opisie prośby i zdanie *Rationale* „The count is this product's own, and the history of the first product is not open to a reader of this repository.”
- WAY-140 — „[…] while reading outside the repository stays with the agent and the cycle's record of the request and of the task's state in the backlog entry the product names (WAY-107) is no effect of the task.” Bez zmiany: cykl tylko czyta backlog, linii przeglądu nie zakłada.
- WAY-161 — w *Rejected*: „the cycle adding the new task to the product's backlog itself — where the backlog lies outside the repository, that is an effect only a human makes”. Bez zmiany; z tego samego powodu linię przeglądu zakłada człowiek.
- WAY-107 — „How a task's line is handled — the status of a new line, its move to ready, the form of its dependencies and of its identifier, how a line is found and kept one to a task, which fields an agent may change […] — is taken from the rules of the task place itself, never from text written at the product or in the-way's skills”.
- WAY-36, WAY-22, WAY-293 — test planu i pytania „Where it goes” w `elements/decisions/template.md` (sekcja „Decision or invariant”), według których partia z To do 2 rozpoznaje wpisy, które decyzjami nie są.
- WAY-328 — the way odstępuje dla własnego kodu i testów od wytycznych kodowania i testów produktu, więc zadanie nie czeka na wytyczne.
- WAY-344 — skrypt the way, który czyta plik pisany przez agenta albo człowieka, kończy się błędem nazywającym brakujące pole; dotyczy tego zadania, jeśli zmiana doda albo przerobi takie czytanie.

## Settlements to record

Candidates: 8 shown, 5 accepted — 2026-11-15

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Od progu przypomnienia cykl czyta backlog produktu i szuka otwartej linii, której nazwa zawiera `review-foundation` i nazwę repozytorium; gdy jej nie ma albo backlogu nie da się przeczytać, przypomnienie w prośbie prosi człowieka o dodanie zadania przeglądu i podaje, co ma stać w jego nazwie; gdy stoi — wskazuje ją i nie ponagla. | sentence of WAY-300 | pytania 2 i 3 (wybory człowieka, warianty niewybrane tam) | czy zdanie ma dwie postaci, po czym rozpoznać linię i co zrobić przy nieczytelnym backlogu |
| 2 | Przegląd fundamentu może stać jako zadanie w backlogu produktu, ale zakłada je człowiek, nigdy cykl; przegląd zostaje przebiegiem skilla `review-foundation` w sesji z człowiekiem. | sentence of WAY-24 | pytanie 2 (wybór człowieka, warianty niewybrane tam) | czy zostawić w WAY-24 „no task of the product's backlog” albo pozwolić cyklowi zakładać linię |
| 3 | Przegląd przy każdym przebiegu znajduje wszystkie wpisy dziennika, które decyzjami nie są, układa je w grupy według miejsca, do którego idą, z liczbą wpisów, a człowiek decyduje o całych grupach, które idą do zadania tym razem. | skill or instruction file: `foundation-review/` (`weak_points.md`, `proposals.md`, `with_the_human.md`) | pytanie 4 (wybór człowieka, wariant niewybrany tam) | czy przegląd sam wybiera partię i jak dużą |
| 4 | Próg przypomnienia to 60 scaleń i stoi w skrypcie przypomnienia (`THRESHOLD = 60`), z testem, który go trzyma, i komentarzem przy wartości z powodem: rytmem przeglądów i przyjętą ceną. | data or code: `task-cycle/review_reminder.py` | pytania 5 i 6 (wybór człowieka, wariant niewybrany w pytaniu 6) | zostawić 30 albo wpisać 60 do zdania WAY-300 i powtórzyć w skrypcie |
| 5 | WAY-300 mówi „od progu skryptu przypomnienia” zamiast liczby i trzyma regułę, że próg to jedna liczba dla każdego produktu, której produkt nie ustala sam. | sentence of WAY-300 | pytanie 6 (wybór człowieka, wariant niewybrany tam) | czy zdanie dalej podaje liczbę i czy reguła jednej liczby zostaje bez niej |

## Out of scope

- Przesunięcie przypięcia the way w loop2, przez które loop2 dostaje próg 60 — zmiana w repozytorium loop2, nie w the way.
- Reakcja doradcy dnia na zdanie przypomnienia (dopisanie linii przeglądu albo pytanie o nią przy scalaniu) — to zmiana setupu Mariusza w `.ai`, nie the way.

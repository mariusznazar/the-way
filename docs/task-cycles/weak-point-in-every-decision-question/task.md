---
title: Pokazywać najmocniejszy argument przeciw propozycji agenta przed jej zatwierdzeniem
status: draft
created: 2026-10-25T16:00
updated: 2026-11-15
tags: [zadanie]
related: "the author's project note of the process of work on the product"
---

# Pokazywać najmocniejszy argument przeciw propozycji agenta przed jej zatwierdzeniem

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Mariusz dostaje od agentów the way warianty, ich koszty i rekomendację, ale nie ma wspólnego wymogu, żeby każda propozycja niosła najmocniejszy argument przeciw rekomendacji.
- Odczuwa to Mariusz, gdy zatwierdza propozycję, której sam nie umiałby równie dobrze sformułować i musi ocenić, czy ją przyjąć, czy skorygować; kontrargument ma go skłonić do zastanowienia się nad słusznością propozycji.
- Wymóg „słabego punktu rekomendowanej opcji” istnieje dziś tylko przy wyborze technologii (WAY-123) i narzędzi wytycznych produktu; inne pytania o decyzję — przy doprecyzowaniu zadań, definiowaniu projektów, zapisie wpisów fundamentu i w opisie PR-a — go nie mają.
- Mariusz czyta tekst przed odpowiedzią po to, żeby wyłapać, według własnej oceny, około 20% spraw, w których rekomendacja idzie w złą stronę (sprawa 18, działanie J3 w `the author's note of settlements of the analyses on Fable`); liczba jest szacunkiem, nie pomiarem, a słaby punkt rekomendacji ma mu to wyłapywanie ułatwić.
- Co jeśli nic: rekomendacja idąca w złą stronę przechodzi, gdy Mariusz sam nie zobaczy powodu, by ją odrzucić; przypadku błędnej decyzji z braku kontrargumentu nie ma udokumentowanego.
- Cotygodniowy audyt procesu (`process-audit`) pyta przy każdej sprawie tylko „ważysz dalej czy odkładasz”, bez wskazania, co w tabeli wymaga działania, i bez rekomendacji — pierwszy audyt, 14.11, kilka razy stanął na „nie rozumiem pytania”; ruszył dopiero, gdy agent sam wyłuskał z tabeli rzecz do zrobienia i postawił ją z rachunkiem (AIR-655).

### To do

1. Decyzja WAY-113 („### WAY-113 — How does an agent of the-way ask a human decision?” w `foundations/decisions.md`) mówi, że pytanie o decyzję podaje drogi otwarte, koszt każdej — w tym koszt cofnięcia jej później, zapisany jednym słowem, gdy jest zerowy — rekomendację i słaby punkt (*weak point*) rekomendowanej drogi: najmocniejszy argument przeciw niej, oparty na materiale, gdy materiał go daje; gdy rekomendowana droga jest drogą na skróty, a inna byłaby właściwa, gdyby koszt nie grał roli, słaby punkt nazywa tę drogę i mówi, dlaczego jej nie polecamy (pytania 2 i 3). Wyjątek pytania kontrolnego zostaje w obecnym brzmieniu (pytanie 2). *Verification* i *Rationale* decyzji mówią o słabym punkcie i koszcie cofnięcia, *Rejected* bierze drogi niewybrane z pytań 2 i 3, a *Scope* obejmuje części, których teksty niosą regułę po zmianie (`task-cycle`, `foundation-review`, `process-audit`, `product-guidelines` obok obecnych).
2. Sekcja „## How a skill asks” w `elements/common/way_of_working.md`, punkt zaczynający się od „A question of decision — a choice that settles something in a file — gives the ways open, what each costs, and a recommendation.”, mówi to samo co punkt 1.
3. Akapit „**What an item carries.**” w `task-cycle/skill/request_template.md` (tam stoi reguła wycofanej WAY-327) daje trzeciej części pozycji, w której człowiek wybiera („3. the recommendation, with its reason in one sentence;”), słaby punkt rekomendacji, jednym zdaniem, tak jak podaje go WAY-113 (pytanie 4), a jej drugiej części („2. each way open, one by one: […] what it costs — time, a round of correction with its review, the risk that stays — and where it can show up later;”) koszt cofnięcia każdej drogi, jednym słowem, gdy jest zerowy (pytanie 5). Oba przykłady pod tym akapitem — „The good item, with its group around it […]” i pozycja z piątą częścią „1. The new page for editing a profile was never opened […]” — pokazują jedno i drugie.
4. Każdy tekst the way poza dziennikiem decyzji, który sam powtarza, co daje pytanie o decyzję (drogi, koszt, rekomendacja), zamiast odesłać do „How a skill asks” — albo, w opisie PR-a, do części pozycji z punktu 3 — dostaje w tym miejscu odesłanie. Cykl szuka takich miejsc sam w śledzonych plikach Markdown; lista ze stanu `foundations` ec7929d nie jest pełna: `elements/common/skill/build_table.md`, `foundation-review/with_the_human.md`, `process-audit/SKILL.md`, `product-guidelines/coding/SKILL.md`, `product-guidelines/styleguide/SKILL.md`, `product-guidelines/testing/SKILL.md`, `project-level/skill/rounds.md`, `project-level/skill/existing_definition.md`, `project-level/lead/answering.md`, `project-level/lead/conversation_template.md`, `project-level/lead/skill/SKILL.md`, `project-level/lead/skill/route_changes.md`, `project-level/plan/skill/delegated_mode.md`, `project-level/task/skill/resolve_gaps.md` (akapit „If two answers conflict, show both and ask which holds.”), a w `task-cycle/skill/request_template.md` punkt *Questions* („recommendation where one exists, from the report of the agent that returned `blocked` […]”) i wiersz „A question from the foundation step” tabeli stanów. Tekst, który już odsyła do „How a skill asks” — jak `project-level/task/skill/orchestrated_mode.md` („where "How a skill asks" requires them”) — zostaje bez zmian. Decyzje, które powtarzają regułę, w tym WAY-174 i WAY-155, cykl uzgadnia przez przeszukanie całego fundamentu (WAY-33).
5. W `elements/common/way_of_working.md`, krok „## 4. Ask, show, write”, punkt 1 („Ask in one round about everything still open, as »How a skill asks« gives it (WAY-113): a value the source does not give, with where to look for it and never the value itself; […]”) nie powtarza, co daje pytanie o decyzję, i odsyła do „How a skill asks” tylko po pytanie o decyzję i pytanie o ocenę; reguła pytania o wartość, której źródło nie podaje — gdzie jej szukać, nigdy sama wartość — zostaje w tym punkcie (pytanie 6).
6. WAY-113 mówi, że w całym doprecyzowaniu definicji projektu — w rundach `define-project` i w kroku jej rzutowanych zmian fundamentu (pytanie 8) — po odpowiedzi człowieka może paść, poza pytaniem cytującym jego wcześniejsze zdanie, któremu odpowiedź przeczy, także pytanie z ruchu „implication” („you wrote X; from X follows Y — does Y hold?”), zakotwiczone w zdaniu człowieka, i pytanie o powód decyzji kosztownej do cofnięcia, gdy tego powodu nie dają ani słowa człowieka, ani materiał; przy doprecyzowaniu zadania zostaje dzisiejsza reguła (pytanie 7). *Verification* decyzji uznaje takie pytanie przy definicji za zgodne, *Rationale* podaje powód z pytania 7 i przyjętą cenę — więcej pytań po odpowiedziach i brak dowodu, że ruch coś złapał — a *Rejected* bierze drogi a i c z pytań 7 i 8. Ruchy w kroku „## Step 4 — row by row”, punkt 1 `elements/common/skill/definition_variant.md` („Three moves give such questions:”) zostają bez zmian, a lista „Two moves run through the rounds:” w `project-level/skill/rounds.md` dostaje oba ruchy — „implication” i pytanie o powód decyzji kosztownej do cofnięcia — obok dwóch, które już ma (pytanie 8).
7. W `process-audit/SKILL.md`, krok „## 3. Put the matters before the human”, zdania „These are questions of assessment, so they stay open and carry no recommendation. A matter ends in one of two outcomes: the human weighs it further, or sets it aside.” zastępuje reguła: zanim padnie pytanie, agent nazywa z wierszy to, co pokazują jako zepsute albo nieaktualne i co da się zmienić krokiem (repozytorium na starej wersji procesu, liczenie, które się nie powiodło, sprawa bez zadania), i stawia każdą taką rzecz jako pytanie o decyzję według „How a skill asks” (WAY-113); rekomendacja opiera się na tym, co wiersze pokazują jako zepsute, nigdy na liczbie powrotów sprawy, czasie czekania ani poziomie kosztu — reguły „How often an issue comes back is material, never a priority” i „The cost of an occurrence is material, never a priority” zostają bez zmian. Gdy wiersze nie pokazują nic do zmiany, agent mówi to jednym zdaniem, a pytanie oceniające zostaje otwarte i bez rekomendacji. Szablon notatki audytu dostaje obok „ważone” i „odłożone” zapis decyzji podjętej przy sprawie (pytanie 9).

### Questions to settle

- Pytanie 1: czy zadanie łączyć z zadaniem „Doprecyzowanie zadania kończy się spisem decyzji, które dokument zostawia wykonawcy, sprawdzonym krytyką”, czy ustawić między nimi zależność?
  - Answer: osobno, bez zależności — zadania nie zmieniają wspólnego fragmentu: tamto zmienia `project-level/task/skill/final_review.md`, `orchestrated_mode.md` i `SKILL.md` doprecyzowania, a z WAY-113 tylko korzysta odesłaniem, więc w dowolnej kolejności scalenia jego sprawy otwarte dostaną regułę z tego zadania.
  - Not chosen:
    - zależność między zadaniami — jedno zadanie czeka bez powodu w tekście; zysk tylko taki, że wyklucza konflikt numeru nowej decyzji przy równoległych cyklach
    - połączenie w jedno zadanie — otwiera na nowo przyjęty dokument spisu decyzji, a cykl dostaje dwie niezwiązane zmiany naraz
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „1 a — osobno, bez zależności. Mój niepokój o wspólny fragment był nietrafny”
- Pytanie 2: co dostaje każde pytanie o decyzję i co dzieje się potem z pytaniem kontrolnym (jednym pytaniem po wyborze, czy wybór trzyma się wobec cytatu z materiału)?
  - Answer: każde pytanie o decyzję podaje słaby punkt rekomendowanej drogi — najmocniejszy argument przeciw niej, oparty na materiale, gdy materiał go daje; reguła używa istniejącego słowa „weak point”. Pytanie kontrolne zostaje z obecnym wyjątkiem: gdy człowiek bierze rekomendowaną drogę tak, jak ją podano, a słaby punkt był oparty na materiale, pytania kontrolnego nie ma; zostaje ono dla odpowiedzi własnymi słowami, odpowiedzi z dodanym warunkiem i drogi nierekomendowanej, a słaby punkt bez oparcia w materiale wyjątku nie uruchamia.
  - Not chosen:
    - słaby punkt przy każdej drodze, nie tylko przy rekomendowanej — pytania wyraźnie dłuższe, a w dużej części powtarza to „koszt każdej drogi”, który już jest
    - kontrargument przy rekomendacji, a pytanie kontrolne zawsze, bez wyjątku — człowiek słyszy tę samą wątpliwość dwa razy, przed wyborem i po nim; tę drogę WAY-113 już raz odrzuciła
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „2 a — słaby punkt rekomendowanej drogi przy każdym pytaniu o decyzję, słowo »weak point«, istniejący wyjątek pytania kontrolnego zostaje”
- Pytanie 3: co z praktyką „poprawka właściwa obok rekomendowanej” z dopisku z 12.11.2026 (kurs Mega.DEV, nagranie s03e01)?
  - Answer: wchłonąć ją w to, co już jest: koszt każdej drogi obejmuje koszt cofnięcia jej później, a gdy ten koszt jest zerowy, reguła pozwala zapisać go jednym słowem; słaby punkt rekomendacji, gdy rekomendowana droga jest drogą na skróty, nazywa drogę właściwą i mówi, dlaczego jej nie polecamy.
  - Not chosen:
    - przejąć praktykę osobno, w pełnym kształcie z kursu (osobny akapit „poprawka właściwa”, nakład i odwracalność przy każdym wariancie) — trzecia rzecz obok kosztu i słabego punktu, częściowo je powtarzająca; pytania wyraźnie dłuższe
    - tylko „poprawka właściwa” w słabym punkcie, bez kosztu cofnięcia — człowiek może wybrać drogę, której nie da się tanio odkręcić, nie wiedząc o tym
    - nic z dopisku — jawne „polecam łatkę, choć właściwa byłaby przebudowa” zależy od tego, czy agent akurat wybierze to jako najmocniejszy argument
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „pytanie 3 — a, z warunkiem, że reguła pozwala zapisać koszt cofnięcia jednym słowem, gdy jest zerowy”
- Pytanie 4: czy reguła obejmuje też pozycje opisu PR-a, w których człowiek wybiera (grupy *Needed from you* i *Fix or let through*, WAY-327)?
  - Answer: tak — trzecia część takiej pozycji to rekomendacja z powodem i jej słabym punktem.
  - Not chosen:
    - reguła tylko w rozmowie, bez opisu PR-a — tam, gdzie człowiek zatwierdza propozycje cyklu przy scaleniu, czyli w miejscu, od którego zadanie wyszło (S7), kontrargumentu by nie było
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „pytanie 4 — a”
- Pytanie 5: czy pozycja opisu PR-a, w której człowiek wybiera, podaje też koszt cofnięcia każdej drogi?
  - Answer: tak — druga część pozycji podaje koszt cofnięcia każdej drogi, jednym słowem, gdy jest zerowy; przy tej regule większość dróg zyska jedno słowo, a wybór przy scaleniu, którego nie da się tanio cofnąć (np. zapisane dane), zostaje nazwany; reguła dla rozmowy i dla PR-a jest jedna.
  - Not chosen:
    - pozycja w PR-ze dostaje tylko słaby punkt, bez kosztu cofnięcia — reguła dla rozmowy i dla PR-a różni się w jednym punkcie, a wybór, którego nie da się tanio cofnąć, przechodzi bez nazwania, chyba że autor sam wpisze go jako ryzyko, które zostaje
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „1 b — pozycja w PR-ze dostaje koszt cofnięcia, jednym słowem, gdy zerowy. Powód: przy regule »jedno słowo, gdy nic« większość dróg zyska jedno słowo, nie pół zdania; a jedyny przypadek, w którym ta informacja naprawdę waży — wybór przy scaleniu, którego nie da się tanio cofnąć (zapisane dane) — to dokładnie ten, który przy wariancie a przechodzi bez nazwania. Do tego reguła dla rozmowy i dla PR-a zostaje jedna.”
- Pytanie 6: co z odsyłaczem kroku 4.1 w `elements/common/way_of_working.md` do „How a skill asks” po pytanie o wartość, której źródło nie podaje, skoro ta sekcja i WAY-113 znają tylko pytanie o decyzję i pytanie o ocenę (uwaga #110-3)?
  - Answer: poprawić odsyłacz — krok 4.1 odsyła do „How a skill asks” tylko po pytanie o decyzję i o ocenę, a reguła pytania o wartość zostaje w tym kroku (*To do* 5; plik zdjęty z listy *To do* 4).
  - Not chosen:
    - dopisać trzeci rodzaj pytania do „How a skill asks” i WAY-113 — WAY-113 rośnie o regułę, której dziś używa tylko ten jeden plik
    - zostawić — szkoda mała, bo agent i tak znajduje regułę w tym samym zdaniu, ale tekst dalej obiecuje coś, czego sekcja nie ma
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15: „2 a (To do 5, plik zdjęty z listy w punkcie 4)”
- Pytanie 7: co z ruchami „implication” i „the reason” w kroku 4, punkt 1 `elements/common/skill/definition_variant.md`, skoro WAY-113 przy doprecyzowaniu definicji pozwala po odpowiedzi człowieka tylko na pytanie cytujące jego wcześniejsze zdanie, któremu odpowiedź przeczy (uwaga #90-1)?
  - Answer: zmienić WAY-113 — przy definicji projektu po odpowiedzi człowieka może paść, poza pytaniem o sprzeczność z jego wcześniejszym zdaniem, także pytanie z ruchu „implication” („napisałeś X; z X wynika Y — czy Y się trzyma?”) i pytanie o powód decyzji kosztownej do cofnięcia; ruchy w `definition_variant.md` zostają (*To do* 6). Powód: zadanie ma dawać człowiekowi więcej kontrargumentów, a „implication” jest jedynym ruchem, który pada po odpowiedzi. Słaby punkt przyjęty świadomie: więcej pytań po odpowiedziach i brak dowodu, że ten ruch kiedykolwiek coś złapał.
  - Not chosen:
    - a) dopasować plik do WAY-113 (ruch „implication” wypada, pytanie o powód kosztownej decyzji zostaje jako zwykłe pytanie o brakującą informację) — kilka zdań w jednym pliku, cofnięcie zerowe; skutek, którego człowiek nie zauważył, póki zmiana jest tania, wychodzi dopiero przy czytaniu całej definicji albo wcale
    - c) zostawić, jak radził opis PR-a #90 — dziś zero kosztu, ale sprzeczność zostaje: raz pada pytanie, którego reguła zabrania, raz nie
  - Source: Mariusz (przekazał doradca dnia), 2026-11-15: „b — zmienić WAY-113, żeby przy definicji projektu pozwalała też na ruch implication (napisałeś X, z X wynika Y — czy Y się trzyma?) i na pytanie o powód kosztownej decyzji; powód: zadanie ma dawać człowiekowi więcej kontrargumentów, a ten ruch jest jedynym po odpowiedzi; słaby punkt przyjęty świadomie: więcej pytań po odpowiedziach i brak dowodu, że ruch coś złapał”
- Pytanie 8: czy zgoda z pytania 7 obejmuje tylko krok, w którym doprecyzowanie definicji znajduje rzutowane zmiany fundamentu (krok 4 `elements/common/skill/definition_variant.md`, jedyne miejsce, gdzie oba ruchy dziś stoją), czy każdą odpowiedź w całym doprecyzowaniu definicji, także w rundach `define-project` (`project-level/skill/rounds.md`, gdzie dziś stoi tylko pytanie o sprzeczność dwóch zdań człowieka)?
  - Answer: całe doprecyzowanie definicji — oba ruchy, „implication” i pytanie o powód decyzji kosztownej do cofnięcia, dochodzą także do rund `define-project`, do listy „Two moves run through the rounds:” w `project-level/skill/rounds.md` (*To do* 6). Powód: tylko ta droga daje kontrargument po odpowiedzi tam, gdzie zapadają zakres, sukces i ryzyka, a o to chodziło w pytaniu 7. Słaby punkt przyjęty świadomie: dłuższe rundy, więcej tur i brak dowodu, że ruch coś złapał.
  - Not chosen:
    - a) tylko krok rzutowanych zmian fundamentu (krok 4 `definition_variant.md`) — zero kosztu ponad *To do* 6, cofnięcie zerowe; najważniejsze odpowiedzi definicji — zakres, sukces, ryzyka — padają w rundach, więc tam kontrargumentu po odpowiedzi dalej by nie było
    - c) całe doprecyzowanie definicji bez zmiany rund — koszt dziś zero, ale WAY-113 pozwalałaby na coś, czego żaden plik nie każe robić, a agent rund, który sam zada takie pytanie, byłby z decyzją zgodny, choć jego skill tego nie przewiduje
  - Source: Mariusz (przekazał doradca dnia), 2026-11-15: „spróbujmy b”; powód i słaby punkt podane przez doradcę dnia w tej samej wiadomości: „tylko b daje kontrargument po odpowiedzi tam, gdzie zapadają zakres, sukces i ryzyka, a o to chodziło w pytaniu 7. Słaby punkt przyjęty świadomie: dłuższe rundy, więcej tur, brak dowodu, że ruch coś złapał”
- Pytanie 9: czy audyt procesu stawia pytania o decyzję z rekomendacją przy tym, co tabela sprawy pokazuje jako zepsute?
  - Answer: tak — pytanie o decyzję z rekomendacją opartą na tym, co zepsute; ocena bez drogi działania zostaje otwarta i bez rekomendacji (*To do* 7).
  - Not chosen:
    - zostawić pytania oceniające bez rekomendacji — audyt staje na „nie rozumiem pytania” przy każdej sprawie z dziesiątkami wierszy
    - osobne zadanie po tym — drugi cykl na ten sam plik, który to zadanie i tak zmienia (*To do* 4)
  - Source: Mariusz w `/ai-review`, 2026-11-15 (AIR-655): „a nie warto by było tego dodać do tego zadania”

## Context

- Pierwotne brzmienie zadania: „the way: propozycja agenta przychodzi z najsilniejszym argumentem przeciw niej, żeby skłonić czytającego do zastanowienia się nad jej słusznością — reguła wspólna dla wszystkich skilli, które pytają człowieka (WAY-113, »How a skill asks« w `elements/common/way_of_working.md`), także doprecyzowanie zadań i definicje projektu; wydzielone z poprawek z uwag cykli S7 (pytanie 3), gdzie dostaje to na razie tylko kandydat na tryb awarii”.
- Zadanie wydzielono z poprawek z uwag cykli S7 (pytanie 3, AIR-480): tam kontrargument przewidziano tylko przy propozycji trybu awarii części, a uogólnienie na wszystkie skille pytające człowieka odłożono do osobnego zadania (Mariusz, 2026-10-21: „niech będzie na ten moment c”); notatka tych poprawek jest zarchiwizowana w historii gita vaulta (commit 7c692492, `Notes/Projects/(P) Proces pracy nad produktem/_zadania/poprawki_z_uwag_cykli_s7.md`).
- Potrzebę Mariusz nazwał przy pytaniu 2 tamtego zadania, 2026-10-21: „żeby było jeszcze bezpieczniej można by zawsze przy propozycji agenta dodawać kontrargument do tej propozycji - coś jak ten komentarz tutaj, żeby skłonić czytającego do głebszego zastanowienia się nad słusznością rozwiązania”.
- Tryby awarii części wycofano z the way (WAY-46 wycofana: mapa części nie ma takiego pola), więc kontrargument z S7 nie stoi dziś nigdzie w the way.
- Dopisek z 12.11.2026 (analizy na Fable, sprawa 10 w `the author's note of settlements of the analyses on Fable`): praktyka „poprawka właściwa obok rekomendowanej” z kursu Mega.DEV (nagranie s03e01) — agent podaje warianty, przy każdym nakład i to, czy da się go tanio cofnąć, potem rekomendację, a potem osobno, który wariant byłby właściwy, gdyby koszt nie grał roli, i dlaczego go nie poleca; źródło: kandydat K10 i działanie D23 w `the author's note of practices from the Mega.DEV course`.
- „Słaby punkt rekomendowanej opcji” stoi dziś w WAY-123 i w tekstach, które ją niosą: `project-level/technology/settle.md`, `project-level/definition_template.md` (akapit kończący się „the weak point of the option recommended (WAY-123)”), `product-guidelines/*/new_tools.md`; po zmianie są szczególnym przypadkiem reguły z WAY-113.
- Skrypt `task-cycle/request_check.py` nie sprawdza części pozycji opisu PR-a (akapit „What an item carries” każe to robić agentowi piszącemu opis), więc punkt 3 nie zmienia kodu.
- Zadanie o spisie decyzji (`zadanie_doprecyzowanie_konczy_sie_spisem_decyzji_z_krytyka.md`) pokazuje sprawy otwarte „jak WAY-113 każe pytać o decyzję”, więc przejmie regułę z tego zadania przez odesłanie, w dowolnej kolejności scalenia; jego zmiana w `orchestrated_mode.md` stoi w akapicie obok miejsca, które już odsyła do „How a skill asks”, dlatego punkt 4 tego pliku nie zmienia.
- Plik `project-level/task/skill/resolve_gaps.md` zmienia także inne zadanie, w innym akapicie (lista przewodnika wdrożeniowego); punkt 4 dotyka w nim tylko akapitu „If two answers conflict, show both and ask which holds.”.
- Przegląd fundamentu 2026-11-14 (G8) przekazał zadaniu dwie uwagi z próśb: #110-3 (pytanie 6) i #90-1 (pytanie 7).
- WAY-327 wycofano w PR #126; tabela „## Withdrawn identifiers” w `foundations/decisions.md` mówi, że jej reguła stoi w `task-cycle/skill/request_template.md` — dlatego *To do* 3 i wiersze 4–5 *Settlements to record* idą do tego pliku.
- Plik danych przeglądu fundamentu 2026-11-14: `the author's data file of the foundation review of 2026-11-14`, sekcja „Grupy uwag”, G8.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-113** — „An agent asks in plain conversation text: a decision question gives the available ways, the cost of each and a recommendation, while a question of assessment stays open; neither opens a separate question panel. After a human choice enters an entry's binding part, the agent asks one question against that choice anchored in the human's words or supplied material, unless the choice ends with the work, or the human took one of the ways offered and the decision question named, anchored in the material, the weak point of that way. […]” — zadanie ją zmienia: pytanie o decyzję podaje też koszt cofnięcia każdej drogi i słaby punkt rekomendowanej drogi (punkt 1 *To do*, pytania 2 i 3), a przy definicji projektu pozwala po odpowiedzi człowieka także na ruch „implication” i na pytanie o powód decyzji kosztownej do cofnięcia (punkt 6 *To do*, pytania 7 i 8).
- **WAY-123** — „[…] each choice with its recommendation and the weak point of the option recommended; in the area of the choices this step settles, this decision prevails over WAY-114 […]” — dzisiejszy wymóg słabego punktu przy wyborze technologii, który po zmianie WAY-113 staje się jej szczególnym przypadkiem; zadanie go nie zmienia.
- **WAY-100** — „A method or practice borrowed from outside a product binds its way of working only through a decision that names what is adopted, where it applies, and why.” — praktyka z kursu Mega.DEV (nagranie s03e01) wiąże dopiero przez decyzję, która ją nazywa (wiersz 3 *Settlements to record*).

## Settlements to record

Candidates: 9 shown, 8 accepted — 2026-11-15

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Każde pytanie o decyzję podaje słaby punkt rekomendowanej drogi — najmocniejszy argument przeciw niej, oparty na materiale, gdy materiał go daje — a pytanie kontrolne zostaje z obecnym wyjątkiem, którego słaby punkt bez oparcia w materiale nie uruchamia. | sentence of WAY-113 | pytanie 2 (wybór człowieka; *Not chosen* tam) | czy słaby punkt podać przy każdej drodze, czy tylko przy rekomendowanej, i czy pytanie kontrolne po takim wyborze dalej pada |
| 2 | Koszt każdej drogi obejmuje koszt cofnięcia jej później, zapisany jednym słowem, gdy jest zerowy, a słaby punkt rekomendowanej drogi na skróty nazywa drogę właściwą i mówi, dlaczego jej nie polecamy. | sentence of WAY-113 | pytanie 3 (wybór człowieka; *Not chosen* tam) | czy praktykę „poprawki właściwej” dać osobnym akapitem, czy wchłonąć ją w koszt i słaby punkt, i czy koszt cofnięcia trzeba rozpisywać także, gdy jest zerowy |
| 3 | WAY-113 nazywa „poprawkę właściwą obok rekomendowanej” praktyką przejętą z kursu Mega.DEV (nagranie s03e01) do pytania o decyzję, z powodem: widać, kiedy agent wybiera drogę na skróty, a to tani sygnał długu — jak WAY-100 każe. | sentence of WAY-113 | WAY-100; pytanie 3; *Context* (dopisek z 12.11.2026; powód z `praktyki_z_kursu_mega_dev_cz2.md`, „Co by dała”); przyjęte przez doradcę dnia w imieniu Mariusza, 2026-11-14: „2 przyjmij” | czy zmiana WAY-113 ma nazwać źródło przejętej praktyki, czy wpisać ją jak własną regułę the way |
| 4 | Pozycja opisu PR-a, w której człowiek wybiera, podaje przy rekomendacji jej słaby punkt, jednym zdaniem, tak jak podaje go WAY-113. | skill or instruction file: `task-cycle/skill/request_template.md` | pytanie 4 (wybór człowieka; *Not chosen* tam) | czy rekomendacja w pozycji PR-a dalej kończy się na jednym zdaniu powodu, bez słabego punktu |
| 5 | Pozycja opisu PR-a, w której człowiek wybiera, podaje przy każdej drodze koszt jej cofnięcia, jednym słowem, gdy jest zerowy, tak jak pytanie o decyzję w rozmowie. | skill or instruction file: `task-cycle/skill/request_template.md` | pytanie 5 (wybór człowieka; *Not chosen* tam) | czy koszt cofnięcia z WAY-113 obowiązuje też w opisie PR-a, który ma własny wzór pozycji |
| 6 | Krok 4.1 „Ask, show, write” odsyła do „How a skill asks” tylko po pytanie o decyzję i pytanie o ocenę; reguła pytania o wartość, której źródło nie podaje, zostaje w tym kroku, a WAY-113 nie dostaje trzeciego rodzaju pytania. | skill or instruction file: `elements/common/way_of_working.md` | pytanie 6 (wybór człowieka; *Not chosen* tam) | czy regułę pytania o wartość przenieść do „How a skill asks” i WAY-113, czy zostawić odsyłacz, który obiecuje coś, czego sekcja nie ma |
| 7 | W całym doprecyzowaniu definicji projektu — w rundach i w kroku rzutowanych zmian fundamentu — WAY-113 pozwala po odpowiedzi człowieka także na ruch „implication” zakotwiczony w jego zdaniu i na pytanie o powód decyzji kosztownej do cofnięcia, gdy powodu nie dają ani jego słowa, ani materiał; przy doprecyzowaniu zadania zostaje dzisiejsza reguła. | sentence of WAY-113 | pytania 7 i 8 (wybory człowieka; *Not chosen* tam) | czy dopasować `definition_variant.md` do WAY-113, czy decyzję do pliku, czy zgoda obejmuje rundy definicji i czy obejmuje też doprecyzowanie zadań |
| 8 | Audyt procesu stawia rzecz, którą wiersze sprawy pokazują jako zepsutą i którą da się zmienić krokiem, jako pytanie o decyzję z rekomendacją opartą na tym, co zepsute; ocena bez drogi działania zostaje otwarta i bez rekomendacji. | skill or instruction file: `process-audit/SKILL.md` | pytanie 9 (wybór człowieka; *Not chosen* tam) | czy reguła „carry no recommendation” obowiązuje też przy rzeczy do naprawy |

## Out of scope

- Spis decyzji, które dokument zadania zostawia wykonawcy — osobne zadanie (`zadanie_doprecyzowanie_konczy_sie_spisem_decyzji_z_krytyka.md`).
- Zmiana WAY-123 i tekstów, które niosą jej słaby punkt przy wyborze technologii i narzędzi wytycznych — zostają bez zmian jako szczególny przypadek reguły z WAY-113.

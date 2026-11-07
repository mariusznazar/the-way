---
title: "the way: gdy to, co przyjąłem, daje już wynik, cykl sam zapisuje pierwszeństwo między decyzjami i nazywa je w PR-ze, zamiast łamać regułę albo stawać"
status: draft
created: 2026-11-02T13:50
updated: 2026-11-07
tags: [zadanie]
related: "the project note of the process of working on a product"
---

# the way: gdy to, co przyjąłem, daje już wynik, cykl sam zapisuje pierwszeństwo między decyzjami i nazywa je w PR-ze, zamiast łamać regułę albo stawać

Status: ready for cycle
Project relation: independent

## Description

### Need

- Gdy dwie decyzje the-way ciągną w przeciwne strony, rozstrzyga to wpis `narrows` w decyzji, która wygrywa, czyli zaznaczenie, że ma pierwszeństwo przed tamtą.
- Reguła mówi, że zapisuje go wyłącznie człowiek, a agent ma stanąć; inna reguła mówi, że wpisy pisze agent, a człowiek przyjmuje je przy scaleniu; cykle dopisują więc `narrows` same, także gdy z ustalenia Mariusza wynika już, która decyzja wygrywa.
- Odczuwają to agenci, którzy muszą złamać literę reguły albo zatrzymać prawie gotowy cykl, oraz Mariusz, bo w PR-ze trudniej odróżnić wpis wynikający z jego decyzji od wpisu, który agent wymyślił.
- Na razie nic się nie psuje — recenzent jednego z takich cykli napisał, że wynik to ten sam tekst — ale reguła dalej mówi co innego niż praktyka, więc każdy cykl rozstrzyga to po swojemu, a następny może uznać za ustalone coś, czego nikt nie ustalił.
- Przy okazji: gdy jedno pytanie Mariusza dotyczyło kilku rzeczy, a zachowane warianty tylko jednej z nich, agenci nie wiedzą, co wpisać w polu odrzuconych wariantów pozostałych decyzji, bo przykład w WAY-134 dosłownie mówi co innego niż praktyka.

### To do

Numery linii odpowiadają stanowi `foundations` @ `52889bc`.

1. W WAY-25, decyzji o zderzeniach między decyzjami, `foundations/decisions.md:639-641`, ostatnie zdanie wiążące („A collision between two decisions with no precedence recorded is never settled by the agent that meets it; a human records the precedence in the decision that prevails.”) ma brzmieć:
   > A collision between two decisions with no precedence recorded is never settled silently by the agent that meets it. Where what the human accepted gives the outcome and the change may write the decision that prevails, the change records the precedence in that decision, and its request names it with the passages of what the human accepted that give the outcome, for the human to accept at the merge (WAY-114); otherwise the agent stops and asks.
2. Przykłady WAY-25, `foundations/decisions.md:647-650`:
   - przykład zgodny mówi, że agent staje wtedy, gdy to, co człowiek przyjął, nie daje wyniku;
   - przykład naruszenia dostaje nową pozycję w rodzaju „the change records a precedence that no passage of what the human accepted gives, or one its request does not name with those passages”.
3. Uzasadnienie i odrzucone warianty WAY-25 opisują decyzję w nowym brzmieniu; odrzucone warianty dostają warianty niewybrane z pytań 1 i 3.
4. Tę samą treść zgrać w miejscach, które dziś mówią, że taka sytuacja zatrzymuje pracę i idzie do człowieka:
   - `elements/decisions/template.md:168-169`,
   - `agent-instructions/README.md:32-35`,
   - `task-cycle/skill/foundation_step.md:26-27`,
   - `elements/decisions/skill/decide_entry.md:11-13`, gdzie zderzenie z inną decyzją jest pytaniem w kroku 4 tylko wtedy, gdy to, co przyjął człowiek, nie daje wyniku,
   - `task-cycle/skill/request_template.md:174-180`, gdzie sekcja wpisów, których Mariusz nie widział przy zadaniu, podaje przy pierwszeństwie zapisanym przez cykl cytat tego, co dało wynik.
5. W WAY-134, `foundations/decisions.md:3345-3347`, przykład zgodny ma brzmieć:
   > a decision row whose question keeps two ways the human did not choose gives its decision those two as rejected options, and one whose source keeps none, or keeps only ways that answer another part of the question, gives `unknown` with no question to the human;

   Reguły w `elements/decisions/template.md` to nie zmienia.

### Questions to settle

- Pytanie 1: co robi agent, który trafia na zderzenie dwóch decyzji bez zapisanego pierwszeństwa, gdy to, co przyjął człowiek, daje już wynik?
  - Answer: zmiana sama zapisuje `narrows` i nazywa je w PR-ze, a Mariusz przyjmuje je przy scaleniu (WAY-114); agent staje i pyta tylko wtedy, gdy to, co człowiek przyjął, nie daje wyniku, albo gdy zmiana nie może zapisać decyzji, która wygrywa (*To do* 1). „Gives the outcome” zostaje osądem agenta; zabezpieczeniem jest to, że PR musi taki wpis nazwać, a Mariusz może go skreślić.
  - Not chosen:
    - wyjątek dla „ustalenia, które mówi, która decyzja wygrywa” — nie obejmował nawet przypadku, który go wywołał
    - trzymanie się litery WAY-25 — czysto, ale prawie gotowy cykl staje dla wpisu, którego treść Mariusz już przyjął
  - Source: Mariusz, 2026-11-02, sesja nad sprawą AIR-571 („przeredagowane (jedna reguła zgodna z WAY-114, krok powrotu bez zmian); ostateczne brzmienie w `the task document in the author's backlog`”), `the ledger of the review of the AI layer in the author's notes`, wpis AIR-571; brzmienie zdania: pierwotna wersja tego dokumentu, 2026-11-02.
- Pytanie 2: jak brzmi przykład zgodny WAY-134, gdy warianty z pytania odpowiadają tylko na inną jego część?
  - Answer: zmienia się sam przykład (*To do* 5), reguła w szablonie decyzji zostaje.
  - Not chosen:
    - nowe zdanie w `elements/decisions/template.md` — przy decyzjach już istniejących kazałoby podmienić ich odrzucone warianty na `unknown`
  - Source: Mariusz, 2026-11-02, sesja nad sprawą AIR-573 („przeredagowane (sam przykład zgodny WAY-134) i dołączone do zadania AIR-571 […] bez osobnego zadania”), `the ledger of the review of the AI layer`, wpis AIR-573.
- Pytanie 3: co dokładnie zapisuje cykl, gdy pierwszeństwo wynika z tego, co przyjął człowiek, i co PR o tym mówi?
  - Answer: cykl zapisuje całe pierwszeństwo w decyzji, która wygrywa — wpis `narrows` i zdanie o zakresie, w którym wygrywa — a PR nazywa je razem z cytatem tego, co człowiek przyjął i co daje wynik (*To do* 1, zgranie w `request_template.md` w *To do* 4). Cytat w PR-ze pozwala Mariuszowi odróżnić wpis z jego ustalenia od wymyślonego, a agent, który nie ma czego zacytować, widzi, że ma stanąć.
  - Not chosen:
    - brzmienie „the change writes the `narrows` and its request names it” — da się przeczytać jako sam wpis w *Relations*, a w PR-ze wpis stoi bez wskazania, skąd wziął się wynik, więc do oceny trzeba zajrzeć do zadania
    - samo „records the precedence in the decision that prevails”, bez cytatu w PR-ze — zamyka pierwszą lukę, drugą zostawia
    - cytat jednego fragmentu („the passage”) — w przypadku `logging-guidelines` wynik daje dopiero połączenie dwóch fragmentów, więc agent czytający dosłownie stanąłby tam, gdzie zaczęła się sprawa
  - Source: Mariusz, 2026-11-07, „B”; pytanie przeciw odpowiedzi zakotwiczone w zdaniu tego dokumentu o wierszu zadania `logging-guidelines` (*Context*), Mariusz, 2026-11-07, „tak jak rekomendujesz” — cytuje się fragmenty, w liczbie mnogiej.
- Pytanie 4: czy instrukcja pisania decyzji, która każe pytać o każde zderzenie z inną decyzją, zmienia się razem z WAY-25?
  - Answer: tak, `elements/decisions/skill/decide_entry.md:11-13` dochodzi do miejsc zgrywanych w *To do* 4; bez tego agent piszący wpisy w cyklu dalej pytałby — przez zablokowany szkic PR-a — także tam, gdzie wynik daje to, co przyjął człowiek.
  - Not chosen:
    - instrukcja bez zmian — mówi co innego niż WAY-25, a agent, który się jej trzyma, zatrzymuje cykl, czyli problem, który zadanie usuwa, zostaje u agenta piszącego wpisy
  - Source: Mariusz, 2026-11-07, „dopiszmy”; `elements/decisions/skill/decide_entry.md:11-13` @ `52889bc`: „The search of the foundation also looks for a collision with another decision, which is a question in step 4 (WAY-25)”.
- Pytanie 5: czy WAY-25 dostaje przykład naruszenia dla ścieżki, na której cykl sam zapisuje pierwszeństwo?
  - Answer: tak (*To do* 2); recenzent zmiany dostaje gotowy test na ryzyko, że agent uzna za wynik coś, czego przyjęte fragmenty nie dają, albo zapisze pierwszeństwo bez cytatu w PR-ze.
  - Not chosen:
    - zmiana samego przykładu zgodnego — recenzent wyprowadza ten test sam ze zdania wiążącego i może przepuścić pierwszeństwo bez cytatu albo oparte na fragmencie, który wyniku nie daje; Mariusz widzi je dopiero w PR-ze
  - Source: Mariusz, 2026-11-07, „dopiszmy”.

## Context

- Źródło: sprawy AIR-571 i AIR-573 z przeglądu warstwy AI, 2026-11-02, w `the ledger of the review of the AI layer in the author's notes`, z cytatami z PR #66 (`logging-guidelines`) i PR #63 (`unsettled-technology-returns`); po 14 dniach od zamknięcia przechodzą do `the archive of that ledger` w tym samym katalogu.
- Przypadek, od którego zaczęła się sprawa, mieści się w brzmieniu *To do* 1: WAY-275 każe linii logu nieść identyfikatory z listy, WAY-276 trzyma sekrety z dala od logu, a wiersz zadania `logging-guidelines` mówi, że sekretów w logu nie ma, a wyjątek dotyczy tylko zakazu danych osobowych, więc identyfikator będący sekretem zostaje poza logiem.
- Tak już to działa w praktyce: autor wpisów w `unsettled-technology-returns` wpisał w raporcie „The human strikes one clause and one link at the merge”, a gdzie indziej odmówił dopisania `narrows`, bo ani zadanie, ani spec tego nie mówiły.
- Warunek „the change may write the decision that prevails” jest potrzebny, bo cykl w produkcie nie może zapisać pierwszeństwa w decyzjach the-way, które leżą poza jego repozytorium; wtedy agent dalej staje i pyta.
- To zmiana sensu zaakceptowanej decyzji, więc Mariusz ma ją zobaczyć przy scaleniu.
- Zadanie powstało przy stanie `f45ca40`; od tego czasu wszystkie miejsca z *To do* przesunęły się bez zmiany treści (WAY-25 z 617-619 na 639-641, szablon decyzji ze 164-165 na 168-169, `agent-instructions/README.md` z 32-34 na 32-35, krok fundamentu z 24-25 na 26-27, przykład WAY-134 z 3233-3235 na 3345-3347).
- Na WAY-25 powołują się też uzasadnienia WAY-32, WAY-172, WAY-268 i WAY-293 (`foundations/decisions.md:838`, `:4962`, `:7973`, `:8973` @ `52889bc`); mówią, po co zapisano tam pierwszeństwo, i nowe brzmienie ich nie przeczy — sprawdzi je przeszukanie całego fundamentu w cyklu (WAY-33).
- Spec cyklu nie jest czymś, co przyjął człowiek: przegląda go agent, nie Mariusz (WAY-135), więc wynik zapisany tylko w specu nie pozwala cyklowi zapisać pierwszeństwa.
- Sprawy AIR-571 i AIR-573 to dwa niezależne wyniki; Mariusz połączył je świadomie w jedno zadanie (wpis AIR-573, 2026-11-02).

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-25 — „Where two decisions both apply and collide, the one that prevails names the other in *Relations* as `narrows`, and its binding sentences state the area where it prevails; nothing follows along a chain, and two decisions that narrow each other are an error. A collision between two decisions with no precedence recorded is never settled by the agent that meets it; a human records the precedence in the decision that prevails.” (`foundations/decisions.md:635-659` @ `52889bc`) — zadanie zmienia drugie zdanie, oba przykłady, uzasadnienie i odrzucone warianty.
- WAY-30 — „A change to a decision that a task needs is written into the task's plan, or into its task document where no plan is written, and approved with that plan or document by the human who accepts decisions (WAY-14) before the code that needs it is made; that approval, including a change carried by a row of *Settlements to record*, answers the question WAY-114 requires, so the agent writing the entry asks only about a meaning beyond what the approved plan or task document carries, and in this area this decision prevails over WAY-114. When a contradiction shows only during implementation, the agent stops, quotes the decision by its number, and either brings the change into line, drops the change, or proposes on the task branch an edit of the decision, a new wording or a narrowing, and the code that needs it waits for that human. […]” — zapisanie pierwszeństwa zmienia sens decyzji, która wygrywa; nowe zdanie WAY-25 mieści się w WAY-30 tylko wtedy, gdy wynik daje to, co człowiek przyjął.
- WAY-114 — „A human accepts the meaning of a foundation entry while its wording is the agent's: […] and that of every other entry at the merge of the change that holds it, where the section of the request's description for the human's decisions gives one plain sentence of its meaning with no identifier […]. Before that, a question goes to the human only where the agent has no recommendation or the entry would change the meaning of an approved decision; a translation never enters the foundation.” — droga, którą pierwszeństwo zapisane przez cykl trafia do Mariusza.
- WAY-134 — „[…] gives a decision written from a row as its rejected options only the ways not chosen that the row's source keeps, `none considered` where the human said so, or `unknown` […]” — zadanie zmienia jej przykład zgodny, nie zdanie wiążące.

## Settlements to record

Candidates: 2 shown, 0 accepted — 2026-11-07

none

## Out of scope

- Czy zderzenie o stan i tak zakazany przez reguły w ogóle wymaga wpisu: przeglądy `logging-guidelines` odpowiedziały „tak” i to zostaje.
- Krok powrotu, czyli końcowe porównanie wpisów z kodem, i jego stosunek do drobnych uwag przeglądu: zdanie, że poprawia on rozjazd także wtedy, gdy przegląd nazwał go drobną uwagą, to niemal dosłownie zdanie odrzucone przy AIR-542, a od tamtej pory nie ma nowych danych.

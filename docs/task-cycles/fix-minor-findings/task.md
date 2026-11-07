---
title: "the way: drobne uwagi przeglądu poprawiane w tym samym PR-ze, nie tylko odkładane na zadania"
status: draft
created: 2026-11-06T22:25
updated: 2026-11-06
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# the way: drobne uwagi przeglądu poprawiane w tym samym PR-ze, nie tylko odkładane na zadania

Status: ready for cycle
Project relation: independent

## Description

### Need

- Gdy cykl zadania the way kończy się PR-em, uwagi przeglądu z oceną Minor i uwagi, które recenzent oznaczył jako wychodzące poza zadanie, zostają niepoprawione (WAY-161).
- Te z nich, które odczuje użytkownik produktu albo człowiek pracujący z procesem, opis PR-a stawia przed Mariuszem z jednym pytaniem, „Make a task of it?” (WAY-289; pozycja 8 sekcji „For you to decide” w `task-cycle/skill/request_template.md:184-189`); odpowiedzi „popraw to w tym PR-ze” pytanie nie przewiduje.
- W PR #77 Mariusz dwa razy odpowiedział wbrew pytaniu: „a ja bym to jeszcze dociągnął w ramach tego”, a potem „nie lubię dodatkowych drobnych zadań / drobne rzeczy powinny być robione przy okazji, żeby potem nie zostawały na dodatkowe zadania i dodatkowe sesje / dociągnij e drobne luki w teście i przy okazji można też te M3 i M4 dorzucić” (Mariusz, 2026-11-06, zacytowane w `reports/11-remarks-1.md` i `reports/21-remarks-2.md` zapisu cyklu).
- Każda z tych odpowiedzi uruchomiła pełną korektę; pierwsza (autor, przegląd, poprawka po przeglądzie, krok zwrotny, testy, nowy zapis i opis) zajęła ok. 32 min i 25 mln tokenów z 1:22:29 i 56,3 mln tokenów całego cyklu (etapy 12–23 w `stages.md` zapisu cyklu); druga zakończyła się przed scaleniem PR-a 2026-11-06.
- Odczuwa to Mariusz, któremu drobiazgi albo zostają w kodzie, albo kosztują turę rozmowy i rundę korekty, albo stają się osobnymi zadaniami, których nie chce; i orkiestrator cyklu, który nie ma reguły na „popraw w tym PR-ze” i wywodzi ją sam.

### To do

1. Cykl poprawia uwagi Minor z przeglądu całej zmiany, których recenzent nie oznaczył jako wykraczających poza zadanie, przed otwarciem PR-a: w poprawce po uwadze blokującej, a bez niej w jednej poprawce tylko dla nich, z jednym przeglądem (pytanie 1).
2. Gdy przegląd poprawki uruchomionej tylko dla uwag Minor znajdzie w niej nową uwagę Critical albo Important, cykl cofa commity tej poprawki i otwiera PR na kodzie przyjętym przez przegląd całej zmiany; poprawiane uwagi Minor i uwaga z przeglądu poprawki trafiają do opisu PR-a (pytanie 2).
3. Pozycja 8 sekcji „For you to decide” szablonu opisu PR-a (`task-cycle/skill/request_template.md:184-189`) stawia każdą niepoprawioną uwagę, którą ktoś odczuje, z pytaniem o dwóch odpowiedziach — „poprawić w tym PR-ze” albo „zrobić zadanie” — na które jedna odpowiedź może objąć całą listę; po korekcie wykonanej na takie „poprawić” pozostałe uwagi dostają już tylko pytanie o zadanie (pytanie 3).

### Questions to settle

- Pytanie 1: kiedy drobne uwagi w zakresie zadania są poprawiane — dopiero na odpowiedź Mariusza w PR-ze, czy przez sam cykl, zanim PR się otworzy?
  - Answer: B. Cykl sam poprawia wszystkie uwagi Minor z przeglądu całej zmiany, których recenzent nie oznaczył jako wykraczających poza zadanie — także te, których według WAY-289 nikt nie odczuje: wchodzą do poprawki, która i tak biegnie przy uwadze blokującej, a gdy uwagi blokującej nie ma, biegnie jedna poprawka tylko dla nich z jednym przeglądem. To zmienia WAY-161, którego *Verification* liczy dziś „a fix runs for Minor findings alone” jako naruszenie; odpowiedź jest zgodą Mariusza na tę zmianę.
  - Not chosen:
    - A. Cykl zostawia drobne uwagi, a pytanie w PR-ze dostaje odpowiedzi „poprawić w tym PR-ze” albo „zrobić zadanie” — każdy PR z poprawkami kosztuje turę rozmowy i korektę (w PR #77 ok. 32 min i 25 mln tokenów), a uwagi, których nikt nie odczuje (jak M4), nie trafiają do pytania.
    - C. Drobne uwagi wchodzą do poprawki tylko wtedy, gdy ta i tak biegnie, a bez uwagi blokującej PR pyta jak w A — w takich cyklach koszt jak A i dwa zachowania cyklu zależne od wyniku przeglądu.
    - D. Zostawić jak jest — dziś nic nie kosztuje, ale każdy kolejny PR z drobiazgami przechodzi jak PR #77.
  - Source: Mariusz, 2026-11-06: „B”, na pytanie „Które wybierasz: A, B, C czy D?”, przy wariancie B, którego słabość nazwano: WAY-161 ostrzega, że runda dla samych drobiazgów idzie na szlifowanie, a nowa poważna uwaga w takiej poprawce może zablokować PR, który bez niej byłby gotowy.
- Pytanie 2: co robi cykl, gdy przegląd poprawki uruchomionej tylko dla uwag Minor znajdzie w niej nową uwagę Critical albo Important?
  - Answer: b) Cykl wycofuje tę poprawkę — cofa jej commity na gałęzi, więc zostają w historii — i otwiera PR na kodzie, który przyjął przegląd całej zmiany; poprawiane uwagi Minor i uwaga znaleziona w poprawce trafiają do opisu PR-a. Trzeciej rundy nie ma. Poprawka, do której uwagi Minor tylko dołożono, bo i tak biegła po uwadze blokującej, kończy się jak dziś według WAY-162. Mariusz w takim przypadku najpewniej zrobi z tego zadanie.
  - Not chosen:
    - a) Jak dziś według WAY-162: PR zablokowany — polerowanie zamienia PR, który bez poprawki byłby gotowy, w zablokowany, a decyzja i tura rozmowy spadają na Mariusza.
    - c) Cykl zostawia część poprawki, którą przegląd przyjął, a resztę cofa — o tym, co zostaje, rozstrzyga orkiestrator, któremu WAY-161 tego zabrania.
  - Source: Mariusz, 2026-11-06: „zdecydowanie b i w takim przypadku zrobię sobie już zadanie pewnie z tego”, na pytanie „Który wariant wybierasz: a, b czy c?”, przy wariancie b, którego słabość nazwano: praca poprawki przepada, a w opisie PR-a stoją drobiazgi niepoprawione mimo wariantu B.
- Pytanie 3: co opis PR-a robi z uwagami, których cykl nie poprawił — spoza zakresu zadania, Minor z przeglądów późniejszych niż przegląd całej zmiany i Minor z poprawki wycofanej według pytania 2?
  - Answer: b) Każdą z nich, którą odczuje użytkownik produktu albo człowiek pracujący z procesem, sekcja decyzji PR-a stawia z pytaniem o dwóch odpowiedziach: „poprawić w tym PR-ze” albo „zrobić zadanie”, a jedna odpowiedź może objąć całą listę. „Poprawić” uruchamia korektę po uwagach człowieka (`task-cycle/skill/correction.md`) z jedną poprawką i jednym przeglądem; uwagi, których po niej nie poprawiono, PR stawia już tylko z pytaniem o zadanie albo zostawia w dolnej części, więc po jednej korekcie pętla się kończy. Uwagi, których nikt nie odczuje, zostają w dolnej części jak dziś.
  - Not chosen:
    - a) Jak dziś, samo „zrobić z tego zadanie?” — gdy Mariusz chce poprawki od razu, odpowiada wbrew pytaniu, jak dwa razy w PR #77, a orkiestrator nie ma na to reguły.
    - c) Jak b), ale w pytaniu także uwagi, których nikt nie odczuje — sekcja decyzji puchnie od kosmetyki, choć jej „none” ma znaczyć „nic nie czeka na tak” (WAY-287), a kosmetykę w zakresie zadania cykl i tak poprawia według pytania 1.
  - Source: Mariusz, 2026-11-06: „b”, na pytanie „Który wariant wybierasz: a, b czy c?”, przy wariancie b, którego słabość nazwano: korekta przynosi własne uwagi Minor, które bez trzeciej rundy (WAY-162) wracają do PR-a już tylko z pytaniem o zadanie albo do dolnej części.

## Context

- Zapis cyklu, w którym sprawa wyszła (PR #77, https://github.com/mariusznazar/the-way/pull/77): w commicie https://github.com/mariusznazar/the-way/tree/fa9a030/docs/task-cycles/part-boundaries-test, po korekcie 2.
- Uwaga o procesie orkiestratora tego cyklu (`cycle.md`, ostatnia pozycja „Process remarks on the-way”): „the-way leaves every Minor finding unfixed and asks the human "Make a task of it?" for each one the user or the human will feel […]; Mariusz answered twice in this cycle that small findings are to be made in the same change, not left for separate tasks and sessions […], which cost two corrections, each with its own review and fix round.”
- Dla porównania: poprawka 1 w tym cyklu, robiona w trakcie cyklu po przeglądzie całej zmiany (autor, przegląd poprawki), zajęła ok. 5 min i 5,1 mln tokenów (etapy 6–9 w `stages.md`).
- W M4, o którego poprawkę Mariusz poprosił, chodzi o zawijanie wierszy w dwóch plikach Markdown — uwagę, której według WAY-289 nikt nie odczuwa, więc opis PR-a nie stawia jej przed człowiekiem.
- PR-y #72–#76 (scalone 2026-11-05 i 2026-11-06) zadawały pytanie „Make a task of it?” osiem razy; ani opisy, ani komentarze tych PR-ów nie zapisują odpowiedzi, więc PR #77 jest jedynym cyklem, w którym odpowiedź Mariusza na to pytanie jest zapisana.
- Korekta po uwagach człowieka już istnieje: `C:\Storage\repos\the-way\task-cycle\skill\correction.md` — uwagi wiążą, autor poprawia z `make-change`, przegląd z `review-change` kończy się jak każdy przegląd (jedna poprawka i jeden przegląd poprawki, WAY-162), potem krok zwrotny, testy, nowy zapis i nowy opis.
- Kod poprawek w cyklu: „The end of a code review” w `C:\Storage\repos\the-way\task-cycle\skill\SKILL.md:358-384` (Minor i spoza zakresu nie są poprawiane, `FAIL` dostaje jedną poprawkę i jeden przegląd).

## Questions carried to cycle

- Czy `task-cycle/skill/correction.md` potrzebuje zdania o odpowiedzi „poprawić w tym PR-ze”, czy obejmuje ją dzisiejsze „The remarks bind”, z uwagami przeglądu wskazanymi w odpowiedzi jako uwagami człowieka.
- Kto robi poprawkę uruchomioną tylko dla uwag Minor i na jakiej klasie modelu — „The end of a code review” (`task-cycle/skill/SKILL.md:372-381`) mówi to dziś tylko o poprawce po `FAIL`.

## Human actions

none

## Decisions in play

- WAY-161: „In the review of the whole change on either route, a finding blocks when the reviewer grades it Critical or Important and has not itself marked it as outside the task's scope, and a review that leaves no blocking finding sends the change to its request without a fix. A finding the reviewer has marked as outside the task's scope […] is not fixed, whatever its grade, nor is a Minor finding, and the request lists those findings in an item of their own and the Minor findings in another, each with the reviewer's words and its place in the code, while the human decides which findings outside the scope become new tasks and creates them. The orchestrator moves no finding from one of these kinds to another.” — w *Verification* jako naruszenie: „a fix runs for Minor findings alone; the fix after the whole-change review of a planned change takes in the Minor findings of its slice reviews”; w *Rationale*: „A minor finding fixed in a round of its own spends that round on polish”.
- WAY-162: „In every code review of a task's cycle […] the findings that block, as WAY-161 grades them, get one fix and one review of that fix, and a new Critical or Important finding in the fix itself counts as one that remains. Where a blocking finding remains after that review of the fix, no third round runs, […] and the cycle opens a draft request marked `blocked` […]. In the code reviews after the review of the whole change, the findings that do not block go unfixed to the request's lists as WAY-161 gives them.”
- WAY-163: „Before the cycle opens a request that a remaining blocking finding blocks (WAY-162), it runs the product's gate on the change and writes its cycle record with its record of stages, while it makes no further slice and runs neither the reconciliation with the target branch nor the return step on code its review has not accepted […].”
- WAY-287: „The section of a request's description for the human's decisions holds everything whose merge needs the human's yes — […] the unfixed findings the product's user or the human working with the process will feel, […] — and its `none` says that nothing else in the request waits for the human's yes.”
- WAY-289: „Writing a request's description, the orchestrator of the cycle judges each Minor finding and each finding outside the task's scope, […] by whether the product's user or the human working with the process will feel it, and restates each that will be felt, in plain words, in the section for the human's decisions as a question whether it becomes a task. Every finding stays in its list of the lower part with the reviewer's words and its place in the code, and the judgment changes no finding's kind or grade and decides no fix and no block.”

## Settlements to record

Candidates: 4 shown, 3 accepted — 2026-11-06

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Cykl sam poprawia przed otwarciem PR-a wszystkie uwagi Minor z przeglądu całej zmiany, których recenzent nie oznaczył jako wykraczających poza zadanie, także te, których nikt nie odczuje — w poprawce, która i tak biegnie po uwadze blokującej, a bez niej w jednej poprawce tylko dla nich z jednym przeglądem; WAY-161 przestaje liczyć poprawkę dla samych uwag Minor jako naruszenie. | decision | pytanie 1 (B) pod *Questions to settle*, z jego *Not chosen* | czy zmienić WAY-161 w miejscu, czy pisać nową decyzję; czy poprawiać tylko uwagi odczuwalne; co trafia do *Rejected* (pytanie w PR-ze, hybryda, bez zmiany) |
| 2 | Gdy przegląd poprawki uruchomionej tylko dla uwag Minor znajdzie w niej nową uwagę Critical albo Important, cykl cofa commity tej poprawki i otwiera PR na kodzie, który przyjął przegląd całej zmiany, bez trzeciej rundy; poprawka, do której uwagi Minor tylko dołożono, kończy się jak dziś według WAY-162. | decision | pytanie 2 (b) pod *Questions to settle*, z jego *Not chosen* | czy taki PR jest zablokowany według dzisiejszego WAY-162, czy cykl zostawia przyjętą część poprawki |
| 3 | Niepoprawioną uwagę, którą odczuje użytkownik produktu albo człowiek pracujący z procesem, sekcja decyzji PR-a stawia z pytaniem o dwóch odpowiedziach — „poprawić w tym PR-ze” albo „zrobić zadanie” — na które jedna odpowiedź może objąć całą listę; „poprawić” uruchamia korektę po uwagach człowieka z jedną poprawką i jednym przeglądem, a po niej pozostałe uwagi dostają już tylko pytanie o zadanie. | decision | pytanie 3 (b) pod *Questions to settle*, z jego *Not chosen* | brzmienie pytania w WAY-289 i w szablonie; czy po korekcie znów pytać „poprawić czy zadanie?”; czy kosmetyka trafia do sekcji decyzji |

## Out of scope

none

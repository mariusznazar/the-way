---
title: "the way: skrócić 12 zapisanych decyzji, które stoją ponad nowy limit długości"
status: draft
created: 2026-11-20T11:17
updated: 2026-11-20
tags: [zadanie]
related: "the note of the project of the process work, in the author's notes"
---

# the way: skrócić 12 zapisanych decyzji, które stoją ponad nowy limit długości

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Dwanaście zapisanych decyzji the way ma akapit zdań wiążących dłuższy, niż pozwala limit ustalony 2026-11-20: najwyżej 3 zdania i najwyżej 300 słów w akapicie.
- Po scaleniu zadania „the way: przywrócić skrypt pilnujący długości zapisanych decyzji” sprawdzenie fundamentu zatrzymuje każdą zmianę, która rusza słowo albo podział na akapity w takiej decyzji, dopóki ta decyzja nie zmieści się w limicie.
- Odczuwa to agent, który zmienia jedną z tych decyzji z innego powodu i musi przy okazji przebudować cały wpis; Mariusz w przeglądzie, bo dostaje przebudowaną decyzję w zmianie, która miała dotyczyć czegoś innego.
- Bez zmiany przebudowy przychodzą pojedynczo, jako dokładki do cudzych zmian; najwcześniej trafi to WAY-344, którą w listopadzie 2026 zmieniały trzy zmiany w dwa dni.

### To do

1. W każdym z dziesięciu wpisów z tabeli „Podział na akapity” pod „Decisions in play” pierwszy akapit zdań wiążących dzieli się pustą linią przed zdaniem, które tabela podaje; słowa i kolejność zdań zostają.
2. W WAY-150 zdanie, które kończy się „the decisions the first paragraph names being opened whole as it gives”, wskazuje po zmianie akapit, w którym stoi reguła o otwieraniu decyzji w całości — po podziale drugi; to jedyne słowo, które zmienia się w zdaniach wiążących tych dziesięciu wpisów.
3. WAY-344 dzieli się na dwie decyzje, tak jak podaje „Decisions in play”: reguła ogólna zostaje pod numerem WAY-344, a wszystko, co mówi o komendzie liczącej audyt, przechodzi do nowej decyzji z następnym wolnym numerem; drugie zdanie WAY-344 dalej wyłącza tę komendę spod reguły ogólnej i nazywa nową decyzję numerem; każdy akapit zdań wiążących obu decyzji mieści się w limicie.
4. Przeniesione zdania WAY-344 zachowują brzmienie; słowa zmieniają się tylko tam, gdzie wymaga tego rozcięcie jej drugiego zdania, nazwanie w nim nowej decyzji numerem i podanie w nowej decyzji obszaru, w którym ma ona pierwszeństwo przed WAY-344.
5. Pola, uzasadnienie (*Rationale*) i odrzucone warianty (*Rejected*) WAY-344 dzielą się między dwie decyzje razem ze zdaniami, których dotyczą: każda klauzula *Verification*, każde zdanie uzasadnienia i każdy odrzucony wariant stoi po zmianie w tej decyzji, w której stoi zdanie, którego dotyczy, i żadne nie znika ani nie stoi w obu; zdanie uzasadnienia, które dotyczy obu stron, zostaje rozcięte na granicy klauzul, a każda część zachowuje brzmienie.
6. W WAY-287 pierwsze zdanie zostaje rozcięte na dwa w miejscu „— in three groups, headed”: pierwsze wylicza, co sekcja zawiera, drugie mówi o trzech grupach; wyliczenie zostaje w decyzji w całości, a akapity układają się tak, jak podaje „Decisions in play”.
7. Każda linia `decision:` testu podaje po zmianie numer decyzji i początek zdania, które stoi w tej decyzji.
8. Każde odwołanie do WAY-344 w kodzie, testach, skillach, wytycznych i innych wpisach fundamentu, które dotyczy zdania przeniesionego do nowej decyzji, wskazuje po zmianie nową decyzję.
9. Opis requestu pokazuje w dolnej części, przy liście wpisów fundamentu, w całości stare i nowe brzmienie zdań wiążących WAY-344, nowej decyzji, WAY-287 i WAY-19 oraz to, które zdania uzasadnienia i które odrzucone warianty WAY-344 trafiły do której z dwóch decyzji.
10. Zdanie wiążące WAY-19, które dziś mówi „a part of the question an existing entry answers is a sentence of that entry where it cannot change without changing that entry”, nazywa po zmianie część pytania tak samo jak WAY-05 scalona requestem #152 — rozróżnia część innego pytania i część własnego pytania wpisu — i nie przeczy WAY-05 co do akapitu takiej części; to, co WAY-19 wiąże (część, która nie może zmienić się bez zmiany wpisu, stoi w tym wpisie, a nie pod własnym numerem), zostaje. Źródło: PR #152, „Fix or let through” 1(a) i „Findings outside the task's scope” 1.
11. Pole *Scope* WAY-391 wymienia po zmianie te same części, co *Applies to* w `guidelines/coding-shared-module.md` (po #152: `relation-model · process-audit · task-cycle · elements-common`), tak jak *Scope* decyzji WAY-386–WAY-390 pokrywa się z *Applies to* wytycznych swojego rodzaju; zdania wiążące WAY-391 się nie zmieniają. Źródło: PR #152, „Fix or let through” 1(c) i „Findings outside the task's scope” 3.
12. W `agent-instructions/README.md`, w akapicie pod „The form of the foundation”, słowa „for this report alone” stają się „for these two reports alone”, bo stoją po dwóch raportach (akapitu ponad limit i wpisu ponad 600 słów). Źródło: PR #152, „Fix or let through” 1(d) i „Minor findings” 1.
13. We wzorze wpisu w `elements/decisions/template.md`, sekcja „Decision entry”, słowa „all the binding sentences together at most 600 words” wychodzą z bloku, który otwiera „optionally”, i stoją osobno po blokach akapitów zdań wiążących, tak żeby czytelnik samego wzoru brał limit za limit całego wpisu. Źródło: PR #152, „Fix or let through” 1(e) i „Minor findings” 2.

### Acceptance criteria

- `python -B elements/common/foundation_check.py` uruchomiony po zmianie nie zgłasza błędu i nie wypisuje żadnej linii `listed:` o długości zdań wiążących.
- Żaden z dwunastu wpisów ani nowa decyzja wydzielona z WAY-344 nie ma po zmianie łącznie ponad 600 słów zdań wiążących.
- Zdania wiążące każdego z dziesięciu wpisów z tabeli „Podział na akapity”, złączone w jeden tekst, są po zmianie słowo w słowo takie same jak przed nią, poza jednym słowem w WAY-150.

### Questions to settle

- Gdzie poprawić 12 wpisów the way, które już dziś stoją ponad limit?
  - Answer: osobnym zadaniem the way, zaraz po zadaniu ze skryptem — tym zadaniem; wpisy loop2 dostają własne zadanie w loop2.
  - Not chosen:
    - w zadaniu ze skryptem — jeden request miesza skrypt z przepisaniem zdań wiążących 12 zatwierdzonych decyzji, spór o jedno brzmienie blokuje całość, a pytania o podział wpisów takich jak WAY-344 weszłyby do tamtego doprecyzowania
    - wcale, każdy wpis poprawia ten, kto go dotknie — to dolegliwość, od której zadanie ze skryptem się zaczęło, tylko wymuszona przez skrypt
  - Source: Mariusz, 2026-11-20, „2. ok b, ale to od razu jak skończymy doprecyzowanie tego zadania to parkujemy dwa zadania, jedno dla the way, drugie dla loop2” — odpowiedź z dokumentu zadania `Notes/Projects/(P) Proces pracy nad produktem/_zadania/zadanie_straznik_dlugosci_decyzji.md`
- Czym doprowadzić wpisy do limitu: podziałem na akapity bez zmiany słów, przepisaniem zdań krócej czy rozbiciem wpisu na kilka decyzji?
  - Answer: podziałem na akapity bez zmiany słów w dziesięciu wpisach, w miejscach z tabeli „Podział na akapity”, z poprawką odwołania „the first paragraph” w WAY-150; WAY-344 i WAY-287 mają własne pytania.
  - Not chosen:
    - przepisać zdania krócej we wszystkich 12 — 12 nowych brzmień zatwierdzonych decyzji do przeczytania słowo po słowie, z ryzykiem, że przy skracaniu zmieni się to, co decyzja wiąże; ok. 100 cytatów początków zdań w testach do poprawienia; powrót do starego brzmienia to kolejna zmiana 12 decyzji
    - rozbić każdy długi wpis na kilka decyzji z nowymi numerami — kilkanaście nowych wpisów, podział uzasadnień i odrzuconych wariantów między nie, poprawki odwołań do numerów w kodzie i skillach; wycofany numer nie wraca
  - Source: doradca dnia w imieniu Mariusza, 2026-11-20, „1 a — podział na akapity bez zmiany słów dla dziesięciu wpisów, według Twojej tabeli (plus poprawka „the first paragraph” w WAY-150)”
- Czy osobny akapit zdań wiążących może nieść część pytania z nagłówka wpisu, czy tylko część innego pytania, jak dziś mówią szablon decyzji i WAY-05?
  - Answer: może — osobny akapit niesie także część własnego pytania wpisu, nie tylko część innego pytania; pięć podziałów z oceną „część pytania z nagłówka” zostaje. Zmianę reguły w WAY-05, szablonie decyzji i skrypcie robi request #152 zadania ze skryptem, nie to zadanie.
  - Not chosen:
    - dzielić bez zmiany reguły — reguła i wpisy mówiłyby co innego, recenzent mógłby słusznie odrzucić podział
    - takie wpisy naprawdę przebudować — nowe brzmienie każdej zatwierdzonej decyzji do czytania
  - Source: Mariusz, 2026-11-20, „a” — przekazał doradca dnia; zmiana zakresu requestu #152: https://github.com/mariusznazar/the-way/pull/152#issuecomment-7038691756
- Czy poza limitem akapitu wpis ma limit łączny, żeby podział na akapity nie był obejściem limitu?
  - Answer: tak — zdania wiążące jednego wpisu, wszystkie akapity razem, mają najwyżej 600 słów; liczy to ten sam skrypt na tych samych zasadach: błąd w decyzji dodanej albo zmienionej, pozostałe tylko wypisane. Także tę zmianę robi request #152.
  - Not chosen:
    - brak limitu łącznego — długości wpisu nie pilnuje wtedy nic, bo limit akapitu spełnia pusta linia
    - limit liczby akapitów — kilka akapitów po 300 słów to dalej bardzo długi wpis
  - Source: Mariusz, 2026-11-20, „b” — przekazał doradca dnia; zmiana zakresu requestu #152: https://github.com/mariusznazar/the-way/pull/152#issuecomment-7038691756
- Co zrobić z WAY-344 (8 zdań, 743 słowa w jednym akapicie, z czego ok. 430 słów to przypadki komendy liczącej audyt)?
  - Answer: dwie decyzje — reguła ogólna zostaje pod WAY-344, a wszystko o komendzie liczącej audyt przechodzi do nowej decyzji z własnym numerem; zmienia to WAY-344.
  - Not chosen:
    - sam podział na 5 akapitów bez zmiany słów (85 / 274 / 131 / 228 / 25) — wpis dalej zbiera przypadki komendy audytu, a dwa akapity stoją pod samym limitem (274 słowa; 228 słów i 3 zdania), więc następna zmiana, która dopisze przypadek, i tak musi wpis przebudować
    - osobna decyzja na każdy przypadek komendy audytu (4–5 nowych decyzji) — koszt podziału kilka razy większy, a przypadki nie zmieniają się na tyle niezależnie od siebie, żeby to uzasadnić
  - Source: doradca dnia w imieniu Mariusza, 2026-11-20, „2 a — WAY-344 na dwie decyzje: reguła ogólna zostaje pod WAY-344, wszystko o komendzie liczącej audyt przechodzi do nowej decyzji z własnym numerem. Powód: to ten wpis rośnie z każdą zmianą komendy audytu, a sam podział na akapity zostawia dwa akapity pod samym limitem.”
- Co zrobić z pierwszym zdaniem WAY-287, które samo ma 305 słów?
  - Answer: rozciąć je na dwa w miejscu „— in three groups, headed”; wyliczenie tego, co sekcja zawiera, zostaje w decyzji.
  - Not chosen:
    - wyjąć wyliczenie z decyzji do szablonu opisu requestu — wpis krótszy o ok. 200 słów, ale lista przestaje być częścią decyzji i rodzaj pozycji dałoby się dodać albo usunąć zmianą samego szablonu; to zmiana znaczenia WAY-287, której uzasadnienie nazywa tę listę bazą
  - Source: doradca dnia w imieniu Mariusza, 2026-11-20, „3 a — WAY-287: rozciąć pierwsze zdanie w miejscu „— in three groups, headed”; lista zostaje w decyzji.”
- Jeden request czy kilka?
  - Answer: jeden request z całością.
  - Not chosen:
    - dwa zadania i dwa requesty, osobno dziesięć wpisów z samym podziałem na akapity i osobno WAY-344 z WAY-287 — drugi pełny cykl z drugim przeglądem Mariusza, a wydzielenie prostych wpisów niczego nie przyspiesza tam, gdzie boli najpierw, bo najczęściej zmieniana jest WAY-344
  - Source: doradca dnia w imieniu Mariusza, 2026-11-20, „4 a — jeden request z całością.”
- Jaki *Scope* dostaje nowa decyzja o komendzie liczącej audyt?
  - Answer: `process-audit` i `task-cycle`, jak WAY-339 i WAY-405.
  - Not chosen:
    - samo `process-audit`, jak WAY-330 — autor zmiany formy raportu etapu albo zapisu cyklu nie zobaczy tej decyzji i dowie się o niej najwyżej z testów audytu
    - wszystkie części, jak WAY-344 — każdy agent dalej dostaje ok. 430 słów o jednej komendzie, czyli podział nic nie daje czytającym
  - Source: doradca dnia w imieniu Mariusza, 2026-11-20, „1 a — Scope nowej decyzji: process-audit i task-cycle, jak WAY-339 i WAY-405.”
- W której sekcji dziennika decyzji staje nowa decyzja?
  - Answer: w sekcji „Process audit”; zdania wiążące WAY-344, tam gdzie wyłączają komendę liczącą audyt spod reguły ogólnej, nazywają nową decyzję numerem, żeby czytający regułę w sekcji „Scripts and the gate” widział, gdzie stoi wyjątek.
  - Not chosen:
    - sekcja „Scripts and the gate”, obok WAY-344 — kto pracuje nad audytem i czyta sekcję „Process audit”, zobaczy tę decyzję tylko jako nagłówek
  - Source: doradca dnia w imieniu Mariusza, 2026-11-20, „2 a — sekcja „Process audit”. Warunek: zdania wiążące WAY-344, tam gdzie wyłączają komendę liczącą audyt spod reguły ogólnej, nazywają nową decyzję numerem — żeby czytający regułę w „Scripts and the gate” widział, gdzie stoi wyjątek.”
- Gdzie zostaje przykład naruszenia z *Verification* WAY-344, który wymienia i skrypty sprawdzające formę, i komendę liczącą audyt: „a script that is neither a check of form nor the count of the audit lists an absent field as an item with exit code 1”?
  - Answer: zostaje w WAY-344 bez zmiany słów.
  - Not chosen:
    - zostaje w WAY-344 skrócony do „a script that is not a check of form lists…” — przykład zaczyna nazywać naruszeniem to, co komenda audytu robi zgodnie z nową decyzją, więc agent porównujący zmianę z WAY-344 zgłosi fałszywe naruszenie
    - rozciąć na dwa przykłady, po jednym w każdej decyzji — nowa decyzja dostaje tekst przykładu, którego nikt nie zatwierdzał, a nie potrzebuje go, bo trzymają ją testy
  - Source: doradca dnia w imieniu Mariusza, 2026-11-20, „3 a — przykład naruszenia zostaje w WAY-344 bez zmiany słów.”
- Co opis requestu pokazuje z przepisanych decyzji?
  - Answer: w całości stare i nowe brzmienie zdań wiążących WAY-344, nowej decyzji i WAY-287 oraz podział uzasadnienia i odrzuconych wariantów; te trzy wpisy Mariusz czyta przed scaleniem, pozostałych, w których przybywa tylko pustych linii, nie musi.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-20, „dokument ma wymagać, żeby opis requestu pokazywał w całości stare i nowe brzmienie zdań wiążących WAY-344, nowej decyzji i WAY-287 oraz podział uzasadnienia i odrzuconych wariantów — te trzy wpisy Mariusz przeczyta przed scaleniem; reszty (same puste linie) nie musi”

## Context

- Limit i sposób liczenia pochodzą z dokumentu zadania ze skryptem, `Notes/Projects/(P) Proces pracy nad produktem/_zadania/zadanie_straznik_dlugosci_decyzji.md` (`Status: ready for cycle`, w cyklu, jeszcze niescalone): każdy akapit zdań wiążących — akapity między nagłówkiem wpisu a jego pierwszym polem — ma najwyżej 3 zdania i najwyżej 300 słów; zdanie zaczyna się na początku akapitu albo po kropce i spacji, a kropka wewnątrz cudzysłowu zdania nie kończy; słowo to ciąg znaków między odstępami.
- Mariusz dodał 2026-11-20 dwie zmiany reguły, które wchodzą do requestu #152 zadania ze skryptem jako zmiana zakresu (https://github.com/mariusznazar/the-way/pull/152#issuecomment-7038691756): osobny akapit może nieść także część własnego pytania wpisu, a zdania wiążące jednego wpisu, wszystkie akapity razem, mają najwyżej 600 słów, liczone tym samym skryptem na tych samych zasadach.
- Łącznie ponad 600 słów zdań wiążących ma dziś tylko WAY-344 (743); najbliżej limitu stoją WAY-150 (592; poprawka jednego słowa tej liczby nie zmienia), WAY-134 (583) i WAY-339 (488). Po podziale WAY-344 jej część ogólna ma ok. 330 słów, a nowa decyzja ok. 440.
- Po scaleniu tamtego zadania limit liczy `elements/common/foundation_check.py`: błąd dla decyzji, którą zmiana dodaje albo której zdania wiążące zmienia — także gdy zmienia tylko ich podział na akapity — i linia `listed:` dla pozostałych.
- Cykl tego zadania zaczyna się po scaleniu zadania ze skryptem; linia zadania nosi tę zależność, a listę wpisów ponad limit liczy wtedy scalony skrypt.
- Tamto zadanie zmienia WAY-05, która niesie limit; jej brzmienie po scaleniu jest brzmieniem obowiązującym dla tego zadania.
- Pomiar 2026-11-20 na `foundations` @ 1b6fe1c1, licznikiem zbudowanym z `binding()` i `begins_sentence()` z `elements/common/foundation_check.py`: 236 wpisów, 281 akapitów zdań wiążących, ponad limit 12 wpisów — te same i z tymi samymi liczbami, co w dokumencie zadania ze skryptem.

  | Wpis | Akapity (zdania, słowa) | Zdania pierwszego akapitu (słowa) |
  |---|---|---|
  | WAY-344 | 8 zd., 743 sł. | 85, 274, 65, 66, 58, 78, 92, 25 |
  | WAY-134 | 3 zd., 478 sł.; 2 zd., 105 sł. | 156, 81, 241 |
  | WAY-287 | 3 zd., 401 sł.; 1 zd., 27 sł. | 305, 46, 50 |
  | WAY-139 | 3 zd., 385 sł. | 72, 34, 279 |
  | WAY-154 | 3 zd., 379 sł. | 68, 237, 74 |
  | WAY-136 | 3 zd., 359 sł. | 87, 61, 211 |
  | WAY-405 | 5 zd., 343 sł. | 67, 56, 123, 65, 32 |
  | WAY-150 | 3 zd., 317 sł.; 1 zd., 44 sł.; 2 zd., 117 sł.; 1 zd., 114 sł. | 115, 169, 33 |
  | WAY-289 | 3 zd., 310 sł. | 128, 146, 36 |
  | WAY-339 | 3 zd., 308 sł.; 2 zd., 180 sł. | 79, 89, 140 |
  | WAY-148 | 3 zd., 304 sł. | 64, 128, 112 |
  | WAY-256 | 3 zd., 301 sł. | 90, 125, 86 |

- Tuż pod limitem słów stoi pięć akapitów innych wpisów: WAY-121 (277), WAY-213 (269), WAY-122 (261), WAY-44 (256), WAY-165 (252).
- Zdania trzech z 12 wpisów trzymają testy liniami `decision:`, które cytują początek zdania: WAY-344 w `agent-instructions/`, `elements/common/`, `process-audit/` i `task-cycle/`, WAY-339 i WAY-405 w `process-audit/test_audit_count.py`, `process-audit/test_record_items.py` i `task-cycle/test_cycle_stages.py`. Sam inny podział na akapity tych cytatów nie rusza; zmiana początku zdania albo przeniesienie zdania do innej decyzji — tak.
- Cytat „The rule binds a script that a change adds and, in a script” stoi dziś także przy testach zachowania komendy liczącej audyt w `process-audit/test_audit_count.py`; po podziale WAY-344 te testy trzymają zdanie nowej decyzji.
- Poza testami do WAY-344 odwołują się m.in. `guidelines/coding.md`, `guidelines/coding-generator.md`, `guidelines/coding-measuring-report.md`, `elements/invariants/template.md`, `process-audit/SKILL.md`, `process-audit/problem_register.md` oraz komentarze w `process-audit/audit_count.py`, `process-audit/record_reading.py`, `process-audit/problem_register.py` i `elements/common/foundation_check.py`.
- W WAY-287 część pierwszego zdania do „— in three groups, headed” ma 219 słów, a część od tego miejsca 86 słów.
- W WAY-344 zdania i części zdań, które zostają, mają razem ok. 320 słów, a te, które przechodzą do nowej decyzji, ok. 430 słów.
- Ocena w kolumnie „Nowy akapit to” tabeli „Podział na akapity” jest oceną agenta, który doprecyzowywał zadanie, nie ustaleniem Mariusza; po odpowiedzi Mariusza oba rodzaje akapitu są dozwolone.
- Reguły, od których zależy, jak wpis wolno zmienić, stoją w `elements/decisions/template.md`, sekcje „Binding sentences” i „Changing a decision”.
- Punkty 10–13 „To do” to cztery z pięciu drobnych uwag z przeglądów korekt requestu #152 (https://github.com/mariusznazar/the-way/pull/152, „Fix or let through”, pozycja 1); Mariusz 2026-11-20 wybrał „a”: bez osobnego zadania, dopisać je do tego zadania, bo rusza ten sam plik decyzji i szablon. Piątą uwagę, (b) — WAY-150 wskazuje swój pierwszy akapit po położeniu — załatwia już punkt 2.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

Pełne brzmienie dwunastu zmienianych wpisów stoi w `foundations/decisions.md` @ 1b6fe1c1; niżej każdy z nich jest nazwany pytaniem z nagłówka i zmianą, a miejsce zmiany — cytatem.

**Podział na akapity** — dziesięć wpisów, zmieniane: pierwszy akapit zdań wiążących dzieli się pustą linią przed podanym zdaniem, bez zmiany słów.

| Wpis | Pytanie wpisu | Nowy akapit zaczyna się od zdania | Słowa po zmianie | Nowy akapit to |
|---|---|---|---|---|
| WAY-256 | Where does a fragment of a skill stand? | „A fragment that some steps of the skill need, not all, stands by what it is” | 215 + 86 | część pytania z nagłówka |
| WAY-148 | How do task-cycle stages pass their work to the orchestrator? | „The orchestrator records the event and relevant choices” | 192 + 112 | część innego pytania: co orkiestrator czyta i zapisuje, gdy dostaje pracę etapu |
| WAY-339 | When do the measures of the audit stop being comparable? | „The audit compares each measure only within a series of its own kind” | 168 + 140 | część innego pytania: jak audyt porównuje miary i co podaje dla cyklu, który zmienił narzędzie pomiaru |
| WAY-289 | Which things the cycle left unfixed or undone does a request put before the human for a decision? | „The answer to fix it runs a correction” | 128 + 182 | część innego pytania: co uruchamia odpowiedź „napraw”; ostatnie zdanie akapitu wraca do pytania z nagłówka |
| WAY-150 | How do the-way skills choose which product foundation material to read? | „Of the decisions it finds by *Scope*” | 115 + 202 | część pytania z nagłówka |
| WAY-405 | How does the audit of the process read the reason of a discarded attempt? | „Where the lines under the item are not sub-items at one indent alone” | 123 + 220 | część pytania z nagłówka |
| WAY-136 | When does a task's change need a plan, and who makes and reviews it? | „A one-author change is reviewed by an agent that did not make it” | 148 + 211 | część pytania z nagłówka |
| WAY-154 | How do agents exchange a project task refinement and keep its result? | „Only a refiner changes the task document's body” oraz „Agent turns, questions and explicit waits” | 68 + 237 + 74 | części innych pytań: kto co zapisuje; jaki stan ma zadanie |
| WAY-139 | What does the-way hold for the skill that deploys a product, and which step checks that a product has one? | „When a task's outcome deploys the product” | 106 + 279 | część pytania z nagłówka |
| WAY-134 | How does a task carry what its refinement settles for the foundation? | „The task's cycle writes each kept row whole” | 237 + 241 | część innego pytania: jak cykl zapisuje to, co zadanie niesie |

- **WAY-344 — What does a script of the-way do when a file it reads lacks a field it needs?** — zmieniana: dzieli się na dwie decyzje.
  - Pod WAY-344 zostają: zdanie „A script of the-way that reads a file an agent or a human writes checks that the file holds each field the script needs”; zdanie „The rule binds a script that a change adds” do słów „reports a missing field whose presence it checks as a finding of its list, with exit code 1”, po których zdanie dalej wyłącza komendę liczącą audyt i nazywa nową decyzję numerem; zdanie „Where a script whose purpose is to check the form of a file reads a copy of the file”; zdanie „Each reading of a file that the rule covers has one test”.
  - Do nowej decyzji przechodzą: reszta drugiego zdania od „and except that the command that counts the audit” do jego końca; zdanie „The command that counts the audit, where a table of weights”; zdanie „Where a stage report has neither of the two columns of the cache writes”; zdanie „Where the command that counts the audit reads a cycle's record that lacks a line or an item”; zdanie „Where the locations file has no key `repository` under `the-way`”.
  - Nowa decyzja odpowiada na pytanie, co robi komenda licząca audyt, gdy plik, który czyta, nie ma pola, którego potrzebuje; nazywa WAY-344 w *Relations* jako `narrows` i podaje w zdaniach wiążących obszar, w którym ma pierwszeństwo: komendę liczącą audyt w przypadkach, które wymieniają przeniesione zdania; poza tymi przypadkami komendę dalej wiąże reguła ogólna WAY-344. W zdaniach wiążących WAY-344 zostaje o tej komendzie tylko to wyłączenie z numerem nowej decyzji.
  - *Scope* nowej decyzji: `process-audit`, `task-cycle`; staje na końcu sekcji „Process audit”.
  - Przykład naruszenia „a script that is neither a check of form nor the count of the audit lists an absent field as an item with exit code 1” zostaje w *Verification* WAY-344 bez zmiany słów.
  - *Rejected* nowej decyzji dostaje, obok wariantów przeniesionych z WAY-344, dwa warianty odrzucone spod pytania „Co zrobić z WAY-344”.
- **WAY-287 — What does a request put before the human for a decision?** — zmieniana: pierwsze zdanie, które otwiera „The section of a request's description for the human's decisions holds everything whose merge needs the human's yes”, zostaje rozcięte w miejscu „— in three groups, headed”; po zmianie pierwszy akapit to zdanie z wyliczeniem (ok. 219 słów), drugi to zdanie o trzech grupach ze zdaniami „Every group stands” i „A blocked request keeps the same skeleton” (ok. 182 słowa), trzeci to dzisiejszy drugi akapit „Another decision may add a kind of item” (27 słów). Zmieniają się tylko słowa na styku rozciętego zdania.
- **WAY-05 — How is a decision entry written?** — bez zmian w tym zadaniu; niesie regułę akapitów, a limit słów akapitu, limit 600 słów wpisu i akapit na część własnego pytania wpisu dopisuje jej request #152 zadania ze skryptem. Cykl czyta jej brzmienie przy podjęciu z gałęzi `foundations`, po scaleniu #152, na które to zadanie czeka; brzmienie sprzed #152: „A decision entry opens with one to three binding sentences that answer its question — in the present tense, describing a state that is to be true, concrete enough to check — and one paragraph of one to three binding sentences for each part of another question that it answers”.
- **WAY-391 — Which file is the exemplar of the kind `shared-module` in the-way's code?** — zmieniane tylko pole *Scope* (punkt 11 „To do”); dziś `- **Scope:** relation-model`.
- **WAY-19 — How are decisions numbered?** — zmieniana: nazwa części pytania w pierwszym zdaniu (punkt 10 „To do”); poza tym podstawa podziału WAY-344: „a new question gets the next free number, a question independent of every existing entry included, while a part of the question an existing entry answers is a sentence of that entry where it cannot change without changing that entry” oraz „When a new decision answers a question that an older one answered in passing, the sentence moves to the new decision, and the older one loses it in the same change.”
- **WAY-25 — What settles a collision between two decisions?** — bez zmian; forma pierwszeństwa nowej decyzji: „Where two decisions both apply and collide, the one that prevails names the other in *Relations* as `narrows`, and its binding sentences state the area where it prevails”.
- **WAY-18 — How is a product's decision log kept?** — bez zmian; miejsce nowej decyzji i jeden koniec relacji — `narrows` zapisuje tylko nowa decyzja, a WAY-344 nazywa ją w zdaniu wiążącym, nie w *Relations*: „in a log so divided a new entry stands at the end of the section of its topic, or, where no section fits, in a new section at the end of the log, which the request that adds the entry names” oraz „A link between entries is written at one end only”. Numer w zdaniu wiążącym nie jest zapisem relacji: przykład naruszenia WAY-18 mówi o polu *Relations* („a decision that another narrows names that other in its own *Relations* as well”), a sama WAY-18 nazywa w zdaniu wiążącym WAY-150, mając *Relations* `none`.
- **WAY-12 — How is a decision checked?** — bez zmian; nowa decyzja i każda decyzja o zmienionych zdaniach musi być czymś trzymana: „The check of the foundation reports as an error a decision that a change adds, or whose binding sentences the change alters, and that nothing holds.”
- **WAY-02 — How does whatever depends on an entry refer to it?** — bez zmian; linie `decision:`: „it gives the number and, in straight double quotation marks, the start of that sentence — from where a sentence of the entry begins, three words or more”.
- **WAY-30 — What happens when a change contradicts a decision?** — bez zmian; zmiany decyzji niesie ten dokument: „A change to a decision that a task needs is written into the task's plan, or into its task document where no plan is written, and approved with that plan or document by the human who accepts decisions (WAY-14) before the code that needs it is made”.
- **WAY-114 — What does a human accept of an entry, and when?** — bez zmian; znaczenie nowej decyzji Mariusz przyjmuje z tym dokumentem, bo powstaje z wiersza „Settlements to record”: „that of an entry written whole from an accepted row of a task's *Settlements to record* with the task document, the row being the human's own settlement”.

## Settlements to record

Candidates: 11 shown, 1 accepted — 2026-11-20

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | To, co komenda licząca audyt robi, gdy plik, który czyta, nie ma pola, stoi w osobnej decyzji z własnym numerem, a WAY-344 trzyma regułę ogólną; zmienia to WAY-344. | decision | pytanie „Co zrobić z WAY-344” (wybór doradcy dnia w imieniu Mariusza; odrzucone warianty pod pytaniem); jej *Scope*, sekcję i wyłączenie w WAY-344 dają pytania „Jaki *Scope* dostaje nowa decyzja” i „W której sekcji dziennika decyzji staje nowa decyzja” | zostawi wszystko w WAY-344 i podzieli ją na pięć akapitów, więc następny przypadek komendy audytu znów trafi do reguły ogólnej |

## Out of scope

- Dziesięć wpisów z tabeli „Podział na akapity” nie traci słów: zadanie ich nie skraca ani nie przepisuje.
- Pięć akapitów innych wpisów, które stoją tuż pod limitem słów.
- Zmiana WAY-05 i skryptu `elements/common/foundation_check.py` oraz reguły szablonu decyzji, także o akapit na część własnego pytania wpisu i o limit 600 słów wpisu: należą do zadania ze skryptem i jego requestu #152; to zadanie przestawia w szablonie tylko miejsce słów o 600 słowach we wzorze wpisu (punkt 13).
- Wpisy loop2 ponad limit: mają własne zadanie w projekcie „(P) Loop”.

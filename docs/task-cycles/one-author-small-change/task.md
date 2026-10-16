---
title: "the way: zmianę, którą obejmie jeden agent, robi jeden autor — rewizja WAY-136"
status: draft
created: 2026-10-16
updated: 2026-10-16
tags: [the-way, zadanie]
related: ["[[(P) Proces pracy nad produktem]]"]
---

# the way: zmianę, którą obejmie jeden agent, robi jeden autor — rewizja WAY-136

Status: ready for cycle
Project relation: independent

## Description

### Need

- Najtańszy cykl `implement-task` kosztuje dziś 50–72 mln tokenów i 51–121 min pracy agentów, także dla zmiany kilku plików tekstu; samo wykonanie zmiany to 9–20% tych tokenów.
- Ponad połowę tokenów małego cyklu zużywa orkiestrator na rozsyłanie pracy, czekanie na agentów i czytanie ich raportów, a każdy kolejny agent czyta zadanie i fundament od nowa.
- WAY-136 prowadzi każde zadanie przez osobnego planistę, osobnego agenta fundamentu i wykonawcę, choć WAY-13 pozwala, by rozmiar zadania odchudził przygotowanie i wykonanie zmiany — plan i liczbę agentów — nigdy jej sprawdzenia.
- Prawie każde zadanie zmienia fundament, więc tańsza droga musi obejmować zadania z wpisami fundamentu, a nie tylko te bez nich.
- Mariusz chce obniżyć koszt i czas wykonywania zadań.

### To do

1. Zmianę, którą według oceny orkiestratora w kroku 4, na podstawie opisu zadania, jeden agent jest w stanie objąć, robi jeden autor bez planu: wpisy fundamentu, kod i krok powrotu.
2. Zdanie niezmiennika i jego test pochodzą przy takiej zmianie od dwóch innych agentów niż autor kodu (WAY-69).
3. Autor, któremu zmiana okaże się za duża, oddaje raport bez kodu; jego próba odpada razem z wpisami fundamentu, które napisał, a planista dzieli zmianę.
4. Droga jednego autora obowiązuje także po specu.
5. Zmianę jednego autora przegląda agent, który jej nie robił, a ten przegląd jest przeglądem całej zmiany i przejmuje to, co dziś sprawdza przegląd planu: pokrycie zadania, każdego wiersza *Settlements to record* i każdego wpisu projektowanego oraz kolejność wpisów fundamentu przed kodem, który od nich zależy.
6. Niezależna ocena zmiany fundamentu (WAY-10), bramka i krok powrotu zostają takie jak dziś.
7. WAY-135 zgadza się z punktem 4 — dziś mówi, że ze specu pisze się plan od nowa.
8. Warunki przeglądu WAY-136 i WAY-135 nie zawierają liczb tokenów; w WAY-136 zostają: pięć cykli na nowej regule, zmiana zwrócona przez autora jako za duża w dwóch cyklach z trzech, więcej niż jeden plasterek z trzech zwrócony jako za duży, termin 2026-11-30.
9. Skill cyklu, skill planu zadania, szablon zapisu cyklu i opis skryptu rozmiaru plasterków opisują drogę jednego autora.

### Questions to settle

- Kto ocenia, że jeden agent obejmie zmianę, i na czym?
  - Answer: Orkiestrator w kroku 4, na podstawie opisu zadania; błędną ocenę ogranicza zwrot autora bez kodu. Odrzucony wariant: zawsze mały plan i decyzja skryptem rozmiaru plasterków — płaci za plan, który zmiana ma zdjąć.
  - Source: Mariusz, 2026-10-16, „poza tym chyba ok” na propozycję 1 przy projekcie WAY-136.
- Czy droga jednego autora obowiązuje także po specu?
  - Answer: Tak; spec rozstrzyga projekt, a gdy wykonanie mieści się w jednym agencie, nie ma czego dzielić.
  - Source: Mariusz, 2026-10-16, „poza tym chyba ok” na propozycję 2 przy projekcie WAY-136.
- Czy warunki przeglądu decyzji mają zawierać liczby tokenów?
  - Answer: Nie dla WAY-136. Mariusz: „nie wiem czy te liczby tokenowe mają sens w decyzji”; rekomendacja: zostawić warunki obserwowalne bez skryptu i policzyć koszt przy przeglądzie.
  - Source: Mariusz, 2026-10-16, rozmowa w sesji refinementu.
- Czy liczbę 363,7 mln tokenów usunąć także z warunków przeglądu WAY-135?
  - Answer: Tak; WAY-135 i tak się zmienia, a obie decyzje o cyklu mają być mierzone tak samo.
  - Source: Mariusz, 2026-10-16, „2. tak”.
- Czy droga jednego autora zostaje po specu także wtedy, gdy spec dotyka kilku części produktu? (pytanie wobec odpowiedzi; zakotwiczenie: WAY-135/1 „a fresh agent given the report writes the spec, from which the plan is written again”)
  - Answer: Tak; po specu orkiestrator ocenia rozmiar tą samą miarą co w kroku 4, a zmiana rozdmuchana przez spec idzie do planisty.
  - Source: Mariusz, 2026-10-16, „3. niech będzie jak proponujesz”.

## Context

### Co na to zadanie czeka

- Zmiana z lekcji m2l4 (wybór stacku zatrzymuje zadanie i wraca do `settle-technology`) czeka na tę rewizję i ma być pierwszym zadaniem nowej drogi; nie należy do zakresu tego zadania.

### Pomiar kosztu cyklu (2026-10-16)

- Pomiar skryptem `task-cycle/cycle_stages.py` z zapisów sesji Codex i Claude Code; etapy przypisane do kategorii po nazwach podagentów; czas to praca agentów bez czekania na człowieka.
- Małe cykle the way: PR #17 (skrócenie cyklu, 1 plasterek) 50,0 mln / 87 min; PR #15 (instalator, 2 plasterki) 54,7 mln / 51 min; PR #18 (wybiórczy odczyt, 2) 72,3 mln / 121 min; PR #14 (przejęcia m1l5, 3) 71,4 mln / 89 min.
- W tych czterech cyklach etapy płacone zawsze — rozpoznanie, plan, fundament z krokiem powrotu, przegląd, ocena, orkiestrator — to 34–45 mln; wykonanie zmiany 6–15 mln; przegląd kodu i niezależna ocena razem ok. 10–15%.
- Udział orkiestratora w tokenach: PR #17 57%, PR #15 68%, PR #18 49%, PR #14 48%.
- W cyklu PR #17 orkiestrator wykonał 159 kroków przy kontekście rosnącym od 33 tys. do 310 tys. tokenów (średnio 179 tys.): 94 polecenia w konsoli, 36 oczekiwań na agentów, 17 wiadomości do agentów, 7 uruchomień agentów.
- Ponad 95% tokenów to wejście czytane z pamięci podręcznej, więc suma nie jest miarą kosztu pieniężnego.
- Duże cykle `loop2`: zadanie 3 (`mag-w-lesie`, 10 plasterków) 205,5 mln / 235 min plus korekta po przeglądzie 140,2 mln / 146 min; `serwer-testowy` (6) 271,1 mln / 390 min.
- Wszystkie siedem zmierzonych zadań zapisało nowe wpisy fundamentu; żadne nie przeszłoby lżejszą drogą wybieraną po tym, czy zmiana dotyka fundamentu.

### Projekt brzmienia WAY-136 pokazany w refinemencie

- Mariusz przyjął go słowami „poza tym chyba ok”, z zastrzeżeniem co do liczb tokenów; cykl wybiera brzmienie, zachowując znaczenie wierszy *Settlements to record* (WAY-134).
- Zdania wiążące z projektu: „A change that, as the orchestrator judges from the task document before any code is made, one agent can hold is made without a plan by one author, who writes its foundation entries, its code and its return step, while an invariant's sentence and its check still come from two other agents (WAY-69); an author that finds the change too large returns a report without code, its attempt is discarded with the foundation entries it wrote, and a planner divides the change. Every other change gets a plan written with the-way's skill `plan-task`, which divides it into slices and holds no code, recommends useful slices that can be worked on and reviewed separately and identifies possible parallel work independently of the chosen execution skill, while the orchestrator records before execution whether that opportunity can be used, from dependencies, shared files or mutable state, separate review and the skill's restrictions; each slice is made by an agent of its own, and a slice that proves too large for it is discarded with its code and goes back to the planner to be split. A one-author change and every slice are reviewed by an agent that did not make them, and a change of more than one slice then gets one review of the whole change, while the review of a one-author change or of a plan's only slice is the review of the whole change.”
- Uzasadnienie z projektu: plan zarabia na siebie podziałem zmiany; gdy jeden agent obejmuje całą zmianę, nie ma czego dzielić, a większość kosztu cyklu leży poza zmianą — w ponownym czytaniu zadania i fundamentu przez kolejnych agentów i w krokach orkiestratora przy każdym przekazaniu; planista, osobny agent fundamentu i wykonawca dokładają ten koszt bez dokładania sprawdzenia, bo wszystkie sprawdzenia gotowej zmiany zostają.
- Odrzucone w projekcie: lżejsza droga wybierana po tym, czy zmiana dotyka fundamentu — prawie każda zmiana pisze wpisy fundamentu, więc nie odchudziłaby prawie niczego; lżejszy przegląd, ocena albo bramka dla małej zmiany — rozmiar nie dowodzi, że znaczenie zmiany zostało (WAY-13); osobna droga dla małych zadań poza cyklem — dwie drogi trzymałyby te same reguły zapisu, MR-a i kroku powrotu.

### Ryzyka wybranego wariantu

- Jeden agent pisze wpisy fundamentu i kod, więc może dopasować wpis do swojego kodu; bronią przed tym niezależna ocena bez rozumowania autora, przegląd innego agenta i osobni autorzy zdania i testu niezmiennika.
- Ocena orkiestratora przed kodem może być błędna; jej koszt ogranicza zwrot autora bez kodu.

### Gdzie szukać

- Teksty, które dziś zakładają plan dla każdego zadania: `task-cycle/skill/SKILL.md` (krok 4, akapit „Design and plan”, kroki 8–9), `task-cycle/plan/SKILL.md`, `task-cycle/record_template.md` (wymienia `plan.md` i `plan-size.md`), opis w `task-cycle/slice_size.py`.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-136/1 — zadanie zmienia jej brzmienie (droga jednego autora) i warunki przeglądu:
  > Every task's cycle writes a plan with the-way's skill `plan-task`, which divides the change into slices and holds no code; the plan recommends useful slices that can be worked on and reviewed separately and identifies possible parallel work independently of the chosen execution skill, while the orchestrator records before execution whether that opportunity can be used, from dependencies, shared files or mutable state, separate review and the skill's restrictions. Each slice is made by an agent of its own and then reviewed by an agent that did not make it, and a change of more than one slice then gets one review of the whole change, while the review of a plan's only slice is the review of the whole change. A slice that proves too large for the agent making it is discarded with its code and goes back to the planner to be split.
- WAY-135/1 — „from which the plan is written again” koliduje z punktem 4:
  > A task's cycle writes a spec, reviewed by an agent other than its author, before its plan where the task leaves an open design choice and nowhere else, and an invariant whose sentence a row of the task's *Settlements to record* or a projected entry of its sources gives leaves none. An agent that meets an open design choice while it makes the change returns a report that holds no code, the attempt is discarded with the foundation entries the cycle wrote for it, and a fresh agent given the report writes the spec, from which the plan is written again.
- WAY-13/1 — pozwala, by rozmiar odchudził przygotowanie i wykonanie, nigdy sprawdzenia; WAY-136 z niej wynika:
  > What a task touches, never its size, sets the path that merges its change and how sharply that change is checked: an agent's analysis at the start of the task settles whether it changes the foundation, which chooses among the paths that merge a change, while three things set how sharply it is checked — the criticality of the parts it touches, as the part map computes it, whether it touches the files of a trust boundary, and whether the change can be undone. Paths that merge a change differ in their steps, never in the outcome a task has to reach, and only a human sets a task to return knowledge instead of a change, which merges nothing. A task's size may lighten how its change is prepared and made — its plan and the number of agents making it — never the outcome it has to reach or the checks run on the finished change, and otherwise serves only as a signal to split it; an agent may check a change more sharply than the map computes, never less, and a human decides on every change that cannot be undone.
- WAY-69/1 — trzech różnych autorów zdania niezmiennika, testu i kodu zostaje przy drodze jednego autora:
  > An invariant's sentence, the check that cites it and the code it covers come from three different agents, and the deliberate break the check is accepted on is written from the sentence by the reviewer of that code, who did not write the check. A check that cites an invariant takes the input it asserts on and the value it expects written out, wherever the code its invariant is about would otherwise compute either; only the side it compares against comes from the run.
- WAY-10/1 — niezależna ocena zostaje bez zmian:
  > A change to an invariant test or to the foundation is assessed by one independent agent, on a model other than its author's where one is available, which sees the diff and the files of the commit it assesses without the task's chronicle or the author's reasoning and names what of the change can be cut, or that nothing can. The author settles each of its remarks and records how, and a settlement that changes the assessed foundation entries or invariant tests is part of the assessed change and does not reopen its assessment. A human accepts the change, with the assessment and its settlement, when merging it.
- WAY-11/1 — krok powrotu robi „an agent”; przy drodze jednego autora robi go autor:
  > A task ends with its return step before its branch is merged: an agent searches the diff and the task's log for new rules and decisions, code behaviour with no invariant over it, environment facts the change rests on that the foundation does not yet hold and words whose use the glossary does not yet settle, writes the resulting foundation entries in the same change, which its independent assessment covers (WAY-10), and compares the foundation with the code in the parts the task touched. Uncovered code behaviour becomes an invariant when changing it in a later task would violate a requirement or a settled rule of the product; an implementation detail that can change without such a violation stays in ordinary tests and the description of the change, and this distinction leaves decision-derived invariants (WAY-12, WAY-22), accepted settlements (WAY-134) and the task's duties for projected entries (WAY-126) required. A periodic review of the foundation runs apart from tasks.
- WAY-01/1 — krok fundamentu przed kodem zostaje; przy drodze jednego autora robi go autor:
  > On the main branch, the foundation describes the product as it is — its rules, together with the listed debt wherever the product does not yet meet them — and roadmaps and plans do not change it. A task that sets out to change the foundation makes that change in its foundation step, and the code follows; a foundation change in progress lives on the task's branch in the product's repository and reaches the main branch in the same merge as the code that follows it. When a task closes, the foundation again matches the current state.
- WAY-125/1 — przyjęte metody Superpowers; zmiana jednego autora ma jeden przegląd całej zmiany, jak dziś plan jednego plasterka:
  > The the-way task cycle adopts Superpowers 6.4.1 methods for brainstorming a design and written spec, test-first implementation, subagent execution with independent task and final code reviews, and preparing a pull or merge request, only for a ready task run through `implement-task`. The orchestrator answers workflow questions and gives provisional stage go-aheads under the task owner's delegation, never records these as human approval, controls the return between stages, keeps agent reports before a borrowed skill cleans its workspace, runs the independent assessment of its foundation change and its return step, and brings the request to the human for review. Decisions reserved to a human by the foundation remain reserved; when required code cannot proceed without one, the cycle opens a blocked draft request; a different Superpowers version requires a reviewed change to the-way before use.

## Settlements to record

Candidates: 5 shown, 5 accepted — 2026-10-16

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Zmianę, którą jeden agent jest w stanie objąć, robi jeden autor bez planu — wpisy fundamentu, kod i krok powrotu; osobni zostają przeglądający, niezależny oceniający i autorzy zdania oraz testu niezmiennika. | decision | Mariusz, 2026-10-16: „tak, wydaje się to sensowne” i „poza tym chyba ok”; To do 1, 2, 6 | Czy zadanie jednego plasterka dalej przechodzi przez planistę, osobnego agenta fundamentu i wykonawcę. |
| 2 | O tym, czy jeden agent obejmie zmianę, rozstrzyga orkiestrator w kroku 4 z opisu zadania; autor, któremu zmiana okaże się za duża, oddaje ją bez kodu planiście. | decision | Questions to settle — kto ocenia; To do 1, 3 | Czy przed decyzją pisać mały plan i mierzyć go skryptem rozmiaru plasterków. |
| 3 | Droga jednego autora obowiązuje także po specu; po specu orkiestrator ocenia rozmiar tą samą miarą co w kroku 4. | decision | Questions to settle — droga po specu i pytanie wobec odpowiedzi; To do 4, 7 | Czy po specu zawsze pisać plan, jak dziś mówi WAY-135. |
| 4 | Przegląd zmiany jednego autora przejmuje sprawdzenia przeglądu planu: pokrycie zadania, wierszy ustaleń i wpisów projektowanych oraz kolejność wpisów fundamentu przed kodem. | decision | To do 5; propozycja z refinementu; Mariusz, 2026-10-16, „przyjmuję propozycje” | Czy przy braku planu ktokolwiek sprawdza pokrycie zadania i kolejność wpisów przed kodem. |
| 5 | Warunki przeglądu decyzji o cyklu nie zawierają liczb tokenów. | decision | Questions to settle — liczby tokenów w WAY-136 i WAY-135; To do 8 | Czy zostawić w warunkach przeglądu WAY-136 i WAY-135 progi 50,0 mln i 363,7 mln tokenów. |

## Out of scope

- Odchudzenie samego orkiestratora (krótszy kontekst, przejęcie pracy przez świeżą sesję na granicy etapu, mniej jego własnych kroków) — osobny pomiar po tym zadaniu.
- Lżejsze stopnie dla zadań produktu bez nowego znaczenia (tekst przycisku, literówka) — wrócą, gdy będzie na czym je sprawdzić.
- Uruchamianie wybranych elementów cyklu: [[cykl_zadania_czesciami]].

---
title: "the way: co robi prowadzący cykl, gdy agent nie przeczytał wskazanego materiału"
status: draft
created: 2026-11-01T08:29
updated: 2026-11-08
tags: [zadanie]
related: "the project note in the author's notes"
---

# the way: co robi prowadzący cykl, gdy agent nie przeczytał wskazanego materiału

Status: ready for cycle
Project relation: independent

## Description

### Need

- Agenci w cyklu the way mają przeczytać w całości wskazane pliki i wpisy fundamentu; gdy tego nie zrobią, piszą o tym w raporcie, ale żadna zasada nie mówi, co dalej.
- Prowadzący cykl raz każe doczytać, raz przekazuje lukę następnemu agentowi, a raz przechodzi nad tym do porządku.
- Odczuwa to Mariusz przy PR-ze: widzi zaliczony przegląd i nie wie, że recenzent znał większość decyzji tylko z tytułów, jak 111 ze 151 w PR #62 repozytorium the-way.
- Jeśli nic nie zrobimy, błąd schowany w nieprzeczytanym materiale przejdzie przez przegląd, który wygląda tak samo jak pełny; w loop2 PR #43 doczytanie dało nową uwagę, ale dopiero po zużyciu jedynej rundy poprawek specyfikacji.

### To do

1. Prowadzący cykl, w `task-cycle/skill/SKILL.md` po słowach „add what it found to the handoffs that follow.”, dostaje dopisek:
   > Where a report says that something its handoff names stayed unread or was read in part, decide before you act on its status: resume the agent to read it, carry the gap into the handoff of the next agent able to judge it, or record an autonomous choice saying why it bears on nothing the agent judged.

   Ostatnie zdanie dopisku z notatki zadania („A reviewer of the whole change that read only part of its selection says how much, and the request carries that one line.”) zastępują punkty 3 i 4 (pytania 2 i 3).
2. Raport każdej z pięciu metod etapów ma stały dział o tym, co ze zlecenia — u recenzenta całej zmiany: z własnego wyboru — zostało nieprzeczytane albo przeczytane w części, albo `none`; prowadzący cykl czyta go w każdym raporcie, a raport bez tego działu wraca do agenta do uzupełnienia (pytanie 1).
3. Opis PR-a (`task-cycle/skill/request_template.md`) stawia w sekcji dla decyzji człowieka, obok pominiętych kroków i nieuruchomionych sprawdzeń, jedną pozycję o niepełnej lekturze recenzenta całej zmiany, z pytaniem, czy scalić mimo to — tylko wtedy, gdy recenzent nie przejrzał reszty swojego wyboru po tytułach albo sam przyznał, że decyzja dotycząca zmiany została nieprzeczytana, a luki nie zamknięto po drodze (pytania 2 i 3).
4. Recenzent całej zmiany czyta w całości decyzje swojego wyboru, które dotyczą tematu zmiany, resztę wybranych przegląda po tytułach i otwiera każdą, której tytuł wskazuje na związek ze zmianą; w raporcie podaje, ile decyzji przeczytał w całości, a ile tylko po tytule. Zmienia się WAY-150 i miejsca, które ją przenoszą do metod (`task-cycle/review/SKILL.md`, sekcja „Read”; „Reading the foundation” w `elements/common/way_of_working.md`), tak że zdanie „The whole log is not read.” przestaje przeczyć praktyce recenzenta (pytanie 3).

### Questions to settle

- Pytanie 1: gdzie agent etapu zapisuje, czego ze zlecenia — a recenzent całej zmiany: ze swojego wyboru — nie przeczytał albo przeczytał w części, tak żeby prowadzący cykl to zobaczył także w raporcie o statusie `done` albo `PASS`?
  - Answer: nowy, stały dział raportu w każdej z pięciu metod etapów (`make-change`, `review-change`, `plan-task`, projektant i recenzent `write-spec`): co ze zlecenia — u recenzenta całej zmiany: z własnego wyboru — zostało nieprzeczytane albo przeczytane w części, albo `none`; prowadzący cykl czyta ten dział w każdym raporcie, a raport bez niego wraca do agenta do uzupełnienia jak raport bez **Searches not found or unclear**.
  - Not chosen:
    - wpisywać to do **Searches not found or unclear** — ten dział trafia słowo w słowo do uwag o procesie the way (WAY-260), a nieprzeczytany plik zwykle dotyczy tylko tej zmiany, więc do uwag o procesie wpadnie szum.
    - zostawić tylko dopisek z punktu 1 — przy statusie `done` albo `PASS` prowadzący nie czyta reszty raportu (`task-cycle/skill/SKILL.md:191-193` @ a3206c1), więc dopisek zadziała tylko wtedy, gdy prowadzący przeczyta więcej, niż musi.
  - Source: Mariusz, 2026-11-08: „a” — na drogę a przedstawioną w rozmowie doprecyzowania; pytanie kontrolne 2026-11-08 (anchor: WAY-150 *Rejected*, `foundations/decisions.md:4113-4114` @ a3206c1, „a record of the selection compared with every *Scope* of the log — it costs every piece of work and records reading, not understanding”): Mariusz, „tak, zostaje” — dział ujawnia tylko lukę, którą agent sam przyzna, i nie zapisuje wyboru lektury.
- Pytanie 2: w której części opisu PR-a stoi linia o niepełnej lekturze recenzenta całej zmiany?
  - Answer: w górnej części, jako pozycja sekcji dla decyzji człowieka, obok pominiętych kroków i nieuruchomionych sprawdzeń — np. „Przegląd całej zmiany przeczytał w całości 40 ze 151 wybranych decyzji; scalić mimo to?”; pozycja stoi tylko wtedy, gdy recenzent nie przejrzał reszty swojego wyboru po tytułach albo sam przyznał, że decyzja dotycząca zmiany została nieprzeczytana, a luki nie zamknięto po drodze (zawężone odpowiedzią na pytanie 3, 2026-11-08: przesiew po tytułach jest odtąd zasadą, więc lektura zgodna z nią nie czeka na zgodę). Słaby punkt przyjęty z tą drogą, przed zawężeniem: sekcja rzadko byłaby pusta, bo sprawa wracała w 15 z 18 przejrzanych cykli, a WAY-287 opiera się na tym, że jej `none` znaczy „można scalać” („One section that holds every such matter makes its `none` a statement the human can merge on.”, `foundations/decisions.md:8831-8832` @ a3206c1).
  - Not chosen:
    - zdanie w górnej części poza sekcją decyzji — niepełny przegląd przechodzi bez zgody człowieka, tylko z adnotacją, w miejscu, które szablon daje na co innego.
    - dolna część, sekcja sprawdzeń — człowiek jej nie czyta, więc dalej nie wie, że przegląd był niepełny.
  - Source: Mariusz, 2026-11-08: „a” — na drogę a przedstawioną w rozmowie doprecyzowania, ze słabym punktem nazwanym w pytaniu; `task-cycle/skill/request_template.md:171-178` @ a3206c1.
- Pytanie 3: czy to zadanie zawęża też wybór lektury recenzenta całej zmiany, czy zostawia to osobnemu zadaniu po pomiarze trafności?
  - Answer: to zadanie zapisuje jako zasadę przesiew, który recenzenci już robią: recenzent całej zmiany czyta w całości decyzje dotyczące tematu zmiany, resztę swojego wyboru przegląda po tytułach i otwiera każdą, której tytuł wskazuje na związek ze zmianą, a w raporcie podaje, ile przeczytał w całości. Nie zawęża lektury względem dzisiejszej praktyki, więc nie czeka na pomiar; zmienia WAY-150 i zawęża, kiedy staje pozycja z pytania 2. Słaby punkt przyjęty z tą drogą: przesiew po tytułach może przepuścić ważną decyzję o niepozornym tytule — dziś dzieje się to samo bez zapisu, więc ryzyko nie rośnie, ale też nie znika.
  - Not chosen:
    - osobne zadanie po pomiarze trafności — do tego czasu pozycja z pytania 2 stoi w prawie każdym PR-ze, a to zadanie tylko ujawnia lukę; Mariusz: „nie lubię mnożyć zadań — mam wtedy poczucie, że robię zadanie, które nic nie znaczy, bo i tak trzeba po nim zrobić następne”.
    - zawężenie wyboru w tym zadaniu bez pomiaru, np. tylko decyzje dotyczące tematu zmiany — nie wiadomo, czy węższy wybór nie zgubi ważnej decyzji.
    - nie zawężać wcale — pozycja w PR-ze zostaje na stałe, a zdanie „The whole log is not read.” (`elements/common/way_of_working.md:78` @ a3206c1) dalej przeczy praktyce.
  - Source: Mariusz, 2026-11-08: „tak, włączamy” — na wariant przesiewu po tytułach przedstawiony w rozmowie doprecyzowania; pytanie kontrolne 2026-11-08 (anchor: WAY-150 *Rejected*, `foundations/decisions.md:4110-4111` @ a3206c1, „selection only from known links or keywords — a governing decision can remain unseen”): Mariusz, „tak, zostaje” — przesiew działa wewnątrz wyboru po *Scope*, nie zamiast niego; praktyka recenzentów: PR #62 testing-skill-shape — 40 ze 151 decyzji w całości, 111 po tytule; kopia-bazy — 69 z 99 odsianych po temacie (`the AI-review ledger in the author's notes (lines 990-993)`, notatka zadania z 2026-11-01).
- Pytanie 4: czy zadanie czeka na własne wytyczne kodowania i testów the way, skoro repozytorium the-way nie ma `guidelines/`, a WAY-215 trzyma zadanie piszące kod albo testy w produkcie bez wytycznych w doprecyzowaniu?
  - Answer: nie czeka; zadanie idzie do cyklu drogą z `agent-instructions/README.md`, jak poprzednie zadania the way, a rozjazd reguły z praktyką zostaje w zadaniu the task about the-way's own guidelines.
  - Not chosen:
    - czekać na zadanie o wytycznych the way — to zadanie nie ma jeszcze kierunku, więc poprawki stałyby bez terminu.
  - Source: Mariusz, 2026-11-06: „nadal jedziemy bez tego” — `another task's note in the author's backlog (lines 93)`; ta sama odpowiedź przeniesiona w pytaniu 4 `another task's note in the author's backlog (lines 86-90)`.

## Context

- Źródło: sprawa AIR-561 z przeglądu warstwy AI, 2026-11-01 — `the AI-review ledger in the author's notes (lines 980-1011)`, z cytatami z trzech cykli (loop2 PR #43, the-way PR #59, the-way PR #62); po 14 dniach od zamknięcia sprawa przechodzi do `ai_review_ledger_archive.md` w tym samym katalogu.
- Sprawa wróciła w 15 kolejnych cyklach, od loop2 PR #44 (2026-11-02) do loop2 PR #62 (2026-11-08) — `the table of read cycles in the author's notes`, wiersze z „AIR-561”; w większości chodzi o recenzenta całej zmiany, który z wyboru po *Scope* przeczytał węższy zestaw (np. 166 z 268 decyzji, 144 decyzje przeczytane tylko w trafieniach wyszukiwań, pominięty plik wytycznych kodu przy zmianie lockfile'a).
- Trzy drogi zamiast dwóch, bo trzecia już działa: w cyklu technology-skill-shape zlecenie recenzenta mówi „Whatever that affects is yours to judge”, a w styleguide-skill-shape recenzent doczytał 21 z 23 pozycji pominiętych przez autora i nie znalazł naruszeń.
- Jedna linia w PR-ze, a nie lista identyfikatorów, bo 111 numerów decyzji nic człowiekowi nie mówi, a WAY-150 mówi, że wyboru lektury się nie zapisuje.
- Notatka zadania wskazywała miejsca według `foundations` @ ea4694e; od tego czasu weszły 152 commity: zdanie-kotwica stoi dziś w `task-cycle/skill/SKILL.md:193`, a opis PR-a nie stoi już w sekcji `task-cycle/record_template.md`, tylko w osobnym `task-cycle/skill/request_template.md` (WAY-286) — stan `foundations` @ a3206c1.
- W każdym raporcie prowadzący czyta dziś tylko sprawdzenia, sięgnięcia poza zlecenie i **Searches not found or unclear**, a resztę raportu tylko przy statusie innym niż `done` (`task-cycle/skill/SKILL.md:191-193` @ a3206c1); żadna z metod etapów (`task-cycle/change/SKILL.md:127-146`, `task-cycle/review/SKILL.md:128-143`, `task-cycle/plan/SKILL.md:194-198`, `task-cycle/spec/design.md:68-74`, `task-cycle/spec/review.md:22-25`) nie ma w raporcie miejsca na materiał nieprzeczytany.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

Cytaty z `foundations/decisions.md`, `foundations` @ a3206c1; numer linii to nagłówek decyzji.

- WAY-148 — How do task-cycle stages pass their work to the orchestrator? (`:3999`): „The handoff names what the agent reads, as the orchestrator selects it (WAY-150, WAY-213) […] a missing or incomplete report is repaired before dependent work proceeds”.
- WAY-150 — How do the-way skills choose which product foundation material to read? (`:4060`): „[…] the reviewer of the whole change selects for its own review […] and every other agent of the cycle reads what its handoff names and reaches for what is missing selectively […] naming each such reach in its report. The selection is neither recorded nor compared with every *Scope* of the log”. Zmienia ją punkt 4 *To do* (pytanie 3): recenzent całej zmiany czyta w całości decyzje dotyczące tematu zmiany, a resztę wyboru przesiewa po tytułach, zamiast czytać każdy wybrany wpis w całości („reads each selected entry whole”).
- WAY-213 — How do the agents of a task's cycle read the product's guidelines? (`:6032`): „the agent reads each file named whole, never excerpts of it or a review checklist in its place, while the reviewer of the whole change selects the guidelines of its own review”. Przesiew po tytułach dotyczy tylko decyzji; plik wytycznych, którego agent nie przeczytał w całości, idzie do działu z punktu 2.
- WAY-159 — When does the task-cycle orchestrator rely on focused-check evidence? (`:4346`): „A report missing the command or the exit code of a check it ran is incomplete, and a claim that tests passed does not repair it”.
- WAY-260 — What does each task-cycle stage report about what it could not find or understand? (`:7721`): „Every task-cycle stage's report states each thing the agent looked for and did not find, or found unclear, wherever it arose, or `none`; it keeps this separate from the report's account of each reach beyond the dispatch.”
- WAY-286 — What form does the description of a request a task cycle opens take? (`:8766`): „first a top part written for the human in plain words, with no file names and no identifiers of entries […] then a lower part that holds, in a fixed order, the technical changes, the checks […]”.
- WAY-287 — What does a request put before the human for a decision? (`:8803`): „The section of a request's description for the human's decisions holds everything whose merge needs the human's yes — […] the steps skipped and the checks not run […] — and its `none` says that nothing else in the request waits for the human's yes.”

## Settlements to record

Candidates: 6 shown, 4 accepted — 2026-11-08

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Gdy raport mówi, że coś, co wskazało mu zlecenie, zostało nieprzeczytane albo przeczytane w części, prowadzący cykl przed działaniem na jego status wybiera jedną z trzech dróg: wznawia agenta, żeby doczytał, przenosi lukę do zlecenia następnego agenta, który może ją ocenić, albo zapisuje autonomiczny wybór z powodem, dla którego luka nie dotyczy niczego, co agent ocenił. | decision | punkt 1 *To do* (dopisek Mariusza z notatki zadania, 2026-11-01) | czy zapisać regułę tylko w skillu prowadzącego, czy jako decyzję; czy przy `PASS` z luką iść dalej, czy wznawiać recenzenta |
| 2 | Raport każdego etapu cyklu ma stały dział o tym, co ze zlecenia — u recenzenta całej zmiany: z własnego wyboru — zostało nieprzeczytane albo przeczytane w części, albo `none`, osobny od działu „czego szukałem i nie znalazłem”; prowadzący czyta go w każdym raporcie, a raport bez niego wraca do agenta do uzupełnienia. | decision | pytanie 1 | czy dopisać lukę do **Searches not found or unclear** (WAY-260), czy zrobić osobny dział; czy brak działu cofa raport |
| 3 | Recenzent całej zmiany czyta w całości decyzje swojego wyboru, które dotyczą tematu zmiany, resztę przegląda po tytułach i otwiera każdą, której tytuł wskazuje na związek ze zmianą, a w raporcie podaje, ile przeczytał w całości, a ile po tytule. | decision | pytanie 3 | czy recenzent czyta każdy wybrany wpis w całości, jak dziś mówi WAY-150 („reads each selected entry whole”), czy przesiewa; zmienia WAY-150 |
| 4 | Opis PR-a stawia przed człowiekiem do decyzji niepełną lekturę recenzenta całej zmiany tylko wtedy, gdy recenzent nie przejrzał reszty swojego wyboru po tytułach albo sam przyznał, że decyzja dotycząca zmiany została nieprzeczytana, a luki nie zamknięto po drodze. | decision | pytania 2 i 3 | czy linia stoi w sekcji decyzji człowieka, w sekcji sprawdzeń, czy w każdym PR-ze; rozszerza listę WAY-287 |

## Out of scope

- Przesiew po tytułach u innych, którzy wybierają lekturę z fundamentu (prowadzący cykl, doprecyzowanie zadania, definicja i plan projektu) — to zadanie zmienia tylko lekturę recenzenta całej zmiany.
- Pomiar, ile decyzji wybranych po *Scope* naprawdę dotyczyło zmiany.

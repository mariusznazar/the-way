---
title: "the way: raport każdego etapu cyklu mówi, gdzie agent szukał i nie znalazł albo co było niejasne — trafia do uwag procesowych rekordu"
status: draft
created: 2026-10-28T21:45
updated: 2026-10-29
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# Raport każdego etapu cyklu mówi, gdzie agent szukał i nie znalazł albo co było niejasne, a orkiestrator przenosi to do uwag procesowych rekordu

Status: ready for cycle
Project relation: independent

## Description

### Need

- W cyklu zadania the way każdy etap — projektant i recenzent specu, planista, autor zmiany, wykonawca kawałka, poprawka, recenzent — prowadzi osobny agent, który oddaje orkiestratorowi raport w pliku (WAY-148).
- Raport ma dziś pozycję „each reach beyond the dispatch: what, where and why” (np. `task-cycle/change/SKILL.md:124`, `task-cycle/review/SKILL.md:118` na `d7a205c`), czyli to, po co agent sięgnął poza zlecenie i co znalazł; nie ma pozycji na to, czego agent szukał i nie znalazł, ani na instrukcję, która była niejasna.
- Niejasność, której agent nie zgłasza orkiestratorowi pytaniem (status `questions`), agent rozwiązuje sam i nie zostaje po niej żaden ślad w określonym miejscu raportu.
- Pole „Process remarks on the-way” rekordu cyklu (`task-cycle/record_template.md:176` na `d7a205c`) wypełnia orkiestrator z tego, co sam zauważył; nocny `ai-review` robi sprawy AIR tylko z tego pola, więc zgubienia agentów etapów nie docierają do Mariusza, kiedy usprawnia the way.
- Bez zmiany miejsca, w których agenci etapów regularnie się gubią albo nie znajdują potrzebnej instrukcji, wychodzą najwyżej przypadkiem, gdy orkiestrator zauważy skutek.

### To do

1. Raport każdego etapu cyklu dostaje osobną pozycję, obok „reach”: wszystko, czego agent szukał i nie znalazł albo co było niejasne — w instrukcji the way, w zleceniu orkiestratora, w zadaniu, w fundamencie albo kodzie produktu; agent nie ocenia, czyja to luka; dozwolone jest „none”, żeby agent nie wpisywał czegoś na siłę. Pozycja „reach” zostaje bez zmian. Pozycję dostaje raport każdej metody etapu: `make-change` (autor zmiany, wykonawca kawałka, poprawka, korekta po uwagach, krok fundamentu, krok powrotu), `review-change`, `plan-task` oraz projektant i recenzent specu w `write-spec`.
2. Orkiestrator przenosi do pola „Process remarks on the-way” rekordu cyklu każdą taką pozycję poza „none”, słowo w słowo, z nazwą etapu i ścieżką raportu; tych samych zgłoszeń z kilku etapów nie łączy.
3. Dziennik decyzji the way dostaje nową decyzję o tej zasadzie, wynikającą z WAY-148 (wiersz *Settlements to record*).

### Acceptance criteria

- Pozycje przeniesione z raportów stoją w rekordzie w bloku, który wycina `cycle_remarks_digest.py` — w punkcie zaczynającym się od „Process remarks” albo w wierszach wciętych pod nim głębiej niż jego znacznik listy.

### Questions to settle

- Co obejmuje nowa pozycja raportu: tylko instrukcje the way, czy wszystko, czego agent szukał i nie znalazł — także w zadaniu, fundamencie i kodzie produktu — i jak ma się do istniejącego „reach”?
  - Answer: wszystko, czego agent szukał i nie znalazł albo co było niejasne — instrukcja the way, zlecenie orkiestratora, zadanie, fundament i kod produktu — jako osobna pozycja obok „reach”, które zostaje bez zmian; agent nie ocenia, czyja to luka.
  - Source: Mariusz, 2026-10-29: „A” — wybór spośród: A — szeroka osobna pozycja (słaby punkt: luki produktu z `loop2` dojdą do nocnej sesji i odpadną jako „produkt”, jak dziś); B — tylko instrukcje the way (agent musi w chwili zgubienia rozstrzygnąć, czyja to luka, i część sygnałów ginie przy wpisywaniu); C — rozszerzyć „reach” i przenosić wszystkie jego wpisy (szum rutynowych odczytów w nocnej sesji, zmiana pozycji, z której orkiestrator korzysta w cyklu). „Reach” na `d7a205c`: `task-cycle/change/SKILL.md:124` — „each reach beyond the dispatch (section 1): what, where and why;”.
- Czy pozycję dostają wszystkie etapy, czy tylko te, które czytają fundament i wytyczne (autor zmiany, recenzent)?
  - Answer: wszystkie — każda metoda etapu, w miejscu, gdzie jej raport ma dziś „reach”.
  - Source: Mariusz, 2026-10-29: „wszystkie, trochę sie obawiam o wzrost kosztów, ale na razie jest nam to potrzebne, żeby mieć podstawę do tego, żeby koszty obniżać, więc bierzemy wszystkie” — przeciw drodze „tylko autor i recenzent” (zgubienia projektanta i planisty, którzy czytają najszerzej, zostają niewidoczne). Miejsca „reach” na `d7a205c`: `task-cycle/change/SKILL.md:124`, `task-cycle/review/SKILL.md:118`, `task-cycle/plan/SKILL.md:181`, `task-cycle/spec/design.md:63`, `task-cycle/spec/review.md:24`.
- Jak orkiestrator traktuje powtórzenia: przenosi każdą pozycję, czy łączy te same zgłoszenia z kilku etapów?
  - Answer: przenosi każdą pozycję poza „none” słowo w słowo, z nazwą etapu i ścieżką raportu, bez łączenia; łączenie zostaje dla nocnej sesji, która widzi uwagi ze wszystkich cykli.
  - Source: Mariusz, 2026-10-29: „przenosimy dosłownie” — przeciw łączeniu przez orkiestratora (ocena, czy dwa zgłoszenia mówią o tym samym, i przeredagowanie ich wbrew zasadzie słowa w słowo z WAY-148; błędne połączenie ukrywa jedną z luk).
- Czy decyzja o zakresie „wszystkie etapy” ma podawać warunek powrotu do niego?
  - Answer: nie — decyzja mówi „wszystkie etapy” bez warunku.
  - Source: Mariusz, 2026-10-29: „bez warunku w decyzji” — na pytanie zakotwiczone w jego słowach „na razie jest nam to potrzebne”, przeciw warunkowi powrotu w decyzji (miara do ustalenia i obowiązek sprawdzenia w samej decyzji).
- Czy zasadę zapisuje nowa decyzja powiązana z WAY-148, czy zmiana samej WAY-148?
  - Answer: nowa decyzja, wynikająca z WAY-148, z własnym uzasadnieniem (zasada głupich pytań, E23) i własnymi odrzuconymi wariantami.
  - Source: Mariusz, 2026-10-29: „nowa” — przeciw zmianie WAY-148 (już długa decyzja o przekazaniu pracy orkiestratorowi rośnie o drugi cel, a nośnik E23 wskazałby decyzję mówiącą głównie o czym innym); słaby punkt nowej: o treści raportu mówią dwie decyzje. WAY-148, `foundations/decisions.md:3787` na `d7a205c`: „How do task-cycle stages pass their work to the orchestrator?”.

## Context

- Źródło: lekcja Mega.DEV s01e03, wiersz E23 mapy `Notes/Projects/(P) Przejście Mega.DEV/mapa_pakietu_mega_dev.md` — „Zasada głupich pytań — świeży agent dostaje zadanie bez szczególnego dostępu i mówi, gdzie się zgubił; miejsca potknięć to braki”, z nagrania; werdykt „przejmuję (the way)”, przyjęty przez Mariusza w kroku 3 lekcji, grupa G2.
- Ten sam wiersz E23 notuje, że w s01e02 odrzucono pokrewny wiersz E4 („raport agenta o tym, co widzi — odrzucone”).
- Kanał dalej istnieje i zmiana go nie dotyka: nocny `ai-review` wycina bloki „Process remarks” z rekordów scalonych do gałęzi głównej (`Notes/Areas/(A) Claude code/scripts/cycle_remarks_digest.py`, funkcja `extract_remark_blocks`), a sesja `/ai-review-cycles` robi z nich sprawy AIR; Mariusz czyta sprawy, nie raporty, więc materiału do czytania mu nie przybywa.
- Sesja `/ai-review-cycles` odrzuca dziś uwagi dotyczące produktu, nie the way (format dziennika odczytów w `cycle_remarks_digest.py`: „odpadły: … <l> produkt”).
- Orkiestrator czyta dziś w każdym raporcie jego sprawdzenia i „reach”, a resztę raportu tylko przy statusie innym niż `done` (`task-cycle/skill/SKILL.md:170–175` na `d7a205c`).
- Uwaga o the way idzie do uwag procesowych rekordu, nigdy do requestu (`task-cycle/skill/SKILL.md:69–70` na `d7a205c`).
- Żaden test w Pythonie the way nie sprawdza brzmienia pozycji raportów ani pola uwag procesowych (`git grep` na `d7a205c`), a zmiana nie pisze kodu, testów ani interfejsu; the way nie ma katalogu `guidelines/`, więc czytanie wytycznych nie ma tu nic do wyboru.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-148** (fragment) — „Every task-cycle stage passes its full handoff and report through files in the cycle's reports directory, while its messages carry routing, the stage's status, commits, a one-line check result naming what failed or did not run, and the report's path, while the agent's questions, concerns and each reach beyond its handoff stand in its report. The handoff names what the agent reads, as the orchestrator selects it (WAY-150, WAY-213), and keeps requirements and values in their own files: it may carry a section of the plan, spec or task copied word for word, never restated in other words, with its file named as its address […]” — nowa decyzja z niej wynika; jej lista tego, co stoi w raporcie, nie wymienia nowej pozycji.
- **WAY-125** (fragment) — „The task cycle `implement-task` uses the-way's own methods: `write-spec` for a spec and its review, `plan-task` for a plan, `make-change` for each change an author, a slice's executor or a fix makes, and `review-change` for each code review; the orchestrator conducts the cycle and its loop of slices itself.” — to metody, których raporty dostają nową pozycję (To do 1).
- **WAY-256** (fragment) — „A fragment of a skill — one the skill of `instruction-files` proposes for any skill, the skills of the-way's process included, or one a change to a skill of the-way adds or rewords — that only one step or one variant of the skill needs stands in a file beside the skill that the step names […]; a fragment of one step or variant that is one instruction, which would otherwise stand in a file beside the skill, stays in `SKILL.md` where its pointer would stand […]” — wiąże miejsce nowej pozycji w każdej metodzie.
- **WAY-27** (fragment) — „Nothing in this repository points to a source outside it that its readers cannot reach: every entry carries its whole reasoning, and what is seen only in such a source is described in the entry instead of being pointed to.” — nowa decyzja opisuje nocny kanał uwag procesowych własnymi słowami, bez odsyłacza do skryptu w prywatnych notatkach.

## Settlements to record

Candidates: 4 shown, 1 accepted — 2026-10-29

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Raport każdego etapu cyklu — wszystkich, bez warunku powrotu — dostaje osobną pozycję obok „reach”: wszystko, czego agent szukał i nie znalazł albo co było niejasne, gdziekolwiek (instrukcja the way, zlecenie, zadanie, fundament, kod produktu), z dozwolonym „none”; orkiestrator przenosi każdą pozycję poza „none” słowo w słowo, z etapem i ścieżką raportu, do uwag procesowych rekordu, bez łączenia; zapisuje to nowa decyzja wynikająca z WAY-148. | decision | Questions to settle — odpowiedzi Mariusza z 2026-10-29 („A”, „wszystkie…”, „przenosimy dosłownie”, „bez warunku w decyzji”, „nowa”), z odrzuconymi drogami; przyjęte przez Mariusza 2026-10-29: „przyjmuję jak rekomendujesz” | czy dopisać regułę do WAY-148, czy pisać nową; zakres pozycji i etapów; czy orkiestrator łączy zgłoszenia; które warianty trafiają do *Rejected* |

## Out of scope

- Po scaleniu, poza cyklem: przestawić nośnik w wierszu E23 sekcji s01e03 mapy `Notes/Projects/(P) Przejście Mega.DEV/mapa_pakietu_mega_dev.md` z linku do tego zadania na numer wpisu WAY — i nic więcej w mapie.
- Jeden zmierzony cykl na `loop2`, na który czeka krok 4 lekcji s01e03.
- Zmiany w `cycle_remarks_digest.py` i w sesji `/ai-review-cycles`.

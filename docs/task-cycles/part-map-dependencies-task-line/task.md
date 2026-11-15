---
title: "the way: mapa części — siedem zależności spoza Depends on i kto mówi, jak powstaje linia zadania"
status: draft
created: 2026-11-15
updated: 2026-11-15
tags: [zadanie]
related: "the project note of the process"
---

# the way: mapa części — siedem zależności spoza Depends on i kto mówi, jak powstaje linia zadania

Status: ready for cycle
Project relation: independent
Defect introduced by: https://github.com/mariusznazar/the-way/pull/126

## Description

### Need

- Przegląd fundamentu the way z 2026-11-14 (sprawdzony commit `21ecb62`) znalazł w mapie części the way miejsca, w których mapa mówi co innego niż kod albo niż reguły; Mariusz zdecydował, że idą jednym zadaniem.
- P26: kod siedmiu części sięga części, której pole *Depends on* tej części nie pozwala, więc mapa obiecuje granicę, której kod nie trzyma, a żaden niezmiennik tego nie oznacza:
  - `decisions` sięga `invariants`, `product-guidelines` i `project-level`;
  - `part-map` sięga `decisions`;
  - `elements-common` sięga `product-guidelines` (kontrola fundamentu czyta formę wytycznych);
  - `project-level` sięga `task-cycle` (czytnik stanów planu zależy od formy zapisu cyklu);
  - `task-cycle` sięga `foundation-review` (przypomnienie liczy od znacznika przeglądu);
  - `process-audit` sięga `gate` (liczenie czyta historię skryptu bramki);
  - `agent-instructions` sięga `foundation-review` i `process-audit` (punkty wejścia skilli).
- Nic w fundamencie nie mówi, co jest zależnością w rozumieniu *Depends on*, więc autor zmiany i czytelnik mapy mogą liczyć zależności różnie.
- Cztery z tych zależności czytają formę cudzego pliku, a zmiana tej formy po stronie piszącej przechodzi po cichu: zablokowane zadanie znika z planu, seria czasów bramki się nie zaczyna, wytyczne przestają być sprawdzane.
- P6 (WAY-107, zdanie części `project-level` w mapie, uwaga #102-5): mapa i `project-level/backlog_place.md` mówią, że the way odpowiada za to, „jak” powstaje linia zadania w backlogu, a od korekty #102 obsługa linii należy do reguł miejsca zadań; WAY-107 nie nazywa wyprowadzenia identyfikatora linii jako jedynej części linii, którą daje the way.
- Uwaga #102-6, którą przegląd dołączył do P6: `project-level/task_line.md` mówi „Where the rules give none of the three forms, ask the human once” (akapit otwierający plik), a lista spraw linii w tym samym akapicie ma ich więcej niż trzy, więc „three” nie wskazuje niczego.

### To do

1. W `foundations/part_map.md` pole *Depends on* pozwala na dziesięć zależności z *Need*: `decisions` dostaje `invariants`, `product-guidelines` i `project-level`; `part-map` dostaje `decisions`; `elements-common` dostaje `product-guidelines`; `project-level` dostaje `task-cycle`; `task-cycle` dostaje `foundation-review`; `process-audit` dostaje `gate`; `agent-instructions` dostaje `foundation-review` i `process-audit`.
2. Słownik the way (`foundations/glossary.md`) ma hasło zależności części od części w znaczeniu z pierwszego pytania pod *Questions to settle*.
3. Fundament the way ma cztery niezmienniki z wierszy 2–5 *Settlements to record*, każdy z testem (*Method* `test`), który pada, gdy strona czytająca i strona pisząca przestaną się zgadzać.
4. WAY-107 (`foundations/decisions.md`, „Where does a product tell the project level where its backlog stands?”) mówi, że the way daje wyłącznie wyprowadzenie identyfikatora linii zadania z planu, a resztę linii, także znaki identyfikatora i jego jednoznaczność, dają reguły miejsca zadań; jej *Verification* i *Rationale* zgadzają się z tym zdaniem. WAY-107 zmienia się w miejscu (WAY-07).
5. `project-level/task_line.md` mówi, że gdy reguły miejsca zadań nie przyjmują wyprowadzonego identyfikatora, agent pyta człowieka i nie pisze linii, a zdanie „Where the rules give none of the three forms, ask the human once” (akapit otwierający plik) nazywa to, czego dotyczy, zamiast „three forms”.
6. `project-level/backlog_place.md`, zdanie kończące się „`project-level/task_line.md` says how a line is written by them (WAY-107)”, mówi, kiedy i przez kogo linia jest pisana według tych reguł oraz że the way daje wyprowadzenie identyfikatora, a nie jak linia jest pisana.
7. Zdanie części `project-level` w `foundations/part_map.md` (zaczyna się „The part answers for the form and writing of a project definition”) staje się dwoma zdaniami, mówi, że część odpowiada za to, kiedy linia zadania jest pisana, dostaje zależności i przechodzi do gotowych według reguł miejsca zadań (WAY-107), a nie za to, jak powstaje, i wymienia przewodnik, który czyta agent piszący albo uzupełniający skill wdrożeniowy produktu (`project-level/task/deployment_skill_guide.md`).

### Questions to settle

- Co liczy się jako zależność jednej części od drugiej w polu *Depends on* mapy części: każde sięgnięcie (skill wywołuje skill albo plik innej części, skrypt czyta plik, formę zapisu, ścieżkę albo znacznik git innej części, import Pythona), czy tylko import Pythona?
  - Answer: a — każde sięgnięcie; definicja zapisana w fundamencie.
  - Not chosen:
    - b) tylko import Pythona — P26 odpada, ale *Depends on* części bez Pythona nic nie znaczą, a mapa nie powie nikomu, że audyt czyta ścieżkę `gate/run_tests.py`.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15, odpowiedź „1 a (zależność = każde sięgnięcie; zapisz definicję)”.
- P26. Przy każdej z dziesięciu zależności siedmiu części: (a) dozwolić — *Depends on* się zmienia, bo ta część ma od tamtej zależeć; (b) przyjąć, jak stoi — niezmiennik „the part X does not depend on Y” z `Violated: yes`; czy (c) zmienić kod, żeby nie sięgał tamtej części?
  - Answer: a dla wszystkich dziesięciu — przy każdej potrzeba wynika z opisu części albo decyzji, nie z tego, że kod już sięga: `decisions`→`invariants` (decyzja nazywa niezmienniki, które z niej wynikają), `decisions`→`product-guidelines` (reguła pisania kodu idzie do wytycznych), `decisions`→`project-level` (decyzja technologii powstaje w kroku poziomu projektu), `part-map`→`decisions` (wpis mapy bywa sprzeczny z decyzją), `elements-common`→`product-guidelines` (zdanie części: „the references of a product's guidelines included”), `project-level`→`task-cycle` (zdanie części: „its reader of task-cycle evidence”), `task-cycle`→`foundation-review` (WAY-300 liczy od ostatniego przeglądu), `process-audit`→`gate` (WAY-339: zmiana programu bramki przerywa porównywalność czasów), `agent-instructions`→`foundation-review` i `process-audit` (zdanie części: punkty wejścia skilli the way).
  - Not chosen:
    - b) niezmiennik z `Violated: yes` — dziesięć nowych testów szukających napisów, które padają na zawsze, i niezmienniki opisujące cel, którego nikt nie chce (punkt wejścia musi wskazywać skill).
    - c) zmienić kod — najdroższe i przy każdej pozycji odbiera funkcję (np. kontrola fundamentu przestałaby sprawdzać wytyczne).
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15, odpowiedź „2 a dla wszystkich dziesięciu — przy każdej potrzeba wynika z opisu części albo decyzji, nie z tego, że kod już sięga (WAY-225 spełnione)”.
- Czy cztery zależności od formy cudzego pliku dostają test, który pada, gdy część docelowa zmieni to, co czyta część zależna?
  - Answer: a — cztery testy formy, każdy z niezmiennikiem, który trzyma.
  - Not chosen:
    - b) bez testów — zepsucie formy łapie tylko krok powrotu, gdy ktoś o nim pomyśli; trzy z czterech przeszłyby po cichu.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15, odpowiedź „3 a — cztery testy formy; trzy zepsucia przeszłyby po cichu”.
- P6. Zmienić WAY-107 tak, by nazwała wyprowadzenie identyfikatora jako jedyną część linii, którą daje the way, czy przywrócić krótką decyzję ze zdaniem WAY-329 i relacją „narrows WAY-107”?
  - Answer: a — zmienić WAY-107, z dopiskiem: gdy reguły miejsca zadań nie przyjmują wyprowadzonego identyfikatora (np. zabraniają myślników), agent pyta człowieka i nie pisze linii.
  - Not chosen:
    - b) przywrócić krótką decyzję ze zdaniem WAY-329 i „narrows WAY-107” — idzie wbrew regule WAY-293, którą #126 zastosował do tej samej decyzji; następny przegląd dziennika może ją wycofać drugi raz.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15, odpowiedź „4 a — zmiana WAY-107 przyjęta, z dopiskiem o reakcji, gdy reguły miejsca nie przyjmują wyprowadzonego identyfikatora (agent pyta człowieka, nie pisze linii)”.
- Kto przeredagowuje zdanie części `project-level` w mapie: to zadanie w całości (także o przewodniku wdrożeniowym), czy każde z dwóch zadań swój kawałek?
  - Answer: a — to zadanie przepisuje całe zdanie; punkt 4 *To do* zadania „the way: drobne poprawki po PR-ach #117–#121” przeszedł tutaj.
  - Not chosen:
    - b) każde zadanie swój kawałek — dwa cykle edytują to samo zdanie, drugi trafia na konflikt przy scalaniu albo przepisuje zdanie bez wiedzy o pierwszym.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15, odpowiedź „5 a — to zadanie przepisuje całe zdanie project-level”.

## Context

- Plik danych przeglądu: `the data file of the foundation review of 2026-11-14 in the author's notes` — sekcja „Fundament” → „Propozycje”, P26 i P6.
- Sprawdzony commit przeglądu: `21ecb627f885de438e2209d7ff5c137b1e1b9d83` (gałąź `foundations`); numery linii w pliku danych odnoszą się do niego.
- Reguła szablonu mapy części o zależności, której *Depends on* nie pozwala: `elements/part-map/template.md`, akapit zaczynający się od „A dependency the code holds that *Depends on* does not allow goes to the human”.
- Pozycja 23 listy drobnych poprawek brzmienia z przeglądu (rozdzielić zdanie z pięcioma „and for”) idzie tu razem z P6 (*To do* 7).
- Dowody P26 sprawdzone na `21ecb62` przy doprecyzowaniu (2026-11-15): wszystkie dziesięć sięgnięć stoi w kodzie; żadne nie jest importem Pythona, więc test niezmiennika `cross-part-imports` żadnego nie widzi.
- Miejsca sięgnięć: `elements/decisions/skill/SKILL.md` („through `record-invariant`”), `elements/decisions/skill/decide_entry.md` (`product-guidelines/template.md`), `elements/decisions/skill/projected.md` (`settle-technology`), `elements/part-map/skill/write.md` („goes through `record-decision`”), `.claude/skills/the-way-review-foundation/SKILL.md` i `.claude/skills/the-way-audit-process/SKILL.md` z bliźniakami w `.agents/skills/`.
- Części bez plików Pythona mają już w *Depends on* części, do których sięgają tylko tekstem skilli — np. `foundation-review` (same pliki `.md`) wymienia siedem części; odpowiedź na pierwsze pytanie zapisuje tę praktykę.
- Po *To do* 1 test `cross-part-imports` przepuszcza też importy Pythona z `project-level` do `task-cycle` i z `process-audit` do `gate`; `project-level` i `task-cycle` zależą od siebie nawzajem, jak już `decisions` i `elements-common`.
- Strony czytające i piszące czterech zależności od formy: `project-level/plan_state.py` rozpoznaje linię `- Request URL and status: blocked draft, opened on this commit`, którą piszą `task-cycle/skill/reserved_return.md` i `task-cycle/skill/blocked_finding.md`; `process-audit/audit_count.py` czyta historię ścieżki `gate/run_tests.py` (`GATE_TEST_RUNNER`); `task-cycle/review_reminder.py` liczy od znacznika `foundation-review/*` (`TAG_PATTERN`), który nadaje `foundation-review/SKILL.md` („Name the tag `foundation-review/YYYY-MM-DD`”); `elements/common/foundation_check.py` sprawdza pliki `guidelines/*.md` (`GUIDELINES`), których miejsce podaje `product-guidelines/template.md`.
- Dziś żaden test nie porównuje strony czytającej ze stroną piszącą: `project-level/test_plan_state.py` trzyma własną kopię linii zablokowanej prośby, a testy w `process-audit/test_audit_count.py` budują sztuczne repozytorium.
- WAY-329 wycofał PR #126 (commit `e643371`, „Withdraw the decisions whose rule stands in a skill or a template”), nie poprawiając WAY-107, którą WAY-329 zawężała; stąd linia `Defect introduced by`.
- Brakujące zależności P26 nie są w linii `Defect introduced by`: zmiany, które je wprowadziły (m.in. #52, #80, #94, #100, #113, #120), nie łamały wymogu znanego przy scaleniu, bo słowo „zależność” nie miało określenia aż do tego zadania — to luka, nie defekt (WAY-355).
- Zdanie mapy „how the line of a task in the product's backlog is made” weszło w #102 (commit `06144e9`); recenzent #102 ocenił je jako nieszkodliwe do przeredagowania przy następnej okazji (uwaga #102-5), więc to nie defekt znaleziony po scaleniu.

## Questions carried to cycle

- Brzmienie hasła słownika o zależności części, czterech niezmienników, zmienionego zdania WAY-107 z jej *Verification* i *Rationale* oraz dwóch zdań części `project-level` w mapie.
- Jak każdy z czterech testów znajduje stronę piszącą (dosłowny tekst w pliku, ścieżka śledzona przez git, wzorzec znacznika) i do której części należy.

## Human actions

none

## Decisions in play

- WAY-225 — What in a product's foundation is derived rather than written by hand?: „a dependency the code holds that the part map does not allow is recorded as an invariant the product does not meet (WAY-51), never by rewriting the allowed dependencies to fit the code.” Bez zmiany; *To do* 1 dopisuje zależności, bo Mariusz uznał każdą za chcianą regułę (drugie pytanie), nie dlatego, że kod już sięga.
- WAY-51 — What does the main branch hold where the product does not meet an invariant?: „an invariant is marked violated only by a change of the foundation that a human accepts, never by a step of implementation.” Bez zmiany; żaden niezmiennik nie dostaje `Violated: yes`.
- WAY-11 — How does a task end?: „an agent compares with the code […] the part map of the parts the task touched, and corrects in the same change whatever no longer matches.” Bez zmiany; hasło słownika z *To do* 2 mówi krokowi powrotu, co porównuje.
- WAY-44 — What assigns a file to a part?: „Verification: invariants: cross-part-imports” — niezmiennik importów między częściami wynika z tej decyzji. Bez zmiany; po *To do* 1 przepuszcza importy w nowo dozwolonych kierunkach.
- WAY-95 — Which words take a glossary entry?: „A word takes a glossary entry when it means, in the product, something other than a reader who knows the product's field takes it to mean”. Bez zmiany; „zależność” w znaczeniu każdego sięgnięcia, nie tylko importu, jest takim słowem (*To do* 2).
- WAY-107 — Where does a product tell the project level where its backlog stands?: „How a task's line is handled — the status of a new line, its move to ready, the form of its dependencies and of its identifier, how a line is found and kept one to a task, which fields an agent may change, the agreement of the lines at both ends of a dependency, a clash of identifiers — is taken from the rules of the task place itself, never from text written at the product or in the-way's skills”. Zadanie zmienia to zdanie: the way daje wyłącznie wyprowadzenie identyfikatora linii zadania z planu, a reguły miejsca — resztę, także znaki identyfikatora i jego jednoznaczność; wybór drogi „4 a” to zgoda na zmianę (WAY-314).
- WAY-293 — What prevails where a task or its spec excludes the entry for a choice?: „In the log of the-way, a rule that stands in one skill or template of the-way stands there with one sentence of its reason. It is an entry of the log only where it carries a choice with a real cost”. Bez zmiany; dlatego wyprowadzenie identyfikatora zostaje w `project-level/task_line.md`, a WAY-329 nie wraca.
- WAY-300 — When does a request tell the human that the foundation waits for a review?: „At the end of every task cycle the orchestrator counts the merges to the main branch since the last review tag”. Bez zmiany; z niej wynika zależność `task-cycle`→`foundation-review` i trzeci niezmiennik.
- WAY-339 — When do the measures of the audit stop being comparable?: „for the times of the gate, also with a change of the test runner of the process”. Bez zmiany; z niej wynika zależność `process-audit`→`gate` i drugi niezmiennik.

## Settlements to record

Candidates: 7 shown, 7 accepted — 2026-11-15

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Zależność części od innej części to każde sięgnięcie do tamtej części: skill wywołuje skill albo plik tamtej części, skrypt czyta jej plik, formę zapisu, ścieżkę albo znacznik git, albo kod ją importuje. | glossary term | pytanie „Co liczy się jako zależność jednej części od drugiej…” (wybór człowieka; droga niewybrana pod pytaniem) | czy dopisać do *Depends on* tylko części, które kod importuje, i czy w ogóle pisać definicję |
| 2 | Linia zablokowanej prośby, którą rozpoznaje `project-level/plan_state.py`, stoi dosłownie w plikach `task-cycle`, które ją piszą. | invariant | pytanie „Czy cztery zależności od formy cudzego pliku dostają test…” (wybór człowieka; droga niewybrana pod pytaniem) | czy pilnować tej formy testem, czy zostawić ją krokowi powrotu |
| 3 | Ścieżka programu bramki, której historię czyta `process-audit/audit_count.py`, jest plikiem, który git śledzi. | invariant | jak wiersz 2 | jak wiersz 2 |
| 4 | Znacznik, który nadaje skill przeglądu fundamentu, pasuje do wzorca, od którego `task-cycle/review_reminder.py` liczy scalenia. | invariant | jak wiersz 2 | jak wiersz 2 |
| 5 | Miejsce plików wytycznych, które sprawdza `elements/common/foundation_check.py`, zgadza się z miejscem wytycznych, które podaje `product-guidelines/template.md`. | invariant | jak wiersz 2 | jak wiersz 2 |
| 6 | The way daje wyłącznie wyprowadzenie identyfikatora linii zadania z planu, żeby doprecyzowanie mogło wpisać zależność, zanim druga linia istnieje; resztę linii, także znaki identyfikatora i jego jednoznaczność, dają reguły miejsca zadań. | sentence of WAY-107 | pytanie „P6. Zmienić WAY-107…” (wybór człowieka; droga niewybrana pod pytaniem) | czy przywrócić WAY-329 jako osobną decyzję, czy zostawić WAY-107 sprzeczną z `task_line.md` |
| 7 | Gdy reguły miejsca zadań nie przyjmują wyprowadzonego identyfikatora, agent pyta człowieka i nie pisze linii. | skill or instruction file: project-level/task_line.md | pytanie „P6. Zmienić WAY-107…”, dopisek w odpowiedzi (wybór człowieka) | czy pisać linię z identyfikatorem wbrew regułom miejsca, przerobić identyfikator po swojemu, czy pytać |

## Out of scope

none

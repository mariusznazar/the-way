---
title: "the way: przy prowadzeniu projektu każde zadanie ma dostawać linię w backlogu produktu z właściwym statusem"
status: draft
created: 2026-11-11T18:00
updated: 2026-11-11
tags: [zadanie]
related: "the project's note in the author's private notes"
---

# the way: przy prowadzeniu projektu każde zadanie ma dostawać linię w backlogu produktu z właściwym statusem

Status: ready for cycle
Project relation: independent

## Description

### Need

- Gdy the way prowadzi plan projektu (skill `lead-project`), zadanie doprecyzowane w rundzie nie dostaje linii w backlogu produktu ani przy założeniu dokumentu, ani przy akceptacji.
- Refiner, czyli agent, którego `lead-project` wysyła do doprecyzowania jednego zadania, ma zakaz pisania poza dokumentem zadania i swoją turą w pliku rozmowy (`project-level/task/skill/orchestrated_mode.md:36` na `52f8164`).
- Orkiestrator, czyli agent prowadzący rundę w rozmowie z Mariuszem, przy akceptacji zmienia tylko `Status:` dokumentu, wiersz planu i dziennik zmian planu (`project-level/lead/skill/SKILL.md:165-168` na `52f8164`).
- W trybie ręcznym `refine-task` robi oba kroki sam: zakłada wpis w backlogu i linkuje z niego dokument (`project-level/task/skill/read_sources.md:17-21`), a po akceptacji aktualizuje wpis tak, jak mówi sekcja `## Backlog` w `AGENTS.md` produktu (`project-level/task/skill/final_review.md:26-28`).
- Odczuwa to Mariusz: wybiera z widoku zadań agentowych w vaulcie, co puścić do cyklu, a zadań gotowych z rundy tam nie widzi; sprawdzanie zgodności notatek z liniami zgłasza je jako notatki bez linii.
- Bez zmiany każda runda kończy się ręcznym dopisywaniem linii, tak jak 2026-11-11 dla zadań 16–20, 23 i 24 planu MVP2 w loop2.

### To do

1. Zasada zapisu refinera w trybie orkiestrowanym mówi, przed czym chroni, zamiast zakazywać wszystkiego poza dokumentem zadania (pytanie 1):
    - refiner pisze to, o co prosi go zlecenie orkiestratora;
    - żaden agent poza orkiestratorem po słowie człowieka nie robi kroku, który należy do akceptacji: przestawienia linii na gotową ani `Status: ready for cycle`;
    - plan, definicja i fundament zostają poza refinerem, jak dziś.
2. Refiner zadania, które nie ma jeszcze linii w backlogu produktu, zakłada ją w turze, w której pierwszy raz tworzy dokument zadania, także gdy refinerzy rundy pracują równolegle (pytanie 2): z linkiem do dokumentu zadania i ze statusem zadania w doprecyzowaniu, w formie, którą dają zasady miejsca zadań (pytanie 3).
3. Orkiestrator przy akceptacji dokumentu, razem ze `Status:` i wierszem planu, przestawia linię zadania na gotową tak, jak mówią zasady miejsca zadań (pytanie 3).
4. Linia zadania z planu dostaje jego zależności z kolumny *Depends on*, w formie, którą dają zasady miejsca zadań (pytanie 4):
    - refiner wpisuje je przy zakładaniu linii;
    - orkiestrator poprawia je w liniach, gdy zmienia zależności w planie.
5. Zasady miejsca zadań — status nowej linii, przejście na gotową, forma zależności — the way bierze z zasad, które ma samo miejsce zadań (u Mariusza rulebook vaultu), a nie z treści zapisanej przy produkcie, w obu trybach doprecyzowania (pytania 3 i 5):
    - ścieżka do zasad stoi we wpisie `task-rules` pliku lokalizacji `~/.the-way/locations.json` pod nazwą produktu, obok wpisu `tasks`;
    - sekcja `## Backlog` w `AGENTS.md` produktu wymienia tylko nazwę tego wpisu, tak jak dziś wpisu `tasks`;
    - gdy wpisu albo pliku, który wskazuje, brakuje, agent pyta raz człowieka i proponuje dopisanie wpisu, jak przy brakującym miejscu zadań.
6. Sekcja `## Backlog` w `AGENTS.md` the way wymienia wpis z zasadami miejsca zadań zamiast dzisiejszego zdania o przestawianiu linii na Ready, które powtarza rulebook.

### Questions to settle

- Pytanie 1: kto zakłada linię zadania w backlogu przy prowadzeniu projektu i jak ma brzmieć zasada zapisu refinera?
  - Answer: refiner robi to, o co prosi zlecenie orkiestratora, a żaden agent nie robi kroku, który należy do akceptacji człowieka. Linię ze statusem „do doprecyzowania” zakłada refiner tego zadania w turze, w której pierwszy raz tworzy dokument. Przestawienie linii na gotową zostaje u orkiestratora, bo idzie po słowie człowieka. Kolejność zapisów do wspólnego pliku, którą ta droga pierwotnie zakładała, Mariusz zdjął w pytaniu 2.
  - Not chosen:
    - orkiestrator przejmuje cały backlog i zasada zostaje bez zmian — „refiner nie robi rzeczy, którą umiałby zrobić, a orkiestrator dostaje kolejny obowiązek, o którym musi pamiętać”;
    - zakładanie linii przez refinera bez kolejności, za to jedną operacją dopisania na koniec pliku i sprawdzeniem — „wymóg techniczny, którego przestrzeganie trzeba pilnować w każdym zleceniu. Zmniejsza ryzyko kolizji, ale go nie usuwa, bo Obsidian albo synchronizacja vaulta też mogą w tej chwili pisać do pliku”;
    - bez poprawki — „każda następna runda zostawi zadania bez linii, a Ty albo ja będziemy to łatać ręcznie”.
  - Source: Mariusz, 2026-11-11, sesja loop2 `744c5db8`: „chyba przstaję być przekonany do zasady, że refiner może cokolwiek pisać poza dokumentem zadania jeśli zostanie o to poproszony to czemu ma tego nie robić”, a potem „B” na pytanie „Odkładamy z B, czy wolisz A albo C?”; koszt wybranej drogi podany w pytaniu: „zasada przestaje być prosta do sprawdzenia („tylko dokument”) i zaczyna zależeć od tego, jak orkiestrator ułoży zlecenia. Gdy się pomyli, linia ginie po cichu”.
- Pytanie 2: czy orkiestrator ma rozkładać zapisy linii w czasie, gdy runda ma wielu refinerów?
  - Answer: nie; refinerzy rundy zakładają swoje linie równolegle, w pierwszej turze, a ryzyko, że dwa zapisy w tej samej chwili zgubią linię, zostaje przyjęte.
  - Not chosen:
    - pierwsze tury refinerów jedna po drugiej — „pierwsza tura rundy trwa tyle, ile wszystkie razem: przy 7 zadaniach kilka razy dłużej niż dziś”;
    - pierwsze tury równolegle, potem orkiestrator po kolei wznawia każdego refinera z krótką prośbą o linię — kilka krótkich wznowień, nowy refiner czytający cały skill, gdy sesja przerwie się po drodze, i wyjątek w WAY-154 od nowego refinera na każdą turę;
    - jak poprzednio, ale zawsze nowy refiner — „najdroższa droga w tokenach”.
  - Source: Mariusz, 2026-11-11: „nie rozumiem pytania 2 - prawdopodobieństwo, że dwóch refinerów trafi na dokładnie ten sam moment edycji pliku jest tak małe, że bym to olał”.
- Pytanie 3: skąd agent bierze status nowej linii i jej przejście na gotową, gdy sekcja `## Backlog` produktu ich nie podaje, i czy ta sama reguła obowiązuje w trybie ręcznym?
  - Answer: z zasad, które ma samo miejsce zadań — u Mariusza z rulebooka vaultu, sekcja „Zadania agentowe” — a nie z treści zapisanej przy produkcie; reguła obowiązuje w obu trybach.
  - Not chosen:
    - status zapisany w sekcji `## Backlog` produktu, a gdy go brak, pytanie i propozycja dopisania do sekcji — Mariusz: „a nie żeby były zapisane gdzieś przy produkcie”;
    - linia w domyślnym stanie narzędzia (w Tasks `[ ]`) — „w vaulcie status jest od razu zły, a sprawdzanie zgodności zgłasza rozjazd”;
    - `[?]` wpisane na stałe w skille the way — „to łamie zasadę, że the way nie zakłada konkretnego narzędzia do backlogu (WAY-101)”.
  - Source: Mariusz, 2026-11-11: „tak, powinna dostać, ale takie wytyczne, powinny być po prostu brane z playbooka obsidianowego w kontekście zadań, a nie żeby były zapisane gdzieś przy produkcie” — w odpowiedzi na pytania 3 i 4 tej rozmowy.
- Pytanie 4: czy linia zadania dostaje zależności z planu i kto je utrzymuje, gdy plan się zmieni?
  - Answer: tak, w tym zadaniu; refiner wpisuje je z kolumny *Depends on* przy zakładaniu linii, orkiestrator poprawia je, gdy zmienia zależności w planie, a ich forma pochodzi z zasad miejsca zadań (u Mariusza pola `🆔` i `⛔` z rulebooka vaultu).
  - Not chosen:
    - osobne zadanie — „to jeszcze jeden pełny cykl, a do tego czasu dopisujesz zależności ręcznie”;
    - wcale — „kolejność czytasz z planu, a widok zadań agentowych nie pokazuje, które zadanie na co czeka”.
  - Source: Mariusz, 2026-11-11: „tak, powinna dostać, ale takie wytyczne, powinny być po prostu brane z playbooka obsidianowego w kontekście zadań, a nie żeby były zapisane gdzieś przy produkcie”; koszt wybranej drogi podany w pytaniu: „druga kopia zależności, którą trzeba utrzymywać zgodną z planem”, którą WAY-144 nazywa „a copy that drifts as soon as one dependency changes”.
- Pytanie 5: jak the way, który nie zakłada konkretnego narzędzia do backlogu, trafia do zasad miejsca zadań, nie trzymając ich treści przy produkcie?
  - Answer: przez wpis w pliku lokalizacji `~/.the-way/locations.json`, osobno pod nazwą każdego produktu, ze ścieżką do zasad; sekcja `## Backlog` w `AGENTS.md` produktu wymienia tylko nazwę wpisu.
  - Not chosen:
    - jeden wpis w pliku lokalizacji wspólny dla wszystkich produktów — trzeba zmienić WAY-320, według której plik ma tylko klucze z nazwami repozytoriów, a produkt, którego zadania leżą gdzie indziej, po cichu dostałby zasady Obsidiana;
    - bez wskazania, agent trafia do rulebooka przez globalne instrukcje Mariusza — nie zadziała w sesji, która ich nie ładuje, np. w chmurze, i stoi w sprzeczności ze zdaniem Mariusza przy WAY-320: „global instructions are probably not the place for such things”.
  - Source: Mariusz, 2026-11-11: „pytanie 5 A”; koszt wybranej drogi podany w pytaniu: „ta sama ścieżka powtórzona w Twoim pliku przy każdym produkcie (dziś przy dwóch)”.

## Context

- W rundzie z 2026-11-11 w loop2 siedmiu refinerów założyło dokumenty w ciągu czterech minut (9:55–9:59).
- Linię zgubioną przy równoległym zapisie widać: sprawdzanie zgodności w vaulcie zgłasza notatkę zadania agentowego bez linii.
- Sekcja `## Backlog` w `AGENTS.md` the way i w `AGENTS.md` loop2 mówi dziś tylko o przestawieniu linii na Ready, `[/]`, i zdjęciu daty, gdy dokument pierwszy raz dochodzi do `ready for cycle`; o statusie nowej linii nie mówi żadna.
- W vaulcie Mariusza `refining` i `waiting for human` odpowiadają `[?]` To Refine, a `ready for cycle` — `[/]` Ready (rulebook vaultu, sekcja „Zadania agentowe”); zadanie zapisane przez `/park` stoi w `[>]` z datą, a agent nie poprawia tego statusu w trakcie doprecyzowania.
- Wzór linii z zależnościami: linie zadań MVP2 16–20, 23 i 24 w backlogu loop2, dopisane ręcznie 2026-11-11 z kolumny *Depends on* planu, np. `🆔 mvp2-18 ⛔ mvp2-16,mvp2-17` (pola zależności wtyczki Tasks).
- Rulebook vaultu już opisuje formę `🆔` i `⛔` (sekcja „Format linii zadania”: miejsce w linii, format identyfikatora, „Zależności od zadania już zrobionego się nie wpisuje”) i statusy zadań agentowych (sekcja „Zadania agentowe”).
- Sekcja `## Backlog` w `AGENTS.md` loop2 trzyma dziś bezwzględną ścieżkę do rulebooka; to sprawa repozytorium loop2, poza tym zadaniem.
- Pliki, których zmiana dotyczy: `project-level/task/skill/orchestrated_mode.md`, `project-level/lead/skill/SKILL.md` (krok 3.1 „Permit one writer per file”, krok 4) i `project-level/lead/conversation_template.md` (sekcja „Ownership and turns”, która opisuje podział zapisów).
- Podobne zakazy pisania poza własnym plikiem mają agent odpowiadający rundy (`project-level/lead/answering.md:11`) i agent zmieniający definicję na zlecenie `lead-project` (`project-level/skill/delegated_mode.md:8`); zadanie ich nie dotyczy, bo luka leży tylko u refinera.
- Źródło zadania: sesja loop2 `744c5db8` z 2026-11-11 (zapis lokalny, wygasa około 2026-12-11).

## Questions carried to cycle

- Jak refiner wyprowadza identyfikator `🆔` zadania, żeby refiner zadania zależnego mógł wpisać go w `⛔`, zanim linia tamtego zadania powstanie; rulebook vaultu wymaga, żeby identyfikator był z małych liter, cyfr i `-` oraz jednoznaczny w całym vaulcie, a nazwa zadania w planie (WAY-147) jest jednoznaczna tylko w planie.

## Human actions

- Dopisać w pliku lokalizacji `~/.the-way/locations.json`, pod `the-way`, wpis `task-rules` ze ścieżką do rulebooka vaultu; sekcja `## Backlog` w `AGENTS.md` the way wymienia go pod tą nazwą — before the cycle, done (2026-11-11, wpis dopisany przez agenta na zgodę Mariusza: „może być teraz”)

## Decisions in play

- WAY-154 — „Project refinement resumes from the plan, task documents and one ignored conversation file per task at `.runs/project-refinement/<task-name>.md`, through which fresh parallel refiners, the answering agent and the project orchestrator take serialized turns on each file; the project orchestrator hands agents only its path and routing, never relays its contents, and each refiner ends its turn as `questions`, `waits for task <n>`, `ready for approval`, `plan change` or `obstacle`. Only a refiner changes the task document's body and transfers settled answers with their sources and the ways the human did not choose (WAY-134) into Questions to settle; the project orchestrator records human answers in conversations, owns ordinary plan updates and their log, and changes only the task document's Status line after the human has accepted that complete document, one document at a time. […]” (`foundations/decisions.md:4411` na `52f8164`) — zadanie zmienia tę decyzję (pytania 1 i 2): refiner pisze też to, o co prosi go zlecenie orkiestratora, w tym linię zadania w backlogu w swojej pierwszej turze, równolegle z innymi refinerami; orkiestrator przy akceptacji, poza `Status:`, przestawia tę linię na gotową.
- WAY-107 — „A product names where it keeps projects and tasks in a `## Backlog` section of its root `AGENTS.md`, outside the block the-way's installer owns. […] when the place is unnamed, or the file or the entry it names is missing, the agent asks the human and offers to record the answer where it fits: the entry in the file for a place on the user's disk, the section otherwise.” (`foundations/decisions.md:2434` na `52f8164`) — zadanie zmienia tę decyzję (pytania 3 i 5): sekcja `## Backlog` wymienia też wpis pliku lokalizacji z zasadami miejsca zadań, a gdy go brak, agent pyta i proponuje dopisanie wpisu.
- WAY-144 — „[…] The plan holds no field naming the tasks a task can be worked on beside, and its order of cycle starts follows the dependencies.” (`foundations/decisions.md:4021` na `52f8164`); uzasadnienie: „a second field derived from them is a copy that drifts as soon as one dependency changes” — zadanie jej nie zmienia, bo plan nie dostaje nowego pola, ale zależności w liniach backlogu są właśnie taką kopią; jej koszt przyjął Mariusz w pytaniu 4.
- WAY-320 — „A user's places on their own disk that lie outside every repository, such as the place of a product's tasks and the place of its projects, are kept in one file, `~/.the-way/locations.json`, […] a JSON object whose keys are repository names, each holding entries by name, such as `tasks` and `projects`, whose values are paths on the user's disk. No file the repository tracks holds an absolute path, or a note link in a Markdown file, […]” (`foundations/decisions.md:10413` na `52f8164`); w odrzuconych drogach: „the place described in words in `## Backlog`, with the path in the user's global instructions — "global instructions are probably not the place for such things"” — zadanie dokłada wpis `task-rules` obok `tasks` i `projects`, czego zdanie „entries by name, such as `tasks` and `projects`” nie zamyka.
- WAY-328 — „The-way departs, for its own code and its own tests, from the general coding guidelines and from the testing guidelines of a product, under WAY-217: in each part named in *Scope*, neither is missing, so a task of the-way that writes code, or writes or changes a test, in such a part waits for neither.” (`foundations/decisions.md:10775` na `52f8164`) — zadanie zmienia skille w części `project-level`, którą ta decyzja obejmuje; zmiany w niej nie robi.

## Settlements to record

Candidates: 6 shown, 5 accepted — 2026-11-11

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Refiner w trybie orkiestrowanym pisze to, o co prosi go zlecenie orkiestratora, a żaden agent poza orkiestratorem po słowie człowieka nie robi kroku, który należy do akceptacji (linia na gotową, `ready for cycle`); plan, definicja i fundament zostają poza refinerem. | decision | pytanie 1 (zmienia WAY-154) | czy refiner może pisać poza dokumentem zadania i plikiem rozmowy, i co mu zostaje zakazane |
| 2 | Refiner zadania bez linii w backlogu zakłada ją ze statusem zadania w doprecyzowaniu w turze, w której pierwszy raz tworzy dokument, równolegle z innymi refinerami rundy, bez kolejki zapisów; orkiestrator przy akceptacji przestawia ją na gotową razem ze `Status:` i wierszem planu. | decision | pytania 1 i 2 (zmienia WAY-154) | kto i kiedy zakłada linię, czy zapisy do backlogu idą po kolei, kto przestawia linię na gotową |
| 3 | Status nowej linii, jej przejście na gotową i forma zależności pochodzą z zasad samego miejsca zadań, nie z treści zapisanej przy produkcie, w doprecyzowaniu ręcznym i orkiestrowanym. | decision | pytanie 3 (zmienia WAY-107) | czy zasady linii wpisać do `AGENTS.md` produktu, w skille the way, czy brać z narzędzia |
| 4 | Ścieżka do zasad miejsca zadań stoi we wpisie `task-rules` pliku lokalizacji pod nazwą produktu, sekcja `## Backlog` wymienia tylko nazwę wpisu, a gdy wpisu brak, agent pyta raz i proponuje jego dopisanie. | decision | pytanie 5 (zmienia WAY-107) | jak agent znajduje zasady: wpis per produkt, wpis wspólny czy globalne instrukcje |
| 5 | Linia zadania z planu dostaje jego zależności z kolumny *Depends on* w formie z zasad miejsca zadań; refiner wpisuje je przy zakładaniu linii, a orkiestrator poprawia, gdy zmienia zależności w planie — koszt kopii zależności poza planem przyjęty. | decision | pytanie 4 | czy linia niesie zależności i kto je utrzymuje po zmianie planu |

## Out of scope

- Zmiana linii zadania, gdy zadanie przechodzi w planie do `in cycle` albo `done`: te statusy ustawia Mariusz, a cykl dopisuje do linii tylko link do requestu.

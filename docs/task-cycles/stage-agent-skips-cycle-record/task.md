---
title: "the way: agent cyklu nie czyta dziennika orkiestratora ani cudzych plików cyklu, których zlecenie nie wskazuje"
status: draft
created: 2026-10-25T13:00
updated: 2026-11-14
tags: [the-way, zadanie]
related: "the author's project note on the process of work on a product"
---

## Po co to

- **Jak jest dziś:** Agent sprawdzający zmianę może przeczytać wcześniejsze rozważania agenta prowadzącego pracę i zasugerować się nimi zamiast ocenić zmianę samodzielnie. W jednym z trzech przejrzanych przebiegów pracy recenzent sięgnął do takich zapisków; potem prowadzący ręcznie dopisywał zakaz do kolejnych wiadomości.
- **Kto to odczuwa:** Agent prowadzący pracę musi pamiętać o dopisywaniu ograniczenia każdemu kolejnemu agentowi. Mariusz otrzymuje recenzję, której niezależność zależy od tego dodatkowego przypomnienia.
- **Co jeśli nic:** Przeczytanie zapisków już wystąpiło przy zmianie dotyczącej ogniska i jedzenia w grze loop2, ale nie stwierdzono szkody ani błędnej oceny z tego powodu. Bez zmiany ręczne przypomnienia pozostają potrzebne, a po ich pominięciu kolejny recenzent może poznać cudzy tok rozumowania przed wydaniem własnej oceny.


# the way: agent cyklu nie czyta dziennika orkiestratora ani cudzych plików cyklu, których zlecenie nie wskazuje

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Orkiestrator cyklu the way prowadzi dziennik cyklu (`cycle.md`): swoje odpowiedzi na pytania agentów, wybory i przebieg; obok, w katalogu `reports/`, leżą zlecenia i raporty wszystkich agentów cyklu.
- Recenzje w cyklu mają być niezależne: recenzent ocenia zmianę na podstawie tego, co dostał w zleceniu, a nie toku rozumowania orkiestratora ani innych agentów.
- Zakaz czytania dziennika stoi dziś tylko w skillu orkiestratora („You alone read `cycle.md`”), którego agent etapu nie czyta; skille etapów pozwalają sięgać poza zlecenie po fragment źródła, decyzję, niezmiennik albo wytyczne i o dzienniku ani o plikach innych agentów nie mówią nic.
- W cyklu `ognisko-i-jedzenie` gry loop2 (PR #25) recenzent specu przeczytał dziennik, żeby sprawdzić, czy orkiestrator rozstrzygnął już pięć punktów projektanta, i sam zgłosił to jako sięgnięcie poza zlecenie; szkody nie stwierdzono.
- Od tamtej chwili orkiestrator dopisywał zakaz ręcznie do wiadomości do agentów, więc ochrona niezależności zależy od tego, czy orkiestrator o niej pamięta.

### To do

1. Lista tego, co niesie każde zlecenie w `task-cycle/skill/SKILL.md` — zdanie otwierane „The handoff gives the user's delegation”, kończące się „and the report path.” (około wiersza 179) — ma po sobie zdanie, które każe orkiestratorowi powiedzieć to agentowi w zleceniu, w brzmieniu: „It tells the agent that `cycle.md` and the other files of the cycle's record directory — other agents' handoffs, reports and findings — are not its to read unless its handoff names them.”
2. Decyzja WAY-148 w `foundations/decisions.md` zmienia się tak, jak podaje *Decisions in play*.

### Questions to settle

- 1. Gdzie stoi zdanie, które agent etapu przeczyta?
  - Answer: (a) na liście tego, co niesie każde zlecenie, w skillu orkiestratora — jedno miejsce, działa w Claude Code i w Codexie.
  - Not chosen:
    - (b) w definicjach typów agentów `the-way-author` i `the-way-stage` — w Codexie i w sesji bez typów zdania nie ma wcale; zmienia sens WAY-368 (definicja typu mówi tylko, czym agent jest) i WAY-370 („the stage reads the same text”), które trzeba by przepisać.
    - (c) w obu miejscach — to samo zdanie w dwóch miejscach do pilnowania i koszt drogi (b).
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „1 a” (odpowiedź na pytanie z drogami (a), (b), (c) i rekomendacją (a)).
- 2. Co obejmuje zakaz?
  - Answer: (b) każdy plik katalogu zapisu bieżącego cyklu, którego zlecenie nie wskazuje — dziennik, cudze zlecenia, raporty i listy znalezisk — w brzmieniu: „It tells the agent that `cycle.md` and the other files of the cycle's record directory — other agents' handoffs, reports and findings — are not its to read unless its handoff names them.”
  - Not chosen:
    - (a) dziennik cyklu i raporty innych agentów (szkic z notatki) — zostają otwarte zlecenia innych agentów, a w nich orkiestrator wpisuje swoje odpowiedzi na ich pytania, czyli ten sam tok rozumowania, który zakaz ma ukryć.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „2 b (Twoje brzmienie zdania)” (odpowiedź na pytanie z drogami (a), (b) i rekomendacją (b)).
- 3. Czy reguła wchodzi do decyzji WAY-148?
  - Answer: (a) tak — cykl rozszerza WAY-148 o zakres z pytania 2 i dopisuje uzasadnienie niezależnością recenzji (przypadek z loop2).
  - Not chosen:
    - (b) zmienia się tylko tekst skilla, fundament zostaje — reguła żyje w jednym zdaniu skilla bez zapisanego powodu i następna przeróbka skilla może ją zgubić.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „3 a” (odpowiedź na pytanie z drogami (a), (b) i rekomendacją (a)).

## Context

- Lista tego, co niesie każde zlecenie: `task-cycle/skill/SKILL.md`, zdanie „The handoff gives the user's delegation, the worktree, the method of the stage by the path of its `SKILL.md` in the pinned the-way, the stage and its boundary, the paths and commits of the frozen task and of the spec and plan where they exist, the answers of step 4, and the report path.” (około wiersza 179, `foundations` @ `6fa755c`).
- Zakaz dla orkiestratora: tamże, akapit otwierany „You decide what each agent reads”, zdanie „You alone read `cycle.md`: an answer or choice that binds an agent goes into its handoff or the message that resumes it.” (około wiersza 225).
- Sięganie poza zlecenie w skillach etapów: akapit otwierany „Where you need something the dispatch does not name” w `task-cycle/spec/SKILL.md` (około wiersza 29), w `task-cycle/plan/SKILL.md` (około wiersza 42) i w `task-cycle/change/SKILL.md` (około wiersza 39), oraz akapit „Beyond what the dispatch names” w `task-cycle/review/SKILL.md` (około wiersza 50).
- Pliki innych agentów, które skill orkiestratora już dziś każe wskazać w zleceniu (`task-cycle/skill/SKILL.md`, `foundations` @ `6fa755c`): recenzentowi raport autora („For a review, it gives the range to review and the author's report”); agentowi poprawki plik znalezisk, a recenzentowi poprawki także raport poprawki („the review of the fix also gets the fix report”); projektantowi specu po porzuconej próbie raport agenta, który trafił na wybór; planiście po zwrocie `returned` raport tej próby; recenzentowi kawałka i recenzentowi całej zmiany raporty wykonawców. Furtka „chyba że zlecenie wskazuje” żadnego z tych przypadków nie odcina.
- Agenci etapów w Claude Code startują jako typy `the-way-author` i `the-way-stage` (`task-cycle/agent-types/`); treść definicji typu jest pierwszym tekstem, który agent dostaje, a kopie w `.claude/agents/` generuje `agent-instructions/agent_type_copies.py`. W Codexie i w sesji bez typów etap startuje bez tej treści (WAY-370).
- Dowód z loop2: `git -C <repozytorium loop2> show 273446f:docs/task-cycles/ognisko-i-jedzenie/reports/02-spec-reviewer-report.md`, wiersz 130: „to see whether the orchestrator had already ruled on the designer's five points (it had not)”.
- Liczba „46 z 54 wywołań z ręcznie dopisanym zakazem” pochodzi od agenta-krytyka i nie jest sprawdzona; zakaz stał w wiadomościach, nie w plikach zleceń. W dwóch innych cyklach po wejściu reguły z `8ccbd6e` nikt dziennika nie czytał.
- Odrzucony przy parkowaniu wariant: to samo zdanie w czterech skillach etapów — działa także wtedy, gdy orkiestrator zapomni, ale to cztery miejsca do utrzymania zamiast jednego.
- Za zadaniem: kurs AI Tech Leaders cytuje badanie, w którym opis autora „to bezpieczna zmiana” obniżał wykrywalność znanych podatności, a usunięcie opisu przed recenzją odzyskało 12 z 17; badanie dotyczy autora, który celowo oszukuje (kandydat K1 w notatce `praktyki_z_kursu_ai_tech_leaders_cz2.md` projektu „Przejście AI Tech Leaders”).
- Przeciw, z zastrzeżeniem: eksperyment recenzji z 12.11.2026 zmierzył, że recenzent bez raportu autora nie łapie więcej (notatka `eksperyment_recenzji.md`, sekcja „Odpowiedź”). Zadanie nie zabiera recenzentowi raportu autora — ten zlecenie nadal wskazuje — więc eksperyment go nie podważa.
- Sprawa AIR-517 w rejestrze ai-review Mariusza.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-148 — How do task-cycle stages pass their work to the orchestrator?: „The handoff names what the agent reads, as the orchestrator selects it (WAY-150, WAY-213), […] and since only the orchestrator reads the cycle record, an answer or choice that binds an agent goes into that agent's handoff or the message that resumes it.” *Verification*, violates: „an agent other than the orchestrator reads the cycle record to learn an answer”. *Rationale*: „The cycle record holds every agent's events; an agent that reads it pays for all of them to learn one answer.”
  - Zmiana, którą robi to zadanie (pytania 2 i 3, droga (a) pytania 3): część wiążąca mówi, że agent etapu nie czyta `cycle.md` ani innych plików katalogu zapisu cyklu — cudzych zleceń, raportów i list znalezisk — których jego zlecenie nie wskazuje, a zlecenie mówi mu to; *Verification* uznaje za naruszenie agenta, który czyta taki plik niewskazany w zleceniu, i zlecenie bez tego zdania; *Rationale* dodaje do kosztu niezależność oceny — agent, który przed własną oceną pozna tok rozumowania orkiestratora albo innego agenta, ocenia pod jego wpływem (recenzent specu w cyklu loop2 `ognisko-i-jedzenie`); *Rejected* zyskuje drogi niewybrane w pytaniach 1, 2 i 3.
- WAY-150 — How do the-way skills choose which product foundation material to read?: „[…] and every other agent of the cycle reads what its handoff names and reaches for what is missing selectively — a search for an identifier or a word and a read of the passage found, never of a whole file of the foundation — naming each such reach in its report.”
- WAY-10 — Who assesses a change to an invariant test or to the foundation?: „an agent that did not make the change reviews the whole change, its foundation entries and invariant tests included, against its task and the foundation”. *Rationale*: „a model judging what it wrote favours it, so an agent that did not make the change reads it.”
- WAY-368 — Which agents run the stages of a task cycle in Claude Code?: „Each type has a body of its own saying what it is”.
- WAY-370 — What does a task cycle do where the session has none of the-way's agent types?: *Rationale*: „A stage dispatched without its type loses only the saving: its handoff already names the method by its file, so the stage reads the same text.”

## Settlements to record

Candidates: 1 shown, 1 accepted — 2026-11-14

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Agent etapu cyklu nie czyta `cycle.md` ani innych plików katalogu zapisu cyklu — cudzych zleceń, raportów i list znalezisk — których jego zlecenie nie wskazuje; mówi mu to zlecenie, a reguła stoi w WAY-148 z uzasadnieniem niezależnością recenzji. | decision | *Questions to settle*, pytania 1 (a), 2 (b) i 3 (a); drogi niewybrane w ich *Not chosen*; wybór doradcy dnia w imieniu Mariusza, 2026-11-14 | czy rozszerzyć WAY-148, czy zmienić tylko tekst skilla; czy zakaz obejmuje cudze zlecenia i listy znalezisk; czy zdanie trafia też do definicji typów agentów |

## Out of scope

none

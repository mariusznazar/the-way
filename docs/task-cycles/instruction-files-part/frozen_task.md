---
title: "the way: pliki instrukcji dla agentów jako nowa część — zasady, mapa wczytywania przez narzędzia, skill maintain-instruction-files i skrypt kontrolny"
status: draft
created: 2026-10-08
updated: 2026-10-08
tags: []
related: "<private notes>/(P) Proces pracy nad produktem"
---

# the way: pliki instrukcji dla agentów jako nowa część — zasady, mapa wczytywania przez narzędzia, skill maintain-instruction-files i skrypt kontrolny

Status: ready for cycle
Project relation: independent

## Description

### Need

- Brakuje zasad, co ma zawierać plik instrukcji dla agentów, kiedy coś do niego dopisać, kiedy usunąć, a kiedy przenieść gdzie indziej.
- Prototyp, który te zasady niesie, powstał poza zadaniem, a cztery jego oceny wykazały luki, które trzeba zamknąć przed wniesieniem do the way.
- Sześć wierszy „przejmuję” z lekcji m1l4 kursu 10xDEVS czeka na wpisy w dzienniku decyzji the way.

### To do

1. Wnieść do the way nową część `instruction-files` z prototypu: `principles.md`, `tool_loading.md`, `skill/SKILL.md`, `check_instructions.py` z testami.
    - wpis części w `foundations/part_map.md`
    - katalog dopisany do listy katalogów w WAY-09 razem z tym, co musi w nim stać, zanim trafi na główną gałąź
2. Zmienić tryb oceny skilla tak, by przy każdej proponowanej zmianie sprawdzał, czy błąd, który ta zmiana ma usunąć, kiedykolwiek wystąpił.
3. Kazać skillowi przed oceną:
    - przeczytać decyzje repo dotyczące jego plików instrukcji (w the way np. WAY-16, WAY-27)
    - przeczytać ustawienia narzędzi, które zmieniają wczytywanie (np. limit rozmiaru w konfiguracji Codexa)
    - ustalić, skąd startują sesje pracujące na repo (np. sesje commitujące w the way startują w vaulcie, gdzie `AGENTS.md` the way się nie ładuje)
4. Poprawić wagi zgłoszeń skryptu kontrolnego:
    - bez `WARN dead-path` dla ścieżki w zdaniu, które mówi, że plik się nie ładuje (przypadek z oceny: `~\.claude\memory\` w globalnym `CLAUDE.md`)
    - bez zgłoszenia skilla bez wskaźnika, gdy narzędzie czyta jego kopię z `.agents/skills` (przypadek z oceny: 11 skilli w `loop2`)
    - naprawdę martwa ścieżka zgłaszana wyżej niż `INFO` (przypadek z oceny: `scripts/locations.json`)
    - sprawdzenie obejmuje też pliki wskazywane z `AGENTS.md` (przypadek z oceny: przewodnik `agent-instructions/README.md` the way)
5. Uzupełnić `tool_loading.md` o to, jak Cursor wczytuje `AGENTS.md` leżący nad katalogiem roboczym (przypadek z oceny: `C:\Storage\AGENTS.md`, dowiązanie do globalnego `CLAUDE.md`).
6. Wpisać do dziennika decyzji the way decyzje dla sześciu wierszy „przejmuję” z m1l4:
    - linia pliku głównego tylko wtedy, gdy spełnia trzy warunki (`principles.md` §2): potrzebna w każdej sesji albo wskazuje drogę do pracy, której inaczej nikt nie znajdzie; agent nie wyczyta jej z repo ani z wiedzy ogólnej; bez niej agent się pomyli — a miejsce reguły wyznacza jej wyzwalacz (§3)
    - plik wzorcowy wskazany ścieżką w backtickach, nigdy `@` (§2, §4)
    - reguła tylko z powtarzalnego błędu: każda ma nazwany błąd, który usuwa, i ten błąd jest potem jej drogą wyjścia (§7)
    - próba reguły w świeżych sesjach to trzy osobne pytania — czy reguła się wczytała, czy agent jej przestrzegał, czy pomogła — każde z inną liczbą sesji (§6)
    - `AGENTS.md` w korzeniu jako wspólny nośnik dla trzech narzędzi, `CLAUDE.md` tylko z dodatkami dla Claude Code i z `@AGENTS.md` w pierwszej linii (§4)
    - to, co musi zajść za każdym razem, idzie do mechanizmu (hook gita, linter, CI, sprawdzenie wyniku kroku), instrukcja tylko uzupełnia (§3, §4)
7. Zapisać jako fakty o otoczeniu, z sondami zbudowanymi z pomiarów prototypu, zachowania narzędzi i wyniki badań, na których stoją decyzje z punktu 6 i `tool_loading.md`.
8. Zmiana, która wchodzi do `foundations` jako druga — ta albo PR #8 (`task/the-way-skills-in-the-way`) — dodaje skillowi wskaźniki `the-way-maintain-instruction-files` w `.claude/skills/` i `.agents/skills/`.
9. Po scaleniu przepiąć junction `C:\Users\Mariusz\.claude\skills\maintain-instruction-files` z `C:\Storage\repos\the-way-instruction-files\instruction-files\skill` na `C:\Storage\repos\the-way\instruction-files\skill`.

### Acceptance criteria

- Nic w `instruction-files/` nie wskazuje na `.runs/` ani na notatki vaultu.

## Context

- Prototyp: gałąź `task/instruction-files`, worktree `C:\Storage\repos\the-way-instruction-files`, commit `af585e3` na `c64a607` (dziś czubek `foundations`), bez pusha.
- Dowody pomiarów leżą w `.runs/instruction-files-prototype/` worktree; opis zawartości w `INDEX.md` tego katalogu.
    - `.runs/` jest ignorowany przez git, a WAY-27 nie pozwala repo wskazywać źródeł, których czytelnik nie otworzy — stąd pomiary wchodzą jako fakty z sondami w `probes/`.
- Research: <private notes>/research_pliki_instrukcji_dla_agentow.
- Kontrola, czy błąd wystąpił, działa dziś tylko przy wstawianiu reguły (`principles.md` §7); w ocenach robiła ją dopiero krytyka, przeszukując zapisy sesji.
- Werdykty i wnioski z ocen: <private notes>/mapa_pakietu_10x, sekcja „m1l4” — tabela (kolumna nośnika „wpis w dzienniku the way… — wiersz otwarty”) i Notatki „(punkt (2) planu)”.
- Zmiana idzie trasą `agent-instructions/README.md`: gałąź zadania od `foundations`, sprawdzenia, przeszukanie fundamentu (WAY-33), jedna niezależna ocena (WAY-10), PR do `foundations`, scala Mariusz.
- Istniejące sondy faktów o narzędziach tylko pilnują cytatów z dokumentacji; sonda zachowania wymaga uruchomienia agenta z poświadczeniami i modelem (`probes/claude-code-path-rules/test_claude_code_path_rules.py`, docstring).

## Questions carried to cycle

- Jak zapisać metodę faktu o zachowaniu narzędzia, gdy sonda wymaga uruchomienia agenta — szablon faktów ma tu `TODO — decision pending` (`elements/environment-facts/template.md`, punkt o konfiguracji, której komenda nie ustawi).

## Decisions in play

- **WAY-09/1** — „What may enter the process repository?”, fragment:
    > On the main branch, this repository holds `foundations/` with the entries of the-way itself, a directory for each part of the process other than `repository` — `elements/<element>/` for each foundation element, `elements/common/` for what the elements share, `relation-model/`, `gate/`, `installation/`, `agent-instructions/`, `project-level/` and `task-cycle/` — …
    - Lista nie zna `instruction-files/`; dopisanie zmienia sens decyzji i wymaga ponownej akceptacji Mariusza (WAY-07).
- **repository-file-location/1** (niezmiennik):
    > Where {merge-onto} exists, every file git tracks lies in `foundations/` or in a directory WAY-09 names for a part of the process, belongs to the `repository` or the `agent-instructions` part of the part map, or is the `README.md` at the root.
- **WAY-10/1** — „Who assesses a change to an invariant test or to the foundation?”, fragment:
    > A change to an invariant test or to the foundation is assessed by one independent agent, on a model other than its author's where one is available, …
- **WAY-27/1** — „Where may this repository point for its reasoning?”:
    > Nothing in this repository points to a source outside it that its readers cannot reach: every entry carries its whole reasoning, and what is seen only in such a source is described in the entry instead of being pointed to.
- **WAY-52/1** — „What is generated from the part map for an agent?”, fragment:
    > From the part map a product generates for its agents only rules pinned to path patterns … No overview of the repository is generated for an agent.
- **WAY-03/1** — „Who may change an invariant test, and when?”, fragment z *Rejected*:
    > a local hook — one switch skips it.
    - Wiersz o mechanizmie jest z tym zgodny: lokalny hook Claude Code jest dodatkiem, nie jedynym nośnikiem.
- **WAY-85/1** — „How is a finding of a study written as an environment fact?”, fragment:
    > A finding of a study stands as an environment fact recording what the study measured, in the version of the paper its source names, …
- **WAY-90/1** — „Which citations of a decision's *Based on* become environment fact entries, and how are they named?”, fragment:
    > … it names a fact entry instead for every citation that, stopping being true today, would send the decision to review — a finding about agents or models, the behaviour of a tool the process uses.
- **WAY-100/1** — „When does a method or practice borrowed from elsewhere bind a product?”, fragment:
    > A method or practice borrowed from outside a product binds its way of working only through a decision that names what is adopted, where it applies, and why.

## Out of scope

- Poprawki przewodnika agentów (`agent-instructions/README.md`) i globalnego `CLAUDE.md` — osobny wątek: <private notes>/wznowienie_przewodnik_agentow_the_way.
- Zmiana instalatora the way — `CLAUDE.md` z `@AGENTS.md` zamiast `.claude/rules/the-way.md` i podział instalowanych skilli na podstawowe i opcjonalne, w tym czy produkt dostaje `maintain-instruction-files` — osobne zadanie.

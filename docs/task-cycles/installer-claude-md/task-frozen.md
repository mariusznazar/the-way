---
title: "the way: instalator — `CLAUDE.md` z `@AGENTS.md` zamiast `.claude/rules/the-way.md`"
status: draft
created: 2026-10-10
updated: 2026-10-10
tags: []
related: "[[(P) Proces pracy nad produktem]]"
---

# the way: instalator — `CLAUDE.md` z `@AGENTS.md` zamiast `.claude/rules/the-way.md`

Status: ready for cycle
Project relation: independent

## Description

### Need

- Claude Code w produkcie z the way dostaje wskazówki the way dwa razy: z `.claude/rules/the-way.md` i z bloku instalatora w `AGENTS.md`, który czyta, gdy repo nie ma `CLAUDE.md`.
- Podwójny zapis maskuje awarię zamiast jej zapobiegać: `CLAUDE.md` założony później wyłącza czytanie `AGENTS.md`, a plik reguł chroni tylko blok the way, nie sekcję Backlog.

### To do

1. Instalator zakłada w korzeniu produktu `CLAUDE.md` z jedną linią `@AGENTS.md`, gdy takiego pliku nie ma.
2. Plan instalacji ostrzega, gdy `CLAUDE.md` w korzeniu istnieje bez tego importu; istniejącego pliku instalator nie zmienia.
3. Instalator przestaje pisać `.claude/rules/the-way.md`.
4. `installation/README.md` opisuje nowy układ plików w produkcie i nową procedurę przesunięcia przypięcia, która dziś każe usunąć `.claude/rules/the-way.md` przed ponownym uruchomieniem instalatora.
5. Skill `maintain-instruction-files` (`instruction-files/SKILL.md`) i przykłady w *Verification* WAY-132 przestają opisywać `.claude/rules/the-way.md` jako plik instalatora.

## Context

- Materiał: [[mapa_pakietu_10x]], sekcja „m1l4”, wiersz „Jedno źródło prawdy” (werdykt WAY-132) i Notatki z krytyki ocen (podwójny zapis jako zabezpieczenie) — werdykt brzmi: „zakłada `CLAUDE.md` z `@AGENTS.md`, gdy pliku nie ma, ostrzega w planie instalacji, gdy `CLAUDE.md` jest bez tego importu albo stoi `CLAUDE.local.md`, i dopiero wtedy przestaje pisać `.claude/rules/the-way.md`”.
- Fakt `claude-code-agents-md/1`: Claude Code od v2.1.277 czyta `AGENTS.md` sam tylko wtedy, gdy ani w katalogu roboczym, ani wyżej nie stoi `CLAUDE.md`, `.claude/CLAUDE.md` ani `CLAUDE.local.md`.
- Ostrzeżenia o `CLAUDE.local.md`, którego chce werdykt, zadanie nie ma: `CLAUDE.local.md` wczytuje się obok `CLAUDE.md` i nie odcina importu, więc po zmianie żadnego przypadku awarii nie wskazuje (Mariusz, w refinemencie).
- Gdy `CLAUDE.md` stoi bez importu, Claude Code w tym produkcie nie dostanie wskazówek the way, dopóki człowiek nie dopisze importu — ostrzeżenie z punktu 2 jest jedynym śladem.
- Niezmierzone: czy `/init` Claude Code zostawia istniejący import w `CLAUDE.md`.
- Powierzchnia `installation-command` w `foundations/part_map.md` mówi, że instalator nie zastępuje żadnego istniejącego pliku i do istniejących dopisuje tylko sekcję `.gitmodules`, blok `AGENTS.md` i linię `.runs/` — nowy `CLAUDE.md` jest nowym plikiem, nie dopisaniem.
- Kod: `installation/install.py` (`RULE`, `plan`, `warnings_for`), testy w `installation/test_install.py`.
- `loop2` dziś: brak `CLAUDE.md`, `CLAUDE.local.md` i `.claude/CLAUDE.md`, stoi `.claude/rules/the-way.md`, przypięcie `1e444a0`.

## Questions carried to cycle

none

## Decisions in play

- **WAY-132/1** — „Which file carries the instructions Claude Code, Codex and Cursor share?”:
    > The skill of `instruction-files` proposes for a repository whose agents use more than one of Claude Code, Codex and Cursor, and the-way keeps for itself, a root `AGENTS.md` that carries the instructions those tools share and a root `CLAUDE.md`, where there is one, whose first line is `@AGENTS.md` alone and which holds only what Claude Code alone needs. The skill leaves out of this proposal the files and the marked block the-way's installer writes in a product.
    - z *Rationale*: „What the installer writes in a product answers to the installer's own surface and stays outside this decision.”
- **WAY-34/1** — „Which version of the process does a product use?”, fragment:
    > A newer version of the process enters a product only through a task in the product that moves the pin.
- **WAY-107/1** — „Where does a product tell the project level where its backlog stands?”, fragment:
    > A product names where it keeps projects and tasks in a `## Backlog` section of its root `AGENTS.md`, outside the block the-way's installer owns.

## Settlements to record

Candidates: 3 shown, 1 accepted — 2026-10-10

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Instalator zakłada w produkcie `CLAUDE.md` z `@AGENTS.md`, gdy pliku nie ma, i ostrzega w planie instalacji, gdy `CLAUDE.md` jest bez tego importu — wskazówki the way dochodzą do Claude Code przez blok w `AGENTS.md`. | decision | werdykt wiersza „Jedno źródło prawdy” ([[mapa_pakietu_10x]], m1l4); To do 1–3; odpowiedź Mariusza na pytanie kontrolne: import, który zniknie z `CLAUDE.md` po instalacji (ręcznie albo przez `/init`), zostaje niepilnowany | czy przy `CLAUDE.md` bez importu instalator dopisuje import, pisze plik reguł zastępczo czy tylko ostrzega — WAY-132 zostawia pliki instalatora poza sobą, więc dziś nic tego nie wiąże |

## Out of scope

- Przesunięcie przypięcia the way w `loop2` — osobne zadanie w produkcie (WAY-34).

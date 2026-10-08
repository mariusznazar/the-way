---
title: "the way: skille the-way dostępne dla Claude Code i Codexa w sesjach pracujących na samym the-way"
status: draft
created: 2026-10-08
updated: 2026-10-08
tags: []
related: "(P) Proces pracy nad produktem"
---

# the way: skille the-way dostępne dla Claude Code i Codexa w sesjach pracujących na samym the-way

Status: ready for cycle
Project relation: independent

## Description

### Need

- The-way powinno pracować na sobie własnymi skillami.
- Sesja pracująca na repo the-way dostaje dziś zamiast nich skille globalne albo żadne:
    - pod nazwami `refine-task` i `critique` odpowiadają skille z vox-ai-tools,
    - `find-foundation-entries`, `define-project`, `settle-technology` i `implement-task` nie są dostępne wcale,
    - pięć skilli elementów jest podpiętych globalnie, więc sesja w worktree czyta je z głównego checkoutu, a nie ze swojego.

### To do

1. Udostępnić Claude Code i Codexowi wszystkie skille the-way w sesjach pracujących na repo the-way, pod nazwami z prefiksem `the-way-`, bez instalowania the-way w nim samym (bez podmodułu, przypięcia i plików fundamentu).
2. Czytać skill i pliki, do których odsyła, z checkoutu albo worktree, w którym pracuje sesja.
3. Sprawić, by skill uruchomiony w the-way odsyłał do innych skilli the-way pod nazwami z prefiksem `the-way-`.
4. Zgłaszać w testach the-way skill, którego sesja na the-way nie widzi.
5. Dopisać do `AGENTS.md` the-way sekcję `## Backlog`, mówiącą, że:
    - zadania the-way żyją w `<private notes>/Notes\Projects\(P) Proces pracy nad produktem\_tasks_active.md`,
    - opis zadania leży w `_zadania/` tego folderu i jest podlinkowany z linii zadania.
6. Zdjąć z `C:\Users\Mariusz\.claude\skills\` globalne dowiązania pięciu skilli elementów, gdy sesja na the-way widzi już skille z punktu 1:
    - `record-decision`, `record-invariant`, `record-glossary-term`, `record-environment-fact`, `update-part-map`.

## Context

- Instalator zakłada w produkcie ten sam kształt: krótkie pliki `.claude/skills/the-way-<nazwa>/SKILL.md` i `.agents/skills/the-way-<nazwa>/SKILL.md`, wskazujące na przypięty `.the-way` (`installation/install.py`, `installation/README.md`).
- Prefiks usuwa zderzenie z globalnymi `refine-task` i `critique` bez polegania na tym, jak Claude Code i Codex rozstrzygają dwa skille o tej samej nazwie.
- Codex i Claude Code czytają skille globalne z jednego katalogu: `C:\Users\Mariusz\.agents\skills` jest dowiązaniem do `C:\Users\Mariusz\.claude\skills`.
- Zadanie wchłania wcześniejsze zadanie o czytaniu skilli elementów z własnego worktree; jego szkic dopisku do `elements/common/way_of_working.md`: AIR-393 w zeszycie ai-review lub w jego archiwum.
- Skille the-way znają dziś dwa tryby pracy, globalny i w produkcie (np. `project-level/task/skill/SKILL.md`, akapit pod nagłówkiem).

## Questions carried to cycle

- Czy wskaźniki tworzy kod instalatora w trybie bez przypięcia, czy osobny mechanizm.

## Decisions in play

- **WAY-09/1** — „What may enter the process repository?”, fragment:
    > …the files that configure the whole repository, which its part map gives to the `repository` part (WAY-44), the root agent instruction files, which the map gives to `agent-instructions` (WAY-44), and a `README.md` that describes the repository.
    - Katalogi `.claude/skills/` i `.agents/skills/` nie są wymienione wprost; cykl ustala, czy mieszczą się w plikach części `agent-instructions`, czy WAY-09 wymaga zmiany sensu do akceptacji przez Mariusza (WAY-07).
- **repository-file-location/1** (niezmiennik, wywiedziony z WAY-09@b829b86a):
    > Where {merge-onto} exists, every file git tracks lies in `foundations/` or in a directory WAY-09 names for a part of the process, belongs to the `repository` or the `agent-instructions` part of the part map, or is the `README.md` at the root.
- **WAY-101/1** — „Who chooses the backlog tool used with the-way?”:
    > The-way's task cycle requires no particular backlog application or service; each product chooses where it keeps its roadmap, projects and tasks.
    - Punkt 5 jest takim wyborem the-way dla samego siebie.
- **Mapa części, `agent-instructions`** — odpowiedzialność: „the instructions agents read when they work on this repository, and for the hooks and the configuration of agents' tools and of CI that direct them”; pliki: `/AGENTS.md`, `/CLAUDE.md`, `agent-instructions/**`.

## Out of scope

none

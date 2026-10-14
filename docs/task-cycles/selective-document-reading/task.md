---
title: "the way: wybiórczy odczyt fundamentu i dokumentów plan-project"
status: draft
created: 2026-10-13
updated: 2026-10-14
tags: [the-way, zadanie]
related: ["[[(P) Proces pracy nad produktem]]"]
---

# the way: wybiórczy odczyt fundamentu i dokumentów plan-project

Status: ready for cycle
Project relation: independent

## Description

### Need

- W źródłowej sesji podziału MVP `loop2` odczytano całą definicję o 2340 liniach i nastąpiła jedna kompakcja kontekstu.
- Mariusz wskazuje także wzrost fundamentu produktu: „wczytywanie rosnącego fundamentu w całości szybko stanie się absurdem”.

### To do

1. Ograniczyć czytanie dużych definicji i istniejących planów projektu w całości przez `plan-project`, dobierając materiał potrzebny do wykonywanej pracy.
2. Wprowadzić domyślnie wybiórczy odczyt fundamentu produktu we wszystkich instrukcjach procesu wymagających dziś jego pełnego odczytu, z wykorzystaniem mapy części i istniejących powiązań wpisów oraz rozszerzaniem odczytu stosownie do wykonywanej pracy.

### Acceptance criteria

- Ograniczenie odczytu zachowuje wymagane pokrycie zakresu projektu, projektowanych wpisów i otwartych pytań w planie oraz jego sprawdzenie skryptem i niezależną ocenę, zgodnie z WAY-146/1.
- Dobór decyzji obejmuje każdą decyzję, której Scope wskazuje część dotkniętą pracą, zgodnie z `decisions-found-for-change/1`.

### Questions to settle

- Czy ograniczenie odczytu ma obejmować tylko definicję i istniejący plan projektu, czy także fundament produktu?
  - Answer: Także fundament produktu; Mariusz podtrzymuje, że „odczyt powinien być robiony wybiórczo, ale «z głową»”.
- Czy zadanie ma ustanowić wspólną zasadę odczytu fundamentu i zastosować ją w miejscach procesu wymagających dziś pełnego odczytu?
  - Answer: Tak; Mariusz: „objąłbym wszystkie te instrukcje”.

## Context

- Źródło: sesja `01246b80`, notatki m2l1 w [[mapa_pakietu_10x]].
- Zadanie wydzielone z [[skrocic_cykl_implement_task]].
- `foundations/invariants.md`, wpis `decisions-found-for-change/1`, wymaga doboru każdej decyzji, której Scope obejmuje część dotkniętą zmianą; jego Method pozostaje `TODO`.
- Nakazy pełnego odczytu fundamentu występują w `elements/common/way_of_working.md`, `elements/part-map/skill/SKILL.md`, `project-level/skill/SKILL.md` i `project-level/technology/SKILL.md`; instrukcje czytania fundamentu mają też `elements/common/skill/SKILL.md`, `project-level/task/skill/SKILL.md` i `task-cycle/skill/SKILL.md`.
- Reguła wspólna w `elements/common/way_of_working.md` obejmuje wszystkie skille elementów fundamentu.
- Zadanie ma zmienić obowiązek pełnego odczytu zapisany w WAY-111/1 i WAY-115/1 oraz uzgodnić z tą zmianą instrukcje wspólne i szczegółowe.
- WAY-33/1 nadal wymaga wyszukiwania niepowiązanych kolizji przy pisaniu lub zmianie wpisu fundamentu; sposób wykonania tego wyszukiwania przy wybiórczym odczycie pozostaje pytaniem wykonawczym.
- Sprawdzenie powiązań i aktualności ich fingerprintów działa w format guards; część decyzji wymaga oceny agenta lub człowieka, a pełny gate the-way nie jest jeszcze zaimplementowany.

## Questions carried to cycle

- Jak dobierać i rozszerzać odczyt wpisów na podstawie mapy części i powiązań, także gdy praca nad projektem nie ma jeszcze diffu plików?
- Jak ograniczyć odczyt definicji i istniejącego planu, zachowując informacje potrzebne do podziału projektu oraz do oceny znaczenia zadań i odpowiedzi?
- Jak sprawdzać kompletność doboru decyzji wobec `decisions-found-for-change/1`, którego Method pozostaje `TODO`?

## Human actions

none

## Decisions in play

- WAY-111/1:
  > Before drafting, the agent reads the product's whole foundation: the part map's files, trust
  > boundaries and surfaces; decisions' binding sentences, scope and relations; invariants' sentences
  > and parts; the glossary; and environment facts. It brings a touched part, a decision the project
  > may change, an invariant it may break or a boundary it crosses to the human as material and asks
  > whether the project changes an existing decision or fits it.

- WAY-115/1:
  > The agent reads the project's sources and the product's whole foundation, then shows the human a
  > complete candidate table with each proposed settlement, its kind, its source and the concrete
  > choice or action the next reader would otherwise have to guess; a row without such a consequence
  > is shown as rejected. The human accepts or rejects rows before they are handed to the skills of
  > their kinds, and each accepted row is recorded as it is worked through. The definition keeps the
  > working table until the step ends, then replaces it with a `Candidates:` line recording how many
  > rows were shown and accepted.

- WAY-21/1:
  > A decision's scope names the parts of the product it governs, taken from the part map, and never
  > file paths, so that the decisions governing a change are found from the files it touches through
  > the part map's rule for assigning files.

- WAY-17/1:
  > Every link of the chain fact → decision → invariant → test is written in the entry that depends
  > on the other, and none is optional: a decision and an invariant name the environment facts they
  > rest on, an invariant derived from a decision names that decision, and a check names its
  > invariant.

- WAY-31/1:
  > A relation `derives from` or `narrows` relies on the binding part of the decision it names and
  > carries that decision's fingerprint (`derives from WAY-01@<fingerprint>`), and an invariant entry's
  > *Derives from* and *Rests on* carry the fingerprint of each entry they name, while its *Part*
  > carries none. A change to the fingerprint of an entry so named reaches the main branch together
  > with every decision that relates to it with a fingerprint and every invariant carrying it, each
  > checked against the new binding part and carrying the new fingerprint.

- WAY-33/1:
  > When a foundation entry is written, or a version changes its binding part, an agent searches the
  > whole foundation for entries it touches that no written link joins to it, and before the version
  > is accepted each finding becomes a relation, a change to one of the entries, or a question to a
  > human. The search runs again against the current main branch before the task branch is merged,
  > and a change to the foundation is merged only with the record of both searches.

- WAY-12/1:
  > A decision is checked through the invariants derived from it, which its *Verification* names by
  > the identifiers of their entries, and tests live only with invariants. Where no invariant can be
  > derived today, an agent compares a change with the decision using a pair of examples — one that
  > complies and one that violates — and where an agent cannot judge, a human assesses it and leaves a
  > trace of who and when. A decision can combine levels, each covering what it can check of its
  > binding sentences.

- WAY-146/1:
  > Before a project plan is handed over, a script checks the form it reads the plan by and what the
  > plan's structure decides: each projected entry of the definition has tasks that realize it, exactly
  > one of them writing it into the foundation; each item of In scope has a task; no task depends on
  > itself through others; some task depends on each preparatory task; and each open question of the
  > definition stands in the plan word for word, with a task of the plan or an answer. The plan's
  > independent critique then judges, against the definition, what no script tells apart: whether each
  > task that is not preparatory ends with something checkable in the running product, whether each
  > technical element enters with the first task that uses it, whether each question stands where the
  > definition puts it or the log of changes gives its move, and whether a quoted answer settles its
  > question. A check a script can make is never left to the critique.

## Settlements to record

Candidates: 2 shown, 2 accepted — 2026-10-14

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Skille the-way domyślnie czytają fundament produktu wybiórczo, dobierając wpisy przez mapę części i ich powiązania oraz rozszerzając odczyt stosownie do wykonywanej pracy. | decision | Mariusz: „odczyt powinien być robiony wybiórczo, ale «z głową»” oraz „objąłbym wszystkie te instrukcje”; propozycja doboru materiału przedstawiona przed wyborem zakresu; To do, punkt 2 | Czy pozostawić nakaz pełnego odczytu w części skilli i czy wybiórczy odczyt pozwala sięgać po dodatkowe potrzebne wpisy. |
| 2 | plan-project ogranicza odczyt dużych definicji i istniejących planów projektu do materiału potrzebnego do wykonywanej pracy. | decision | To do, punkt 1; źródłowy zakres zadania: ograniczenie czytania dużych dokumentów w całości przez plan-project | Czy agent ma nadal ładować całą definicję i istniejący plan przy każdym rozpoczęciu lub wznowieniu pracy. |

## Out of scope

- Pozostałe zmiany organizacji cyklu `implement-task` opisane w [[skrocic_cykl_implement_task]].

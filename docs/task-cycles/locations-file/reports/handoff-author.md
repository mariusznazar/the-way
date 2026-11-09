# Handoff — the one author of the change (`make-change`, "the whole change as the one author")

Delegation: the person who requested this cycle delegated every intermediate choice to the
orchestrator. Do not ask the human anything. Questions go to the orchestrator in your report with the
status `questions`; a missing fact or permission is `blocked`; an open design choice you meet is
`returned` with no code (WAY-135).

## Where you work

- Worktree (work from its root): `the root of the task's worktree`
- Branch: `task/locations-file`, base `17b83bf145653be0beeb43f5fa8175a4197a3700` (`foundations`)
- Method: the project skill `the-way-make-change`, whose method file is
  `task-cycle/change/SKILL.md` in the worktree (the entry point is
  `.claude/skills/the-way-make-change/SKILL.md`). Read `task-cycle/change/SKILL.md` whole. Your
  variant: **the whole change as the one author**. Read a file the method names only when the step
  or variant that names it comes.
- Foundation step: `task-cycle/skill/foundation_step.md`; the return step is taken later by you,
  resumed, with `task-cycle/skill/return_step.md` — read it only then.
- Integration route for the-way itself: `agent-instructions/README.md` (read it whole). The gate
  (`python -B gate/run_tests.py`) is mine to run; you run focused checks:
  `python -B gate/run_tests.py <directory>`.
- Report to write: `.runs/task-cycles/locations-file/reports/author-report.md`
- The record of the cycle is mine; you do not read `cycle.md` and you commit nothing under `.runs/`.

## The task

The frozen task document, to read whole: `.runs/task-cycles/locations-file/task.md`
(`Status: ready for cycle`, `Project relation: independent`). It was approved 2026-11-08 by Mariusz.
There is no spec and no plan: the task leaves no open design choice. Its *Questions carried to
cycle* leaves you one choice — how the foundation records the new check, within row 3 of
*Settlements to record* — and you make it and name it in your report as an autonomous choice, with
the way you did not take and its cost if wrong.

Answers of step 4 of the cycle:

- Trust boundary: no. Irreversible operation: no.
- Open design choice: none. Reserved choice: none.
- No guidelines of the product exist (`guidelines/` is absent; question 5 of the task settles that
  the task does not wait for them).
- The human action "Mariusz creates `~/.the-way/locations.json` with the `tasks` entry under
  `the-way`" is done; the file exists on this machine. **Never copy its content, its path inside the
  home directory beyond `~/.the-way/locations.json`, or the path it holds into any file you write.**
  You may read the file only to see its form.

## Foundation you read (selected by "Reading the foundation")

Parts touched: `agent-instructions` (root `AGENTS.md`), `gate` (the new test), `project-level` and
`foundation-review` and `product-guidelines` and `installation` (skills and tests that name the
`## Backlog` section), `decisions`, `invariants` (the entries below). Read whole, from
`foundations/` in the worktree:

- decisions WAY-27, WAY-107, WAY-309, WAY-308, WAY-61, WAY-140, WAY-16, WAY-33, WAY-114, WAY-134;
  search the decision log for any other decision whose *Scope* names a touched part and that speaks
  of `## Backlog`, the place of the tasks, an absolute path, or the invariant `outbound-link-reach`;
- invariant `outbound-link-reach`, and the invariants whose *Part* is a touched part or `every`
  that your search of the foundation reaches;
- the part map (`foundations/part_map.md`) and the glossary (`foundations/glossary.md`).

Write the entries through the pinned skills of their elements (`.claude/skills/the-way-record-decision`,
`the-way-record-invariant`, …) as `foundation_step.md` gives.

## What the change is — the task's *To do*, word for word

1. the way ustala plik lokalizacji użytkownika `~/.the-way/locations.json`, leżący poza każdym repozytorium: obiekt JSON, którego klucze to nazwy repozytoriów, a pod każdym — pozycje po nazwie (np. `tasks`, `projects`) ze ścieżkami na dysku użytkownika (pytanie 1).
2. Sekcja `## Backlog` głównego `AGENTS.md` the-way wskazuje miejsce zadań pozycją `tasks` pod `the-way` w tym pliku, bez ścieżki bezwzględnej; gdy pliku albo pozycji brakuje, agent pyta człowieka i proponuje dopisać ją do pliku (pytanie 1).
3. Każdy skill the way, który szuka backlogu produktu w sekcji `## Backlog`, znajduje go także wtedy, gdy sekcja wskazuje pozycję pliku lokalizacji; gdy miejsca brakuje, proponuje zapisać je do pliku lokalizacji, jeśli to miejsce na dysku użytkownika poza repozytorium, a w przeciwnym razie do sekcji `## Backlog`, jak dotąd (pytania 1 i 4).
4. the way dostaje test uruchamiany przez `python -B gate/run_tests.py`, który czyta każdy plik śledzony przez git i nie przechodzi, wypisując plik i linię, gdy znajdzie ścieżkę bezwzględną (litera dysku, katalog domowy) albo link do notatki `[[...]]` — tym samym wzorcem, którym szuka ich `task-cycle/private_paths_check.py` — bez wyjątku dla sekcji `## Backlog` (pytanie 1); pomija tylko pliki z listy w samym teście, które z natury piszą przykładowe ścieżki — dziś `task-cycle/private_paths_check.py`, `task-cycle/test_private_paths_check.py`, `instruction-files/check_instructions.py` i `instruction-files/test_check_instructions.py` (pytanie 2).
5. Linia sekcji `## Backlog` w `AGENTS.md` o przestawieniu zadania na Ready zachowuje samo polecenie, a rulebook notatek autora nazywa słowami, bez ścieżki (pytanie 3).

Settlements to record (rows 1–3 of *Settlements to record* of the frozen task), each written whole as
an entry of its kind by the foundation step: row 1 and row 2 as decisions (they change WAY-27 and
WAY-107 — edit those in place, WAY-07, or write a new decision where the decisions' template calls
for it), row 3 as an invariant (it changes `outbound-link-reach`). *Decisions in play* of the task
lists WAY-27, WAY-107, WAY-309, WAY-61, WAY-140 and WAY-16.

Hints from the orchestrator's reading (verify; they are no source):

- About 15 tracked files name the `## Backlog` section (`grep -rn "## Backlog"` over tracked files):
  among them `foundation-review/SKILL.md`, `project-level/skill/first_write.md`,
  `project-level/task/skill/read_sources.md`, `project-level/task/skill/final_review.md`,
  `project-level/lead/skill/SKILL.md`, `project-level/definition_template.md`,
  `product-guidelines/coding/recognize.md`, `product-guidelines/testing/recognize.md`, and four
  `installation/test_*_installation.py` tests. Decide which really read the section to find the
  place of tasks or projects (they change) and which only mention it (they may stay).
- `task-cycle/private_paths_check.py` defines the pattern (`FINDING`, `WINDOWS_DRIVE`,
  `POSIX_DRIVE`, `HOME_DIRECTORY`, `NOTE_LINK`); the new test uses that same pattern — import it from
  that file (the test suite's imports follow `script-imports` and the part map: `gate` depends on
  `none`, so check what the part map allows before importing across parts and decide how the test
  stays within it, e.g. by reading the pattern as the existing tests of the gate do their shared
  code; name your choice).
- The orchestrator's inventory (2026-11-08, `a3206c1`): the pattern finds 100 places over tracked
  files — 2 in `## Backlog` of `AGENTS.md` and 98 in the four files of *To do* 4. Today's tracked
  files may differ; make the test pass on the tree you deliver and fail, naming file and line, when
  you put a path into a tracked file.
- Do not rewrite the pattern's behaviour in `private_paths_check.py`; this task changes no script
  of the cycle beyond what *To do* 4 needs.
- Keep `~/.the-way/locations.json` described in the-way's own files by its form only: an object whose
  keys are repository names and under each, entries by name (`tasks`, `projects`) holding a path on
  the user's disk. Do not put the author's real paths anywhere, in examples included — write a
  placeholder that the pattern does not list (e.g. described in words).
- The test must pass in the worktree (an ignored `.runs/` directory is not tracked; the test reads
  `git ls-files`).

## Out of scope

Paths already in the public history; the `## Backlog` section of the product `loop2`; any change to
the author's private notes or global instructions; anything outside the repository.

## Report

Write `.runs/task-cycles/locations-file/reports/author-report.md` as the method gives, with every
check's command and exit code, your own-work check, your weakest-point check, the foundation
entries with one sentence of meaning in English and one in Polish and their mark (`row <n>` or
`the cycle's`), the choice named above, and the sections **Searches not found or unclear** and the
reach beyond this handoff. Return: status, commits, a one-line check result, and the report path.
Commit on the task branch; leave the worktree clean.

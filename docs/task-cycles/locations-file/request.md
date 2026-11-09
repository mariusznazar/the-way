**State: ready** — the change is complete, was reviewed by agents that did not make it, and the full tests pass; one question waits for your yes below.

## What you will see

- The repository no longer says where your private notes are. The line that tells an agent where the-way's tasks are kept now names an entry in a small places file in your home folder (a file you created before the cycle), instead of a drive path to your notes. The line about moving a task to Ready now names your rules for agent tasks in words, without a path.
- An agent that cannot find that file or that entry asks you where the place is and offers to add the entry. A place on your own disk goes to the places file; a folder of the repository or the address of a public tracker stays in the backlog section as before.
- Every skill that looks for a product's backlog now reads it the same way, through one shared page, so a product can also name its place by an entry of the places file.
- A new test in the one command that runs all tests fails, naming file and line, if any tracked file contains a drive path, a home-folder path or a link to a note. Four files that by nature write example paths are the only exception, and the list stands in the test.
- The foundation says so: the rule about where this repository may point no longer exempts a path in the backlog section, and the new places file has its own decision.

### Underneath

The places file is a JSON object in a fixed place in your home folder, whose keys are repository names and whose entries (one for tasks, one for projects) hold paths on your disk; no environment variable is used. The paths already published in the repository's history stay there.

## For you to decide

1. An agent now treats a place whose entry exists but whose path does not exist on your disk as missing, and asks you where it is. The task did not say what to do then; the other answer is to treat only a missing file or entry as missing, and a moved folder would then fail without a question. Accept it? (Minor findings, 1)
2. One decision was changed that you did not see at the task: the decision on how the cycle finds private paths now names the new test as a check of it. It changes no rule. Accept?

## Cost

About 40 minutes of working time in 13 stages, plus the waits for the tests: 21.7 million tokens (16.7 million on claude-sonnet-5-5, 5.0 million on claude-opus-5-5), mostly cached input. Review rounds: 2 on the change (one failed with 2 blocking findings, fixed once and passed), 1 on the follow-up edit (passed). The table of stages is in the committed record.

## How to merge

Use a merge that keeps the commits, because the link to the record survives only then. The branch has 3 commits on top of the target branch and the target branch has not moved.

<details>
<summary>W języku zadania (polski)</summary>

**Stan: gotowe** — zmiana jest kompletna, przejrzana przez agentów, którzy jej nie pisali, a pełne testy przechodzą; poniżej czeka jedno pytanie o Twoje „tak”.

## Co zobaczysz

- Repozytorium przestaje mówić, gdzie leżą Twoje prywatne notatki. Linia, która mówi agentowi, gdzie są zadania the-way, wskazuje teraz pozycję w małym pliku miejsc w Twoim katalogu domowym (plik, który założyłeś przed cyklem), a nie ścieżkę na dysku do notatek. Linia o przestawieniu zadania na Ready nazywa Twoje reguły dla zadań agentowych słowami, bez ścieżki.
- Agent, który nie znajdzie tego pliku albo tej pozycji, pyta Cię, gdzie jest to miejsce, i proponuje dopisać pozycję. Miejsce na Twoim dysku trafia do pliku miejsc; katalog w repozytorium albo adres publicznego trackera zostaje w sekcji backlogu jak dotąd.
- Każdy skill, który szuka backlogu produktu, czyta go teraz tak samo, przez jedną wspólną stronę, więc produkt może też wskazać miejsce pozycją pliku miejsc.
- Nowy test w jednym poleceniu uruchamiającym wszystkie testy nie przechodzi, wypisując plik i linię, jeśli którykolwiek plik śledzony zawiera ścieżkę z literą dysku, ścieżkę z katalogu domowego albo link do notatki. Wyjątkiem są tylko cztery pliki, które z natury piszą przykładowe ścieżki; lista stoi w teście.
- Fundament mówi to samo: reguła o tym, dokąd to repozytorium może wskazywać, nie robi już wyjątku dla ścieżki w sekcji backlogu, a plik miejsc ma własną decyzję.

### Pod spodem

Plik miejsc to obiekt JSON w stałym miejscu w katalogu domowym, którego klucze to nazwy repozytoriów, a pozycje (jedna dla zadań, jedna dla projektów) trzymają ścieżki na Twoim dysku; zmiennej środowiskowej nie ma. Ścieżki już opublikowane w historii repozytorium zostają w niej.

## Do rozstrzygnięcia

1. Agent traktuje teraz miejsce, którego pozycja istnieje, ale ścieżka z niej nie istnieje na Twoim dysku, jako brakujące i pyta, gdzie jest. Zadanie nie mówiło, co robić w takim razie; druga odpowiedź to uznać za brakujące tylko brak pliku albo pozycji, a przeniesiony katalog skończyłby się wtedy bez pytania. Przyjąć? (Minor findings, 1)
2. Zmieniła się jedna decyzja, której nie widziałeś przy zadaniu: decyzja o tym, jak cykl znajduje prywatne ścieżki, wskazuje teraz nowy test jako jej sprawdzian. Nie zmienia to żadnej reguły. Przyjąć?

## Koszt

Około 40 minut czasu pracy w 13 etapach, plus oczekiwanie na testy: 21,7 mln tokenów (16,7 mln na claude-sonnet-5-5, 5,0 mln na claude-opus-5-5), głównie wejście z pamięci podręcznej. Rundy przeglądu: 2 dla zmiany (jedna nie przeszła z 2 uwagami blokującymi, poprawiona raz i przeszła), 1 dla dodatkowej poprawki (przeszła). Tabela etapów jest w zatwierdzonym zapisie.

## Jak scalić

Użyj scalenia, które zachowuje commity, bo link do zapisu przeżywa tylko wtedy. Gałąź ma 3 commity ponad gałęzią docelową, a gałąź docelowa się nie ruszyła.

</details>

## Technical changes

The change makes the places outside the repository a thing a file names instead of a path a file contains; the main part is a decision, a test and a shared skill page.

- Commit `973ee64`: the root `AGENTS.md` `## Backlog` section now names the entry `tasks` under `the-way` in `~/.the-way/locations.json` (no path; a missing file or entry makes the agent ask); the Ready line names the author's rules in words. New `project-level/backlog_place.md` says how a skill reads the section, resolves an entry of the locations file and records a missing place. Six readers of the section point to it: `foundation-review/SKILL.md`, `project-level/skill/first_write.md`, `project-level/task/skill/read_sources.md`, `project-level/task/skill/final_review.md`, `project-level/lead/skill/SKILL.md`, `task-cycle/skill/SKILL.md`; `project-level/definition_template.md` shows the new form. New test `task-cycle/test_tracked_files_private_paths.py` (128 lines) reads every tracked file with `private_paths_check.check_file` and skips four listed files. Foundation entries in `foundations/decisions.md` and `foundations/invariants.md` (below).
- Commit `ba36539`: the fix of the review's findings — the exemption of four files restored in the new decision, with the reasoning of question 2 of the task (price and three rejected ways); the sentence that forbade a cycle to write outside the repository narrowed to the locations file; the example name made the-way's own.
- Commit `2984b5f`: the return step named the new invariant in the *Verification* of WAY-309.

The test is in `task-cycle/`, not `gate/`: `gate` depends on nothing, so it could not import the script whose pattern the task requires the test to use. `python -B gate/run_tests.py` discovers it from there.

## Checks

- The gate, `python -B gate/run_tests.py`, on the final tree: exit 0, 826 tests in 9 directories, every directory passed (separate checkout of `2984b5f`). Also on the reviewed change before the return step (`ba36539`): exit 0, 826 tests. On the base (`17b83bf`): exit 0, 817 tests; no check failed on the base. No check failed or did not run.
- The new test, the author's failing run: before the `AGENTS.md` change, `python -B gate/run_tests.py task-cycle` exit 1, one failure listing exactly `AGENTS.md:20` and `AGENTS.md:25`; passing run after: exit 0, 209 tests. The reviewer also showed the test failing when the base `AGENTS.md` was restored, and failing when the file list in the invariant drifts from the test's.
- Own-work checks: the author checked *To do* 3 by grepping tracked files for `## Backlog`, `backlog` and `WAY-107` and reading each hit — six readers found, all pointing to the shared page; the whole-change reviewer repeated it with wider terms and found none missed. The fix compared WAY-320 word by word with question 2 of the task.
- `python -B elements/common/foundation_check.py`: exit 0, 0 errors.
- No user interface is touched; no screenshot applies.
- Reconciliation with the target branch: `origin/foundations` is still the base commit, so no merge and no review of a merge.
- Form check of this description: `python -B task-cycle/request_check.py .runs/task-cycles/locations-file/request.md --task .runs/task-cycles/locations-file/task.md`: last run exit 0 (CHECKS_PENDING).
- Check of private paths on this description: `python -B task-cycle/private_paths_check.py .runs/task-cycles/locations-file/request.md`: last run exit 0 (CHECKS_PENDING).
- Checks on the copy of the record: remarks check, private paths and image files — CHECKS_PENDING.

## Foundation entries

- WAY-320 (new, `row 2`): a user's places outside every repository are kept in one file, `~/.the-way/locations.json`, in a fixed place and without an environment variable — an object whose keys are repository names and whose entries (`tasks`, `projects`) hold paths on the user's disk; tracked files name an entry instead of a path, other than the four files the new invariant names.
- WAY-107 (edited, `row 1`): a place on the user's disk outside every repository stands in `## Backlog` as a locations-file entry, never as a path; a directory of the repository or a public tracker stays as it was; a missing place, file or entry makes the agent ask and offer to record it where it fits.
- WAY-27 (edited, `row 1`): the exception for the place of the tasks stays, but `## Backlog` names it by a locations-file entry, never by a path.
- Invariant `tracked-file-private-paths` (new, `row 3`, method `test`; derives from WAY-320 and WAY-309): no tracked file, other than `task-cycle/private_paths_check.py`, `task-cycle/test_private_paths_check.py`, `instruction-files/check_instructions.py` and `instruction-files/test_check_instructions.py`, contains an absolute path or a note link as WAY-309 names them. Its test is `task-cycle/test_tracked_files_private_paths.py`, new in this change; it is the invariant test the change writes, and no existing invariant test is altered.
- Invariant `outbound-link-reach` (edited, `row 3`, stays `review`): the exception for a link to the place of the tasks is removed. Its *Violated* mark stays `no`; no *Violated* mark was set or cleared and no surface changed.
- WAY-309 (edited, `the cycle's`, by the return step): its *Verification* names the invariant `tracked-file-private-paths`.

## Minor findings

1. The new shared page also counts a path that the entry holds but that does not exist as a missing place, which WAY-107 does not say (`project-level/backlog_place.md:21-22`). The reviewer's words: "Treating a dangling path as missing is a reasonable user's expectation and contradicts nothing, so it is Minor; either add \"or the path it holds does not exist\" to WAY-107 or leave it as the operational reading." The review of the fix kept it as Minor and accepted the author's choice to leave it.

## Findings outside the task's scope

none

## Course of the cycle

- **Task and sources:** an independent task (`Status: ready for cycle`, accepted 2026-11-08): keep places outside the repository in a locations file instead of paths in tracked files, with a test; sources: the task's questions 1–5 and rows 1–3, the foundation at `17b83bf`.
- **Process pin:** this checkout, the base commit `17b83bf`; the cycle did not move the pin.
- **Spec:** none — the task leaves no open design choice; the one choice carried to the cycle (how to record the new check) was bounded by row 3 and by the rule that a test checks what its invariant's sentence is about.
- **Route:** one author without a plan (one agent could hold it); class `same` as the orchestrator, because the change spans many parts; resumed for the fix and the return step.
- **Plan:** none.
- **Choices:** 5 other choices of the cycle, in the questions table of the record (the new invariant as a separate entry, the test in `task-cycle/`, one shared page for the rule, a missing path counted as a missing place, a cycle not writing the locations file), plus the choice of the route and of running the gate again on the final tree.
- **Blocking findings left:** none.
- **Record:** RECORD_LINK_PENDING

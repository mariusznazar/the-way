# Handoff: executor of slice 2, task `decision-log-reading-index`

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator, which
answers your questions from the task, its sources, the foundation and the code; no answer is the
human's approval. You never ask the human. The cycle has one human contact, the request.

## Where you work, and your stage

- Worktree (your working directory): `the task's worktree`, branch
  `task/decision-log-reading-index`. The head you start from is `30c5b1b`; the foundation entries of the plan
  (F1–F10) and the earlier slices are already committed on the branch. Nobody else writes in this worktree while
  you work.
- Method of your stage: `task-cycle/change/SKILL.md` — read it whole; your variant is "a slice, or the retry of
  a slice", so read `task-cycle/change/slice.md` too, and read a file either names only when its step comes.
- Boundary: slice 2 below and nothing else; no run of the product's full gate (the orchestrator runs it);
  commit by `git add <paths>`, never `git add -A`; commit messages in English, imperative. Return before any review.
- Report: `.runs/task-cycles/decision-log-reading-index/reports/executor-2-report.md`, as your method gives it, with
  the own-work check, **Unread material** and **Searches not found or unclear**.
- Risk of the slice: none.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed.
The files that a product's own tools and tests make by themselves are no working copy of the agent
and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a
worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside
its report what the report needs, and states in the report where each copy stood and that it was
removed. Where a removal fails, the agent finishes all the same and names in the report the
remainder, with its full path and the reason it stayed.

Your directory for working copies: `.runs/executor-2/`.

## Files of the task and the plan (addresses)

- Frozen task (Polish): `.runs/task-cycles/decision-log-reading-index/task.md`; the plan:
  `.runs/task-cycles/decision-log-reading-index/plan.md`. The passages below are copied from them word for word;
  the files are their addresses.
- The decision log is divided into 28 topical sections (`## ` headings); the report of the agent that made the
  division, `.runs/task-cycles/decision-log-reading-index/reports/foundation-entries-report.md`, lists them. The
  decisions F1–F9 wrote are commit `dae85e1`, the division is `104e126`, and the log's last edit is `0023a28`.
- Slice 1 added `elements/common/decision_index.py` (the index of selected decisions), its tests and a sentence of
  `elements-common` in `foundations/part_map.md`.

## What to read (identifiers with ranges, or files), at your head

Decisions in `foundations/decisions.md`, each whole (to the next `#` heading): WAY-18 (lines 713–764, as F4 leaves it), WAY-07 (468–496), WAY-38 (2511–2536), WAY-344 (2707–2819). `foundations/invariants.md` lines 86–94 (tracked-file-private-paths) and 116–144 (script-language, script-imports, script-subprocesses). `elements/common/foundation_check.py` lines 236–251, 345–358, 416–455; `elements/common/migrate_foundation.py` lines 133–150; the sibling script of slice 1, `elements/common/decision_index.py`, for the house style of a script of this directory. Every file you change, whole, before you change it.

## Slice 2 (copied word for word from the plan, "The comparison of a log's entries, and the check on a log with sections")

### Slice 2 — The comparison of a log's entries, and the check on a log with sections

- **Goal:** a script of the-way, `elements/common/compare_log_entries.py`, with its tests in
  `elements/common/test_compare_log_entries.py`, compares the entries of two copies of a product's
  decision log, given as two file paths: an entry is a block a `### <PREFIX>-<NN> — ` heading
  opens, from its heading to the line before the next heading of any level, without the blank lines
  at its end, keyed by its identifier, and the block of `## Withdrawn identifiers` where it stands
  is compared the same way. It reports each entry that stands in one copy only, each that stands
  twice in a copy, and each whose bytes differ, with the first line that differs; exit code 0 when
  every entry is the same byte for byte, 1 when it reports any, 2 with `Error: <message>` for a copy
  it cannot read or that holds no entry (WAY-344, with one test of it). Its docstring says that it
  serves the division of a log into sections, the-way's or a product's. The sentence of
  `elements-common` in `foundations/part_map.md` names it among what the part answers for. In
  `elements/common/test_foundation_check.py` one test pins that the check reads a log with topical
  sections: the fixture's log divided into two `## ` sections passes as the undivided one does, and
  an error in an entry of the second section is reported at its own line — the check needs no change
  for it, and the slice changes `elements/common/foundation_check.py` only where that test fails.
  With the script the slice confirms the division of F10: the log at the commit before the division
  against the log at the division's commit, both named in the report of the agent of the foundation
  entries, ends with exit code 0, and the slice's report gives the command and its output for the
  request.
- **Change:** `elements/common/compare_log_entries.py` ·
  `elements/common/test_compare_log_entries.py` · `elements/common/test_foundation_check.py` ·
  `foundations/part_map.md`
- **Read:** `.runs/task-cycles/decision-log-reading-index/task.md:33-42` To do ·
  `.runs/task-cycles/decision-log-reading-index/task.md:67-72` Questions to settle (question 3) ·
  WAY-18 as F4 leaves it · `foundations/decisions.md:209-236` WAY-07 ·
  `foundations/decisions.md:1093-1117` WAY-38 · `foundations/decisions.md:8245-8356` WAY-344 ·
  `foundations/invariants.md:86-94` tracked-file-private-paths ·
  `foundations/invariants.md:116-144` script-language, script-imports, script-subprocesses ·
  `elements/common/foundation_check.py:236-251` · `elements/common/foundation_check.py:345-358` ·
  `elements/common/foundation_check.py:416-455` · `elements/common/migrate_foundation.py:133-150`
- **Model:** cheaper
- **Risk:** none
- **Checks:** first a failing test of an entry whose text differs;
  `python -B -m unittest discover -s elements/common -p test_compare_log_entries.py`;
  `python -B -m unittest discover -s elements/common -p test_foundation_check.py`;
  `git show <commit before the division>:foundations/decisions.md > .runs/<the executor's
  directory>/before.md` and `git show <division commit>:foundations/decisions.md > .runs/<the
  executor's directory>/after.md`, then `python -B elements/common/compare_log_entries.py
  .runs/<the executor's directory>/before.md .runs/<the executor's directory>/after.md` exits 0
- **Depends on:** Slice 1 · F4 · F10

## The passages of the task the slice's *Read* names (copied word for word)

### To do (`task.md:33-42`)

### To do

1. Spis decyzji: skrypt the way, z testami, wypisuje do pliku, który wskaże agent, spis wybranych decyzji dziennika produktu — dla każdej decyzji jej numer, pytanie z nagłówka, zdania wiążące i *Scope*. Zdania wiążące to każdy akapit przed pierwszym polem wpisu, nie tylko pierwszy, bo wpis ma osobny akapit na każdą dołączoną część pytania (WAY-05). Wybór podaje się częściami produktu, a w dzienniku z sekcjami tematycznymi także sekcjami (punkt 7). Spis nie jest plikiem repozytorium i nie ma czego w nim odświeżać ani pilnować bramką (pytanie 1). Skrypt działa na dzienniku każdego produktu — w produkcie z przypiętej kopii the way — z sekcjami i bez nich.
2. Reguła czytania (`elements/common/way_of_working.md`, „Reading the foundation”, krok 2) i WAY-150 (przez `record-decision`): agent tworzy skryptem z punktu 1 spis swojego wyboru i go czyta; w całości otwiera tylko te decyzje, które praca zmienia, którym przeczy albo na których pytanie proponuje inną odpowiedź — tę ostatnią razem z wariantami odrzuconymi — te nazwane w zadaniu albo w źródle pracy i te, których zdania wiążące zostawiają otwarte, co praca ma zrobić.
3. Do wyboru dochodzi każda decyzja, której zdanie zmieniany test pilnuje linią `decision:`, i jest czytana w całości.
4. Recenzent całej zmiany czyta spis wszystkich wybranych decyzji i podaje w raporcie, ile z nich przeczytał w całości; przeglądanie decyzji po tytułach jako główna lektura znika z reguły i z każdego miejsca the way, które je dziś opisuje (instrukcja recenzenta, sekcja **Unread material** raportu i WAY-326, szablon opisu prośby o scalenie). Zostaje tylko przegląd po pytaniach decyzji spoza sekcji tematów pracy z punktu 7.
5. Dziennik decyzji the way (`foundations/decisions.md`) dostaje 20–30 sekcji tematycznych po kilkanaście wpisów, każdą z nagłówkiem i jednym zdaniem, co obejmuje: numery wpisów bez zmian, treść każdego wpisu bajt w bajt ta sama, co potwierdza skrypt porównujący wpisy przed podziałem i po nim. Listę sekcji i przydział wpisów proponuje cykl; opis prośby o scalenie pokazuje listę sekcji z liczbą wpisów i zdaniem opisu każdej oraz wynik skryptu porównującego, a Mariusz przyjmuje listę przy scaleniu (pytanie 3).
6. Szablon decyzji (`elements/decisions/template.md`, sekcja „Where entries go”, punkt, który otwiera „A product keeps all its decisions in one log”) i WAY-18 (przez `record-decision`): dziennik może mieć sekcje tematyczne; nowy wpis staje na końcu sekcji swojego tematu, a gdy żadna sekcja nie pasuje, autor zakłada nową sekcję na końcu dziennika i opis prośby o scalenie ją wymienia (pytanie 3).
7. Wybór po temacie (`elements/common/way_of_working.md`, „Reading the foundation”, i WAY-150 przez `record-decision`): w dzienniku z sekcjami agent wybiera z listy sekcji (nagłówek i zdanie opisu) sekcje tematów pracy i czyta spis ich decyzji; do tego czyta pytania — same nagłówki — decyzji spoza tych sekcji, których *Scope* nazywa dotkniętą część, i otwiera te, których pytanie wskazuje na związek z pracą (pytanie 2). W dzienniku bez sekcji — jak dziennik gry do jego podziału w projekcie Loop — wybór zostaje po częściach produktu, a spis zastępuje lekturę w całości tak jak w punkcie 2.
8. Pomiar przed i po: `task-cycle/cycle_measures.py` liczy dla każdego agenta cyklu, ile bajtów dziennika decyzji i spisu weszło do jego kontekstu i ile razy, a WAY-347 (przez `record-decision`) dostaje ten pomiar. „Przed”: cykl tego zadania uruchamia rozszerzony skrypt na zapisach sesji ostatniego cyklu gry i ostatniego cyklu the way sprzed zmiany i podaje liczby w opisie prośby o scalenie; „po” przychodzi w pomiarach każdego następnego cyklu (pytanie 4).

### Questions to settle, question 3 (`task.md:67-72`)

- 3. Jak drobne są sekcje dziennika the way i kto przyjmuje ich listę?
  - Answer: 20–30 drobnych tematów; listę sekcji i przydział wpisów proponuje cykl, Mariusz przyjmuje je przy scaleniu z opisu prośby, który pokazuje listę sekcji z liczbą wpisów i zdaniem opisu. Nowy wpis, do którego żadna sekcja nie pasuje, zakłada nową sekcję na końcu dziennika, a opis prośby ją wymienia.
  - Not chosen:
    - sześć obszarów z notatki zadania AIR-518 — prawie pokrywają się z częściami produktu, sekcja „cykl zadania” miałaby ok. 100 wpisów, więc podział niewiele daje ponad wybór po częściach
    - drobne tematy z listą ustaloną w doprecyzowaniu — dłuższe doprecyzowanie, w zamian brak niespodzianek przy scaleniu
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „3 b (z Twoją propozycją: nowa sekcja na końcu dziennika, wymieniona w opisie prośby)”

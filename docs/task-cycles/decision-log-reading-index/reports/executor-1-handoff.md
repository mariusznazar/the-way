# Handoff: executor of slice 1, task `decision-log-reading-index`

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator, which
answers your questions from the task, its sources, the foundation and the code; no answer is the
human's approval. You never ask the human. The cycle has one human contact, the request.

## Where you work, and your stage

- Worktree (your working directory): `the task's worktree`, branch
  `task/decision-log-reading-index`. Slice 1's base is `21ecb627f885de438e2209d7ff5c137b1e1b9d83`; the foundation
  entries of the plan (F1–F10) are already committed on the branch (`dae85e1`, `104e126`, `0023a28`) and the
  head you start from is `0023a28`. Nobody else writes in this worktree while you work.
- Method of your stage: `task-cycle/change/SKILL.md` — read it whole; your variant is "a slice, or the retry of
  a slice", so read `task-cycle/change/slice.md` too, and read a file either names only when its step comes.
- Boundary: slice 1 below and nothing else; no run of the product's full gate (the orchestrator runs it);
  commit by `git add <paths>`, never `git add -A`; commit messages in English, imperative. Return before any
  review.
- Report: `.runs/task-cycles/decision-log-reading-index/reports/executor-1-report.md`, as your method gives it,
  with the own-work check, **Unread material** and **Searches not found or unclear**.
- Risk of the slice: none. The two answers of step 4 (trust boundary yes — `task-cycle/cycle_measures.py`, a later
  slice's file; irreversible operation no) do not touch your files.

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

Your directory for working copies: `.runs/executor-1/`.

## Files of the task and the plan (addresses)

- Frozen task (Polish): `.runs/task-cycles/decision-log-reading-index/task.md`; the plan:
  `.runs/task-cycles/decision-log-reading-index/plan.md`. The passages below are copied from them word for
  word; the files are their addresses.
- The log is now divided into 28 topical sections (`## ` headings); the list of sections, with each
  heading, its sentence, its count and its numbers, is in
  `.runs/task-cycles/decision-log-reading-index/reports/foundation-entries-report.md` under "Entries"/the
  list of sections (read only what your slice's checks need).

## Foundation entries to read, by identifier, with their ranges in `foundations/decisions.md` at your head

Each runs from its heading to the next `#` heading; read each whole.
WAY-150 (lines 1465–1589; as rewritten by the plan's F1–F3, F5, F6), WAY-18 (713–764; as F4 leaves it),
WAY-05 (604–654), WAY-09 (11–79), WAY-38 (2511–2536), WAY-344 (2707–2819).
Other files: `foundations/part_map.md` lines 65–75 (elements-common); `foundations/invariants.md` lines 86–94
(tracked-file-private-paths), 116–144 (script-language, script-imports, script-subprocesses), 348–356
(cross-part-imports); `elements/common/way_of_working.md` lines 58–100 ("Reading the foundation" — it still
describes the earlier reading; slice 3 rewrites it; read it for the search of *Scope* the script replaces);
`elements/common/foundation_check.py` lines 1–160, 236–345, 974–989; `elements/common/test_foundation_check.py`
lines 1–30. (Slice 2 and later slices do not exist yet; the files are as at the base unless the lines above say
otherwise.)

## Slice 1 (copied word for word from the plan)

### Slice 1 — The index script

- **Goal:** a script of the-way, `elements/common/decision_index.py`, writes to a file the agent
  names the index of the decisions it selects from a product's decision log, with its tests in
  `elements/common/test_decision_index.py`, and the sentence of `elements-common` in
  `foundations/part_map.md` names the script among what the part answers for. The script works on
  the log of any product, run from the product's pinned copy of the-way as from the-way itself,
  with sections and without them: it takes the product's root as an optional positional argument,
  the working directory by default, and reads `foundations/decisions.md` under it, reading a
  byte-order mark and CRLF line endings as well as LF. Its selection is given by switches:
  `--part ID` (repeatable) selects the decisions whose *Scope* names the part as a whole item, read
  as the reading rule reads *Scope* today (each `- **Scope:**` line with its indented continuation
  lines, items joined by `,` or ` · `); `--section HEADING` (repeatable) selects every decision of
  that topical section, a section being a `## ` heading of the log other than "Withdrawn
  identifiers", named by its heading's text; `--decision NUMBER` (repeatable) adds a decision by its
  number; `--output PATH` names the file it writes, in UTF-8. For each selected decision the index
  gives its number, its question as its heading gives it, its binding sentences — every paragraph
  before its first field, not the first only, as the check's `binding` reads them (WAY-05) — and
  its *Scope*. Where `--section` and `--part` are both given, the index adds after the decisions of
  the sections the headings alone — number and question — of the decisions outside those sections
  whose *Scope* names a given part. The switch `--sections` writes instead the list of the log's
  sections, each with its heading, its sentence and the number of its entries. The index opens with
  one fixed title line that holds the script's name, which Slice 5 recognises in a tool's output,
  and states how many decisions it lists in full and how many by heading alone; the docstring names
  that line, the usage and the exit codes. Exit code 0 when it has written the file; 2 with
  `Error: <message>` on stderr and nothing written for a log it cannot read, a section the log does
  not hold, a number the log does not hold, a selection given no switch, and — WAY-344 — a decision
  that lacks *Scope* or a heading of the log's form, the message naming the file, the entry and the
  field. The script reuses the reading functions of `elements/common/foundation_check.py` (`blocks`,
  `fields`, `binding`) by import, rather than copying them, and needs no git. Each reading the
  script makes has one test that gives the log without a field it needs and asserts the message
  that names it (WAY-344); the tests build their logs in temporary directories, with no absolute
  path in a tracked file.
- **Change:** `elements/common/decision_index.py` · `elements/common/test_decision_index.py` ·
  `foundations/part_map.md`
- **Read:** `.runs/task-cycles/decision-log-reading-index/task.md:33-42` To do ·
  `.runs/task-cycles/decision-log-reading-index/task.md:56-66` Questions to settle (questions 1 and
  2) · `.runs/task-cycles/decision-log-reading-index/task.md:123-135` Settlements to record ·
  WAY-150 as Foundation entries F1–F3, F5, F6 leave it · WAY-18 as F4 leaves it ·
  `foundations/decisions.md:158-207` WAY-05 · `foundations/decisions.md:268-335` WAY-09 ·
  `foundations/decisions.md:1093-1117` WAY-38 · `foundations/decisions.md:8245-8356` WAY-344 ·
  `foundations/part_map.md:65-75` elements-common · `foundations/invariants.md:86-94`
  tracked-file-private-paths · `foundations/invariants.md:116-144` script-language, script-imports,
  script-subprocesses · `foundations/invariants.md:348-356` cross-part-imports ·
  `elements/common/way_of_working.md:58-100` Reading the foundation ·
  `elements/common/foundation_check.py:1-160` · `elements/common/foundation_check.py:236-345` ·
  `elements/common/foundation_check.py:974-989` · `elements/common/test_foundation_check.py:1-30`
- **Model:** cheaper
- **Risk:** none
- **Checks:** first a failing test of the index of a two-section log;
  `python -B -m unittest discover -s elements/common -p test_decision_index.py`; on the-way itself,
  after F10, `python -B elements/common/decision_index.py --sections --output
  .runs/<the executor's directory>/sections.md` lists 20–30 sections, and `python -B
  elements/common/decision_index.py --part task-cycle --output .runs/<the executor's
  directory>/index.md` writes an index whose count matches the decisions whose *Scope* names
  `task-cycle`; `python -B elements/common/foundation_check.py --skip-test-citations` reports no
  error the slice caused
- **Depends on:** F2 · F3 · F6 · F10

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

### Questions to settle, questions 1 and 2 (`task.md:56-66`)

- 1. Gdzie stoi spis i jak zostaje aktualny?
  - Answer: bez pliku — agent uruchamia skrypt z częściami produktu (po podziale także z tematami) i dostaje do pliku roboczego spis dokładnie swojego wyboru; spis nigdy nie jest nieświeży, nie ma czego pilnować bramką ani scalać, a wyszukiwanie decyzji po częściach robi skrypt. Odpada zdanie z wcześniejszego kierunku „Bramka testów zgłasza spis nieświeży”.
  - Not chosen:
    - plik w repozytorium, odświeżany skryptem po każdej zmianie dziennika, bramka zgłasza nieświeży — każda zmiana decyzji musi pamiętać o odświeżeniu; dwie równoległe gałęzie dopisujące decyzję kłócą się przy scalaniu także o plik spisu; w produkcie nieświeży spis musiałby zgłaszać skrypt kontroli fundamentu, a instalator zakładać plik
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „1 b”
- 2. Jak agent wybiera decyzje w dzienniku podzielonym na tematy?
  - Answer: tematy plus zabezpieczenie — spis decyzji z sekcji tematów pracy, do tego same pytania decyzji spoza tych sekcji, których *Scope* nazywa dotkniętą część, i otwarcie tych, których pytanie wskazuje na związek; dla tego zadania to ok. 16 KB nagłówków, ok. 4 tys. tokenów więcej.
  - Not chosen:
    - tylko tematy — najtańsze, ale decyzja z innego tematu, która rządzi dotkniętą częścią, przepada bez śladu
    - tematy dla wszystkich poza recenzentem całej zmiany, który czyta spis całego wyboru po częściach — recenzent nic nie zyskuje na podziale (dla tego zadania ok. 33 tys. tokenów spisu)
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14: „2 b”

### Settlements to record (`task.md:123-135`)

## Settlements to record

Candidates: 9 shown, 7 accepted — 2026-11-14

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Agent czyta spis swojego wyboru decyzji, a w całości otwiera tylko te, które praca zmienia, którym przeczy albo na których pytanie proponuje inną odpowiedź (z wariantami odrzuconymi), te nazwane w zadaniu albo w źródle pracy i te, których zdania wiążące zostawiają otwarte, co praca ma zrobić; recenzent całej zmiany czyta spis całego wyboru i podaje, ile przeczytał w całości. | sentence of WAY-150 | pytanie 0 | czy dalej czytać decyzje w całości, a recenzent po tytułach |
| 2 | Spis nie jest plikiem repozytorium: skrypt the way wypisuje na żądanie spis wybranych decyzji — numer, pytanie, zdania wiążące, *Scope*. | sentence of WAY-150 | pytanie 1 | plik spisu w repozytorium z testem świeżości w bramce |
| 3 | W dzienniku z sekcjami tematycznymi agent wybiera sekcje tematów pracy i czyta spis ich decyzji, a pytania decyzji spoza tych sekcji, których *Scope* nazywa dotkniętą część, przegląda i otwiera te, które wskazują na związek. | sentence of WAY-150 | pytanie 2 | wybór wyłącznie po temacie, bez zabezpieczenia |
| 4 | Dziennik decyzji ma sekcje tematyczne bez zmiany numerów; nowy wpis staje na końcu sekcji swojego tematu, a gdy żadna nie pasuje, w nowej sekcji na końcu dziennika, którą opis prośby o scalenie wymienia. | sentence of WAY-18 | pytanie 3 | gdzie postawić nowy wpis i czy autor może założyć sekcję |
| 5 | Decyzja, której zdanie zmieniany test pilnuje linią `decision:`, wchodzi do wyboru lektury i jest czytana w całości. | sentence of WAY-150 | *To do* 3; *Context*, uwaga recenzenta prośby #120; przyjęte: doradca dnia w imieniu Mariusza, 2026-11-14 | czy zmiana testu z linią `decision:` prowadzi do lektury tej decyzji |
| 6 | W dzienniku bez sekcji tematycznych wybór zostaje po częściach produktu, a spis zastępuje lekturę decyzji w całości. | sentence of WAY-150 | *To do* 7; przyjęte: doradca dnia w imieniu Mariusza, 2026-11-14 | czy w dzienniku gry, do jego podziału, dalej czytać decyzje w całości |
| 7 | Pomiary kontekstu cyklu liczą dla każdego agenta, ile bajtów dziennika decyzji i spisu weszło do jego kontekstu i ile razy. | sentence of WAY-347 | pytanie 4 | jednorazowy pomiar poza procesem |

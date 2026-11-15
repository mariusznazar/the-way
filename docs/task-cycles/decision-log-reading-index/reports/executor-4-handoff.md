# Handoff: executor of slice 4, task `decision-log-reading-index`

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator, which
answers your questions from the task, its sources, the foundation and the code; no answer is the
human's approval. You never ask the human. The cycle has one human contact, the request.

## Where you work, and your stage

- Worktree (your working directory): `the task's worktree`, branch
  `task/decision-log-reading-index`. The head you start from is `dbdfdad`; the foundation entries of the plan
  (F1–F10) and the earlier slices are already committed on the branch. Nobody else writes in this worktree while
  you work.
- Method of your stage: `task-cycle/change/SKILL.md` — read it whole; your variant is "a slice, or the retry of
  a slice", so read `task-cycle/change/slice.md` too, and read a file either names only when its step comes.
- Boundary: slice 4 below and nothing else; no run of the product's full gate (the orchestrator runs it);
  commit by `git add <paths>`, never `git add -A`; commit messages in English, imperative. Return before any review.
- Report: `.runs/task-cycles/decision-log-reading-index/reports/executor-4-report.md`, as your method gives it, with
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

Your directory for working copies: `.runs/executor-4/`.

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

Decisions in `foundations/decisions.md`, each whole (to the next `#` heading), in the wording now committed: WAY-150 (lines 1466–1591), WAY-18 (713–765), WAY-287 (6455–6570). Files: `elements/common/way_of_working.md` (as slice 3 left it, "Reading the foundation"), `task-cycle/review/whole_change.md`. Every file you change, whole, before you change it: `task-cycle/review/SKILL.md`, `task-cycle/skill/SKILL.md`, `task-cycle/skill/request_template.md`. Note: WAY-326, whose rule you carry in `task-cycle/skill/SKILL.md`, is withdrawn and stays withdrawn (its rule now stands in the paragraph of that file about the stage reports); you do not change `foundations/decisions.md`.

## Slice 4 (copied word for word from the plan, "The reviewer, its report and the request")

### Slice 4 — The reviewer, its report and the request

- **Goal:** the reading by title as the main reading leaves every file of `task-cycle` that
  describes it today, and they give the reading of F1 and F3 and the item of F8. In
  `task-cycle/review/SKILL.md`, section 1 has the reviewer of the whole change select by "Reading
  the foundation", read the index of its whole selection, open whole the decisions that method names
  and count how many it read whole, for its report; the paragraph **Unread material** opens, in the
  review of the whole change, with how many decisions of the index it read whole, and goes on with
  each decision that bears on the change and stayed unread and each guideline file it did not read
  whole. In `task-cycle/skill/SKILL.md`, the sentence "A decision the reviewer of the whole change
  read by title as WAY-150 gives is no gap" becomes the same for a decision the reviewer knows from
  the index (the rule that stood in WAY-326). In `task-cycle/skill/request_template.md`, item 14 of
  the top part follows F8 — an item where the reviewer did not read the index of its whole selection
  or named a decision bearing on the change as unread, with how many decisions of the index it read
  whole — and the lower part's **Foundation entries** names each topical section of the decision
  log that the change opens, with its sentence (F4).
- **Change:** `task-cycle/review/SKILL.md` · `task-cycle/skill/SKILL.md` ·
  `task-cycle/skill/request_template.md`
- **Read:** `.runs/task-cycles/decision-log-reading-index/task.md:33-42` To do ·
  `.runs/task-cycles/decision-log-reading-index/task.md:79-91` Context ·
  `.runs/task-cycles/decision-log-reading-index/task.md:123-135` Settlements to record · WAY-150 as
  F1–F3, F5, F6 leave it · WAY-18 as F4 leaves it · WAY-287 as F8 leaves it ·
  `elements/common/way_of_working.md` · `task-cycle/review/whole_change.md`
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B -m unittest discover -s task-cycle -p test_request_check.py`;
  `python -B -m unittest discover -s task-cycle -p test_remarks_check.py`; a search of
  `task-cycle/` for "by title" and "title only" finds nothing that describes the reading by title
- **Depends on:** Slice 3 · F1 · F3 · F4 · F8

## The passages of the task the slice's *Read* names (copied word for word)

### To do — passage (`task.md:33-42`)

### To do

1. Spis decyzji: skrypt the way, z testami, wypisuje do pliku, który wskaże agent, spis wybranych decyzji dziennika produktu — dla każdej decyzji jej numer, pytanie z nagłówka, zdania wiążące i *Scope*. Zdania wiążące to każdy akapit przed pierwszym polem wpisu, nie tylko pierwszy, bo wpis ma osobny akapit na każdą dołączoną część pytania (WAY-05). Wybór podaje się częściami produktu, a w dzienniku z sekcjami tematycznymi także sekcjami (punkt 7). Spis nie jest plikiem repozytorium i nie ma czego w nim odświeżać ani pilnować bramką (pytanie 1). Skrypt działa na dzienniku każdego produktu — w produkcie z przypiętej kopii the way — z sekcjami i bez nich.
2. Reguła czytania (`elements/common/way_of_working.md`, „Reading the foundation”, krok 2) i WAY-150 (przez `record-decision`): agent tworzy skryptem z punktu 1 spis swojego wyboru i go czyta; w całości otwiera tylko te decyzje, które praca zmienia, którym przeczy albo na których pytanie proponuje inną odpowiedź — tę ostatnią razem z wariantami odrzuconymi — te nazwane w zadaniu albo w źródle pracy i te, których zdania wiążące zostawiają otwarte, co praca ma zrobić.
3. Do wyboru dochodzi każda decyzja, której zdanie zmieniany test pilnuje linią `decision:`, i jest czytana w całości.
4. Recenzent całej zmiany czyta spis wszystkich wybranych decyzji i podaje w raporcie, ile z nich przeczytał w całości; przeglądanie decyzji po tytułach jako główna lektura znika z reguły i z każdego miejsca the way, które je dziś opisuje (instrukcja recenzenta, sekcja **Unread material** raportu i WAY-326, szablon opisu prośby o scalenie). Zostaje tylko przegląd po pytaniach decyzji spoza sekcji tematów pracy z punktu 7.
5. Dziennik decyzji the way (`foundations/decisions.md`) dostaje 20–30 sekcji tematycznych po kilkanaście wpisów, każdą z nagłówkiem i jednym zdaniem, co obejmuje: numery wpisów bez zmian, treść każdego wpisu bajt w bajt ta sama, co potwierdza skrypt porównujący wpisy przed podziałem i po nim. Listę sekcji i przydział wpisów proponuje cykl; opis prośby o scalenie pokazuje listę sekcji z liczbą wpisów i zdaniem opisu każdej oraz wynik skryptu porównującego, a Mariusz przyjmuje listę przy scaleniu (pytanie 3).
6. Szablon decyzji (`elements/decisions/template.md`, sekcja „Where entries go”, punkt, który otwiera „A product keeps all its decisions in one log”) i WAY-18 (przez `record-decision`): dziennik może mieć sekcje tematyczne; nowy wpis staje na końcu sekcji swojego tematu, a gdy żadna sekcja nie pasuje, autor zakłada nową sekcję na końcu dziennika i opis prośby o scalenie ją wymienia (pytanie 3).
7. Wybór po temacie (`elements/common/way_of_working.md`, „Reading the foundation”, i WAY-150 przez `record-decision`): w dzienniku z sekcjami agent wybiera z listy sekcji (nagłówek i zdanie opisu) sekcje tematów pracy i czyta spis ich decyzji; do tego czyta pytania — same nagłówki — decyzji spoza tych sekcji, których *Scope* nazywa dotkniętą część, i otwiera te, których pytanie wskazuje na związek z pracą (pytanie 2). W dzienniku bez sekcji — jak dziennik gry do jego podziału w projekcie Loop — wybór zostaje po częściach produktu, a spis zastępuje lekturę w całości tak jak w punkcie 2.
8. Pomiar przed i po: `task-cycle/cycle_measures.py` liczy dla każdego agenta cyklu, ile bajtów dziennika decyzji i spisu weszło do jego kontekstu i ile razy, a WAY-347 (przez `record-decision`) dostaje ten pomiar. „Przed”: cykl tego zadania uruchamia rozszerzony skrypt na zapisach sesji ostatniego cyklu gry i ostatniego cyklu the way sprzed zmiany i podaje liczby w opisie prośby o scalenie; „po” przychodzi w pomiarach każdego następnego cyklu (pytanie 4).

### Context (`task.md:79-91`)

## Context

- Kierunek Mariusz wybrał 2026-11-12 przy przeglądzie raportu o dzienniku decyzji (`the author's private report on slimming the decision log`, „Decyzje dla Mariusza”, decyzja 1, i karty D2, D3, D7).
- Brzmienie 7h raportu, od którego warto zacząć punkt 2: „Read the index line of each decision found — its question, binding sentences and *Scope*. Read whole each decision the work changes, goes against or proposes another answer to, each one the task names, and each whose binding sentences leave open what the work has to do. The reviewer of the whole change reads the index of every decision found and states how many it read whole.”
- Podział dziennika the way na tematy przeszedł tu z zadania AIR-518 („Ułatwić rozumienie i znajdowanie zasad the way…”, jego punkt 3), które zostaje z punktami 1 i 2.
- Dziennik gry dzieli się w zadaniu porządków dziennika gry w projekcie Loop, po wyprowadzeniu z niego wpisów, które decyzjami nie są.
- Punkt 3 przyszedł z zadania zbiorczego „the way: drobne poprawki po PR-ach #117–#121” (pozycja 3, sprawa 3), które go tu przekazało; cytat recenzenta: „WAY-150's selection does not take in the decision a test holds by a line `decision:` … A reviewer or author altering such a test is not led to the decision whose sentence it holds, except through the line itself”.
- Zadanie o przeglądzie całej zmiany, z którym wcześniejsza notatka kazała to zgrać, jest scalone (the way, prośba #109) i nie zmieniło reguły czytania decyzji.
- Rachunek raportu dla gry (ustalenie 4, „bajty przez cztery”, nie tokenizer): dziś recenzent czyta ok. 31 tys. tokenów i zna ok. 15% zdań wiążących; sam spis — ok. 54 tys. i 100%; spis po podziale na tematy — 10–13 tys. i 100% w tematach zadania; założenie „3–5 tematów na zadanie” jest autora raportu, nie pomiar.
- `task-cycle/cycle_measures.py` liczy już z zapisów sesji Claude Code i Codex, jak agenci jednego cyklu używają kontekstu, a cykl uruchamia go w każdym przebiegu; jego zmiana zaczyna nową serię tych pomiarów w audycie procesu (`process-audit/SKILL.md`, punkt „Measures are compared inside a series only”).
- Miejsca, które dziś opisują lekturę po tytułach: `elements/common/way_of_working.md` („Reading the foundation”, krok 2), `task-cycle/review/SKILL.md` (punkt „For the review of the whole change” i sekcja **Unread material**), `task-cycle/skill/SKILL.md` (zdanie „A decision the reviewer of the whole change read by title”), `task-cycle/skill/request_template.md` (akapit o tym, ile recenzent przeczytał w całości).
- Szablon decyzji mówi dziś w „Where entries go”: „the log has no topical sections, and a new entry goes at its end (WAY-18)”.
- Cały dokument przyjął doradca dnia w imieniu Mariusza, 2026-11-14.

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

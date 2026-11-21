# Handoff — executor of slice 6

You make slice 6 of a planned change in a task cycle of the-way. The person who requested the cycle has delegated every intermediate choice to the orchestrator; no answer you get is that person's approval. You never ask the human; questions go back to the orchestrator in your report.

- Worktree (your working directory for everything): `the worktree root`, task branch `task/small-fixes-from-ai-review-and-audit`. Slice 6's base: `3b34de039d1b31e63801df9162e200e27b31dd9c` (`git rev-parse HEAD` now). Start from the worktree's root.
- Method: `task-cycle/change/SKILL.md` (`make-change`) in the worktree, read whole. Your variant, in the words of its table's row: "a slice, or the retry of a slice". Read `task-cycle/change/slice.md` beside it. The skill tool is not yours: a skill a file names is the `SKILL.md` whose frontmatter `name:` is that name, read as a file under the same root.
- Stage and boundary: slice 6 only. You do not start slice 7.
- Report path: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/reports/executor-6-report.md`.
- Your directory for working copies: `.runs/executor-6/`.
- Answers of the cycle's step 4: trust boundary yes for the change as a whole (not for this slice, whose risk is `none` — but `process-audit/` holds trust-boundary files (`process-audit/audit_count.py`, `record_reading.py`, `problem_register.py`, `record_items.py`, `audit_shared.py`): this slice changes none of them, and what it reads from them it reads through their existing functions); irreversible operation no.
- Frozen task: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md` (open only the lines the slice's *Read* names).

## Your slice, word for word from the plan

### Slice 6 — the audit's image of each series, and Q1 as numbers of cycles

- **Goal:** the result of `process-audit/audit_count.py` gives, for each series of each of its four kinds, an image of the whole series, and Q1 of every group of cycles is the numbers of its cycles; the rules of Row 1 and Row 3 of the plan's *Foundation entries* (and the task's point 4) are what it makes true. The new module `process-audit/series_summary.py` turns a list of cycles into the cells of an image; it is imported, never run, and runs nothing when imported (the guideline of the kind `shared-module`), and it takes from `process-audit/version_analysis.py` the functions it needs that depend on cycles alone, such as the median, the number of a mechanism measure and the gate values, which move there with no change of what they do, so that `process-audit/version_analysis.py` grows by little and imports the new module and not the other way round. The image of a series of the cost: its cycles, those with a known cost, and the median cost of those, with no Q3. The image of a series of the count of remarks: Q1 as `yes n · no n · unknown n`, the number of the series' cycles whose own answer is each; Q2 as the sums of the slices planned and of the slices returned too large over the cycles whose plans are read, with the answer taken from those sums by the rule that `too_large_of` applies to one version today (the answer is unknown where a plan of the series is not read), and *Plans read*; no Q3. The image of a series of the mechanism measures: for each measure the number of cycles that give a value and their median, with no *falls*. The image of a series of the gate times: for the total and for each directory any run has, the runs compared (the runs that passed with no other gate run beside them) with their number and median, and the runs not compared with their number and median, shown apart, with no *falls* (WAY-350). The report writes the image of a series as a table under the series' heading and before its table per version; the tables per version stay, and a version's Q1 cell is now the same form, `yes n · no n · unknown n` over the cycles of the version, so that a version has no Q1 answer of its own: the line of *Unknown values* that gave a reason for a version's Q1 answer being unknown is no longer written, and what each cycle gives as unknown stays with its reason; the Q2 and Q3 cells and the reasons of the versions stay as they are. The text of `process-audit/audit_report.py` that says Q1 is `yes`, `no` or `unknown`, and the docstring of `process-audit/version_analysis.py`, say what is now true. The old assertions about a version's Q1 cell in `process-audit/test_process_versions.py` change to the new form, each with its cause named in the test: Row 3 of the settlements; the new tests, in `process-audit/test_process_versions.py` and the new file `process-audit/test_series_summary.py`, take their input and their expected values written out by hand: an image of a series of two versions with two cycles each for each of the four kinds, Q1 numbers over a series whose cycles answer `yes`, `no` and `unknown`, the Q2 sums where all plans are read and where one is not, the gate image with compared and not compared runs, and a series with one cycle.
- **Change:** `process-audit/series_summary.py` · `process-audit/version_analysis.py` · `process-audit/audit_report.py` · `process-audit/test_process_versions.py` · `process-audit/test_series_summary.py`
- **Read:** `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md:35-35` *To do* point 4 · `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md:56-61` *Questions to settle*, what point 4 shows · `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md:69-74` *Questions to settle*, the answers Q1 to Q3 for a group · `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md:87-90` *Context*, the lines on the series and Q1 · `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md:111-112` *Decisions in play*, WAY-339 and WAY-350 · `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md:120-122` *Settlements to record*, rows 1 and 3 · Row 1 and Row 3 of the plan's *Foundation entries* · `foundations/decisions.md:8607-8746` WAY-339 · `foundations/decisions.md:8747-8783` WAY-350 · `foundations/decisions.md:8890-8987` WAY-416 · `foundations/decisions.md:11087-11134` WAY-385 · `foundations/decisions.md:6820-6857` WAY-365 · `foundations/invariants.md:411-420` audit-series-script-paths · `foundations/invariants.md:441-470` ruff-blocking-rules, formatter-layout, function-and-file-size · `foundations/part_map.md:128-143` process-audit · `guidelines/coding.md` · `guidelines/coding-measuring-report.md` · `guidelines/coding-shared-module.md` · `guidelines/testing.md` · `process-audit/record_reading.py:166-232` GateRun, Cycle and Read · `process-audit/problem_register.py:60-100` Problem and Register · `process-audit/audit_shared.py` · `process-audit/test_audit_count.py:1-355` the fixtures Repository and AuditCountCase
- **Model:** same — a new analysis over four kinds of series with decisions of its own on the form of the tables, which must keep every figure that a version already gives
- **Risk:** none
- **Checks:** the new tests and the changed assertions fail on the base and then pass: `python -B -m unittest discover -s process-audit -p "test_series_summary.py"` and `python -B -m unittest discover -s process-audit -p "test_process_versions.py"`; `python -B gate/run_tests.py process-audit` passes (the invariant `audit-series-script-paths` among its tests); `python -B gate/run_tests.py agent-instructions` passes (no function over 110 lines, no file over 1200).
- **Depends on:** Slice 1 · Row 1 · Row 3


## Passages of the task your slice's *Read* names, word for word (file: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md`)

### Lines 35-35

4. Liczenie audytu (`process-audit/audit_count.py`) podaje dla każdej serii obraz całej serii, każdej z tym, co dziś niesie jej rodzaj, bez Q3 i bez „spada”: seria kosztu — medianę kosztu ze wszystkich jej cykli ze znanym kosztem; seria liczby uwag — odpowiedzi Q1 i Q2 ze wszystkich jej cykli; seria pomiarów mechanizmu — medianę każdego pomiaru; seria czasów bramki — medianę z jej przebiegów porównywanych, a przebiegi nieporównywane osobno (ich liczba i mediana), jak w wierszach per wersja (WAY-350). Odpowiedzi mają postać, którą daje odpowiedź na pytanie o odpowiedzi Q1–Q3 dla grupy cykli niżej. Wiersze per wersja zostają, a ich Q1 przechodzi na tę samą postać liczb cykli (`yes n · no n · unknown n`).

### Lines 56-61

- Co pokazuje punkt 4 audytu zamiast samych wierszy per wersja?
  - Answer: obraz każdej serii (to, co niesie jej rodzaj, ze wszystkich jej cykli, bez Q3 i bez „spada”; Q3 i „spada” tylko w porównaniach dwóch grup) oraz porównanie „przed i po zmianie” wewnątrz serii — cykle na wersjach z daną zmianą wobec cykli na wersjach bez niej, obie grupy w tej samej serii; reguła „Set no number of one series beside a number of another […] and no week's count beside the week before” zostaje bez zmian.
  - Not chosen:
    - Sam obraz serii, bez porównań — mówi, jak jest, ale nie daje podstawy do decyzji, czy zmiana pomogła; audyty dalej odkładałyby ją w tym miejscu.
    - Porównywanie serii z serią — wymaga zmiany reguły, która zabrania stawiać liczby jednej serii obok liczb innej, a różnicę między seriami robi częściowo zmiana narzędzia pomiaru, której nie da się oddzielić od zmiany procesu.
  - Source: Mariusz, 2026-11-21, audyt procesu i zapis zadania („obraz serii plus porównanie »przed i po zmianie« wewnątrz serii”).

### Lines 69-74

- Jak wyglądają odpowiedzi Q1–Q3 dla grupy wielu cykli (obraz serii i każda grupa porównania „przed i po”)?
  - Answer: liczby zamiast jednego słowa, w jednej formie wszędzie: Q1 dla każdej grupy cykli — wersji, obrazu serii i każdej strony porównania „przed i po” — to liczba cykli z każdą odpowiedzią (`yes n · no n · unknown n`); Q2 to sumy odcinków planowanych i zbyt dużych z odpowiedzią z tych sum, jak dziś dla wersji; Q3 i „spada” pomiarów mechanizmu i czasów bramki stoją tylko tam, gdzie są dwie grupy — wersja wobec poprzedniej wersji serii, jak dziś, i mediana po poprawce wobec mediany przed nią; obraz serii daje medianę i liczbę cykli ze znaną wartością, bez Q3.
  - Not chosen:
    - Te same reguły co dla wersji, przyłożone do całej grupy — Q1 w każdej dłuższej serii wychodzi prawie na pewno `yes`, bo wystarczy jeden cykl, a Q3 w jednej grupie nie ma z czym porównać.
    - Liczby tylko dla obrazu serii i porównań „przed i po”, a w wierszach per wersja Q1 jak dziś — dwie postaci tej samej odpowiedzi w jednym wyniku.
  - Source: doradca dnia w imieniu Mariusza (tryb samodzielny), 2026-11-21: „b — liczby zamiast jednego słowa; tylko tak audyt pokazuje stan taki, jaki jest, a »spada« liczy się tam, gdzie są dwie grupy. Słaby punkt (dwie postaci Q1) usuń, zamiast go przyjmować: Q1 w wierszach per wersja też liczbami (tak · nie · nieznane), jeśli to zmienia tylko formę wyniku liczenia, a nie zapisane dane ani coś, co ten wynik czyta maszynowo”; warunek sprawdzony 2026-11-21: wynik liczenia czytają tylko `process-audit/audit_report.py` (który go pisze), `process-audit/SKILL.md` (człowiek) i `process-audit/test_audit_count.py` w the-way @ `19e5774a`, a żaden skrypt vaulta nie czyta jego kolumny Q1; żadna decyzja fundamentu nie ustala formy odpowiedzi Q1.

### Lines 87-90

- Porównanie „przed i po” to ten sam mechanizm co ocena poprawki w punkcie 2 audytu (`process-audit/SKILL.md`, reguła „Whether a fix works is read from the version, never from the date”, około linii 79), tylko zbiera wiele wersji naraz.
- Seria to odcinek o stałym narzędziu pomiaru (WAY-339), więc liczenie w jej obrębie nie łamie reguły porównywania tylko wewnątrz serii (`process-audit/SKILL.md`, około linii 52).
- Dziś odpowiedź Q1 dla wersji brzmi `yes`, gdy choć jeden jej cykl daje `yes`, a `no`, gdy każdy daje `no` (`process-audit/version_analysis.py`, `contradiction_of`); Q2 liczy się z sum odcinków planów wersji; Q3 porównuje medianę kosztu z poprzednią wersją tej samej serii.
- Wynik liczenia z 2026-11-21 ma 7 serii kosztu i 54 serie liczby uwag, bo serię uwag przerywa każda zmiana w katalogach recenzenta i autora.

### Lines 111-112

- WAY-339 — dostaje zdania z wierszy 1–2 *Settlements to record*, bez zmiany tego, co już mówi; punkty 4–7 liczą w obrębie serii: „The audit compares each measure only within a series of its own kind, and judges a version of the process by the cycles that ran on it, never one week against another; […]”; poprawka z punktu 8 zaczyna nową serię czasów bramki: „a new series of those starts only with a change of the script that counts them or of the script that records them, and, for the times of the gate, also with a change of the test runner of the process”.
- WAY-350 — punkty 4–5 dokładają porównania czasów bramki ponad wersją, z tym samym ograniczeniem do przebiegów porównywanych: „The audit compares the times of the gate between versions of the process — the median of each version and whether it falls against the previous version of the same series — only over the runs that passed and during which no other such run was going, and shows the other runs apart.”

### Lines 120-122

| 1 | Punkt 4 audytu pokazuje obraz każdej serii (to, co niesie jej rodzaj, ze wszystkich jej cykli, bez Q3 i bez „spada”; Q3 i „spada” tylko w porównaniach dwóch grup) oraz porównanie „przed i po zmianie” wewnątrz serii — cykle na wersjach z daną zmianą wobec cykli na wersjach bez niej, obie grupy w tej samej serii. | sentence of WAY-339 | *Questions to settle*: „Co pokazuje punkt 4 audytu zamiast samych wierszy per wersja?” | czy grupowanie po wersji wewnątrz serii wiąże dalej, czy jest tylko formą tego wyniku, którą późniejsza zmiana może zastąpić porównaniem po dacie |
| 2 | Porównanie „przed i po” dostaje każda naprawiona sprawa z rejestru problemów (z commitem poprawki). | sentence of WAY-339 | *Questions to settle*: „Które zmiany dostają porównanie »przed i po« wewnątrz serii?” | po jakich zmianach liczenie rozbiera serię: po każdym scaleniu, po liście prowadzonej ręcznie czy po poprawkach z rejestru |
| 3 | Odpowiedź Q1 dla każdej grupy cykli — wersji, obrazu serii i strony porównania — to liczby cykli (tak · nie · nieznane), a Q3 i „spada” stoją tylko tam, gdzie są dwie grupy. | decision | *Questions to settle*: „Jak wyglądają odpowiedzi Q1–Q3 dla grupy wielu cykli…?” | czy Q1 grupy brzmi `yes`, gdy jeden cykl daje `yes`, jak dziś dla wersji |

## The foundation entries that the plan's *Foundation entries* rows 1 and 3 became (commit `a946862b`)

- Rows 1 and 2: two sentences added to WAY-339 and a clause of its *Verification*: `foundations/decisions.md:8607-8758` (the added sentences are at lines 8627-8633 and in the *Verification* near 8665-8680).
- Row 3: the new decision WAY-417, `foundations/decisions.md:8995-9038`.

## Notes of the orchestrator for this slice

- The slice-1 move already happened: the tests of the versions are in `process-audit/test_process_versions.py` (it defines `HERE` itself and imports the fixtures it uses from `process-audit/test_audit_count.py`); `process-audit/test_audit_count.py` keeps the fixtures `Repository` and `AuditCountCase`. The *Read* range `process-audit/test_audit_count.py:1-355` for the fixtures is current.
- The rule from sums to the answer of Q2 stands in code only (`too_large_of` in `process-audit/version_analysis.py`): WAY-417 says "the answer that those sums give"; read the code for it, and put the same rule in the image of a series.
- The decision WAY-417 and the sentences of WAY-339 (rows 1 and 3) are the rules this slice makes true: read them whole. Where the Goal below and those entries differ, the entries and the task's passages above hold; name the difference in your report.
- The new module is a shared module (`guidelines/coding-shared-module.md`): it is imported, never run, and runs nothing at import; it opens with a description of its use. The functions it takes from `process-audit/version_analysis.py` move with no change of what they do; `process-audit/version_analysis.py` imports the new module and not the other way round (check the invariant `cross-part-imports`/`script-imports` through `python -B gate/run_tests.py agent-instructions`, which also holds the size thresholds: no function over 110 lines, no file over 1200).
- The new test file `process-audit/test_series_summary.py` is a file of tests that git tracks only after you `git add` it; run the `agent-instructions` check after you commit or `git add`, so that it sees the file (a lesson of slice 1: a check run before the file was tracked passed, and failed afterwards).
- Tests: take the input and the expected values written out by hand (`guidelines/testing.md`), each changed assertion about a version's Q1 cell with its cause named in the test.

## What you return and keep (WAY-148, WAY-164, WAY-260)

- Make the slice from its section above and the *Read* it names; do not open the plan. Where the plan and the code disagree, `slice.md` says what to do.
- Write the failing test first where the slice changes behaviour, and keep the failing run's command and exit code for your report. A check you report carries its command and its exit code; run only the focused checks the slice's *Checks* names, never the product's gate (`python -B gate/run_tests.py` with no directory), which the orchestrator or CI runs.
- Commit your work on the task branch, by path (`git add <path> <path>`, never `git add -A`, `git add .` or `git commit -a`), with commit messages in English; leave the worktree clean. Name your commits in the report. Do not push.
- Your report holds: the status (`done`, `done with concerns`, `questions`, `returned` or `blocked`, as the method gives), your commits, each check with its command and exit code, the own-work check the method asks for (the weakest point of your work, how you tested it, what it showed), each reach beyond this handoff (what, where, why), each working copy (where it stood and that you removed it, or the remainder with its full path), **Unread material:** each file, entry or passage this handoff names that you did not read whole or read in part, or `none`, and **Searches not found or unclear:** each thing you looked for and did not find or that was unclear, or `none`. Return the status, your commits, a one-line check result naming what failed or did not run, and the report's path.
- Do not read `cycle.md` or any file of `.runs/task-cycles/small-fixes-from-ai-review-and-audit/` that this handoff does not name.
- The report file is the input of the cycle's scripts (`task-cycle/remarks_check.py` reads it), so write it at the path above although its name could look like one Claude Code refuses a subagent to write; if the write is refused all the same, return the report whole as your answer.

## Working copies (word for word from the process of the cycle)

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed,
except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
says, to the place the product's foundation settles for screenshots, and into the agent's directory
only where no such place is settled. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
`git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed. It
removes a copy, as any directory, by its path written out in full in the command, never through a
shell variable: an empty variable turns the removal on the directory the shell stands in.

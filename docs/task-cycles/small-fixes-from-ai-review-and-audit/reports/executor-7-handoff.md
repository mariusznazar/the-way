# Handoff — executor of slice 7

You make slice 7 of a planned change in a task cycle of the-way. The person who requested the cycle has delegated every intermediate choice to the orchestrator; no answer you get is that person's approval. You never ask the human; questions go back to the orchestrator in your report.

- Worktree (your working directory for everything): `the worktree root`, task branch `task/small-fixes-from-ai-review-and-audit`. Slice 7's base: `29a1c6ae` (the head of slice 6) (`git rev-parse HEAD` now). Start from the worktree's root.
- Method: `task-cycle/change/SKILL.md` (`make-change`) in the worktree, read whole. Your variant, in the words of its table's row: "a slice, or the retry of a slice". Read `task-cycle/change/slice.md` beside it. The skill tool is not yours: a skill a file names is the `SKILL.md` whose frontmatter `name:` is that name, read as a file under the same root.
- Stage and boundary: slice 7 only. You do not start slice 8.
- Report path: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/reports/executor-7-report.md`.
- Your directory for working copies: `.runs/executor-7/`.
- Answers of the cycle's step 4: trust boundary yes for the change as a whole (not for this slice, whose risk is `none` — but `process-audit/` holds trust-boundary files (`process-audit/audit_count.py`, `record_reading.py`, `problem_register.py`, `record_items.py`, `audit_shared.py`): this slice changes none of them, and what it reads from them it reads through their existing functions); irreversible operation no.
- Frozen task: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md` (open only the lines the slice's *Read* names).

## Your slice, word for word from the plan

### Slice 7 — the audit's comparison before and after a fix, inside each series

- **Goal:** the result of `process-audit/audit_count.py` gives, inside each series of the four kinds, for each issue of the register of problems whose *Fate* is `fixed` and whose *Fix* is a commit, the comparison of the cycles on the versions that lack the fix with the cycles on the versions that hold it (the rules of Row 1, Row 2 and Row 3 of the plan's *Foundation entries* and of the task's point 5 are what it makes true). Whether a version holds the fix is the answer of `Ancestry.holds` for the version's full commit and the fix, never a date: a version that holds it is on the side after, one that lacks it on the side before, and a version whose answer is unknown stands on neither side and puts its reason into *Unknown values*, as the other answers of that kind do. The register's fixed issues with their fix commits reach the measure series through a new field of the object `Versions` that `process_versions` fills, so that the signature of `measure_versions`, and `process-audit/audit_count.py`, do not change. A comparison stands in a series only where cycles stand on both sides (for the gate times, runs compared on both sides, of the total); a series with no such issue has none. Each side carries what the image of the series of its kind carries (Slice 6): the cost, the number of cycles with a known cost and the median cost; Q1 as `yes n · no n · unknown n` and Q2 as the sums with their answer, for the count of remarks; for each measure the cycles with a value and the median, for the mechanism measures; and for each measure the runs compared and the runs not compared, with their medians, for the gate times. The comparison adds one verdict on top of the sides: Q3 for the cost, and *falls* for the mechanism measures and for the gate times of the runs compared: `yes` where the median of the side after is lower than the median of the side before, `no` where it is not, `unknown` with its reason in *Unknown values* where a median is not known; the count of remarks has no verdict, only the two sides. The report writes the comparisons of a series as a table under the image of the series and before its table per version, one pair of rows (before, after) for each issue and, for the measures, for each measure; the issues stand in the order of the register, never ranked. The tests give each of the four kinds a series of versions on both sides of a fix, with the sides worked out by hand: a version that is later by date but lacks the fix lands before it, a series with cycles on one side only has no comparison, a fix that the checkout of the-way lacks gives no comparison and an unknown value with its reason, two issues with the same fix, a series of the count of remarks that a change of `task-cycle/review` splits into two, each with one side, and a fixed issue whose *Fix* is not a commit.
- **Change:** `process-audit/series_summary.py` · `process-audit/version_analysis.py` · `process-audit/audit_report.py` · `process-audit/test_process_versions.py` · `process-audit/test_series_summary.py`
- **Read:** `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md:36-36` *To do* point 5 · `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md:62-68` *Questions to settle*, which changes get the comparison · `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md:87-88` *Context*, the lines on the comparison and the series · `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md:111-112` *Decisions in play*, WAY-339 and WAY-350 · `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md:120-122` *Settlements to record*, rows 1 to 3 · Row 1, Row 2 and Row 3 of the plan's *Foundation entries* · `foundations/decisions.md:8607-8746` WAY-339 · `foundations/decisions.md:8747-8783` WAY-350 · `foundations/decisions.md:8509-8543` WAY-330 · `foundations/decisions.md:8890-8987` WAY-416 · `foundations/decisions.md:11087-11134` WAY-385 · `foundations/decisions.md:6820-6857` WAY-365 · `foundations/invariants.md:441-470` ruff-blocking-rules, formatter-layout, function-and-file-size · `foundations/part_map.md:128-143` process-audit · `guidelines/coding.md` · `guidelines/coding-measuring-report.md` · `guidelines/coding-shared-module.md` · `guidelines/testing.md` · `process-audit/record_reading.py:166-232` GateRun, Cycle and Read · `process-audit/problem_register.py:60-100` Problem and Register · `process-audit/audit_shared.py` · `process-audit/test_audit_count.py:1-355` the fixtures Repository and AuditCountCase
- **Model:** same — the sides of a comparison come from the history of git for four kinds of series, and the result must stay the same bytes for the same input
- **Risk:** none
- **Checks:** the new tests fail on the slice's base and then pass: `python -B -m unittest discover -s process-audit -p "test_series_summary.py"` and `python -B -m unittest discover -s process-audit -p "test_process_versions.py"`; `python -B gate/run_tests.py process-audit` passes; `python -B gate/run_tests.py agent-instructions` passes (no function over 110 lines, no file over 1200).
- **Depends on:** Slice 6 · Row 2


## Passages of the task your slice's *Read* names, word for word (file: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md`)

### Lines 36-36

5. Liczenie audytu podaje wewnątrz serii porównanie „przed i po zmianie”: cykle na wersjach z daną zmianą wobec cykli na wersjach bez niej, obie grupy w tej samej serii, a o tym, czy wersja ma zmianę, rozstrzyga wersja, nigdy data — dla każdej sprawy rejestru problemów naprawionej (*Fate* `fixed`) z commitem poprawki w *Fix*, w każdej serii, w której po obu stronach poprawki stoją cykle (dla czasów bramki: przebiegi porównywane). Każda strona niesie to, co obraz serii z punktu 4, a porównanie dodaje Q3 (seria kosztu) i „spada” (pomiary mechanizmu i czasy bramki): mediana po poprawce niższa niż przed nią; seria liczby uwag daje dwie strony liczb Q1 i Q2 bez osobnego werdyktu.

### Lines 62-68

- Które zmiany dostają porównanie „przed i po” wewnątrz serii?
  - Answer: każda sprawa rejestru problemów naprawiona (*Fate* `fixed`) z commitem poprawki w *Fix* — ten sam mechanizm co punkt 2 audytu („What came back after a fix”), działający bez ręcznego prowadzenia czegokolwiek; zmiana procesu bez sprawy w rejestrze nie dostaje porównania.
  - Not chosen:
    - Każde scalenie PR-a do `foundations` — dziesiątki porównań na serię, większość z jednym cyklem po jednej stronie, czyli ten sam szum, który dziś blokuje decyzję.
    - Zmiany wskazane w trakcie audytu, z ponownym uruchomieniem liczenia z podanym commitem — nowa opcja liczenia i krok w skillu, a porównanie powstaje tylko na prośbę i nie ma go w wyniku liczenia uruchamianego według harmonogramu.
    - Nowa tabela „zmiany do oceny” w rejestrze — zmiana szablonu rejestru i jego czytnika, dopisanie tabeli do rejestru ręcznie i jej ręczne prowadzenie; nie dokładana, dopóki nie wiadomo, że sprawy naprawione nie wystarczają, a dołożenie później jest tanie.
  - Source: doradca dnia w imieniu Mariusza (tryb samodzielny), 2026-11-21: „a — porównanie »przed i po« dostaje każda naprawiona sprawa z rejestru problemów (z commitem poprawki). To ten sam mechanizm co punkt 2 audytu, działa bez ręcznego prowadzenia czegokolwiek; d nie dokładamy, dopóki nie wiadomo, że a nie wystarcza — wycofanie tanie.”

### Lines 87-88

- Porównanie „przed i po” to ten sam mechanizm co ocena poprawki w punkcie 2 audytu (`process-audit/SKILL.md`, reguła „Whether a fix works is read from the version, never from the date”, około linii 79), tylko zbiera wiele wersji naraz.
- Seria to odcinek o stałym narzędziu pomiaru (WAY-339), więc liczenie w jej obrębie nie łamie reguły porównywania tylko wewnątrz serii (`process-audit/SKILL.md`, około linii 52).

### Lines 111-112

- WAY-339 — dostaje zdania z wierszy 1–2 *Settlements to record*, bez zmiany tego, co już mówi; punkty 4–7 liczą w obrębie serii: „The audit compares each measure only within a series of its own kind, and judges a version of the process by the cycles that ran on it, never one week against another; […]”; poprawka z punktu 8 zaczyna nową serię czasów bramki: „a new series of those starts only with a change of the script that counts them or of the script that records them, and, for the times of the gate, also with a change of the test runner of the process”.
- WAY-350 — punkty 4–5 dokładają porównania czasów bramki ponad wersją, z tym samym ograniczeniem do przebiegów porównywanych: „The audit compares the times of the gate between versions of the process — the median of each version and whether it falls against the previous version of the same series — only over the runs that passed and during which no other such run was going, and shows the other runs apart.”

### Lines 120-122

| 1 | Punkt 4 audytu pokazuje obraz każdej serii (to, co niesie jej rodzaj, ze wszystkich jej cykli, bez Q3 i bez „spada”; Q3 i „spada” tylko w porównaniach dwóch grup) oraz porównanie „przed i po zmianie” wewnątrz serii — cykle na wersjach z daną zmianą wobec cykli na wersjach bez niej, obie grupy w tej samej serii. | sentence of WAY-339 | *Questions to settle*: „Co pokazuje punkt 4 audytu zamiast samych wierszy per wersja?” | czy grupowanie po wersji wewnątrz serii wiąże dalej, czy jest tylko formą tego wyniku, którą późniejsza zmiana może zastąpić porównaniem po dacie |
| 2 | Porównanie „przed i po” dostaje każda naprawiona sprawa z rejestru problemów (z commitem poprawki). | sentence of WAY-339 | *Questions to settle*: „Które zmiany dostają porównanie »przed i po« wewnątrz serii?” | po jakich zmianach liczenie rozbiera serię: po każdym scaleniu, po liście prowadzonej ręcznie czy po poprawkach z rejestru |
| 3 | Odpowiedź Q1 dla każdej grupy cykli — wersji, obrazu serii i strony porównania — to liczby cykli (tak · nie · nieznane), a Q3 i „spada” stoją tylko tam, gdzie są dwie grupy. | decision | *Questions to settle*: „Jak wyglądają odpowiedzi Q1–Q3 dla grupy wielu cykli…?” | czy Q1 grupy brzmi `yes`, gdy jeden cykl daje `yes`, jak dziś dla wersji |

## The foundation entries that the plan's *Foundation entries* rows 1, 2 and 3 became (commit `a946862b`)

- Rows 1 and 2: two sentences added to WAY-339 and a clause of its *Verification*: `foundations/decisions.md:8607-8758` (the sentences are at lines 8627-8633 and in the *Verification* near 8665-8680).
- Row 3: the new decision WAY-417, `foundations/decisions.md:8995-9038`.

## Notes of the orchestrator for this slice

- Slice 6 (commits `0ee90d8e` and `29a1c6ae`, the head of the branch now) wrote `process-audit/series_summary.py` (the image of a series), changed `process-audit/version_analysis.py` and `process-audit/audit_report.py`, and wrote `process-audit/test_series_summary.py`; the tests of the versions stand in `process-audit/test_process_versions.py`. Read what slice 6 made as the base you build on (its report is not yours to read; read the code and its tests). The report of slice 6 says: `AuditCountCase.section` in `process-audit/test_audit_count.py` reads all table lines under a series heading, so it is wrong for a series that has an image; `process-audit/test_process_versions.py` overrides it in a subclass. Use that subclass for your tests of the comparison; do not change `process-audit/test_audit_count.py` (it is not in your *Change*).
- The comparison is made for each fixed issue of the register of problems with a fix commit: take the register's issues through the existing `Register`/`Problem` objects of `process-audit/problem_register.py` (read them; do not change that file) and the answer of `Ancestry.holds` of `process-audit/version_analysis.py` for the version and the fix.
- WAY-417 and the sentences of WAY-339 are the rules this slice makes true: read them whole. Where the Goal below and those entries differ, the entries and the task's passages above hold; name the difference in your report.
- Size: `process-audit/version_analysis.py` stands at about 1000 lines and the limit is 1200; put the code of the comparison into `process-audit/series_summary.py` where it fits (it must stay a module that is imported, never run), and check the size and format invariants with `python -B gate/run_tests.py agent-instructions` after you `git add`/commit the new files (a check run before a file is tracked sees nothing of it).
- Tests: input and expected values written out by hand (`guidelines/testing.md`); each of the cases the Goal lists gets a test, and the new tests fail on your base before they pass.

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

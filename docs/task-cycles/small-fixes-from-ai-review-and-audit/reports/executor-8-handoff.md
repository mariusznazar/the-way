# Handoff — executor of slice 8

You make slice 8 of a planned change in a task cycle of the-way. The person who requested the cycle has delegated every intermediate choice to the orchestrator; no answer you get is that person's approval. You never ask the human; questions go back to the orchestrator in your report.

- Worktree (your working directory for everything): `the worktree root`, task branch `task/small-fixes-from-ai-review-and-audit`. Slice 8's base: `ca55d4e8` (the head of slice 7) (`git rev-parse HEAD` now). Start from the worktree's root.
- Method: `task-cycle/change/SKILL.md` (`make-change`) in the worktree, read whole. Your variant, in the words of its table's row: "a slice, or the retry of a slice". Read `task-cycle/change/slice.md` beside it. The skill tool is not yours: a skill a file names is the `SKILL.md` whose frontmatter `name:` is that name, read as a file under the same root.
- Stage and boundary: slice 8 only. It is the last slice.
- Report path: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/reports/executor-8-report.md`.
- Your directory for working copies: `.runs/executor-8/`.
- Answers of the cycle's step 4: trust boundary yes — this slice changes the docstring of `process-audit/audit_count.py`, which the part map names as a trust boundary: its CODE must not change (the check of your slice shows only lines inside the docstring differ), and a fresh agent reviews the slice; irreversible operation no.
- Frozen task: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md` (open only the lines the slice's *Read* names).

## Your slice, word for word from the plan

### Slice 8 — the skill of the audit and the description of the command say what the result now shows

- **Goal:** `process-audit/SKILL.md` has its point 4 of step 3, "What each version of the process shows" (from the line 221), show first the image of each series and the before-and-after comparisons of each series that Slice 6 and Slice 7 write, as the matter the human weighs, and the rows per version after them; each series is still taken one at a time with the line that says why it begins where it does, the rules that no number of one series stands beside a number of another and that no week's count stands beside the week before stay as they are, and the wording of what Q1, Q2 and Q3 are is the one of Row 3, with Q1 as the numbers of cycles. The rule "Measures are compared inside a series only" (the lines 52 to 61) says, in one added sentence at its place, that a series of the count of remarks begins anew at every change under `task-cycle/change`, `task-cycle/plan`, `task-cycle/review` and `task-cycle/spec` and of `task-cycle/agent-types/the-way-stage.md`, and at a date of *Added* or *Withdrawn* of the register's list of classes, so that the comparison before and after a fix of the count of remarks works only for a fix outside those files and dates, while for the cost it works widely, since its series begins only at a new price list or a change of the script that measures the cost. The docstring of `process-audit/audit_count.py` is made true: its paragraph on what the result gives per version of a series (Q1 and Q2, "Each answer is `yes`, `no` or `unknown`") and its paragraph on the measure versions say that each series gives an image and the comparisons before and after a fix besides the rows per version, and that Q1 is the numbers of cycles; the rest of the docstring, and the code of the file, do not change. No other file changes.
- **Change:** `process-audit/SKILL.md` · `process-audit/audit_count.py`
- **Read:** `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md:37-38` *To do* points 6 and 7 · `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md:56-74` *Questions to settle*, what point 4 shows, which changes get the comparison, the answers of a group · `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md:111-112` *Decisions in play*, WAY-339 and WAY-350 · Row 1, Row 2 and Row 3 of the plan's *Foundation entries* · `foundations/decisions.md:8607-8746` WAY-339 · `foundations/decisions.md:8747-8783` WAY-350 · `foundations/invariants.md:411-420` audit-series-script-paths · `foundations/invariants.md:551-560` audit-count-refuses-record-links · `foundations/part_map.md:128-143` process-audit · `guidelines/coding.md` · `guidelines/coding-measuring-report.md` · `process-audit/audit_report.py`
- **Model:** same — the text of a skill that a human reads must say exactly what the code of slices 6 and 7 now gives, and the docstring of a trust-boundary file must be made true without a change of code
- **Risk:** trust boundary — `process-audit/audit_count.py`
- **Checks:** `git diff` of `process-audit/audit_count.py` shows lines of its docstring only (no line outside the quotes of the docstring changes); `python -B gate/run_tests.py process-audit` passes; `python -B gate/run_tests.py agent-instructions` passes.
- **Depends on:** Slice 7


## Passages of the task your slice's *Read* names, word for word (file: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md`)

### Lines 37-38

6. Punkt 4 „What each version of the process shows” w `process-audit/SKILL.md` (około linii 221) pokazuje przede wszystkim obraz każdej serii i porównania „przed i po” z punktów 4–5, a wiersze per wersja za nimi.
7. `process-audit/SKILL.md` mówi wprost o ograniczeniu: seria liczby uwag zaczyna się od nowa przy każdej zmianie w `task-cycle/change`, `task-cycle/plan`, `task-cycle/review`, `task-cycle/spec` i `task-cycle/agent-types/the-way-stage.md` oraz przy dacie *Added* albo *Withdrawn* na liście klas rejestru (reguła „Measures are compared inside a series only”, około linii 52–61), więc porównanie „przed i po” dla uwag działa tylko dla poprawek spoza tych plików i dat; dla kosztu działa szeroko, bo jego seria zaczyna się tylko przy nowym cenniku albo zmianie skryptu pomiaru kosztu.

### Lines 56-74

- Co pokazuje punkt 4 audytu zamiast samych wierszy per wersja?
  - Answer: obraz każdej serii (to, co niesie jej rodzaj, ze wszystkich jej cykli, bez Q3 i bez „spada”; Q3 i „spada” tylko w porównaniach dwóch grup) oraz porównanie „przed i po zmianie” wewnątrz serii — cykle na wersjach z daną zmianą wobec cykli na wersjach bez niej, obie grupy w tej samej serii; reguła „Set no number of one series beside a number of another […] and no week's count beside the week before” zostaje bez zmian.
  - Not chosen:
    - Sam obraz serii, bez porównań — mówi, jak jest, ale nie daje podstawy do decyzji, czy zmiana pomogła; audyty dalej odkładałyby ją w tym miejscu.
    - Porównywanie serii z serią — wymaga zmiany reguły, która zabrania stawiać liczby jednej serii obok liczb innej, a różnicę między seriami robi częściowo zmiana narzędzia pomiaru, której nie da się oddzielić od zmiany procesu.
  - Source: Mariusz, 2026-11-21, audyt procesu i zapis zadania („obraz serii plus porównanie »przed i po zmianie« wewnątrz serii”).
- Które zmiany dostają porównanie „przed i po” wewnątrz serii?
  - Answer: każda sprawa rejestru problemów naprawiona (*Fate* `fixed`) z commitem poprawki w *Fix* — ten sam mechanizm co punkt 2 audytu („What came back after a fix”), działający bez ręcznego prowadzenia czegokolwiek; zmiana procesu bez sprawy w rejestrze nie dostaje porównania.
  - Not chosen:
    - Każde scalenie PR-a do `foundations` — dziesiątki porównań na serię, większość z jednym cyklem po jednej stronie, czyli ten sam szum, który dziś blokuje decyzję.
    - Zmiany wskazane w trakcie audytu, z ponownym uruchomieniem liczenia z podanym commitem — nowa opcja liczenia i krok w skillu, a porównanie powstaje tylko na prośbę i nie ma go w wyniku liczenia uruchamianego według harmonogramu.
    - Nowa tabela „zmiany do oceny” w rejestrze — zmiana szablonu rejestru i jego czytnika, dopisanie tabeli do rejestru ręcznie i jej ręczne prowadzenie; nie dokładana, dopóki nie wiadomo, że sprawy naprawione nie wystarczają, a dołożenie później jest tanie.
  - Source: doradca dnia w imieniu Mariusza (tryb samodzielny), 2026-11-21: „a — porównanie »przed i po« dostaje każda naprawiona sprawa z rejestru problemów (z commitem poprawki). To ten sam mechanizm co punkt 2 audytu, działa bez ręcznego prowadzenia czegokolwiek; d nie dokładamy, dopóki nie wiadomo, że a nie wystarcza — wycofanie tanie.”
- Jak wyglądają odpowiedzi Q1–Q3 dla grupy wielu cykli (obraz serii i każda grupa porównania „przed i po”)?
  - Answer: liczby zamiast jednego słowa, w jednej formie wszędzie: Q1 dla każdej grupy cykli — wersji, obrazu serii i każdej strony porównania „przed i po” — to liczba cykli z każdą odpowiedzią (`yes n · no n · unknown n`); Q2 to sumy odcinków planowanych i zbyt dużych z odpowiedzią z tych sum, jak dziś dla wersji; Q3 i „spada” pomiarów mechanizmu i czasów bramki stoją tylko tam, gdzie są dwie grupy — wersja wobec poprzedniej wersji serii, jak dziś, i mediana po poprawce wobec mediany przed nią; obraz serii daje medianę i liczbę cykli ze znaną wartością, bez Q3.
  - Not chosen:
    - Te same reguły co dla wersji, przyłożone do całej grupy — Q1 w każdej dłuższej serii wychodzi prawie na pewno `yes`, bo wystarczy jeden cykl, a Q3 w jednej grupie nie ma z czym porównać.
    - Liczby tylko dla obrazu serii i porównań „przed i po”, a w wierszach per wersja Q1 jak dziś — dwie postaci tej samej odpowiedzi w jednym wyniku.
  - Source: doradca dnia w imieniu Mariusza (tryb samodzielny), 2026-11-21: „b — liczby zamiast jednego słowa; tylko tak audyt pokazuje stan taki, jaki jest, a »spada« liczy się tam, gdzie są dwie grupy. Słaby punkt (dwie postaci Q1) usuń, zamiast go przyjmować: Q1 w wierszach per wersja też liczbami (tak · nie · nieznane), jeśli to zmienia tylko formę wyniku liczenia, a nie zapisane dane ani coś, co ten wynik czyta maszynowo”; warunek sprawdzony 2026-11-21: wynik liczenia czytają tylko `process-audit/audit_report.py` (który go pisze), `process-audit/SKILL.md` (człowiek) i `process-audit/test_audit_count.py` w the-way @ `19e5774a`, a żaden skrypt vaulta nie czyta jego kolumny Q1; żadna decyzja fundamentu nie ustala formy odpowiedzi Q1.

### Lines 111-112

- WAY-339 — dostaje zdania z wierszy 1–2 *Settlements to record*, bez zmiany tego, co już mówi; punkty 4–7 liczą w obrębie serii: „The audit compares each measure only within a series of its own kind, and judges a version of the process by the cycles that ran on it, never one week against another; […]”; poprawka z punktu 8 zaczyna nową serię czasów bramki: „a new series of those starts only with a change of the script that counts them or of the script that records them, and, for the times of the gate, also with a change of the test runner of the process”.
- WAY-350 — punkty 4–5 dokładają porównania czasów bramki ponad wersją, z tym samym ograniczeniem do przebiegów porównywanych: „The audit compares the times of the gate between versions of the process — the median of each version and whether it falls against the previous version of the same series — only over the runs that passed and during which no other such run was going, and shows the other runs apart.”

## The foundation entries of the plan's *Foundation entries* rows 1–3 (commit `a946862b`)

- Rows 1 and 2: sentences added to WAY-339 and a clause of its *Verification*: `foundations/decisions.md:8607-8758`. Row 3: WAY-417, `foundations/decisions.md:8995-9038`.

## Notes of the orchestrator for this slice

- Slices 6 and 7 (the commits `0ee90d8e`, `29a1c6ae`, `ca55d4e8`) wrote what the result of the command now shows: an image of each series (`process-audit/series_summary.py`, written into the report by `process-audit/audit_report.py`) and, inside each series, the comparison before and after a fix. Read `process-audit/audit_report.py` and `process-audit/series_summary.py` (for what they write, in what order and under which headings) before you write the skill's text, so that the text says what the result shows; run the command on a test repository if you need to see a result (the tests of `process-audit/test_process_versions.py` build such a repository), in your own directory for working copies.
- Two texts say today that Q1 of a version is a word (the executor of slice 6 found them): the docstring of `process-audit/audit_count.py` (about lines 146-148: "Each answer is `yes`, `no` or `unknown`" and Q1's rule "yes where ... no where every ...") and `process-audit/SKILL.md` (about lines 223-225: "Each answer is `yes`, `no` or `unknown` inside its series"). Both are to say what is now true (Q1 is the numbers of cycles, `yes n · no n · unknown n`, in every group).
- WAY-417 and the sentences of WAY-339 are the rules the text must agree with: read them whole.
- `process-audit/SKILL.md` is a skill that a human reads in a weekly session; keep its tone, its numbering and its other rules, and change only what the slice's Goal names (the point 4 of step 3, the one added sentence in the rule "Measures are compared inside a series only", and the words about Q1 to Q3).
- Check, besides the slice's checks: `git diff ca55d4e8..HEAD -- process-audit/audit_count.py` shows only lines inside the docstring (name the first and last changed line in your report and the line where the docstring ends).

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

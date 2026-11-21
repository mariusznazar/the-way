# Handoff — reviewer of slice 8

You review slice 8 of a planned change in a task cycle of the-way, as an agent that did not make it. The person who requested the cycle has delegated every intermediate choice to the orchestrator; no answer you get is that person's approval. You never ask the human; questions go back to the orchestrator in your report. You are read-only: you change no file of the worktree and make no commit.

- Worktree (your working directory): `the worktree root`, task branch `task/small-fixes-from-ai-review-and-audit`. The range you review is fixed by commits: base `ca55d4e880c7f7f3b3b8b3863d93e335b90c35b9`, head `f52c5657` (the full identifier is what `git rev-parse f52c5657` prints). Compute `git diff ca55d4e8..f52c5657` and `git log ca55d4e8..f52c5657` yourself and confirm that `git rev-parse HEAD` is that head.
- Method: `task-cycle/review/SKILL.md` (`review-change`) in the worktree, read whole. You review a slice: read what this handoff names, as the orchestrator selected it. The skill tool is not yours: a skill a file names is the `SKILL.md` whose frontmatter `name:` is that name, read as a file under the same root.
- Trust boundary: yes. The slice changes the docstring of `process-audit/audit_count.py`, which the part map names as a trust boundary. Check that no line of its code changed (the orchestrator compared the syntax trees of the base and the head of the file and found them equal apart from the module docstring: verify that yourself), and that the docstring says what the code and the report writer now do. Irreversible operation: no.
- Report path: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/reports/review-slice-8-report.md`. Its first line is `PASS <sha>` or `FAIL <sha>` (the full sha of the head you reviewed), or `questions`. The report file is the input of the cycle's scripts (`task-cycle/remarks_check.py` reads it); write it there although its name could look like one Claude Code refuses a subagent to write; if the write is refused all the same, return the report whole as your answer.
- Your directory for working copies: `.runs/review-slice-8/`.
- The author's report: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/reports/executor-8-report.md`: a set of claims to verify, not evidence.
- Do not read `cycle.md` or any file of `.runs/task-cycles/small-fixes-from-ai-review-and-audit/` that this handoff does not name.
- What you read, besides the slice's section below: the frozen task `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md` lines 37-38, 56-74 and 111-112 (it also holds the question about which changes get the comparison); `foundations/decisions.md` WAY-339 (8607-8758), WAY-350 (8759-8795) and WAY-417 (8995-9038), each whole; `foundations/invariants.md` 411-420 (`audit-series-script-paths`) and 551-560 (`audit-count-refuses-record-links`); `foundations/part_map.md` 128-143; the guideline files `guidelines/coding.md` and `guidelines/coding-measuring-report.md`, each whole; `process-audit/audit_report.py` and `process-audit/series_summary.py`, to verify that what the skill's text and the docstring say is what the result shows (the code of slices 6 and 7 is outside your range and is not yours to review; a mismatch between it and the text you review is a finding on the text). Grade and scope are yours.

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

## What your report holds

Your report holds, after its first line, what the method gives: the graded findings (blocking and Minor, each with the place in the code, the reason and — for a blocking one — whether it contradicts the settlements, with the mark `Contradiction: yes` or `Contradiction: no` as the method asks), the findings outside the task's scope, the checks you ran each with its command and exit code, each reach beyond this handoff (what, where, why), each working copy (where it stood and that you removed it, or the remainder with its full path), **Unread material:** each file, entry or passage this handoff names that you did not read whole or read in part, or `none`, and **Searches not found or unclear:** each thing you looked for and did not find or that was unclear, or `none`. Return the report's first line, the checks you ran with their results, and the report's path.

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

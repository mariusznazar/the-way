# Handoff — review of the commits of the return step (task `project-closure-step`)

You are a fresh reviewer of the strongest class, and you made none of this change. Review, with
`review-change` (`task-cycle/review/SKILL.md`), the commits of the return step, read-only: change and commit
nothing. Questions go to the orchestrator.

- Worktree and branch: `the task's worktree`, `task/project-closure-step`. Work
  from its root.
- Range: base `d4cfe7105964f38e11db4f4bd6db91136bafe8f7` (the head the review of the fix passed), head `e9a7a81f`
  (confirm `git rev-parse HEAD`; compute `git diff d4cfe710..e9a7a81f` and `git log d4cfe710..e9a7a81f`
  yourself): one commit, changing `foundations/decisions.md` only (WAY-411, WAY-412, WAY-414).
- Review it against the task and the foundation entries the return step writes or corrects, as section 2 of
  `task-cycle/review/SKILL.md` gives for the commits of the return step. The task, to read whole where you need
  it: `.runs/task-cycles/project-closure-step/task.md` (Polish). The rows of its *Settlements to record* the
  commit touches, word for word:

| 1 | Zamknięcie projektu jest krokiem skilla prowadzącego plan, opisanym w osobnym pliku obok skilla, a nie osobnym skillem; wróci do osobnego skilla, gdy zamknięcie urośnie o przegląd fundamentu albo retrospektywę projektu. | decision | pytanie „Gdzie w procesie mieszka zamknięcie projektu?” (jego *Not chosen*) | czy zapisać, dlaczego zamknięcie nie jest osobnym skillem — bez wpisu następna zmiana skilla prowadzącego może je wydzielić, nie znając kosztu |
| 2 | Każdemu zadaniu wycofanemu człowiek wybiera przy zamknięciu jedno z trzech miejsc — następny projekt (sekcja w istniejącej notatce następnego projektu w miejscu projektów, nowy plik tylko gdy jej nie ma), samodzielne zadanie w miejscu zadań albo porzucone z powodem — a zamknięcie samo zapisuje przeniesienie razem z celem zadania, pytaniami planu i wpisem fundamentu, którego zadanie nie zapisało. | decision | pytanie „Dokąd może pójść zadanie wycofane przy zamknięciu…” (jego *Not chosen*) | czy zamknięcie przenosi treść samo, czy tylko zapisuje w planie, dokąd zadanie poszło, i czy zakłada nowy plik, gdy notatka następnego projektu już jest |
| 5 | Zamknięcie sprawdza, czy wpis przewidywany zadania wycofanego jest w fundamencie produktu, szukając go po pytaniu wpisu na konkretnym commicie, i pisze „brak w fundamencie na commicie X” albo wskazuje znaleziony wpis, także częściowy, a niepewne trafienie stawia człowiekowi jako pytanie w podglądzie. | decision | pytanie „Skąd zamknięcie wie, że wpis fundamentu zadania wycofanego nie powstał?” (jego *Not chosen*) | czy wnioskować brak wpisu z samej tabeli planu |

- The author's report of the return step, a set of claims to verify:
  `.runs/task-cycles/project-closure-step/reports/author-return-report.md`. The earlier review of the fix, whose
  two notes (WAY-414's search against `closure.md` for a change of a current decision; the words "withdrew" and
  "dropped" against the settled word) the commit answers: `.runs/task-cycles/project-closure-step/reports/review-fix-report.md`.
- The step's file `project-level/lead/skill/closure.md` at the head is what WAY-414 and the other edited
  entries have to agree with, in both directions. Read it whole, and the three decisions whole with their
  *Rejected*; add the foundation entries and the guideline files by your own reading where a finding needs them
  (name each reach in your report).
- Trust boundary: yes for the change as a whole (`plan_check.py`, `plan_state.py`); this commit touches neither.
  Irreversible operation: no.
- Checks: you may run `python -B elements/common/foundation_check.py` and the tests of one directory; not the
  whole gate. Report each check with its command and exit code.
- Your report: `.runs/task-cycles/project-closure-step/reports/review-return-report.md`, first line `PASS <sha>`
  or `FAIL <sha>`, graded findings, **Unread material**, **Searches not found or unclear**. Your directory for
  working copies: `.runs/review-return/`; the same paragraph on working copies as in the earlier handoffs holds
  (make nothing outside it, remove it before you return, state it in the report).
- The files of the record directory other than those named here are not yours to read.

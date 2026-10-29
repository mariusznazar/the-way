# Author report

**Status:** done

**Worktree and base:** `C:/Storage/repos/the-way/.runs/worktrees/retain-failed-checks`, based on `d115159c554752601749efa8270ae76fbe02f4df`.

**Changes:**

| File | Added | Removed | Purpose |
|---|---:|---:|---|
| `foundations/decisions.md` | 52 | 0 | Added WAY-260 and WAY-261 for cycle request evidence and author reports of failed checks that pass on rerun. |
| `task-cycle/record_template.md` | 11 | 3 | Retains every failed run and specifies how the request presents rerun results, run counts and outside-part checks. |
| `task-cycle/skill/SKILL.md` | 13 | 4 | Carries the check and outside-scope details into the request, with part classification evidence taken from file paths. |
| `task-cycle/change/SKILL.md` | 2 | 1 | Requires both command and exit-code results in the author's report. |

**Settlement rows:**

| Row | Entry | Meaning |
|---|---|---|
| 1 | WAY-260 | Każde padające uruchomienie sprawdzenia zostaje w zapisie; request pokazuje wynik powtórki i liczbę uruchomień, w których sprawdzenie padło i przeszło, a sprawdzenie spoza części zadania trafia też obok uwag spoza zakresu. |
| 2 | WAY-261 | Raport autora lub wykonawcy podaje komendę i kod wyjścia nieudanego uruchomienia oraz udanej powtórki. |

**Checks:**

- `python -B gate/run_tests.py` on the unchanged base, run by the orchestrator before author edits: exit code 0; 613 tests in eight directories passed, with five platform-specific skips. The author did not run the full gate after the changes because the handoff reserves it to the orchestrator.
- `python -B instruction-files/check_instructions.py .`: exit code 0. It reports 0 errors and one existing `dead-path` warning at `AGENTS.md:21` for the private backlog directory.
- `python -B elements/common/foundation_check.py`: exit code 0, 0 errors.
- `git diff --check`: exit code 0.
- No behavioral tests were added: the change only edits Markdown instructions and decisions, and its method says prose for people gets no test. No invariant test changed.

**Own-work weakest-point check (WAY-164):** The requirement most likely to be misapplied is deciding whether a check lies outside the task's parts when WAY-150 does not preserve the selection as a second record. I assigned the frozen task's three `task-cycle/**` targets and the changed foundation entries to `task-cycle` using the part map; the map assigns `gate/**` checks to `gate`. This confirms the request rule can keep a check in *Checks* while adding it beside outside-scope findings only when its file maps to a different part. The check's file path is the evidence carried with that request item; no separate selection list is maintained.

**Foundation search and decision placement:** After settling the two meanings, I searched `foundations/` and `task-cycle/` for flaky tests, reruns, failed and passing checks, outside-task findings and request checks. WAY-243 governs the product testing guidelines; WAY-159 requires command and exit-code evidence for author checks; WAY-160 requires failed or unchecked checks in the request; WAY-161 governs review findings marked outside scope. None states the two cycle rules or the request's failure/pass counts. I therefore recorded the independent cycle-record/request rule as WAY-260 and the author-report rule as WAY-261, linked to the existing decisions that govern them. I left WAY-150 unchanged; it says selection is not recorded, and the new request instruction derives the parts at request time from the frozen task, changed paths and part map.

**Choices and risks:**

- I wrote two decisions rather than adding both settlements to WAY-159 or WAY-160 because the task separates cycle/request handling from the author's report. If this split was wrong, adjacent rules could drift; the entries name their existing governing decisions and their distinct artifacts.
- I classify an outside check when preparing the request by comparing its file's mapped part with the task's parts recovered from its frozen document and changed paths. The request includes the check file path so the classification can be reviewed. If the frozen task and actual changed paths disagree, classification could be wrong; the review can compare the paths and map directly.
- I did not add an invariant or a behavior test because the settlements govern process instructions and prose, not testable product behavior. No invariant test was changed.

**Reads beyond the dispatch:**

- Read the repository integration guide and the worktree's own skills and templates named by the make-change and foundation methods, as required by the repository instructions.
- Read `C:/Storage/The Brain/The Brain/.ai/rules/scripts.md`, `knowledge_artifacts.md` and `git.md` before running scripts, editing knowledge and committing.
- Read `C:/Storage/The Brain/The Brain/Notes/Areas/(A) Claude code/konwencje_skilli_i_commandow.md` before editing the task-cycle skills.

**Not run in this stage:** the full gate after the change, the review, the return step and reconciliation with the target branch. The handoff assigns the gate to the orchestrator and says to return before review and the return step.

**Commit:** `2a46aec` (`docs: retain failed check runs in task-cycle evidence`).

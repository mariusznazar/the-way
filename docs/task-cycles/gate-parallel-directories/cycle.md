# Cycle record — the way: shorter gate — test directories in parallel and no run on the starting state

- Task source: the task's note in the author's private backlog, status `ready for cycle`, updated 2026-11-13 (frozen copy: `task.md` beside this record)
- Task relation: independent
- Product repository: the-way (https://github.com/mariusznazar/the-way)
- Process pin: this checkout is the-way itself, `f749cfc`
- Target branch and base: `foundations`, `f749cfc`
- Task branch: `task/gate-parallel-directories`
- Status: request open

## Two questions at start

- Trust boundary: yes, in part — `task-cycle/gate_times.py` is a trust boundary of the part `task-cycle`, but this task does not have to change it (it reads the blocks `== <directory>` and the first `Ran <n> tests in <s>s` of a block, and the task keeps the report of a directory one block); the files the change touches are `gate/run_tests.py` (part `gate`, no trust boundary), `task-cycle/skill/SKILL.md`, `task-cycle/record_template.md`, `task-cycle/skill/request_template.md` (part `task-cycle`, boundary only for the three scripts), the decision log and `agent-instructions/README.md`. Every review is told to check that `gate_times.py` still reads the new output of the runner, and that the runner takes no input from outside the repository other than the option values.
- Irreversible operation: no.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none — every question of the task's *Questions to settle* carries the human's answer and its source; the names of the two new options, the form of the buffered report and the numbers of the decisions follow from the answers and are choices of how to make what the task settles.
- Reserved choice: none — no language, framework, library, store of data, way of logging in or place to run is in play.
- Execution route and reason: one author without a plan — one script of about 140 lines with its tests, edits of four process files by the task's own words, two decisions and a changed one; one agent holds it. Class `same` as the orchestrator's (sonnet), not `cheaper`, because the change reaches two parts (`gate`, `task-cycle`) and writes decisions of the foundation that the one author has to weigh against WAY-16, WAY-55, WAY-160, WAY-243 and WAY-349.
- Author: `same` as the orchestrator (sonnet), for its code, foundation entries and return step; resumed for the fix and the return step.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: completion notification (background agents); no limit hit so far
- Whole-change review: a fresh reviewer (sonnet, the orchestrator's class) by `review-change`, range `f749cfc`..`264703f`, `reports/whole-review-report.md`, first line `PASS 264703fd074620f18a2b044a7f84761aef337998`; 8 changed files (520 added, 57 removed lines at that head); 0 blocking, 5 Minor within the task, 1 outside it (the audit's series); every item of the task covered (items 1–5, the three answers of *Questions to settle*, both rows of *Settlements to record*, the change of WAY-349), no projected entry; source fidelity: WAY-366 and WAY-367 against the task's wording and *Not chosen* lists, WAY-349's change one sentence and its *Verification*. Its **Unread material** named nine decisions bearing on the change as unopened and files read in part, so the same reviewer was resumed on the final head and closed them (`reports/fix-review-report.md`): nothing changed a grade or the PASS.
- Review rounds:
  - findings `reports/whole-review-findings.md`: the review of the whole change passed with five Minor findings within the task (no blocking finding). One fix by the author, resumed, on `same`: commit `9282e6f` (range `264703f`..`9282e6f`), fix report `reports/fix-report.md`; the same reviewer, resumed, reviewed the fix once, `reports/fix-review-report.md`, `PASS 9282e6f408fba466b583eaec75118e4f87e8bbf6`: the five findings fixed, two new Minor findings in the fix (the queue is cancelled only on an interrupt, not when a worker raises; the interrupt test reaches the runner through `loaded['concurrent'].futures`), no new Critical or Important finding. The fix was not reverted.
- Weakest-point checks: author — requirement: the final line, the exit codes and the report of each directory as before (task items 1 and 4); check: a temporary git repository of four directories (passing, failing, skipped, exiting 0 with no report) run with the runner of the base and with the new one at `--jobs 1`, outputs compared with `diff`; it showed one extra blank line under a directory that prints nothing, fixed with its test, then `diff` exit 0 (`reports/author-report.md`). The review ran mutations of the runner (`max_workers=1` fails 3 of 10 new tests, the failed list in order of ending fails 1) and confirmed the tests fail on a runner that does the opposite (`reports/whole-review-report.md`, `reports/fix-review-report.md`).

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

One author, no plan: no slices.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-13 | start | orchestrator (sonnet) | task document | `task.md` | `foundations` equals `origin/foundations` (`f749cfc`), no fast-forward needed; branch `task/gate-parallel-directories` and worktree created; the gate on the base started in `.runs/base-check` through `gate_times.py` |
| 2026-11-13 | author | author (sonnet, `same`) | `reports/author-handoff.md`, `make-change` "the whole change as the one author" | `reports/author-report.md` | `done with concerns`; commits `a6807f1`, `9bea9a1`, `264703f`; mechanical check: clean tree, non-empty range, 8 files (runner and its tests, `task-cycle/test_gate_times.py`, the decision log, step 4/2/10 of `SKILL.md`, `record_template.md`, `request_template.md`, `agent-instructions/README.md`), report holds checks with commands and exit codes, own-work check, Unread material and Searches; its gaps (lines 31–39 of `request_template.md`, four files read in passages, WAY-68/89 read from *Scope*, nine decisions by title) go to the reviewer's handoff; next: review of the whole change |
| 2026-11-13 | review of the whole change | reviewer (sonnet) | `reports/whole-review-handoff.md`, `review-change`, range `f749cfc`..`264703f` | `reports/whole-review-report.md` | `PASS 264703f`; 0 blocking, 5 Minor within the task, 1 outside (the audit's series); next: one fix of the 5 Minor findings and one review of it |
| 2026-11-13 | fix | author, resumed (sonnet) | `reports/fix-handoff.md`, findings `reports/whole-review-findings.md` | `reports/fix-report.md`; commit `9282e6f` | `done`; mechanical check: clean tree, 8 files = the files of the five findings; next: review of the fix |
| 2026-11-13 | review of the fix and gap reading | reviewer, resumed (sonnet) | `reports/fix-review-handoff.md`, findings `reports/whole-review-findings.md`, range `264703f`..`9282e6f` | `reports/fix-review-report.md` | `PASS 9282e6f`; 2 new Minor within the task, none blocking; the gaps of the first report closed, nothing changes a grade; next: return step |
| 2026-11-13 | return step | author, resumed (sonnet) | `reports/return-step-handoff.md`, `foundation_step.md`, `return_step.md` | `reports/return-step-report.md` | `done`, nothing mismatched, no commit; no review of the return step since it committed nothing |
| 2026-11-13 | gate | orchestrator | `python -B task-cycle/gate_times.py ... -- python -B gate/run_tests.py` on `9282e6f` (the final tree) | `gate_times.md`, `final-gate.log` | exit 0, 1238 tests in 10 directories passed (697 s); `origin/foundations` had not moved (`f749cfc`), no reconciliation merge needed |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | Class of the one author (step 4) | `same` (sonnet) | the change reaches two parts and writes decisions of the foundation | `cheaper` — a wrong weighing of WAY-349 against the task costs a fix round and a review | one fix round | author |
| Q2 | The default number of directories at once and the names of the options (the task: "all at once or as many as the cycle chooses") | all at once by default; `--jobs N` and `--slowest N` | the author's choices 1 and 2 (`reports/author-report.md`) | the number of processors as the default — one gate then takes different times on two machines | ten processes at once on the-way, more in a product with more directories; a product writes `--jobs` | author |
| Q3 | Review of the Minor findings of the fix (two new, both Minor within the task) | not fixed: a Minor finding of the review of a fix goes to the request's list | `reports/fix-review-report.md` | a second fix round — the cycle allows one | a worker that raises leaves the queue running at `--jobs N` below the number of directories; a silent change of an import style breaks one test with an unhelpful message | request, lower part |
| Q4 | The audit's series (out of scope finding 6) | for the human: not fixed, since the task leaves `gate_times.py` untouched | `reports/whole-review-report.md` (6), `process-audit/SKILL.md` lines 57–60 | changing the audit's rule in this cycle — outside the task | the medians of the gate times before and after this change stand in one series | request, item for the human |
| Q5 | Environment fact for `unittest`'s `durations` or git's `^2^{tree}` | none written: no decision's *Based on* and no invariant's *Rests on* needs it | `reports/return-step-report.md` | writing a fact no entry cites | none seen | return step |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| Frozen task | `task.md` | orchestrator | — |
| Change | commit `a6807f1` (runner and its tests), `9bea9a1` (WAY-366, WAY-367, WAY-349), `264703f` (instruction files), report `reports/author-report.md` | author (sonnet) | PASS, `reports/whole-review-report.md` |
| Fix of the Minor findings | commit `9282e6f`, report `reports/fix-report.md` | author, resumed | PASS, `reports/fix-review-report.md` |
| Return step | `reports/return-step-report.md`, no commit | author, resumed | nothing to review |
| Gate, stages, measures | `gate_times.md`, `final-gate.log`, `stages.md`, `mechanism_measures.md` | orchestrator | — |
| Request | `request.md` | orchestrator | — |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| `python -B task-cycle/gate_times.py --output ../task-cycles/gate-parallel-directories/gate_times.md -- python -B gate/run_tests.py` | orchestrator, base `f749cfc`, separate checkout `.runs/base-check` | 0; 1221 tests in 10 directories, every directory passed (1357 s, with the author's focused checks beside it) | none failed on the base |
| `python -B task-cycle/gate_times.py --output docs/task-cycles/gate-parallel-directories/gate_times.md -- python -B gate/run_tests.py` | orchestrator, `9282e6f` (final tree), the task worktree | 0; 1238 tests in 10 directories, every directory passed (697 s; the base run took 1357 s with the author's focused checks beside it) | none |
| `python -B gate/run_tests.py gate`, `task-cycle`, `elements/part-map`, `elements/common`, `agent-instructions` | author on `264703f` and `9282e6f` | 0; 35 and 36, 386, 39, 144, 18 tests OK; the new tests failed first on the old runner (8 of 33) | none |
| `python -B elements/common/foundation_check.py` | author, reviewers, return step | 0; 0 errors | none |
| mutations of the runner (`max_workers=1`; failed list in order of ending; `cancel_futures` removed) | reviewer, copies in its scratchpad | the new tests fail on each mutation (3 of 10, 1 of 10, the interrupt test) | none |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator | 0; `tag: foundation-review/2026-11-06`, `merges: 33`, `threshold: 30`, `reminder: yes` | none |
| `python -B task-cycle/cycle_stages.py --output docs/task-cycles/gate-parallel-directories/stages.md`; `python -B task-cycle/cycle_measures.py --output docs/task-cycles/gate-parallel-directories/mechanism_measures.md` | orchestrator | both 0 | none |
| `python -B task-cycle/request_check.py docs/task-cycles/gate-parallel-directories/request.md --task docs/task-cycles/gate-parallel-directories/task.md`; `python -B task-cycle/private_paths_check.py docs/task-cycles/gate-parallel-directories/request.md` | orchestrator | 0 and 0 (1 run each before publishing) | none |
| `python -B task-cycle/private_paths_check.py docs/task-cycles/gate-parallel-directories` | orchestrator, on the copy, before its commit | last run 0 (0 listed of 19 files); the first run listed 13 places (one task-note path, five worktree and scratchpad paths, six note links of the task copy), which the cleaning rewrote in every file | none |
| `python -B task-cycle/image_files_check.py docs/task-cycles/gate-parallel-directories` | orchestrator, on the copy | last run 0 (0 listed) | none |
| `python -B task-cycle/remarks_check.py docs/task-cycles/gate-parallel-directories` (original) and `python -B task-cycle/remarks_check.py docs/task-cycles/gate-parallel-directories` (copy) | orchestrator | original: 2 runs, the first listed 15 items, then the items were appended and the last run exited 0 with 15 items in the remarks; copy: last run 0, 0 not in the remarks | none |

The checks failing on the base: none. The move of the pin: none (the-way itself).

## Return step

- Foundation compared with code: the entries the change writes or changes (WAY-366, WAY-367, WAY-349), those the task names (WAY-16, WAY-55, WAY-160, WAY-243), WAY-350 and WAY-63, and the part-map entries `gate`, `task-cycle` and `test-runner-command`, each compared with the repository on `9282e6f`; nothing no longer matched (`reports/return-step-report.md`)
- Decisions written or changed: WAY-366 (new, row 1), WAY-367 (new, row 2), WAY-349 (changed in place)
- Invariants written or changed: none
- Environment facts: none
- Glossary terms: none
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: row 1 as WAY-366, row 2 as WAY-367

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/111, opened as a draft, marked ready after the record's commit
- Description: `request.md` beside this record, written by `task-cycle/skill/request_template.md`; form check `python -B task-cycle/request_check.py docs/task-cycles/gate-parallel-directories/request.md --task docs/task-cycles/gate-parallel-directories/task.md` last exit 0 (1 run before publishing), check of private paths on it last exit 0 (1 run); the edit that adds the record's link and the runs of the three checks on the copy is checked again after this commit
- Writes to the task's backlog entry: the request link added as `[url::…]` to the task's line in the backlog; its state stays `[/]` (Ready), as the rules of the task place name no state for an open request
- Corrections after the request opened: none
- Process remarks on the-way:
  - author, docs/task-cycles/gate-parallel-directories/reports/author-report.md: The handoff says to grep the tracked files (not `.runs/`, not `docs/`) for what else names the run on the base, naming `starting state|run on the base|the base alone|checks already failing`. The words of the files are "the base" and "failing on it", not "starting state" (only WAY-349 says "starting state"); I searched also for `on the base`, `base.*(gate|check|fail)` and `gate_times`, and read each hit.
  - author, docs/task-cycles/gate-parallel-directories/reports/author-report.md: The task says "the step 2 mention of the run on the commit that moved the pin" and the handoff "step 2's mention of the run on the base": step 2 does not run the gate on the base itself, it sends to step 4 ("record its base and the checks failing on it as step 4 gives"); I changed only its clause that reads "passed on the base", which presumed a base run. The rule itself stands once, in step 4.
  - author, docs/task-cycles/gate-parallel-directories/reports/author-report.md: The task item 4 says the list is taken "z zapisu tamtego cyklu w historii gita" but names no command to find it. I named the file (`docs/task-cycles/<task-slug>/cycle.md`) and its section (*Verification*) in step 4 and wrote no `git log` recipe. I tried the rule on this very base: `git rev-parse f749cfc^{tree}` and `git rev-parse f749cfc^2^{tree}` both print `d84c44465c727f4067bbb048a7d0bc49a59d5ce6` (exit 0), and `git log --diff-filter=A --name-only --format=%h f749cfc^1..f749cfc^2 -- docs/task-cycles` finds the copy `45efc2d:docs/task-cycles/ close-decision-pending-templates/cycle.md`, whose *Verification* holds the final gate (exit 0, 1221 tests), so the rule is workable on the-way's own history.
  - author, docs/task-cycles/gate-parallel-directories/reports/author-report.md: I did not find in the task a way to run "the failing tests" on the base in general (a product's command for one test differs: for the-way it is `python -B gate/run_tests.py <directory>`, which runs a directory, not one test); step 4 says "run the failing tests on the base" and leaves the command to the product's rules.
  - fix, docs/task-cycles/gate-parallel-directories/reports/fix-report.md: The handoff says the interrupt test must "not wait on long sleeps"; the finding's own repro used 3 s directories. I made the interrupt come from a patched `as_completed`, as the reviewer's repro did, and used 0.3 s directories. It does not send a real interrupt to a process (not portable on Windows), so it shows that queued directories are cancelled, not that Ctrl-C reaches the running ones.
  - fix, docs/task-cycles/gate-parallel-directories/reports/fix-report.md: Finding 5 named the lines of `README.md:55-60` and `decisions.md` ~11605-11607 only roughly; I re-wrapped the whole paragraph of each.
  - review of the fix, docs/task-cycles/gate-parallel-directories/reports/fix-review-report.md: A way to send a real Ctrl-C to a Python process from this shell: not found, so the interrupt is simulated (the same limit as the fix's test).
  - review of the fix, docs/task-cycles/gate-parallel-directories/reports/fix-review-report.md: The words "starting state" and "base" name one commit and only the first stands in the decisions (WAY-349, WAY-367); no glossary entry says so. Not a finding; named for the human's choice.
  - return step, docs/task-cycles/gate-parallel-directories/reports/return-step-report.md: The method says to write an environment fact for each source outside the product that the change rests on; its template limits the facts to those a decision or an invariant rests on, so I found no fact to write and say so rather than add one no entry cites. If the orchestrator holds that the `durations` parameter is such a source, the entry is its call.
  - return step, docs/task-cycles/gate-parallel-directories/reports/return-step-report.md: The handoff names no entry beyond the change's own, so "the entries the task names" were taken from the task's *Decisions in play*.
  - review of the whole change, docs/task-cycles/gate-parallel-directories/reports/whole-review-report.md: A rule of size for the-way (`guidelines/coding.md`, heading `### Size of a function and a file`): not found (the-way has no such file); so no threshold test, and the structure judgment rests on the line counts.
  - review of the whole change, docs/task-cycles/gate-parallel-directories/reports/whole-review-report.md: The handoff says to check "any file the author did not search that names the run on the base": the files name it as "the base" and "failing on it", not "starting state"; I searched the words `on the base`, `\bbase\b` near `gate|check|fail|run`, `failing on`, `already failing`, `starting state`, `gate_times`; the one stale hit is `record_template.md:100`.
  - review of the whole change, docs/task-cycles/gate-parallel-directories/reports/whole-review-report.md: Whether the runner ever read a real Python older than 3.12: no such interpreter on this machine; unverified.
  - review of the whole change, docs/task-cycles/gate-parallel-directories/reports/whole-review-report.md: The task's *Questions to settle* and *Decisions in play* point to notes of the author's private backlog (the author's report on process improvements, the author's note of measurements before changes of the process): not available to me; I judged source fidelity against the task's own quotation of them.
  - review of the whole change, docs/task-cycles/gate-parallel-directories/reports/whole-review-report.md: Step 4 names no way to find the merged branch's copy of the record and its `<task-slug>` is ambiguous (Minor 3).

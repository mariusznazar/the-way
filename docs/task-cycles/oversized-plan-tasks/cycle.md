# Cycle record — Wyłapywać zbyt duże zadania przed oddaniem planu projektu Mariuszowi

- Task source: the task document, the task's note in the author's backlog, approved 2026-11-14 (`Status: ready for cycle`, settlements accepted 2026-11-14); frozen copy `task.md` beside this record
- Task relation: independent
- Product repository: the-way (github.com/mariusznazar/the-way)
- Process pin: not applicable (the-way itself)
- Target branch and base: `foundations`, `5a24ac97277fa1c04fbb967da5c6a2854d17cb8f` (the session's checkout was fast-forwarded to it from `6fa755c`; the remote target branch had not moved at the end of the cycle)
- Task branch: `task/oversized-plan-tasks`, worktree `.runs/worktrees/oversized-plan-tasks`
- Status: request open

## Two questions at start

- Trust boundary: no — the change edits `project-level/plan/skill/cut_tasks.md`, `project-level/plan/skill/critique_plan.md`, `project-level/plan/template.md` and the entry WAY-146 in `foundations/decisions.md`; the part map names as boundary of `project-level` only `readiness_check.py`, `plan_check.py` and `plan_state.py`, which the task leaves untouched (*Out of scope*)
- Irreversible operation: no

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none — rows 1 and 2 of *Settlements to record* settle the criterion and who decides a split; question 2 of the task rules out a script threshold; the wording of the two skill lines and of the decision's sentences follows from them with no way left open
- Reserved choice: none
- Execution route and reason: one author without a plan — four files of one part (`project-level`) and one decision entry, no division needed
- Author: `the-way-author`, class `cheaper` (ordinary wording change settled by the task), model haiku-5-5; resumed for the answers to its questions, for the fix of the Minor findings and for the return step; no replacement
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: native completion notification of the harness (background agents, yielded the turn)
- Whole-change review: a fresh `the-way-stage` reviewer on sonnet-5-5 (same class as the orchestrator), `review-change`; range `5a24ac9..44c1d99`; first line `PASS 44c1d9924ea5832b0ce8dfb825814c30e063c6e6`, report `reports/review-whole-report.md`; changed files: `foundations/decisions.md` (WAY-146) +21, `project-level/plan/skill/critique_plan.md` +3, `project-level/plan/skill/cut_tasks.md` +5, `project-level/plan/template.md` +2 (the reviewer's size script); every task item, both settlement rows and source fidelity covered (the report's section "Against the task"); 0 blocking, 3 Minor within the task, 1 Minor outside
- Review rounds:
  - findings `reports/whole-review-findings.md`: the whole-change review passed with three Minor findings within the task (the case figure in *Rejected*, the unqualified first sentence of `cut_tasks.md`, the pointer to the test in `critique_plan.md`); the one fix is `4e3c4cf` (`reports/author-fix-report.md`); the same reviewer, resumed, reviewed `44c1d99..4e3c4cf` (`reports/review-fix-report.md`): `PASS 4e3c4cfbf789d0736516c860fe4f7adbb88414d5`, three of three fixed, one new cosmetic Minor, not fixed; no blocking finding remained and none was reverted
- Weakest-point checks: author — that the size clause reaches every place the critic or the author reads it and that no sentence of the entry contradicts another; checked by reading the files after the edit, result: clause in `cut_tasks.md`, `critique_plan.md` and WAY-146, the old "A large task is split" gone, no contradiction with WAY-13, WAY-120, WAY-143, WAY-145 (`reports/author-report.md`)

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-14 | start | orchestrator, Sonnet 5.5 | task read; checkout fast-forwarded; worktree and branch created from `5a24ac9` | `task.md` | two questions answered, route chosen: one author |
| 2026-11-14 | one author | the-way-author, haiku (class cheaper) | `reports/author-handoff.md`; `task-cycle/change/SKILL.md` variant "the whole change as the one author"; frozen task | `reports/author-report.md` | dispatched; returned `done with concerns`, commit `0ed5ad7`, three questions |
| 2026-11-14 | one author, questions | orchestrator to the-way-author (resumed) | answers to Q2 to Q4 of the questions table | `reports/author-report.md` | three questions answered; author resumed |
| 2026-11-14 | one author, resumed | the-way-author, haiku | answers above | `reports/author-report.md`; commits `0ed5ad7`, `44c1d99` | `done`; foundation_check exit 0, project-level unittest exit 0 (275 tests); mechanical check: clean worktree, range non-empty, 4 files, report holds checks with command and exit code, Unread material, Searches, own-work check |
| 2026-11-14 | whole-change review | the-way-stage, sonnet (class same as the orchestrator) | `reports/review-whole-handoff.md`; `task-cycle/review/SKILL.md`; range `5a24ac9..44c1d99` | `reports/review-whole-report.md` | `PASS 44c1d99`; 0 blocking; Minor within the task 3; Minor outside the task 1; foundation_check exit 0, project-level unittest exit 0 (275 tests); the reviewer read 13 of 79 decisions of its selection whole and 66 by title; unread: WAY-106 and WAY-230 (title only), WAY-134 (rule taken from the decisions template), decisions of the part `decisions`; the orchestrator judged the gap to bear on nothing the reviewer judged and the request carries it as an item |
| 2026-11-14 | fix of the Minor findings | the-way-author (resumed), haiku | `reports/author-fix-handoff.md`; findings `reports/whole-review-findings.md` | `reports/author-fix-report.md` | `done`, commit `4e3c4cf`; foundation_check exit 0; project-level unittest exit 0 (275 tests); mechanical check: clean worktree, range `44c1d99..4e3c4cf` non-empty, 3 files as the findings name, Unread material and Searches present |
| 2026-11-14 | review of the fix | the-way-stage (resumed), sonnet | `reports/review-fix-handoff.md`; findings `reports/whole-review-findings.md`; fix report | `reports/review-fix-report.md` | `PASS 4e3c4cf`; 3 of 3 findings fixed; 0 blocking; 1 new Minor, cosmetic (116-character line at `cut_tasks.md:5`; short stray line at `foundations/decisions.md:4227`), not fixed, goes to the request's list; foundation_check exit 0; Unread material none beyond the fix scope; Searches none |
| 2026-11-14 | return step | the-way-author (resumed), haiku | `reports/author-return-handoff.md`; `task-cycle/skill/return_step.md`, `task-cycle/skill/foundation_step.md` | `reports/author-return-report.md` | `done`, no commit; head stays `4e3c4cf`; nothing needed correction; no glossary, environment fact, invariant or part-map entry; both settlement rows written by the one edit of WAY-146; Unread material: WAY-13, WAY-33, WAY-143 read in part by the author (the whole-change reviewer read WAY-13 and WAY-143 whole, so the gap bears on nothing the return step judged); no review needed, no commit |
| 2026-11-14 | gate on the final tree, run 1 | orchestrator | `python -B task-cycle/gate_times.py --output .runs/task-cycles/oversized-plan-tasks/gate_times.md -- python -B gate/run_tests.py` on `4e3c4cf` | `final-gate-1-failed.log`, `final-gate-1-failed.exit` | exit 1; 1274 tests in 10 directories; failed `gate`: `test_a_number_of_jobs_limits_the_directories_that_run_at_once` (a trial directory did not meet the others within 120 s); the test is of the part `gate`, outside the task's parts; the change is prose only |
| 2026-11-14 | diagnosis of the failed directory | orchestrator | `python -B gate/run_tests.py gate` on `4e3c4cf` | `gate-dir-diagnosis.log` | exit 0, 36 tests in 25 s: the directory passes alone; the failure came under the load of ten directories at once; serves diagnosis only (WAY-243), no gate run passes by it |
| 2026-11-14 | gate on the final tree, run 2 | orchestrator | same command, `4e3c4cf`; `origin/foundations` still `5a24ac9`, so no merge to make and the tree is the one the run checked | `final-gate.log`, `final-gate.exit` | exit 0; 1271 tests in 10 directories; every directory passed |
| 2026-11-14 | stages and measures | orchestrator | `python -B task-cycle/cycle_stages.py --output .runs/task-cycles/oversized-plan-tasks/stages.md <session>`; `python -B task-cycle/cycle_measures.py --output .runs/task-cycles/oversized-plan-tasks/mechanism_measures.md <session>` | `stages.md`, `mechanism_measures.md` | both exit 0 |
| 2026-11-14 | request | orchestrator | `python -B task-cycle/review_reminder.py origin/foundations`; `task-cycle/skill/request_template.md` | `request.md`; pull request 118 | `reminder: yes` (tag `foundation-review/2026-11-06`, 40 merges, threshold 30); form check exit 0, check of private paths exit 0 (1 run each); branch pushed, request opened as a draft |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | Does the task leave an open design choice? Task, *Settlements to record* | No | rows 1 and 2, questions 2 and 3 of the task | writing a spec | a spec cycle spent on settled wording | route |
| Q2 | Add a clause on size to `project-level/plan/template.md`, which restates WAY-146's list of what the critique judges and is not named by the task? Author's report | Yes, one clause, same words as the decision | the template paragraph copies WAY-146's binding sentence; leaving it makes a derived document misstate the decision; the whole-change review judged it right | leaving the template stale and listing it in the request | one clause in an unnamed file, struck on a finding of the review | `44c1d99`, whole-change review |
| Q3 | Touch the `plan_check.py` docstring (lists what the check judges nothing about)? Author's report | No | task *Out of scope*; the docstring stays true | editing it | an incomplete docstring | none |
| Q4 | Keep the third item of WAY-146's *Rejected* (author splits after the critique's remark)? Author's report | Keep | the task's question 3, *Not chosen*; the whole-change review judged it required | striking it | one extra item in *Rejected* | `0ed5ad7` |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| frozen task | `.runs/task-cycles/oversized-plan-tasks/task.md` | orchestrator | n/a |
| code commits | `0ed5ad7`, `44c1d99` | the-way-author (haiku) | `PASS 44c1d99` |
| fix commit | `4e3c4cf` | the-way-author (haiku) | `PASS 4e3c4cf` |
| agent reports | `reports/author-report.md`, `reports/review-whole-report.md`, `reports/author-fix-report.md`, `reports/review-fix-report.md`, `reports/author-return-report.md` | the agents named in Events | see Events |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| gate on the base | not run: `5a24ac9` is a merge commit whose tree equals the tree of the head `c4f57da` of the merged branch (`git rev-parse` of both print `c4f94c669f3c88b6eb9f8459794b5f04fb9c4ddb`); the list is taken from the final gate of that branch's cycle: `docs/task-cycles/installer-junction-refusal/cycle.md` in the commit `73c5437` | final gate of that cycle, tree `a6ddd8c`: exit 0, 1271 tests in 10 directories, every directory passed | no test failing before the change |
| `python -B task-cycle/gate_times.py --output .runs/task-cycles/oversized-plan-tasks/gate_times.md -- python -B gate/run_tests.py`, run 1 | orchestrator, `4e3c4cf`, Windows | exit 1; 1274 tests in 10 directories (`final-gate-1-failed.log`) | failed: directory `gate`, `test_a_number_of_jobs_limits_the_directories_that_run_at_once`, a trial directory did not meet the others within 120 s; outside the task's parts; cause unproven, ten directories ran at once |
| `python -B gate/run_tests.py gate` | orchestrator, `4e3c4cf` | exit 0, 36 tests in 25 s (`gate-dir-diagnosis.log`) | none; diagnosis only |
| same gate command, run 2 | orchestrator, `4e3c4cf`, Windows | exit 0; 1271 tests in 10 directories, every directory passed (`final-gate.log`) | none; the check failed in 1 of 2 cycle runs and passed in 1 |
| `python -B elements/common/foundation_check.py` | author, reviewers, each head | exit 0, `0 errors` | none |
| `python -B -m unittest discover -s project-level -p "test_*.py"` | author on each of three heads, whole-change reviewer | exit 0, 275 tests | none; the reviewer of the fix did not rerun it, the fix being prose |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator | exit 0; tag `foundation-review/2026-11-06`, merges 40, threshold 30, `reminder: yes` | none |
| `python -B task-cycle/cycle_stages.py`, `python -B task-cycle/cycle_measures.py` | orchestrator | exit 0, exit 0 | none |
| `python -B task-cycle/request_check.py .runs/task-cycles/oversized-plan-tasks/request.md --task .runs/task-cycles/oversized-plan-tasks/task.md` | orchestrator | exit 0 (1 run) | none |
| `python -B task-cycle/private_paths_check.py .runs/task-cycles/oversized-plan-tasks/request.md` | orchestrator | exit 0, 1 file, 0 listed (1 run) | none |
| `python -B task-cycle/remarks_check.py .runs/task-cycles/oversized-plan-tasks` | orchestrator, original | run 1 exit 1 listed 10 items; they were appended word for word to the process remarks; run 2 exit 0 (`checked: 5 reports, 10 items other than none, 0 not in the process remarks`); 2 runs | none; the last runs of the three checks on the copy of the record stand in the request's *Checks* |

## Return step

- Foundation compared with code: the entry WAY-146 (binding sentence, *Verification*, *Rationale*, *Rejected*) against `cut_tasks.md`, `critique_plan.md`, `plan/template.md` and the two rows of *Settlements to record*; WAY-13, WAY-143, WAY-120 of the task's *Decisions in play*; the two decisions that derive from WAY-146 and the invariants `project-plan-form` and `project-plan-check`; the part map entry `project-level`: nothing no longer matched, nothing corrected (`reports/author-return-report.md`)
- Decisions written or changed: WAY-146, edited in place (WAY-07) by the change
- Invariants written or changed: none
- Environment facts: none
- Glossary terms: none (the author judged that "too large" is defined inside WAY-146 and `cut_tasks.md` and needs no entry)
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: row 1 and row 2, both by the edit of WAY-146 (no second entry)

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/118, draft until the record's link is added, then ready for review
- Description: `request.md` beside this record, written by `task-cycle/skill/request_template.md`; form check `python -B task-cycle/request_check.py .runs/task-cycles/oversized-plan-tasks/request.md --task .runs/task-cycles/oversized-plan-tasks/task.md` exit 0 (1 run), check of private paths `python -B task-cycle/private_paths_check.py .runs/task-cycles/oversized-plan-tasks/request.md` exit 0 (1 run); in this copy the description is written and checked, and is rewritten after this commit with the record's link and the runs of the three checks on the copy (written and checked after this commit). The reminder of a review of the foundation: `python -B task-cycle/review_reminder.py origin/foundations`: tag `foundation-review/2026-11-06`, merges 40, threshold 30, `reminder: yes`.
- Writes to the task's backlog entry: the request link added to the task's line and its state moved from Ready to Selected (the entry `tasks` under `the-way` in the locations file)
- Corrections after the request opened: none
- Process remarks on the-way:
  - fix, .runs/task-cycles/oversized-plan-tasks/reports/author-fix-report.md: None for this fix. The earlier open items (WAY-13 and WAY-33 tails not read) remain as recorded in `reports/author-report.md`.
  - one author, .runs/task-cycles/oversized-plan-tasks/reports/author-report.md: The handoff's decisions SKILL.md path (`elements/decisions/SKILL.md`): not found there; found at `elements/decisions/skill/SKILL.md`.
  - one author, .runs/task-cycles/oversized-plan-tasks/reports/author-report.md: WAY-33 search for WAY-146 references (grep over the repo): found `foundations/decisions.md` (the WAY-146 entry itself and the two derived entries above), `foundations/invariants.md` lines 238 and 257 (derives from WAY-146; tests; no change needed), `project-level/definition_template.md` line 98, `project-level/plan/skill/critique_plan.md` line 8, `project-level/plan/template.md` lines 6, 123, 181, 187, 188, `project-level/plan_check.py` line 2.
  - one author, .runs/task-cycles/oversized-plan-tasks/reports/author-report.md: Search for "too large", "large task", "tells apart": the other hits concern slices (WAY-?? slice size), audit counts or unrelated "large task" senses; none touches plan tasks.
  - one author, .runs/task-cycles/oversized-plan-tasks/reports/author-report.md: Unclear: whether WAY-146 should gain a *Relations* link to WAY-13 (the size signal). I did not add one; the field is a closed list of two types and WAY-13 is not a higher decision it serves in the strict sense. The cost is small.
  - return step, .runs/task-cycles/oversized-plan-tasks/reports/author-return-report.md: Searched the glossary for "too large", "critique", "preparatory", "project plan": one hit for "preparatory task", none for the others. Unclear whether "task too large" needs an entry; decided none (see above).
  - return step, .runs/task-cycles/oversized-plan-tasks/reports/author-return-report.md: Searched the part map for "critique" and "the check of that plan": hits at lines 70 and 80, both consistent with the change.
  - whole-change review, .runs/task-cycles/oversized-plan-tasks/reports/review-whole-report.md: Not found: a rule in the-way's coding guidelines of size, or guidelines for the-way's own code (none, WAY-328).
  - whole-change review, .runs/task-cycles/oversized-plan-tasks/reports/review-whole-report.md: Unclear: whether the critic of the plan receives `cut_tasks.md` or only the author's prompt (Minor 3); `critique_plan.md` does not say how the criterion reaches it.
  - whole-change review, .runs/task-cycles/oversized-plan-tasks/reports/review-whole-report.md: The handoff said the part map's boundary files of `project-level` are untouched: confirmed by the diff (none of the three scripts changed).

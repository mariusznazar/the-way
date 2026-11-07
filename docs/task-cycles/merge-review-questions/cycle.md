# Cycle record — the way: the order for the merge review asks whether both sides still hold together and names the decisions the merge brought in

- Task source: `C:\Storage\The Brain\The Brain\Notes\Projects\(P) Proces pracy nad produktem\_zadania\zadanie_the_way_pytania_do_przegladu_scalenia.md`, `Status: ready for cycle`, settlements accepted 2026-11-06 (frozen copy: `task.md` beside this record)
- Task relation: independent
- Product repository: `C:\Storage\repos\the-way` (the-way itself; worktree `C:\Storage\repos\the-way\.runs\worktrees\merge-review-questions`)
- Process pin: none (the-way itself)
- Target branch and base: `foundations` (`origin/foundations`), `52889bc700123b50258c4201835034f0529351df`
- Task branch: `task/merge-review-questions`
- Status: request open

## Two questions at start

- Trust boundary: no — the change edits files of the part `task-cycle` (trust boundary: none in `foundations/part_map.md`) and `foundations/decisions.md` (part `decisions`); no script, no network, key, deployment or outside file is touched.
- Irreversible operation: no — text edits and foundation entries only.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none — the four *To do* items give the exact wording; the two rows of *Settlements to record* settle their entries (decisions), and where the rule stands in the log (a new decision or an addition to WAY-162 / WAY-135) is the foundation step's writer's call under WAY-33/WAY-134, not a way left open in the change. Rejected: writing a spec — nothing in the change is left to design. Cost if wrong: a spec round for a four-sentence edit.
- Reserved choice: none
- Execution route and reason: one author without a plan. Four short text edits in five files of one part plus two foundation entries; one agent holds it.
- Author: one author, class `same` (model `sonnet`) — the foundation step writes two decisions into a 9,400-line log with a search of the whole foundation (WAY-33) and a *Rejected* field per decision, which asks for more judgment than ordinary implementation; resumptions: none yet.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: Claude Code background `Agent` calls; completion notification, the turn is yielded while only the result remains.
- Whole-change review: fresh reviewer (sonnet, not cheaper than the orchestrator) by `review-change`; range `52889bc..3601aba`; report `reports/04-whole-review-report.md`, first line `PASS 3601aba4d9277868e8291ffe190c49427bdeb4a6`; six files, `foundations/decisions.md` +69, `task-cycle/skill/SKILL.md` +4 −2, `return_step.md` +4 −3, `spec_review.md` +3 −2, `spec/SKILL.md` +2 −1, `spec/review.md` +2 −2; coverage: every *To do* item 1–4 word for word, both rows of *Settlements to record* (row 1 = WAY-306, row 2 = WAY-307), out of scope untouched, source fidelity confirmed; one-author route, no plan
- Review rounds: no review blocked. The review of the whole change passed with two Minor findings within the task; one fix for them (`a5d6d5f`, range `3601aba..a5d6d5f`, `reports/05-fix-findings.md`, `reports/06-fix-report.md`) and one review of the fix by the same reviewer resumed (`reports/07-fix-review-report.md`, `PASS a5d6d5fafe289985a77518a9ba799bf773d67bb5`, both Minor findings resolved, no new finding). The fix was not reverted. Return step committed nothing, so it had no review. The target branch had not moved at step 12 (no merge, no reconciliation review).
- Weakest-point checks: author: the six quoted sentences of *To do* 1–4 word for word — script, six of six `True` (`reports/02-author-report.md`); fix: the fix stays as small as the findings ask, binding sentences, *Scope*, *Relations* and *Rejected* untouched — `git diff 3601aba` shows 8 insertions and 10 deletions in *Rationale* of WAY-306 and *Verification* and *Rationale* of WAY-307 (`reports/06-fix-report.md`)

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

One-author route: no slices.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 12:00 | Start | orchestrator (sonnet) | task document, `task-cycle/skill/SKILL.md` | — | fast-forwarded the checkout from `86cc21e` to `52889bc` (`origin/foundations`); the skill changed in between, so it was read again from the start |
| 12:10 | Reconcile | orchestrator | `git diff dfd50e5 HEAD` on the five target files | — | the task was written at `dfd50e5`; none of `return_step.md`, `spec_review.md`, `spec/`, `review/SKILL.md` changed, and the step-12 sentence is word for word as the task quotes it (now at `SKILL.md:415-418`, was 389-391); the task's *To do* stands as written |
| 12:12 | Branch | orchestrator | `git worktree add` | worktree above | branch `task/merge-review-questions` at `52889bc`; base gate started in a detached checkout `.runs/base-52889bc` of the worktree, log `base_gate.log` |
| 12:25 | Author | one author, sonnet (class `same`), background | `reports/01-author-handoff.md`, `task-cycle/change/SKILL.md` | `reports/02-author-report.md` | `done`; commits `5932216` (WAY-306, WAY-307 in `foundations/decisions.md`, +69) and `3601aba` (5 skill files, +14 −8); checks: foundation_check exit 0, `gate/run_tests.py task-cycle` exit 0, `elements/common` exit 0, own-work script exit 0 |
| 12:35 | Mechanical check | orchestrator | `git status`, `git diff --stat 52889bc HEAD`, report | — | worktree clean; range non-empty (6 files); each check carries command and exit code; **Searches** section present; own-work check present; `task-cycle/review/SKILL.md` untouched |
| 12:40 | Whole-change review | fresh reviewer, sonnet (class `same`, not cheaper than the orchestrator), background | `reports/03-whole-review-handoff.md`, `task-cycle/review/SKILL.md`, range `52889bc..3601aba` | `reports/04-whole-review-report.md` | `PASS 3601aba4d9277868e8291ffe190c49427bdeb4a6`; 0 blocking, 2 Minor within the task, 0 out of scope; six files +84 −10 (`decisions.md` +69, `SKILL.md` +4 −2, `return_step.md` +4 −3, `spec_review.md` +3 −2, `spec/SKILL.md` +2 −1, `spec/review.md` +2 −2); checks: foundation_check exit 0, `gate/run_tests.py task-cycle` exit 0 |
| 12:55 | Fix of the Minor findings (WAY-161) | the one author resumed, sonnet (class `same`) | `reports/05-fix-findings.md` (reviewer's words), `task-cycle/change/SKILL.md` | `reports/06-fix-report.md` | `done`; commit `a5d6d5f` (`foundations/decisions.md` +8 −10); `spec_review.md` and the other four sentences untouched; foundation_check exit 0, `gate/run_tests.py task-cycle` exit 0; mechanical check passed (clean tree, non-empty range, searches `none`) |
| 13:05 | Review of the fix | same reviewer resumed, sonnet | range `3601aba..a5d6d5f`, `reports/06-fix-report.md`, `reports/05-fix-findings.md` | `reports/07-fix-review-report.md` | `PASS a5d6d5fafe289985a77518a9ba799bf773d67bb5`; both Minor findings resolved, no new finding; foundation_check exit 0, `gate/run_tests.py task-cycle` exit 0; searches `none` |
| 13:15 | Gate (step 10) | orchestrator | `python -B gate/run_tests.py` on `a5d6d5f` | `gate_a5d6d5f.log` | exit 0; 765 tests in 9 directories, every directory passed |
| 13:35 | Return step (step 11) | the one author resumed, sonnet | `reports/08-return-step-handoff.md`, `task-cycle/skill/return_step.md`, `foundation_step.md` | `reports/09-return-step-report.md` (pending) | dispatched |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | Does the task stand after the checkout moved from `dfd50e5` to `52889bc`? (*Inputs and authority*, step 1) | Yes; line numbers of step 12 differ (415-418), text and the four other targets are unchanged | `git diff dfd50e5 HEAD --stat` on the target files: empty; `grep` of the step-12 sentence | stopping to re-ask the human | none | author's handoff |
| Q3 | How is Minor 2 of the whole-change review fixed, given that the fix would need words in `spec_review.md` beyond the sentence the task fixes word for word? (reviewer: "the cycle's call") | Leave the five sentences of *To do* 1–4 as the human fixed them; align WAY-307's *Verification* examples with what the skill texts say; if that cannot be done, the author says so and `spec_review.md` stays | `reports/04-whole-review-report.md` Minor 2; task *To do* 3 and 4, *Questions to settle* 3 | add words to `spec_review.md` telling the orchestrator to put the path in the dispatch | the orchestrator may omit the path (the reviewer's method still names it); a later task adds the words | fix handoff `reports/05-fix-findings.md` |
| Q2 | Does the cycle need a spec? | No (see *Open design choice at start*) | task document: wording given in full in *To do*; *Questions to settle* all answered | a spec | a spec round for four sentences | route |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| Frozen task | `task.md` beside this record (source path above) | orchestrator | — |
| Code and entries | `5932216` (WAY-306, WAY-307), `3601aba` (five skill files), `a5d6d5f` (fix of the Minor findings) | one author (sonnet) | `PASS 3601aba`, fix `PASS a5d6d5f` |
| Stages | `stages.md` beside this record | orchestrator | — |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| `python -B gate/run_tests.py` on the reviewed change (worktree, `a5d6d5f`, log `gate_a5d6d5f.log`) | orchestrator, `a5d6d5f`, Windows | exit 0; 765 tests in 9 directories, every directory passed | none |
| `python -B task-cycle/remarks_check.py .runs/task-cycles/merge-review-questions` | orchestrator, `a5d6d5f` | first run exit 1 (8 items listed, all from reports 02 and 04, appended word for word); last run exit 0, nothing listed; 3 runs in all (the third before the commit of the record) | none |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator | exit 0, `reminder: no` (3 merges since tag `foundation-review/2026-11-06`, threshold 30) | none |
| `python -B task-cycle/request_check.py .runs/task-cycles/merge-review-questions/request.md --task .runs/task-cycles/merge-review-questions/task.md` | orchestrator | exit 0, form holds (run 1 of 1 before this commit) | none |
| `python -B elements/common/foundation_check.py` and `python -B gate/run_tests.py task-cycle` (reported by author, reviewers, return step) | agents, `a5d6d5f` | exit 0 and exit 0 (0 errors; 151 tests OK) | none |
| `python -B gate/run_tests.py` on the base (detached checkout `.runs/base-52889bc`, log `base_gate.log`) | orchestrator, `52889bc`, Windows | exit 0; 765 tests in 9 directories, every directory passed. No check failing on the base. | none |

## Return step

- Foundation compared with code: WAY-306 against step 12 (`SKILL.md:415-420`), WAY-307 against `spec_review.md`, `spec/SKILL.md`, `spec/review.md`, the task's WAY-150, WAY-162, WAY-11, WAY-135, and the `task-cycle` part-map entry; nothing no longer matched; search of the foundation found nothing that disagrees; `foundation_check.py` 0 errors (`reports/09-return-step-report.md`)
- Decisions written or changed: WAY-306, WAY-307 (written by the foundation step; none by the return step)
- Invariants written or changed: none
- Environment facts: none
- Glossary terms: none
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: row 1 — WAY-306; row 2 — WAY-307
- Result: `done`, no commit, so no review of the return step

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/81 — draft at first, marked ready for review after the record's link is in the description
- Description: `request.md` beside this record, written by `task-cycle/skill/request_template.md`; form check `python -B task-cycle/request_check.py .runs/task-cycles/merge-review-questions/request.md --task .runs/task-cycles/merge-review-questions/task.md` exit 0 on the first run (1 run before this commit); written and checked after this commit for the record link
- Writes to the task's backlog entry: the request link and the state, in the task's line of `_tasks_active.md`, after the request is ready
- Process remarks on the-way:
  - Author, C:/Storage/repos/the-way/.runs/worktrees/merge-review-questions/.runs/task-cycles/merge-review-questions/reports/02-author-report.md: The handoff says the step-12 sentence is at `task-cycle/skill/SKILL.md:415-418`; it was (now 415-420 after the edit). The task's cited numbers (`389-391`, `:10-11`, `:6-7`, `:18-19`, `:18-20`) matched the files at the base commit for the four other targets, within a line or two. None unclear.
  - Author, C:/Storage/repos/the-way/.runs/worktrees/merge-review-questions/.runs/task-cycles/merge-review-questions/reports/02-author-report.md: A mismatch in the task text: *To do* 2 quotes a sentence that PR #75 changed; the answer to question 1 resolves it and I followed it. Not unclear.
  - Author, C:/Storage/repos/the-way/.runs/worktrees/merge-review-questions/.runs/task-cycles/merge-review-questions/reports/02-author-report.md: `elements/decisions/examples.md` names WAY-03 as the example; not read separately beyond the template and the entries read for the handoff (WAY-01, 11, 30 ... follow the same form). Recorded here in case the reviewer holds that reading was required.
  - Author, C:/Storage/repos/the-way/.runs/worktrees/merge-review-questions/.runs/task-cycles/merge-review-questions/reports/02-author-report.md: Otherwise: none.
  - Whole-change review, C:/Storage/repos/the-way/.runs/worktrees/merge-review-questions/.runs/task-cycles/merge-review-questions/reports/04-whole-review-report.md: The handoff says the step-12 sentence is "now at `task-cycle/skill/SKILL.md:415-420`"; it is at 415-420. Clear.
  - Whole-change review, C:/Storage/repos/the-way/.runs/worktrees/merge-review-questions/.runs/task-cycles/merge-review-questions/reports/04-whole-review-report.md: I did not read `product-guidelines/reading.md` or the guidelines of the `task-cycle` part: the change is prose of skills and two decision entries and writes no code or guidelines; whether a guideline of the `task-cycle` part exists that a skill sentence must meet was not searched beyond `git grep` of the changed phrases. Marked unverified, not found to be a gap.
  - Whole-change review, C:/Storage/repos/the-way/.runs/worktrees/merge-review-questions/.runs/task-cycles/merge-review-questions/reports/04-whole-review-report.md: `elements/decisions/examples.md` not read (the template was enough to judge form). Unclear whether the author's report note on it matters; I found no consequence.
  - Whole-change review, C:/Storage/repos/the-way/.runs/worktrees/merge-review-questions/.runs/task-cycles/merge-review-questions/reports/04-whole-review-report.md: Otherwise: none.

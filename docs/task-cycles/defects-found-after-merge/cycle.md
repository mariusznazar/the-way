# Cycle record — Miara błędów znalezionych po scaleniu: linia w nagłówku każdego zadania i nazwana przyczyna każdej poprawki po otwarciu prośby

- Task source: the task's note in the author's backlog — settlements accepted 2026-11-12, `Status: ready for cycle`; frozen copy `task.md` beside this record
- Task relation: independent
- Product repository: the-way (mariusznazar/the-way)
- Process pin: the-way itself, no pin; the worktree's own tree
- Target branch and base: foundations, `6814c6f6c9ff2b29d34612fa5cc86945ec3a2812`
- Task branch: task/defects-found-after-merge (worktree `.runs/worktrees/defects-found-after-merge`)
- Status: request open, corrected once

## Two questions at start

- Trust boundary: no — the change edits `project-level/task/template.md` and its skill files, `task-cycle/record_template.md`, `task-cycle/skill/correction.md`, `task-cycle/skill/request_template.md` and `process-audit/problem_register.md`, and writes decisions. The part map names as trust boundary `task-cycle/cycle_stages.py`, `cycle_measures.py`, `gate_times.py`, `process-audit/audit_count.py` and three scripts of project-level; none is a file the task changes.
- Irreversible operation: no — the two human actions (the classes in the user's own register, the nightly review) are effects outside the repository that the human performs at the request, listed there; the cycle performs neither.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none — every choice of the task is a row of *Settlements to record* or an answer in *Questions to settle*. The two *Questions carried to cycle* (the number of the new kind of item, the place of the new record item) follow from the existing files (kinds 1–16 stand in `request_template.md`; the record template's last item is the process remarks), see the questions table.
- Reserved choice: none
- Execution route and reason: one author without a plan — the change is edits of six existing files and eleven decisions, all of one meaning; one agent can hold it.
- Author: one author, class `same` (not `cheaper`): the change crosses three parts (project-level, task-cycle, process-audit) and eleven decision entries must match the wording of the files in all three. Model: the harness model closest to the orchestrator's (sonnet). Resumptions: for the fix of the three Minor findings (commit `6d3298b`) and for the return step (no commit).
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: Claude Code — a foreground `Agent` call blocks; a background agent reports by completion notification, on which the turn is yielded.
- Whole-change review: fresh reviewer, sonnet (same class), `review-change`; range `6814c6f..10c0f9e` (head of the author's first return), nine files, 305 added and 11 removed lines; first line `PASS 10c0f9eed88d05b2cff8145d2c58227e94346c6d`, report `reports/reviewer-report.md`; coverage: all four *To do* items, all eleven rows (WAY-355 to WAY-359) and the *Questions to settle* answers checked, source fidelity checked, no blocking finding, so none comes from a slice; 5 Minor findings, 3 within the task (fixed), 2 outside it (in the request); 18 decisions read whole and 165 by title. The reviewer named WAY-286, 288, 295, 306, 308, 309, 323, 337, 344, 161, invariants of part `every` and the glossary as unread; the gap was closed by the same reviewer, resumed, in the review of the fix (28 decisions whole, 155 by title; no new finding).
- Review rounds:
  - findings `reports/whole-change-findings.md`: fix of the three Minor findings of the whole-change review within the task (blocking findings: none). Fix range `10c0f9e..6d3298b` (one commit, `6d3298b`), fix report `reports/author-fix-report.md`; review of the fix by the same reviewer, resumed: `PASS 6d3298b`, `reports/reviewer-fix-report.md`, no finding; no revert.
- Weakest-point checks: the author named "the readers still read the forms" (the new record item must not disturb `remarks_check.py`, the audit's reading of the record, and a description with item 17 must pass the form check): two tests added, a mutation run (the corrections item moved after the remarks fails the template test), and a script that ran the form check on a description with item 17 alone and the header reader on the new task header — no reader broke (`reports/author-report.md`, own-work check). The reviewer repeated the mutation run on a copy of the head.

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

Not applicable: the one-author route.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-13 15:5x | start | orchestrator (sonnet 5.5) | `implement-task`; task document | `task.md` | task `ready for cycle`, `Project relation: independent`; checkout of `foundations` equal to `origin/foundations` at `6814c6f`, clean |
| 2026-11-13 16:00 | start | orchestrator | worktree and branch from `foundations` | branch `task/defects-found-after-merge` | base `6814c6f`; checkout of the base in `.runs/base-check` |
| 2026-11-13 16:10 | make change | one author, class `same`, sonnet (background `Agent`) | `reports/author-handoff.md`; `make-change` "the whole change as the one author"; frozen task | `reports/author-report.md` | dispatched; the turn yields until its completion notification |
| 2026-11-13 16:35 | make change (return) | one author, sonnet | — | `reports/author-report.md`; commits `4fcec13`, `aea8c2c`, `15b1041`, `10c0f9e` | `done with concerns`; mechanical check: worktree clean, range non-empty, nine files all within the task's four *To do* items and its rows; checks have commands and exit codes, own-work check, Unread material and Searches present; gap of unread process-audit decisions carried to the reviewer of the whole change (choice Q3) |
| 2026-11-13 16:40 | whole-change review | fresh reviewer, same class (sonnet) | `reports/reviewer-handoff.md`; `review-change` "the whole change"; range `6814c6f..10c0f9e` | `reports/reviewer-report.md` | dispatched |
| 2026-11-13 17:00 | whole-change review (result) | reviewer | — | `reports/reviewer-report.md` | `PASS 10c0f9e`; 0 blocking, 5 Minor (3 within the task, 2 outside); 18 decisions read whole, 165 by title; named as unread that may bear: WAY-286, 288, 295, 306, 308, 309, 323, 337, 344, 161, invariants of part `every`, the glossary — to be read by the reviewer in the review of the fix |
| 2026-11-13 17:05 | fix of Minor findings | one author, resumed | `reports/whole-change-findings.md` (findings 1–3) | `reports/author-fix-report.md` | dispatched |
| 2026-11-13 17:20 | fix of Minor findings (result) | one author | `reports/whole-change-findings.md` | `reports/author-fix-report.md`; commit `6d3298b` | `done`; four files, six lines; mechanical check: worktree clean, range non-empty, report has checks with commands and exit codes, own-work check, Unread material, Searches. The author also updated `author-report.md` after the first return |
| 2026-11-13 17:25 | review of the fix + closing the reviewer's unread gap | reviewer, resumed | message naming `reports/whole-change-findings.md`; range `10c0f9e..6d3298b`; decisions WAY-286, 288, 295, 306, 308, 309, 323, 337, 344, 161 and invariants/glossary to read | `reports/reviewer-fix-report.md` | dispatched |
| 2026-11-13 17:35 | review of the fix (result) | reviewer, resumed | — | `reports/reviewer-fix-report.md` | `PASS 6d3298b`; no finding; the reviewer read whole WAY-286, 288, 295, 306, 308, 309, 323, 337, 344, 161, three invariants and the glossary: gap closed; 28 decisions whole and 155 by title |
| 2026-11-13 17:40 | return step | one author, resumed | `reports/author-return-handoff.md`; `return_step.md`, `foundation_step.md` | `reports/author-return-report.md` | dispatched; the gate starts after it and any review of it |
| 2026-11-13 16:02 | verification | orchestrator | gate on the base through `gate_times.py` | `gate_times.md`, `base_gate_stdout.txt` | exit 0, 1200 tests; see *Verification* |
| 2026-11-13 17:50 | return step (result) | one author | — | `reports/author-return-report.md` | `done`; no commit, nothing to correct; every row written; no review of the return step since it committed nothing |
| 2026-11-13 17:52 | reconciliation | orchestrator | `git fetch`; target branch `foundations` still `6814c6f` | — | nothing to merge; the final tree equals the reviewed one |
| 2026-11-13 17:55 | verification | orchestrator | gate on the final tree through `gate_times.py` | `gate_times.md`, `final_gate_stdout.txt` | exit 0, 1203 tests |
| 2026-11-13 18:20 | stages and measures | orchestrator | `cycle_stages.py`, `cycle_measures.py`, session `74cb4adf-a7bb-4219-8069-9e18b8fdc041` | `stages.md`, `mechanism_measures.md` | both exit 0 |
| 2026-11-13 18:25 | request | orchestrator | `request.md`; form check and private-path check | https://github.com/mariusznazar/the-way/pull/107 | draft, blocked: two human actions; branch pushed first |
| 2026-11-13 19:00 | correction 1 (start) | orchestrator (sonnet 5.5, new session) | link to the human's remarks: comment on the request, written by the advisor of the day on the human's behalf; `correction.md` | `reports/correction-1-remarks.md` | remarks bind: item 3 of *Fix or let through* (finding outside the task's scope 2, kind 8) — "fix it in this request"; the two items of *Needed from you* are done outside the repository and untouched. `git fetch`: target branch `foundations` still `6814c6f`, the branch's base; main checkout level with `origin/foundations`; nothing to merge, so no review of a merge. Record field *Reserved choice*: `none` |
| 2026-11-13 19:05 | correction 1 (dispatch) | fresh author, class `same` (the first author's agent cannot be resumed from this session), sonnet (foreground `Agent`) | `reports/correction-1-author-handoff.md`; `make-change` "a correction for the human's remarks" | `reports/correction-1-author-report.md` | dispatched |
| 2026-11-13 19:10 | correction 1 (result) | fresh author, sonnet | — | `reports/correction-1-author-report.md`; commit `a3152c9` | `done`; one file (`task-cycle/skill/request_template.md`, +6 −1); mechanical check: worktree clean, range `716b22a..a3152c9` non-empty, the changed file is the one the remark names; checks with commands and exit codes (task-cycle tests 367 OK, foundation check 0 errors, private-path check 0), own-work check, Unread material and Searches present; no decision changed |
| 2026-11-13 19:12 | correction 1 (review) | fresh reviewer, same class (sonnet) | `reports/correction-1-reviewer-handoff.md`; `review-change` "a later change to an open request"; range `716b22a..a3152c9`; remarks in place of a findings file | `reports/correction-1-reviewer-report.md` | dispatched |
| 2026-11-13 19:25 | correction 1 (review result) | reviewer, sonnet | — | `reports/correction-1-reviewer-report.md` | `PASS a3152c9`; 0 blocking, 2 Minor (wording of the two-source example: "a defect the task required", "which the cycle judged nothing about"), 1 outside the task (the variants table row "A correction" asks for "corrected for your remarks" in the state line, which a refresh-only correction has no remarks for); a correction's Minor findings are not fixed and go to the request's lists. Unread: the tail of the *Rejected* paragraph of WAY-289 — recorded as Q5, bears on nothing it judged |
| 2026-11-13 19:30 | correction 1 (return step) | fresh author resumed, sonnet | `reports/correction-1-return-handoff.md`; `return_step.md`, `foundation_step.md` | `reports/correction-1-author-return-report.md` | dispatched; the gate starts after it and any review of it |
| 2026-11-13 19:40 | correction 1 (return step result) | author, resumed | — | `reports/correction-1-author-return-report.md` | `done`, no commit: WAY-287, WAY-357, WAY-358 and the part-map entry of `task-cycle` compared with the changed sentence, nothing no longer matched; no review of the return step since it committed nothing |
| 2026-11-13 19:45 | correction 1 (verification) | orchestrator | gate on the corrected tree `a3152c9` through `gate_times.py` | `gate_times.md`, `correction-1_gate_stdout.txt` | exit 0, 1203 tests in 10 directories, 714.5 s |
| 2026-11-13 20:05 | correction 1 (stages and measures) | orchestrator | `cycle_stages.py`, `cycle_measures.py`, sessions `74cb4adf-a7bb-4219-8069-9e18b8fdc041` and `d0bcc7ef-db77-46e6-8c08-87e6b6618829` | `stages.md`, `mechanism_measures.md` | both exit 0 (run again at the end of the correction, below) |
| 2026-11-13 20:15 | correction 1 (reconciliation) | orchestrator | `git fetch`: the target branch `foundations` moved to `65b6d70` (pull request #108, merged during the correction); `git merge origin/foundations` conflicted in `foundations/decisions.md`: both sides added WAY-353 and WAY-354 | merge commit `73fb11d` | the target branch's two keep their numbers; this branch's five became WAY-355 to WAY-359, with their references; this record names them by the new numbers everywhere except in this line and the next; the reports and handoffs written before the merge (`reports/author-*`, `reviewer-*`, `whole-change-findings.md`, `correction-1-author-*`) name them by their old numbers WAY-353 to WAY-357 |
| 2026-11-13 20:20 | correction 1 (merge work) | fresh author resumed, sonnet | `reports/correction-1-merge-handoff.md` | `reports/correction-1-merge-report.md`; commit `73fb11d` | `done`; checks exit 0 (foundation check; task-cycle 367, process-audit 180, project-level 275, elements/common 144, agent-instructions 18 tests); the author read the target branch's WAY-353 and WAY-354 by heading and block only: carried into the review of the merge |
| 2026-11-13 20:30 | correction 1 (review of the merge) | fresh reviewer, same class (sonnet) | `reports/correction-1-merge-review-handoff.md`; `review-change` "the reconciliation with the target branch"; merge `73fb11d` | `reports/correction-1-merge-reviewer-report.md` | dispatched |
| 2026-11-13 20:45 | correction 1 (review of the merge, result) | reviewer, sonnet | — | `reports/correction-1-merge-reviewer-report.md` | `PASS 73fb11d`; 0 blocking, 1 Minor (the *Return step* lines of this record named the old numbers; corrected in the record, which no commit holds before the copy), 0 outside the task; read whole every decision named (WAY-353 and WAY-354 of the target branch among them): the author's gap closed; checks exit 0 |
| 2026-11-13 20:50 | correction 1 (verification) | orchestrator | gate on the merged tree `73fb11d` through `gate_times.py` | `gate_times.md`, `correction-1_merged_gate_stdout.txt` | exit 0, 1203 tests in 10 directories, 788.1 s; the target branch `foundations` still `65b6d70` after a fetch |
| 2026-11-13 21:10 | correction 1 (stages and measures) | orchestrator | `cycle_stages.py`, `cycle_measures.py`, sessions `74cb4adf-a7bb-4219-8069-9e18b8fdc041` and `d0bcc7ef-db77-46e6-8c08-87e6b6618829` | `stages.md`, `mechanism_measures.md` | both exit 0 |
| 2026-11-13 21:25 | correction 1 (request) | orchestrator | `request.md` rewritten by `request_template.md`, variant for a correction; form check and check of private paths | https://github.com/mariusznazar/the-way/pull/107 | the form check and the check of private paths exit 0; the copy of the record is committed next, then the link and the copy's checks are added and the description published with `gh pr edit` |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | Number of the new kind of item in the request template's list of kinds (*Questions carried to cycle*) | 17 | `task-cycle/skill/request_template.md` "The kinds of items" holds kinds 1–16; the kind stands in *You accept by merging*, after kind 15, since the items of a group come in the order of their kinds | reuse of a number, or a kind numbered inside the group's order | a reader of "item 17" meets another kind; each reference to the number would need a change | author, `request_template.md`, `correction.md` |
| Q2 | Place of the new item in the record template (*Questions carried to cycle*) | an item of *Request handoff* placed before the item `Process remarks on the-way`, which stays the last item of the record | `record_template.md` "Request handoff", and WAY-296 ("the last item of the record") | a section of its own after the remarks, or in *Events* | the check of the remarks and the nightly review cut the remarks as the last item; a section after it would break the cut | author, `record_template.md` |
| Q3 | The author's Unread material: 14 decisions of `process-audit` scope left unread | carry the gap into the handoff of the reviewer of the whole change, which selects its own reading and reads whole what concerns the topic | the handoff to the author said "as far as the new classes and columns need"; the author judged the 14 by title | resuming the author to read them: the reviewer's own, independent reading covers the same ground | a decision about the register or the count that the change contradicts goes unnoticed until after the merge | `reports/reviewer-handoff.md` |
| Q4 | Concern 1 of the author: the description after correction n shows only that correction's pairs | accept as the task words it ("pary tej poprawki"); the record keeps every line | task *To do* 3 | showing every correction's pairs: not asked by the task | a reader of a twice-corrected request does not see the first correction's pairs in the description | request, *You accept by merging* item on kind 17 |
| Q5 | Reviewer of correction 1 read WAY-289 whole except the last lines of its *Rejected* paragraph | accept: the gap bears on nothing the reviewer judged — the correction touches kind 17 only, and WAY-289 concerns the answers to items 8, 4, 9 and 14 | `reports/correction-1-reviewer-report.md` (Agreement section: WAY-289 not reached by the diff) | resuming the reviewer to read the tail | a rejected alternative of WAY-289 that bears on kind 17 stays unseen | request, *Course of the cycle* |
| Q6 | Cause of correction 1: source and kind | `item 8 · not-required`: the human answered item 3 of the request ("fix it in this request"), whose kind in the template is 8 (a finding outside the task's scope); the task asked the description to show the pairs in one sentence and no document asked for the sentence of a refresh-only correction, so what the correction changed was not required | `task.md` (*To do* 3); WAY-287, WAY-358; reviewer report: the finding was marked outside the task's scope | `item 8 · defect`: counts a missing example as a defect the cycle saw and left, which the task did not require | the register's count of defects left by the cycle is one too high | record line of correction 1, request item on the cause |
| Q7 | Form of the sentence of a refresh-only correction in kind 17 (the author's choice, correction 1) | an example introduced by "such as", with a second example for a correction of two sources, inside kind 17 | `reports/correction-1-author-report.md` (Choices); `request_template.md`, kind 17 | a fixed required wording | a writer takes the example too literally or words it slightly differently; harmless, since the form check judges no content | request, *You accept by merging* |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| Frozen task | `.runs/task-cycles/defects-found-after-merge/task.md` | orchestrator | — |
| Code and foundation commits | `4fcec13`, `aea8c2c`, `15b1041`, `10c0f9e` (range `6814c6f..10c0f9e`) | one author | `PASS 10c0f9e` (whole change) |
| Fix of Minor findings | `6d3298b` | one author, resumed | `PASS 6d3298b` |
| Full reports | `reports/author-report.md`, `author-fix-report.md`, `author-return-report.md`, `reviewer-report.md`, `reviewer-fix-report.md`; findings `reports/whole-change-findings.md` | agents | — |
| Correction 1 | `a3152c9` (range `716b22a..a3152c9`); remarks `reports/correction-1-remarks.md`; reports `correction-1-author-report.md`, `correction-1-reviewer-report.md`, `correction-1-author-return-report.md` | fresh author, resumed for the return step | `PASS a3152c9` |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| `python -B task-cycle/gate_times.py --output ../task-cycles/defects-found-after-merge/gate_times.md -- python -B gate/run_tests.py` | orchestrator, base `6814c6f`, `.runs/base-check` | 0 — 1200 tests in 10 directories, every directory passed (1213.8 s) | none; no check fails on the base |
| `python -B task-cycle/gate_times.py --output .runs/task-cycles/defects-found-after-merge/gate_times.md -- python -B gate/run_tests.py` | orchestrator, final tree `6d3298b`, worktree | 0 — 1203 tests in 10 directories, every directory passed (667.5 s) | none |
| `python -B elements/common/foundation_check.py --skip-test-citations .` | author (first return, fix, return step) and reviewer | 0 — 0 errors | none |
| `python -B gate/run_tests.py <directory>` for `task-cycle`, `process-audit`, `project-level`, `elements/common`, `agent-instructions` | author; reviewer (all but `elements/common`), commits `10c0f9e`, `6d3298b` | 0 each; one failed run of `process-audit` (the author's own new test asserted a wrong value; corrected in `10c0f9e`) | none |
| `python -B task-cycle/remarks_check.py .runs/task-cycles/defects-found-after-merge` | orchestrator, original record | last run exit 0, 2 runs (the first listed 10 items, then added to the process remarks) | none |
| `python -B task-cycle/cycle_stages.py` and `python -B task-cycle/cycle_measures.py` | orchestrator | both exit 0 | none |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator | exit 0; `merges: 29`, `threshold: 30`, `reminder: no` | none |
| `python -B task-cycle/request_check.py .runs/task-cycles/defects-found-after-merge/request.md --task .runs/task-cycles/defects-found-after-merge/task.md` and `python -B task-cycle/private_paths_check.py` on the same file | orchestrator | last run of each exit 0, 1 run of each | none |
| `python -B task-cycle/private_paths_check.py docs/task-cycles/defects-found-after-merge` | orchestrator, cleaned copy | last run exit 0, 2 runs (the first listed 12 places: absolute paths and note links; cleaned by one rewriting) | none |
| `python -B task-cycle/image_files_check.py docs/task-cycles/defects-found-after-merge` | orchestrator, cleaned copy | exit 0, 1 run | none |
| `python -B task-cycle/remarks_check.py docs/task-cycles/defects-found-after-merge` | orchestrator, cleaned copy | exit 0, 1 run, 10 items, 0 missing | none |
| `python -B task-cycle/gate_times.py --output .runs/task-cycles/defects-found-after-merge/gate_times.md -- python -B gate/run_tests.py` | orchestrator, corrected tree `a3152c9`, worktree (correction 1) | 0 - 1203 tests in 10 directories, every directory passed (714.5 s) | none |
| `python -B gate/run_tests.py task-cycle`, `python -B -m unittest task-cycle/test_request_check.py`, `python -B elements/common/foundation_check.py --skip-test-citations .`, `python -B task-cycle/private_paths_check.py task-cycle/skill/request_template.md` | author and reviewer of correction 1, commit `a3152c9` | 0 each (367 tests; 74 tests; 0 errors; 0 listed) | none |
| `python -B task-cycle/gate_times.py --output .runs/task-cycles/defects-found-after-merge/gate_times.md -- python -B gate/run_tests.py` | orchestrator, merged tree `73fb11d`, worktree (correction 1, after the merge) | 0 - 1203 tests in 10 directories, every directory passed (788.1 s) | none |
| `python -B elements/common/foundation_check.py --skip-test-citations .` and `python -B gate/run_tests.py <directory>` for `task-cycle`, `process-audit`, `project-level`, `elements/common`, `agent-instructions` | author and reviewer of the merge, merge commit `73fb11d` | 0 each (367, 180, 275, 144, 18 tests; 0 errors); `foundation-review` holds no test file | none |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator, after the merge | exit 0; `merges: 30`, `threshold: 30`, `reminder: yes` | none |
| the nightly review of cycles | not run | the user's tool, outside the repository | unchecked |

## Return step

- Foundation compared with code: WAY-355 to WAY-359 and WAY-287, the entries of the task's *Decisions in play*, and the part-map entries of `project-level`, `task-cycle` and `process-audit` compared with the files; nothing no longer matched, nothing corrected (`reports/author-return-report.md`)
- Decisions written or changed: WAY-355, WAY-356, WAY-357, WAY-358, WAY-359 written; WAY-287 changed in place
- Invariants written or changed: none
- Environment facts: none
- Glossary terms: none
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: rows 2 (WAY-355); 1, 3, 7, 8 (WAY-356); 4, 9 (WAY-357); 5, 10 (WAY-358); 6, 11 (WAY-359) — all eleven

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/107, draft, blocked
- Description: `request.md` beside this record, written by `task-cycle/skill/request_template.md` in its variant for a correction; form check `python -B task-cycle/request_check.py .runs/task-cycles/defects-found-after-merge/request.md --task .runs/task-cycles/defects-found-after-merge/task.md` exit 0 and check of private paths exit 0 on the description written for the correction; in the copy committed after the correction: `written and checked after this commit`
- Writes to the task's backlog entry: none — the line stays `[/]` as the author set it; the rules of the task place (the author's rulebook) give no form for a request link on a line, and `project-level/task_line.md` says to write no form of one's own
- Corrections after the request opened:
  - correction 1, remarks `reports/correction-1-remarks.md`: item 8 · not-required
- Process remarks on the-way:
  - make change (one author), .runs/task-cycles/defects-found-after-merge/reports/author-report.md: The handoff says to check "that the nightly cut of the remarks ... still read the template's form"; the nightly review is the user's tool outside the repository, so I could check only `remarks_check.py` (whose cut the nightly review is said to follow) and `audit_count.py`, not the tool itself. Unclear whether the nightly cut reads exactly as `remarks_check.remark_blocks` does.
  - make change (one author), .runs/task-cycles/defects-found-after-merge/reports/author-report.md: The handoff names `project-level/task/skill/` "the file that fits — `draft.md` is the likely place"; no file of the skill lists the header lines of the task document, so `draft.md` is a judgment, not a found place.
  - make change (one author), .runs/task-cycles/defects-found-after-merge/reports/author-report.md: No decision or glossary entry states the term "fixing task" or "correction"; I used them in their ordinary meaning.
  - review of the fix, .runs/task-cycles/defects-found-after-merge/reports/reviewer-fix-report.md: The nightly review of cycles (the user's tool) is outside the repository; I could not check that it reads the new item, the remarks files and the line `Defect introduced by:`; I checked only `remarks_check.py` and `audit_count.py` (unchanged from my first report).
  - review of the fix, .runs/task-cycles/defects-found-after-merge/reports/reviewer-fix-report.md: I found no file that lists the header lines of a task document, so `project-level/task/skill/draft.md` as the place that has the line filled is a judgment (unchanged from my first report).
  - review of the fix, .runs/task-cycles/defects-found-after-merge/reports/reviewer-fix-report.md: `task-cycle/review/fix.md` (the method for the review of a fix) was not named by the coordinator; I read it after writing the first draft of this report. It asks for each finding fixed or remains (given above: all three fixed), the fix diff inspected for what the fix broke (nothing: four wording changes), and only a new Critical or Important finding failing the review (none).
  - whole-change review, .runs/task-cycles/defects-found-after-merge/reports/reviewer-report.md: The nightly review of cycles (the user's tool) is outside the repository, so I could not check that it reads the new item and the remarks files as the task's *Human actions* ask; I checked only `remarks_check.py` and `audit_count.py`.
  - whole-change review, .runs/task-cycles/defects-found-after-merge/reports/reviewer-report.md: No file lists the header lines of a task document, so `project-level/task/skill/draft.md` as the place that has the line filled is a judgment (the author's; I found no better place and accept it).
  - whole-change review, .runs/task-cycles/defects-found-after-merge/reports/reviewer-report.md: "Fixing task" and "correction" have no glossary entry (the author's third search); no sentence in the files is read wrongly for lack of one, so it is no finding.
  - whole-change review, .runs/task-cycles/defects-found-after-merge/reports/reviewer-report.md: The handoff's author note that the other three directories were not run again after the final test fix: I ran all of them on the head myself (see Checks).

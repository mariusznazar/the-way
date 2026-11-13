# Cycle record — the way: close the "decision pending" notes in the templates in one change

- Task source: the task's note in the author's private backlog, approved 2026-11-13 (frozen copy: `task.md` beside this record)
- Task relation: independent
- Product repository: the-way (https://github.com/mariusznazar/the-way)
- Process pin: this checkout is the-way itself, `fca8491`
- Target branch and base: `foundations`, `fca8491`
- Task branch: `task/close-decision-pending-templates`
- Status: request open

## Two questions at start

- Trust boundary: no — the changed files are templates and a skill file of the elements; the part map gives their parts (`elements-common`, `environment-facts`, `glossary`, `invariants`, `part-map`) no trust boundary.
- Irreversible operation: no.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none — every question of the task's *Questions to settle* (S0, S20–S25, S27) carries the human's answer with its source; the 32 dopiski and the 19 cases are mapped by the task to a decision number or plain text; no entry follows from the change with a way left open.
- Reserved choice: none
- Execution route and reason: one author without a plan — text edits in seven files of the elements, each given by the task; fits one agent; class `cheaper`.
- Author: `cheaper` than the orchestrator (model: haiku), the default for ordinary implementation; resumed for the fix and the return step.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: completion notification (background agents); no limit hit so far
- Whole-change review: a fresh reviewer (sonnet, the orchestrator's class) by `review-change`, range `fca8491`..`2c27260`, `reports/whole-review-report.md`, first line `PASS 2c27260d68a571a0c0d6dafbdad645957f7388cb`; 7 changed files, 45 added and 95 removed lines; 0 blocking, 3 Minor within the task, 1 Minor outside it; every item of the task covered (items 1–9, S0–S25, S27), no settlement row, no projected entry; source fidelity: all citations checked against the whole entries. Its **Unread material** named gaps (23 decisions read whole, no pass by title), so the same reviewer was resumed on the final head and read through all 323 titles, 80 decisions whole, all 33 invariants, the glossary and the part-map entries: `reports/gap-review-report.md`, first line `PASS faee0f877d899070ba090c4e4d546f6ab5af713c`, no blocking finding, two new Minor findings outside the task.
- Review rounds:
  - findings `reports/whole-review-findings.md`: the review of the whole change passed with three Minor findings within the task (no blocking finding). One fix by the author on `cheaper`, commit `faee0f8` (range `2c27260`..`faee0f8`), fix report `reports/fix-report.md`; the same reviewer reviewed the fix once, `reports/fix-review-report.md`, `PASS faee0f877d899070ba090c4e4d546f6ab5af713c`, no new finding. The fix was not reverted.
- Weakest-point checks: author — requirement: each citation is supported by the whole text of its decision entry and no rule changes sense beyond the task's S5 ending and items 2–9; check: reading the 26 decisions of the handoff whole, comparing each citation, `grep -rn "decision pending" elements` listing exactly S26 and S28, `grep -n Draft` on the invariants template empty; it showed four citations weaker than the rest (S3, S4, S7/S11, S9), which went to the review (`reports/author-report.md`). The review confirmed S4, S5 and S10, accepted the departures at S7 and S11, and found S3 and S9 over-cited, fixed (`reports/whole-review-report.md`, `reports/fix-report.md`).

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

One author, no plan: no slices.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-13 | start | orchestrator (sonnet) | task document | `task.md` | `foundations` fast-forwarded 8079485 → fca8491 (17 commits, none touching the skill); branch and worktree created; base-gate started in `.runs/base-check-close-decision-pending-templates` |
| 2026-11-13 | author | author (haiku, `cheaper`) | `reports/author-handoff.md`, `make-change` "the whole change as the one author" | `reports/author-report.md`; commit `2c27260` | `done with concerns`; mechanical check: clean tree, non-empty range, 7 files = the task's files, report holds checks with commands and exit codes, own-work check, Unread material, Searches; next: review of the whole change |
| 2026-11-13 | review of the whole change | reviewer (sonnet) | `reports/whole-review-handoff.md`, `review-change`, range `fca8491`..`2c27260` | `reports/whole-review-report.md` | `PASS 2c27260`; 3 Minor within the task, 1 outside; next: one fix and one review of it |
| 2026-11-13 | fix | author, resumed (haiku) | `reports/fix-handoff.md`, findings `reports/whole-review-findings.md` | `reports/fix-report.md`; commit `faee0f8` | `done`; mechanical check: clean tree, 3 files = the 3 findings' files; next: review of the fix |
| 2026-11-13 | review of the fix | reviewer, resumed (sonnet) | `reports/fix-review-handoff.md`, findings `reports/whole-review-findings.md`, range `2c27260`..`faee0f8` | `reports/fix-review-report.md` | `PASS faee0f8`; no new finding |
| 2026-11-13 | return step | author, resumed (haiku) | `reports/return-step-handoff.md`, `foundation_step.md`, `return_step.md` | `reports/return-step-report.md` | `done`, nothing mismatched, no commit; no review of the return step since it committed nothing |
| 2026-11-13 | review gap | reviewer, resumed (sonnet) | `reports/review-gap-handoff.md` | `reports/gap-review-report.md` | `PASS faee0f8`; read through all titles, 80 decisions whole, all invariants; two new Minor findings outside the task |
| 2026-11-13 | gate | orchestrator | `python -B task-cycle/gate_times.py ... -- python -B gate/run_tests.py` on `faee0f8` | `gate_times.md`, `final-gate.log` | exit 0, 1221 tests in 10 directories passed; `origin/foundations` had not moved, no reconciliation merge needed |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | Class of the one author (step 4) | `cheaper` | the task is text edits mapped by the task to citations; the reviews run on the orchestrator's class | `same` — dearer, nothing in the task needs design | an author's wrong citation costs one fix round; the review checks every citation | author |
| Q3 | The review of the whole change left decisions it named as bearing on the sentences unread (WAY-326) | resumed the same reviewer on the final head to read through the rest by title and to read whole what it had named | `reports/review-gap-handoff.md`, `reports/gap-review-report.md` | leaving a request item 14 for the human — a human question where a reading was cheap | the gap review costs one more review turn; none if it finds nothing | review of the whole change |
| Q4 | Judgment of item 8 (WAY-289): do the two new Minor findings and the one old one, all outside the task, reach the user of a product or the person working with the process? | no: the WAY-05 citation (four templates) and the pointer of step 4.1 to »How a skill asks« are the task's own wording; the rule of entries in a skill (`decide_entry.md`) was there before the change | `reports/whole-review-report.md`, `reports/gap-review-report.md` | making each an item for the human to answer | a reader of step 4.1 looks for the value rule in the section the sentence names and finds it only in step 3 | request, lower part |
| Q2 | Foundation entries read by the author (WAY-150) | the task's *Decisions in play* plus WAY-01, 28, 33, 35, 76, 85, 89, 134, 150; four invariants | search of `Scope` of the decision log by the five parts gives 97 decisions; the task's change touches rule wording only | all 97 decisions whole | a missed decision shows in the review of the whole change, which selects on its own | author |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| Frozen task | `task.md` | orchestrator | — |
| Change | commit `2c27260` (7 files), report `reports/author-report.md` | author (haiku) | PASS, `reports/whole-review-report.md` |
| Fix of the Minor findings | commit `faee0f8`, report `reports/fix-report.md` | author, resumed | PASS, `reports/fix-review-report.md` |
| Return step | `reports/return-step-report.md`, no commit | author, resumed | nothing to review |
| Gap review | `reports/gap-review-report.md` | reviewer, resumed | PASS `faee0f8` |
| Gate, stages, measures | `gate_times.md`, `stages.md`, `mechanism_measures.md` | orchestrator | — |
| Request | `request.md`, pull request 110 | orchestrator | — |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| `python -B task-cycle/gate_times.py --output ../task-cycles/close-decision-pending-templates/gate_times.md -- python -B gate/run_tests.py` | orchestrator, base `fca8491`, separate checkout under `.runs/` | 0; 1221 tests in 10 directories, every directory passed (872 s) | none failed on the base |
| `python -B task-cycle/gate_times.py --output docs/task-cycles/close-decision-pending-templates/gate_times.md -- python -B gate/run_tests.py` | orchestrator, `faee0f8` (final tree), the task worktree | 0; 1221 tests in 10 directories, every directory passed (727 s) | none |
| `python -B elements/common/foundation_check.py --skip-test-citations` | author on `2c27260` and `faee0f8`, reviewers on both heads | 0; 0 errors | none |
| `python -B gate/run_tests.py elements/common`, `elements/part-map` | author on `2c27260`; `elements/common` again on `faee0f8` | 0; 144 and 39 tests OK | none |
| `grep -rn "decision pending" elements` | author | exactly the two notes that stay (S26, S28) | none |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator | 0; `merges: 32`, `threshold: 30`, `reminder: yes` | none |
| `python -B task-cycle/cycle_stages.py --output docs/task-cycles/close-decision-pending-templates/stages.md <session>`; `python -B task-cycle/cycle_measures.py --output docs/task-cycles/close-decision-pending-templates/mechanism_measures.md <session>` | orchestrator | both 0 | none |
| `python -B task-cycle/request_check.py docs/task-cycles/close-decision-pending-templates/request.md --task docs/task-cycles/close-decision-pending-templates/task.md`; `python -B task-cycle/private_paths_check.py docs/task-cycles/close-decision-pending-templates/request.md` | orchestrator | 0 and 0 (1 run each before publishing) | none |
| `python -B task-cycle/private_paths_check.py docs/task-cycles/close-decision-pending-templates` | orchestrator, on the copy, before its commit | last run 0 (0 listed of 21 files); 4 runs, the first two listed 19 places before the cleaning replaced them | none |
| `python -B task-cycle/image_files_check.py docs/task-cycles/close-decision-pending-templates` | orchestrator, on the copy | last run 0 (0 listed); 4 runs | none |
| `python -B task-cycle/remarks_check.py docs/task-cycles/close-decision-pending-templates` (original) and `... docs/task-cycles/close-decision-pending-templates` (copy) | orchestrator | original: 4 runs, the first two listed 10 and 3 items, then the items were appended and the last two runs exited 0 with 13 items in the remarks; copy: last run 0, 4 runs | none |

The checks failing on the base: none. The move of the pin: none (the-way itself).

## Return step

- Foundation compared with code: the seven files the change edits, the decisions the task names and the decisions its citations name (unchanged in the log, as the task requires), the invariants of the touched parts (`element-directory-contents`, `skill-rule-source`, `tracked-file-private-paths`, `return-step-record`) and the part map of the five touched parts, each compared with the repository on `faee0f8`; nothing no longer matched (`reports/return-step-report.md`)
- Decisions written or changed: none
- Invariants written or changed: none
- Environment facts: none
- Glossary terms: none
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: none

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/110, opened as a draft, marked ready after the record's commit
- Description: `request.md` beside this record, written by `task-cycle/skill/request_template.md`; form check `python -B task-cycle/request_check.py docs/task-cycles/close-decision-pending-templates/request.md --task docs/task-cycles/close-decision-pending-templates/task.md` last exit 0 (2 runs), check of private paths on it last exit 0 (2 runs); the edit that adds the record's link and the runs of the three checks on the copy is checked again after this commit
- Writes to the task's backlog entry: none yet — the request link and the state are written after the request is ready
- Corrections after the request opened: none
- Process remarks on the-way:
  - author, docs/task-cycles/close-decision-pending-templates/reports/author-report.md: A search for an existing test or script that reads the removed text (`decision pending`, `Draft`, `present tense`, `finding it is a task`, `Moving the product`, `4.1`) — none found.
  - author, docs/task-cycles/close-decision-pending-templates/reports/author-report.md: The `return-step-record` invariant requires the record of this task's return step in one commit of the change. I wrote no such record: the dispatch does not name one, and it is the cycle's return step. Unclear whether the cycle expects it from the author; flagged here.
  - author, docs/task-cycles/close-decision-pending-templates/reports/author-report.md: Whether `elements/common/rules.md` says what a bare `TODO` means for a fact entry (concern C6).
  - fix, docs/task-cycles/close-decision-pending-templates/reports/fix-report.md: None new. The `*Based on*` italic marker is split across a line break in the Source sentence; markdown renders it, but the line break is a formatting choice the reviewer may want to see.
  - review gap, docs/task-cycles/close-decision-pending-templates/reports/gap-review-report.md: A decision or invariant that states "a field stays in a template only while read" for the elements other than decisions: not found (see Minor 1).
  - review gap, docs/task-cycles/close-decision-pending-templates/reports/gap-review-report.md: A place that gives "a value the source does not give" as a kind of question besides step 3 and WAY-54: not found (see Minor 2).
  - review gap, docs/task-cycles/close-decision-pending-templates/reports/gap-review-report.md: A guideline of the-way's own files setting a rule of size: not found; no structure test applies to Markdown.
  - return step, docs/task-cycles/close-decision-pending-templates/reports/return-step-report.md: A glossary entry or invariant that names the removed text: none found (grep of the four foundation files).
  - return step, docs/task-cycles/close-decision-pending-templates/reports/return-step-report.md: Whether the cycle wants the `return-step-record` committed: unclear; the earlier cycle records were committed and removed from the final tree.
  - return step, docs/task-cycles/close-decision-pending-templates/reports/return-step-report.md: The return step found no word with a second meaning introduced by the change; I did not run `record-glossary-term`, since no term needed an entry.
  - review of the whole change, docs/task-cycles/close-decision-pending-templates/reports/whole-review-report.md: A guideline of the-way that sets a rule of size for these files: not found (`grep` of `product-guidelines/` finds only the instructions for writing one).
  - review of the whole change, docs/task-cycles/close-decision-pending-templates/reports/whole-review-report.md: Whether the cycle expects the return step's record from the author's commit: not stated in the handoff; the invariant `return-step-record` does not apply while the-way has no main branch. Unclear, not blocking.
  - review of the whole change, docs/task-cycles/close-decision-pending-templates/reports/whole-review-report.md: Whether WAY-05, scoped to decisions, is meant to bear on the "Fields and their readers" line of the other four templates: the task says so and WAY-54 does the same in a *Rejected* line; no entry says so as a rule. Unclear, not blocking.


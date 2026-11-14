# Cycle record — the grade of a finding about the structure of code in a product that has no rule of size: close the sentence of the review skill and WAY-363

- Task source: the task's note in the author's backlog; frozen copy `task.md` beside this record; document's `updated:` 2026-11-13, `Status: ready for cycle`
- Task relation: independent
- Product repository: https://github.com/mariusznazar/the-way (the-way itself)
- Process pin: this checkout, `1be9057` (the-way itself; no pin)
- Target branch and base: `foundations`, `1be90579bf3daa618dd87c06bd56042eabb642c1`
- Task branch: `task/structure-grade-no-rule-cases`
- Status: request open

## Two questions at start

- Trust boundary: no — the change rewrites a sentence of `task-cycle/review/SKILL.md` and one entry of `foundations/decisions.md`; neither is a file the part map names as a trust boundary (`task-cycle/cycle_stages.py` is the one of task-cycle).
- Irreversible operation: no.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none — the task fixes both the content (a finding of structure is Minor in every product with no rule of size; the three known cases stand as examples, not a closed list) and the places (`task-cycle/review/SKILL.md` section 3, WAY-363's binding sentence and the references to the narrow scope in its Verification, Rationale and Rejected, the wrapping of the entry); `task-cycle/review/whole_change.md` is the model the wording follows. The wording of a sentence is the author's, not a choice among ways open. No row of *Settlements to record* and no projected entry (none).
- Reserved choice: none.
- Execution route and reason: one author without a plan — two files, one idea in three sentences, one agent holds it; orchestrator's judgment from the task at the start.
- Author: `the-way-author`, class `cheaper` (ordinary implementation: text of two files), model haiku (the harness's model closest to a class cheaper than the orchestrator's, sonnet); resumptions and any replacement are listed below.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: Claude Code: background agent, completion notification; yield the turn when only that result remains; no timeout limit met so far.
- Whole-change review: `the-way-stage`, sonnet (class `same`), by `review-change`; range `1be9057..5554f5d` (one commit); first line `PASS 5554f5da9d8be1cf3076ec31bde4e2b14a0d49a8`, report `reports/whole-review-report.md`; changed files `foundations/decisions.md` +12 −10, `task-cycle/review/SKILL.md` +4 −3; every item of *To do* 1–4 and the acceptance criterion met by reading (`whole_change.md` already gives Minor for the pre-rule case through "the product's guidelines hold no such rule", so it stays unedited); no row of *Settlements to record*, no projected entry; blocking 0, Minor 0, out of scope 0; read 14 of 260 selected decisions whole and 246 by title after its second turn (first count 7 and 190, corrected by the reviewer); its invariants, part map, glossary, WAY-328, `settle.md` and `template.md` read whole in the second turn, nothing bears on the PASS
- Review rounds: none — the review passed with no finding of any grade, so no fix and no review of a fix ran
- Weakest-point checks: author — requirement: the three cases get one grade in the review skill, the binding sentence and the whole-change bullet; check: a search of the repository for the old two-case wording and a reading of every hit; showed: only the two edited places name the cases, the bullet covers the third through "hold no such rule"; named weakest point: the bullet does not name the pre-rule case in words (report `reports/author-report.md`). The reviewer judged it met

The last commit of a discarded attempt or of a slice returned too large is a historical name, not
a link to follow: the commit is reachable only until the reflog expires. A choice or ruling of a
discarded attempt keeps its row in the questions table, with *Used by* naming the discarded
attempt.

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

Not used: one author without a plan.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-14 00:50 | start | orchestrator, sonnet | `task-cycle/skill/SKILL.md` | — | fetch; `foundations` fast-forwarded from `f04f046` to `1be9057` (clean tree, on the branch, no local commits); skill unchanged by the fast-forward, no restart needed; task branch and worktree created from `1be9057` |

| 2026-11-14 01:05 | author | `the-way-author` agent type, haiku (class `cheaper`) | `reports/author-handoff.md`; `make-change`, "the whole change as the one author"; frozen task | `reports/author-report.md` | dispatched in the background; next: mechanical check, whole-change review |
| 2026-11-14 01:12 | author return | `the-way-author`, haiku | `reports/author-handoff.md` | `reports/author-report.md`; commit `5554f5d` (`task-cycle/review/SKILL.md` +4 −3, `foundations/decisions.md` +12 −10) | `done`; mechanical check by orchestrator: clean worktree, range `1be9057..5554f5d` non-empty, changed files match *To do* 1–4 (`whole_change.md` deliberately not changed by the author — left to the review), checks with command and exit code (`foundation_check.py` 0; `gate/run_tests.py task-cycle` 0, 394 tests; `gate/run_tests.py foundations` 1 — the directory holds no tests), **Unread material** and **Searches not found or unclear** and own-work check present. Next: review of the whole change |
| 2026-11-14 01:14 | whole-change review | `the-way-stage`, sonnet (class `same`) | `reports/whole-review-handoff.md`; `review-change` (`task-cycle/review/SKILL.md`, `whole_change.md`); range `1be9057..5554f5d` | `reports/whole-review-report.md` | dispatched; next: Minor fixes if any, then gate |
| 2026-11-14 01:25 | whole-change review return | `the-way-stage`, sonnet | `reports/whole-review-handoff.md` | `reports/whole-review-report.md`; first line `PASS 5554f5da9d8be1cf3076ec31bde4e2b14a0d49a8`; `decisions.md` +12 −10, `task-cycle/review/SKILL.md` +4 −3 | no finding of any grade; read 7 decisions whole, 190 by title; its unread invariants/part-map/glossary and `settle.md`/`template.md` settled by autonomous choice Q2; no fix round; next: return step by the resumed author |
| 2026-11-14 01:27 | return step | `the-way-author`, haiku, resumed | `reports/return-handoff.md`; `task-cycle/skill/return_step.md` | `reports/return-report.md` | dispatched by resuming the author |
| 2026-11-14 01:30 | return step return | `the-way-author`, haiku | `reports/return-handoff.md` | `reports/return-report.md`; no commit, head `5554f5d`, worktree clean | `done`, nothing to change; all fields none; **Unread material** and **Searches not found or unclear** present; no commit, so no review of it |
| 2026-11-14 01:33 | gate | orchestrator | `python -B task-cycle/gate_times.py --output docs/task-cycles/structure-grade-no-rule-cases/gate_times.md -- python -B gate/run_tests.py` on `5554f5d` | `gate_output.log` beside this record | started in the background |
| 2026-11-14 01:50 | gate result | orchestrator | gate on `5554f5d` | `gate_output.log`, `gate_times.md` | exit 0; 1267 tests in 10 directories, every directory passed (955 s, one other gate running at the same time) |
| 2026-11-14 01:52 | reconciliation | orchestrator | fetch; `origin/foundations` had advanced to `3c572b9` (PR #114: the slice reading limit, `task-cycle/slice_size.py`, its test, decision WAY-371) | merge commit `6914b90` | clean merge; the merge touches none of the reviewed code: its diff against `5554f5d` has no hunk in `task-cycle/review/` and none in WAY-363, and no hit for the structure terms; `foundation_check.py` 0 errors; no review of the merge (Q3); final tree differs from the one the gate checked, so the gate runs again |
| 2026-11-14 01:53 | gate | orchestrator | the same command on `6914b90` | `gate_output_final.log` | started in the background |
| 2026-11-14 02:25 | whole-change review, second turn | `the-way-stage`, sonnet, resumed | message resuming the reviewer to read its unread material (instead of leaving it as an item of the request) | `reports/whole-review-report.md`, amended; first line unchanged `PASS 5554f5da9d8be1cf3076ec31bde4e2b14a0d49a8` | read invariants, part map, glossary, WAY-328, `settle.md`, `template.md` whole; corrected its selection count to 260 (14 whole, 246 by title); no finding, no change of verdict; the gap of Q2 is closed by the reviewer |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | Which class of model for the one author? Step 4 | `cheaper` (haiku): a text change in two files with the wording already given by `whole_change.md` | task `To do` 1–4 | `same` — dearer, and this change needs no design | a wrong sentence returns as a finding of the whole-change review and costs one fix round | Author |
| Q2 | The whole-change reviewer left unread the invariants, part-map and glossary entries of its selection, WAY-328, and `product-guidelines/coding/settle.md` and `template.md`; does the gap bear on its judgment? | Superseded by the reviewer's second turn (Events, 02:25), which read all of it and found nothing. First answer: no — recorded as an autonomous choice. The orchestrator read `settle.md` lines 86–90 and `template.md` lines 74–80: both name only the departure case ("always Minor"), which stays correct; a search of the glossary, invariants and part map for "rule of size" and "structure of code" finds nothing. The change adds no glossary word, changes no invariant and no part's responsibility. The return step compares the part map and the entries again. | orchestrator's reading of the two files and the grep, `reports/whole-review-report.md` *Unread material* | resume the reviewer to read them — dearer, and it would read the same two lines | an entry the reviewer did not read disagrees with the new wording; the return step's review would find it | whole-change review |
| Q3 | Does the merge of `origin/foundations` (PR #114) change the reviewed code, so that a fresh reviewer must review it? Step 12 | No review: the merge brings WAY-371, `slice_size.py` and its test, none of which the change reads or edits; its diff against the reviewed head `5554f5d` holds no hunk in `task-cycle/review/` and none in WAY-363 (hunks at old lines 3734 and 12447 of the log only), and a search of that diff for "rule of size", "structure of", "WAY-363" and "no coding guidelines" finds nothing. The gate runs again on the final tree. | `git diff 5554f5d HEAD`, the search above | a fresh reviewer on the merge — about two minutes of an agent for a merge that touches neither side's text | WAY-371 binds against the new sentence in a way the grep missed; the human would see it at the merge | request |
| Q4 | Edit `task-cycle/review/whole_change.md` too? Task acceptance criterion: the three cases give one grade in the review skill, the binding sentence and the last bullet of the structure section of that file | No edit. The bullet already says "or the product's guidelines hold no such rule … a finding of structure is Minor", which the pre-rule case falls under; the task's *To do* lists no edit of that file and *Context* names it as the model the wording follows. Author and reviewer both read it so. | `task.md` *Context*; `reports/author-report.md` choices; `reports/whole-review-report.md` | name the pre-rule case in the bullet too — one more place that repeats the list of examples and can drift from the other two | a reviewer reads "hold no such rule" narrowly and grades the pre-rule case Important; the task's own gap returns for that one place | request |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| frozen task | `task.md` beside this record | orchestrator | — |
| code commit | `5554f5d` | the-way-author | `PASS` of the whole-change review |
| merge commit | `6914b90` (merge of `origin/foundations` at `3c572b9`) | orchestrator | no review (Q3); gate on it exit 0 |
| reports | `reports/author-report.md`, `reports/whole-review-report.md`, `reports/return-report.md` | the agents named in the Events | — |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| list of the tests failing before the change | orchestrator, base `1be9057` (merge; tree `ba2ef352185ea2e86f5aa047a149ac1d35072f5e` equals that of its second parent `cd134bf`) | taken from `docs/task-cycles/gate-series-on-test-runner/cycle.md` of commit `97ac793`, *Verification*, its final gate on `1f7dab2` (final tree merged with #112): exit 0, 1267 tests in 10 directories, every directory passed | none failing on the base; no gate run on the base |

| `python -B elements/common/foundation_check.py` | author, reviewer; orchestrator on `6914b90` | 0; 0 errors | none |
| `python -B gate/run_tests.py task-cycle` | author on `5554f5d` | 0; 394 tests | none |
| `python -B gate/run_tests.py foundations` | author | 1; "no test found in foundations": the directory holds no tests | not a check of the change; stands in the process remarks |
| `python -B task-cycle/gate_times.py --output docs/task-cycles/structure-grade-no-rule-cases/gate_times.md -- python -B gate/run_tests.py` | orchestrator, `5554f5d` (the reviewed change) | 0; 1267 tests in 10 directories, every directory passed (955 s, one other gate running at the same time) | none |
| the same command | orchestrator, `6914b90` (final tree, merged with #114) | 0; 1267 tests in 10 directories, every directory passed (763 s, one other gate running at the same time) | none |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator | 0; `tag: foundation-review/2026-11-06`, `merges: 37`, `threshold: 30`, `reminder: yes` | none |
| `python -B task-cycle/cycle_stages.py --output docs/task-cycles/structure-grade-no-rule-cases/stages.md 07a4756c-bb67-40a5-86d3-f282fdd9b6fd`; `python -B task-cycle/cycle_measures.py --output docs/task-cycles/structure-grade-no-rule-cases/mechanism_measures.md 07a4756c-bb67-40a5-86d3-f282fdd9b6fd` | orchestrator | both 0 | none |
| `python -B task-cycle/remarks_check.py .runs/task-cycles/structure-grade-no-rule-cases` | orchestrator, on the original | last run exit 0, 5 runs (exit 1 listing 4 items, then 0 after they were appended; exit 1 for the one item the reviewer's second turn added, then 0; 0 after the entry of an item the report no longer holds was removed) | none |
| `python -B task-cycle/remarks_check.py docs/task-cycles/structure-grade-no-rule-cases` | orchestrator, on the copy | last run exit 0, 3 runs, nothing listed | none |
| `python -B task-cycle/private_paths_check.py docs/task-cycles/structure-grade-no-rule-cases` | orchestrator, on the copy | last run exit 0, 3 runs; the first listed 8 places (the task's note path and link, the worktree path in the three handoffs), cleaned by one rewriting | none |
| `python -B task-cycle/image_files_check.py docs/task-cycles/structure-grade-no-rule-cases` | orchestrator, on the copy | last run exit 0, 3 runs, no image file | none |
| `python -B task-cycle/request_check.py docs/task-cycles/structure-grade-no-rule-cases/request.md --task docs/task-cycles/structure-grade-no-rule-cases/task.md`; `python -B task-cycle/private_paths_check.py docs/task-cycles/structure-grade-no-rule-cases/request.md` | orchestrator, on the description | both exit 0, 1 run each; run again on each later edit of the description | none |

The checks failing on the base: none. The move of the pin: none (the-way itself). The part of each changed file, by the part map: `task-cycle/review/SKILL.md` — `task-cycle`; `foundations/decisions.md` — `decisions`; no check failed in a cycle run, so no file of another part is listed.

## Return step

- Foundation compared with code: WAY-363 (changed), WAY-362 and WAY-360 (named by the task), each compared with `task-cycle/review/SKILL.md` section 3, `task-cycle/review/whole_change.md`, `product-guidelines/coding/settle.md` and `template.md`: all agree; the part map's `task-cycle` entry still describes the part; nothing no longer matched (`reports/return-report.md`)
- Decisions written or changed: WAY-363 (edited in place by the change itself, WAY-07)
- Invariants written or changed: none
- Environment facts: none
- Glossary terms: none
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: none (the task carries none)
- Result: the return step committed nothing, so no review of it ran

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/115, ready for review (opened as a draft, marked ready after the record's commit)
- Description: `request.md` beside this record, by `task-cycle/skill/request_template.md`; form check (`python -B task-cycle/request_check.py docs/task-cycles/structure-grade-no-rule-cases/request.md --task docs/task-cycles/structure-grade-no-rule-cases/task.md`) exit 0, 1 run; private paths check on it exit 0, 1 run; the checks on the copy of the record are written after its commit
- Writes to the task's backlog entry: the request link added to the task's line as its `url` field; the status left as the human gave it
- Corrections after the request opened: none
- Process remarks on the-way:
  - author return, docs/task-cycles/structure-grade-no-rule-cases/reports/author-report.md: `gate/run_tests.py foundations` reports "no test found in foundations" (exit 1). The foundations directory has no tests; the handoff asked for the tests of the directories changed, and I took this as no test to run. The orchestrator should judge whether that is the intended reading.
  - author return, docs/task-cycles/structure-grade-no-rule-cases/reports/author-report.md: Nothing else looked for was unclear.
  - whole-change review (second turn), docs/task-cycles/structure-grade-no-rule-cases/reports/whole-review-report.md: My first search for the selection parsed multi-line *Scope* fields wrongly and gave 196 instead of 216 (found and corrected above); I found nothing unclear beyond that.
  - return step return, docs/task-cycles/structure-grade-no-rule-cases/reports/return-report.md: Grep of glossary and invariants for "size" and "structure" returned no hit, so no term or invariant could be checked against the change. Nothing else unclear.

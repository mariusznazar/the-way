# Cycle record — Skrypty the way sprawdzają dane wejściowe i padają z nazwą brakującego pola, zamiast po cichu przepuszczać

- Task source: the task's note in the author's backlog, `Status: ready for cycle`, frozen as `task_frozen.md` beside this record on 2026-11-11 (the document carries `updated: 2026-11-11`, no commit)
- Task relation: independent
- Product repository: https://github.com/mariusznazar/the-way (the-way itself; no pin)
- Process pin: none (the-way is the product)
- Target branch and base: `foundations`, `e9a0f926dc9758f6554e8c0a30925d3e4d68cfed`
- Task branch: `task/scripts-fail-on-missing-fields`, worktree `.runs/worktrees/scripts-fail-on-missing-fields`
- Status: request open

## Two questions at start

- Trust boundary: no — the change writes one decision into `foundations/decisions.md`, a file of the part `decisions`, whose part-map *Trust boundary* is `none`; no script, network input, key or deployment file is touched.
- Irreversible operation: no — a decision is text under git; nothing is performed outside the repository.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none — the task's four *Settlements to record* rows settle the decision's form (separate decision beside WAY-328, not an exception to it and not an invariant), its reach (new scripts; in a changed script the whole reading of a file whose way of reading the change reworks), its check (review plus one test per file read) and its exit codes (2; 1 in a form-checking script). The remaining wording (identifier, title, *Relations*, *Verification*, *Rationale*, *Rejected*) is how to make what the task settles, not a choice left open. Ways weighed: spec first — rejected, nothing to design; one author — chosen.
- Reserved choice: none — no language, framework, library, store, login or place to run is in play.
- Execution route and reason: one author without a plan — one file (`foundations/decisions.md`), one entry, plus the foundation search and return step.
- Author: one author with `make-change`, class `same` as the orchestrator's, model `sonnet` (closest available; the orchestrator is Sonnet 5.5). Reason for a class other than `cheaper`: the entry binds all later script work in every part and needs the whole-foundation search of WAY-33 with the rejected ways of WAY-328 and WAY-38 carried correctly; a wrong *Scope* or *Relations* would pass foundation_check silently.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: Claude Code `Agent` call in the foreground, which blocks until the agent returns; background results arrive by completion notification and the turn is yielded.
- Whole-change review: fresh reviewer (sonnet, class same) by `review-change`; range `e9a0f92..4905a56`; report `reports/review_whole_report.md`, first line `PASS 4905a56544ff8d9600af406d52afdfcd588e3493`; changed files `foundations/decisions.md` +79 −0; coverage of every *To do* item and settlement rows 1–4 met, source fidelity met (*Rejected* holds exactly the eight *Not chosen* ways); 40 decisions read whole, 248 by title only; no plan.
- Review rounds: no review blocked. Whole-change review PASS with 4 Minor within the task; one fix (`5922ffc`, Minor 2 and 4 changed, 1 and 3 left as the reviewer suggested) and its review `reports/review_fix_report.md` PASS `5922ffce36e42ef1e6f98f9f04cc49b32e8aff14` (one new Minor: a clause tail dropped). Return step committed nothing, so no review. Reconciliation with the target branch: merge `c32cfe1`, reviewed PASS `reports/review_merge_report.md`, one Minor outside the task.
- Weakest-point checks: author — requirement "*Scope* names all parts of the map"; check: a one-off run comparing the entry's *Scope* with the part headings of `foundations/part_map.md` as sets; showed 16 and 16, equal (`reports/author_report.md`). Orchestrator repeated it after the merge: 17 and 17, equal.

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

One author, no plan: no rows.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 21:27 | start | orchestrator (Sonnet 5.5) | task document read; checkout `foundations` clean at `e9a0f92`, equal to `origin/foundations` after fetch | worktree `.runs/worktrees/scripts-fail-on-missing-fields`, branch `task/scripts-fail-on-missing-fields` | frozen task copied; base checks started in `.runs/base-check` |
| ~21:29 | author | one author (sonnet, class same) | `reports/author_handoff.md`, `the-way-make-change` variant "the whole change as the one author", frozen task | `reports/author_report.md` (expected) | dispatched in the background; resumes on completion notification |
| ~21:33 | author result | one author | `reports/author_report.md` | `done with concerns`; commit `4905a56`, `foundations/decisions.md` +79; own check `python -B elements/common/foundation_check.py` exit 0 | mechanical check: clean worktree, non-empty range, one file, report has Unread material and Searches sections and own-work check. Unread material (WAY-03, `request_check.py` after line 120, rest of decisions/invariants) carried to the whole-change reviewer (autonomous choice Q2). Concerns 1–3 go to the request |
| ~21:34 | whole-change review | reviewer (sonnet, class same) | `reports/review_whole_handoff.md`, `the-way-review-change` variant "the whole change", range `e9a0f92..4905a56` | `reports/review_whole_report.md` (expected) | dispatched in the background |
| ~21:36 | whole-change review result | reviewer | `reports/review_whole_report.md` | `PASS 4905a56544ff8d9600af406d52afdfcd588e3493`; 0 blocking, 4 Minor within the task, 2 Minor outside; `foundation_check` exit 0; 40 decisions read whole, 248 by title | Minor 1–4 within the task go to one fix (`reports/fix_findings.md`, cut from the report word for word) |
| ~21:37 | fix of Minor findings | author resumed (class same) | `reports/fix_findings.md`, variant "the fix of a review's findings" | `reports/fix_report.md`; commit `5922ffc` (+5 −6 in WAY-330); `foundation_check` exit 0 | Minor 2 and 4 changed; Minor 1 and 3 left (the reviewer's suggestion: carried by the request); author also dropped a clause beyond the suggestion |
| ~21:37 | review of the fix | same reviewer resumed | range `4905a56..5922ffc`, `fix.md` | `reports/review_fix_report.md` | `PASS 5922ffce36e42ef1e6f98f9f04cc49b32e8aff14`; one new Minor within the task (the tail of the Rejected clause dropped); no Critical or Important; goes to the request's list |
| ~21:38 | return step | author resumed (class same) | `reports/return_handoff.md`, `foundation_step.md`, `return_step.md` | `reports/return_report.md` (expected) | dispatched in the background |
| ~21:50 | return step result | author resumed | `reports/return_report.md` | `done`; no commit (nothing to correct); `foundation_check` exit 0; rows 1–4 of Settlements all written in the decision | no review of the return step (no commit) |
| ~21:50 | gate on the reviewed tree | orchestrator | `python -B gate/run_tests.py` at `5922ffc` | `gate_final.txt`: exit 0, 919 tests in 9 directories | superseded by the merge below |
| ~21:51 | stages table | orchestrator | `python -B task-cycle/cycle_stages.py <session id> --output stages.md` | `stages.md` | written before the merge; to be rerun |
| ~21:52 | reconciliation | orchestrator | `git fetch`: `origin/foundations` moved `e9a0f92` → `3bcad13` (the weekly process audit: decisions WAY-330…343, part `process-audit`) | merge commit `c32cfe1`; conflict in `foundations/decisions.md` (both sides appended after WAY-329) | resolved by keeping the target's entries and renumbering ours to WAY-344; Scope gained `process-audit` (17 parts); `foundation_check` exit 0; Scope equals the part map as sets |
| ~21:53 | gate on the merged tree | orchestrator | `python -B gate/run_tests.py` at `c32cfe1` | `gate_merged.txt` (running) | result under Verification |
| ~21:54 | review of the merge | fresh reviewer (sonnet, class same) | `reports/review_merge_handoff.md`, `the-way-review-change`, reconciliation with the target branch | `reports/review_merge_report.md` (expected) | dispatched in the background |
| 21:27 | base checks | orchestrator | `python -B gate/run_tests.py` in a detached checkout of `e9a0f92` under the worktree's ignored `.runs/base-check` | `docs/task-cycles/scripts-fail-on-missing-fields/base_gate.txt` | running in the background; result recorded under Verification |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q2 | Author's Unread material (WAY-03, `request_check.py` after line 120, rest of decisions and invariants) — report | carried to the reviewer of the whole change, who selects its own foundation; no resume of the author | author's report; the form passes `foundation_check` | resume the author to read WAY-03 — the reviewer reads the form anyway, one agent call saved | a form flaw WAY-03 would show is caught by the review, or reaches the request as a finding | whole-change review |
| Q4 | Conflict in `foundations/decisions.md` at the merge: both sides appended after WAY-329, and the target took WAY-330…343 for the audit | kept the target's block unchanged and renumbered ours to WAY-344, after WAY-343 | `git log HEAD..origin/foundations`; reviewer of the merge compared `3bcad13..HEAD` (one file, +78, no deletions) | renumbering the target's entries — they are already on the target branch and merged requests cite them | a wrong order of numbers breaks nothing; a lost entry would be caught by `foundation_check` and the merge review | reconciliation |
| Q3 | The task counts 16 parts; the target's part map now has 17 (`process-audit`) — merge | the entry's *Scope* names all 17 | the task's own rule that *Scope* names every part and a new part is added to it; *Scope* equals the part map as sets | leaving 16 — it would break that rule on the day of the merge | a later change that finds a part missing must add it in the same change; low | request item 2 |
| Q1 | Class of the one author — step 4 | `same` as the orchestrator's | the entry binds every part's later scripts; WAY-33 search of the whole foundation | `cheaper` (default) — the risk is a quietly wrong *Scope* or *Relations* that foundation_check accepts | one extra fix round if the cheaper author had erred; the cost of `same` is tokens | Author |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| Frozen task | `docs/task-cycles/scripts-fail-on-missing-fields/task_frozen.md` | orchestrator | n/a |
| Code commit | `4905a56` (WAY-330 as first numbered; `foundations/decisions.md` +79) | one author | whole-change review PASS |
| Fix commit | `5922ffc` (+5 −6 inside the entry) | one author | fix review PASS |
| Merge commit | `c32cfe1` (conflict resolved; entry renumbered to WAY-344, *Scope* + `process-audit`) | orchestrator | merge review PASS |
| Reports | `reports/author_report.md`, `fix_report.md`, `return_report.md`, `review_whole_report.md`, `review_fix_report.md`, `review_merge_report.md`, handoffs beside them | agents | see above |
| Stages | `stages.md` | orchestrator | n/a |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| `python -B gate/run_tests.py` (base) | orchestrator, `e9a0f92`, separate checkout under the worktree's `.runs/base-check` | exit 0; 919 tests in 9 directories, every directory passed (`base_gate.txt`) | none failing on the base |
| `python -B gate/run_tests.py` | orchestrator, `5922ffc` | exit 0; 919 tests in 9 directories (`gate_final.txt`) | superseded by the merged tree |
| `python -B gate/run_tests.py` | orchestrator, `c32cfe1` (final tree) | exit 0; 1066 tests in 10 directories, every directory passed (`gate_merged.txt`) | none failed or did not run |
| `python -B elements/common/foundation_check.py` | author (after entry, after fix), return-step author, reviewers, orchestrator after the merge | exit 0, `0 errors`, each run | none |
| Scope vs part map as sets (one-off script) | author at `4905a56`; orchestrator and merge reviewer at `c32cfe1` | exit 0; 16=16, then 17=17, equal | none |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator | exit 0; `merges: 24`, `threshold: 30`, `reminder: no` | none |
| `python -B task-cycle/remarks_check.py .runs/task-cycles/scripts-fail-on-missing-fields` | orchestrator, original | 2 runs: exit 1 (5 items listed, then appended to the remarks), exit 0 | none |
| `python -B task-cycle/private_paths_check.py docs/task-cycles/scripts-fail-on-missing-fields` | orchestrator, on the copy of the record | 4 runs: exit 1 (13 listed), exit 1 (13 listed, again after a failed rewriting script), exit 0, exit 0 (0 listed) | none |
| `python -B task-cycle/image_files_check.py docs/task-cycles/scripts-fail-on-missing-fields` | orchestrator, on the copy | 3 runs, all exit 0 (0 listed) | none |
| `python -B task-cycle/remarks_check.py docs/task-cycles/scripts-fail-on-missing-fields` | orchestrator, on the cleaned copy | 3 runs, all exit 0 (0 not in the remarks) | none |
| `python -B task-cycle/request_check.py … --task …/task_frozen.md` | orchestrator | 1 run so far: exit 0 | none |
| `python -B task-cycle/private_paths_check.py` on `request.md` | orchestrator | 1 run so far: exit 0, 0 listed | none |

## Return step

- Foundation compared with code: none — nothing no longer matched (`reports/return_report.md`); after the merge, the part map's 17 parts and the entry's *Scope* compared as sets: equal
- Decisions written or changed: WAY-344 (written by the change; first numbered WAY-330)
- Invariants written or changed: none
- Environment facts: none
- Glossary terms: none
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: rows 1, 2, 3, 4 → WAY-344

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/103 — draft at first; marked ready after the record's copy is committed and the description is edited
- Description: `request.md` beside this record; written by `task-cycle/skill/request_template.md`; form check 1 run, last exit 0; private-paths check 1 run, last exit 0; written and checked after this commit for the record link and the checks on the copy
- Writes to the task's backlog entry: none yet (the backlog entry of this task is not found by an agent without the author's locations file entry; see the request link)
- Process remarks on the-way:
  - author, docs/task-cycles/scripts-fail-on-missing-fields/reports/author_report.md: none found for anything the handoff asked to find; two points were unclear:
  - author, docs/task-cycles/scripts-fail-on-missing-fields/reports/author_report.md: The handoff says the foundation step is read "whole" in `task-cycle/skill/foundation_step.md`; the file is 33 lines and was read whole. It says "a question for the human arises only where..."; I found no such case. Unclear: whether the Verification examples count as an entry content "no row carries" (see Choices) — I treated them as the writer's wording under row 1–4 and flag them here.
  - whole-change review, docs/task-cycles/scripts-fail-on-missing-fields/reports/review_whole_report.md: none found for anything I looked for.
  - whole-change review, docs/task-cycles/scripts-fail-on-missing-fields/reports/review_whole_report.md: Unclear: whether a pair of examples that the writer proposes and no human has accepted may stand in an entry that the cycle writes from rows (the skill's step 3 says "where the human gives one or accepts one you propose"; WAY-114 puts the acceptance at the merge); I treated the merge as the acceptance and graded it Minor 3.
  - whole-change review, docs/task-cycles/scripts-fail-on-missing-fields/reports/review_whole_report.md: Unclear: what "reworks the way of reading" covers in the binding sentence when a change adds the reading of a further file to an existing script (Minor 2).

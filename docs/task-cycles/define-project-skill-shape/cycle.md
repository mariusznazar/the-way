# Cycle record — define-project in the shape of WAY-256

- Task source: the task's note in the author's backlog, `Status: ready for cycle`, document updated 2026-11-06 (frozen copy: [`task.md`](task.md) beside this record)
- Task relation: independent
- Product repository: the-way itself (`mariusznazar/the-way`)
- Process pin: none — the session works on the-way itself; no pin to move
- Target branch and base: `foundations`, `2754675` (`2754675c` merge of PR #84; equal to `origin/foundations` after fetch and fast-forward on 2026-11-08; the files this task changes or counts are identical to `dfd50e5`, the task's base: `git diff --stat dfd50e5 2754675 -- project-level/skill project-level/definition_template.md project-level/lead elements/common/way_of_working.md` is empty)
- Task branch: `task/define-project-skill-shape`
- Status: request open

## Two questions at start

- Trust boundary: no — the change touches only Markdown files in `project-level/skill/`; the part map's `project-level` entry names as its trust boundary only `project-level/readiness_check.py`, `plan_check.py` and `plan_state.py`, which the task leaves unchanged.
- Irreversible operation: no — nothing to prepare for a human to perform.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none — questions 1–4 of the task settle the limits of the change (only `project-level/skill/`), that no new sentence grants the delegated turn reading of its own steps only, that the critic and the orchestrator get nothing in place of step 7's text, and the routes on which words are counted; To do 1–2 settle the shape (picture of the whole, shared rules and pointers in `SKILL.md`, a file per step or variant, step numbers 0–7 and 7.1–7.5 kept, the heading "Delegated definition change and gate" kept with its pointer). The names of the files and the wording of pointers are a way of making what the task settles. No row of *Settlements to record* and no projected entry is carried (`Candidates: 6 shown, 0 accepted`).
- Reserved choice: none — no language, framework, library, store, login or place to run.
- Execution route and reason: one author without a plan; one skill file split into files beside it, plus an assessment and word counts, all resting on one judgment of rule preservation, so one agent holds the change.
- Author: one author with `make-change`, class `same` as the orchestrator (Opus 5.5, harness model `opus`). Reason for a class other than `cheaper`: the change rewrites instruction text where a lost or reworded rule produces no failing test, and the assessment needs the judgment "when is a fragment needed and does the agent recognise that moment" (WAY-257); a weaker class is likelier to merge or drop a rule silently.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: native completion notification (Claude Code background `Agent` call).
- Whole-change review: reviewer other than the author, Opus 5.5 (`same`, not cheaper than the orchestrator), by `review-change`; range `2754675..c0a0f52`; first line `FAIL c0a0f5271cf251055b1ec50f32087220da328698`, report [`reports/review_report.md`](reports/review_report.md); 10 files in `project-level/skill/`, +188 −129; 1 blocking (Important I-1), 3 Minor within the task, 0 out of scope. Coverage: To do 1–6 and every acceptance criterion walked by the reviewer (routes 1, 3a, 4, 5 by hand, all 54 assessment rows against the files, every nonblank base line once, the delegated mode reaching step 7, the fragments of criterion 5, nothing outside `project-level/skill/`, own recount of all words); no row of *Settlements to record* and no projected entry to cover.
- Review rounds: whole-change review `FAIL c0a0f52`: I-1 (a readiness-check finding handed back from step 6 by `project-level/technology/close.md` no longer reached 7.1's routing). One fix `eeca32c` (range `c0a0f52..eeca32c`, report [`reports/fix_report.md`](reports/fix_report.md)) for I-1 with the Minor M-1 to M-3 within the task; the review of the fix (same reviewer, [`reports/review_fix_report.md`](reports/review_fix_report.md)) `PASS eeca32c97a492aca5954e82914daf28d7ee59758`, all four fixed, no new finding. No fix was reverted. The return step committed `09b0dd0`; its review (fresh reviewer, [`reports/return_review_report.md`](reports/return_review_report.md)) `PASS 09b0dd0c7dafe1840c788f280f90e90fdd7944fa`, 1 Minor (record only), not fixed.
- Weakest-point checks: author — requirement named: every fragment stands after the rebuild where the step or variant that needs it names it, with the assessment's *New place* true; check: `make_assessment.py` (every nonblank base line in exactly one row, each row's units in the file it names), `compare_sentences.py` (every unit of the base against all ten files), `check_pointers.py` (each file named at its step, the jumps of criterion 5), each shown able to fail; showed 0 unexpected misses and 7 named rewordings ([`reports/author_report.md`](reports/author_report.md)). The author named a second weak point: whether a dispatched agent keeps the delegated mode through steps 0 to 6 is argued, not measured. The check missed the hand-back of `close.md` to 7.1 (I-1), which the review found; the fix extended `check_pointers.py` to `readiness_gate.md` under steps 6 and 7 ([`reports/fix_report.md`](reports/fix_report.md)).

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

None — one author without a plan.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-08 | start | orchestrator, Opus 5.5 | `/the-way-implement-task` with the task document | — | task read in full; `Status: ready for cycle`, `Human actions: none`, `Project relation: independent`, `Questions carried to cycle: none`, no settlements |
| 2026-11-08 | fast-forward | orchestrator | `git fetch`; checkout on `foundations`, clean, 5 commits behind `origin/foundations`; `git merge --ff-only` to `2754675`; entry point and `task-cycle/skill/SKILL.md` unchanged by it, so the cycle went on from the entry point's checks | checkout at `2754675` | — |
| 2026-11-08 | branch | orchestrator | `git worktree add -b task/define-project-skill-shape .runs/worktrees/define-project-skill-shape 2754675` | worktree `.runs/worktrees/define-project-skill-shape` | base `2754675` |
| 2026-11-08 | base checks | orchestrator | `python -B gate/run_tests.py` in a separate detached checkout of `2754675` at `.runs/base-check` (ignored `.runs/` of the worktree), output [`base_gate.txt`](base_gate.txt) | running in background | result under *Verification* when finished |
| 2026-11-08 | author dispatch | one author, Opus 5.5 (`same`), background `Agent` | handoff [`reports/author_handoff.md`](reports/author_handoff.md); method `task-cycle/change/SKILL.md` ("the whole change as the one author") with `instruction-files/SKILL.md`; frozen [`task.md`](task.md) | report path [`reports/author_report.md`](reports/author_report.md) | dispatched from base `2754675`; waiting for completion notification |
| 2026-11-08 | author return | one author, Opus 5.5 | [`reports/author_handoff.md`](reports/author_handoff.md) | [`reports/author_report.md`](reports/author_report.md); commit `c0a0f52`; `project-level/skill/` 10 files (1 changed, 9 new), +188 −129 | `done with concerns` — concerns (author's "Choices" 3, 4; counts): step 0's pointer names a dispatched turn; only `gate.md` points back to the delegated mode; route 1's figure outside the task's estimate; 1937 vs 1929 is the locale of `wc -w` (UTF-8 vs C). Mechanical check: clean tree, range `2754675..c0a0f52` non-empty, every changed file in `project-level/skill/`, each check with command and exit code, own-work check present, **Searches not found or unclear** 6 items (copied to process remarks). Next: review of the whole change |
| 2026-11-08 | whole-change review dispatch | reviewer, Opus 5.5 (`same`, not cheaper than the orchestrator), background `Agent` | [`reports/review_handoff.md`](reports/review_handoff.md); method `task-cycle/review/SKILL.md` + `whole_change.md`; range `2754675..c0a0f52` | [`reports/review_report.md`](reports/review_report.md) | dispatched; waiting |
| 2026-11-08 | whole-change review return | reviewer, Opus 5.5 | [`reports/review_handoff.md`](reports/review_handoff.md) | [`reports/review_report.md`](reports/review_report.md); first line `FAIL c0a0f5271cf251055b1ec50f32087220da328698` | FAIL: 1 blocking (Important I-1: a readiness-check finding handed back from step 6 by `project-level/technology/close.md` no longer reaches 7.1's routing, which stands only in `gate.md`), 3 Minor within the task, 0 out of scope. Checks with command and exit code present; **Searches not found or unclear** present. Next: one fix by the author |
| 2026-11-08 | fix dispatch | author resumed, Opus 5.5 (`same`) via `SendMessage` | [`reports/findings.md`](reports/findings.md) (I-1 and M-1 to M-3 in the reviewer's words); variant "the fix of a review's findings" | [`reports/fix_report.md`](reports/fix_report.md) | dispatched from reviewed head `c0a0f52`; waiting |
| 2026-11-08 | fix return | author, Opus 5.5 (resumed) | [`reports/findings.md`](reports/findings.md) | [`reports/fix_report.md`](reports/fix_report.md); commit `eeca32c` (`SKILL.md` +9 −6, `delegated_mode.md` +3, `existing_definition.md` +4 −4) | `done`, I-1 and M-1 to M-3 fixed, none contested; checks with command and exit code present; own-work check present; **Searches not found or unclear** 1 item (copied to process remarks); clean tree. Next: review of the fix range `c0a0f52..eeca32c` by the same reviewer |
| 2026-11-08 | review of the fix dispatch | reviewer resumed, Opus 5.5, via `SendMessage` | method `task-cycle/review/fix.md`; range `c0a0f52..eeca32c`; [`reports/findings.md`](reports/findings.md), [`reports/fix_report.md`](reports/fix_report.md) | [`reports/review_fix_report.md`](reports/review_fix_report.md) | dispatched; waiting |
| 2026-11-08 | review of the fix return | reviewer, Opus 5.5 (resumed) | [`reports/findings.md`](reports/findings.md), [`reports/fix_report.md`](reports/fix_report.md) | [`reports/review_fix_report.md`](reports/review_fix_report.md); first line `PASS eeca32c97a492aca5954e82914daf28d7ee59758` | PASS, 0 blocking; I-1 and M-1 to M-3 fixed; no new finding; the fix report's search item judged a note outside the fix, not a finding (the base routed no other finding of step 0's check either); **Searches not found or unclear** 2 items (copied to process remarks). Next: return step; gate on `eeca32c` running |
| 2026-11-08 | step 10 gate | orchestrator | `python -B gate/run_tests.py` in a detached checkout of `eeca32c` at `.runs/gate-check` | [`gate_eeca32c.txt`](gate_eeca32c.txt) | started in the background |
| 2026-11-08 | return step dispatch | author resumed, Opus 5.5 (`same`) via `SendMessage` | `task-cycle/skill/foundation_step.md` and `task-cycle/skill/return_step.md`; reviewed head `eeca32c` | [`reports/return_report.md`](reports/return_report.md) | dispatched; waiting |
| 2026-11-08 | step 10 gate return | orchestrator | `python -B gate/run_tests.py` in a detached checkout of `eeca32c` | [`gate_eeca32c.txt`](gate_eeca32c.txt) | exit 0, 804 tests in 9 directories; checkout removed. The return step then committed, so the gate runs again on the final tree |
| 2026-11-08 | return step return | author (resumed), Opus 5.5 | `task-cycle/skill/foundation_step.md`, `return_step.md` | [`reports/return_report.md`](reports/return_report.md); commit `09b0dd0` (`gate.md` renamed `readiness_gate.md`, its three pointers in `SKILL.md` and `existing_definition.md`) | `done with concerns`: the file name used "gate", which the glossary gives as the test command; renamed. Concern: text moved word for word still says "the gate" for the readiness gate, as WAY-118 and the definition template do; left to proposal 4. No foundation entry written or corrected. Checks with command and exit code; own-work check; **Searches not found or unclear** 1 item (copied to process remarks); clean tree. The return step committed, so its range gets a review |
| 2026-11-08 | return step review dispatch | fresh reviewer, Opus 5.5 (`same`), background `Agent` | [`reports/return_review_handoff.md`](reports/return_review_handoff.md); method `task-cycle/review/SKILL.md`; range `eeca32c..09b0dd0` | [`reports/return_review_report.md`](reports/return_review_report.md) | dispatched; waiting |
| 2026-11-08 | return step review return | reviewer, Opus 5.5 | [`reports/return_review_handoff.md`](reports/return_review_handoff.md) | [`reports/return_review_report.md`](reports/return_review_report.md); first line `PASS 09b0dd0c7dafe1840c788f280f90e90fdd7944fa` | PASS, 0 blocking, 1 Minor within the task (earlier reports of the record still name `gate.md`; record only), not fixed, to the request's list; 0 out of scope; **Searches not found or unclear** 1 item (copied to process remarks) |
| 2026-11-08 | step 10 gate | orchestrator | `python -B gate/run_tests.py` in a detached checkout of `09b0dd0` at `.runs/gate-check` | [`gate_09b0dd0.txt`](gate_09b0dd0.txt) | started in the background |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | Which class of model for the one author (step 4)? Source: skill step 4, WAY-229 | `same` as the orchestrator | the change is a rule-preserving rewrite of instruction text; see *Author* | `cheaper` (default for ordinary implementation) | a rule lost or reworded without a failing test; caught only by the whole-change review | Author |
| Q2 | The checkout stood 5 commits behind `origin/foundations`, on `foundations`, clean, no local commits | fast-forward, then start again from the entry point | `git status -sb` `[behind 5]`; `git merge --ff-only` | — | none | start |
| Q3 | `wc -w project-level/skill/SKILL.md` on the base gives 1929; the task states 1937 words (Need, first point) | the author counts by `wc -w` as question 4 gives and the request states the counted figure, naming the task's figure beside it | `wc -w` run by the orchestrator at the start | taking 1937 as stated | a reader comparing the request with the task sees an 8-word difference; no comparison shifts, since both sides are counted by one script | author handoff, request |
| Q4 | The author's figure for the base: 1937 under a UTF-8 locale, 1929 in the C locale (8 standalone em dashes). Source: author's report, "Counts" | the request states the UTF-8 figures, as the task and the series' earlier counts did, and names the C-locale figure once | [`reports/author_report.md`](reports/author_report.md); `verify_counts.py` runs `wc -w` under both locales | the C-locale figures | none for comparisons, both sides use one locale | Q3, request |
| Q5 | The author's choices of how to make what the task settles: four shared rules in a section "Rules that hold across the steps" of `SKILL.md`; one variant file of step 0 for both resume cases; the condition of step 0's pointer naming a dispatched turn; only the file of step 7 pointing back to the delegated mode; step 6 in a file of its own; the file names; counting under a UTF-8 locale | see [`reports/author_report.md`](reports/author_report.md), "Choices" | [`reports/author_report.md`](reports/author_report.md) | the alternatives it names there | words read on every route, or a dispatched agent at steps 4–6 asking the human directly, though the delegated mode read first forbids it | request (*For you to decide* 2) |
| Q6 | Do the Minor findings of the whole-change review go into the one fix with its blocking finding? Source: skill, "The end of a code review" and the handoff paragraph on a fix | yes — all three within the task and unmarked as out of scope, after the blocking finding in the findings file | [`reports/findings.md`](reports/findings.md) | a second fix for them alone | none: the review of the fix passed with no new finding | fix |
| Q7 | The return step renamed `gate.md` to `readiness_gate.md` against the glossary's "gate"; does a renamed file need a new review? Source: skill step 11 | yes — the return step committed, so a fresh reviewer reviewed `eeca32c..09b0dd0`; the gate ran again on `09b0dd0` | [`reports/return_report.md`](reports/return_report.md), [`reports/return_review_report.md`](reports/return_review_report.md) | — | none | request |
| Q8 | `task-cycle/remarks_check.py` listed the line `verify_counts result: …` of the return step's report as a search item | held wrong (WAY-295): the line is a check result appended after the section's one item; not appended as an item; the case named in the process remarks as the orchestrator's entry and as item 3 of *For you to decide* | [`reports/return_report.md`](reports/return_report.md), last line | appending it as an item | the request carries one item more for the human; no item of a report is lost | request |
| Q9 | The Minor finding of the review of the return step (earlier reports name `gate.md`) — fixed? Source: skill, "The end of a code review" | not fixed: a Minor finding of the return step's review goes to the request's list; the description carries no passage naming the old file as current | [`reports/return_review_report.md`](reports/return_review_report.md) | editing the agents' reports | a reader of the record meets the old name in reports written before the rename | request |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| Frozen task | `.runs/task-cycles/define-project-skill-shape/task.md` | orchestrator | — |
| Code | `c0a0f52` (the rebuild), `eeca32c` (the fix), `09b0dd0` (the return step) on `task/define-project-skill-shape`; range `2754675..09b0dd0`, 10 files in `project-level/skill/` | one author | whole-change review `FAIL c0a0f52`; review of the fix `PASS eeca32c`; review of the return step `PASS 09b0dd0` |
| Assessment of the skill | [`reports/assessment.md`](reports/assessment.md) (54 rows: 15 keep, 39 move; 6 proposals), [`reports/proposals.md`](reports/proposals.md), [`reports/make_assessment.py`](reports/make_assessment.py), not committed in the tree | one author | checked row by row by the reviewer |
| Word counts | [`reports/word-counts.md`](reports/word-counts.md), [`reports/make_word_counts.py`](reports/make_word_counts.py), [`reports/verify_counts.py`](reports/verify_counts.py) | one author | recomputed by the reviewers |
| Rule-preservation checks | [`reports/compare_sentences.py`](reports/compare_sentences.py) with [`reports/compare_sentences.txt`](reports/compare_sentences.txt), [`reports/check_pointers.py`](reports/check_pointers.py) | one author | rerun by the reviewers |
| Reports | `author_report.md`, `fix_report.md`, `return_report.md`, `review_report.md`, `review_fix_report.md`, `return_review_report.md`; handoffs `author_handoff.md`, `review_handoff.md`, `return_review_handoff.md`; `findings.md` | agents | — |
| Stages | [`stages.md`](stages.md) | orchestrator | — |
| Base and final gate output | [`base_gate.txt`](base_gate.txt), [`gate_eeca32c.txt`](gate_eeca32c.txt), [`gate_09b0dd0.txt`](gate_09b0dd0.txt) | orchestrator | — |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| Base: `python -B gate/run_tests.py` | orchestrator, detached checkout of `2754675` at `.runs/base-check` (removed after the run), Windows | exit 0 — 804 tests in 9 directories, every directory passed (output [`base_gate.txt`](base_gate.txt)) | no check failing on the base. Five tests skipped on Windows, so unchecked, all in `instruction-files/test_check_instructions.py`: `test_a_fifo_named_like_an_instruction_file_does_not_stop_the_run` (no FIFO), `test_a_dot_dot_after_a_directory_link_is_resolved_as_the_system_does`, `test_a_link_loop_is_reported_as_unreadable_and_the_run_goes_on`, `test_an_absolute_link_out_of_the_repository_is_not_read`, `test_every_directory_link_is_reported_wherever_it_points` (the last four need POSIX) |
| Fix: `gate/run_tests.py project-level`, `foundation_check.py`, `skill_entry_points.py`, `check_instructions.py`, the author's scripts | author, `eeca32c` | each exit 0 ([`reports/fix_report.md`](reports/fix_report.md)) | `installation` and `agent-instructions` tests not run by the fix (Markdown they do not read); run in the final gate |
| Author: `gate/run_tests.py project-level` (271), `agent-instructions` (18), `installation` (44); `foundation_check.py`; `skill_entry_points.py`; `check_instructions.py . --file` on each of the ten files; `verify_counts.py`; `compare_sentences.py`; `make_assessment.py`; `check_pointers.py` | author, `c0a0f52` | each exit 0 ([`reports/author_report.md`](reports/author_report.md), "Checks") | `check_instructions.py`: 1 warning on the repository (`AGENTS.md:21`, as on the base) |
| Return step: `gate/run_tests.py project-level`, `agent-instructions`; `foundation_check.py`; `skill_entry_points.py`; `check_instructions.py`; the author's scripts (`verify_counts.py` 279 figures, 0 differ) | author, `09b0dd0` | each exit 0 ([`reports/return_report.md`](reports/return_report.md)) | `installation` tests not run (nothing they read changed); run in the final gate |
| Reviews' focused checks and own recounts of words | reviewers, `c0a0f52`, `eeca32c`, `09b0dd0` | each exit 0, save the reviewers' clause scripts, which exit 1 by design listing the named rewordings ([`reports/review_report.md`](reports/review_report.md), [`reports/review_fix_report.md`](reports/review_fix_report.md), [`reports/return_review_report.md`](reports/return_review_report.md)) | — |
| `python -B gate/run_tests.py` | orchestrator, detached checkout of `eeca32c` (the reviewed fix), Windows | exit 0 — 804 tests in 9 directories ([`gate_eeca32c.txt`](gate_eeca32c.txt)) | the same five tests as on the base skipped on Windows |
| Final: `python -B gate/run_tests.py` | orchestrator, detached checkout of `09b0dd0` (the final tree: the target branch had not moved, `origin/foundations` still `2754675` after a fetch, so the reconciliation is empty), Windows | exit 0 — 804 tests in 9 directories, every directory passed ([`gate_09b0dd0.txt`](gate_09b0dd0.txt)) | no check failed in a cycle run. The same five tests as on the base skipped on Windows (POSIX or FIFO only), so they are unchecked |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator | exit 0 — `tag: foundation-review/2026-11-06`, `merges: 7`, `threshold: 30`, `reminder: no` | — |
| `python -B task-cycle/remarks_check.py .runs/task-cycles/define-project-skill-shape` (original) | orchestrator | runs after each stage report; one run listed the line `verify_counts result: …` of the return step's report, held wrong (Q8); last run exit 0, `checked: 6 reports, 16 items other than none, 0 not in the process remarks` | — |
| Copy: `python -B task-cycle/private_paths_check.py docs/task-cycles/define-project-skill-shape` | orchestrator, the copy on the task branch | run 1 exit 1, 12 places listed (absolute paths of the worktree in handoffs and scripts, of the task's note and of the author's rules, one note link in the task copy), cleaned by one rewriting with the private note names the check does not list; every later run exit 0, `checked: 28 files, 0 listed` | — |
| Copy: `python -B task-cycle/remarks_check.py docs/task-cycles/define-project-skill-shape` | orchestrator, the cleaned copy | exit 0 on every run, `checked: 6 reports, 16 items other than none, 0 not in the process remarks` | — |
| `python -B task-cycle/cycle_stages.py 1532b3d9-fc13-47ec-bd5d-b4231c364b08 --output .runs/task-cycles/define-project-skill-shape/stages.md` | orchestrator | exit 0, warnings none | — |

## Return step

- Foundation compared with code: the decisions of the task's *Decisions in play* (WAY-256, 257, 265, 106, 112, 118, 156, 120, 113, 111, 127, 259) and those the skill cites (WAY-30, 114, 121, 142, 150), the invariants `skill-rule-source`, `outbound-link-reach`, `project-definition-form`, `project-readiness-gate`, `skill-entry-points`, `derived-file-content`, the part-map entry `project-level`, the glossary, and a search of the whole foundation for entries naming a step, section or file of the skill, each compared with the new files: one mismatch — the new file `gate.md` used "gate", which the glossary gives as the one command that runs all tests; renamed `readiness_gate.md` with its three pointers (`09b0dd0`). Text moved word for word from the base still says "the gate" for the readiness gate, as WAY-118 and the definition template do; left to proposal 4 ([`reports/return_report.md`](reports/return_report.md))
- Decisions written or changed: none
- Invariants written or changed: none
- Environment facts: none
- Glossary terms: none written; a use against the entry "gate" corrected in the file name the change added
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: none

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/85 — draft while the record is committed; marked ready for review after its description carries the link to the record by SHA
- Description: `request.md` beside this record, written by `task-cycle/skill/request_template.md`; form check `python -B task-cycle/request_check.py .runs/task-cycles/define-project-skill-shape/request.md --task .runs/task-cycles/define-project-skill-shape/task.md`, run 3 times, last exit 0, and `python -B task-cycle/private_paths_check.py .runs/task-cycles/define-project-skill-shape/request.md`, run 2 times, last exit 0, before the request opened; the description with the record's links and the checks on the copy stand after this commit — `written and checked after this commit`. Number check: [`reports/verify_request.py`](reports/verify_request.py), exit 0, 0 numbers unmatched (shown able to fail by a control copy with four wrong numbers, exit 1).
- Writes to the task's backlog entry: none — the request link was not added to the task's entry in the backlog; closing the series is outside this task
- Process remarks on the-way:
  - author (rebuild, report of the one author), .runs/task-cycles/define-project-skill-shape/reports/author_report.md: The task's Context says the file last changed in `4a3ee37`; `git log --follow` gives `e19ee2d`
    (2026-10-22), and `4a3ee37` does not touch `project-level/skill/SKILL.md` (it changes
    `definition_template.md` and `project-level/technology/`). No figure depends on it.
  - author (rebuild, report of the one author), .runs/task-cycles/define-project-skill-shape/reports/author_report.md: The task's 1937 against the handoff's 1929: found - the locale of `wc -w` (above).
  - author (rebuild, report of the one author), .runs/task-cycles/define-project-skill-shape/reports/author_report.md: Route 3a: question 4 gives "the delegated mode, step 0 and step 7"; whether step 0 includes the
    variant file of an existing definition is not said. I count it, since a dispatched turn always
    works on a named definition; without it route 3a would show 205 words fewer, and `word-counts.md`
    says the rule.
  - author (rebuild, report of the one author), .runs/task-cycles/define-project-skill-shape/reports/author_report.md: The route 1 estimate of the task: no reading of question 1 that I found reproduces it.
  - author (rebuild, report of the one author), .runs/task-cycles/define-project-skill-shape/reports/author_report.md: "The gate" means the test command in the glossary and the readiness gate here: unclear which a
    reader takes; proposal 4.
  - author (rebuild, report of the one author), .runs/task-cycles/define-project-skill-shape/reports/author_report.md: No mistake of an agent working by this skill in the records searched; every ground of the table
    is a carried decision or step, or a cost.
  - whole-change review, .runs/task-cycles/define-project-skill-shape/reports/review_report.md: Where `define-project` "names where" a finding of `close.md` goes, other than 7.1: not found in
    `SKILL.md`, `technology.md` or any file beside them (I-1).
  - whole-change review, .runs/task-cycles/define-project-skill-shape/reports/review_report.md: The task's Context says `SKILL.md` last changed in `4a3ee37`: `git log --follow` gives `e19ee2d`,
    and `4a3ee37` does not touch the file — the author's note holds; no figure depends on it.
  - whole-change review, .runs/task-cycles/define-project-skill-shape/reports/review_report.md: Whether route 3a's step 0 includes `existing_definition.md`: question 4 does not say; the
    author counts it, and the dispatched turn always works on a named definition, so I agree.
  - whole-change review, .runs/task-cycles/define-project-skill-shape/reports/review_report.md: Whether "Once the definition is written (step 3)" could be read by a resuming agent as "once step
    3 ran in this session": unclear in principle; the parenthesis names the step that writes the
    file, and the file exists, so I did not raise it.
  - fix of the review's findings, .runs/task-cycles/define-project-skill-shape/reports/fix_report.md: Step 0 runs `readiness_check.py` on an approved definition (`existing_definition.md:9-12`) and
    routes only a fingerprint mismatch (to step 7). It does not say where another finding of that
    run goes. In the base, 7.1 stood in the same file. It is unclear whether the base meant 7.1 to
    route such a finding at step 0. The review did not raise it, and I did not extend the pointer to
    step 0, since that could add a route. Route 4 goes on to step 7, which runs 7.1 anyway.
  - review of the fix, .runs/task-cycles/define-project-skill-shape/reports/review_fix_report.md: A place where the base routed a non-mismatch finding of step 0's check on an approved definition:
    not found (judged above).
  - review of the fix, .runs/task-cycles/define-project-skill-shape/reports/review_fix_report.md: Whether "a turn that `lead-project` dispatches" (`delegated_mode.md:3`) could be read as a
    condition wider than "a definition edit or step 7 through a refinement conversation path": unclear
    in principle; the next sentence gives the exact condition and `SKILL.md` has the file read only on
    it, so I raised nothing.
  - return step, .runs/task-cycles/define-project-skill-shape/reports/return_report.md: Whether the uses of "the gate" moved from the base fall under "a term used against its entry
    takes the use corrected": they predate the change, they stand in WAY-118's binding sentences, and
    correcting them leaves `project-level/skill/`. I read the rule as binding the change's own uses.
    The question is left to proposal 4.
  - the orchestrator: `task-cycle/remarks_check.py` lists the line `verify_counts result: exit 0, 279
    figures compared, 0 differ` of `.runs/task-cycles/define-project-skill-shape/reports/return_report.md`
    as an item of its **Searches not found or unclear**. The cycle holds the listing wrong: the line is
    no item but a check result the author appended after the section's one bullet, the last line of
    the file, separated from the bullet by a blank line and not opening with `- `; it repeats the
    report's own result of `verify_counts.py`. It is not appended as an item (WAY-295).
  - return step review, .runs/task-cycles/define-project-skill-shape/reports/return_review_report.md: Which reports the request description will draw from is not stated anywhere in the record
    (`cycle.md:98` "Description: pending"); M-1 is graded on the assumption that `fix_report.md` may be
    one of them.

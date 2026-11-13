# Cycle record — the way: audit of the process — a new series of gate times after parallel directories

- Task source: the task's note in the author's backlog, `Status: ready for cycle`, accepted 2026-11-13 (answer "1 a" through the day's adviser); frozen copy `task.md` beside this record
- Task relation: independent
- Product repository: the-way (mariusznazar/the-way)
- Process pin: `715ae20` (the-way itself; no pin to move)
- Target branch and base: `foundations`, `715ae20d9e817299bd81554e5fdcb6baaf465099`
- Task branch: `task/gate-series-on-test-runner`
- Status: request open

## Two questions at start

- Trust boundary: yes — `process-audit/audit_count.py` is the part map's trust boundary of the part `process-audit` (it reads cycle records and git history of products, files from outside). The change edits it, so every code review of the cycle is told so and checks crafted input at it: a path in the list of instrument files, a malformed `gate_times.md`, a repository whose history lacks `gate/run_tests.py`.
- Irreversible operation: no

## Spec and execution route

- Open design choice at start: none — the task settles which file starts a series (every change of `gate/run_tests.py`, as of `task-cycle/gate_times.py`), that the audit names it as the reason of the split, that other series are not split by it, and that WAY-339 and `process-audit/SKILL.md` say the same. What the code makes of it (a tuple of paths for `instrument_series`, the wording of the reason) is a choice of how to make what the task settles.
- Reserved choice: none
- Execution route and reason: one author without a plan — one function, one constant, one paragraph of the skill, one decision and their tests; one agent holds it
- Author: `cheaper` class (WAY-229), the harness's haiku model; ordinary implementation with a few decisions of its own
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: native completion notification of the harness (background agent), no limit reached
- Whole-change review: a fresh reviewer (sonnet, `same`), `review-change`; range `715ae20..909fcb9`; `FAIL 909fcb9` (`reports/whole-review-report.md`); changed files with lines before to after: `foundations/decisions.md` 12341→12353, `process-audit/SKILL.md` 225→227, `process-audit/audit_count.py` 2972→2983, `process-audit/test_audit_count.py` 3128→3186; both items of *To do* and row 1 of *Settlements to record* met in code, skill and WAY-339 (finding 1 against the *violates* list); no spec, no plan; read 8 of 46 selected decisions whole and 39 by title, none of the 39 bearing on the change; invariants and glossary read by a resumption (19 invariants, 0 new findings)
- Review rounds:
  - findings `reports/fix-findings.md`: review of the whole change `715ae20..909fcb9`, `FAIL`: 1 Important (WAY-339 *Verification*: the correct *violates* bullet about the recording script deleted on a false claim) and 4 Minor within the task (the runner named "of the gate" not "of the process"; *Rejected* tense; *Rationale* sentence against the task's reason; structure note asking no change); fix `909fcb9..b8dc239` (`reports/fix-report.md`), review of the fix `PASS b8dc239` (`reports/fix-review-report.md`), one new Minor (unwrapped lines of *Rejected*), fixed afterwards by the return step's commit; no blocking finding remained
- Weakest-point checks: author: requirement "a change of `gate/run_tests.py` starts a gate series only, and the reason names it"; check: two new tests, failing on the old code (the medians of the gate series; `IndexError` on the missing reason), passing now; the reviewer judged the tests protect the behaviour (`reports/author-report.md`, `reports/whole-review-report.md`)

## Slices

Not applicable: one author, no plan.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-13 | start | orchestrator (sonnet 5.5) | task, `task-cycle/skill/SKILL.md`, foundation reading | this record | branch and worktree created from `715ae20`; base is a merge with the tree of its second parent, so the failing list is taken from the merged cycle's final gate |
| 2026-11-13 | one author | author (haiku, `cheaper`) | `reports/author-handoff.md`; `task-cycle/change/SKILL.md`, variant "the whole change as the one author"; `task.md` | `reports/author-report.md` | dispatched from base `715ae20` |
| 2026-11-13 | one author, return | author | `reports/author-handoff.md` | `reports/author-report.md`, commit `909fcb9` | `done`; mechanical check passed: clean tree, range `715ae20..909fcb9` non-empty, 4 files (decisions.md, SKILL.md, audit_count.py, test_audit_count.py) match the task; process-audit run exit 0 (182 tests), foundation_check exit 0; own-work check, Unread material and Searches present. The author flags a removed *violates* bullet of WAY-339 — passed to the reviewer |
| 2026-11-14 | whole-change review | reviewer (sonnet, `same`) | `reports/whole-review-handoff.md`; `task-cycle/review/SKILL.md`; range `715ae20..909fcb9` | `reports/whole-review-report.md` | dispatched |
| 2026-11-14 | whole-change review, fix | reviewer (sonnet), resumed once for its unread invariants and glossary | `reports/whole-review-handoff.md` | `reports/whole-review-report.md`: `FAIL 909fcb9`; 1 Important, 4 Minor within the task, 0 outside; addendum read 19 invariants and the glossary: 0 new findings | the gap in the reviewer's own selection is closed by the resumption; findings file `reports/fix-findings.md` cut from the report in its words; author resumed for the fix |
| 2026-11-14 | fix | author (haiku), resumed | `reports/fix-handoff.md`, `reports/fix-findings.md`; `task-cycle/change/fix.md` | `reports/fix-report.md` | dispatched from `909fcb9` |
| 2026-11-14 | fix, return | author (haiku), resumed | `reports/fix-handoff.md` | `reports/fix-report.md`, commit `b8dc239` | `done`; mechanical check passed: clean tree, range `909fcb9..b8dc239` holds 1 file (decisions.md), `foundation_check.py` exit 0, own-work check, Unread and Searches present. The author first wrote the report into the original checkout's `.runs/` and deleted the file; the two empty directories it left there were removed by the orchestrator |
| 2026-11-14 | fix review | reviewer (sonnet), resumed | `reports/fix-review-handoff.md`; `task-cycle/review/fix.md`; range `909fcb9..b8dc239` | `reports/fix-review-report.md` | dispatched |
| 2026-11-14 | fix review result | reviewer (sonnet), resumed | as above | `reports/fix-review-report.md`: `PASS b8dc239` | no blocking finding remains; the reviewer found one new Minor (the edited lines of *Rejected* in WAY-339 are not re-wrapped, `foundations/decisions.md:11277-11278`): not fixed, goes to the request's list |
| 2026-11-14 | return step | author (haiku), resumed | `reports/return-handoff.md`; `task-cycle/skill/return_step.md` | `reports/return-report.md` | dispatched from `b8dc239` |
| 2026-11-14 | return step result | author | as above | `reports/return-report.md`, commit `5b87cb1` | `done`; one correction: the *Rejected* paragraph of WAY-339 re-wrapped to the entry's width, no word changed (word diff of the commit is empty); `foundation_check.py` exit 0; other entries, part map and glossary match |
| 2026-11-14 | return step review | fresh reviewer (sonnet, `same`) | `reports/return-review-handoff.md`; range `b8dc239..5b87cb1` | `reports/return-review-report.md` | dispatched |
| 2026-11-14 | return step review result | fresh reviewer (sonnet) | as above | `reports/return-review-report.md`: `PASS 5b87cb1` | 0 findings; the commit changes whitespace only, WAY-339 hashes the same before and after once whitespace is collapsed |
| 2026-11-14 | gate on `5b87cb1` | orchestrator | `python -B task-cycle/gate_times.py --output docs/task-cycles/gate-series-on-test-runner/gate_times.md -- python -B gate/run_tests.py` | `final-gate.log` | exit 0; 1240 tests in 10 directories, every directory passed (610 s); superseded by the run on the merged tree below |
| 2026-11-14 | merge of the target branch | orchestrator | `git merge origin/foundations` (#112, `f04f046`) | merge commit `1f7dab2` | clean; brought the cycle's agent types and WAY-368..370; no review of the merge (Q2); gate run again on the merged tree |
| 2026-11-14 | gate on `1f7dab2` | orchestrator | the same command | `final-gate.log` (the earlier one kept as `final-gate-before-merge.log`) | exit 0; 1267 tests in 10 directories, every directory passed; one other gate was running at the same time (the row of `gate_times.md` says 1), so by WAY-350 this run is shown apart from the compared ones |
| 2026-11-14 | measures | orchestrator | `task-cycle/cycle_stages.py`, `task-cycle/cycle_measures.py` naming this session | `stages.md`, `mechanism_measures.md` | both exit 0 |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | Class of the one author (step 4) | `cheaper` (haiku) | the change is ordinary implementation: a constant, a function parameter, text and tests | `same` — dearer, nothing here calls for design | a failed review round, one fix | author |
| Q2 | Does the merge of the moved target branch (#112) change the reviewed code, so that a fresh reviewer must review it? (step 12) | no review of the merge | the merge is clean; `git diff 715ae20 origin/foundations --name-only` names no file of `process-audit/` or `gate/` and the upstream diff of `foundations/decisions.md` adds only WAY-368, WAY-369 and WAY-370 (agent types), not touching WAY-339, WAY-349 or WAY-350; the upstream part-map edits concern `task-cycle`, `repository` and `installation`, not `process-audit` or `gate`; `foundation_check.py` on the merged tree: exit 0, 0 errors | a reviewer for the merge — dearer, nothing of the change meets what the merge brought | a conflict of meaning between WAY-368..370 and the edited WAY-339 left unseen; the final gate and the foundation check run on the merged tree | step 12 |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| frozen task | `task.md` beside this record | orchestrator | none |
| code and foundation commits | `909fcb9`, `b8dc239`, `5b87cb1`; merge `1f7dab2` | author (haiku) | `FAIL`, `PASS`, `PASS`; merge not reviewed (Q2) |
| reports | `reports/author-report.md`, `fix-report.md`, `return-report.md`, `whole-review-report.md`, `fix-review-report.md`, `return-review-report.md` | agents | as listed in Events |
| measures | `stages.md`, `mechanism_measures.md`, `gate_times.md` | scripts | none |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| list of the tests failing before the change | orchestrator, base `715ae20` (merge; tree `3c1b04de766a2659437af30eabc8ec1dc08adfc5` equals that of its second parent `c3aded0`) | taken from `docs/task-cycles/gate-parallel-directories/cycle.md` of commit `575f286`, *Verification*, its final gate (`9282e6f`): exit 0, 1238 tests in 10 directories, every directory passed | none failing on the base; no gate run on the base |

| `python -B gate/run_tests.py process-audit` | author on `909fcb9`; reviewer on `909fcb9` | 0; 182 tests; the new tests failed first on the old code | none |
| `python -B elements/common/foundation_check.py` | author, reviewers, return step; orchestrator on `1f7dab2` | 0; 0 errors | none |
| `python -B task-cycle/gate_times.py --output docs/task-cycles/gate-series-on-test-runner/gate_times.md -- python -B gate/run_tests.py` | orchestrator, `5b87cb1` (final tree before the merge) | 0; 1240 tests in 10 directories, every directory passed (610 s) | none |
| the same command | orchestrator, `1f7dab2` (final tree, merged with #112) | 0; 1267 tests in 10 directories, every directory passed (747 s, one other gate running at the same time) | none |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator | 0; `tag: foundation-review/2026-11-06`, `merges: 35`, `threshold: 30`, `reminder: yes` | none |
| `python -B task-cycle/cycle_stages.py --output docs/task-cycles/gate-series-on-test-runner/stages.md <session>`; `python -B task-cycle/cycle_measures.py --output docs/task-cycles/gate-series-on-test-runner/mechanism_measures.md <session>` | orchestrator | both 0 | none |

The checks failing on the base: none. The move of the pin: none (the-way itself).

## Return step

- Foundation compared with code: WAY-339 (written), WAY-349 and WAY-350 (named by the task), the part-map entries `process-audit`, `task-cycle` and `gate`, and the glossary compared with `process-audit/audit_count.py`, `process-audit/SKILL.md`, `gate/run_tests.py` and `task-cycle/gate_times.py`: the *Rejected* paragraph of WAY-339 had lines far over the width of the entry after the fix, re-wrapped in `5b87cb1` (no word changed); nothing else no longer matched (`reports/return-report.md`; the commit's review `PASS 5b87cb1`)
- Decisions written or changed: WAY-339
- Invariants written or changed: none
- Environment facts: none
- Glossary terms: none
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: row 1, WAY-339

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/113, draft (marked ready after the record's commit)
- Description: `request.md` beside this record, written by `task-cycle/skill/request_template.md`; form check `python -B task-cycle/request_check.py docs/task-cycles/gate-series-on-test-runner/request.md --task docs/task-cycles/gate-series-on-test-runner/task.md` last exit 0 (1 run), private paths check on it last exit 0 (1 run); the copy's checks are written after this commit
- Writes to the task's backlog entry: pending (see the final report)
- Corrections after the request opened: none
- Process remarks on the-way:
  - one author, docs/task-cycles/gate-series-on-test-runner/reports/author-report.md: None unresolved. Note: a first full-module `unittest` run was started by mistake and stopped (TaskStop) before any result was read; it did not change files.
  - one author, docs/task-cycles/gate-series-on-test-runner/reports/author-report.md: Repository harness: `Repository.commit` writes only the files it is given (not inherited from the parent), as the fixture test showed. Noted in the test comment.
  - whole-change review, docs/task-cycles/gate-series-on-test-runner/reports/whole-review-report.md: Coding guidelines and testing guidelines of the-way: not found, by WAY-328 they do not exist for its own code.
  - whole-change review, docs/task-cycles/gate-series-on-test-runner/reports/whole-review-report.md: The rule `### Size of a function and a file` of a product's `guidelines/coding.md`: no `guidelines/` directory in the-way; so no size test.
  - whole-change review, docs/task-cycles/gate-series-on-test-runner/reports/whole-review-report.md: The base text of WAY-339 was not available as a file at the base commit in this worktree beyond the diff; I read it from the diff (`git diff 715ae20..909fcb9`), which is complete for that entry.
  - return step review, docs/task-cycles/gate-series-on-test-runner/reports/return-review-report.md: A written line-width rule for foundation entries: not found (`elements/common/rules.md` and a search of the worktree's `*.md` and `*.py`). The return report's phrase "the entry's width" has no stated number.

# Cycle record — the way: mapa części — siedem zależności spoza Depends on i kto mówi, jak powstaje linia zadania

- Task source: `the task's note in the author's backlog`, settlements accepted 2026-11-15; frozen copy `task.md` beside this record
- Task relation: independent
- Product repository: mariusznazar/the-way (the-way itself)
- Process pin: none — the-way is the top-level repository; the process is the checkout's own
- Target branch and base: `foundations`, `c2541ed6ef1aca0e5509cc9a929f377d97a108bc`
- Task branch: `task/part-map-dependencies-task-line`, worktree `the root of the task's worktree`
- Status: request open

## Two questions at start

- Trust boundary: no — the change edits `foundations/*.md`, `project-level/task_line.md`, `project-level/backlog_place.md` and adds tests; none of the files the part map names as a trust boundary (`project-level/readiness_check.py`, `plan_check.py`, `plan_state.py`, `task-cycle/cycle_stages.py`, `cycle_measures.py`, `gate_times.py`, `process-audit/audit_count.py`, `instruction-files/check_instructions.py`, `installation/install.py`) is to change; the new tests read `plan_state.py`, `audit_count.py`, `review_reminder.py` and `foundation_check.py` as they stand. Each review is told to name any such file the change touches after all.
- Irreversible operation: no — nothing in the change cannot be undone; the task's *Human actions* is `none`.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none — the task settles each choice (the meaning of a dependency, `Depends on` for all ten, four tests, the change of WAY-107, who rewrites the sentence of `project-level`); each row of *Settlements to record* and each decision of *Decisions in play* is settled; what *Questions carried to cycle* leaves — the wording of the entries and how each test finds its writing side — is a choice of how to make what the task settles (no way costly to turn back: a test is edited with its entry).
- Reserved choice: none — no language, framework, library, store of data, login or place to run is open.
- Execution route and reason: one author without a plan — the task names every file and sentence; ten lines of one file, one glossary entry, four invariants with four small tests, one sentence of WAY-107 and three sentences in two skill files fit one agent (WAY-136). No slice-size script run.
- Author: `the-way-author`, class `same` as the orchestrator (a change across many parts: `decisions`, `part-map`, `glossary`, `invariants`, `project-level`, and tests that stand in the parts they test), the harness's model `sonnet`; its resumptions follow in the Events.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: native completion notification of the harness; foreground `Agent` calls block where the mode allows, a background agent reports by notification; no limit met yet
- Whole-change review: a fresh reviewer (`the-way-stage`, `sonnet`, class `same`) by `review-change`; range `c2541ed..af76148`, report `reports/review-whole-report.md`, first line `FAIL af7614867a6e477088a7831fc170c4b279b6ba21`; 12 files, +420 / −51 (`elements/common/test_guidelines_place.py` 86/0, `elements/invariants/examples.md` 4/3, `elements/part-map/template.md` 11/9, `foundations/decisions.md` 44/23, `foundations/glossary.md` 6/0, `foundations/invariants.md` 40/0, `foundations/part_map.md` 18/13, `process-audit/test_gate_runner_path.py` 48/0, `project-level/backlog_place.md` 3/2, `project-level/task_line.md` 5/1, `project-level/test_blocked_request_line.py` 69/0, `task-cycle/test_review_tag_pattern.py` 86/0); coverage: each of the seven items of *To do* and each of the seven rows judged one by one, the ten dependencies compared with the diff of the map, 18 breaks of the four tests each seen failing, source fidelity found sound; 13 of the 63 decisions of its index read whole; 1 blocking (I-1) and 4 Minor within the task (M-1 to M-4); one commit, no plan, no slice
- Review rounds:
  - findings `reports/whole-findings.md`: review of the whole change `FAIL af76148` with the blocking finding I-1 (the part-map sentence of `project-level` denied the derivation of the identifier that the part holds) and the Minor findings M-1, M-2, M-3 within the task (M-4 the reviewer marked outside the scope; the cycle did not fix it); fix by the one author, range `af76148..1b5aba9`, report `reports/author-fix-report.md`: I-1, M-1, M-2 fixed, M-3 fixed where it lay within the task, the binding sentence of WAY-225 kept as the frozen task says ("Bez zmiany"); review of the fix by the same reviewer, `PASS 1b5aba91fce0a23ee95d6bab2e107eb187b34d67`, report `reports/review-whole-fix-report.md`; no blocking finding remained; one new Minor in the fix (line 4 of `foundations/part_map.md` is 106 characters), kept in the request's list; no revert
- Weakest-point checks: the author named "each of the four tests fails when the reading side or the writing side changes alone", broke each side, found `test_guidelines_place.py` too narrow at first and widened it (`reports/author-report.md`, *Own-work check*); the fix author's: "the split leaves each rule with its own test failing alone", two breaks, each failed only its own test (`reports/author-fix-report.md`)

The last commit of a discarded attempt or of a slice returned too large is a historical name, not
a link to follow: the commit is reachable only until the reflog expires. A choice or ruling of a
discarded attempt keeps its row in the questions table, with *Used by* naming the discarded
attempt.

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

One author, no plan.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-15 01:5x UTC | start | orchestrator, session `777280c9-9741-4f22-86df-3621b2ac7c7d` (claude-sonnet-5-5) | entry point `the-way-implement-task`, task document, `AGENTS.md`, `agent-instructions/README.md` | — | the checkout `foundations` stood 9 commits behind `origin/foundations` with a clean tree: fast-forwarded to `c2541ed`; the skill's step 13 changed in that range and was read again; the-way is the top-level repository (no superproject, no `.the-way` entry) |
| 2026-11-15 01:5x UTC | step 4 removal | orchestrator | `python -B task-cycle/remove_merged_worktrees.py --apply --target foundations` | exit 0 | removed `foundation-review-reminder`; kept four directories (listed under *Directories of earlier tasks kept*) |
| 2026-11-15 01:5x UTC | branch | orchestrator | `git worktree add --no-track -b task/part-map-dependencies-task-line ../the-way-wt/part-map-dependencies-task-line origin/foundations` | worktree at `c2541ed` | base is a merge commit (`c2541ed`, second parent `880fd4c`) whose tree `a7e061d1b0a9a2774a27f6caf5e1c4346d4f9777` equals that of its second parent, so no gate run on the base |
| 2026-11-15 02:0x UTC | author | `the-way-author`, model `sonnet` (class `same`), foreground | `reports/author-handoff.md`; `make-change`, "the whole change as the one author"; frozen task; index of decisions `.runs/orchestrator/index.md` | `reports/author-report.md` | done with concerns; commit `af76148`; mechanical check: clean worktree, non-empty range, 12 files; report has own-work check, unread material, searches, commands with exit codes; its gaps are carried to the whole-change review |
| 2026-11-15 02:2x UTC | whole-change review | `the-way-stage`, model `sonnet` (same class), foreground | `reports/review-whole-handoff.md`; `review-change`, whole change, range `c2541ed..af76148` | `reports/review-whole-report.md` | `FAIL af76148`: 1 blocking (I-1, Important: the part-map sentence of `project-level` denies the derivation of the identifier that the part holds), 4 Minor within the task (M-1 to M-4; M-4 the reviewer marks outside the scope and the cycle leaves it), 2 out of scope; 13 of 63 decisions read whole; 18 breaks of the four tests all failed as they should; next: one fix with the findings file `reports/whole-findings.md` |
| 2026-11-15 02:4x UTC | fix | `the-way-author` (the same author, resumed), class `same`, model `sonnet` | `reports/author-fix-handoff.md`; `make-change`, "the fix of a review's findings"; findings `reports/whole-findings.md` | `reports/author-fix-report.md` | done with concerns; commit `1b5aba9`; mechanical check: clean worktree, 8 files; I-1, M-1, M-2 fixed (M-2 by a split into `blocked-request-wording` and `blocked-request-label`), M-3 fixed in part: the author left the binding sentence of WAY-225 and the prose of WAY-225 and WAY-51, citing the task's "Bez zmiany", with evidence; unread `none` |
| 2026-11-15 02:5x UTC | review of the fix | `the-way-stage`, same reviewer resumed, model `sonnet` | `reports/review-whole-fix-handoff.md`; `review-change`, fix range `af76148..1b5aba9`; findings `reports/whole-findings.md` | `reports/review-whole-fix-report.md` | `PASS 1b5aba9`; no new Critical or Important finding; one new Minor (line 4 of `foundations/part_map.md` is 106 characters; no width rule found) goes to the request's list; M-3's remainder (the bare word in WAY-225, which the task keeps unchanged) accepted by the reviewer as outside the fix; next: return step |
| 2026-11-15 03:0x UTC | return step | `the-way-author` resumed, class `same`, model `sonnet` | `reports/return-step-handoff.md`; `task-cycle/skill/return_step.md`, `foundation_step.md` | `reports/return-step-report.md` | done, no commit (nothing no longer matched), head stays `1b5aba9`, so no review of the return step; checks: `foundation_check.py` exit 0 `0 errors`, `skill_entry_points.py` exit 0, `gate/run_tests.py elements/part-map` exit 0; searches `none`, unread `none`; `origin/foundations` still `c2541ed`, so no reconciliation; next: the full gate, which waits for the signal `start` of the day's advisor (the user's order of this cycle) |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | Does the-way have product guidelines (`guidelines/`) the agents are to read (`product-guidelines/reading.md`)? | No: the repository has no `guidelines/` directory, so there is none to name in a handoff; WAY-328 is among the headings of the index, not opened (the change writes no code beyond four small tests) | `ls guidelines` fails at the worktree root | read WAY-328 whole | a test written without the product's coding rules; the whole-change reviewer reads its own selection | author handoff |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| frozen task | `docs/task-cycles/part-map-dependencies-task-line/task.md` | orchestrator | — |
| code and foundation entries of the one author | commit `af76148` | one author (`the-way-author`, `sonnet`) | `FAIL af76148`, then fixed |
| fix of the whole-change review's findings | commit `1b5aba9` | the same author, resumed | `PASS 1b5aba9` |
| return step | no commit; head stays `1b5aba9` | the same author, resumed | no change to review |
| reports | `reports/author-handoff.md`, `author-report.md`, `review-whole-handoff.md`, `review-whole-report.md`, `whole-findings.md`, `author-fix-handoff.md`, `author-fix-report.md`, `review-whole-fix-handoff.md`, `review-whole-fix-report.md`, `return-step-handoff.md`, `return-step-report.md` | the agents and the orchestrator | — |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| list of the tests failing before the change | orchestrator, base `c2541ed` (merge; tree `a7e061d1b0a9a2774a27f6caf5e1c4346d4f9777` equals that of its second parent `880fd4c`) | taken from `docs/task-cycles/foundation-review-reminder/cycle.md` of commit `025583e` (the only copy the merged branch added), *Verification*: its final gate, run 1 on `e5ae875`, exit 0, 1445 tests in 10 directories, every directory passed; the earlier cycle's `decision-log-second-round` run had failed only `gate` on `test_by_default_every_directory_runs_at_the_same_time`, a flaky timing test | none failing before the change; one test known flaky; no gate run on the base |
| `python -B task-cycle/gate_times.py --output docs/task-cycles/part-map-dependencies-task-line/gate_times.md -- python -B gate/run_tests.py` (run 1) | orchestrator, `1b5aba9` (the final tree; `origin/foundations` had not moved from `c2541ed`, so no reconciliation), Windows, started 2026-11-15 02:35 UTC (by the clock of `gate_times.md`) on the signal `start` of the day's advisor (about 17 GB free by its word; checked by the orchestrator: 16.6 GB free, no `run_tests` process) | 0; 1456 tests in 10 directories, 365.9 s, 0 other gate runs at the same time; every directory passed | none |
| `python -B elements/common/foundation_check.py`, without `--skip-test-citations` | orchestrator, `1b5aba9` | 0; `0 errors`; no `listed:` line | none |
| `python -B task-cycle/review_reminder.py origin/foundations` (after `git fetch --tags`) | orchestrator | 0; `tag: foundation-review/2026-11-15`, `merges: 2`, `threshold: 60`, `reminder: no` | none |
| focused checks of the author, the fix and the reviewers: `python -B gate/run_tests.py elements/part-map` (39), `elements/common` (235), `project-level` (278), `process-audit` (184), `task-cycle` (483), `agent-instructions` (25); `python -B agent-instructions/skill_entry_points.py` | author, fix author, reviewers | exit 0 each in its last run | none |
| the first failing run of each new invariant test: the writing or the reading side broken for a moment, `python -B -m unittest <test file>` | author, reviewers (18 breaks, all exit 1), fix author | exit 1 each break, then exit 0 restored | none |
| `python -B task-cycle/cycle_stages.py --output docs/task-cycles/part-map-dependencies-task-line/stages.md 777280c9-9741-4f22-86df-3621b2ac7c7d`; `python -B task-cycle/cycle_measures.py --output docs/task-cycles/part-map-dependencies-task-line/mechanism_measures.md 777280c9-9741-4f22-86df-3621b2ac7c7d` | orchestrator, the one session of the cycle (run before the final steps of the request, which the figures do not count) | both 0 (working time 0:37:28, waiting for tools 0:13:43, 40.9 million tokens, all `claude-sonnet-5-5`) | none |
| `python -B task-cycle/remarks_check.py .runs/task-cycles/part-map-dependencies-task-line` | orchestrator, on the original | exit 1 listing 8 items (appended word for word to the process remarks), then 0 | none |
| `python -B task-cycle/private_paths_check.py docs/task-cycles/part-map-dependencies-task-line`; `python -B task-cycle/image_files_check.py docs/task-cycles/part-map-dependencies-task-line`; `python -B task-cycle/remarks_check.py docs/task-cycles/part-map-dependencies-task-line` | orchestrator, on the cleaned copy of the record | each exit 0 in its last run, run again after each fresh copy of the record, the last run on the copy committed (0 listed in 18 files; 0 image files; 5 reports, 8 items, 0 not in the remarks); the original's remarks check: exit 1 then 0, 2 runs | none |
| `python -B task-cycle/request_check.py docs/task-cycles/part-map-dependencies-task-line/request.md --task docs/task-cycles/part-map-dependencies-task-line/task.md`; `python -B task-cycle/private_paths_check.py docs/task-cycles/part-map-dependencies-task-line/request.md` | orchestrator, on the description before it was published | both exit 0, 1 run each, before the record's link was added | none |
| unchecked: a second copy of the pattern for guidelines files in `elements/common/migrate_foundation.py`, held by no test; the paths `MEASURES_SCRIPT` and `GATE_SCRIPT` of `process-audit/audit_count.py`; the width of line 4 of `foundations/part_map.md` | reviewers, as they report | not covered by any invariant or rule; named in the request's lists | all three unchecked |

## Return step

- Foundation compared with code: the entries the change writes or changes (the part map's ten *Depends on* and the sentence of `project-level`; the glossary term `dependency of a part`; the five invariants `blocked-request-wording`, `blocked-request-label`, `gate-runner-path`, `review-tag-pattern`, `guidelines-file-place` against their tests and the constants and files they read; WAY-107 against `task_line.md` and `backlog_place.md`; the *Verification* of WAY-153, WAY-300, WAY-339 and WAY-167), those the task names (WAY-225, WAY-51, WAY-11, WAY-44, WAY-95, WAY-293, WAY-300, WAY-339) and the part map of the touched parts. Nothing no longer matched; a search for the retired identifier `blocked-request-line`, "three forms" and "invariant of allowed dependencies" found no use left. No correction, no commit.
- Decisions written or changed: WAY-107 (sentence, *Verification*, *Rationale*, *Rejected*, foundation step); *Verification* of WAY-153, WAY-300, WAY-339 and WAY-167 (foundation step)
- Invariants written or changed: `blocked-request-wording` and `blocked-request-label` (set by row 2; derive from WAY-153), `gate-runner-path` (row 3; WAY-339), `review-tag-pattern` (row 4; WAY-300), `guidelines-file-place` (row 5; WAY-167)
- Environment facts: none
- Glossary terms: `dependency of a part` (row 1)
- Part-map changes: the ten *Depends on* of seven parts and the sentence of `project-level` (*To do* 1 and 7)
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: row 1 → glossary term `dependency of a part`; rows 2–5 → the five invariants above (row 2 as two); row 6 → sentence of WAY-107; row 7 → `project-level/task_line.md`, a file of a place, no entry. Choices that bind after the merge and stand in an entry or a skill: that a test of a reading and writing pair belongs to the reading side's part is WAY-44 applied, so no entry (WAY-293). Reviewed: `PASS 1b5aba9`.

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/130 — opened as a draft; marked ready for review after the record's commit is linked
- Description: written and checked after this commit
- Writes to the task's backlog entry: pending
- Working copies left: reviewer of the whole change, `.runs/review-whole/index.md` (a file, no checkout; it goes with the task's directory)
- Directories of earlier tasks kept:
  - agent-path-to-running-product, branch `task/agent-path-to-running-product`: the branch has no merge git can see on origin/foundations: not merged, merged by squash or rebase, or its request open or closed
  - ci-on-merge-requests, branch `task/ci-on-merge-requests`: the branch has no merge git can see on origin/foundations: not merged, merged by squash or rebase, or its request open or closed
  - base-check-stage-remarks, detached: the branch task/stage-remarks its name gives is not found
  - base-fix-minor-findings, detached: the branch task/minor-findings its name gives is not found
- Corrections after the request opened: none
- Process remarks on the-way:
  - author, docs/task-cycles/part-map-dependencies-task-line/reports/author-report.md: The glossary uses of the word `dependency`: I searched the English text of the tracked files for its forms (274 lines outside Python); I judged each by its context and read the lines on parts and the part map; the lines of tasks and of products' packages carry the reader's meaning and I left them. I did not read each of the 274 lines in its full paragraph.
  - author, docs/task-cycles/part-map-dependencies-task-line/reports/author-report.md: No convention found for naming a test of an invariant; I used `test_<subject>.py`.
  - author, docs/task-cycles/part-map-dependencies-task-line/reports/author-report.md: The task gives no decision for rows 2 and 5 (see Choices, 4).
  - author, docs/task-cycles/part-map-dependencies-task-line/reports/author-report.md: The template says "one sentence" for a part while the task asks for two (Choices, 2).
  - whole-change review, docs/task-cycles/part-map-dependencies-task-line/reports/review-whole-report.md: WAY-33's cycle-side "search of the whole foundation" is not recorded in the commit; I cannot tell from the files what the author's search covered beyond the author's report, and I searched the word `dependency`, `three forms` and the identifier derivation myself.
  - whole-change review, docs/task-cycles/part-map-dependencies-task-line/reports/review-whole-report.md: No convention for naming the test files of an invariant was found (author's report says the same); `test_<subject>.py` fits the neighbours.
  - whole-change review, docs/task-cycles/part-map-dependencies-task-line/reports/review-whole-report.md: The task's item 7 says "a nie za to, jak powstaje" with no exception for the derivation, while its row 6 gives the derivation to the-way: unclear how the task meant both to hold (I-1).
  - fix, docs/task-cycles/part-map-dependencies-task-line/reports/author-fix-report.md: The finding M-3 says "and the like" without a list; I searched the part map, `elements/part-map/`, `elements/invariants/examples.md` and the decision log for the bare words and changed those that speak of the part map's dependency, leaving the decisions' prose as above.
  - the orchestrator: `python -B elements/common/decision_index.py --decision NUMBER` takes the number in the form `WAY-107` and answers `no decision 107` for `107`; `elements/common/way_of_working.md` step 2 and the script's own `--help` call the value a NUMBER, and the first call of both the orchestrator and the reviewer failed on it.

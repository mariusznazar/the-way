# Cycle record — the way: instalator odmawia zapisu przez junction Windows w folderze ustawień agentów produktu

- Task source: the task's note in the author's backlog, `Status: ready for cycle`, copy frozen 2026-11-14 as `task.md` beside this record
- Task relation: independent
- Product repository: the-way (github.com/mariusznazar/the-way)
- Process pin: the-way itself, `6fa755c`
- Target branch and base: `foundations`, `6fa755c` (checkout fast-forwarded from `ac75340` first; no change to the cycle's own files)
- Task branch: `task/installer-junction-refusal`, worktree `.runs/worktrees/installer-junction-refusal`
- Status: request open

## Two questions at start

- Trust boundary: yes — `installation/install.py` is the trust boundary of the part `installation`; the change edits it. Every code review of the cycle is told so and checks crafted input there (a junction in the product's agent settings folder, in a skill entry folder and at `.the-way`).
- Irreversible operation: no — the change removes the installer's way of writing or deleting through a junction; it prepares and performs no irreversible operation. The installer's own deletion of stale entries stays as it is, with the new refusal added.

## Spec and execution route

- Open design choice at start: none — the task settles the rule (question 1: refuse and recognise junction wherever a symlink is recognised today; question 2: an invariant with a citing test, row 1 of *Settlements to record*) and the means (`os.path.isjunction`, standard library of Python 3.14, WAY-38). How a helper is shaped is a choice of making what the task settles.
- Reserved choice: none — no language, framework, library, store, login or place to run is in play.
- Execution route and reason: one author without a plan — the change is one file of the installer with its tests plus one invariant; one agent holds it.
- Author: `the-way-author`, class `same` (a Sonnet-class model, the harness's closest to mine): the change touches a trust boundary and writes a foundation entry (invariant), across the parts `installation` and `invariants`.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: Claude Code `Agent` call, completion notification
- Whole-change review: `the-way-stage` (sonnet), `reports/review-whole-report.md`, `FAIL 474df77904b199e3ba1acb438c5a88c9a47d13c1`, range `6fa755c..474df77`; reviewer read 10 decisions whole, ~30 by title; all task items, row 1 and the decisions in play covered; one blocking finding
- Review rounds:
  - findings `reports/whole-review-findings.md`: whole-change review `reports/review-whole-report.md` range `6fa755c..474df77`, `FAIL`, blocking: invariant sentence broader than the code; fix range `474df77..ee6126c` (`62ec7c1`, `ee6126c`), review of the fix by the same reviewer `reports/review-fix-report.md` `PASS ee6126cd7899630918d1e3b07dbfd18df5150904`, no blocking finding remained
- Weakest-point checks: the one author — requirement "a junction is recognised at every directory-level site, the removal of stale entries and `.the-way` included": `grep is_symlink` before and after, one crafted case for each place, 18 subtests failing before the fix (`reports/author-report.md`); after the review, the new direct test of the scans found one more site (`.claude`/`.agents` themselves in `stale_entry_points`) and the fix closed it (`reports/author-fix-report.md`).

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

One-author route: no slices.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-14T01:50 | start | orchestrator | task document, `task-cycle/skill/SKILL.md` | worktree `.runs/worktrees/installer-junction-refusal` on `6fa755c` | route chosen: one author |
| 2026-11-14T01:53 | gate on base | orchestrator, `gate_times.py` in `.runs/base-check` | base `6fa755c` is a merge whose tree (5084aba) differs from its second parent's (2d086b4), so the gate runs on the base | `base-gate.log`, `base-gate.exit`, `gate_times.md` | exit 0, 1267 tests in 10 directories, none failing; next: dispatch the author |
| 2026-11-14T02:10 | author | `the-way-author`, sonnet (class `same`) | `reports/author-handoff.md`, `make-change` (the whole change as the one author), frozen `task.md` | `reports/author-report.md` | dispatched in background; waits by completion notification |
| 2026-11-14T02:40 | author return | orchestrator | `reports/author-report.md` | status `done`; commits `54ed53c`, `474df77` | mechanical check: worktree clean, range `6fa755c..474df77` non-empty, five files changed (install.py, test_install.py, test_agent_types_installation.py, README.md, invariants.md); report holds checks with command and exit code (failing run before fix 18 subtests, passing run after, directory run 59 tests exit 0, foundation_check both forms exit 0), own-work check, **Unread material** and **Searches**. Author left three junction checks without a test (named in report). Next: review of the whole change |
| 2026-11-14T02:45 | whole-change review | `the-way-stage`, sonnet (class `same`, none cheaper than the orchestrator) | `reports/review-whole-handoff.md`, `review-change` (whole change), range `6fa755c..474df77`, frozen task, author report | `reports/review-whole-report.md` | dispatched; waits by completion notification |
| 2026-11-14T03:05 | whole-change review return | orchestrator | `reports/review-whole-report.md` | `FAIL 474df77904b199e3ba1acb438c5a88c9a47d13c1`; 1 blocking (invariant broader than code: git writes through a junction at `.git/modules`), Minor 2-6 within the task, Minor 7 out of scope; changed files by line counts: install.py +11/-5, test_install.py +94, README +9/-2, invariants.md +10, test_agent_types_installation.py +2 | one fix for the blocking and the Minor findings within the task; findings file `reports/whole-review-findings.md` |
| 2026-11-14T03:15 | fix | `the-way-author` resumed, sonnet (class `same`) | `reports/author-fix-handoff.md`, findings `reports/whole-review-findings.md`, `make-change` (the fix of a review's findings) | `reports/author-fix-report.md` | dispatched |
| 2026-11-14T03:45 | fix return | orchestrator | `reports/author-fix-report.md` | status `done`; commits `62ec7c1`, `ee6126c`; mechanical check: clean worktree, range `474df77..ee6126c` non-empty, five files changed; checks with command and exit code (directory run 60 tests exit 0, foundation_check exit 0); report names one code change beyond the findings (`stale_entry_points` also checks `.claude`/`.agents`) and a mismatch of the line count of `test_install.py` (+41 reported, +37 by `git diff --stat`), both passed to the review of the fix | review of the fix |
| 2026-11-14T03:50 | review of the fix | `the-way-stage` resumed (same reviewer), sonnet | `reports/review-fix-handoff.md`, findings `reports/whole-review-findings.md`, range `474df77..ee6126c`, fix report | `reports/review-fix-report.md` | dispatched |
| 2026-11-14T04:10 | review of the fix return | orchestrator | `reports/review-fix-report.md` | `PASS ee6126cd7899630918d1e3b07dbfd18df5150904`; all six findings fixed, no new Critical/Important; Minor notes A (hole of git's writes under `.git` stated only in the author's report), B (`os.path.isjunction` vs `Path.is_junction`), C (line count +41 vs +37 in the author's report) go to the request's list | return step |
| 2026-11-14T04:15 | return step | `the-way-author` resumed, sonnet (class `same`) | `reports/author-return-handoff.md`, `task-cycle/skill/return_step.md` | `reports/author-return-report.md` | dispatched |
| 2026-11-14T04:40 | return step return | orchestrator | `reports/author-return-report.md` | status `done`; commit `e899494` (environment fact `python-junction-detection` restated for `Path.is_junction`, +2/-2); no decision, glossary term or part-map change; README note A not made | review of the return step by a fresh reviewer |
| 2026-11-14T04:45 | review of the return step | `the-way-stage`, sonnet (fresh) | `reports/review-return-handoff.md`, range `ee6126c..e899494`, return report | `reports/review-return-report.md` | dispatched |
| 2026-11-14T05:20 | review of the return step return | orchestrator | `reports/review-return-report.md` | `PASS e899494ac7d7a860f56af738694753b0d7257524`; blocking 0, Minor 0; reviewer left unread the README, the part map entries `installation`/`installation-command`, WAY-73, WAY-80 and the glossary and read the first 150 lines of `elements/common/rules.md` (autonomous choice Q6: it bears on nothing a two-line change to a fact needed) | gate on the final tree |
| 2026-11-14T05:25 | gate on the final tree `e899494` | orchestrator, `gate_times.py` | `final-gate.log`, `final-gate.exit`, `gate_times.md` | exit 1; 1271 tests in 10 directories, failed: `elements/part-map` (`test_the_way_imports_only_from_allowed_parts`: `installation/test_install.py:800` and `:819` run a file the check cannot work out); other nine directories passed; passes on the base | fix of the failure by the author |
| 2026-11-14T05:30 | fix of the gate failure | `the-way-author` resumed, sonnet (class `same`) | `reports/author-gatefix-handoff.md` | `reports/author-gatefix-report.md` | dispatched |
| 2026-11-14T05:50 | gate-fix return | orchestrator | `reports/author-gatefix-report.md` | status `done`; commit `a6ddd8c` (`installation/test_install.py`, +16/-11; helper `empty_product` replaces the `self.product` assignment of `another_product`; `make_writable` moved to module level); `elements/part-map` passes (exit 0, 39 tests); mechanical check: clean worktree, non-empty range | review of the fix by the reviewer of the return step; rerun of the gate on `a6ddd8c` started at the same time (first failed run kept as `final-gate-1-failed.log`) |
| 2026-11-14T05:55 | review of the gate fix | `the-way-stage` resumed (reviewer of the return step), sonnet | `reports/review-gatefix-handoff.md`, range `e899494..a6ddd8c` | `reports/review-gatefix-report.md` | dispatched |
| 2026-11-14T05:55 | return step over the gate fix's range | `the-way-author` resumed, sonnet | message naming `task-cycle/skill/return_step.md` and range `e899494..a6ddd8c` | `reports/author-return2-report.md` | dispatched |
| 2026-11-14T06:10 | gate-fix review and second return comparison | orchestrator | `reports/review-gatefix-report.md`, `reports/author-return2-report.md` | `PASS a6ddd8ca313ce3528534db7c1d54d9ef98740c78` (zero findings; `shutil.rmtree` of Python 3.14.3 removes a junction without following it, 22 resets left the outside folders unchanged); the return step over `e899494..a6ddd8c`: nothing to change, no commit | gate again |
| 2026-11-14T06:12 | gate run 2 on `a6ddd8c`, started while the review of the gate fix ran on the same machine | orchestrator, `gate_times.py` | `final-gate-2-failed.log` | exit 1; 1274 tests in 10 directories, failed `gate`: `test_by_default_every_directory_runs_at_the_same_time` (three directories did not meet within 120 s); does not touch the change | rerun with the machine idle |
| 2026-11-14T06:30 | gate run 3 on `a6ddd8c`, machine idle | orchestrator, `gate_times.py` | `final-gate.log`, `final-gate.exit` | exit 0; 1271 tests in 10 directories, every directory passed | request |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | Author's class of model | `same` | change touches a trust boundary and writes an invariant | `cheaper` (default) | a weaker agent may write a gap in a refusal or an invariant not in the template's form; caught by the reviews | author |
| Q2 | The author's **Unread material**: `foundations/invariants.md` lines 16-100 and 199-255 unread, including the example `return-step-record` | Autonomous choice: the gap bears on nothing the author judged beyond the form of the new entry, which `foundation_check.py` passes; carried to the whole-change reviewer, who reads the invariants whole | author report, section Unread material | resuming the author to read it | an entry of a wrong form; the reviewer reads the template and the entry | whole-change review |
| Q3 | The author's concerns 1 (`Rests on: none`) and 2 (part map `installation-command` unedited) | Carried to the whole-change reviewer to judge; no answer given by the orchestrator | author report, Questions and concerns | answering from memory | an invariant without a platform fact it should rest on, or a promise to products left unwritten | whole-change review |
| Q4 | Fix of blocking finding 1: narrow the sentence, or add a check of `.git`/`.git/modules` | Narrow the sentence to the installer's own code (reviewer's first way) | review finding 1 and 7; task item 1 asks for refusal on the path of a file the installer writes | adding a check to `plan` — widens the task, reviewer holds it out of scope | the human may want git's writes refused too: a new task | fix |
| Q5 | Minor 4, `Rests on` for a Windows junction | Write an environment fact through its skill from the Python 3.14 documentation; if the skill's rules cannot be met, leave `none` | review finding 4 names this as the cycle's choice; WAY-80 forbids a fact from memory | leaving `none` with no attempt | one more entry the human accepts at the merge | fix |
| Q6 | Unread material of the review of the return step (README, part map entries, WAY-73, WAY-80, glossary; `rules.md` read in part) | Autonomous choice: bears on nothing it judged — the commit changes two lines of one environment fact | review-return-report, Unread material | resuming the reviewer to read it | a defect in the fact the reviewer missed; the fact was also read by the return step's author and checked by the whole-change reviewer's fix review | request |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| Frozen task | `task.md` beside this record | orchestrator | n/a |
| Code commits | `54ed53c` (installer, tests, README), `474df77` (invariant `installation-paths-through-links`), `62ec7c1` (test of the scans, `stale_entry_points` checks `.claude`/`.agents`, README), `ee6126c` (invariant narrowed to the installer's own code; environment fact `python-junction-detection`), `e899494` (return step: the fact restated for `Path.is_junction`), `a6ddd8c` (gate fix: test helper) | the-way-author | `FAIL 474df77` then `PASS ee6126c`; return `PASS e899494`; gate fix `PASS a6ddd8c` |
| Author reports | `reports/author-report.md`, `reports/author-fix-report.md`, `reports/author-return-report.md`, `reports/author-gatefix-report.md`, `reports/author-return2-report.md` | the-way-author | see above |
| Review reports | `reports/review-whole-report.md`, `reports/review-fix-report.md`, `reports/review-return-report.md`, `reports/review-gatefix-report.md` | the-way-stage | see above |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| `python -B task-cycle/gate_times.py --output ../task-cycles/installer-junction-refusal/gate_times.md -- python -B gate/run_tests.py` | orchestrator, base `6fa755c`, checkout `.runs/base-check`, Windows | exit 0; 1267 tests in 10 directories, every directory passed (`base-gate.log`) | none failing on the base |
| gate command as above | orchestrator, tree `e899494`, Windows | exit 1; 1271 tests in 10 directories; failed `elements/part-map` (`test_the_way_imports_only_from_allowed_parts`: `installation/test_install.py:800`, `:819` run a file the check cannot work out) — the author's new helper assigned `self.product` a second value (`final-gate-1-failed.log`) | failed; fixed by `a6ddd8c`; `python -B gate/run_tests.py elements/part-map` on `a6ddd8c`: exit 0, 39 tests (author and reviewer) |
| gate command as above | orchestrator, tree `a6ddd8c`, Windows, while the review of the gate fix ran tests on the same machine | exit 1; 1274 tests in 10 directories; failed `gate` (`test_by_default_every_directory_runs_at_the_same_time`, the three trial directories did not meet within 120 s) (`final-gate-2-failed.log`) | failed; a test of a part outside the task's parts; the cause is unproven — the run overlapped with other test runs of the cycle |
| gate command as above | orchestrator, tree `a6ddd8c`, Windows, machine idle | exit 0; 1271 tests in 10 directories, every directory passed (`final-gate.log`) | none |
| `python -B elements/common/foundation_check.py` | author, reviewers, on the head after each commit | exit 0, `0 errors` | none |
| `python -B gate/run_tests.py installation` | author, tree `ee6126c` | exit 0, 60 tests, the three junction tests not skipped | none |
| invariant test, seen failing once | author, `python -B -m unittest installation.test_install -k junction -k stale_entry` on the base code, then after the fix | exit 1, 18 failing subtests, then exit 0, 3 tests | none |

## Return step

- Foundation compared with code: the invariant `installation-paths-through-links` against `install.py` and the tests; the environment fact `python-junction-detection` against the call `Path.is_junction` (it quoted `os.path.isjunction`: corrected in `e899494`, quotation checked against the live page and its archived copy by the author and by the reviewer); WAY-48, WAY-13, WAY-38, WAY-328, WAY-235, WAY-34, WAY-141, WAY-368; the part map entries `installation`, `invariants`, `environment-facts` and the surface `installation-command` (not widened, the orchestrator's ruling; no change); the range `e899494..a6ddd8c` compared again, nothing to change. Review: `reports/review-return-report.md` `PASS e899494`.
- Decisions written or changed: none (the choice that removal skips and writing refuses stays a row of the questions table; the reasons are in `reports/author-return-report.md`)
- Invariants written or changed: `installation-paths-through-links`, set by row 1 of the task's *Settlements to record* (questions 1 and 2 of the task)
- Environment facts: `python-junction-detection` (Python 3.14 documentation of `Path.is_junction`), marked `the cycle's`
- Glossary terms: none
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: row 1, `installation-paths-through-links`

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/117, draft until the record's link is added, then ready for review
- Description: `request.md` beside this record, written by `task-cycle/skill/request_template.md`; form check `python -B task-cycle/request_check.py .runs/task-cycles/installer-junction-refusal/request.md --task .runs/task-cycles/installer-junction-refusal/task.md` exit 0 (1 run), check of private paths `python -B task-cycle/private_paths_check.py .runs/task-cycles/installer-junction-refusal/request.md` exit 0 (1 run); in this copy the description is written and checked, and is rewritten after this commit with the record's link and the runs of the three checks on the copy (written and checked after this commit). The reminder of a review of the foundation: `python -B task-cycle/review_reminder.py origin/foundations`: tag `foundation-review/2026-11-06`, merges 39, threshold 30, `reminder: yes`.
- Writes to the task's backlog entry: the request link added to the task's line and its state moved from Ready to Selected (the entry `tasks` under `the-way` in the locations file)
- Corrections after the request opened: none
- Process remarks on the-way:
  - fix, .runs/task-cycles/installer-junction-refusal/reports/author-fix-report.md: None that matter. The reviewer's `crafted.py` of case B is in a scratchpad I did not open.
  - author, .runs/task-cycles/installer-junction-refusal/reports/author-report.md: No environment fact for what a Windows junction is, and no instruction that says whether `Rests on` of this invariant must name one (see concerns). Searched `foundations/environment_facts.md` for `junction`: no hit.
  - author, .runs/task-cycles/installer-junction-refusal/reports/author-report.md: The handoff says "`test_agent_types_installation.py:263`" shows an existing symlink test form; at this base commit the test is at line 255-264 (the `link` helper at 247). No effect.
  - review of the fix, .runs/task-cycles/installer-junction-refusal/reports/review-fix-report.md: None. (The `isjunction` page text was found in both copies; no glossary entry for "junction" exists, as before, and no sentence is read wrongly for lack of it.)
  - whole-change review, .runs/task-cycles/installer-junction-refusal/reports/review-whole-report.md: Glossary entry or environment fact for "Windows junction": searched `foundations/glossary.md` and `foundations/environment_facts.md` for `junction`, `symlink`, `symbolic`: no entry (the same as the author found). No finding for the glossary: no sentence is read wrongly for lack of it.
  - whole-change review, .runs/task-cycles/installer-junction-refusal/reports/review-whole-report.md: Whether `instruction-files` is "a part of test helpers" under `cross-part-imports`: not looked up; it matters only for the helper copy and I do not dispute it.
  - whole-change review, .runs/task-cycles/installer-junction-refusal/reports/review-whole-report.md: The author's report says `installation/README.md` is +9 / -2; the diff shows +9 / -2 (11 lines in `--stat`); consistent.
  - the orchestrator: the gate's test `test_by_default_every_directory_runs_at_the_same_time` (`gate/test_run_tests.py`) waits 120 seconds for three trial directories to start together and failed once, on a run that overlapped with another test run of the cycle on the same machine; it passed on the base, on the first run of the final code and on a rerun with the machine idle. The cycle started a gate run while a review ran tests, which the skill's step 10 orders after the reviews; the cause of the failure is not proven.

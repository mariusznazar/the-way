# Cycle record — Show on the example of loop2 how to prepare the deployment instruction of the next product

- Task source: the task document in the author's backlog (`_zadania` folder of the-way tasks), approved with its settlements 2026-11-14; working copy `.runs/task-cycles/deployment-skill-guide/task.md`. Original path: the task's note in the author's backlog
- Task relation: independent
- Product repository: github.com/mariusznazar/the-way
- Process pin: none (the-way itself)
- Target branch and base: `foundations`, `d40d1cb942c4fbaddb7ece1dc6d472d15cd83430`
- Task branch: `task/deployment-skill-guide`
- Status: request open

## Two questions at start

- Trust boundary: no — the change edits `project-level/task/skill/resolve_gaps.md`, adds a file in `project-level/task/` and edits WAY-139 in `foundations/decisions.md`; none is one of the part map's boundary files of `project-level` (`readiness_check.py`, `plan_check.py`, `plan_state.py`).
- Irreversible operation: no.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none — both rows of *Settlements to record* settle where the guide lies, how it is reached and how loop2 is shown; the file name is the cycle's (task To do 1).
- Reserved choice: none
- Execution route and reason: one author without a plan; one new prose file and two small edits, one agent holds it.
- Author: `the-way-author`, class `same` as the orchestrator, model sonnet; reason for a class other than `cheaper`: the guide's value is separating the general from loop2's own, and a leaked real address would go into a public repository. Resumptions: none yet.
- Plan: none
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: native completion notification (Claude Code background agent).
- Whole-change review: `the-way-stage` (sonnet), `review-change`, range `d40d1cb..a900916` (head `a900916e8980eaf6d913e2c8bd0b6cbd212deb21`), report `reports/review-whole-report.md`, first line `FAIL a900916e8980eaf6d913e2c8bd0b6cbd212deb21`; changed files: `foundations/decisions.md` +32 -6, `project-level/task/deployment_skill_guide.md` +336, `project-level/task/skill/resolve_gaps.md` +5 -1; coverage of every To do item 1-7 and both settlement rows checked item by item in the report, source fidelity read against loop2 at the one commit, privacy searched in the loop2 files and the changed text; 2 Important findings (I1, I2), 4 Minor within the task (M1-M4), 1 Minor outside the task (M5); read 12 decisions whole, 67 by title only. After the fix: same reviewer, range `a900916..4e60278`, `reports/review-fix-report.md`, first line `PASS 4e60278098e8e83504e1ae145e18b23986ac47f4`.
- Review rounds:
  - correction 1 (the human's remarks `reports/correction-1-remarks.md`, in place of a findings file): one change by the resumed author, `31120e9..aa21be7`, report `reports/author-correction-report.md`; review by the same reviewer `reports/review-correction-report.md`, first line `PASS aa21be7fa4aa23ab64dd0c7b701967f371c2fe74`, no new Critical or Important finding; the reconciliation with the target branch (merge `dc18abf`) reviewed by a fresh reviewer `reports/review-merge-report.md`, `PASS dc18abf32122d3f7466d629edbe904d0e8182cd0`, two Minor findings left for the request's list; the second merge (`dd91dd2`) touched none of the change's files and none of the entries it bears on, so it had no review of its own.
  - findings `reports/review-whole-findings.md`: whole-change review of `a900916` blocked with I1 and I2 (Important) and carried M1-M4 (Minor within the task); one fix by the resumed author, range `a900916..4e60278`, report `reports/author-fix-report.md`; the same reviewer reviewed the fix once: PASS, no new Critical or Important finding, two new Minor findings (N1, N2) left for the request's list; no blocking finding remained.
- Weakest-point checks: author, first report: requirement 'nothing of loop2's own unmarked, every fragment a true excerpt, no real address'; check: search for the strings and a script comparing each quotation with the loop2 files; showed 11 explained differences and no leak (`reports/author-report.md`); the review found a cut clause the script had explained away (I2). Author, fix report: the same requirement for the fix, same script, same result (`reports/author-fix-report.md`). Reviewer: privacy search of the loop2 files and the changed text, found none in the changed text (`reports/review-whole-report.md`, `reports/review-fix-report.md`).

## Slices

Not used (one-author route).

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 04:40 | start | orchestrator, sonnet | fast-forward of the checkout from `5a24ac9` to `d40d1cb`; worktree `.runs/worktrees/deployment-skill-guide`; base is a merge commit with tree equal to its second parent's | — | no gate on the base; list taken from the record of the merged branch |
| 04:55 | one author | `the-way-author`, sonnet | `reports/author-handoff.md`, `make-change`, whole change as the one author | `reports/author-report.md`, commit `a900916` | done; checks with command and exit code, own-work check, Unread material and Searches present; mechanical check: clean worktree, range `d40d1cb..a900916` non-empty, three files all within the task |
| 05:10 | whole-change review | `the-way-stage`, sonnet | `reports/review-whole-handoff.md`, `review-change`, range `d40d1cb..a900916` | `reports/review-whole-report.md` | dispatched (event written just after the dispatch); the author's unread loop2 ranges and the tail of WAY-140 carried into the handoff |
| 05:25 | whole-change review result | `the-way-stage`, sonnet | report read for checks, unread material, searches | `reports/review-whole-report.md` | `FAIL a900916e8980eaf6d913e2c8bd0b6cbd212deb21`: 2 Important (I1, I2), 4 Minor within the task (M1-M4), 1 Minor outside the task (M5); findings file `reports/review-whole-findings.md` written from the report's words |
| 05:30 | fix | `the-way-author`, sonnet, resumed | `reports/fix-handoff.md`, `make-change`, the fix of a review's findings, `reports/review-whole-findings.md` | `reports/author-fix-report.md` | dispatched |
| 05:45 | fix result | `the-way-author`, sonnet, resumed | report read for checks with command and exit code, Unread material, Searches, own-work check | `reports/author-fix-report.md`, commit `4e60278` | done; all six findings fixed, none contested; mechanical check: clean worktree, range `a900916..4e60278` non-empty, two files changed, both inside the original change |
| 05:50 | review of the fix | `the-way-stage`, sonnet, the same reviewer resumed | findings file `reports/review-whole-findings.md`, fix report | `reports/review-fix-report.md` | dispatched |
| 06:10 | review of the fix result | `the-way-stage`, sonnet | first line read, the report's checks, unread material, searches | `reports/review-fix-report.md` | `PASS 4e60278098e8e83504e1ae145e18b23986ac47f4`; two new Minor findings (N1, N2) go to the request's list, not fixed |
| 06:15 | return step | `the-way-author`, sonnet, resumed | `reports/author-return-handoff.md`, `task-cycle/skill/return_step.md`, `foundation_step.md` | `reports/author-return-report.md` | dispatched |
| 06:20 | return step result | `the-way-author`, sonnet, resumed | report read | `reports/author-return-report.md` | done, no commit, no correction, no new entry; no review of it |
| 06:25 | gate | orchestrator | `python -B task-cycle/gate_times.py ... -- python -B gate/run_tests.py` on `4e60278` | `final-gate.log`, `gate_times.md` | exit 0, 1271 tests in 10 directories; the remote target branch had not moved (`d40d1cb`), no merge |
| 06:45 | measures | orchestrator | `cycle_stages.py`, `cycle_measures.py`, `review_reminder.py` | `stages.md`, `mechanism_measures.md` | exit 0 each; reminder: yes |
| 06:55 | request | orchestrator | `request_check.py`, `private_paths_check.py` on `request.md` | `request.md` | both exit 0 |
| 07:15 | correction 1 | orchestrator | request link read; comment `issuecomment-6872066189` on the request; remote target branch unchanged (`d40d1cb`), nothing merged; *Reserved choice* is `none` | `reports/correction-1-remarks.md` | remarks recorded word for word: fix the first two minor findings, make a task of the WAY-09 list gap (via `/park` after the correction), let the review's reading gap through, items 3-6 accepted |
| 07:20 | correction 1 | `the-way-author`, sonnet, resumed | `reports/correction-1-handoff.md`, `make-change`, a correction for the human's remarks | `reports/author-correction-report.md` | dispatched |
| 07:30 | correction 1 result | `the-way-author`, sonnet, resumed | report read: checks with command and exit code, Unread material, Searches (none), own-work check | `reports/author-correction-report.md`, commit `aa21be7` | done; clean worktree; range `31120e9..aa21be7` is one file, the guide, two places |
| 07:35 | review of the correction | `the-way-stage`, sonnet, the same reviewer resumed | the remarks `reports/correction-1-remarks.md` in place of a findings file; range `31120e9..aa21be7`; `reports/author-correction-report.md` | `reports/review-correction-report.md` | dispatched |
| 08:15 | review of the correction result | `the-way-stage`, sonnet, resumed | first line, checks, unread material, searches read | `reports/review-correction-report.md` | `PASS aa21be7fa4aa23ab64dd0c7b701967f371c2fe74`, no new Critical or Important finding; the reviewer's own run of the part's tests was lost (no result, no notification; its row in the report still reads the placeholder), so the orchestrator ran the same command itself, alone: exit 0, 275 tests (`project-level-tests-correction.log`) |
| 08:25 | return step for the correction | orchestrator | not run | — | the remarks touch two sentences of the guide that no entry states; WAY-139 names neither the automation nor the 60 days, so there is nothing for the return step to compare or correct |
| 08:26 | gate | orchestrator | `python -B task-cycle/gate_times.py ... -- python -B gate/run_tests.py --jobs 4` on `aa21be7` (fewer directories at once, since the machine was out of memory earlier) | `final-gate-correction.log`, `gate_times.md` | started |
| 09:10 | gate result | orchestrator | `final-gate-correction.log` | `gate_times.md` | exit 0, 1271 tests in 10 directories on `aa21be7` (`--jobs 4`, one run); then the remote target branch had moved from `d40d1cb` to `0e1cd3c`: merged into the task branch, merge commit `dc18abf`, no conflict, `foundation_check.py` 0 errors; the merge changes the decision log, the decisions template, the request and record templates, so it is reviewed and the gate is rerun on the merged tree |
| 09:15 | review of the merge | `the-way-stage`, sonnet, fresh | `reports/review-merge-handoff.md`, `review-change`, the reconciliation with the target branch, `aa21be7` to `dc18abf`; entries brought in: WAY-02, 03, 05, 11, 12, 17, 19, 22, 115, 134, 167, 168, 171, 172, 241, 293 | `reports/review-merge-report.md` | dispatched |
| 09:40 | review of the merge result | `the-way-stage`, sonnet, fresh | first line, checks, unread material, searches read | `reports/review-merge-report.md` | `PASS dc18abf32122d3f7466d629edbe904d0e8182cd0`; 2 Minor findings (not fixed, to the request's list); it ran no test and says so |
| 09:45 | gate on the merged tree | orchestrator | `gate_times.py ... -- python -B gate/run_tests.py --jobs 4` on `dc18abf` | `final-gate-merged.log` | exit 0, 1326 tests in 10 directories; `foundation_check.py` without `--skip-test-citations`: exit 0, 0 errors, no `listed:` line |
| 10:10 | merge of the target branch again | orchestrator | `origin/foundations` moved to `0b77f5a`; merge commit `dd91dd2`, no conflict, `foundation_check.py` 0 errors; entries it changed: WAY-35, WAY-60, WAY-80, WAY-84 (an element skill's content, the place of an invariant's condition, an environment fact's source and a setting changed outside the repository) | — | none bears on the deployment skill, the guide or WAY-139, and none of our three files changed (`git diff --numstat 0b77f5a HEAD` shows only ours), so no review of this merge was dispatched; the gate is run again on this tree |
| 10:35 | gate on the final tree | orchestrator | `gate_times.py ... -- python -B gate/run_tests.py --jobs 4` on `dd91dd2` | `final-gate-merged-2.log`, `gate-dir-diagnosis.log`, `gate_times.md` | exit 1, 1331 tests in 10 directories; failed: directory `gate`, `test_a_number_of_jobs_limits_the_directories_that_run_at_once` (a trial directory did not meet the others within 120 s); diagnosis `python -B gate/run_tests.py gate` exit 0, 36 tests in 18 s; the same test failed in run 1 of the gate of the merged branch's cycle that supplies the list of failing tests (Verification); no further gate run to make it pass (WAY-243) |
| 10:40 | measures | orchestrator | `cycle_stages.py`, `cycle_measures.py`, `review_reminder.py` after the correction | `stages.md`, `mechanism_measures.md` | exit 0 each; merges 43, `reminder: yes` |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | Which loop2 commit do the fragments come from? The task's *Context* names `main` at `6ab6a32b` (2026-11-14); `origin/main` has moved | `e54f23c0ea3bd1db13d2635333417eb50412d6a0`, tip of loop2 `origin/main` at the cycle's start, which holds the skill and its three `references/` files | `git ls-tree` of that commit; `gh repo view` says the repository is public | `6ab6a32b`, the commit named as context: it is a state of the day, not a requirement of the task, and the skill may have changed since | a fragment may differ from the later skill; the link names the commit, so it stays true | author handoff |
| Q3 | The author's report says it read parts of loop2's `references/` and the tail of WAY-140's *Rationale* not at all; does the gap matter? | Carried into the review's handoff: the reviewer reads what it needs itself | `reports/author-report.md` *Unread material* | resume the author to read them: the fragments come from ranges it read, so little is gained | a missed loop2 passage that bears on a part would show only at the review | whole-change review |
| Q2 | Class of the author | `same` | task is prose whose value lies in judgment about what is general; leak of real addresses is the risk | `cheaper` (the default) | a weaker model might copy loop2 specifics unmarked; the reviews would catch it, at the price of a fix round | author |
| Q4 | Wording of the refusal and the "no notice" answers in parts 7 and 8 | The guide's own wording, labelled as written for the guide | loop2 settled both items and has no such passage; author report, choice 4 | invent a loop2 fragment | none for a product; the wording binds nothing | author |
| Q5 | How to treat loop2's exception "except deployment started by the existing automation" in part 5 | Quote the whole sentence with the exception marked as loop2's and add one paragraph on automation as a third actor | review finding I2; `reports/review-whole-findings.md` | cut the exception (the author's first choice) | one paragraph the human may not want, removable alone | fix |
| Q6 | What "a preview of deployments" means | Both: seeing what runs and what a deployment did, and trying a change on the server before the main line; the guide says so | the list gives no definition; author report, choice 1; review M4 | a per-branch preview environment only | part 2's questions would need a change; other parts do not depend on it | author, fix |
| Q7 | After correction 1, is the return step repeated? | No: the remarks touch two sentences of the guide that no entry states | WAY-139 names neither the automation nor the 60 days; `reports/author-correction-report.md` | repeat it (about a minute of the author) | a changed sentence that an entry quotes would go unseen; none quotes these | correction 1 |
| Q8 | The target branch moved a second time during the correction: is the second merge reviewed, and the gate rerun? | Gate rerun (it is the rule); no separate review: the merge changed none of the change's files and entries on a deployment skill, the guide, logs or failures were not among the four it changed (WAY-35, WAY-60, WAY-80, WAY-84) | `git diff --numstat 0b77f5a HEAD`; the headings of the changed hunks | review the merge once more | an interaction the first merge's review did not cover would go unseen | correction 1 |
| Q9 | The machine ran out of memory earlier: how many directories does the gate run at once? | `--jobs 4`, a documented option of the declared gate command | `agent-instructions/README.md` | the default (ten at once) | a different timing of the one flaky timing test | correction 1 |


## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| Frozen task | `.runs/task-cycles/deployment-skill-guide/task.md` | orchestrator | — |
| Code and foundation entry | commit `a900916` | the-way-author | FAIL (review of the whole change) |
| Fix | commit `4e60278` | the-way-author | PASS (review of the fix) |
| Correction | commit `aa21be7` | the-way-author | PASS (review of the correction) |
| Merges with the target branch | `dc18abf` (PASS, review of the merge), `dd91dd2` (no review: see Q8) | orchestrator | — |
| Reports | `reports/author-report.md`, `review-whole-report.md`, `author-fix-report.md`, `review-fix-report.md`, `author-return-report.md` | agents as named | — |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| gate on the base | not run: `d40d1cb` is a merge commit whose tree equals the tree of the head `0f66409`-side branch (`git rev-parse` of both print `7c4593e79bded6ddc86328661a2fff920f37fb5f`); list taken from the final gate of the branch `oversized-plan-tasks`: `docs/task-cycles/oversized-plan-tasks/cycle.md` in the commit `0f66409` | final gate of that cycle: exit 0 on run 2, 1271 tests in 10 directories; run 1 exit 1 on `gate`, `test_a_number_of_jobs_limits_the_directories_that_run_at_once` (a trial directory did not meet the others within 120 s, passed on diagnosis) | no test failing before the change; one test known flaky |
| `python -B task-cycle/gate_times.py --output .runs/task-cycles/deployment-skill-guide/gate_times.md -- python -B gate/run_tests.py` | orchestrator, `4e60278`, Windows | exit 0; 1271 tests in 10 directories, every directory passed (`final-gate.log`, `final-gate.exit`); one run | none |
| `python -B elements/common/foundation_check.py` | author, reviewers, each head | exit 0, `0 errors` | none |
| `python -B -m unittest discover -s project-level -p "test_*.py"` | author on both heads, reviewers | exit 0, 275 tests | none |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator | exit 0; tag `foundation-review/2026-11-06`, merges 41, threshold 30, `reminder: yes` | none |
| `python -B task-cycle/cycle_stages.py`, `python -B task-cycle/cycle_measures.py` | orchestrator | exit 0, exit 0 | none |
| `python -B task-cycle/request_check.py .runs/task-cycles/deployment-skill-guide/request.md --task .runs/task-cycles/deployment-skill-guide/task.md` | orchestrator | exit 0 (2 runs) | none |
| `python -B task-cycle/private_paths_check.py .runs/task-cycles/deployment-skill-guide/request.md` | orchestrator | exit 0, 1 file, 0 listed (2 runs) | none |
| `python -B -m unittest discover -s project-level -p "test_*.py"` alone, correction head | orchestrator, `aa21be7`, Windows (the reviewer's own run of it was lost) | exit 0, 275 tests (`project-level-tests-correction.log`) | none |
| gate with `--jobs 4`, on the correction head | orchestrator, `aa21be7`, Windows | exit 0, 1271 tests in 10 directories (`final-gate-correction.log`) | none |
| gate with `--jobs 4`, on the tree merged with the target branch | orchestrator, `dc18abf`, Windows | exit 0, 1326 tests in 10 directories (`final-gate-merged.log`) | none |
| gate with `--jobs 4`, on the final tree | orchestrator, `dd91dd2`, Windows | exit 1, 1331 tests in 10 directories (`final-gate-merged-2.log`) | failed: directory `gate`, `test_a_number_of_jobs_limits_the_directories_that_run_at_once` (a trial directory did not meet the others within 120 s); the same test failed in run 1 of the gate of the cycle that supplies the list of failing tests, so it is known flaky and outside the task's parts; across this correction's three gate runs it failed in 1 and passed in 2 |
| `python -B gate/run_tests.py gate` | orchestrator, `dd91dd2` | exit 0, 36 tests in 18 s (`gate-dir-diagnosis.log`) | none; diagnosis only |
| `python -B elements/common/foundation_check.py` (no `--skip-test-citations`) | orchestrator, `dd91dd2` | exit 0, `0 errors`, no `listed:` line | none |
| `python -B task-cycle/cycle_stages.py`, `cycle_measures.py`, `review_reminder.py origin/foundations` | orchestrator, after the correction | exit 0, 0, 0; merges 43, `reminder: yes` | none |


## Return step

- Foundation compared with code: WAY-139 (edited by the change), WAY-09, WAY-140, WAY-165, WAY-270 and the part map entry `project-level` against the guide, `resolve_gaps.md` and the files; nothing no longer matched, nothing corrected (`reports/author-return-report.md`)
- Decisions written or changed: WAY-139, edited in place (WAY-07)
- Invariants written or changed: none
- Environment facts: none (no decision rests on how loop2's skill behaves)
- Glossary terms: none
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: row 1 and row 2, both by the edit of WAY-139 (no second entry)

The return step committed nothing, so no review of it ran. After correction 1 the return step was not repeated: the remarks touch two sentences of the guide that no entry states.

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/119, ready for review; description rewritten for correction 1
- Description: `request.md` beside this record, written by `task-cycle/skill/request_template.md`; form check `python -B task-cycle/request_check.py .runs/task-cycles/deployment-skill-guide/request.md --task .runs/task-cycles/deployment-skill-guide/task.md` exit 0 (2 runs), check of private paths `python -B task-cycle/private_paths_check.py .runs/task-cycles/deployment-skill-guide/request.md` exit 0 (2 runs); written and checked after this commit (rewritten with the record's link and the runs of the three checks on the copy). The reminder of a review of the foundation: `python -B task-cycle/review_reminder.py origin/foundations`: tag `foundation-review/2026-11-06`, merges 41, threshold 30, `reminder: yes`.
- Writes to the task's backlog entry: the request link added to the task's line and its state moved, as the task rules of the author's backlog give (the entry `tasks` under `the-way` in the locations file); done after the request opened
- Corrections after the request opened:
  - correction 1, remarks `reports/correction-1-remarks.md`: `item 8 · not-required`
- Process remarks on the-way:
  - one author, .runs/task-cycles/deployment-skill-guide/reports/author-report.md: The meaning of "a preview of deployments" in WAY-139: not defined in the entry or in the task; chosen as in choice 1.
  - one author, .runs/task-cycles/deployment-skill-guide/reports/author-report.md: A loop2 passage for the human's refusal of an item, or for a deliberate absence of a notice: none exists (loop2 settled both), so parts 7 and 8 carry wording of the guide.
  - return step, .runs/task-cycles/deployment-skill-guide/reports/author-return-report.md: none. (The meaning of "a preview of deployments" in WAY-139, which the first report noted as undefined, stays so; the guide says that it reads it as both of two things.)
  - review of the fix, .runs/task-cycles/deployment-skill-guide/reports/review-fix-report.md: none new. The unresolved question from the first review (whether the human wants the third-actor paragraph at all) stays with the human; the author notes it is one paragraph to drop.
  - whole-change review, .runs/task-cycles/deployment-skill-guide/reports/review-whole-report.md: The meaning of "a preview of deployments" in WAY-139: no definition in the decision, the task, the glossary or my grep of the repository (`preview of deployments` appears only in WAY-139 and the guide). Unclear; see M4.
  - whole-change review, .runs/task-cycles/deployment-skill-guide/reports/review-whole-report.md: A loop2 passage for the human's refusal of an item or for a deliberate absence of a notice: none exists, as the author reports; the guide's wording for both is labelled as its own and I accept that.
  - whole-change review, .runs/task-cycles/deployment-skill-guide/reports/review-whole-report.md: A statement in WAY-09, the part map or WAY-139's scope that the guide belongs to refinement or to the cycle: not found; see M5.
  - whole-change review, .runs/task-cycles/deployment-skill-guide/reports/review-whole-report.md: Whether the human accepted the exception's omission (I2) before the cut: the frozen task is silent on it; `task.md` gives no instruction on quoting the sentence.
  - whole-change review, .runs/task-cycles/deployment-skill-guide/reports/review-whole-report.md: Guidelines for the-way's own prose files: none (WAY-328 covers code and tests only); I judged the guide against the task, the decisions named and the form of neighbouring step files.
  - review of the merge, .runs/task-cycles/deployment-skill-guide/reports/review-merge-report.md: A test or invariant that holds any sentence of WAY-139: not found (none exists; the pair of examples holds the entry).
  - review of the merge, .runs/task-cycles/deployment-skill-guide/reports/review-merge-report.md: A width rule for the lines of `foundations/decisions.md`: not found in the template, `rules.md` or the check.
  - review of the merge, .runs/task-cycles/deployment-skill-guide/reports/review-merge-report.md: Whether WAY-139's "that item and that task point to the guide" covers the *To do* items of the three items handled apart: unclear (Minor 2).

# Cycle record — Doprecyzowanie zadania kończy się spisem decyzji, które dokument zostawia wykonawcy, sprawdzonym krytyką — człowiek widzi tylko sprawy otwarte

- Task source: the task's note in the author's backlog; accepted 2026-11-14 (`Status: ready for cycle`; the note's last commit in the author's vault: `1a64a1b2`, 2026-11-14); frozen copy `task.md` beside this record
- Task relation: independent
- Product repository: the-way (`https://github.com/mariusznazar/the-way`)
- Process pin: not applicable (the repository is the-way itself; its checkout is the process)
- Target branch and base: `foundations`, `9cbc6b2c46837c956f863843de0dd0bc3d32d8f1` (merge commit of PR #132; fast-forwarded from `7f5c5a5` at start)
- Task branch: `task/decisions-list-in-refinement` (worktree `the task's worktree (the repository's root)`)
- Status: request open

Instruction of the human with the order, which binds the cycle: before EVERY full run of the product's gate
the orchestrator writes it to the human (a note that the tree is ready, with free memory and other gate
runs seen) and waits for the signal `start` of the day's advisor.

## Two questions at start

- Trust boundary: no — the change edits skill files of the part `project-level` (`project-level/task/skill/final_review.md`, `orchestrated_mode.md`, `SKILL.md`) and writes two decisions in `foundations/decisions.md`; none of the files the part map names as trust boundary (`project-level/readiness_check.py`, `plan_check.py`, `plan_state.py`) is touched
- Irreversible operation: no — the change is text of skills and decisions in a repository, undone by a revert

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none — the task fixes where the step stands (`final_review.md`), when it runs (question 1), for which agents and class (question 3), what the human sees (question 2) and the orchestrated variant (point 7); both rows of *Settlements to record* go to a decision and are settled by the human's questions
- Reserved choice: none — no language, framework, library, store, login or place to run is needed
- Execution route and reason: one author without a plan; the change is three small edits of skill text and two decisions, which one agent holds
- Author: `the-way-author`, class `same` as the orchestrator's (not the default `cheaper`): the text is normative wording that later agents of the process follow and two decisions with a rationale, so the quality of wording outweighs the lower price; resumed twice (fix 1, return step), never replaced
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: the harness's completion notification (each agent dispatched in the background, the turn yielded until its notification); no limit reached, no timeout, no interruption
- Whole-change review: `the-way-stage`, class `same`, a reviewer that made none of the change; range `9cbc6b2..51f2590`, report `reports/review-whole-report.md`, first line `FAIL 51f2590` — 1 blocking (I1, Important), 5 Minor within the task (M1-M5), 0 outside scope; changed files `foundations/decisions.md` +103, `final_review.md` +39, `orchestrated_mode.md` +10, `SKILL.md` +3 −1; it covered every task item (To do 1-8), both settlement rows (WAY-377, WAY-378) and the source fidelity of the five points the orchestrator put to it
- Review rounds:
  - findings `reports/fix-1-findings.md`: whole change, range `9cbc6b2..51f2590`, report `reports/review-whole-report.md`; blocking finding I1 (the skill's quotation check did not reach the guesses the critique calls settled, though WAY-378's example needs it) and the Minor findings M1-M5 within the task (fixed with it, WAY-161); fix by the resumed author, range `51f2590..b084a4a`, report `reports/author-fix-report.md`; review of the fix by the same reviewer resumed, `reports/review-fix-1-report.md`, `PASS b084a4a`; no blocking finding remained; one new Minor finding N1 (the widened check names "settled in the repository" only) is not fixed and goes to the request's list
- Weakest-point checks: author — the requirement "who writes what file in `.runs/` and the orchestrated variant (To do 5, 7)": read against the task item by item, `reports/author-report.md` *Own-work check*; author's fix — that skill, WAY-378 and the orchestrated bullet say the same about what the quotation check covers: three texts read side by side, `reports/author-fix-report.md`; the reviewer's own check of the same, `reports/review-fix-1-report.md`

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

One-author route: no slices.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| (order only; time not read from the clock) | start | orchestrator | skill `task-cycle/skill/SKILL.md`, steps 1-5 | — | the task read in full: `Status: ready for cycle`, *Human actions* `none`, independent; the checkout `foundations` fast-forwarded from `7f5c5a5` to `9cbc6b2` (39 commits; the skill file differed only in the exit-code-2 sentence of step 12); the entry point started over |
| (order only) | step 4 | orchestrator | `python -B task-cycle/remove_merged_worktrees.py --apply --target foundations` | exit 0 | removed `the-way-wt/scripts-after-foundation-review`; stay for a human decision: four directories (below, *Directories of earlier tasks kept*) |
| (order only) | step 4 | orchestrator | `git worktree add --no-track -b task/decisions-list-in-refinement ../the-way-wt/decisions-list-in-refinement foundations` | base `9cbc6b2` | the base is a merge commit whose tree `2658fba095c52e1a2de3f792aeb6e0cf2cb8739a` equals that of its second parent: no gate run on the base; the list of tests failing before the change is taken from the earlier cycle's record (see *Verification*) |
| (order only) | step 9, one author | `the-way-author`, class `same` (model: the harness's, the same as the orchestrator's) | `reports/author-handoff.md`; skill `task-cycle/change/SKILL.md`, variant "the whole change as the one author"; frozen task; index `.runs/orchestrator/index.md` | `reports/author-report.md` | commit `51f2590` (4 files: +155 / −1); status `done`; mechanical check: worktree clean, range non-empty, changed files cover To do 1-8 (`final_review.md`, `orchestrated_mode.md`, `SKILL.md`, `decisions.md`); checks with commands and exit codes, **Unread material**, **Searches not found or unclear** and own-work check present; the author's gaps in unread material (WAY-113/134/124/154 whole, part-map entries, linked entries of the invariants, four `instruction-files` files) carried to the whole-change reviewer, who selects its own reading; the author's choices 4-7, which the task does not state, put to the reviewer; working copy `.runs/author/` removed |
| (order only) | step 9, whole-change review | `the-way-stage`, class `same` | `reports/review-whole-handoff.md`; `task-cycle/review/SKILL.md`, variant whole change; range `9cbc6b2..51f2590` | `reports/review-whole-report.md` | `FAIL 51f2590`: 1 blocking (I1), 5 Minor within the task (M1-M5), 0 outside scope; checks it ran: `foundation_check.py`, `check_instructions.py`, `change_file_sizes.py`, `decision_index.py`, `gate/run_tests.py project-level` (278 OK), all exit 0; its **Unread material** (WAY-95, 114, 313-315, 155, 267, 35, 256, 12, 05 read by sentence only; invariants by *Part* line; six `instruction-files` files) bears on nothing it judged (Q3); working copy `.runs/review-whole/` removed |
| (order only) | step 9, fix 1 | `the-way-author` resumed, class `same` | `reports/fix-1-findings.md` (the review's findings in its words; the orchestrator's direction for I1 is Q2) | `reports/author-fix-report.md` | commit `b084a4a` (fix range `51f2590..b084a4a`; 4 files, +39 / −29); status `done`; clean worktree, non-empty range; checks with exit codes, own-work check, **Unread material** (the review's report not read; findings file read whole) and **Searches** (`none`) present; working copy removed |
| (order only) | step 9, review of fix 1 | `the-way-stage` (the same reviewer, resumed), class `same` | `reports/fix-1-findings.md`, `reports/author-fix-report.md`; range `51f2590..b084a4a` | `reports/review-fix-1-report.md` | `PASS b084a4a`: I1 and M1-M5 fixed; one new Minor (N1), not blocking, not fixed, goes to the request's list; checks: `foundation_check.py` exit 0, `check_instructions.py` exit 0, line-length and grep checks; its one `decision_index.py` run failed with exit 2 by its own removed directory and was not repeated; no second round (WAY-162) |
| (order only) | step 11, return step | `the-way-author` resumed, class `same` | `reports/return-step-handoff.md`; `task-cycle/skill/return_step.md`, `foundation_step.md` | `reports/author-return-step-report.md` | status `done`; nothing to correct, nothing committed, head stays `b084a4a`, so no review of the return step; its **Unread material** bears on nothing the return step judged (Q4); **Searches**: `none`; working copy removed |
| (order only) | step 12 | orchestrator | `git fetch origin --tags`; `git merge-base --is-ancestor origin/foundations HEAD` | `origin/foundations` still `9cbc6b2`, an ancestor of the head | no reconciliation with the target branch, no review of one; final tree = `b084a4a` |
| (order only) | step 10 | orchestrator | note to the human that the tree was ready (13.8 GB free; another session's gate run seen: `gate_times.py` with `run_tests.py` of a loop2 task worktree) | — | waited for the signal `start` of the day's advisor before the full gate, by the human's order of this cycle |
| 2026-11-15 11:34:54 UTC | step 10 | orchestrator | the signal `start` of the day's advisor: "bramka loop2 nie przeszkadza, pamięci wystarczy" | `reports/gate-run1.log`, `gate_times.md` | full gate on `b084a4a`, exit 0 (see *Verification*) |
| (order only) | step 12 | orchestrator | `task-cycle/cycle_stages.py`, `task-cycle/cycle_measures.py`, `task-cycle/remarks_check.py` | `stages.md`, `mechanism_measures.md` | exit 0, 0, then 1 with 6 items (appended to the process remarks, below) |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | Which class does the one author work on? (step 4, WAY-229) | `same` as the orchestrator's | the task changes the normative wording of a skill and writes two decisions; the author takes decisions of wording of its own | `cheaper` (default): a weaker model on wording that other agents will follow | a vague sentence in a skill is followed by every later agent; the whole-change review and the fix absorb it | author |
| Q2 | I1 of the whole-change review: the skill's quotation check covers only matters to be shown, WAY-378's example needs it also for guesses the critique calls settled. Which way does the fix go? (task To do 5 reads "przy każdej sprawie, którą pokaże"; the human's *Not chosen* of question 2 gives as the reason for the check the case of a critique that wrongly calls a matter settled) | widen the check in `final_review.md`, `orchestrated_mode.md` and, where needed, WAY-378 to the quotation behind every verdict that keeps a matter from the human (settled, most likely right); a quotation that does not hold counts the guess open | reviewer's recommendation in `reports/review-whole-report.md` I1; task *Not chosen* of question 2 | change WAY-378's example to a shown matter: keeps To do 5's words, leaves the case the human named as reason unguarded | the refining agent opens more files (bounded by the list); the request puts the widening before the human | fix 1 |
| Q3 | The whole-change reviewer's unread material (see its report): does it bear on something it judged? | no: what it read only by sentence or by heading is not named by the task and none of its findings rests on those entries | `reports/review-whole-report.md` *Unread material* | resume the reviewer to read them: cost of a turn, no finding expected | an entry unread in full could hold a rule against the change; the review of the fix and the foundation check cover it | none |
| Q4 | The return step's unread material (see its report): does it bear on something it judged? | no: nothing was found to correct; the reviewers read the decisions of the task whole and the invariants of the part are not touched by prose of a skill | `reports/author-return-step-report.md`, `reports/review-whole-report.md` | resume the author to read them: a turn, no finding expected | a missed entry would show in the foundation check, which passes | none |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| frozen task | `task.md` beside this record (copy of the note of the same name; note commit `1a64a1b2`) | human, accepted 2026-11-14 | accepted |
| code, decisions WAY-377 and WAY-378 | commit `51f2590` | `the-way-author` | whole-change review `FAIL 51f2590` (I1, M1-M5) |
| fix of the findings | commit `b084a4a` | `the-way-author` | `PASS b084a4a` (N1 Minor remains) |
| reports | `reports/author-report.md`, `review-whole-report.md`, `author-fix-report.md`, `review-fix-1-report.md`, `author-return-step-report.md`; handoffs `author-handoff.md`, `review-whole-handoff.md`, `return-step-handoff.md`; findings `fix-1-findings.md` | agents | — |
| gate log | `reports/gate-run1.log`, `gate_times.md` | orchestrator | exit 0 |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| list of the tests failing before the change | orchestrator, base `9cbc6b2` (merge; tree `2658fba095c52e1a2de3f792aeb6e0cf2cb8739a` equals that of its second parent) | taken from `docs/task-cycles/scripts-after-foundation-review/cycle.md` of commit `c40ed70` (the only copy the merged branch added), *Verification*: its final gate, run 2 on `cf4fe17`, exit 0, 1561 tests in 11 directories, every directory passed | none failing before the change; no gate run on the base |
| `python -B task-cycle/gate_times.py --output .runs/task-cycles/decisions-list-in-refinement/gate_times.md -- python -B gate/run_tests.py` (final gate, run 1) | orchestrator, `b084a4a` (the final tree: `origin/foundations` fetched and still `9cbc6b2`, so no reconciliation), Windows, started 2026-11-15 11:34:55 UTC by the clock of `gate_times.md`, on the signal `start` of the day's advisor after the orchestrator's note that the tree was ready (13.8 GB free; the orchestrator saw one gate run of another session, in a loop2 worktree; the advisor: it does not interfere, memory is enough) | 0; 1561 tests in 11 directories, 861.9 s, 2 other gate runs at the same time (counted by the script); every directory passed (log `reports/gate-run1.log`); the slowest directories were `process-audit` (860.8 s) and `installation` (751.3 s) | none |
| `python -B elements/common/foundation_check.py`, without `--skip-test-citations` | orchestrator, `b084a4a` | 0; `0 errors` | none |
| `python -B task-cycle/review_reminder.py origin/foundations` (after `git fetch origin --tags`) | orchestrator | 0; `tag: foundation-review/2026-11-15`, `merges: 5`, `threshold: 60`, `reminder: no` | none |
| `python -B task-cycle/cycle_stages.py --output .runs/task-cycles/decisions-list-in-refinement/stages.md 397f5de7-5d0a-4193-9103-86ff4b0cf1c1`; `python -B task-cycle/cycle_measures.py --output .runs/task-cycles/decisions-list-in-refinement/mechanism_measures.md 397f5de7-5d0a-4193-9103-86ff4b0cf1c1` | orchestrator, the one session of the cycle, run before the final steps of the request (the figures do not count them) | both 0 | none |
| focused checks of the author, the fixer and the reviewers, the last run of each | author, reviewers | exit 0 each: `foundation_check.py`, `check_instructions.py`, `gate/run_tests.py` for `project-level` (278 tests), `elements/common` (242), `agent-instructions` (27), `instruction-files` (104, 5 skipped POSIX-only) | the reviewer's one `decision_index.py` run of the fix review failed with exit 2 by its own removed directory (not repeated; `foundation_check.py` parses both entries); no check failed otherwise; no test of behaviour exists for the prose of skills |

## Return step

- Foundation compared with code: the entries the change writes (WAY-377, WAY-378), those the task names (WAY-374, WAY-120, WAY-113, WAY-229, WAY-100, WAY-134, WAY-124, WAY-154), the search of the whole foundation and the part-map entries of `project-level` and `decisions`, over the range `9cbc6b2..b084a4a` (`reports/author-return-step-report.md`); nothing no longer matched after fix 1, so nothing was corrected and nothing committed
- Decisions written or changed: WAY-377 and WAY-378 (written in the foundation step, changed once in fix 1)
- Invariants written or changed: none
- Environment facts: none (the course is not open to a reader; WAY-377's *Rationale* describes what the notes hold, as WAY-100 and WAY-27 give)
- Glossary terms: none
- Part-map changes: none
- Projected entries written whole or in part: none (the task is independent)
- Rows of *Settlements to record* written: row 1 → WAY-377, row 2 → WAY-378, both in `foundations/decisions.md`, section "Task refinement and readiness"

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/133 — opened as a draft, to be marked ready after the record is committed and the description's link and checks are filled in
- Description: `request.md` beside this record, written by `task-cycle/skill/request_template.md`; form check `python -B task-cycle/request_check.py .runs/task-cycles/decisions-list-in-refinement/request.md --task .runs/task-cycles/decisions-list-in-refinement/task.md` exit 0 (1 run before publishing; the last run is recorded in *Verification* after the link edit); in a copy committed before the description's link and checks were added, `written and checked after this commit`
- Writes to the task's backlog entry: none
- Working copies left: none
- Directories of earlier tasks kept:
  - `agent-path-to-running-product` · `task/agent-path-to-running-product` · the branch has no merge git can see on origin/foundations: not merged, merged by squash or rebase, or its request open or closed
  - `ci-on-merge-requests` · `task/ci-on-merge-requests` · uncommitted changes: a tracked file changed or a new file that git does not ignore; the branch has no merge git can see on origin/foundations: not merged, merged by squash or rebase, or its request open or closed
  - `base-check-stage-remarks` · detached · the branch task/stage-remarks its name gives is not found
  - `base-fix-minor-findings` · detached · the branch task/minor-findings its name gives is not found
- Corrections after the request opened: none
- Process remarks on the-way:
  - the orchestrator: the times of the first rows of *Events* were written before the clock was read; they were replaced by "order only", and the time of the gate row is the script's (a remark of the orchestrator's own, not an item of a report)
  - author, `.runs/task-cycles/decisions-list-in-refinement/reports/author-report.md`: WAY-100 asks that a decision which adopts an outside practice put in *Rejected* what it leaves out of the practice. The task's rows and *Not chosen* keep no such way, and the notes of the course are not open to me, so WAY-377's *Rationale* states what is taken (the list and the mark) and what is the-way's own, and its *Rejected* holds only the three ways the task keeps. Unclear whether this satisfies WAY-100 in the human's eyes.
  - author, `.runs/task-cycles/decisions-list-in-refinement/reports/author-report.md`: The project orchestrator's own files (`project-level/lead/…`) say nothing of this request type; its step 3.1 says it performs "all child dispatches their borrowed workflows request" and the conversation template's *Child-work requests* line says "needed critique or other delegated work and full paths of material", which covers it in general terms. I changed no lead file (outside the task's *To do*).
  - author, `.runs/task-cycles/decisions-list-in-refinement/reports/author-report.md`: Test holding WAY-374's sentences: none found (`decision: WAY-374` appears in no file).
  - whole-change review, `.runs/task-cycles/decisions-list-in-refinement/reports/review-whole-report.md`: A pointer in `project-level/lead/` to this request type: not found (M2).
  - whole-change review, `.runs/task-cycles/decisions-list-in-refinement/reports/review-whole-report.md`: A test that holds a sentence of WAY-374, WAY-377 or WAY-378 by `decision:`: none; not needed (pair of examples).
  - whole-change review, `.runs/task-cycles/decisions-list-in-refinement/reports/review-whole-report.md`: Whether WAY-100's "what it leaves out" can be written from a row's source that keeps no such way: unclear (M3). Removed: .runs/review-whole/ (index.md, sections.md) at the end of the review.

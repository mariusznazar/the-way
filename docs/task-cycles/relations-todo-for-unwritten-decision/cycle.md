# Cycle record — the way: decision derived from a not yet written decision gets a descriptive `TODO` in *Relations*

- Task source: the task's note in the author's backlog — status `ready for cycle`, last change of the document in the author's notes 2026-11-14 (commit da85ceff of the notes repository); frozen copy `task.md` beside this record
- Task relation: independent
- Product repository: https://github.com/mariusznazar/the-way (the-way itself)
- Process pin: the checkout itself (the-way is the top-level repository; no pin)
- Target branch and base: `foundations`, `30c947f686b3d304f5a952cb6efe547762cfa247`
- Task branch: `task/relations-todo-for-unwritten-decision`
- Status: running

## Two questions at start

- Trust boundary: no — the change edits `foundations/decisions.md`, `elements/common/rules.md`, `elements/decisions/template.md`, `elements/common/foundation_check.py` with its test, and `task-cycle/skill/request_template.md`; the part map names `none` as the trust boundary of the parts `decisions` and `elements-common`, and `task-cycle`'s boundary files (`cycle_stages.py`, `cycle_measures.py`, `gate_times.py`) are not touched.
- Irreversible operation: no — text and a check; nothing outside the repository.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none — the task's *To do* 1–6 and its four *Questions to settle* (answers given by the day advisor for the human, 2026-11-14) fix the form (`TODO — <the decision, and where it is expected>`, last item of *Relations*, bare `TODO` an error, *Origin* unchanged, scope every unwritten decision, one sentence in WAY-126) and the files; the wording of the binding sentences is the entry the task carries, not a choice left open. The two alternatives (the form checked against a definition by the script; the partial entry as the default) are rejected in the task.
- Reserved choice: none — no language, framework, library, store, login or place to run is needed.
- Execution route and reason: one author without a plan — six edits in six files over three parts (`decisions`, `elements-common`, `task-cycle`), each stated by the task, with one script change and its tests; one agent holds it.
- Author: `the-way-author`, class `same` (sonnet): the change rewrites binding sentences of two decisions and changes a check's reading of a field, over three parts, and a wrong word in a binding sentence or a condition in the check is hard to see in review; `cheaper` rejected for that. Dispatch 1 returned commit `452f123`; resumptions: none yet.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: native completion notification of the harness for a background agent; no limit reached
- Whole-change review: `the-way-stage` on opus, `review-change`; range `30c947f..452f123`; first line `FAIL 452f123d65de88143c91fe37b5633ecd341d88ee`, `reports/review-whole-report.md`; changed files as in the Events row; coverage of every To do item 1-6, the four questions, *Decisions in play*, *Out of scope* and source fidelity stated in the report; blocking finding I1 comes from the one commit (no plan)
- Review rounds:
  - findings `reports/review-whole-findings.md`: review of the whole change, range `30c947f..452f123`, report `reports/review-whole-report.md`, `FAIL`; blocking: I1 (Important, a bare `TODO` behind a relation type passes the check, comes from the one commit); Minor within the task: M1, M2, M3 (fixed with it, WAY-161); Minor outside the task's scope: M4, M5 (not fixed); fix `68d8645` (range `452f123..68d8645`), its review by the same reviewer: `reports/review-fix-report.md`, `PASS 68d8645c78e55bf751161fedd26dedf31cb43dbc`; Minor findings of the fix's review N1 and N2 remain and go to the request's list
  - findings `reports/review-return-step-findings.md`: review of the return step, range `68d8645..763af69`, report `reports/review-return-step-report.md`, `FAIL`; blocking: I1 (Important); Minor m1 not fixed; fix `07a23b3` (range `763af69..07a23b3`), its review by the same reviewer: `reports/review-fix-2-report.md`, `PASS 07a23b3a1ee8680697d3ad0aeb26e9803a693fb5`
- Weakest-point checks: author - the check accepts the form on the real log and still checks what stands before it (own-work check, `reports/author-report.md`); fix - a bare `TODO` is reported in whatever form it stands (own-work check, `reports/author-fix-report.md`); the reviewer's scratch runs on the real log confirmed both

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

One author, no plan: no rows.

## Events

| Time (UTC; read from the stage table of `stages.md`) | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-16 06:41 | start | orchestrator, Sonnet 5.5 | `/the-way-implement-task`; task document | — | `git fetch`: `foundations` was 15 commits behind `origin/foundations`; fast-forwarded the checkout `8f0c1c3` → `30c947f` (clean tree, on the branch, no local commits); `task-cycle/skill/SKILL.md` changed in them (CI is the final gate), so the skill was read again from the updated checkout |
| 2026-11-16 06:42 | worktree cleanup | orchestrator | `python -B task-cycle/remove_merged_worktrees.py --apply --target foundations` | — | exit 0; removed `ci-replaces-local-final-gate`; four directories kept (listed under *Directories of earlier tasks kept*) |
| 2026-11-16 06:42 | branch | orchestrator | `git worktree add --no-track -b task/relations-todo-for-unwritten-decision … origin/foundations` | — | worktree at `30c947f`, tree clean; the base is a merge commit and `git rev-parse 30c947f^{tree}` = `git rev-parse 30c947f^2^{tree}` = `00c7a1e62fbfec060c9395a0a50b641f2bf43585`, so no gate on the base |
| 2026-11-16 06:43 | reading | orchestrator | `elements/common/way_of_working.md` "Reading the foundation", `product-guidelines/reading.md`, `guidelines/coding.md`, `guidelines/testing.md`, `foundations/part_map.md`, WAY-71 and WAY-126 whole, `agent-instructions/README.md` | `.runs/orchestrator/index.md` (91 decisions of the parts `elements-common` and `decisions`, plus WAY-71, WAY-126, WAY-17, WAY-287, WAY-07, WAY-33, WAY-114) | reconciliation with the sources, see the first two rows of the questions table |
| 2026-11-16 06:44 | author (whole change) | `the-way-author`, sonnet (class `same`), background | `reports/author-handoff.md`; `make-change`, "the whole change as the one author"; frozen task | `reports/author-report.md` (expected) | dispatched; next: mechanical check, then the review of the whole change |
| 2026-11-16 06:56 | author returned | `the-way-author`, sonnet | `reports/author-report.md` | commit `452f123` (6 files, +132 -49) | status `done with concerns`; mechanical check by the orchestrator: tree clean, range `30c947f..452f123` holds one commit, the changed files are the six of To do 1-6, each check of the report carries command and exit code, **Unread material** and **Searches not found or unclear** present, own-work check present. Concerns: WAY-287's list of fields stale by one (left as the task says); `ruff` absent in the author's environment; `way_of_working.md` read in part - all three carried to the review's handoff |
| 2026-11-16 06:56 | whole-change review | `the-way-stage`, opus (strongest class allowed by the session; `fable` is disabled by the user's instruction) | `reports/review-whole-handoff.md`; `review-change`, whole change; range `30c947f..452f123`; frozen task; author report | `reports/review-whole-report.md` (expected) | dispatched |
| 2026-11-16 07:03 | whole-change review returned | `the-way-stage`, opus | `reports/review-whole-report.md` | `FAIL 452f123d65de88143c91fe37b5633ecd341d88ee`; files with counts: foundation_check.py +24/-16, test_foundation_check.py +52/-8, rules.md +6/-4, template.md +9/-3, decisions.md +38/-16, request_template.md +3/-2 | 1 Important (I1, within the task, blocking), Minor M1-M3 within the task, M4 and M5 outside the task's scope (not fixed; go to the request's list); reviewer read 6 decisions whole of its index; WAY-287 read in part (outside the change's blocking findings, carried to the request as M4). Next: one fix by the resumed author, then one review of the fix |
| 2026-11-16 07:04 | fix of the review's findings | `the-way-author`, sonnet (resumed) | `reports/author-fix-handoff.md`; findings `reports/review-whole-findings.md` | `reports/author-fix-report.md` | fix commit `68d8645` (4 files, +63 -25); status `done`; mechanical check by the orchestrator: tree clean, range `452f123..68d8645` holds one commit, files are those of the findings, each check carries command and exit code, **Unread material** and **Searches not found or unclear** present (`none`), own-work check present. Choice in the report: the file `foundation_check.py` kept at 999 lines (threshold 1000) by shortening the author's own additions; next addition there needs a move first |
| 2026-11-16 07:10 | review of the fix | `the-way-stage`, opus (same reviewer, resumed) | `reports/review-fix-handoff.md`; findings `reports/review-whole-findings.md`; range `452f123..68d8645` | `reports/review-fix-report.md` | `PASS 68d8645c78e55bf751161fedd26dedf31cb43dbc`; I1, M1, M2, M3 fixed; no new Critical or Important; two new Minor (N1, N2), within the task, not fixed (a Minor finding of a fix review does not block and goes to the request's list); `foundation_check.py` 999 lines; no unread material, no searches open |
| 2026-11-16 07:13 | return step | `the-way-author`, sonnet (resumed) | `reports/author-return-step-handoff.md`; `task-cycle/skill/return_step.md`, `foundation_step.md` | `reports/author-return-step-report.md` (expected) | dispatched; the CI run on the request's last head is the final gate (the repository holds `.github/workflows/tests.yml` on `pull_request`), so the orchestrator runs no full gate on its own system here (step 10) |
| 2026-11-16 07:16 | return step returned | `the-way-author`, sonnet | `reports/author-return-step-report.md` | commit `763af69` (`foundations/decisions.md` WAY-71 *Verification*, 2 comment lines in `elements/common/test_foundation_check.py`) | status `done with concerns`; tree clean, range `68d8645..763af69` one commit; checks carry command and exit code; **Unread material** states `reports/review-whole-report.md` unread and the entries WAY-17, WAY-07, WAY-33, WAY-114, WAY-287 not read again in this stage (read whole in the first stage) - recorded as an autonomous choice: it bears on nothing the return step judged, since the compared entries are WAY-71 and WAY-126 whole and the review of the return step reads WAY-287 context from the findings; **Searches** `none`. Concern: WAY-287 (named for the human) |
| 2026-11-16 07:17 | review of the return step | `the-way-stage`, opus (fresh) | `reports/review-return-step-handoff.md`; range `68d8645..763af69` | `reports/review-return-step-report.md` | `FAIL 763af6951a65f6cca17b032a037c60c7b2d59e0a`; 1 Important (I1, within the task, blocking: the `tests:` clause of WAY-71 names the comma join and the described form after known relations, which no test holds by a line `decision:`, while their examples were removed from the pair), 1 Minor (m1, the report's argument for WAY-287; not fixed, goes to the request's list); the reviewer read WAY-71, WAY-126, WAY-12, WAY-22 whole; WAY-287 in part. Next: one fix by the resumed author, one review of it by the same reviewer |
| 2026-11-16 07:22 | fix of the return step's findings | `the-way-author`, sonnet (resumed) | `reports/author-fix-2-handoff.md`; findings `reports/review-return-step-findings.md` | `reports/author-fix-2-report.md` | fix commit `07a23b3` (`elements/common/test_foundation_check.py`, +2 comment lines); status `done`; way (a) chosen over (b) (restoring two examples to the pair); mechanical check: tree clean, range `763af69..07a23b3` one commit, checks carry command and exit code, own-work check, **Unread material** names only the review report (the findings file holds the finding whole), **Searches** `none` |
| 2026-11-16 07:24 | review of the fix of the return step | `the-way-stage`, opus (same reviewer, resumed) | `reports/review-fix-2-handoff.md`; findings `reports/review-return-step-findings.md`; range `763af69..07a23b3` | `reports/review-fix-2-report.md` (expected) | dispatched |
| 2026-11-16 07:27 | review of the fix of the return step returned | `the-way-stage`, opus | `reports/review-fix-2-report.md` | `PASS 07a23b3a1ee8680697d3ad0aeb26e9803a693fb5` | I1 of the return step's review fixed; no new finding; **Unread material** `none`, **Searches** `none`; known Minor findings m1, M4, M5, N1, N2 go to the request's list. Next: target branch check (contained), cycle_stages and cycle_measures, remarks check, request description |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | The task's *Context* says the-way has no `guidelines/` and its *Questions to settle* 4 asks whether that holds the task (WAY-215). Source: task document. | It no longer does: `guidelines/coding.md`, `guidelines/coding-check.md`, `guidelines/testing.md` stand on `foundations` (WAY-379, WAY-392). The cycle reads them by `product-guidelines/reading.md` and the author follows them: `foundation_check.py` is of the kind `check`; its test is a test of `elements-common`. The answer of the task (does not hold) stays right. | `guidelines/coding.md` lines 1–22, `guidelines/testing.md` lines 1–20 | stop for the stale claim — nothing needs the human | the author works without the guidelines (not the case: named in the handoff) | author handoff |
| Q2 | *Decisions in play* names WAY-37 and WAY-32 as entries "without change". Source: task document. | Both are withdrawn: their rules stand in `elements/common/way_of_working.md` (WAY-37) and `elements/decisions/template.md` (WAY-32), as the table "Withdrawn identifiers" of `foundations/decisions.md` says. They stay unchanged, as the task says; the effect on the required outcome is none. The WAY-126 sentence that To do 5 adds names the successors' files, not the withdrawn identifiers. | `foundations/decisions.md` lines 10566 and 10567 | stop — the required outcome is still established | a binding sentence cites a withdrawn identifier (the review checks it) | author handoff |
| Q3 | The user's delegation (the command's arguments): before every full run of the test gate, say so and wait for the start signal of the day advisor; reviewers on the strongest class run with `model: opus`, not `fable` (disabled). | Applied: no handoff lets an agent run the full gate; the orchestrator's own full runs — where CI is not the gate, or CI gives no result in 30 minutes, or the gate must run on the base — stop for the signal. Every reviewer is dispatched with `model: opus`. | the command's arguments | ignore the stop — the human's instruction binds | a full run starts without the signal | whole-change review, return-step review, every fix review, gate runs |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| frozen task | `.runs/task-cycles/relations-todo-for-unwritten-decision/task.md` | orchestrator (copy of the document above) | — |
| code commit | `452f123` (the change) | the-way-author, sonnet | `FAIL` of the whole-change review, fixed by `68d8645` |
| code commit | `68d8645` (the fix of the whole-change review) | the-way-author, sonnet | `PASS` (`reports/review-fix-report.md`) |
| code commit | `763af69` (the return step) | the-way-author, sonnet | `FAIL` (`reports/review-return-step-report.md`), fixed by `07a23b3` |
| code commit | `07a23b3` (the fix of the return step's review) | the-way-author, sonnet | `PASS` (`reports/review-fix-2-report.md`) |
| reports | `reports/` (handoffs, reports, findings files, the reviewers' index `review-whole-index.txt`) | agents | as listed in Events |
| description | `request.md` | orchestrator | form check exit 0 |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| list of the tests failing before the change, from the final gate of the merged branch's cycle: `docs/task-cycles/ci-replaces-local-final-gate/cycle.md` as added by commit `8162a28` (the last copy), *Verification* rows of the gate on `cdfcf48` (exit 0, 1601 tests in 11 directories) and the CI run 43813765998 on `026308f` (both jobs green); the request #140 *Checks* read through `gh pr view 140`: `tests` SUCCESS, `tests-windows` SUCCESS. The base is a merge commit with the tree of its second parent, so no gate on the base | orchestrator, read from git history and the host | no test failing on the base | none failing |
| `python -B elements/common/foundation_check.py` on `07a23b3`, without `--skip-test-citations` | orchestrator, Windows | exit 0, `0 errors`, no `listed:` line | none |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator | exit 0 - tag foundation-review/2026-11-15, merges 13, threshold 60, `reminder: no` | none |
| `python -B task-cycle/remarks_check.py .runs/task-cycles/relations-todo-for-unwritten-decision` on the original | orchestrator | run 1 exit 1 (2 items listed, appended to the process remarks), run 2 exit 0 (2 runs) | none |
| `python -B task-cycle/request_check.py .runs/task-cycles/relations-todo-for-unwritten-decision/request.md --task .runs/task-cycles/relations-todo-for-unwritten-decision/task.md` and `python -B task-cycle/private_paths_check.py` on the same description | orchestrator | exit 0 and exit 0 (2 runs each) | none |
| step 10: the final gate is the CI run on the request's last head (the repository holds `.github/workflows/tests.yml` that runs on `pull_request`); the cycle has no local time of it and runs no full gate on its own system; its result stands in *Checks* of the request's description and not in the copy of the record | orchestrator | not applicable | CI result pending until the request is open |
| target branch: `git fetch --tags origin`; `origin/foundations` is `30c947f`, already contained in `07a23b3` (`git merge-base --is-ancestor`) | orchestrator | no merge needed, so no review of a merge and no second gate | none |
| `python -B task-cycle/cycle_stages.py` and `python -B task-cycle/cycle_measures.py` naming this session | orchestrator | 0 and 0 | none |
| focused checks by the agents (reports): `python -B gate/run_tests.py elements/common` 257 OK (author, fix, return step, two fix reviews, review of the whole change); `task-cycle` 534 OK and `product-guidelines` 14 OK and `agent-instructions` 37 OK (author, on `452f123`); `ruff` not installed on this system, so the linter's blocking rules ran in no agent's check - the gate (CI) runs it | agents, Windows | all exit 0 | `ruff` not run locally |

## Return step

- Foundation compared with code: WAY-71 and WAY-126 (the entries the change writes), the entries the task names (WAY-17, WAY-07, WAY-33, WAY-114, WAY-287), the part-map entries `decisions` and `elements-common` and the files of the change were compared with the code at `68d8645`: they agree; WAY-287's list of three fields is one short of item 16 of the request template and is left as the task says, for the human (`reports/author-return-step-report.md`). One correction: WAY-71's *Verification* now opens with a `tests:` clause, since the tests this change writes hold the *Relations* part, and the examples they hold were removed from the pair; the review of the return step found that two of the four parts had no line `decision:`, and the fix `07a23b3` added the two lines (`reports/review-return-step-report.md`, `reports/review-fix-2-report.md`)
- Decisions written or changed: WAY-71 and WAY-126 (changed; both marked `the cycle's` by the author)
- Invariants written or changed: none
- Environment facts: none
- Glossary terms: none
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: none (the section reads `none`)

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/141 - opened as a draft, to be marked ready for review once CI on the last head is green
- Description: `request.md` beside this record, written by `task-cycle/skill/request_template.md`; `request_check.py` last exit 0 and `private_paths_check.py` last exit 0 (2 runs each, the second after the wording of *Minor findings* was edited), written and checked before the request opened; the edit that adds the record's link, the checks on the copy and the CI result is checked again after the commit of the copy
- Writes to the task's backlog entry: none
- Working copies left: none
- Directories of earlier tasks kept:
  - agent-path-to-running-product · task/agent-path-to-running-product · the branch has no merge git can see on origin/foundations
  - audit-answers-contradiction-after-code · task/audit-answers-contradiction-after-code · the branch has no merge git can see on origin/foundations
  - base-check-stage-remarks · detached · the branch task/stage-remarks its name gives is not found
  - base-fix-minor-findings · detached · the branch task/minor-findings its name gives is not found
- Corrections after the request opened: none
- Process remarks on the-way:
  - author, .runs/task-cycles/relations-todo-for-unwritten-decision/reports/author-report.md: `elements/common/way_of_working.md` was named by the handoff but, as the foundation step reads it, the step table in it was not read whole; whether a step there needs a sentence for the *Relations* `TODO` is unclear to me. I found only the generic lines 167–168 (reads "what stays open ... is written as `rules.md` gives it"), which already cover it.
  - author, .runs/task-cycles/relations-todo-for-unwritten-decision/reports/author-report.md: No test in the repository holds a sentence of WAY-71 or WAY-126 by a line `decision:`; both are held by their pairs of examples, as before.
  - whole-change review, .runs/task-cycles/relations-todo-for-unwritten-decision/reports/review-whole-report.md: Whether a `TODO` item in *Relations* may carry a relation type before it (`derives from TODO — …`): neither WAY-71, `rules.md` nor the template says; the template's example puts no type before it (`derives from WAY-x · TODO — …`). Unclear in the sources, and the script neither accepts it as the form nor reports it (I1).
  - whole-change review, .runs/task-cycles/relations-todo-for-unwritten-decision/reports/review-whole-report.md: `ruff` in this environment: not found (Checks).
  - review of the return step, .runs/task-cycles/relations-todo-for-unwritten-decision/reports/review-return-step-report.md: A line `decision: WAY-71` at the tests of the comma join and of the form after known relations — not found (I1).
  - review of the return step, .runs/task-cycles/relations-todo-for-unwritten-decision/reports/review-return-step-report.md: A line `decision: WAY-126` anywhere — not found (expected; question 3).
  - fix, .runs/task-cycles/relations-todo-for-unwritten-decision/reports/author-fix-report.md: None. (A search of the repository for other places that quote the sentence "a bare `TODO` in *Relations*" found only the template sentence and WAY-71's *violates* line, both changed.)
  - return step, .runs/task-cycles/relations-todo-for-unwritten-decision/reports/author-return-step-report.md: None. A search of the glossary for `TODO` and `descriptive` found no entry.

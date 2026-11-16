# Cycle record — Uzupełnić w decyzjach the way źródła i to, czego nie biorą z przejętych praktyk

- Task source: the task's note in the author's backlog, `Status: ready for cycle`, settlements accepted 2026-11-15; frozen copy `task.md` beside this record
- Task relation: independent
- Product repository: https://github.com/mariusznazar/the-way (the-way itself; no pin to move)
- Process pin: not applicable — the-way is the repository changed; the process root is the worktree
- Target branch and base: `foundations`, `aba5ee92a0734c2e775cc69662af669bf6455795`
- Task branch: `task/decision-sources-and-leftouts` (worktree the worktree of the task)
- Status: request open

## Two questions at start

- Trust boundary: no — the change touches `foundations/decisions.md`, a file of the part `decisions`, whose trust boundary the part map gives as `none`.
- Irreversible operation: no — the change edits text of the decision log; the author only reads git history, the author's vault and public pages.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none — the two settlements (rows 1 and 2) settle the change to WAY-100; how each entry is worded is the writer's (WAY-134). The wording of an entry's *Rejected* positions and the outcome for each decision of the lists depend on what the source says, which the task puts to the author's search, not to a design.
- Reserved choice: none
- Execution route and reason: one author without a plan. The change is one file (`foundations/decisions.md`) and one kind of edit — the fields *Based on*, *Rationale*, *Rejected* and *Relations* of about twenty-five entries — and the finding of a source, the comparison of source and decision and the wording are one line of thought that a division would cut: a slice that finds a source needs the same reading of the decision as the slice that writes its *Rejected*. Returned for size if the author finds it does not fit one agent.
- Author: `the-way-author`, class `strongest` (model `opus`: the strongest model the session's settings allow, as the human named it — `fable` is disabled and a sub-agent given `fable` takes the session's model); reason for a class other than `cheaper`: the change needs judgment about what a source says and what a decision leaves out, and a wrongly invented source looks like a true one.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: background agents report by completion notification; the turn is yielded while only that result remains.
- Whole-change review: `the-way-stage` on `opus`, a fresh reviewer, by `review-change`; range `aba5ee9..05b4648`, one commit, `foundations/decisions.md` +199 −88; first line `FAIL 05b4648…`, report `reports/review-whole-report.md`; blocking: I1 (Important); Minor within the task: M1, M2; outside the scope: O1. It covered every task item (*To do* 1–8, both lists of *Need*, WAY-136 and WAY-148 each judged separately, the eight lesson decisions, WAY-199, WAY-203, WAY-100's rows 1 and 2, acceptance criteria 1 and 2) and compared both added citations word for word with the sources it re-fetched. Slices: none (one-author route).
- Review rounds:
  - findings `reports/review-whole-findings.md`: the review of the whole change failed on I1 (WAY-142 *Rejected* listed "the estimates", which the practice's source rejects; `foundations/decisions.md:4843-4845`); the fix, commit `01ab269`, range `05b4648..01ab269`, report `reports/author-fix-report.md`, also fixed the Minor findings M1 and M2 of the same review; the same reviewer, resumed, reviewed the fix range: `PASS 01ab269…`, report `reports/review-fix-report.md`; one new Minor finding N1 (not fixed, goes to the request's list); no blocking finding remained; the fix was not reverted.
  - correction 1, remarks `reports/correction-1-remarks.md` (in place of a findings file): the correction is commit `d48638a`, range `b679864..d48638a`, report `reports/author-correction-report.md`; reviewed by a fresh reviewer on `opus`: `PASS d48638a…`, report `reports/review-correction-report.md`, no blocking finding, six Minor findings (M1–M6, not fixed: they go to the request's list), one outside the scope (the course name spelled two ways); the same review did the unread reading of the remarks' item 2 (Part B).
- Weakest-point checks: the author — acceptance criterion 1 (the binding sentences of no listed decision change): a script comparing the text before each entry's *Scope* at the base and in the tree; showed `['WAY-100']` only, with that as the positive control; the fix: a reason carried from a map row, each compared with its row (author's table in `reports/author-fix-report.md`).

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

The one-author route has no slices.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-16 03:10 | start | orchestrator, session model Sonnet 5.5 | skill `the-way-implement-task`, task document | `task.md` | Step 4: checkout `foundations` at `aba5ee9` equals `origin/foundations` after fetch, clean; no fast-forward needed |
| 2026-11-16 03:12 | cleanup of finished directories | orchestrator | `python -B task-cycle/remove_merged_worktrees.py --apply --target foundations` | none | exit 0; 0 directories removed; 4 kept (see *Directories of earlier tasks kept*) |
| 2026-11-16 03:14 | branch and worktree | orchestrator | `git worktree add --no-track -b task/decision-sources-and-leftouts ../the-way-wt/decision-sources-and-leftouts aba5ee9` | worktree created | base `aba5ee9` is a merge commit; its tree and the tree of `aba5ee9^2` are both `5b58e7b32c9c1e4d013e2a045e2a2037bfe7c6fa`, so no gate on the base; the list of failing tests taken from the record of the merged branch (see *Verification*) |
| 2026-11-16 03:25 | author | `the-way-author`, model `opus` (strongest class) | `reports/author-handoff.md`, method `task-cycle/change/SKILL.md` variant "the whole change as the one author", frozen task `task.md` | `reports/author-report.md` (expected) | dispatched in the background; wait by completion notification, no polling |
| 2026-11-16 03:42 | author returned | the-way-author, opus | `reports/author-report.md` | commit `05b4648` on the branch, `foundations/decisions.md` only, +199 −88; status `done with concerns` | Mechanical check: worktree clean, range non-empty, changed file within the task, every check of the report with command and exit code, **Unread material**, **Searches not found or unclear** and own-work check present. Concerns: WAY-145 has WAY-136's old gap and is on no list (outside scope, goes to the request); WAY-100 marked `the cycle's`; WAY-136 evidence only, WAY-148 adopts. Reach (course skills from a local archive, the author's plan item P30, research note, `gh api` of a public commit) added to the review's handoff. Unread P7 file and partly read lesson notes → Q4 |
| 2026-11-16 03:50 | review of the whole change | `the-way-stage`, model `opus` (strongest class) | `reports/review-whole-handoff.md`, method `task-cycle/review/SKILL.md`, range `aba5ee9..05b4648` | `reports/review-whole-report.md` (expected) | dispatched in the background |
| 2026-11-16 04:10 | review returned | the-way-stage, opus | `reports/review-whole-report.md` | first line `FAIL 05b4648…`: 1 Important (I1: WAY-142 *Rejected* lists "the estimates" that the practice's source rejects), 2 Minor within the task (M1 WAY-143 *Rationale*, M2 reasons of new *Rejected* items), 1 outside the scope (O1: WAY-145, 139, 165) | Mechanical read: checks with commands and exit codes (one exit 1 explained: the directory has no tests), reaches, unread material and searches present. Reviewer's judgments: WAY-136 evidence only, WAY-148 adopts (agrees with the author), P7 read. Unread: lesson notes of m2l4 and m3l5 (author read them in part; the map's rows stand for them) — no finding rests on them, so no resumption. Findings file `reports/review-whole-findings.md` written in the reviewer's words (I1, then M1 and M2). Next: one fix by the resumed author and one review of the fix |
| 2026-11-16 04:15 | fix | the-way-author (resumed), opus | `reports/author-fix-handoff.md`; findings `reports/review-whole-findings.md` | `reports/author-fix-report.md` (expected) | resumed in the background |
| 2026-11-16 04:25 | fix returned | the-way-author (resumed), opus | `reports/author-fix-report.md` | commit `01ab269` (range `05b4648..01ab269`), status `done`; I1, M1, M2 fixed, none contested | Mechanical read: tree clean, range non-empty, only `foundations/decisions.md`; checks with command and exit code; unread: the reviewer's full report (findings file held the evidence); searches none; reach: `project-level/plan/template.md:95` |
| 2026-11-16 04:30 | review of the fix | the-way-stage (same reviewer resumed), opus | `reports/review-fix-handoff.md`; findings `reports/review-whole-findings.md`; range `05b4648..01ab269` | `reports/review-fix-report.md` (expected) | resumed in the background |
| 2026-11-16 04:40 | review of the fix returned | the-way-stage (same reviewer), opus | `reports/review-fix-report.md` | `PASS 01ab269b7d36541d4b79069b63e0fa5f7d0d5514`; no blocking finding; one new Minor N1 (WAY-142 *Rejected*, parked list reason says "copies what the definition puts out of scope", a little more than the map row) → request's list; unread: the course map was not reopened, reasons compared with the rows read in the first review | Mechanical read: checks with command and exit code, unread material and searches present. Next: return step (author resumed) |
| 2026-11-16 04:45 | return step | the-way-author (resumed), opus | `reports/author-return-step-handoff.md`, `task-cycle/skill/return_step.md` | `reports/author-return-step-report.md` (expected) | resumed in the background |
| 2026-11-16 05:05 | full gate | orchestrator | start signal of the session `doradca-dnia` ("start — uruchom pełną bramkę") after the orchestrator's message that the gate waited for it | `final-gate.log`, `gate_times.md` | exit 0, 1600 tests in 11 directories, 387.451 s (see *Verification*) |
| 2026-11-16 04:55 | return step returned | the-way-author (resumed), opus | `reports/author-return-step-report.md` | status `done`, no commit, head stays `01ab269`; no entry written (no environment fact: the two new citations are places a practice was taken from, not findings about agents or a tool the process uses; no invariant, glossary term, part-map change; rows 1 and 2 stand in WAY-100) | Nothing committed, so no review of the return step. Unread: `elements/environment-facts/skill/SKILL.md` (the template's section gave the test) — bears on nothing it judged. Next: step 10, the full gate, after the day advisor's start signal (Q3) |
| 2026-11-16 06:00 | correction 1: remarks | orchestrator | the human's comment on the request (answers to the items 1 and 2 of *Fix or let through*; items 3–6 accepted), given through the session `doradca-dnia` | `reports/correction-1-remarks.md` | Target branch: fetch shows `origin/foundations` at `aba5ee9`, already contained in the head `b679864`; no merge. *Reserved choice*: none. Route kept: author resumed for the fix of the three entries (item 1, `item 8 · not-required`); a fresh reviewer reviews it and does the unread reading (item 2, `item 14 · defect`) |
| 2026-11-16 06:05 | correction 1: author | `the-way-author` (resumed), opus | `reports/author-correction-handoff.md`, remarks `reports/correction-1-remarks.md` | `reports/author-correction-report.md` (expected) | resumed in the background |
| 2026-11-16 06:20 | correction 1: author returned | the-way-author (resumed), opus | `reports/author-correction-report.md` | commit `d48638a` (range `b679864..d48638a`), `foundations/decisions.md` +42 −14, status `done` | Mechanical read: tree clean, range non-empty, one file; check with command and exit code; unread: m3l5 note in part, roadmap skill in part, reviewers' reports (the handoff quotes their places). The author found a taking for all three entries (each now derives from WAY-100, names its practice, says the lessons are closed, lists leftovers) and names a contradiction: the frozen task's *Out of scope* calls WAY-139 evidence-only and the second round of the log removed its `derives from WAY-100`; the human's remark names WAY-139 and the author followed it → goes to the request, *You accept by merging*. Searches unclear (WAY-165's other matters may come from the lesson on autonomous product development) → process remarks |
| 2026-11-16 06:30 | correction 1: review and the unread reading | `the-way-stage`, opus, a fresh reviewer (not the author of either earlier review) | `reports/review-correction-handoff.md`, remarks `reports/correction-1-remarks.md`, range `b679864..d48638a` | `reports/review-correction-report.md` (expected) | dispatched in the background; part B is item 2 of the remarks |
| 2026-11-16 07:00 | correction 1: review returned | `the-way-stage`, opus (fresh) | `reports/review-correction-report.md` | `PASS d48638a7d493c4913be74d08477c3eb2f4d35906`; no blocking finding; 6 Minor (M1–M6, Part A 5, Part B 1) → the request's list, not fixed; 1 outside the scope (O1, two spellings of the course's name in the log); Part B: WAY-256 read whole agrees with the addition; the lesson notes of m2l4 and m3l5 read whole agree with the leftovers and reasons of WAY-268, 270, 273 save M6 | Mechanical read: checks with commands and exit codes, unread material and searches present. Remark 2 done by Part B. Unread: skill `10x-roadmap` in part, m1l5 note one section, m2l1 note — bear on nothing the reviewer judged beyond its stated limits |
| 2026-11-16 07:10 | correction 1: return step | `the-way-author` (resumed), opus | `reports/author-correction-return-step-handoff.md`, `task-cycle/skill/return_step.md` | `reports/author-correction-return-step-report.md` | status `done`, no commit, head stays `d48638a`; nothing no longer matched; no entry written. Next: the gate on the corrected tree after the day advisor's start signal |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | Which class of model for the one author? Skill step 4 | `strongest`, model `opus` | the change needs judgment on sources; the human's instruction names `opus` as the strongest allowed model | `cheaper`: a missed or invented source is the very fault the task removes | the cost of a rerun of the author | author dispatch |
| Q2 | May the author read the author's private vault and the web? Task *To do* 1 | yes, reading only; no path or note link of the vault reaches a commit | task *To do* 1 and WAY-27, WAY-140 | no vault reading: the sources of the seven decisions are found only by it | a private path in the history of a public repository | author handoff |
| Q3 | Does the author or any agent run the product's full gate? The human's instruction in the command | no agent runs it; the orchestrator writes that the full gate is about to start and waits for the signal `start` of the day advisor before each full run | the command's arguments | running it without the wait | a run on a machine the advisor keeps for another task | step 10 |
| Q4 | The author left the data file of the foundation review (P7) unopened and read the lesson notes and the skill `10x-roadmap` in part. Skill, reports' unread material | carry the gap to the reviewer of the whole change, who can judge it (handoff item 7); no resumption of the author | P7's conclusion on WAY-136 is quoted in the task's *Context*; the author's trace (item P30 of the author's plan) settled WAY-136 and WAY-148 | resume the author to read them: the reviewer reads them independently, which costs less and is not anchored on the author's reading | a wrong evidence-only judgment on WAY-136 would leave the decision without its practice named | review of the whole change |
| Q5 | Correction 1: the human's remark names WAY-139 among the three decisions to fix, while the frozen task's *Out of scope* lists it as evidence-only and the second round of the log removed its `derives from WAY-100`. Remarks, task | follow the remark (it binds and the trace supports it): WAY-139 now names its practice and derives from WAY-100; the contradiction is shown in the request's *You accept by merging* | the author's trace (map rows m1l5 and m3l5 carry the list to WAY-139; the second round removed the relation because the text then named no practice); the fresh reviewer judged the fix true to the source (`reports/review-correction-report.md`, check 3) | leave WAY-139 as it was: the remark names it, and the next review of the foundation would report the gap again | the human finds the earlier judgment of the second round reversed without having been asked | correction 1 |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| frozen task | `task.md` beside this record | orchestrator | none |
| code commit | `05b4648` (the whole change), `foundations/decisions.md` only | `the-way-author`, opus | review of the whole change `FAIL`, one blocking finding |
| code commit | `01ab269` (the fix of the review's findings) | `the-way-author`, opus (resumed) | review of the fix `PASS` |
| reports | `reports/author-report.md`, `review-whole-report.md`, `author-fix-report.md`, `review-fix-report.md`, `author-return-step-report.md`; handoffs `*-handoff.md`; `reports/review-whole-findings.md` | agents and orchestrator | — |
| gate log | `final-gate.log`, `gate_times.md`, `stages.md`, `mechanism_measures.md` | orchestrator | — |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| list of tests failing before the change, from the final gate of the merged branch's cycle: `docs/task-cycles/small-fixes-after-prs-117-121/cycle.md` as added by commit `7e7b891` (base is a merge commit, no gate on the base), *Verification* row of the gate on the corrected head `5cb2e1f` | orchestrator, read from git history | the gate exited 0 — 1600 tests in 11 directories, every directory passed | none failing on the base |
| `python -B task-cycle/gate_times.py --output .runs/task-cycles/decision-sources-and-leftouts/gate_times.md -- python -B gate/run_tests.py` on the final code head `01ab269`, started after the day advisor's start signal (message of the session `doradca-dnia`: "start — uruchom pełną bramkę"; 160 GB free) | orchestrator, Windows | 0 — 1600 tests in 11 directories, every directory passed; 387.451 s; log `final-gate.log` | none failed |
| `python -B elements/common/foundation_check.py` without `--skip-test-citations` | orchestrator, `01ab269` | exit 0, `0 errors`, no `listed:` line | none |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator | exit 0 — tag foundation-review/2026-11-15, merges 11, threshold 60, `reminder: no` | none |
| target branch merged into the task branch: `git fetch origin`; `origin/foundations` is `aba5ee9`, already contained | orchestrator | no merge needed, so no review of a merge and no second gate: the final tree is the one step 10 checked | none |
| `python -B task-cycle/cycle_stages.py --output … stages.md` and `cycle_measures.py --output … mechanism_measures.md` naming this session | orchestrator | 0 and 0 | none |
| `python -B task-cycle/remarks_check.py .runs/task-cycles/decision-sources-and-leftouts` on the original | orchestrator | run 1 exit 1 (9 items listed, appended to the process remarks), run 2 exit 0 (2 runs) | none |
| `python -B task-cycle/request_check.py … --task …` and `private_paths_check.py` on the description | orchestrator | exit 0 and exit 0 (2 runs each; the second after the edit that added the record's link and the checks) | none |
| `private_paths_check.py` on the copy of the record (2 runs: 13 listed, then 0; last exit 0), `image_files_check.py` (1 run, exit 0), `remarks_check.py` on the copy (1 run, exit 0) | orchestrator | as stated | none |
| CI on the request (`gh pr checks 139 --watch`) | GitHub Actions, head `b679864` (the commit that removes the record); the run on `01ab269` was cancelled by the next push | job `tests`: success, 1 m 15 s, run 43795872801 | none |
| `python -B task-cycle/gate_times.py --output .runs/task-cycles/decision-sources-and-leftouts/gate_times.md -- python -B gate/run_tests.py` on the corrected code head `d48638a` (correction 1), started after the day advisor's start signal (message of the session `doradca-dnia`: "start — uruchom pełną bramkę"; 159 GB free) | orchestrator, Windows | 0 — 1600 tests in 11 directories, every directory passed; 438.931 s; log `final-gate-2.log` | none failed |
| `python -B elements/common/foundation_check.py` without `--skip-test-citations` (correction 1) | orchestrator, `d48638a` | exit 0, `0 errors` | none |
| `python -B task-cycle/review_reminder.py origin/foundations` (correction 1) | orchestrator | exit 0 — merges 11, `reminder: no` | none |
| target branch refresh for correction 1: `git fetch origin`; `origin/foundations` is `aba5ee9`, already contained in the task branch | orchestrator | no merge, so no review of a merge | none |
| `python -B task-cycle/cycle_stages.py` and `cycle_measures.py` naming this session, rerun after the correction | orchestrator | 0 and 0 | none |
| `python -B task-cycle/remarks_check.py` on the original after correction 1 | orchestrator | run 1 exit 1 (3 items listed, appended), run 2 exit 0 (2 runs) | none |

## Return step

_Correction 1 repeated the step for the three entries it changed (WAY-139, WAY-145, WAY-165): `reports/author-correction-return-step-report.md` — every file that names them still matches, `derives from WAY-100` has the form the template gives, no test holds a sentence of them by a line `decision:`, the part `decisions` still matches; nothing corrected, no commit, no entry written, no review needed. The first step's result follows._

- Foundation compared with code: `reports/author-return-step-report.md` — WAY-100 and the other changed decisions compared with `elements/decisions/template.md`, `elements/common/rules.md`, `elements/environment-facts/template.md`, `agent-instructions/README.md` and a search of every tracked `*.md` for WAY-100's wording and the changed decisions' numbers; no test holds a sentence of the changed decisions by a line `decision:`; the part `decisions` of the part map matches; nothing no longer matched, so nothing was corrected and the step committed nothing (head stays `01ab269`; no review of it).
- Decisions written or changed: none in this step (the change itself wrote WAY-100 and changed 24 more, in `05b4648` and `01ab269`)
- Invariants written or changed: none
- Environment facts: none — the two citations the change added (Limen `templates/worker.md` line 25; Open Mercato `customers/AGENTS.md` line 7) are places a practice was taken from, and fail WAY-90's test
- Glossary terms: none
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: rows 1 and 2 → WAY-100 (second binding paragraph), by the foundation step in `05b4648`

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/139 — draft at first, to be marked ready after CI
- Description: `request.md` beside this record, written by `task-cycle/skill/request_template.md`; form check `python -B task-cycle/request_check.py .runs/task-cycles/decision-sources-and-leftouts/request.md --task .runs/task-cycles/decision-sources-and-leftouts/task.md` exit 0 (1 run), `python -B task-cycle/private_paths_check.py` on it exit 0 (1 run); to be checked again after the edit that adds the record's link and the checks
- Writes to the task's backlog entry: none
- Working copies left: none
- Directories of earlier tasks kept: four directories that the script of step 4 kept —
  - `agent-path-to-running-product` | `task/agent-path-to-running-product` | the branch has no merge git can see on origin/foundations: not merged, merged by squash or rebase, or its request open or closed
  - `audit-answers-contradiction-after-code` | `task/audit-answers-contradiction-after-code` | the branch has no merge git can see on origin/foundations: not merged, merged by squash or rebase, or its request open or closed
  - `base-check-stage-remarks` | detached | the branch task/stage-remarks its name gives is not found
  - `base-fix-minor-findings` | detached | the branch task/minor-findings its name gives is not found
- Corrections after the request opened:
  - correction 1, remarks `reports/correction-1-remarks.md`: `item 8 · not-required`, `item 14 · defect`
- Process remarks on the-way:
  - author, `.runs/task-cycles/decision-sources-and-leftouts/reports/author-report.md`: WAY-145 (who places an open question after the readiness gate): the map of the course carries its row "Blokery zewnętrzne…" ("przejmuję w zmienionej postaci", take in changed form) to WAY-145, yet WAY-145 has *Based on* `none`, no `derives from WAY-100` and no sentence naming the practice. It stands on no list of the task, so I changed nothing; it looks like the same gap as WAY-136 had. Recommendation: a task of its own, or the orchestrator's call whether this cycle should take it.
  - author, `.runs/task-cycles/decision-sources-and-leftouts/reports/author-report.md`: Whether the course skill `10x-roadmap` is open to a reader: it comes in the course's package for the lesson (fetched with the course's CLI); I treated it as course material that a reader cannot open, as the task's answer to question 3 treats the lessons. Not verified against the CLI's terms.
  - author, `.runs/task-cycles/decision-sources-and-leftouts/reports/author-report.md`: WAY-121's lesson "Towards Autonomous Product Development": the author's note on it records a public-looking address on mega.dev; I followed the task (question 3: the lessons are not public) and did not check the page.
  - author, `.runs/task-cycles/decision-sources-and-leftouts/reports/author-report.md`: WAY-164: the commit `e746877` the review-loop task names is a short hash; `gh api` resolved it to `e746877e8ef195ab9a34a070bdd3b000d0b6cf10` (2026-10-17). The line number 25 holds at that commit.
  - author, `.runs/task-cycles/decision-sources-and-leftouts/reports/author-report.md`: WAY-236: the archived copy named in *Based on* was not fetched; the live page was, and its passages match the two quoted ones word for word.
  - author, `.runs/task-cycles/decision-sources-and-leftouts/reports/author-report.md`: No decision of either list was left without a found source: no `TODO` stays.
  - review of the whole change, `.runs/task-cycles/decision-sources-and-leftouts/reports/review-whole-report.md`: `elements/decisions/` holds no test (`gate/run_tests.py elements/decisions`: "no test found").
  - review of the whole change, `.runs/task-cycles/decision-sources-and-leftouts/reports/review-whole-report.md`: Whether the course skills `10x-roadmap` and `10x-plan-review` are open to a reader: I treated them as course material that a reader cannot open, as the author did. Not verified against the course's terms.
  - review of the whole change, `.runs/task-cycles/decision-sources-and-leftouts/reports/review-whole-report.md`: Whether the lesson of WAY-121 is public: settled by the human's answer to question 3, not checked (see Declined to judge).
  - correction 1, author, `.runs/task-cycles/decision-sources-and-leftouts/reports/author-correction-report.md`: The lesson "Towards Autonomous Product Development" behind WAY-121 may also be where WAY-165's other matters (interface, development data) come from; WAY-121 already credits that lesson for them, and WAY-165 derives from WAY-121, so I credited WAY-165 only with what the trace ties to it (the record's life, from m3l5).
  - correction 1, review, `.runs/task-cycles/decision-sources-and-leftouts/reports/review-correction-report.md`: The skill's new questions (Step 6f, "surfaced during Step 5") come from the interview, which runs before the breakdown. Whether "a question that arises in the breakdown" is that practice's element or the-way's own is a matter of reading. The map files it under the taking "in changed form", and I accepted that.
  - correction 1, review, `.runs/task-cycles/decision-sources-and-leftouts/reports/review-correction-report.md`: The author's map gives "*Review when* ↔ sygnał zmiany decyzji" as the-way's equivalent. That field is withdrawn (WAY-119), so this part of the map is out of date. It does not change any verdict.

# Cycle record — the way: decyzja, że samo the way odchodzi od wytycznych kodowania i testów

- Task source: the task document in the author's private backlog, approved 2026-11-11; its frozen copy is `task.md` beside this record
- Task relation: independent
- Product repository: the-way (github.com/mariusznazar/the-way)
- Process pin: not applicable — the-way itself, checkout of the worktree
- Target branch and base: `foundations`, `e3825a8`
- Task branch: `task/guidelines-departure` (worktree `.runs/worktrees/guidelines-departure`)
- Status: request open

## Two questions at start

- Trust boundary: no — the change edits `foundations/decisions.md` (part `decisions`, *Trust boundary* none in `foundations/part_map.md`).
- Irreversible operation: no.

## Spec and execution route

- Open design choice at start: none — both rows of *Settlements to record* settle the entry (WAY-134, WAY-135); whether rows 1 and 2 become one entry or two is a choice of how to make what the task settles, left to the author.
- Reserved choice: none
- Execution route and reason: one author without a plan — one new decision entry (or two) in one file, one part, no code.
- Author: general-purpose agent, class `same` (sonnet): the entry binds 16 parts and needs the author's search of the whole foundation (WAY-33), more than the ordinary implementation `cheaper` stands for.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: Claude Code `Agent` call, foreground; completion notification.
- Whole-change review: reviewer other than the author, `the-way-review-change`; range e3825a8..7442841; `PASS 7442841…` (`reports/review-whole-report.md`); decisions.md +47/-0; covers *To do* item 1, rows 1 and 2 and source fidelity; counts 21 decisions read whole, 7 in part, ~257 by title
- Review rounds: none blocked. The review of the whole change passed with 4 Minor findings within the task; one fix (b4bfca8) and one review of it (`PASS b4bfca8…`): 4 fixed, 1 new Minor left for the request
- Weakest-point checks: author: *Scope* equal to the 16 parts of the part map — a script compared the sets, True (author-report.md)

## Slices

Not applicable (one-author route).

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-11 | start | orchestrator (sonnet 5.5) | task read; checkout at origin/foundations e3825a8, clean; worktree and branch created | — | base gate started in `.runs/base-check-guidelines-departure` (output `base-gate.txt` beside this file) |
| 2026-11-11 | one author | general-purpose, sonnet (same) | `reports/author-handoff.md`; `the-way-make-change`, whole change as the one author | `reports/author-report.md`; commit 7442841 (decisions.md +47, WAY-327) | `done`; foundation_check exit 0; mechanical check passed (clean tree, non-empty range, only decisions.md); Unread material read: WAY-03 not read, bears on nothing judged (form is checked by foundation_check and by the review) — autonomous choice Q2; next: review of the whole change |
| 2026-11-11 | whole-change review | reviewer, sonnet (same) | `reports/review-whole-handoff.md`; `the-way-review-change`, range e3825a8..7442841; gap of the author's unread decisions of Scope `decisions` carried | pending | dispatched |
| 2026-11-11 | whole-change review result | reviewer | `reports/review-whole-report.md` | `PASS 7442841…`; 0 blocking; 4 Minor within the task; 1 out of scope; unread: 8 decisions by title (WAY-150, no gap); foundation_check exit 0 | Minor findings go to one fix (reports/fix-findings.md) and one review of it (WAY-161); author resumed |
| 2026-11-11 | fix of the Minor findings | author (resumed), sonnet | `reports/fix-findings.md` | `reports/fix-report.md`; commit b4bfca8 | `done`; foundation_check exit 0; Unread none, Searches none; next: review of the fix |
| 2026-11-11 | review of the fix | reviewer (resumed), sonnet | range 7442841..b4bfca8 | `reports/review-fix-report.md` | `PASS b4bfca8…`; 4 Minor fixed; 1 new Minor within the task (not fixed: wider wording of the third sentence), goes to the request; foundation_check exit 0 |
| 2026-11-11 | return step | author (resumed), sonnet | `reports/return-handoff.md` | `reports/return-report.md` | `done`, no commit, nothing to correct; Unread: record_template, README, part_map read in part — bears on nothing judged (autonomous choice Q4); no review of the return step (nothing committed) |
| 2026-11-11 | gate | orchestrator | `python -B gate/run_tests.py` in the task worktree at b4bfca8, started in background | `final-gate.txt` | exit 0; 864 tests in 9 directories passed; nothing failed or unrun |
| 2026-11-11 | correction: input | orchestrator | the human's remark in conversation: fix the finding of item 1 in this request, and resolve the conflicts after the merge of two other tasks | — | merged `origin/foundations` (024f486) into the branch: one conflict in decisions.md (both sides added WAY-327); kept the other side's WAY-327, renumbered this entry WAY-328; merge commit 66cc61d, foundation_check exit 0; next: review of the merge |
| 2026-11-11 | review of the merge | fresh reviewer, sonnet | `reports/merge-review-handoff.md` | `reports/merge-review-report.md` | `PASS 66cc61d…`; 0/0/0 findings; foundation_check exit 0; unread: the two earlier review reports, parts of the merged side — bears on nothing it judged |
| 2026-11-11 | correction | author (resumed), sonnet | `reports/correction-remarks.md` | `reports/correction-report.md`; commit 062b772 | `done`; third binding sentence per discipline; foundation_check exit 0 |
| 2026-11-11 | review of the correction | reviewer (resumed), sonnet | range 66cc61d..062b772 | `reports/correction-review-report.md` | `PASS 062b772…`; 0 Critical/Important; 1 new Minor (7) left for the request: long sentence, and the per-discipline meaning is the orchestrator's choice |
| 2026-11-11 | return step after the correction | author (resumed), sonnet | message naming `return_step.md` | `reports/return-report-2.md` | `done`, no commit, nothing no longer matched; foundation_check exit 0 |
| 2026-11-11 | gate on the corrected tree | orchestrator | `python -B gate/run_tests.py` at 062b772, once after the return step | `final-gate-2.txt` | exit 0; 913 tests in 9 directories passed |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | Class of the author's model (step 4) | `same` as the orchestrator | the entry binds 16 parts and needs WAY-33's search | `cheaper` default | a weaker entry caught by the reviews, one fix | author |
| Q2 | The author's report: WAY-03 unread (step 'Unread material') | the gap bears on nothing the author judged; the reviewer selects its own foundation | form of an entry is fixed by the template, 5 decisions read whole and foundation_check exit 0 | resume the author to read WAY-03 | form deviation caught by review | whole-change review |
| Q3 | Rows 1 and 2 as one entry or two (author's choice under the template) | one entry, WAY-327; row 2 is its second binding sentence | author report; review of the whole change judged it sound | two entries | a reviewer splits it, no other entry refers to either | whole-change review |
| Q4 | Return report: parts of record_template, README, part_map read in part | the gap bears on nothing it judged; no commit came of the step | the step compared entries and found nothing to correct | resume the author to read them whole | a missed mismatch the gate or request reading shows | return step |
| Q5 | The human gave no meaning for withdrawing the decision when only one discipline's guidelines are written (correction) | per discipline: one discipline's guidelines take it out, both withdraw the decision | WAY-217 applies a departure to the work it expressly covers; reviewer's finding 6 | both-or-nothing wording from the reviewer's suggestion | a task writing one discipline leaves the other released or withdraws too much; one sentence to edit | correction |
| Q6 | Does the correction also take the outside-scope finding on kinds of code (WAY-216)? | no: the reviewer marked it outside the task's scope and the remark named the first matter | request item 1 asked to fix 'the first' | fixing both | a design choice of the departure not in the task's rows | correction |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| frozen task | `task.md` | orchestrator | — |
| foundation entry WAY-328 (first WAY-327) | commits 7442841, b4bfca8, merge 66cc61d, correction 062b772 | author | `PASS` (whole change, then fix) |
| reports | `reports/author-report.md`, `reports/review-whole-report.md`, `reports/fix-report.md`, `reports/review-fix-report.md`, `reports/return-report.md` | agents | see Events |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| `python -B gate/run_tests.py` on the base (`base-gate.txt`) | orchestrator, `e3825a8`, separate checkout `.runs/base-check-guidelines-departure` | exit 0; 864 tests in 9 directories passed | none failed; none unrun |
| `python -B gate/run_tests.py` on the final tree (`final-gate.txt`, before the correction) | orchestrator, `b4bfca8`, task worktree | exit 0; 864 tests in 9 directories passed | none failed; none unrun |
| `python -B gate/run_tests.py` on the corrected tree (`final-gate-2.txt`), once after the return step | orchestrator, `062b772`, task worktree | exit 0; 913 tests in 9 directories passed | none failed; none unrun |
| `python -B elements/common/foundation_check.py --skip-test-citations` | author, reviewers, return steps; `7442841`, `b4bfca8`, `66cc61d`, `062b772` | exit 0; 0 errors | none |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator | `reminder: no` (19 merges, threshold 30) | none |
| `python -B task-cycle/remarks_check.py` on the original | orchestrator | 2 runs: exit 1 listing 9 items, then exit 0 after appending them | none |

## Return step

- Foundation compared with code: WAY-327, WAY-215, WAY-217, WAY-209, WAY-244, WAY-173, WAY-09, the part map and the reading of guidelines compared with the repository's files: nothing no longer matched; none corrected
- Decisions written or changed: WAY-327 (written in the foundation step, fixed once; renumbered WAY-328 by the merge with the target branch; its third binding sentence corrected for the human's remark) — second return step (`reports/return-report-2.md`) after the correction: nothing no longer matched, no commit
- Invariants written or changed: none
- Environment facts: none
- Glossary terms: none
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: row 1 and row 2, both as WAY-328

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/98 — ready for review
- Description: `written and checked after this commit`
- Writes to the task's backlog entry: the request link, written after the request opened; none since
- Process remarks on the-way:
  - one author, .runs/task-cycles/guidelines-departure/reports/author-report.md: No `guidelines/` directory and no decision on a departure for the-way found in the log, as the task's *Context* says (confirmed by grep for "depart").
  - one author, .runs/task-cycles/guidelines-departure/reports/author-report.md: Unclear: `elements/decisions/skill/SKILL.md` step 3 says *Verification* names invariants "those step 4.4 writes"; I wrote none, so *Verification* holds only the pair of examples, a form the template allows.
  - one author, .runs/task-cycles/guidelines-departure/reports/author-report.md: The handoff's selection step 1 (decisions whose *Scope* names `decisions`) I did not run in full: the decisions I read by identifier and by the search above were enough for this entry, but I did not read whole every decision whose *Scope* names `decisions`.
  - review of the fix, .runs/task-cycles/guidelines-departure/reports/review-fix-report.md: none found missing.
  - review of the fix, .runs/task-cycles/guidelines-departure/reports/review-fix-report.md: Unclear: whether row 1's "własne wytyczne" means both disciplines together or either one (finding 6).
  - whole-change review, .runs/task-cycles/guidelines-departure/reports/review-whole-report.md: Not found: a `guidelines/` directory; any decision before WAY-327 that departs from guidelines for the-way itself (matches the task's *Context*).
  - whole-change review, .runs/task-cycles/guidelines-departure/reports/review-whole-report.md: Not found: any statement in `agent-instructions/` about guidelines (no match; the README defines the integration route only).
  - whole-change review, .runs/task-cycles/guidelines-departure/reports/review-whole-report.md: Unclear: whether the handoff's "part `decisions`" or the WAY-44 rule (all 16 parts) is the intended selection; I took the second and report the cost above.
  - whole-change review, .runs/task-cycles/guidelines-departure/reports/review-whole-report.md: Unclear: out-of-scope finding 5 (kinds of code under WAY-216).
  - review of the correction, .runs/task-cycles/guidelines-departure/reports/correction-review-report.md: Unclear: whether the human wants the per-discipline meaning or "both or nothing" (finding 7).
  - review of the merge, .runs/task-cycles/guidelines-departure/reports/merge-review-report.md: The handoff names `b4bfca8` as a parent of the merge; the first parent is `dae4cf9` (explained above).
  - review of the merge, .runs/task-cycles/guidelines-departure/reports/merge-review-report.md: A search of the merged side's log diff for text about departures from guidelines found nothing; this is the expected result and was a search for a contradiction, not for a thing that should exist.
  - review of the merge, .runs/task-cycles/guidelines-departure/reports/merge-review-report.md: Otherwise none.
  - review of the correction, .runs/task-cycles/guidelines-departure/reports/correction-review-report.md: none found missing.

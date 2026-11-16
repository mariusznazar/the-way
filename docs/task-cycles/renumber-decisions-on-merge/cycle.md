# Cycle record — the way: renumbering the decisions of a task at the merge of the target branch, when a parallel task took the same numbers

- Task source: `the task document in the author's private backlog notes`; *Settlements to record* accepted 2026-11-14; frozen copy `.runs/task-cycles/renumber-decisions-on-merge/task.md`
- Task relation: independent
- Product repository: the-way (github.com/mariusznazar/the-way)
- Process pin: not applicable (the-way itself, the checkout is the process)
- Target branch and base: `foundations`, `1feb483cbb5a6538a475d6e42629441ba563d7f8` (merge commit of request #141)
- Task branch: `task/renumber-decisions-on-merge`
- Status: request open

## Two questions at start

- Trust boundary: no — the change touches `task-cycle/skill/SKILL.md`, `task-cycle/skill/correction.md` and `foundations/decisions.md`; the part map's trust boundary of `task-cycle` is `cycle_stages.py`, `cycle_measures.py` and `gate_times.py`, none of which the task names
- Irreversible operation: no — text of a skill and a decision entry only

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none — the four *Questions to settle* are answered with their rejected ways and the source, *Settlements to record* rows 1 and 2 settle the decision and where the conversion stands; where the rule stands in the skill (step 12) and in `correction.md` follows from the task's *To do* 1–4; no reserved choice
- Reserved choice: none
- Execution route and reason: one author without a plan — three files of text (two skill files and the decision log) plus the search of the foundation for entries the new decision touches (WAY-33); no code, no slice-size question
- Author: `the-way-author`, class `same` (sonnet): the change writes a decision entry whose form `foundation_check.py` holds, with rejected ways, a pair of examples or a holding test, and a search of the whole foundation, which asks for more than the default `cheaper` class does; resumed for the fix and the return step
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: completion notification of the background agent; no limit reached
- Whole-change review: dispatched 10:00, `the-way-stage` on opus; range `1feb483..34db268`
- Review rounds:
  - findings `reports/review-whole-findings.md`: review of the whole change `FAIL 34db2685` (`reports/review-whole-report.md`), blocking I-1 and I-2, Minor M-1; fix `059b891`, review of the fix `PASS 059b891` (`reports/review-fix-report.md`); one new Minor N-1 left for the request's list
- Weakest-point checks: the author's: the one pass on an overlapping map (`reports/author-passcheck.py`), and after the fix the count check on an overlapping map and on a second renumbering (`reports/author-fix-passcheck.py`); the reviewer's: a scratch run of steps 2 and 3 that showed I-1 and I-2, and 20 000 random maps after the fix

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-16 09:00 | start | orchestrator, Sonnet 5.5 | `/the-way-implement-task`; the task document | — | the checkout was 10 commits behind `origin/foundations`; fast-forwarded `30c947f` → `1feb483` (clean tree, on the branch, no local commits); `task-cycle/skill/SKILL.md` and `agent-instructions/README.md` did not change in them, so the skill was not read again |
| 2026-11-16 09:05 | start | orchestrator | `python -B task-cycle/remove_merged_worktrees.py --target foundations`, then `--apply` | removed `relations-todo-for-unwritten-decision` | dry run exit 0, apply exit 0; one directory kept (see *Directories of earlier tasks kept*) |
| 2026-11-16 09:10 | start | orchestrator | `git worktree add --no-track -b task/renumber-decisions-on-merge` from `1feb483` | worktree `the-way-wt/renumber-decisions-on-merge` | the base is a merge commit with the tree of its second parent (`679dd48b`), so no gate on the base; the list of failing tests taken from the merged cycle's record |
| 2026-11-16 09:15 | user's rule for this cycle | orchestrator | the human's command arguments | — | (1) before every full run of the gate on this system the orchestrator writes it to the human and waits for the start signal of the day's advisor; the final gate is the CI run (step 10), so no such run is planned; (2) the strongest model the session allows is `opus`: reviewers of the strongest class are dispatched with `model: opus`, never `fable` (a `fable` subagent takes the session's model) || 2026-11-16 09:30 | one author | `the-way-author`, sonnet (class `same`), background | `reports/author-handoff.md`; `task-cycle/change/SKILL.md` variant "the whole change as the one author", `task-cycle/skill/foundation_step.md`; the frozen task | `reports/author-report.md` (expected) | dispatched; waits by completion notification |
| 2026-11-16 09:55 | one author | `the-way-author`, sonnet | `reports/author-handoff.md` | `reports/author-report.md`, status `done`, commit `34db268` | mechanical check: clean worktree, range `1feb483..34db268` holds one commit, 4 files (`foundations/decisions.md`, `task-cycle/skill/SKILL.md`, `task-cycle/skill/correction.md`, `task-cycle/record_template.md`), commands and exit codes present, own-work check present, unread and searches sections present; the author read WAY-135 to its first paragraph only: carried to the reviewer of the whole change (autonomous choice: the cycle wrote no spec, so WAY-135 probably bears on nothing the author judged; the reviewer reads it whole) |
| 2026-11-16 10:00 | whole-change review | `the-way-stage`, opus (strongest allowed; `fable` is disabled) | `reports/review-whole-handoff.md`; `task-cycle/review/SKILL.md` | `reports/review-whole-report.md` (expected) | dispatched in the background |
| 2026-11-16 10:15 | whole-change review | `the-way-stage`, opus | `reports/review-whole-handoff.md` | `reports/review-whole-report.md`: `FAIL 34db2685`; 2 Important (I-1 step-3 check fails on overlapping maps, I-2 rewriting an earlier conversion row corrupts it), 1 Minor within the task (M-1), 0 out of scope; WAY-135 read whole, no spec needed; unread material none; the author's four choices: three accepted, the fourth split (commit in the merge review's range accepted, the rewrite of an earlier row is I-2) | findings file `reports/review-whole-findings.md` written in the reviewer's words (blocking findings, then the Minor finding); the author is resumed for the one fix |
| 2026-11-16 10:20 | fix | `the-way-author`, sonnet (resumed, class `same`) | `reports/author-fix-handoff.md`; `reports/review-whole-findings.md` | `reports/author-fix-report.md` (expected) | dispatched |
| 2026-11-16 10:40 | fix | `the-way-author`, sonnet (resumed) | `reports/author-fix-handoff.md`; `reports/review-whole-findings.md` | `reports/author-fix-report.md`, status `done`, commit `059b891` | mechanical check: clean worktree, range `34db268..059b891` one commit, 2 files, commands and exit codes present, own-work check present, unread (full review report not read; the findings file covers it) and searches sections present; I-2 solved by leaving earlier conversion rows as written (rejected: rewriting only the right side) |
| 2026-11-16 10:45 | review of the fix | `the-way-stage`, opus (resumed reviewer, the same as the whole-change review) | `reports/review-fix-handoff.md`; `reports/review-whole-findings.md` | `reports/review-fix-report.md` (expected) | dispatched |
| 2026-11-16 10:55 | review of the fix | `the-way-stage`, opus (resumed) | `reports/review-fix-handoff.md` | `reports/review-fix-report.md`: `PASS 059b891f`; I-1, I-2, M-1 fixed; one new Minor N-1 (two rows may hold one number with two meanings after two renumberings; not fixed, goes to the request's list); the reviewer notes that leaving an earlier conversion row as written is a choice beyond the task's text, for *You accept by merging* | no third round; step 10: the final gate is the CI run on the request's last head, no local full gate |
| 2026-11-16 11:00 | return step | `the-way-author`, sonnet (resumed, class `same`) | `reports/author-return-step-handoff.md`; `task-cycle/skill/return_step.md`, `foundation_step.md` | `reports/author-return-step-report.md` (expected) | dispatched |
| 2026-11-16 11:20 | return step | `the-way-author`, sonnet (resumed) | `reports/author-return-step-handoff.md` | `reports/author-return-step-report.md`, status `done`, no commit | nothing no longer matched; gaps of reading (glossary and invariants by headings, part map in part) judged as bearing on nothing, see Q11; no review of the return step since it committed nothing |
| 2026-11-16 11:25 | target branch | orchestrator | `git fetch --tags origin` | `origin/foundations` is still `1feb483` | no merge, no renumbering, no review of a merge, no second gate |
| 2026-11-16 11:30 | request | orchestrator | `request.md`; `request_check.py` exit 0, `private_paths_check.py` exit 0 | https://github.com/mariusznazar/the-way/pull/142 (draft) | branch pushed; step 13 `review_reminder.py`: 14 merges, `reminder: no`; foundation check without `--skip-test-citations` on `059b891`: exit 0, 0 errors; next: the record's pair of commits, then the wait for CI |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | The task's *Decisions in play* names WAY-306, WAY-357 and WAY-328; are they in force? Source: step 1, reconciliation of the task with the foundation | They are withdrawn in the log since the task was accepted: WAY-306's rule stands in `task-cycle/skill/correction.md`, WAY-357's in `task-cycle/record_template.md`, WAY-328 ended (WAY-379, WAY-392 replace it). The task needs no change: the change cites them as places, not as decisions; the new decision's *Relations* name only live entries | `foundations/decisions.md` table of withdrawn identifiers, lines 10719, 10753, 10730 | stop the cycle: the required outcome is still established | a *Relations* link to a withdrawn number fails the foundation check | author handoff |
| Q2 | Next free number of the new decision (WAY-19) | WAY-403 (the log's highest is WAY-402); another running cycle may take it, which is the case the task's rule serves | `foundations/decisions.md` read at `1feb483`; open request #138 on another branch | a placeholder number | a collision at the merge, which the new rule and the author's search settle | author handoff |
| Q3 | Author's class (step 4, WAY-229) | `same` (sonnet) | see *Author* | `cheaper` by default | a weaker entry caught by the review of the whole change | author dispatch |
| Q4 | WAY-135 read only to its first paragraph by the author: does it bear on the change? | Carried to the reviewer of the whole change, who read it whole: no open design choice, so no spec | `reports/review-whole-report.md`, section WAY-135 | stopping to read it myself | none | review dispatch |
| Q5 | Where does row 2 of *Settlements to record* (where the conversion stands) go? Source: the author's choice 1 | A second paragraph of WAY-403, not an entry of its own | `reports/author-report.md`, *Choices*; accepted by the review of the whole change | a separate entry | one entry split out later, no reference to repair beyond the skill | author |
| Q6 | Where does the procedure stand? Source: author's choice 2 | A new section of `task-cycle/skill/SKILL.md` that step 12 and `correction.md` point to | `reports/author-report.md`; accepted by the review | the procedure inside step 12 | none | author |
| Q7 | Is the renumbering commit in the range of the merge's review? Source: author's choice 3 | Yes | `reports/author-report.md`; accepted by the review | commit left out of the range | a wrong number in the branch's files not seen by the reviewer of the merge | author |
| Q8 | Form of the examples of WAY-403: author's choice 4 | Bare numbers (500 to 504), since the foundation check rejects an invented prefixed number | `reports/author-report.md`; accepted by the review | prefixed numbers | none | author |
| Q9 | An earlier reconciliation's conversion row after a second renumbering (finding I-2): author's fix choice | The row stays as written; the rows are followed one after the other; WAY-403 binds it | `reports/author-fix-report.md`; `PASS` of the review of the fix, which names it a choice beyond the task's text | rewriting only the right side of the earlier row | a reader of an old number follows two rows (Minor finding N-1: which row to start from) | author fix |
| Q10 | How is the pass checked (finding I-1): author's fix choice | By counts: each old number's references before the pass, each new number's after it; a search for an old number is no check where old and new ranges overlap | `reports/author-fix-report.md`; the review of the fix tried 20 000 random maps | search for old numbers | a missed reference not caught | author fix |
| Q11 | The return step's gaps in reading (glossary, invariants, part map only in part): does it bear on anything the author judged? | No: the review of the whole change read the invariants the change could reach whole and found none affected; no entry beyond WAY-403 was written | `reports/author-return-step-report.md`; `reports/review-whole-report.md` | resuming the author to read them whole | an entry that should have been corrected stays | return step |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| frozen task | `.runs/task-cycles/renumber-decisions-on-merge/task.md` | orchestrator | — |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| list of the tests failing before the change, from the final gate of the merged branch's cycle: `docs/task-cycles/relations-todo-for-unwritten-decision/cycle.md` as added by commit `dcd9c30` (the last copy); *Verification* of that copy gives the CI run 43828067871 on `423ed9d`, `tests` and `tests-windows` pass; the base `1feb483` is a merge commit with the tree of that head (both `679dd48b28fa0140a56ba3e6335879c275c88a2f`), so no gate on the base | orchestrator, read from git history | no test failing on the base | none failing |
| step 10: the final gate is the CI run on the request's last head (the repository holds `.github/workflows/tests.yml` that runs on `pull_request`); the cycle has no local time of it and runs no full gate on its own system; its result stands in *Checks* of the request's description and not in the copy of the record | orchestrator | not applicable | the result stands in the CI row once it is written |

## Return step

- Foundation compared with code: WAY-403 against the final text of the skill section and of both merge paragraphs of `correction.md`; WAY-19, WAY-02, WAY-293, WAY-294 and WAY-162; the part map entries `task-cycle` and `decisions`; nothing no longer matched, so no return commit (`reports/author-return-step-report.md`)
- Decisions written or changed: WAY-403 (the cycle's, written in the foundation step)
- Invariants written or changed: none
- Environment facts: none
- Glossary terms: none (renumbering, conversion row and reconciliation take no entry under WAY-95)
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: row 1 and row 2, both in WAY-403 (row 1 its first paragraph, row 2 its second), with their places in step 12, the section "The renumbering of the task's decisions" of `task-cycle/skill/SKILL.md`, `task-cycle/skill/correction.md` and `task-cycle/record_template.md`

The return step corrects in the same change whatever no longer matches. It writes an invariant
only for a rule the task, a decision or the human sets, never for behaviour merely because no
invariant covers it.

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/142, draft (to be marked ready after the CI run)
- Description: `request.md` beside this record; `python -B task-cycle/request_check.py .runs/task-cycles/renumber-decisions-on-merge/request.md --task .runs/task-cycles/renumber-decisions-on-merge/task.md` exit 0 and `python -B task-cycle/private_paths_check.py` on it exit 0 (1 run each before publishing); rewritten after the record's commit with its link and the copy's checks
- Writes to the task's backlog entry: none
- Working copies left: none
- Directories of earlier tasks kept: audit-answers-contradiction-after-code · task/audit-answers-contradiction-after-code · uncommitted changes, commits not on origin, and the branch has no merge git can see on origin/foundations (not merged, merged by squash or rebase, or its request open or closed)
- Corrections after the request opened: none
- Process remarks on the-way:
  - one author, .runs/task-cycles/renumber-decisions-on-merge/reports/author-report.md: The task's *Rejected* items "renumbering the decisions of the target branch" and "a temporary marker in place of a number" keep no reason beside the way in the task document, so the entry's *Rejected* lists them with none (choice 6).
  - one author, .runs/task-cycles/renumber-decisions-on-merge/reports/author-report.md: `task-cycle/skill/SKILL.md` step 12 does not say in what form the orchestrator sees "a new decision of the task branch" — the section I wrote gives it ("the log of the task branch holds it and its log at the merge base does not"); the task's wording did not.
  - one author, .runs/task-cycles/renumber-decisions-on-merge/reports/author-report.md: The handoff says WAY-306, WAY-357 and WAY-328 are withdrawn; confirmed in the withdrawn table (lines of `foundations/decisions.md` ending the file); none is linked.
  - whole-change review, .runs/task-cycles/renumber-decisions-on-merge/reports/review-whole-report.md: `decision_index.py --decision WAY-306` (and WAY-357, WAY-328, named in the task's *Decisions in play*) — not found as entries: withdrawn, as the handoff says; their rules stand in `task-cycle/skill/correction.md` and `task-cycle/record_template.md`.
  - whole-change review, .runs/task-cycles/renumber-decisions-on-merge/reports/review-whole-report.md: Unclear: whether the merge's review in step 12 runs whenever a renumbering ran, since step 12 asks for it only "where that changes the reviewed code" (`SKILL.md:592`). Read as: a renumbering runs only where the target branch added decisions to the log the change also changed, so the merge always changes a reviewed file then; no finding.

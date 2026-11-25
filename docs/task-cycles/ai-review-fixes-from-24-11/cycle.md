# Cycle record — the way: drobne poprawki z przeglądu warstwy AI, zbierane od 24.11 — opis prośby o scalenie poprawiany fragmentem i powiązanie niezmiennika z decyzją, z której wynika

- Task source: the task's note in the author's backlog, `Status: ready for cycle`, accepted 2026-11-25 (Questions 1–4 answered by the day's adviser for the human, 2026-11-25; two settlements accepted the same day); frozen copy `.runs/task-cycles/ai-review-fixes-from-24-11/task.md`
- Task relation: independent
- Product repository: the-way (https://github.com/mariusznazar/the-way)
- Process pin: none (the-way itself; the session's worktree is the process root)
- Target branch and base: `foundations`, `07aa55df` (merge of PR #158)
- Task branch: `task/ai-review-fixes-from-24-11`
- Status: request open

## Two questions at start

- Trust boundary: no — the parts the change touches are `task-cycle` (`task-cycle/skill/request_template.md`), `invariants` (`elements/invariants/skill/write.md`, `elements/invariants/skill/decide_entry.md`), `elements-common` (`elements/common/foundation_check.py` and its test) and `decisions` (`foundations/decisions.md`); the part map lists as their trust boundaries only `task-cycle/cycle_stages.py`, `task-cycle/stage_transcripts.py`, `task-cycle/cycle_measures.py` and `task-cycle/gate_times.py`, none of which the change touches, and `elements-common` and `decisions` have none. The change adds no read of outside data: the check reads the foundation files and git, as it does today.
- Irreversible operation: no

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none — five items of *To do* give the wording of two skill sentences, the check's rule (error where a change adds or alters either entry of the link, a `listed:` line otherwise, the message naming the identifier to add and the decision to add it to), the fifteen links by identifier and the first sentence of a skill paragraph; Questions 1–4 settle the four points the task left open; *Settlements to record* rows 1 and 2 settle the new paragraphs of WAY-30 and WAY-12 (their wording stands under *Decisions in play*). What stays is how to make the check inside the script (beside `check_held`, under WAY-385's size limits) and how to write the two tests, which follow the script's existing checks and tests.
- Reserved choice: none
- Execution route and reason: one author without a plan — one script check with its tests, two sentences of two skill files, one sentence of the request template, two paragraphs of two decisions and the *Verification* lines of three decisions; one agent holds it.
- Author: `the-way-author`, class `same` as the orchestrator's (model `sonnet`); reason for a class other than `cheaper`: the author writes a check inside a script that is held to a size limit and to a base-commit comparison, takes its design decisions of its own (how the change is detected for both entries), and writes two foundation entries (new paragraphs of WAY-12 and WAY-30) through `record-decision`; a cheaper class that fails costs a fix round and a stronger review.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: completion notification of the harness (Claude Code); no limit set by the cycle.
- Whole-change review: `reports/review-whole-2-report.md`, `FAIL 2dca6873` on range `07aa55df..2dca6873` by a fresh reviewer, `the-way-stage` on `opus` (`claude-opus-5-5`), 13 decisions of its index read whole and the index of its whole selection read; changed files at the review: `README.md` 246→248, `agent-instructions/README.md` 136→138, `foundation_check.py` 1115→1193, `test_foundation_check.py` 2519→2648, `decisions.md` 11851→11895, `elements/decisions/template.md`, `elements/invariants/template.md`, the two skill files and `request_template.md`; items 1–5, rows 1 and 2 and Questions 1–4 covered, the fifteen links checked against the invariants' *Derives from*. An earlier review of the same change, `reports/review-whole-report.md`, `PASS 225bf1c5` by `the-way-stage` that ran on `claude-sonnet-5-5` and not on the `fable` asked for (Q1, Q2), one Minor finding fixed in `2dca6873`, its fix `PASS` in `reports/review-fix-1-report.md`; it stands as the earlier review and is superseded by the second, which decides.
- Review rounds:
  - findings `reports/review-whole-findings.md`, contradiction no: review of the whole change `reports/review-whole-report.md`, `PASS 225bf1c5` on `07aa55df..225bf1c5` with one Minor finding within the task (two re-wrapped lines over 100 columns) and one outside the scope (`foundation_check.py` at 1193 of 1200 lines); fix `2dca6873` (range `225bf1c5..2dca6873`, two README lines re-wrapped) by the one author resumed; review of the fix `reports/review-fix-1-report.md`, `PASS 2dca6873`; no blocking finding.
  - findings `reports/review-whole-2-findings.md`, contradiction yes: second review of the whole change `reports/review-whole-2-report.md`, `FAIL 2dca6873` on `07aa55df..2dca6873`; blocking findings I-1 (the check keyed decisions by a zero-padded label; marked as contradicting the third paragraph of WAY-12 and Question 2) and I-2 (*Rejected* of WAY-12 and WAY-30 held ways the rows' sources do not keep; marked as contradicting WAY-134), Minor M-1 (an invariant of the earlier form with a version in its heading got a second line) and M-2 (a wording of the new WAY-30 sentence), both within the task and fixed with them; fix `b87125b6` (range `2dca6873..b87125b6`) by the one author resumed; review of the fix `reports/review-fix-2-report.md`, `PASS b87125b6`, no new finding; no blocking finding remained.
- Weakest-point checks: author — the acceptance criterion and "either entry as a whole, anywhere in the entry": a change of the decision's rationale alone and of the invariant's part alone each turn an old gap into an error (`reports/author-report.md`); the tests seen failing with the call of the new check removed (7 of 19 selected); fix 2 — the two new tests seen failing before the fix (`reports/author-fix-2-report.md`).

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 17:00 | start | orchestrator, Sonnet 5.5 | `/the-way-implement-task`, task document | — | fetch: checkout `foundations` at `07aa55df`, equal to `origin/foundations`, clean; no fast-forward needed |
| 17:02 | step 4, removal of finished tasks | orchestrator | `python -B task-cycle/remove_merged_worktrees.py --apply --target foundations` | — | exit 0; removed the worktree of `installer-foundation-check-full-path`; kept two detached checkouts that belong to no cycle; directories of cycles kept for a human decision: none |
| 17:05 | step 4, branch | orchestrator | `git worktree add --no-track -b task/ai-review-fixes-from-24-11 ../the-way-wt/ai-review-fixes-from-24-11 origin/foundations` | — | worktree created at `07aa55df`; the base is a merge commit whose tree equals that of its second parent (`6bc144e8145bb2f2129d11bb3e1a45731dd3bf71` both): no gate run on the base, the list of failing tests taken from the merged request (see Verification) |

| 17:20 | author (one author, `make-change`, foundation step) | `the-way-author`, model `sonnet` (class `same`) | `reports/author-handoff.md`; `task-cycle/change/SKILL.md`, `task-cycle/skill/foundation_step.md`, frozen task | `reports/author-report.md` | dispatched on base `07aa55df` |

| 17:36 | author returned | `the-way-author` (sonnet) | `reports/author-report.md` | commit `225bf1c5` (10 files, +282/−23: `README.md`, `agent-instructions/README.md`, `elements/common/foundation_check.py` +78, `elements/common/test_foundation_check.py` +129, `elements/decisions/template.md`, `elements/invariants/skill/decide_entry.md`, `elements/invariants/skill/write.md`, `elements/invariants/template.md`, `foundations/decisions.md`, `task-cycle/skill/request_template.md`) | status `done`; clean worktree; non-empty range; checks with commands and exit codes, **Unread material**, **Searches** and own-work check present. Gaps carried to the whole-change reviewer: WAY-14, 33, 150, 02, 379, 382, 385 not read whole; part-map entries, glossary, invariants of `elements-common`/`every` unread. Concerns carried: a pair of examples added to WAY-30's *Verification* beyond row 1; root `README.md` and the two templates edited beyond the five items |
| 17:40 | review of the whole change | `the-way-stage`, model `fable` | `reports/review-whole-handoff.md`; `task-cycle/review/SKILL.md`, `task-cycle/review/whole_change.md`, range `07aa55df..225bf1c5`, frozen task, author report | `reports/review-whole-report.md` | dispatched |

| 17:50 | review of the whole change returned | `the-way-stage` (fable) | `reports/review-whole-report.md` | `PASS 225bf1c5`: 0 blocking, 1 Minor within the task (two wrapped lines over 100 columns in `README.md:94` and `agent-instructions/README.md:24`), 1 out of scope (`foundation_check.py` 1193 of 1200 lines); changed files: README.md +2, agent-instructions/README.md +2, foundation_check.py +78, test_foundation_check.py +129, decisions.md +44, template rows and skill files; the reviewer read 2 decisions whole (WAY-12, WAY-30) and judged none of the rest it left unread as bearing on the change; points (1)–(3) judged within scope | the Minor within the task is fixed before step 10 (WAY-161): fix 1 by the one author, resumed |
| 17:52 | fix 1 | `the-way-author` (sonnet), resumed | `reports/author-fix-1-handoff.md`, findings `reports/review-whole-findings.md` | `reports/author-fix-1-report.md` | dispatched on reviewed head `225bf1c5` |

| 18:00 | fix 1 returned | `the-way-author` (sonnet), resumed | `reports/author-fix-1-report.md` | commit `2dca6873` (`README.md` +2/−2, `agent-instructions/README.md` +2/−2) | status `done`; clean worktree; checks with commands and exit codes, **Unread material** and **Searches** present; words unchanged (word diff empty); no finding held wrong |
| 18:02 | review of fix 1 | `the-way-stage` (fable), resumed | `reports/review-fix-1-handoff.md`, findings `reports/review-whole-findings.md`, fix report `reports/author-fix-1-report.md` | `reports/review-fix-1-report.md` | dispatched on range `225bf1c5..2dca6873` |

| 18:08 | review of fix 1 returned | `the-way-stage` (fable), resumed | `reports/review-fix-1-report.md` | `PASS 2dca6873`: finding fixed, no new finding; the two README paragraphs read word for word as before | step 10: CI runs on the request (`.github/workflows/tests.yml`), so no local full gate; step 11 follows |
| 18:10 | return step | `the-way-author` (sonnet), resumed | `reports/author-return-handoff.md`; `task-cycle/skill/return_step.md` | `reports/author-return-report.md` | dispatched on head `2dca6873` |

| 18:20 | return step returned | `the-way-author` (sonnet), resumed | `reports/author-return-report.md` | no commit; head stays `2dca6873` | status `done`; nothing to correct; **Unread material** and **Searches** present; `foundation_check.py` exit 0, `0 errors`; no review of the return step (it committed nothing); WAY-30's added pair carried to the request word for word |
| 18:25 | step 12 | orchestrator | `git fetch`; `python -B task-cycle/review_reminder.py origin/foundations`; `python -B task-cycle/cycle_stages.py $CLAUDE_CODE_SESSION_ID`; `python -B task-cycle/cycle_measures.py $CLAUDE_CODE_SESSION_ID` | — | `origin/foundations` still at `07aa55df`, an ancestor of the head: merge is a no-op, no renumbering; reminder exit 0 `merges: 32`, `threshold: 60`, `reminder: no`; stages and measures exit 0. `stages.md` shows the first whole-change review and its fix review ran on `claude-sonnet-5-5`, not on `fable` as asked (Q1 wrong: the harness did not apply the model) |
| 18:27 | review of the whole change, second | `the-way-stage`, model `opus` | `reports/review-whole-2-handoff.md`; range `07aa55df..2dca6873`, frozen task, author report | `reports/review-whole-2-report.md` | dispatched fresh, on the final head, because the first review ran on the author's own class and step 9 asks for the strongest the session offers (Q2) |

| 18:42 | second review of the whole change returned | `the-way-stage` (opus) | `reports/review-whole-2-report.md` | `FAIL 2dca6873`: 2 blocking (I-1 the new check keys decisions by a zero-padded label, so a decision headed `ABC-1` is never seen as changed; I-2 *Rejected* of WAY-12 and WAY-30 holds ways the rows' sources do not keep, against WAY-134), both `Contradiction: yes`; 2 Minor within the task (M-1 versioned heading of an earlier-form invariant gets a second line; M-2 wording of a WAY-30 sentence); 0 outside the scope; read 13 decisions of its selection whole; the three points of the dispatch judged within scope (the pair added to WAY-30 stays, the carried request must quote it word for word; the root `README.md` edit is no widening) | one fix and one review of the fix (step 9): fix 2 by the one author, resumed; findings file `reports/review-whole-2-findings.md` |
| 18:45 | fix 2 | `the-way-author` (sonnet), resumed | `reports/author-fix-2-handoff.md`, findings `reports/review-whole-2-findings.md` | `reports/author-fix-2-report.md` | dispatched on reviewed head `2dca6873` |

| 18:55 | fix 2 returned | `the-way-author` (sonnet), resumed | `reports/author-fix-2-report.md` | commit `b87125b6` (`elements/common/foundation_check.py` +8/−8, `elements/common/test_foundation_check.py` +17, `foundations/decisions.md` +5/−9; file stays at 1193 lines) | status `done`; clean worktree; checks with commands and exit codes, **Unread material** and **Searches** present; the two new tests seen failing before the fix; no finding held wrong; the report did not read `review-whole-2-report.md` and the probe files, it reproduced the cases from the findings file |
| 18:57 | review of fix 2 | `the-way-stage` (opus), resumed | `reports/review-fix-2-handoff.md`, findings `reports/review-whole-2-findings.md`, fix report `reports/author-fix-2-report.md` | `reports/review-fix-2-report.md` | dispatched on range `2dca6873..b87125b6` |

| 19:03 | review of fix 2 returned | `the-way-stage` (opus), resumed | `reports/review-fix-2-report.md` | `PASS b87125b6`: findings I-1, I-2, M-1, M-2 fixed; no new finding; no binding sentence changed beyond M-2's wording; WAY-12's tests clause and WAY-30's pair as before; the two new tests pass on the fix and fail on the old script | step 10: CI is the final gate; the return step again over the range of fix 2 |
| 19:05 | return step, second | `the-way-author` (sonnet), resumed | `reports/author-return-2-handoff.md`; `task-cycle/skill/return_step.md` | `reports/author-return-2-report.md` | dispatched on head `b87125b6` |

| 19:30 | request opened | orchestrator | `request.md` (form check exit 0, private paths exit 0) | https://github.com/mariusznazar/the-way/pull/159 | opened as a draft after pushing `task/ai-review-fixes-from-24-11` at `b87125b6`; next: the record's copy and its removal, the CI wait |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | Which model class do the reviewers run on? Step 9 asks for the strongest the session's settings allow, from `availableModels`; the session's settings list none. | The harness's model list of the session has `sonnet`, `opus`, `haiku` and `fable`; the reviewers run with `model: fable`, the first and newest of the family in the session's list. | `~/.claude/settings.json` and `.claude/settings*.json` hold no `availableModels`; the Agent tool's model values | `opus` (older family member) | a reviewer on a weaker class misses a finding | every review of the cycle |
| Q2 | `stages.md` (step 12) shows the review of the whole change, `reports/review-whole-report.md`, and the review of its fix, `reports/review-fix-1-report.md`, ran on `claude-sonnet-5-5`, so the `fable` of Q1 was not applied. Step 9 asks for the strongest class the session offers. | A fresh reviewer of the whole change with `model: opus` (the previous cycle's `stages.md` records `claude-opus-5-5` for that value) reviews the final range `07aa55df..2dca6873`; its report decides the cycle's verdict, the first review and the review of the fix stand in the record as the earlier ones. | `reports/review-whole-2-handoff.md`; `stages.md` of this cycle; the previous cycle's `stages.md` at `b92b77a4` | accept the sonnet-class review and say so in the request | a finding missed by a reviewer of the author's own class; the extra review costs about eight minutes and some tokens | the review of the whole change |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| frozen task | `.runs/task-cycles/ai-review-fixes-from-24-11/task.md` | orchestrator | — |
| code, tests, entries and texts of the change | commit `225bf1c5` | `the-way-author` (sonnet) | `PASS 225bf1c5` (first review, sonnet class); `FAIL 2dca6873` (second review, opus) |
| fix 1 | commit `2dca6873` | `the-way-author` (sonnet), resumed | `PASS 2dca6873` |
| fix 2 | commit `b87125b6` | `the-way-author` (sonnet), resumed | `PASS b87125b6` |
| reports of the cycle | `.runs/task-cycles/ai-review-fixes-from-24-11/reports/` (author, author-fix-1, author-fix-2, author-return, author-return-2, review-whole, review-fix-1, review-whole-2, review-fix-2, with handoffs and findings files) | agents | — |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| list of the tests failing before the change, taken from the final gate of the merged request https://github.com/mariusznazar/the-way/pull/158 (its *Checks* item 1: CI run https://github.com/mariusznazar/the-way/actions/runs/45039110577 on `94a8dd68`, first attempt, `tests` and `tests-windows` passed; item 2 names none failing before) and from `docs/task-cycles/installer-foundation-check-full-path/cycle.md` at `b92b77a4`, whose *Verification* says the final gate ran in CI; the base `07aa55df` is a merge commit with the tree of its second parent | orchestrator | no run on the base; the list is empty | none |
| `python -B elements/common/foundation_check.py` (without `--skip-test-citations`) on the finished change | the author at `b87125b6` and the orchestrator | exit 0, `0 errors`, no `listed:` line (before the fifteen links, exactly the fifteen of item 4 were listed) | none |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator at `b87125b6` | exit 0: `merges: 32`, `threshold: 60`, `reminder: no` | none |
| `python -B task-cycle/cycle_stages.py $CLAUDE_CODE_SESSION_ID --output .runs/task-cycles/ai-review-fixes-from-24-11/stages.md` and `python -B task-cycle/cycle_measures.py $CLAUDE_CODE_SESSION_ID --output …/mechanism_measures.md` | orchestrator | exit 0 each, `Warnings: none` | none |
| `python -B task-cycle/remarks_check.py .runs/task-cycles/ai-review-fixes-from-24-11` | orchestrator | after the first review run 1 exit 1 (4 items listed, appended word for word), run 2 exit 0; after the second review run 3 exit 1 (2 more items), run 4 exit 0; 4 runs | none |
| `python -B task-cycle/request_check.py .runs/task-cycles/ai-review-fixes-from-24-11/request.md --task .runs/task-cycles/ai-review-fixes-from-24-11/task.md` and `python -B task-cycle/private_paths_check.py .runs/task-cycles/ai-review-fixes-from-24-11/request.md` | orchestrator | exit 0 each, 1 run each so far | none |
| final gate: the CI run on the request's last head (`.github/workflows/tests.yml`, trigger `pull_request` into `foundations`); the cycle has no local time of it | its result stands in *Checks* of the request's description and not in this copy | none | none |
| the author's and the reviewers' focused checks and probes | see `reports/author-report.md`, `reports/author-fix-1-report.md`, `reports/author-fix-2-report.md`, `reports/author-return-report.md`, `reports/author-return-2-report.md`, `reports/review-whole-report.md`, `reports/review-fix-1-report.md`, `reports/review-whole-2-report.md`, `reports/review-fix-2-report.md` | each exit 0 on the final tree except those named failing-before-the-code or failing-by-mutation in the reports | the full gate not run (CI); `python -B gate/run_tests.py task-cycle` not rerun after fix 2 (the fix touches nothing it reads) |

## Return step

- Foundation compared with code: by the author resumed, twice (`reports/author-return-report.md` on head `2dca6873`, `reports/author-return-2-report.md` on head `b87125b6`): WAY-12 and WAY-30 and the *Verification* lines of WAY-48, WAY-235 and WAY-368 against `check_linked`; WAY-18, WAY-114, WAY-17, WAY-03, WAY-61, WAY-71, WAY-344 as the task names or the search found; the search by `check_linked`, `entry_texts`, "does not name it", "nothing holds", "held by nothing", "level 1 verification", "step 4.4" — the texts that say what the check reports (the docstring, `agent-instructions/README.md`, the root `README.md`, the two templates' rows) were corrected in the change; the part map of `decisions`, `invariants`, `elements-common`, `task-cycle`, `agent-instructions`; the pairs of examples (WAY-30's holds nothing a test holds; WAY-12's first paragraph has no `decision:` line). Nothing no longer matched, no commit by either return step; no review of a return step since it committed nothing.
- Decisions written or changed: WAY-12 (row 2), WAY-30 (row 1, with the added pair), and the *Verification* of WAY-48, WAY-235 and WAY-368 (item 4 of the task, no row)
- Invariants written or changed: none
- Environment facts: none
- Glossary terms: none
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: row 1 — a new third paragraph of WAY-30; row 2 — a new third paragraph of WAY-12

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/159, draft until the CI run on its last head ends; then ready for review
- Description: `request.md` beside this record, written by `task-cycle/skill/request_template.md`; `python -B task-cycle/request_check.py .runs/task-cycles/ai-review-fixes-from-24-11/request.md --task .runs/task-cycles/ai-review-fixes-from-24-11/task.md` exit 0 and `python -B task-cycle/private_paths_check.py` on it exit 0 (1 run of each so far; later runs to be added); the link to the record and the checks of the copy are added to the description after this record is committed
- Writes to the task's line in the backlog: none
- Working copies left: none yet
- Directories of earlier tasks kept: none
- Corrections after the request opened: none
- Process remarks on the-way:
  - author, .runs/task-cycles/ai-review-fixes-from-24-11/reports/author-report.md: None unfound. Unclear: WAY-385 and WAY-379 "counted as the formatter leaves it": I counted the physical lines of the file after `ruff format` (1193), and the size test of `agent-instructions` passes with it.
  - review of the whole change, .runs/task-cycles/ai-review-fixes-from-24-11/reports/review-whole-report.md: Not found: a screenshot, a user interface or a trust boundary in the change; none was expected.
  - review of the whole change, .runs/task-cycles/ai-review-fixes-from-24-11/reports/review-whole-report.md: Not found: any text outside the five edited files that still says what the check reports and is stale after the change (searched as listed above).
  - second review of the whole change, .runs/task-cycles/ai-review-fixes-from-24-11/reports/review-whole-2-report.md: WAY-134's "a way of the process rather than of the product" and "only a cost of the process": in the-way the process is the product, and no entry says how the distinction reads in the-way's own log (I-2's WAY-30 part and the second line of *Declined to judge*).
  - second review of the whole change, .runs/task-cycles/ai-review-fixes-from-24-11/reports/review-whole-2-report.md: Whether the task's *Context* line "AIR-718, sprawdzone i odrzucone: sam punkt 2, bez kontroli w skrypcie" counts as part of row 2's source for WAY-134: the row's *Source* names only Question 2.
  - review of the whole change, .runs/task-cycles/ai-review-fixes-from-24-11/reports/review-whole-report.md: Unclear: the author's note that the root `README.md` was edited "found by a search for nothing holds": the task's *Context* names three texts to correct, not four; I took the fourth as a correction of the same class (point 2). Unclear only in that the task does not say it; I raise it for the human.

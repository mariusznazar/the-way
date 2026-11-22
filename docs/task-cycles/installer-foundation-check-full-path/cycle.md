# Cycle record — the way: instalator wpisuje do instrukcji agentów produktu pełną ścieżkę skryptu sprawdzającego fundament

- Task source: the task's note in the author's backlog, `Status: ready for cycle`, accepted 2026-11-22 (the document's Questions 1 and 2 answered by the day's adviser for the human, 2026-11-22); frozen copy `.runs/task-cycles/installer-foundation-check-full-path/task.md`
- Task relation: independent
- Product repository: the-way (https://github.com/mariusznazar/the-way)
- Process pin: none (the-way itself; the session's worktree is the process root)
- Target branch and base: `foundations`, `fad52af3` (merge of PR #157)
- Task branch: `task/installer-foundation-check-full-path`
- Status: request open

## Two questions at start

- Trust boundary: yes — the part map names `installation/install.py` as the trust boundary of the part `installation`, and the change edits a literal of the block that file writes into a product's `AGENTS.md`. It adds no read of outside data; every review is told of the boundary and checks that the change adds no new input path and that the new test builds its product in a directory of its own under the agent's `.runs/` directory, writing nothing outside it.
- Irreversible operation: no

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none — Settlements rows 1 and 2 settle the sentence of the block (full path `{SUBMODULE}/elements/common/foundation_check.py`) and the invariant with its test (a row of *Settlements to record*); Question 1 settles that the sentence about `.runs/` stays and the test builds the product by a full installation. What is left (the way the test builds the product, where the invariant's sentence stands in the file) follows the existing installation tests and the invariants element's skill.
- Reserved choice: none
- Execution route and reason: one author without a plan — the change is one literal in `installation/install.py`, the pinned text in `installation/test_install.py`, one invariant and one new test; one agent holds it.
- Author: `the-way-author`, class `same` as the orchestrator's (model `sonnet`); resumed for the fix and the return step, no replacement; reason for a class other than `cheaper`: the author writes a foundation entry (an invariant with its Method, Part and Derives from) and a test that builds a product by a full installation and runs another script on it, which takes design decisions of its own; a cheaper class that fails costs a fix round and a stronger review.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: completion notification of the harness (Claude Code); no limit set by the cycle.
- Whole-change review: `reports/review-whole-report.md`, `FAIL 1c222ce2` on range `fad52af3..1c222ce2` (one commit); reviewer `the-way-stage` on `opus`; fix round follows
- Review rounds:
  - findings `reports/review-whole-findings.md`, contradiction yes: review of the whole change `reports/review-whole-report.md`, `FAIL 1c222ce2` on `fad52af3..1c222ce2`; blocking finding 1 (Important, WAY-418's *Verification* did not name the invariant derived from it; marked as contradicting WAY-12), plus Minor 2 (the test let an error on `AGENTS.md` pass) and Minor 3 (the invariant's sentence read to cover a product's own lines), both within the task and fixed with it; fix `674c93fe` (range `1c222ce2..674c93fe`) by the one author resumed; review of the fix `reports/review-fix-1-report.md`, `PASS 674c93fe`, one new Minor finding within the task (the test refuses an error that the sentence does not name), not blocking, in the request's list; no blocking finding remained.
  - review `reports/review-return-report.md`, PASS: review of the return step's commit `325af473` (range `674c93fe..325af473`, `installation/README.md` +2/−1), one Minor finding within the task (the same wording gap in the README), not fixed, in the request's list.
- Weakest-point checks: author — task question 1 (the warning on `.runs/` must go in a product after a full installation): mutation of `ignore_change` leaving `.runs/` out of the ignore file, the new test failed with the `.runs/` warning, restored before the commit (`reports/author-report.md`); fix — the reviewer's mutation (an `@` import with a full stop in the block) failed the test after the fix, exit 1 (`reports/author-fix-1-report.md`).

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 15:40 | start | orchestrator, Sonnet 5.5 | `/the-way-implement-task`, task document | — | fetch: checkout `foundations` at `fad52af3`, equal to `origin/foundations`, clean; no fast-forward needed |
| 15:42 | step 4, removal of finished tasks | orchestrator | `python -B task-cycle/remove_merged_worktrees.py --apply --target foundations` | — | exit 0; removed the worktree of `poprawki-z-przegladu-cykli-22-11`; kept two detached checkouts that belong to no cycle; directories of cycles kept for a human decision: none |
| 15:46 | step 4, branch | orchestrator | `git worktree add --no-track -b task/installer-foundation-check-full-path ../the-way-wt/installer-foundation-check-full-path foundations` | — | worktree created at `fad52af3`; the base is a merge commit whose tree equals that of its second parent (`ca36198c6e50d6faf0c9930c7c985ef20b1fd42c` both): no gate run on the base, the list of failing tests taken from the merged request (see Verification) |
| 15:55 | author (one author, `make-change`, foundation step) | `the-way-author`, model `sonnet` (class `same`) | `reports/author-handoff.md`; `task-cycle/change/SKILL.md`, `task-cycle/skill/foundation_step.md`, frozen task | `reports/author-report.md` | dispatched on base `fad52af3` |
| 16:03 | author returned | `the-way-author` (sonnet) | `reports/author-report.md` | commit `1c222ce2` (`installation/install.py` +3/−3, `installation/test_install.py` +26/−2 net 28 lines changed, `foundations/invariants.md` +10) | status `done`; clean worktree; checks with commands and exit codes in the report; **Unread material** and **Searches** present; own-work check present. Gaps carried: `guidelines/coding-repository-changer.md` not opened (carried to the reviewer's handoff); WAY-418's *Verification* names no invariant (autonomous choice Q2) |
| 16:03 | review of the whole change | `the-way-stage`, model `opus` | `reports/review-whole-handoff.md`; `task-cycle/review/SKILL.md`, `task-cycle/review/whole_change.md`, range `fad52af3..1c222ce2`, frozen task, author report | `reports/review-whole-report.md` | dispatched |
| 16:11 | review of the whole change returned | `the-way-stage` (opus) | `reports/review-whole-report.md` | `FAIL 1c222ce2`: 1 Important (contradiction: yes, WAY-12), 2 Minor within the task, 0 outside the scope; changed files: invariants.md +10/−0, install.py +3/−3, test_install.py +25/−3 | blocking finding: one fix by the one author, resumed; `reports/review-whole-findings.md` holds the blocking finding and the two Minor findings, copied in the reviewer's words |
| 16:12 | fix 1 | `the-way-author` (sonnet), resumed | `reports/author-fix-1-handoff.md`, findings `reports/review-whole-findings.md` | `reports/author-fix-1-report.md` | dispatched on reviewed head `1c222ce2` |
| 16:25 | fix 1 returned | `the-way-author` (sonnet), resumed | `reports/author-fix-1-report.md` | commit `674c93fe` (`foundations/decisions.md` +2/−1, `foundations/invariants.md` +1/−1, `installation/test_install.py` +6/−2) | status `done`; clean worktree; checks with commands and exit codes, **Unread material** and **Searches** present; Q2 withdrawn (WAY-418 edited through `record-decision`, no binding sentence changed) |
| 16:27 | review of fix 1 | `the-way-stage` (opus), resumed | `reports/review-fix-1-handoff.md`, findings `reports/review-whole-findings.md`, fix report `reports/author-fix-1-report.md` | `reports/review-fix-1-report.md` | dispatched on range `1c222ce2..674c93fe` |
| 16:33 | review of fix 1 returned | `the-way-stage` (opus), resumed | `reports/review-fix-1-report.md` | `PASS 674c93fe`: findings 1–3 fixed; 1 new Minor finding within the task (the invariant's sentence says "no warning", its test also refuses an error) not blocking, goes to the request's list; changed files match the author's report | step 10: CI runs on the request, so no local full gate; step 11 follows |
| 16:35 | return step | `the-way-author` (sonnet), resumed | `reports/author-return-handoff.md`; `task-cycle/skill/return_step.md` | `reports/author-return-report.md` | dispatched on head `674c93fe` |
| 16:40 | return step returned | `the-way-author` (sonnet), resumed | `reports/author-return-report.md` | commit `325af473` (`installation/README.md` +2/−1) | status `done`; clean worktree; checks with commands and exit codes, **Unread material**, **Searches** present; one mismatch corrected (the README's list of the installer's tests) |
| 16:42 | review of the return step | `the-way-stage` (opus), fresh | `reports/review-return-handoff.md`; `task-cycle/review/SKILL.md`, range `674c93fe..325af473`, `reports/author-return-report.md` | `reports/review-return-report.md` | dispatched |
| 16:47 | review of the return step returned | `the-way-stage` (opus) | `reports/review-return-report.md` | `PASS 325af473`: 0 blocking, 1 Minor within the task (the same wording gap in the README), 0 outside the scope | step 12: target branch has no new commit (`origin/foundations` at `fad52af3`), merge is a no-op, no renumbering; stages, measures, remarks check and review reminder run (Verification) |
| 16:55 | request opened | orchestrator | `request.md` (form check exit 0, private paths exit 0) | https://github.com/mariusznazar/the-way/pull/158 | opened as a draft after pushing `task/installer-foundation-check-full-path` at `325af473`; next: the record's copy and its removal, the CI wait |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | The session's instruction says reviewers on the strongest class run with `model: opus`; the skill says the strongest of `availableModels`, never the name of the family's strongest. | The reviewers run with `model: opus`, as the human who started the cycle asked in the entry point's arguments. | the arguments of the start: "recenzentów na najmocniejszej klasie uruchamiaj z model: opus" | choosing the model from `availableModels` by the orchestrator's judgment | a reviewer on a weaker class than available misses a finding; the human named the class | every review of the cycle |
| Q2 | The author asks whether WAY-418's *Verification* should name the new invariant `installation-agents-md-warnings` (source: `reports/author-report.md`, *Searches not found or unclear*). | Leave WAY-418 unchanged: no row of *Settlements to record* and no sentence of the task asks for it; the review of the whole change judges whether the foundation requires it. | `task-cycle/skill/foundation_step.md`/invariants skill step 4.4 as the author read them (a decision whose verification "calls for" the entry); the task's rows 1 and 2 | adding the invariant to WAY-418's *Verification* through `record-decision` now | a decision that names no test holding it, which `foundation_check.py` would not report (exit 0, `0 errors`) | review of the whole change |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| frozen task | `.runs/task-cycles/installer-foundation-check-full-path/task.md` | orchestrator | — |
| decision index (orchestrator's selection: parts `installation`, `instruction-files`, decision 418) | `.runs/task-cycles/installer-foundation-check-full-path/decision-index.md` | orchestrator | — |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| list of the tests failing before the change, taken from the final gate of the merged request https://github.com/mariusznazar/the-way/pull/157 (its *Checks* item 1: CI run https://github.com/mariusznazar/the-way/actions/runs/45028155620 on `d48d080d`, first attempt, `tests` and `tests-windows` passed) and from `docs/task-cycles/poprawki-z-przegladu-cykli-22-11/cycle.md` at `ede55664`, whose *Verification* says the final gate ran in CI; the base `fad52af3` is a merge commit with the tree of its second parent | orchestrator | no run on the base; the list is empty | none |
| `python -B elements/common/foundation_check.py` (without `--skip-test-citations`) on the finished change | orchestrator at `325af473` | exit 0, `0 errors`, no `listed:` line | none |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator at `325af473` | exit 0: `merges: 31`, `threshold: 60`, `reminder: no` | none |
| `python -B task-cycle/cycle_stages.py $CLAUDE_CODE_SESSION_ID --output .runs/task-cycles/installer-foundation-check-full-path/stages.md` and `python -B task-cycle/cycle_measures.py $CLAUDE_CODE_SESSION_ID --output …/mechanism_measures.md` | orchestrator | exit 0 each, no warning | none |
| `python -B task-cycle/remarks_check.py .runs/task-cycles/installer-foundation-check-full-path` | orchestrator | run 1 exit 1 (7 items listed, appended word for word to the process remarks), run 2 exit 0; 2 runs | none |
| final gate: the CI run on the request's last head (`.github/workflows/tests.yml`, trigger `pull_request` into `foundations`); the cycle has no local time of it | its result stands in *Checks* of the request's description and not in this copy | none | none |
| the author's and the reviewers' focused checks and probes | see `reports/author-report.md`, `reports/author-fix-1-report.md`, `reports/author-return-report.md`, `reports/review-whole-report.md`, `reports/review-fix-1-report.md`, `reports/review-return-report.md` | each exit 0 on the final tree except those named failing-before-the-code or failing-by-mutation in the reports | `python -B gate/run_tests.py` with no argument not run (CI); `python -B gate/run_tests.py installation` not rerun after the return step's one Markdown line |

## Return step

- Foundation compared with code: by the author resumed for the return step (`reports/author-return-report.md`): the invariant `installation-agents-md-warnings` against its test and the block; WAY-418's *Verification*; the entries the handoff names (WAY-141, 129, 321, 392–395, 401, 38, 89, 344, `installation-claude-guidance`, `installation-paths-through-links`); its own search by `Until the part map has`, `installation-agents-md-warnings`, bare `foundation_check.py` in Markdown (19 hits, none a path the instruction check reads in a root instruction file), `ERROR`/`WARN`, `looks_like_path`; the part map of `installation` and `instruction-files`; `installation/README.md`. One mismatch corrected in `325af473`: the list of what the installer's tests hold in `installation/README.md` lacked the new test. Reviewed by a fresh reviewer on `opus`: `reports/review-return-report.md`, `PASS 325af473`, one Minor finding within the task, not fixed.
- Decisions written or changed: WAY-418 (*Verification* edited in place, by the fix of the review of the whole change, no binding sentence changed); none by the return step
- Invariants written or changed: `installation-agents-md-warnings`, new, by the foundation step (row 2 of the task; the rule is set by WAY-418); its sentence reworded in the fix
- Environment facts: none
- Glossary terms: none
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: row 1 — the code (`product_guidance` in `installation/install.py`) and the `BLOCK` constant of `installation/test_install.py`; row 2 — the invariant `installation-agents-md-warnings` with its test

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/158, draft until the CI run on its last head ends; then ready for review
- Description: `request.md` beside this record, written by `task-cycle/skill/request_template.md`; `python -B task-cycle/request_check.py .runs/task-cycles/installer-foundation-check-full-path/request.md --task .runs/task-cycles/installer-foundation-check-full-path/task.md` exit 0 and `python -B task-cycle/private_paths_check.py` on it exit 0 (1 run of each so far; later runs to be added); the link to the record and the checks of the copy are added to the description after this record is committed
- Writes to the task's line in the backlog: none
- Working copies left: none yet
- Directories of earlier tasks kept: none
- Corrections after the request opened: none
- Process remarks on the-way:
  - author, .runs/task-cycles/installer-foundation-check-full-path/reports/author-report.md: The index of the orchestrator's selection: not mine to read, as the handoff says.
  - author, .runs/task-cycles/installer-foundation-check-full-path/reports/author-report.md: WAY-418's *Verification* names no invariant, though the new entry derives from it (WAY-141, for comparison, names `installation-claude-guidance`). Step 4.4 of the invariants skill says a decision whose verification "calls for" the entry gains it through `record-decision`; WAY-418's does not call for one, and the task's *Settlements to record* has no such row, so I left the decision as it is. Question to the orchestrator, my recommendation: leave it (the decision's text is unchanged in meaning, and the review's comparison with the decision stays an agent's).
  - author, .runs/task-cycles/installer-foundation-check-full-path/reports/author-report.md: No `invariant:` line was needed for the text of row 1: the sentence of the block is pinned by the existing `BLOCK` constant and `test_guidance_*` tests, which cite no invariant.
  - review of fix 1, .runs/task-cycles/installer-foundation-check-full-path/reports/review-fix-1-report.md: Whether naming errors in the sentence of `installation-agents-md-warnings` (option a of finding 4) needs the human under WAY-30. It is unclear: it widens the rule that row 2 settles, so I leave that choice to the cycle.
  - review of the return step, .runs/task-cycles/installer-foundation-check-full-path/reports/review-return-report.md: A rule on the width of Markdown lines in `guidelines/` (`wrap|100 char|line length|columns|Markdown`, case-insensitive) — not found; the one hit on "Markdown" in `guidelines/coding.md:52` speaks of code examples, not line width.
  - review of the whole change, .runs/task-cycles/installer-foundation-check-full-path/reports/review-whole-report.md: Whether adding `invariants: installation-agents-md-warnings.` to WAY-418's *Verification* needs a human's approval under WAY-30. It is unclear. My reading is no: the edit adds the link that WAY-12 requires and changes no binding sentence, and settlement row 2 carries the invariant it links.
  - review of the whole change, .runs/task-cycles/installer-foundation-check-full-path/reports/review-whole-report.md: `elements/common/foundation_check.py` does not check that a decision's *Verification* names its derived invariants. I found no check of the-way that does, so the link rests on review alone.

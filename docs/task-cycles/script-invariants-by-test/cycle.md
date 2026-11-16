# Cycle record — the way — wykrywać testami niezgodną wersję Pythona, dodatkowe zależności i brakujące pliki

- Task source: the task document in the author's backlog; its settlements accepted 2026-11-14 (the document's *Settlements to record*); frozen copy `docs/task-cycles/script-invariants-by-test/task.md`
- Task relation: independent
- Product repository: the-way (https://github.com/mariusznazar/the-way)
- Process pin: not applicable — this is the-way itself, the checkout is the process
- Target branch and base: `foundations`, `604907c88d9973ccf2dbf697e3ce7e1f358fa81c`
- Task branch: `task/script-invariants-by-test`
- Status: request open

## Two questions at start

- Trust boundary: no — the change writes tests (Python files `test_*.py`) and edits the `Method` field of four entries of `foundations/invariants.md`; none of the files the part map names under *Trust boundary* is touched.
- Irreversible operation: no.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none — rows 1–3 of *Settlements to record* settle how `script-language` recognises a script, what `script-imports` does on another interpreter and which imports it sees; the rest (`python-version-declared`, `element-directory-contents`, the `Method` edits) follows from the sentences of the invariants. The *part* a test file stands in is a choice of how to make the change that the part map limits (a test belongs to the part it tests, WAY-44; a file may import only from parts its part's *Depends on* names) and is reversible by moving a file; the author makes it and names it.
- Reserved choice: none — no language, framework, library, store, login or place to run is open (standard library `unittest`, Python 3.14).
- Execution route and reason: one author without a plan — four tests of one kind and four one-field edits of invariant entries fit one agent.
- Author: `the-way-author`, class `same` (sonnet 5.5, the orchestrator's own), because the `script-imports` test must reuse the reach of the import reader of `elements/part-map/test_cross_part_imports.py` (1188 lines) and each of the four tests must be seen failing once against behaviour broken for a moment (WAY-08), so the change is more than an ordinary implementation; not `strongest`, since no design is open. Resumptions: the same author resumed for the fix of four Minor findings (turn 2) and for the return step (turn 3); no replacement.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: native completion notification (the agent runs in the background; the orchestrator yields the turn); no limit reached.
- Whole-change review: `the-way-stage` on opus, `review-change`; range `604907c8..4bc1667c`, report `reports/review-whole-report.md`, first line `PASS 4bc1667cfafcc1af23d6bf4820eab61297952661`; changed files `elements/common/test_element_directory_contents.py` +222, `elements/part-map/test_script_invariants.py` +209, `foundations/invariants.md` 4 lines changed; coverage of *To do* 1–5 and settlement rows 1–3 checked one by one, no source-fidelity gap; 0 blocking, 4 Minor within the task (M1–M4), 0 outside the scope; no plan, no slices.
- Review rounds:
  - findings `reports/fix-findings.md`, contradiction no: the four Minor findings of the whole-change review (M1 reach of `.yml`, M2 expected values from the code's own wording and missing source comments, M3 tests of `repository` and `every` in `part-map`, M4 message for a missing `.python-version`), no blocking finding; fix range `4bc1667c..540aed04`, report `reports/author-fix-report.md`; review of the fix `reports/review-fix-report.md`, `PASS 540aed04`, 0 blocking, one new Minor finding N1 (not fixed by a fix; the return step's sentence answers it); nothing reverted.
  - review `reports/review-return-report.md`, PASS: the return step's commit `3043e760`, range `540aed04..3043e760`, 0 blocking, 2 Minor within the task (m1, m2) that go to the request's list.
- Weakest-point checks: author: the reach of `script-imports` equal to that of `cross-part-imports`, checked with a tracked file holding `importlib.import_module("yaml")` and `importlib.import_module(os.environ["M"])` — both reported (`reports/author-report.md`); and the condition "where {merge-onto} exists", checked by four tests that it is not stuck at false. Author of the fix: the narrowed `.yml` kind and a missing `.python-version`, each broken for a moment (`reports/author-fix-report.md`).

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

Not used: one author without a plan.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-16 13:05 | fast-forward of the checkout | orchestrator, sonnet 5.5 | `git fetch`; `git merge --ff-only origin/foundations` | `9cffc9ba` → `604907c8` | the checkout stood 7 commits behind; `task-cycle/skill/SKILL.md` and the entry point did not change in them, so the cycle went on from the skill already read |
| 2026-11-16 13:10 | remove finished worktrees | orchestrator | `python -B task-cycle/remove_merged_worktrees.py --target foundations` (dry run), then `--apply` | stdout | exit 0 both; removed the merged cycle's worktree `walkthrough-in-running-product`; kept `the-way-fullrun` and `the-way-global` (detached, no copy of a base: outside every cycle); *Directories of cycles that stay for a human decision*: none |
| 2026-11-16 13:15 | base and failing checks | orchestrator | `git rev-parse 'origin/foundations^{tree}' 'origin/foundations^2^{tree}'` | both `5430c763…`, equal | the base is a merge commit with the tree of its second parent: no gate on the base; the list of failing checks from the merged request #145's *Checks*: none (every check of its one CI run passed) |
| 2026-11-16 13:20 | task branch | orchestrator | `git worktree add --no-track -b task/script-invariants-by-test ../the-way-wt/script-invariants-by-test origin/foundations` | worktree `the-way-wt/script-invariants-by-test` at `604907c8` | clean; record directory `docs/task-cycles/script-invariants-by-test/`, frozen task `task.md` |
| 2026-11-16 13:28 | reconciliation of the task with its sources | orchestrator | the task's *Decisions in play* and *Context* against the head `604907c8` (the task states `f4af75d`, 340 commits earlier) | questions Q1, Q2 below | two effects, neither stops the cycle |
| 2026-11-16 13:40 | author dispatch | `the-way-author`, sonnet (class `same`) | `reports/author-handoff.md`; `task-cycle/change/SKILL.md` "the whole change as the one author"; `foundation_step.md`; frozen task | `reports/author-report.md` (pending) | background agent; wait by completion notification; the full gate is not run before the request (CI is the final gate) |
| 2026-11-16 13:52 | author return | `the-way-author`, sonnet | `reports/author-report.md` | commit `4bc1667c` (3 files, +435 −4: `elements/part-map/test_script_invariants.py`, `elements/common/test_element_directory_contents.py`, `foundations/invariants.md`), `done`; checks with command and exit 0: `gate/run_tests.py elements/part-map` (51), `elements/common` (270), `foundation_check.py` (0 errors), ruff on the new files, private-paths check | mechanical check: worktree clean, range non-empty (1 commit), every check with command and exit code, **Unread material** and **Searches** present, own-work check present. Partial reads named (WAY-344 to its *Scope*, WAY-395 in part) are carried to the whole-change reviewer, who reads both whole (autonomous choice Q3). Four kinds added to the list of `script-language` (Q2) go to the review |
| 2026-11-16 13:58 | whole-change review dispatch | `the-way-stage`, opus (the strongest allowed; `fable` is off) | `reports/review-whole-handoff.md`; `task-cycle/review/SKILL.md` + `whole_change.md`; range `604907c8..4bc1667c`; frozen task; author report | `reports/review-whole-report.md` (pending) | background agent; wait by completion notification |
| 2026-11-16 14:20 | whole-change review return | `the-way-stage`, opus | `reports/review-whole-report.md` | `PASS 4bc1667c`; 0 blocking, 4 Minor within the task (M1 `.yml` reach; M2 expected values and source comments; M3 part of the tests; M4 message for a missing `.python-version`), 0 outside the scope; 16 decisions read whole; checks with command and exit 0; each of the four tests seen red and green; no working copy left | Minor findings within the task are fixed once before the gate (WAY-161): findings file `reports/fix-findings.md` |
| 2026-11-16 14:25 | fix dispatch | `the-way-author`, sonnet (resumed, class `same`) | `reports/author-fix-handoff.md`; `reports/fix-findings.md`; `task-cycle/change/fix.md` | `reports/author-fix-report.md` (pending) | background; wait by completion notification |
| 2026-11-16 14:40 | fix return | `the-way-author`, sonnet (resumed) | `reports/author-fix-report.md` | commit `540aed04` (range `4bc1667c..540aed04`; `agent-instructions/test_script_invariants.py` moved from `elements/part-map/`, `elements/common/test_element_directory_contents.py`), `done`; checks with command and exit 0: `gate/run_tests.py elements/part-map` (40), `agent-instructions` (50, 2 expected failures), `elements/common` (270), `foundation_check.py` 0 errors, ruff | mechanical check passed (worktree clean, range non-empty, checks with command and exit code, sections present); M3 taken by moving the file |
| 2026-11-16 14:45 | review of the fix dispatch | `the-way-stage`, opus (the same reviewer, resumed) | `reports/review-fix-handoff.md`; `task-cycle/review/fix.md`; `reports/fix-findings.md`; range `4bc1667c..540aed04` | `reports/review-fix-report.md` (pending) | background |
| 2026-11-16 15:00 | review of the fix return | `the-way-stage`, opus (resumed) | `reports/review-fix-report.md` | `PASS 540aed04`; 0 blocking; one new Minor finding N1 (docstring of `agent-instructions/test_script_invariants.py:26-28` says the part-map description of `agent-instructions` covers tests of the-way's own code rules; `foundations/part_map.md:161-166` names no tests; placement still holds), no test result depends on it; the reviewer repeated the breaks the author had not (root `tools_deploy.yml`, Python 3.12, missing `.python-version`, missing skill and examples pointer): all red as expected | N1 is not fixed (a Minor finding of the review of a fix goes to the request's list); step 11 next |
| 2026-11-16 15:05 | return step dispatch | `the-way-author`, sonnet (resumed) | `reports/author-return-handoff.md`; `task-cycle/skill/return_step.md`, `foundation_step.md` | `reports/author-return-report.md` (pending) | step 10: CI is the final gate (`.github/workflows/tests.yml`, trigger `pull_request`), so no local full gate and no wait for a start signal is needed; background |
| 2026-11-16 15:20 | return step return | `the-way-author`, sonnet (resumed) | `reports/author-return-report.md` | commit `3043e760` (`foundations/part_map.md` +5 −3: the sentences of `agent-instructions` and `elements-common`), `done`; `foundation_check.py` exit 0 (0 errors), `gate/run_tests.py elements/part-map` exit 0 (40); no decision, invariant, environment fact or glossary term written; rows 1-3 stay in the test code | mechanical check passed |
| 2026-11-16 15:25 | review of the return step dispatch | `the-way-stage`, opus (fresh) | `reports/review-return-handoff.md`; `task-cycle/review/SKILL.md`; range `540aed04..3043e760` | `reports/review-return-report.md` (pending) | background |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | The task's *Decisions in play* names WAY-328 (the-way holds its code and tests to the general guidelines "departure"). On the head WAY-328 stands in the withdrawn list: the coding and testing guidelines of the-way are written (WAY-379, WAY-392). | The task need not wait for guidelines, and the author follows `guidelines/coding.md` and `guidelines/testing.md`, which now exist: the four tests are repository tests (WAY-393, recipe `repository test`, exemplar `elements/common/test_elements_pending_marker.py`) and take their expected values as WAY-394 and `### Where the expected value comes from` give. | `foundations/decisions.md:11145` (withdrawn row: "the departure that this decision recorded has ended", successors WAY-379 · WAY-392); `guidelines/testing.md` | treat WAY-328 as still binding and ignore the guidelines — it would let the tests miss the written rules | a test that breaks a rule of the guidelines is found by the review and fixed | author handoff |
| Q2 | The task's *Context* says git tracks only `.md`, `.py`, `.gitignore`, `.gitattributes` and `.python-version`. On the head it also tracks `.github/workflows/tests.yml`, `requirements-quality.in`, `requirements-quality.txt` and `ruff.toml` (the parts `repository` and `agent-instructions` claim them). | Row 1 of *Settlements to record* decides this case: the test reports each file of a kind outside the list, and the author adds a kind that is no script to the list in the test with a comment giving the reason, the four new ones included, and no file of those kinds is reported once added. The author states in its report, for each added kind, why it is no script. | `git ls-files` on the head: kinds `.yml` 1, `.in` 1, `.txt` 1, `.toml` 1 beyond the five of the list; row 1 | list the five kinds only, so that the test is red on the head — it contradicts "the check passes on the repository as it is" | the review finds a kind added that is a script, or a script kind missing | author handoff |
| Q3 | The author read WAY-344 only to its *Scope* and WAY-395 in part (its report, **Unread material**). | The whole-change reviewer reads both whole and judges the tests against WAY-344; no resumption of the author. | `reports/author-report.md` Unread material | resume the author to read them: the reviewer reads whole anyway and is independent | a finding of WAY-344 shows in the review and goes into the one fix | review-whole handoff |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| frozen task | `docs/task-cycles/script-invariants-by-test/task.md` | orchestrator | — |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| list of the tests failing before the change, taken from the merged request https://github.com/mariusznazar/the-way/pull/145 (*Checks*: the final gate ran in CI on its last head `1575669d`) | orchestrator; the base `604907c8` is a merge commit with the tree of its second parent | no run on the base; every check of that CI run passed | the list is empty |
| `python -B elements/common/foundation_check.py` on the finished change (no `--skip-test-citations`) | orchestrator, head `3043e760` | exit 0, `0 errors`, no `listed:` line | none |
| focused checks of the agents: `gate/run_tests.py elements/part-map` (51 at `4bc1667c`, 40 at `540aed04`), `elements/common` (270), `agent-instructions` (50, 2 expected failures) | author, reviewers | exit 0 each; each of the four invariants' tests seen failing once and passing after (author), repeated by the reviewer in working copies, and after the fix the narrowed `.yml`, Python 3.12 and a missing `.python-version` | the moved test was not run on 3.12 by the author (the reviewer ran it) |
| `python -B task-cycle/cycle_stages.py`, `cycle_measures.py`, `review_reminder.py origin/foundations` | orchestrator | exit 0 each; `reminder: no` (19 merges since `foundation-review/2026-11-15`, threshold 60) | none |
| `python -B task-cycle/remarks_check.py .runs/task-cycles/script-invariants-by-test` | orchestrator on the original | run 1 exit 1 (7 items listed, appended word for word), run 2 exit 0; 2 runs | none |
| final gate | CI on the request's last head (`.github/workflows/tests.yml`, trigger `pull_request`) | the final gate is the CI run on the request's last head; the cycle has no local time of it; its result stands in *Checks* of the request's description and not in the copy | not in the copy |

## Return step

- Foundation compared with code: the four invariants, WAY-38, WAY-89, WAY-09, WAY-08, WAY-61 and those the search found (WAY-03, WAY-44, WAY-60, WAY-62, WAY-63, WAY-69, WAY-321, WAY-344, WAY-379, WAY-385, WAY-392–395, WAY-401), the facts `python-stdlib-modules` and `git-path-patterns`, the part map of `agent-instructions`, `elements-common`, `invariants` and `part-map`; what no longer matched: the sentences of `agent-instructions` and `elements-common` named neither the moved script tests nor the element-directories test — corrected in `3043e760`; review `reports/review-return-report.md` PASS with two Minor findings.
- Decisions written or changed: none
- Invariants written or changed: the four `Method` fields `review` to `test` (task *To do* 5), sentences unchanged
- Environment facts: none
- Glossary terms: none
- Part-map changes: sentences of `agent-instructions` and `elements-common`
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: rows 1–3 in the code of `agent-instructions/test_script_invariants.py` (`SUFFIXES`, `NAMES`, `PLACES`; `wrong_interpreter`; `outside_imports`)

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/146, draft while the CI run waits, to be marked ready after it passes
- Description: `request.md` beside this record, written by `task-cycle/skill/request_template.md`; `request_check.py` exit 0 (1 run before the request opened), `private_paths_check.py` on it exit 0 (1 run); written and checked again after the record's commit
- Writes to the task's backlog entry: none
- Working copies left: none so far
- Directories of earlier tasks kept: none
- Corrections after the request opened: none
- Process remarks on the-way:
  - author, docs/task-cycles/script-invariants-by-test/reports/author-report.md: The task names WAY-328, withdrawn on this base (Q1 of the handoff); not looked up further.
  - author, docs/task-cycles/script-invariants-by-test/reports/author-report.md: `guidelines/coding-<kind>.md`: I found no kind that matches a test file, so none was read.
  - author, docs/task-cycles/script-invariants-by-test/reports/author-report.md: The task says git tracks only five kinds; it also tracks `.yml`, `.in`, `.txt` and `ruff.toml` (Q2 of the handoff), handled above.
  - review of the fix, docs/task-cycles/script-invariants-by-test/reports/review-fix-report.md: `git grep` for the old path `elements/part-map/test_script_invariants` at `540aed04`: no match. That is the expected result. The positive control is described under M3.
  - review of the return step, docs/task-cycles/script-invariants-by-test/reports/review-return-report.md: Unclear: what WAY-44's "Tests belong to the part they test" asks of a test of an invariant whose *Part* is `repository`. That part has no directory (WAY-09). See m2.
  - whole-change review, docs/task-cycles/script-invariants-by-test/reports/review-whole-report.md: WAY-328, named in the task's *Decisions in play*, is withdrawn on this base. The orchestrator says so (Q1), and WAY-379 and WAY-392 stand in its place in the index.
  - whole-change review, docs/task-cycles/script-invariants-by-test/reports/review-whole-report.md: Unclear: what WAY-44's "Tests belong to the part they test" asks of a test whose invariant names `repository`. That part has no directory, and WAY-09 gives it only configuration files (M3).

# Cycle record — the way: seven fixes of the cycle's instructions from the remarks after the last cycles

- Task source: `the task's note in the author's backlog`, `Status: ready for cycle`, settlements accepted 2026-11-19; frozen copy `task.md` beside this record (md5 `158e5f9c2c664d203c7c6049e52bfdbe`)
- Task relation: independent
- Product repository: https://github.com/mariusznazar/the-way (the-way itself)
- Process pin: `0b43a27d` (the checkout and the worktree are the-way itself; no pin to move)
- Target branch and base: `foundations`, `0b43a27d`
- Task branch: `task/cycle-instruction-seven-fixes`
- Status: request open

## Two questions at start

- Trust boundary: no — the change edits `task-cycle/skill/SKILL.md`, `task-cycle/plan/SKILL.md`, `task-cycle/change/SKILL.md`, `task-cycle/review/SKILL.md`, `task-cycle/slice_size.py` with its test, `elements/decisions/template.md` and three decisions of `foundations/decisions.md`; the files the part map names as the trust boundary of the `task-cycle` part (`cycle_stages.py`, `stage_transcripts.py`, `cycle_measures.py`, `gate_times.py`) are not among them
- Irreversible operation: no — text and one measuring script of the repository; nothing outside it

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none — every point of the task's *To do* gives the wording of its change, the questions of *Questions to settle* answer the places the points left open (the sentences of WAY-136, WAY-255 and WAY-134, point 4's two additions), and *Settlements to record* settles the three sentences of the decisions; the rejected variants stand in the task and are not to be restored. The orchestrator found no choice the task leaves open
- Reserved choice: none
- Execution route and reason: one author without a plan — the change is eight small text edits in five files of two parts, one change of a script with one test, and three sentences in the decision log; one agent holds it; no preliminary plan was written and no slice-size script was run
- Author: `the-way-author`, class `same` (Sonnet 5.5, the harness's closest model `sonnet`) — the change crosses two parts (task-cycle, decisions), writes three binding sentences in the decision log through the skill of the element and changes a script with a test over a large log; resumed twice (the fix of the Minor findings, the return step), no replacement
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: Claude Code; a background or resumed agent reports by completion notification, the turn is yielded when only that result remains
- Whole-change review: reviewer `fable` (the strongest class, the user's instruction `model: fable`), by `review-change`; range `0b43a27d..bcaddc2b`, `reports/review-whole-report.md`, first line `PASS bcaddc2b`; changed files with added and removed lines: `elements/decisions/template.md` 5/2, `foundations/decisions.md` 55/23, `task-cycle/change/SKILL.md` 4/2, `task-cycle/plan/SKILL.md` 3/1, `task-cycle/review/SKILL.md` 2/1, `task-cycle/skill/SKILL.md` 20/7, `task-cycle/slice_size.py` 17/11, `task-cycle/test_slice_size.py` 31/0; coverage: points 1–7 and rows 1–3 in the task's wording, no rejected variant restored; blocking 0, Minor within the task 4, outside the task 2
- Review rounds:
  - findings `reports/review-whole-fix-findings.md`, contradiction no: the fix of the four Minor findings within the task of the review of the whole change (`bcaddc2b..52801a69`, commits `76b6b172`, `20210259`, `52801a69`; author's report `reports/author-fix-report.md`), reviewed once by the same reviewer, `reports/review-fix-report.md`, `PASS 52801a69`, no finding remained or was new. Finding 1 asked for no commit (the author corrected its report), findings 2 to 4 were fixed in the commits. No blocking finding in the round; the fix of Minor findings alone, not reverted
- Weakest-point checks: author (`reports/author-report.md`): the requirement that a slice naming a range of a large decision log in *Read* is measured by the range while a slice naming none still counts the whole file; checked by a plan of two slices against the real log (range: 8 521 characters, `fits`; no range: 916 646 characters, `too large`; the base: both `too large`) and by three mutations caught by the new tests, which the reviewer repeated with four mutations, each caught

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

None: the one-author route.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 18:3x | start | orchestrator (Sonnet 5.5) | `task-cycle/skill/SKILL.md` read whole; the task read whole | — | `git fetch`: the checkout stood 16 commits behind `origin/foundations`; fast-forwarded to `0b43a27d` (clean tree, no local commits); the files of `task-cycle/skill/` did not change in that range |
| 18:4x | start | orchestrator | `python -B task-cycle/remove_merged_worktrees.py --apply --target foundations` | stdout: removed `the-way-wt/project-closure-step`; kept the main checkout and two detached checkouts that are no cycle's | exit 0; directories of cycles kept for a human decision: none |
| 18:4x | start | orchestrator | worktree `../the-way-wt/cycle-instruction-seven-fixes`, branch `task/cycle-instruction-seven-fixes` from `0b43a27d` with `--no-track` | — | created; `.runs/` ignored |
| 18:4x | start | orchestrator | base `0b43a27d` is a merge commit; `git rev-parse` of its tree and of the tree of its second parent: both `7a9697e824f719dc9496daefea05b4ec4fbc3d27` | — | no gate run on the base; the list of the failing tests taken from the merged request (see *Verification*) |
| 18:5x | start | orchestrator | the user's instruction of this run: before every full run of the gate, write that the run is about to start and wait for the signal `start` from the day's adviser; reviewers on the strongest class are dispatched with `model: fable` | — | binds the orchestrator for this cycle; no full gate is planned, since CI runs on the request and is the final gate (step 10) |
| 18:5x | author | `the-way-author`, Sonnet 5.5 (class `same`) | `reports/author-handoff.md`; `task-cycle/change/SKILL.md`, variant "the whole change as the one author"; `task.md`, `orch_index.md` | `reports/author-report.md` | dispatched in the background; completion by notification |
| 19:1x | author, return | `the-way-author` | — | `reports/author-report.md`; commits `2a0df03c`, `fc88ee2c`, `bcaddc2b` (range `0b43a27d..bcaddc2b`) | `done with concerns`. Mechanical check by the orchestrator: clean worktree, non-empty range, eight files changed, all within the task (four skills, `slice_size.py` with its test, the decision template, `foundations/decisions.md`); each check of the report has its command and exit code except the first red run of the new test, which the author ran through a pipe (the run's FAILED line stands in place of the exit code; the state before the code cannot be rerun without discarding the commit, so the report is accepted with that limit and the limit is named in *Verification*); **Unread material** names parts of WAY-316, WAY-148 and WAY-140 (decisions the change leaves unchanged) and WAY-03 (named by the examples file): the orchestrator records an autonomous choice (Q3) that they bear on nothing the author judged, and the reviewer of the whole change selects its own foundation; **Searches** items go to the process remarks. Next: the review of the whole change |
| 19:2x | review of the whole change | `the-way-stage`, `fable` (the strongest class, set by the user's instruction `model: fable`) | `reports/review-whole-handoff.md`; `task-cycle/review/SKILL.md`, "the review of the whole change"; range `0b43a27d..bcaddc2b` | `reports/review-whole-report.md` | dispatched in the background |
| 19:4x | review of the whole change, return | reviewer (`fable`) | — | `reports/review-whole-report.md`, first line `PASS bcaddc2b` | PASS; 0 blocking, 4 Minor within the task, 2 outside it (findings 5 and 6, which go to the request's list). Choices (a) and (b) accepted by the reviewer. Unread material read (named parts of WAY-05, WAY-12, WAY-385, WAY-293 opened by name only: the reviewer's own selection, a known index gap per WAY-150, no gap). The four Minor findings within the task are cut word for word into `reports/review-whole-fix-findings.md` and fixed before the request (WAY-161) |
| 19:5x | fix of the Minor findings | `the-way-author` resumed, Sonnet 5.5 (the one author's class) | `reports/author-fix-handoff.md`, `reports/review-whole-fix-findings.md`; `task-cycle/change/SKILL.md`, variant "the fix of a review's findings" | `reports/author-fix-report.md` | resumed in the background |
| 20:0x | fix, return | `the-way-author` | — | `reports/author-fix-report.md`; commits `76b6b172`, `20210259`, `52801a69` (range `bcaddc2b..52801a69`) | `done`; clean worktree, non-empty range, two files (`foundations/decisions.md`, `task-cycle/test_slice_size.py`); every check has command and exit 0; unread material only the review report (not its to read); searches `none`. Next: the review of the fix |
| 20:0x | review of the fix | reviewer (`fable`), resumed | `reports/review-fix-handoff.md`, `reports/review-whole-fix-findings.md`, `reports/author-fix-report.md`; `task-cycle/review/fix.md` | `reports/review-fix-report.md` | resumed in the background |
| 20:1x | review of the fix, return | reviewer (`fable`) | — | `reports/review-fix-report.md`, first line `PASS 52801a69` | PASS; blocking 0, Minor remaining 0, new 0; all four findings fixed; unread: parts of `author-report.md` (read the corrected section only) and WAY-136, WAY-134 not read whole again — bears on nothing the fix judged; searches none; working copies none |
| 20:1x | return step | `the-way-author` resumed, Sonnet 5.5 | `reports/author-return-handoff.md`; `task-cycle/skill/return_step.md`, `foundation_step.md` | `reports/author-return-report.md` | resumed in the background |
| 20:3x | return step, return | `the-way-author` | — | `reports/author-return-report.md` | `done`, committed nothing, so no review of it; unread material (tails of WAY-316, WAY-148 and WAY-140) was read by the reviewer of the whole change; searches none; the choices Q2 and Q4 stay rows of the questions table (recorded under *Return step*) |
| 20:4x | request | orchestrator | `git fetch`: the remote `foundations` holds no commit beyond the base, so no merge and no renumbering (no decision of the task is new); `python -B task-cycle/review_reminder.py origin/foundations` exit 0, `reminder: no`; `cycle_stages.py` and `cycle_measures.py` exit 0; `remarks_check.py` run 1 exit 1 (9 items appended word for word), run 2 exit 0 | `request.md`; https://github.com/mariusznazar/the-way/pull/151 | the description passed the form check and the check of private paths (exit 0 each, 1 run); the branch was pushed and the request opened as a draft; next: the record's copy |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | Which class of model for the one author (step 4) | `same` | the change crosses two parts and writes binding sentences into the decision log | `cheaper`: the sentences of the log and the change of the measure of a slice bear on every later cycle, and the author reads a log of 900 KB by entries | a fix round if the author errs | author |
| Q2 | Author's question (a): *Read* names one changed file both whole and by ranges — which count? (task point 4(a)) | the file counts whole: an explicit whole reading is read whole; one sentence and one test added by the author | the task's sentence "any other file counts whole where either field names it whole" and the existing test `test_changed_file_named_again_in_read_counts_once`; the measure must not count less than the agent is told to read | ranges win over a whole entry — counts less than what is read | one condition in `measure`, one sentence, one test | author; review of the whole change |
| Q3 | Author's **Unread material**: parts of WAY-316, WAY-148, WAY-140, and WAY-03 | the gaps bear on nothing the author judged: the change leaves the four decisions unchanged, and the author's checks that touch them (WAY-33 search) read their binding sentences and *Rationale* beginnings | `reports/author-report.md`, *Unread material* | resume the author to read them — the reviewer of the whole change selects its own foundation and reads them | an unseen collision, caught by that review | author's search of the foundation |
| Q4 | Author's question (b): are the ways "only the skill, the decision unchanged" (row 1) and "only the two skills" (row 2) ways of the process, which the sentence of row 3 keeps out of *Rejected*? | yes, they are ways of where the answer is recorded; they stay out | the sentence of point 5: "how or when an answer is recorded … stays out"; the task lists them under *Not chosen* of the questions and not as options of the decisions | write them into *Rejected* with the costs the source gives | two or three clauses | author; reviews |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| frozen task | `task.md` beside this record | orchestrator | — |
| index of decisions of the orchestrator's selection | `orch_index.md` beside this record | orchestrator | — |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| list of the tests failing before the change, taken from the merged request https://github.com/mariusznazar/the-way/pull/150 (*Checks*: the CI run https://github.com/mariusznazar/the-way/actions/runs/44578468147 on its last head `300d0d17`, `tests` and `tests-windows` passed in the first attempt; its committed copy `docs/task-cycles/project-closure-step/cycle.md` at `ade8e97a` says the final gate ran in CI) | orchestrator; the base `0b43a27d` is a merge commit with the tree of its second parent (`7a9697e824f719dc9496daefea05b4ec4fbc3d27` both) | no run on the base; the list is empty | none |
| `python -B gate/run_tests.py task-cycle`, `elements/common`, `agent-instructions`, `instruction-files`, `product-guidelines` (focused, not the full gate) | author at `fc88ee2c`..`bcaddc2b`, again after the fix and for `task-cycle`, `elements/common` and `agent-instructions` at `52801a69`; reviewer at `bcaddc2b` for each | exit 0 each (`task-cycle` 537 tests, `elements/common` 271, `agent-instructions` 52, `instruction-files` 105, `product-guidelines` 14) | the full gate not run on the cycle's own system |
| `python -B -m unittest task-cycle/test_slice_size.py` | author before the code (new test red) and after (19 tests) | before: 1 failure of 19, its FAILED line stands in place of an exit code (the author ran it through a pipe); after: exit 0 | the exit code of the red run before the code was not captured |
| `python -B elements/common/foundation_check.py` | author, reviewer at `bcaddc2b` and `52801a69`, return step at `52801a69` | exit 0, `0 errors` | none |
| ruff on the two changed Python files | reviewer (the pinned version), at `bcaddc2b` and `52801a69` | exit 0 | the author could not run it (not installed in its session) |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator | exit 0, `merges: 24`, `threshold: 60`, `reminder: no` | none |
| `python -B task-cycle/cycle_stages.py` and `python -B task-cycle/cycle_measures.py` naming this session | orchestrator | exit 0 each | none |
| `python -B task-cycle/remarks_check.py` on the original | orchestrator | run 1 exit 1 (9 items listed and appended word for word), run 2 exit 0 | none |
| final gate | the CI run on the request's last head (`.github/workflows/tests.yml`, trigger `pull_request` into `foundations`); the cycle has no local time of it | its result stands in *Checks* of the request's description and not in this copy | none; the full gate is not run on the cycle's own system |

## Return step

- Foundation compared with code: WAY-136, WAY-255, WAY-134 and `elements/decisions/template.md` agree with the four skills and the script; WAY-140, WAY-316, WAY-373 and WAY-148 contradict nothing the change writes, apart from the known collision of WAY-140 with WAY-316, which the task leaves (the skill takes an exception, the decisions do not); the part-map entries of `decisions` and `task-cycle` need no change; no invariant, glossary term or environment fact names the three decisions; the search of the whole foundation found nothing to correct (`reports/author-return-report.md`)
- Decisions written or changed: WAY-136, WAY-255, WAY-134 (rows 1–3, written by the foundation step, marked `the cycle's` as well for the clauses added to their *Verification* and *Rationale*); no new decision, no commit of the return step
- Invariants written or changed: none
- Environment facts: none
- Glossary terms: none
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: row 1 — WAY-136; row 2 — WAY-255; row 3 — WAY-134 (and `elements/decisions/template.md`, point 5)
- Result: the return step committed nothing, so no review of it ran; the choices Q2 (a file named whole and by ranges counts whole: in the code, the docstring and a test) and Q4 stay rows of the questions table, the first because one rule of one script is in its code and test, the second because writing it into the decisions would extend a meaning the human accepted beyond the task

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/151, draft (to be marked ready after the CI run on its last head passes)
- Description: `request.md` beside this record; first written and checked before the request opened: `python -B task-cycle/request_check.py .runs/task-cycles/cycle-instruction-seven-fixes/request.md --task .runs/task-cycles/cycle-instruction-seven-fixes/task.md` exit 0 (1 run) and `python -B task-cycle/private_paths_check.py .runs/task-cycles/cycle-instruction-seven-fixes/request.md` exit 0 (1 run); written and checked after this commit: the record's link, the checks on the copy and the CI result
- Writes to the task's line in the backlog: none (the task's line is in the author's private notes, and the cycle writes only what the product's backlog allows; the-way names its tasks key in `~/.the-way/locations.json`)
- Working copies left: none
- Directories of earlier tasks kept: none
- Corrections after the request opened: none
- Process remarks on the-way:
  - author, `.runs/task-cycles/cycle-instruction-seven-fixes/reports/author-report.md`: `ruff` not available in the session (`ruff: command not found`): the linter and the formatter were not run by me directly.
  - author, `.runs/task-cycles/cycle-instruction-seven-fixes/reports/author-report.md`: The task's sentence for point 4(a) is unclear for a file that *Read* names both whole and by ranges (see Choices 1).
  - author, `.runs/task-cycles/cycle-instruction-seven-fixes/reports/author-report.md`: The task's point 5 leaves open whether a way such as "only the skill, the decision unchanged" is a way of the process (see Choices 2); the template sentence names "how or when an answer is recorded" as an example, and where the rule is recorded is the nearest case.
  - author, `.runs/task-cycles/cycle-instruction-seven-fixes/reports/author-report.md`: Whether `task-cycle/skill/foundation_step.md` (the sentence "a decision's *Rejected*, which takes the ways not chosen that the row's source keeps, `none considered` where the human said so, or `unknown`, as the decisions' template gives") should carry the new words: unclear, since the task does not name that file; I left it.
  - review of the whole change, `.runs/task-cycles/cycle-instruction-seven-fixes/reports/review-whole-report.md`: "the lead": searched the task-cycle skills and `foundations/glossary.md` for the word; it stands in the new sentence of point 2 alone, and no entry says who it is (finding 5).
  - review of the whole change, `.runs/task-cycles/cycle-instruction-seven-fixes/reports/review-whole-report.md`: A decision or an invariant that says how `task-cycle/slice_size.py` counts a file: searched `foundations/` for `slice_size`, "too large" and "estimated tokens"; found only the withdrawn WAY-371, whose rule "stands in `task-cycle/slice_size.py`". The foundation holds nothing to compare point 4(a) with.
  - review of the whole change, `.runs/task-cycles/cycle-instruction-seven-fixes/reports/review-whole-report.md`: Whether the-way's foundation settles a way to its own running product, and whether the printed report of `slice_size.py` is "a command in a terminal" in the sense of WAY-406: searched `foundations/` and found no sentence on either.
  - review of the whole change, `.runs/task-cycles/cycle-instruction-seven-fixes/reports/review-whole-report.md`: A rule on the width of a line of Markdown: searched `elements/common/rules.md`, `instruction-files/`, `agent-instructions/`, `guidelines/` and `README.md`; none found, so the lines the edits left long or short (`task-cycle/skill/SKILL.md:218`, `elements/decisions/template.md:95`, `foundations/decisions.md:6311`, `:6331`, `:6725-6726`) are no finding.
  - review of the whole change, `.runs/task-cycles/cycle-instruction-seven-fixes/reports/review-whole-report.md`: Whether "only the skill, the decision unchanged" is "a way of the process rather than of the product": the sentence of point 5 does not say what the process is where the product is the-way, whose skills and decisions are the product (choice (b)).
  - the orchestrator: the process of the user's instruction of this run (a signal `start` from the day's adviser before every full gate) has no place in the skill; it bound this cycle only through the user's prompt, and no full gate was run, since CI is the final gate.

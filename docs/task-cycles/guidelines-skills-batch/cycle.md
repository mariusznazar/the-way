# Cycle record — the way: zbiorcze skille wytycznych kodu, testów i styleguide'u

- Task source: `the task's note in the author's backlog`, `Status: ready for cycle`; settlements accepted 2026-11-07 (frozen copy beside this record: `task.md`, sha256 `041932b8ef280dcac0c3324ed57f46ebed5d0974262f5f1a21e596446ac61699` of the uncleaned original)
- Task relation: independent
- Product repository: the-way (mariusznazar/the-way), working on itself as the top-level repository
- Process pin: none (the-way is the process itself; the checkout is the worktree)
- Target branch and base: `foundations`, `05534d381b95a4e2692875263dd0d8875097b89d`
- Task branch: `task/guidelines-skills-batch`
- Status: request open

## Two questions at start

- Trust boundary: no — the change edits skills and templates of `product-guidelines/`, a file of `project-level/task/skill/`, `instruction-files/judging.md` and `foundations/decisions.md`; the part map names as trust boundaries only `project-level/readiness_check.py`, `plan_check.py`, `plan_state.py`, `instruction-files/check_instructions.py` and `installation/install.py`, none of which the task touches.
- Irreversible operation: no — text edits and decision records in git; nothing outside the repository.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none — each of the 20 items of *To do* names the text to change and the rule it follows; the four questions and the five rows of *Settlements to record* are settled by the human (2026-11-07). Where an item leaves wording open, the wording is the author's to choose within the item (a choice of how to make what the task settles). Whether a settlement is a new decision or an edit of a standing one is answered by `record-decision`, not a design choice.
- Reserved choice: none (no language, framework, library, store, login or place to run is in play)
- Execution route and reason: one author without a plan. The change is text across a few files of one family (three discipline skills, two shared files, one instruction-files file, the decision log); each item is small and independent, and one agent can hold all 20 items and 5 decision records. Class `same` as the orchestrator's (a change across four parts: product-guidelines, project-level, instruction-files, decisions), model `sonnet`.
- Author: one author with `make-change`, class `same`, model sonnet; resumed for the fix and the return step.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: Claude Code `Agent` calls in the background report by completion notification; no limit set by the orchestrator.
- Whole-change review: opus reviewer (not the author), `review-change` with `whole_change.md`; range `05534d3..e66e8e7` (21 files, +317/-131); first line `FAIL e66e8e7`, report `reports/review-whole-report.md`; coverage table of the 20 items and 5 settlement rows in the report (all met; I1 on items 10 and 15, M1-M8 on items 1, 5, 6, 9, 14, 16, 20 and row 3); source fidelity checked against the frozen task. One-author route: no plan, so no slice per finding; the blocking finding comes from no slice.
- Review rounds: (1) whole change `05534d3..e66e8e7`: FAIL, 1 Important (I1), 8 Minor within the task (M1-M8, fixed with I1 in one fix), 2 out of scope (O1, O2); fix `e66e8e7..2c46cb7` (commit `2c46cb7`, report `reports/fix-1-report.md`); review of the fix by the same reviewer: `PASS 2c46cb7`, `reports/review-fix-1-report.md`, no blocking finding remains, one new Minor N1 left unfixed. (2) return step `2c46cb7..f5ae96f` (commit `f5ae96f`): `PASS f5ae96f`, `reports/review-return-report.md`, no findings. No revert, no blocking finding left. (3) correction for the human's remarks `120917c..9703d0b` (commit `9703d0b`, report `reports/correction-report.md`; remarks `reports/remarks-correction.md`): reviewed by the same opus reviewer, `PASS 9703d0b`, `reports/review-correction-report.md`, no findings.
- Weakest-point checks: author, item by item (requirement, the check by reading the changed passage against the item and the decision it names, what it showed) in `reports/author-report.md`; for the fix, per finding in `reports/fix-1-report.md`; the return step in `reports/return-step-report.md`. No code and no test: prose and foundation entries only.

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

None — the one-author route has no slices.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-08 | Start | orchestrator (Sonnet 5.5) | task read in full; `agent-instructions/README.md`; `task-cycle/skill/SKILL.md` | worktree `.runs/worktrees/guidelines-skills-batch`, branch `task/guidelines-skills-batch` from `foundations` `05534d3`; base checkout `.runs/base-guidelines-skills-batch` (detached `05534d3`) | gate on the base started in background, log `.runs/base-guidelines-skills-batch-gate.log` |
| 2026-11-08 | Author (whole change) | fresh general-purpose agent, sonnet (class `same`), background | `reports/handoff-author.md`; method `task-cycle/change/SKILL.md`, variant "the whole change as the one author"; frozen task `task.md` | `reports/author-report.md` | dispatched; wait for completion notification |
| 2026-11-08 | Author returned | sonnet author | `reports/author-report.md` | commits `e6d0f9e`, `e66e8e7`; 21 files, +317/-131 | `done with concerns`; mechanical check: clean worktree, non-empty range, 6 checks with command and exit code, Searches section (8 items) and own-work check present; next: review of the whole change |
| 2026-11-08 | Whole-change review | fresh general-purpose agent, opus (stronger than the orchestrator, class not cheaper), background | `reports/handoff-review-whole.md`; method `task-cycle/review/SKILL.md` + `whole_change.md`; range `05534d3..e66e8e7`; frozen task; `reports/author-report.md` | `reports/review-whole-report.md` | dispatched |
| 2026-11-08 | Whole-change review returned | opus reviewer | `reports/review-whole-report.md` | `FAIL e66e8e7`: 1 Important (I1), 8 Minor within the task (M1-M8), 2 out of scope (O1, O2) | blocking finding: fix by the author (resumed) with the Minor findings, then one review of the fix |
| 2026-11-08 | Fix of the review's findings | author resumed (sonnet) | message with `reports/findings-1.md` (I1 + M1-M8 in the reviewer's words); method `task-cycle/change/fix.md`; range from `e66e8e7` | `reports/fix-1-report.md` | dispatched; then one review of the fix by the same reviewer |
| 2026-11-08 | Fix returned | author (sonnet) | `reports/fix-1-report.md` | commit `2c46cb7`, 9 files +28/-24; status `done`; clean worktree; 6 checks with command and exit code; Searches section present | next: review of the fix by the same reviewer |
| 2026-11-08 | Review of the fix | reviewer resumed (opus) | message: range `e66e8e7..2c46cb7`, `reports/findings-1.md`, `reports/fix-1-report.md`; method `task-cycle/review/fix.md` | `reports/review-fix-1-report.md` | dispatched |
| 2026-11-08 | Review of the fix returned | opus reviewer | `reports/review-fix-1-report.md` | `PASS 2c46cb7`; no Critical/Important; one new Minor N1 (`coding/template.md` row for `### Recording a failure`, wording of one cell differs from neighbours) not fixed, goes to the request's list | next: gate on the reviewed head (separate checkout `.runs/gate-guidelines-skills-batch`, log `.runs/gate-guidelines-skills-batch-1.log`), return step |
| 2026-11-08 | Return step | author resumed (sonnet) | message naming `task-cycle/skill/foundation_step.md` and `return_step.md`; head `2c46cb7` | `reports/return-step-report.md` | dispatched |
| 2026-11-08 | Return step returned | author (sonnet) | `reports/return-step-report.md` | commit `f5ae96f` (2 files: summary sentences in `coding/SKILL.md`, `testing/SKILL.md` aligned with `hand_back.md`); no entry written; clean worktree; checks with command and exit code; Searches section present | `done`; next: review of the return step's range by a fresh reviewer |
| 2026-11-08 | Review of the return step | fresh general-purpose agent, sonnet (not cheaper than the orchestrator) | `reports/handoff-review-return.md`; range `2c46cb7..f5ae96f` | `reports/review-return-report.md` | dispatched |
| 2026-11-08 | Correction: human's remark | human, orchestrator | the human's answer to item 3 of *For you to decide*: fix the two unfixed findings (O1, O2) in this request; `correction.md` read; fetch: `origin/foundations` still `05534d3`, nothing to merge; *Reserved choice* is `none` | `reports/remarks-correction.md` | the answer binds; correction by the author (resumed, `make-change` variant "a correction for the human's remarks"), reviewed by `review-change`, return step and gate repeated as the remarks touch them |
| 2026-11-08 | Correction made | author resumed (sonnet) | message with `reports/remarks-correction.md` (O1, O2 bind) | `reports/correction-report.md`; commit `9703d0b`, 2 files (`product-guidelines/coding/SKILL.md`, `product-guidelines/testing/SKILL.md`); status `done`; clean worktree; checks with command and exit code; Searches `none` | next: review of the correction by the same reviewer |
| 2026-11-08 | Review of the correction | reviewer resumed (opus) | range `120917c..9703d0b`, remarks in place of a findings file; method `task-cycle/review/fix.md` | `reports/review-correction-report.md` | dispatched |
| 2026-11-08 | Return step repeated | author resumed (sonnet) | message: repeat for what the correction touched | `reports/return-step-2-report.md` | `done`, nothing needed correcting, no commit; Searches `none`; `foundation_check.py` exit 0 |
| 2026-11-08 | Gate on the corrected tree | orchestrator | detached checkout `.runs/gate3-guidelines-skills-batch` at `9703d0b`, log `.runs/gate-guidelines-skills-batch-3.log` | exit 0, 804 tests in 9 directories | next: stages, record copy, description for a correction |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | Did the sources change since the task was accepted? Task says `foundations` `f447bb6`. | Only `product-guidelines/{coding,styleguide,testing}/SKILL.md`: one paragraph reworded in each (`each skill named below or in the files beside this skill`), none of the task's 20 items. Line numbers of decisions moved by about 26 (WAY-240 heading at `:6988` instead of `:6962`); the author finds places by content, as the task says. | `git diff f447bb6 HEAD -- product-guidelines project-level/task instruction-files` (3 files, 12 insertions, 9 deletions) | — | none | author handoff |
| Q2 | Item 12: where does the sentence "a choice found in the product's tests is a proposal, never a rule" stand so that it reaches every path? | Moved from the testing audit file into the rules that hold across the steps of the testing skill | `reports/author-report.md`, Choices | keep in the audit file and add copies in the other paths | one line to move back | author, review |
| Q3 | Item 3: pointers to research, new tools and staged cleaning kept also inside the step files? | Named directly from the step of the skill, and kept in the step files, since the rule on variant files asks for both places | `reports/author-report.md` item 3, Choices | remove the pointers from the step files | one repeated line to delete | author, review |
| Q4 | Settlements 2 and 3: new decisions or edits of the standing ones? | New entries: the departure line of personal data as a field of a rule, and the rows of the judging table, since the standing decisions do not answer those questions | `reports/author-report.md`, Choices; reviewer left it (`reports/review-whole-report.md`, Declined to judge) | edit the form decision and the judging-table decision in place | a rename of two entries | author, foundation |
| Q5 | Settlement 5: new entry or edit? | Edit in place of the decision on a new kind of code, which answers the same question; `narrows` the standing-checks decision | `reports/author-report.md`, Choices | a new entry | two lines to move | author, foundation |
| Q6 | Item 14 and settlement 1: how is the precedence recorded? | A sentence in the binding sentences of the test-level decision and `narrows` the glossary-words decision, as the rule on precedence between decisions asks; the older decision itself is not edited | `reports/author-report.md`, Choices; `reports/return-step-report.md` | edit the older decision too | one more edited entry | author, foundation |
| Q7 | Item 6: what does a standing check "touch"? | No criterion written: left to the agent's judgement, as the decision's rationale already has it (the reviewer's smaller reading, M4) | `reports/fix-1-report.md` M4 | state a criterion in the decision (a new binding rule) | a decision edit accepted at the merge | fix, review of the fix |
| Q8 | Item 5: does the second trial run redo the audit's list of causes? | No: the rerun is "for the split alone" (the reviewer's smaller reading, M8) | `reports/fix-1-report.md` M8 | a rule for redoing the list | a decision | fix, review of the fix |
| Q9 | Item 9(e): where do kept rules keep the meaning of a failure after a departure? | In their own text; the table row moved the statement to the column of what stays (M1) | `reports/fix-1-report.md` M1 | the product's decision | one table cell | author, fix |
| Q10 | Finding I1: where is the exemplar of a level with no recipe settled? | In the settling file of the testing skill (one bullet) and one sentence in the new-level file, not in the step-3 condition of item 10 | `reports/fix-1-report.md` I1, `reports/review-fix-1-report.md` | change the condition of step 3 | a few lines | fix, review of the fix |
| Q11 | Item 18: who starts the return of the stopped skill? | The skill "returns" at the moment the human separates the work; no trigger named (no source names one) | `reports/author-report.md` Searches 3; `reports/review-whole-report.md` Searches | name `refine-task` or the human as the trigger | a sentence | author |
| Q12 | Item 20: the verdict of a proposal row in the judging table? | Left unspecified; the row is "of its own" | `reports/author-report.md` Searches 5; `reports/review-whole-report.md` Searches | add a fifth verdict | a decision | author |
| Q13 | The reviewers' out-of-scope findings O1 and O2: fixed? | Not in the first pass (the reviewer marked them out of scope, so they went to the request's list); fixed afterwards in a correction on the human's answer (commit `9703d0b`) | `reports/review-whole-report.md` | fix them in this request | scope growth | request |
| Q14 | The new Minor finding N1 of the review of the fix: fixed? | No; a Minor finding of a review of a fix is not fixed, it goes to the request's list | `reports/review-fix-1-report.md` | a second fix | an extra review round | request |
| Q15 | The remarks check read no reports: why? | It reads only files `reports/*report.md`; the stage reports were first named otherwise. Renamed to `*-report.md`, references in this record corrected | `python -B task-cycle/remarks_check.py` first run: 0 reports | none | none | orchestrator |
| Q16 | Reconciliation with the target branch (step 12): anything to merge? | No: `origin/foundations` is still `05534d3`, the base, an ancestor of the head; nothing merged, no review of a merge | `git rev-parse origin/foundations` after a fetch | merge anyway | none | orchestrator |
| Q17 | Correction: what does "the same way as the styleguide skill" mean for the coding and testing skills? | The styleguide skill's two-way paragraph and the clause of its table row copied word for word, and testing steps 2 and 4 name `research.md` and `new_tools.md` directly, the pointers inside the variant files kept | `reports/correction-report.md`; `reports/review-correction-report.md` (PASS) | rewording each skill in its own words | three skills reading differently | correction |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| Frozen task | `.runs/task-cycles/guidelines-skills-batch/task.md` | orchestrator | — |
| Author's report | `reports/author-report.md` (commits `e6d0f9e`, `e66e8e7`) | sonnet author | reviewed by `reports/review-whole-report.md` (FAIL, then fixed) |
| Fix | `reports/fix-1-report.md` (commit `2c46cb7`), findings `reports/findings-1.md` | sonnet author | `reports/review-fix-1-report.md` PASS |
| Return step | `reports/return-step-report.md` (commit `f5ae96f`) | sonnet author | `reports/review-return-report.md` PASS |
| Correction | `reports/correction-report.md` (commit `9703d0b`), remarks `reports/remarks-correction.md` | sonnet author | `reports/review-correction-report.md` PASS |
| Return step, repeated | `reports/return-step-2-report.md` (no commit) | sonnet author | no commit, so no review |
| Handoffs | `reports/handoff-author.md`, `reports/handoff-review-whole.md`, `reports/handoff-review-return.md` | orchestrator | — |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| `python -B gate/run_tests.py` on the base alone (detached checkout `.runs/base-guidelines-skills-batch`, run before any change; log `.runs/base-guidelines-skills-batch-gate.log`) | orchestrator, `05534d3`, Windows 11 | exit 0; 804 tests in 9 directories, every directory passed | no check failing on the base |
| `python -B gate/run_tests.py` on the reviewed change `2c46cb7` (step 10; detached checkout `.runs/gate-guidelines-skills-batch`; log `.runs/gate-guidelines-skills-batch-1.log`) | orchestrator, Windows 11 | exit 0; 804 tests in 9 directories, every directory passed | none failed; same count as the base |
| `python -B gate/run_tests.py` on the final tree `f5ae96f` (step 12; detached checkout `.runs/gate2-guidelines-skills-batch`; log `.runs/gate-guidelines-skills-batch-2.log`) | orchestrator, Windows 11 | exit 0; 804 tests in 9 directories, every directory passed | none failed; the tree differs from the first run by the return step's two sentences only |
| `python -B gate/run_tests.py` on the corrected tree `9703d0b` (detached checkout `.runs/gate3-guidelines-skills-batch`; log `.runs/gate-guidelines-skills-batch-3.log`) | orchestrator, Windows 11 | exit 0; 804 tests in 9 directories, every directory passed | none failed; the first gate run of the correction |
| `python -B task-cycle/review_reminder.py origin/foundations` after the fetch of the correction | orchestrator | `origin/foundations` is still `05534d3`, the base; nothing to merge, no reminder written (8 merges, threshold 30) | none |
| `python -B task-cycle/request_check.py .runs/task-cycles/guidelines-skills-batch/request.md --task .runs/task-cycles/guidelines-skills-batch/task.md` | orchestrator | last exit 0 on the final text (repeated after each edit of the description) | none |
| `python -B task-cycle/private_paths_check.py` on `request.md` | orchestrator | last exit 0 on the final text (repeated after each edit) | none |
| `python -B task-cycle/private_paths_check.py docs/task-cycles/guidelines-skills-batch` (the copy) | orchestrator | first run exit 1, 24 places listed; last exit 0, 0 listed; 3 runs | the first run's listing was cleaned by one rewriting of the copy |
| `python -B task-cycle/remarks_check.py` on the original `.runs/task-cycles/guidelines-skills-batch` | orchestrator | 4 runs: the first read 0 reports (file names), the second and third listed 20 items, the last exit 0 with nothing listed | none left |
| `python -B task-cycle/remarks_check.py docs/task-cycles/guidelines-skills-batch` (the copy) | orchestrator | 2 runs; the last exit 0, nothing listed | none |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator, after a fetch | exit 0; `merges: 8`, `threshold: 30`, `reminder: no` | none |
| `python -B elements/common/foundation_check.py`, `python -B instruction-files/check_instructions.py .`, focused tests of `instruction-files`, `project-level`, `elements/common`, `agent-instructions`, the two installation unittest modules | author, fix, return step, reviewers (commands and exit codes in their reports) | all exit 0 | `product-guidelines/**` has no test directory and `check_instructions.py` does not read it: the skill texts there were checked by reading only |

## Return step

- Foundation compared with code: by the return-step agent, `reports/return-step-report.md`: the five entries the change wrote or changed, the task's *Decisions in play* and the part map of the touched parts against the files; one mismatch, the summary sentences of where each of the two skills hands back (coding and testing skills), corrected in `f5ae96f`; nothing else differed.
- Decisions written or changed: WAY-240 (edited), WAY-216 (edited), WAY-282 (edited), WAY-310 (new), WAY-311 (new) — all by the foundation step, none by the return step
- Invariants written or changed: none
- Environment facts: none
- Glossary terms: none (the glossary template got one sentence naming the exception for test-level names, by the foundation step's search of the foundation)
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: 1 → WAY-240; 2 → WAY-310; 3 → WAY-311; 4 → WAY-282; 5 → WAY-216
- Return step repeated after the correction: `reports/return-step-2-report.md`; the entries WAY-172, WAY-124, WAY-265, WAY-256 and those the change wrote compared with the two changed skills and the part map of `product-guidelines`: all match; no commit, no entry
- Review of the return step's commit: `reports/review-return-report.md`, `PASS f5ae96f`, no findings

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/86, ready for review; corrected once for the human's remarks (the two unfixed findings), `**State: ready** — corrected for your remarks`
- Description: `request.md` beside this record, rewritten by `task-cycle/skill/request_template.md` in its variant for a correction, with the form check's last command and exit code and the number of its runs (see Verification); in the copy committed with the record: `written and checked after this commit`
- Writes to the task's backlog entry: the request link as `[url::https://github.com/mariusznazar/the-way/pull/86]` on the task's line in the backlog of the author's private notes (written at the first request); the state stays `[/]` (the human sets it on merge)
- Process remarks on the-way:
  - Author (whole change), .runs/task-cycles/guidelines-skills-batch/reports/author-report.md: Item 6: "the standing checks a new kind touches" has no definition in the task or in WAY-216. I wrote "those whose tool reads the language of the kind's files", the same criterion the row gives for the extension. This leaves unsaid how the audit of dependencies (which reads manifests, not a language) counts. A reviewer may want a sharper line.
  - Author (whole change), .runs/task-cycles/guidelines-skills-batch/reports/author-report.md: Item 5: a second trial run for the chosen set produces new reports, and the audit's list of causes is built from the reports of the first run (`trial_run.md`, last bullet). The task and WAY-204 say nothing of redoing that list. I wrote nothing about it; step 3 has already ordered and "gone back" to the causes, so redoing them is a larger rule that needs a decision.
  - Author (whole change), .runs/task-cycles/guidelines-skills-batch/reports/author-report.md: Item 18: the task does not say who starts the return of the stopped skill or where it resumes. I wrote "this skill returns" at the moment the human separates the work; the trigger (the human, or `refine-task`) is not named in any source I read.
  - Author (whole change), .runs/task-cycles/guidelines-skills-batch/reports/author-report.md: Item 9(e): the task says the remaining rules keep the meaning of "failure" and "expected refusal" but not where the meaning stands once the departed rule's heading holds only `none — <PREFIX-NN>`. I wrote "in its own text" (the kept rule's), the least rule that follows from way 3 of the departures. If the intended place is the product's decision instead, the table row changes.
  - Author (whole change), .runs/task-cycles/guidelines-skills-batch/reports/author-report.md: Item 20: the four verdicts have none for a proposal to add a rule. I wrote only "a row of its own" and left the verdict column of such a row unspecified.
  - Author (whole change), .runs/task-cycles/guidelines-skills-batch/reports/author-report.md: Item 17: step 1 of the other skill reads files of the product (`AGENTS.md`, `guidelines/`); "its mode alone" drops the refresh check and its question, but the reads that give the mode remain. The task asks only for the question to leave the audit, so I left the reads.
  - Author (whole change), .runs/task-cycles/guidelines-skills-batch/reports/author-report.md: Line numbers in the task all moved; I found each place by its content, none was missing.
  - Author (whole change), .runs/task-cycles/guidelines-skills-batch/reports/author-report.md: The handoff names `instruction-files/check_instructions.py` as the check for skill files; it checks the repository's instruction files and listed only `AGENTS.md`, `CLAUDE.md` and `agent-instructions/README.md`; it does not read `product-guidelines/**`. So the skill files I changed were checked by reading only.
  - Fix of the review's findings, .runs/task-cycles/guidelines-skills-batch/reports/fix-1-report.md: The sources give no criterion for what a standing check "touches" (M4); I left it open on purpose, as the reviewer allowed. The open point about the audit of dependencies from the first report remains for whoever refines it.
  - Fix of the review's findings, .runs/task-cycles/guidelines-skills-batch/reports/fix-1-report.md: Nothing else unclear.
  - Return step, .runs/task-cycles/guidelines-skills-batch/reports/return-step-report.md: The task says "9 shown, 5 accepted" but names only the five accepted rows; I cannot tell which of the four others (if any) is item 19 or 17, so I took "no row" as "no entry".
  - Return step, .runs/task-cycles/guidelines-skills-batch/reports/return-step-report.md: Whether WAY-95 should name WAY-240 in its own *Verification* (an example now read against WAY-240's area) is unclear; WAY-25 puts the record in WAY-240 only. I left it.
  - Return step, .runs/task-cycles/guidelines-skills-batch/reports/return-step-report.md: The questions of `author.md` listed under "Searches not found or unclear" (the audit of dependencies under "touches", the trigger of the stopped skill's return, the verdict of a proposal row in `judging.md`) remain open; no source settles them.
  - Review of the fix, .runs/task-cycles/guidelines-skills-batch/reports/review-fix-1-report.md: What a standing check "touches" (M4) now has no criterion in the skill or in WAY-216. This is the reading the review offered, and the sources give none. The question of the audit of dependencies stays open for a later refinement.
  - Whole-change review, .runs/task-cycles/guidelines-skills-batch/reports/review-whole-report.md: The author's open point 3 (who starts the return of a stopped audit after the work is separated): `hand_back.md` "return here" with `refine-task` leading the conversation is enough; no source names a trigger. Not a finding.
  - Whole-change review, .runs/task-cycles/guidelines-skills-batch/reports/review-whole-report.md: The author's open point 4 ("in its own text" for the meaning a kept rule takes): it follows from way 3 of the departures; the task does not say where the meaning stands. Only the column issue (M1) is a finding.
  - Whole-change review, .runs/task-cycles/guidelines-skills-batch/reports/review-whole-report.md: The author's open point 5: a proposal row in `judging.md` has no verdict among the four, and neither question 3 nor WAY-311 gives one. Left unclear; the source settles nothing more.
  - Whole-change review, .runs/task-cycles/guidelines-skills-batch/reports/review-whole-report.md: The author's open point 6 (the reads of the other skill's step 1 stay): it agrees with item 17. Not a finding.
  - Whole-change review, .runs/task-cycles/guidelines-skills-batch/reports/review-whole-report.md: Item 8 at "the first guidelines": `guidelines/coding.md` does not exist then, so the clause is vacuous. The task asks for it; it does no harm.
  - Whole-change review, .runs/task-cycles/guidelines-skills-batch/reports/review-whole-report.md: `check_instructions.py` does not read `product-guidelines/**` (the author's point 8); the skill texts were checked by reading only.

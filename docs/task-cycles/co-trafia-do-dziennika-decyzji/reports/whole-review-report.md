PASS 39d702a61fce67962c5788dbac8636dc5c6e67ae

# Review of the whole change — co-trafia-do-dziennika-decyzji

Range `ac753401de0bfaae0b9b8175c10c17387736f8d8..39d702a61fce67962c5788dbac8636dc5c6e67ae`. `git rev-parse HEAD` printed `39d702a61fce67962c5788dbac8636dc5c6e67ae`, the head given. The reviewed worktree was clean before and after the review.

Result: 0 Critical, 0 Important, 15 Minor (14 within the task, 1 outside it), 0 blocking. No question for the orchestrator is open.

## Verdict in short

The change does what the frozen task, the spec and the plan ask. The script reads and checks the line `decision:`, learns the base from git, reports decisions that nothing holds (error when the change adds or alters them, listed otherwise) and lists an invariant whose sentence changed while no citing file did. I verified each by reading the script and its tests and by two negative controls on a clean worktree of the head. The thirteen edited decisions and the two attached paragraphs say what the code and the templates do. The five questions stand once, in `elements/decisions/template.md`. The findings are small gaps of wording and one cost of the script that has no effect on any result.

## Findings

All findings are Minor. "Slice" names the slice of the plan the finding comes from; a finding that cannot be blocking has no fix route of its own but belongs to the findings file of the fix if the cycle makes one (they are within the task unless the line says otherwise).

### M1. The foundation check reads every non-Markdown file of the base through one git process each, for a result that the base side never changes

- Place: `elements/common/foundation_check.py:759-763` (`list_invariants`: `git ls-tree -r` of the base, then `at_commit` per file).
- Slice: 4 (`12286a5`).
- What: when at least one invariant reading `test` has a reworded sentence, the script starts one `git show` for every non-Markdown file the base holds, only to learn which files cited the invariant at the base. I traced the cases: a file that cites at the base and is unchanged also cites now, and a file that changed or was deleted is in `changed` and so excludes the listing in either set; the set of citing files at the base changes no result. The slice 4 executor says the same (no test fails on its removal). The executor of slice 4 also says the cost is only on a candidate; that is right, but a candidate is the ordinary case of the change this entry exists for.
- Why it matters: measured here, 62 non-Markdown files cost 5.2 s with `subprocess.run(["git","show",...])` (about 0.08 s each) and the whole run of the script rose from 1.3 s to 6.0 s when I reworded `fingerprint-definition`. A product with a thousand non-Markdown files would pay about 80 s, five thousand about 400 s, on every run of its gate while such a rewording stands. The spec (D1) names `git grep` for this reading.
- Evidence: `python -B elements/common/foundation_check.py` in a detached worktree of the head, 1.3 s clean and 6.0 s with the sentence of `fingerprint-definition` reworded (listed line printed, exit 0).
- To settle: drop the base-side set (the test `test_citing_file_deleted_is_a_change_and_not_listed` keeps its value through `changed`), or read the base with one `git grep` call.

### M2. The docstring of the script calls the report of an uncited invariant "the last report named below"

- Place: `elements/common/foundation_check.py:11`.
- Slice: 3 and 4 (`ea2d186`, `12286a5`) added two reports after it, in the same docstring.
- What: "The switch `--skip-test-citations` skips the last report named below, the invariant that reads `test` and has no citing line." The report of decisions that nothing holds and the listing of a reworded invariant now stand after it (lines 78-93). A reader who takes "last" literally takes the switch to skip the listing too; WAY-321, which the change does not alter, says the switch skips that one report only.
- Why it matters: a name that stopped being true (WAY-362); the code skips only the one report (checked: `check_held` and `list_invariants` run before and apart from `if not skip_test_citations`, and `test_skip_switch_skips_nothing_of_the_decisions_nothing_holds` protects it).
- To settle: replace "the last report named below" with "the report named at line 66" or with the words of the report.

### M3. The decision skill points "the switch of step 3" and means step 4.3 of the shared way of working

- Place: `elements/decisions/skill/SKILL.md:41`.
- Slice: 6 (`64cd4ad`).
- What: the added bullet says the run "right after the entry is written ... and the switch of step 3 does not skip that report". Step 3 of this skill is "Draft", which names no switch; the switch is passed in step 4.3 of `elements/common/way_of_working.md` (also WAY-321).
- Why it matters: a reader of the skill looks for the switch in the wrong step.
- To settle: write "the switch of the run in step 4 of `way_of_working.md`" or name `--skip-test-citations`.

### M4. The task template does not give the values of the column *Goes to* that spec D5 lists

- Place: `project-level/task/template.md:203-210`; also `elements/common/skill/task_variant.md:26-28`.
- Slice: 7 (`f20a62c`).
- What: D5 gives the cell values (`sentence of <PREFIX-NN>`, `skill or instruction file: <name or path>`, `guidelines: <discipline>`, `data or code: <place>`, and `decision`, `invariant`, `glossary term`, `environment fact` as before). The template lists the places in words and says "each named as those questions name it"; the questions name places, not a form of cell. Only `product-guidelines/template.md:114` writes `guidelines: <discipline>`. The executor chose this to avoid copying the questions (its report says so).
- Why it matters: two writers of a table write the cell two ways; the foundation step must read the cell as a place. No script reads it, so nothing breaks today. The task's own text (*To do* 2) is met.
- To settle: write the four value forms once in the paragraph of "Settlements to record" (they are values, not the questions).

### M5. Row 1's threshold sentence stands in the template and in no entry of the log

- Place: `foundations/decisions.md:390` (WAY-11) against `elements/decisions/template.md:148-149`.
- Slice: none (foundation entries step, `d629ed8`).
- What: row 1 of *Settlements to record* is accepted as a decision (change of WAY-11) and reads "wpisem zostaje tylko to, co przeszło wszystkie, i tylko tam, gdzie ktoś, kto decyzji nie zna, zrobiłby inaczej, a test, który go zatrzyma, nie powie mu dlaczego". WAY-11 binds "only where it passes all of them" and does not carry the second half. The agent of the foundation entries says so in its report (choice 1). The template carries the sentence (as *To do* 1 asks), so no agent works wrongly, but the log's entry is narrower than the row the human accepted, and the sentence has no one-line reason beside it in the template.
- Why it matters: the row's meaning is to be written whole (WAY-134); a reader of the log does not find the threshold.
- To settle: add the threshold to a binding sentence of WAY-11 (the entry is held by its pair, so the check passes) or record by a decision of the human that the template alone carries it.

### M6. The lower part of the request description is not extended for a guidelines rule the cycle found

- Place: `task-cycle/skill/request_template.md:291-297` (kind 6, done) and `:449-452` (*Foundation entries*, not done).
- Slice: 9 (`39d702a`).
- What: D7 says a rule the cycle found itself is named in kind 6 and in *Foundation entries* of the lower part. Slice 9 extended kind 6 and, in the lower part, only the invariant listing and the tests with `decision:`; the plan's Goal for slice 9 also named only kind 6.
- Why it matters: the lower part is the full list of what the human is shown; a rule found by the cycle is absent from it. Small, since kind 6 reaches the human.
- To settle: one clause in the lower part, or a note that the lower part lists entries and a rule with *Decision* `none` is no entry.

### M7. Kind 7 says "without the switch" where the switch it means is not named

- Place: `task-cycle/skill/request_template.md:436-441`.
- Slice: 9. The executor raised it as a concern (report, "Concern and question").
- What: the spec's word "switch" is `--skip-test-citations`. The template names none.
- To settle: write "without `--skip-test-citations`".

### M8. The step for a row that goes outside the log says nothing of how it is written there

- Place: `task-cycle/skill/foundation_step.md:7-13` and `task-cycle/skill/return_step.md:14-18`.
- Slice: 7 and 6.
- What: the foundation step still says "Each is written by following the pinned `SKILL.md` of its element", and lists the five elements; a row that goes to a skill, to guidelines or to the product's data has no `SKILL.md`. `decide_entry.md:5-9` says what to do for a rule that the questions send elsewhere (written in the same change, a guidelines rule as the guidelines template gives it), but a writer of the foundation step does not read that file for such a row. `return_step.md` says "go to the place the questions ... give it", without the sentence that no entry is written there (*To do* 3: "nie powstaje wpis"). Nothing is wrong in either sentence; the rule is implicit.
- Why it matters: a row going to a skill or to code reaches the writer with no named way to write it.
- To settle: one sentence in `foundation_step.md` ("a row whose column names no element is written in its place by the rule of that place, in the same change as the code") and "no entry is written" in `return_step.md`.

### M9. WAY-134 and WAY-115 now say different things about the column; WAY-134's *Rejected* cites a rule of WAY-19 that this change rewrote

- Place: `foundations/decisions.md:2836` (WAY-115, "its kind"), `:3611` onward (WAY-134, "in place of its kind"), `:3710` (WAY-134 *Rejected*: "a new rule beside an existing one is a new question (WAY-19)").
- Slice: none (foundation entries step).
- What: WAY-115 binds the table to show "its kind"; WAY-134, which derives from WAY-115, replaces the kind by the place in task mode, with no relation recording the precedence between the two. The spec judged WAY-115 to need no change. Separately, WAY-19 no longer says "a new rule next to an existing decision is a new question" (it now says a part that cannot change apart from an entry is its sentence), and WAY-134's *Rejected* still quotes the old rule as its argument against folding the rule into WAY-29. The argument still holds (WAY-29's question is independent), but its parenthetical reads the old WAY-19.
- Why it matters: a reader compares two entries that disagree on one word; WAY-25 asks for a recorded precedence where two applicable decisions collide.
- To settle: add "narrows" or reword "its kind" in WAY-115 to "its kind or its place"; reword the clause of WAY-134's *Rejected*.

### M10. WAY-17 still reads as a closed chain

- Place: `foundations/decisions.md:578` (WAY-17, unchanged; its *Verification* reads `none`, so the script lists it).
- Slice: none.
- What: "Every link of the chain fact → decision → invariant → test is written ..., and none is optional ... a check names its invariant". A test that holds a decision's sentence by `decision:` names the decision, with no invariant between. The spec says to leave WAY-17 alone unless the foundation step found the chain stated as closed; it is stated so.
- Why it matters: small; the entries WAY-12, WAY-22 and the template state the new path.
- To settle: one clause in WAY-17 (this makes it a changed decision; it then needs a pair of examples or the same would stop the gate, as spec D2 warns).

### M11. The docstring of `README.md`/script and the decision log carry lines over the width

- Place: `foundations/decisions.md:5221` (WAY-167 rationale, broken line), `foundations/decisions.md:3711ff` (WAY-134, short and long lines mixed), `task-cycle/skill/foundation_step.md:9` and `:19`, `task-cycle/skill/request_template.md:437` and `:450`, `product-guidelines/template.md:12` (the word "and" alone on a line), `product-guidelines/template.md:353`.
- Slice: foundation entries step, 7, 8, 9.
- What: reflow left lines of 100-170 characters and one orphan word. Cosmetic, no sentence read wrongly.
- To settle: reflow.

### M12. The script grew by 290 lines (694 to 984) into one class that now has about 40 methods; the file of tests by 457 (1052 to 1509)

- Place: `elements/common/foundation_check.py` (`Foundation`, `list_invariants` about 40 lines, `check_decision_line` about 42 lines, `check_held` about 28).
- Slice: 1 to 4.
- What: numbers from `python -B task-cycle/change_file_sizes.py ac75340... 39d702a...` (exit 0). The-way has no coding guidelines and no rule of size (WAY-328), so there is no test of the invariant to run and no threshold was crossed; each of the three functions I read stays well below any usual limit and does one thing. No code without a user except M1.
- Grade: Minor by WAY-363 (no rule of size). To settle: if the script keeps growing, move the base and the listing into a module of their own; not needed now.

### M13. A `decision:` comment line in a product's own code is now an error at the line

- Place: `elements/common/foundation_check.py:150-151` (`CITATION` now matches `decision` as well).
- Slice: 1.
- What: any tracked non-Markdown file with a comment line that starts a comment sign followed by `decision:` (for example `// decision: use a queue`) is reported as `decision: gives no decision number as the log writes it`. The spec (D3) mandates this form and error, as it does for `invariant:`; slice 1 read the-way's own files and found none. A product pinned to this commit that has such a comment finds it at its first run.
- Grade: Minor and outside the task (the spec decided it); named so the orchestrator can name it in the request if it wants.

### M14. `decide_entry.md` words "where the first yes is not the log" although question 4 ends in no place

- Place: `elements/decisions/skill/decide_entry.md:5-9`.
- Slice: 6.
- What: "Where the first 'yes' is not the log, no entry is written, and the rule goes to the place that answer names". Question 4 ("only the lack of a feature") names no place; it is not written. Question 5 is a "yes" that is the log. The sentence after it covers 5 and the template covers 4, so no agent works wrongly.
- To settle: "or, where it is question 4, is not written".

### M15. Two tests of slice 4 pass before the code and the reason is the base-side set

- Place: `elements/common/test_foundation_check.py` (`test_citing_file_deleted_is_a_change_and_not_listed`).
- Slice: 4.
- What: eight of the nine tests of slice 4 passed before its code (they assert that nothing is listed, which the old script never wrote). I checked each fails when the matching rule is broken (changed set, method, added invariant, no citing file, missing field): the tests protect the behaviour. Only M1's base-side set has no test; with it removed the deleted-file test still passes through `changed`.
- Grade: Minor; no action beyond M1.

## What I judged and kept as it stands

- The choices of the orchestrator. (1) `--skip-test-citations` skips only the report WAY-321 names and WAY-321 is unchanged: followed (`check_held` and `list_invariants` stand outside the `if not skip_test_citations`; a test pins it). (2) "A decision the change changes" is a change of its binding sentences, whitespace-normalised: followed (`binding` plus `" ".join`). A wrong one would flood or silence the gate; this one is the cheapest correct reading. (3) Rows 11 and 12 are attached paragraphs of WAY-12 and WAY-03: followed; each paragraph has 2 or 3 sentences (counted by script for all thirteen entries: every paragraph stands at 1-3 sentences). (4) The unknown-base line is written only where the log holds a decision, and a base lacking `foundations/decisions.md` or `foundations/invariants.md` is unknown for that file, never an empty one: followed and tested; `installation/test_install.py::test_empty_foundations_have_valid_form` is unchanged (ran as part of nothing I reran; slice 2 reports it, and my run of `elements/common` and the empty-log test in the test file cover the same rule). (5) Pair-then-trim stands in step 3 of `elements/decisions/skill/SKILL.md` and in `task-cycle/skill/return_step.md`: followed. (6) `task-cycle/record_template.md` is edited for the item naming a row's place: followed, one item changed, label kept.
- Slice 2's choice: a remote HEAD that shares no history with HEAD makes the base unknown, with no fall back to `main`. I judge it right: the order is of branches, D1 gives it so, and a fall back would pick a base from a branch the repository does not name as main. The test `test_remote_head_naming_another_branch_is_preferred_over_main` protects the order.
- Slice 5's change of the non-goal sentence in "Trade-off principles and non-goals": needed (WAY-22 now gives such a sentence a test with a line `decision:` and no invariant, and the old sentence said a derived invariant) and right.
- The base in this checkout: the script finds it as `git merge-base HEAD` the first of `refs/remotes/origin/HEAD` (here `refs/remotes/origin/foundations`), `refs/heads/main`, `refs/heads/master`. Here it gives `ac753401...`; the executors of slices 3 and 4 saw no base because their checkouts had no `origin/HEAD`, which the script handles as the one listed line. Not a defect of the code.
- The base case in the-way's own foundation: with the base known, the thirteen edited decisions and the two paragraphs stay held (each by its pair). Negative control: in a detached worktree of the head I reworded the binding sentence of WAY-17 (held by nothing): the script printed `foundations/decisions.md:578: `WAY-17` is added or changed by this change and nothing holds it: ...`, `1 error`, exit 1. The worktree was removed.
- The `decision:` lines of the tests: seven distinct quotations of WAY-12 and WAY-03 stand in their entries (the script reads them in the real repository and passes). No test file gives a `decision:` line for WAY-02, whose attached sentence the tests of the line also exercise; D8 names WAY-12 and WAY-03 only.
- No template, skill or request file copies the five questions: `grep` for each question text finds it once, in `elements/decisions/template.md`. The enumerations of places in WAY-134 and in `project-level/task/template.md` list places, not questions.
- The surface `foundation-check-command`: path, one argument (a root), exit codes 0, 1, 2 are kept (`main`, `run` read); nothing new a caller must pass; the script starts only git and stays on the standard library; the names `elements/part-map/test_cross_part_imports.py` imports stay. Not a trust boundary of the part map.
- Reserved choices: none taken (no language, framework, library, store, login or place to run).
- Invariant tests: no invariant test is changed by this change; no invariant is written or edited.

## Coverage of the task

*To do* 1-9:

1. Five questions, threshold sentence and the the-way variant of question 1: `elements/decisions/template.md:135-155`; WAY-293 second paragraph; WAY-11. Threshold absent from the log (M5).
2. Column *Goes to*: `project-level/task/template.md`, `task_variant.md`, `build_table.md`, `foundation_step.md`, WAY-134. Values not spelled out (M4); how a row outside the log is written is implicit (M8).
3. Return step and decision skill apply the questions and the report names the place: `return_step.md:14-18, 26-27`, `decide_entry.md:5-9`, `record_template.md:184-186`.
4. Guidelines rule with no decision: `product-guidelines/template.md`; WAY-168, 167, 171, 172; kind 6 of the request template.
5. Part of a question is a sentence; 1-3 sentences per part: template "Changing a decision" and "Binding sentences"; WAY-19, WAY-05.
6. Line `decision:` with quotation, `tests:` clause, pair only for the part no test holds, no derived invariant, named in the request, reasoning kept whole: script (reading and errors), template "Verification", WAY-12, 22, 03, 02, request kind 7. The pairs of WAY-12 and WAY-03 stay for the return step (see below).
7. Decisions that nothing holds: error for added or altered, listed otherwise: `check_held`, the base, tests, WAY-12 attached paragraph, README lines.
8. Invariant whose sentence changed with its test left alone: `list_invariants`, tests, WAY-03 attached paragraph, request kind 7 and lower part.
9. The thirteen decisions: WAY-02, 03, 05, 11, 12, 19, 22, 134, 167, 168, 171, 172, 293 say what points 1-8 say (read in the diff and in the entries as they stand; no `should`, `will`, `!`, capital keyword or file name in a binding sentence or in the new *Rationale* text, checked by script).

*Settlements to record*, rows 1-12: each is met by the entry or text it was given to (row 1 partly: M5; row 3 M4 and M8). *Rejected* ways of the answered questions are kept where the plan said (WAY-293 (a) and (c), WAY-172 (b) and (c), WAY-05 (a) and (c), WAY-22 (b), WAY-02 (a) and (c), WAY-12 (a) and (b)).

Carried questions: (1) the base: `origin/HEAD`, then `main`, then `master`, `git merge-base`, no new argument or exit code. (2) The script that lists the invariant: `foundation_check.py`; the request names it in kind 7 and in the lower part. (3) *Goes to* replaces *Kind* in the task table, and the table of a definition keeps *Kind* (`definition_template.md:288`).

Source fidelity: nothing is taken from the task that is altered or invented; the one omission is M5. Where the entries use words the task lacks ("held", "reworded"), WAY-12 defines "held" in its own sentence and no one reads "reworded" wrongly.

## Slices that had no review of their own

I judged each as section 2 gives, own-work check included.

- Foundation entries `ac75340..d629ed8`: matches the code and the templates (checked entry by entry above). Findings M5, M9, M10, M11.
- Slice 1 `d629ed8..6440ca9` (cheaper): the reading of the line is right against D3 (number, quotation, three words, sentence start through the paragraph start or `. `, text after, Markdown and untracked files). Six of nine tests passed before the code because the old generic check of numbers gives the same outcome; the three that guard new behaviour (no quotation, text after, quotation outside the binding sentences, only rationale, inside a sentence, fewer than three words) fail before. Own-work check adequate. Finding M13 (outside).
- Slice 2 `6440ca9..269fecc`: right; the git failure modes (no commit, shallow, base lacking a file, non-UTF-8 file, remote HEAD dangling) each have a test; the fix the executor made (`at_commit` on bytes) is sound. M2 partly.
- Slice 3 `269fecc..ea2d186`: right; the held test, the stale line counted as held (reported once), an entry of the earlier form or with no *Verification* left to the check of fields, and the listed and error outputs match D2. The concern the executor names (a *Verification* of `TODO` gives a second report for a new decision) is the spec's rule and the check of fields already reports it; not a finding. M2.
- Slice 4 `ea2d186..12286a5` (cheaper): right against D4; M1, M15. Both READMEs now describe the script (`README.md:81-88`, `agent-instructions/README.md:13-17`); the split of one sentence there changes no meaning.
- Slice 5 `12286a5..c8dcc56`: the template says what the spec says; the five questions are in D6's words; WAY-35 holds. Judged the non-goal sentence above.
- Slice 6 `c8dcc56..64cd4ad` (cheaper): M3, M8, M14.
- Slice 7 `64cd4ad..f20a62c` (cheaper): M4, M8, M9, M11.
- Slice 8 `f20a62c..5c4db42` (cheaper): the template says what D7 says, `none` in the *Decision* line, the bullet on examples reworded, WAY-173 kept; the guidelines checks of the script read no *Decision* `none`. M11 (the lone "and").
- Slice 9 `5c4db42..39d702a` (cheaper): M6, M7.

## Declined to judge

- A `decision:` comment line in a product's code becoming an error: the spec's own rule (D3); named as M13 for the request only.
- Whether the human wants the switch to skip the error of a decision that a later slice holds (spec D2 gives the question as open and the human did not see it): outside this review; it belongs to the line for the request's decisions for the human.
- The merge of the moved `origin/foundations` (PR #116: the decisions template and the log): the orchestrator's step 12.
- The text of the thirteen entries against the human's native wording of the rows: I compared with the English of the task document only for the meaning; the Polish sentences of the request belong to the request's writer.

## Notes for the return step (not findings)

- WAY-12 and WAY-03 now carry tests with a `decision:` line. Per the entries' own rule their *Verification* should name those tests by the clause `tests:` and keep a pair only for the part no test holds; both still hold their whole pairs and no `tests:` clause (the entries report, choice 6). The return step is to make that edit; the script keeps them held by the lines either way.
- Entries read by the script as changed in the return step stay held (a pair or a test line) or the script stops: WAY-17 has neither (listed today); if M10 is taken, give it a pair.

## Checks run

| Check | Command | Result |
|---|---|---|
| Head | `git rev-parse HEAD` | `39d702a61fce67962c5788dbac8636dc5c6e67ae` |
| File sizes | `python -B task-cycle/change_file_sizes.py ac753401de0bfaae0b9b8175c10c17387736f8d8 39d702a61fce67962c5788dbac8636dc5c6e67ae` | exit 0; 17 files, +1025 lines |
| Foundation of the-way | `python -B elements/common/foundation_check.py` (reviewed worktree) | exit 0; one listed line (WAY-17), `0 errors` |
| Tests of the directory | `python -B gate/run_tests.py elements/common` | exit 0; `Ran 198 tests ... OK` |
| Entry points | `python -B agent-instructions/skill_entry_points.py` | exit 0; `entry points are current` |
| Negative control, decisions | the same script in a detached worktree of the head after rewording the binding sentence of WAY-17 | exit 1; `WAY-17 ... is added or changed by this change and nothing holds it`; `1 error` |
| Negative control, invariant | the same after rewording the sentence of `fingerprint-definition` | exit 0; one `listed:` line for it naming `relation-model/test_fingerprint.py`; 6.0 s against 1.3 s |
| Cost of reading the base | Python loop of `git show ac75340:<file>` over the 62 non-Markdown files | 5.2 s |
| Sentences of the thirteen entries | a script over `foundations/decisions.md` using the script's `binding` | every paragraph 1-3 sentences; no `should`, `will`, capital keyword or file name in the new text |
| Search for copies of the questions | `grep` for each question text | one place, `elements/decisions/template.md` |

Not run: the gate (`python -B gate/run_tests.py` with no directory), `gate/run_tests.py installation`, `project-level`, `task-cycle`, `agent-instructions` and `process-audit` (the executors' runs are in their reports; a repeat is the gate's). The worktree I made for the controls was removed with `git worktree remove`.

## Reaches beyond the dispatch

- `foundations/glossary.md` entries "binding part", "binding sentence" and "invariant test": to compare the script's reading of binding sentences with the glossary.
- `foundations/invariants.md` entries `fingerprint-definition`, `test-method-citation`, `map-reference-target`: to choose a candidate for the negative control and to see who cites it.
- `foundations/part_map.md` whole: to name the touched parts.
- `product-guidelines/template.md`, `task-cycle/skill/foundation_step.md`, `return_step.md`, `request_template.md` (parts), `elements/common/skill/task_variant.md`, `build_table.md`, `project-level/task/template.md` (parts): to read the changed files whole where the diff alone did not show a finding.
- `foundations/decisions.md` WAY-14, 17, 18, 22, 26, 33, 35, 36, 60, 65, 114, 115, 344 whole: to compare each with the new text where the spec names them.
- Every report of the slices and of the foundation entries agent.
- A search of the repository for the old *Kind* column and for "tests live only", "names no decision", "a new rule next to": to find what the change should have brought in line.

## Unread material

Counts for the selection of decisions (parts touched: decisions, elements-common, project-level, task-cycle, product-guidelines, agent-instructions; 291 decisions whose *Scope* names one of them): read whole 20 (WAY-01, 02, 03, 10, 11, 12, 14, 17, 18, 22, 26, 33, 35, 36, 60, 65, 114, 115, 134, 344); read as the change's own hunks with their binding sentences, fields and the changed rationale, not the untouched remainder, 7 (WAY-05, 19, 167, 168, 171, 172, 293); by title only 264.

Decisions that bear on the change and that I did not open: WAY-113, 124, 126, 25, 30, 38, 61, 150, 161, 169, 170, 173, 174, 213, 235, 241, 263, 268, 286, 287, 290, 315, 321, 364. I took their bearing from the spec's list "Other decisions of the log the change reaches", from the code (WAY-321, 61) and from the entries that cite them. The untouched parts of WAY-05, 19, 167, 168, 171, 172 and 293 (their older *Rationale* and *Rejected*) are unread; I read the entry whole only for the seven that are in the first list. No guideline file exists in the-way (`guidelines/` is absent), so none is unread. The task and the spec were read whole; the plan was read whole; the reports of slices 1 to 7 and of the foundation entries agent were read in the parts that bear on findings, those of slices 8 and 9 in their concerns and unread sections. `elements/part-map/test_cross_part_imports.py` and `installation/test_install.py` were not opened (the names the first imports are kept, checked in the script; the empty-log rule of the second is in the executor's run and in my reading of `list_unknown_base`).

## Searches not found or unclear

- Not found: a test with a line `decision:` for WAY-02 (not required by D8); an invariant or test that holds WAY-17 (its *Verification* reads `none`).
- Not found: the five questions copied outside `elements/decisions/template.md` (the wanted result).
- Unclear: whether the cycle wants the request to name the unknown-base listing (a product run without `origin/HEAD` prints it); kind 7 asks only for the `listed:` lines of a corrected invariant, and I left the question open.
- Unclear: the spec's "(a changed file with such a line)" in D4 for tests whose line `decision:` the change "alters": the request template says "adds, drops or alters"; WAY-03's Verification says the same and its binding sentence says "alters". I read them as one rule.
- The orchestrator's handoff said the executors of slices 3 and 4 saw an unknown base here; with `refs/remotes/origin/HEAD` set the base is known in this checkout, as I ran it.

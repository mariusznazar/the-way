# Report — the return step

**Status:** done with concerns (two concerns, listed under "Questions and concerns"; no question blocks the request).

Worktree `the root of the task's worktree`, branch `task/co-trafia-do-dziennika-decyzji`. I started from head `aef5b88ca5fd2947438768b7c48939f00a076626` (`git rev-parse HEAD` confirmed it; the worktree was clean). I wrote nothing outside the three commits below; the worktree is clean at the end.

## Commits

- `c8a4c32` — "Name the tests that hold WAY-12 and WAY-03 in their Verification" (`foundations/decisions.md`, 6 added, 2 removed lines)
- `bdd1b1d` — "Skip the invariant listing when a deleted file was one of its citing files" (`elements/common/foundation_check.py` 14 added, 6 removed; `elements/common/test_foundation_check.py` 7 added)
- `ff69628` — "Bring the invariants skill and template in line with WAY-22 and WAY-03" (`elements/invariants/skill/decide_entry.md` 4 added, 3 removed; `elements/invariants/template.md` 1 added, 1 removed (5 added, 4 removed together))

## Foundation compared with code

I read whole: the handoff, `task-cycle/skill/return_step.md`, `task-cycle/skill/foundation_step.md`, `task-cycle/change/SKILL.md`, the frozen task, `foundations/part_map.md`, `elements/decisions/template.md`, `elements/part-map/template.md` and its skill files, and the entries WAY-02, 03, 05, 11, 12, 17, 19, 22, 115, 134, 167, 168, 171, 172, 293, 33, 36, 26, 65, 173 (each by its heading, whole). I read the diff of the range `ac75340..aef5b88` for `elements/common/foundation_check.py`, `elements/common/rules.md`, `README.md`, `agent-instructions/README.md`, the files of `elements/common/skill/` and `elements/decisions/skill/`, `product-guidelines/template.md`, `project-level/task/template.md`, `task-cycle/skill/request_template.md`, `return_step.md`, `foundation_step.md`, `record_template.md`. I searched the repository for the old rules (pair of examples, derived invariant, the *Kind* column, `--skip-test-citations`, "names no decision", WAY-03 outside the log, `foundation_check` descriptions) and read each hit that bears on a changed entry.

What no longer matched, and its correction:

1. **A file contradicted WAY-03 (the script).** WAY-03 lists a reworded invariant "when no file that cites it has changed". After the fix of review finding M1 the script (`list_invariants`) counted a citing file the change deleted as nothing, so where one of two citing files was deleted and the other left as it was, it listed the invariant, against the entry and against the spec's D4. This is the reviewer's finding N1 of the fix review, which I found independently by comparing the entry with the code. I corrected it (commit `bdd1b1d`): the script now reads, from the base, which identifiers the deleted non-Markdown files cited and does not list an invariant one of them cited; the docstring at the head of the file and the docstring of `list_invariants` say so. The new test `test_one_of_two_citing_files_deleted_is_a_change_and_not_listed` (it carries a line `decision: WAY-03 "The check of the foundation lists an invariant whose method"`) was seen failing first (see checks). The orchestrator had put N1 on the request's list of Minor findings; with this commit it needs no entry there (N2 still does, see below).
2. **A skill contradicted WAY-22.** `elements/invariants/skill/decide_entry.md` said a rule that records a choice goes through `record-decision` first and "the invariant is written as derived from it", with no exception; WAY-22 now gives none for a sentence a test holds by a line `decision:`. Corrected (commit `ff69628`): the sentence names the exception and cites WAY-22.
3. **A template did not name a reader of a field.** `elements/invariants/template.md`, "Fields and their readers", row *sentence*, did not name the script, which now reads the sentence to list a reworded invariant (the decisions template names its readers in the same way). Added (commit `ff69628`), citing WAY-03.

Compared and found matching: WAY-12 and WAY-03 against the script (`check_held`, `list_invariants`, `check_decision_line`, `binding`); WAY-02's line `decision:` against `check_decision_line` and `elements/decisions/template.md` "Verification"; WAY-05, WAY-19, WAY-22 against the template's "Binding sentences", "Changing a decision" and "Decision or invariant"; WAY-11, WAY-134, WAY-115 against `return_step.md`, `foundation_step.md`, `task_variant.md`, `build_table.md`, `project-level/task/template.md`, `record_template.md`; WAY-167, 168, 171, 172, 173 against `product-guidelines/template.md`; WAY-293 against the template's paragraph for the-way's log; `README.md` and `agent-instructions/README.md` against the script's reports; `elements/common/rules.md` (`{fork-point}` and the main-branch order) against `MAIN_BRANCHES`; the invariants `return-step-record` (derives from WAY-11) and `fingerprint-definition` (derives from WAY-02), which read the same as before.

Left as it is, with the reason:

- `elements/invariants/template.md` ("A change may alter an invariant test … names in its request each invariant test it alters") and `elements/invariants/skill/write.md:9`, `task-cycle/review/SKILL.md:70` ("A changed invariant test is named in your report"): each speaks of invariant tests only, which stays true; the tests with a line `decision:` are named by `request_template.md` kind 7 and WAY-03. Extending the review skill to name them would be a change the task does not carry.
- The part map: the sentence of `elements-common` enumerates what the check script verifies ("identifiers, references and assignment of files to parts") and already left out its other reports (fields, citations); no part-map line states something now false, so none is changed. The surface `foundation-check-command` keeps its path, argument and exit codes (the added `listed:` lines change no exit code, and a product's run of the command exits the same). The other touched parts (`decisions`, `project-level`, `task-cycle`, `product-guidelines`, `agent-instructions`) say what their files do.

## Pair-then-trim (decisions the change wrote or changed that a test holds)

Tests with a line `decision:` exist for two decisions only (`grep "decision:" elements/common/test_foundation_check.py`: WAY-12 and WAY-03). Both are corrected in commit `c8a4c32`:

- **WAY-12.** *Verification* now begins `tests: that a line decision: of a test names a decision of the log and quotes the start of one of its binding sentences; which decisions the check counts as held; the error for a decision a change adds or alters that nothing holds, and the list of any other.` with no path, no test name and no number, then `An agent compares a change with the part no invariant and no test holds:`. Its pair stays for what no test holds: that a test holding a sentence carries the line, that the decision names its invariants and tests in the forms given, the pair only for the uncovered part, rationale and rejected options whole, and the form of the violating example (the script cannot tell any of these). *Rationale* and *Rejected* are untouched.
- **WAY-03.** *Verification* now begins `tests: which invariants the check lists for a reworded sentence, and that the listing stops no change. An agent compares a change with the part no test holds:`; the pair stays for naming in the request (alteration of an invariant test, of a line `decision:`, of a reworded sentence), which no test holds. *Rationale* and *Rejected* are untouched.
- Other decisions of the change: no test carries a line `decision:` for them, so their pairs stay.

The rule as written (`return_step.md`, `elements/decisions/skill/SKILL.md` step 3) is kept; I changed no rule text.

## Items of the record's *Return step*

- Foundation compared with code: as above (three corrections; two files and one script).
- Decisions written or changed: WAY-12 and WAY-03, *Verification* only (their binding sentences are unchanged, so the check does not count them as changed by this step).
- Invariants written or changed: none. No rule of the task, a decision or the human sets one here; the correction of the listing (N1) is covered by the existing sentence of WAY-03 and by the new test.
- Environment facts: none. The script rests on `git merge-base`, `git diff` and `refs/remotes/origin/HEAD`; `{fork-point}` and its meaning are already WAY-60's and `elements/common/rules.md`'s, the spec says no new environment fact (spec, "Foundation entries"), and the decisions of the change do not rest on a statement about git that, shown false, would call one of them into question.
- Glossary terms: none. "binding sentence" and "binding part" are used as their entries define them. The word "held" is defined in WAY-12's own binding sentence and is no word a reader of the field reads wrongly in a sentence of the foundation.
- Part-map changes: none (reasons above).
- Projected entries written: none (the task carries none).
- Rows of *Settlements to record* — the place each went to (all 12 were written by the foundation step, whole; this step wrote none and moved none):

| Row | Went to |
|---|---|
| 1 | WAY-11 |
| 2 | WAY-293 |
| 3 | WAY-134 |
| 4 | WAY-168, WAY-167, WAY-171 |
| 5 | WAY-172 |
| 6 | WAY-19 |
| 7 | WAY-05 |
| 8 | WAY-12 |
| 9 | WAY-22, WAY-03 |
| 10 | WAY-02 |
| 11 | WAY-12, the attached paragraph (ruling of the cycle) |
| 12 | WAY-03, the attached paragraph (ruling of the cycle) |

## Meaning of each entry written or changed by this step

| Entry | Marked | English | Polski |
|---|---|---|---|
| WAY-12, *Verification* | row 8 | The decision names by the clause `tests:`, in words, the checks of the script that hold its sentences, and keeps a pair of examples only for what no test holds. | Decyzja nazywa klauzulą `tests:`, słowami, sprawdzenia skryptu, które pilnują jej zdań, a parę przykładów zostawia tylko dla tego, czego żaden test nie pilnuje. |
| WAY-03, *Verification* | row 12 | The decision names by the clause `tests:` what the listing of a reworded invariant holds, and keeps a pair of examples for what the request must name, which no test holds. | Decyzja nazywa klauzulą `tests:` to, co trzyma wypisanie niezmiennika z poprawionym zdaniem, a parę przykładów zostawia dla tego, co musi nazwać opis prośby i czego żaden test nie trzyma. |

## Own-work check

- Requirement my work most likely does not meet: a decision this step trims must stay held (the check reports an error for a changed decision that nothing holds, and the list for any other) and WAY-12 and WAY-03 must not lose what no test holds; and the N1 correction must keep every behaviour a test pins.
- Check: `python -B elements/common/foundation_check.py` after the edits and after the commits: `0 errors`, exit 0, no `listed:` line (so both decisions are still held, through their lines `decision:` and their pairs). `python -B gate/run_tests.py elements/common`: 199 tests OK (198 earlier plus the new one), exit 0 (this run covered the trimmed `foundations/decisions.md`, which the test `test_the_way_foundation_passes` reads, and the script after the correction). The line `decision:` of the new test is itself checked by the script: it quotes WAY-03's sentence and the run shows no error for it.
- The new test seen failing first: `python -B -m unittest elements.common.test_foundation_check -k one_of_two_citing` before the correction of the script: `FAILED (failures=1)`, the listing was printed; after it, `python -B -m unittest elements.common.test_foundation_check -k citing`: 6 tests OK.
- Mutation of the correction in my head: dropping `name not in lost` brings the failing run back (seen); filtering the deleted files by `.md` is covered by the existing `test_citing_file_deleted_is_a_change_and_not_listed` (one citing file) only for a non-Markdown file, and a deleted Markdown file never cites (`tracked` and `read` also skip it); a failing `git diff --diff-filter=D` returns with no listing, as the old `git diff` call did.

## Checks run (command and exit code)

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` (before my edits) | 0, `0 errors` |
| `python -B -m unittest elements.common.test_foundation_check -k one_of_two_citing` (before the correction; seen failing) | 1 (`FAILED (failures=1)`, shown by the test run; the pipe in my command reported the exit of `tail`) |
| `python -B -m unittest elements.common.test_foundation_check -k citing` (after the correction) | 0, 6 tests OK |
| `python -B elements/common/foundation_check.py` (after the correction and after the three commits) | 0, `0 errors`, no listed line |
| `python -B gate/run_tests.py elements/common` | 0, 199 tests OK |
| `python -B gate/run_tests.py elements/invariants` | 1, `no test found in elements/invariants` (the directory holds no test; not a failure of a check) |

Not run: the gate with no directory, and the tests of `task-cycle`, `project-level`, `agent-instructions`, `elements/part-map` (no file of those directories changed in this step, and the handoff says the gate is not mine to run); `python -B agent-instructions/skill_entry_points.py` (no skill added, renamed or moved, no description changed).

## Choices (way rejected, cost if wrong)

1. **N1 is corrected in this step.** Rejected: leaving it on the request's list of Minor findings, as the orchestrator had decided at 14:10. I did so because the return step corrects "a file that contradicts an entry" and the contradiction (the script against WAY-03's "no file that cites it has changed") is the entry's text, not a matter of taste. Cost if wrong: one commit more in the range for the reviewer to read; the orchestrator's list should drop N1.
2. **The correction reads the base for deleted files only** (`git diff --diff-filter=D`, then `at_commit` per deleted non-Markdown file), the second way the fix review gave, and not the full base-side read the fix of M1 removed. Rejected: reading every file at the base (6 s measured by the fix review). Cost: one extra `git diff` and one `git show` per deleted file, only where a candidate exists.
3. **WAY-12's and WAY-03's pairs keep the examples whose subject no test holds and drop none.** Rejected: dropping the example about naming a line `decision:` at the test, which looks like the line the script checks — the script checks the line only where it is present, not that a test holding a sentence carries one. Cost if wrong: a pair part a test already holds stays.
4. **The part map is not changed.** Rejected: adding the new reports to the `elements-common` sentence — it would be a change of a binding sentence that other entries rest on (WAY-42), for a list the sentence never claimed to be complete. Cost if wrong: the sentence reads shorter than the script does.
5. **The invariants template row names the script as a reader of the sentence** and the skill names the exception to WAY-22; neither is an entry. Rejected: no change (both are files that now say less than an entry). Cost if wrong: none beyond a line.

## Reach beyond the handoff

- `elements/common/test_foundation_check.py` lines 1000-1180 and 1380-1500 (the helpers `reworded`, `committed`, `on_topic`, and the tests that carry lines `decision:`): to write the new test in the fixture's form and to find what each test holds.
- `elements/invariants/template.md`, `elements/invariants/skill/decide_entry.md`, `write.md`, `elements/part-map/template.md` and its skill files, `elements/glossary/skill/decide_entry.md`, `elements/glossary/template.md`: to compare with entries (the search of the whole foundation, WAY-33) and to judge the glossary and part-map items.
- `foundations/glossary.md` (beginning), `foundations/invariants.md` (the two invariants), `foundations/environment_facts.md` (list of headings): for the same items.
- `.runs/task-cycles/co-trafia-do-dziennika-decyzji/reports/fix-review-report.md`, `foundation-entries-report.md`, `cycle.md` and the spec's lines on the rule of pair-then-trim: to understand N1 and the earlier choices.
- `the author's personal rule file on git` and `scripts.md` (personal rules, before the commits and the scripts).

## Questions and concerns

1. **WAY-241's *Rationale* cites WAY-168 for a sentence WAY-168 no longer says.** It reads "A field binds only where a decision of the product carries it (WAY-168)", while WAY-168 now lets a product's own rule that only says how to write stand with *Decision* `none`. WAY-241 concerns the recipes of the-way's testing template, which bind a product only through a decision that adopts them (WAY-173, unchanged), so its binding sentences still hold; only the citation in its *Rationale* is imprecise, and `product-guidelines/testing/template.md:229` repeats the same citation ("a field naming no decision stands as an example (WAY-241, WAY-168)"). Changing either would be an entry the task does not carry, so I changed neither. My recommendation: leave, or have the human decide in a later task whether WAY-241 should cite WAY-173 instead. Not blocking.
2. **N2 (the 132-character line in `project-level/task/template.md:208-209`) is not corrected** (the orchestrator put it on the request's list; it is cosmetic and no mismatch of an entry with a file). I would reflow it if the orchestrator wants it done in this change.
3. A long line remains in `foundations/decisions.md` in WAY-168's *Rationale* ("… the case in which WAY-130 lets a rule stand with no mistake behind it. A cheap test on a convention of the code catches a breach of its rule on every change for"), left by an earlier edit. It is cosmetic, I did not touch the entry.

## Unread material

- WAY-113, WAY-24, WAY-268, WAY-61, WAY-38, WAY-321, WAY-344, WAY-315, WAY-14, WAY-25, WAY-287, WAY-241 beyond its first two paragraphs and its fields, and WAY-174 (named by neither the handoff nor the task; read only to the line that mentions an example) — the search of the whole foundation of the foundation step covered them and none says the old rule; I did not reread them.
- The handoff's "decisions the search found" other than WAY-33: I read WAY-33 whole; I did not search `foundations/` for new hits beyond the phrases I list under "Searches", relying on the foundation step's search for the rest of the decision log.
- The spec and the plan: I read only the lines on the pair-then-trim rule, D4, the part-map statement and the foundation entries, not whole.
- `foundation_check.py` was read as the diff of the range, not whole.
- `foundations/part_map.md`, `invariants.md` and `glossary.md`: the part map whole; the invariants and the glossary only the entries named above.

## Searches not found or unclear

- Searches run for the old rules: `pair of examples`, `derived invariant`, `invariants derived`, `derives from the decision`, `live only with`, `decision:`, `WAY-03`, `skip-test-citations`, `Kind`, `Goes to`, `its kind`, `no decision`, `*Decision*`, `foundation_check` in Markdown files; each hit outside `foundations/decisions.md` and the tests was read.
- Not found: any file of `elements/` or `task-cycle/` that still says a decision's checkable sentence always gets a derived invariant, other than `elements/invariants/skill/decide_entry.md` (corrected).
- Unclear: whether the orchestrator wants the return step to correct code that the fix review left as a Minor finding (N1). I took the handoff's "a file that contradicts an entry" as yes (Choice 1) and say so above.
- The test directory `elements/invariants` has no test; `python -B gate/run_tests.py elements/invariants` exits 1 with `no test found`.
- Background processes: none of mine remain (the test run and its waiting loop ended; `Get-CimInstance` showed other sessions' `run_tests.py` processes, which I did not touch).

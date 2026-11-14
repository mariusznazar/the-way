# Report — the return step again, for correction 1

**Status:** done. Nothing no longer matches; no commit made.

Worktree `the root of the task's worktree`, branch `task/co-trafia-do-dziennika-decyzji`, head `8571691effd77b70b96293f3184ac700c4ca7784` (`git rev-parse HEAD`); worktree clean before and after. Commits: none.

## What was compared

I read the handoff and the human's remarks, and the diff of the correction (`git diff 306a122..HEAD`, the two commits `7a5fea4` and `8571691`, 6 files). I read whole the entries WAY-03, WAY-12 and WAY-241 as they now stand (extract of `foundations/decisions.md`, with WAY-173 and WAY-168 checked at the places where WAY-241 and the testing template cite them), and compared them with:

- `README.md` (lines 80-90) and `agent-instructions/README.md` (lines 10-20) against the reports of `elements/common/foundation_check.py` (its docstring and the code of `check_held`, `list_invariants`, `check_decision_line`, read in the first return step; the script is unchanged by the correction): the READMEs now say "adds or whose binding sentences it alters" and "each invariant that reads `test`", which the docstring and code say.
- `task-cycle/skill/request_template.md` kind 7 (line 305) and the lower part (line 458) against WAY-03's *Verification*: "a test that holds a sentence of a decision by a line `decision:`, where the change adds, drops or alters the test or its line" is what the *Verification* of WAY-03 says in its first example ("adds, drops or alters a test that holds … or alters its line"); WAY-03's binding sentence ("alters … a test that holds a sentence of a decision by a line `decision:`") is not changed and is covered by both.
- `product-guidelines/testing/template.md:229` and WAY-241's *Rationale*: both cite WAY-173 for "a field that binds only through a decision of the product"; WAY-173's binding sentence says that (a template's rules bind a product only through a decision of its log that adopts them). The other WAY-168 citations of the testing template (rules with *Invariant* `none`) still match WAY-168.
- `elements/decisions/template.md` ("Verification", "Decision or invariant"), `elements/invariants/template.md` (row *sentence*) and `elements/invariants/skill/decide_entry.md` (the lines the first return step corrected): they still say what WAY-12, WAY-22 and WAY-03 say; the correction did not touch them.
- The part map: `foundation-check-command` (path, argument, exit codes) is kept by the unchanged script; `elements-common` says what its files answer for, as before (reasons in `return-report.md`).
- The merge `f398251` brought entries and files from the main branch that the correction does not bear on (a template paragraph on a product's own measurements, an invariant of the installation command, the installation code); I read the diffs of `elements/decisions/template.md`, `elements/environment-facts/template.md` and `foundations/invariants.md` and found no sentence that says something about the lines `decision:`, the held decisions or the listing of invariants; I did not compare the rest of the merge.

## What no longer matched and its correction

None.

## Items of the record's *Return step* for this correction

- Decisions written or changed by this step: none (WAY-03's *Verification* and WAY-241's *Rationale* were changed by the correction, not by this step; WAY-03's pair stays for the part no test holds, which the pair-then-trim rule asks for, and the tests that hold its second paragraph are named by the clause `tests:` as before).
- Invariants, glossary terms, environment facts, part-map changes, projected entries: none written or changed.
- Rows of *Settlements to record*: unchanged; each row stays where the first return step recorded it (rows 1 to 12: WAY-11; WAY-293; WAY-134; WAY-168, WAY-167, WAY-171; WAY-172; WAY-19; WAY-05; WAY-12; WAY-22 and WAY-03; WAY-02; WAY-12 attached paragraph; WAY-03 attached paragraph).

## Own-work check

- Requirement most likely not met: no file that says the same as WAY-03 as the correction rewrote it, or the citation of WAY-173, still states the old text.
- Check: searched the tracked files (`git grep` of ``line `decision:` ``, ``decision:``, `WAY-168`, `WAY-173` and "adds, drops or alters") outside `foundations/decisions.md`; the only files that state when a change names a test with a line `decision:` are `request_template.md` (two places, both corrected by the correction) and WAY-03; the only files that state what the READMEs state are the docstring of the script and the two READMEs, which now agree. `python -B elements/common/foundation_check.py`: exit 0, `0 errors`, no `listed:` line.

## Checks run

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` (at head `8571691`) | 0, `0 errors` |

Not run: the tests of any directory (nothing was changed by this step, and the script the correction left unchanged was tested in the first return step: `python -B gate/run_tests.py elements/common`, 199 tests OK, exit 0).

## Unread material

- The two review reports of the correction (`unread-review-report.md`, `unread-fix-review-report.md`) and the findings m1–m5 and o1: not read; the handoff puts them outside this step.
- The rest of the merge `f398251` (installation code and tests, plan skill files, the new entries of the log that the merge brought): not compared, as it does not bear on the correction.
- `foundations/decisions.md` outside WAY-03, WAY-12, WAY-241, WAY-173, WAY-168 (cited places only): not read in this round.

## Searches not found or unclear

none. No background process was started in this round.

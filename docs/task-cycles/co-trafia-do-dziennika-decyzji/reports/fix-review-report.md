PASS aef5b88ca5fd2947438768b7c48939f00a076626

# Review of the fix of the Minor findings

Range `39d702a61fce67962c5788dbac8636dc5c6e67ae..aef5b88ca5fd2947438768b7c48939f00a076626` (five commits). `git rev-parse HEAD` printed `aef5b88ca5fd2947438768b7c48939f00a076626`; the worktree was clean before and after. Method: `task-cycle/review/fix.md`. The findings file bounds the review: M1-M11 and M14 (M12, M13, M15 are not taken, as the review said).

Result: all twelve findings fixed. No new Critical or Important finding. Two new Minor findings (N1, N2), neither blocking. One of them (N1) comes from my own advice for M1, which was incomplete.

## Each finding

- **M1 (base-side read of citing files): fixed as to the cost; leaves N1.** `list_invariants` no longer runs `git ls-tree -r` and one `git show` per file (`elements/common/foundation_check.py`, the block that is gone sat at lines 759-763). The run of the script with a reworded `fingerprint-definition` took 1.6 s by the fix agent's report, against the 6.0 s I measured. All 198 tests pass, including `test_citing_file_deleted_is_a_change_and_not_listed`. But my finding said the base-side set "changes no result" and that was wrong in one case; see N1.
- **M2 (docstring "the last report"): fixed.** `foundation_check.py:11-14` now names the report by its opening words and says "skips only"; the second docstring bullet and the docstring of `list_invariants` match the new reading.
- **M3 ("the switch of step 3"): fixed.** `elements/decisions/skill/SKILL.md:41-43` names `--skip-test-citations` and points to step 4 of `elements/common/way_of_working.md`, where item 3 gives it.
- **M4 (values of *Goes to*): fixed.** `project-level/task/template.md:203-209` gives the eight forms once (`decision`, `invariant`, `glossary term`, `environment fact`, `sentence of <PREFIX-NN>`, `skill or instruction file: <name or path>`, `guidelines: <discipline>`, `data or code: <place>`); `task_variant.md:28-29` points to the paragraph and copies none. The five questions are still not copied (WAY-35).
- **M5 (threshold sentence in the log): fixed.** WAY-11's second binding sentence now reads "only where it passes all of them and where someone who does not know the decision would do otherwise and a test that stops them would not tell them why". The paragraph still has 3 sentences by the count script; WAY-11 stays held by its invariant and its pair. The wording agrees with `elements/decisions/template.md:148-149`. The extra sentence in WAY-11's *Rationale* ("An entry that nobody would act against, or whose test already tells why, only repeats what the code says.") I judge right: it gives the threshold the reason I said it lacked, names no file, script or count (WAY-05), and changes no meaning the human accepted; keep it.
- **M6 (lower part of the request): fixed.** `task-cycle/skill/request_template.md` now ends *Foundation entries* with a sentence naming a guidelines rule with *Decision* `none` that the cycle found (WAY-172).
- **M7 (the switch in kind 7): fixed.** Kind 7 says "without `--skip-test-citations`".
- **M8 (rows outside the log): fixed.** `foundation_step.md` has one sentence: a row whose column names no element is written in its place by the rule of that place, in the same change as the code, and no entry is written for it; "Each is written" became "Each entry is written", so the sentence about `SKILL.md` no longer reaches such a row. `return_step.md` adds "where the place is another, no entry is written".
- **M9 (WAY-115 and WAY-134): fixed.** WAY-115 says the table shows "its kind or its place"; WAY-134's *Rejected* now reads "the rule can change apart from it, so it is a question of its own (WAY-19)", which matches WAY-19 as it stands. The word-level diff of `foundations/decisions.md` shows only these changes plus WAY-11, WAY-17 and the reflow; no other word moved. Both entries keep their pairs.
- **M10 (WAY-17 a closed chain): fixed.** WAY-17's last binding sentence now allows a check that holds a decision's sentence by `decision:` to name that decision with no invariant between; its *Verification* went from `none` to a pair of examples that says what holds and what breaks. It is held, so the listing of WAY-17 is gone: `python -B elements/common/foundation_check.py` printed only `0 errors`. The entry has one binding paragraph of one sentence (count script).
- **M11 (reflow): fixed in the lines the fix touched; the anchor `product-guidelines/template.md:353` does not exist.** The file has 145 lines; I confirm the fix agent's note, and I cannot say which anchor I meant (the lone "and" of line 12, which is fixed, is the one thing I saw there). The reflowed places read the same: the word-level diff of the decisions and the diff of the other files show no changed word except the intended ones. N2 is the only line the fix newly leaves over the width.
- **M14 (question 4 in `decide_entry.md`): fixed.** "...no entry is written: the rule goes to the place that answer names, in the same change, or, where it is question 4, is not written."

## New findings in the fix range

### N1. Minor (new, caused by the fix of M1; no blocking). A reworded invariant is listed when one of two citing files was deleted

- Place: `elements/common/foundation_check.py`, `list_invariants` (the loop over `tracked`, the base-side set gone).
- What: the invariant's citing files are now only those git tracks today, so a citing file the change deleted is no longer among them. Spec D4 and WAY-03 say the listing is made only "when no file that cites it has changed", a deleted file counting as changed (WAY-65: a file that cited at the fork point is an invariant test). With two citing files, one unchanged and one deleted, the old code did not list the invariant and the new one does.
- Evidence: I built a small product (`elements/common/test_foundation_check.py` constants `FILES` and `INVARIANTS`) with `tests/test_saving.py` and `tests/test_other.py` both citing `save-round-trip`, committed on `main`, then on a branch reworded the sentence and `git rm`ed `tests/test_other.py`: the script printed `foundations/invariants.md:3: listed: `save-round-trip` ... while no file citing it changed (tests/test_saving.py)`, exit 0, `0 errors`. By D4 it should not be listed. No test pins this case: `test_citing_file_deleted_is_a_change_and_not_listed` has one citing file.
- Why it matters: a false listing, nothing stops, and the request names a deleted test anyway under WAY-03; the docstring now says "a file the change deleted cites nothing now, so it leaves the invariant with no citing file", which is true only for the sole citer. My review said the set changed no result; that was incomplete, and the fault of the advice is mine.
- To settle: read only the deleted files at the base (`git diff --name-only --diff-filter=D -z <base>`, then `at_commit` for those few) and add them to the citing set; or take the false listing as the price and say so in the docstring. Add the two-citer test.

### N2. Minor (new). One new line over the width

- Place: `project-level/task/template.md:208-209`: `"nothing" is a rejected row with that reason. An environment fact stands only where a kept decision or invariant rests on it, and` is 132 characters. `foundation_step.md` line 9 and three lines of WAY-134's *Rejected*/WAY-17 are 102-105 characters.
- Cosmetic; no sentence is read wrongly. Reflow when the file is next touched.

## Did the fix break what the change did

- The script keeps every behaviour a test pins: `python -B gate/run_tests.py elements/common` exit 0, 198 tests OK (146 s). N1 is a case no test pins.
- The edited entries stay at one to three sentences per paragraph: WAY-02 [3], 03 [2, 3], 05 [3], 11 [3], 12 [3, 3], 17 [1], 19 [3], 22 [3], 115 [3], 134 [3], 167 [3], 168 [3], 171 [3], 172 [3], 293 [3, 2] (count by the script's `binding` and a sentence splitter).
- The foundation of the-way passes with no listed line: `python -B elements/common/foundation_check.py` exit 0, `0 errors`.
- WAY-115, WAY-134, WAY-17 and WAY-11 as they now stand agree with each other, with WAY-19, with the template and with the task template.
- No file the fix touched is outside the findings' places except `task_variant.md` (M4's second place) and `project-level/task/template.md`, both named by M4.

## Checks run

| Check | Command | Result |
|---|---|---|
| Head | `git rev-parse HEAD` | `aef5b88ca5fd2947438768b7c48939f00a076626` |
| Diff | `git log --oneline 39d702a..HEAD`, `git diff -w 39d702a..HEAD` (code and text), word-level `git diff --word-diff` of `foundations/decisions.md` | read whole |
| Foundation of the-way | `python -B elements/common/foundation_check.py` | exit 0; `0 errors`; no listed line |
| Tests of the directory | `python -B gate/run_tests.py elements/common` | exit 0; 198 tests OK |
| Sentences per paragraph | script over `foundations/decisions.md` | all 1-3 |
| Case of N1 | the script on a temporary two-citer product in the scratchpad (`mini`) | exit 0; the invariant listed |
| Lines over 100 characters added by the fix | `git diff -U0` and `awk` | 7 lines, 1 of 132 characters |

Not run: the gate with no directory; `task-cycle`, `project-level` and `agent-instructions` (the fix report gives their exit codes). No background process of mine is left; the temporary product lies in the scratchpad, outside the repository.

## Unread material

The fix's own report was read whole; the findings file and the fix handoff's rulings were read whole. I did not reread the rest of `foundations/decisions.md` or the decisions I counted by title in the review of the whole change; for the entries the fix changed (WAY-11, 17, 115, 134, 167) I read the changed hunks by word diff and WAY-11, WAY-17 and WAY-115 as they now stand; WAY-134 and WAY-167 only at the changed lines. I did not read `reports/fix-handoff.md` (the rulings are quoted in the handoff I was given).

## Searches not found or unclear

- `product-guidelines/template.md:353` of M11: not found (file has 145 lines); my anchor was wrong.
- Unclear to me: whether the cycle wants N1 settled in this fix (a Minor finding of a fix blocks nothing); I give both ways above.

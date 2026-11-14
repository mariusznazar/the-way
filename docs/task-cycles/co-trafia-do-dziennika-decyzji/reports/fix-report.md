# Report of the fix of the Minor findings of the review of the whole change

**Status:** done

Range: `39d702a61fce67962c5788dbac8636dc5c6e67ae..HEAD`. The worktree is clean.

## Commits

| Commit | What |
|---|---|
| `d06a9ac` | M1, M2: `elements/common/foundation_check.py` |
| `52214b4` | M3, M14: `elements/decisions/skill/SKILL.md`, `elements/decisions/skill/decide_entry.md` |
| `f06353c` | M4: `project-level/task/template.md`, `elements/common/skill/task_variant.md` |
| `41c20d9` | M6, M7, M8, M11 (part): `task-cycle/skill/request_template.md`, `task-cycle/skill/foundation_step.md`, `task-cycle/skill/return_step.md`, `product-guidelines/template.md` |
| `aef5b88` | M5, M9, M10, M11 (part): `foundations/decisions.md` |

Files changed (added/removed lines, `git diff --stat 39d702a..HEAD`): see that command; ten files, about 166 added and 155 removed, most of the count being reflowed lines that change no word.

## Each finding

- **M1 fixed.** Dropped the base-side set of citing files in `list_invariants` (the `git ls-tree -r` plus one `at_commit` per non-Markdown file). Only the files `tracked` now count as citing, and `changed` still excludes any file the change altered, added or deleted. Docstring of the script and of `list_invariants` no longer say "at the base or now". No test changed: `test_citing_file_deleted_is_a_change_and_not_listed` passes as it was (a deleted file is not in `tracked`, so the invariant has no citing file and the report of an uncited invariant fires, with no `listed:` line). Evidence: with the sentence of `fingerprint-definition` reworded in the worktree, the run of the script took 1.6 s (`time python -B elements/common/foundation_check.py`, listed line printed, `0 errors`), against the reviewer's 6.0 s; the rewording was reverted with `git checkout` and the tree is clean.
- **M2 fixed.** "the last report named below" replaced by the words of the report: "skips only the report of an invariant that reads `test` and has no citing line, the one that begins "an invariant whose *Method* reads `test`" below".
- **M3 fixed.** `elements/decisions/skill/SKILL.md`: "the switch of step 3" is now "the switch `--skip-test-citations` of that run, which step 4 of `elements/common/way_of_working.md` gives". The run itself is item 3 of step 4 there (checked in the file).
- **M4 fixed.** The paragraph "Settlements to record" of `project-level/task/template.md` now writes the forms once: `decision`, `invariant`, `glossary term`, `environment fact`; `sentence of <PREFIX-NN>`; `skill or instruction file: <name or path>`; `guidelines: <discipline>`; `data or code: <place>`. `task_variant.md` step 2 points to that paragraph and copies none.
- **M5 fixed.** WAY-11, second sentence of its binding paragraph: "... and as an entry of the decision log only where it passes all of them and where someone who does not know the decision would do otherwise and a test that stops them would not tell them why". The paragraph stays at two sentences. I also added one sentence to its *Rationale* ("An entry that nobody would act against, or whose test already tells why, only repeats what the code says.") so that the threshold has a reason beside it, as the finding says it lacked; this is a small addition beyond the ruling, easy to drop if unwanted. WAY-11 is held by its invariant and its pair, so no further holder was needed.
- **M6 fixed.** The lower part *Foundation entries* of `task-cycle/skill/request_template.md` has one added sentence: a guidelines rule with no decision that the cycle found itself stands there too, named as a rule whose *Decision* reads `none` (WAY-172, the same citation kind 6 gives).
- **M7 fixed.** Kind 7 now says "without `--skip-test-citations`".
- **M8 fixed.** `foundation_step.md`: one sentence says a row whose column names no element (a skill or instruction file, a guidelines discipline, the product's data or code) is written in its place by the rule of that place, in the same change as the code, and no entry is written. `return_step.md`: "where the log is one such place; where the place is another, no entry is written."
- **M9 fixed.** Decisions changed and why:
  - WAY-115: "its kind" became "its kind or its place" in its binding paragraph (the table of candidates shows the place in task mode). Its pair of examples already holds it.
  - WAY-134, *Rejected*: the parenthetical "a new rule beside an existing one is a new question (WAY-19)" became "the rule can change apart from it, so it is a question of its own (WAY-19)", which matches what WAY-19 now says. *Rejected* is no binding sentence; WAY-134 keeps its pair of examples.
- **M10 fixed.** WAY-17: the last binding sentence now ends "and a check names its invariant, or, where it holds a decision's sentence by a line `decision:`, that decision, with no invariant between." WAY-17's *Verification* went from `none` to a pair of examples (`complies`, `violates`), so the entry is held and the one `listed:` line for it is gone.
- **M11 fixed in what I touched.** Reflowed, changing no word (a script joined and re-wrapped at 100 characters, then I read the diffs): WAY-167 rationale (the 125-character line), WAY-134 (binding paragraph tail, both *Verification* items, *Rationale*, *Rejected*), WAY-115 first paragraph, WAY-11 and WAY-17 binding paragraphs; `foundation_step.md` first paragraph; `return_step.md` second half of the first paragraph; `request_template.md` kind 7 and the end of *Foundation entries*; `product-guidelines/template.md` lines 11-14 (the orphan "and" is gone). Not reflowed: lines over 100 characters that I did not touch (for example `product-guidelines/template.md` lines 90-144 and `foundation_step.md` line 30), because the finding names touched lines.
- **M14 fixed.** `decide_entry.md`: "no entry is written: the rule goes to the place that answer names, in the same change, or, where it is question 4, is not written".
- Not taken, as the handoff says: M12, M13, M15.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` : exit 0, `0 errors`, no `listed:` line (the WAY-17 one is gone).
- `python -B gate/run_tests.py elements/common` : exit 0, 198 tests OK.
- `python -B gate/run_tests.py task-cycle` : exit 0, 394 tests OK.
- `python -B gate/run_tests.py project-level` : exit 0, 275 tests OK.
- `python -B gate/run_tests.py agent-instructions` : exit 0, 25 tests OK.
- `python -B agent-instructions/skill_entry_points.py` : exit 0, "entry points are current".
- The gate with no directory: not run (the orchestrator's alone).
- I ran these once, after all edits and before the commits; the commits changed no file after that.

## Own-work check

The requirement most likely not met: the fix of M1 must keep every behaviour the tests pin, above all the deleted-file case, and remove the cost. Check: the tests of `elements/common` (including `test_citing_file_deleted_is_a_change_and_not_listed` and the whole family `test_reworded_*`) pass, and the timed run above gives 1.6 s with the listing printed. I did not see a test fail for the removed set (none can, as the slice 4 executor and the reviewer said); this is a removal of dead work, not a behaviour change, so I broke nothing to see it fail.

## Reach beyond the dispatch

none. I read only the files the findings name, WAY-11, WAY-17, WAY-115, WAY-134, WAY-167 (to reflow), `elements/decisions/template.md` (question list), `elements/common/way_of_working.md` (step numbers) and spec D5 (grep of its lines).

## Questions and concerns

- M11 names `product-guidelines/template.md:353`; that file has 145 lines, so I could not match that anchor (perhaps another file); I fixed the orphan "and" at line 12 only.
- The handoff for M3 says "step 4 of `way_of_working.md`" and the finding says step 4.3: both agree with the file (item 3 under "## 4. Ask, show, write"); I wrote "step 4".
- The short *Rationale* sentence in WAY-11 (M5) goes slightly beyond the ruling; named above.

## Choices

- M1: dropped the base side rather than `git grep`: removes the read, adds no new call. Cost if wrong: none seen; a citing file the change removed is reported by the report of an uncited invariant.
- M10: the pair of examples written for WAY-17 says what holds and what breaks in the chain; the alternative, an invariant, would have cited a test of nothing that exists.

## Unread material

none (the reviewer's full report `whole-review-report.md` was not read: the findings file was enough).

## Searches not found or unclear

- `product-guidelines/template.md:353` of M11 (file has 145 lines).

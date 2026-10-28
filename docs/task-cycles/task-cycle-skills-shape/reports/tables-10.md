## (a) Judgment table

Lines are of `task-cycle/review/SKILL.md` at `cf11541` (the slice's base `00d000e` holds the same
file). Ground: no session records were searched (plan, *Common*, point 2); each ground is the
decision or the step of the cycle the fragment carries.

| # | Fragment | When an agent needs it / does it recognise that moment (WAY-257) | Verdict | Reason | Ground |
|---|---|---|---|---|---|
| 1 | `:1-4` frontmatter, the description | every use — the entry points `the-way-review-change` are generated from it; in the cycle the handoff names the method / no moment to recognise | keep | the trigger and the source of the entry points; the plan keeps it unchanged | step: WAY-127 |
| 2 | `:6-13` "Reviews one range of commits…" — the picture of the whole, listing the six reviews | every use / no moment | keep | the picture of the whole stays in `SKILL.md` | WAY-256, WAY-162 |
| 3 | `:15-16` where the-way lies | every use (the whole-change reviewer reaches `elements/common/` and `product-guidelines/`; every reviewer reaches the foundation) / no moment | keep | common | WAY-127 |
| 4 | `:18-22` heading `## 1. Read`; "The dispatch: what is reviewed … the base and head commits of the range, and the report path." | every use / no moment — it is what tells the reviewer its variant | keep | common | WAY-148 |
| 5 | `:22-23` "The return step's commits are reviewed as section 2 gives, against the task and the foundation entries the return step writes or corrects." | only the reviewer of the return step's commits / yes — the dispatch names them | keep (one-instruction exception) | one instruction of one variant, in the bullet that names the variant, where its pointer would stand; moved out, a pointer would replace it | WAY-256 (exception); step 11, `task-cycle/skill/SKILL.md:362-364` |
| 6 | `:24-29` "For the review of the whole change: the frozen task document whole, … the slice reviews the dispatch lists." | only the reviewer of the whole change / yes — the dispatch says the whole change | move → `whole_change.md` (`## Read`), pointer in its place (`SKILL.md:24-25` after) | one variant's reading; it goes with row 29 behind one pointer that stands where it stood, so the reviewer reads it at the same step | WAY-158, WAY-164, WAY-136; step 9, `task-cycle/skill/SKILL.md:332-339` |
| 7 | `:29-32` "You alone among the reviewers select your own foundation and guidelines: … by "Reading the foundation" in `elements/common/way_of_working.md`, … by `product-guidelines/reading.md`, each … whole (WAY-150, WAY-213)." | only the reviewer of the whole change / yes — as row 6 | keep, after the pointer of row 6 | it names two files outside the skill; in `whole_change.md` they would be a second level of reference (plan, *Common*, point 5, one level deep; base `instruction-files/SKILL.md`, "Ways in and routes", fact `claude-skill-nested-references`); kept in `SKILL.md`, the files stay named by the step that needs them (WAY-125 as changed) | WAY-150, WAY-213; `task-cycle/skill/SKILL.md:156-157` |
| 8 | `:33-39` "For any other review — … what the dispatch names, as the orchestrator selected it …"; "A slice's reviewer gets the selection its executor got and judges the slice against the passages of the task the dispatch gives, not the plan alone." | five of the six variants (every one but the whole change); the slice's sentence only the slice reviewer / yes — the dispatch names the review | keep | common to five variants, not one; the slice's sentence is one instruction of one variant inside a common bullet (exception) | WAY-150, WAY-213, WAY-148; `task-cycle/skill/SKILL.md:144-148`; WAY-256 (exception) |
| 9 | `:40-41` the author's report, claims to verify | every use / no moment | keep | common | WAY-164, WAY-148 |
| 10 | `:42-44` "For the review of a fix, the findings file … and the fix report. For the review of a correction made for the human's remarks on the request, those remarks and the correction report." | only the reviewer of a fix or of a correction / yes — the dispatch gives the findings file or the remarks | move → `fix.md` (`## Read`), pointer in its place (`SKILL.md:38-39` after) | the reading of two variants that share section 4; with row 27–28 the variants hold several instructions against one pointer | WAY-161, WAY-162; `task-cycle/skill/SKILL.md:134-136`, `:456-458` |
| 11 | `:45-48` the diff computed yourself; never `HEAD~1`; confirm `HEAD`; on a mismatch, a question "of section 6" | every use / yes — the mismatch shows at once | keep; "section 6" reworded "section 4" | common; the report's section is renumbered when sections 4 and 5 leave (no change of meaning) | WAY-158; step of the activity |
| 12 | `:50-55` reach beyond the dispatch, named in the report (with its clause on the whole change) | every use, when something is missing / yes — the gap shows during the work | keep | common; the whole-change clause is part of one sentence | WAY-150, WAY-213 |
| 13 | `:57-58` a dispatch's grade or scope does not bind | every use / no moment | keep | common | WAY-161; `task-cycle/skill/SKILL.md:371-373` |
| 14 | `:60-63` heading `## 2. Review`; begin at the reach; the claim most likely false | every use / no moment | keep | common | step of the activity |
| 15 | `:64-67` against the task; silence is not permission | every use / no moment | keep | common | step of the activity |
| 16 | `:68-70` against the foundation; a changed invariant test named | every use / no moment | keep | common | WAY-11, WAY-150 |
| 17 | `:71-72` the tests; a test that asserts nothing | every use / no moment | keep | common | step of the activity |
| 18 | `:73-75` hostile input at a trust boundary; an operation that cannot be undone only prepared | where the dispatch or the part map names one — the occasion of a slice review, and any other review whose change touches one / yes — the dispatch or the part map names it | keep | a condition on the change's content, not a variant; two conditions of one instruction each, so moved out each would leave a pointer of the same condition (exception) | WAY-256 (exception); step 9, sub-step 5 |
| 19 | `:76-77` the author's own-work check | every use / no moment | keep | common | WAY-164 |
| 20 | `:78-79` a user interface: the styleguide's states and the screenshot evidence | only a change with a user interface / yes — the diff shows the screen | keep (one-instruction exception) | one instruction under one condition; a pointer would replace it | WAY-219; WAY-256 (exception) |
| 21 | `:80-83` the checks that tell the change from a broken one; a separate worktree; not the full suite; unverified | every use / no moment | keep | common | WAY-160, WAY-159 |
| 22 | `:84-86` a long command in the background | every use, when a command may run long / yes | keep | common | WAY-255 |
| 23 | `:87` the whole review yourself; no subagent | every use / no moment | keep | common | step of the activity |
| 24 | `:89-95` heading `## 3. Grade`; Critical, Important, Minor | every use / no moment | keep | common | WAY-161 |
| 25 | `:97-100` appearance by its effect; a guideline example; a mandated defect | every use (the first two when a finding concerns appearance or an example) / yes — the finding shows it | keep | common to every review that grades; `implement-task` names `review-change` as the holder of these criteria | WAY-220, WAY-221; `task-cycle/skill/SKILL.md:369-371` |
| 26 | `:102-107` what blocks; **Declined to judge**; out of scope; what each finding carries | every use / no moment | keep | common | WAY-161 |
| 27 | `:109-116` heading `## 4. Review of a fix`; the findings file bounds the review; fixed or remains; contested; what the fix broke; outside the fix diff | only the reviewer of a fix / yes — as row 10 | move → `fix.md` (`## Review of a fix`) | one variant's procedure of several instructions | WAY-161, WAY-162; `task-cycle/skill/SKILL.md:380-388` |
| 28 | `:118-119` "For a correction made for the human's remarks, the remarks take the findings file's place: …" | only the reviewer of a correction / yes — the dispatch gives the remarks | move → `fix.md`, under row 27 as at the base | it substitutes into row 27 ("the findings file's place"), so it stays beside it; separated, its meaning would lean on a text the correction reviewer no longer reads | WAY-162; `task-cycle/skill/SKILL.md:456-458` |
| 29 | `:121-131` heading `## 5. Review of the whole change` and its paragraph | only the reviewer of the whole change / yes — as row 6 | move → `whole_change.md` (`## Review of the whole change`) | one variant's procedure of several instructions | WAY-136, WAY-158, WAY-161, WAY-164; step 9, `task-cycle/skill/SKILL.md:332-343` |
| 30 | `:133-137` heading `## 6. Report`; the first line; `FAIL` | every use / no moment | keep; heading renumbered `## 4. Report` | common | WAY-148, WAY-158 |
| 31 | `:139-141` findings by grade, "and in the review of the whole change of a plan, each blocking finding with the slice it comes from, or none" | the bullet every use; its clause only the whole change of a plan / yes — at the report step, beside the item it qualifies | keep (one-instruction exception for the clause) | the clause is one instruction needed at the report step; in `whole_change.md`, read at step 1, it would need a pointer at the report step to be met when the report is written — one instruction against one pointer; and it would split a sentence | WAY-136, WAY-158; WAY-256 (exception) |
| 32 | `:142-143` "for the review of a fix, each finding … as fixed or remains, and kept or withdrawn where contested; for a correction, each remark as made or not;" | only the reviewers of a fix and of a correction / yes — at the report step | keep (one-instruction exception) | one instruction per variant, needed at the report step; as row 31 | WAY-161, WAY-162; WAY-256 (exception) |
| 33 | `:144-147` **Declined to judge**; checks with command and exit code; reaches | every use / no moment | keep | common | WAY-161, WAY-159, WAY-150 |
| 34 | `:149-153` the short return; `questions` | every use / no moment | keep | common; see (e) | WAY-148 |

Added by the rebuild (rewordings of *Common*, point 4 — pointers and file headers, no rule):

- `SKILL.md:24-25`, step 1: "For the review of the whole change, read `whole_change.md` and
  follow it: what you read and what you check besides section 2." — in place of the base `:24-29`;
  its condition names the moment as the reviewer meets it, the dispatch's "the whole change".
- `SKILL.md:38-39`, step 1: "For the review of a fix, or of a correction made for the human's
  remarks on the request, read `fix.md` and follow it: what you read and what bounds the review." —
  in place of the base `:42-44`.
- `SKILL.md:43`, "as a question of section 4" for "of section 6", and `SKILL.md:104`, `## 4. Report`
  for `## 6. Report`: the renumbering after sections 4 and 5 leave.
- `whole_change.md:1-3` and `fix.md:1-4`, title and purpose, in the form Slices 7–9 gave the files
  beside a skill.

Layout after the rebuild (one level deep; neither file beside the skill points to another file):

```
task-cycle/review/
  SKILL.md          picture of the whole; 1. Read (common; the return step's sentence, row 5;
                    the pointer to whole_change.md and the whole-change reviewer's own selection,
                    rows 6–7; the pointer to fix.md, row 10); 2. Review; 3. Grade; 4. Report
                    (unchanged items, rows 31–32)
  whole_change.md   Read (the whole-change reading list); Review of the whole change (base section 5)
  fix.md            Read (findings file and fix report; remarks and correction report);
                    Review of a fix (base section 4, the correction's paragraph included)
```

**Form: a pointer at step 1, not a table of variants.** Of six variants, two need a file, one (the
return step) has one instruction, the slice's one instruction stands inside a common bullet, and
the reconciliation has nothing of its own. Step 1 already listed the readings per variant as
bullets, so each pointer takes the place of the reading it moves, as Slice 9 did. A table, as
Slice 7 measured, would add about 150 words to `SKILL.md`, a row for each of the four variants that
need nothing — about as much as the fix variant's whole file. Pointers at each step (Slice 8's
form) would give each file two pointers, at step 1 for its reading and at section 4 or 5 for its
procedure. Way rejected: a table like `make-change`'s. Cost if wrong: one more pointer style among
the five skills; the change to a table is mechanical.

## (b) "Remove" and "reword" proposals (no edit)

None. No fragment meets a condition of "When to remove a rule" (`judging.md`) on the text alone:
each carries a decision or a step of the cycle, and no session records were searched (plan,
*Common*, point 2). The contradiction of (e) is an observation for the orchestrator, not a
proposal: settling it changes the content of a rule in one of two skills.

## (c) Words read before and after

Commands (in the worktree, after the commit):

```
git show cf11541:task-cycle/review/SKILL.md | wc -w                            -> 1860
wc -w task-cycle/review/*.md  -> 220 fix.md, 1478 SKILL.md, 273 whole_change.md
cat task-cycle/review/SKILL.md task-cycle/review/whole_change.md | wc -w      -> 1751
cat task-cycle/review/SKILL.md task-cycle/review/fix.md | wc -w               -> 1698
```

| Agent | Variant | Reads | Before | After | Change |
|---|---|---|---|---|---|
| reviewer | a slice | `SKILL.md` | 1860 | 1478 | −382 (−21%) |
| reviewer | the whole change | `SKILL.md`, `whole_change.md` | 1860 | 1751 | −109 (−6%) |
| reviewer | the fix of a review's findings | `SKILL.md`, `fix.md` | 1860 | 1698 | −162 (−9%) |
| reviewer | the return step's commits | `SKILL.md` | 1860 | 1478 | −382 (−21%) |
| reviewer | the reconciliation with the target branch | `SKILL.md` | 1860 | 1478 | −382 (−21%) |
| reviewer | a correction made for the human's remarks | `SKILL.md`, `fix.md` | 1860 | 1698 | −162 (−9%) |

A reviewer resumed for the review of the fix of its own findings (`task-cycle/skill/SKILL.md:387`,
"The same reviewer") already holds what it read for the first review; resumed after the whole
change it reads `fix.md` besides, 1971 words in all against 1860 before (+111). A fresh reviewer of
a fix reads 1698.


## 7a. Table of judgment (22 rows of the example, confirmed or corrected)

Criterion in every row: when an agent needs the fragment and whether it recognises the moment (WAY-257). Lines are at the base (`cf11541`). Session records were not searched; ground is the decision or step the fragment carries.

| # | Fragment (`file:line`) | Needed when / recognised? | Verdict | Reason | Ground |
|---|---|---|---|---|---|
| 1 | `SKILL.md:1-4` frontmatter | every use / no moment | keep (unchanged) | description is the trigger and the source of the entry points | WAY-127 |
| 2 | `:6-12` picture of the whole | every use / no moment | keep | picture of the whole stays | WAY-256 |
| 3 | `:14-15` where the-way lies | every use / no moment | keep | common | WAY-127 |
| 4 | `:19-22` "Read what your dispatch names", the dispatch | every use / no moment | keep; the table of variants goes before it | common to the variants | WAY-150 |
| 5 | `:23-24` (example: 23-25) one author: whole task and spec | only the one author / yes, dispatch says "the change" | keep, as the one-author row of the table | one instruction against one pointer (exception of WAY-256): the sentence stands where a pointer would; the sentence is word for word | step 9 of `task-cycle/skill/SKILL.md:280` |
| 6 | `:24-28` slice: section of the plan, passages, task binds | only the slice / yes, dispatch gives the number | move -> `slice.md` | several sentences for one variant | WAY-148, WAY-229 |
| 7 | `:29-31` foundation entries and guidelines | every use / no moment | keep | common | WAY-213 |
| 8 | `:32-33` fix: findings file, Minor not yours | only the fix / yes, dispatch gives the file | move -> `fix.md` | one variant, two sentences | WAY-161 |
| 9 | `:34` correction: remarks bind | only the correction / yes | keep, as the correction row of the table | one instruction; reading and report of the correction stand together in the row | step 'Correction after review', `task-cycle/skill/SKILL.md:450-464` |
| 10 | `:35-36` retry of a slice | only a retried slice / yes, dispatch gives the failed report | move -> `slice.md` | variant of the slice variant | step 9 sub-step 4, `task-cycle/skill/SKILL.md:315` |
| 11 | `:37` each changed file whole | every use / no moment | keep | common | step of the activity |
| 12 | `:39-45` reaching beyond the dispatch | every use, when something is missing / yes | keep | common; the clause "(section 6)" keeps its number | WAY-213, WAY-150 |
| 13 | `:47-50` value that does not pass; exploratory edit | every use / yes | keep | common | step of the activity |
| 14 | `:52-80` section 2, tests | every change with code / yes | keep | all variants; the exception for prose is in the section | WAY-253 and steps of the activity |
| 15 | `:84-86` own-work check (inset "for a slice, of your slice read against the passages of the task your dispatch gives", 4 words in the middle of a sentence) | every use / no moment | keep, the inset stays in place | **departure from the example's layout line** ("slice.md holds the insets of sections 3 and 5"): the inset is one instruction and a pointer would be longer than it (exception of WAY-256, Foundation entries row 3); moving it would also cut a sentence in the middle. The example's own table row says keep | WAY-164 |
| 16 | `:87-91` UI states and screenshot | only when the change alters a screen / yes, the agent knows it changes a screen | move -> `ui_check.md`; pointer "Before you finish a change that alters what a screen shows, read `ui_check.md`." | one kind of change; five sentences | WAY-219 |
| 17 | `:92-97` focused checks, long commands in the background | every use / no moment | keep | common | WAY-160, WAY-255 |
| 18 | `:99-105` section 4, plan and code | only the slice (the one author has no plan) / yes | move -> `slice.md`; heading and number stay in `SKILL.md` with one pointer sentence | one variant; the number stays because sections 5 and 6 cite "section 4" | step of the cycle, `task-cycle/skill/SKILL.md:280-300` |
| 19 | `:107-120` section 5, return without code (inset "for a slice, one you searched the task and spec for, as section 1 gives, and found unsettled", `:112-114`; and "for a slice's retry, to reset", `:120`) | every use / yes, the moment is a choice the task does not settle | keep, the insets stay in place | **departure from the example** (it moves the inset of `:112-114`): the inset is a clause in the middle of the first bullet; a pointer would be longer, and moving it means rewriting the bullet around a gap, which I cannot show to keep its meaning. Doubt named in point 7e/doubts below | WAY-135, WAY-136 |
| 20 | `:122-138`, `:141-150` commit and report | every use / no moment | keep | common | WAY-148 |
| 21 | `:139-140` (example: `:139`) first half "for a fix, each blocking finding as fixed ... or contested, with the evidence" | only the fix / yes | move -> `fix.md`, section Report | the example's rows 21 and 22 split by line, but the base bullet is one bullet over lines 139-140; I split it at the semicolon | WAY-161 |
| 22 | `:140` (second half) "for a correction, each remark as made, and how" | only the correction / yes | keep, in the correction row of the table | one instruction | step 'Correction after review' |

Doubts in the table (kept as the text stood where unsure): rows 15 and 19, above. Row 9/22 text: the row holds "For a correction, the human's remarks on the request; each remark binds. For a correction, the report holds each remark as made, and how." The second sentence is the base clause reworded to stand alone (no change of meaning).

## 7b. Proposals of "remove" and "reword" (no edit made)

None. No remove or reword that changes the content of a rule was found. No session records were searched, so none rests on "When to remove a rule" conditions.

## 7c. Words read per variant, before and after

Commands (run in `task-cycle/change/`):

- before: `git show cf11541:task-cycle/change/SKILL.md | wc -w` -> 1777
- after: `wc -w SKILL.md slice.md fix.md ui_check.md` -> SKILL.md 1619, slice.md 201, fix.md 77, ui_check.md 90

| Variant | Before | After | Difference |
|---|---|---|---|
| one author | 1777 | 1619 | -158 |
| slice (retry too) | 1777 | 1619 + 201 = 1820 | +43 |
| fix | 1777 | 1619 + 77 = 1696 | -81 |
| correction | 1777 | 1619 | -158 |
| any variant that alters a screen | as above | + 90 | |

The slice variant reads more words than before, and the example's estimates (about 1450 / 1650 / 1500) are not reached. Reasons: the table of variants adds about 150 words in `SKILL.md` for every agent (the two kept rows, the pointer rows with their content notes, the lead sentence), the slice file adds a heading and a short intro, and the two insets of rows 15 and 19 stay in place. The saving the example promised depended partly on moving the insets and on thinner pointer rows. The pointer rows describe what the file holds (WAY-257: the agent must recognise the moment), which is what costs the words. If the orchestrator prefers a thinner table, the content notes of the `slice.md` and `fix.md` rows can be cut to the path and a condition, saving about 40 words per agent. I did not do it: I judged recognition worth more than the words and name it as a choice.


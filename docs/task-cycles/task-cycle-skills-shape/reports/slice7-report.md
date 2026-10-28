# Slice 7 report

**Status:** done with concerns (the rebuild saves no words for the slice variant; see point 7c)

**Commit:** 9b776fe on `task/task-cycle-skills-shape` (not pushed). Worktree clean.

**Files changed** (all in `task-cycle/change/`): `SKILL.md` (+22 / -34 lines incl. frontmatter untouched), new `slice.md`, `fix.md`, `ui_check.md`. Method read whole from `.runs/the-way-base/task-cycle/change/SKILL.md` (identical to `cf11541` and to the worktree file); judged with the base copy's `maintain-instruction-files` (`SKILL.md`, `judging.md`, `kind_skill.md`, `tool_loading.md`).

## Layout made

- `SKILL.md`: frontmatter, picture of the whole, then step 1 opens with a table of four variants. Rows: one author (the base sentence, in place), slice or retry (pointer to `slice.md`), fix (pointer to `fix.md`), correction (the base sentence of reading plus a sentence for the report). Then the common reading, tests, own-work check (pointer to `ui_check.md` in place of the UI bullet), section 4 reduced to a one-line pointer so that the numbers "section 4/5/6" stay valid, return without code, commit and report.
- `slice.md`: the slice reading, the retry reading, "When the plan and the code disagree".
- `fix.md`: the findings reading, and the report of a fix.
- `ui_check.md`: the UI bullet word for word.
- No file beside the skill points to another file or back to `SKILL.md`.

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

## 7d. Sentence comparison

Commands: `git show cf11541:task-cycle/change/SKILL.md | tr -d '\r' | tr '\n' ' ' | tr -s ' ' | sed 's/\([.!?]\) /\1\n/g' | sort > slice7-before.txt`; the same over `cat task-cycle/change/*.md` into `slice7-after.txt`; `comm -3` output kept in `reports/slice7-comm.txt`. Every printed line is a heading or list marker or table frame merged with a neighbouring sentence by the pipeline, or a reworded pointer row. Accounted, in the output's order (before-only lines have no leading tab):

1. "- As the one author ... you make the whole change." (before) / "| You make | Read | |---|---| | the whole change as the one author | As the one author ... you make the whole change." (after): the same sentence, now in row 5 of the table; list marker replaced by the table frame. Row 5.
2. "- Before you finish a change that alters what a screen shows, read `ui_check.md`." (after only): the pointer of row 16.
3. "- For a correction, the human's remarks on the request; each remark binds." (before) / "| a correction ... | For a correction, the human's remarks ...; each remark binds." (after): the same sentence in the correction row. Row 9.
4. "- For a fix, the findings file ... and the code it names." (before) / "## Read - For a fix, the findings file ..." (after): the same sentence now in `fix.md` under a heading. Row 8.
5. "# Checking a changed user interface What the own-work check adds ..." , "# Fixing a review's findings What ...", "# Making a slice What ...": heading and the one-line intro of each new file, added text, no rule in them. Rows 16, 8, 6.
6. "## Read - For a slice, your section ... whole task." (after) / "For a slice, your section ... whole task." (before, leading "- " lost to the pipeline's merge): the same sentence in `slice.md`. Row 6.
7. "## Report - For a fix, the report holds each blocking finding ..." (after): the first half of the base bullet `:139-140` reworded to stand alone ("For a fix, the report holds each blocking finding as fixed ..." for "for a fix, each blocking finding as fixed ..."). No change of meaning. Row 21.
8. "## When the plan and the code disagree - A small mismatch ..." (after) / "When the plan and the code disagree - A small mismatch ..." (before): the section's first bullet, in `slice.md` with the heading at the level `##`. Row 18. The next line, "When the plan and the code disagree Where you make a slice, this section stands in `slice.md`.", is the pointer left in `SKILL.md` under the kept heading of section 4. Row 18.
9. "| | a correction ... | For a correction, the human's remarks ..." , "| | a slice, or the retry ... | `slice.md`, for how ...", "| | the fix of a review's findings | `fix.md`, for ...": rows of the table of variants (a row of the table of variants is a rewording the plan allows). Rows 9, 6, 10, 18, 8.
10. "| Read what your dispatch names; ... (WAY-150)." and "Read Read what your dispatch names ...": the base sentence merged with the table's last line and with the heading; the sentence is unchanged. Row 4.
11. "| You make | Read | ..." is item 1 above; "Read Your dispatch says which of these you make; read for it as its row gives.": the lead sentence of the table (added text). Row 4.
12. "For a correction, the report holds each remark as made, and how.": the second half of base bullet `:139-140` reworded to stand alone (no change of meaning). Row 22.
13. Two long lines "Write the full report ...": the report list, as a single line because it has no full stop. Before: includes the bullet "for a fix ... ; for a correction, each remark as made, and how;"; after: that bullet is gone, moved by rows 21 and 22. Every other bullet of the list is unchanged.

Nothing printed is left unaccounted; no rule sentence was dropped.

## 7e. Contradictions with `task-cycle/skill/SKILL.md`

Read: `:68`, `:128-196`, `:259-364`, `:366-398`, `:450-464` (dispatch places `:280`, `:289`, `:293`, `:350`, `:381`, `:456`).

- Found one, expected: `:67-69` (step 3) says "Each stage agent reads the method of its stage, and what it names, whole". After this rebuild a file beside the skill is read at its variant, not whole at the start; WAY-125 as changed says so. The change belongs to the `implement-task` slice (task, To do 1), not this one. Not touched.
- Not a contradiction but to note: step 9 also dispatches `make-change` for the foundation entries of the plan and for the return step (`:289`, `:350`). Neither is one of the four variants of the table; they work under section 1's foundation-entry sentence ("Where you write a foundation entry through an element's skill ...") and the common part. The table says "Your dispatch says which of these you make"; a dispatch for foundation entries names none of the four rows. The base text has the same gap (its first bullet lists the same four). Unchanged.
- Otherwise none found: statuses at `:175`, the findings file for a fix (`:381-385`), the retry (`:315`) and the correction (`:450-464`) match the variants.

## Checks (command and exit code)

- `grep -n 'slice.md\|fix.md\|ui_check.md' task-cycle/change/SKILL.md`: exit 0; lines 24, 25 (table rows), 85 (section 3, UI), 95 (section 4 pointer). Each file named at the step or variant that needs it.
- `ls task-cycle/change/`: `SKILL.md fix.md slice.md ui_check.md`, exactly the files named.
- `git diff cf11541 -- task-cycle/change/SKILL.md`: first hunk starts at line 16, so lines 1-4 unchanged.
- `python -B agent-instructions/skill_entry_points.py`: "entry points are current", exit 0.
- `grep -rn -E "Storage|The Brain|_zadania|Notes/" task-cycle/change/`: printed nothing, exit 1 (no match).
- `python -B gate/run_tests.py task-cycle` (output in `reports/slice7-gate-task-cycle.log`): 41 tests, OK, exit 0.
- `git diff --check`: nothing, exit 0.
- Not run: whole `gate/run_tests.py` (the orchestrator's). No tests were written or changed (no code in this slice).

## Own-work check

Requirement most likely missed: "every sentence of the base stands, word for word, in `SKILL.md` or a file beside it". Check: the sentence comparison above, every line accounted. It showed only merges of headings and markers, the pointer sentences, two rewordings that change no meaning (rows 21, 22), and the removed report bullet whose halves moved.

## Choices, with the way rejected and its cost if wrong

- Insets of rows 15 and 19 kept in place (departure from the example's layout line). Rejected: move to `slice.md` as the example's layout says. Cost if wrong: about 30 more words saved for the slice variant if the orchestrator wants the moved version; the cost of mine is that one more mention of "a slice" stays in common text.
- Section 4 kept as a heading with a pointer sentence. Rejected: delete the section and renumber. Cost: one stub sentence for every agent; renumbering would have changed the citations "section 4/5/6" in the text.
- Pointer rows describe their file's content. Rejected: path and condition only. See 7c.
- `slice.md`, `fix.md`, `ui_check.md` each begin with a heading and a one-line intro naming the use of the file; names are the example's.

## Reaches beyond the dispatch

None. The task's To do 7 and the foundation entries were read from the handoff; no foundation file was opened beyond the Read.

## Problems observed

The example's rows 5/6 overlap (`:23-25` vs `:24-28`) and its rows 21/22 split one bullet by lines (`:139`, `:140`); corrected in the table above. Cause not investigated.

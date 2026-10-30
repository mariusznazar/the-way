## Blocking findings

### 1. The word counts leave out one file section the base has read twice (Important)

**Anchor:** `.runs/task-cycles/styleguide-skill-shape/reports/word-counts.md:7` (and every route list and the summary, `:18-24`); the read it misses is base `product-guidelines/styleguide/SKILL.md:93` and `project-level/task/skill/read_sources.md:5`.

**To paste:** The section "Reading the foundation" of `elements/common/way_of_working.md` (492 words) is read by `refine-task` and again at the base's step 0, yet it is in no route's list, so every "before" figure is 984 too low and every "after" figure 492 too low. The rule of the count says that a file read twice counts twice.

**Why I report it:** To do 4 and task question 3 make the second reading of a file the very thing the figures must show ("plik czytany dwa razy w stanie „przed” liczy się dwa razy"), and the orchestrator's rule says every read counts, refine-task's first reading of a file the skill makes the session read again included.

The mechanism: base line 93 reads "Select and read the product's foundation by "Reading the foundation" in `elements/common/way_of_working.md`", the same section `read_sources.md:5` has the session read at refine-task's step 1. That makes four things step 0 reads again, not the three `word-counts.md:7` lists (`tools/word_counts.py:66` holds only those three). The stated exclusion of "the entries of its foundation" (`word-counts.md:12`) covers the product's entries, not this section, which is the-way's own method text and has the same size in every product. No line of the file says it was left out on purpose.

The effect is on the figure the human reads as the gain: the second reading disappears in the rebuild, so the saving is understated by 492 words on all seven routes; on route 2, "without first reads" before is 9334 / 9843, not 8842 / 9351. The first reads become 2835 words, not 2343.

Figures with the section counted, recomputed by `recheck.py` from the same file sizes (the after figures without first reads do not change):

| Route | Before: to step 4 / total | After: to step 4 / total | Before without first reads | After without first reads |
|---|---|---|---|---|
| 1 | 12678 / 12678 | 7281 / 9663 | 9843 / 9843 | 4446 / 6828 |
| 2 | 12169 / 12678 | 6239 / 9452 | 9334 / 9843 | 3404 / 6617 |
| 3 | 12678 / 12678 | 7518 / 9900 | 9843 / 9843 | 4683 / 7065 |
| 4 | 12169 / 12678 | 6239 / 9452 | 9334 / 9843 | 3404 / 6617 |
| 5 | 12678 / 12678 | 7518 / 9900 | 9843 / 9843 | 4683 / 7065 |
| 6 | 12678 / 12678 | 7385 / 9767 | 9843 / 9843 | 4550 / 6932 |
| 7 | 12169 / 12169 | 4077 / 4077 | 9334 / 9334 | 1242 / 1242 |

The task's own estimate of about 8850 (2830 + about 6000) did not include this section, so `word-counts.md` should say that this is why its "before" figure now stands about 490 above the estimate.

Fix: add the section to `FIRST_READS` and `STEP0` in `tools/word_counts.py`, regenerate, and correct the sentence on "three files" and the author's figures. No file of the commits changes.

### 2. `recognize.md` has the session read again the guidelines `refine-task` already read (Important)

**Anchor:** `product-guidelines/styleguide/recognize.md:10`; against `project-level/task/skill/read_sources.md:28` and `product-guidelines/reading.md:40`; the sentence that should cover it is `product-guidelines/styleguide/SKILL.md:65-69`.

**To paste:** To do 2 says what the session read at refine-task's steps 1 and 2 is not read a second time. `recognize.md:10` still reads "every file under `guidelines/`", which includes the files of the task's parts that refine-task step 1 read whole. On a refresh or an extension that is the styleguide itself.

**Why I report it:** To do 2 has two halves: each file is read at the step that needs it, and "to, co sesja przeczytała już w krokach 1 i 2 `refine-task`, nie jest czytane drugi raz". The second half holds for the three files and the foundation and is missed here.

The mechanism: `read_sources.md:28` reads the product's guidelines of the parts the task touches, and `reading.md:40` reads whole every file whose *Applies to* names such a part. For a task about the styleguide of part `web`, that is `guidelines/styleguide-web.md` and any other file naming `web`. Then `recognize.md:10` says "Read the product's root `AGENTS.md` and every file under `guidelines/`", with no exception. The sentence right after it in the same bullet makes exactly the exception for the foundation ("besides what `refine-task` selected at its step 1"), so the file treats two reads of the same kind differently. `SKILL.md:65-69` lists what is not read again and does not list the guidelines.

The route this costs most is 4 and 5: an agent reads the accepted styleguide twice before step 2. The cost is the product's words, so it stays out of the word counts by the orchestrator's rule, and that is why nothing showed it. The author's assessment row for line 92 does not mention it; proposal P1 notes the repetition and bundles it with narrowing the reading, which is a different change.

This is not P1. The set of files the session has read after step 1 stays the same, so the rule's meaning stays the same, and the frozen task accepts it as a meaning-preserving reword.

Fix: at `recognize.md:10`, "Read the product's root `AGENTS.md` and every file under `guidelines/` that `refine-task` did not read at its step 1." Add the row's note to `assessment.md` (row `:92-92`).

# Word counts of the seven routes

Method. Words are whitespace-separated, Markdown and frontmatter included; of a file read by sections, the sections read. Figures are from the worktree (after) and from commit 525cde1 for the base `SKILL.md` (before).

Rules of the count:

- Every read of the route counts, in both states. The first reads of refine-task are the first reading of the files that the base skill's step 0 makes the session read again: `project-level/task/skill/SKILL.md`, `project-level/task/template.md` and the sections "How a skill asks" and "Reading the foundation" of `elements/common/way_of_working.md` (2835 words together). They count in both states; in the before state the second reading counts again (a file read twice counts twice, task question 3); in the after state the second reading is gone. The last column of the summary leaves the first reads out, for comparison with the task's estimate (about 8850 before and 5900 after, which counted `SKILL.md` and the files of step 0 only, and not the section "Reading the foundation" of `way_of_working.md` that step 0 reads a second time: this is why the before figure stands about 490 words above the estimate).
- Other files refine-task reads (`read_sources.md`, `draft.md`, `product-guidelines/reading.md` and so on) are the same in both states and are left out; this is the cycle's rule: the files refine-task sends the session to are equal in both states and stay out of the counts. Where the session started on route 6, refine-task's own `orchestrated_mode.md` and `project_plan_task.md` are likewise equal in both states and left out.
- A file a counted file sends the session to on the route counts in both states: the files beside `elements/common/critique/SKILL.md` (`prepare.md`, `check.md`, `settle.md`), read once on the route by the author who runs and settles the critique, at the first critique (step 2 where research ran, else step 4); a later critique of the same session does not read them again. The critic's own reading is another agent's context and is not counted.
- "Before step 4" is the text read before step 4 begins; "total" is the sum at the end of the run. In the before state step 0 reads everything at the start, also on route 7, where the run ends at step 1.
- Route 3 is counted with a human without a preference, so research and audit both run. Route 5 is an extension with changed screens, so research and audit both run; its figures equal route 3.
- The product's own files (its root `AGENTS.md`, `guidelines/`) and the entries of its foundation differ by product and are left out of both states. Conditional files read only on a condition the routes do not name — `new_tools.md` (a new tool left as a technology question) and `staged_cleaning.md` (the human chooses to clean the screens as tasks touch their styles) — are not read on any route here; their words come on top where the condition holds.

## Summary

| Route | Before: to step 4 | Before: total | After: to step 4 | After: total | Before without first reads (to 4 / total) | After without first reads (to 4 / total) |
|---|---|---|---|---|---|---|
| 1. First styleguide, no screens, human without a preference | 12678 | 12678 | 7290 | 9672 | 9843 / 9843 | 4455 / 6837 |
| 2. First styleguide, no screens, human with a preference | 12169 | 12678 | 6248 | 9461 | 9334 / 9843 | 3413 / 6626 |
| 3. First styleguide, there are screens | 12678 | 12678 | 7527 | 9909 | 9843 / 9843 | 4692 / 7074 |
| 4. Refresh, screens unchanged | 12169 | 12678 | 6248 | 9461 | 9334 / 9843 | 3413 / 6626 |
| 5. Extension, screens changed | 12678 | 12678 | 7527 | 9909 | 9843 / 9843 | 4692 / 7074 |
| 6. Orchestrated mode on route 1 | 12678 | 12678 | 7394 | 9776 | 9843 / 9843 | 4559 / 6941 |
| 7. Product without a user interface, ends at step 1 | 12169 | 12169 | 4086 | 4086 | 9334 / 9334 | 1251 / 1251 |

## 1. First styleguide, no screens, human without a preference

Route: research runs, no audit.

### Before

Read before step 4 (files in the order read), 12678 words:

  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/styleguide/SKILL.md: 2830
  - product-guidelines/styleguide/template.md: 1957
  - product-guidelines/template.md: 1336
  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Read from step 4 to the end: nothing beyond the files above.

Total at the end of the run: 12678 words. Without the first reads of refine-task (2835 words): before step 4 9843, total 9843.

### After

Read before step 4 (files in the order read), 7290 words:

  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/styleguide/SKILL.md: 906
  - product-guidelines/styleguide/recognize.md: 345
  - product-guidelines/styleguide/template.md: 1957
  - product-guidelines/styleguide/starting_rules.md: 205
  - product-guidelines/styleguide/research.md: 211
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Read from step 4 to the end, 2382 words:

  - product-guidelines/template.md: 1336
  - product-guidelines/styleguide/settle.md: 576
  - product-guidelines/styleguide/task_document.md: 343
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - product-guidelines/styleguide/hand_back.md: 73

Total at the end of the run: 9672 words. Without the first reads of refine-task (2835 words): before step 4 4455, total 6837.

## 2. First styleguide, no screens, human with a preference

Route: no research, no audit.

### Before

Read before step 4 (files in the order read), 12169 words:

  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/styleguide/SKILL.md: 2830
  - product-guidelines/styleguide/template.md: 1957
  - product-guidelines/template.md: 1336
  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - elements/common/critique/SKILL.md: 322

Read from step 4 to the end, 509 words:

  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Total at the end of the run: 12678 words. Without the first reads of refine-task (2835 words): before step 4 9334, total 9843.

### After

Read before step 4 (files in the order read), 6248 words:

  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/styleguide/SKILL.md: 906
  - product-guidelines/styleguide/recognize.md: 345
  - product-guidelines/styleguide/template.md: 1957
  - product-guidelines/styleguide/starting_rules.md: 205

Read from step 4 to the end, 3213 words:

  - product-guidelines/template.md: 1336
  - product-guidelines/styleguide/settle.md: 576
  - product-guidelines/styleguide/task_document.md: 343
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70
  - product-guidelines/styleguide/hand_back.md: 73

Total at the end of the run: 9461 words. Without the first reads of refine-task (2835 words): before step 4 3413, total 6626.

## 3. First styleguide, there are screens

Route: counted with a human without a preference, so research and audit both run.

### Before

Read before step 4 (files in the order read), 12678 words:

  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/styleguide/SKILL.md: 2830
  - product-guidelines/styleguide/template.md: 1957
  - product-guidelines/template.md: 1336
  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Read from step 4 to the end: nothing beyond the files above.

Total at the end of the run: 12678 words. Without the first reads of refine-task (2835 words): before step 4 9843, total 9843.

### After

Read before step 4 (files in the order read), 7527 words:

  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/styleguide/SKILL.md: 906
  - product-guidelines/styleguide/recognize.md: 345
  - product-guidelines/styleguide/template.md: 1957
  - product-guidelines/styleguide/starting_rules.md: 205
  - product-guidelines/styleguide/research.md: 211
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70
  - product-guidelines/styleguide/audit.md: 237

Read from step 4 to the end, 2382 words:

  - product-guidelines/template.md: 1336
  - product-guidelines/styleguide/settle.md: 576
  - product-guidelines/styleguide/task_document.md: 343
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - product-guidelines/styleguide/hand_back.md: 73

Total at the end of the run: 9909 words. Without the first reads of refine-task (2835 words): before step 4 4692, total 7074.

## 4. Refresh, screens unchanged

Route: no research (a refresh), no audit (screens unchanged).

### Before

Read before step 4 (files in the order read), 12169 words:

  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/styleguide/SKILL.md: 2830
  - product-guidelines/styleguide/template.md: 1957
  - product-guidelines/template.md: 1336
  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - elements/common/critique/SKILL.md: 322

Read from step 4 to the end, 509 words:

  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Total at the end of the run: 12678 words. Without the first reads of refine-task (2835 words): before step 4 9334, total 9843.

### After

Read before step 4 (files in the order read), 6248 words:

  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/styleguide/SKILL.md: 906
  - product-guidelines/styleguide/recognize.md: 345
  - product-guidelines/styleguide/template.md: 1957
  - product-guidelines/styleguide/starting_rules.md: 205

Read from step 4 to the end, 3213 words:

  - product-guidelines/template.md: 1336
  - product-guidelines/styleguide/settle.md: 576
  - product-guidelines/styleguide/task_document.md: 343
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70
  - product-guidelines/styleguide/hand_back.md: 73

Total at the end of the run: 9461 words. Without the first reads of refine-task (2835 words): before step 4 3413, total 6626.

## 5. Extension, screens changed

Route: research runs (every extension), audit runs.

### Before

Read before step 4 (files in the order read), 12678 words:

  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/styleguide/SKILL.md: 2830
  - product-guidelines/styleguide/template.md: 1957
  - product-guidelines/template.md: 1336
  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Read from step 4 to the end: nothing beyond the files above.

Total at the end of the run: 12678 words. Without the first reads of refine-task (2835 words): before step 4 9843, total 9843.

### After

Read before step 4 (files in the order read), 7527 words:

  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/styleguide/SKILL.md: 906
  - product-guidelines/styleguide/recognize.md: 345
  - product-guidelines/styleguide/template.md: 1957
  - product-guidelines/styleguide/starting_rules.md: 205
  - product-guidelines/styleguide/research.md: 211
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70
  - product-guidelines/styleguide/audit.md: 237

Read from step 4 to the end, 2382 words:

  - product-guidelines/template.md: 1336
  - product-guidelines/styleguide/settle.md: 576
  - product-guidelines/styleguide/task_document.md: 343
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - product-guidelines/styleguide/hand_back.md: 73

Total at the end of the run: 9909 words. Without the first reads of refine-task (2835 words): before step 4 4692, total 7074.

## 6. Orchestrated mode on route 1

Route: route 1 with the orchestrated mode; the refiner requests research and critiques from the orchestrator, and the files it reads are counted as on route 1.

### Before

Read before step 4 (files in the order read), 12678 words:

  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/styleguide/SKILL.md: 2830
  - product-guidelines/styleguide/template.md: 1957
  - product-guidelines/template.md: 1336
  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Read from step 4 to the end: nothing beyond the files above.

Total at the end of the run: 12678 words. Without the first reads of refine-task (2835 words): before step 4 9843, total 9843.

### After

Read before step 4 (files in the order read), 7394 words:

  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/styleguide/SKILL.md: 906
  - product-guidelines/styleguide/orchestrated_mode.md: 104
  - product-guidelines/styleguide/recognize.md: 345
  - product-guidelines/styleguide/template.md: 1957
  - product-guidelines/styleguide/starting_rules.md: 205
  - product-guidelines/styleguide/research.md: 211
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Read from step 4 to the end, 2382 words:

  - product-guidelines/template.md: 1336
  - product-guidelines/styleguide/settle.md: 576
  - product-guidelines/styleguide/task_document.md: 343
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - product-guidelines/styleguide/hand_back.md: 73

Total at the end of the run: 9776 words. Without the first reads of refine-task (2835 words): before step 4 4559, total 6941.

## 7. Product without a user interface, ends at step 1

Route: nothing after step 1 is read.

### Before

Read before step 4 (files in the order read), 12169 words:

  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/styleguide/SKILL.md: 2830
  - product-guidelines/styleguide/template.md: 1957
  - product-guidelines/template.md: 1336
  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - elements/common/critique/SKILL.md: 322

Total at the end of the run: 12169 words. Without the first reads of refine-task (2835 words): before step 4 9334, total 9334.

### After

Read before step 4 (files in the order read), 4086 words:

  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/styleguide/SKILL.md: 906
  - product-guidelines/styleguide/recognize.md: 345

Total at the end of the run: 4086 words. Without the first reads of refine-task (2835 words): before step 4 1251, total 1251.

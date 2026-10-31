# Word counts of the six routes

Words are counted as `wc -w` counts them (whitespace-separated), Markdown and frontmatter included; of a file read by sections, the sections read (heading to the line before the next heading of the same or a higher level). Figures come from the worktree (state "after") and from commit 00c0a74 for `product-guidelines/testing/SKILL.md` (state "before"); every other file counted is identical in both states, except the files new beside the skill.

Rules of the count:

- The first reading in `refine-task` is the files that step 0 of the base skill makes the session read a second time: `project-level/task/skill/SKILL.md`, `project-level/task/template.md`, and the sections "How a skill asks" and "Reading the foundation" of `elements/common/way_of_working.md` (2835 words together; the task's figure of 2835 words is the same). They count in both states; in state "before" the second reading counts again (a file read twice counts twice); in state "after" it is gone.
- Other files `refine-task` reads (`read_sources.md`, `draft.md`, `product-guidelines/reading.md`, and so on) are the same in both states and stay out; where the session starts on route 6, `refine-task`'s own `orchestrated_mode.md` is equally the same in both and stays out.
- A file a counted file sends the session to on the route counts in both states: the files beside `elements/common/critique/SKILL.md` (`prepare.md`, `check.md`, `settle.md`; 509 words) are read once, at the first critique of the session (step 2 where research ran, else step 4); a later critique does not read them again. The critic's own reading is another agent's context and is not counted.
- "Before step 4" is the text read before step 4 begins; the total is the sum at the end of the run, the file of the last step included.
- The product's own files (its root `AGENTS.md`, `guidelines/`) and the entries of its foundation differ by product and stay out of both states. The conditional files `new_tools.md` (a new tool left as a technology question) are read on none of these routes, and their words come on top where the condition holds.
- In state "before", step 0 reads at the start of every run, whatever the route: both templates, the task skill and template, the two sections of the way of working and `critique/SKILL.md`.
- Route 3 counts a human without a preference (research runs); an extension also runs research and the audit, so its figures equal route 3.

## Summary

| Route | Before: to step 4 | Before: total | After: to step 4 | After: total | Before without the first reading (to step 4 / total) | After without the first reading (to step 4 / total) | Change of the total |
|---|---|---|---|---|---|---|---|
| 1. First guidelines, no tests, human without a preference | 14120 | 14120 | 8791 | 11272 | 11285 / 11285 | 5956 / 8437 | -20.2% |
| 2. First guidelines, no tests, human with a preference | 13611 | 14120 | 7728 | 11040 | 10776 / 11285 | 4893 / 8205 | -21.8% |
| 3. Tests and no guidelines, no preference; also an extension | 14120 | 14120 | 9021 | 11502 | 11285 / 11285 | 6186 / 8667 | -18.5% |
| 4. Refresh | 13611 | 14120 | 7958 | 11270 | 10776 / 11285 | 5123 / 8435 | -20.2% |
| 5. "A new level", recipe already standing, no step 2 | 13611 | 14120 | 7647 | 10959 | 10776 / 11285 | 4812 / 8124 | -22.4% |
| 6. Orchestrated mode on route 1 | 14120 | 14120 | 8889 | 11370 | 11285 / 11285 | 6054 / 8535 | -19.5% |

## 1. First guidelines, no tests, human without a preference

Reading counted: steps 0-2, 4, 5 run; step 2 runs research and the critique of its reports; no step 3 (no tests, no new level); the critique of step 4 runs.

### Before

Read before step 4 (files in the order read), 14120 words:

  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/testing/SKILL.md: 3042
  - product-guidelines/template.md: 1336
  - product-guidelines/testing/template.md: 3187
  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Total at the end of the run: 14120 words. Without the first reading in `refine-task` (2835 words): before step 4 11285, total 11285.

### After

Read before step 4 (files in the order read), 8791 words:

  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/testing/SKILL.md: 1200
  - product-guidelines/testing/recognize.md: 363
  - product-guidelines/testing/template.md: 3187
  - product-guidelines/testing/starting_set.md: 143
  - product-guidelines/testing/research.md: 232
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Read from step 4 to the end, 2481 words:

  - product-guidelines/template.md: 1336
  - product-guidelines/testing/settle.md: 654
  - product-guidelines/testing/task_document.md: 364
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - product-guidelines/testing/hand_back.md: 73

Total at the end of the run: 11272 words. Without the first reading in `refine-task` (2835 words): before step 4 5956, total 8437.

## 2. First guidelines, no tests, human with a preference

Reading counted: steps 0-2, 4, 5 run; step 2 runs no research (the human has a preference); no step 3; the critique of step 4 runs, and it is the first critique of the session.

### Before

Read before step 4 (files in the order read), 13611 words:

  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/testing/SKILL.md: 3042
  - product-guidelines/template.md: 1336
  - product-guidelines/testing/template.md: 3187
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

Total at the end of the run: 14120 words. Without the first reading in `refine-task` (2835 words): before step 4 10776, total 11285.

### After

Read before step 4 (files in the order read), 7728 words:

  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/testing/SKILL.md: 1200
  - product-guidelines/testing/recognize.md: 363
  - product-guidelines/testing/template.md: 3187
  - product-guidelines/testing/starting_set.md: 143

Read from step 4 to the end, 3312 words:

  - product-guidelines/template.md: 1336
  - product-guidelines/testing/settle.md: 654
  - product-guidelines/testing/task_document.md: 364
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70
  - product-guidelines/testing/hand_back.md: 73

Total at the end of the run: 11040 words. Without the first reading in `refine-task` (2835 words): before step 4 4893, total 8205.

## 3. Tests and no guidelines, no preference; also an extension

Reading counted: steps 0-5 run; step 2 runs research and the critique of its reports (no preference, or every extension); the audit of step 3 runs (the product has tests); no new level; the critique of step 4 runs.

### Before

Read before step 4 (files in the order read), 14120 words:

  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/testing/SKILL.md: 3042
  - product-guidelines/template.md: 1336
  - product-guidelines/testing/template.md: 3187
  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Total at the end of the run: 14120 words. Without the first reading in `refine-task` (2835 words): before step 4 11285, total 11285.

### After

Read before step 4 (files in the order read), 9021 words:

  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/testing/SKILL.md: 1200
  - product-guidelines/testing/recognize.md: 363
  - product-guidelines/testing/template.md: 3187
  - product-guidelines/testing/starting_set.md: 143
  - product-guidelines/testing/research.md: 232
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70
  - product-guidelines/testing/audit.md: 230

Read from step 4 to the end, 2481 words:

  - product-guidelines/template.md: 1336
  - product-guidelines/testing/settle.md: 654
  - product-guidelines/testing/task_document.md: 364
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - product-guidelines/testing/hand_back.md: 73

Total at the end of the run: 11502 words. Without the first reading in `refine-task` (2835 words): before step 4 6186, total 8667.

## 4. Refresh

Reading counted: steps 0-5 run; step 2 runs no research (a refresh); the audit of step 3 runs (it audits each level again); no new level; the critique of step 4 runs, and it is the first critique of the session.

### Before

Read before step 4 (files in the order read), 13611 words:

  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/testing/SKILL.md: 3042
  - product-guidelines/template.md: 1336
  - product-guidelines/testing/template.md: 3187
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

Total at the end of the run: 14120 words. Without the first reading in `refine-task` (2835 words): before step 4 10776, total 11285.

### After

Read before step 4 (files in the order read), 7958 words:

  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/testing/SKILL.md: 1200
  - product-guidelines/testing/recognize.md: 363
  - product-guidelines/testing/template.md: 3187
  - product-guidelines/testing/starting_set.md: 143
  - product-guidelines/testing/audit.md: 230

Read from step 4 to the end, 3312 words:

  - product-guidelines/template.md: 1336
  - product-guidelines/testing/settle.md: 654
  - product-guidelines/testing/task_document.md: 364
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70
  - product-guidelines/testing/hand_back.md: 73

Total at the end of the run: 11270 words. Without the first reading in `refine-task` (2835 words): before step 4 5123, total 8435.

## 5. "A new level", recipe already standing, no step 2

Reading counted: steps 0, 1, 3 (the new-level case only, no audit), 4, 5 run; no step 2, so no research; the critique of step 4 runs, and it is the first critique of the session.

### Before

Read before step 4 (files in the order read), 13611 words:

  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/testing/SKILL.md: 3042
  - product-guidelines/template.md: 1336
  - product-guidelines/testing/template.md: 3187
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

Total at the end of the run: 14120 words. Without the first reading in `refine-task` (2835 words): before step 4 10776, total 11285.

### After

Read before step 4 (files in the order read), 7647 words:

  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/testing/SKILL.md: 1200
  - product-guidelines/testing/recognize.md: 363
  - product-guidelines/testing/template.md: 3187
  - product-guidelines/testing/new_level.md: 62

Read from step 4 to the end, 3312 words:

  - product-guidelines/template.md: 1336
  - product-guidelines/testing/settle.md: 654
  - product-guidelines/testing/task_document.md: 364
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70
  - product-guidelines/testing/hand_back.md: 73

Total at the end of the run: 10959 words. Without the first reading in `refine-task` (2835 words): before step 4 4812, total 8124.

## 6. Orchestrated mode on route 1

Reading counted: route 1 with orchestrated mode: the refiner reads orchestrated_mode.md and requests research and critiques from the orchestrator; the files it reads are counted as on route 1 plus orchestrated_mode.md.

### Before

Read before step 4 (files in the order read), 14120 words:

  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/testing/SKILL.md: 3042
  - product-guidelines/template.md: 1336
  - product-guidelines/testing/template.md: 3187
  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Total at the end of the run: 14120 words. Without the first reading in `refine-task` (2835 words): before step 4 11285, total 11285.

### After

Read before step 4 (files in the order read), 8889 words:

  - project-level/task/skill/SKILL.md: 396
  - project-level/task/template.md: 1739
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/testing/SKILL.md: 1200
  - product-guidelines/testing/orchestrated_mode.md: 98
  - product-guidelines/testing/recognize.md: 363
  - product-guidelines/testing/template.md: 3187
  - product-guidelines/testing/starting_set.md: 143
  - product-guidelines/testing/research.md: 232
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Read from step 4 to the end, 2481 words:

  - product-guidelines/template.md: 1336
  - product-guidelines/testing/settle.md: 654
  - product-guidelines/testing/task_document.md: 364
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - product-guidelines/testing/hand_back.md: 73

Total at the end of the run: 11370 words. Without the first reading in `refine-task` (2835 words): before step 4 6054, total 8535.


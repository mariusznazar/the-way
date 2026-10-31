# Word counts of the seven routes

Words are counted as `wc -w` counts them (whitespace-separated), Markdown and frontmatter included; of a file read by sections, the sections read (heading to the line before the next heading of the same or a higher level). Figures come from the worktree (state "after") and from commit f86fd71 for `product-guidelines/coding/SKILL.md` (state "before"); every other file counted is identical in both states, except the files new beside the skill.

Rules of the count:

- The first reading in `refine-task` is the files that step 0 of the base skill makes the session read a second time: `project-level/task/skill/SKILL.md`, `project-level/task/template.md`, and the sections "How a skill asks" and "Reading the foundation" of `elements/common/way_of_working.md` (3391 words together; the task's figure of 3391 words is the same). They count in both states; in state "before" the second reading counts again (a file read twice counts twice); in state "after" it is gone.
- Other files `refine-task` reads (`read_sources.md`, `draft.md`, `product-guidelines/reading.md`, and so on) are the same in both states and stay out; where the session starts on route 7, `refine-task`'s own `orchestrated_mode.md` is equally the same in both and stays out.
- A file a counted file sends the session to on the route counts in both states: the files beside `elements/common/critique/SKILL.md` (`prepare.md`, `check.md`, `settle.md`; 509 words) are read once, at the first critique of the session (step 2 where research ran, else step 4); a later critique does not read them again. The critic's own reading is another agent's context and is not counted.
- "Before step 4" is the text read before step 4 begins; the total is the sum at the end of the run, the file of the last step included (`hand_back.md`; in state "before" the last step is in `SKILL.md`).
- The product's own files (its root `AGENTS.md`, `guidelines/`) and the entries of its foundation differ by product and stay out of both states. The conditional file `new_tools.md` (a new tool left as a technology question) is read on none of these routes, and its words (69) come on top where the condition holds.
- In state "before", step 0 reads at the start of every run, whatever the route: both templates, the task skill and template, the two sections of the way of working, "Critique before collective review" and `critique/SKILL.md`; the base has one text for all routes, so the figures of state "before" are the same on every route except for the order of the files read.
- Route 3 counts a human without a preference (research runs); an extension also runs research, the trial run and the audit, so its figures equal route 3.
- Route 6 in state "before": the base has no route for one kind; a run on it reads the same text as any run, and that is what is counted.

## Summary

| Route | Before: to step 4 | Before: total | After: to step 4 | After: total | Before without the first reading (to step 4 / total) | After without the first reading (to step 4 / total) | Change of the total |
|---|---|---|---|---|---|---|---|
| 1. No code, human without a preference | 14511 | 14511 | 8620 | 11267 | 11120 / 11120 | 5229 / 7876 | -22.4% |
| 2. No code, human with a preference | 14002 | 14511 | 7592 | 11070 | 10611 / 11120 | 4201 / 7679 | -23.7% |
| 3. Code, no guidelines, no preference; also an extension | 14511 | 14511 | 9064 | 11711 | 11120 / 11120 | 5673 / 8320 | -19.3% |
| 4. Refresh | 14002 | 14511 | 8036 | 11514 | 10611 / 11120 | 4645 / 8123 | -20.7% |
| 5. "A new kind", guidelines already standing | 14002 | 14511 | 5300 | 10890 | 10611 / 11120 | 1909 / 7499 | -25.0% |
| 6. One kind whose files exist (fifth mode, To do 9-13) | 14002 | 14511 | 7607 | 11085 | 10611 / 11120 | 4216 / 7694 | -23.6% |
| 7. Orchestrated mode on route 1 | 14511 | 14511 | 8733 | 11380 | 11120 / 11120 | 5342 / 7989 | -21.6% |

## 1. No code, human without a preference

Reading counted: steps 0-2, 4, 5 run; step 2 runs research and the critique of its reports; no step 3 (no code); the critique of step 4 runs and is not the first of the session.

### Before

Read before step 4 (files in the order read), 14511 words:

  - project-level/task/skill/SKILL.md: 463
  - project-level/task/template.md: 2228
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/coding/SKILL.md: 3396
  - product-guidelines/template.md: 1336
  - product-guidelines/coding/template.md: 2112
  - project-level/task/skill/SKILL.md: 463
  - project-level/task/template.md: 2228
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Total at the end of the run: 14511 words. Without the first reading in `refine-task` (3391 words): before step 4 11120, total 11120.

### After

Read before step 4 (files in the order read), 8620 words:

  - project-level/task/skill/SKILL.md: 463
  - project-level/task/template.md: 2228
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/coding/SKILL.md: 1506
  - product-guidelines/coding/recognize.md: 403
  - product-guidelines/coding/template.md: 2112
  - product-guidelines/coding/starting_set.md: 180
  - product-guidelines/coding/research.md: 197
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Read from step 4 to the end, 2647 words:

  - product-guidelines/template.md: 1336
  - product-guidelines/coding/settle.md: 635
  - product-guidelines/coding/task_document.md: 509
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - product-guidelines/coding/hand_back.md: 113

Total at the end of the run: 11267 words. Without the first reading in `refine-task` (3391 words): before step 4 5229, total 7876.

## 2. No code, human with a preference

Reading counted: steps 0-2, 4, 5 run; step 2 runs no research (the human has a preference); no step 3; the critique of step 4 runs and is the first of the session.

### Before

Read before step 4 (files in the order read), 14002 words:

  - project-level/task/skill/SKILL.md: 463
  - project-level/task/template.md: 2228
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/coding/SKILL.md: 3396
  - product-guidelines/template.md: 1336
  - product-guidelines/coding/template.md: 2112
  - project-level/task/skill/SKILL.md: 463
  - project-level/task/template.md: 2228
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - elements/common/critique/SKILL.md: 322

Read from step 4 to the end, 509 words:

  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Total at the end of the run: 14511 words. Without the first reading in `refine-task` (3391 words): before step 4 10611, total 11120.

### After

Read before step 4 (files in the order read), 7592 words:

  - project-level/task/skill/SKILL.md: 463
  - project-level/task/template.md: 2228
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/coding/SKILL.md: 1506
  - product-guidelines/coding/recognize.md: 403
  - product-guidelines/coding/template.md: 2112
  - product-guidelines/coding/starting_set.md: 180

Read from step 4 to the end, 3478 words:

  - product-guidelines/template.md: 1336
  - product-guidelines/coding/settle.md: 635
  - product-guidelines/coding/task_document.md: 509
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70
  - product-guidelines/coding/hand_back.md: 113

Total at the end of the run: 11070 words. Without the first reading in `refine-task` (3391 words): before step 4 4201, total 7679.

## 3. Code, no guidelines, no preference; also an extension

Reading counted: steps 0-5 run; step 2 runs research and the critique of its reports; step 3 runs the trial run and the audit of every kind; the critique of step 4 runs and is not the first of the session.

### Before

Read before step 4 (files in the order read), 14511 words:

  - project-level/task/skill/SKILL.md: 463
  - project-level/task/template.md: 2228
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/coding/SKILL.md: 3396
  - product-guidelines/template.md: 1336
  - product-guidelines/coding/template.md: 2112
  - project-level/task/skill/SKILL.md: 463
  - project-level/task/template.md: 2228
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Total at the end of the run: 14511 words. Without the first reading in `refine-task` (3391 words): before step 4 11120, total 11120.

### After

Read before step 4 (files in the order read), 9064 words:

  - project-level/task/skill/SKILL.md: 463
  - project-level/task/template.md: 2228
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/coding/SKILL.md: 1506
  - product-guidelines/coding/recognize.md: 403
  - product-guidelines/coding/template.md: 2112
  - product-guidelines/coding/starting_set.md: 180
  - product-guidelines/coding/research.md: 197
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70
  - product-guidelines/coding/trial_run.md: 249
  - product-guidelines/coding/kinds.md: 195

Read from step 4 to the end, 2647 words:

  - product-guidelines/template.md: 1336
  - product-guidelines/coding/settle.md: 635
  - product-guidelines/coding/task_document.md: 509
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - product-guidelines/coding/hand_back.md: 113

Total at the end of the run: 11711 words. Without the first reading in `refine-task` (3391 words): before step 4 5673, total 8320.

## 4. Refresh

Reading counted: steps 0-5 run; step 2 runs no research (a refresh); step 3 runs the trial run and the audit of every kind; the critique of step 4 runs and is the first of the session.

### Before

Read before step 4 (files in the order read), 14002 words:

  - project-level/task/skill/SKILL.md: 463
  - project-level/task/template.md: 2228
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/coding/SKILL.md: 3396
  - product-guidelines/template.md: 1336
  - product-guidelines/coding/template.md: 2112
  - project-level/task/skill/SKILL.md: 463
  - project-level/task/template.md: 2228
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - elements/common/critique/SKILL.md: 322

Read from step 4 to the end, 509 words:

  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Total at the end of the run: 14511 words. Without the first reading in `refine-task` (3391 words): before step 4 10611, total 11120.

### After

Read before step 4 (files in the order read), 8036 words:

  - project-level/task/skill/SKILL.md: 463
  - project-level/task/template.md: 2228
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/coding/SKILL.md: 1506
  - product-guidelines/coding/recognize.md: 403
  - product-guidelines/coding/template.md: 2112
  - product-guidelines/coding/starting_set.md: 180
  - product-guidelines/coding/trial_run.md: 249
  - product-guidelines/coding/kinds.md: 195

Read from step 4 to the end, 3478 words:

  - product-guidelines/template.md: 1336
  - product-guidelines/coding/settle.md: 635
  - product-guidelines/coding/task_document.md: 509
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70
  - product-guidelines/coding/hand_back.md: 113

Total at the end of the run: 11514 words. Without the first reading in `refine-task` (3391 words): before step 4 4645, total 8123.

## 5. "A new kind", guidelines already standing

Reading counted: steps 0, 1, 3 (the paragraph "A new kind" in SKILL.md only; no trial_run.md, no kinds.md), 4, 5 run; no step 2; the coding template is read first at step 4; the critique of step 4 runs and is the first of the session.

### Before

Read before step 4 (files in the order read), 14002 words:

  - project-level/task/skill/SKILL.md: 463
  - project-level/task/template.md: 2228
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/coding/SKILL.md: 3396
  - product-guidelines/template.md: 1336
  - product-guidelines/coding/template.md: 2112
  - project-level/task/skill/SKILL.md: 463
  - project-level/task/template.md: 2228
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - elements/common/critique/SKILL.md: 322

Read from step 4 to the end, 509 words:

  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Total at the end of the run: 14511 words. Without the first reading in `refine-task` (3391 words): before step 4 10611, total 11120.

### After

Read before step 4 (files in the order read), 5300 words:

  - project-level/task/skill/SKILL.md: 463
  - project-level/task/template.md: 2228
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/coding/SKILL.md: 1506
  - product-guidelines/coding/recognize.md: 403

Read from step 4 to the end, 5590 words:

  - product-guidelines/template.md: 1336
  - product-guidelines/coding/template.md: 2112
  - product-guidelines/coding/settle.md: 635
  - product-guidelines/coding/task_document.md: 509
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70
  - product-guidelines/coding/hand_back.md: 113

Total at the end of the run: 10890 words. Without the first reading in `refine-task` (3391 words): before step 4 1909, total 7499.

## 6. One kind whose files exist (fifth mode, To do 9-13)

Reading counted: steps 0, 1, 3 (kinds.md, with the coding template read there; no trial run), 4, 5 run; no step 2; the critique of step 4 runs and is the first of the session. In the state before the base has no such route; its reading is counted as the base text gives it to any run.

### Before

Read before step 4 (files in the order read), 14002 words:

  - project-level/task/skill/SKILL.md: 463
  - project-level/task/template.md: 2228
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/coding/SKILL.md: 3396
  - product-guidelines/template.md: 1336
  - product-guidelines/coding/template.md: 2112
  - project-level/task/skill/SKILL.md: 463
  - project-level/task/template.md: 2228
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - elements/common/critique/SKILL.md: 322

Read from step 4 to the end, 509 words:

  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Total at the end of the run: 14511 words. Without the first reading in `refine-task` (3391 words): before step 4 10611, total 11120.

### After

Read before step 4 (files in the order read), 7607 words:

  - project-level/task/skill/SKILL.md: 463
  - project-level/task/template.md: 2228
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/coding/SKILL.md: 1506
  - product-guidelines/coding/recognize.md: 403
  - product-guidelines/coding/template.md: 2112
  - product-guidelines/coding/kinds.md: 195

Read from step 4 to the end, 3478 words:

  - product-guidelines/template.md: 1336
  - product-guidelines/coding/settle.md: 635
  - product-guidelines/coding/task_document.md: 509
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70
  - product-guidelines/coding/hand_back.md: 113

Total at the end of the run: 11085 words. Without the first reading in `refine-task` (3391 words): before step 4 4216, total 7694.

## 7. Orchestrated mode on route 1

Reading counted: route 1 with orchestrated mode: the refiner reads orchestrated_mode.md and requests research and critiques from the orchestrator; the files it reads are counted as on route 1 plus orchestrated_mode.md.

### Before

Read before step 4 (files in the order read), 14511 words:

  - project-level/task/skill/SKILL.md: 463
  - project-level/task/template.md: 2228
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/coding/SKILL.md: 3396
  - product-guidelines/template.md: 1336
  - product-guidelines/coding/template.md: 2112
  - project-level/task/skill/SKILL.md: 463
  - project-level/task/template.md: 2228
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Total at the end of the run: 14511 words. Without the first reading in `refine-task` (3391 words): before step 4 11120, total 11120.

### After

Read before step 4 (files in the order read), 8733 words:

  - project-level/task/skill/SKILL.md: 463
  - project-level/task/template.md: 2228
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/coding/SKILL.md: 1506
  - product-guidelines/coding/orchestrated_mode.md: 113
  - product-guidelines/coding/recognize.md: 403
  - product-guidelines/coding/template.md: 2112
  - product-guidelines/coding/starting_set.md: 180
  - product-guidelines/coding/research.md: 197
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Read from step 4 to the end, 2647 words:

  - product-guidelines/template.md: 1336
  - product-guidelines/coding/settle.md: 635
  - product-guidelines/coding/task_document.md: 509
  - elements/common/way_of_working.md section "Critique before collective review": 54
  - product-guidelines/coding/hand_back.md: 113

Total at the end of the run: 11380 words. Without the first reading in `refine-task` (3391 words): before step 4 5342, total 7989.


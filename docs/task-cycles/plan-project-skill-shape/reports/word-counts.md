# Word counts of the seven routes

Words are counted as `wc -w` counts them (whitespace-separated), Markdown and frontmatter included; of a file read by sections, the sections read (the heading to the line before the next heading of the same or a higher level). The state "before" is commit 2f51e6c (`project-level/plan/skill/SKILL.md` is its only file of the skill); the state "after" is the worktree after the last change of a counted file. The definition, the plan and the product's files are outside the count.

Rules of the count:

- "Skill text" is `SKILL.md` and the files beside it that the route reads. "Read beside the skill" is what the route reads outside the skill: `project-level/plan/template.md` (step 0, every route), the section "How a skill asks" of `elements/common/way_of_working.md` (step 0), the section "Reading the foundation" of the same file and `product-guidelines/reading.md` (step 1, where step 1 runs), `project-level/lead/conversation_template.md` (a dispatched turn) and the four files of the critique (`elements/common/critique/SKILL.md`, `prepare.md`, `check.md`, `settle.md`), where the author runs the critique. The critic's own reading is another agent's context and is not counted.
- Both states count the same files beside the skill; they differ only in the skill text. A route that skips a step in the state "before" skips it in the state "after" too, except that `existing_plan.md` has a session working on an existing plan go through `read.md` (step 1) before it goes on; step 1 is therefore carried out on every route that reads that file, in both states (see the next rule).
- The rule for step 1 on a route that goes on from a later step (routes 3 and 6): the sentence of `existing_plan.md` has the session go through `read.md`, that is carry step 1 out, so the readings of step 1 count, the section "Reading the foundation" and `product-guidelines/reading.md` included. The recorded sessions ran the readiness check in 14 of 14 and reached the foundation in 11, whatever the base's text said, so the state "before" counts step 1 as carried out too, on these two routes; the table above and the summary use that reading. The base's text read literally sent a resumed draft from the first unfinished step, past step 1; the figures of that literal reading are given beside, after the summary.
- A file the skill reads for a condition that does not hold on the route is not counted: `guideline_tasks.md` only on routes 2 and 5b. Route 4 reads no `place_questions.md` (no question moves in a split of a task); where one moves, its words come on top.
- Route 5 is counted in the two readings the task gives: 5a, the agent reads its own steps; 5b, it reads everything.

## Summary

| Route | Skill text before | Total before | Skill text after | Total after | Change of the skill text | Change of the total |
|---|---|---|---|---|---|---|
| 1. New breakdown, the guidelines reading found nothing | 2344 | 6897 | 2407 | 6960 | +2.7% | +0.9% |
| 2. New breakdown with the guidelines file | 2344 | 6897 | 2583 | 7136 | +10.2% | +3.5% |
| 3. Resume of a draft from step 5 | 2344 | 6897 | 1949 | 6502 | -16.9% | -5.7% |
| 4. Human's correction to a handed-over plan, for example a split of a task | 2344 | 6897 | 2429 | 6982 | +3.6% | +1.2% |
| 5a. Narrow dispatched turn, one change, the agent reads its own steps | 2344 | 7485 | 1986 | 7127 | -15.3% | -4.8% |
| 5b. Narrow dispatched turn, one change, the agent reads everything | 2344 | 7485 | 3047 | 8188 | +30.0% | +9.4% |
| 6. Dispatched turn of the hand over alone | 2344 | 7485 | 1730 | 6871 | -26.2% | -8.2% |
| 7. Dispatched recheck after the definition's gate | 2344 | 7485 | 2871 | 8012 | +22.5% | +7.0% |

## The literal reading of the base on routes 3 and 6

Read literally, the base sent a resumed draft from the first unfinished step, past step 1, so that a route which goes on from step 5 or hands over alone did not read the foundation or the guidelines. The figures of that reading, the state "before" without the section "Reading the foundation" and `product-guidelines/reading.md`, set beside the state "after" with step 1 carried out:

- Route 3: before, literal reading, 5264 words in total (skill text 2344); after, step 1 carried out, 6502 words in total (skill text 1949); the change of the total is +23.5%. Before with step 1 carried out, as the table counts it: 6897 words, change -5.7%.
- Route 6: before, literal reading, 5852 words in total (skill text 2344); after, step 1 carried out, 6871 words in total (skill text 1730); the change of the total is +17.4%. Before with step 1 carried out, as the table counts it: 7485 words, change -8.2%.

## Comparison with the estimates of the task (question 1 and its correction)

The estimates are for the text of the skill alone, the first column of each state above.

- A fresh breakdown, estimated 2300-2900 words: route 1 reads 2407 and route 2 reads 2583. Both inside.
- A narrow turn that reads its own steps, estimated 1650-1850 and corrected to 1800-2000 once the file of step 1 is counted: route 5a reads 1986, inside the corrected range. Route 6 (the hand over alone, which reads the files of steps 0 and 1 and step 7) reads 1730, below it: the estimate did not cover a turn of one step.
- A narrow turn that reads everything, estimated 2800-3250: route 5b reads 3047, inside; route 7 (a recheck, no guidelines file) reads 2871, inside.
- The cost of reading everything against today, estimated 450-900 words more than 2344: route 5b reads 703 more, inside.
- The not-chosen way of question 4 expected the realistic change of the skill text at -15% to +25%: the real range is -26.2% to +30.0% (routes 6 and 5b), so those two fall outside it; the totals with the files read beside the skill change by -8.2% to +9.4%, step 1 counted in both states on routes 3 and 6; counted in the state after alone the totals of routes 3 and 6 would rise (see the literal reading above).
- The task's 'about 170 words on every route with an existing plan' is the file `read.md` alone (141 words); what the sentence of `existing_plan.md` sets off on routes 3 and 6 is that file plus the section 'Reading the foundation' (492 words) and `product-guidelines/reading.md` (1141 words), 1774 words together with the file.
- Figures that the task states and that the files confirm: `SKILL.md` 2344 words at 2f51e6c, `project-level/plan/template.md` 1881 words, the section 'How a skill asks' 208 words. The file of step 1 (`read.md`) is 141 words against the estimate of about 170 for the reading of step 1.

## 1. New breakdown, the guidelines reading found nothing

Reading counted: steps 0-7 run, a human-led session; the critique of step 6 runs (critique files read); no existing plan, no guidelines file.

### Before

Skill text, 2344 words:

  - project-level/plan/skill/SKILL.md: 2344

Read beside the skill, 4553 words:

  - project-level/plan/template.md: 1881
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/reading.md: 1141
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Total at the end of the run: 6897 words.

### After

Skill text, 2407 words:

  - project-level/plan/skill/SKILL.md: 623
  - project-level/plan/skill/read.md: 141
  - project-level/plan/skill/reading_definition_and_plan.md: 291
  - project-level/plan/skill/cut_tasks.md: 267
  - project-level/plan/skill/assign_entries.md: 213
  - project-level/plan/skill/place_questions.md: 165
  - project-level/plan/skill/write_and_check.md: 254
  - project-level/plan/skill/critique_plan.md: 242
  - project-level/plan/skill/hand_over.md: 211

Read beside the skill, 4553 words:

  - project-level/plan/template.md: 1881
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/reading.md: 1141
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Total at the end of the run: 6960 words.

## 2. New breakdown with the guidelines file

Reading counted: route 1 and the guidelines tasks of step 2 (guideline_tasks.md read).

### Before

Skill text, 2344 words:

  - project-level/plan/skill/SKILL.md: 2344

Read beside the skill, 4553 words:

  - project-level/plan/template.md: 1881
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/reading.md: 1141
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Total at the end of the run: 6897 words.

### After

Skill text, 2583 words:

  - project-level/plan/skill/SKILL.md: 623
  - project-level/plan/skill/read.md: 141
  - project-level/plan/skill/reading_definition_and_plan.md: 291
  - project-level/plan/skill/cut_tasks.md: 267
  - project-level/plan/skill/guideline_tasks.md: 176
  - project-level/plan/skill/assign_entries.md: 213
  - project-level/plan/skill/place_questions.md: 165
  - project-level/plan/skill/write_and_check.md: 254
  - project-level/plan/skill/critique_plan.md: 242
  - project-level/plan/skill/hand_over.md: 211

Read beside the skill, 4553 words:

  - project-level/plan/template.md: 1881
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/reading.md: 1141
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Total at the end of the run: 7136 words.

## 3. Resume of a draft from step 5

Reading counted: steps 0, 5, 6, 7 run, a human-led session on an existing plan whose status reads draft; step 1 is carried out in the state after (existing_plan.md has the session go through read.md), so the foundation and the guidelines are read, and in the state before as well, by the rule below; the critique runs.

### Before

Skill text, 2344 words:

  - project-level/plan/skill/SKILL.md: 2344

Read beside the skill, 4553 words:

  - project-level/plan/template.md: 1881
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/reading.md: 1141
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Total at the end of the run: 6897 words.

### After

Skill text, 1949 words:

  - project-level/plan/skill/SKILL.md: 623
  - project-level/plan/skill/existing_plan.md: 187
  - project-level/plan/skill/reading_definition_and_plan.md: 291
  - project-level/plan/skill/read.md: 141
  - project-level/plan/skill/write_and_check.md: 254
  - project-level/plan/skill/critique_plan.md: 242
  - project-level/plan/skill/hand_over.md: 211

Read beside the skill, 4553 words:

  - project-level/plan/template.md: 1881
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/reading.md: 1141
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Total at the end of the run: 6502 words.

## 4. Human's correction to a handed-over plan, for example a split of a task

Reading counted: steps 0, 1, 2, 3, 5, 6, 7 run, a human-led session on an existing plan; step 4 (no question moves) and the guidelines file are not read; the critique runs.

### Before

Skill text, 2344 words:

  - project-level/plan/skill/SKILL.md: 2344

Read beside the skill, 4553 words:

  - project-level/plan/template.md: 1881
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/reading.md: 1141
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Total at the end of the run: 6897 words.

### After

Skill text, 2429 words:

  - project-level/plan/skill/SKILL.md: 623
  - project-level/plan/skill/existing_plan.md: 187
  - project-level/plan/skill/reading_definition_and_plan.md: 291
  - project-level/plan/skill/read.md: 141
  - project-level/plan/skill/cut_tasks.md: 267
  - project-level/plan/skill/assign_entries.md: 213
  - project-level/plan/skill/write_and_check.md: 254
  - project-level/plan/skill/critique_plan.md: 242
  - project-level/plan/skill/hand_over.md: 211

Read beside the skill, 4553 words:

  - project-level/plan/template.md: 1881
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/reading.md: 1141
  - elements/common/critique/SKILL.md: 322
  - elements/common/critique/prepare.md: 145
  - elements/common/critique/check.md: 294
  - elements/common/critique/settle.md: 70

Total at the end of the run: 6982 words.

## 5a. Narrow dispatched turn, one change, the agent reads its own steps

Reading counted: a turn dispatched by lead-project that applies a requested change: steps 0, 1, 3, 5 run; the critique is requested through the conversation, so the critique files are not read; delegated_mode.md read.

### Before

Skill text, 2344 words:

  - project-level/plan/skill/SKILL.md: 2344

Read beside the skill, 5141 words:

  - project-level/plan/template.md: 1881
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/reading.md: 1141
  - project-level/lead/conversation_template.md: 1419

Total at the end of the run: 7485 words.

### After

Skill text, 1986 words:

  - project-level/plan/skill/SKILL.md: 623
  - project-level/plan/skill/delegated_mode.md: 277
  - project-level/plan/skill/existing_plan.md: 187
  - project-level/plan/skill/reading_definition_and_plan.md: 291
  - project-level/plan/skill/read.md: 141
  - project-level/plan/skill/assign_entries.md: 213
  - project-level/plan/skill/write_and_check.md: 254

Read beside the skill, 5141 words:

  - project-level/plan/template.md: 1881
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/reading.md: 1141
  - project-level/lead/conversation_template.md: 1419

Total at the end of the run: 7127 words.

## 5b. Narrow dispatched turn, one change, the agent reads everything

Reading counted: the turn of 5a (steps 0, 1, 3, 5 run) reading every file of the skill, the guidelines file included.

### Before

Skill text, 2344 words:

  - project-level/plan/skill/SKILL.md: 2344

Read beside the skill, 5141 words:

  - project-level/plan/template.md: 1881
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/reading.md: 1141
  - project-level/lead/conversation_template.md: 1419

Total at the end of the run: 7485 words.

### After

Skill text, 3047 words:

  - project-level/plan/skill/SKILL.md: 623
  - project-level/plan/skill/delegated_mode.md: 277
  - project-level/plan/skill/existing_plan.md: 187
  - project-level/plan/skill/reading_definition_and_plan.md: 291
  - project-level/plan/skill/read.md: 141
  - project-level/plan/skill/cut_tasks.md: 267
  - project-level/plan/skill/guideline_tasks.md: 176
  - project-level/plan/skill/assign_entries.md: 213
  - project-level/plan/skill/place_questions.md: 165
  - project-level/plan/skill/write_and_check.md: 254
  - project-level/plan/skill/critique_plan.md: 242
  - project-level/plan/skill/hand_over.md: 211

Read beside the skill, 5141 words:

  - project-level/plan/template.md: 1881
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/reading.md: 1141
  - project-level/lead/conversation_template.md: 1419

Total at the end of the run: 8188 words.

## 6. Dispatched turn of the hand over alone

Reading counted: a turn dispatched by lead-project that only hands the plan over: steps 0 and 7 run (step 1 is carried out in both states by the rule below, as existing_plan.md has it); no critique run.

### Before

Skill text, 2344 words:

  - project-level/plan/skill/SKILL.md: 2344

Read beside the skill, 5141 words:

  - project-level/plan/template.md: 1881
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/reading.md: 1141
  - project-level/lead/conversation_template.md: 1419

Total at the end of the run: 7485 words.

### After

Skill text, 1730 words:

  - project-level/plan/skill/SKILL.md: 623
  - project-level/plan/skill/delegated_mode.md: 277
  - project-level/plan/skill/existing_plan.md: 187
  - project-level/plan/skill/reading_definition_and_plan.md: 291
  - project-level/plan/skill/read.md: 141
  - project-level/plan/skill/hand_over.md: 211

Read beside the skill, 5141 words:

  - project-level/plan/template.md: 1881
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/reading.md: 1141
  - project-level/lead/conversation_template.md: 1419

Total at the end of the run: 6871 words.

## 7. Dispatched recheck after the definition's gate

Reading counted: a turn dispatched by lead-project that rechecks the plan from step 0: steps 0-7 run, no guidelines file; the critique is requested through the conversation, so the critique files are not read.

### Before

Skill text, 2344 words:

  - project-level/plan/skill/SKILL.md: 2344

Read beside the skill, 5141 words:

  - project-level/plan/template.md: 1881
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/reading.md: 1141
  - project-level/lead/conversation_template.md: 1419

Total at the end of the run: 7485 words.

### After

Skill text, 2871 words:

  - project-level/plan/skill/SKILL.md: 623
  - project-level/plan/skill/delegated_mode.md: 277
  - project-level/plan/skill/existing_plan.md: 187
  - project-level/plan/skill/reading_definition_and_plan.md: 291
  - project-level/plan/skill/read.md: 141
  - project-level/plan/skill/cut_tasks.md: 267
  - project-level/plan/skill/assign_entries.md: 213
  - project-level/plan/skill/place_questions.md: 165
  - project-level/plan/skill/write_and_check.md: 254
  - project-level/plan/skill/critique_plan.md: 242
  - project-level/plan/skill/hand_over.md: 211

Read beside the skill, 5141 words:

  - project-level/plan/template.md: 1881
  - elements/common/way_of_working.md section "How a skill asks": 208
  - elements/common/way_of_working.md section "Reading the foundation": 492
  - product-guidelines/reading.md: 1141
  - project-level/lead/conversation_template.md: 1419

Total at the end of the run: 8012 words.


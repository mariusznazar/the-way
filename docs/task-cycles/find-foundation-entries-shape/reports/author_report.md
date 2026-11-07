# Report of the one author - find-foundation-entries in the shape of WAY-256

**Status:** done with concerns. The concern is one number of the task that does not match the file (see "Searches not found or unclear", item 1); nothing blocks the request.

## What was made

- Commit `a15de09` on `task/find-foundation-entries-shape` (base `f447bb6`; a fix commit `e9c900a` follows, see `fix.md`): `docs: split find-foundation-entries into SKILL.md and files beside it by step and variant (WAY-256)`.
- Files, all in `elements/common/skill/` (added / removed lines against the base):
  - `SKILL.md` +19 -95: the picture of the whole, the caller table with the variant files, the resume rule, step 3 whole, and a pointer at each of steps 1, 2, 4 and 5.
  - `read.md` +12: step 1, the procedure common to both variants.
  - `build_table.md` +15: step 2, the procedure common to both variants.
  - `definition_variant.md` +65: the project-definition variant (what the caller gives; the lines for steps 1, 2, 4, 5).
  - `task_variant.md` +52: the task variant (the same headings).
- Nothing outside `elements/common/skill/` changed: not `projected_mode.md`, not `way_of_working.md`, not a caller, not the description, not the entry points, no Python.
- Written under `.runs/task-cycles/find-foundation-entries-shape/reports/` (not in a commit): `assessment.md` (table of 30 rows and four proposals), `word-counts.md`, `verify_counts.py`, `route_check.py` and this report.
- Foundation step: the task's *Settlements to record* holds no row (`Candidates: 11 shown, 0 accepted`) and the task carries no projected entry, so there is no entry to write. No spec and no plan existed.

## Words

<!-- counts:begin -->
| Route and sum | Before (base) | After | Change |
|---|---|---|---|
| Task mode, sum 1: the skill's own text read on the route | 1584 | 1397 | -12% |
| Task mode, sum 2: sum 1 with the files read beside it (`way_of_working.md`, the task template section) | 3741 | 3554 | -5% |
| Task mode, sum 3: sum 2 without what step 1 of `refine-task` read earlier (the whole task template, "How a skill asks", "Reading the foundation") | 2625 | 2438 | -7% |
| Project definition, sum 1: the skill's own text read on the route | 1584 | 1546 | -2% |
| Project definition, sum 2: sum 1 with the files read beside it (`way_of_working.md`, the definition template section, `projected_mode.md`) | 4429 | 4391 | -1% |

Files after the rebuild: `SKILL.md` 598, `read.md` 126, `build_table.md` 198, `definition_variant.md` 624, `task_variant.md` 475; together 2021 words (base `SKILL.md`: 1584).

Files read beside the skill, unchanged: `way_of_working.md` 1752; its sections "How a skill asks" 208 and "Reading the foundation" 503; the task template section "Settlements to record" with its rule 405; the definition template section "Projected foundation changes" 674; `projected_mode.md` 419.
<!-- counts:end -->

The counts were made after the commit, and `verify_counts.py` fails if `elements/common/skill/` is not clean, if any number here or in `word-counts.md` differs from the files, or if a number of the proposals in `assessment.md` differs.

## Checks

| Command (from the worktree root) | Exit code | Result |
|---|---|---|
| `python -B gate/run_tests.py elements/common` | 0 | 109 tests, OK |
| `python -B gate/run_tests.py agent-instructions` | 0 | 18 tests, OK |
| `python -B gate/run_tests.py installation` | 0 | 44 tests, OK |
| `python -B elements/common/foundation_check.py` | 0 | 0 errors |
| `python -B agent-instructions/skill_entry_points.py` | 0 | "entry points are current" |
| `python -B instruction-files/check_instructions.py .` | 0 | 0 errors, 1 warning (`AGENTS.md:21`, `_zadania\` does not exist; not a file of this skill) |
| `python -B instruction-files/check_instructions.py --file elements/common/skill/<each of the five files>` | 0 each | 0 errors; 3, 2, 0, 2 and 3 dead-path warnings (10 together), which the `--file` mode gives for any repository-relative path; the base `SKILL.md` gives 10 as well |
| `python -I -B .runs/task-cycles/find-foundation-entries-shape/reports/verify_counts.py` | 0 | 0 problems; one note: the task's 424 is lines 181-208, the report counts 405 |
| `python -I -B .runs/task-cycles/find-foundation-entries-shape/reports/route_check.py` | 0 | 0 problems; with a leaked and a lost phrase added on purpose it reports both (3 problems), so it can fail |

Not run: the whole gate (`python -B gate/run_tests.py`), which is the orchestrator's run. No test was written and no failing run exists, because the change is prose for agents with no behaviour a test of this repository reaches (`task-cycle/change/SKILL.md` section 2: prose is tested by what an agent does with it - see the walkthrough below); no invariant's test changed.

## Own-work check (section 3)

- Requirement most likely not met: "every rewritten conditional or pointer is compared with the base, adds no route and loses none" - the cut of a text by variant is where a rule is lost without a failing test.
- Check: `route_check.py` takes 30 distinctive phrases of the base, each with the variants that needed it on the base (both, definition only, task only), and tests that the phrase is on the route of every variant that needed it and on no route of one that did not, and that the callers' words ("task mode" in four callers, "Settlements to record", "Projected foundation changes") stand in `SKILL.md`. It shows 0 problems; the same script with two false expectations added reports them, so a lost or leaked phrase would be seen. Also, a 5-word window of the base against the five new files left only the places the table below explains (the labels "for a project definition" and "for a task", the sentence on the search, the lines of step 4 and 5 that open with a label).
- The check is a presence check; a changed meaning is not a presence. The comparison below is made by hand for each conditional.
- Walkthrough, task mode. `SKILL.md` -> caller table, second row ("task mode", rows of "Settlements to record") -> step 1: read `task_variant.md`, carry out `read.md` -> reads `way_of_working.md`, the task template section and rule, the projected entries of *Decisions in play*, the source, the foundation, the element templates -> step 2: `build_table.md` and the lines for step 2 of `task_variant.md` -> step 3 in `SKILL.md` -> step 4: `SKILL.md` says the step does not run, the lines for step 4 of `task_variant.md` take its place -> step 5 of `task_variant.md`. Left: the whole text of the definition variant, `projected_mode.md`, the definition template section. Dropped from the route: nothing task mode used.
- Walkthrough, project definition. `SKILL.md` -> caller table, first row (`define-project`, projected entries into "Projected foundation changes") -> step 1: read `definition_variant.md`, carry out `read.md` -> reads `way_of_working.md`, the definition template section, `projected_mode.md`, the source, the foundation, the element templates -> step 2: `build_table.md` and the definition lines -> step 3 -> step 4 (question, answer, hand over, added rows) and step 5 of `definition_variant.md`. Left: the task variant.

## Comparison with the base - each changed conditional or pointer

| What changed | Base | After | Route added | Route lost |
|---|---|---|---|---|
| Choice of variant | Lines 24-28: three "for a project definition" bullets; lines 30-34: "For the refinement of a task (WAY-134), `refine-task` gives ..." | `SKILL.md` table: the caller (`define-project` with a project definition and projected entries / `refine-task`, "task mode", rows of "Settlements to record") and the file of each | none | none. A caller that is neither had no rule on the base and has none now |
| Resume | Lines 36-37, before step 1 | Same sentence, before step 1, same place | none | none |
| Template reading at step 1 | Lines 41-46: `way_of_working.md` in full, "and in `definition_template.md` the section ... in full; for a task, in `task/template.md` the section ... in full"; for a definition also `projected_mode.md` | Both variants read `way_of_working.md` in full (`read.md`). Definition: definition section and `projected_mode.md`. Task: task section and rule only | none | In task mode, the reading of the definition template section - under the base's second reading of the sentence ("in addition to"); the first reading ("instead of") is kept. Settled by question 2 of the task (answer: not read) |
| Projected entries of *Decisions in play* | Lines 55-56 "For a task, also read ..." | `task_variant.md`, Step 1 | none | none |
| Candidates to take (step 2) | Lines 60-63 unlabelled (a definition's headings); lines 75-79 "For a task: ..." | Definition variant / task variant, Step 2 | none | none: the headings of lines 60-63 ("Inputs and constraints", "Success") are not those of a task document, and lines 75-79 stay for the task |
| Writing the table (step 2) | Lines 72-74 unlabelled (the definition's table); line 80-81 "... and show it whole as above" | Definition variant: the same text. Task variant: states, display and reasons written out | none | none: what "as above" imported is now stated in the task variant (see the next section) |
| Who makes the one search | Lines 82-86: "For a project definition, `define-project` makes ... for a task, its cycle makes it ..." | `build_table.md` keeps "No search of the whole foundation runs here; those lines say who makes it" and the collision rule; each variant holds its clause | none | none |
| Step 4 | Lines 95-125: "For a task, this step does not run: ..." and "For a project definition, for each accepted row ..." | `SKILL.md` step 4: "For a project definition, carry out the lines for step 4 of `definition_variant.md`. In task mode this step does not run; carry out in its place the lines for step 4 of `task_variant.md`" | none | none |
| Step 5 | Lines 129-133 "For a project definition ...", 134-138 "For a task ..." | `SKILL.md` step 5 names the lines of each variant file | none | none |
| Read or carry out | One file; nothing to name | Each pointer says which: the variant file is read in full once and its lines are carried out at their steps; `read.md` and `build_table.md` are carried out | none | none |
| Come to a later step without the file | Not stated: a resumed use read step 1 first | "where you come to step 2, 4 or 5 without having read it, read it first" | none | none: a use that reads the file at step 1 is not told to read it again |

## Comparison with the base - each new sentence and what it switches off

| New sentence (file) | What it switches off |
|---|---|
| "The caller gives the source, the next reader and the mode of the entries. Their values, and what else changes with the caller at steps 1, 2, 4 and 5, stand in the file of your variant:" and the table (`SKILL.md`) | An agent taking the values of the other variant, or reading both variant files; nothing in a rule |
| "Read the file of your variant in full once, at step 1; where you come to step 2, 4 or 5 without having read it, read it first." (`SKILL.md`) | A second read of the variant file at each step; coming to a later step - by a start there or by a resume that passes step 1 - without the variant's lines (WAY-256, a later step has the file read unless an earlier step did) |
| Step 1, 2, 4, 5 pointers (`SKILL.md`): "Read ... then carry out `read.md` ...", "Carry out `build_table.md` ...", "For a project definition, carry out the lines for step 4 of `definition_variant.md`. In task mode this step does not run; ...", step 5 likewise | The text of the other variant's step; step 4 in task mode (the base sentence "this step does not run" kept) |
| "Carry out the lines for step 1 of the file of your variant: they name what else to read." (`read.md`) | A template section read outside the variant file, which is how the definition section was read in task mode under the second reading of the base |
| "Take the candidates as the lines for step 2 of the file of your variant give." (`build_table.md`) | Taking candidates from the other variant's headings (for example "Success" in a task document) |
| "Write the table where, and with the row states, those lines give." (`build_table.md`) | Writing the table into the definition in task mode, or under "Settlements to record" in the definition variant |
| "No search of the whole foundation runs here; those lines say who makes it." (`build_table.md`) | A search of the whole foundation by this skill in either variant (WAY-33, WAY-118) - the base sentence, with the clause on who makes it moved to the variant |
| "`define-project` makes the one search of the whole foundation at the readiness gate, once every entry is written (WAY-118)." (`definition_variant.md`) | The base clause "For a project definition, ..." without its "for a task" half |
| "The task's cycle makes the one search of the whole foundation when it writes each kept row (WAY-33, WAY-134)." (`task_variant.md`) | The other half of the same base clause |
| Task Step 2: "proposed rows start `waiting`, and rows with no concrete next-reader consequence start `rejected`. Show the whole table, including the source and next-reader column, with a reason for each rejected row." (`task_variant.md`) | Showing the task's table partly, starting its rows in another state, or leaving out the reason of a rejected row - what the base reached by "as above" (acceptance criterion 3) |
| The one-sentence introductions and the headings "Step N - ..." of the variant files, and the title and first line of `read.md` and `build_table.md` | Nothing in a rule; they name the file's variant and steps so that an agent that opens it by path recognises it |
| "Step 4 - in place of row by row", the opening "An accepted row stays a row, ..." and "In place of step 4, a row that carries a choice ..." (`task_variant.md`) | Row-by-row hand-over in task mode: the base said "this step does not run" in the same paragraph; that sentence now stands once, in `SKILL.md` step 4 |

Dropped without replacement, each judged to carry no rule: "and the differences below each step name what changes" (base line 33-34), replaced by the files' own structure; the labels "For a project definition," and "For a task," on lines that moved into a variant file.

## Reach beyond the dispatch (section 1)

- `agent-instructions/README.md`: `AGENTS.md` of the repository asks to read it before work on the-way itself.
- `instruction-files/tool_loading.md`, `judging.md`, `kind_skill.md`, `changing.md`: the method the handoff names (`instruction-files/SKILL.md`) has them read.
- `project-level/task/template.md` lines 78-90 and 178-212 and `project-level/definition_template.md` lines 255-350, to count the sections the task names and to place the reading of each (the dispatch names the entries to read, not these files).
- `project-level/plan/skill/SKILL.md` and `read.md`, `project-level/task/skill/SKILL.md`, and `git log` of the series, to see how earlier rebuilt skills name step and variant files (conventions of pointers).
- `foundations/decisions.md` WAY-09, WAY-35 and the other entries the handoff names were read whole; no entry outside the handoff was needed.

## Searches not found or unclear

1. The task states 424 words for the task template's section "Settlements to record" with its rule (Context, and question 4). I found no reading of "the section with its rule" that gives 424: the section's own lines 80-87 hold 60 words and the rule's bullet under "What each section carries" 345, 405 together; 424 equals lines 181-208, the rule's bullet, the bullet "Out of scope" and the paragraph below it, without the section's own lines. I counted 405 and said so in `word-counts.md`; the request should state 405, or the human should confirm 424.
2. Question 4 gives the sum 3 only for task mode; I gave the definition route two sums and no third.
3. Session records: not opened (not asked of me beyond the task's own figures); the assessment names the ground of each move as the cost the task measured, not a mistake found in records.
4. No test, gate test or script names `elements/common/skill/` files beyond `installation/install.py:30` (the path of `SKILL.md`, unchanged); I found no behaviour test to extend.
5. Unclear in the base, not resolved by me: line 36-37 resumes "for a task, from the first row still `waiting`" - the states of a task table are `waiting` and `rejected`, and the accepted state is not named in this skill (the template has it). I kept the sentence as written.

## Choices made

- The variant file is read once at step 1 and holds the lines for steps 1, 2, 4 and 5 (question 1 of the task, which names its weak point: the definition variant carries the step-4 procedure from step 1). Rejected: one file per step and variant. Cost if wrong: the definition agent carries the step-4 procedure from step 1, in a variant the task measured at about 1 use in 108.
- A caller table in `SKILL.md` that holds the callers' own words. Rejected: a pointer at each step only (an agent that opens `SKILL.md` by path would not know which of two files is its own). Cost if wrong: the table's words in `SKILL.md`, read by both variants.
- The resume rule stays in `SKILL.md` as one sentence for both variants. Rejected: one half in each variant file, because the agent needs it before it has read its variant. Cost if wrong: the half of the sentence the other variant does not use.
- Step 3 stays in `SKILL.md` (question 1).
- "this step does not run" stays once, in `SKILL.md` step 4 - it is one instruction (WAY-256 exception) - and `task_variant.md` does not repeat it. Cost if wrong: a task agent that opens `task_variant.md` alone would not see the sentence; it is a file read after `SKILL.md`.
- The row-structure bullet is kept as the base wrote it, "or a section of the definition" included, in `build_table.md`. Rejected: rewording it now, because it changes a rule's text (proposal 2). Cost if wrong: three words of the definition on the task route.
- `read.md` and `build_table.md` as names, after `read.md`, `cut_tasks.md` and `draft.md` of the other rebuilt skills.
- Nothing proposed is applied. Four proposals in `assessment.md`: reading three sections of `way_of_working.md` in task mode, rewording "a section of the definition", removing the sentence on future callers, moving the reading of `projected_mode.md` to step 4 (not recommended).

## Problems as observed

- The first draft of the five files was longer than the estimate of question 1 on both routes; I cut the introductions of the files and shortened the table in `SKILL.md`. No rule was cut: the 5-word window check showed the same places before and after the cut.
- `verify_counts.py` prints a note, not a failure, for the 424 (item 1 above).

## The weakest point of the work

An agent that opens `SKILL.md` by its path and meets a caller phrase that is neither "task mode", "Settlements to record" nor "Projected foundation changes", for example a caller that says only "for a project definition", must still infer the variant. The table's first row names "a project definition" as the source, so the phrase maps, but a caller whose words do not match either row has no rule - as on the base. Check made: `route_check.py` checks the words of the six caller files named by the task and finds each in `SKILL.md`; I did not run an agent through the skill, so the recognition by an agent is argued, not measured.

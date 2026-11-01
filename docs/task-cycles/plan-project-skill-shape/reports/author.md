# Author report - plan-project in the WAY-256 shape

**Status:** done with concerns (the concerns are in "Concerns" below; none blocks).

Branch `task/plan-project-skill-shape`, base 2f51e6c. Worktree clean after the commit.

## Commits

- `db3845c` Split plan-project into a picture of the whole and a file for each step and variant (WAY-256) - author address `mariusznn@gmail.com` (`git log --format='%h %ae'`).

## Files changed

In `C:/Storage/repos/the-way/.runs/worktrees/plan-project-skill-shape/project-level/plan/skill/`:

| File | Words | What it holds |
|---|---|---|
| `SKILL.md` | 623 | frontmatter (unchanged), intro, location, the pointer under the heading "Delegated work while leading a plan", "Rules that hold across the steps", steps 0-7 as headings with pointers |
| `delegated_mode.md` | 277 | lines 25-46 of the base, unchanged |
| `existing_plan.md` | 185 | step 0 work on an existing plan (base 52-61), with pointers to the reading file, `assign_entries.md`, `hand_over.md` and the sentence that has `read.md` read |
| `read.md` | 141 | step 1 |
| `reading_definition_and_plan.md` | 291 | the reading section minus lines 81-83 and 105-106 |
| `cut_tasks.md` | 267 | step 2 and the pointer to `guideline_tasks.md` |
| `guideline_tasks.md` | 176 | base lines 115-127 |
| `assign_entries.md` | 213 | step 3 |
| `place_questions.md` | 165 | step 4 |
| `write_and_check.md` | 254 | step 5 and the list of what steps 2-4 send here |
| `critique_plan.md` | 242 | step 6 |
| `hand_over.md` | 211 | step 7 |

Also `C:/Storage/repos/the-way/.runs/worktrees/plan-project-skill-shape/project-level/lead/skill/SKILL.md` (one sentence, lines 30-31, now points to `project-level/plan/skill/reading_definition_and_plan.md`). The frontmatter description is unchanged; no Python changed. 13 files, all Markdown, LF. (`wc -w` of the files after the final pointer clauses; the exact figures are in `word-counts.md`.)

The sum of all twelve files is 3045 words against 2344 in the base: reading everything costs +701 (+30%).

## Materials

- `C:/Storage/repos/the-way/.runs/worktrees/plan-project-skill-shape/.runs/task-cycles/plan-project-skill-shape/reports/assessment.md` - 34 rows, every nonblank line of the base in exactly one row (the builder checks coverage and overlap), sections in the order of `judging.md`, verdicts keep and move only, 6 proposals listed at the end (proposals 2-5 are the repetitions with `template.md`), and a list of each added sentence with what it switches off.
- `C:/Storage/repos/the-way/.runs/worktrees/plan-project-skill-shape/.runs/task-cycles/plan-project-skill-shape/reports/word-counts.md` - the seven routes (5 in two versions), before and after, each file with its count, the reading of each route stated, comparison with the task's estimates.
- Helpers under `.../tools/`: `compare_sentences.py` (sentence comparison, output in `reports/sentence_diff.txt`), `make_assessment.py` (builds the table, checks coverage and the declared places), `word_counts.py` (builds `word-counts.md`), `verify_counts.py` (compares every figure with the files: 271 figures, 0 differ, exit 0, run after the last change of a counted file). The old `example_*.py` were not used.

## Word counts against the task's estimates (skill text alone)

| Route | Before | After | Estimate of the task |
|---|---|---|---|
| 1 fresh breakdown, nothing found | 2344 | 2407 | 2300-2900: inside |
| 2 fresh breakdown with the guidelines file | 2344 | 2583 | 2300-2900: inside |
| 5a narrow turn, own steps | 2344 | 1984 | 1800-2000 (corrected): inside |
| 5b narrow turn, reads everything | 2344 | 3045 | 2800-3250: inside |
| 7 recheck after the gate | 2344 | 2869 | 2800-3250: inside |
| 6 hand over alone | 2344 | 1728 | none for one step; below the narrow-turn range |

Outside the "-15% to +25%" of question 4's not-chosen way: route 6 (-26.3%) and route 5b (+29.9%). With the files read beside the skill, totals change by -10.5% to +9.4%. The task's own figures (2344, 1881, 208) agree with my count; no figure of the task had to be bent. The task expected about 170 words for the file of step 1; it is 141.

## The judgement and the choices

Each choice with the way not taken:

1. **One file per step (steps 1-7) and four variant files**, as the sibling `project-level/task/skill/` does. Not taken: grouping steps 3-4 in one file (the word saving is small and the two steps have different pointers and different questions to step 5), or keeping steps 5-7 in `SKILL.md` (each is several instructions, not one).
2. **Step 0's first bullet (template and "How a skill asks") and "Otherwise begin with step 1" stay in `SKILL.md`**: one instruction each; moving them trades one instruction for one pointer (WAY-256 exception).
3. **Lines 81-83 and 105-106 stay in `SKILL.md`** under "Rules that hold across the steps", as the task says. Not taken: keeping lines 102-104 ("Expand whenever ...", "Before a resumed edit ...") there too. I judged them a reading procedure that the session holds before any step 2-4 edit, because a resume or correction reads the reading file at step 0 and a fresh breakdown reads it at step 1. This is the boundary judgement WAY-256 leaves to the table; it is my weakest placement (see Concerns).
4. **The condition of the step 0 pointer** says "When an existing plan is named, by the human or in a dispatched turn by its conversation file". The base said "When the human names an existing plan". Not taken: the literal base wording, which would leave a dispatched turn (11 of the 14 recorded uses) without the file although the section "Delegated work" (bullets 1 and 4) presupposes the existing-plan bullet. By what it selects, the new wording selects the same turns the base sent through the bullet; it is the one wording I ask the reviewer to confirm. Cost if wrong: a dispatched turn reads `existing_plan.md` that a reading of the base would not have made it read - a read, not a rule lost.
5. **A fragment needed in more than one place, placed by its kind.** The three cases of the task: (a) the questions to the human of steps 2-4 are stated again in `write_and_check.md` as the list "What steps 2-4 send here" (rewordings that keep the meaning), the originals staying at their steps; (b) the finding of `plan_check.py` about two tasks on one entry stands in `existing_plan.md`, `assign_entries.md` and `hand_over.md`; (c) "A new complete breakdown processes every scope item ..." stays in `SKILL.md` for steps 2-4. Not taken: moving the sentences out of steps 2-4 files to step 5 only (the agent meets the moment at the step).
6. **The delegated file reaches steps 5-7** by a first sentence in `write_and_check.md`, `critique_plan.md` and `hand_over.md` ("ask nothing of the human yourself", "do not run `critique` yourself", "show the human nothing yourself") and by a clause in the pointers of steps 5-7 in `SKILL.md` (WAY-265). Not taken: one sentence in the delegated file (the file is read once at the start and the step files are read later without a mention of it).
7. **Variant condition for `guideline_tasks.md`**: "found a styleguide, general coding file or testing guidelines missing or uncertain, or the approved scope has a task create the first file of a kind of code, work on a kind that has files but no entry in the guidelines index, make the first test of a level, or extend existing guidelines". It covers the five matters of lines 115-127. The extra word "uncertain" selects the file in a case the bullet did not name (the reading kept "missing or uncertain" in the working evidence); cost: an unneeded read of 176 words, no rule lost.
8. **No `Settlements to record`, no foundation entry written.** An entry I found that no longer matches: none.
9. **Names of the files** are mine: `delegated_mode.md`, `existing_plan.md`, `read.md`, `reading_definition_and_plan.md` (the name carries the old section title so that the reference in `lead-project` names what it reads), `cut_tasks.md`, `guideline_tasks.md`, `assign_entries.md`, `place_questions.md`, `write_and_check.md`, `critique_plan.md`, `hand_over.md`.
10. **Route readings** for the word counts (task question 4 leaves them to the author): route 3 runs steps 0, 5, 6, 7 and reads the file of step 1 but not its foundation and guidelines; route 4 runs 0, 1, 2, 3, 5, 6, 7 without step 4; routes 5-7 are dispatched turns that request the critique and do not read the critique files; route 5a runs steps 0, 1, 3, 5. The definition of each is the first line under every route in `word-counts.md`. Not taken: counting step 4 on route 4 (words of `place_questions.md` come on top where a question moves).

## Own-work check (weakest point: rule preservation)

- **Sentence comparison** (`tools/compare_sentences.py`, whitespace normalised, list markers and headings dropped, output `reports/sentence_diff.txt`): 3 base sentences are not verbatim in the rebuilt files. Each is a pointer reworded: (1) "When the human names an existing plan, run `plan_check.py` ... and read it by \"Reading the definition and plan\" below (WAY-151)." - now the condition stands in the `SKILL.md` step 0 pointer and the sentence in `existing_plan.md` points to the reading file; (2) "A finding that two tasks realize one entry with no order ... as step 3 gives it, ... as step 7 gives it (WAY-230)." - now with the file names; (3) "Read the definition by \"Reading the definition and plan\" below (WAY-151)." - now with the file name. Every other base sentence stands verbatim in some file. The sentences new to the files are the pointers, the three openers, the list in `write_and_check.md`, the two bullets about two tasks, the sentence in `existing_plan.md` that has `read.md` read, and the first sentence of the reading file; each is accounted for with what it switches off in the last section of `assessment.md`.
- **What the new sentences switch off** (the comparison cannot see this) - read one by one: the openers of steps 5-7 switch off asking the human, running `critique`, and showing the human, for a dispatched turn only, which the base's section "Delegated work" did; the step 2 condition switches off `guideline_tasks.md` only for a breakdown with none of the five matters; "each unless step 0 had you read it" switches off a second reading only. The sentence in `existing_plan.md` that has `read.md` read adds a read for a draft resume that formerly happened by having read the whole file.
- **Quotes of `assessment.md` against the base, line coverage:** `make_assessment.py` cuts each quote from `git show 2f51e6c:...` and fails on a nonblank line in no row or in two rows; it reported 34 rows and no coverage error. It also compares each row's declared places with the files: one report, for lines 102-104, is the artefact of the line ending mid-sentence ("A new complete" begins the next sentence); the row says so.
- **Each route's sum** is added by `verify_counts.py` from the file lines: 271 figures compared, 0 differ, exit 0 (run after the last change of a counted file; the commit changed none after).
- **Hand walk of the seven routes** (an agent from `SKILL.md` to the file of the last step). Each route reads `SKILL.md` first (623 words).
  1. Fresh breakdown, nothing found: step 0 reads the template and "How a skill asks" and, no plan named, goes on; step 1 reads `read.md` and the reading file; step 2 reads `cut_tasks.md`, whose guidelines condition does not hold; 3, 4, 5 read their files; step 6 reads `critique_plan.md` and runs `critique`; step 7 reads `hand_over.md`. Falls away: `delegated_mode.md`, `existing_plan.md`, `guideline_tasks.md`. Stays: all rules of working, in `SKILL.md`.
  2. Same plus `guideline_tasks.md` at step 2, named in `SKILL.md` and in `cut_tasks.md` with the same condition; its sentence "Follow step 5 for questions or work beyond the approved definition" reaches step 5 through the list "from step 2" in `write_and_check.md`.
  3. Resume of a draft from step 5: step 0 reads the template, names the plan, reads `existing_plan.md` and the reading file; the draft goes on from the first unfinished step (step 5); the last bullet of `existing_plan.md` has the session read `read.md`; step 5 reads `write_and_check.md` and finds there the questions of steps 2-4 it did not read; step 6 and step 7 as usual. Falls away: `cut_tasks.md`, `assign_entries.md`, `place_questions.md`, `delegated_mode.md`; the finding of `plan_check.py` about two tasks reaches it through `existing_plan.md` and `hand_over.md`, and the file `assign_entries.md` is named there for the settlement.
  4. Human's correction (a split): as 3, plus `read.md` run at step 1 (the foundation and the guidelines are read), `cut_tasks.md` and `assign_entries.md`; `place_questions.md` only if a question moves. The critique is run (`critique_plan.md`). Falls away: `delegated_mode.md`, `guideline_tasks.md` unless its condition holds.
  5a. Dispatched narrow turn, own steps: `SKILL.md` Delegated pointer, `delegated_mode.md` first (with `conversation_template.md`), step 0 reads `existing_plan.md` and the reading file by the widened condition, `read.md`, `assign_entries.md`, `write_and_check.md` whose opener returns questions through the conversation. Falls away: the cutting, question-placing, critique and hand over files.
  5b. The same turn reading everything: adds the files of steps 2, 4, 6, 7 and `guideline_tasks.md`; nothing runs the critique because `critique_plan.md`'s opener switches it off.
  6. Hand over alone: `delegated_mode.md`, step 0 files, `read.md` (sentence of `existing_plan.md`), `hand_over.md` whose opener and last sentence return the material through the conversation.
  7. Recheck after the gate: `delegated_mode.md`, step 0 files, `read.md`, `cut_tasks.md`, `assign_entries.md`, `place_questions.md`, `write_and_check.md`, `critique_plan.md`, `hand_over.md`; the fourth bullet of `delegated_mode.md` starts at step 0, which reaches the existing-plan file.
- **Incoming references:** step numbers 0-7 unchanged; the heading "Delegated work while leading a plan" stays in `SKILL.md`; the sentence in `project-level/lead/skill/SKILL.md:30-31` names `reading_definition_and_plan.md`; `project-level/lead/skill/SKILL.md:214`, `project-level/skill/SKILL.md:49` ("step 0") and WAY-156 stand. `git grep` found no other reference to a section of this skill.

## Checks

All run in the worktree on commit `db3845c`, after the last change of a counted file; none failed.

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` | 0 | 0 errors |
| `python -B instruction-files/check_instructions.py .` | 0 | 0 error, 1 warn, 3 info; the same as on the base exported from 2f51e6c (the dead-path warning on `AGENTS.md:21` for `_zadania\` stands on the base) |
| `python -B agent-instructions/skill_entry_points.py --write` | 0 | "entry points are current"; it changed nothing (`git status` clean afterwards) |
| `python -B gate/run_tests.py agent-instructions` | 0 | 18 tests OK |
| `python -B gate/run_tests.py installation` | 0 | 44 tests OK |
| `python -B gate/run_tests.py project-level` | 0 | 268 tests OK |
| `python -B .runs/task-cycles/plan-project-skill-shape/tools/verify_counts.py reports/word-counts.md` | 0 | 271 figures, 0 differ |
| `python -B .runs/task-cycles/plan-project-skill-shape/tools/compare_sentences.py reports/sentence_diff.txt` | 0 | 3 base sentences differ (pointers) |
| `python -B .runs/task-cycles/plan-project-skill-shape/tools/make_assessment.py` | 0 | 34 rows, one report that is the mid-sentence artefact of lines 102-104 |

The whole gate was not run (the orchestrator's). No test was written first: only Markdown changed, and the tests of the skill's shape are those above. Output of the last run: `reports/final_checks.txt`.

## Reach beyond the handoff

- None beyond the handoff's list. Decisions read whole for this: WAY-150, WAY-151, WAY-152, WAY-156, WAY-200, WAY-218, WAY-230, WAY-242, WAY-247, WAY-256, WAY-265, WAY-266 (the quotes of the task's *Decisions in play* supplied WAY-257, WAY-145, WAY-146, WAY-143, WAY-120, WAY-113, WAY-106, WAY-127 and WAY-259). Not read whole: WAY-13, WAY-35, WAY-125, WAY-126, WAY-142, WAY-144, WAY-147 and the rest of the handoff's list; I relied on the sentences the skill cites them for. The part map, the six invariants, the environment fact `claude-skill-nested-references` and the glossary were not read whole: the change moves text between Markdown files and touches no script, check or entry point (the check of the entry points and the tests of `project-level` report no change). `instruction-files/SKILL.md`, `judging.md`, `kind_skill.md` and `task-cycle/change/SKILL.md` were read whole.

## Concerns

1. **Lines 102-104** ("Expand whenever ...", "Before a resumed edit ...") stand in the reading file, not in `SKILL.md`. If the reviewer judges them a rule of working kept during steps 2-4, they move to "Rules that hold across the steps" (about 55 words).
2. **The widened condition of the step 0 pointer** (choice 4).
3. **Does "reads `read.md` before it goes on" mean that the session also performs step 1?** The task's wording is "reads it before it goes on" and its cost of 170 words counts the file only; the file's bullets are instructions (run `readiness_check.py`, read the foundation), so a session that follows them does step 1. The base did not make a draft resume run step 1. I kept the task's wording and counted the file only; the sentence of `existing_plan.md` and the route notes of `word-counts.md` say so.
4. The restatements (the list in `write_and_check.md`, the finding about two tasks in three files, the opener in each of steps 5-7) are repeated text that must be changed together; proposals 5 and the repetition with the template stand in `assessment.md`.
5. The real figure for reading everything is +701 words (+30% of the skill text), inside the task's 450-900 range.

## Searches not found or unclear

- `gh pr view 51 --comments` returned nothing (no output); remarks of PR #51 were not read. The grep of the other six PRs found no remark about `plan-project`, its section names or its file path (only PR #50 names `task-cycle/plan/SKILL.md`, a different file). Mistake grounds in the table therefore read "not found in the records searched".
- No session record was searched for the mistakes (the handoff names the git history, PR remarks and the task's Context; I did not open the Claude Code or Codex records).
- The task does not say whether the dispatched turns of route 5 run step 1; I counted them as running it (concern in the route readings).
- The task does not fix the readings of routes 3, 4, 6 and 7; the readings are mine and stated.

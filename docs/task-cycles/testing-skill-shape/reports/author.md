# Author report - maintain-testing-guidelines in the WAY-256 shape

> Repair note: this report was renumbered after the repair (see `author-repair.md`): the first entry of the rebuild, row 1, is written into WAY-256 in place; the variant-file entry is WAY-265 and the session entry WAY-266. Citations of "WAY-256" that stood for the old WAY-265 now read WAY-256; the commit message of `1c66173` still uses the old numbers, and choices 7 and 8 below describe the old form and are superseded by the repair.

**Status:** done with concerns (concerns: the foundation reading was partial, see "Reach"; two open points under "Concerns").

## Commits (branch `task/testing-skill-shape`, base 00c0a74; author address `mariusznn@gmail.com` verified with `git log --format='%h %ae'`)

- `1c66173` docs: record where skill fragments needed by some steps stand and what a guideline skill session reads first - `foundations/decisions.md` (WAY-256, WAY-265, WAY-266), `instruction-files/kind_skill.md` (third answer), `product-guidelines/styleguide/SKILL.md` (the step 0 sentence).
- `d024d56` docs: rebuild maintain-testing-guidelines in the WAY-256 shape - `product-guidelines/testing/SKILL.md` and ten new files beside it.

Not pushed, no request opened. The worktree is clean (`git status --short` empty; `.runs/` is ignored).

## Files changed

| File | Added / removed lines |
|---|---|
| `C:/Storage/repos/the-way/.runs/worktrees/testing-skill-shape/product-guidelines/testing/SKILL.md` | rewritten (3042 -> 1161 words) |
| new: `audit.md` (230 words), `hand_back.md` (73), `new_level.md` (98), `new_tools.md` (69), `orchestrated_mode.md` (98), `recognize.md` (422), `research.md` (232), `settle.md` (618), `starting_set.md` (143), `task_document.md` (364), all in `product-guidelines/testing/` | new |
| `C:/Storage/repos/the-way/.runs/worktrees/testing-skill-shape/instruction-files/kind_skill.md` | +7 / -2 (see `git show --stat 1c66173`) |
| `C:/Storage/repos/the-way/.runs/worktrees/testing-skill-shape/product-guidelines/styleguide/SKILL.md` | +2 / -1 (the sentence only) |
| `C:/Storage/repos/the-way/.runs/worktrees/testing-skill-shape/foundations/decisions.md` | +about 85 (three entries) |

Totals: `git diff --stat 00c0a74 HEAD` gives the exact figures. No Python changed.

## Materials

- `C:/Storage/repos/the-way/.runs/worktrees/testing-skill-shape/.runs/task-cycles/testing-skill-shape/reports/assessment.md` (44 rows, 235 nonblank lines covered once each, 46 quotes verified literal against 00c0a74, the Question 3 row, the list of text added that no base line carries, two proposals P1 and P2, check-script output before and after, contradictions before and after).
- `C:/Storage/repos/the-way/.runs/worktrees/testing-skill-shape/.runs/task-cycles/testing-skill-shape/reports/word-counts.md` (six routes, before and after, three figures each, file lists).
- `C:/Storage/repos/the-way/.runs/worktrees/testing-skill-shape/.runs/task-cycles/testing-skill-shape/reports/sentence-diff.txt` (the sentence comparison).
- Helpers, all under `.../tools/`: `make_assessment.py`, `word_counts.py`, `compare_sentences.py`, `verify_reports.py` (adapted from the `example_*.py` of the earlier skill; the paths, base commit and file lists were rewritten and the output checked by `verify_reports.py` and by hand, not taken on trust).

## Word counts (details and file lists in `word-counts.md`)

| Route | Before: to step 4 / total | After: to step 4 / total | Total change |
|---|---|---|---|
| 1 first guidelines, no tests, no preference (research runs) | 14120 / 14120 | 8801 / 11246 | -20.4% |
| 2 same, with a preference (no research) | 13611 / 14120 | 7738 / 11014 | -22.0% |
| 3 tests, no guidelines, no preference; also extension (research, audit) | 14120 / 14120 | 9031 / 11476 | -18.7% |
| 4 refresh (no research, audit) | 13611 / 14120 | 7968 / 11244 | -20.4% |
| 5 "A new level", recipe standing, no step 2 | 13611 / 14120 | 7693 / 10969 | -22.3% |
| 6 orchestrated mode on route 1 | 14120 / 14120 | 8899 / 11344 | -19.7% |

All include the first reading in `refine-task` (2835 words); the figures without it are in the file. Difference with the task's figures: every figure of the task that I could count agrees (2835, 1336, 3187, 54, 322, 509, 396, 1739, 208, 492; `SKILL.md` 3042). The task's estimates were "about 14 100" before (counted 14 120) and "11 100-11 800" total and "7600-9000" to step 4 after (counted 10 969-11 476 and 7 693-9 031): route 5 total is about 130 words below the estimate's low end and route 3 to step 4 about 30 above its high end. Not bent.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` - exit 0, "0 errors" (run after the entries were written).
- `python -B instruction-files/check_instructions.py .` - exit 0, "0 error, 1 warn, 3 info"; the output is identical to the base (checked with `diff` against the same command on an export of 00c0a74); the one warning is the dead path `_zadania\` on `AGENTS.md:21`, which stands on the base.
- `python -B agent-instructions/skill_entry_points.py --write` - exit 0, "entry points are current"; it changed nothing (the description is unchanged).
- `python -B gate/run_tests.py agent-instructions` - exit 0, 18 tests OK.
- Not asked, run for safety: `python -B -m unittest installation.test_testing_guidelines_installation` (2 tests OK), `instruction-files.test_check_instructions` (104 tests OK, 5 skipped), `gate.test_skills_reach_the_way_sessions` (2 tests OK). The whole gate was not run.
- `python -I -B .../tools/verify_reports.py` - quotes 46, mismatches 0, overlaps none, missing nonblank lines none, route sums consistent (21 sections), no named path missing.
- No test was written first and no invariant's test changed: only Markdown and a foundation log changed, and no new invariant was called for.

## Own-work check (the weakest point: rule preservation)

Requirement: no rule disappears or changes meaning. Check: `compare_sentences.py` compares the base `SKILL.md` with the eleven rebuilt files sentence by sentence (whitespace normalised, list markers and headings dropped, split also after `;` and `:`). Result: 17 base fragments are not verbatim in the new files, and every one is accounted for:

- 1 reworded: "reads only the document" -> "reads only the task document" (meaning-preserving; the heading that gave "document" its referent moved).
- 5 removed as a second reading (the frozen task's To do 2): the clauses of step 0 reading both templates, `project-level/task/skill/SKILL.md`, `project-level/task/template.md`, the section "How a skill asks" - the first two templates moved to steps 2, 3, 4; the task skill, task template and "How a skill asks" are not read again; plus the clause "`elements/common/critique/SKILL.md`", which moved to the first critique.
- 2 moved to step 1 with the wording changed to "that refine-task did not read" (root `AGENTS.md` and `guidelines/`, then the foundation clause without "by Reading the foundation", which refine-task already did).
- 2 about the mode of a new level (`:120`), reworded to say what `product-guidelines/reading.md:77-78` says (see Choices, 3).
- 2 where the research bullet was cut at the semicolon: its condition and the refresh clause stand in `starting_set.md` with a pointer to `research.md` added.
- 1 "Where research ran, give one fresh agent..." -> "Once the reports are in, ..." plus the pointer "Before the first critique of the session, read `elements/common/critique/SKILL.md`".
- 1 label "**A new level.**" and 1 label "**New tools.**" dropped where the file title replaces them; 1 the step 4 clause "a new level of \"A new level\"" -> "of step 3 (`new_level.md`)"; 1 "**Critique.** ... as \"Critique before collective review\" gives" -> with the file named and the reading pointer; 1 step 5 "what \"What reaches the task document\" names" -> "what `task_document.md` beside this skill names".

No sentence is lost; the other direction (new sentences that are not in the base) is the pointers, the step 0 sentence and the additions listed in `assessment.md` under "Text added that no base line carries". The test of "the check found what it should": the helper reports the 17 above, and I read each of them against the new files.

Second check, walks (done by hand from `SKILL.md` to the last step's file; presence of a text was not the test, the order and condition were):

1. First guidelines, no tests, no preference: `SKILL.md` whole (rules, step 0 sentence); step 1 `recognize.md` (parts named first, then root `AGENTS.md`/`guidelines/`/foundation additions, then what the product has, then the mode "no tests"); step 2 the testing template, then `starting_set.md` (preference question, "How to show" pointer), no preference -> `research.md`, first critique -> `critique/SKILL.md` -> `prepare.md`, `check.md`, `settle.md`; step 3 "Otherwise there is no step 3" (no tests, no new level); step 4 `product-guidelines/template.md`, testing template not read again, `settle.md`, `task_document.md`; the critique clause reads the section "Critique before collective review", `critique/SKILL.md` not again; step 5 `hand_back.md`, `task_document.md` not again.
2. Same with a preference: `starting_set.md` keeps the preference question; the condition of its second bullet (no preference, or an extension) is false, so `research.md` is not read. Step 4's critique then reads `critique/SKILL.md` (and its three files) for the first time.
3. Tests, no guidelines (or an extension): as 1 plus step 3 `audit.md` (testing template already read at step 2).
4. Refresh: step 2 `starting_set.md` ("At a refresh, do no research"), step 3 `audit.md`, step 4 first critique reads `critique/SKILL.md`.
5. "A new level", recipe standing: `SKILL.md`, `recognize.md` (mode: new-level case, no step 2), step 3 testing template + `new_level.md` (no `audit.md`, since step 1 gave no audit), step 4, step 5; `research.md` and `starting_set.md` never read. Where the recipe does not stand, the same step 1 sends the agent through step 2.
6. Orchestrated: route 1 plus `orchestrated_mode.md` read before step 1.

## Choices (way taken, way not taken, cost if wrong)

1. **Names and grouping of files** (yours to choose): the styleguide's eleven-file shape with testing names (`starting_set.md` for `starting_rules.md`; `new_level.md` as a variant file of its own). Not taken: one file for steps 2 and 3 (they carry different conditions); cost if wrong: a file more or less.
2. **"How to show" and "Write each answer" stay in `SKILL.md`** under "Rules that hold across the steps", as rules of working that steps 1, 2 and 4 keep (task Question 2, WAY-256). Not taken: `how_to_show.md` named by steps 2 and 4 (about 130 words fewer in `SKILL.md`, but it is a rule the agent keeps, and the pointer would be an instruction too). Cost if wrong: about 130 words carried through steps that do not ask.
3. **The new-level mode (`:120`) reworded**: a level whose recipe stands with an empty *Exemplar* takes the new-level case and no step 2; a level with no recipe is an extension and takes step 2 as well (task To do 3, `product-guidelines/reading.md:77-78`); the case also covers "tests at a level its cycle chooses", because the base sentence on that case stood in the same fragment. Not taken: leaving "the first test of a level" as is (the route of acceptance criterion 5 then has no stated way to skip step 2). Cost if wrong: an agent on a level with no recipe skips step 2 - guarded by the explicit extension clause.
4. **Reading of the foundation additions and the trust boundaries at step 1** (second bullet, after the parts are named, WAY-248 order kept). Not taken: boundaries at step 3 only (step 4 needs them on every route, the new-level route included).
5. **`product-guidelines/template.md` read at step 4**, as in the styleguide skill (it is a template of the form of every file; step 2 of this skill does not use it). Not taken: step 2. Cost if wrong: the starting set drafted without the general form, caught at step 4.
6. **Step 3 pointer** names both files directly and separately (audit when step 1 gave the audit; new level when the outcome is a first test or the level is the cycle's choice), so neither agent reads the other's file (acceptance criterion 5). Not taken: `audit.md` pointing on to `new_level.md` (then the new-level agent would read the audit first).
7. **Entries as three new decisions, not an edit of WAY-256**: row 1 is written as WAY-256 (derives from WAY-256; "Fragments that stand unchanged are not bound" repeated), row 2 as WAY-265 (based on `claude-skill-nested-references`), row 3 as WAY-266. Reason: Question 8 says WAY-256 does not change, and a new entry leaves its binding sentences as approved. Not taken: adding the case into WAY-256 (changes an approved decision, WAY-30). Cost if wrong: the human reads row 1 as an extension of WAY-256 and asks for the edit; the third answer in `kind_skill.md` then cites WAY-256 only.
8. **WAY-266 carries the clause "Skills of guidelines whose text stands unchanged are not bound by it until they are rebuilt"** (not in the row; my wording of the meaning of "task 8 will repeat it"). Without it the coding skill would breach the entry on the day of the merge. Cost if wrong: the human wanted the entry to bind all three skills at once; drop the clause.
9. **The *Rejected* of the three entries** keep the ways not chosen from the Not chosen lists of Questions 2, 3 and 4 without their word counts (WAY-134, the template forbids counts in author-written prose); the first-listed way of Question 3 ("two levels as in task 4") is worded as the layout where SKILL.md names only the step's file, which is my reading of that line (concern below).

## Reach beyond the handoff

- None beyond the foundation list, but the reading of that list was partial: I read WAY-01 to WAY-171 of the list as binding sentences, relations and *Verification* (not *Rationale*/*Rejected*), and of WAY-172 onward only WAY-213, 214, 215, 217, 242, 244 and 251 (plus WAY-256 to WAY-259 and WAY-264 whole, and the ends of WAY-260 to WAY-262). I did not read the other listed decisions, the invariants (except to know the names), the glossary or the part map beyond the `product-guidelines` entry's *Files* pattern. The checks (foundation_check, check_instructions, entry-points test) pass, but a reviewer should treat the foundation reading as incomplete.
- Read for the work beyond the list: `product-guidelines/styleguide/*.md` (the shape), `instruction-files/SKILL.md`, `judging.md`, `kind_skill.md`, `elements/decisions/skill/*.md` and `elements/decisions/template.md` (the entries), `project-level/task/skill/SKILL.md` and `read_sources.md`, `product-guidelines/reading.md`, `elements/common/critique/*.md`, `elements/common/way_of_working.md` headings.

## Concerns

- The sentence in `new_level.md` "the level's recipe comes into being with it" stands as in the base but is true only for a level with no recipe; on the route with a recipe standing it reads as if the recipe were written again. Proposal P2 in the assessment, not applied.
- The *Rejected* of WAY-265 renders "two levels as in task 4" as "the variant named only in the step's file". The task's own wording is ambiguous (in the styleguide skill the step file already points to its variant file; only SKILL.md does not name it). If the human meant something else, that line is the one to correct.
- Step 2's heading pointer "which step 1 gives for tests with no testing guidelines yet and for a refresh or an extension" is long; it names the moment as step 1 gives it, which the walks need.
- Recognition after the move: `SKILL.md` step 1 reads only `recognize.md`; a session that skips the "Name the parts" bullet and reads only the second would still pass every check - an inherent limit of any file-split.

## Searches not found or unclear

- No remark of PRs #50, #51, #52, #59 or #60 (their comments, reviews and inline comments, read by `gh pr view <n> --comments` and `gh api`) mentions this skill; #51 has no comment. No mistake that a fragment of this skill was added for was found in the five commits of its history (judged from their messages and the PRs; I did not read the five diffs line by line).
- `rg`-style search for incoming references to sections of this skill (`What reaches the task document`, `A new level`, `Starting set`, `Orchestrated mode`) found them only inside this skill and in `product-guidelines/coding/SKILL.md`, which has its own sections of the same names (not touched). `product-guidelines/reading.md:79`, `testing/template.md:7`/`:105`, `project-level/task/skill/guideline_findings.md`, `project-level/plan/skill/SKILL.md:122` and `installation/*` name the skill, not a section.
- The task text "`product-guidelines/testing/SKILL.md:53-54`" (the name "Writing the file") is the template's section; it stands in `task_document.md` unchanged and the template's `## Writing the file` exists (`template.md:264`).
- Unclear: whether row 1 should extend WAY-256 itself (choice 7); what "two levels as in task 4" in Question 3 means exactly (concern 2).
- Nothing else was looked for and not found.

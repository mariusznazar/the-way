# Report of the one author - coding-skill-shape

**Status:** done with concerns (concerns below; none blocks).

**Commit:** `097123e` on `task/coding-skill-shape` (author address `mariusznn@gmail.com` checked with
`git log --format='%h %ae'`). Worktree clean after the commit. Not pushed.

## Files changed

- `product-guidelines/coding/SKILL.md`: rewritten, 3396 -> 1499 words.
- New beside it (10 files): `orchestrated_mode.md` (113), `recognize.md` (403), `starting_set.md` (180),
  `research.md` (197), `trial_run.md` (249), `kinds.md` (195), `new_tools.md` (69), `settle.md` (629),
  `task_document.md` (489), `hand_back.md` (113). Each in
  `C:/Storage/repos/the-way/.runs/worktrees/coding-skill-shape/product-guidelines/coding/`.
- `foundations/decisions.md`: WAY-216 and WAY-266 edited in place (26 lines changed). No new entry.
- Unchanged, as the task requires: `description`, the Python code, the entry points
  (`skill_entry_points.py --write` printed "entry points are current" and changed nothing), the templates,
  `reading.md`, the other skills.

## Materials (under `C:/Storage/repos/the-way/.runs/task-cycles/coding-skill-shape/`)

- `reports/assessment.md` - the table of To do 6: 56 rows, 249 nonblank lines each in exactly one row, quotes
  literal with permalink ranges on f86fd71; sections in the order of `judging.md`; the added text and the two
  proposals follow the table.
- `reports/word-counts.md` - the seven routes, three figures each, file lists, the reading counted beside each route.
- `tools/make_assessment.py`, `tools/check_assessment.py`, `tools/word_counts.py`, `tools/verify_counts.py`,
  `tools/compare_sentences.py`. `reports/sentences.txt` is the sentence comparison output.

## Checks (command and exit code)

| Check | Result |
|---|---|
| `python -B elements/common/foundation_check.py` (after the edits and again before the commit) | exit 0, "0 errors" |
| `python -B instruction-files/check_instructions.py .` | exit 0; output identical to the base's (diff of `reports/check_base.txt`, made on a `git archive` export of f86fd71, and `reports/check_after.txt`): the `_zadania\` dead-path warning on `AGENTS.md:21` stands on the base, 0 error, 1 warn, 3 info |
| `python -B agent-instructions/skill_entry_points.py --write` | exit 0, changed nothing |
| `python -B gate/run_tests.py agent-instructions` (after the last change to the skill) | exit 0, 18 tests OK |
| `python -B gate/run_tests.py installation` | first run before my last small edit of `SKILL.md` step 3: 44 tests OK (exit 0). Second run after the last edit: see the last line of this report |
| `python -B tools/check_assessment.py reports/assessment.md` | exit 0: 56 rows, quotes literal, every nonblank line covered once |
| `python -B tools/verify_counts.py reports/word-counts.md` | exit 0: 346 figures compared, 0 differ. Run after my last change to a counted file (the step 3 wording of `SKILL.md`); the commit followed with no further change to a counted file |
| whole gate | not run (the orchestrator's) |

No test was written: only Markdown changes and no invariant is added.

## Word counts (from `reports/word-counts.md`)

Before step 4 / total to the end of the skill / total without the first reading in `refine-task` (3391 words, which
my four files give as 463 + 2228 + 208 + 492):

| Route | Before | After |
|---|---|---|
| 1 no code, no preference | 14511 / 14511 / 11120 | 8613 / 11234 / 7843 |
| 2 no code, preference | 14002 / 14511 / 11120 | 7585 / 11037 / 7646 |
| 3 code, no guidelines, also extension | 14511 / 14511 / 11120 | 9057 / 11678 / 8287 |
| 4 refresh | 14002 / 14511 / 11120 | 8029 / 11481 / 8090 |
| 5 "A new kind" | 14002 / 14511 / 11120 | 5293 / 10857 / 7466 |
| 6 one kind, files exist | 14002 / 14511 / 11120 | 7600 / 11052 / 7661 |
| 7 orchestrated, route 1 | 14511 / 14511 / 11120 | 8726 / 11347 / 7956 |

Changes of the total: -19.5% (route 3) to -25.2% (route 5).

**Where the task's figures do not match mine** (not bent):

- Question 1 gives ca. 10 600-11 300 words to the end (-22 to -27%) and ca. 5100-8800 before step 4. Mine: 10 857-11 678
  (-19.5% to -25.2%) and 5293-9057. Routes 3 and 4 exceed the task's upper bounds (11 678 and 11 481 vs 11 300; 9057 and
  8029 vs 8800 for route 3).
- Question 1 gives "total text larger by ca. 400 words". Mine: files beside the template total 4136 words against 3396
  (+740): the pointers, the sentence repeated in `settle.md`/`hand_back.md`/`task_document.md`, the sentences of To do 9-13
  and the headings.
- Task Context says ca. 7200 words are read at step 0; my count of the eight files it names is 7215 (and 3391 for the first
  reading) - no difference there.

## Rule preservation (the weakest point)

`tools/compare_sentences.py` (whitespace normalised, list markers dropped, headings dropped) gives `reports/sentences.txt`.
**Of the base's sentences, 13 differ**; every other one stands verbatim in the rebuilt corpus. Account:

1. "The cycle's author was not in the conversation and reads only the document ..." - meaning-preserving rewording
   ("the task document"), moved to "Rules that hold across the steps".
2-5. The four pieces of step 0's first bullet (both templates; the task skill and template; two sections of the way of
   working; the critique skill) - pointers at the steps that use each; the second reading of the `refine-task` files is
   removed as To do 2 accepts; the critique files move to `research.md`/`settle.md`.
6. "Read the product's root `AGENTS.md` and every file under `guidelines/`." - `recognize.md`, reworded; the set read after
   `refine-task` is the same as in the base.
7. "Select and read the product's foundation ..." - `recognize.md`, "besides what `refine-task` selected at its step 1"
   (To do 2: only the entries added at step 0).
8-9. The research condition and the refresh sentence - `starting_set.md`; the second lost only its capital letter and
   the connective "read `research.md`".
10. "Where research ran, give one fresh agent ..." - `research.md`, "Once the reports are in" (the file is read only where
   research runs); plus one sentence reading the critique skill before the first critique.
11. "**New tools.** For each new tool ... show the options ..." - cut in two: the condition stands in `settle.md`, the
   procedure in `new_tools.md`.
12. "**Critique.** ... as 'Critique before collective review' gives" - `settle.md`, naming the file of that section and the
   read of the critique skill.
13. "Check that the task document holds what 'What reaches the task document' names ..." - `hand_back.md`, the section
   now being `task_document.md`.

Sentences present in the rebuilt corpus and not in the base (all listed in `reports/assessment.md` under "Text added that
no base line carries"): the pointers and their conditions; the sentence of WAY-266 (testing skill's wording); the fifth mode
(To do 9); "The route of one kind" in `SKILL.md` (To do 10, 11) with a one-line opening in `settle.md`, `hand_back.md`,
`task_document.md` pointing to it; the sentence of `kinds.md` (To do 12); "Word it as 'How to show' ..." in
`starting_set.md`.

**By-hand walk of the seven routes** (what an agent reads, in order; each reads `SKILL.md` first and whole):

1. No code, no preference: `recognize.md` (mode: no code) -> step 2 pointer ("before the first code") -> coding template,
   `starting_set.md` (preference question worded by "How to show"; documentation rule for no code) -> sends to `research.md`
   (no preference) -> critique skill with its files -> no step 3 -> step 4: general template, `settle.md`,
   `task_document.md` (coding template and critique skill not read again) -> step 5: `hand_back.md`.
2. No code, preference: as 1, but `starting_set.md` does not send to `research.md`; the documentation rule is in
   `starting_set.md`, so it reaches this route; step 4 does not read the coding template again (step 2 did). The critique
   skill is first read at step 4 through `settle.md`.
3. Code, no guidelines, no preference (and extension): as 1, then step 3 pointer: `trial_run.md` and `kinds.md` (template
   already read at step 2).
4. Refresh: `starting_set.md` states the refresh rule (no research, no `research.md`); step 3 both files.
5. "A new kind": the mode list names "A new kind" in step 3; the step 3 pointer's two conditions do not hold, so neither
   `trial_run.md` nor `kinds.md` is read; the paragraph in `SKILL.md` governs; the coding template is first read at step 4.
6. One kind: the fifth mode of `recognize.md`; step 3 second sentence: template (not read by step 2) and `kinds.md` alone;
   its first bullet carries the one-kind sentence; no `starting_set.md`, `research.md` or `trial_run.md`; steps 4 and 5
   open with the pointer to "The route of one kind".
7. Orchestrated: `SKILL.md` -> `orchestrated_mode.md` before step 1, then as 1.

Conditions of the acceptance criteria, walked: the step 2 pointer names the three conditions and says "no
`guidelines/coding.md`; a kind of code without a file of its own is not that case"; "How to show", "Extend what exists" and
"A choice found in the product's files" are in `SKILL.md` and so reach every route, "A new kind" included; "What reaches the
task document" is named by the pointers of steps 4 and 5 (`recognize.md` says itself that *To do* gains a part; step 3's
files say what step 4 proposes - as in the base); the no-code documentation rule and the refresh sentence stand in
`starting_set.md`; the fragment 197-199 stands in `SKILL.md` outside the condition "where the product has code"; "Where the
skill works" is kept whole; WAY-210 order in step 1 (parts named first, then the reading, then the product's tools) kept.

## Foundation step

- **Row 1 and 2** (one edit of WAY-216): the three binding sentences (the third in the wording of the task's *Context*);
  `narrows WAY-251` in *Relations* of WAY-216 only; WAY-251 untouched. *Verification* gained one example in each of
  `complies` and `violates`; *Rationale* one sentence; *Rejected* two ways from the source (the four modes left and the
  gap described as a proposal; the rejected wording "Neither task is an extension ...").
- **Row 3** (edit of WAY-266 in place): the last sentence removed.
- `foundation_check.py`: 0 errors.
- **Search of the whole foundation (WAY-33)** after the entries were settled: `git grep` of `WAY-216`, `WAY-266`, "not bound by it
  until", "stands unchanged", "unindexed", "trial run", "comparison WAY-200" through `foundations`, `elements`,
  `agent-instructions`, `project-level`, `product-guidelines`, `task-cycle`, `instruction-files`, `installation`. Found:
  WAY-216's own references in WAY-218-area entries (`foundations/decisions.md` lines near 6012, 6020, 6873: references to
  the first-file case, unaffected), `product-guidelines/reading.md:76`, `project-level/task/skill/SKILL.md:46` and
  `guideline_findings.md:4` (references to WAY-216 for the first-file case, unaffected), the WAY-265 text on "stands
  unchanged" (a different rule, unaffected), and the testing and styleguide skills' copies of the WAY-266 sentence (they keep
  it). No other entry restates the dropped sentence of WAY-266 or the old end of WAY-216. Not searched: the glossary and the
  part map by hand beyond the grep (no term or part is new).
- Skill read for writing the entry: `elements/decisions/skill/SKILL.md` with `read.md` and `decide_entry.md`, and
  `elements/decisions/template.md`. I did not run the interactive steps of that skill (no question: the rows give the
  meaning and the wording).

## Choices, with the way not taken

1. **The rule of one kind in `SKILL.md`, plus a one-line pointer at the head of `settle.md`, `hand_back.md` and
   `task_document.md`.** Not taken: the rule only in `SKILL.md` - the files of steps 4 and 5 then list "each standing check"
   with no sign of the exception, and the case is brought about by the mode list, not the step. Cost if wrong: about 70 words,
   and a pointer that must be kept in line with the rule's name.
2. **"Extend what exists" and "A choice found in the product's files" go to "Rules that hold across the steps"** in `SKILL.md`,
   not `recognize.md`/`kinds.md`: they hold on the route "A new kind", which reads neither. Cost: ~100 words in `SKILL.md`
   that routes with no step 3 also carry.
3. **The reading of `AGENTS.md`/`guidelines/`/foundation in `recognize.md` as its second bullet**, after the parts are named
   (as the testing skill does). Not taken: first bullet, which would turn WAY-210's order around; the third bullet, after
   finding what the product has, which would make the reading come after the finding.
4. **Fifth mode's condition: "where that file stands"**, so a product without `guidelines/coding.md` goes by "code and no
   coding guidelines" (the whole audit), not by the one-kind route. Not taken: the one-kind route for that case too -
   WAY-202 needs the general file's decisions to be written by a task, which only the second mode does.
5. **The step 3 pointer splits the routes by what step 1 gave** ("the trial run and the audit" / "the mode of one kind ... and
   not the trial run and the audit"), so a task that combines the one-kind mode with "A new kind" still reads `kinds.md`. Not
   taken: "only the mode of one kind", which would have switched `kinds.md` off for that combination (I changed it before
   committing).
6. **`kinds.md` keeps the lead-in "Where the product has code:"** and the one-kind sentence sits at "the audit covers every
   one of them", as To do 12 gives.
7. **WAY-216 edit also touched *Verification*, *Rationale* and *Rejected***, not only the sentences and *Relations*. Not taken:
   leaving them - *Verification* would not hold the new third sentence and *Rejected* would not keep the ways the source
   keeps. The *Rationale* sentence is my wording (no source gives one).
8. **Route 6 "before"**: the base has no such route; counted as the base text gives it to any run (same figures as routes 2/4/5).
9. **Proposals** (not applied): P1 the contradiction of "A new kind" with lines 223-224, 269 and 63-69 (To do 8); P2 narrowing
   the reading of `guidelines/` (lines 108), as the earlier skills' P1, not recommended. No other remove/reword was
   found that changes a rule's meaning; the two remarks of PR #60/#62 on reading `guidelines/` are P2.

## Reaches beyond this handoff

- `elements/decisions/template.md` (read whole, for the writing of the edit); `product-guidelines/reading.md:30-110`,
  `project-level/task/skill/read_sources.md`, `product-guidelines/testing/*.md` and `styleguide/*.md` (as shapes, as the
  handoff names them); `gh pr view` of the six PRs. No decision beyond the handoff's list was needed.
- **Foundation read:** whole - WAY-35, 128, 200, 209, 210, 213, 214, 216, 251, 256, 265, 266 (and those quoted whole in the
  task's *Decisions in play*: 257, 265, 266, 216, 200 (fragment), 199, 201, 202, 204, 209, 210, 211, 251, 247, 174, 268, 120,
  154, 172, 127, 259 as fragments of the task, which I read as quoted, not in the log). **Not read whole:** the other
  decisions of the list (WAY-01, 05, 08, 14, 16, 28-30, 33, 44, 51, 61, 100, 107, 113, 121, 123-125, 129, 134, 150, 155, 167, 168,
  171-173, 198, 202-208, 211, 212, 215, 217, 228, 231, 247, 248, 257, 259, 268), the part-map entries `product-guidelines`
  and `decisions`, the eight invariants, the environment fact `claude-skill-nested-references` (read as cited in
  `instruction-files/SKILL.md`) and the glossary. A decision I did not read whole that bears on the work would be a gap of this
  report; the ones I cite in the text are cited as the base cited them.

## Searches not found or unclear

- `gh pr view 51 --comments` returned no output (a PR comment search found nothing); the remarks of #50, #52 and #59 do not
  mention this skill.
- The task's "ca. 400 words more" and the upper bounds of the route estimates (see "Word counts") do not match my count.
- "wider mode governs" (To do 9): for the one-kind mode combined with "A new kind", neither mode is wider; I read the rule
  as covering the combination of the one-kind mode with the audit modes and let both narrow modes run side by side.
  Unclear in the task; a reviewer should say if the other reading was meant.
- The task's acceptance criteria says steps 1 and 3 "say themselves what they add to the document". Step 1 does (*To do* gains a
  part). Step 3's files say what step 4 proposes (violated invariant, reformatting) and the *Context* items stay in
  `task_document.md`, as in the base; I found no sentence in the base's step 3 that writes into *Context* itself.
- Unclear: whether the sentence "At step 3 ... A new kind" in `SKILL.md` should state its own condition for a product that has
  code (the base's list reached it from the mode list); I left it with the mode list's wording.

## Concerns

- Total text rose by 740 words; the pointer repetition is the price of the trap in the handoff (a rule at several moments).
- The WAY-216 *Rationale* sentence is mine.
- The "wider mode governs" reading above.

## Installation gate, second run

`python -B gate/run_tests.py installation` after the last edit of `SKILL.md`: exit 0, 44 tests OK.

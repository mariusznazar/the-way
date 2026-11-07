PASS a15de0906961981bc58982f97cb1443875341518

# Review of the whole change - find-foundation-entries in the shape of WAY-256

Range: `f447bb62ce4f8d4a4badb1b283a10f62651d65d7..a15de0906961981bc58982f97cb1443875341518`, one commit
(`git log f447bb6..a15de09`), one author without a plan, no spec, no slices. `git rev-parse HEAD`
printed `a15de0906961981bc58982f97cb1443875341518`, the head given. Method: `task-cycle/review/SKILL.md`
and `task-cycle/review/whole_change.md`, read whole.

Counts: blocking 0, Minor 3 (all within the task), out of scope 0.

## Findings

### Critical

none

### Important

none

### Minor

1. `elements/common/skill/SKILL.md:32-33` - "where you start at step 2, 4 or 5 and have not read it,
   read it first". Within the task. A resumed use whose first row is still `waiting` (the resume rule
   at `SKILL.md:35-36`) starts at step 3, not at 2, 4 or 5, so by the letter the sentence does not
   reach it when it comes to step 4 or 5. The route is not lost: the pointers at `SKILL.md:56-57` and
   `:61-62` name the variant file and have the agent carry out its lines, and the entry point reads a
   file when the step that names it comes (WAY-127, WAY-259). What can be lost is "in full": such an
   agent may read only the "Step 4" section and miss the variant's "What the caller gives". Little
   rides on it, because the table in `SKILL.md` names the source and the mode of each variant. A
   wording such as "where you come to step 2, 4 or 5 without having read it, read it first" would
   cover every start. Evidence: hand walk of a resumed task-mode use (below).
2. `elements/common/skill/task_variant.md:38-39` - "An accepted row stays a row, and the task's cycle
   writes its entry (WAY-134). In its place, a row that carries a choice ...". Within the task. On the
   base (`SKILL.md:95-96`) "In its place" followed "this step does not run" and meant step 4. That
   clause now stands only in `SKILL.md:56-57`, so inside `task_variant.md` the nearest antecedent of
   "its" is "its entry". The meaning reaches the agent through the heading "Step 4 - in place of row by
   row" and `SKILL.md` "carry out in its place the lines for step 4 of `task_variant.md`", so no rule
   changes; the sentence reads awkwardly to an agent that opens the file by its path. "In place of
   step 4, ..." would close it. Evidence: 6-word window comparison of base and new files (checks
   below), which places this run among the reworded ones.
3. `.runs/task-cycles/find-foundation-entries-shape/reports/assessment.md` proposal 3 and "Before the
   table". Within the task (To do 1 and 5). `instruction-files/judging.md:32-33` says removals are
   proposed as "When to remove a rule" (`judging.md:72-81`) gives. Proposal 3 (remove the sentence on
   future callers, base `SKILL.md:12-14`) names none of that section's conditions and gives only "no
   step depends on it". The judgement also skipped the search of records that `judging.md:7-9` puts
   before the table (the author says so openly). The verdicts of the table rest on cost or a carried
   decision, which `judging.md:32` allows, so no row's verdict is wrong for lack of the search. But the
   request will show the human a removal without the ground the method asks for. The proposal should
   say which condition it meets, or that the sentence is a statement of plan and no rule, so that the
   section does not apply.

## Acceptance criteria the handoff asks of me

### 1. Both routes walked by hand

Method: read `SKILL.md` at `a15de09` as an agent that has only its path, followed each pointer in
order, and compared with the base `git show f447bb6:elements/common/skill/SKILL.md`.

- **Task variant.** `SKILL.md` front matter, picture, location -> "What the caller gives": the second
  table row ("`refine-task`, with a task document as the source and rows of its section 'Settlements
  to record' as the mode - 'task mode' ...") -> `:32` read `task_variant.md` in full at step 1 -> resume
  rule -> step 1: read `task_variant.md`, carry out `read.md`: `way_of_working.md` in full; the
  variant's step 1 lines (task template section and its rule; projected entries of *Decisions in
  play*); the source; the foundation by "Reading the foundation"; the element templates -> step 2:
  `build_table.md` (candidates from the variant's lines; row shape; last column; material is a
  proposal; write where the variant says; no whole-foundation search; collision rule) with
  `task_variant.md` step 2 (items of Need/To do/AC/Out of scope and answers; the kinds, never the
  part map; human's words; table under "Settlements to record" with *State*, `waiting`/`rejected`,
  shown whole with source and next-reader column and a reason per rejected row; the cycle makes the
  search) -> step 3 in `SKILL.md` -> step 4: `SKILL.md` "In task mode this step does not run" plus
  `task_variant.md` step 4 (questions against choices, at most three, answers and ways not taken into
  *Source*) -> step 5: `task_variant.md` step 5 (take out rejected rows and *State*, `Candidates:`
  line, renumber, `none`, tell `refine-task` the counts).
  - Stays: every base line the task variant used: L8-20, L30-34 (with "step 4 does not run" in
    `SKILL.md` step 4), L36-37, L41 (`way_of_working.md`), L42-44 (task section), L47-56, L64-71,
    L75-81 with what "as above" imported from L72-74, L82-86 (common sentences plus the cycle's
    clause), L88-91, L95-101, L134-138.
  - Drops: L24-28, the definition template section of L41-42, L45-46 (`projected_mode.md`), L60-63,
    L72-74 as such, L102-125, L129-133 - all text of the definition. The reading of the definition
    template section in task mode drops under the "in addition" reading of base L41-44; the frozen
    task's question 2 settles that it is not read. Base L60-63 is unlabelled; the frozen task (Need)
    classes `:60-63` as the definition's and the base's own "For a task: take each item ..." at L75
    stands in its place, so nothing of a rule drops there either.
  - Dropped without replacement: "and the differences below each step name what changes" (L33-34),
    which only pointed into the one file; the labels "For a project definition," / "For a task," on
    moved lines.
- **Project-definition variant.** `SKILL.md` -> first table row (`define-project`, a project
  definition as the source, projected entries into "Projected foundation changes") -> step 1:
  `definition_variant.md` in full, `read.md`: `way_of_working.md`, definition template section,
  `projected_mode.md`, source, foundation, element templates -> step 2: `build_table.md` with the
  definition's step 2 lines (L60-63, L72-74, the readiness-gate search) -> step 3 -> step 4: the four
  numbered items of `definition_variant.md` -> step 5: `definition_variant.md` close and the count.
  - Stays: L8-28, L36-37, L41-54, L58-74, L82-91, L102-133 - every line the definition used.
  - Drops: L30-34 (except what both share), L42-44's task section, L55-56, L75-81, L95-101,
    L134-138 - all text of the task.

### 2. Every row of `assessment.md` against the real place, and every nonblank base line

All 30 rows checked against the five files: each fragment stands where the row's "Place after"
says (rows 1-5, 8, 9, 16, 24, 25, 28 in `SKILL.md`; 6, 11, 17, 21, 27, 29 in `definition_variant.md`;
7, 15, 22, 30 in `task_variant.md`; 12-14 in `read.md`; 18-20 in `build_table.md`; the split rows 10,
23, 26 in each place named). The rows' line ranges cover every nonblank base line once (L101-102
split at the line break, "For a project" / "definition, ..."), and the Words column sums to 1584,
counted by hand from the table. The 6-word window check (below) finds no base text missing from the
five files outside the places the rows call reworded.

### 3. Rewritten conditionals and pointers, and new sentences

Each rewritten conditional and each new sentence in `author.md`, sections "Comparison with the
base", checked against the base and the files:

- Choice of variant: the table holds both callers' values as the base did; no caller gains or loses a
  variant. Adds none, loses none.
- Template reading at step 1: closes the "in addition" reading in task mode, as question 2 of the task
  settles; the definition keeps its section and `projected_mode.md`. No other route changes.
- Step 2 split: `build_table.md` "Take the candidates as the lines for step 2 ... give" switches off
  taking candidates from the other variant's headings; "Write the table where, and with the row
  states, those lines give" switches off writing the table in the other variant's place; "those lines
  say who makes it" keeps the base's "No search ... runs here" and moves only the who. Adds none,
  loses none.
- Step 4 and 5 pointers: "this step does not run" kept for task mode; the definition's procedure word
  for word. Adds none, loses none.
- "where you start at step 2, 4 or 5 ...": adds no route; it reaches less far than it could (Minor 1).
- Each "switches off" the author names is right; I found no new sentence that switches off a rule.

### 4. "Show it whole as above"

`task_variant.md:29-32` states: proposed rows start `waiting`, rows with no concrete next-reader
consequence start `rejected`, the whole table is shown with the source and next-reader column and a
reason for each rejected row - the text of base L72-74, which L80-81 pointed to. Met.

### 5. Pointers say read or carry out, and name the variant in the callers' words

- Read: `SKILL.md:32` and `:40` ("Read the file of your variant in full"). Carry out: `:41` (`read.md`),
  `:46` (`build_table.md`), `:56-57`, `:61-62` (the variant's lines for steps 4 and 5); `read.md:4` and
  `build_table.md:3` carry out the variant's lines. Each names the step ("step 1", "step 2", ...) and
  the variant ("for a project definition", "in task mode"); each variant file's sections are headed
  "Step N - ...".
- Callers: "task mode" (`project-level/task/skill/orchestrated_mode.md:17`,
  `product-guidelines/coding/hand_back.md:24`, `product-guidelines/styleguide/hand_back.md:11`,
  `product-guidelines/testing/hand_back.md:16`) stands in the table row (`SKILL.md:30`) and in each
  pointer; "rows of the document's section *Settlements to record*" (`find_settlements.md:6-7`) and
  "projected entries into 'Projected foundation changes' as the mode" (`project-level/skill/SKILL.md:129-131`)
  stand in the table's rows. WAY-265 holds: the variant files `read.md` and `build_table.md` point to
  are named at steps 1 and 2 of `SKILL.md` with their conditions. Met.

### 6. Nothing outside `elements/common/skill/`

`git diff --stat f447bb6 a15de09 -- . ':!elements/common/skill'` printed nothing; the five changed
paths are all `.md` in `elements/common/skill/`; lines 1-4 of `SKILL.md` (front matter, description)
are unchanged; no Python changed; `skill_entry_points.py` reports the entry points current. Also,
between the task's base `dfd50e5` and `f447bb6` nothing in `elements/common/skill/` or
`project-level/task/template.md` changed (`git diff --stat dfd50e5 f447bb6 -- project-level elements
product-guidelines` lists other files only), so the base line numbers hold. Met.

### 7. Word counts

Recomputed by my own script (whitespace split, as `wc -w`) on the committed files:

| Figure | Mine | `word-counts.md` / `author.md` |
|---|---|---|
| base `SKILL.md` (f447bb6 and dfd50e5) | 1584 | 1584 |
| `SKILL.md`, `read.md`, `build_table.md`, `definition_variant.md`, `task_variant.md` | 599, 126, 198, 624, 473 | same |
| together | 2020 | 2020 |
| task sum 1 / 2 / 3, after | 1396 / 3553 / 2437 | same |
| task sum 1 / 2 / 3, before | 1584 / 3741 / 2625 | same |
| definition sum 1 / 2, after | 1547 / 4392 | same |
| definition sum 1 / 2, before | 1584 / 4429 | same |
| `way_of_working.md`; "How a skill asks"; "Reading the foundation"; "Critique before collective review" | 1752; 208; 503; 89 | same (89 in `assessment.md`) |
| `definition_template.md:260-348`; `projected_mode.md` | 674; 419 | same |
| task template section with its rule (`template.md:80-87` + `:181-202`) | 60 + 345 = 405 | 405 |

Percentages (-12, -5, -7, -2, -1) and the proposal figures in `assessment.md` (800, 952, 2601, 1485)
follow from these. All within the estimates of question 1 (task 1300-1450, definition 1500-1650,
files +370-550: +436).

**424 against 405:** 405 is the right reading. "The section 'Settlements to record' and its rule
under 'What each section carries'" is the section's own lines `project-level/task/template.md:80-87`
(60 words) and the rule's bullet `:181-202` (345). The task's 424 equals `:181-208`: the rule's
bullet plus the bullet "Out of scope" and the paragraph below it, without the section's own lines,
so it cannot be "the section with its rule". (The closing paragraph at `:206-208` holds one sentence
on rows of *Settlements to record*; even with it the figure is not 424, and the figure stands on both
sides of every before/after comparison, so no change shifts.) The request should state 405.

The request is not written yet; `verify_counts.py` checks `author.md`, `word-counts.md` and
`assessment.md`, and must be run on the request's text once it exists to meet the task's criterion
that every number stated in the request, prose included, is compared with the files.

### 8. Foundation entries

Selected for the part `elements-common` (`foundations/part_map.md:65-73`) and the task's *Decisions
in play*: WAY-256, WAY-265, WAY-257, WAY-258, WAY-259, WAY-115, WAY-134 read whole; WAY-35, WAY-117,
WAY-127 as quoted in the frozen task. The change keeps them: the picture, the rule of working kept
across steps (resume), step 3 as one instruction and the pointers stay in `SKILL.md`; procedures of a
step or variant stand beside it; the variant file, which steps 1, 2, 4, 5 need, is named at each of
them and read once unless a later start comes first (WAY-256); the variant files are named in
`SKILL.md` at the steps whose files point to them (WAY-265); references stay one level deep from
`SKILL.md` with WAY-265's naming (WAY-258's ground); rules of entries stay in the element templates
(WAY-35); the table's shape (WAY-115, WAY-134) is unchanged in both variants. No invariant test
changed. The change writes or changes no foundation entry; the task carries no row of *Settlements to
record* and no projected entry, so the foundation step had nothing to write.

## Against the whole task (whole_change.md)

- To do 1: the assessment exists, in judge mode for a skill, and the rebuild follows it (Minor 3 on
  the removal proposal and the record search).
- To do 2: two step files (`read.md`, `build_table.md`), one file per variant named at each step it
  concerns with its condition and read once at step 1, step 3 in `SKILL.md`. Met.
- To do 3: the table quotes each fragment with its line range on the base, when needed, recognised,
  verdict, place after. Met (for the request to carry).
- To do 4: counts on both routes as question 4 gives. Met.
- To do 5: proposals 1-4, proposal 1 the three sections of `way_of_working.md`. Met.
- To do 6: nothing outside `elements/common/skill/`. Met.
- Own-work check: the author named the weakest requirement (no route added or lost) and checked it by
  `route_check.py`, a presence check, plus a comparison by hand of each conditional; I repeated the
  comparison independently (6-word windows and the hand walk) and found the same places.

## Declined to judge

- Whether proposal 1 (three sections of `way_of_working.md` in task mode) should be taken: a decision
  the frozen task leaves to the human (question 3).
- The base clause "for a task, from the first row still `waiting`" (`SKILL.md:35-36`), which the author
  calls unclear: unchanged text, outside the rebuild.

## Checks

| Command (from the worktree root) | Exit code | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `a15de0906961981bc58982f97cb1443875341518` |
| `git diff --stat f447bb6..a15de09`; `git diff --stat f447bb6 a15de09 -- . ':!elements/common/skill'`; `git status --short` | 0 | 5 files in `elements/common/skill/`; nothing outside; clean |
| `git diff --stat dfd50e5 f447bb6 -- project-level elements product-guidelines` | 0 | no file of this skill or of the task template |
| `python -B agent-instructions/skill_entry_points.py` | 0 | "entry points are current" |
| `python -B gate/run_tests.py elements/common` | 0 | 109 tests, OK |
| `python -B gate/run_tests.py agent-instructions` | 0 | 18 tests, OK |
| `python -B gate/run_tests.py installation` | 0 | 44 tests, OK |
| `python -B elements/common/foundation_check.py` | 0 | 0 errors |
| `python -B instruction-files/check_instructions.py .` | 0 | 0 error, 1 warn (`AGENTS.md`, private notes path) |
| `python -B instruction-files/check_instructions.py --file elements/common/skill/<each of five>` | 0 each | 0 errors; 3, 2, 0, 2, 3 warnings |
| `python -I -B .runs/task-cycles/find-foundation-entries-shape/reports/verify_counts.py` | 0 | 0 problems; note on 424 |
| `python -I -B .runs/task-cycles/find-foundation-entries-shape/reports/route_check.py` | 0 | 0 problems |
| `python -I -B <scratchpad>/counts.py <worktree> <out>` (my own counts, scratchpad `C:\Users\Mariusz\AppData\Local\Temp\claude\6b84451ec494cdda\3a9bd485-0e4a-4608-a08e-b723e098f59b\scratchpad\counts.py`) | 0 | every figure as in the table above |
| `python -I -B <scratchpad>/shingles.py <worktree> <out>` (6-word windows of base against the five files and back, `C:\Users\Mariusz\AppData\Local\Temp\claude\6b84451ec494cdda\3a9bd485-0e4a-4608-a08e-b723e098f59b\scratchpad\shingles.py`) | 0 | base runs missing only at labels, the caller paragraph, the template-reading sentence, "as above", the search clause and the step 4/5 openings - the places the assessment calls reworded |
| Hand walk of both routes and a resumed task-mode use | - | as in criterion 1; Minor 1 |

Not run: the whole gate (`python -B gate/run_tests.py`), the orchestrator's run.

## Reach beyond the dispatch

- `instruction-files/judging.md`, whole: to judge whether the assessment follows the method To do 1
  names (Minor 3).
- `foundations/decisions.md` WAY-258: named by WAY-256's ground and the rule of references one level
  deep that WAY-265 rests on.
- `project-level/task/template.md:70-211`: to settle 424 against 405 and to check the task variant's
  states against the template.
- The callers named in the handoff (`project-level/skill/SKILL.md:125-134`,
  `project-level/task/skill/find_settlements.md`, `orchestrated_mode.md`,
  `product-guidelines/{coding,styleguide}/hand_back.md`), and a search of `find-foundation-entries|task mode`
  over the repository, to check the callers' words against `SKILL.md`.
- `.claude/skills/the-way-find-foundation-entries/SKILL.md`: what the entry point has the agent read.
- `foundations/part_map.md` entry `elements-common`: to select the foundation.

## Searches not found or unclear

- The task's 424 words for the task template section with its rule: no reading of "the section with
  its rule" gives it; it equals `project-level/task/template.md:181-208`, which leaves out the
  section's own lines. 405 is right (criterion 7).
- `foundations/decisions.md`: no decision states the future callers that base `SKILL.md:12-14` (proposal
  3) names; searched `find-foundation-entries|finds? (the )?entries` - one hit, `:233`, not about callers.
- The request whose numbers criterion 7 asks me to compare does not exist yet; I compared the numbers
  of `author.md`, `word-counts.md` and `assessment.md`.

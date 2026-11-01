FAIL db3845c37d706f27caa89886f80e8b004e65bbed

# Review of the whole change: plan-project in the WAY-256 shape

Range `2f51e6c31f5911ac8a0292a80a4f599bd4bd0092..db3845c` (one commit). `git rev-parse HEAD` gives
`db3845c37d706f27caa89886f80e8b004e65bbed`, the head given. One author, no plan, no spec; this is the
only review the change gets (WAY-136). Blocking findings: 1. Minor: 4. Out of scope: 3 (the lines of
Declined to judge).

Short version: no rule of the base was lost and none changed its meaning. Every quote, row, figure
and sum of the materials checks out. What blocks is one new sentence whose effect the materials
state in a way that does not hold, and two routes of the word counts that rest on it.

W = `C:/Storage/repos/the-way/.runs/worktrees/plan-project-skill-shape`.
C = `W/.runs/task-cycles/plan-project-skill-shape`.

## Important (blocking)

### 1. What the sentence that has `read.md` read does to step 1 is stated two opposite ways, and routes 3 and 6 are counted on the reading the task rejected

**Anchors:** `W/project-level/plan/skill/existing_plan.md:15-16`,
`W/project-level/plan/skill/SKILL.md:48-49`, `C/reports/assessment.md:81`,
`C/reports/word-counts.md:8`, `:18`, `:22`, `:33`, `:139`, `:322`. Slice: none (one author, no plan).

**To paste:** The assessment says that the last bullet of `existing_plan.md` "does not make step 1
run", while routes 4, 5a and 7 count step 1 as run although `SKILL.md` step 1 is switched off for
every session that passed that bullet. Say what the sentence does, and count routes 3 and 6 by that.

**Why I report it:**

What the sentence is for. The task's question 3 chose the pointer to `read.md` so that a session on
an existing plan keeps what all sessions do today. The way it turned down reads: "po cichu wyłącza
to, co dziś robią wszystkie sesje; agent zmienia plan bez fundamentu w głowie, a jedyną ochroną
zostaje `plan_check.py`". The same answer records `readiness_check.py` run in 14 of 14 sessions and
`foundations/` reached in 11 of 14.

The mechanism. The rebuilt files give one instruction, "reads it", and the materials give it two
effects:

- Routes 3 and 6: the session reads `read.md` and does none of it. `assessment.md:81`: "it does not
  make step 1 run (the readings of step 1 are done only where step 1 runs)".
  `word-counts.md:139`: "step 1 is not run (its file is read, as existing_plan.md has it, so the
  foundation and the guidelines are not read)". `:322` says the same of route 6.
- Routes 4, 5a and 7: step 1 runs, with the foundation and the guidelines counted. But on these
  routes too the session passed the same bullet at step 0, so `SKILL.md:48-49`, "Read `read.md` ...
  each unless step 0 had you read it", gives it nothing to do at step 1. That pointer is the whole
  of step 1 in `SKILL.md`. If reading `read.md` at step 0 does not carry it out, then nothing on
  these routes carries it out, and "the plan is checked against it from step 1"
  (`existing_plan.md:9`) has an empty step behind it. In the base, reaching step 1 meant its four
  bullets.

So the two claims cannot both hold:

- If "reads" means reads and carries out, as every other "Read `<file>`" pointer of `SKILL.md`
  means, the skill's text is consistent: step 0 carries `read.md` out and step 1 rightly skips it.
  Then `assessment.md:81` is false, and routes 3 and 6 reach the section "Reading the foundation"
  (492 words) and `product-guidelines/reading.md` (1141), which question 4 counts "tam, gdzie droga
  do nich dochodzi".
- If "reads" means sees and does not carry out, as the materials say of routes 3 and 6, those routes
  are the outcome question 3 turned down (a plan changed with no foundation in mind), and on routes
  4, 5a and 7 no pointer has the readiness check or the foundation run.

The figures, routes 3 and 6, totals with the files read beside the skill:

| Route | Stated before | Stated after | Stated change | After, step 1 counted | Before as stated | Before, step 1 counted too |
|---|---|---|---|---|---|---|
| 3 | 5264 | 4867 | -7.5% | 6500 | +23.5% | 6897, so -5.8% |
| 6 | 5852 | 5236 | -10.5% | 6869 | +17.4% | 7485, so -8.2% |

The absolute saving stays the same (397 and 616 words) only where both states count step 1, and the
recorded sessions argue for counting both: 14 of 14 ran the readiness check though the base's text
sent no resumed draft to step 1. Counted in the state "after" alone, the sign turns. Either way the
stated range "-10.5% to +9.4%" (`word-counts.md:33`, repeated in `author.md:51`) is not what the
request may carry as it stands, and the task's "ok. 170 słów na każdej drodze z istniejącym planem"
is the file alone, not what the sentence sets off.

The author raised this as concern 3 and kept the task's word "czyta". Grade and scope are mine: the
task requires each new sentence to be compared by what it selects and switches off, and this line
of the materials names an effect the text does not give. It is within To do 5, To do 8 and the
second acceptance criterion. A rationale in the report does not lower it.

Fix, recommended: keep the skill's text, which is consistent on the first reading; correct
`assessment.md:81` to say that the session carries `read.md` out; state in `word-counts.md` the rule
and routes 3 and 6 with step 1 counted, in both states, giving the figure for the literal base
beside it; correct the comparison paragraph and `author.md`'s route notes the request draws on.
Precedent for the plain wording, should the orchestrator want the sentence itself unmistakable: the
sentence WAY-266 has the guidelines skills carry says "goes through `refine-task` steps 1 and 2
first" (`W/product-guidelines/testing/SKILL.md:79-81`). If the orchestrator rules for the second
reading instead, `SKILL.md:48-49` has to change, so that a session that goes on from step 1 carries
out the file it already read.

Left as it is: the request tells the human that a resume and a hand-over turn get cheaper by 7.5%
and 10.5% and that step 1 does not run there, while agents will run it as they do today; the human
then reads the first real run (task question 5) against a wrong baseline.

## Minor

### 2. The opener of step 6 switches off the critique's run but not its question to the human

**Anchor:** `W/project-level/plan/skill/critique_plan.md:3-5` against `:17-18`;
`C/reports/assessment.md:26` (row L34-L37).

**To paste:** In a dispatched turn, "goes back to the human" at step 6 stands with no qualifier; the
opener speaks only of running the critique. Add that clause to the opener, and step 6 to the row.

**Why I report it:** `critique_plan.md:17-18` says a correction changing a human's answer "goes back
to the human". The task's criterion names asking the human at steps 5-7. The openers of steps 5 and
7 switch that off in words; the opener of step 6 does not, and the row for lines 34-37 says the
bullet reaches steps 5 and 7 only. It is not a lost rule: the opener names `delegated_mode.md`,
which the turn read first and which says "Return every human question" and "Do not speak to the
human". So the file does reach step 6 and the criterion is met; the point is that this one sentence
relies on the agent's memory where the other two steps have the words. Cost of the fix: a clause.
Left: a dispatched agent at step 6 has one unqualified sentence against one rule read earlier.

### 3. For a reader from `lead-project`, the pointer in the reading file names a bare `SKILL.md`

**Anchor:** `W/project-level/plan/skill/reading_definition_and_plan.md:3-4`;
`W/project-level/lead/skill/SKILL.md:30-31`.

**To paste:** A reader who comes from `lead-project` has another `SKILL.md` in mind. Write "the
`SKILL.md` beside this file".

**Why I report it:** This is a consequence of what To do 3 and 4 mandate, named so: the lead's
sentence now reaches the reading file and not lines 81-83 and 105-106, which stay in the plan's
`SKILL.md`. Three of the four sentences it loses it holds otherwise (`lead/skill/SKILL.md:33-34`
checks the original whole files, `:84` runs `plan_check.py` after changes). The one it holds only
through the pointer is "Selection is no reading cap; read a small file whole where useful". The
opening sentence of the reading file is there for this reader (`assessment.md:36`), and it names
`SKILL.md` with no address, while the lead's own file bears that name and has no such heading.
Cost of the fix: three words. Left: the lead may not open the plan's file and keeps a cap the base
ruled out.

### 4. The step 0 condition lists two sources where "named" alone would cover a third

**Anchor:** `W/project-level/plan/skill/SKILL.md:42-43`; `C/reports/assessment.md:70` (proposal 6).

**To paste:** "When an existing plan is named, read ..." selects all that the listed wording selects,
and also a plan named by a skill or a document that sends the session here. The listed sources add
nothing.

**Why I report it:** I confirm the author's reading (see "Answers to what the author asked") for the
two sources it names. A third exists: `W/project-level/task/skill/project_plan_task.md:8` returns a
finding "to `plan-project`", and the recorded recheck `9baf7986` was a call the session made itself
from `refine-task` (transcript line 823). There the human had named the plan in the session's first
message, so the condition holds. It would not where a task document is what names the plan: the
condition fails, "Otherwise begin with step 1" takes over, and the session starts as a new breakdown
with `existing_plan.md` unread. The base's literal condition did not select that case either, so
this is no route lost by the letter, but in the base the bullet stood in view and now it does not.
Cost of the fix: twelve words fewer, and proposal 6 falls away. Left: a rare route with a wrong
start; `plan_check.py` and the plan's status would show it soon after.

### 5. Corrections to the assessment's proposals and two lines

**Anchors:** `C/reports/assessment.md:63`, `:65`, `:16`, `:14`, `:24`.

**To paste:** The list says the repetitions with the template "are 2-5"; there are more. Proposal 1
is labelled reword and proposes a removal. The proposals stand in no rows of their own.

**Why I report it:**

- `assessment.md:63` states the repetitions as closed, and To do 9 asks for them. Not listed:
  `template.md:128` with `place_questions.md:10-11` (a move of the writer is the human's);
  `template.md:129-132` with `assign_entries.md:7-12` (the rule itself; proposal 2 cites only the
  item's format at `:162-168`); `template.md:143-145` with `place_questions.md:5-6` (a line in the
  change log for a moved question); `template.md:171` with `hand_over.md:7-9` (items shown at
  handover). No rule is affected; the human decides on a shorter list than exists.
- Proposal 1 (`:65`) is labelled **reword** and says "Remove the sentence"; `judging.md` has
  remove.
- The handoff asked for proposals "in rows of their own kind"; the table has none, and only the row
  L6-L12 refers to one. To do 9 itself is met by the list after the table.
- `:14` leaves PR #51 out of the records searched with no word. `gh pr view 51` shows 0 comments and
  0 reviews, so it can say that it has no remarks. `author.md:117` reads as if the search had failed.
- `:24`: "cost: 277 words of the file in the 3 uses that are not dispatched" has it backwards; those
  three uses do not read the file, and the words are what they save.

## Declined to judge

- Whether a narrow turn will read only its own steps or everything: the task settles it in question
  1 and measures it at the first real use (question 5).
- Whether the repetitions with the template should go: To do 9 makes them the human's, as proposals.
- "each skill named below" and "cited below" (`SKILL.md:12`, `:17`), which now reach text standing
  in files beside the skill for a session without the entry point: the sentences stand unchanged,
  and the skills of the series rebuilt earlier keep the same words
  (`W/product-guidelines/testing/SKILL.md:21`), so it is a wording for the series, beyond this task.
  `assessment.md:22` does claim the paragraph covers those files; it does so only by a loose reading.

## Answers to what the author asked

- **Widened step 0 condition (choice 4): confirmed, by what it selects.** Base: "When the human names
  an existing plan". A dispatched turn is always on an existing plan: `lead-project` requires a
  handed-over plan (`lead/skill/SKILL.md:33`) and the conversation template's header holds `Plan:`.
  The base sent such a turn through the bullet by its own text ("Verify its product, plan and
  process pin", "run the existing whole-original checks", "start at step 0 and recheck the plan").
  The new words select those turns and no new breakdown, so no route is added. See finding 4 for the
  source left out.
- **Lines 102-104 in the reading file (concern 1): confirmed.** "Expand whenever ..." is close to a
  rule of working, and the row's *Needed* cell says as much. But To do 3 moves the section and names
  what stays, WAY-256 leaves the boundary to the row, and the reach holds: on every walked route the
  reading file is read at step 0 or 1, before any edit of steps 2-4, so no step reaches an edit
  without it. Moving them would add about 55 words to every use for no reach gained.
- **`uncertain` in the guidelines condition (choice 7): no route lost.** It widens only a read.
- **Concern 3:** finding 1.

## To do and acceptance

| Item | Result | How checked |
|---|---|---|
| To do 1, the judgement and the rebuild | met | sections in the order of `judging.md`, verdicts keep and move only; each step and variant has its file, and step 0's bullet 1 and bullet 3 stay as one instruction each |
| To do 2, steps 0-7 and the heading | met | numbers unchanged; heading in `SKILL.md:23`; lines 25-46 byte-identical in `delegated_mode.md` by `diff` |
| To do 3, the reading section | met | file named at steps 0 and 1; lines 81-83 in `SKILL.md:31-33` |
| To do 4, the lead's sentence | met | one sentence in the diff, the only change there |
| To do 5, existing plan | met in the file; effect misstated | `existing_plan.md`; finding 1 |
| To do 6, guidelines file | met | lines 115-127 byte-identical in substance by `diff`; named at step 2 with one condition, equal in both places |
| To do 7, the table | met | 34 rows, see below |
| To do 8, word counts | **not met for routes 3 and 6** | every figure holds as arithmetic; finding 1 |
| To do 9, proposals | met, list incomplete | finding 5 |
| Acceptance 1, no rule lost or changed | met | own comparison, below |
| Acceptance 2, conditions compared, switch-offs named | **not met for one sentence** | finding 1; the other 35 new clauses hold |
| Acceptance 3, condition of the guidelines file | met | all five matters; compared by what it selects, below |
| Acceptance 4, pointers name step or variant | met | "beside this skill" and the step's heading at every pointer; `delegated_mode.md` by the base's own condition |
| Acceptance 5, the review's walk and row comparison | done | below |
| Acceptance 6, fragments needed in several places | met | `:125`, `:135`, `:142-143`, `:160-163` in `write_and_check.md:15-22`; `:59-61` in `assign_entries.md:13-15`, `hand_over.md:12-14`, `existing_plan.md:12-14`; `:105-106` in `SKILL.md:35-36` |
| Acceptance 7, delegated file reaches steps 5-7 | met | three openers, three clauses of `SKILL.md`; see finding 2 |
| Acceptance 8, description and Python unchanged | met | lines 1-21 of `SKILL.md` same hash in both commits; no non-Markdown file in the diff |
| Acceptance 9, counts after the last change, helper compares each figure | met | `SKILL.md` last written 09:01:00, `word-counts.md` 09:04:46, commit 09:05:00; `verify_counts.py` read: it recounts each file line |
| Settlements to record, projected entries | none carried, none written | the diff touches no file of `foundations/` |

## Rule preservation, by my own comparison

Method: base and rebuilt files split into clauses, whitespace normalised, list markers and headings
dropped, with my own script (no helper of the author's). 144 clauses of the base, 3 not verbatim, the
same 3 the author names, each a pointer reworded: lines 52-54, 59-61 and 69. 36 clauses are new. I
read all 36 by hand for what they select and switch off:

- 3 reworded pointers: the same rule with a file for a section. Selection unchanged, apart from step
  0, answered above.
- `SKILL.md`, delegated pointer: same condition as the base's, verbatim. Switches off nothing.
- `SKILL.md`, steps 0-7 pointers: the step 1 pointer is finding 1; the others are unconditional or
  repeat a condition checked here.
- Step 2 condition, compared with lines 115-127 by what it selects: "missing" selects line 115;
  "first file of a kind" lines 119-120; "kind that has files but no entry in the guidelines index"
  lines 120-121; "first test of a level" lines 121-123; "extend existing guidelines" lines 123-125.
  "uncertain" adds a read and loses nothing. A scoped departure (line 118) matters only where a file
  is absent; `reading.md:45-48` then reports nothing missing, so no task is placed and the rule has
  nothing to bear on, and where only part is departed from, "missing" still holds. No route is added
  and none is lost. `cut_tasks.md:8-12` keeps the place of the bullet: "before the next bullet".
- Three openers: the condition is the base's. Each switches off one act, for a dispatched turn, and
  no item below it otherwise; the base's bullets 2 and 3 did the same.
- List in `write_and_check.md:14-22`: restates lines 125-126, 135-136, 142-143, 160-163 with no gain
  or loss of meaning. "never silently enlarged into the plan" for "never silently enlarge it" keeps
  WAY-218's "the plan silently enlarges the approved scope". The list does not read as closing the
  generic sentence above it, which stands.
- `assign_entries.md:13-15`, `hand_over.md:12-14`: restate lines 59-61; "the bullet above" and "the
  first bullet" point to the right bullets (the opener is no bullet).
- `reading_definition_and_plan.md:3-4`: finding 3. `existing_plan.md:15-16`: finding 1.

Foundation: the change does what WAY-256 and WAY-265 say, apart from what is reported above.
WAY-151's three sentences stand across `SKILL.md`, the reading file and `critique_plan.md`. WAY-156's
"plan-project step 0" stands. WAY-230's showing at handover stands. No invariant test changed.
`skill-entry-points` and `derived-file-content` are unaffected: no `SKILL.md` was added and the
description is unchanged.

## Assessment against the base and the files

Own script, no helper of the author's: each row's link range, quote and word figure read from the
base. 34 rows, 0 quotes differ, 0 links differ, each of the 179 nonblank lines in exactly one row,
"Words in the base" equal in each row and summing to 2344. Each row's *New place* compared with the
place, bullet by bullet: every sentence of each row stands where the row says, apart from the rows
that say they reword, and the bullet numbers hold. Findings 2 and 5 are the rows' other lines. The
template lines the proposals cite hold. The 13 lines of "Text added" hold, apart from the one in
finding 1.

## The walk

As an agent that reached `SKILL.md` by its path, no entry point, from the first line to the last
step's file.

**Route 2, new breakdown with the guidelines file.** `SKILL.md`: delegated pointer, condition false;
rules across the steps read. Step 0: template and "How a skill asks"; no plan named; "Otherwise begin
with step 1". Step 1: `read.md`, reading file. Step 2: `cut_tasks.md`, whose third bullet sends to
`guideline_tasks.md` before task numbers are given, the base's order. Steps 3, 4, 5 (opener inert,
list read), 6 (critique runs), 7. Falls away: `delegated_mode.md`, `existing_plan.md`. Stays:
everything else. Rule not reached: none.

**Route 3, resume of a draft from step 5.** Step 0: template, "How a skill asks"; plan named by the
human; `existing_plan.md` and the reading file; `plan_check.py` on the whole file; inventories; the
draft goes on from step 5; the last bullet has `read.md` read (finding 1 on what that does). Step 5:
`write_and_check.md`, whose list gives the questions of steps 2-4 unread. Steps 6, 7. Falls away:
`cut_tasks.md`, `guideline_tasks.md`, `assign_entries.md` (unless `plan_check.py` reports a pair,
when `existing_plan.md:12-14` names it), `place_questions.md`, `delegated_mode.md`. Rule not reached:
none the route needs. An answer at step 5 that adds a task needs step 2's rules; step 2's heading and
pointer stand in `SKILL.md`, and the template's *Goal* column carries the main one.

**Route 4, human's correction, a split of a handed-over plan.** Step 0 as route 3; "a plan handed
over changes only as its change log records"; `read.md`. Step 1: the pointer gives nothing (finding
1). Step 2: `cut_tasks.md`, and the guidelines file where its condition holds. Step 3:
`assign_entries.md`. Step 4 only where a question moves. Steps 5, 6, 7; `hand_over.md:10` has the
correction logged, and `existing_plan.md:7` said so at the start. Falls away: `delegated_mode.md`,
`place_questions.md` unless a question moves, `guideline_tasks.md` unless its condition holds. Rule
not reached: none, given finding 1.

**Route 5, narrow dispatched turn, one change.** `SKILL.md`: delegated pointer, condition true:
`delegated_mode.md` first, then the conversation file and `conversation_template.md`, all turns, the
requested change. Step 0: plan named by the conversation file; `existing_plan.md`, reading file,
`read.md`. 5a: steps 1 (finding 1), 3, 5; `write_and_check.md` opens by routing each question through
the conversation; the question lists of steps 2 and 4 reach the turn there. Falls away: `cut_tasks.md`,
`guideline_tasks.md`, `place_questions.md`, `critique_plan.md`, `hand_over.md`. The critique is
requested as `delegated_mode.md` gives; the handover goes through the conversation by its second
bullet. 5b reads the rest; nothing there acts, because the openers of steps 5-7 hold. In `critique_plan.md`,
see finding 2. Rule not reached: none. The risk question 1 named, a narrow turn that skips step 3,
stands and is the task's to carry.

**Route 7, recheck after the definition's gate, dispatched.** As route 5 to step 0. `delegated_mode.md`
bullet 4 starts at step 0. `plan_check.py` reports the fingerprint; `existing_plan.md:10-11`: verify
approval and go on, no second gate; the plan "is checked against it from step 1"; `read.md`. Step 1:
the pointer gives nothing (finding 1). Steps 2-7 by their pointers, openers at 5-7; the critique
requested; the fingerprint updated with its logged reason, and results returned, by bullet 4. Falls
away: `guideline_tasks.md` unless its condition holds. Rule not reached: none, given finding 1.

## Word counts, recomputed

Own script over commits exported to the scratchpad, sections cut by heading, sums by route. All 175
per-file figures, all sums and totals of the 8 route versions and all percentages hold, 0 differ.
Each route's file list matches the reading it states, apart from what finding 1 says of routes 3 and
6. `wc -w` on `SKILL.md` at the base gives 2344, on the twelve files 3045.

## Checks run

| Command or method | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | the head given |
| `git diff 2f51e6c..db3845c`, `git show --stat db3845c` | 0 | 13 Markdown files; `foundations/`, `.claude/`, `.agents/` and Python untouched |
| `python -B <scratchpad>/rv/check_assessment.py` (own) | 0 | 34 rows, 0 bad, 179 lines each once, words sum 2344 |
| `python -B <scratchpad>/rv/compare_all.py` (own) | 0 | 144 clauses, 3 not verbatim, 36 new |
| `diff` of base 25-46 with `delegated_mode.md`; of base 115-127, markers stripped, with `guideline_tasks.md` | 0, 0 | identical |
| hash of lines 1-21 of `SKILL.md` at both commits | 0 | identical |
| `git ls-files --eol project-level/plan/skill` | 0 | all LF |
| `python -B <scratchpad>/rv/check_counts.py` (own) | 0 | 175 file figures, 8 routes, 0 differ |
| `python -B tools/verify_counts.py reports/word-counts.md` (author's, run as a second reading) | 0 | 271 compared, 0 differ |
| `python -B instruction-files/check_instructions.py .` on both exported trees, outputs compared | 0, 0, diff 0 | 0 error, 1 warn, 3 info, the same |
| `gh pr view <n> --comments --json comments,reviews` for 50, 51, 52, 59, 60, 62, 64, search for the skill's names | 0 | 51 empty; only 50 hits, on `task-cycle/plan/SKILL.md`, another file, as the author says |
| search of `W` for the section names and `plan/skill`, outside the skill | 0 | only `lead/skill/SKILL.md:31` and the entry points and installer, which name `SKILL.md` |
| manual: routes 2, 3, 4, 5, 7 | n/a | above |
| manual: 36 new clauses, 34 rows | n/a | above |

Read, not run: `C/head-gate.log`, `C/head-gate.exit`, the orchestrator's gate on this head: exit 0,
615 tests in 8 directories. Not run: the whole gate (the orchestrator's) and the focused suites,
since that log covers them. Nothing else was left unrun. The review changed nothing in the reviewed
worktree: `git status --short` was empty after the checks.

## Foundation read

Selected by "Reading the foundation" for the part `project-level`.

Read whole, 70 decisions: WAY-09, 13, 35, 38, 89, 100, 101, 102, 106-118, 120-127, 134, 137-140,
142-147, 150-156, 165, 166, 172, 200, 214-218, 230, 238, 242, 247, 256, 257, 259, 265-270, 277. That
is every decision whose *Scope* names `project-level` (63), every decision of the task's *Decisions in
play*, and every decision the moved text cites.

Part map entry `project-level`. Invariants whose *Part* names `project-level` or `every`, each whole,
among them project-plan-form, project-plan-check, skill-entry-points, instruction-file-imports,
repository-file-location, outbound-link-reach, derived-file-content. The glossary whole (short). The
fact `claude-skill-nested-references`.

Not read whole: the other 167 decisions, among them those the read ones link to and the work did not
need: WAY-21, 33, 128, 148.

No invariant test is altered. The change writes no foundation entry, and none it read has stopped
matching.

## Reach beyond the dispatch

- `~/.claude/projects/C--Storage-repos-loop2/9baf7986-d1d2-4c5c-acc2-99de91dc6e13.jsonl`, the recorded
  recheck of the task's Context: how that session named the plan, for the step 0 condition (finding 4).
- `W/product-guidelines/testing/SKILL.md:75-81`, for WAY-266's wording, as precedent (finding 1).
- `W/project-level/task/skill/project_plan_task.md`, `W/project-level/lead/conversation_template.md`,
  `W/product-guidelines/reading.md`, `W/project-level/plan/template.md`, `W/instruction-files/judging.md`,
  `W/instruction-files/kind_skill.md`: incoming references, the proposals and the method of the table.
- The cycle's `author-handoff.md` and `cycle.md`, for what the materials were asked to hold.

## Searches not found or unclear

- The handoff of the author says proposals stand "in rows of their own kind"; To do 9 asks only that
  the request give them. I read the first as a form, not a requirement (finding 5).
- The task's question 3 says "czyta go" and its reasons speak both of what an agent saw and of the
  foundation in mind: unclear which it requires. Finding 1 rests on that.
- The first search of the invariants was cut at 250 lines; I read the rest of the file directly.

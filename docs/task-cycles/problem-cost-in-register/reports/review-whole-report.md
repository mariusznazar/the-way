PASS 18b4a3fb99df3d95e939d1c348fe84f2bc50e0c0

# Review of the whole change, problem-cost-in-register

Range `55afa8e57aa1b83c77108576a36642722e0dda15..18b4a3f` (two commits, `f5e1d45` and `18b4a3f`);
`git rev-parse HEAD` is `18b4a3fb99df3d95e939d1c348fe84f2bc50e0c0`, the head given. Method:
`task-cycle/review/SKILL.md` and `whole_change.md`, read whole. One-author route, no plan, no slices:
this review is the only one the change gets. Blocking findings: 0. Minor findings: 4 (3 within the
task, 1 outside it). Out-of-scope findings besides: 1 (an open point for the human, no code).

## Verdict in short

Every item of *To do* 1-4, the answers of *Questions to settle* and *Settlements to record* rows 1-3
are carried out by the commits. The trust boundary holds against the crafted input I tried. The
author's three points to judge come out as follows: the exit-2 rule for a missing heading, table or
column is required by WAY-344 and lies within the task; the one new result section is a fair reading
of "przy sprawach"; the foundation entries fit their rows.

## Findings

### Critical

none

### Important

none

### Minor

1. **Stale count of tables in the template** (within the task). `process-audit/problem_register.md:39`
   still reads "Text outside the four tables is not read; write there what you like." The same file
   now says five tables six lines above (line 29: "reads the five tables below"). A user who adapts
   the template reads two counts in one section and may take the new table *Costs of an occurrence*
   for text outside the tables. Evidence: `grep -n "four tables" process-audit/problem_register.md`
   gives line 39 only. Fix: "five tables".

2. **A test whose name claims more than it checks** (within the task).
   `process-audit/test_audit_count.py`, `test_a_column_in_another_order_or_an_extra_one_is_refused_not_missing`
   (the test just after `test_every_field_missing_from_the_register_is_named_in_one_error`): it builds
   only the extra-column header (`| Issue | Note |`); no case puts the columns of *Problems* in
   another order. The behaviour is right (my scratch run `col_swapped`, Cost and Weight swapped:
   exit 1, table refused, result written, stderr `... does not have the header row the template
   gives`), but a change that turned a reordered header into exit 2 would pass this test. The test
   exists to guard exactly the line "no field is missing, so the table is refused". Add a reordered
   case to it, or rename it.

3. **Reflow damage in the edited WAY-330** (within the task). `foundations/decisions.md`, *Rationale*
   and *Rejected* of WAY-330 (about lines 10968-10985 at the head): after the in-place edit three lines
   run to 123, 109 and 110 characters ("cycles itself would repeat it every week, and could repeat it
   differently. A template lets another user of the-way keep the", "problem to its fix would have to
   be rebuilt each time; the-way taking over the review of the remarks of cycles") where the rest of the
   log wraps at about 100. Cosmetic only; the words are right. Evidence: `awk '{print length}'` on
   lines 10960-10972 and the diff of `18b4a3f`.

4. **The exit code of the row labels of the two level tables differs from the letter of WAY-344**
   (outside the task: the task mandates it, and I name it so, as `review-change` section 3 asks of a
   mandated defect). WAY-344 lists "a row label" among the fields and, for a changed script's reworked
   reading of a file, asks exit 2 for every field. `audit_count.py` ends with exit 2 for a missing
   heading, table or column, but for a missing or doubled level in *Weights* or *Costs of an
   occurrence* (`read_register`, the `sorted(...) != sorted(COST_LEVELS)` check) it gives exit 1, a
   written result and the register error. The task says exactly this ("tak jak dziś tabelę wag bez
   czterech poziomów wagi", To do 2), and WAY-344's purpose, no quiet pass, is met: the error is on
   stderr and in *Unknown values*, the table is refused, nothing is read as empty (scratch cases
   `costs_missing_level`, `costs_dup_level`: exit 1, error naming the table). I do not ask for a
   change; the error names the table, not the level, which is the one gap against "names the field".
   The human may rule whether WAY-344 or the task prevails here; that is a decision for the human, and
   if WAY-344 prevails the fix is small (raise instead of refuse, for both tables, and two test
   expectations).

### Out of scope, not a finding on the change

- WAY-339 and the cost levels (the author's open point). WAY-339 names the list of classes, the price
  list, the stage report and the reviewer's instructions as starting a new series, not the meaning of
  a cost level. Today the count compares no cost level across time, so a user who adapts a meaning
  starts nothing that is measured. If a later task compares the cost levels of one week with another,
  WAY-339 has to be revisited then. Nothing to do in this change.

## Judging the author's points

1. **Exit code of a missing field.** Within the task. WAY-344 binds "in a script that a change
   changes, the whole reading of each file whose way of reading the change reworks — every field of
   that file", with exit 2, and exempts only a script whose purpose is to check a file's form;
   `audit_count.py` is not one. The change reworks the reading of the register (new table, new column,
   new cell count), so the old headings, tables and columns come under exit 2 as well, and the task's
   Context says that a missing field "kończy się błędem, który je nazywa (WAY-344)". The old exit 1 for
   a missing table was the earlier author's form: no decision names it (the author searched; I found
   none either, see "Searches"). The docstring, the skill's exit-code list (`SKILL.md:109-116`) and the
   tests moved with it, and the old test of exit 1 was replaced, not weakened (the replacement asserts
   exit 2, the field named, an empty results directory, six variants). Row labels: Minor 4 above.
   Verified by scratch runs: `no_costs_table`, `costs_in_fence` (heading only inside a code fence),
   `empty`, `old_form`: exit 2, nothing written, one `Error:` line naming every missing field, no
   register text echoed (the names come from the constant table of headings and columns).
2. **Where the result shows the cost.** The section `## Cost of an occurrence by issue` (Issue, Fate,
   five levels, Refused rows; one row per issue of the register, in the register's order, for fixed,
   open and dropped alike) answers the task: To do 3 and the answer of *Questions to settle* say
   "przy sprawach", against "przy cyklach", not "in the existing three tables"; WAY-346 says "for each
   issue, fixed, open and dropped". The cost of the choice is two tables per issue for the reader; the
   skill says so and quotes the row with its header at steps 2 and 3 (`SKILL.md:147-156`). Fifteen
   repeated columns in three tables would have cost more. One property to know, not a defect: the row
   counts a problem by its row, whether or not its cycle is read, and does not split fixed issues by
   the pin; its total can therefore exceed the *Problems* column of the same issue in *Fixed issues* or
   *Open issues*. The section's paragraph says "A problem counts by its row, whether or not its cycle
   is read", and the test with the repository `ghost` pins it.
3. **Foundation entries.** WAY-345 (row 1): the binding sentence carries the row (five fixed levels,
   each dearer, highest level reached, user adapts only meanings); *Rejected* holds the three ways
   the question's *Not chosen* keeps, with their reasons; *Based on* and *Origin* `none` fit
   (`elements/decisions/template.md`: the human's answer is no outside source; the reasoning is in the
   entry). WAY-346 (row 2): carries the row, *Rejected* holds the task's two ways with reasons.
   Glossary `cost of an occurrence` (row 3): one sentence, *Not* names the money cost of a cycle by
   `WAY-337` in backticks, the carrier the glossary template allows. The in-place edit of WAY-330 is
   within the task: *Decisions in play* lists WAY-330 with "Zmiana, którą wprowadza zadanie: rejestr
   trzyma ... także koszt jednego wystąpienia ... a audyt nie nadaje go sam"; the edit says that and
   nothing more (binding sentence, *Verification*, *Rationale*, *Rejected* say "class, weight and cost
   of an occurrence"). The edit of its heading question follows from the binding sentence (the question
   would otherwise ask less than the entry answers); I judge it within the task, and the request should
   list it for the human at the merge. WAY-345 and WAY-346 as separate entries rather than a widening
   of WAY-333 or WAY-336: the author's reasoning (one entry, one question) is sound and the rows say
   "decision" in the plural. One arguable point on the form: the *Rationale* of WAY-345 says "A scale
   the counting command knows in order lets it count the levels as a scale"; the template asks the
   author's own *Rationale* to name no script or what the process's tools do today. The sentence is the
   source's reasoning (*Not chosen*: "polecenie liczące nie zna kolejności poziomów") turned into
   rationale, and WAY-337 and WAY-342 carry similar wording; I do not grade it.
4. **Unread material of the author.** I read the changed parts of `test_audit_count.py` through the
   diff and the whole file's tests ran green; I read the `process-audit` entry of the part map and all
   invariants whose *Part* is `every` or `process-audit` (none has `process-audit`); see "Unread
   material" for my own gaps. No test outside `RegisterCount` needed a change (the helper
   `problem_row` gained `cost="nothing"` and is used by `Run` and `ProcessVersions` too; they pass).
5. **Open points.** Both are covered above (Out of scope for WAY-339; the WAY-330 heading edit within
   the task).

## Against the task, point by point

- To do 1: the template has the column after *Weight*, a table `## Costs of an occurrence` with the
  five levels and the meanings of the task's list (compared word by word with the task's *Questions to
  settle*), and prose that the user adapts meanings, never levels. Met.
- To do 2: `COST_LEVELS`, `Problem.cost`, 8 cells per row, refusal "the cost of an occurrence is not
  one of the five levels" by the same path as an unknown weight, level table checked as *Weights* is
  (`read_register`). Met; scratch `costs_extra` (a sixth level row): exit 0, only its row refused;
  `costs_missing_level`, `costs_dup_level`: exit 1 with the register error.
- To do 3: met, see point 2 above. Literal expected rows in
  `test_the_problems_of_each_issue_are_counted_on_each_level_of_the_cost_of_an_occurrence` differ from
  the weights on purpose, include a problem with no issue (in no row) and an unread repository.
- To do 4: `SKILL.md` quotes the cost row beside each issue (steps 2 and 3), holds the rule "material,
  never a priority" (WAY-346, WAY-336), updates the exit codes. No priority, order or score is set from
  the cost. Met.
- Questions to settle (3 answers) and *Settlements to record* rows 1-3: carried out, nothing invented
  beyond them. The column order (cost beside weight) and the header word are the author's choices,
  recorded in its report.
- Nothing added that nobody asked for besides the WAY-330 edit (within the task) and the exit-2 rule
  (required by WAY-344).

## Trust boundary: `process-audit/audit_count.py`

Hostile register input, run end to end against the head with a throwaway locations file in the
scratchpad (script `scratchpad/rv/run_cases.py`, 16 cases): a cost cell that is no level (`Steps`,
`STEPS`, empty, a weight word, `steps` + ESC sequence, `st|eps`, `steps` + U+2028, U+202E + `steps`);
control characters and U+202E in the *What* cell; a level missing, doubled, extra; the heading of the
new table absent, written twice, only inside a code fence; the new column absent, swapped, with an
extra column beside; the old form of the register; an empty register; CRLF line ends. Results: every
bad cost cell refuses its row (reason text is fixed, never the cell), `at least n` in the issue's row
of the new section, **no unprintable character in any result** (checked over the whole result file for
code points below 32 other than LF, DEL, U+2028, U+202E), all cells that carry register text reach the
result through the existing `cell`/`display` path or are issue names the code has already validated
against the name pattern, fates validated against the closed list. Exit codes as the section above
gives. A register that does not read never gives a traceback.

## Declined to judge

- The user's own register copy and the nightly session's rules (the task's *Human actions*; the
  orchestrator told me their absence is no finding). Consequence the author named and I confirm: until
  the user's register has the new column and the table, the nightly count ends with exit 2 and the
  line naming them.
- The request's list of the WAY-330 edit for the human: the orchestrator's step.
- Whether the old exit 1 for a missing table had any consumer outside the repository (the nightly
  scheduler's wrapper): not visible from the repository; the skill is the only reader inside and was
  updated.

## Checks run

| Check | Command / method | Result |
|---|---|---|
| Head and range | `git rev-parse HEAD`; `git log --oneline 55afa8e..18b4a3f`; `git diff --stat 55afa8e..18b4a3f` | exit 0; head is `18b4a3f...`, 2 commits, 6 files, 406 insertions, 71 deletions |
| Tests of the part | `python -B gate/run_tests.py process-audit` (from the worktree, background) | exit 0; 129 tests OK, 263.8 s |
| Foundation check | `python -B elements/common/foundation_check.py` | exit 0; `0 errors` |
| Hostile and shape cases | `python -I scratchpad/rv/run_cases.py` (16 registers, each run through `process-audit/audit_count.py --repository the-way --today 2026-11-13` against the worktree as repository, results in a directory outside it) | exit 0; exit codes of the cases: 0 (ok, badcost_ctrl, what_ctrl, costs_extra, crlf, cost_cell_empty_nl), 1 (costs_missing_level, costs_dup_level, costs_heading_twice, col_swapped, col_extra), 2 (no_costs_table, costs_in_fence, old_form, empty) |
| Worktree untouched | `git status --short` after the runs | empty |
| Stale count | `git grep -n -i "four tables\|7 cells\|not 7" -- process-audit` | one hit outside tests: `problem_register.md:39` (Minor 1); one test line asserting the *old* count of a row as a deliberate cell-count case (`test_audit_count.py:1718`, correct) |

Not run: the whole gate (`python -B gate/run_tests.py` with no argument), by the handoff;
`elements/common`, `agent-instructions` and the private-path checks, which the author ran and nothing
since changed (no commit after `18b4a3f`), I did not repeat them. A mutation of the cost check I did
not repeat; the author's mutation (cost check switched off, the cost test fails, restored) I take as
claimed, and the cost test's literals would also fail for a cost read from the weight column (the
weights differ from the costs on purpose).

## Reaches beyond the dispatch

- `elements/decisions/template.md`, `elements/glossary/template.md`, `elements/common/rules.md`,
  `elements/common/way_of_working.md`, each whole: to judge the form of WAY-345, WAY-346 and the
  glossary entry.
- `foundations/part_map.md` lines 105-135 (the `process-audit` entry and its neighbours' lines): the
  part's responsibility, dependencies and trust boundary.
- `foundations/invariants.md` entries whose *Part* is `every` (all read whole, 27 headings checked):
  nothing in the change reaches them (no import, no subprocess, no private path, `SKILL.md`
  description unchanged).
- `the author's own rule file for scripts` (the author's own rule for scripts): for
  writing the scratch script.

## Unread material

- Decisions of my selection (those whose *Scope* names `process-audit`, found by a search of the
  `- **Scope:**` lines and their continuation lines): **18 decisions, 18 read whole, 0 by title only**:
  WAY-328, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346. I
  read the changed WAY-330 whole at the head and read the diff of it. Decisions outside the selection
  that bear on the change and stayed unread: none.
- Guideline files: none apply (WAY-328: the-way's own code and tests are held to no general coding or
  testing guidelines), none read.
- `foundations/glossary.md`: the new entry whole, with the first 40 lines; the other entries I did
  not read, the ones named in the diff and the form entries aside. `foundations/part_map.md`: the
  `process-audit` entry and the neighbouring header lines (lines 105-135), not the whole file.
- `process-audit/test_audit_count.py`: I read the diff whole; I did not read the whole file, of
  which the author read lines 1-220 and 1100-1599. The remainder (the classes `CycleFound`,
  `ProcessPin`, `Remarks`, `Times`, `CraftedInput`, `Locations`, `Cost`, `Run`, `ProcessVersions`,
  `PriceBoundary`) I judged by the green run of the whole file only.
- `process-audit/audit_count.py`: read the diff whole and, outside it, `register_table`,
  `read_register`, `named_rows`, `check_*`, `analyse`'s issue loop, `counted`, `cell`/`table`, `main`;
  not the reading of repositories, prices and times (not touched).
- `process-audit/SKILL.md`: the diff whole and the exit-code and step 2-3 passages; not every step.
- `task.md`, the author's report, the handoff, the `SKILL.md` and `whole_change.md` of this review:
  whole.

## Searches not found or unclear

- A decision or document that names exit 1 for a missing table of the register as a decision (not as a
  description): not found by `grep -rn "exit 1\|exit code 1" foundations/decisions.md process-audit`
  and a search of WAY-330 to WAY-346; the docstring and the skill state it as description only. So I
  treat the old exit 1 as the earlier author's form, as the author did.
- Unclear: whether the user's nightly scheduler wrapper reads the exit code 1 versus 2 of the count
  (outside the repository; see Declined to judge).
- Unclear: whether WAY-344's "row label" reaches the closed level names of *Weights* and *Costs of an
  occurrence* (they are checked, not looked up by); I grade the mismatch Minor 4 and put the question
  to the human.
- The line numbers of the WAY-330 passages (Minor 3) are those of the head; the file is 11,494 lines
  and I cite them by the nearest anchors given.

FAIL ee85f143fd43c01a94f46511680a8c2f3cb87db9

# Review of the whole change — task `project-closure-step`

Range: base `cb5feab98c697354ae79a8f559b950fbf10d0030`, head `ee85f143fd43c01a94f46511680a8c2f3cb87db9`
(`git rev-parse HEAD` gives the head; five commits, 13 files). Route: one author, no spec, no plan, so
no slice and no slice review; no blocking finding comes from a slice. Paths below are relative to the
root of the worktree.

Counts: 5 blocking findings (Important, within the task), 9 Minor findings within the task, 1 Minor
finding outside the task.

The two scripts do what *To do* 5 asks, and the crafted inputs I ran at their trust boundary found no
way to make the reader report a plan closed whose rows the check would refuse. The blocking findings
all lie in the step's file `project-level/lead/skill/closure.md`, its pointer in the lead skill and the
entry WAY-414.

## Findings

### Important

**I1. The agent is never told to say which row holds the closing (*To do* 2, second half).**
Place: `project-level/lead/skill/SKILL.md` lines 88–91 (the last bullet of step 1);
`project-level/lead/skill/closure.md` lines 3–4 and 18–20.
*To do* 2 requires that, where a row stands in a state other than the three final ones, "zamknięcie się
nie zaczyna, a agent mówi człowiekowi, który wiersz i w jakim stanie je wstrzymuje". The instruction
stands only in `closure.md` section 1 ("tell the human which row, by its number and name, and in which
state holds it"). `SKILL.md` has `closure.md` read only "When the reconciliation leaves every row" final,
and `closure.md` opens with the same condition. An agent that follows the skill with one row `in cycle`
and the rest done therefore never opens the file and tells the human nothing; the bullet in `SKILL.md`
only says that the file "keeps a row in any other state … from starting the closing". The requirement
is written and cannot be reached. Before the change the bullet at least told the human that closure was
next. Evidence: the two conditions of reading, quoted above; no other line of `SKILL.md` or of the
files beside it names the row that holds the closing (searched `project-level/lead/` for `holds it`,
`holds the closing` and `which row`: `closure.md` line 19 is the one place).
A one-instruction fragment stays in `SKILL.md` where its pointer stands (WAY-256), so the sentence
belongs in the bullet of step 1.
Contradiction: no

**I2. The closing does not test, before it writes, the second condition the plan check holds a closed
plan to.**
Place: `project-level/lead/skill/closure.md` lines 13–21 (section 1), 29–32 (the scope not delivered),
120–124 (section 7).
A handed-over plan may hold a row `done — goal delivered in task <n>` whose task n is
`dropped — approved by human`: the check reports it only once the `Status:` line reads `closed`
(crafted input "row 2 delivered in dropped task 1": one `closed` finding in a closed plan, nothing in a
handed-over plan). Section 1 starts the closing on the three states alone, section 2 counts the In
scope items of such a row as delivered, the human accepts a preview built on that, the moves, the
closing item and the `Status:` line are written, and only then does section 7 run the check, which
fails. "Resolve a finding before you tell the human the project is closed" does not say how: section 8
has the closing leave the rows as they are, the closing item already written claims as delivered the
scope of a task nobody made (what item G of the task's first question exists to prevent), and the next
session meets a closed plan with a finding, on which step 0 only stops. The step has to hold such a row
as it holds a row in another state, before the preview. `SKILL.md` keeps "Do not equate a dropped task
with a delivered goal", which is no test.
Contradiction: no

**I3. For a projected change of a current entry the search by identifier always hits, and the step
has the hit written as "found".**
Place: `project-level/lead/skill/closure.md` lines 40–52.
The file extends the search beyond the new decisions the task speaks of: "for a change of a current
decision, its number; for an invariant, a glossary term, an environment fact or a part of the part
map, its identifier or term". `project-level/definition_template.md` (lines 328–332) gives a change of
a current decision, invariant or fact the heading of the current entry, and a change of the part map
`<identifier> (changed)`. The entry of that identifier stands in the foundation whether or not the
withdrawn task wrote the change, so the search finds it every time, and the first matching result is
"the entry is found: name it by its identifier". Nothing tells the agent to compare the text at the
commit with the projected text; the file says the opposite of the wording ("no key to search by"). The
closing item and the moved note would then record as present a change that never entered the
foundation, and the next project would not take it up: the loss the step exists to prevent, mirrored.
The same holds for a new invariant, term or fact whose identifier another entry already carries. The
results need a case for an entry that stands under the identifier and does not hold the projected
change.
Contradiction: no

**I4. `closure.md` restates WAY-414 more broadly: the entry gives one key, the file two.**
Place: `foundations/decisions.md` lines 5350–5377 (WAY-414, binding sentence at 5352–5356, *Rationale*
at 5372); `project-level/lead/skill/closure.md` lines 43–47.
WAY-414 binds: the closing searches "by the question the entry's heading holds, which the plan keeps
word for word", and its *Rationale* says "The headings of the entries of the foundation are
questions". Only a decision's heading holds a question; a projected invariant, glossary term,
environment fact and change of the part map have an identifier or a term (definition template, lines
328–332; the glossary term `projected entry` names all five). The file searches "by the question or the
identifier of the entry's heading". The entry is faithful to row 5, but for four of the five kinds it
cannot be followed, and the file does something it does not say. By WAY-263 a file that restates an
entry the change writes more broadly is Important. The sentence of WAY-414 has to name what the file
does (the heading's question for a decision, its identifier or term for another entry), and that
addition to row 5 is the cycle's, to be put before the human.
Contradiction: yes — WAY-414

**I5. A withdrawn task that already has a task document gets a second one, and nothing of the first
travels.**
Place: `project-level/lead/skill/closure.md` lines 65–70 (place 2), 76–85 (section 4);
`foundations/decisions.md` lines 5402–5403 (the violating example of WAY-415, "the closing rewrites
the body of a document a refiner has taken up").
A task that was refined before the human gave it up has a document, linked from the plan's `Document`
cell, with `Status: dropped — approved by human` and `Project relation: plan item: …`
(`project-level/task/template.md` lines 97–99). The file says "Create the task document …" and "A
document the plan's `Document` cell already links for the task is left as it is". The result is two
documents for one task. The file does not say what the new one is called where the old one holds the
name, whether the existing line, which links the old document, is moved to the new one, or that the
new place refers to the old document — which holds the answers the human gave while the task was
refined, and which neither the section in the note of the next project nor the new document mentions.
The task does not settle the case; the author named it in the report (choice 9, "Cost if wrong: two
documents for one task") and wrote the choice into the pair of examples of WAY-415. The human settled
"bez dubla" for the line and for the section (row 6), and the `Document` cell is one of the things the
plan pins to a task, so a second document made in silence is not what a reasonable user expects, and
an agent that follows the file has to guess at the three points above. Until the human settles it, the
smallest change is to have the step show the existing document in the preview and ask which document
stands, and to carry a reference to it to the new place.
Contradiction: no

### Minor, within the task

1. `project-level/test_plan_state.py` lines 502–515 and `project-level/test_plan_check.py` lines
   1083–1096 — two behaviours the scripts' descriptions give are held by no test. (a) With `return 0`
   after the `closed:` line removed from `plan_state.py` (line 685), so that the reader goes on to
   read Git, the three new tests of the closed plan still pass; the description says "no Git evidence
   is read for it". Asserting that the output holds no `repository:` line would hold it. (b) With
   `closed_date` reading the last `Status:` line of the header and not the first, all 136 tests of
   `test_plan_check.py` and the three reader tests pass, though the author's report lists that
   mutation as caught by the second-line test; that test uses rows that are all final, so it cannot
   tell. (c) The comment at line 504 gives exit code 0 as the one "the script's description gives to a
   completed observation"; the description now gives it "or for a closed plan", and a closed plan gets
   no observation. (d) The author's report says each test citing the two invariants was seen failing
   once on the base code; `Header.test_a_closed_date_that_is_no_calendar_date_is_reported` and the
   reader test `test_a_closed_line_off_its_form_or_doubled_is_no_closed_plan` pass on the base code,
   which refuses every `closed` line. The first does fail once the calendar check of a closed date is
   removed from the head code, so it protects what it names.
2. `project-level/lead/skill/closure.md` lines 37–39 — the second case of "a projected entry goes with
   a withdrawn task" never applies in a plan that passes the check: `Written by` names exactly one of
   the realizing tasks (`project-level/plan/template.md` lines 131–132), so where every realizing task
   is withdrawn the writing task is withdrawn too, which is the first case. The sentence is an
   instruction in play that no use needs.
3. `project-level/task_line.md` lines 3–4 and 14–15 — the file still says that it is read by
   `lead-project` only "where it moves a line to ready or brings the dependencies of lines in step",
   and that "a refiner makes one. This is the one place of the rule", while `closure.md` lines 67–70
   has the project orchestrator make a line "as that file gives". The file also leaves the closing to
   guess whether the new line carries the identifier and dependencies of "a task of a project plan"
   (line 26) or none, as "a task that belongs to no plan" (line 37): the task is `source only` and
   leaves the plan.
4. `foundations/decisions.md` lines 5388–5390 (WAY-415) — "from the first refinement of the document
   on, WAY-154 governs it". WAY-154 governs the refinement of a plan's tasks led through
   `lead-project`; the document belongs to a task that left the plan, and a closed plan has no round.
   A reader takes from the sentence that the document is refined through the exchange of WAY-154.
   The precedence itself is warranted (see "The points the handoff asked about", 2).
5. `project-level/lead/skill/closure.md` lines 92–106 — the form of the closing item leaves two things
   to guess. "one nested item for each of the four parts below, the last two reading `none`" against
   "one `withdrawn:` line for each withdrawn task": a plan with no withdrawn task has no line for the
   second part. And the item is "in the language of the plan" while the form gives English labels
   (`project closed`, `tasks:`, `withdrawn:`, `not delivered:`, `projected entries not written by a
   withdrawn task:`) without saying that they are markers kept in English (WAY-142). The last label
   can be read as "entries that another task wrote".
6. `project-level/plan/template.md` lines 116–117 — "A closed plan holds no row in another state" has
   nothing for "another" to refer to; the three states stand 46 lines above, in the header's bullet.
7. `project-level/lead/skill/closure.md` lines 60–70 — section 3 gives the moves in imperatives of
   writing ("add a section about the task to it", "Create the task document") with no word of the
   acceptance in that section; read alone, place 1 is the violating example of WAY-413 ("writes a
   section … as soon as the human has named the note"). Sections 1, 2, 6 and 7 hold the guard, and I
   judge that an agent that reads the file whole cannot take it as leave to write before the
   acceptance; an agent that comes back to section 3 after an interruption meets the imperative alone.
8. One state has two words in the entries the change writes: "dropped" in WAY-142, the invariant
   `project-plan-check` and the plan template, "withdrawn" in the part map, the skill's description,
   `closure.md` and WAY-411 to WAY-415, beside "dropped for good" for one of the three places.
   `closure.md` line 8 defines "withdrawn"; the part map and the description use it undefined.
9. `project-level/plan/template.md` lines 193–197 — the check of a closed plan is cited to WAY-146,
   whose question is what checks a plan "before it is handed over"; the invariant derives it from
   WAY-142. The author named this in the report and left WAY-146 as it is.

### Minor, outside the task

10. `project-level/plan_check.py` lines 877–901 (`check_closed`) — rows that deliver one another in a
    ring pass a closed plan: task 2 `done — goal delivered in task 3` and task 3
    `done — goal delivered in task 2` give no finding, and `plan_state.py` reports the plan closed
    with exit code 0. No task was made, which is the harm the task's last question names, reached by
    an input its two conditions do not cover. The task asks for the two conditions only, so this is
    out of scope.

## The points the handoff asked about

1. **Q1 (which projected entries go with a withdrawn task).** The section reads as the choice gives
   it, and I find it the reading *To do* 3 and item F require: "realizują albo piszą tylko zadania
   wycofane" is "only withdrawn tasks realize it, or the task that writes it is withdrawn", and
   *To do* 4 asks the closing item for "wpisy przewidywane, których zadanie wycofane nie zapisało". The
   reading that asks for every realizing task to be withdrawn would drop the entry a withdrawn task was
   to write while a finished task realizes it. Minor 2 is the only remark.
2. **WAY-415 `narrows WAY-154`.** Warranted: *To do* 3, second bullet, and the answer to the question
   on a task of its own both have the closing create the document and make the line a task lacks, and
   WAY-154 gives both to a refiner; WAY-25 lets the change record it, with those passages in the
   request. I read WAY-140, WAY-153, WAY-145, WAY-269, WAY-107, WAY-124, WAY-126 and WAY-134 whole
   against the closing and found no other collision: the closing is no task cycle (WAY-140), the reader
   still writes no document (WAY-153), the question's line in the plan stays and no writing task
   changes (WAY-145), and a `source only` task may write a projected entry (WAY-126). Minor 3 and 4 are
   what remains.
3. **The second `Status:` line as a `form` finding.** No finding. It keeps the check and the reader in
   agreement, the template now says the line "stands once", the invariant `project-plan-form` holds it
   through the template, and the only plan it newly fails is one with two `Status:` lines above the
   first section, which the reader already refused.
4. **`plan_state.py` on a closed plan.** Meets *To do* 5 and does not go against WAY-153, which speaks
   of what the reader proposes and changes. Minor 1 (a) is the gap. The surface
   `project-plan-state-command` keeps its exit codes; 0 gains a case that no earlier plan could reach.
5. **"closing item".** Right against the glossary: `entry` is the text of the foundation, and the plan
   template already calls the lines of the change log items. The word is used the same way in
   `closure.md`, the template, WAY-412 and WAY-413; no "closing entry" stands in the diff.
6. **`closure.md` and the pointer.** WAY-256 and WAY-265 are kept: the step that only the last session
   of a project reaches stands in a file beside the skill, and `SKILL.md` names it at step 1 with its
   condition. Against *To do* 1 to 7: 1, 4, 6 and 7 are met; 2 in its first half (I1, I2); 3 with I3, I5
   and Minor 2, 3; 5 met. An agent could not follow the file without guessing at the points of I2, I3,
   I5 and Minor 3 and 5.
7. **Size and form.** See "The structure of the code".

## Coverage and source fidelity

*To do*: 1 met (`SKILL.md` description, opening, step 1; entry points regenerated and current); 2 see
I1 and I2; 3 see I3, I5; 4 met (`closure.md` section 5); 5 met (template, `plan_check.py`,
`plan_state.py`, step 0 of the skill); 6 met (section 6, WAY-413); 7 met (section 8).

*Settlements to record*: row 1 → WAY-411; row 2 → WAY-412; row 3 → WAY-413; row 4 → the invariant
`project-plan-check`, with five tests citing it; row 5 → WAY-414 (I4); row 6 → WAY-415. Each decision
keeps the meaning of its row. *Rejected* of each holds only the ways its source question keeps under
*Not chosen* (three, three, one, one, one), and the sentence added to the *Rejected* of WAY-142 is the
one way not chosen of the question on the new state.

What the entries add that no row gives: the five pairs of examples (the author marked them `the
cycle's`); in WAY-411 "that the skill's `SKILL.md` names at the step with the condition under which it
is read" (from *To do* 1 and WAY-265); in WAY-412 the second paragraph (from *To do* 3 and 4); in
WAY-413 "The human's choice of a place … is no such acceptance" (from the way not chosen); in WAY-415
"in the state `refining`" and the clause on the rules of the task place (from *To do* 3), the paragraph
of precedence, and in its pair the violating example "the closing rewrites the body of a document a
refiner has taken up", which no passage of the task gives and which carries the choice of I5; the
edit of WAY-142 and of the part map. The condition of return in row 1 ("wróci do osobnego skilla, gdy
…") stands in the *Rejected* of WAY-411 and not in its binding sentence; the meaning is kept.

Invariant tests the change alters or adds, to be named in the request (WAY-03):
`project-level/test_plan_check.py` — `Header.test_a_status_off_its_forms_is_reported` (cites
`project-plan-form`; four inputs added, assertion unchanged), new
`Header.test_a_closed_date_that_is_no_calendar_date_is_reported` and
`Closed.test_a_second_status_line_is_reported_at_that_line` (`project-plan-form`), and five new tests of
class `Closed` citing `project-plan-check`. I read each against its sentence: they assert the
condition and the row, take their values from the invariant and the template, and no code of the
scripts is made for a test's input.

The author's own-work check names a requirement of the two scripts, and its tests and crafted inputs
would catch it unmet. The change is weakest in the step's file, which no test reaches (testing
guidelines, "Not tested on purpose"), so the check could not catch I1 to I3. The walk: the-way settles
no agent's way to a running product for itself, the author ran the two commands in its place, and the
judgment that the change alters what two commands print and one skill does agrees with the diff.

No reserved choice is taken: the change settles no language, library, store or place to run.

## The structure of the code

- `python -B task-cycle/change_file_sizes.py cb5feab98c697354ae79a8f559b950fbf10d0030 ee85f143`:
  `project-level/plan_check.py` 986 → 1041 lines, `project-level/plan_state.py` 703 → 709,
  `project-level/test_plan_check.py` 1224 → 1309, `project-level/test_plan_state.py` 991 → 1033,
  `project-level/lead/skill/closure.md` 136 (new), `project-level/lead/skill/SKILL.md` 197 → 202,
  `project-level/plan/template.md` 191 → 203, `foundations/decisions.md` 11413 → 11575; 13 files,
  +506 lines.
- The test of the invariant `function-and-file-size` names nothing on the base and nothing on the
  head, so the change pushed nothing over a threshold. The functions the diff reaches: `check_status`
  31 lines, `closed_date` 8, `check_closed` 25, `check` 29, `sources` 34, `main` of `plan_state.py`
  42, against 110. `plan_check.py` stands 159 lines under the 1200 of WAY-385.
- No code is left without a user, and no move out was owed (WAY-365). One name is less true than it
  was: the help of the reader's first argument still reads "original handed-over project plan".
  No finding of structure.

## Declined to judge

- Reopening a closed plan: no step gives it; the task asks for none.
- A closing date later than today, or earlier than the date of handing over: the check accepts both;
  the task asks only for a calendar date.
- Conversation files of a withdrawn task left under `.runs/project-refinement/` at the closing: outside
  the task.
- `plan_state.py` on a closed plan does not look at its second argument (a repository that does not
  exist still gives exit code 0): it follows from reading no Git evidence, and the task asks only for
  the plain statement.
- Whether rows 1, 2, 3, 5 and 6 are decisions or lines of one skill: the human accepted the *Goes to*
  column with the task.
- The plans and the note of the next project named in the task's *Context*: the human's notes, out of
  scope by the task.

## Checks

| Check | Command or method | Result |
|---|---|---|
| Head of the range | `git rev-parse HEAD` | exit 0, `ee85f143fd43c01a94f46511680a8c2f3cb87db9` |
| Sizes of the changed files | `python -B task-cycle/change_file_sizes.py cb5feab98c697354ae79a8f559b950fbf10d0030 ee85f143` | exit 0 |
| Size test on the base and on the head | `python -B -m unittest discover -s agent-instructions -p "test_size_invariant.py"`, in a worktree of each | exit 0 and 0, 4 tests each |
| Tests of the directory | `python -B gate/run_tests.py project-level` | exit 0, 293 tests |
| Foundation check | `python -B elements/common/foundation_check.py` | exit 0, `0 errors` |
| Linter, formatter, size and entry-point tests | `python -B gate/run_tests.py agent-instructions` | exit 0, 52 tests |
| Dead pointers of the skills | `python -B gate/run_tests.py product-guidelines` | exit 0, 14 tests |
| Entry points current | `python -B agent-instructions/skill_entry_points.py` | exit 0, `entry points are current` |
| Tracked private paths | `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` | exit 0 |
| Whitespace of the diff | `git diff --check cb5feab98c697354ae79a8f559b950fbf10d0030..ee85f143` | exit 0 |
| Crafted input at the trust boundary | `python -B review-whole-crafted-inputs.py <worktree of the head> <output> <scratch directory>`, kept beside this report with its output `review-whole-crafted-inputs.txt` | exit 0; see below |
| The new tests on the base code of the two scripts | in the worktree of the head, the two scripts taken from the base, `python -B -m unittest test_plan_check.Closed test_plan_check.Header` and the three new tests of `test_plan_state.Command` | exit 1, 16 failures in 9 tests, as the author reports; two new tests pass (Minor 1 d) |
| Mutation: the reader goes on after the `closed:` line | `return 0` removed at `plan_state.py` line 685, the three new reader tests | exit 0: not caught (Minor 1 a) |
| Mutation: no calendar check of a closed date | `check_status` checking `date` only, `test_plan_check` and the three reader tests | exit 1: caught by two tests, `Header.test_a_closed_date_that_is_no_calendar_date_is_reported` and the reader test of a closed line off its form |
| Mutation: `closed_date` reads the last `Status:` line | `reversed(preamble)`, the same tests | exit 0, 136 tests: not caught (Minor 1 b) |

What the crafted inputs showed, through `plan_check.check` and through `plan_state.py` as a process:

- A closed plan whose rows are final gives no finding, with LF and with CRLF, and with a closing item
  of the form `closure.md` gives in its change log; the reader says it is closed, with a byte-order
  mark and CRLF as well.
- A closed line followed by spaces, a tab, a no-break space, U+2028, a form feed or U+001F still reads
  as closed, and a row `in cycle` under it is reported; a zero-width space after the date, full-width
  or Arabic-Indic digits, two spaces, a tab between the words, a `Z` after the date, en dashes in the
  date, a lower-case label, a leading space or a byte-order mark before `Status:` give `form` and no
  closed plan.
- `closed 2026-02-29`, `2026-02-30`, `2026-13-01` and `0000-01-01` give `form` (no calendar date);
  `9999-12-31` is accepted.
- Two `Status:` lines in either order, a line off its form before a closed one, a closed line in a
  code fence before a handed-over one, and a closed line split from a handed-over one by a bare
  carriage return give `form` at the second line, and the reader exits 1; a closed line inside an
  HTML comment is no `Status:` line, and one below `## Tasks` is not read.
- A row `in cycle`, `Done`, with a hyphen for the dash, empty, `done done`, with an escaped pipe, or
  delivered in a task written with a full-width digit or as `01` is reported as `closed` (and `form`);
  a row delivered in itself or in a task the plan lacks gives `form`; a row delivered in a dropped task
  gives `closed` at that row, also where a third row is delivered in it; two rows with one number give
  `form`. A plan whose every row is dropped passes. A ring of delivered rows passes (Minor 10).
- The reader exits 1 with the finding for a closed plan with a row `in cycle`, a row delivered in a
  dropped task, a doubled line, a date that is no calendar date, non-ASCII digits and a fingerprint
  other than the definition's.

Not run: the whole gate (`python -B gate/run_tests.py` with no directory), by the handoff; Ruff as a
command of its own, since the two invariant tests of `agent-instructions` run it over every part.

## Reaches beyond the handoff and my selection

- `project-level/task_line.md`, `project-level/backlog_place.md`, `project-level/task/template.md`,
  whole: `closure.md` sends the agent to them, and I5 and Minor 3 rest on what they say.
- `project-level/definition_template.md`, the passages on the headings of projected entries (lines
  291–337): to judge the search key of WAY-414 (I3, I4).
- `project-level/plan/template.md`, whole, and `project-level/plan_check.py` beyond the diff
  (`read_table`, `read_tasks`, `check_sections`, `check`, `main`): to see what the closed check gets
  from the rows and whether a writing task is always a realizing one (Minor 2).
- `elements/decisions/template.md`, the lines on *Relations* and on the pair of examples: to judge the
  form of the new entries.
- Decisions outside the handoff's pointers, read whole: WAY-25, WAY-30, WAY-114, WAY-140, WAY-269,
  WAY-19, WAY-03, WAY-69, WAY-17, WAY-235, WAY-394, WAY-395, WAY-143, WAY-144, WAY-147, WAY-230: for
  the precedence, the numbering, the changed invariant tests and the source of the tests' values.
- The files of the user's own rules for scripts and for git, outside the repository, which the
  session's hooks have an agent read before it writes a script or runs git: no part of the review.

## Working copies

All stood under `.runs/review-whole/`: a worktree of the head (`head`) and one of the base (`base`),
both removed with `git worktree remove --force` and `git worktree prune`; a scratch directory `ps` with
a plan and a definition for the reader; the script of crafted inputs and its output; the logs of the
runs; the index of decisions and the list of sections. All were deleted, the directory stands empty,
`git worktree list` shows no worktree of mine and `git status` of the reviewed worktree is clean. Kept
in `reports/` beside this report: `review-whole-crafted-inputs.py` and
`review-whole-crafted-inputs.txt`, which hold no path of the machine. No remainder.

## Unread material

Of the 164 decisions of the index of my selection (47 listed in full, 117 by heading alone) I read 32
whole: WAY-142, 143, 144, 146, 147, 153, 230, 411, 412, 413, 414, 415, 154, 107, 25, 30, 114, 118, 126,
145, 256, 265, 134, 140, 269, 19, 03, 69, 17, 235, 394, 395.

Decisions that bear on the change and that I read by the binding sentences of the index only: WAY-124,
WAY-385, WAY-379, WAY-380, WAY-382, WAY-365, WAY-361, WAY-363, WAY-263, WAY-297, WAY-364, WAY-150,
WAY-213, WAY-113, WAY-33; by heading only: WAY-48, WAY-320, WAY-293, WAY-401. WAY-344: its binding
sentences and *Scope*, not its *Verification*, *Rationale* and *Rejected*.

Guidelines: `guidelines/coding.md`, `guidelines/coding-check.md`,
`guidelines/coding-measuring-report.md` and `guidelines/testing.md` read whole; the four other files
of kinds match neither a touched part with the kind nor the work, and were not read beyond their
headers. The invariants, the part map and the glossary were read whole.

Of the change itself: `project-level/plan_check.py` lines 250–394 and 620–924, `plan_state.py` lines
12–625, and the parts of the two test files outside the diff and the helpers the new tests use, were
not read.

## Searches not found or unclear

- What the closing does where a withdrawn task already has a document: the task, the foundation and
  the files of `project-level` give nothing (I5).
- What "the rules of the task place allow" the closing to change in a line that stands: those rules
  lie outside the repository and were not read; the file does not say which change the closing wants.
- A rule of line width for a Markdown file of a skill: none found; `closure.md` lines 44 and 105 are
  longer than the rest of the file after the last commit, and I make no finding of it.
- Whether the target branch has taken a number from 411 on since the base: the remote-tracking ref of
  the target branch stands at the base here, and I did not fetch.
- `decision_index.py --decision` takes the number with its prefix (`WAY-118`); my first run with the
  bare number ended with exit code 2 and wrote nothing.

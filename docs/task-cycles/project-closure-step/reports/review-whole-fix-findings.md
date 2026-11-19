# Findings of the review of the whole change, for the fix (task `project-closure-step`)

Cut from `reports/review-whole-report.md`, head reviewed `ee85f143fd43c01a94f46511680a8c2f3cb87db9`, in the reviewer's words. Blocking findings first, each with the reviewer's mark of contradiction with the settlements; after them the Minor findings of the review of the whole change that lie within the task, which are fixed in the same round (SKILL.md, "The end of a code review"). The one Minor finding the reviewer marks outside the task (its item 10) is not fixed and is not here.

## Blocking findings (Important)

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

## Minor findings within the task

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

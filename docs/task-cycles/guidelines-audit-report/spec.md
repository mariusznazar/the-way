# Spec — the way: audyt w skillach wytycznych podaje wagę każdego ustalenia i kolejność naprawy

- Task: `.runs/task-cycles/guidelines-audit-report/task.md`
- Open choice: the English words of the scale, of a finding and of a cause; how the audit shows the
  cost of a fix; how rows 1–6 of *Settlements to record* enter the decision log; who merges the
  causes of a task joining code and tests; where each result stands in the task document. The six
  choices of the designer's handoff, and what follows from them where the settled rows meet the
  existing text.

## Intent

The three audits of `maintain-coding-guidelines`, `maintain-styleguide` and
`maintain-testing-guidelines` end today with places in the code and no weight, no common source and
no order. After this change they end alike: every finding belongs to one cause, every cause has one
weight on one scale, the causes stand in one order of repair, the first few are checked again and
put to the human, and the rest stay in the task document, deferred together.

## Goals and non-goals

Goals:

- To do 1–8 of the task, whole, its answers to questions 1–9 and its six rows of *Settlements to
  record*, which this spec takes as settled and does not reopen.
- One text for the end of an audit, reached by all three skills, so that the three cannot drift.
- `charge` leaves the-way; one word for what an audit finds in all three disciplines.

Non-goals:

- Applying the new end in any product (*Out of scope* of the task).
- A periodic audit, or an audit as a skill of its own (questions 8 and 9).
- A new section of the task template, a new status of a task, a number on the scale, a test of the
  text of these files.
- An end for what is no audit: the route of one kind (WAY-216, `coding/kinds.md:6-9`) and the first
  test of a new level (`testing/SKILL.md:98`). A refresh and an extension run the audit as they do
  today and so take the new end (WAY-251); a styleguide with no changed screens has no step 3 and no
  end.

## Constraints

- The task's *To do*, questions 1–9 and rows 1–6 bind this spec.
- A decision holds one to three binding sentences (WAY-05, `elements/decisions/template.md:25`); a
  number stands for one question, and a sentence an older decision answered in passing moves and
  leaves that entry in the same change (WAY-19).
- Each row enters whole, its *Rejected* holding only the ways not chosen its source keeps (WAY-134);
  the entry names what it adopts, where and why, and describes it in its own words (WAY-100,
  WAY-27).
- The changes of WAY-187, WAY-201 and WAY-250 are carried by row 4 and its *Decisions in play*, so
  the human's acceptance of the task approved them (WAY-30).
- WAY-200, WAY-204, WAY-205, WAY-216, WAY-235, WAY-251 stay unchanged; what the linter's and the
  boundaries' results set off today stays (question 5).
- WAY-173: the scale binds the shared file and the skills, never a product's code, screens or tests.
- WAY-174: the human hears each cause by its effect, never by a rule's or a technique's name; a term
  is said in plain words before its first use.
- WAY-256, WAY-265: a step names each file it reads, with its condition, in `SKILL.md`; a later step
  has a file read unless an earlier step did.
- WAY-120: the critique of a complete set of proposals stays, one fresh agent, before the set is
  shown.
- `project-level/task/template.md`: headings, status values and markers stay in English, the rest
  in the document's language; each fact has one home; each sentence of *Context* stands in a list
  item of its own.
- **Trust boundaries.** No file this change touches is one. The part map names
  `project-level/readiness_check.py`, `plan_check.py` and `plan_state.py` for `project-level`, none
  of them touched, and none for `product-guidelines` or `decisions`.

## Decisions

### 1. The words of the scale

The scale is called **weight**, the task's own word (`waga`). A cause *has a weight*; the review of
a change *grades* a finding. The four weights, from the heaviest, each in backticks as a value of a
closed list, as `do not copy` is: **`grave`, `heavy`, `medium`, `light`** — in the task's words,
krytyczna, wysoka, średnia, niska.

- None of them is Critical, Important or Minor, nor uses `critical`, which stands in the glossary in
  `critical flow`. The scale has no link to a critical flow: what a cause weighs comes from its
  stake, and a flaw inside a critical flow is not `grave` for that reason alone.
- The stops' texts and the examples of each discipline are question 2's, in English, kept in
  meaning. `heavy`, `medium` and `light` read as an order with no definition; `grave` tops them.
- **Weight words take no glossary entry.** A reader who knows the field gives them the meaning the
  scale narrows, not another (`elements/glossary/template.md:42-45`); they are defined once in the
  shared file, as Critical, Important and Minor are in `task-cycle/review/SKILL.md:99-103`.
- **To the human.** The human hears a weight in the human's language, as its meaning, with the
  sentence of what it means at first use (WAY-174); in Polish, the task's own words. The file of the
  skill fixes no translation. In the task document the English word stays as a marker, as a status
  does, so a later agent reads it in any product; the sentence beside it is in the document's
  language.

Rejected:

- `critical`, `high`, `medium`, `low` — the task forbids the first; the second and last are also
  the values of the advisory severity the audit of dependencies settles in the same skill
  (`coding/settle.md:24`, WAY-206), so one file would hold two scales in one vocabulary.
- `severe`, `serious`, `moderate`, `slight` — the first two do not order themselves, `severe` sits
  beside the `severity` above, and `moderate` is an advisory value of common tools.
- Words naming the stake (loss, failure, friction, blemish) — no order readable without a
  definition, and each stop covers more than its word.

Cost if wrong: a rename in the shared file and six entries, before any product pins it.

### 2. How the audit shows the cost of a fix

Each cause carries, beside its fix, two plain facts and no score:

- **Removes:** how much of the problem goes with that one fix — its count of places, or what goes
  where a count says nothing.
- **Reaches:** how far the fix goes, one of three literal values, `one file`, `one part`, `several
  parts`, `part` as the part map means it.

Within one weight, the cause that removes more and reaches less stands first. Where the two pull
apart, the agent judges, and the line of the cause it puts first says why in one clause. The fix's
sentence names anything that makes it long despite a small reach. So the human reads where the
order comes from at each line, and a critic can dispute a place in it, with no arithmetic. A count
of places is no number on the scale: question 7 refused turning weights into numbers, not counting.

Rejected:

- Hours or points — figures the agent cannot back, read as measured.
- `small`, `medium`, `large` — a size with no ground to check, and `medium` would mean two things.
- The fix's sentence alone — thirty free sentences cannot be compared, by the human or by a critic.
- A ratio of gain to work — the conversion to numbers question 7 refused.

Cost if wrong: one field of a line, in one file. Its weak point: reach is a proxy for work, which
the clause on what makes a fix long only partly covers.

### 3. The words for a finding and a cause; the end of `charge`

- **`finding`** — one thing an audit found at one place. It is already the word of
  `coding/task_document.md:44`. **`cause`** — the one source of one or more findings, which one fix
  removes; a cause may come from a single finding.
- **`charge` is retired**, as a noun and as a verb, from all it stands in: the eight lines of
  `styleguide/audit.md`, `testing/audit.md`, `styleguide/task_document.md` and
  `testing/task_document.md`, and WAY-187, WAY-201 and WAY-250. The two other hits of the word in
  `foundations/decisions.md` are its ordinary sense and stay.
- **No entry for any of them.** A reader who knows the field gives `finding` the meaning it has in
  the review of a change, in `reading.md` and in an audit: what an inspection found. A definition
  true of one is true of the others, so that is one word with one meaning, and the review's grades
  and blocking belong to the review. `cause` means what `coding/template.md:187` means by it. Under
  WAY-95 neither takes an entry. `weight` is under decision 1. `debt` keeps its entry: it is a
  breach of a rule of the foundation, and a finding of an audit need not be one.

Rejected: keeping `charge` for the screens and tests beside `finding` for code — one thing under two
words in three audits that must end alike; a new word (`fault`, `flaw`) — a third word for no gain;
`cause` alone, with no word for what merges into it — To do 2 needs both.

Cost if wrong: a rename. Cost of the way chosen: the three entries are rewritten anyway.

### 4. Six new decisions, three changed in place

Rows 1–6 enter as **six new decisions, one for each row**, all of *Scope* `product-guidelines`,
`project-level` added to E. Each answers a question of its own (WAY-19), keeps its own *Rejected*,
and fits in one to three binding sentences without losing a clause. The list is under *Foundation
entries*.

The sentence of the limit moves from WAY-187 and WAY-250 to the new decision D, and those entries
lose it in the same change (WAY-19); WAY-201, which holds no limit, only gains the list. So nothing
narrows: no decision goes against another in a narrower area, and each of the three says where the
end of its audit stands.

Rejected:

- **One new decision** — three sentences cannot hold six rows whole; a change to one would reopen
  all, and the *Rejected* of six rows would stand in one entry.
- **Changes of the three decisions alone** — the scale, the order and the top written three times
  drift, and row 1 calls for one scale described once.
- **Fewer entries, rows 3 and 4 joined** — it fits, but their questions and their ways not chosen
  differ, and it saves nothing a reader needs.

Cost if wrong: entries to merge before the merge of the request. Cost of the way chosen: six more
entries in a long log.

### 5. The shared file

**`product-guidelines/audit_end.md`**, beside `reading.md`, headed as the end of an audit. It holds
**all that the three audits do alike**, not the scale alone: the three audits must end alike, and a
step's text repeated in three files drifts. The discipline files keep what only they know.

The unit's interface:

- **Takes:** the discipline's findings, each with its place and effect; for the styleguide its
  category, for coding the `do not copy` files and the trial run's reports, for testing the trust
  boundaries a test of refusal is due at and that have none.
- **Holds, each read at its step:** the scale with an example from each discipline; merging; the
  order with the cost of a fix; going back to check; the top of the list; what is shown and asked at
  step 4; the form of the list; a task joining code and tests; what is checked before handing back.
- **Gives:** the list in *Context* and the top of it for step 4.
- **Says of itself:** read from the checkout or pinned the-way the skill runs from; it binds the
  skills, never a product (WAY-173); a weight blocks nothing.

Each of the three `SKILL.md` names it at steps 3, 4 and 5, on the condition that the step's audit
ran, steps 4 and 5 with "unless an earlier step did" (WAY-256). On coding's route of one kind and at
a new level of tests, it is not named. A `SKILL.md` names `product-guidelines/audit_end.md` directly,
as it names `product-guidelines/template.md`; "the files named below lie there" already covers a
product's `.the-way`.

What stays in each discipline's file:

- **`styleguide/audit.md`:** both directions, the standing question, the running product and what
  stays unchecked. It says each finding has its place and effect and that a cause takes one of the
  four categories; its "End with three to five" and its sentence on what is deferred go, and it
  sends the agent to the shared file.
- **`testing/audit.md`:** for each level, its exemplar test and its findings, judged all, with no
  limit, each with its place and effect, against the same rules as today; the trust boundaries as
  decision 11 gives. Its "three to five" and its sentence on what is deferred go.
- **`coding/kinds.md` and `trial_run.md`:** the kinds, the exemplars and `do not copy` as today, with
  what decisions 11 and 12 add. `trial_run.md` runs first, as step 3 reads it.

Rejected: only the scale shared, the rest in each discipline's file — the three texts of the order,
the top and the check are what would drift; a file for the scale and one for the procedure — two
files read together at the same steps; `weighing.md` — the file is more than the weighing.

Cost if wrong: moving text between files of one part.

### 6. One list across disciplines

The end of an audit belongs to neither discipline, so **it runs once, for a task joining code and
tests, at the end of the audit that runs last**:

1. Each skill finds its own causes and gives each its first weight, as its discipline knows them.
2. An audit stops after weighing where the other skill's step 1, which the agent runs before this
   audit ends, gives that skill the audit in this task, and that audit has not yet run. The test is
   the audit that runs, not what the product has: coding's route of one kind and a new level of
   tests are no audit, so with either of them this audit ends as any other. The audit that stops
   writes its causes into *Context* with no place in the order, its step 4 settles all it settles
   except the top, and its skill hands back to `refine-task` step 3, for the other skill to lead its
   matters. Only the skill of the audit that runs last hands back to step 4.
3. From there the causes are the list's, whichever discipline found them. The audit that runs last
   merges both audits' causes, orders them, goes back to check the top in the form of each cause's
   discipline (decision 13), lowers or withdraws a cause of either discipline by what it sees, sets
   the top, and its step 4 puts it to the human, once.

Causes of the two audits merge only where one fix removes both, the heavier weight standing. In the
order the first audit's lines get their numbers, and its `do not copy` marks with them. Which
discipline runs first is free. Where the two skills run in separate sessions, the list in the
document carries the first audit's work over.

**What the first audit's step 4 settled stands.** The check moves a cause, never an answer of the
human. Where the last audit withdraws a cause on which something settled rests, such as the
`do not copy` status of a file (`coding/settle.md:26-27`), that status stays as the human settled it,
and goes back to the human with the top, as one question for each: keep it or change it, with what
the check saw. The answer stands under the question that settled it, with its own source, so no
choice stands without the human's words. A cause lowered touches nothing settled.

**WAY-247 is not narrowed, and C names no `narrows`.** What WAY-247 leaves to each skill is what its
discipline's guidelines are to carry, as its violating example shows, the coding skill settling the
levels of tests; a skill settles all of that with the human at its own step 4, and the end never
changes it. A cause's weight is none of that: it is no meaning of the guidelines and binds only the
skill (WAY-173). Decision C says so and derives from WAY-247.

Rejected:

- Each skill keeps its own top — row 3 and question 7 give one list.
- Both step 3 before either step 4, always — it makes every joint refinement wait, for what only the
  top needs.
- `refine-task` merges — it holds the order of work and knows no audit's content.
- Each cause checked by its own discipline's skill — one more round through a skill whose work has
  ended, for a check the shared file gives in full.
- C naming `narrows WAY-247` — it would state a collision where nothing a discipline settles is
  touched.
- The withdrawn cause taking a settled status with it — an agent would undo the human's answer, in
  another skill's session.

Cost if wrong: one section of one file; if a weight is held to be a discipline's matter, C gains
`narrows WAY-247` and a sentence stating its area (WAY-25). Weak point: the first skill's step 4 and
the top reach the human in two rounds.

### 7. Which step does what

The three skills number these steps alike.

| What | Step | How |
|---|---|---|
| To do 1–3, weight, merging, places | 3 | after the discipline's file; for coding after `trial_run.md` and `kinds.md` |
| To do 4, the order | 3 | once causes and costs stand |
| To do 5, going back to check | 3 | on the top the order gives, before step 4; what it lowers or withdraws moves the order, and a cause that so enters the top is checked in its turn, until every cause of the top stands `checked` or `unchecked` |
| To do 6, the list and the top | 3 | written into *Context* as step 3 ends |
| To do 6, the top shown | 4 | with the rest of the set |
| To do 7, the proposal | 4 | which causes of the top enter and which are deferred, joining the set of proposals before the critique |
| To do 7, the human's decision and the question on a `grave` cause | 4 | after the critique, as the set is shown; answers under *Questions to settle* |
| To do 7, a yes turned into a task | 5 | decision 10 |
| To do 8 | 3–5 | each `task_document.md` says what reaches the document; `hand_back.md` checks it |

**The check and the critique.** The check of To do 5 comes first: it is the author's own and comes
before the set is complete. WAY-120's critique follows, on the proposal and the top, with the full
list among its sources, so a critic can see a heavier cause standing too low. Its independence is
what question 6 says the check lacks. A cause the author's verdict moves goes through the order
again, and a cause entering the top is checked before the set is shown. Each `settle.md` gains one
item before its **Critique**, which stands as it is.

Rejected: the check after the critique — the critic would read what the author has not yet looked
at twice, and To do 5 only asks that it come before the human; a second critique after a move — one
critic for a set (WAY-120).

### 8. Where each result stands, and the form of the list

| Thing | Section |
|---|---|
| Weights, causes with places, order, deferred causes with reasons, causes the check withdrew | *Context*, one list |
| `do not copy` files, the trial run's evidence, trust boundaries, what could not be seen | *Context*, as today |
| The fix of a cause taken | *To do*, one item for each, replacing "each item the audit calls for" |
| The human's decision on the top; each answer on a backlog task | *Questions to settle*, with the human's words and date |

*Settlements to record* gains nothing: which causes a task takes ends with the task (WAY-36), so
these answers are no rows, and the choice passes without the one question against an answer ("How a
skill asks", `way_of_working.md:28-33`).

**The list** opens with one item, in English, naming itself as the audit's list and saying which
places of the order are its top. Under it, one item for each cause, in the order, with its details
nested below it, as *Questions to settle* nests them, labels in English and values in the document's
language:

- **Item:** the place in the order as its number, the weight, and the cause in one sentence of its
  effect on the user or the owner.
- **`Category:`** — the styleguide's four categories, one for each cause (WAY-187, To do 3). Only
  there.
- **`Places:`** — file and line; for the linter's rules the number of files; for a boundary its name.
- **`Fix:`** — one sentence of what the one fix does, and **`Removes:`** and **`Reaches:`** as
  decision 2 gives.
- **`Checked:`** — the places gone back to and what was seen, with the weight the cause had where
  the check lowered it, or **`Unchecked:`** — what could not be seen and why. For every cause the
  check went back to: the top, and a cause the check lowered out of it, which keeps its mark.
- **`Taken:`** naming the *To do* item, or for a boundary's cause its invariant (decision 11), or
  **`Deferred:`** with its reason; a cause below the top that the human did not take reads
  `Deferred: below the top`, the English of `poza górą listy`.

A cause's data stand in that line alone; the *To do* item gives the fix and names the cause by its
number. This weighs "each fact has one home" over "keep data needed to make a change in its item"
of the task template, deliberately, since a list of places copied into *To do* would stand twice.

**A cause the check withdraws** leaves the order and stays in the list, so the record of the check
stands where it changed most. After the last cause stands one item for each, with no number,
opening `Withdrawn:`, holding the cause in one sentence, the weight it had and its `Checked:`, with
no `Fix:` and no `Taken:` or `Deferred:`. A cause the author's verdict on the critique withdraws
takes the same form, its `Checked:` saying so. So the critic reads what the author dropped, and at
step 4 the human hears in one line how many causes the check withdrew or lowered out of the top, and
where they stand.

An audit with no finding says so in one item and has no top and no question.

Rejected:

- A withdrawn cause leaving no line, and `Checked:` only on the top — the check would be recorded
  only where it confirmed, and the critic, the one independent reader question 6 names, would not
  see what the author dropped.
- **A new section of the task template** (as *Technology* appears once used) — it fits the list
  better, since *Context* is "concise", but it changes the template of every task for what one kind
  of task holds, and To do 8 names `task_document.md` alone. Today's skills already send an audit's
  results and the trial run's evidence to *Context*. The weak point stays: a long list in a section
  meant to be short.
- A table — a cell takes no line break, and a cause can hold many places.
- Two lists, top and rest — one order would stand twice.
- Causes taken standing whole in *To do* — the full list would no longer stand in one place.

Cost if wrong: a section to move, in three files and one form.

### 9. The top of the list

To do 6's "three to five" can be read two ways: fill to five, or let the agent choose. This spec
picks a rule with no judgement in it:

The top is the first causes of the order: as many as the larger of three and the number of `grave`
causes; then, up to five, the next cause while it weighs as much as the one before it. Over five
`grave` causes, all of them and nothing more. Fewer than three causes, all of them. The count runs
over the whole audit, never by level.

Rejected: always five where five exist — the lower bound would mean nothing, and a `light` cause
would take the human's attention more often, the fear in *Need*; the agent's judgement — no way to
check it.

Cost if wrong: one sentence, and it stays within what the task allows.

### 10. A deferred `grave` cause

A `grave` cause always stands in the top, so the extra question is put only there, at step 4, for
each `grave` cause the human defers, as soon as the human has decided.

- **The skill itself:** proposes, asks, writes each answer under *Questions to settle* and the cause
  `Deferred:` with its reason. It writes no backlog and no plan, as its table of what it never writes
  and each `orchestrated_mode.md` already say.
- **Returned to `refine-task`:** a yes. At step 5, before handing back, the session follows a new
  short section of `project-level/task/skill/guideline_findings.md`, which holds refinement's route
  for a deferred cause, and whose opening condition widens to name it. Each `SKILL.md` names that file
  at step 5, on the condition of such a yes (WAY-265). The write is `refine-task`'s, as for a
  prerequisite (WAY-215), and comes with the hand-back, so the skill's table of what it never writes
  stays true also where a product's git tracks its backlog.
- **The route** is that of `guideline_findings.md:12-17`, differing in that nothing waits: for an
  independent or source-only task, the task is added to the product's backlog by the conventions of
  `read_sources.md`, holding the cause's effect, weight and places; for a plan member, `refine-task`
  returns `plan change` naming the cause, or, where the plan holds such a task, the cause names it
  as its reason. There is no `waits for task <n>` and no dependency: the refined task does not need
  the fix.
- **Orchestrated mode** is the plan-member case and needs no change of the three
  `orchestrated_mode.md`: the question goes into the turn, the skill ends it, and `plan change` is
  one of the refiner's results, after which the refinement resumes as for any other.
- **`hand_back.md`** of each skill gains one check, reading the last section of the shared file:
  every cause stands `Taken:` or `Deferred:`, every cause of the top stands `Checked:` or
  `Unchecked:`, a cause the check moved out of the top keeps its `Checked:`, a withdrawn cause stands
  as a `Withdrawn:` item, every deferred `grave` cause has its answer, and every settled status put
  back to the human has its answer. An audit that stopped after weighing (decision 6) checks only
  that its causes stand weighed, and hands back to `refine-task` step 3.

A no leaves the cause deferred in the document; nothing forces a return, the weak point question 3
accepted. Causes below the top reach the human as one choice, with their number and where they
stand, so WAY-174 holds and nobody is asked one by one.

Rejected: the route written in the shared file — a step of `refine-task` would stand in another
part; the prerequisite's paragraph applied as it stands — it makes the task wait; the skill adding
the task itself — it would write what it says it never writes.

### 11. The linter, the trust boundaries and the reformatting

- **Linter (coding).** `trial_run.md` keeps its count, and its result enters the list: the reports of
  the rules that block are grouped by one reason, each reason a cause told by its effect, its place
  the number of files, with no rule's name; the output's path stays in *Context*. That is why
  WAY-201's violation, an audit ending with the reports listed by rule, is not met. Rules that went
  among the examples flagged sound code and yield no cause.
- **Boundary (testing).** `testing/audit.md` keeps saying, for each boundary, whether a test checks
  its refusal. A boundary a test is due at under WAY-235 and that has none is also a cause, its place
  the boundary's name. A boundary that is only the configuration of someone else's service has no
  test due: WAY-235 and `testing/settle.md:35-36` leave it with the review of WAY-48, so the audit says
  that beside it and it is **no cause**. It would have no fix and no invariant, and by its stake it
  could take a place in the top, and draw the backlog question, for a test the foundation says not to
  write. To do 2 keeps every boundary a test is due at.
- **What they set off stays.** `settle.md` proposes the invariants of WAY-205 and WAY-235 as today,
  whatever the human decides of the cause, and the invariant is never a second question inside the
  decision on the top. A boundary's cause whose fix is the test its accepted invariant brings stands
  `Taken:`, naming that invariant, also below the top. A linter's cause is not closed by a marked
  invariant. A proposal to take a linter's cause takes that reason's files, and never grows into
  cleaning the whole product (WAY-205).
- **Reformatting.** The formatter's count stays in `trial_run.md` and never enters the list.

### 12. A `do not copy` place and its cause

Both stand, as two views of one finding. The `do not copy` list stays apart, whole, under no limit,
with each file's file and line as WAY-201 and `kinds.md` give, and tells the next agent what not to
copy. Each such place is a finding, so it also stands in the `Places:` of its one cause, which says
what to fix. In the task document each `do not copy` line gains the number of that cause, so a
reader sees one fact seen twice and not two problems. A file with two breaks has two findings. The
mark stands in the task document alone; the table of a kind's files in a product's guidelines and
WAY-200 do not change. A cause withdrawn because its place shows no break takes that `do not copy`
with it while it is still a proposal; once a step 4 has settled it, decision 6 gives the way, and
the status stands with the `Withdrawn:` item as its mark until the human answers. A cause lowered
takes nothing with it.

Rejected: the cause pointing to the `do not copy` list for its places — To do 3 has the cause carry
them; the `do not copy` list pointing to causes for its lines — WAY-201 has it carry them.

### 13. How going back reads in each discipline

The shared text says one thing for all three: go back to the places the cause names and see whether
the effect it describes occurs; what does not hold is lowered or withdrawn; `Checked:` records what
was gone back to, whatever the check did to the cause, as decision 8 gives; what cannot be seen
without the running product stays `Unchecked:`, its weight kept, and the human hears so. Its forms
stand beside it, one line each, a cause taking the form of the discipline that found it:

- **Code:** follow the way from the input to the harm, through the lines.
- **Tests:** follow what the test asserts and see that the fault named gets past it.
- **Screens:** open the screen by the agent's way to the running product where the foundation settles
  one; otherwise from the code, marking what shows only on a running screen (`styleguide/audit.md:11-13`).

Every place given by file and line is gone back to. A cause placed by a number of files has no line
to return to, so the reports behind the number are read and the line says how many were followed.
A boundary's cause is gone back to by looking for the test.

A cause the human takes from below the top, that the check never went back to, gets no such mark:
To do 5 reaches the top alone.

### 14. Repository and installation

- No test of this repository reads these files. In `*.py` files, `product-guidelines` stands only in
  `installation/install.py` and the three `installation/test_*_installation.py`, each by the path of
  a `SKILL.md`, whose paths and names do not change.
- Nothing is needed from `installation/`: `.the-way` is a submodule of the whole repository, so the
  shared file reaches a product as `reading.md` does.
- No skill's *description* changes, so `skill_entry_points.py --write` is not run.
- `README.md`, `installation/README.md`, `project-level/` and `agent-instructions/` say nothing of
  how these audits end.

## Foundation entries

New decisions, one for each row, each from its row whole. Their relations are given below; each
number is the next free one when it is written.

| Entry | Row | Meaning | *Rejected* from | Relations |
|---|---|---|---|---|
| A — on what scale an audit of the three skills weighs a cause | 1 | The audit gives each cause one of the four weights on one scale described once in a file the three skills share, measured by the effect on the user or the owner and by what is at stake, never by how many places break a rule; the-way adopts weight, merging and order from a course's skill for auditing observability, and not the audit as a skill of its own. | questions 2 and 8 | derives from WAY-100 · derives from WAY-173 |
| B — what such an audit merges and lists | 2 | Several violations of one source are one cause and one fix, each finding in one cause; a cause carries its places; the list also holds a trust boundary a test of refusal is due at under WAY-235 and that has none, and the linter's rules broken from one reason, told by effect with a number of files and no rule's name, and a reformatting is no finding. | question 5 | derives from A |
| C — in what order the causes stand | 3 | The audit ends with an order of repair from the heaviest down, and within a weight the fix that removes most for least work first; a task joining code and tests has one list and one order, made at the end of the audit that runs last, which may lower or withdraw a cause of either discipline and changes nothing the human settled for a discipline. | question 7 | derives from A · derives from B · derives from WAY-247 |
| D — what of the list the human decides on | 4 | The full list stays in the task document, and the human gets the top of it: three to five causes for the whole audit, every `grave` one always, all and nothing more over five, all under three; the `do not copy` list stands apart. | question 1 | derives from C |
| E — what decides which causes a task takes | 5 | The weight proposes and the human decides of the top; on deferring a `grave` cause the agent asks whether to open a backlog task, and a yes takes the route of a prerequisite with nothing waiting; causes below the top are deferred together, unless the human takes one. | question 3 | derives from D · derives from WAY-174 · derives from WAY-215 |
| F — how a cause of the top is checked | 6 | Before reaching the human each cause of the top is gone back to by the agent leading the audit, to see whether its effect occurs; what does not hold is lowered or withdrawn, each check is recorded, the check of a cause it lowers or withdraws included, and what cannot be seen without the running product stays marked unchecked. | question 6 | derives from D |

- Rows 3, 4 and 5 all name question 7 as a source. Its ways not chosen are all ways of ordering, so
  they stand in C alone.
- Row 2's "granicę zaufania bez testu odmowy" is kept for every boundary a test is due at. Its
  sources do not speak of a boundary WAY-235 leaves with the review, so B collides with no row and
  no current entry, and the row's writer has no question to ask under `foundation_step.md`.
- C names no `narrows WAY-247` (decision 6).
- A's *Rationale* names what is adopted, where and why, describes the pattern in its own words, and
  points to nothing a reader cannot open (WAY-27), naming the course and lesson without an address;
  *Origin* is `none`. A's binding sentence names the four words.
- Each row's weak point, kept in its question's *Source*, belongs in the entry's *Rationale*.
- `Based on` is `none` for all six.

Changed decisions, in place, each describing the decision as it then stands (WAY-07):

- **WAY-187** — audits in both directions and ends with the list D gives, each cause in one of its
  four categories; the standing question and the marking of what is unchecked stay. Three-to-five
  leaves it. *Verification* and *Rationale* lose `charge`; the rationale's "a few charges … can be
  weighed" goes to D. *Rejected* unchanged. *Relations:* derives from D.
- **WAY-201** — ends with the exemplar and the `do not copy` files as today, and with the list D
  gives. Its violation on the linter's reports stays. *Rationale* loses `charges`. *Rejected*
  unchanged. *Relations:* adds derives from D.
- **WAY-250** — ends, for each level, with its exemplar test and what the product gains, for each
  trust boundary with whether a test of its refusal exists, and with the list D gives, over the
  whole audit and not per level. *Verification* and *Rationale* lose `charge`. **Its *Rejected***
  keeps "shown as a comparison of the tests' code"; "every fault … listed — a list too long to
  weigh" leaves it with the sentence it rejected, and stands in D, rewritten as question 1 keeps it:
  every cause put to the human in turn, too long to weigh even merged. *Relations:* adds derives
  from D.

No other entry: no glossary term (decisions 1 and 3), no invariant, since no row is one and no test
reads this text, no environment fact, no change of the part map, whose `product-guidelines` entry
covers the file. WAY-120, WAY-174, WAY-205, WAY-235, WAY-247 stay as they are. The writer makes the
search of WAY-33 once the entries are settled.

## Left to the maker

- The wording of `product-guidelines/audit_end.md` and of each entry, the order of its sections, and
  the file's heading, keeping the file's name.
- Files to change, beyond the shared one: `coding/SKILL.md`, `kinds.md`, `trial_run.md`, `settle.md`,
  `task_document.md`, `hand_back.md`; `styleguide/SKILL.md`, `audit.md`, `settle.md`,
  `task_document.md`, `hand_back.md`; `testing/SKILL.md`, `audit.md`, `settle.md`,
  `task_document.md`, `hand_back.md`; `project-level/task/skill/guideline_findings.md`;
  `foundations/decisions.md`. Each `task_document.md` says in its own lines what reaches the
  document, as To do 8 asks: the weights, the causes with their places, the order and the deferred
  causes, the form standing in the shared file.
- How `kinds.md`, read on the route of one kind as well, words its condition, so that the sentence
  on causes reaches the audit alone.
- The wording of the top's question and of the line for the causes below the top.
- Whether one author can hold the change or it needs a plan, judged at step 7 of the cycle.

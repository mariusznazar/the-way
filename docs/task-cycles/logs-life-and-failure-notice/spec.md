# Spec — the way: krok technologii pyta też, jak długo żyją logi produktu i skąd człowiek dowiaduje się o awarii

- Task: `.runs/task-cycles/logs-life-and-failure-notice/task.md`
- Open choice: what a resumed step does with a list written before this change (a logs item standing `— held by:` or `— projected:`, a list with no item on how a human learns of a failure), and in which file the look at that new item stands and how the step reaches it.

## Intent

The step that settles technology asks where a product's logs go and how an agent reads them. After
this change it also asks how long that record lives, between deployments too, and, as a choice of
its own, how a human learns of a failure of the running product. A log good enough to check a change
right after a deployment is not good enough to diagnose a failure from before it, and a human who
learns of a failure only from users has chosen that without knowing. The change also reaches a
product whose definition is already approved, through the list of its deployment skill.

This spec settles what the task left to the cycle. Its *To do*, its answers to questions 1–6 and its
four rows of *Settlements to record* bind it and are not reopened here.

In this spec, "the failure item" is a working label for the matter of how a human learns of a
failure of the running product. It is no term of the-way and no file uses it.

## Goals and non-goals

Goals:

- The logs ask how long the record lives, between deployments too (To do 1, row 1).
- How a human learns of a failure stands on a definition's list as a choice of its own, outside the
  matters of an agent's way to the running product, by a criterion of its own (To do 2, 3, rows 2,
  3).
- The list of a deployment skill gains the two items, and refinement asks the human about what no
  decision and no approved definition answers of them (To do 4, row 4, read as D6 gives).
- Both matters are settled by the step's ordinary mechanism, and a deliberate absence always enters
  the failure item's comparison, though it has no page of documentation (To do 5).
- A resumed definition behaves as a new list does, and a definition the gate has approved does not
  come back (To do 6).

Non-goals:

- What the code writes to its logs and in what form (the task's *Out of scope*).
- A mandatory failure item, or any change to the readiness gate. None of
  `project-level/readiness_check.py`, `project-level/plan_check.py`, `project-level/plan_state.py`
  changes: the nested items this spec uses are details the check already passes over.
- A definition already past the step, at `ready for gate` or approved: nothing brings it back.
- A look of either kind in a run at a task; WAY-267 stays as it is.
- A research skill of its own, a new invariant, a new glossary term, a change to the part map.
- Anything in `loop2`.

## Constraints

- The task's settled answers and rows; the restriction in its Context on what may not be opened.
- The step's text names no tool (To do 5, `project-level/technology/research.md:18-19`).
- WAY-106: the step writes into the document only.
- WAY-05 by `elements/decisions/template.md`: one to three binding sentences. WAY-121 and WAY-165
  hold three each today, so what they gain joins an existing sentence. A binding sentence names no
  stage of the product, so the task's "na początek" stays out of the new decision's binding
  sentences.
- WAY-19: a new rule next to an existing decision is a new question.
- WAY-25: the decision that prevails names the other as `narrows`, and its binding sentences state
  the area where it prevails.
- WAY-134 and the decisions template: *Rejected* of an entry written from a row holds only the ways
  the row's source keeps.
- No test pins the text of the step's files, and a file under `project-level/**` belongs to its part
  already. The skill's description does not change, so `agent-instructions/skill_entry_points.py`
  has nothing to write.

## Decisions

### D1. A list written before this change (the main choice)

**The rule.** An entry holds one of the three matters only where it answers everything the matter
asks as the template gives it. This holds for a decision of the foundation and for a projected
decision of the definition, for a new list and for a list already written, and for each of the three
matters. It is stated timelessly, as a rule of the look in `running_product.md`, not as a step for
old lists, so it also serves any later widening of a matter. The test is whether the entry says, not
whether its answer is good: "the record lives until the next deployment" answers the question.

**What a resumed step at a definition does.** `start.md` takes the look at every resume, so:

| What the list holds | What the resumed step does |
|---|---|
| a logs item `— held by: X`, X saying how long the record lives | nothing; the item stands |
| a logs item `— held by: X`, X silent on it | the item ends `— open`, with X nested under it |
| a logs item `— projected: Q`, Q's decision saying it | nothing; the item stands |
| a logs item `— projected: Q`, Q's decision silent on it | the item ends `— open`, with that projected decision nested under it; settling it rewrites that projected decision |
| a logs item `— open` | it stays open; a report that does not answer what the matter asks is not reused |
| no logs item, a decision silent on it | as today: the look finds the matter missing and adds it `— open`, with the decision nested |
| no failure item, the criterion met (D4), no decision of the foundation on it | the look of D2 adds it `— open` |
| no failure item, the criterion not met or a decision on it | nothing is added |

Wherever the look adds or changes an item, the list is shown again before anything goes on, as
`start.md` already gives for an added one, with one sentence saying what the named entry leaves
unsaid. The open item is the whole matter, since the task's Context says such a decision does not
settle the matter, and how long a record lives can depend on where it goes. The nested entry's
present answer enters the comparison as an option, so a human who wants to keep today's answer picks
it, its life now said, at the cost of one wave.

**Two traps this rule meets, which the change closes.**

1. `start.md`'s bullet on open items ends an open item `— projected` where a decision written for
   that choice stands, so a projected item turned `— open` would turn straight back. That lookup
   counts only a decision that answers what the template asks of the choice. A resumed step after an
   interrupted write still finds a rewritten decision.
2. The same bullet reuses a report under `.runs/technology/` that reads `critique: passed`. For a
   projected item turned open such a report exists and says nothing of the record's life. Reuse
   counts only a report that answers what the template asks of the choice.

**Reaching the nested entry.** A held decision is no longer `held by`, so `settle.md` sub-step 1 and
the opening of `research.md`, which give the binding sentences of `held by` decisions, extend to a
decision nested under an open choice, and `research.md` step 1 lets its answer enter the comparison
beside an option the human named. A run at a task nests decisions the same way and gains the same.

**Writing the result over the nested entry.** The rule stands in `settle.md` sub-step 7, the place
that hands a choice to `record-decision`: where an entry is nested under the choice, the hand-over
names it as the entry the result rewrites, so that one question keeps one projected entry.

- A projected decision of the definition is replaced under its heading, its meaning sentence with it.
- A decision of the foundation is projected as its change, under `#### <PREFIX>-<NN> — <question>`.
- The nested line goes when the item ends `— projected`, here and in the lookup of trap 1.

Without this, nothing finds a projected entry: `record-decision` searches the log, and a projected
`(new)` entry stands in the definition. The readiness check would pass the two entries, since it keeps
questions as a set, and the silent one would stand. No file of `elements/decisions/` or
`elements/common/` changes: the forms of both headings stand in `elements/decisions/skill/SKILL.md`
and in the template, and an entry that goes through projected mode again already has a precedent at
the gate (`project-level/skill/SKILL.md`, step 7). What was missing is only who names the entry, and
that is the hand-over's. `task_run.md` replaces sub-step 7 with its own *Write*, which already says
which decision a choice changes, so a run at a task gains nothing here.

**Who may open what.**

- At a definition the agent opens no held decision. WAY-121 has the step list each matter no decision
  settles, and a decision that leaves part of the matter unanswered does not settle it, so nothing
  stands held. The human sees the changed item with its reason before any research, and the decision
  changes only through a projected edit the human chooses and the gate approves.
- The rule of `task_run.md`, "An agent never opens one", and WAY-267's matching sentence have no
  bearing at a definition. They bind a run at a task, where a note bounds the run and no gate follows.
  Both stay as they are.
- At a task none of the above runs. The look is not taken, and the logs reach a run only through a
  note the human agreed to (D6), which is the human's word.
- An approved definition does not come back for any of this (`start.md`, To do 6).

**The entry that carries it after the merge:** WAY-165, whose question is what an answer to a matter
must settle. Its binding part says that a decision or a projected decision leaving part of a matter
unanswered does not settle that matter. Its *Verification* gives both markers as compliant examples,
and as violations an item left standing on a silent entry and an approved definition sent back.

**Ways rejected.**

- Leave `held by` and `projected` items alone: no text changes, but the result depends on when the
  list was written, and a silent projected decision enters the foundation already failing the next
  project's look.
- A second item "how long the record lives" beside the untouched item: no marker turns and neither
  trap arises, but one matter stands as two choices where a new list gives one, research is bound to
  a destination that may be why the record dies, and the task's Context says the decision does not
  settle the matter.
- Reopen `held by` and leave `projected`: the one kind of entry that is still a draft would be the
  one left silent.
- Add a failure item only to a new list: two regimes, while `start.md` takes the look at every resume
  anyway.

**Cost if wrong:** a definition in flight spends one wave more on one item; the text is reversible,
and the reach is only definitions at `definition — open: Technology` when the pin moves.

### D2. Where the look at the failure item stands

A new file beside the skill, `project-level/technology/failure_notice.md`. It is the look at how a
human learns of a failure, and does one thing:

- **It says:** the criterion of D4; that a decision of the foundation settling the matter, a
  deliberate absence included, keeps it off the list; that otherwise the matter stands as a choice
  of its own, ending `— open`, even where its answer adds nothing to run, pay for or back up; that it
  is no matter of an agent's way to the running product; that a listed item is settled like any
  other. The comparison's rules stay in the template and `research.md` (D5).
- **Used by:** the steps below, which read it and list what it says.
- **Depends on:** the template's Technology section and the product's foundation.

How the step reaches it:

- `SKILL.md` step 0: where the section holds a list, read this file as well as `running_product.md`,
  and `list.md` when a look adds or changes an item.
- `SKILL.md` step 1: where the section reads `TODO`, `list.md`, `running_product.md` on its condition
  as today, and this file on the condition of D4. Step 1 thus has two conditions, each with its file.
- `list.md`: one bullet after the look of `running_product.md`, on the same condition of D4.
- `start.md`, the list bullet: takes both looks, and its closing sentence on an approved definition
  covers both.
- `task_run.md`: D7.

Ways rejected:

- A second section in `running_product.md`: no new file, but the file's whole subject is an agent's
  way to the running product, and a reader of it would take WAY-166 to apply, which answer 1 rules
  out.
- A bullet each in `list.md` and `start.md`, pointing to the template: no new file and no change to
  step 1, but the criterion is applied in two places, and the pattern the skill uses for a look read
  on its own condition is broken.

**Cost if wrong:** one small file to fold into another.

### D3. One new decision, beside WAY-121

Rows 2 and 3 go into **one new decision**, as answer 1 says: "nową decyzję i osobne zdanie o tym,
kiedy krok tę sprawę sprawdza". Its binding sentences say when the item stands on a definition's
list and that no definition must hold it, the gate does not check it and an approved definition does
not come back; what the item asks and that it is outside an agent's way; and that a deliberate
absence always enters the comparison, stating the area where this prevails.

Beside WAY-121: the new decision names WAY-121 as `narrows`, since it lists an item whose answer may
add nothing to run, pay for or back up, and states that area. WAY-121 cannot take a fourth sentence;
it gains a pointer inside an existing one, so that its reader sees a second exception exists, and a
*Verification* example.

WAY-100: the new decision's *Rationale* names what is adopted from lesson m3l5 of the 10xDEVS course,
namely the two questions of how long the record lives and how a human learns of a failure; where they
apply, by decision (WAY-165, the new decision, WAY-139); and why. It says that the ordinary mechanism
of the step is kept, with no research skill of its own. Its *Relations* name WAY-100 as `derives
from`, and WAY-165 and WAY-139 name the new decision as `derives from`, so each of the three places
reaches the one that names the adoption. The lesson itself is not opened.

Ways rejected:

- Two new decisions: one row each, but two entries for one question, and against answer 1's wording.
- Row 3 as a fourth sentence of WAY-121: its reader finds the rule in one place, but it breaks the
  limit of three sentences and puts a new rule next to an existing decision (WAY-19).

**Cost if wrong:** one entry split later, which WAY-07 allows in place.

### D4. How the criterion reads

Row 3's criterion is that the project runs the product outside the machine on which it is made. The
step applies it as one condition, in the same words in `SKILL.md` step 1, in the `list.md` bullet and
in `failure_notice.md`: **the condition holds unless the definition, or a decision of the foundation,
keeps the product on that machine.** A definition that says the product goes to a server meets it, a
definition silent on where the product runs meets it, and a definition or a decision that keeps the
product there does not.

The condition reads what the definition and the foundation say, never a marker, because in `list.md`
the look comes before any item has its marker. Silence counts as a yes because the first project,
with its place to run not yet chosen, is the case To do 3 exists for, and a run takes no second look
after a wave. A wrong yes costs one item answered by a deliberate absence, once for the product; a
wrong no leaves the question to the check of D6, which reaches only a task that deploys the product.
How long the record lives follows the logs' own criterion (answer 2), so it gains no condition.

No dependency between the failure item and the logs or the place to run is written into the step:
`settle.md`'s rule on dependencies decides, and an alert built on logs comes in a later table, the
weak point answer 1 accepted.

### D5. The deliberate absence, and what stays with the logs

- `project-level/definition_template.md`: the logs bullet gains how long the record lives, between
  deployments too; the exception bullet gains that an entry leaving part unanswered does not settle
  a matter; a new bullet gives the failure item: what it asks, that no definition must hold it, that
  it is outside an agent's way, that whether an agent reads an option is an ordinary consequence,
  and that a deliberate absence always enters with no page of documentation, its consequences
  anchored in the document. The research bullet (WAY-122) stands as it is, and the new bullet prevails
  over it by name.
- `project-level/technology/research.md` step 1: the same exception. The source of the absence's
  consequences is the document and the pages of the options it is compared with, so the critique of
  `settle.md` sub-step 4, which gets the document, has what to check them against.
- Step 2 of `research.md` does not bear on the absence: it weighs what code is written in or against.
  An option a tool's code is written against is weighed there like a library (task, WAY-122).
- The step's files name no tool and, of the kinds of answer, only the deliberate absence, because the
  options come from research. The kinds in row 2 stand in the new decision only, and no product's name
  stands anywhere in this change.
- Tested when recommended: nothing changes. `settle.md` sub-step 5 tests the option recommended for
  every choice, and WAY-138 covers the absence. The new decision's *Verification* shows it.
- Staying with the logs, its life included, and not reaching the failure item: WAY-166, the sentence
  on an agent's way in `research.md` step 3, and the sentence in `settle.md` sub-step 5. All three are
  worded for that family, so none changes. An option whose panel only a human reads can be
  recommended for the failure item.

### D6. The deployment skill (row 4)

WAY-139's list gains the two items. Its check, at the closing paragraph of
`project-level/task/skill/resolve_gaps.md`, goes on for the five items as today. For the two new
items:

1. A deployment skill that records the human's refusal covers the item under the check.
2. Where a decision of the foundation or an approved definition the task carries answers the item,
   the file's first paragraph applies: quote it, ask nothing, and the *To do* gains the item that
   writes it into the skill. A logs decision silent on the record's life answers nothing here.
3. Otherwise the human is asked, once, whether to run the step at this task with a note on what the
   skill does not say and no decision and no approved definition answers. The human may answer each
   item apart.
4. A yes is the third case of that file's list, "the human asks for a run while the task is refined",
   so no fourth case is added. It is also the human's word that `task_run.md` asks for where a logs
   decision stands. The *To do* gains the item that gives the skill the answer.
5. A no gives the *To do* the item that records the refusal in the skill.
6. With no skill at all, the question comes before the offer to split, because a split task that only
   writes a skill has no deployment outcome and takes no check. The split task carries the answer or
   the refusal.

Three readings picked, each of which the text could leave open:

- **An item an entry already answers is quoted, not asked (step 2).** Row 4 guards against an agent
  filling an item in without the human's choice; here the choice already stands in the entry, and the
  human reads the quote when accepting the task document and can still ask for a run. Asking would
  offer a run that cannot reopen a projected decision of an approved definition (WAY-267).
- **The run answers only what the note names.** With a held logs decision the item stands `— open`
  with that decision nested, and the result changes it. With a projected decision of an approved
  definition, that decision stays untouched (WAY-118, WAY-267): the record's life stands as an item
  of its own, which reopens nothing, and the cycle writes it.
- **A refusal closes the question of this check, not the look at a later definition.** Row 3's
  criterion reads the foundation, and a refusal is no decision. The next project of that product
  lists the item once, and a deliberate absence chosen there ends it. Making the look read the
  product's deployment skill would take a new source for one question asked once more.

**Cost if wrong:** the first reading gives the skill an answer the human sees only in the document,
and an edit of the check turns it back. The second is rare and textual. The third costs one more item
on one list.

### D7. A run at a task

`project-level/technology/task_run.md`: its line on the look extends to `failure_notice.md`, so the
failure item enters a list only where the note touches it, and its *Settle* line on WAY-165 and
WAY-166 gains the new decision, for the same case, while the WAY-166 half stays limited to the three
matters. Nothing else changes: answer 5 leaves WAY-267 as it is, and its sentence "settles what the
note and the task name" already covers the failure item.

### D8. The boundary of answer 3

No text of the-way states the boundary the task quotes; the phrase stands nowhere in this repository.
The nearest text is WAY-165's *Rejected*, on what the product logs and in what form, which agrees
with answer 3. So no text has to change for the boundary. Its practical point, that what a tool's
hook-up in code takes shows as the cost of changing it later, already follows from WAY-123, and
appears as a compliant example of the new decision.

### D9. Glossary

No new term. "Failure" and "deliberate absence" mean what a reader of the field takes them to mean,
so neither passes the template's "Which words take an entry", and new texts write the matter out in
plain words. `agent's way to the running product` stays: the failure item falls outside it by its
definition, and a record that outlives a deployment is still a means by which an agent checks what
the product did.

### Files

| File | Change |
|---|---|
| `foundations/decisions.md` | the entries below |
| `project-level/definition_template.md` | D1, D5 |
| `project-level/technology/failure_notice.md` | new, D2 |
| `project-level/technology/running_product.md` | the rule of D1, the marker and the nested entry |
| `project-level/technology/SKILL.md` | steps 0 and 1, D2 |
| `project-level/technology/start.md` | both looks, a changed item shown again, the two traps of D1 |
| `project-level/technology/list.md` | one bullet, D2 |
| `project-level/technology/research.md` | the nested decision, step 1 (D1, D5) |
| `project-level/technology/settle.md` | sub-step 1, the nested decision; sub-step 7, the entry the result rewrites (D1) |
| `project-level/technology/task_run.md` | D7 |
| `project-level/task/skill/resolve_gaps.md` | closing paragraph, D6 |

`close.md`, `reserved_choices.md`, the task template, the files of `elements/decisions/` and
`elements/common/`, and the three scripts of the trust boundary do not change.

## Foundation entries

Written or changed:

- **New decision, next free number** (rows 2, 3). Meaning: where a project runs the product outside
  the machine on which it is made, which holds unless the definition or a decision of the foundation
  keeps the product there, and no decision settles the matter, the step lists how a human learns of
  a failure as a choice of its own, outside an agent's way to the running product, with a deliberate
  absence always in the comparison, while no definition must hold it, the gate does not check it and
  an approved definition does not come back. *Scope:* project-level, decisions. *Relations:* derives
  from WAY-100 · narrows WAY-121 · narrows WAY-122. *Based on:* none. *Verification* carries
  examples of the absence kept, tested and anchored in the document, a human-only panel recommended,
  a hook-up shown as a cost, a definition silent on where the product runs listing the item, and a
  product kept on that machine and a product with a decision listing nothing.
- **WAY-165, edit** (row 1, D1). Meaning: the logs also ask how long the record lives, between
  deployments too, and an entry that leaves part of a matter unanswered does not settle it. Its
  compliant example says the record's life, a violation leaves it unsaid, the examples of D1 join, its
  rationale also speaks of diagnosis after a deployment, and its *Relations* gain the new decision.
- **WAY-139, edit** (row 4, as D6 reads it). Meaning: the list gains the two items; where the skill
  does not say one, the check quotes the answer a decision of the foundation or an approved definition
  the task carries already gives, and the *To do* writes it into the skill, and otherwise asks the
  human whether to run the step instead of filling the item in; a recorded refusal covers the item.
  *Relations* gain `derives from` WAY-267 and `derives from` the new decision.
- **WAY-121, edit** (D3). Meaning unchanged but for a pointer to the second exception and a compliant
  example. The maker checks its example of a project that "records that the foundation holds every
  choice it needs", which now holds only for a product whose foundation also settles the failure item
  where the criterion is met.

Read and unchanged, each with its reason:

- WAY-122: narrowed by the new decision, with its text left in place, as WAY-166 leaves WAY-123.
- WAY-123, WAY-138, WAY-143, WAY-140, WAY-106, WAY-219, WAY-268: they apply as they stand.
- WAY-166: worded for its family, which the failure item is outside.
- WAY-267: answer 5.
- Invariant `project-technology-record`: unchanged in meaning (To do 6).
- Glossary and part map: D9; `project-level/**` already claims the new file, and the part's
  responsibility holds.

## Left to the maker

- The wording of every entry and text, within what is decided above, including how the new text
  writes the matter out, and the *Rationale* of each entry.
- The next free number, and whether the *Rejected* of the new decision and of WAY-139 share the one
  way answer 5 keeps, by the template's rule for a row's source.
- How the pointer sits in WAY-121, and how WAY-165 keeps to three sentences.
- The search of the whole foundation (WAY-33) and the return step.
- Whether one author can hold the change is the orchestrator's choice.

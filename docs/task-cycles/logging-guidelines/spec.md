# Spec — Ustalić, co produkt zapisuje w logach, żeby dało się sprawdzać jego działanie

- Task: `.runs/task-cycles/logging-guidelines/task.md`
- Open choice: whether a product's decision on the new rules of the coding template is part of the
  decision adopting that template or an entry of its own, and what it holds; which English words the
  template uses for "przepływ" and "część"; and the form of those rules in the template — the rule
  of scope To do 3 names, the headings, their place in the required form, their fields, and how a
  product's file departs from them.

## Intent

An agent can reach a running product's logs, but nothing in the-way says what code has to write to
them, so the agent writing a change and the agent reviewing it share no rule by which to judge
whether a change leaves a trace of a failure. The change gives the coding template required rules on
failures and logs, makes the skill `maintain-coding-guidelines` lead a product to its own decision on
them, and gives the review two general lines that compare a change with rules of this sort. It
changes the-way's text and foundation only; no product is touched.

## Goals and non-goals

Goals:

- the coding template requires six rules on failures and logs in the general file;
- each product reaches one decision of its log that adopts those rules or departs from them, on the
  first coding guidelines, at an extension, and at a refresh that finds them missing;
- the eight rows of *Settlements to record* stand in the-way's log, each whole;
- the review compares a change with every rule without an invariant that it reaches, and compares
  changed guidelines with their templates, with no line naming these rules.

Non-goals:

- where the logs go, how long they live and how a human learns of a failure: the step that settles
  technology keeps them (WAY-165, WAY-270);
- extending any product's guidelines (the task's *Out of scope*);
- a fourth standing check, a new mode of the skill, a change of WAY-211, a new skill, or an
  invariant or test of the-way;
- a change to what the audit reads (D8).

## Constraints

- The task's *To do*, its answers to questions 1–12, read with the marks of which answer replaces
  which, and rows 1–8 are settled; this spec reopens none of them.
- To do 1 and question 6: rules, each with *Invariant* `none` unless a cheap test checks the whole
  rule on a convention of the product's code. Question 8: the events are a rule of their own.
  Question 12: the list stands in a rule of the guidelines and the principle in the decision.
- WAY-171 and `product-guidelines/template.md`: a binding rule stands under `## Rules` with the four
  fields, its heading in English; a dropped required rule holds only `none — <PREFIX-NN>`.
- WAY-173: what the template carries binds a product only through a decision of its log.
- `elements/decisions/template.md`: one to three binding sentences (WAY-05); a new rule next to an
  existing decision is a new question (WAY-19).
- WAY-104: in a product's `foundations/`, the last word of a term of the-way's glossary, written
  bare, keeps the meaning of the process.
- WAY-27, WAY-05, WAY-134: an entry points to no source a reader cannot reach, its prose names no
  file, and its *Rejected* comes only from the row's source.
- The task's Context and its question 11: no product is read or named, in any entry or file.
- Trust boundary: no file this change touches is one the part map names as a trust boundary. The
  files named there in `project-level` are its three scripts, and this change touches only a
  Markdown file of that part.

## Decisions

### D1 — The product's decision is one entry of its own

A product's decision on these rules is one entry of its log, apart from the decision adopting the
coding template. The rules bind a product only through that entry; the decision adopting the template
does not carry them, whatever its wording and at whichever pin it was written.

It holds, in at most three binding sentences:

1. which of the rules the product adopts, all of them unless the human reported a departure from a
   rule or from the ban on personal data, and the form of a line;
2. the principle of scope: which identifiers and which business events the product logs;
3. the boundary: an item that fits the principle the agent adds alone, an identifier of a thing
   among them, and whatever points to a person takes the human's consent, the number the product
   gives a user being settled when the list is accepted and taking consent if added later.

The reason for what is left out stands in *Rationale*. Which rules the product takes is one question
(WAY-19), so a departure from a single rule is this entry, not a second one; a later departure edits
it in place, approved as WAY-30 and WAY-172 give. A dropped rule reads `none —` with this entry's
number, the other rules name the same number in *Decision*, and D3 gives the form of each departure.

| Way | Gives | Costs | Verdict |
|---|---|---|---|
| one entry of its own | one shape on both routes; a product that adds the rules leaves its adopting decision alone; To do 3's four items fit three sentences | one entry more in each log | chosen |
| part of the decision adopting the template | one entry fewer for a product with no guidelines | adoption plus four items will not fit three sentences; a product that adds the rules edits an old decision; an adopting decision worded generally could be read as pulling in rules at a later pin, against "binds from its decision" (question 2) | rejected |
| several entries (adoption, scope, form) | each changes alone | To do 3, questions 12 and 1 and the Context speak of one decision; a departure has to drop each | rejected |

Cost if wrong: an entry too many in each product's log, merged by a change of that log.

What a product's log ends up holding:

| Product | Its log |
|---|---|
| no guidelines, adopts the rules | what it holds today (the decision adopting the template, each standing check, each exemplar), plus this one entry, plus a decision of the library where one is chosen (D6) |
| has guidelines, adds the rules | its adopting decision unchanged, plus this one entry, plus a library's decision where one is chosen |
| departs from all the rules, a "no" at a refresh included | this one entry, saying so with the reason, and nothing else: no principle, boundary, form or list, and no question of a library |
| departs from one rule | this one entry, naming the rule and the reason and keeping only what a kept rule reads; where the rule is `### Logging scope`, it names the two rules that go with it (D3) |
| departs from the ban on personal data alone | this one entry, naming that ban and the reason; the rule stays, with the rest of what it holds (D3) |
| logs an identifier that points to a person, and nothing more | no departure: this one entry as it stands, and an item on the list, with the human's consent (D3) |

The law binds a product whatever it decides here (WAY-86); this entry does not restate it.

### D2 — The words

| Polish | English | Why, and what was rejected |
|---|---|---|
| przepływ | `case flow` — what the product does for one case, from a request or a background job to its end | Bare `flow` is rejected: in a product's foundation and in the-way's log it keeps the process meaning, a critical flow in short form (WAY-104, WAY-45), so a rule on "flow lines" would read as limited to critical flows. `request flow` leaves out a background job. `operation` collides with nothing but gives no sense of size or of end to end. `trace` names a record and a tool, not what the product does. Bare `case` would need an entry, which then costs every product whose domain says "case" a qualifier. `case flow` is a phrase holding the word, as WAY-104 asks, built from the task's own "sprawa". |
| część | `the rules on failures and logs`; once introduced, `these rules` | `part` is a part of the map, in the same file and in *Applies to*. `section` is what a `##` heading opens, which these rules are not. `set` is a linter's set of rules in the same template. No noun is needed: the phrase says what the rules are about. |
| pozycja listy | `item` | `entry` is a term of the glossary. |
| log (działającego produktu) | `logs`, `log line`; never bare `the log` or `the product's log` | In these templates and in the foundation `the log` is the decision log. `the logs` is the wording of WAY-165 and WAY-270. |
| zakres produktu | `logging scope` | `scope` alone reads as a decision's field. |
| awaria; przewidziana odmowa | `failure`; `expected refusal` | |
| tryb awaryjny | `degraded mode` | |
| ostatnie miejsce | `last-resort handler` | |
| zadanie w tle | `background job` | `task` is the process's word; `background-job` already stands as a kind in the template. |

The test of `elements/glossary/template.md` (WAY-95): a word takes an entry when it means something
other than a reader who knows the field takes it to mean. `case flow` means what its two words say,
and its sentence stands in the rule and in the entry of row 5; `the rules on failures and logs` is
ordinary words. Neither takes an entry, for the reader of the template or of a product's guidelines.
`failure` stays out of the glossary too: its meaning is a choice of row 2, carried by that entry and
the rule, and an entry would make every other use of the word a second meaning.

The human hears neither phrase as a term. Following "How to show" in `SKILL.md` and WAY-174, the
skill's question asks about the rules as a whole by their effect: when something goes wrong for a
user the logs say what broke and why, the product never pretends all went well, what happened to
one order can be found, and no password or personal detail lands there. It first says in plain
words what logs are. A case flow reaches the human as everything the product did for one order or
one request.

Cost if wrong: a rename across the template, the skill and nine entries, cheap before the merge; the
human sees the words at the merge (WAY-114).

### D3 — The form of the rules in the template

**Six rules.** The five of To do 1 say how code writes a record; the rule of scope says what the
product promises to log, so it is a sixth. To do 3 and question 12 name one rule holding the list,
and question 8 makes the events a rule of their own, so identifiers and events stand apart.

| Way | Costs | Verdict |
|---|---|---|
| a sixth rule holding both lists; the identifiers, events and personal-data rules name it | one heading more | chosen |
| identifiers and events under one heading, carrying the list | against question 8, To do 1 and row 1 | rejected |
| each list in its own rule, no sixth | two places to add an item, no "rule of scope" as To do 3 names one | rejected |
| a section `## Logging scope` of its own | a list outside a rule, against question 12, with no *Decision* field | rejected |

The headings, in this order under `## Rules`, each required:

| Heading | Its *how to apply* holds | Row |
|---|---|---|
| `### Recording a failure` | what a failure and an expected refusal are; a failure written always with its cause, the original error and not a bare string, once, where code handles it; one last-resort handler for each separately running program | 2 |
| `### Hiding a failure` | a failure turned neither into an "all fine" answer nor into an empty list; a degraded mode only where a task sets it, recording it as a decision of the product, and always leaving a line | 3 |
| `### Identifiers in log lines` | a line of a case flow carries the identifiers that join its events, each under the same name in every line, so that a search finds the whole case, in the form the product's decision gives; a line outside a case flow carries none; a line from the last-resort handler need carry none | 5 |
| `### Business events` | each event `### Logging scope` lists leaves a line | 5 |
| `### Secrets and personal data` | no secret in the logs, with no exception, so an identifier that is a secret stays out even where it stands on the list; no personal data, the identifiers `### Logging scope` lists being the one exception, to this ban alone; no whole object or request body, which does not touch the error itself; an original error that quotes such values is written without them, with its kind, code and place in the code, this rule prevailing over `### Recording a failure` | 6 |
| `### Logging scope` | the list of today: the identifiers, each with the name it takes in every line, and the business events; that the list is the product's promise and no inventory of its code; how an item is added: in the change that brings it where it fits the principle, and through WAY-172 where it points to a person | 4 |

**Place in the required form.** The six stand after `### Dependency audit` and before
`### <further rules of the whole product>`, in the order above: the rules of how first, the list
that grows last. The bullet of the required form that says the product's further rules follow the
standing checks now says that the required rules follow them and the further rules follow those.
A product that already has further rules takes the six in between when it adds them. A file of a
kind is unchanged. *What each section carries* gains one bullet for each rule, as the testing
template has them, and says these are no standing checks.

**Fields of each of the six.**

- *Decision*: the product's one entry of D1. A degraded mode's own decision is not listed here, or
  the rule would change with every such decision.
- *Invariant*: `none`, unless a cheap test checks the whole rule on a convention of the product's
  code. A test that catches only a fragment, such as an empty block, is a rule of the product's
  linter under that linter's invariant, once it passes the trial of WAY-203, and not a rule of these.
- *Good* and *Bad*: the template proposes none; the product writes them or `none`, as in the testing
  template. Neither copies the list.
- The list stands in the text after the fields of `### Logging scope`, in no field. A rule carries no
  reason (WAY-168): the reasons stand in the-way's entries and in the product's.

**A product that departs.** From all the rules: each of the six headings stands, holding only
`none — <PREFIX-NN>` with the entry of D1, since WAY-171 keeps a dropped required rule at its place;
the list goes. From one rule: that heading holds the marker and the others stay, save the one case in
the table below: a rule whose subject has gone reads `none —` too, with the same entry, so a departure
from `### Logging scope` puts the marker on three headings. Text the decision keeps as an example may
stand under `## Examples`.

**A product that departs from the ban on personal data and keeps the ban on secrets.** Row 6 lets a
product depart from that ban, and one heading carries it with three things nobody chose to remove.

| Way | What the product's file holds | Costs | Verdict |
|---|---|---|---|
| the rule stays, one ban departed from | the heading and its fields, *Decision* naming the entry of D1; in the rule's text, in place of the ban, the one line `Personal data: none — <PREFIX-NN>`; the rest of the rule as it stands | one line of form, named by the coding template for this rule alone | chosen |
| only the list: what points to a person goes on it with the human's consent | an item of `### Logging scope` | no new form, and the boundary of D1 already holds it, but the exception covers identifiers, so a product that departs from the ban, as row 6 lets it, has no way to write personal data that is no identifier | kept as what comes first, and no departure; rejected as the whole answer |
| the heading dropped, with a warning | `none — <PREFIX-NN>` | the ban on secrets goes too, with the ban on whole objects and the precedence, so a product cannot depart from the ban on personal data and keep the ban on secrets | rejected for this departure; it stays the form of dropping the rule whole |
| two headings, `### Secrets` and `### Personal data` | `none —` on the second | seven rules where To do 1 holds one rule and D3 six | rejected: it changes a settled form |

The order of the skill and of the template:

1. A wish to log something that points to a person is first an item of the list, with the human's
   consent, where the thing is an identifier. That is no departure, and nothing else changes.
2. A departure from the ban itself is the chosen way. The entry of D1 names that ban and the reason.
   The rule keeps the ban on secrets, the ban on whole objects and request bodies, and its precedence
   over `### Recording a failure` for a secret: an original error that quotes a secret is written
   without it, with its kind, code and place. An original error that quotes personal data is written
   as it stands. Only this ban departs in this way, because row 6 names it alone.
3. Dropping the rule whole stays open under WAY-173, with `none —` on the heading, and the skill says
   first what goes with it, as the table below gives.

The line is no second form of a dropped rule: the rule is not dropped, so WAY-171's "holds only" does
not reach it, and WAY-171 lets a discipline's template add what it names at its places. It keeps
WAY-171's reason, that a departure shows where the text would stand. No entry of the-way needs a
correction for it.

What a kept rule still needs, which the template says beside the departure:

| Departed from | Goes with it | Stays |
|---|---|---|
| `### Logging scope` | `### Identifiers in log lines` and `### Business events`, which have nothing left to read and read `none —` with the same entry; the principle, the boundary, the form | `### Secrets and personal data`, with no exception |
| `### Identifiers in log lines` | the form of a line | the identifiers of the list, as the exception to the ban on personal data, while that rule stands |
| `### Business events` | the events of the list and of the principle | the rest |
| `### Secrets and personal data`, the rule whole | the ban on secrets and the ban on whole objects and request bodies; `### Recording a failure` is no longer narrowed, so an original error may write what it quotes, secrets included | the boundary, while `### Logging scope` stands |
| the ban on personal data alone | the exception of the list, which has nothing left to except; the precedence as to personal data | everything else of the rule; the list and the boundary, while `### Logging scope` stands |
| `### Recording a failure` or `### Hiding a failure` | nothing else | the rest |

Cost if wrong: one heading more in each product's file, moved by a later change of the template; and
one line of form in one rule, for a departure few products make.

### D4 — How the rules reach a product

- First guidelines and any extension: step 4 proposes the rules where `guidelines/coding.md` does not
  yet hold them, whatever else the task is about.
- A refresh: `recognize.md`, where the mode is given and before step 2 forks on research, gains the
  check. A `guidelines/coding.md` lacking the required headings, which stay in English in every
  product, gets the proposal. "Yes" makes the task an extension, so steps 2 and 3 run as for one; "no"
  is a departure with its reason, which the same task writes as D1 and D3 give. Headings holding
  `none —` are no absence.
- `recognize.md` also looks for what writes the product's log lines, beside the linter and the
  rest, so that step 4 extends what exists (WAY-210).
- An extension whose only subject is these rules has no tool of its own to research. Its research
  stays the ordinary one: each standing check, with these rules as "the scope being added", as
  `starting_set.md` and `research.md` already say. The linter's agent is the one with something to
  find: rules of a set that catch a fragment of them. A report that a formatter or an audit has
  nothing for this scope is a sound result. Neither file changes, and neither do `trial_run.md` and
  `kinds.md`: `kinds.md` already marks `do not copy` against "a rule the product holds or the task
  settles". That price is the one the human took at question 2, whose narrow way would have changed
  WAY-211.

### D5 — What the skill settles, records and checks

**`settle.md`.** Under "What it settles": the decision of D1, asked of the rules as a whole, with a
departure taken when the human reports it, the skill saying first, as WAY-174 has it, what the table
of D3 gives for that departure, so that a human leaving `### Logging scope` hears that two more rules
go and one dropping `### Secrets and personal data` hears that the ban on secrets goes, and a wish to
log what points to a person being put first as an item of the list; the principle; the form of a line;
the list of today, at adoption from what the product has in code or in its plan; the number the
product gives a user, put to the human at that moment. Under "Invariants": the rule of the fragment
from D3.
Under "Weak points", each said when the choice is proposed, the five of questions 1, 3, 5, 8 and 9
and no others:

- question 1: a list written by hand can drift from the code, and an agent judges whether an item
  fits the principle;
- question 3: the reviewer sees code and not what an error holds at run time, so an unusual leak can
  pass, and whether a user's number in the logs is lawful stays the product's to judge;
- question 5: an agent and the reviewer judge the line between a failure and a refusal, and a
  degraded mode leaves a line while the user sees a working page, so nobody knows unless someone
  reads the logs; how a human learns of a failure belongs to the step that settles technology;
- question 8: the rule covers only listed events, and the agent adds them, so a function nobody lists
  leaves no line;
- question 9: the last-resort handler usually writes without identifiers, and a program that dies
  whole writes only what it manages to.

**`task_document.md`.** *To do* gains writing the six rules or their markers, with the list at
adoption, and installing and configuring the library a task settles. *Questions to settle* gains each
choice above, by the same terms as the others.

**Readiness.** A task of the first guidelines, of an extension, or of a refresh that met the check of
D4 is not ready without the decision of D1 among the choices settled: adopted or departed from with
its reason. These rules are no standing check, and the glossary's term and WAY-202 stay as they are;
the condition rests on a new entry (E9). `hand_back.md` checks it. A refresh that finds the rules in
place and the route of one kind check nothing here. Without this, a task could end with no decision,
which is the "optional" way question 2 turned down.

**`SKILL.md`.** Its opening sentence on what the skill settles, and its bullet "Extend what exists",
gain what D5 and D6 add. Its *description* does not change, so `skill_entry_points.py --write` is not
needed, and no test is touched: `installation/test_coding_guidelines_installation.py` reads the
skill's path and description alone, and no other test reads the text of these files.

### D6 — The library that writes a line

Before anything else the skill looks at what the product has. A way of writing the chosen form that
the product or its language already gives raises no question (WAY-210). Where the form needs a
library, the choice stands as a technology question of the task, and step 4 puts it to the human by
`new_tools.md`, the route `settle.md` already gives "each new tool or library". Where that library
meets the test of `project-level/technology/reserved_choices.md`, as one that adds something to run
or pay for, it is a reserved choice: refinement runs `settle-technology` at the task document instead
and the task is not ready until the human settles it (WAY-268).

- A library that is chosen is a decision of its own in the product's log, as a tool is; the three
  sentences of D1 are full. A later cycle that wants a library, or another one, meets the example
  below: the choice is no cycle's, so it stops at a blocked draft request, as *Writing the files*
  and WAY-172 give, and picks none alone. This closes row 7's guess.
- No research runs for the library: the route for a library today has none, and the price is the one
  WAY-268 already states of a small library. Rejected: adding it to `research.md` and
  `starting_set.md` — research comes at step 2, before the form that shows the need is chosen at
  step 4, and the task does not ask for it. Cost if wrong: options from a model's memory, for a choice
  one task can change.
- `reserved_choices.md` gains an example: such a library chosen by the guidelines skill stays on that
  skill's route, and one that adds something to run or pay for stops. Without it, the row "a small
  library … stays with the task" would have a cycle's agent pick one, against row 7.
- Agreement with WAY-268: the reserved limb is tested first, and only a library that is not reserved
  is a tool of the skill's route, so nothing goes against WAY-268: the entry names `derives from`,
  not `narrows`. A tool that collects failures, and the code that hooks it up, stay with the step
  (the task's Context, WAY-270).

### D7 — The review

`task-cycle/review/SKILL.md`, section 2, gains the two general lines of To do 5, citing WAY-168 and
WAY-170, naming no rule of these and naming the paths of the two templates with their `.the-way`
form, as the line on a reserved choice does. Section 2 binds every review, the whole change included
("Besides section 2"), and a reviewer already gets the guidelines (WAY-213: its own selection for the
whole change, the handoff's for any other). `whole_change.md`, `reading.md` and the handoffs do not
change.

### D8 — The file where a program starts

It stays as the task says. The audit reads named kinds, and nothing reaches that file; what it misses
goes under the existing *Context* item of `task_document.md`, "what the audit or the trial run could
not see", and the review reaches the file when a change does. Widening the audit is a change to
WAY-200 and WAY-201 no row carries.

### D9 — Readings picked

- **A line of the last-resort handler.** To do 1 says it carries no identifiers; row 2 says it may
  carry none. The reason given, that it usually does not know the case, fits row 2. The rule does not
  require them and does not forbid them. E5 writes this as an exception in advance, so E2 and E5 do
  not collide. A line outside a case flow carries none, as row 5 says.
- **"Each separately running program."** The word stays as To do 1 has it, narrowed by no definition.

### Units

Each unit is one file; what it does for the rest is its interface.

| File | Change | Depends on |
|---|---|---|
| `product-guidelines/coding/template.md` | the six headings and the place of further rules in the required form; a bullet for each rule; the departure; *Writing the files* where needed | E1–E6, E9 |
| `product-guidelines/coding/recognize.md` | the check at a refresh, and what writes the lines (D4) | E8 |
| `product-guidelines/coding/settle.md` | D5, D6 | E2–E7, E9 |
| `product-guidelines/coding/task_document.md` | D5 | template |
| `product-guidelines/coding/hand_back.md` | D5 | E9 |
| `product-guidelines/coding/SKILL.md` | D5, D6 | settle |
| `task-cycle/review/SKILL.md` | D7 | WAY-168, WAY-170 |
| `project-level/technology/reserved_choices.md` | the example of D6 | E7 |
| `foundations/decisions.md` | the entries below | — |

Searched once and left as they are: `product-guidelines/template.md`, `product-guidelines/reading.md`,
`new_tools.md`, `starting_set.md`, `research.md`, `trial_run.md`, `kinds.md`,
`orchestrated_mode.md`, `task-cycle/review/whole_change.md`, the testing and styleguide templates,
`README.md` and `installation/README.md`, neither of which says what coding guidelines hold, the
glossary, the invariants and the part map.

## Foundation entries

Nine new decisions, numbered from the next free number, WAY-271. Each row of the task is one entry
and needs no split: rows 2, 4 and 6, the longest, each fit three sentences. E9 is this spec's own. The
search of the foundation for "failure", "swallow", "personal data" and "log" finds no row already
stated; the author repeats it once the wording is settled (WAY-33).

| Entry | Row | Meaning | *Scope* | *Relations* | *Rejected* from |
|---|---|---|---|---|---|
| E1 | 1 | The coding template requires the six rules on failures and logs in the general file, each under its own heading, after the standing checks, *Invariant* `none` unless a cheap test checks the whole rule. | product-guidelines | derives from WAY-173, WAY-168 | `unknown`: the source keeps no way |
| E2 | 2 | The template holds what a failure is, an expected refusal being an ordinary answer outside the rule; that a failure is written always with its cause, the original error, once, where code handles it; and that each separately running program has one last-resort handler, whose line may carry no identifiers. | product-guidelines | derives from E1 | questions 5 and 9 |
| E3 | 3 | The template holds that a failure is not hidden, in an "all fine" answer or an empty list, and that a degraded mode is allowed only where a task sets it as a decision of the product and always leaves a line. | product-guidelines | derives from E1, WAY-100 | question 5 |
| E4 | 4 | The product's principle of scope stands in its decision and the list of today in a rule of its guidelines, as a promise and no inventory; the agent adds an item that fits in the change that brings it, seen at the merge, any identifier of a thing included; whatever points to a person, an email, name, telephone, home address and IP address among them, takes the human's consent, the number the product gives a user being settled when the list is accepted and taking consent later. | product-guidelines | derives from E1, WAY-172, WAY-225 | questions 1, 3, 10 and 12 |
| E5 | 5 | The template holds that the business events the product's scope lists leave a line, that a line of a case flow, one from the last-resort handler apart, carries the identifiers, each under one name in every line, that a line outside one carries none, and that the product's decision chooses the form of a line. | product-guidelines | derives from E1 | questions 4 and 8 |
| E6 | 6 | The template holds that the logs hold no secret, and no personal data, the identifiers on the product's list being an exception to the second ban alone, and no whole object or request body, the error itself apart; where an original error quotes such values this rule prevails over E2 and the error is written without them, with its kind, code and place; the ban on personal data is the template's choice and no restatement of law, so a product may depart from that ban with a reason, the rest of the rule standing and the law binding it regardless. | product-guidelines | narrows E2, derives from E1, WAY-86; its sentence states the area, as WAY-25 asks | questions 3 and 10 |
| E7 | 7 | The human chooses a library that writes a line, on the route of the guidelines skill, in the task that adopts the rules, and the step that settles technology runs only where that choice is a reserved one. | product-guidelines, project-level | derives from E1, WAY-268, WAY-210 | `unknown`: the ways under question 4 answer the form of a line and stand in E5 |
| E8 | 8 | The rules reach a product with guidelines by an ordinary extension, with no route of their own; a refresh that finds them missing proposes them, a yes making the task an extension and a no being a departure with its reason. | product-guidelines | derives from E1, WAY-251, WAY-211, WAY-173 | question 2 |
| E9 | spec | A product's decision on the rules is one entry of its own, apart from the decision adopting the coding template; it says which rules it adopts and what it departs from, the form of a line, the principle of scope and the boundary of E4, keeps only what a kept rule reads, and a task of the first guidelines, of an extension or of a refresh that found the rules missing is not complete without it. | product-guidelines | derives from E1, WAY-173, WAY-171 | the two ways D1 rejects |

How rows meet the rest:

- **E3 and WAY-100, WAY-27.** The binding sentences name what is adopted and where. *Rationale* says,
  as WAY-268 and WAY-270 do, that the-way takes this one rule from lesson m3l5 of the 10xDEVS course,
  because the cause of a failure nobody sees cannot be found, and describes in its own words what the
  lesson says: first stop hiding what happens in the system, then fix the cause. It gives no address.
  *Based on* and *Origin* read `none`. WAY-270 stays true, since it speaks of two questions of the step.
- **E5.** Its *Rationale* carries the explanation the task's Context leaves outside the template, in
  its own words, naming no product: by the number of an order, the id of a user and the id of a
  request, one follows an order's whole history, a user's actions over time and calls between
  applications.
- **E2 and E5.** Both apply to a line of the last-resort handler during a case flow. E5 carries the
  exception in its own sentence, as WAY-30 allows for one written in advance, so neither entry names
  the other as `narrows`, and row 5 loses nothing by it.
- **E6.** *Based on* carries the three passages of question 3 with their addresses and date, as
  sources quoted and no environment fact: the decision would stand if they changed. *Rationale* keeps
  the task's note that this reading is an agent's and no legal opinion.
- **WAY-165, WAY-270, WAY-202 and WAY-167** need no correction: the first two leave what code writes
  to the code, the third is about tools, and the six are rules of the whole of the code.
- No glossary entry, no invariant, no environment fact and no change of the part map.

## Left to the maker

- The numbers, each entry's wording and question, and its *Verification* pair.
- The wording of every line of the template and the skill, within the words of D2 and the headings of
  D3.
- Where in section 2 of the review the two lines stand, and in which bullet of `recognize.md` the two
  additions go.
- Whether *Writing the files* needs a word on the list.
- Running `python -B elements/common/foundation_check.py .` and the gate. No test of the-way is
  written: no invariant comes, and nothing that runs changes. A change of a skill's *description*,
  which this spec does not ask for, would call for `skill_entry_points.py --write`.

# Decision entry template

This file defines how an entry in a product's decision log (`foundations/decisions.md` in the
product's repository) is written. The log says what binds today: one entry for each decision, which
a change edits in place, while git keeps its earlier wordings (WAY-07).

The rules of form the elements share — the language of an entry, the words `none` and `TODO`,
references and identifiers — stand in `elements/common/rules.md`; this template holds what is
particular to a decision (WAY-35).

## Where entries go

- A product keeps all its decisions in one log, `foundations/decisions.md`, whatever they are
  about; the log has no topical sections, and a new entry goes at its end (WAY-18).
- Each decision is one entry under its number, with no version: a change edits the entry in place,
  on the main branch as before it, and the entry holds only its current wording (WAY-07).
- Numbers carry the product's prefix (WAY-19). The forms below use `WAY`, the prefix of this
  repository.

## Decision entry

```markdown
### WAY-NN — <the question this decision answers>

<1–3 binding sentences that answer the question>

<1–3 binding sentences for a part of another question this entry answers, one paragraph for each
such part; none where there is no such part>

- **Scope:** <parts from the part map>
- **Based on:** <environment facts by identifier and sources quoted, joined by ` · `> | TODO — <what is missing, with its source> | none
- **Relations:** derives from WAY-x · narrows WAY-y | none
- **Verification:** invariants: <identifier> · <identifier>. tests: <the parts of the sentences they
  hold, in words>. An agent compares a change with the part no invariant and no test holds:
  - complies: <…>
  - violates: <…>
- **Origin:** <where the full reasoning lives> | recovered from the code at <place> | none

*Rationale:* <…>
*Rejected:* <…> | none considered | unknown
```

- The question names a choice someone could answer otherwise; "what do we take from X" or "what
  changed" is no question, and what such a list carries goes to the decisions that carry each rule
  (WAY-19).
- *Scope* names parts of the part map, never file paths (WAY-21).
- *Based on* names every source outside the product that the decision rests on, joined by ` · `:
  once the environment facts element has entries, an environment fact entry, by its identifier
  alone, for every citation that, once it stopped being true, would call the decision into
  question — a finding about agents or models, the behaviour of a tool the process uses; any other
  source as its address, the place in it, the passage quoted word for word and the date it was read
  (WAY-90).
- A measurement that the product's own people made — its author and its agents — and whose record a
  reader of the product's repository cannot open is no such source and gets no fact entry: its result
  stands in *Rationale*, or in *Rejected* where it weighs a way not chosen, with what was measured and
  under which conditions, and that prose says that the measurement is the product's own and that its
  record is not open to a reader of the repository. A measurement whose report a reader can open at
  an address is a citation, and a fact where the point above asks for one (WAY-90).
- What is not yet known, or the decider's own motive, is no source outside the product.
- Where the decision's source is silent on what it rests on, *Based on* reads
  `TODO — <what is missing, with its source>`, never a bare `TODO` and never `none`; the main branch
  may hold it, and a change that leaves one there puts it before the human (WAY-71).
  `elements/common/foundation_check.py` reports a bare `TODO` there as an error. Where the source is
  silent on only some of what the decision rests on, the known facts and sources stay named and the
  missing one is the last item, `<fact> · TODO — <what is missing, with its source>`; its
  description runs to the end of the value, so a comma or a ` · ` inside it joins nothing
  (WAY-71). *Relations* and *Origin* never read `TODO`: the script reports it (WAY-71).
- *Relations* and *Verification* follow "Relations and precedence" and "Verification" below;
  *Origin* follows "Origin" and "Recovered decisions".
- *Rationale* and *Rejected* are prose which, where the entry's author writes it rather than
  quotes a source, names no file, script or count — a count being how many files, tests or entries
  of its foundation the product holds; a measurement the choice rests on may stand, with what was
  measured and under which conditions, never as a general bound — nor what the process's own tools
  do or lack today, and does not tell how the decision was reached (WAY-05, WAY-29). What a decision forces on
  later work stands in a binding sentence or a field, never in prose (WAY-05).
- `none considered` in *Rejected* says the human weighed no other way; `unknown` says nobody knows
  what was weighed.
- The *Rejected* of a decision written from a row of a task's *Settlements to record* holds the
  ways not chosen that the row's source keeps — under the answer in *Questions to settle* that the
  row's *Source* names, or in that *Source* itself — each with the cost or the reason kept beside
  it; `none considered` where the human said so; or `unknown`, written with no question to the
  human. A way the writer derives — from what the cycle would otherwise guess, from the cost of
  the way chosen, or from the foundation — never enters it (WAY-134).
- In the decision of a technology choice a project or a task settles, the lacks of the option chosen
  and the risks the human took with it stand in *Rationale*, each risk marked as a hypothesis, never
  in *Based on* (WAY-138). The writer of a decision from a row whose *Source* names a question a run
  of the step that settles technology settled reads that question: its *Not chosen* gives *Rejected*,
  its *Based on* gives *Based on*, and its *Lacks* and *Risks taken* give *Rationale*. Where the
  choice changes a decision, the writer edits that decision in place (WAY-30), the human's
  acceptance of the task document being its approval.
- Every field of a decision takes `none` and `TODO` as `elements/common/rules.md` gives them
  (WAY-71).

### Fields and their readers

A field stays in the template only while someone or something reads it (WAY-05).

| Field | Who reads it, when |
|---|---|
| number (heading) | references from entries, tests and code (WAY-02); `elements/common/foundation_check.py`, which reports a number the log does not hold |
| question (heading) | the author and the skill: does the log already answer this question (WAY-19) |
| binding sentences | an agent comparing a change with the decision (WAY-12); the author's search of the foundation (WAY-33); `foundation_check.py`, which compares them with the quotation of each line `decision:` of a test (WAY-02) and with those at the base to find a decision a change alters (WAY-12) |
| Scope | finding the decisions for a change (WAY-21); `foundation_check.py`, which reports a part the map does not hold |
| Based on | the author of a change to a fact or a source, searching for what rests on it (WAY-33); `foundation_check.py`, which reports a fact the foundation does not hold |
| Relations | an agent meeting two decisions that collide (WAY-25); the author's search of the foundation (WAY-33) |
| Verification | its invariants: whoever looks for the checks of the decision, and `foundation_check.py`, which reports an invariant the foundation does not hold; its clause `tests:`: an agent comparing a change with the decision, who learns which parts of the sentences a test holds, while the script does not read the clause (WAY-12); its pair of examples, for the part no invariant and no test holds: an agent comparing a change with the decision (WAY-12) |
| Origin | whoever wants to change the decision and needs the full reasoning (WAY-29) |
| Rationale | the agent in a borderline case; a human considering a change |
| Rejected | the agent proposing an option already weighed, who says what has changed since; the search of the foundation (WAY-33) |

## Binding sentences

- One to three sentences answer the question of the heading, in the first paragraph under it. A part
  of another question that the entry answers (WAY-19) has its own paragraph after that one, also of
  one to three sentences, one paragraph for each part (WAY-05).
- Present tense, describing a state that is to be true, concrete enough to check (WAY-05).
- Normative words — *must*, *must not* — appear only here, in lower case.
- The words *should* and *will*, exclamation marks and the keywords of RFC 2119 in capitals (MUST,
  SHALL, SHOULD, MAY, REQUIRED, RECOMMENDED, OPTIONAL) do not appear; other words in capitals, such
  as `CI`, do (WAY-05).
- Say what is, rather than what is not, unless the forbidden thing is concrete and visible in
  a change.
- An exception foreseen in advance is written into the binding sentences ("X is allowed when
  Y"); acting on it is then not a contradiction (WAY-30).
- A binding sentence states what holds today and names no stage of the product, such as "in the
  MVP": a decision holds until a change replaces, narrows or withdraws it (WAY-01, WAY-22,
  WAY-24).

## Decision or invariant

- An **invariant** names its method of checking and says nothing about why, or about what was
  rejected (WAY-22).
- A **decision** is a choice between options, with a rationale. It binds later work until a change
  replaces, narrows or withdraws it, including what cannot be checked on a commit: direction,
  trade-off principles, non-goals (WAY-22).
- **Test:** can you point to a commit on which the sentence is false? Yes — it is an invariant.
  It is about a choice or a direction — it is a decision (WAY-22).
- **Plan test:** does the rule still bind once the change that brings it is merged? No — it
  belongs to the plan of that work, or to the choices of its cycle record where no plan is
  written, not to the log (WAY-36).
- **Where it goes:** a settlement that passed the plan test goes through five questions, in this
  order. The first "yes" names its place; what passes all five is an entry of the log.
  1. "Is it an instruction for how an agent works?" — it goes to a skill or an instruction file.
  2. "Is it a rule only for how to write code, tests or the look of the product?" — it goes to the
     guidelines of that discipline, as a rule with its reason in one sentence; a rule that carries a
     choice with a real cost stays a decision and the rule names it.
  3. "Is it a single text, number, list or location?" — it goes to the product's data or code, with
     the test that holds it and, where the reason is not obvious, a comment at the value.
  4. "Is it only the lack of a feature?" — it is not written, unless another entry stands on it
     (WAY-26).
  5. "Does an entry of the log already answer the question it answers, in whole or in part?" — it
     becomes a sentence of that entry ("Changing a decision").

  An entry stands only where someone who does not know the decision would do otherwise and a test
  that stops them would not tell them why.

  In the log of the-way itself, question 1 reads "Is it an instruction for how an agent works and
  does it stand in one skill or template of the-way?": the rule stands there with one sentence of
  its reason, and is an entry only where it carries a choice with a real cost, one for which someone
  could reasonably propose the rejected way, in which case the skill or template names the
  decision. In a product's log question 1 stays as above (WAY-293).
- A test holds a decision's sentence by a line `decision:` ("Verification"); a sentence so held gets
  no invariant derived from the decision, and an invariant stays for a rule with no choice behind it
  and for a rule on which several decisions stand (WAY-22). A decision names in *Verification* the
  invariants derived from it and, by the clause `tests:`, the tests that hold its sentences
  (WAY-12).

## Changing a decision

- A number stands for the question a decision answers, carries the product's prefix and is given
  in the order entries are written; a new question gets the next free number, a question
  independent of every existing entry included (WAY-19). A part of the question an existing entry
  answers is a sentence of that entry, in a paragraph of its own ("Binding sentences"), where it
  cannot change without changing that entry; a part that can change on its own is a question of its
  own with its own number (WAY-19). No entry and no withdrawn number holds the next free number.
- A change to a decision edits its entry in place: the binding sentences, the fields, *Rationale*
  and *Rejected* describe the decision as it then stands, never the change (WAY-07, WAY-19).
- A human accepts the changed meaning by merging the request that carries the change (WAY-14),
  unless the change was written whole from an accepted row of a task's *Settlements to record*,
  whose meaning the human accepted with the task document (WAY-114).
- When a new decision answers a question that an older one answered in passing, the sentence moves
  to the new decision, and the older one loses it in the same change (WAY-19).
- A decision no longer needed leaves the log in the change that ends it: its number goes to the
  list of withdrawn numbers, and that change rewrites every reference to it (WAY-02, WAY-18).

## Withdrawn numbers

- A withdrawn number stays withdrawn: it never names a decision again, and nothing refers to it.
- The log carries its withdrawn numbers in one list after its last entry, in this form; a log
  with none leaves the list out:

  ```markdown
  ## Withdrawn identifiers

  | Identifier | Why | Successors |
  ```

- *Why* says why the decision was withdrawn. *Successors* lists the numbers of the decisions that
  took its place, joined by ` · `, each a decision or a withdrawn number of the log, or reads
  `none`.
- `elements/common/foundation_check.py` reports a withdrawn number that stands as an entry or twice
  on the list, a reference to it anywhere outside the list, and a successor the log does not hold.

## Relations and precedence

- *Relations* use a closed list of two types: `derives from` — a higher decision this one serves;
  `narrows` — a decision this one deliberately goes against in a narrower area (WAY-32).
- A relation names the other decision by its number alone, as `derives from WAY-01` (WAY-02), and
  is written in the entry that depends on the other (WAY-18).
- Where two decisions both apply and collide, the one that prevails names the other in
  *Relations* as `narrows`, and its binding sentences state the area where it prevails; nothing
  follows along a chain, and two decisions that narrow each other are an error (WAY-25).
- A collision between two decisions with no precedence recorded is never settled silently by the
  agent that meets it. Where what the human accepted gives the outcome and the change may write
  the decision that prevails, the change records the precedence in that decision and its request
  names it with the passages of what the human accepted that give the outcome, for the human to
  accept at the merge; otherwise the work stops and a human records the precedence by an edit
  (WAY-25).

## Verification

- *Verification* names, after `invariants:`, the invariants of the product's invariants file that
  derive from the decision, each by its identifier, and only where such invariants exist; each of
  them names the decision in *Derives from* (WAY-12, WAY-17).
- A test that holds a sentence of the decision carries beside it a line `decision:`: a comment in a
  tracked file other than Markdown, in the comment forms of the line `invariant:`, that holds
  `decision:`, one decision number as its heading writes it, and one quotation in straight double
  quotation marks to the end of the line, a closing `*/` or `-->` allowed after it. The quotation
  holds no `"`, begins at the start of a sentence of the entry's binding sentences — the start of
  them, the start of one of their paragraphs, or the first word after a full stop and a space — and
  holds at least three words; it stands in the binding sentences once every run of spaces and line
  breaks is replaced by a single space. The line stands at the test that holds the sentence
  (WAY-02).
- *Verification* names the tests that hold the sentences of the decision by the clause
  `tests: <the parts of the sentences they hold, in words>`, with no path, no test name and no
  number: the lines `decision:` find the tests, so the clause is no second copy of the link, and
  the script does not read it (WAY-12, WAY-18).
- A pair of examples is optional: `complies:` a change that keeps the decision and `violates:` one
  that breaks it, for an agent comparing a change with the part of the sentences that no invariant
  and no test checks (WAY-12). A decision whose sentence a test holds in whole carries no pair; one
  whose test holds part of it carries a pair only for the part no test holds. The violating example
  is code that goes against the decision while its entry stays as it is, never a change that
  replaces the decision together with its code (WAY-12).
- A decision whose sentence a test holds keeps its *Rationale* and *Rejected* whole: a test cannot
  say why, and the pair of examples is all that goes (WAY-12).
- With none of these, *Verification* is `none`. Each part stands alone:

```markdown
- **Verification:** invariants: <identifier> · <identifier>.
```

```markdown
- **Verification:** tests: <the parts of the sentences they hold, in words>.
```

```markdown
- **Verification:** an agent compares a change with the decision:
  - complies: <…>
  - violates: <…>
```

## Trade-off principles and non-goals

- A trade-off principle is an ordinary decision. Its question is "What do we choose when A
  conflicts with B?", its binding sentence "When A conflicts with B, we choose A.", and its
  *Rationale* names the problem the principle solves (WAY-26).
- Precedence between principles is recorded pair by pair, as between any two decisions: the one
  that prevails names the other as `narrows`. There is no single ranked list (WAY-25).
- A non-goal is an ordinary decision, one per non-goal: "The product does not do X", with the
  reason (WAY-26). What the product does not do only because no work has brought it yet is no
  non-goal: where later work builds on it, a decision states what the product does today (WAY-26).
  Non-goals live only at product level; a task's exclusions live in its plan,
  or in the choices of its cycle record where no plan is written (WAY-36).
  A non-goal that can be checked on a commit gets a derived invariant, or a test that holds its
  sentence by a line `decision:` and no invariant (WAY-22).

## Origin

*Origin* points to where the full reasoning lives: a research document, a design document, a
merge request, a ticket, or a file at a fixed commit — never to anything deleted when its task
closes. When the whole reasoning is in the entry, it is `none`. Documents go in *Origin*;
*Based on* names sources about the world. The task a decision was made in is not recorded, and a
task document is never named in *Origin*, wherever the product keeps its tasks: the place of tasks
is where work is found, never a source an entry points to (WAY-27). What it holds of the reasoning
goes into the entry's *Rationale* and *Rejected*; *Origin* then reads `none`.

## Recovered decisions

A decision recovered from the code of a product (WAY-29):

- *Origin* is the one sentence `recovered from the code at <place>`, naming where in the code the
  decision shows.
- *Rationale* and *Rejected* are `unknown`, quoted from a source with that source, or given by a
  human who knows them. A rationale an agent proposes goes to a human as a question, never into the
  entry.

## Examples

`examples.md` names, by number, the decisions of this repository's log (`foundations/decisions.md`)
that show the form of an entry; they are read there, in the commit of the-way a product pins,
instead of being copied (WAY-05, WAY-34).

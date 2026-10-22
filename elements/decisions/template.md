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

<1–3 binding sentences>

- **Scope:** <parts from the part map>
- **Based on:** <environment facts by identifier and sources quoted, joined by ` · `> | none
- **Relations:** derives from WAY-x · narrows WAY-y | none
- **Verification:** invariants: <identifier> · <identifier>. An agent compares a change with the
  decision:
  - complies: <…>
  - violates: <…>
- **Origin:** <where the full reasoning lives> | recovered from the code at <place> | none

*Rationale:* <…>
*Rejected:* <…> | none considered
```

- *Scope* names parts of the part map, never file paths (WAY-21).
- *Based on* names every source outside the product that the decision rests on, joined by ` · `:
  once the environment facts element has entries, an environment fact entry, by its identifier
  alone, for every citation that, once it stopped being true, would call the decision into
  question — a finding about agents or models, the behaviour of a tool the process uses; any other
  source as its address, the place in it, the passage quoted word for word and the date it was read
  (WAY-90).
- What is not yet known, or the decider's own motive, is no source outside the product.
- *Relations* and *Verification* follow "Relations and precedence" and "Verification" below;
  *Origin* follows "Origin" and "Recovered decisions".
- *Rationale* and *Rejected* are prose which, where the entry's author writes it rather than
  quotes a source, names no file, script or count, nor what the process's own tools do or lack
  today, and does not tell how the decision was reached (WAY-05, WAY-29). What a decision forces on
  later work stands in a binding sentence or a field, never in prose (WAY-05).
- In the decision of a technology choice a project settles, the lacks of the option chosen and the
  risks the human took with it stand in *Rationale*, each risk marked as a hypothesis, never in
  *Based on* (WAY-138).
- Every field of a decision takes `none` and `TODO` as `elements/common/rules.md` gives them
  (WAY-71).

### Fields and their readers

A field stays in the template only while someone or something reads it (WAY-05).

| Field | Who reads it, when |
|---|---|
| number (heading) | references from entries, tests and code (WAY-02); `elements/common/foundation_check.py`, which reports a number the log does not hold |
| question (heading) | the author and the skill: does the log already answer this question (WAY-19) |
| binding sentences | an agent comparing a change with the decision (WAY-12); the author's search of the foundation (WAY-33) |
| Scope | finding the decisions for a change (WAY-21); `foundation_check.py`, which reports a part the map does not hold |
| Based on | the author of a change to a fact or a source, searching for what rests on it (WAY-33); `foundation_check.py`, which reports a fact the foundation does not hold |
| Relations | an agent meeting two decisions that collide (WAY-25); the author's search of the foundation (WAY-33) |
| Verification | its invariants: whoever looks for the checks of the decision, and `foundation_check.py`, which reports an invariant the foundation does not hold; its pair of examples: an agent comparing a change with the decision (WAY-12) |
| Origin | whoever wants to change the decision and needs the full reasoning (WAY-29) |
| Rationale | the agent in a borderline case; a human considering a change |
| Rejected | the agent, before proposing an option already rejected; the search of the foundation (WAY-33) |

## Binding sentences

- One to three sentences: the first paragraph under the heading (WAY-05).
- Present tense, describing a state that is to be true, concrete enough to check (WAY-05).
- Normative words — *must*, *must not* — appear only here, in lower case.
- The words *should* and *will*, exclamation marks and the keywords of RFC 2119 in capitals (MUST,
  SHALL, SHOULD, MAY, REQUIRED, RECOMMENDED, OPTIONAL) do not appear; other words in capitals, such
  as `CI`, do (WAY-05).
- Say what is, rather than what is not, unless the forbidden thing is concrete and visible in
  a change.
- An exception foreseen in advance is written into the binding sentences ("X is allowed when
  Y"); acting on it is then not a contradiction (WAY-30).

## Decision or invariant

- An **invariant** names its method of checking and says nothing about why, or about what was
  rejected (WAY-22).
- A **decision** is a choice between options, with a rationale. It binds future choices,
  including ones that cannot be checked on a commit: direction, trade-off principles,
  non-goals (WAY-22).
- **Test:** can you point to a commit on which the sentence is false? Yes — it is an invariant.
  It is about a choice or a direction — it is a decision (WAY-22).
- **Plan test:** does the rule still bind once the change that brings it is merged? No — it
  belongs to the plan of that work, or to the choices of its cycle record where no plan is
  written, not to the log (WAY-36).
- Tests live only with invariants; a decision names in *Verification* the invariants derived from
  it (WAY-12).

## Changing a decision

- A number stands for the question a decision answers, carries the product's prefix and is given
  in the order entries are written; a new question gets the next free number, and a new rule next
  to an existing decision is a new question (WAY-19). No entry and no withdrawn number holds the
  next free number.
- A change to a decision edits its entry in place: the binding sentences, the fields, *Rationale*
  and *Rejected* describe the decision as it then stands, never the change (WAY-07, WAY-19).
- A human accepts the changed meaning by merging the request that carries the change (WAY-14).
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
- A collision between two decisions with no precedence recorded stops the work: the agent that
  meets it never settles it, and a human records the precedence by an edit (WAY-25).

## Verification

- *Verification* names, after `invariants:`, the invariants of the product's invariants file that
  derive from the decision, each by its identifier, and only where such invariants exist; each of
  them names the decision in *Derives from* (WAY-12, WAY-17).
- A pair of examples is optional: `complies:` a change that keeps the decision and `violates:` one
  that breaks it, for an agent comparing a change with what no invariant of the decision checks
  (WAY-12).
- With neither, *Verification* is `none`. Either part stands alone:

```markdown
- **Verification:** invariants: <identifier> · <identifier>.
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
  reason (WAY-26). Non-goals live only at product level; a task's exclusions live in its plan,
  or in the choices of its cycle record where no plan is written (WAY-36).
  A non-goal that can be checked on a commit gets a derived invariant (WAY-22).

## Origin

*Origin* points to where the full reasoning lives: a research document, a design document, a
merge request, a ticket, or a file at a fixed commit — never to anything deleted when its task
closes. When the whole reasoning is in the entry, it is `none`. Documents go in *Origin*;
*Based on* names sources about the world. The task a decision was made in is not recorded: git
history gives it.

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

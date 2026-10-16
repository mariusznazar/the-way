# Decision entry template

This file defines how an entry in a product's decision log (`foundations/decisions.md` in the
product's repository) is written. On the main branch the log is append-only: an entry that has
reached the main branch is never edited (WAY-07). The latest version of each number is in force
(WAY-18); the view of the decisions in force answers to the invariants `view-versions` and
`view-links`.

The rules of form the elements share — the language of an entry, the words `none` and `TODO`, the
marks of where a value comes from, the terms of the glossary — stand in
`elements/common/rules.md`; this template holds what is particular to a decision (WAY-35).

## Where entries go

- Every decision version and review record is appended at the end of `foundations/decisions.md`,
  in the order it is written (WAY-18). The log has no topical sections (WAY-18).
- The log holds **decision versions** and **review records** (WAY-18, WAY-24).
- An entry on the main branch is never edited; a fix to it, however small, is a new version.
  Before the main branch, an entry is edited in place, and an edit that changes its meaning is
  accepted again (WAY-07).
- Numbers carry the product's prefix (WAY-19). The forms below use `WAY`, the prefix of this
  repository.

## Decision version

```markdown
### WAY-NN/V — <the question this decision answers>

<1–3 binding sentences>

- **Change:** new decision | <kind>
- **Scope:** <parts from the part map>
- **Based on:** <facts named as <identifier>@<fingerprint>, other citations quoted with their sources> | none
- **Relations:** derives from WAY-x@<fingerprint> · narrows WAY-y@<fingerprint> | none
- **Verification:** level 1 | 2 | 3 — <…>
- **Review when:** <observable state> · check by: YYYY-MM-DD | none
- **Origin:** <where the full reasoning lives> | inherited — searched: <…>; found: <…> | none
- **Approved by:** <who>, YYYY-MM-DD

*Rationale:* <…>
*Rejected:* <…> | none considered
```

In version 2 and later, *Rationale* becomes *Rationale for change* (WAY-19).

- *Change* names the kind of change from the list in "Kinds of change" (WAY-20).
- *Scope* names parts of the part map, never file paths (WAY-21).
- *Based on* quotes every citation with its source, given as an environment fact's source is
  given (WAY-80); it names a fact entry instead, as `<identifier>@<fingerprint>`, for every
  citation that, stopping being true today, would send the decision to review (WAY-90).
- *Rationale* and *Rejected* are prose which, where the entry's author writes it rather than
  quotes a source, names no file, script or count, nor what the process's own tools do or lack
  today, and does not tell how the decision was reached (WAY-05, WAY-29). What a decision forces on
  later work stands in a binding sentence or a field, never in prose (WAY-05).
- In the decision of a technology choice a project settles, the lacks of the option chosen and the
  risks the human took with it stand in *Rationale*, each risk marked as a hypothesis, never in
  *Based on* (WAY-138).

### Which fields take `none` and `TODO`

Every field of a decision version takes `none` and `TODO` (`elements/common/rules.md`, WAY-71),
except:

| Word | Fields that never hold it |
|---|---|
| `none` | *Change*, *Rationale for change*, *Approved by* |
| `TODO` | *Approved by* |

### Fields and their readers

A field stays in the template only while someone or something reads it (WAY-05). Each field
carries the mark of where its value comes from (`elements/common/rules.md`); a reader not built
yet is named by the invariant it answers to
(`TODO — decision pending: which decision names a reader not built yet by its invariant`).

| Field | Who reads it, when | Where its value comes from |
|---|---|---|
| number (heading) | references from entries, tests and code (WAY-02); the format guard (`log-reference-target`) | judgment |
| version (heading) | the format guard (`decision-version-sequence`); the view of the decisions in force (`view-versions`). A reference to a specific version (`WAY-01/1`) is historical and never flagged (WAY-02) | read off |
| question (heading) | the author and the skill: is this a new version of an existing number, or a new number (WAY-19) | judgment |
| binding sentences | an agent comparing a change with the decision (WAY-12); the fingerprint (WAY-31) | judgment |
| Change | the format guard (`decision-change-kind`, `decision-binding-across-versions`); the view (`view-versions`) | judgment |
| Scope | the part map's guard (`decision-scope-names`); finding the decisions for a change (`decisions-found-for-change`) | judgment |
| Based on | the environment facts guard (`based-on-fact-fingerprint`); a human reviewing the decision when a fact changes (WAY-90) | transcribed; for a fact named, judgment, and read off for its fingerprint |
| Relations | the format guard (`relation-type`, `relation-fingerprint-presence`, `narrows-pairs`, and checking a merge `relation-fingerprint-value`); the view (`view-links`) | judgment, and read off for a fingerprint |
| Verification | level 1: the invariants guard (`level-one-decision-invariants`, `verification-invariant-derivation`); level 2: an agent comparing a change with the decision; level 3: a human (WAY-12) | judgment |
| Review when | the periodic review of the foundation (WAY-24); the format guard (`decision-guard-overdue-review`) | judgment |
| Origin | whoever wants to change the decision and needs the full reasoning; the next agent, so it does not repeat a search (WAY-29) | transcribed |
| Approved by | a human considering a change; the format guard (`decision-approval-record`, `decision-approver`) | transcribed |
| Rationale / Rationale for change | the agent in a borderline case; a human considering a change | judgment |
| Rejected | the agent, before proposing an option already rejected; the search of the foundation (WAY-33) | judgment |

## Binding sentences

- One to three sentences: the first paragraph under the heading (WAY-05).
- Present tense, describing a state that is to be true, concrete enough to check (WAY-05).
- Normative words — *must*, *must not* — appear only here, in lower case
  (`TODO — decision pending: which decision keeps normative words to binding sentences`).
- The words *should* and *will*, exclamation marks and the keywords of RFC 2119 in capitals (MUST,
  SHALL, SHOULD, MAY, REQUIRED, RECOMMENDED, OPTIONAL) do not appear; other words in capitals, such
  as `CI`, do (WAY-05).
- Say what is, rather than what is not, unless the forbidden thing is concrete and visible in
  a change (`TODO — decision pending: which decision asks binding sentences to say what is`).
- An exception foreseen in advance is written into the binding sentences ("X is allowed when
  Y"); acting on it is then not a contradiction (WAY-30).

The fingerprint covers only the binding sentences, so a fix to the rationale does not
flag references (WAY-02).

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
- Tests live only with invariants. A decision is verified through the invariants derived from
  it (WAY-12).

## Numbers and versions

- A number stands for the question a decision answers, carries the product's prefix and is given
  in the order entries are written; a new question gets the next free number, and a new rule next
  to an existing decision is a new question (WAY-19).
- On the main branch, every change to a decision is a new version of its number, which gives the
  rationale for the change and restates the binding sentences and fields in full; a repeal has no
  binding sentences (WAY-19).
- *Rationale for change* describes only this change (WAY-19), and so does *Rejected*
  (`TODO — decision pending: which decision sets that *Rejected* of a later version describes only
  this change`).
- When a new decision answers a question that an older one answered in passing, the sentence moves
  to the new decision, and the older one loses it — by a new version on the main branch, by an edit
  before it (WAY-19).

## Kinds of change

The list is closed. Adding a kind takes a decision (WAY-20); the column on references follows
WAY-31.

| Kind | What changes | Binding sentences vs previous version | References to the decision |
|---|---|---|---|
| new decision | — (version 1) | — | — |
| editorial correction | wording, not meaning | differ | flagged; whoever clears the flag confirms the meaning is unchanged (`TODO — decision pending: which decision sets that whoever clears the flag of an editorial correction confirms the meaning is unchanged`) |
| unchanged sentences | fields, the rationale or the rejected options only | identical | not flagged |
| new wording | what the decision says, a whole new answer included | differ | flagged |
| narrowing | an exception is added | differ | flagged |
| challenge | nothing yet — the decision is in doubt | identical | not flagged; still in force, and the view shows a warning |
| repeal | the question no longer needs an answer | none | flagged; in the view, a single line in place of the decision (`view-versions`) |

A reference is flagged when the fingerprint of the binding sentences it carries changes (WAY-31),
and the flag names the kind of change that raised it (`TODO — decision pending: which decision sets
that the flag names the kind of change that raised it`).

A *narrowing* version writes the exception into the decision itself. The relation `narrows` is
used when a different, more specific decision deliberately goes against this one (WAY-32).

## Relations and precedence

- *Relations* use a closed list of two types: `derives from` — a higher decision this one serves;
  `narrows` — a decision this one deliberately goes against in a narrower area (WAY-32).
- Both rely on the binding part of the decision they name and carry its fingerprint:
  `derives from WAY-01@<fingerprint>` (WAY-31).
- A change to a decision's fingerprint reaches the main branch together with every decision that
  relates to it with a fingerprint, each checked against the new binding part and carrying the new
  fingerprint (WAY-31).
- A relation is written in the entry that depends on the other; the view shows it at the other
  entry (WAY-18).
- Where two decisions both apply and collide, the one that prevails names the other in
  *Relations* as `narrows`, and its binding sentences state the area where it prevails; nothing
  follows along a chain, and two decisions that narrow each other are an error, which the format
  guard reports (`narrows-pairs`) (WAY-25).
- A collision between two decisions with no precedence recorded stops the work: the agent that
  meets it never settles it, and a human records the precedence — by a new version on the main
  branch, by an edit before it (WAY-25).

## Verification

- Level 1 — invariants derived from the decision, each named by the identifier of its entry in
  the product's invariants file; every entry named names the decision in *Derives from* (WAY-12,
  WAY-17, WAY-18).
- Level 2 — an agent compares a change with the decision, using a pair of examples:
  `complies:` and `violates:` (WAY-12).
- Level 3 — a human assessment, leaving a trace of who and when (WAY-12).
- Level 2 or 3 only while no invariant can be derived today. When one is derived, the decision
  moves to level 1 — by a version of the kind unchanged sentences on the main branch, by an edit
  before it (WAY-12).
- Deriving an invariant means naming a sentence that a commit can make false. Knowing how to
  check it is separate: its *Method* may still be `TODO` (WAY-12, WAY-71). An unknown method alone
  does not move the decision to level 2 or 3.
- A decision can combine levels: each level covers what it can check of the binding
  sentences (WAY-12).

```markdown
- **Verification:** level 1 — invariants: <identifier> · <identifier>. Level 2 for <…> — an
  agent compares the change with the decision:
  - complies: <…>
  - violates: <…>
```

A decision checked at level 2 alone:

```markdown
- **Verification:** level 2 — an agent compares the change with the decision:
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

## Review

A decision that rests on a prediction carries *Review when*: an observable state and a check-by
date. The field does not lift the decision; whether the state has come is checked by the periodic
review of the foundation. On the date, a review record is appended (WAY-24):

```markdown
### WAY-NN · review YYYY-MM-DD

- **Result:** condition not met — <what was observed>
- **Next check:** YYYY-MM-DD
- **Checked by:** <who>
```

*Result* takes one of three forms (WAY-24):

- `condition not met — <what was observed>`; *Next check* is a date;
- `condition met, decision kept — <why>`; *Next check* is a date or `none`;
- `condition met — changed in WAY-NN/V+1`; *Next check* is `none`, and the new version sets its
  own *Review when*.

`Next check: none` closes the condition. A review record is not a new version of the decision
(WAY-24). In a review record, `none` stands only in *Next check*, and every field takes `TODO`
(WAY-71).

Before the main branch, an edit in place that the decision's approver accepts again answers the
date as well when it rewrites *Review when* from what was observed; a check-by date is moved in no
other way (WAY-24).

*Review when* is only for a state of the world or the product that someone is waiting for.
A change in a decision this one derives from or narrows is caught by the fingerprint of the
relation, not by this field (WAY-31).

## Origin

*Origin* points to where the full reasoning lives: a research document, a design document, a
merge request, a ticket, or a file at a fixed commit — never to anything deleted when its task
closes. When the whole reasoning is in the entry, it is `none`. Documents go in *Origin*;
*Based on* names facts about the world. The task a decision was made in is not recorded: git
history gives it
(`TODO — decision pending: which decision sets what *Origin* holds`).

## Inherited decisions

A decision recovered from the existing state of a product (WAY-29):

- *Origin* records what was searched and what was found: `inherited — searched: <…>; found:
  <…>`.
- *Rationale* is `unknown`, quoted from the source *Origin* points to, or given by a human who
  knows it. A rationale proposed by an agent goes to a human as a question, never into the entry.
- While the rationale is unknown, any change to the decision is approved by a human (WAY-14).

## Approval

- Every version carries *Approved by*: who approved it and when, as `<who>, YYYY-MM-DD`, or who
  approved it by merging the request that carries it, as `<who>, merge of <request URL>`. The second
  form is for an entry an agent writes before the merge that accepts it: it names the approver and
  that merge, because the approver's act is the merge; the agent never writes a date for it. A
  version is approved by a human, never by an agent; a version nobody has approved yet has nothing
  to record there, so *Approved by* never holds `TODO` (WAY-14).
- In the-way, the approver is Mariusz (WAY-14).

## Examples

`examples.md` names, by number, the decisions of this repository's log (`foundations/decisions.md`)
that show the form of an entry; they are read there, in the commit of the-way a product pins,
instead of being copied (WAY-05, WAY-34).

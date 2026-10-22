# Invariant entry template

> **Draft.** This template is written ahead of the decisions it still waits for, so that they can
> be settled against real entries instead of imagined ones. A rule that cites no decision is a
> proposal settled during the element's research, waiting for its decision. Until those decisions
> are written, nothing here binds beyond what the cited decisions already say, and the template
> does not reach the main branch
> (`TODO — decision pending: which decision keeps a draft template off the main branch until its
> decisions are written`).

This file defines how an invariant entry is written. An invariant names its method of checking and
says nothing about why, or about what was rejected (WAY-08, WAY-22). Its status comes from running
its test, never from a status written by hand, and a rule no cheap test can check is kept by review
(WAY-08).

The rules of form the elements share — the language of an entry, every field and the words `none`
and `TODO`, the form of an identifier, when it stays and when a split or a merge replaces it, its
one space with the part map and the environment facts, the list of withdrawn identifiers,
`{fork-point}` and the absence of versions — stand in `elements/common/rules.md`; this template
holds what is particular to an invariant (WAY-35).

## Where entries go

- A product's invariant entries stand in one file, `foundations/invariants.md`, and after its last
  entry the file holds its withdrawn identifiers (WAY-64).
- The identifier names what the sentence constrains, never what it demands, so that a reworded
  sentence leaves it true; where another entry constrains the same thing, it adds the aspect this
  one protects, as `invariant-part-names` and `invariant-part-form`
  (`TODO — decision pending: which decision sets how an invariant's identifier is named`).
- An entry is edited in place and holds only its current wording; it carries no version, and its
  earlier wordings are read from git (WAY-57). An entry that takes in a clause of another keeps its
  identifier, and the other is split
  (`TODO — decision pending: which decision sets that an entry taking in a clause of another keeps
  its identifier`).

## Form of an entry

```markdown
## <identifier>

<one sentence: the invariant>

- **Method:** test | review
- **Rests on:** <environment fact> · … | TODO — <the fact, with its source> | none
- **Derives from:** <decision> · … | <address> § <place> — "<passage>"; read <YYYY-MM-DD> · … | recovered from code — <the place in the code that shows it> | `TODO — <the decision, and where it is expected>` | none
- **Part:** <parts from the part map> | every
- **Violated:** no | yes
```

The form above gives each field the words it takes. The rest of the rule on `none` and `TODO`
stands in `elements/common/rules.md` (WAY-71). After the last entry the file carries its withdrawn
identifiers, in the form, with the *Why* and the *Successors*, that `elements/common/rules.md`
gives (WAY-64).

## Method and test

- *Method* reads `test` where a test of the product's test suite checks the sentence, and `review`
  where no cheap test can: then the review of each change the invariant reaches, by an agent that
  did not make the change, compares the change with the sentence (WAY-08). An invariant whose test
  is not written yet reads `review` (WAY-105).
- An invariant's test is a test of the product's own suite, in the product's language, run by the
  command that runs the product's tests (WAY-61).
- A test checks what its sentence is about, as it stands on the commit being checked: a test fed
  input made up for it is the method of a sentence about the check it exercises, never of one about
  the data that check reads (WAY-61).
- A test cites each invariant it checks, at the test, as a line `invariant: <identifier>` in the
  comment form of its file's language, and names each file it reads as its data on a line
  `data: <path>` (WAY-65). A test stands in a file of code; a Markdown file holds no citing test
  (`TODO — decision pending: which decision sets that a citing test stands in a file of code`).
- An invariant's result is `pass` where every test citing it ran and passed, and `fail` where one of
  them failed; a run in which no test citing it ran gives it no result (WAY-63, WAY-65).
- An invariant's test is seen failing once, with the command that later shows it passing: run before
  the code that satisfies it, or, where the code already has the behaviour, against that behaviour
  broken for a moment (WAY-08). No other break is written for it, and it takes no agent of its own
  (WAY-69). A test protecting elements of an earlier version is accepted the same way when that
  history holds none yet (WAY-223).
- A test that gives different verdicts on one commit is fixed as any test of the product is; the
  foundation records no quarantine for it (WAY-68).
- A change may alter an invariant test in any step of its task, and names in its request each
  invariant test it alters (WAY-03). A file is an invariant test of a change when it cites an
  invariant on `{fork-point}` or on the commit being checked (WAY-65).

## The sentence

- One entry states one invariant, in one sentence. The method and the links stand beside it, not
  inside it (WAY-56). What one sentence may join is judged against the complying and violating pair
  in WAY-56's *Verification* (WAY-56, WAY-12).
- The sentence is the binding part; the method, the links, *Part* and *Violated* stand outside it
  (WAY-56).
- A condition that decides whether a commit makes the sentence true stands in the sentence, unless
  an entry of the foundation or a decision — of the product's own log, or of the-way at the commit
  the product pins — holds it; then the entry links to that entry or decision (WAY-60;
  `TODO — decision pending: which decision sets that an entry links to any entry or decision
  holding its condition`). A condition held in a document the product neither writes nor pins,
  such as an outside standard, stands in the sentence, and the fact it rests on is named in
  *Rests on* (WAY-60, WAY-73).
- A sentence names no branch — neither as a point to compare with nor as the place where it holds —
  since a branch names a different commit by the hour: outside quoted text it holds neither the
  words "main branch" nor "task branch" (WAY-60). A sentence measuring what a commit, a merge or a
  merge request changes names the commit it is measured against as `{fork-point}`, while a state it
  compares may be the one on `{merge-onto}`, the commit of the main branch that a merge into it is
  made onto (WAY-60). A sentence that is to hold on the main branch alone holds where
  `{merge-onto}` exists (WAY-60).
- A sentence may be about a check the product itself holds, as it may be about anything else the
  product holds: whether a check belongs to the product is settled by the part map
  (`TODO — decision pending: which decision lets the part map settle whether a check belongs to
  the product`), and the method of such a sentence is a test feeding that check input made up for
  it (WAY-61). Such a sentence names `{fork-point}` or `{merge-onto}` in quotation marks where it is
  what the check is given (WAY-60, WAY-61). Quoted text, in this template, is text between
  quotation marks; a value in backticks is not quoted.
- A sentence that bounds or equates a quantity measured while the product runs names its bound or
  tolerance, the statistic and the population it is computed over (WAY-60). A bound written with a
  tilde — `~2 seconds` — names no bound, so the sentence states one as a number or has none
  (WAY-60).
- A sentence about what a check reports may also mean that the data it reads meets a rule; where
  it does, the data takes a sentence of its own, and the two stand as two entries, one about the
  check and one about the data (WAY-56, WAY-61).

## Links

- *Derives from* names every decision entry this invariant is derived from, and *Rests on* every
  environment fact it rests on, each by its identifier alone; neither link is optional, and a link
  the author knows is missing reads `TODO` rather than `none` (WAY-17).
- *Rests on* names every environment fact holding a condition that decides whether a commit makes
  the sentence true, and no other: read otherwise, such a fact would change whether some commit
  makes the sentence true, or change a value the sentence copies from it. A fact that is only a
  reason for a decision the entry derives from stays in that decision's *Based on* (WAY-73).
- An entry that no decision entry of the product's own log carries, taken from a source outside
  that log — a ticket, a requirement of the product, met today or not yet — names in *Derives from*
  each such source as a decision's *Based on* quotes a source that is no environment fact: its
  address, the place in it, the passage stating the rule, quoted word for word between quotation
  marks, and the date it was read, as `https://tracker.example.org/browse/GAME-12 § Acceptance
  criteria — "a save of another version is rejected whole"; read 2026-10-21` (WAY-58).
- An entry a human chose from what the product already did before the task writing it began, and
  that neither a decision entry of the product's own log nor such a source carries, reads in
  *Derives from* `recovered from code —` and the place in the code that shows the behaviour
  (WAY-58).
- Neither a source nor the place in the code comes with a reason for the behaviour, nor one an
  agent infers (WAY-58). A decision named anywhere but the product's own log — a numbered decision
  in a concept document, a decision of the-way at the commit the product pins — is no decision
  entry of it (WAY-58).

## Part

- *Part* names the parts of the part map in which a change can make the sentence false, or `every`
  where a change to any part can; never both. A part missing from the list leaves the invariant
  unread by a change that can make it false, and nothing shows it, so a writer in doubt names more
  (WAY-62).
- *Part* has no third value. A sentence no commit of this product can make false is not an
  invariant of this product: it belongs to the foundation of the product whose commits
  decide it (`TODO — decision pending: which decision sets that a sentence no commit of the product
  can make false belongs to another product's foundation`).
- A change, against `{fork-point}`, reaches an entry that names `every` or a part the change
  touches, or that a test the change alters cites, and the agent making the change reads every
  entry it reaches (WAY-62).
- The entry names no failure mode, critical flow or surface (WAY-62).
- In the file holding invariant entries, a change of an entry touches the parts that entry names,
  and `every` touches all (WAY-44, WAY-62).

## Violated

- An invariant the product does not meet today stays whole and reads `yes` in *Violated*; every
  other reads `no` (WAY-51).
- *Violated* turns to `yes` only by a change of the foundation that a human accepts, never by a step
  of implementation, and a change that sets or clears it names that in its request (WAY-51).
- The test of an invariant that reads `yes` in *Violated* stands in the product's suite marked as
  an expected failure in the product's test tool, such as `expectedFailure` or `test.fails`; the
  change in which it starts to pass removes that marking and turns *Violated* to `no` (WAY-51).

## Fields and their readers

A field stays in this template only while someone or something reads it
(`TODO — decision pending: which decision keeps a field in an element's template only while it is
read`).

| Field | Who reads it, when |
|---|---|
| identifier (heading) | a test citing the invariant; `elements/common/foundation_check.py`, which finds every citation and link naming it |
| sentence | the agent making or reviewing a change the invariant reaches |
| Method | the agent making a change the invariant reaches, which runs its test or keeps to its sentence; the agent reviewing that change |
| Rests on | the author of a change to a fact it names, through the search of the foundation; `foundation_check.py` |
| Derives from | the author of a change to a decision it names, through the search of the foundation; the human weighing a change to a recovered invariant or to one taken from a source outside the log; `foundation_check.py`, which reports a decision number the log does not hold, outside a quoted source |
| Part | the agent selecting the invariants its change reaches; `foundation_check.py` |
| Violated | the agent reviewing a change and the human merging it, who see the mark set or cleared in its request |
| withdrawn identifiers | whoever follows an identifier that no longer names an entry; `foundation_check.py`, which keeps a withdrawn identifier from naming an entry again |

## Examples

`examples.md` names, by identifier, the entries of this repository's own invariants
(`foundations/invariants.md`) that show the form of an entry; they are read there, in the commit of
the-way a product pins, instead of being copied (WAY-09, WAY-34).

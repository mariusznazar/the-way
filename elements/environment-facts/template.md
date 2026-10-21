# Environment fact entry template

This file defines how an environment fact entry is written. Facts are about such things as a
platform, a format, a licence, a law, the behaviour of a tool or a finding of a study. An entry is a
sentence and its source: the address, the passage word for word and the date it was read (WAY-80).
Nothing runs to check a fact and no status stands beside it (WAY-81), and nothing its sentence says
is an invariant (WAY-76). An invariant names the facts holding a condition of its sentence in
*Rests on* (WAY-73), and a decision names the facts it rests on in *Based on* (WAY-90).

The rules of form the elements share — the language of an entry, every field and the words `none`
and `TODO`, references, the form of an identifier, when it stays and when a split or a merge
replaces it, its one space with the invariants and the part map, the list of withdrawn identifiers,
`{fork-point}` and the absence of versions — stand in `elements/common/rules.md`; this template
holds what is particular to an environment fact (WAY-35).

## Where entries go

- A product's fact entries stand in one file, `foundations/environment_facts.md` (WAY-64); after
  its last entry the file carries its withdrawn identifiers, in the form, with the *Why* and the
  *Successors*, that `elements/common/rules.md` gives.
- The identifier names what the fact is about, never its value or the edition it cites, so that a
  new edition leaves it true: `json-text`, not `json-rfc-8259`
  (`TODO — decision pending: which decision sets how an environment fact's identifier is named`).
- An entry is edited in place and holds only its current wording; it carries no version, and its
  earlier wordings are read from git (WAY-79).

## Form of an entry

```markdown
## <identifier>

<one sentence: the fact>

- **Source:** <address of the edition> § <place> — "<passage, word for word>"; read <YYYY-MM-DD> · … | <address of the page> (archived: <address of the archived copy>, <YYYY-MM-DD>) § <place> — "<passage, word for word>"; read <YYYY-MM-DD>
```

The form above gives the entry its one field: *Source* takes neither `none` nor `TODO`, since a fact
without a source is not written (WAY-80). The rest of the rule on `none` and `TODO` stands in
`elements/common/rules.md` (WAY-71). After the last entry the file carries its withdrawn
identifiers.

## Which facts are written

- A decision's *Based on* names a fact entry for every citation that, once it stopped being true,
  would call the decision into question — a finding about agents or models, the behaviour of a tool
  the process uses — and quotes every other citation with its source, as a precedent or a past event
  (WAY-90).
- A finding of a study is such a citation. Its fact says what the study found; the version of the
  paper stands in the address of its source, and the models the study measured, by the names it
  gives them, in the sentence or in a passage *Source* quotes. That the agents of this process
  behave the same is no part of the fact; a decision citing a finding none of whose measured models
  come from the publisher of this process's models says in its rationale that it takes the finding
  across publishers (WAY-85).
- An invariant names in *Rests on* only the facts holding a condition that decides whether a commit
  makes its sentence true (WAY-73). A fact about what runs an invariant's test — how a tool behaves
  under the runner's configuration, which interpreter runs a script — is no such fact
  (`TODO — decision pending: which decision sets that a fact about what runs a test is not one an
  invariant rests on`).
- The current state of a setting that people of the product change outside its repository — who
  can open it, a host's access rule — is a fact, its source the place where that state is shown. A
  choice of such a setting is a decision only where the product declares it, and that decision
  rests on the fact (WAY-84).
- A fact may be about something outside that depends on the product — a product that pins it and
  reads one of its surfaces — only where a decision about that surface would be called into question
  were it no longer true. The partners themselves stay in the part map's external context
  (`TODO — decision pending: which decision sets when a fact may be about something outside that
  depends on the product`).
- A task's return step writes, in the same change, each source outside the product that the change
  rests on and the foundation does not yet hold, as a fact where this section asks for one (WAY-11).
- A fact stands only while an invariant's *Rests on* or a decision's *Based on* names it (WAY-73).

## The sentence

- One entry states one fact, in one sentence: what one edition of one source says, with one reason
  to change. Pages of one document published together in one edition count as one source. That is
  the most an entry holds, not a reason to join: two facts from one edition whose sentences are
  about different things stand as two entries (WAY-76).
- The sentence states what is true of the world today, in the present tense
  (`TODO — decision pending: which decision sets that a fact's sentence is in the present tense`),
  and nothing it says is an invariant (WAY-76).
- The sentence says no more than its source says: where the source recommends, the sentence does
  not require (WAY-80).
- The sentence names an edition of its source only where the product stands on that edition
  (`TODO — decision pending: which decision sets that a fact's sentence names an edition only where
  the product stands on it`). What the fact is true of is shown by the edition its source cites, or,
  for a source that publishes no editions, by the date it was read; the entry has no field that
  names it again (WAY-77).
- The sentence holds no word whose meaning moves with the date, such as "latest" or "newest"
  (WAY-77).
- A range the product declares — the version of Python it runs, in a file a tool reads — is a
  sentence about the product, so an invariant states it, never a fact (WAY-77).
- The binding part of the entry is its sentence; *Source* stands outside it, so a source re-read on
  a new date that still says the same changes nothing that rests on the fact (WAY-78).

## Source

- Every entry has a source; a fact without one is not written (WAY-80), and finding it is a task
  (`TODO — decision pending: which decision sets that finding a missing source is a task`).
- A source takes one of two forms (WAY-80):
  - an edition with its publisher's own address, the place in it, the passage the fact rests on word
    for word, and the date read. An address the publisher moves to newer text is no edition,
    whatever version its path names: cite the frozen address, and where there is none, the page is
    one without editions;
  - a page without editions, with the closest archived copy that already exists and its date — never
    one made for the entry, since that writes to someone else's service — and the place, the passage
    and the date read.
- A further page of the same edition names its address and place. Another place of the same page
  follows that page's last passage as `§ <place> — "<passage, word for word>"`, joined by ` · `,
  and shares the page's address and date read. Several addresses stand in one entry only as pages
  of one edition, or as a page and its archived copy (WAY-80, WAY-76).
- The passage is the page's text as a reader sees it, with markup dropped and whitespace collapsed,
  taken from one run of text — a paragraph, a list item or a table cell; a rule spread over several
  runs is quoted as several passages of the same place, joined by ` · ` (WAY-80).
- A citation that names no edition names the edition its dependant stands on, where the dependant's
  sentence names one, and otherwise the edition in force on the date the citation was read
  (`TODO — decision pending: which decision sets which edition a citation naming none takes`).
- A fact resting on a whole section of rules — a pattern syntax, an algorithm — quotes the sentence
  of the source that sets those rules, and names the section by its place alone, where the edition
  has an address of its own (WAY-80).
- A model's memory, an agent's paraphrase, and a text quoting the source are no source (WAY-80).
- The passage is what a reader compares the source with to see whether it still says so; no digest
  of the source is kept, so a change to the text next to the passage passes unseen (WAY-78).
- A fact about the visibility of a repository the product links to names that one repository,
  since each has its own owner and changes on its own (WAY-84); where an invariant rests on the
  visibility of the repositories linked, each new link adds such a fact, named in its *Rests on*
  (WAY-84, WAY-73).
- The source of a setting only its setter can read is
  `TODO — decision pending: which form of Source a setting read only with its setter's credentials
  takes, since WAY-80 gives none`.

## Changing a fact

- A fact changes when someone finds that its source no longer says what its sentence says, or that
  a newer edition the product stands on says otherwise — the author of a change that reads the
  fact, a task's return step, or the review of the foundation against the product, a task of the
  product's backlog (WAY-82, WAY-24). The entry is then changed in place, or withdrawn as shown
  false.
- A change of a fact's sentence reaches every invariant whose *Rests on* and every decision whose
  *Based on* names it: the author's search of the foundation finds them, and each is checked against
  the new sentence and corrected in the same change (WAY-33).
- A newer edition of a source, or a newer release of a tool the sentence names, leaves the fact true
  of the one it names, and an announced revision changes nothing until the new edition is out
  (WAY-82). Moving the product to another release is a decision's to make
  (`TODO — decision pending: which decision sets that moving the product to another release of a
  tool is a decision's to make`).
- An entry names no date or condition for its review, and no decision citing it names one for it
  (WAY-82, WAY-24).

## Withdrawn identifiers

A fact shown false does not leave the file: its identifier moves to the list that closes it, with
what showed it false in *Why*, so that nobody writes it again. A fact whose last dependant goes is
withdrawn in the same change, with that in *Why* (WAY-64, WAY-73).

## Catalogues and obligations

- A voluntary catalogue of requirements — ASVS, WCAG where no law requires it — binds the product
  only through a decision adopting it, naming the catalogue, its edition, the level or list taken,
  and the area of the product (WAY-86). A requirement of it that an invariant takes a condition
  from is then a fact (WAY-86): its source is the edition, the requirement's identifier and its
  text word for word, and the invariant names it in *Rests on* (WAY-73).
- A binding rule — a law, a contract, a licence — needs no adoption: what it requires is a fact,
  and the product is held to it until a human settles, in a decision, that the rule does not apply
  (WAY-86).
- A descriptive source — an RFC, a list of modules — needs nothing beyond the fact
  (`TODO — decision pending: which decision sets that a descriptive source needs nothing beyond the
  fact`).
- A likeness an agent notices between the product and a requirement nothing has adopted or applied
  goes to a human as a question: "do we adopt this?" or "does this bind us?" (WAY-86).
- How an obligation raises the criticality of a part stands in the part map template (WAY-46).

## Fields and their readers

A field stays in this template only while someone or something reads it
(`TODO — decision pending: which decision keeps a field in an element's template only while it is
read`).

| Field | Who reads it, when |
|---|---|
| identifier (heading) | an invariant's *Rests on* and a decision's *Based on*; `elements/common/foundation_check.py`, which reports a fact they name that the file does not hold |
| sentence | whoever writes, changes or reviews what rests on the fact; the author's search of the foundation (WAY-33) |
| Source | whoever checks whether the source still says what the sentence says; the human reviewing the fact |
| withdrawn identifiers | whoever follows a citation to a fact shown false; `foundation_check.py`, which keeps a withdrawn identifier from naming an entry again |

## Examples

The entries of the-way's own `foundations/environment_facts.md` serve as this element's examples
(WAY-09). Until the foundation is migrated, they still carry the earlier form below — a version,
*Holds for* and *Method* — which the form above leaves out.

## Read by the format guard until the migration

The three sections below hold the earlier form of an entry, which `format_guard.py` beside this file
and its tests read while `foundations/environment_facts.md` still keeps that form: a version in the
heading, *Holds for*, *Method* and a fact's result. They bind no entry written by the sections
above, and they go with the format guard when the foundation is migrated
(`agent-instructions/README.md`).

## Entry

Earlier form, read by the format guard only until the migration.

```markdown
## <identifier>/<version>

<one sentence: the fact>

- **Holds for:** <the tools, platforms, editions or measured models the sentence is true of, with versions>
- **Source:** <address of the edition> § <place> — "<passage, word for word>"; read <YYYY-MM-DD> · … | <address of the page> (archived: <address of the archived copy>, <YYYY-MM-DD>) § <place> — "<passage, word for word>"; read <YYYY-MM-DD> | observed: `<command>` on <tool and version, platform>; run <YYYY-MM-DD>
- **Method:** `<program> <arguments>` | <path of a file a human re-reads the source against> | `TODO`
```

## Holds for

Earlier form, read by the format guard only until the migration. *Holds for* named what the
sentence is true of, with versions. It never reads "latest" or "newest".

## Result

Earlier form, kept until the migration. A fact's result was `pass`, `fail`, `unchecked` for a
reason the invariants template gave, or `error`.

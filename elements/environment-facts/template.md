# Environment fact entry template

This file defines how an environment fact entry is written. Facts are about such things as a
platform, a format, a licence, a law, the behaviour of a tool or a finding of a study. A fact names
its method of checking (WAY-81), and nothing its sentence says is an invariant (WAY-76). An
invariant names the facts holding a condition of its sentence in *Rests on* (WAY-73), and a decision
names the facts it rests on in *Based on* (WAY-17, WAY-90). Its current result comes from running
its method, never from a status written by hand
(`TODO — decision pending: which decision sets that a fact's result never comes from a status
written by hand`).

The rules of form the elements share — the language of an entry, every field and the words `none`
and `TODO`, the terms of the glossary, the marks of where a value comes from, the form of an
identifier and its one space with the invariants and the part map, the list of withdrawn
identifiers, human verdicts, `{fork-point}` and the version of an entry — stand in
`elements/common/rules.md`; this template holds what is particular to an environment fact
(WAY-35).

## Where entries go

- A product's fact entries stand in one file, `foundations/environment_facts.md` (WAY-75); after
  its last entry the file carries its withdrawn identifiers, in the form, with the *Why* and the
  *Successors*, that `elements/common/rules.md` gives.
- The identifier names what the fact is about, never its value or the edition it cites, so that a
  new edition or a new range leaves it true: `json-text`, not `json-rfc-8259`
  (`TODO — decision pending: which decision sets how an environment fact's identifier is named`).
- An identifier the file held on the commit the task branch left the main branch from stays, as an
  entry or as a withdrawn identifier giving why and naming its successors or `none`. Splitting or
  merging entries gives each entry that comes out of it a new identifier, and any other change keeps
  it (WAY-75).

## Which facts are written

- A decision's *Based on* names a fact entry for every citation that, stopping being true today,
  would send the decision to review — a finding about agents or models, the behaviour of a tool the
  process uses — and quotes every other citation with its source, as a precedent or a past event
  (WAY-90).
- A finding of a study is such a citation. Its fact records what the study measured, with the
  version of the paper in *Source*, and stays true;
  what the decision draws from it is that the agents of this process behave the same, which stops
  holding as the measured models go. That is a prediction: it stands in *Review when* of each
  decision citing the fact, as a state a script can check, never in the fact (WAY-85, WAY-24).
- An invariant names in *Rests on* only the facts holding a condition that decides whether a commit
  makes its sentence true (WAY-73). A fact about what runs a method — how a tool behaves under the
  runner's configuration, which interpreter runs a script — is no such fact (WAY-73).
- The current state of a setting that people of the product change outside its repository — who
  can open it, a host's access rule — is a fact whose method reads that state where it lives, or is
  a re-read by the person who sets it where reading it takes their credentials. A choice of such a
  setting is a decision only where the product declares it, and that decision rests on the fact
  (WAY-84).
- A fact may be about something outside that depends on the product — a product that pins it and
  reads one of its surfaces — only where a decision about that surface would need review were it no
  longer true. The partners themselves stay in the part map's external context
  (`TODO — decision pending: which decision sets when a fact may be about something outside that
  depends on the product`).
- A fact stands only while an invariant's *Rests on* or a decision's *Based on* names it (WAY-88).

## Entry

```markdown
## <identifier>/<version>

<one sentence: the fact>

- **Holds for:** <the tools, platforms, editions or measured models the sentence is true of, with versions>
- **Source:** <address of the edition> § <place> — "<passage, word for word>"; read <YYYY-MM-DD> · … | <address of the page> (archived: <address of the archived copy>, <YYYY-MM-DD>) § <place> — "<passage, word for word>"; read <YYYY-MM-DD> | observed: `<command>` on <tool and version, platform>; run <YYYY-MM-DD>
- **Method:** `<program> <arguments>` | <path of a file a human re-reads the source against> | `TODO`
```

The form above gives each field the words it takes: *Method* alone takes `TODO`, no field takes
`none`, and *Source* takes neither (WAY-80). Every field appears in every entry, and the rest of the
rule on `none` and `TODO` stands in `elements/common/rules.md` (WAY-71).

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
  the product stands on it`).

## Holds for

- *Holds for* names what the sentence is true of: a tool and its version, a platform, an edition, or
  the version of a paper and the models it measured — by their dated identifiers where the study
  gives them, and by the names it gives otherwise, which a script checking a decision's
  *Review when* resolves; that script does not exist yet (WAY-77, WAY-85).
- It never reads "latest" or "newest", since what they name changes with the date (WAY-77).
- Where the source publishes no editions — a page with no versions, or documentation of a tool that
  shows only its current release — *Holds for* names what the sentence is about and says the source
  gives no version: `JSON Lines, which jsonlines.org publishes without versions`. The date read
  stays in *Source*, so that a re-read flags nothing (WAY-77, WAY-78).
- The sentence and *Holds for* are the binding part: the entry's fingerprint covers the sentence
  and the value of *Holds for* joined by a line break, computed as WAY-39 says. The source, its
  passage and its date stay outside it, so a re-read source that says the same flags nothing
  (WAY-78).
- A claim that differs in a new range changes the sentence or *Holds for*, and so the version
  (WAY-77, WAY-79); the new claim does not refute the claim true in the past range
  (`TODO — decision pending: which decision sets that a claim for a new range leaves the claim for
  the past range true`).
- A newer release of a tool *Holds for* names coming out fails nothing: the fact about the named
  release stays true, and a probe run on the newer release fails only where the behaviour differs
  (WAY-91). Moving the product to another release is a decision's to make, and what calls for it is
  a condition in that decision's *Review when*, such as the named release leaving support (WAY-24;
  `TODO — decision pending: which decision sets that moving the product to another release of a
  tool is a decision's to make`).
- A range the product declares — the version of Python it runs, in a file a tool reads — is a
  sentence about the product, so an invariant states it, never a fact (WAY-77).

## Source

- Every entry has a source; a fact without one is not written (WAY-80), and finding it is a task
  (`TODO — decision pending: which decision sets that finding a missing source is a task`).
- A source takes one of three forms (WAY-80):
  - an edition with its publisher's own address, the place in it, the passage the fact rests on word
    for word, and the date read. An address the publisher moves to newer text is no edition,
    whatever version its path names: cite the frozen address, and where there is none, the page is
    one without editions;
  - a page without editions, with the closest archived copy that already exists and its date — never
    one made for the entry, since that writes to someone else's service — and the place, the passage
    and the date read;
  - an observation naming the command, the tool and its version, the platform and the date it ran.
- A further page of the same edition names its address and place. Another place of the same page
  follows that page's last passage as `§ <place> — "<passage, word for word>"`, joined by ` · `,
  and shares the page's address and date read. Several addresses stand in one entry only as pages
  of one edition, or as a page and its archived copy (WAY-80, WAY-76).
- The passage is the page's text as a reader sees it, with markup dropped and whitespace collapsed,
  taken from one run of text — a paragraph, a list item or a table cell; a rule spread over several
  runs is quoted as several passages of the same place, joined by ` · ` (WAY-80).
- A citation that names no edition names the edition its dependant stands on, where the dependant's
  sentence names one, and otherwise the edition in force on the date the citation was read — for a
  decision's *Based on*, the date of the version citing it
  (`TODO — decision pending: which decision sets which edition a citation naming none takes`).
- A fact resting on a whole section of rules — a pattern syntax, an algorithm — quotes the sentence
  of the source that sets those rules, and names the section by its place alone, where the edition
  has an address of its own (WAY-80). Where the source publishes worked examples of those rules,
  they are the probe's test data, not its source
  (`TODO — decision pending: which decision sets that a probe runs on the test data its source
  publishes`).
- A model's memory, an agent's paraphrase, and a text quoting the source are no source (WAY-80).
- The passage is what a re-reading compares against: the watch checks that it still stands at the
  address, and no digest of the source is kept, so a change to the text next to the passage passes
  unseen (WAY-78, WAY-82).
- A fact about the visibility of a repository the product links to names that one repository,
  since each has its own owner and changes on its own, and its method reads it
  anonymously (WAY-84); where an invariant rests on the visibility of the repositories linked, each
  new link adds such a fact, named in its *Rests on* (WAY-84, WAY-73).
- The source of a setting only its setter can read is
  `TODO — decision pending: which form of Source a setting read only with its setter's credentials takes, since WAY-80 gives none`.

## Method

- A method is a command that begins with the name of the program it runs, or the path alone of a
  file a human re-reads the source against, or `TODO` (WAY-81); no kind of method is written beside
  it (`TODO — decision pending: which decision keeps a method's kind from being written beside
  it`). A fact whose method reads `TODO` is unchecked, and never counts as passed (WAY-74).
- A command whose program the product does not yet declare or produce is written out in full all
  the same, with the program named as it will run (WAY-81); the fact is then unchecked for want of a
  declared or produced command, a different reason (WAY-74).
- A command may probe, watch, or both (WAY-81):
  - a probe runs on test data the source itself publishes where there is any, as NIST's example
    digests (`TODO — decision pending: which decision sets that a probe runs on the test data its
    source publishes`), and asks about the behaviour, never about a version number in its place;
  - a watch reads such data as `obsoleted_by` of an RFC, a withdrawal, a model's deprecation state
    or a support schedule, and checks that the passage still stands.
  A human re-reads what no command can read: law, a licence, an access rule readable only with the
  credentials of whoever sets it (WAY-81, WAY-84).
- A command sets for itself whatever in the runner's configuration a command can set and could
  change its verdict (`-c core.ignorecase=false`), so that it gives the same verdict on every
  machine (WAY-81). Where it cannot — a model that runs the method — that configuration is read off
  the product, and the deliberate break shows the method's fidelity, which holds only where the
  break gives high confidence of detection
  (`TODO — decision pending: which decision sets how a method whose runner's configuration a command
  cannot set shows its fidelity`). The release of a tool a probe runs is read off the
  machine instead, as the next point says (WAY-91). Whether a fact's command, like a check citing an invariant,
  counts only when a deliberate break makes it fail is
  `TODO — decision pending: whether WAY-08's deliberate break binds a fact's method`.
- Where *Holds for* names a release of the tool a probe runs, the probe reads the release it runs
  on and records it in the `description` of its line: a `fail` on any release is a `fail`, and a
  `pass` counts only on a release *Holds for* names, a build of it included, as Git for Windows
  builds git. The method rests on no fact about that release (WAY-91, WAY-73).
- A check cites each fact it gives a verdict for, at the check, as a line
  `fact: <identifier>/<version>` in the comment form of its file's language, and a run records no
  verdict for a fact no check cites (WAY-81); a check citing a version other than the current one
  fails the gate (WAY-79). A check stands in a file of code; a Markdown file holds no citing check
  (`TODO — decision pending: which decision sets that a citing check stands in a file of code`).
- Where the checks of a product's facts stand in the part map is set when its first fact is written
  (`TODO — decision pending: which decision sets that where the checks of a product's facts stand is
  settled with its first fact`). Whether a file holding such a check is read-only during
  implementation, as an invariant test is (WAY-03), is not settled.
- A command records a fact's verdict in the-way's own record of a run, at the one `.jsonl` path it
  names, which git ignores, on a line holding `fact` as `<identifier>/<version>` where a line for an
  invariant holds `invariant`; a failure recorded for no entry holds `invariant` as `null` (WAY-74).

## When a method runs

- When a change enters an entry or changes any of its fields, or alters a file its command names, the gate runs its method on that change (WAY-82; for a change of a field beyond rewording the entry, `TODO — decision pending: whether a change of a fact's field that does not reword its entry runs its method`).
- By the clock, for every fact at once, on the main branch — never inside the gate of a change that
  neither enters nor changes the entry nor alters a file its command names, since the world changes
  with no commit and the gate's verdict would then depend on the date (WAY-82, WAY-60). When the
  clock exits non-zero answers to the invariant `fact-clock-exit`.
- A human verdict on a fact whose method is a path stands where `elements/common/rules.md` places
  it; for a fact, *Until* is the date after which the verdict lapses (WAY-83).

## Result

- A fact's result is `pass`, `fail`, `unchecked` for a reason on the one closed list of reasons the
  invariants template gives for invariants and environment facts, or `error` where there is no
  verdict for any other reason (WAY-63, WAY-74).
- In the gate of a change that runs a fact's method, its `fail` or `error` makes the gate's command
  fail (WAY-63). Elsewhere a `fail` stops no change (WAY-82). The clock records each fact's verdict
  in the-way's own record of a run and exits non-zero when some fact results `fail` or `error`
  (WAY-82); what a failure then becomes — a task, a branch, a message — waits for the design of the
  task cycle (`TODO — decision pending: what a fact's failure on the clock becomes`).
- A watch fails on a published change to its edition — superseded, withdrawn, or updated by a
  published change — or when its passage no longer stands (WAY-82); that leads to a review of the
  fact and does not make the sentence false
  (`TODO — decision pending: which decision sets that a failed watch leads to a review of the fact
  and leaves its sentence true`). An announced revision fails nothing: until the new edition is
  out, the fact holds, and whoever wants to look ahead writes the condition in *Review when* of the
  decision citing the fact (WAY-82, WAY-24). Only the human deciding the change that follows the
  review changes the sentence or *Holds for* (WAY-10), and the new fingerprint then reaches every
  invariant and decision naming the fact (WAY-66, WAY-90).

## Version

- The version of an entry follows `elements/common/rules.md`, with no exception: every change of the
  sentence or of *Holds for* raises the version by one, and no correction keeps it (WAY-79).

## Withdrawn identifiers

A fact shown false does not leave the file: its identifier moves to the list that closes it, with
what showed it false in *Why*, so that nobody writes it again and an older decision citing it still
finds it. A true fact whose last dependant goes is withdrawn in the same change, with that in *Why*,
or the merge fails (WAY-75, WAY-88).

## Catalogues and obligations

- A voluntary catalogue of requirements — ASVS, WCAG where no law requires it — binds the product
  only through a decision adopting it, naming the catalogue, its edition, the level or list taken,
  and the area of the product (WAY-86). A requirement it holds is then a fact: its source is the
  edition, the requirement's identifier and its text word for word
  (`TODO — decision pending: which decision sets that a requirement of an adopted catalogue is a
  fact`), and an invariant taking a condition from it names it in *Rests on* (WAY-73).
- A binding rule — a law, a contract, a licence — needs no adoption: whether it applies is a fact,
  read as applying until a human settles otherwise (WAY-86). Whether a commit that removes what the
  rule covers makes that fact false is
  `TODO — decision pending: whether "the rule applies" is a fact, against WAY-76`.
- A descriptive source — an RFC, a list of modules — needs nothing beyond the fact
  (`TODO — decision pending: which decision sets that a descriptive source needs nothing beyond the
  fact`).
- A likeness an agent notices between the product and a requirement nothing has adopted or applied
  goes to a human as a question: "do we adopt this?" or "does this bind us?" (WAY-86).
- How an obligation raises the criticality of a part stands in the part map template (WAY-87).

## Fields and their readers

A field stays in this template only while someone or something reads it
(`TODO — decision pending: which decision keeps a field in an element's template only while it is
read`). Each field carries the mark of where its value comes from (`elements/common/rules.md`); a
reader not built yet is named by the invariant it answers to
(`TODO — decision pending: which decision names a reader not built yet by its invariant`).

| Field | Who reads it, when | Where its value comes from |
|---|---|---|
| identifier (heading) | an invariant's *Rests on*, a decision's *Based on*, a `fact:` line; the format guard (`fact-identifier-form`, `identifier-holders`) | judgment |
| version (heading) | a check citing the fact (`fact-citation-version`); the format guard, which computes what the version must be (`fact-version-new`, `fact-version-changed`, `fact-version-unchanged`) | read off |
| sentence | whoever reviews what rests on the fact; the fingerprint (`fact-fingerprint-input`) | prose |
| Holds for | the fingerprint (`fact-fingerprint-input`); whoever writes an invariant naming a version within it; a probe, which compares the release it runs on with it (WAY-91); a script checking a decision's *Review when* against the models a study measured, which no invariant states yet | transcribed from the source |
| Source | the watch, which checks that the passage still stands; the human reviewing the fact; the format guard (`fact-source-form`) | transcribed |
| Method | the gate, on a change that enters or changes the fact or alters a file its command names (`gate-fact-run`); the clock (`fact-clock-exit`); a human, for a path; the format guard (`fact-method-form`) | judgment |
| withdrawn identifiers | whoever follows a citation to a fact shown false; the format guard, which keeps it from coming back and checks its successors (`fact-withdrawal-persistence`, `fact-withdrawal-successors`) | judgment for *Why*; read off for the rest |

## Examples

The entries of the-way's own `foundations/environment_facts.md` serve as this element's examples
(WAY-09).

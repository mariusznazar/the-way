# Environment fact entry template

> **Draft.** This template is written ahead of the decisions it still waits for, so that they can
> be settled against real entries instead of imagined ones. Every place that waits carries
> `TODO — decision pending: <question>`. A rule that cites no decision is a proposal settled during
> the element's research, waiting for its decision. Until those decisions are written, nothing here
> binds beyond what the cited decisions already say, and the template does not reach the main branch
> (WAY-06, WAY-09).

This file defines how an environment fact entry is written. An environment fact is something true
about the world around the product — a platform, a format, a licence, a law, the behaviour of a tool,
a finding of a study — with a method of checking it. It says nothing about the product itself: that
is an invariant (WAY-04, WAY-22). An invariant names the facts holding a condition of its sentence
in *Rests on* (WAY-73), and a decision names the facts it rests on in *Based on* (WAY-17). Its current
result comes from running its method, never from a status written by hand.

## Where entries go

- A product's fact entries stand in one file, `foundations/environment_facts.md`, which ends with its
  list of withdrawn identifiers.
- Every entry carries an identifier of one or more words in lower case joined by hyphens, held by no
  other entry or withdrawn identifier of this file, of the invariants or of the part map; `none` is
  no identifier, since *Successors* uses that word.
- The identifier names what the fact is about, never its value or the edition it cites, so that a
  new edition or a new scope leaves it true: `json-text`, not `json-rfc-8259`.
- An identifier the file held on the commit the task branch left the main branch from stays, as an
  entry or as a withdrawn identifier naming its successors or `none` (as WAY-64 has it for
  invariants).
- An entry holds only its current wording; earlier wordings are read from git (as WAY-57).
- An entry is written in English, whatever language the product shows the people who use it and
  whatever language its team speaks (WAY-72).

## Entry

```markdown
## <identifier>/<version>

<one sentence: the fact>

- **Holds for:** <the tools, platforms, editions or measured models the sentence is true of, with versions>
- **Source:** <address of the edition> § <place> — "<passage, word for word>"; read <YYYY-MM-DD> · … | observed: `<command>` on <tool and version, platform>; run <YYYY-MM-DD>
- **Set by:** none | <who in the product sets it, outside the repository>
- **Method:** `<program> <arguments>` | <path of a file a human re-reads the source against> | `TODO`
- **Correction:** none | <fingerprint on the main branch> → <current fingerprint>
```

Every field of the form above appears in every entry. A field holds `none` or `TODO` only where the
form above gives it that word: `none` states that nothing is there, `TODO` that something is known
to be missing (WAY-71). *Source* takes neither: a fact without a source is not written.

After the last entry the file carries its withdrawn identifiers; *Successors* lists identifiers
joined by ` · `, or reads `none`:

```markdown
## Withdrawn identifiers

| Identifier | Why | Successors |
```

## The sentence

- One entry states one fact, in one sentence: what one edition of one source says, with one reason
  to change. Pages of one document published together in one edition count as one source. That is
  the most an entry holds, not a reason to join: two facts from one edition whose sentences are
  about different things stand as two entries.
- The sentence states what is true of the world today, in the present tense, and says nothing of the
  product: a sentence a commit of the product can make true or false is an invariant (WAY-04,
  WAY-22).
- The sentence says no more than the passage in *Source* says: where the source recommends, the
  sentence does not require.
- The sentence names an edition of its source only where the product stands on that edition.
- A fact about what runs a method — how a tool behaves under the runner's configuration, which
  interpreter runs a script — is no fact an invariant rests on; the method's command is written so
  that it does not matter, as `git -c core.ignorecase=false check-attr` (WAY-73, WAY-61).
- A fact may be about something outside that depends on the product — a product that pins it and
  reads one of its surfaces. It is written when a decision about that surface would need review
  were it no longer true, and that decision names it in *Based on*; until then the part map's
  partners stand as the map holds them.
- A finding of a study states what the study measured, on which models, in which version of the
  paper. That the agents of this process behave the same is a prediction: it stands in *Review when*
  of each decision citing the fact, as a state a script can check (WAY-24).

## Holds for

- *Holds for* names what the sentence is true of: a tool and its version, a platform, an edition, or
  the models a study measured — by their dated identifiers where the study gives them, and by the
  names it gives otherwise, which a script checking a decision's *Review when* resolves. It never reads "latest", since what that
  names changes with the date. Where the source publishes no editions, *Holds for* names what the
  sentence is about and says the source gives no version — `JSON Lines, which jsonlines.org
  publishes without versions` — and the date read stays in *Source*, so that a re-read flags
  nothing; a changed page fails the watch, since the passage no longer stands.
- The sentence and *Holds for* bind together: the entry's content fingerprint covers the sentence,
  a line break and the value of *Holds for* (WAY-39). The source, its passage and its date stay
  outside it, so a re-read source that says the same flags nothing.
- A claim that differs in a new scope changes the sentence or *Holds for*, and so the version; a
  claim true in a past scope is not refuted by it.
- A newer release of a tool *Holds for* names fails nothing: the fact about the named release stays
  true. Moving the product to the newer release is a decision's to make, and the release is a
  condition in its *Review when* (WAY-24).
- A scope the product declares — the version of Python it runs, in a file a tool reads — is a
  sentence about the product, so an invariant holds it, never a fact. An invariant that depends on
  that version names it in its sentence and names the fact in *Rests on*: a change of the fact's
  scope reaches it through the fingerprint (WAY-66), and whoever writes it sees that the version it
  names lies within the fact's scope. No script compares the two, since *Holds for* is prose.

## Source

- Every entry has a source; a fact without one is not written, and finding it is a task.
- A source is the edition the publisher gives its own address, the place in it, the passage the fact
  rests on word for word, and the date it was read. A source that publishes no editions also names the
  archived copy closest to the reading, with its date. Several addresses stand in one entry only as pages of one edition.
- A fact resting on a whole section of rules — a pattern syntax, an algorithm — quotes the sentence
  of the source that sets those rules, and names the section by its place alone, where the edition
  has an address of its own: its text does not change, and the watch reads its state. Where the
  source publishes worked examples of those rules, they are the probe's test data, not its source.
- An observation is a source when it names the command, the tool and its version, the platform and
  the date it ran: `observed: <command> on <tool and version, platform>; run <YYYY-MM-DD>`.
- A model's memory, an agent's paraphrase, and a text quoting the source are no source.
- The passage is what a re-reading compares against: the method checks that it still stands at the
  address; no digest of the source is kept.

## Set by

*Set by* reads `none` for what nobody in the product sets. A setting that people of the product
change outside the repository — who can open it, a host's access rule — names who sets it, as
"the repository owner", and its method reads the current state where it lives; where reading it
takes the credentials of whoever sets it, the method is a re-read by that person, whose verdict
names the date until which it is in force. The choice of such a
setting becomes a decision only where the product declares it, and that decision then rests on the
fact.

## Method

- A method is a command that begins with the name of the program it runs, or the path alone of a
  file a human re-reads the source against, or `TODO`; no kind of method is written beside it
  (as WAY-61). A fact whose method reads `TODO` is unchecked, and never counts as passed.
- A command whose program the product does not yet declare or produce is written out in full all
  the same, with the program named as it will run; the fact is then unchecked for want of a
  declared or produced command, a different reason (as WAY-63).
- A command may probe, watch, or both:
  - a probe asks the tool how it behaves here and now — on test data the source itself publishes
    where there is any (NIST's example digests, a JSON test suite), and about the behaviour, never
    about a version number;
  - a watch reads the state the source publishes as data — `obsoleted_by` of an RFC, a withdrawal,
    a model's deprecation state, a support schedule — and checks that the passage in *Source* still
    stands at its address.
  A human re-reads what no command can read: law, a licence, an access rule without an API.
- A command sets for itself whatever in the runner's configuration could change its verdict
  (`-c core.ignorecase=false`), so that it gives the same verdict on every machine.
- A command cites each fact it gives a verdict for, as a line `fact: <identifier>/<version>` in the
  comment form of its file's language; a command citing a version other than the current one fails
  the gate (as WAY-65, WAY-57).
- A command records a fact's verdict in the-way's own record of a run, on a line holding `fact` as
  `<identifier>/<version>` where a line for an invariant holds `invariant`; a line holds one of the
  two, or neither for a failure recorded for no entry. The key adds to WAY-74, which needs a new
  version; lines already written stay valid.

## When a method runs

- When an entry enters or its wording changes: its method passes on that commit, or reads `TODO`.
- By the clock: one command runs the method of every fact at once, on the main branch — never inside
  the gate of a change that does not touch the fact, since the world changes with no commit and the
  gate's verdict would then depend on the date (WAY-60, WAY-61). A human verdict on a re-read names
  the date until which it is in force, and after that date the fact is unchecked.
- A human verdict stands in `foundations/human_verdicts.md`, one file for invariants and facts, as a
  row naming the entry, its version, the verdict, who gave it, when, the commit assessed, and
  *Until* — a date for a fact; `none` for an invariant, whose verdict lapses when a change since
  that commit reaches it (WAY-63). The gate reads the row for the entry's current version; a row
  for an earlier version is in force for nothing.

      | Entry | Version | Verdict | By | On | Commit | Until |
- When a change alters a file the command names — the file that pins a tool, or declares the
  product's version of Python — the gate runs the method on that change, since there a change of the
  repository does change the fact.

## Result

- A fact's result is `pass`, `fail`, `unchecked` for its method reading `TODO`, for a command the
  product does not declare or produce, or for no human verdict in force, or `error` where there is no verdict for any other reason (as WAY-63).
- A `fail` opens a review of the fact; it does not block a change that does not touch the fact. The
  clock's command records each fact's verdict in the-way's own record of a run and exits non-zero
  when some fact results `fail` or `error`; whether a failure then becomes a task, a branch or a
  message is set by the task cycle, not by this element.
- An edition that is superseded, withdrawn, or updated by a published change fails the watch, and so
  opens a review; it does not make the sentence false. An announced revision fails nothing: until
  the new edition is out, the fact holds, and whoever wants to look ahead writes the condition in
  *Review when* of the decision citing the fact (WAY-24). Only the human deciding the review changes the sentence or *Holds for*,
  and the new fingerprint then reaches every entry naming the fact (WAY-66).

## Version and correction

- An entry carries a version, starting at 1. When its fingerprint differs from its fingerprint on the
  main branch, its version is one higher, unless *Correction* names both fingerprints and the human
  deciding the change confirms, with both wordings in front of them, that the meaning is unchanged
  (as WAY-57).
- A change after which some command citing the fact would need a different expected value is a
  raise, never a correction.
- The guard compares an entry with its state where the task branch left the main branch; where there
  is no main branch, it compares nothing, says so, and every entry stays at version 1 (as WAY-57).

## Withdrawn identifiers

A fact shown false does not leave the file: its identifier moves to the list that closes it, with
what showed it false in *Why*, so that nobody writes it again and an older decision citing it still
finds it. A fact split or merged gives its results new identifiers, and *Why* says so.

## Catalogues and obligations

- A voluntary catalogue of requirements — ASVS, WCAG where no law requires it — binds the product
  only through a decision adopting it, naming the catalogue, its edition, the level or list taken,
  and the area of the product. A requirement it holds is then a fact: its source is the edition, the
  requirement's identifier and its text word for word, and an invariant taking a condition from it
  names it in *Rests on* (WAY-58, WAY-73).
- A binding rule — a law, a contract, a licence — needs no adoption: whether it applies is a fact,
  read as applying until a human settles otherwise.
- A descriptive source — an RFC, a list of modules — needs nothing beyond the fact.
- A likeness an agent notices between the product and a requirement it has not adopted goes to a
  human as a question: "do we adopt this?" or "does this bind us?".
- An obligation that raises the criticality of a part enters the part map as a failure mode of that
  part, whose detection names an invariant resting on the fact of the obligation (WAY-46).

## Fields and their readers

A field stays in this template only while someone or something reads it (WAY-05).

| Field | Who reads it, when | Where its value comes from |
|---|---|---|
| identifier (heading) | an invariant's *Rests on*, a decision's *Based on*, a `fact:` line; the format guard | judgment |
| version (heading) | a command citing the fact; the guard, which computes what the version must be | read off |
| sentence | whoever reviews what rests on the fact; the content fingerprint | prose |
| Holds for | the content fingerprint; whoever writes an invariant naming a version within it; a script checking a decision's *Review when* against the models a study measured | read off the source |
| Source | the watch, which checks that the passage still stands; the human reviewing the fact | read off |
| Set by | the human reviewing a failed run, who learns whom to ask | judgment |
| Method | the clock's command; the gate, on a change to a file the command names; a human, for a path | judgment |
| Correction | the guard, which lets the version stand; the human who confirms it | judgment for the declaration; read off for both fingerprints |
| human verdicts | the gate, which counts a re-read fact as passed until *Until*; the clock, which reports it unchecked after | judgment for the verdict and *Until*; read off for the rest |
| withdrawn identifiers | whoever follows a citation to a fact shown false; the guard, which keeps it from coming back and checks its successors | judgment for *Why*; read off for the rest |

A field marked *judgment* holds someone's call: no tool reads its value off the product, and no
question about a fact settles it. A reader takes such a value as a call, not as a reading (WAY-54).
A field marked *prose* carries text rather than a value.

## What the format guard checks

- The product has exactly one file of fact entries: the file checked stands in
  `foundations/environment_facts.md` from the root of its repository, letter case included, as git
  lists it, and no other Markdown file git tracks holds an entry, save `examples.md` beside this
  template, which holds copies.
- The file holds its entries, then its withdrawn identifiers, each in the form above, and no other
  heading; the heading of an entry carries its version as a number.
- Every identifier has the form above and is held once among the entries and withdrawn identifiers of
  this file, of the invariants and of the part map taken together; every identifier held on the
  commit the task branch left the main branch from stands in the file still, and one withdrawn there
  is withdrawn still; every successor is an entry, a withdrawn identifier, or `none`.
- Every entry carries every field of the form, and `none` or `TODO` only where the form gives it:
  `none` in *Set by* and *Correction*, `TODO` in *Method* (WAY-71). No entry carries a field the
  form does not hold, nor text outside its sentence and fields.
- Every entry states its fact in one sentence, and no *Holds for* reads "latest" or "newest".
- Every source has one of the two forms above: an address, a place, a quoted passage and a date
  read — or, for a further page of the same edition, an address and a place — or an observation. The guard checks the form; whether the passage stands at the address is
  the watch's to check.
- Every entry carries a version; an entry with no fingerprint on the main branch carries version 1
  and no correction; an entry whose fingerprint differs from there carries a version one higher or a
  correction naming both fingerprints; an entry whose fingerprint equals it there keeps its version.
- The fingerprint of an entry covers its sentence and *Holds for* alone, and a change to anything
  else in the entry leaves it unchanged.
- Every method is a command that begins with a program's name, the path alone of a file that exists,
  or `TODO`.
- Every `fact:` line names an entry at its current version, never a withdrawn identifier.
- Every row of `foundations/human_verdicts.md` naming a fact names an entry whose method is a path,
  gives `pass` or `fail`, and carries a date in *Until*.
- Every entry is named by an invariant's *Rests on* or a decision's *Based on*; one that is not is a
  warning, and, checking a merge onto the main branch, an error.
- Every example in `examples.md` matches its entry in the file word for word (WAY-05).
- The guard reports what it could not check and why, never agreement (WAY-38).

## Examples

Examples live in `examples.md`: entries copied word for word from a real set of facts. Until the
first entries are written, only the forms above stand (WAY-05).

# Environment fact entry template

> **Draft.** Every rule below cites the decision that sets it, and every place that waits for a
> decision carries `TODO — decision pending: <question>`. The template reaches the main branch only
> together with the element's examples, skill and guard (WAY-06, WAY-09).

This file defines how an environment fact entry is written. An environment fact is something true
about the world around the product — a platform, a format, a licence, a law, the behaviour of a tool,
a finding of a study — with a method of checking it. It says nothing about the product itself: that
is an invariant (WAY-04, WAY-22, WAY-76). An invariant names the facts holding a condition of its
sentence in *Rests on* (WAY-73), and a decision names the facts it rests on in *Based on* (WAY-17,
WAY-90). Its current result comes from running its method, never from a status written by hand
(WAY-08, WAY-81).

## Where entries go

- A product's fact entries stand in one file, `foundations/environment_facts.md`, which ends with its
  list of withdrawn identifiers (WAY-75).
- Every entry carries an identifier of one or more words in lower case joined by hyphens, held by no
  other entry or withdrawn identifier of this file, of the invariants or of the part map; `none` is
  no identifier, since *Successors* uses that word (WAY-75, WAY-64).
- The identifier names what the fact is about, never its value or the edition it cites, so that a
  new edition or a new range leaves it true: `json-text`, not `json-rfc-8259` (WAY-75).
- An identifier the file held on the commit the task branch left the main branch from stays, as an
  entry or as a withdrawn identifier giving why and naming its successors or `none`. Splitting or
  merging entries gives each entry that comes out of it a new identifier, and any other change keeps
  it (WAY-75).
- An entry holds only its current wording; earlier wordings are read from git (WAY-79).
- An entry is written in English, whatever language the product shows the people who use it and
  whatever language its team speaks (WAY-72).

## Which facts are written

- A decision's *Based on* names a fact entry for every citation that, stopping being true today,
  would send the decision to review — a finding about agents or models, the behaviour of a tool the
  process uses — and quotes every other citation with its source, as a precedent or a past event
  (WAY-90).
- A finding of a study is such a citation. Its fact records what the study measured and stays true;
  what the decision draws from it is that the agents of this process behave the same, which stops
  holding as the measured models go. That is a prediction: it stands in *Review when* of each
  decision citing the fact, as a state a script can check, never in the fact (WAY-85, WAY-24).
- An invariant names in *Rests on* only the facts holding a condition that decides whether a commit
  makes its sentence true (WAY-73).
- A fact may be about something outside that depends on the product — a product that pins it and
  reads one of its surfaces — only where a decision about that surface would need review were it no
  longer true. The partners themselves stay in the part map's external context (WAY-90).
- A fact stands only while an invariant's *Rests on* or a decision's *Based on* names it (WAY-88).

## Entry

```markdown
## <identifier>/<version>

<one sentence: the fact>

- **Holds for:** <the tools, platforms, editions or measured models the sentence is true of, with versions>
- **Source:** <address of the edition> § <place> — "<passage, word for word>"; read <YYYY-MM-DD> · … | <address of the page> (archived: <address of the archived copy>, <YYYY-MM-DD>) § <place> — "<passage, word for word>"; read <YYYY-MM-DD> | observed: `<command>` on <tool and version, platform>; run <YYYY-MM-DD>
- **Set by:** none | <who in the product sets it, outside the repository>
- **Method:** `<program> <arguments>` | <path of a file a human re-reads the source against> | `TODO`
- **Correction:** none | <fingerprint on the main branch> → <current fingerprint>
```

Every field of the form above appears in every entry. A field holds `none` or `TODO` only where the
form above gives it that word: `none` states that nothing is there, `TODO` that something is known
to be missing (WAY-71). *Source* takes neither (WAY-80).

After the last entry the file carries its withdrawn identifiers; *Successors* lists identifiers
joined by ` · `, or reads `none` (WAY-75):

```markdown
## Withdrawn identifiers

| Identifier | Why | Successors |
```

## The sentence

- One entry states one fact, in one sentence: what one edition of one source says, with one reason
  to change. Pages of one document published together in one edition count as one source. That is
  the most an entry holds, not a reason to join: two facts from one edition whose sentences are
  about different things stand as two entries (WAY-76).
- The sentence states what is true of the world today, in the present tense, and says nothing a
  commit of the product can make true or false: such a sentence is an invariant (WAY-22, WAY-76).
- The sentence says no more than its source says: where the source recommends, the sentence does
  not require (WAY-80).
- The sentence names an edition of its source only where the product stands on that edition
  (WAY-78).
- A fact about what runs a method — how a tool behaves under the runner's configuration, which
  interpreter runs a script — is no fact an invariant rests on; the method's command is written so
  that it does not matter, as `git -c core.ignorecase=false check-attr` (WAY-73, WAY-81).
- A finding of a study states what the study measured, on which models; the version of the paper
  stands in *Source*, and *Holds for* names it beside the models (WAY-85).
- A sentence that speaks of what a glossary term defines uses the term, never a paraphrase of its
  definition (WAY-100).

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
- A claim that differs in a new range changes the sentence or *Holds for*, and so the version; the
  new claim does not refute the claim true in the past range (WAY-77, WAY-79).
- A newer release of a tool *Holds for* names coming out fails nothing: the fact about the named
  release stays true, and a probe run on the newer release fails only where the behaviour differs
  (WAY-91). Moving the product to another release is a decision's to make, and what calls for it is a
  condition in that decision's *Review when* — for Python, the named release leaving bugfix support
  (WAY-77, WAY-89).
- A range the product declares — the version of Python it runs, in a file a tool reads — is a
  sentence about the product, so an invariant states it, never a fact (WAY-77).

## Source

- Every entry has a source; a fact without one is not written, and finding it is a task (WAY-80).
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
  decision's *Based on*, the date of the version citing it (WAY-80, WAY-77).
- A fact resting on a whole section of rules — a pattern syntax, an algorithm — quotes the sentence
  of the source that sets those rules, and names the section by its place alone, where the edition
  has an address of its own. Where the source publishes worked examples of those rules, they are the
  probe's test data, not its source (WAY-80).
- A model's memory, an agent's paraphrase, and a text quoting the source are no source (WAY-80).
- The passage is what a re-reading compares against: the watch checks that it still stands at the
  address, and no digest of the source is kept, so a change to the text next to the passage passes
  unseen (WAY-78, WAY-81).

## Set by

*Set by* reads `none` for what nobody in the product sets. A setting that people of the product
change outside the repository — who can open it, a host's access rule — names who sets it, as
"the repository owner", and its method reads the current state where it lives; where reading it
takes the credentials of whoever sets it, the method is a re-read by that person, whose verdict
names the date until which it is in force (WAY-84, WAY-83). The choice of such a setting becomes a
decision only where the product declares it, and that decision then rests on the fact. A setting
set outside the product — the visibility of a repository it links to — reads `none` and is probed
anonymously (WAY-84).

- The source of a setting only its setter can read is
  `TODO — decision pending: which form of Source a setting read only with its setter's credentials takes, since WAY-80 gives none`.
- A fact about the visibility of a repository the product links to names that one repository,
  since each has its own owner and changes on its own (WAY-76); where an invariant rests on the
  visibility of the repositories linked, each new link adds such a fact, named in its *Rests on*
  (WAY-84, WAY-73).

## Method

- A method is a command that begins with the name of the program it runs, or the path alone of a
  file a human re-reads the source against, or `TODO`; no kind of method is written beside it. A
  fact whose method reads `TODO` is unchecked, and never counts as passed (WAY-81, WAY-63).
- A command whose program the product does not yet declare or produce is written out in full all
  the same, with the program named as it will run; the fact is then unchecked for want of a
  declared or produced command, a different reason (WAY-81).
- A command may probe, watch, or both (WAY-81):
  - a probe asks the tool how it behaves here and now — on test data the source itself publishes
    where there is any, as NIST's example digests — and about the behaviour, never about a version number in its place;
  - a watch reads the state the source publishes as data — `obsoleted_by` of an RFC, a withdrawal,
    a model's deprecation state, a support schedule — and whether the passage still stands.
  A human re-reads what no command can read: law, a licence, an access rule readable only with the
  credentials of whoever sets it (WAY-81, WAY-84).
- A command sets for itself whatever in the runner's configuration a command can set and could
  change its verdict (`-c core.ignorecase=false`), so that it gives the same verdict on every
  machine. Where it cannot — a model that runs the method — that configuration is read off the
  product, and the deliberate break shows the method's fidelity, which holds only where the break
  gives high confidence of detection (WAY-81). The release of a tool a probe runs is read off the
  machine instead, as the next point says (WAY-91). Whether a fact's command, like an invariant's test,
  counts only when a deliberate break makes it fail is
  `TODO — decision pending: whether WAY-08's deliberate break binds a fact's method`.
- Where *Holds for* names a release of the tool a probe runs, the probe reads the release it runs
  on and records it in the `description` of its line: a `fail` on any release is a `fail`, and a
  `pass` counts only on a release *Holds for* names, a build of it included, as Git for Windows
  builds git. The method rests on no fact about that release (WAY-91, WAY-73).
- A check cites each fact it gives a verdict for, at the check, as a line
  `fact: <identifier>/<version>` in the comment form of its file's language, and a run records no
  verdict for a fact no check cites (WAY-81); a check citing a version other than the current one
  fails the gate (WAY-79). A check stands in a file of code; a Markdown file holds no citing check.
- Where the checks of a product's facts stand in the part map is set when its first fact is written
  (WAY-81). Whether a file holding such a check is read-only during implementation, as an invariant
  test is (WAY-03), is not settled.
- A command records a fact's verdict in the-way's own record of a run, at the one `.jsonl` path it
  names, which git ignores, on a line holding `fact` as `<identifier>/<version>` where a line for an
  invariant holds `invariant`; a failure recorded for no entry holds `invariant` as `null` (WAY-74).

## When a method runs

- When a change enters an entry or changes any of its fields, or alters a file its command names, the gate runs its method on that change (WAY-82).
- By the clock: one command runs the method of every fact at once, on the main branch — never inside
  the gate of a change that neither enters nor changes the entry nor alters a file its command
  names, since the world changes with no commit and the gate's verdict would then depend on the date
  (WAY-82, WAY-60). The clock's command does not exist yet, and with no scheduler it runs by hand
  (WAY-82).
- A human verdict stands in `foundations/human_verdicts.md`, one file for invariants and facts, as a
  row naming the entry, its version, the verdict — `pass` or `fail` — who gave it, when, the commit
  assessed, and *Until* — a date for a fact. It counts only for the entry's current version, and a
  fact's verdict lapses after *Until*, which the gate compares with the committer date of the commit
  it checks and the clock with the day it runs. The part of the map that holds the file is set with
  the first verdict written (WAY-83):

  ```markdown
  | Entry | Version | Verdict | By | On | Commit | Until |
  ```

## Result

- A fact's result is `pass`, `fail`, `unchecked` for a reason on the list below, or `error` where
  there is no verdict for any other reason (WAY-81, WAY-63).
- Reasons for `unchecked` — a closed list (WAY-81, WAY-83, WAY-63, WAY-91):
  - the method reads `TODO`;
  - the method's command is not declared or produced by the product;
    - the method is a path, and no human verdict is in force;
  - a probe ran on a release of its tool outside *Holds for*.
- In the gate of a change that runs a fact's method, its `fail` or `error` makes the gate's command
  fail (WAY-63). Elsewhere a `fail` stops no change. The clock's command records each fact's verdict
  in the-way's own record of a run and exits non-zero when some fact results `fail` or `error`; what
  a failure then becomes — a task, a branch, a message — is set when the task cycle is designed
  (WAY-82).
- A watch fails on a published change to its edition — superseded, withdrawn, or updated by a
  published change — or when its passage no longer stands; that leads to a review of the fact and
  does not make the sentence false. An announced revision fails nothing: until the new edition is
  out, the fact holds, and whoever wants to look ahead writes the condition in *Review when* of the
  decision citing the fact (WAY-82, WAY-24). Only the human deciding the change that follows the
  review changes the sentence or *Holds for*, and the new fingerprint then reaches every invariant
  and decision naming the fact (WAY-66, WAY-90).

## Version and correction

- An entry carries a version, starting at 1. When its fingerprint differs from its fingerprint on the
  main branch, its version is one higher, unless *Correction* names both fingerprints and the human
  deciding the change confirms, with the old and the new binding part in front of them, that the
  meaning is unchanged (WAY-79).
- A change after which some check citing the fact would need a different expected value is a raise,
  never a correction (WAY-79).
- The guard compares an entry with its state where the task branch left the main branch; where there
  is no main branch, it compares nothing, says so, and every entry stays at version 1 (WAY-79).
- Until the confirmation has a home, the guard reports a declared correction as "correction
  declared, confirmation not checked", never as agreeing (WAY-79).

## Withdrawn identifiers

A fact shown false does not leave the file: its identifier moves to the list that closes it, with
what showed it false in *Why*, so that nobody writes it again and an older decision citing it still
finds it; where entries are split or merged, *Why* says so. A true fact whose last dependant goes is
withdrawn in the same change, with that in *Why*, or the merge fails (WAY-75, WAY-88).

## Catalogues and obligations

- A voluntary catalogue of requirements — ASVS, WCAG where no law requires it — binds the product
  only through a decision adopting it, naming the catalogue, its edition, the level or list taken,
  and the area of the product. A requirement it holds is then a fact: its source is the edition, the
  requirement's identifier and its text word for word, and an invariant taking a condition from it
  names it in *Rests on* (WAY-86, WAY-73).
- A binding rule — a law, a contract, a licence — needs no adoption: whether it applies is a fact,
  read as applying until a human settles otherwise (WAY-86). Whether a commit that removes what the
  rule covers makes that fact false is
  `TODO — decision pending: whether "the rule applies" is a fact, against WAY-76`.
- A descriptive source — an RFC, a list of modules — needs nothing beyond the fact (WAY-86).
- A likeness an agent notices between the product and a requirement nothing has adopted or applied
  goes to a human as a question: "do we adopt this?" or "does this bind us?" (WAY-86).
- An obligation that raises the criticality of a part enters the part map as a failure mode of that
  part, whose detection names an invariant resting on the fact of the obligation (WAY-87).

## Fields and their readers

A field stays in this template only while someone or something reads it (WAY-05).

| Field | Who reads it, when | Where its value comes from |
|---|---|---|
| identifier (heading) | an invariant's *Rests on*, a decision's *Based on*, a `fact:` line; the format guard | judgment |
| version (heading) | a check citing the fact; the guard, which computes what the version must be | read off |
| sentence | whoever reviews what rests on the fact; the fingerprint | prose |
| Holds for | the fingerprint; whoever writes an invariant naming a version within it; a script checking a decision's *Review when* against the models a study measured | transcribed from the source |
| Source | the watch, which checks that the passage still stands; the human reviewing the fact | transcribed |
| Set by | the human deciding the change that follows a failed run, who learns whom to ask | judgment |
| Method | the clock's command; the gate, on a change that enters or changes the fact or alters a file its command names; a human, for a path | judgment |
| Correction | the guard, which lets the version stand; the human who confirms it | judgment for the declaration; read off for both fingerprints |
| human verdicts | the gate, which takes a re-read fact's result from the row in force until *Until*; the clock, which reports it unchecked after; the format guard, which checks the row | judgment for the verdict and *Until*; read off for the rest |
| withdrawn identifiers | whoever follows a citation to a fact shown false; the guard, which keeps it from coming back and checks its successors | judgment for *Why*; read off for the rest |

A field marked *judgment* holds someone's call: no tool reads its value off the product, and no
question about a fact settles it. A reader takes such a value as a call, not as a reading (WAY-54).
A field marked *prose* carries text rather than a value.

## What the format guard checks

- The product has exactly one file of fact entries: the file checked stands in
  `foundations/environment_facts.md` from the root of its repository, letter case included, as git
  lists it, and no other Markdown file git tracks holds an entry — a section
  `## <identifier>/<version>` carrying a *Holds for* field, outside a fenced block — save
  `examples.md` beside this template, which holds copies (WAY-75).
- The file holds its entries, then its withdrawn identifiers, each in the form above, and no other
  heading; the heading of an entry carries its version as a number (WAY-75, WAY-79).
- Every identifier has the form above and is held once among the entries and withdrawn identifiers of
  this file, of the invariants and of the part map taken together; every identifier held on the
  commit the task branch left the main branch from stands in the file still, and one withdrawn there
  is withdrawn still; every withdrawn identifier gives why, and every successor is an entry, a
  withdrawn identifier, or `none` (WAY-75).
- Every entry carries every field of the form, and `none` or `TODO` only where the form gives it:
  `none` in *Set by* and *Correction*, `TODO` in *Method* (WAY-71). No entry carries a field the
  form does not hold, nor text outside its sentence and fields.
- Every entry states its fact in one sentence, and no *Holds for* reads "latest" or "newest" (WAY-76,
  WAY-77).
- Every source has one of the forms above; the guard checks the form alone (WAY-80).
- Every entry carries a version; an entry with no fingerprint on the main branch carries version 1
  and no correction; an entry whose fingerprint differs from there carries a version one higher or a
  correction naming both fingerprints; an entry whose fingerprint equals it there keeps its version
  and declares no correction whose second fingerprint differs from it (WAY-79).
- The fingerprint of an entry covers its sentence and *Holds for* alone, and a change to anything
  else in the entry leaves it unchanged (WAY-78).
- Every method is a command that begins with a program's name, the path alone of a file that exists,
  or `TODO` (WAY-81).
- Every path ending in `.jsonl` that a command names is one git ignores, as git itself answers, and
  no command names two (WAY-74).
- Every `fact:` line in a check names an entry at its current version, never a withdrawn identifier
  (WAY-79, WAY-81).
- Every row of `foundations/human_verdicts.md` names an entry of the invariants or of the environment
  facts; a row naming a fact names an entry whose method is a path, gives `pass` or `fail`, names who
  gave it, when and the commit assessed, and carries a date in *Until* (WAY-83).
- Every fact the *Based on* of the latest version of a decision names carries a fingerprint, and,
  checking a merge onto the main branch, the current one (WAY-90).
- Every entry is named by an invariant's *Rests on* or by the *Based on* of the latest version of a
  decision; one that is not is a warning, and, checking a merge onto the main branch, an error
  (WAY-88).
- Every example in `examples.md` matches its entry in the file word for word (WAY-05).
- The guard reports what it could not check and why, never agreement (WAY-38).
- Given the path of a record, the guard writes the-way's own record of the run there, with a verdict
  for each invariant its checks cite (WAY-61, WAY-74); given `none` as either commit, it records the
  checks that need that commit as `unchecked`; a call to git that fails, the file standing outside a
  git repository included, is a failure of the run, never an unchecked check (WAY-61, WAY-63).

## Examples

Examples live in `examples.md`: entries copied word for word from a real set of facts. Until the
first entries are written, only the forms above stand (WAY-05).

# Invariant entry template

> **Draft.** This template is written ahead of the decisions it still waits for, so that they can
> be settled against real entries instead of imagined ones. A rule that cites no decision is a
> proposal settled during the element's research, waiting for its decision. Until those decisions
> are written, nothing here binds beyond what the cited decisions already say, and the template
> does not reach the main branch
> (`TODO — decision pending: which decision keeps a draft template off the main branch until its
> decisions are written`).

This file defines how an invariant entry is written. An invariant names its method of checking and
says nothing about why, or about what was rejected (WAY-08, WAY-22). Its current result comes from
running that method, never from a status written by hand (WAY-08).

The rules of form the elements share — the language of an entry, every field and the words `none`
and `TODO`, the terms of the glossary, the marks of where a value comes from, the form of an
identifier, when it stays and when a split or a merge replaces it, its one space with the part map
and the environment facts, the list of withdrawn identifiers, human verdicts, `{fork-point}` and
the version of an entry — stand in `elements/common/rules.md`; this template holds what is
particular to an invariant (WAY-35).

## Where entries go

- A product's invariant entries stand in one file, `foundations/invariants.md` (WAY-64). After its
  last entry the file holds its withdrawn identifiers (WAY-64), its quarantined invariants (WAY-68)
  and its recovered invariants (WAY-58), in that order, the last list closing the file
  (`TODO — decision pending: which decision sets the order of the lists closing the invariants
  file`).
- One derived file lies beside it: the list of violated invariants (WAY-51).
- The identifier names what the sentence constrains, never what it demands, so that a raised
  version leaves it true; where another entry constrains the same thing, it adds the aspect this
  one protects, as `entry-version-number` and `entry-version-correction`
  (`TODO — decision pending: which decision sets how an invariant's identifier is named`).
- Where a change keeps an entry's identifier, as `elements/common/rules.md` gives it (WAY-64), a
  change of meaning moves the version (WAY-57). An entry that takes in a clause of another keeps
  its identifier, and the other is split
  (`TODO — decision pending: which decision sets that an entry taking in a clause of another keeps
  its identifier`).

## Entry

```markdown
## <identifier>/<version>

<one sentence: the invariant>

- **Method:** `<program> <arguments>` | <path of a file a human assesses the product against> | `TODO`
- **Rests on:** <environment fact>@<fingerprint> · … | TODO — <the fact, with its source> | none
- **Derives from:** <decision>@<fingerprint> · … | `TODO — <the decision, and where it is expected>` | none
- **Part:** <parts from the part map> | every
- **Correction:** none | <fingerprint on the commit the task branch left the main branch from> → <current fingerprint>
```

The form above gives each field the words it takes. The rest of the rule on `none` and `TODO` —
every field in every entry, and the fields the main branch holds `TODO` in — stands in
`elements/common/rules.md` (WAY-71).

After the last entry the file carries its withdrawn identifiers, in the form, with the *Why* and
the *Successors*, that `elements/common/rules.md` gives (WAY-64).

A quarantined invariant stands on the list of quarantined invariants, after the withdrawn
identifiers; *Until* is a date as `YYYY-MM-DD` (WAY-68), resting on a judgment of the human who
accepts the quarantine (WAY-54):

```markdown
## Quarantined invariants

| Identifier | Version | Until |
```

A recovered invariant stands on the list of recovered invariants, which closes the file, in a row
naming its identifier and its current version, with `searched: <…>` in *Searched* and
`found: <…>` in *Found* (WAY-58):

```markdown
## Recovered invariants

| Identifier | Version | Searched | Found |
```

## Method

- A method is either a command the gate runs, which counts as a command the product declares
  (WAY-38), begins with the name of the program it runs and is never a path alone, or the path
  alone of a file a human assesses the product against (WAY-61). The form is the route; no kind of
  method is written beside it
  (`TODO — decision pending: which decision keeps a method's kind from being written beside it`).
- A command is the same on every run and names no commit, branch or revision itself. A commit the
  sentence names is a value the gate fills in, from this closed list, which grows by a new version
  of WAY-61: `{fork-point}`, as `elements/common/rules.md` gives it; `{merge-onto}` — the commit of
  the main branch that a merge into it is made onto. Where the commit does not exist, the gate
  fills in `none` in its place (WAY-61).
- A method checks what its sentence is about, as it stands on the commit being checked: a check fed
  input made up for it is the method of a sentence about that check, not about the data it reads
  (WAY-61).
- k and n, for a method that does not give the same verdict every time, stand in the command
  (WAY-08).
- A method a product cannot yet name as any command reads `TODO`, and the entry is reported
  unchecked for that reason (WAY-63). A command whose program the product does not yet declare or
  produce is written out in full all the same, with the program named as it will run; that entry is
  reported unchecked for want of a declared or produced command, a different reason (WAY-63,
  WAY-38, WAY-47, WAY-51).
- A command whose program is a Python interpreter may name a script not yet written, since no
  format guard judges whether a command's script exists; its script is read as a POSIX shell splits
  the command. A method whose program is declared or produced by the product but is no Python
  interpreter, and whose script does not exist yet, reads `TODO` instead (WAY-105).
- One run may check many invariants. An entry's result is the verdict the run records for its
  identifier and current version, in a format from this closed list, which grows by a new version of
  WAY-61: the-way's own record of a run, whose form and path answer to the invariants
  `run-record-form`, `run-record-path` and `run-record-lines` (WAY-74). A run that records no
  verdict for the entry never gives it a pass (WAY-61).
- The path of the-way's own record is one git ignores, and the gate clears it before the run
  (WAY-74) and runs no command naming a path git does not ignore
  (`TODO — decision pending: which decision keeps the gate from running a command that names a
  path git does not ignore`). A failure no rule of a check gave names the program that ran as its
  `check` (`TODO — decision pending: which decision sets what a failure no rule gave names as its
  check`).
- A population the product meets only in use — the loads real players make, for one — has no form
  yet: the method of a sentence about it reads
  `TODO — decision pending: the method of a population met only in use`, and the gate reports the
  entry unchecked (WAY-61).

## The sentence

- One entry states one invariant, in one sentence. The method and the links stand beside it, not
  inside it (WAY-56). The format guard counts sentences only, so two rules joined in one sentence
  pass it; what one sentence may join is judged against the complying and violating pair in
  WAY-56's *Verification* (WAY-56, WAY-12).
- The sentence is the binding part: the entry's fingerprint covers the sentence alone (WAY-56,
  WAY-02). The method, the links, the version and a declaration of a correction stay outside it
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
  merge request changes names the commit it is measured against by its value on the gate's list
  above, `{fork-point}`, while a state it compares may be the one on `{merge-onto}` (WAY-60,
  WAY-61). A sentence that is to hold on the main branch alone holds where `{merge-onto}` exists
  (WAY-60).
- A sentence may be about a check the product itself holds, as it may be about anything else the
  product holds: whether a check belongs to the product is settled by the part map
  (`TODO — decision pending: which decision lets the part map settle whether a check belongs to
  the product`), and the method of such a sentence is a test fed input made up for it (WAY-61).
  Such a sentence names a value of the gate's list in quotation marks, as what the check is given,
  and its command need not take it (WAY-60, WAY-61). Quoted text, in this template, is text
  between quotation marks; a value in backticks is not quoted.
- A sentence that bounds or equates a quantity measured while the product runs names its bound or
  tolerance, the statistic and the population it is computed over (WAY-60). A bound written with a
  tilde — `~2 seconds` — names no bound, so the sentence states one as a number or has none
  (WAY-60).
- A sentence about what a check reports may also mean that the data it reads meets a rule; where
  it does, the data takes a sentence of its own, and the two stand as two entries, one about the
  check and one about the data (WAY-56, WAY-61).

## Links

- *Derives from* names every decision entry this invariant is derived from, and *Rests on* every
  environment fact it rests on; neither link is optional, and a link the author knows is missing
  reads `TODO` rather than `none` (WAY-17).
- *Rests on* names every environment fact holding a condition that decides whether a commit makes
  the sentence true, and no other: read otherwise, such a fact would change whether some commit
  makes the sentence true, or change a value the sentence copies from it. A fact that is
  only a reason for a decision the entry derives from stays in that decision's *Based on* (WAY-73).
- An invariant that depends on a version the product declares names that version in its sentence
  and names the fact in *Rests on*: a change of the fact's range reaches it through the fingerprint
  (WAY-73, WAY-31), and whoever writes it sees that the version it names lies within the fact's
  *Holds for*. No script compares the two, since *Holds for* is prose
  (`TODO — decision pending: which decision sets that no script compares a declared version with
  *Holds for*`).
- Both carry the fingerprint of each entry they name, and *Part* carries none. A change to
  that fingerprint reaches the main branch with every invariant carrying it, each checked against
  the new binding part and carrying the new fingerprint (WAY-31).

## Part

- *Part* names the parts of the part map in which a change can make the sentence false, or `every`
  where a change to any part can; never both. A part missing from the list stops the invariant from
  running where it can break, and nothing shows it, so a writer in doubt names more (WAY-62).
- *Part* has no third value. A sentence no commit of this product can make false is not an
  invariant of this product: it belongs to the foundation of the product whose commits
  decide it (`TODO — decision pending: which decision sets that a sentence no commit of the product
  can make false belongs to another product's foundation`).
- A change, against the commit its branch left the main branch from, reaches an entry that names
  `every` or a part the change touches, or whose method names a file the change alters (WAY-62).
- The entry names no failure mode, critical flow or surface (WAY-62).
- In the file holding invariant entries, a change of an entry touches the parts that entry names,
  and `every` touches all (WAY-44, WAY-62).

## Version and correction

- The version of an entry follows `elements/common/rules.md`, with one exception: an entry whose
  fingerprint differs from its fingerprint on the commit the task branch left the main branch from
  keeps its version where *Correction* names both fingerprints and the human who accepts the change
  at the merge confirms, with the old and the new binding part in front of them, that the meaning is unchanged
  (WAY-57).
- A change after which some test citing the entry would need a different expected value is a
  raise, never a correction (WAY-57).
- Whether the human confirmed a declared correction answers to the invariant
  `invariant-correction-confirmation`.

## Test

- A check cites each invariant it gives a verdict for, at the check, as a line
  `invariant: <identifier>/<version>` in the comment form of its file's language; a run records no
  verdict for an invariant its check does not cite (WAY-65). The version a check cites follows
  `elements/common/rules.md` (WAY-57). Several checks citing one invariant in one run pass only
  when each of them does (WAY-65).
- Each file such a check reads and names there stands on a line `data: <path>` — a recorded output
  it compares against, for one (WAY-65).
- A check stands in a file of code; a Markdown file holds no citing check
  (`TODO — decision pending: which decision sets that a citing check stands in a file of code`).
- An invariant test is read-only during implementation (WAY-03), and a file is one for the task
  when it is one on the commit the task branch left the main branch from or on the commit being
  checked. A path a human assesses against is no invariant test
  (`TODO — decision pending: which decision sets that a path a human assesses against is no
  invariant test`).
- A test counts only when a deliberate break of the invariant makes it fail (WAY-08).
- A test takes the input it asserts on and the value it expects written out, wherever the code its
  invariant is about would otherwise compute either; only the side it compares against comes from
  the run (WAY-69). Which files a test names, so that a fixture or a builder of its input cannot be
  changed underneath it, is not settled.
- An invariant's sentence, the check that cites it and the code it covers come from three different
  agents, and the deliberate break the check is accepted on is written from the sentence by the
  reviewer of that code, who did not write the check (WAY-69). This binds the act of writing a
  check, not the history of the file it joins.

## Recovered

An entry a human chose from what the product already did before the task writing it began, and that
names no decision entry of the product's own log it derives from, stands on the list of recovered
invariants; no other entry stands there (WAY-58). A decision named anywhere but that log — a
numbered decision in a concept document, a decision of the-way at the commit the product pins — is
no such decision, and the entry still stands on the list (WAY-58). The source of an invariant taken
from a product's own requirements, which the product does not meet yet, is not recorded by WAY-58
(`TODO — decision pending: where the source of an invariant taken from a product's own
requirements, which the product does not meet yet, is recorded`).

*Found* names the place of each source the search found that gives a reason for keeping the
behaviour or calls for a different one, or reads `found: nothing`. A place that only cites another is
followed to the place it cites, and is marked where that source is superseded. *Found* never states
a reason itself, nor one an agent infers (WAY-58). The row rests on a judgment: the human deciding
the change sets it with the gate's report in front of them, which answers to the invariant
`gate-fork-point-evidence` (WAY-58). An entry whose binding part changes — by a raised version, by
a correction, or by a split or a merge — enters again, and its row is set again (WAY-57, WAY-58,
WAY-64).

## Result, report and debt

- An entry's result on the commit being checked is `pass`, `fail`, `unchecked` for a reason on the
  list below, or `error` where there is no verdict for any other reason, or where a quarantine has
  lapsed (WAY-63, WAY-68).
- Reasons for `unchecked` — one closed list for invariants and environment facts, which grows by a
  new version of WAY-63 (WAY-63, WAY-74):
  - the method reads `TODO`;
  - the method is a path, and no human verdict is in force;
  - the method's command or file is not declared or produced by the product, except a command
    declared on the commit the branch left the main branch from, whose drop makes the result `error`
    (WAY-38, WAY-47, WAY-51, WAY-105);
  - the method takes a commit the gate filled in as not existing;
  - the product does not pin the-way, or the commit of the-way it pins does not hold what the
    method compares with (WAY-34);
  - the entry stands on the list of quarantined invariants at its current version, and the
    committer date of the commit being checked is no later than its *Until* (WAY-68);
  - for an environment fact, a probe ran on a release of its tool outside *Holds for* (WAY-81).
- Which entries the gate reports a result for, when its command exits non-zero, and how it reads a
  record of a run and a human verdict answer to the invariants of the part `gate`:
  `gate-reported-set`, `gate-exit-code`, `gate-result-values`, `gate-unchecked-reason`,
  `gate-verdict-per-entry`, `gate-pass-without-verdict`, `gate-quarantine-result` and
  `gate-human-verdict`. A human verdict on an entry whose method is a path stands where
  `elements/common/rules.md` places it (WAY-83).
- A declared command that cannot start, or a record holding a value off a closed list, is `error`;
  a record holding a line off the form above gives `error` to every entry whose method wrote it
  (`TODO — decision pending: which decision sets which failures of a run give an error, and to
  which entries`).
- Runs on a deliberate break, and the run WAY-58 asks for, give evidence, not results
  (`TODO — decision pending: which decision sets that runs on a deliberate break give evidence, not
  results`).

## Quarantine

- A check that records both `pass` and `fail` for one commit is answered by a foundation change;
  a quarantine is the last answer, and never covers an invariant a critical flow names (WAY-68).
- Where a test records both `pass` and `fail` for one commit, the recorded `fail` stays the entry's
  result on that commit until a foundation change answers the flipping, whatever a later run
  records (WAY-68).
- A quarantine row names the entry's identifier, its current version and an end date, and
  stands on the list of quarantined invariants (WAY-68).

## Violated invariants

The derived file beside the invariants, `foundations/violated_invariants.md`, holds every invariant
the product does not meet today, by identifier and current version. A listed `fail` leaves the
gate's command at zero, and a listed `pass` makes it fail until the same change drops the row.
A row is added only by a change of the foundation that a human accepts, never by a step of
implementation. The file is checked as a subset of the list on the commit the branch left the main
branch from, never regenerated from scratch (WAY-53, WAY-51).

```markdown
## Violated invariants

| Identifier | Version |
```

## Fields and their readers

A field stays in this template only while someone or something reads it
(`TODO — decision pending: which decision keeps a field in an element's template only while it is
read`). Each field carries the mark of where its value comes from (`elements/common/rules.md`); a
reader not built yet is named by the invariant it answers to
(`TODO — decision pending: which decision names a reader not built yet by its invariant`).

| Field | Who reads it, when | Where its value comes from |
|---|---|---|
| identifier (heading) | a check citing the invariant; the format guard (`invariant-identifier-form`, `identifier-holders`, `invariant-citation-target`); the part map's guard, in a flow and a failure mode's detection (`flow-invariant-link`, `map-invariant-names`) | judgment |
| version (heading) | a check citing the invariant, and the test runner, which records the verdict at the version cited (`invariant-citation-version`, `test-runner-pass-line`); the format guard, which computes what the version must be (`invariant-version-new`, `invariant-version-changed`, `invariant-version-unchanged`) | read off |
| sentence | the agent checking a change against the invariant; the fingerprint (`invariant-fingerprint-input`); the format guard (`invariant-sentence-count`, `sentence-branch-names`, `sentence-gate-values`) | judgment |
| Method | the gate, which runs a command or hands a path to a human, and reports a command run under a Python interpreter whose script does not exist (`gate-check-source`, `gate-verdict-per-entry`, `gate-missing-script`); the format guard (`invariant-method-form`, `method-gate-values`, `run-record-path`) | judgment |
| Rests on | whoever reviews the invariant when a fact changes; the format guard, which compares each fingerprint with the current one (`link-fingerprint-presence`, `link-fingerprint-value`) | judgment for the fact named; read off for its fingerprint |
| Derives from | whoever changes the decision; the format guard, which checks a decision's level 1 verification against it and each fingerprint against the current one (`level-one-decision-invariants`, `verification-invariant-derivation`, `link-fingerprint-presence`, `link-fingerprint-value`) | judgment for the decision named; read off for its fingerprint |
| Part | the gate, which runs the invariants a change reaches (`change-reach`); the format guard (`invariant-part-names`, `invariant-part-form`) | judgment |
| Correction | the format guard, which lets the version stand (`invariant-version-changed`); the human who confirms it (`invariant-correction-confirmation`) | judgment for the declaration; read off for both fingerprints |
| withdrawn identifiers | whoever follows an identifier that no longer names an entry; the format guard, which keeps a withdrawn identifier from coming back and checks its form, that it gives why it was withdrawn, and its successors (`invariant-identifier-persistence`, `invariant-withdrawal-persistence`, `withdrawal-successors`) | as `elements/common/rules.md` gives it |
| quarantined invariants | the gate, which reports the entry `unchecked` or `error` (`gate-quarantine-result`); the format guard (`quarantine-position-form`, `quarantine-flow-invariants`) | judgment for the date; read off for the version |
| recovered invariants | the human weighing a change to the invariant; the format guard (`invariant-recovered-form`, `invariant-recovered-derived`) | judgment for what was searched and found; read off for the version |
| violated invariants | the gate, which leaves a listed `fail` at zero and fails on a listed `pass` (`gate-exit-code`); the format guard, which compares the list with the commit the branch left the main branch from (`violated-list-growth`, `violated-position-version`) | judgment for the row; read off for the version |

## Examples

`examples.md` names, by identifier, the entries of this repository's own invariants
(`foundations/invariants.md`) that show the form of an entry; they are read there, in the commit of
the-way a product pins, instead of being copied (WAY-09, WAY-34). The format guard checks that each
identifier it names is the identifier of an entry of that file (`invariant-example-target`).

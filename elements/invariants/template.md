# Invariant entry template

> **Draft.** This template is written ahead of the decisions it still waits for, so that they can
> be settled against real entries instead of imagined ones. Every place that waits carries
> `TODO — decision pending: <question>`, naming the question as the queue of the invariants
> element holds it. A rule that cites no decision is a proposal settled during the element's
> research, waiting for its decision. Until those decisions are written, nothing here binds beyond
> what the cited decisions already say, and the template does not reach the main branch (WAY-06,
> WAY-09).

This file defines how an invariant entry is written. An invariant is a sentence about the product
that a commit makes true or false, with a method of checking it; it says nothing about why, or about
what was rejected (WAY-22). Its current result comes from running that method, never from a status
written by hand (WAY-08).

## Where entries go

- A product's invariant entries stand in one file, `foundations/invariants.md`, which ends with
  its list of withdrawn identifiers (WAY-64) and its list of quarantined invariants (WAY-68).
- One derived file lies beside it: the list of violated invariants (WAY-67).
- Every entry carries an identifier of one or more words in lower case joined by hyphens, held by
  no other entry or withdrawn identifier of this file or of the part map (WAY-64); `none` is no
  identifier, since *Successors* uses that word.
- The identifier names what the sentence constrains, never what it demands, so that a raised
  version leaves it true; where another entry constrains the same thing, it adds the aspect this
  one guards, as `entry-version-number` and `entry-version-correction` (WAY-64).
- An identifier the file held on the commit the task branch left the main branch from stays, as
  an entry or as a withdrawn identifier naming its successors or `none`; one that never reached
  the main branch may go (WAY-64).
- Splitting or merging entries held there gives every result a new identifier, and any other change
  keeps it (WAY-64); a change of meaning then moves the version (WAY-57). An entry that takes in a
  clause of another keeps its identifier, and the other is split (WAY-64).
- An entry holds only its current wording; earlier wordings are read from git (WAY-57).
- An entry is written in English, whatever language the product shows the people who use it and
  whatever language its team speaks (WAY-72).

## Entry

```markdown
## <identifier>/<version>

<one sentence: the invariant>

- **Method:** `<program> <arguments>` | <path of a file a human assesses the product against> | `TODO`
- **Rests on:** <environment fact>@<fingerprint> · … | TODO — <the fact, with its source> | none
- **Derives from:** <decision>@<fingerprint> · … | `TODO — <the decision, and where it is expected>` | none
- **Part:** <parts from the part map> | every
- **Correction:** none | <fingerprint on the main branch> → <current fingerprint>
- **Recovered:** none | recovered — searched: <…>; found: <…>
```

Every field of the form above appears in every entry. A field holds `none` or `TODO` only where the
form above gives it that word: `none` states that nothing is there, `TODO` that something is known
to be missing (WAY-71).

After the last entry the file carries its withdrawn identifiers, and then the list of quarantined
invariants that closes it (WAY-68); *Successors* lists identifiers joined by ` · `, or reads
`none`:

```markdown
## Withdrawn identifiers

| Identifier | Successors |
```

A quarantined invariant stands on the last list in the file; *Until* is a date as
`YYYY-MM-DD`, resting on a judgment of the human who accepts the quarantine (WAY-68):

```markdown
## Quarantined invariants

| Identifier | Version | Until |
```

## Method

- A method is either a command the gate runs, which counts as a command the product declares
  (WAY-38), begins with the name of the program it runs and is never a path alone, or the path
  alone of a file a human assesses the product against. The form is the route; no kind of method is
  written beside it (WAY-61).
- A command is the same on every run and names no commit, branch or revision itself. A commit the
  sentence names is a value the gate fills in, from this closed list, which grows by a new version
  of WAY-61: `{fork-point}` — the commit the task branch left the main branch from, which is the
  last commit of the main branch the branch contains; `{merge-onto}` — the commit of the main branch
  that a merge into it is made onto. Where the commit does not exist, the gate fills in that it does
  not exist (WAY-61).
- A method checks what its sentence is about, as it stands on the commit being checked: a check fed
  input made up for it is the method of a sentence about that check, not about the data it reads
  (WAY-61).
- k and n, for a method that does not give the same verdict every time, stand in the command
  (WAY-08, WAY-61).
- A method a product cannot yet name as any command reads `TODO`, and the entry is reported
  unchecked for that reason (WAY-63). A command whose program the product does not yet declare or
  produce is written out in full all the same, with the program named as it will run; that entry is
  reported unchecked for want of a declared or produced command, a different reason (WAY-63,
  WAY-38, WAY-47, WAY-67).
- One run may check many invariants. An entry's result is the verdict the run records for its
  identifier and current version, in a format from this closed list, which grows by a new version of
  WAY-61: the-way's own record of a run — TODO: its form. A run that records no verdict for the
  entry never gives it a pass (WAY-61).
- A population the product meets only in use — the loads real players make, for one — has no form
  yet: the method of a sentence about it reads
  `TODO — decision pending: the method of a population met only in use`, and the gate reports the
  entry unchecked (WAY-61).

## The sentence

- One entry states one invariant, in one sentence. The method and the links stand beside it, not
  inside it (WAY-56). The format guard counts sentences only, so two rules joined in one sentence
  pass it; what one sentence may join is judged against the complying and violating pair in
  WAY-56's *Verification* (WAY-56, WAY-12).
- The sentence is what binds: the entry's content fingerprint covers the sentence alone (WAY-59,
  WAY-39). The method, the links, the version, a declaration of a correction and the *Recovered*
  field stay outside it.
- A condition that decides whether a commit makes the sentence true stands in the sentence, or
  outside it only where changing it takes a change of the foundation that a human decides — an
  entry of the foundation, or an element's template, each written as the record of a decision — or
  where a decision of the product's own log, or of the-way at the commit the product pins, places
  it; where it has no such place, it stands in the sentence (WAY-60).
- A condition held in a document the product neither writes nor pins, such as an outside standard,
  has no such place: it stands in the sentence, and the fact it rests on is named in *Rests on*
  (WAY-60, WAY-73).
- A sentence names no branch — neither as a point to compare with nor as the place where it holds —
  since a branch names a different commit by the hour. A sentence measuring what a commit, a merge
  or a merge request changes names the commit it is measured against by its value on the gate's
  list above: `{fork-point}`, unless the decision the entry derives from chooses `{merge-onto}`. A
  sentence that is to hold on the main branch alone holds where `{merge-onto}` exists (WAY-60,
  WAY-61).
- A sentence about a check the product itself holds names a value of that list in quotation marks,
  as what the check is given, and its command, a test fed input made up for it, need not take it
  (WAY-60, WAY-61). Quoted text, in this template, is text between quotation marks; a value in
  backticks is not quoted.
- A sentence that bounds or equates a quantity measured while the product runs names its bound or
  tolerance, the statistic and the population it is computed over (WAY-60). A bound written with a
  tilde — `~2 seconds` — names no bound, so the sentence states one as a number or has none
  (WAY-60).
- A sentence may be about a check the product itself holds, as it may be about anything else the
  product holds: whether a check is part of the product is settled by the part map, and the method
  of such a sentence is a test fed input made up for it (WAY-61).
- A sentence about what a check reports may also mean that the data it reads meets a rule; where
  it does, the data takes a sentence of its own, and the two stand as two entries, one about the
  check and one about the data (WAY-56, WAY-61).

## Links

- *Derives from* names every decision entry this invariant is derived from, and *Rests on* every
  environment fact it rests on; neither link is optional, and a link the author knows is missing
  reads `TODO` rather than `none` (WAY-17).
- *Rests on* names every environment fact holding a condition that decides whether a commit makes
  the sentence true, and no other: read otherwise, such a fact would give some commit another
  verdict under the same sentence, or change a value the sentence copies from it. A fact that is
  only a reason for a decision the entry derives from stays in that decision's *Based on* (WAY-73).
- Both carry the content fingerprint of each entry they name, and *Part* carries none. A change to
  that fingerprint reaches the main branch with every invariant carrying it, each checked against
  the new wording and carrying the new fingerprint (WAY-66).
- Until the environment facts element has entries, a fact is written as
  `TODO — <the fact, with its source>` (WAY-66).

## Part

- *Part* names the parts of the part map in which a change can make the sentence false, or `every`
  where a change to any part can; never both. A part missing from the list stops the invariant from
  running where it can break, and nothing shows it, so a writer in doubt names more (WAY-62).
- *Part* has no third value. A sentence no commit of this product can make false is not an
  invariant of this product (WAY-22): it belongs to the foundation of the product whose commits
  decide it.
- A change, against the commit its branch left the main branch from, reaches an entry that names
  `every` or a part the change touches, or whose method names a file the change alters (WAY-62).
- The entry names no failure mode, critical flow or surface (WAY-62).
- In the file holding invariant entries, a change of an entry touches the parts that entry names,
  and `every` touches all (WAY-44, WAY-62).

## Version and correction

- An entry carries a version, starting at 1. When its fingerprint differs from its fingerprint on
  the main branch, its version is one higher than there, unless *Correction* names both
  fingerprints and the human who decides the change confirms, with both wordings in front of them,
  that the meaning is unchanged (WAY-57).
- A change after which some test citing the entry would need a different expected value is a
  raise, never a correction (WAY-57).
- The guard compares an entry with its state where the task branch left the main branch; where
  there is no main branch, it compares nothing, says so, and every entry stays at version 1
  (WAY-57).
- Until the confirmation has a home, the guard reports a declared correction as "correction
  declared, confirmation not checked", never as agreeing (WAY-57).

## Test

- An invariant test cites its invariant by identifier and version, and a test that cites a version
  other than the current one fails the gate (WAY-57).
- A check cites each invariant it gives a verdict for, at the check, as a line
  `invariant: <identifier>/<version>` in the comment form of its file's language; a run records no
  verdict for an invariant its check does not cite. Several checks citing one invariant in one run
  pass only when each of them does (WAY-65).
- Each file such a check reads and names there stands on a line `data: <path>` — a recorded output
  it compares against, for one (WAY-65).
- A check stands in a file of code; a Markdown file holds no citing check.
- The file holding a citing check, and each file it names on a `data:` line, are invariant tests,
  read-only during implementation (WAY-03), when they are so on the commit the task branch left the
  main branch from or on the commit being checked. A path a human assesses against is no invariant
  test (WAY-65).
- A test counts only when a deliberate break of the invariant makes it fail (WAY-08).
- A test takes the input it asserts on and the value it expects written out, wherever the code its
  invariant is about would otherwise compute either; only the side it compares against comes from
  the run (WAY-70). Which files a test names, so that a fixture or a builder of its input cannot be
  changed underneath it, is not settled.
- An invariant's sentence and a check that cites it come from separate acts by different agents,
  and the break the check is accepted on is written from the sentence by an agent other than the
  check's author, with that check and the files it reads out of its input (WAY-69). This binds the
  act of writing a check, not the history of the file it joins.

## Recovered

An entry a human chose from what the product already did before the task writing it began, and that
names no decision entry of the product's own log it derives from, reads
`recovered — searched: <…>; found: <…>`; every other entry reads `none` (WAY-58). A decision named
anywhere but that log — a numbered decision in a concept document, a decision of the-way at the
commit the product pins — is no such decision, and the entry still reads `recovered`.

*found* names the place of each source the search found that gives a reason for keeping the
behaviour or calls for a different one, or reads `nothing`. A place that only cites another is
followed to the place it cites, and is marked where that source is superseded. *found* never states
a reason itself, nor one an agent infers. The field rests on a judgment: the human deciding the
change sets it with the gate's report in front of them — whether the entry's method passes on the
commit the branch left the main branch from and fails there on a deliberate break, or that this
could not be checked (WAY-58). An entry whose wording changes — by a raised version, by a
correction, or by a split or a merge — enters again, and its field is set again (WAY-57, WAY-58,
WAY-64).

## Result, report and debt

- An entry's result on the commit being checked is `pass`, `fail`, `unchecked` for a reason on the
  list below, or `error` where there is no verdict for any other reason, or where a quarantine has
  lapsed (WAY-63, WAY-68).
- The gate reports a result for at least every entry a change reaches and every entry a critical
  flow names. Its command exits non-zero when some result it reports is `error`, when an entry on
  the list of violated invariants results `pass`, when an entry not on that list results `fail`, or
  when a run records a failure for no entry, and zero otherwise (WAY-63, WAY-67).
- Reasons for `unchecked` — a closed list, which grows by a new version of WAY-63:
  - the method reads `TODO`;
  - the method is a path, and no human verdict is in force;
  - the method's command or file is not declared or produced by the product, except a command
    declared on the commit the branch left the main branch from, whose drop makes the result `error`
    (WAY-38, WAY-47, WAY-67);
  - the method takes a commit the gate filled in as not existing;
  - the entry stands on the list of quarantined invariants at its current version, and the
    committer date of the commit being checked is no later than its *Until* (WAY-68).
- A human verdict names who, when and the commit assessed, and is in force until a change since that
  commit reaches the entry (WAY-63).
- Where a human verdict is recorded, and how the gate reads it, is
  `TODO — decision pending: where a human verdict stands and how the gate reads it`. Until that is
  settled, an entry whose method is a path is reported `unchecked` for want of a verdict in force.
- A declared command that cannot start, or a record holding a value off a closed list, is `error`.
  Runs on a deliberate break, and the run WAY-58 asks for, give evidence, not results (WAY-63).

## Quarantine

- An invariant test that records both `pass` and `fail` for one commit is answered by a foundation
  change; a quarantine is the last answer, and never covers an invariant a critical flow names
  (WAY-68).
- Where a test records both `pass` and `fail` for one commit, the recorded `fail` stays the entry's
  result on that commit until a foundation change answers the flipping, whatever a later run
  records (WAY-68).
- A quarantine position names the entry's identifier, its current version and an end date, and
  stands on the last list in the file (WAY-68).
- A rerun set anywhere but the method's command is no change of a test's form, so a human decides
  it (WAY-10).

## Violated invariants

The derived file beside the invariants, `foundations/violated_invariants.md`, holds every invariant
the product does not meet today, by identifier and current version. A listed `fail` leaves the
gate's command at zero, and a listed `pass` makes it fail until the same change drops the position.
A position is added only by a change of the foundation that a human accepts, never by a step of
implementation. The file is checked as a subset of the list on the commit the branch left the main
branch from, never regenerated from scratch (WAY-53, WAY-67).

```markdown
## Violated invariants

| Identifier | Version |
```

## Fields and their readers

A field stays in this template only while someone or something reads it (WAY-05).

| Field | Who reads it, when | Where its value comes from |
|---|---|---|
| identifier (heading) | a citing test; the part map, in a flow and a failure mode's detection | judgment |
| version (heading) | a citing test; the guard, which computes what the version must be | read off |
| sentence | the agent checking a change against the invariant; the content fingerprint; the gate, through the method | prose |
| Method | the gate, which runs a command or hands a path to a human | judgment |
| Rests on | whoever reviews the invariant when a fact changes; the format guard, which compares each fingerprint with the current one (WAY-66) | judgment for the fact named; read off for its fingerprint |
| Derives from | whoever changes the decision; the check that an invariant named in a decision's level 1 verification names that decision (WAY-17); the format guard, which compares each fingerprint with the current one (WAY-66) | judgment for the decision named; read off for its fingerprint |
| Part | the gate, which runs the invariants a change reaches; the agent analysing a task | judgment |
| Correction | the guard, which lets the version stand; the human who confirms it | judgment for the declaration; read off for both fingerprints |
| Recovered | the human weighing a change to the invariant; the agent recovering a part's decisions | judgment |
| withdrawn identifiers | whoever follows an identifier that no longer names an entry, from a citing test or a decision on the main branch (WAY-07, WAY-64); the format guard, which keeps a withdrawn identifier from coming back and checks its successors (WAY-64) | read off |
| quarantined invariants | the gate, which reports the entry `unchecked` or `error`; the format guard | judgment for the date; read off for the version |
| violated invariants | the gate, which leaves a listed `fail` at zero and fails on a listed `pass`; the format guard, which compares the list with the commit the branch left the main branch from | judgment for the position; read off for the version |
A field marked *judgment* holds someone's call: no tool reads its value off the product, and no question about a fact settles it. A reader takes such a value as a call, not as a reading (WAY-54). A field marked *prose* carries text rather than a value.

## What the format guard checks

- The product has exactly one file of invariant entries, `foundations/invariants.md` (WAY-64).
- The file holds its entries, then its withdrawn identifiers, then its quarantined invariants, each
  in the form above, and no other heading (WAY-64, WAY-68).
- Every identifier has the form above, and none is held by another entry or withdrawn identifier
  of this file or of the part map (WAY-64).
- Every identifier the file held on the commit the task branch left the main branch from stands in
  it, and one withdrawn there is withdrawn still (WAY-64).
- Every successor a withdrawn identifier names is an entry or a withdrawn identifier of this file,
  or `none` (WAY-64).
- Every entry carries every field of the form above, and no field holds `none` or `TODO` where the
  form does not give it that word (WAY-71).
- No entry carries a field the form above does not hold, nor text outside its sentence and fields.
- Every entry states its invariant in one sentence (WAY-56).
- Every entry carries a method (WAY-08).
- Every entry carries a version; an entry with no fingerprint on the main branch carries version 1
  and no correction; an entry whose fingerprint differs from there carries a version one higher or
  a correction naming both fingerprints; an entry whose fingerprint equals it there keeps its
  version and declares no correction whose second fingerprint differs from it (WAY-57).
- No entry holds, beside its current wording, a wording it held on the commit the branch left the
  main branch from (WAY-57).
- The fingerprint of an entry is the fingerprint of its sentence alone, and a change to anything
  else in the entry leaves it unchanged (WAY-59).
- Every entry carries *Recovered*, as `none` or in its form; an entry that names a decision entry
  of the product's own log it derives from holds `none` (WAY-58).
- No sentence, outside quoted text, contains the words "main branch" or "task branch" (WAY-60).
- Every value from the gate's list that a sentence names outside quoted text is taken by its
  command, unless its method is not a command (WAY-60).
- No sentence bounds or equates a measured quantity with a tilde in place of a number (WAY-60).
- Every entry names `every` or at least one part of the part map, never both (WAY-62).
- Every method is a command that begins with a program's name, the path alone of a file that
  exists, or `TODO`; every value a command takes from the gate, and every value in braces a sentence
  names outside quoted text, stands on the list above (WAY-61, WAY-63).
- Every name in *Rests on* or *Derives from*, other than `none` or `TODO`, carries the current
  fingerprint of the entry it names (WAY-66).
- Every invariant test cites its invariant with a version, and none cites a version other than the
  current one (WAY-57).
- Every `invariant:` line in a check names an entry, and every `data:` line names a file that
  exists (WAY-65).
- The list of violated invariants is a subset of the list on the commit the branch left the main
  branch from; every position names an entry at its current version and no other (WAY-67).
- Every quarantine position names an entry at its current version and an end date, and none names
  an invariant a critical flow names (WAY-68).
- Every example in `examples.md` matches its entry in the file word for word (WAY-05).
- The guard reports how many entries it could not check and why, never agreement (WAY-38).

## Examples

Examples live in `examples.md`: entries copied word for word from a real set of invariants. Until
the first entries are written, only the forms above stand (WAY-05).

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
  its list of withdrawn identifiers (WAY-64).
- One derived file lies beside it: the list of violated invariants (WAY-67).
- Every entry carries an identifier of one or more words in lower case joined by hyphens, never
  `none`, held by no other entry or withdrawn identifier of this file or of the part map (WAY-64).
- The identifier names what the sentence constrains, never what it demands, so that a raised
  version leaves it true; where another entry constrains the same thing, it adds the aspect this
  one guards, as `entry-version-number` and `entry-version-correction` (WAY-64).
- An identifier the file held on the commit the task branch left the main branch from stays, as
  an entry or as a withdrawn identifier naming its successors or `none`; one that never reached
  the main branch may go (WAY-64).
- Splitting or merging entries held there gives every result a new identifier. Any other change,
  a change of meaning included, keeps the identifier and moves the version (WAY-57); an entry that
  takes in a clause of another keeps its identifier, and the other is split (WAY-64).
- An entry holds only its current wording; earlier wordings are read from git (WAY-57).

## Entry

```markdown
## <identifier>/<version>

<one sentence: the invariant>

- **Method:** `<program> <arguments>` | <path of a file a human assesses the product against>
- **Rests on:** <environment fact>@<fingerprint> · … | TODO — <the fact, with its source> | none
- **Derives from:** <decision>@<fingerprint> · … | none
- **Part:** <parts from the part map> | every
- **Correction:** none | <fingerprint on the main branch> → <current fingerprint>
- **Recovered:** none | recovered — searched: <…>; found: <…>
```

The file ends with its withdrawn identifiers; *Successors* lists identifiers joined by ` · `, or
reads `none`:

```markdown
## Withdrawn identifiers

| Identifier | Successors |
```

## Method

- A method is a command the gate runs, which begins with the name of the program it runs and is
  never a path alone, or the path alone of a file a human assesses the product against. The form is
  the route; no kind of method is written beside it (WAY-61).
- A command is the same on every run and names no commit, branch or revision itself. A commit the
  sentence names is a value the gate fills in, from this list: `{fork-point}` — the commit the task
  branch left the main branch from, which is the last commit of the main branch the branch contains;
  `{merge-onto}` — the commit a merge is made onto. Where the commit does not exist, the gate fills
  in that it does not exist (WAY-61).
- A method checks what its sentence is about, as it stands on the commit being checked: a check fed
  input made up for it is the method of a sentence about that check, not about the data it reads
  (WAY-61).
- k and n, for a method that does not give the same verdict every time, stand in the command
  (WAY-08, WAY-61).
- One run may check many invariants. An entry's result is the verdict the run records for its
  identifier and current version, in a format from this list: the-way's own record of a run —
  TODO: its form. A run that records no verdict for the entry never gives it a pass (WAY-61).
- A quantity met only in use has no form yet: its method reads
  `TODO — decision pending: the method of a population met only in use`, and it is reported as
  unchecked (WAY-61).

*Derives from* and *Rests on* carry the content fingerprint of each entry they name, and *Part*
carries none. A change to that fingerprint reaches the main branch with every invariant carrying
it, each checked against the new wording and carrying the new fingerprint (WAY-66).

## The sentence

- One entry states one invariant, in one sentence. The method and the links stand beside it, not
  inside it (WAY-56). What one sentence may join is judged against a pair of examples; the format
  guard counts sentences only.
- The sentence is what binds: the entry's content fingerprint covers the sentence alone (WAY-59,
  WAY-39). The method, the links, the version, a declaration of a correction and the *Recovered*
  field stay outside it.
- A condition that decides whether a commit makes the sentence true stands in the sentence, or
  outside it only where changing it takes a change of the foundation that a human decides, or where
  a decision places it; where it has no such place, it stands in the sentence (WAY-60).
- A sentence whose truth turns on what a branch or a merge changes names a commit of the main
  branch fixed by the commit being checked — such as the last commit of the main branch that the
  branch contains, or the commit a merge is made onto — never the main branch as it stands when the
  check runs (WAY-60).
- A sentence that bounds or equates a quantity measured while the product runs names its bound or
  tolerance, the statistic and the population it is computed over (WAY-60). A bound given with a
  wave — `~`, "about", "roughly" — is an error of the entry, since it only looks checkable.
- The sentence states a property of the product, not the mechanism that produces it. Whether it
  names a mechanism is settled by the part map, not by wording: a sentence about the quality gate is
  a property of the product where the gate's files belong to a part of the map.

## Part

- *Part* names the parts of the part map in which a change can make the sentence false, or `every`
  where a change to any part can; never both. A part missing from the list stops the invariant from
  running where it can break, and nothing shows it, so a writer in doubt names more (WAY-62).
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
  raise, never a correction.
- The guard compares an entry with its state where the task branch left the main branch; where
  there is no main branch, it compares nothing, says so, and every entry stays at version 1.
- Until the confirmation has a home, the guard reports a declared correction as "correction
  declared, confirmation not checked", never as agreeing.

## Test

- An invariant test cites its invariant by identifier and version, and a test that cites a version
  other than the current one fails the gate (WAY-57).
- A check cites each invariant it gives a verdict for, at the check, as a line
  `invariant: <identifier>/<version>` in the comment form of its file's language; a run records no
  verdict for an invariant its check does not cite. Several checks citing one invariant in one run
  pass only when each of them does (WAY-65).
- A file it reads that cannot carry the line itself, such as a recorded output it compares against,
  is named by the check's file on a line `data: <path>` (WAY-65).
- The file holding a citing check, and each file it names on a `data:` line, are invariant tests,
  read-only during implementation (WAY-03), when they are so on the commit the task branch left the
  main branch from or on the commit being checked. A path a human assesses against is no invariant
  test (WAY-65).
- A test counts only when a deliberate break of the invariant makes it fail (WAY-08). The
  expected value is written out, never computed by the function under test.

## Recovered

An entry a human chose from what the product already did before the task writing it began, and
that names no decision it derives from, reads `recovered — searched: <…>; found: <…>`; every other
entry reads `none` (WAY-58). *found* names the place of each source that gives a reason for keeping
the behaviour or calls for a different one, or reads `nothing`; it never states a reason itself.
The field rests on a judgment: the human deciding the change sets it, with the gate's report on the
commit the branch left from in front of them.

## Result, report and debt

- An entry's result on the commit being checked is `pass`, `fail`, `unchecked` for a reason on the
  list below, or `error` where there is no verdict for any other reason (WAY-63).
- The gate reports a result for at least every entry a change reaches and every entry a critical
  flow names. Its command exits non-zero when some result it reports is `error`, a listed
  entry's result is `pass`, or an unlisted entry's result is `fail`, or a run records a failure for
  no entry, and zero otherwise (WAY-63, WAY-67).
- Reasons for `unchecked` — a closed list, which grows by a new version of WAY-63:
  - the method reads `TODO`;
  - the method is a path, and no human verdict is in force;
  - the method's command or file is not declared or produced by the product, except a command
    declared on the commit the branch left the main branch from, whose drop makes the result `error`
    (WAY-38, WAY-47, WAY-67);
  - the method takes a commit the gate filled in as not existing.
- A human verdict names who, when and the commit assessed, and is in force until a change since that
  commit reaches the entry (WAY-63).
- A declared command that cannot start, or a record holding a value off a closed list, is `error`.
  Runs on a deliberate break, and the run WAY-58 asks for, give evidence, not results (WAY-63).
- TODO — decision pending: quarantine. How a flaky test is handled.
- TODO — decision pending: who writes what. Who may write an invariant's sentence, its test and its
  deliberate break.

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
| identifier / version (heading) | a citing test; the part map, in a flow and a failure mode's detection; the guard, which computes what the version must be | read off |
| sentence | the agent checking a change against the invariant; the content fingerprint; the gate, through the method | prose |
| Method | the gate, which runs a command or hands a path to a human | judgment |
| Rests on | whoever reviews the invariant when a fact changes; the format guard, which compares each fingerprint with the current one (WAY-66) | judgment for the fact named; read off for its fingerprint |
| Derives from | whoever changes the decision; the check that a decision is verified through its invariants (WAY-12); the format guard, which compares each fingerprint with the current one (WAY-66) | judgment for the decision named; read off for its fingerprint |
| Part | the gate, which runs the invariants a change reaches; the agent analysing a task | judgment |
| Correction | the guard, which lets the version stand; the human who confirms it | read off |
| Recovered | the human weighing a change to the invariant; the agent recovering a part's decisions | judgment |
| withdrawn identifiers | a test, a flow or a failure mode naming an identifier that no longer names an entry | read off |
A field marked *judgment* holds someone's call: no tool reads its value off the product, and no question about a fact settles it. A reader takes such a value as a call, not as a reading (WAY-54). A field marked *prose* carries text rather than a value.

## What the format guard checks

- The product has exactly one file of invariant entries, `foundations/invariants.md` (WAY-64).
- Every identifier has the form above, and none is held by another entry or withdrawn identifier
  of this file or of the part map (WAY-64).
- Every identifier the file held on the commit the task branch left the main branch from stands in
  it, and one withdrawn there is withdrawn still (WAY-64).
- Every successor a withdrawn identifier names is an entry or a withdrawn identifier of this file,
  or `none` (WAY-64).
- Every entry states its invariant in one sentence (WAY-56).
- Every entry carries a version; an entry with no fingerprint on the main branch carries version 1
  and no correction; an entry whose fingerprint differs from there carries a version one higher or
  a correction naming both fingerprints; an entry whose fingerprint equals it there keeps its
  version (WAY-57).
- The fingerprint of an entry is the fingerprint of its sentence alone, and a change to anything
  else in the entry leaves it unchanged (WAY-59).
- Every entry carries *Recovered*, as `none` or in its form; an entry that names a decision it
  derives from holds `none` (WAY-58).
- No sentence, outside quoted text, names the main branch after "than", "subset of", "differs
  from", "equals", "compared with" or "against" without naming a commit of it (WAY-60).
- No sentence gives a bound with a wave.
- Every entry names `every` or at least one part of the part map, never both (WAY-62).
- Every method is a command that begins with a program's name, or the path alone of a file that
  exists; every value a command takes from the gate stands on the list above (WAY-61).
- Every name in *Rests on* or *Derives from*, other than `none` or `TODO`, carries the current
  fingerprint of the entry it names (WAY-66).
- Every invariant test cites its invariant with a version, and none cites a version other than the
  current one (WAY-57).
- Every `invariant:` line in a check names an entry, and every `data:` line names a file that
  exists (WAY-65).
- The list of violated invariants is a subset of the list on the commit the branch left the main
  branch from; every position names an entry at its current version and no other (WAY-67).
- The guard reports how many entries it could not check and why, never agreement (WAY-38).

## Examples

Examples live in `examples.md`: entries copied word for word from a real set of invariants. Until
the first entries are written, only the forms above stand (WAY-05).

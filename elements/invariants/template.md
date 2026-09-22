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

- TODO — decision pending: how an invariant entry is identified. Where the entries of a product
  live (one file or several), what identifies an entry, and what happens to a citing test when an
  entry is split, merged or withdrawn — the counterpart of WAY-41 for the map.
- An entry holds only its current wording; earlier wordings are read from git (WAY-57).

## Entry

```markdown
## <identifier>/<version>

<one sentence: the invariant>

- **Method:** <handle — a command or a path, never prose> · reads: <how the result is read> ·
  runs as: script | declared | human
- **Rests on:** <environment facts> | none
- **Derives from:** <decision> | none
- **Part:** TODO — decision pending: what an invariant entry names in the part map
- **Correction:** none | <fingerprint on the main branch> → <current fingerprint>
- **Recovered:** none | recovered — searched: <…>; found: <…>
```

TODO — decision pending: how an invariant is checked. The *Method* line above follows the settled
proposal (handle, reading, way of running) and waits for its decision; so does an optional kind of
evidence, and the place of k and n for a test that does not give the same result every time.

TODO — decision pending: which links beside the sentence carry a content fingerprint. *Rests on*
and *Derives from* are written today as bare identifiers; whether they carry the fingerprint of
the entry they name, as `derives from` does between decisions (WAY-31), waits for that decision.

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
- TODO — decision pending: how an entry is linked to its test. The form of the citation (in the
  test file, or `not markable` with a reason where there is no file to mark), which paths are
  protected, and comparison with the base branch.
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

- TODO — decision pending: what the gate reports. The states of a result and which of them block.
- TODO — decision pending: debt, quarantine and the rules on who writes what. How an invariant
  the product violates is listed, how a flaky test is handled, and who may write an invariant's
  sentence and its test.

## Fields and their readers

A field stays in this template only while someone or something reads it (WAY-05).

| Field | Who reads it, when | Where its value comes from |
|---|---|---|
| identifier / version (heading) | a citing test; the guard, which computes what the version must be | read off |
| sentence | the agent checking a change against the invariant; the content fingerprint; the gate, through the method | prose |
| Method | the gate, which runs it | judgment |
| Rests on | whoever reviews the invariant when a fact changes | judgment |
| Derives from | whoever changes the decision; the check that a decision is verified through its invariants (WAY-12) | judgment |
| Part | TODO — decision pending | — |
| Correction | the guard, which lets the version stand; the human who confirms it | read off |
| Recovered | the human weighing a change to the invariant; the agent recovering a part's decisions | judgment |
A field marked *judgment* holds someone's call: no tool reads its value off the product, and no question about a fact settles it. A reader takes such a value as a call, not as a reading (WAY-54). A field marked *prose* carries text rather than a value.

## What the format guard checks

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
- Every invariant test cites its invariant with a version, and none cites a version other than the
  current one (WAY-57).
- The guard reports how many entries it could not check and why, never agreement (WAY-38).

## Examples

Examples live in `examples.md`: entries copied word for word from a real set of invariants. Until
the first entries are written, only the forms above stand (WAY-05).

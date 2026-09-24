# Invariant entry examples

Verbatim copies of entries from this repository's invariants (`foundations/invariants.md`), chosen
to show each form the template describes: a method that runs a format guard on the real file; a
method that runs the tests of a guard, for a sentence about what the guard reports; `every` in
*Part* with a fact in *Rests on*; a fact of an outside standard behind a value the sentence names;
and a `TODO` method under a sentence that holds only where `{merge-onto}` exists. Before the main
branch a copy follows its entry, and the format guard checks that every example matches its entry
word for word.

## log-entry-field-presence/1

Every entry of the decision log carries every field the decision template gives an entry of its kind.

- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --record .runs/decisions.jsonl`
- **Rests on:** none
- **Derives from:** WAY-71@8b16c32e
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## decision-guard-overdue-review/1

The decision guard, given a date, warns of every check-by date earlier than it that no later review entry answers.

- **Method:** `python -B -m unittest discover -s elements/decisions -p "test_*.py"`
- **Rests on:** none
- **Derives from:** WAY-24@058a356a
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## file-part-assignment/1

Every file git tracks matches the path patterns of exactly one part of the part map, or stands on the map's list of files left out on purpose.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md`
- **Rests on:** TODO — git matches a path pattern as it matches a pattern of a `.gitattributes` file (https://git-scm.com/docs/gitattributes), and reports the match through `git check-attr` (https://git-scm.com/docs/git-check-attr)
- **Derives from:** WAY-44@220f5b85
- **Part:** every
- **Correction:** none
- **Recovered:** none

## fingerprint-definition/1

The relation model's script gives a text the first eight characters, in lower-case hexadecimal, of the SHA-256 digest of that text encoded in UTF-8, after every run of spaces and line breaks is replaced by a single space and both ends are trimmed.

- **Method:** `python -B -m unittest discover -s relation-model -p "test_*.py"`
- **Rests on:** TODO — SHA-256 as the Secure Hash Standard, FIPS 180-4, specifies it (https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf), and UTF-8 as RFC 3629 defines it (https://www.rfc-editor.org/rfc/rfc3629.html)
- **Derives from:** WAY-39@a3b77692
- **Part:** relation-model
- **Correction:** none
- **Recovered:** none

## return-step-record/1

Where {merge-onto} exists, every change against {fork-point} carries the record of its task's return step.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-11@52847c55
- **Part:** every
- **Correction:** none
- **Recovered:** none

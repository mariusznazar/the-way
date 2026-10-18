# Guidelines template

This file defines the form every file of a product's guidelines takes, whatever its discipline. A
product's guidelines are written by hand and stand outside its foundation (WAY-167). They hold no
rule of their own: each binding rule names the decision of the product's log that carries its
choice and each invariant that checks it, and says what to do and how; its reasons and rejected
options stand in that decision alone (WAY-168). The form check of guidelines,
`product-guidelines/form_check.py`, checks every file of a product's guidelines against this
template and, where the-way gives one, against the template of the file's discipline, at the commit
of the-way the repository uses (WAY-170).

Each rule below cites the decision of the-way that sets it, and a rule of this template changes
only with such a decision (WAY-171). Nothing of this template is copied into a product: a product's
guidelines are checked against it at the commit the product pins (WAY-34).

## Where guidelines go

- A product's guidelines stand in the directory `guidelines/` at the root of its repository, in a
  file `guidelines/<discipline>.md` for each discipline of work on the product it keeps guidelines
  of; the guidelines of the styleguide discipline stand in a file `guidelines/styleguide-<part>.md`
  for each user interface of the product, `<part>` being the identifier of the part of the
  product's map whose files draw that user interface (WAY-167).
- The directory `guidelines/` belongs to the part of the product's map whose files direct whoever
  carries out its tasks, as its instruction files and skills do; the task that writes the
  product's first guidelines adds `guidelines/**` to that part's files (WAY-167).
- A file's name agrees with its *Discipline*, and the form check reports a file whose name and
  *Discipline* disagree (WAY-167, WAY-170).

## Required form

The form check reads the form from the fenced block of this section. A discipline's template adds
sections and required rules to it at the places it names (WAY-171).

```markdown
# <Discipline> guidelines — <what they cover>

- **Discipline:** <discipline>
- **Applies to:** <part> · …

## When to read

## Rules

### <rule name>

- **Decision:** <PREFIX-NN>@<fingerprint> · …
- **Invariant:** <identifier>@<fingerprint> · … | none
- **Good:** <a use that follows the rule>
- **Bad:** <a use that breaks it>

<how to apply the rule: what to do, and how>

## Examples

### <example name>

## Where in code
```

- *Discipline* names the discipline the file covers. Where the-way holds a template of that
  discipline, `product-guidelines/<discipline>/template.md`, that template adds to this form;
  otherwise this form alone applies, so a product may keep guidelines of a discipline the-way gives
  no template of (WAY-170, WAY-171).
- *Applies to* names parts of the product's map, joined by ` · `; the form check reports a part the
  map does not hold (WAY-171).
- `## When to read` says when an agent reads the file: before which work, on which part (WAY-171).
- **A binding rule** stands under `## Rules`, under a `### ` heading of its own, with the fields
  *Decision*, *Invariant*, *Good* and *Bad* in that order, followed by how to apply it (WAY-171).
  *Decision* names at least one decision of the product's log that carries the rule's choice;
  *Invariant* names each invariant that checks the rule, or reads `none`; *Good* gives a use that
  follows the rule and *Bad* one that breaks it (WAY-168). A discipline's template may require an
  invariant in every rule; the styleguide's template does (WAY-188).
- **A rule carries no rationale and no rejected options**: those stand in the decision it names
  (WAY-168).
- **What names no decision is an example**, not a rule: it stands under `## Examples`, under a
  `### ` heading of its own, and carries no *Decision* field (WAY-168).
- **`## Where in code`** lists, as paths in backticks relative to the root of the repository, the
  files and directories of the product the guidelines point to, and copies no value from them
  (WAY-171). Each path names something git tracks; a path that is absolute or holds a `..` segment,
  a drive or a UNC prefix is an error of the form check (WAY-170).
- **A required section or required rule the product drops** holds, as its only text, the marker
  `none —` followed by the product's decision that departs from the template, with its fingerprint:
  `none — <PREFIX-NN>@<fingerprint>` (WAY-171). Text the departing decision keeps as an example may
  then stand under `## Examples` (WAY-168).

## Rules of writing

- **References.** A reference is a run of characters anywhere in the file outside fenced code — in
  a field, a `none —` line, a table row, a rule's text or an example — of one of two forms: a
  decision number with the log's prefix, or an identifier the invariants file holds as an entry or
  as a withdrawn identifier, followed by `@` and a run of letters and digits; or any identifier
  followed by `@` and exactly eight lower-case hexadecimal characters with no letter or digit after
  them (WAY-169).
- A reference relies on the binding part of the entry it names and carries that entry's
  fingerprint: the first eight lower-case hexadecimal characters of the SHA-256 digest of the
  binding part, as `relation-model/fingerprint.py` computes it (WAY-02). It names a decision the log
  holds and has not repealed, or an invariant the invariants file holds and has not withdrawn, and
  carries its current fingerprint on the commit checked and, where a main branch exists, after the
  merge onto it (WAY-169).
- **A reference whose entry changed its binding part stops the merge**: the same change brings the
  guidelines in line with the entry's new binding part and only then gives the reference the new
  fingerprint. A fingerprint is never renewed without reading the text that relies on it (WAY-169).
- **A bare identifier** — a decision number or an invariant's identifier with no `@` after it — is
  allowed anywhere and is never flagged (WAY-02). A versioned package name, `<package>@<version>`,
  fits neither form of a reference and is no reference, unless its name is a decision number or an
  identifier of the invariants file, or its version is eight hexadecimal characters. Text that would
  read as a reference but is none — an address, a sample, such a package name — stands in fenced
  code (WAY-169).
- **Language.** The headings of the required form, the header lines, the field names, the values of
  closed lists, the headings of required rules and the marker `none —` stay in English, because the
  form check reads them; the rest of the text is in the language the product writes its guidelines
  in, which the-way does not set (WAY-171). Its price: a product may write one file of guidelines in
  one language and another in another.

## Note: a file of guidelines read as an instruction file

This note is no rule of the template and cites no decision as setting it. It says how two files of
the-way read a file of guidelines once a product's root `AGENTS.md` or `CLAUDE.md` names it by its
path: the file is then a repository instruction file, as the glossary of the-way defines that term,
and these files read it as one.

- `instruction-files/check_instructions.py` follows such a file and checks it as an instruction
  file. It takes text in backticks holding a `/` for a path, and reports it as a dead path when
  nothing lies there; and it takes an `@` followed by a word holding `.` or `/`, outside code, for an
  import. A file of guidelines that keeps that script quiet writes the names of code, at-rules and
  selectors in backticks, a class name or a value holding a `/` — a fraction, or a role with an
  opacity after a slash — in fenced code, and no `@` import of a file outside code.
- `instruction-files/principles.md` puts emphasis — words written in capitals to make a rule stand
  out — on one rule per file at most, and `instruction-files/check_instructions.py` warns where more
  than one line of a file carries such words.

## The invariants of guidelines

Two invariants check a product's guidelines, and this template gives their identifiers and
sentences. The sentences are given, not the product's to reword: the form check cites
`guidelines-form/1` and `guidelines-reference-current/1`, and a product that reworded either would
raise its version and leave its run with no verdict for it. A change to either sentence is a change
of the-way, which raises the-way's own entry and the form check's citation together (WAY-170).

The-way holds both in its own invariants file, deriving `guidelines-form` from WAY-170 and WAY-171
and `guidelines-reference-current` from WAY-169; with no `guidelines/` of its own, both hold there.
A product that keeps guidelines holds copies with the same identifiers and sentences, written
through the skill `record-invariant` by the task that writes its first guidelines (WAY-170). A
product's copy reads `Derives from: none`, since no decision of the product's log carries it; its
sentence comes from the decisions of the-way named above.

```markdown
## guidelines-form/1

Every file `guidelines/<name>.md` holds, in their order, the header lines, sections, rules, rule fields and tables that the template of guidelines and the template of its discipline require at the commit of the-way the repository uses — the commit checked, in the-way itself, and the pinned commit, in a product — each with the values and the links those templates give it, with a name that agrees with its *Discipline*, each section or rule it drops reading `none —` with a decision of the log and that decision's fingerprint, each part it names being a part of the map, and each path under `## Where in code` naming something git tracks.

- **Method:** `python -B .the-way/product-guidelines/form_check.py --record .runs/guidelines-form.jsonl`
- **Rests on:** none
- **Derives from:** none
- **Part:** every
- **Correction:** none
```

```markdown
## guidelines-reference-current/1

Every reference outside fenced code in a file `guidelines/<name>.md` — a decision number of the log or an identifier of the invariants file followed by `@` and a run of letters and digits, or any identifier followed by `@` and eight lower-case hexadecimal characters — names a decision of the log that is not repealed or an invariant of the file that is not withdrawn, and carries the fingerprint of that entry's binding part in the foundation of the same commit and, where {merge-onto} exists, in the foundation a merge onto {merge-onto} leaves.

- **Method:** `python -B .the-way/product-guidelines/form_check.py --merge-onto {merge-onto} --record .runs/guidelines-reference.jsonl`
- **Rests on:** none
- **Derives from:** none
- **Part:** <the part whose files direct whoever carries out the product's tasks> · <the part holding `foundations/**`> · <the part holding `.the-way`>
- **Correction:** none
```

- `guidelines-form` names `every` in *Part*: a renamed file of the product, a renamed part or a
  moved pin can make it false whatever part a change touches (WAY-62).
- `guidelines-reference-current` names the part that holds `guidelines/**`, the part that holds the
  product's foundation, whose reworded decision or invariant leaves a reference stale, and the part
  that holds the pinned the-way, whose move can change how fingerprints are read (WAY-62).
- In the-way itself the methods run `product-guidelines/form_check.py`, and the reference
  invariant's *Part* reads `product-guidelines · decisions · invariants` (WAY-62).
- Before the product has a main branch, the gate fills in `none` for `{merge-onto}`: the check
  after the merge records `unchecked` beside the verdict of the check on the same commit, and that
  is the expected state (WAY-61).

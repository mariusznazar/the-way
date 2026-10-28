# Guidelines template

This file defines the form every file of a product's guidelines takes, whatever its discipline. A
product's guidelines are written by hand and stand outside its foundation (WAY-167). They hold no
rule of their own: each binding rule names by identifier the decision of the product's log that
carries its choice, names the invariant whose test checks it where a cheap test can, and says what
to do and how; its reasons and rejected options stand in that decision alone (WAY-168). No script
checks the form of guidelines: the review of a change that writes or changes them compares them
with this template and, where the-way gives one, the template of their discipline, and
`elements/common/foundation_check.py` reports a decision number, a rule's invariant or a part of
*Applies to* that the foundation does not hold, or holds as withdrawn (WAY-170).

A rule below that a decision of the-way sets cites that decision. Nothing of this template is copied
into a product: a product's guidelines follow it at the commit the product pins (WAY-34).

## Where guidelines go

- A product's guidelines stand in the directory `guidelines/` at the root of its repository, in a
  file `guidelines/<discipline>.md` for each discipline of work on the product it keeps guidelines
  of, save the styleguide and coding disciplines (WAY-167).
- The guidelines of the styleguide discipline stand in a file `guidelines/styleguide-<part>.md` for
  each user interface of the product, `<part>` being the identifier of the part of the product's
  map whose files draw that user interface (WAY-167).
- The guidelines of the coding discipline stand in a file `guidelines/coding.md`, which holds the
  product's standing checks, the rules of the whole of its code and a table naming each other file
  of the discipline with when to read it, and in a file `guidelines/coding-<kind>.md` for each kind
  of code that has an exemplar, which holds that exemplar and its rules, `<kind>` being the
  identifier of the kind that the decision designating that exemplar gives (WAY-167).
- The directory `guidelines/` belongs to the part of the product's map whose files direct whoever
  carries out its tasks, as its instruction files and skills do; the task that writes the
  product's first guidelines adds `guidelines/**` to that part's files (WAY-167).
- A file's name agrees with its *Discipline* (WAY-167).

## Required form

Every file of guidelines holds the form of the fenced block below. A discipline's template adds
sections and required rules to it at the places it names (WAY-171).

```markdown
# <Discipline> guidelines — <what they cover>

- **Discipline:** <discipline>
- **Applies to:** <part> · …

## When to read

## Rules

### <rule name>

- **Decision:** <PREFIX-NN> · …
- **Invariant:** <identifier> · … | none
- **Good:** <one line describing a use that follows the rule> | none
- **Bad:** <one line describing a use that breaks it> | none

<how to apply the rule: what to do, and how>

## Examples

### <example name>

## Where in code
```

- *Discipline* names the discipline the file covers. Where the-way holds a template of that
  discipline, `product-guidelines/<discipline>/template.md`, that template adds to this form;
  otherwise this form alone applies, so a product may keep guidelines of a discipline the-way gives
  no template of (WAY-171).
- *Applies to* names parts of the product's map, joined by ` · `; `foundation_check.py` reports a
  part the map does not hold (WAY-170, WAY-171).
- `## When to read` says when an agent reads the file: before which work, on which part (WAY-171).
- **A binding rule** stands under `## Rules`, under a `### ` heading of its own, with the fields
  *Decision*, *Invariant*, *Good* and *Bad* in that order, followed by how to apply it (WAY-171).
  *Decision* names, by identifier, at least one decision of the product's log that carries the
  rule's choice; *Good* may describe in one line a use that follows the rule and *Bad* one that
  breaks it, and each reads `none` where the rule gives no such use (WAY-168, WAY-171).
- **An invariant only where a cheap test checks the rule.** *Invariant* names the invariant whose
  test in the product's suite checks the rule on a convention of the product's code — a value
  written in place of a design token, an endpoint that skips the validation of its input — and
  reads `none` for a rule no such test can check; the review of each change the rule reaches then
  compares the change with it (WAY-168).
- **A rule carries no rationale and no rejected options**: those stand in the decision it names
  (WAY-168).
- **What names no decision is an example**, not a rule: it stands under `## Examples`, under a
  `### ` heading of its own, and carries no *Decision* field (WAY-168).
- **`## Where in code`** lists, as paths in backticks relative to the root of the repository, the
  files and directories of the product the guidelines point to, each a path git tracks, and copies
  no value from them (WAY-171).
- **A required section or required rule the product drops** holds, as its only text, the marker
  `none —` followed by the product's decision that departs from the template: `none — <PREFIX-NN>`
  (WAY-171). Text the departing decision keeps as an example may then stand under `## Examples`
  (WAY-168).

## Rules of writing

- **References.** Guidelines name a decision of the product's log or an invariant of its foundation
  by its identifier alone, with no fingerprint and no version, and name an entry the foundation
  holds and has not withdrawn (WAY-02); `elements/common/foundation_check.py` reports a decision
  number anywhere in the file, and an invariant of a rule's *Invariant*, that names no entry or a
  withdrawn one (WAY-170).
- **A changed entry brings its rules along.** A change that changes the binding part of a decision
  or an invariant the guidelines name brings every rule naming it in line in the same change; its
  author finds those rules by the entry's identifier (WAY-169).
- **Language.** The headings of the required form, the header lines, the field names, the values of
  closed lists, the headings of required rules and the marker `none —` stay in English, because
  the-way's templates and skills name them and the check of references reads fields by their names;
  the rest of the text is in the language the product writes its guidelines in, which the-way does
  not set (WAY-171). Its price: a product may write one file of guidelines in one language and
  another in another.

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
- Code a rule or an example shows stays in fenced code, where that script reads no path and no
  import. That script switches between code and text on every line that starts, after any leading
  whitespace, with three backticks or three tildes.
- `instruction-files/SKILL.md` puts emphasis — words written in capitals to make a rule stand
  out — on one rule per file at most, and `instruction-files/check_instructions.py` warns where more
  than one line of a file carries such words.

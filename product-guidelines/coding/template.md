# Coding guidelines template

This file defines what the guidelines of the coding discipline add to the form every product's
guidelines share, `product-guidelines/template.md`, and what each section of a product's coding
guidelines carries. It is written for the author who writes a product's coding guidelines in a
task's cycle. A product keeps them in a general file `guidelines/coding.md`, which holds its
standing checks, the rules of the whole of its code and a table naming each other file of the
discipline with when to read it, and in a file `guidelines/coding-<kind>.md` for each kind of code
that has an exemplar, which holds that exemplar and its rules, `<kind>` being the identifier of the
kind that the decision designating that exemplar gives (WAY-167).

The rules this template carries bind a product only through a decision of the product's log adopting
them, and the product departs from any of them only by a decision of its log that gives the reason;
a decision of the-way on what this template carries binds the template, never a product's code
directly (WAY-193). Each rule below cites the decision of the-way that sets it (WAY-171). The rules
of form every file of guidelines keeps — the header lines, the fields of a rule, the test cases of a
rule, references, code in backticks or fenced code, the language of the text, a dropped section or
rule — stand in `product-guidelines/template.md`; this template holds what is particular to coding
guidelines.

## Required form

The form check reads the merged form of the general file `guidelines/coding.md` from the fenced
block of this section: the form of `product-guidelines/template.md` with the section
`## Kinds of code` and the required rules of the coding discipline in their places (WAY-171).

```markdown
# Coding guidelines — <the product>

- **Discipline:** coding
- **Applies to:** <part> · …

## When to read

## Kinds of code

| Kind | File | When to read |
|---|---|---|

## Rules

### Linter
### Formatter
### Dependency audit
### <further rules of the whole product>

## Examples

### <example name>

## Where in code
```

- Each `### ` under `## Rules` carries the fields *Decision*, *Invariant*, *Good* and *Bad* the
  template of guidelines gives a rule, and its *Invariant* names at least one invariant that checks
  it, by a script where a script can decide it and otherwise by an agent whose method sets k of n
  runs, never by an agent judging whether new code follows the exemplar of its kind (WAY-171,
  WAY-196).
- The three standing checks, `### Linter`, `### Formatter` and `### Dependency audit`, stand in the
  order above, and each that the product goes without reads `none — <PREFIX-NN>@<fingerprint>`,
  naming the product's decision that departs from it with its reason (WAY-171, WAY-202). The
  product's further rules follow them.
- A rule that neither a script nor such an agent can check is an example, not a rule, whatever
  decision it names: the product drops it by a decision, and may keep its text under `## Examples`
  (WAY-196).
- *Applies to* names every part of the product's map that holds code, the scripts of its build
  included (WAY-208).
- `## When to read` gives the condition under which an agent reads the file: before any change of
  the product's code (WAY-212).
- `## Kinds of code` holds the table of the product's files of a kind, one row for each, with when
  to read it; a product with no exemplar yet keeps the table with its header and no row (WAY-167,
  WAY-212).

## Required form of a kind

The form check reads the merged form of a file `guidelines/coding-<kind>.md` from the fenced block
of this section: the form of `product-guidelines/template.md` with the section
`## Files of this kind` in its place (WAY-171, WAY-199).

```markdown
# Coding guidelines — <kind>

- **Discipline:** coding
- **Applies to:** <part> · …

## When to read

## Files of this kind

| File | Status | Decision |
|---|---|---|

## Rules

### <rule a script checks from the exemplar>

## Examples

### <example name>

## Where in code
```

- Each `### ` under `## Rules` carries the fields *Decision*, *Invariant*, *Good* and *Bad* the
  template of guidelines gives a rule, and its *Invariant* names at least one invariant that checks
  it, by a script where a script can decide it and otherwise by an agent whose method sets k of n
  runs, never by an agent judging whether new code follows the exemplar (WAY-171, WAY-196).
- A rule that neither a script nor such an agent can check is an example, not a rule, whatever
  decision it names (WAY-196).
- The file's name holds the identifier of its kind, as the decision designating the kind's exemplar
  gives it: words of lower-case letters and digits joined by single hyphens, as `endpoint` or
  `background-job` (WAY-167).
- *Applies to* names the parts of the product's map that the files of the kind lie in (WAY-171).
- `## When to read` gives the condition under which an agent reads the file: before adding or
  changing a file of its kind (WAY-212).

## What each section carries

Each section below is marked as a rule or an example, with what it carries and, for a rule, the
decision and invariant the skill `maintain-coding-guidelines` proposes for it. The product writes
those decisions and invariants in its own foundation; the coding guidelines name them.

- **`## Kinds of code`** — a table of the general file, one row for each file of a kind (WAY-167,
  WAY-212):
  - *Kind*: the identifier of the kind, as the name of its file holds it;
  - *File*: the path of that file, `guidelines/coding-<kind>.md`, in backticks;
  - *When to read*: the condition under which an agent reads that file, such as "before adding or
    changing an endpoint".

  No row stands for a kind that has no exemplar yet (WAY-167).
- **Linter** — rule. *Decision*: the product's decision adopting the linter and its set of rules,
  naming the set, its edition, the parts it reads and the rules of the set that stand among the
  examples for the reports they give that lead to no change of code worth making (WAY-86, WAY-202,
  WAY-203, WAY-204). *Invariant*:
  1. a script the product declares, that no file of the parts named breaks a rule of the set that
     blocks, resting on the environment fact of the set's edition (WAY-203, WAY-73); an inline
     suppression of a rule that blocks counts as a break, since such a rule gives no report that
     leads to no change worth making, so no suppression of it is sound, and a fault of one file is
     fixed in that file (WAY-203, WAY-207, WAY-193);
  2. the rules that block are exactly the list of the adopting decision, so that turning one off
     fails the gate until that decision changes (WAY-207, WAY-60). Where the method of the first
     invariant passes that list to the tool itself, the first invariant already holds it and no
     second is written; where the method reads the product's configuration, a second invariant, by
     a script, keeps that configuration to the list; the skill names in the task which way the tool
     allows (WAY-207);
  3. where the product's code already breaks the rules that block, the first invariant stands on
     the list of violated invariants, and beside it an invariant that holds from its first day: no
     file of the parts named holds more reports of those rules than on `{fork-point}`, and a file
     not on `{fork-point}` holds none (WAY-205).
- **Formatter** — rule. *Decision*: the product's decision adopting the formatter and its
  configuration (WAY-202). *Invariant*: a script the product declares, that every file of the parts
  named stands as the formatter leaves it. A product whose code does not stand so when the formatter
  enters is reformatted whole, once, by the task that brings the formatter, with no second invariant
  (WAY-205).
- **Dependency audit** — rule. *Decision*: the product's decision adopting the audit, naming its
  tool, the advisory database it reads and the severity from which a vulnerability counts; the skill
  puts that severity to the human with every severity among the ways (WAY-202, WAY-206, WAY-60).
  *Invariant*: a script the product declares, that the change against `{fork-point}` brings in no
  version of a dependency with a known vulnerability of at least that severity, as that database
  gives it when the check runs (WAY-206).
- **The *Part* of each invariant of a standing check** names the parts holding the code it reads and
  the part holding the product's build configuration and its lockfile, where the tool's
  configuration and its pinned version stand; the audit's names the parts holding every manifest and
  lockfile it reads. A change of a configuration file or of the lockfile alone thus reaches it
  (WAY-62).
- **A standing check the product goes without** reads `none — <PREFIX-NN>@<fingerprint>`, naming the
  product's decision that departs from it with its reason (WAY-202, WAY-171).
- **Further rules of the whole product** — rule each, with an invariant each (WAY-196).
- **`## Files of this kind`** — a table of the file of a kind, one row for each file of the kind it
  lists (WAY-199):
  - *File*: the path of the file, in backticks, relative to the root of the repository; it names
    something git tracks;
  - *Status*: one of `exemplar`, `copy` or `do not copy`;
  - *Decision*: on the row whose *Status* is `exemplar`, the product's decision designating that
    file, with its fingerprint; on every other row, `—`.

  Exactly one row is the exemplar's, and the binding sentences of its decision name in backticks
  that path and the kind's identifier (WAY-198, WAY-199). The audit that writes or refreshes the
  file lists every file of the kind the product then holds, with its status; a file added after
  that audit takes no row until the guidelines are refreshed or extended (WAY-200).
- **Rules of a file of a kind** — what a script can check of the exemplar: where a file of the kind
  lies, what it calls, how it validates its input; a rule and an invariant each (WAY-198).
- **`## Examples`** — example. The rest of the exemplar (WAY-198), and the rules of the linter's set
  kept for the reports they give that lead to no change of code worth making, each named as the tool
  names it (WAY-203); nothing here binds (WAY-168).
- **`## Where in code`** — in the general file, the configuration files of the standing checks and
  the product's scripts of their invariants; in a file of a kind, the directories its files lie in;
  no value is copied from them (WAY-171).
- **The product's copy of `guidelines-form`** carries, in coding guidelines, what the form check
  reports of their tables and test cases: the table of `## Kinds of code` and its agreement with
  the files of a kind, the closed list of *Status*, the one exemplar and its decision naming its
  path and kind, each *File* naming something git tracks, and the test cases of each rule with
  their paths.
  These are values and links the templates give, which that invariant's sentence covers (WAY-170,
  WAY-171).
- **Test cases of the standing checks** — each rule gives a pair of cases for each invariant it
  names, as `product-guidelines/template.md` has it (WAY-168):
  - for the first invariant of `### Linter`, a short new source file at a new path within the parts
    named, one breaking a rule that blocks and one following it;
  - for its second, where it is written, the linter's configuration file at its path, one with a
    rule of the decision's list turned off and one holding the list exactly;
  - for its third, where it is written, a short new source file holding one report of a rule that
    blocks and one holding none;
  - for `### Formatter`, a short new source file left unformatted and the same file formatted;
  - for `### Dependency audit`, a manifest or lockfile of one dependency at a new path within the
    parts the audit reads, one naming a version with a known vulnerability and one a version with
    none.

  The product's scripts read a short file at a new path within the parts they read: the linter and
  the formatter every file of those parts, the audit every manifest and lockfile there. Where the
  first invariant of `### Linter` stands on the list of violated invariants, its cases are read
  against the commit's own result, while those of the third take the strict reading (WAY-168,
  WAY-205).

## The tools of the standing checks

- **Pinned versions.** Each standing check's tool stands at an exact version in the product's
  declared dependencies and lockfile, and the method of each of its invariants runs that pinned
  version from the product's own environment, never a version fetched when the check runs: a
  command is the same on every run (WAY-61). A new version of a linter that changes the edition of
  the adopted set is a change of the adopting decision and of the set's environment fact (WAY-86,
  WAY-172). The advisory database the audit reads is read as it stands when the check runs
  (WAY-206).
- **One environment fact for each edition of a set.** The fact's sentence holds which rules the set
  holds at the edition the decision adopts, quoting the page of the tool's documentation of that
  version that lists them: one edition of one source, one thing — the set's membership — and one
  reason to change, a new edition (WAY-76). A rule of a set is a requirement whose content the
  pinned tool carries out, so the invariant takes from the set its membership alone, where a
  criterion of WCAG, a requirement of its own in prose, stands as a fact of its own (WAY-191). The
  invariant of the rules that block rests on that fact (WAY-73); no fact stands for each rule.
- **The rules that block stand in the adopting decision**, as the set taken whole less the rules it
  keeps among the examples (WAY-60, WAY-204); the first or the second invariant of `### Linter`
  keeps them there (WAY-207).
- **Inline suppressions** of a rule that blocks count as breaks in the first invariant of
  `### Linter`, as that rule has it above (WAY-203, WAY-193).
- **The record of a run.** Each invariant's method is a script the product declares, which runs the
  tool and writes the-way's record of a run: a line for each invariant it gives a verdict for,
  `pass` or `fail` from the tool's result, and a failure recorded for no entry where the tool could
  not run (WAY-61, WAY-74), as the scripts of a styleguide's invariants do (WAY-189). The-way gives
  no adapter for a tool's own report; the product's command stands where the-way has none (WAY-38).
- **No command of its own in the instructions.** The coding guidelines and the product's `AGENTS.md`
  name the invariants, never a command of a tool to run beside the gate (WAY-16).

## Writing the files

For the author who writes the coding guidelines in a task's cycle:

- Take every tool, set of rules, exemplar, status and departure from the task's settlements and
  from the decisions the task's foundation step wrote, never from memory (WAY-172, WAY-211).
- Point to the configuration and to the code; copy no value into the guidelines (WAY-171).
- Write each test case as `product-guidelines/template.md` gives it (WAY-168).
- Run the form check. A choice the task did not settle is a question that stops the cycle at a
  blocked draft request, never a rule or a row (WAY-172).

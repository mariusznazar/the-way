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
directly (WAY-173). A rule below that a decision of the-way sets cites that decision. The rules
of form every file of guidelines keeps — the header lines, the fields of a rule, references, code in
backticks or fenced code, the language of the text, a dropped section or rule — stand in
`product-guidelines/template.md`; this template holds what is particular to coding guidelines.

## Required form

The general file `guidelines/coding.md` holds the form of the fenced block of this section: the
form of `product-guidelines/template.md` with the section `## Kinds of code` and the required rules
of the coding discipline in their places (WAY-171).

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
### Recording a failure
### Hiding a failure
### Identifiers in log lines
### Business events
### Secrets and personal data
### Logging scope
### <further rules of the whole product>

## Examples

### <example name>

## Where in code
```

- Each `### ` under `## Rules` carries the fields *Decision*, *Invariant*, *Good* and *Bad* the
  template of guidelines gives a rule. The rule of each standing check names the invariants of that
  check as the section "What each section carries" gives; any other rule names an invariant where a cheap test checks it on a
  convention of the product's code, and otherwise reads `none`, the review of each change the rule
  reaches comparing the change with it (WAY-168, WAY-202).
- The three standing checks, `### Linter`, `### Formatter` and `### Dependency audit`, stand in the
  order above, and each that the product goes without reads `none — <PREFIX-NN>`, naming the
  product's decision that departs from it with its reason (WAY-171, WAY-202).
- The six required rules on failures and logs, from `### Recording a failure` to `### Logging scope`,
  follow the standing checks in the order above, and the product's further rules follow those; a
  product that already has further rules takes the six in between when it adds them (WAY-271). A
  file of a kind holds none of the six.
- *Applies to* names every part of the product's map that holds code, the scripts of its build
  included (WAY-208).
- `## When to read` gives the condition under which an agent reads the file: before any change of
  the product's code (WAY-212).
- `## Kinds of code` holds the table of the product's files of a kind, one row for each, with when
  to read it; a product with no exemplar yet keeps the table with its header and no row (WAY-167,
  WAY-212). A kind is code of the product other than its tests; the rules of the tests stand in the
  product's testing guidelines (WAY-231).

## Required form of a kind

A file `guidelines/coding-<kind>.md` holds the form of the fenced block of this section: the form of
`product-guidelines/template.md` with the section `## Files of this kind` in its place (WAY-171,
WAY-199).

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
  template of guidelines gives a rule, and its *Invariant* names the invariant whose test checks
  the rule on the files of the kind (WAY-171, WAY-198).
- The file's name holds the identifier of its kind, as the decision designating the kind's exemplar
  gives it: words of lower-case letters and digits joined by single hyphens, as `endpoint` or
  `background-job` (WAY-167). A kind is code of the product other than its tests (WAY-231).
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
  WAY-203, WAY-204). *Invariant*: that no file of the parts named breaks a rule of the set that
  blocks, resting on the environment fact of the set's edition (WAY-203, WAY-73). A comment in the
  code that turns off a rule that blocks has no effect: where the tool can be told so by a flag or
  its configuration, the invariant's test runs it so, and where it cannot, the review of each
  change finds such a comment; a fault of one file is fixed in that file (WAY-203, WAY-207,
  WAY-173). Turning a rule that blocks off in the linter's configuration is a change of the
  adopting decision; the rule of the linter carries this one invariant, and the review of each
  change to the configuration holds the configuration to the decision (WAY-207).

  Where the product's code already breaks the rules that block, the invariant is marked violated
  until the code is cleaned (WAY-205, WAY-51).
- **Formatter** — rule. *Decision*: the product's decision adopting the formatter and its
  configuration (WAY-202). *Invariant*: that every file of the parts named stands as the formatter
  leaves it. A product whose code does not stand so when the formatter enters is reformatted whole,
  once, by the task that brings the formatter (WAY-205).
- **Dependency audit** — rule. *Decision*: the product's decision adopting the audit, naming its
  tool, the advisory database it reads and the severity from which a vulnerability counts; the skill
  puts that severity to the human with every severity among the ways (WAY-202, WAY-206, WAY-60).
  *Invariant*: that the change against `{fork-point}` brings in no version of a dependency with a
  known vulnerability of at least that severity, as that database gives it when the check runs
  (WAY-206).
- **The *Part* of each invariant of a standing check** names the parts holding the code it reads and
  the part holding the product's build configuration and its lockfile, where the tool's
  configuration and its pinned version stand; the audit's names the parts holding every manifest and
  lockfile it reads. A change of a configuration file or of the lockfile alone thus reaches it
  (WAY-62).
- **A standing check the product goes without** reads `none — <PREFIX-NN>`, naming the product's
  decision that departs from it with its reason (WAY-202, WAY-171).
- **The rules on failures and logs** — the six rules below. They are no standing checks: no tool
  comes with them, and each is a rule of the whole of the code (WAY-271). They say how code writes to
  the product's logs and what the product promises to log; where the logs go, how long they live and
  how a human learns of a failure stay with the step that settles technology (WAY-165, WAY-270).
  Each carries:
  - *Decision*: the product's one decision on these rules, apart from the decision adopting this
    template, which holds in at most three binding sentences which of the rules it adopts and what it
    departs from, the form of a log line, the principle of its logging scope and the boundary of what
    an agent adds alone (WAY-279). The decision a degraded mode takes is not named here, or the rule
    would change with every such decision;
  - *Invariant*: `none`, unless a cheap test checks the whole rule on a convention of the product's
    code. A test that catches only a fragment, such as an empty block that catches an error, is a
    rule of the product's linter under that linter's invariant, once it passes the trial WAY-203
    gives, and not a rule of these (WAY-271);
  - *Good* and *Bad*: this template proposes none; the product writes them or `none`, and neither
    copies the list of `### Logging scope`.

  Below, each rule's bullet gives what the product's text says of how to apply it. A rule carries no
  reason: the reasons stand in the decisions it names (WAY-168).
- **Recording a failure** — rule. A failure is a situation in which the product did not do what it
  was asked to do or what it was to do on its own, for a reason other than an expected refusal, a
  failed outside service included; an expected refusal, such as a wrong password, is an ordinary
  answer, which the rule does not reach. A failure is written always with its cause, the original
  error and not a bare string, once, where code handles it. Each separately running program of the
  product has one last-resort handler, which writes what no code handled (WAY-272).
- **Hiding a failure** — rule. A failure is turned neither into an "all fine" answer nor into an
  empty list. A degraded mode, in which the product goes on without one function, is allowed only
  where a task sets it, recording it as a decision of the product, and it always leaves a line in
  the logs (WAY-273).
- **Identifiers in log lines** — rule. A line of a case flow, which is what the product does for one
  case from a request or a background job to its end, carries the identifiers that join the events
  of that case flow, each under the same name in every line, so that a search finds the whole case,
  in the form of a line the product's decision gives. A line outside a case flow, such as one at the
  start of a program or one of a build script, carries none. A line from the last-resort handler
  need carry none, since that handler usually does not know what the case was (WAY-275).
- **Business events** — rule. Each business event `### Logging scope` lists leaves a log line
  (WAY-275).
- **Secrets and personal data** — rule. The logs hold no secret, with no exception, so an identifier
  that is a secret stays out even where it stands on the list. They hold no personal data, the
  identifiers `### Logging scope` lists being the one exception, to this ban alone. Code writes no
  whole object and no request body, which does not touch the error itself. An original error that
  quotes such values is written without them, with its kind, code and place in the code, this rule
  prevailing over `### Recording a failure` (WAY-276).
- **Logging scope** — rule. After the rule's fields, in no field, stands the list of today: the
  identifiers the product logs, each with the name it takes in every line, and its business events,
  at adoption from what the product has in its code or in its plan. The text says that the list is
  the product's promise and no inventory of its code, and how an item is added: where it fits the
  principle of the product's decision, in the change that brings it; where it points to a person,
  the number the product gives a user included, only with the human's consent, as a new meaning
  (WAY-274, WAY-172).
- **Further rules of the whole product** — rule each, naming an invariant where a cheap test checks
  it on a convention of the code and otherwise `none` (WAY-168).
- **`## Files of this kind`** — a table of the file of a kind, one row for each file of the kind it
  lists (WAY-199):
  - *File*: the path of the file, in backticks, relative to the root of the repository; it names
    something git tracks;
  - *Status*: one of `exemplar`, `copy` or `do not copy`;
  - *Decision*: on the row whose *Status* is `exemplar`, the product's decision designating that
    file, by its identifier; on every other row, `—`.

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
  the product's tests of their invariants; in a file of a kind, the directories its files lie in;
  no value is copied from them (WAY-171).

## Departing from the rules on failures and logs

A product departs from these rules only by its one decision on them, which gives the reason; a later
departure edits that decision in place, approved as WAY-30 and WAY-172 give (WAY-173, WAY-279). The
ways below stand in the order they are taken: the first that does what the product wants is the one
it takes.

1. **What points to a person, wanted in the logs.** Where the thing is an identifier, it is first an
   item of `### Logging scope`, with the human's consent. That is no departure, and nothing else
   changes (WAY-274).
2. **From the ban on personal data alone.** The rule stays, with its heading and fields, *Decision*
   naming the product's decision. In the rule's text the one line `Personal data: none — <PREFIX-NN>`
   stands in place of the ban, and the rest of the rule stands as it is: the ban on secrets, the ban
   on whole objects and request bodies, and its precedence over `### Recording a failure` for a
   secret. An original error that quotes a secret is written without it, with its kind, code and
   place; one that quotes personal data is written as it stands. The line stays in English in
   whatever language the product writes its guidelines, as the marker `none —` does, since this
   template names it and a reviewer compares the file with this template. Only this ban departs in
   this way, because WAY-276 names it alone.
3. **From one rule.** That heading holds only `none — <PREFIX-NN>`, naming the product's decision,
   and the others stay. A rule whose subject has gone reads `none —` too, with the same decision, so
   a departure from `### Logging scope` puts the marker on three headings (WAY-171, WAY-279).
4. **From all of them.** Each of the six headings stands, holding only `none — <PREFIX-NN>`, and the
   list goes; the product's decision says so with its reason and holds nothing else, no principle,
   boundary or form of a line, and no question of a library comes (WAY-171, WAY-279).

Text the decision keeps as an example may stand under `## Examples` (WAY-168). What a kept rule still
needs:

| Departed from | Goes with it | Stays |
|---|---|---|
| `### Logging scope` | `### Identifiers in log lines` and `### Business events`, which have nothing left to read and read `none —` with the same decision; the principle, the boundary, the form of a line | `### Secrets and personal data`, with no exception |
| `### Identifiers in log lines` | the form of a line | the identifiers of the list, as the exception to the ban on personal data, while that rule stands |
| `### Business events` | the events of the list and of the principle | the rest |
| `### Secrets and personal data`, the rule whole | the ban on secrets and the ban on whole objects and request bodies; `### Recording a failure` is no longer narrowed, so an original error may write what it quotes, secrets included | the boundary, while `### Logging scope` stands |
| the ban on personal data alone | the exception of the list, which has nothing left to except; the precedence as to personal data | everything else of the rule; the list and the boundary, while `### Logging scope` stands |
| `### Recording a failure` or `### Hiding a failure` | nothing else | the rest |

## The tools of the standing checks

- **Pinned versions.** Each standing check's tool stands at an exact version in the product's
  declared dependencies and lockfile, and the test of each of its invariants runs that pinned
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
  keeps among the examples (WAY-60, WAY-204); the review of each change to the linter's
  configuration keeps the configuration to them (WAY-207).
- **Comments that turn a rule off** have no effect where the tool can be told so, and the review of
  each change finds them where it cannot, as `### Linter` has it above (WAY-203, WAY-173).
- **The test of each invariant.** Each invariant of a standing check has a test in the product's
  suite, in its language, that runs the pinned tool on the parts the invariant names and fails where
  the tool reports a break or cannot run (WAY-61, WAY-63).
- **No command of its own in the instructions.** The coding guidelines and the product's `AGENTS.md`
  name the invariants, never a command of a tool to run beside the gate (WAY-16).

## Writing the files

For the author who writes the coding guidelines in a task's cycle:

- Take every tool, library, set of rules, exemplar, status and departure from the task's settlements
  and from the decisions the task's foundation step wrote, never from memory (WAY-172, WAY-211,
  WAY-277).
- Point to the configuration and to the code; copy no value into the guidelines (WAY-171). The list
  of `### Logging scope` is no such copy: it is the product's promise, written from the task's
  settlements, never read off the code (WAY-274).
- A choice the task did not settle is a question that stops the cycle at a blocked draft request,
  never a rule or a row (WAY-172).

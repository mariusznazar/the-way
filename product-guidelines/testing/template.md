# Testing guidelines template

This file defines what the guidelines of the testing discipline add to the form every product's
guidelines share, `product-guidelines/template.md`, and what each section of a product's testing
guidelines carries. It is written for the author who writes a product's testing guidelines in a
task's cycle. Testing is a discipline of its own, apart from coding: a product keeps one file
`guidelines/testing.md`, written from this template, and the skill `maintain-testing-guidelines`
leads the work that creates and keeps it (WAY-167, WAY-231).

The rules this template carries bind a product only through a decision of the product's log adopting
them, and the product departs from any of them only by a decision of its log that gives the reason;
a decision of the-way on what this template carries binds the template, never a product's tests
directly (WAY-173). A rule below that a decision of the-way sets cites that decision. The rules of
form every file of guidelines keeps — the header lines, the fields of a rule, references, code in
backticks or fenced code, the language of the text, a dropped section or rule — stand in
`product-guidelines/template.md`; this template holds what is particular to testing guidelines. No
script checks its form (WAY-170).

## Required form

The file `guidelines/testing.md` holds the form of the fenced block of this section: the form of
`product-guidelines/template.md` with the sections `## Levels`, `## Recipes` and
`## Not tested on purpose` and the required rules of the testing discipline in their places
(WAY-171).

```markdown
# Testing guidelines — <the product>

- **Discipline:** testing
- **Applies to:** <part> · …

## When to read

## Levels

| Level | Decision |
|---|---|

| Part | Where its complexity lies |
|---|---|

## Rules

### Choosing the level
### A lower test for a bug caught high
### Where the expected value comes from
### Test inputs and expected values
### Changing an existing test
### Behaviour, not implementation
### Trust boundaries
### AI in tests
### Flaky tests
### <further rules of the product>

## Recipes

### <level>

- **Purpose:**
- **Files:**
- **Shape:**
- **Doubles:**
- **Data:**
- **Time and randomness:**
- **Exemplar:**
- **Command:**
- **Time limit:**

## Not tested on purpose

- <category of behaviour or of code> (<PREFIX-NN>)

## Examples

### <example name>

## Where in code
```

- Each `### ` under `## Rules` carries the fields *Decision*, *Invariant*, *Good* and *Bad* the
  template of guidelines gives a rule (WAY-171). Its *Invariant* reads `none` for every required
  rule but `### Trust boundaries`, which names the refusal invariant of each trust boundary of the
  product (WAY-235); a further rule names an invariant where a cheap test checks it on a convention
  of the product's code, and otherwise reads `none`, the review of each change the rule reaches
  comparing the change with it (WAY-168). This template proposes no *Good* or *Bad* line of its
  own: the product writes them, or `none`.
- The required rules stand in the order above, and each that the product goes without reads
  `none — <PREFIX-NN>`, naming the product's decision that departs from it with its reason
  (WAY-171, WAY-173). The product's further rules follow them.
- `## Recipes` holds one `### <level>` for each level the table of `## Levels` names, with the
  fields above in that order (WAY-241).
- A required section the product drops reads `none — <PREFIX-NN>` as well (WAY-171). This marker
  differs from the plain `none` of `## Not tested on purpose`, which says that the product excludes
  nothing (WAY-237).
- *Applies to* names every part of the product's map whose code the product's tests check and
  every part that holds test files; before the product's first test, the parts the product's plan
  gives tests (WAY-246).
- `## When to read` gives the condition under which an agent reads the file: before writing or
  changing a test (WAY-246).

## What each section carries

Each section below is marked as a rule or an example, with what it carries and, for a rule, the
decision and invariant the skill `maintain-testing-guidelines` proposes for it. The product writes
those decisions and invariants in its own foundation; the testing guidelines name them.

- **`## Levels`** — two tables (WAY-240):
  - the table of levels, one row for each level of the product's tests: *Level*, the name the
    product uses for it; *Decision*, the product's decision that sets the level. The table has no
    column for a definition. A level whose name means in the product something other than in the
    field — "integration" above all — is a term of the product's glossary, defined there by the
    resources a test of that level may touch, such as files, the network or a browser; the table
    names that term and copies no definition, so that the meaning stands once (WAY-240, WAY-226). A
    level whose name means what the field means takes no definition;
  - the table of parts, one row for each part *Applies to* names: *Part*, its identifier; *Where its
    complexity lies*, one sentence of whether the part's complexity lies in computation or in its
    connections (WAY-240).

  Neither table holds a proportion of levels (WAY-238).
- **Choosing the level** — rule. *Decision*: the product's decision adopting this template.
  *Invariant*: `none`. A test stands at the lowest level at which the break it names turns it red,
  unless going lower would mean replacing with a double exactly what can break; the author of the
  change chooses, in the task's cycle, which behaviour gets a permanent test and at which level,
  naming the break each test catches, and the review checks the choice against the product's
  testing guidelines; the guidelines give no proportion of levels (WAY-238). How to apply it: the
  table below, in which each row asks a question about the behaviour and gives the test a yes calls
  for. It names levels by their meaning in the field; a product reads each as the level of its
  `## Levels` that has that meaning.

  | Question about the behaviour | If yes |
  |---|---|
  | Is it a rule or a calculation that can be run without the network, files or a browser? | a permanent unit test |
  | Can a sentence be said that holds for every input — an operation undone by its inverse, a simpler version that gives the same result, something kept after every step, a result easier to check than to compute? | a property test, in place of examples or beside them |
  | Does the code talk to something the product controls itself — its own database, its files, its own server run locally? | an integration test against the real thing, one dependency at a time |
  | Does the code talk to someone else's service? | a double of that service in the test, and a separate contract test: a check that both sides agree on the format |
  | Can the break lie in the configuration or in how the parts are put together? | a smoke test after the build: a short check that the whole starts at all |
  | Is it a user journey whose break a person would report as "the product does not work"? | one end-to-end test for each such journey |
  | Was the bug caught only by a high-level test or by a human? | a test at the lowest level that catches the bug |
  | Does the code only copy or pass data on, with no rule of its own? | no permanent test, unless it lies on a trust boundary |
  | Can the test not be kept in a state where it gives the same result on the same code every time? | no permanent test; the review, or a check made once |
- **A lower test for a bug caught high** — rule. *Decision*: the product's decision adopting this
  template. *Invariant*: `none`. A bug that only a high-level test or a human caught also gets a
  test at the lowest level that catches it (WAY-239).
- **Where the expected value comes from** — rule. *Decision*: the product's decision adopting this
  template, and the product's decision naming those of its documents that are sources of expected
  values, such as its decision log, its glossary or its task descriptions. *Invariant*: `none`. The
  expected value of every test comes from one of: those documents; a relation the code under test
  does not compute; a crash counted as a failure; a human's judgement. It never comes from what the
  code gives today, snapshots and characterization tests included. Where a test's name does not show
  the source of a value, a comment in the test names it, by the line of the document or by the human
  and the date, and the review of a change asks of each assertion where its value comes from
  (WAY-232).
- **Test inputs and expected values** — rule. *Decision*: the product's decision adopting this
  template. *Invariant*: `none`; the review of each change compares its tests with the rule
  (WAY-168). A test takes the input it asserts on and the value it expects written out, wherever the
  code under test would otherwise compute either; only the side it compares against comes from the
  run. A property test takes its inputs from a test library's generator and its expected value from
  a relation the code under test does not compute — undoing the operation, an invariant's sentence,
  or a simpler version written from the requirement, not copied from the code — and a
  counterexample the library finds is kept as an ordinary test with its values written out
  (WAY-228). Which files a test names, so that a fixture or a builder of its input cannot be changed
  underneath it, this template does not settle.
- **Changing an existing test** — rule. *Decision*: the product's decision adopting this template.
  *Invariant*: `none`. Changing the expected value of an existing test, deleting a test, weakening
  an assertion, and skipping or disabling a test are one kind of change, each made with its cause on
  the side of the data or of the requirement and a pointer to the evidence of that cause; the review
  reads such a change made without them as masking a defect (WAY-233). How to apply it: the ways a
  test is weakened — equality loosened to "contains", a count removed, a tolerance raised, a skip, a
  deletion (WAY-233).
- **Behaviour, not implementation** — rule. *Decision*: the product's decision adopting this
  template. *Invariant*: `none`. A test's assertions check the behaviour its rule or its task
  requires; a detail of how the code carries it out that the requirement does not ask for is no
  condition of the test passing. The review asks of each assertion whether the code could change so
  that the required behaviour stays and the assertion breaks; a yes marks a detail. A check of the
  case's setup is allowed where it stands before the action, is marked as a precondition and checks
  a property of the case that the requirement names, never the structure of the data that builds the
  case (WAY-234). How to apply it: three details an assertion does not pin — a rule's index where a
  lasting identifier would serve the same behaviour, the exact wording of a message where the
  requirement asks only for a refusal, and the order of internal calls where only the result counts.
  No general exception allows comparing a whole state (WAY-234).
- **Trust boundaries** — rule. *Decision*: the product's decision adopting this template, and the
  product's decisions on permissions. *Invariant*: for each trust boundary of the product's map, at
  least one invariant that the boundary refuses crafted input or unauthorised access, checked by a
  permanent test that checks the refusal directly, takes the expected refusal from the product's
  decisions on permissions and is seen failing once (WAY-235, WAY-08). This is the one required rule
  whose *Invariant* is not `none`, although its tests check the product's behaviour rather than a
  convention of its code (WAY-235). A boundary that does not refuse today has its invariant marked
  violated (WAY-51); a boundary that is only the configuration of someone else's service stays with
  the review of each change that touches it (WAY-48, WAY-235). For authorization, the text of the
  rule holds a table of who, which resource and which action with the expected result — *Who*,
  *Resource*, *Action*, *Expected result*, *Decision* — each row naming by identifier the product's
  decision on permissions it comes from (WAY-235). Those decisions are grouped so that each keeps to
  one to three binding sentences (WAY-05), and the table copies no rationale from them; no decision
  holds the table, since a decision has no place for one.
- **AI in tests** — rule. *Decision*: the product's decision adopting this template, and the
  product's decision adopting each AI tool its tests use. *Invariant*: `none`. AI is no level of
  test: a test an AI wrote follows every rule of the testing guidelines, and an agent exploring the
  running product finds cases that become ordinary tests. An AI judge enters a permanent test only
  where the behaviour cannot be checked by a plain comparison, its verdict is yes or no, it has been
  checked on examples a human judged and runs on a pinned version of its model, and the testing
  guidelines say how they treat the spread of its verdicts. A tool that heals a test by itself
  changes only how the test finds what it acts on; a changed assertion or a red test turned into a
  skipped one is a change of `### Changing an existing test`. How each AI tool the product's tests
  use behaves stands in an environment fact of the product, naming the version the product uses,
  with the date its source was read (WAY-236).
- **Flaky tests** — rule. *Decision*: the product's decision adopting this template. *Invariant*:
  `none`. Running a flaky test again serves only the diagnosis of what makes it flaky, never making a
  run of the gate pass; disabling or deleting such a test is a change of
  `### Changing an existing test` (WAY-243).
- **Further rules of the product** — rule each, naming an invariant where a cheap test checks it on
  a convention of the code and otherwise `none` (WAY-168).
- **`## Recipes`** — for each level, the same fields in this order (WAY-241). A field that binds ends
  with the identifier of the product's decision that carries it, in parentheses, as
  `(<PREFIX-NN>)`; a field naming no decision stands as an example (WAY-241, WAY-168). A field that
  repeats another level's reads "as in `<level>`" (WAY-241).
  1. *Purpose* — what the level is for, and when not to use it;
  2. *Files* — where the level's files lie and how they are named;
  3. *Shape* — the name and build of a test: its name a sentence about behaviour, three phases, one
     behaviour, no logic in the test;
  4. *Doubles* — a real dependency where it is fast, deterministic and simple, then a working
     simplified version, then a stub or a mock; foreign types wrapped in an adapter of the product's
     own; the code under test never replaced; an assertion on a call only for an effect visible
     outside the product;
  5. *Data* — a value an assertion depends on stands in the test; shared setup only where nothing
     changes it;
  6. *Time and randomness* — the clock and the seed given from outside; waiting for an event with a
     limit in place of a fixed sleep;
  7. *Exemplar* — the level's exemplar test by its path, with the product's decision designating it;
     the field stands empty until a decision designates one, and designating another test is a
     change of that decision (WAY-242);
  8. *Command* — the gate's one command and how it narrows to the level, a file or a test, where the
     gate can; `none` where it cannot; no command of the test tool of its own (WAY-241, WAY-16);
  9. *Time limit* — a pointer to the configuration file that holds it, never its value (WAY-241).

  The defaults of fields 3 to 6 are what this template proposes; a product adopts them or departs
  from them by a decision (WAY-241, WAY-173).
- **`## Not tested on purpose`** — a section the template requires: one item for each category of
  behaviour or of code the product deliberately does not test, never a single file or test, each
  naming the product's decision that excludes it, whose binding sentences give the condition under
  which the category is tested again and whose rationale gives the reason; `none` where nothing is
  excluded. A trust boundary never stands here (WAY-237).
- **`## Examples`** — example. The kinds of tests without value that no rule above carries: a
  duplicate of another test, a test of trivial code, a loop over nearly identical inputs; nothing
  here binds (WAY-168).
- **`## Where in code`** — the configuration files of the test tools, the directories of each
  level's tests and the exemplar tests, each a path git tracks, with no value copied from them
  (WAY-171). Before the product's first test it names what git already tracks of these, and it may
  hold no item.

## Writing the file

For the author who writes the testing guidelines in a task's cycle:

- Take every level, document that is a source, exemplar, exclusion, departure and field of a recipe
  that binds from the task's settlements and from the decisions the task's foundation step wrote,
  never from memory (WAY-172).
- Point to the configuration and to the tests; copy no value into the guidelines (WAY-171).
- A choice the task did not settle is a question that stops the cycle at a blocked draft request,
  never a rule, a row or a field (WAY-172).

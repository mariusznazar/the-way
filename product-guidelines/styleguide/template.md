# Styleguide template

This file defines what the guidelines of the styleguide discipline add to the form every product's
guidelines share, `product-guidelines/template.md`, and what each section of a styleguide carries.
It is written for the author who writes a product's styleguide in a task's cycle. A product keeps a
styleguide for each of its user interfaces — its screens, an admin panel added to its backend
included — in a file `guidelines/styleguide-<part>.md`, `<part>` being the part of its map whose
files draw that user interface (WAY-167, WAY-183).

The rules this template carries bind a product only through a decision of the product's log adopting
them, and the product departs from any of them only by a decision of its log that gives the reason
(WAY-173). Each rule below cites the decision of the-way that sets it (WAY-171). The rules of form
every file of guidelines keeps — the header lines, the fields of a rule, references, code in
backticks or fenced code, the language of the text, a dropped section or rule, the test cases of a
rule that names an invariant — stand in `product-guidelines/template.md`; this template holds what
is particular to a styleguide.

## Required form

The form check reads the merged form of a styleguide from the fenced block of this section: the
form of `product-guidelines/template.md` with the section `## Roles` and the required rules and
examples of the styleguide in their places (WAY-171).

```markdown
# Styleguide guidelines — <the user interface it covers>

- **Discipline:** styleguide
- **Applies to:** <part>

## When to read

## Roles

| Role | Kind | Meaning for the user | Text on it | Decision |
|---|---|---|---|---|

## Rules

### Each role in its meaning
### Every background with its text
### No value in place of a design token
### Visible focus
### Contrast of every pair
### States of shared controls
### A fault of one screen is fixed in its component
### Every value with its source
### The kitchen-sink page
### <further rules of the product>

## Examples

### Mockups
### Plan of a user-interface change
### <further examples>

## Where in code
```

- Each `### ` under `## Rules` carries the fields *Decision*, *Invariant*, *Good* and *Bad* the
  template of guidelines gives a rule, and its *Invariant* names at least one invariant that checks
  it, by a script where a script can decide it and otherwise by an agent whose method sets k of n
  runs (WAY-171, WAY-188).
- Each required rule stands in the order above, or reads `none — <PREFIX-NN>@<fingerprint>`, naming
  the product's decision that drops it with its reason (WAY-171, WAY-173). The product's further
  rules follow the required ones.
- A rule that neither a script nor an agent can check is an example, not a rule, whatever decision
  it names: the product drops it by a decision, and may keep its text under `## Examples`
  (WAY-188).
- *Applies to* names the part of the map whose files draw the user interface the styleguide covers
  (WAY-167, WAY-171).
- `## When to read` gives the condition under which an agent reads the styleguide: before it
  changes a file of that part (WAY-192).

## What each section carries

Each section below is marked as a rule or an example, with what it carries and, for a rule, the
decision and invariant the skill `maintain-styleguide` proposes for it. The product writes those
decisions and invariants in its own foundation; the styleguide names them.

- **`## Roles`** — a table, one row for each role (WAY-176):
  - *Role*: the role's name in code, named by what it is for and never by a colour — `primary`,
    `muted`, `destructive`;
  - *Kind*: one of `background`, `text` or `other`;
  - *Meaning for the user*: one sentence of what someone using the product understands on seeing
    the role;
  - *Text on it*: for a role of the kind `background`, the role of the kind `text` in this table
    that stands on it, as `foreground` stands on `background`; for any other role, `—`;
  - *Decision*: the decision of the product's log that carries the role's meaning, with its
    fingerprint.

  The table holds no value: `## Where in code` points to the file of design tokens that holds them
  (WAY-176, WAY-171).
- **Each role in its meaning** — rule. A screen uses each role only in the meaning its decision
  gives, and a new or changed meaning is a new or changed decision, approved before the code that
  uses it (WAY-176, WAY-172). *Decision*: every decision the table of `## Roles` names. *Invariant*:
  one an agent checks with k of n, whose sentence speaks of every file of the user interface's
  part — no file of `<part>` uses a role in a meaning other than the one its decision gives — and
  whose *Part* names that part and the part holding `foundations/**` (WAY-189).
- **Every background with its text** — rule. A role of the kind `background` is always written
  with the role of the kind `text` that stands on it in the table; the contrast rule holds the
  pair's values in code (WAY-176). *Decision*: the product's decision adopting this template.
  *Invariant*: the product's copy of `guidelines-form`, whose form check reports a background with
  no text role (WAY-170, WAY-176).
- **No value in place of a design token** — rule. The files of the user interface read colours,
  lengths and fonts from design tokens (WAY-189). *Decision*: the product's decision that defines
  what counts as a value written in place of a design token (WAY-60). *Invariant*: a script the
  product declares, that no file of the part holds such a value; where the product cleans its
  screens as tasks touch their styles, beside it the invariant that no file of the part holds more
  such values than on `{fork-point}` and a file not on `{fork-point}` holds none (WAY-189,
  WAY-190).
- **Visible focus** — rule. Every control shows its focus with the style of the focus role
  (WAY-189). *Decision*: the product's decision adopting WCAG (WAY-191). *Invariant*: a script the
  product declares, resting on the environment fact of WCAG's criterion of visible focus (WAY-189,
  WAY-191).
- **Contrast of every pair** — rule. Every pair of a background and the text on it reaches the
  contrast WCAG sets, computed from the values of the file of design tokens (WAY-189).
  *Decision*: the decisions of the roles and the decision adopting WCAG. *Invariant*: a script the
  product declares, resting on the environment fact of WCAG's criterion of contrast (WAY-189,
  WAY-191).
- **States of shared controls** — rule. It points by its path to the directory of the product's
  shared components, and every shared control has the states default, hover, visible focus,
  disabled, error, empty and loading, each shown on the page of every state or marked as not
  applying with its reason; it names a component by its path only where that component departs from
  the list of states, and never copies the list of components the code holds (WAY-177).
  *Decision*: the product's decision adopting this template. *Invariant*: one an agent checks with
  k of n by reading the page of every state, or a script where the product's technology lets one
  decide it (WAY-188).
- **A fault of one screen is fixed in its component** — rule. A global design token carries a
  meaning for the whole product, so changing its meaning is a new or changed decision, while a
  change of its value that keeps its meaning is none; a fault of one screen is fixed in that
  screen's component, never by changing a global design token's value for that screen's sake
  (WAY-178, WAY-172). *Decision*: the product's decision adopting this template. *Invariant*: one
  an agent checks with k of n over the changes to the file of design tokens, judging whether a
  change alters what a role means or changes a global value for one screen's sake, or a script that
  every role on `{fork-point}` keeps its name and its kind (WAY-188).
- **Every value with its source** — rule. Each value of the file of design tokens carries beside it
  where it comes from; the styleguide names the source the skill chose with the human for this
  product, never a list of tools (WAY-182). *Decision*: the product's decision adopting this
  template. *Invariant*: a script the product declares (WAY-188).
- **The kitchen-sink page** — rule. It names by its path the page of the product that shows its
  shared components and samples in every state, served in development alone and never in
  production; the page is code of the product, not a piece of the styleguide's text (WAY-180).
  *Decision*: the product's decision adopting this template. *Invariant*: a script the product
  declares, that a production build does not serve the page (WAY-188).
- **Mockups** — example. A mockup is a pattern a screen is compared against, not its
  specification: the meanings on a screen come from the styleguide, and its values from the file of
  design tokens. No check can tell from a commit whether a mockup was read as a specification, so
  it carries no decision and no invariant (WAY-179).
- **Plan of a user-interface change** — example. The order of a plan for a change to a user
  interface: the environment and the library first, then the values in their source, then one
  screen, then its states. It is an example, never a rule (WAY-181).
- **`## Where in code`** — the paths of the file of design tokens, of the directory of shared
  components and of the page of every state, with no value copied from them (WAY-171, WAY-176,
  WAY-177, WAY-180).

## Pairs, meanings and role names

- **Pairs in code and in writing.** Which text role stands on which background is a rule, written
  in the decision of the roles and in the table of `## Roles`; the pair's values stand only in the
  file of design tokens (WAY-176, WAY-04).
- **Why the meanings stand twice.** A role's meaning stands in a decision of the product's log,
  where it is approved and weighed against the product's other choices; the table says the same
  meaning for the agent at work, and the fingerprint in *Decision* stops the merge of a change that
  rewords the decision until the table follows it (WAY-176, WAY-169). A decision holds one to three
  binding sentences (WAY-05), so the roles are grouped into several decisions — signal colours, a
  neutral scale, focus — each with its roles' meanings and pairs.
- **Translated meanings.** Where the product writes the text of its guidelines in another language
  than its decisions, which are in English, *Meaning for the user* and the text of each rule are
  translations of the decisions they restate (WAY-171). The fingerprint flags a reworded decision,
  never a drifted translation, and no check compares the two: a translation that drifts while its
  decision stands is caught only by a reader, by the review of the change that edits the table, or
  by the invariant of each role in its meaning, which judges the screens against the decisions, not
  against the table. A product that wants such a drift caught writes the text of its guidelines in
  English.
- **Role names.** A role's name avoids a word the glossary of the-way holds in another meaning —
  `surface`, `element`, `part`, `entry`, `result`, `verdict`, `gate` among them. Where the product's
  technology gives a role such a name, the code and the styleguide keep it, and the product's
  foundation writes it with a qualifier, as "the `surface` colour role" (WAY-176, WAY-104).

## Writing the file

For the author who writes the styleguide in a task's cycle:

- Take every meaning from the task's settlements and from the decisions the task's foundation step
  wrote (WAY-172).
- Take every value, and its source, from the task's *To do*, which names for each role the value
  and its source as the human settled them, or the exact address of the source and the item in it
  the value is read from; never from memory or from a mockup (WAY-182, WAY-179).
- Point to the values; write none into the styleguide (WAY-176, WAY-171).
- Write the test cases of each rule as the section "Test cases of a rule" of
  `product-guidelines/template.md` gives them (WAY-168). `### Every background with its text`, whose
  invariant is the product's copy of `guidelines-form`, carries none. Where the product cleans its
  screens as tasks touch their styles, the invariant of `### No value in place of a design token`
  that no file of the part holds such a value stands on the list of violated invariants: its cases
  are read against the commit's own result, while those of the invariant beside it that compares
  each file with `{fork-point}` take the strict reading (WAY-168, WAY-190).
- Run the form check. A meaning the task did not settle is a question that stops the cycle at a
  blocked draft request, never a row of `## Roles` (WAY-172).

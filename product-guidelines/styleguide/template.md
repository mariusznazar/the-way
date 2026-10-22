# Styleguide template

This file defines what the guidelines of the styleguide discipline add to the form every product's
guidelines share, `product-guidelines/template.md`, and what each section of a styleguide carries.
It is written for the author who writes a product's styleguide in a task's cycle. A product keeps a
styleguide for each of its user interfaces — its screens, an admin panel added to its backend
included — in a file `guidelines/styleguide-<part>.md`, `<part>` being the part of its map whose
files draw that user interface (WAY-167, WAY-183).

The rules this template carries bind a product only through a decision of the product's log adopting
them, and the product departs from any of them only by a decision of its log that gives the reason
(WAY-173). A rule below that a decision of the-way sets cites that decision. The rules of form
every file of guidelines keeps — the header lines, the fields of a rule, references, code in
backticks or fenced code, the language of the text, a dropped section or rule — stand in
`product-guidelines/template.md`; this template holds what is particular to a styleguide.

## Required form

The fenced block of this section gives the merged form of a styleguide, which the review of a
change that writes or changes one compares it with (WAY-170): the form of
`product-guidelines/template.md` with the section `## Roles` and the required rules and examples of
the styleguide in their places (WAY-171).

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
  template of guidelines gives a rule (WAY-171). Its *Invariant* names an invariant only where a
  cheap test of the product's suite checks the rule on a convention of the product's code — the
  items below name the three such invariants the skill proposes — and otherwise reads `none`, and
  the review of each change the rule reaches compares the change with it (WAY-168).
- Each required rule stands in the order above, or reads `none — <PREFIX-NN>`, naming the product's
  decision that drops it with its reason (WAY-171, WAY-173). The product's further rules follow the
  required ones.
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
  - *Decision*: the decision of the product's log that carries the role's meaning.

  The table holds no value: `## Where in code` points to the file of design tokens that holds them
  (WAY-176, WAY-171).
- **Each role in its meaning** — rule. A screen uses each role only in the meaning its decision
  gives, and a new or changed meaning is a new or changed decision, approved before the code that
  uses it (WAY-176, WAY-172). *Decision*: every decision the table of `## Roles` names. *Invariant*:
  `none` — the review of each change to the files of the part reads the roles it uses against their
  decisions (WAY-168, WAY-189).
- **Every background with its text** — rule. A role of the kind `background` is always written
  with the role of the kind `text` that stands on it in the table; the contrast rule holds the
  pair's values in code (WAY-176). *Decision*: the product's decision adopting this template.
  *Invariant*: `none` — the review of a change to the table reads each background with its text
  (WAY-168, WAY-170).
- **No value in place of a design token** — rule. The files of the user interface read colours,
  lengths and fonts from design tokens (WAY-189). *Decision*: the product's decision that defines
  what counts as a value written in place of a design token (WAY-60). *Invariant*: one whose test
  in the product's suite finds no such value in any file of the part; where the product cleans its
  screens as tasks touch their styles, it is marked violated until the cleaning ends, with no
  second invariant beside it (WAY-189, WAY-51).
- **Visible focus** — rule. Every control shows its focus with the style of the focus role
  (WAY-189). *Decision*: the product's decision adopting WCAG (WAY-191), and the product's decision
  that says which elements are controls and how the code marks them — a class, a component, an
  attribute (WAY-60). *Invariant*: one whose test in the product's suite finds that every control
  of the part, as that decision marks it, shows its focus, resting on the environment fact of
  WCAG's criterion of visible focus (WAY-189, WAY-191).
- **Contrast of every pair** — rule. Every pair of a background and the text on it reaches the
  contrast WCAG sets, computed from the values of the file of design tokens (WAY-189).
  *Decision*: the decisions of the roles and the decision adopting WCAG. *Invariant*: one whose
  test in the product's suite computes the contrast of every pair from the file of design tokens,
  resting on the environment fact of WCAG's criterion of contrast (WAY-189, WAY-191).
- **States of shared controls** — rule. It points by its path to the directory of the product's
  shared components, and every shared control has the states default, hover, visible focus,
  disabled, error, empty and loading, each shown on the page of every state or marked as not
  applying with its reason; it names a component by its path only where that component departs from
  the list of states, and never copies the list of components the code holds (WAY-177).
  *Decision*: the product's decision adopting this template. *Invariant*: `none`, unless the
  product's technology lets a cheap test decide it on a convention of its code (WAY-168).
- **A fault of one screen is fixed in its component** — rule. A global design token carries a
  meaning for the whole product, so changing its meaning is a new or changed decision, while a
  change of its value that keeps its meaning is none; a fault of one screen is fixed in that
  screen's component, never by changing a global design token's value for that screen's sake
  (WAY-178, WAY-172). *Decision*: the product's decision adopting this template. *Invariant*:
  `none` — the review of a change to the file of design tokens judges whether it alters what a role
  means or changes a global value for one screen's sake (WAY-168).
- **Every value with its source** — rule. Each value of the file of design tokens carries beside it
  where it comes from; the styleguide names the source the skill chose with the human for this
  product, never a list of tools (WAY-182). *Decision*: the product's decision adopting this
  template. *Invariant*: `none`, unless a cheap test decides it on a convention of the file of
  design tokens (WAY-168).
- **The kitchen-sink page** — rule. It names by its path the page of the product that shows its
  shared components and samples in every state, served in development alone and never in
  production; the page is code of the product, not a piece of the styleguide's text (WAY-180).
  *Decision*: the product's decision adopting this template. *Invariant*: `none`, unless a cheap
  test decides on a convention of the product's code that a production build does not serve the
  page (WAY-168).
- **Mockups** — example. A mockup is a pattern a screen is compared against, not its
  specification: the meanings on a screen come from the styleguide, and its values from the file of
  design tokens. No check can tell from a commit whether a mockup was read as a specification, so
  it carries no decision and no invariant.
- **Plan of a user-interface change** — example. The order of a plan for a change to a user
  interface: the environment and the library first, then the values in their source, then one
  screen, then its states. It is an example, never a rule (WAY-213).
- **`## Where in code`** — the paths of the file of design tokens, of the directory of shared
  components and of the page of every state, with no value copied from them (WAY-171, WAY-176,
  WAY-177, WAY-180).

## Pairs and meanings

- **Pairs in code and in writing.** Which text role stands on which background is a rule, written
  in the decision of the roles and in the table of `## Roles`; the pair's values stand only in the
  file of design tokens (WAY-176, WAY-225).
- **Why the meanings stand twice.** A role's meaning stands in a decision of the product's log,
  where it is approved and weighed against the product's other choices; the table says the same
  meaning for the agent at work, and a change that rewords the decision brings the table in line
  in the same change, its author finding the table by the decision's identifier (WAY-176,
  WAY-169). A decision holds one to three binding sentences (WAY-05), so the roles are grouped into
  several decisions — signal colours, a neutral scale, focus — each with its roles' meanings and
  pairs.
- **Translated meanings.** Where the product writes the text of its guidelines in another language
  than its decisions, which are in English, *Meaning for the user* and the text of each rule are
  translations of the decisions they restate (WAY-171). No check compares the two: a translation
  that drifts while its decision stands is caught only by a reader or by the review of a change
  that edits the table or the screens, which reads the roles against their decisions (WAY-168). A
  product that wants such a drift caught writes the text of its guidelines in English.

## Writing the file

For the author who writes the styleguide in a task's cycle:

- Take every meaning from the task's settlements and from the decisions the task's foundation step
  wrote (WAY-172).
- Take every value, and its source, from the task's *To do*, which names for each role the value
  and its source as the human settled them, or the exact address of the source and the item in it
  the value is read from; never from memory or from a mockup (WAY-182).
- Point to the values; write none into the styleguide (WAY-176, WAY-171).
- A meaning the task did not settle is a question that stops the cycle at a blocked draft request,
  never a row of `## Roles` (WAY-172).

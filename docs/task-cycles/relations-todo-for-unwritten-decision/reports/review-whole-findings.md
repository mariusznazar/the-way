# Findings of the review of the whole change (`reports/review-whole-report.md`, first line `FAIL 452f123d65de88143c91fe37b5633ecd341d88ee`)

Cut from the report in the reviewer's words. The blocking finding first, then the Minor findings within the task (M1-M3). M4 and M5 are marked by the reviewer outside the task's scope and are not fixed.

## Blocking

### Important

**I1 — A bare `TODO` in *Relations* that carries a relation type passes the check (within the task; blocking; comes from the one commit `452f123`, there is no plan).**

- Place: `elements/common/foundation_check.py:264` (`todo_item`) and `:573-577`
  (`check_foundation_references`, the new *Relations* branch); the claim it fails stands in
  `elements/decisions/template.md:75-76` and in WAY-71 `foundations/decisions.md:612`.
- What is wrong: `todo_item` finds a `TODO` item only where the piece of the value *begins* with
  `TODO`. In *Relations* every item naturally begins with its type, `derives from` or `narrows`, so
  the value `derives from TODO`, or `derives from WAY-01 · derives from TODO`, has no piece that
  begins with `TODO`: the script reads it as an ordinary relation, finds no decision number in it
  and reports nothing. A bare `TODO` stands in *Relations* and passes. With a description, `derives
  from TODO — <the decision>` also passes as a plain relation, and where the description holds a
  decision number, the script reports that number as a reference ("names no decision of the log"),
  which points the author at the wrong thing instead of at the form.
- Why it matters: To do 4 asks that a bare `TODO` in *Relations* be reported as an error with the
  hint of the form, and the template sentence this change writes says "The script reports a bare
  `TODO` in *Relations* ... as an error (WAY-71)". WAY-71's *Rejected* names the cost: "letting a
  bare `TODO` pass — the main branch would hold a gap that names no fact". *Rests on*, *Derives from*
  and *Based on* carry no type word before an item, so this gap is new with *Relations*; and the
  form an author is most likely to write by analogy with the other items of the field, `derives
  from TODO …`, is exactly the one that slips through. The files do not do what the entry they
  change requires (WAY-263), so the grade is Important. Before the change the same value also passed
  (the old check matched `TODO` only at the start of the value), but the old rule forbade `TODO` in
  *Relations* altogether, and this change is the one that invites the word into the field.
- Evidence: scratch run in a worktree of the head under `.runs/review-whole/head`, WAY-71's
  *Relations* line (`foundations/decisions.md:617`) replaced in turn, then
  `python -B elements/common/foundation_check.py`:
  - `- **Relations:** derives from WAY-01 · derives from TODO` → `0 errors`, exit 0;
  - `- **Relations:** derives from TODO` → `0 errors`, exit 0;
  - `- **Relations:** derives from WAY-01 · derives from TODO — WAY-9999, expected later` →
    `foundations/decisions.md:617: \`WAY-9999\` names no decision of the log`, 1 error.
  No test of `elements/common/test_foundation_check.py` holds a value with a type before `TODO`
  (`test_relations_a_bare_todo_names_no_decision` tries `TODO`, `` `TODO` ``, `TODO —`, `TODO — `,
  `derives from ABC-01 · TODO`, `derives from ABC-01 · `TODO``, `derives from ABC-01 · TODO —`).
  The author's own-work check (four values on the real log) did not try this form either.
- What a fix may do (not prescribed): in *Relations*, read a `TODO` that follows a relation type at
  the start of an item as the start of a `TODO` item too, and report it — bare, with the hint of the
  form, or with a description, with a message that the `TODO` item takes no type — with a test for
  each.

## Minor findings within the task

**M1 — WAY-126's new sentence says the `TODO` is replaced "with its identifier", which for *Relations* drops the relation type (within the task).**
`foundations/decisions.md:3736-3738`: "A change that writes a projected entry into the foundation
replaces with its identifier each descriptive `TODO` that points at it, in a decision's *Relations*
and in an invariant's *Derives from*." The complying example at `:3751-3753` says the same ("replaces
with its number the `TODO` that names it in the *Relations* of a decision"). In an invariant's
*Derives from* the identifier alone is the right value; in a decision's *Relations* an item is a type
and a number (`derives from WAY-NN`, template "Relations and precedence"), and the script checks no
type, so a literal reading would leave `WAY-NN` with no type and pass. The template's closed list and
its example `derives from WAY-01` steer most writers right, which keeps this Minor. Wording such as
"replaces each descriptive `TODO` that points at it with a reference to it by its identifier — in a
decision's *Relations* as `derives from <number>`" would close it.

**M2 — No test holds the check of a decision number on a continuation line of the known part of *Relations* (within the task).**
`elements/common/foundation_check.py:573-577` now skips every line of *Relations* in
`check_decision_numbers` (`relation_lines`) and checks the known part line by line through
`zip(lines, value.split("\n"))`. The only test of a wrong number in a known relation,
`test_decision_relation_that_does_not_exist` (`test_foundation_check.py:390`) and the new
`test_relations_a_decision_before_a_todo_is_still_checked` (`:748`), use a one-line value, so a
mutation that checks only the first line of the known part (for example `lines[:1]`) passes every
test. The behaviour is right today: my scratch run with `WAY-9999` on the second line of WAY-126's
*Relations*, `foundations/decisions.md:3744`, gave `foundations/decisions.md:3744: \`WAY-9999\` names
no decision of the log`, 1 error. Before the change the generic line check covered such lines, so the
protection the change removed from there has no test in the new place. One test with a value over
two lines and an unknown number on the second, with no `TODO`, would hold it.

**M3 — One docstring line runs past the width of the rest after the reflow (within the task).**
`elements/common/foundation_check.py:49`: "is an error (WAY-71). A `TODO` after a comma or a line
break instead of ` · ` begins such an item too: a bare" — about 111 characters, while the paragraph
around it wraps at 100. No blocking rule of the linter covers line length (`ruff.toml` selects no
`E501`), so this is style only.

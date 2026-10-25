# Slice 1 report — the template of the testing discipline

- **Status:** done
- **Files changed:** `product-guidelines/testing/template.md` (new, +259 −0)
- **Commits:** `083ab5d` Add the template of the testing discipline (author `mariusznn@gmail.com`),
  on `task/testing-guidelines` from slice base `57917c3`. Worktree clean afterwards (`.runs/` aside).

## Checks

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` — every decision number in the file names a live entry |
| `python -B gate/run_tests.py elements/common` | 0 | 109 tests, OK |
| `git grep -n "^### " -- product-guidelines/testing/template.md` | 0 | lines 44–52 list the nine required rules in D3's order, then `<further rules of the product>`, `<level>` (Recipes), `<example name>` |
| `git diff --check 4302f72 -- product-guidelines/` | 0 | prints nothing |

No test written: the slice is prose (the plan's *Checks*: "no test asserts the template"). Full gate
not run (the cycle's run).

## Own-work check

- Requirement most likely missed: "each rule and section cites the decision of the-way that sets
  it" together with "nothing of the Q14 cut list stands in the file".
- Check: an awk pass over "What each section carries" printing, for each top-level bullet, whether
  it holds a `WAY-<n>`; and `grep -n -i "red before|before the fix|proportion|percent|quarantin|snapshot"`.
- Showed: all 15 bullets cite a decision (the one `MISSING` line is the intro paragraph before the
  first bullet). The grep hits only "no proportion of levels" (twice, as a ban) and "snapshots and
  characterization tests included" (as part of "never from what the code gives today"); no "red
  before the fix", no quarantine, no command of a test tool. Decisions cited: WAY-05, 08, 16, 48, 51,
  167, 168, 170, 171, 172, 173, 226, 228, 231–243, 246.

## Reaches beyond the *Read*

- `elements/common/foundation_check.py:365-415, 470-515, 592-596` — to learn what the check reads in
  a template (decision numbers on every line; fields only in `guidelines/*.md`), so that I knew the
  fenced `<PREFIX-NN>` placeholders and field lines are not checked as references.
- `foundations/decisions.md` heading grep for WAY-05 (and the other cited numbers) — WAY-05 is not
  in the *Read*, but D3 cites it for grouping the permission decisions; I confirmed only that it
  exists (`### WAY-05 — How is a decision entry written?`, line 124), not its text.
- `git ls-files --eol product-guidelines/` and `.gitattributes` — line endings (LF).

## Choices within the spec

- **Table headers in the fenced form.** `## Levels` shows both tables' headers (`| Level | Decision |`,
  `| Part | Where its complexity lies |`) and `## Recipes` shows `### <level>` with the nine fields as
  `- **Field:**` lines, following the coding (`## Kinds of code`) and styleguide (`## Roles`)
  templates. Rejected: headings only. Cost if wrong: a few lines removed.
- **Labels.** Recipe fields: *Purpose*, *Files*, *Shape*, *Doubles*, *Data*, *Time and randomness*,
  *Exemplar*, *Command*, *Time limit*. Parts column: *Where its complexity lies*. Authorization table
  columns: *Who*, *Resource*, *Action*, *Expected result*, *Decision* (described in the rule's text,
  not in the fenced form, since the table stands inside a rule's how-to). Cost if wrong: renames.
- **How a binding recipe field names its decision:** the field's text ends with the identifier in
  parentheses, `(<PREFIX-NN>)`; a field with none is an example. The same parenthesis form is shown
  for an item of `## Not tested on purpose` (`- <category of behaviour or of code> (<PREFIX-NN>)`).
  Rejected: a trailing *Decision* field per recipe — doubles the fields. Cost if wrong: one sentence
  and the fenced line.
- **The plain `none` of `## Not tested on purpose` set apart** from the drop marker `none — <PREFIX-NN>`
  in one bullet of the required form, since both may stand in that section. Adds no meaning beyond
  WAY-171 and WAY-237.
- **Good/Bad:** the template proposes none of its own; the product writes them or `none` (sister
  templates give none either).
- **Yes/no table (research §1)** rendered in English as nine rows, two columns, source column dropped,
  "czerwony przed poprawką" dropped from the bug row. The four property-test questions stay in one
  row as in the research. I added one sentence after the lead-in: "It names levels by their meaning
  in the field; a product reads each as the level of its `## Levels` that has that meaning" — so
  that "unit", "integration", "end-to-end" in the table do not override a product's own level names
  (WAY-240). Cost if wrong: one sentence removed.
- **`## Examples`** cites WAY-168 only (what names no decision is an example); no decision of the-way
  sets the three kinds of valueless tests — WAY-237 names them only in its rationale.
- **No extra section** beyond the three D3 names (no analogue of the coding template's "The tools of
  the standing checks").

## Concerns

- `### Trust boundaries` cites WAY-48 for "stays with the review": WAY-235 says "the review of
  WAY-48"; I wrote "the review of each change that touches it (WAY-48, WAY-235)". A reviewer may
  prefer WAY-235's own words.
- The research table's rows "one end-to-end test for each such journey" and "a separate contract
  test" are carried over as the research gives them; neither is a proportion of levels, but they are
  the table's only counts.

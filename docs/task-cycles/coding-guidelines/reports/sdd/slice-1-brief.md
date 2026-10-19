### Slice 1 — The common template names the coding files and gives test cases

- **Goal:** `product-guidelines/template.md` gives, each rule citing the decision that sets it
  (WAY-171): "Where guidelines go" with `guidelines/coding.md` and `guidelines/coding-<kind>.md` and
  the general file's table of kind files as WAY-167 now gives them; *Good* and *Bad* that describe a
  use in one line, the field names and the fenced required form otherwise unchanged so the form
  check reads it as before; the rule on test cases of spec §5.1 citing WAY-168 — one
  `good <identifier> <path>` and one `bad <identifier> <path>` block per invariant the rule names
  other than `guidelines-form`, after the four fields, each the whole text of a file at a product
  path, the relative reading for a listed invariant and the strict reading for its per-file
  companion (C19), every fenced block of such a rule a test case, illustration under `## Examples`,
  short files at paths that may not exist, the path limits and the 1 MiB limit, the three-backtick
  outer fence and no fence-opening line inside, the bare-fence consequence (C21), the exemption of
  a rule whose *Invariant* is `guidelines-form` (C11), every discipline (C1); "A discipline's
  template may require an invariant in every rule" names coding beside the styleguide (WAY-196);
  the note on `check_instructions.py` says the cases' paths and texts stay in fenced code. No value.
- **Change:** `product-guidelines/template.md`
- **Read:** `docs/task-cycles/coding-guidelines/task-frozen.md`
  `docs/task-cycles/coding-guidelines/spec.md`
  `docs/task-cycles/coding-guidelines/reports/design-rulings.md`
  `product-guidelines/styleguide/template.md` · `instruction-files/check_instructions.py`
  `product-guidelines/form_check.py:262-433` · `foundations/glossary.md`
  `foundations/decisions.md:1440-1474` · `foundations/decisions.md:1745-1797`
  `foundations/decisions.md:1972-2006` · `foundations/decisions.md:5439-5715`
  `foundations/decisions.md:6286-6315` · `foundations/decisions.md:6352-6386`
  `foundations/decisions.md:6633-6713` · `foundations/decisions.md:6974-7015`
  `foundations/invariants.md:2133-2251`
- **Checks:** text, no behaviour; no test of its own. `python -B gate/run_tests.py product-guidelines`:
  the same tests pass and fail as after F4 (the required form still parses), compared by name;
  `python -B product-guidelines/form_check.py --record .runs/guidelines-form.jsonl` exits 0 with
  `pass` for `guidelines-form/1` on the-way. On a temporary git repository whose root `AGENTS.md`
  names in backticks a `guidelines/testing.md` holding one rule with a good/bad pair written as the
  template gives (info strings on opening fences, a path with `/`, an `@` inside a case),
  `python -B instruction-files/check_instructions.py <temporary repository>` reports no `error`, no
  dead path and no import — the check of the C12 assumption the design left unverified; output
  kept. `python -B gate/run_tests.py gate`. `git diff --check`. Manual, in the report: each bullet
  of spec §5.1 present; each rule names its decision; no glossary *Avoid* word.
- **Depends on:** F1a (WAY-167, WAY-168, WAY-196, WAY-197) · F1b (WAY-205) · F2 · F3
  (`guidelines-check-example-files`) · F4


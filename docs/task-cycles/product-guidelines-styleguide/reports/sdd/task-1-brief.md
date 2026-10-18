### Task 1 — The guidelines template and the styleguide template

- **Goal:** `product-guidelines/template.md` gives the common form of spec §3 — what it binds, the
  fenced skeleton the form check reads, the rules of writing (references, code in backticks or
  fenced code, language), the sentences of `guidelines-form` and `guidelines-reference-current`
  as given, not the product's to reword, with the-way's decisions they come from — and
  `product-guidelines/styleguide/template.md` gives the merged form of spec §4.1, what each part
  carries (§4.2, each rule with the decision and invariant the skill proposes, each example under
  `## Examples`), the pairs and translated-meanings notes, role names (WAY-176) and "Writing the
  file" for the cycle's author (§4.3). The required-rule headings are written verbatim as §4.1
  gives them — `### Each role in its meaning` exactly, since `guidelines-check-carrier` and the F4
  tests name it. Each rule cites the decision that sets it (WAY-171, C27); the rule "A fault of
  one screen is fixed in its component" follows WAY-178 with WAY-172's clause that a value kept
  with its meaning is no decision; no value is written.
- **Change:** `product-guidelines/template.md` · `product-guidelines/styleguide/template.md`
- **Read:** `.runs/task-cycles/product-guidelines-styleguide/task.md`
  `.runs/task-cycles/product-guidelines-styleguide/spec.md`
  `.runs/task-cycles/product-guidelines-styleguide/cycle.md:89-92`
  `elements/common/rules.md` · `elements/invariants/template.md` · `foundations/glossary.md`
  `foundations/part_map.md` · `instruction-files/check_instructions.py`
  `product-guidelines/test_form_check_invariants.py`
  `foundations/decisions.md:38-69` · `foundations/decisions.md:95-135`
  `foundations/decisions.md:234-315` · `foundations/decisions.md:543-573`
  `foundations/decisions.md:657-683` · `foundations/decisions.md:775-804`
  `foundations/decisions.md:995-1056` · `foundations/decisions.md:1525-1556`
  `foundations/decisions.md:1709-1743` · `foundations/decisions.md:2008-2070`
  `foundations/decisions.md:2454-2486` · `foundations/decisions.md:2550-2798`
  `foundations/decisions.md:2901-2953` · `foundations/decisions.md:3056-3085`
  `foundations/decisions.md:3833-4044` · `foundations/decisions.md:5439-6368`
  `foundations/invariants.md:2133-2212`
- **Checks:** text, no behaviour: no test of its own. After it, the F4 tests can reach the
  templates; `python -B gate/run_tests.py product-guidelines` still fails for want of
  `form_check.py` — recorded. On a temporary git repository whose root `AGENTS.md` names in
  backticks a `guidelines/styleguide-web.md` filled from the template (every required rule, a role
  table, a class with `/` in fenced code, a versioned package name), run
  `python -B instruction-files/check_instructions.py <temp repository>`: no `error`, no
  `dead-path`, no `at-import`; output kept. `python -B elements/part-map/format_guard.py foundations/part_map.md --base none`
  shows `product-guidelines/**` matching files. `git diff --check`. Manual check in the report:
  every `### ` of spec §4.1 present, verbatim and in order, matching the headings the F4 fixtures
  use; each rule names its decision; each part of §4.2 marked rule or example; no value, no
  package name, no glossary *Avoid* word.
- **Depends on:** F1 (WAY-167–WAY-192) · F2 (the term, the part) · F3 (the two sentences the
  template gives) · F4 (the headings its fixtures use)


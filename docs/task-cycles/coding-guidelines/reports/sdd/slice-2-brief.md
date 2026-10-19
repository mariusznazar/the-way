### Slice 2 — The coding template, and the form check reads its two forms

- **Goal:** `product-guidelines/coding/template.md` holds spec §4 — its opening (WAY-193, WAY-171),
  `## Required form` and `## Required form of a kind` with the fenced forms of §4.1 and §4.2, their
  headings, columns and the *Status* list verbatim as the F4 fixtures use them, the sentence "its
  *Invariant* names at least one invariant" in each form section, what each section carries
  (§4.3, with C3, C4, C5, C13, C14 and the standing checks' test cases of C12, C18, C19), the rules
  for the tools (§4.4) and "Writing the files" (§4.5), each rule citing its decision, no value, no
  tool named as the-way's choice. `product-guidelines/form_check.py` does items 1, 2 and 6 of spec
  §5.2: an optional second form per discipline; `<discipline>-<kind>.md` names agreeing with
  *Discipline* `coding` and the names §5.2 item 1 refuses; `requires_invariant` read from each form
  section; role checks only on a table whose columns are the roles', every other table checked for
  its header and number of cells; the coding template's structural words read back from it,
  `TemplateError` where one is missing; its docstring lists the new findings, each an error of
  `guidelines-form/1`; the command, options and exit codes unchanged. `product-guidelines/test_form_check.py`:
  the fixtures using `coding` as a discipline with no template (`:142-145`, `:264-277`, `:288`,
  `:364`) move to `observability`; ordinary tests of §5.3 bullets 2 and 3 and of the template words.
  The F4 coding tests of `guidelines-check-form/1` and `guidelines-check-carrier/1` pass.
- **Change:** `product-guidelines/coding/template.md` · `product-guidelines/form_check.py`
  `product-guidelines/test_form_check.py`
- **Read:** `docs/task-cycles/coding-guidelines/task-frozen.md`
  `docs/task-cycles/coding-guidelines/spec.md`
  `docs/task-cycles/coding-guidelines/reports/design-rulings.md`
  `docs/task-cycles/coding-guidelines/reports/f4-check.md`
  `product-guidelines/template.md` · `product-guidelines/styleguide/template.md`
  `product-guidelines/test_form_check_invariants.py` · `elements/common/guard_shared.py`
  `foundations/part_map.md` · `foundations/glossary.md`
  `foundations/decisions.md:492-517` · `foundations/decisions.md:1114-1142`
  `foundations/decisions.md:1370-1394` · `foundations/decisions.md:1440-1474`
  `foundations/decisions.md:1709-1828` · `foundations/decisions.md:1972-2006`
  `foundations/decisions.md:2072-2167` · `foundations/decisions.md:2454-2486`
  `foundations/decisions.md:4011-4044` · `foundations/decisions.md:4315-4352`
  `foundations/decisions.md:5439-5921` · `foundations/decisions.md:6286-6386`
  `foundations/decisions.md:6460-7262` · `foundations/invariants.md:547-575`
  `foundations/invariants.md:1497-1525` · `foundations/invariants.md:2133-2251`
- **Checks:** The F4 RED list, by test name, is in `docs/task-cycles/coding-guidelines/reports/f4-check.md`; *File* cells of `## Kinds of code` and `## Files of this kind` hold paths in backticks, as spec §4.3 gives and the F4 fixtures write them (C32). Then: start from the F4 coding tests of `guidelines-check-form/1` and
  `guidelines-check-carrier/1`, RED at F4, and from a failing ordinary test (a
  `guidelines/coding-endpoint.md` named by the second form is refused). Ordinary tests: kind names
  `coding-.md`, `coding--a.md`, `coding-A.md`, `coding-a/b.md` (warned, not read), `coding-a.md.md`,
  `Coding-a.md`; a table row with `|` inside backticks, too few or too many cells, a separator row
  in the middle, a header off by one space; `read_templates` on a temporary copy of the templates
  missing each structural word raises `TemplateError`, and the command exits 2; the moved
  `observability` fixtures pass as before. Run `python -B gate/run_tests.py product-guidelines`
  (the F4 tests of kind-index, exemplar and test cases still RED, by name);
  `python -B product-guidelines/form_check.py --record .runs/guidelines-form.jsonl` (exit 0, `pass`);
  `python -B product-guidelines/form_check.py --merge-onto none --record .runs/guidelines-reference.jsonl`
  (exit 0; merge `unchecked`); `python -B elements/part-map/format_guard.py foundations/part_map.md --base none`
  (`product-guidelines/coding/template.md` claimed by `product-guidelines`);
  `python -B gate/run_tests.py installation` after the commit (the styleguide installation test
  runs the form check of the committed `HEAD`; `NAMES` RED until S11); `python -B gate/run_tests.py gate`.
  WAY-48: the reviewer checks the crafted names and rows against §5.3 and that no new regular
  expression has nested repetition. Manual: every `### ` heading and column of §4.1–§4.2 verbatim.
- **Depends on:** Slice 1 · F1a (WAY-167, WAY-193, WAY-196, WAY-198–WAY-202) · F1b (WAY-203–WAY-208,
  WAY-211, WAY-212) · F2 · F3 (carrier, check-form) · F4


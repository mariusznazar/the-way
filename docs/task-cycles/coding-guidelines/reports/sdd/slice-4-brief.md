### Slice 4 — The form check: test cases, and a filled product end to end

- **Goal:** `product-guidelines/form_check.py` does item 5 of spec §5.2: in every kept rule whose
  *Invariant* names an invariant other than `guidelines-form`, one `good <identifier> <path>` and one
  `bad <identifier> <path>` block per such invariant after the fields, each path passing `refused()`;
  a block naming an invariant the rule does not name is an error; the info string read only from an
  opening fence; a line inside a case that would open a fence is an error at that line; any other
  fenced block of such a rule's body a malformed test case at its opening line, a case left open an
  error at its opening line (C21); a rule naming only `guidelines-form` needs no blocks; no case path
  opened, given to git or written; each finding an error of `guidelines-form/1`; docstring updated.
  The F4 tests of `guidelines-check-example-files/1` pass, and with them the whole
  `product-guidelines` run.
- **Change:** `product-guidelines/form_check.py` · `product-guidelines/test_form_check.py`
- **Read:** `docs/task-cycles/coding-guidelines/task-frozen.md`
  `docs/task-cycles/coding-guidelines/spec.md`
  `docs/task-cycles/coding-guidelines/reports/design-rulings.md`
  `docs/task-cycles/coding-guidelines/reports/f4-check.md`
  `product-guidelines/template.md` · `product-guidelines/test_form_check_invariants.py`
  `elements/common/guard_shared.py` · `instruction-files/check_instructions.py`
  `foundations/part_map.md` · `foundations/decisions.md:1114-1142`
  `foundations/decisions.md:1370-1394` · `foundations/decisions.md:1440-1474`
  `foundations/decisions.md:1745-1797` · `foundations/decisions.md:1972-2006`
  `foundations/decisions.md:5439-5715` · `foundations/decisions.md:6352-6386`
  `foundations/decisions.md:6674-6713` · `foundations/decisions.md:6974-7015`
  `foundations/invariants.md:547-575` · `foundations/invariants.md:2133-2251`
- **Checks:** The F4 RED list, by test name, is in `docs/task-cycles/coding-guidelines/reports/f4-check.md`; *File* cells of `## Kinds of code` and `## Files of this kind` hold paths in backticks, as spec §4.3 gives and the F4 fixtures write them (C32). Then: start from the F4 test-case tests, RED, and a failing ordinary test (a rule naming an
  invariant with no blocks passes). Ordinary tests of spec §5.3 bullets 4, 5 and 7 with the expected
  reports C21 gives: a fence left open to the end, a tilde fence, a fence of four backticks closing
  three, a fence-opening line inside a case, `good` with no identifier or path,
  `good x  a.ts b.ts`, `GOOD x a.ts`, a block naming an invariant the rule does not name, a rule
  naming two invariants with a pair for one only, a 1 MiB info string, an info string on a closing
  fence, a bare three-backtick line inside a `good` case (malformed case at the former closing
  fence), a rule naming `guidelines-form` with and without blocks and with another invariant, a
  test-case path refused as in S3, a file just over 1048576 bytes refused unread; no case path
  reaches git or is opened. End to end: on a temporary product with a part map, decisions (one
  designating an exemplar by path and kind) and invariants, a `guidelines/coding.md` and a
  `guidelines/coding-endpoint.md` filled from the coding template, with a pair per named invariant,
  pass `python -B <the-way>/product-guidelines/form_check.py --record …` and `--merge-onto none`,
  and `python -B instruction-files/check_instructions.py <product>` with a root `AGENTS.md` naming
  `guidelines/coding.md` reports no `error`, dead path or import; outputs kept. Run
  `python -B gate/run_tests.py product-guidelines` (all pass); both form-check runs on the-way;
  `python -B gate/run_tests.py gate`. WAY-48: the reviewer checks the inputs above.
- **Depends on:** Slice 3 · Slice 1 · F1a (WAY-168, WAY-197) · F1b (WAY-205) · F3
  (`guidelines-check-example-files`) · F4


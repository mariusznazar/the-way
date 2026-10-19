### Slice 3 — The form check: the index of kinds and the files of a kind

- **Goal:** `product-guidelines/form_check.py` does items 3 and 4 of spec §5.2: every
  `guidelines/coding-<kind>.md` git lists named by a row of `## Kinds of code` whose *File* is that
  path, every row naming a kind file git lists, a kind file with no `guidelines/coding.md` an error;
  in `## Files of this kind` exactly one `exemplar` row, every *Status* on the closed list, every
  *File* passing `refused()` and naming something git tracks (from the one list git gives), the
  exemplar row's *Decision* a decision of the log whose binding sentences hold `` `<path>` `` and
  `` `<kind>` `` after whitespace is collapsed, `—` on the other rows, its fingerprint checked as every
  reference is; no completeness asked (C13); `Foundation` keeps each decision's binding text; each
  finding an error of `guidelines-form/1`; docstring updated. The F4 tests of
  `guidelines-check-kind-index/1` and `guidelines-check-exemplar/1` pass.
- **Change:** `product-guidelines/form_check.py` · `product-guidelines/test_form_check.py`
- **Read:** `docs/task-cycles/coding-guidelines/task-frozen.md`
  `docs/task-cycles/coding-guidelines/spec.md`
  `docs/task-cycles/coding-guidelines/reports/design-rulings.md`
  `docs/task-cycles/coding-guidelines/reports/f4-check.md`
  `product-guidelines/template.md` · `product-guidelines/test_form_check_invariants.py`
  `elements/common/guard_shared.py` · `relation-model/fingerprint.py`
  `elements/decisions/format_guard.py:216-298` · `elements/decisions/format_guard.py:878-883`
  `foundations/decisions.md:38-69` · `foundations/decisions.md:1114-1142`
  `foundations/decisions.md:1370-1394` · `foundations/decisions.md:5439-5758`
  `foundations/decisions.md:6715-6815` · `foundations/decisions.md:7223-7262`
  `foundations/invariants.md:547-575` · `foundations/invariants.md:2133-2251`
- **Checks:** The F4 RED list, by test name, is in `docs/task-cycles/coding-guidelines/reports/f4-check.md`; *File* cells of `## Kinds of code` and `## Files of this kind` hold paths in backticks, as spec §4.3 gives and the F4 fixtures write them (C32). Then: start from the F4 tests of kind-index and exemplar, RED, and a failing ordinary test
  (a kind file missing from the index passes). Ordinary tests of spec §5.3: a *File* or index *File*
  absolute, UNC, holding `..`, `\`, `:`, a drive, a character not printable, a pathspec magic word,
  200 KiB long — refused before git sees it (the git calls captured), no socket opened, within a
  time bound; an index row differing from a file only by case or by a Unicode look-alike; two
  `exemplar` rows, none; a decision holding the path only outside backticks, `` `src/a.ts` `` where the
  row says `src/a.tsx`, a number with another log's prefix, a repealed decision; a line of 1 MiB of
  `|` or backticks. Run `python -B gate/run_tests.py product-guidelines` (test-case tests still RED,
  by name); both form-check runs of S2; `python -B gate/run_tests.py elements/decisions`,
  `relation-model`, `gate`. WAY-48: the reviewer checks those inputs and the bound on matching.
- **Depends on:** Slice 2 · F1a (WAY-167, WAY-198, WAY-199) · F1b (WAY-212) · F3 (kind-index,
  exemplar) · F4


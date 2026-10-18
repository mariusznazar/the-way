### Task 3 — The form check: references and the merge

- **Goal:** `product-guidelines/form_check.py` finds every reference of the two forms of spec §3.2
  outside fenced code (`~~~` fences included, C28 (4)), whatever its section, withdrawn
  identifiers counting (C28 (3)), and reports error 7 of §5.3 under
  `guidelines-reference-current/1` with the lines and fragments the F4 tests assert — malformed
  fingerprint, a decision absent or repealed, an invariant absent or withdrawn, a fingerprint
  other than the current one on the same commit and, with `--merge-onto`, after the merge
  (decisions from the decisions guard's merged log; an invariant as on the branch where its
  sentence differs from the fork point, else as on the onto commit) — computing every fingerprint
  through `relation-model/fingerprint.py`, borrowing the decisions and invariants guards' parsers
  with discarded reports, never offering to renew a fingerprint; `--merge-onto none` records the
  same-commit `pass` or `fail` and the merge `unchecked` with the shared reason; without the
  option the merge check does not run and a `note:` says so; the F4 tests of
  `guidelines-check-reference-target` and `-stale-reference` pass.
- **Change:** `product-guidelines/form_check.py` · `product-guidelines/test_form_check.py`
- **Read:** `.runs/task-cycles/product-guidelines-styleguide/task.md`
  `.runs/task-cycles/product-guidelines-styleguide/spec.md`
  `.runs/task-cycles/product-guidelines-styleguide/cycle.md:92-92`
  `.runs/task-cycles/product-guidelines-styleguide/reports/check-author.md`
  `product-guidelines/test_form_check_invariants.py` · `elements/common/guard_shared.py`
  `relation-model/fingerprint.py` · `elements/decisions/format_guard.py:1-300`
  `elements/decisions/format_guard.py:805-965` · `elements/invariants/format_guard.py:1-461`
  `elements/invariants/format_guard.py:1403-1525` · `gate/test_wording_reaches_dependants.py`
  `foundations/decisions.md:38-69` · `foundations/decisions.md:519-541`
  `foundations/decisions.md:575-633` · `foundations/decisions.md:903-962`
  `foundations/decisions.md:1619-1660` · `foundations/decisions.md:1907-1936`
  `foundations/decisions.md:1972-2006` · `foundations/decisions.md:2105-2138`
  `foundations/decisions.md:5529-5569` · `foundations/invariants.md:6-15`
  `foundations/invariants.md:507-516` · `foundations/invariants.md:587-596`
  `foundations/invariants.md:1357-1366` · `foundations/invariants.md:2143-2152`
  `foundations/invariants.md:2183-2202`
- **Checks:** start from the failing F4 reference tests and a failing ordinary test (a run with
  `--merge-onto` records `guidelines-reference-current/1` lines only). Ordinary tests:
  `react@18`, `tailwindcss@4`, `lucide-react@0` and a bare identifier in prose pass; a token in
  fenced code is ignored; a decision log whose copies conflict with the onto commit gives no
  `log-merge-copies` line and no exit 1; without `--merge-onto` a `note:`. Run
  `python -B gate/run_tests.py product-guidelines` (all pass);
  `python -B product-guidelines/form_check.py --merge-onto none --record .runs/guidelines-reference.jsonl`
  (exit 0; same-commit `pass`, merge `unchecked`);
  `python -B product-guidelines/form_check.py --record .runs/guidelines-form.jsonl` (still `pass`);
  `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none`;
  `python -B gate/run_tests.py elements/decisions`, `elements/invariants`, `relation-model`, `gate`.
  End to end: on a temporary product with a part map, decisions and invariants, a
  `guidelines/styleguide-web.md` filled from the template passes the form check, and after a
  decision it names is reworded fails it with both fingerprints in the message. WAY-48: the
  reviewer checks the reference pattern for runaway matching on the long-line input of S2.
- **Depends on:** Slice 2 · F3 (`guidelines-reference-current`, two `guidelines-check-*`) · F4 ·
  WAY-169


### Task 2 — The form check: form, carriers, parts and paths

- **Goal:** `product-guidelines/form_check.py` runs as spec §5.1 gives it — `ROOT`,
  `--merge-onto` (accepted and recorded as selecting the reference checks, which S3 adds),
  `--record`, exit codes 0/1/2, one report per guidelines file and one for the run — reads the
  templates from the-way checkout it lies in (C28 (1)), reads what §5.2 gives except the
  foundation's decisions and invariants, treats `~~~` fences as fenced code (C28 (4)), reports
  errors 1–6 and 5a of §5.3 under `guidelines-form/1` with the lines and message fragments the F4
  tests assert (C28 (2), (6)), holds the trust boundary of §5.4, cites
  `# invariant: guidelines-form/1` where it records it, loads the part-map guard's parser by path
  with a discarded report of its own, and passes the F4 tests of `guidelines-check-form`,
  `-carrier`, `-colour-pair` and `-code-path`; run on the-way (no `guidelines/`) it records `pass`
  for `guidelines-form/1`.
- **Change:** `product-guidelines/form_check.py` · `product-guidelines/test_form_check.py`
- **Read:** `.runs/task-cycles/product-guidelines-styleguide/task.md`
  `.runs/task-cycles/product-guidelines-styleguide/spec.md`
  `.runs/task-cycles/product-guidelines-styleguide/cycle.md:92-92`
  `.runs/task-cycles/product-guidelines-styleguide/reports/check-author.md`
  `product-guidelines/test_form_check_invariants.py` · `foundations/part_map.md`
  `elements/common/guard_shared.py` · `elements/part-map/format_guard.py:1-330`
  `elements/part-map/format_guard.py:704-777` · `elements/invariants/format_guard.py:1122-1191`
  `elements/decisions/format_guard.py:1-80` · `instruction-files/check_instructions.py`
  `gate/run_tests.py:1-80` · `foundations/decisions.md:38-69` · `foundations/decisions.md:95-135`
  `foundations/decisions.md:1114-1142` · `foundations/decisions.md:1370-1438`
  `foundations/decisions.md:1745-1936` · `foundations/decisions.md:1972-2006`
  `foundations/decisions.md:2105-2138` · `foundations/decisions.md:2488-2515`
  `foundations/decisions.md:5487-5527` · `foundations/decisions.md:5571-5655`
  `foundations/decisions.md:5835-5873` · `foundations/decisions.md:6227-6296`
  `foundations/invariants.md:547-576` · `foundations/invariants.md:877-886`
  `foundations/invariants.md:1317-1326` · `foundations/invariants.md:1497-1516`
  `foundations/invariants.md:2133-2142` · `foundations/invariants.md:2153-2182`
  `foundations/invariants.md:2203-2212`
- **Checks:** start from the F4 tests, failing without the script (recorded), and from a failing
  ordinary test in `product-guidelines/test_form_check.py` (a repository with no `guidelines/`
  exits 0 with a `note:`). Ordinary tests cover what no invariant's sentence holds: records with no
  option (`guidelines-form/1` lines only), findings of two files under their own paths, `warning:`
  for `guidelines/styleguide/web.md` and `guidelines/x.MD`, the trust boundary (a symlink —
  skipped where the platform cannot create one — a directory `x.md`, `guidelines` as a file,
  non-UTF-8 bytes, a file over 1 MiB refused unread, a file just under 1 MiB of one line of
  backticks, `@` and hex runs finished within a bound, the git subprocess calls captured to show
  no refused path reaches git, a patched `socket` failing if called), a non-`.jsonl` record path
  exiting 2, and each report's count line. The report states what a no-option run does on a
  reference error (C28 (5)). Run `python -B gate/run_tests.py product-guidelines` (the F4
  reference tests still fail until S3 — recorded);
  `python -B product-guidelines/form_check.py --record .runs/guidelines-form.jsonl` (exit 0,
  `pass` for `guidelines-form/1`);
  `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none`
  (no `invariant-citation-target` error); `python -B elements/part-map/format_guard.py foundations/part_map.md --base none`
  (trust boundary and surface name existing items); `python -B gate/run_tests.py gate`. WAY-48:
  the reviewer checks the crafted inputs above against §5.4.
- **Depends on:** Slice 1 · F3 (`guidelines-form`, four `guidelines-check-*`) · F4 · WAY-168,
  WAY-170, WAY-171, WAY-176, WAY-188, WAY-189 · F2 (part, trust boundary, surface)


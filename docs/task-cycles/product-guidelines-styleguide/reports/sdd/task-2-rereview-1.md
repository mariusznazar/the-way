# Task 2 re-review — fix round 1

- **Fix range:** `2e5d038..d79f692` — `8d97ab9` (the author of the F4 tests: new code-path cases in
  `product-guidelines/test_form_check_invariants.py`) and `d79f692` (the executor), read from
  `.superpowers/sdd/plan-tasks/review-2e5d038..d79f692.diff`, with the "Fix round 1" section of
  `task-2-report.md`.
- **Runs:** a detached worktree `C:/Storage/repos/the-way-wt/pg-review-s2r` at `d79f692`, removed
  after the review; the main checkout was not touched.
- Line numbers are of the files at `d79f692`.

## Finding Verdicts

### I1 — the styleguide check can be bypassed (5a): ADDRESSED

**Anchor:** `product-guidelines/form_check.py:583-589` (the new loop in `check_parts`),
`product-guidelines/form_check.py:664` (the call now passes `disciplines`); test
`product-guidelines/test_form_check.py:253-264` (`Names`).

Before the name test accepts `<discipline>.md` or `<discipline>-<part>.md`, `check_parts` now
checks every discipline the-way gives a template of. A file whose stem is `<t>` or `<t>-…` while
*Discipline* is not `t` is reported and the check returns. I re-ran my own probe of the first
review: `guidelines/styleguide-web.md`, written in the common form with *Discipline*
`styleguide-web`, against the script at `d79f692`. It now exits 1 with
`guidelines/styleguide-web.md:0: error: the file's name is one of guidelines of the discipline
`styleguide`, whose template the-way gives, but its *Discipline* reads `styleguide-web`; it would be
held to the wrong form`. (It exited 0 at `2e5d038`; see `slice-2-review-probes.txt`.) The new
ordinary test went red before the fix (`slice-2-fix1-red.txt`, per the report). Its assertion
needs both `styleguide-web` and `Discipline` in an error message under the file's path, so the
old "does not agree" message could not satisfy it by accident: that message never named the
stem's discipline.

### I2 — the absolute-path guard has no test: ADDRESSED

**Anchor:** guard `product-guidelines/form_check.py:611-612`; tests
`product-guidelines/test_form_check.py:267-283` (`Paths`) and
`product-guidelines/test_form_check_invariants.py:718-747`
(`CodePath.test_a_path_out_of_the_repository_is_reported_though_its_remainder_is_tracked`, with
the citation `# invariant: guidelines-check-code-path/1`).

Both new tests use paths whose remainder git tracks (`/src/tokens.css`, `/tests/fixtures.py`,
`./../tests/fixtures.py`, `src/components/../tokens.css`, drive and UNC forms). So the refusal
alone decides the error, and the F4 test first proves that each remainder passes. I repeated
the deliberate break (below): removing the `/` refusal now fails both tests and raises the
invariant's `fail` count. No code change was needed; the report says so, correctly.

## New Breakage in the Fix Diff

None that bites today. One thing to watch:

- **A prefix shared by two disciplines with templates** (`form_check.py:583-584`). The test is
  `stem.startswith(other + "-")` over every discipline the-way gives a template of. If the-way
  ever held templates for both `a` and `a-b`, a correct `guidelines/a-b-web.md` with *Discipline*
  `a-b` would be reported as a file of `a`. Today `styleguide` is the only discipline with a
  template, so this cannot happen. If a second template ever shares a prefix, skip `other` when
  `discipline` itself starts with `other + "-"` and has a template (`discipline in
  disciplines`). Minor, latent; no action needed for this task.

The rest of the fix diff is sound:
- The early `return` (`form_check.py:589`) skips only the part-in-name check, and a file that
  reaches it already carries an error.
- The message prints *Discipline* through `shown()` and the template name as it stands, which is
  the-way's own text.
- `PRODUCT_ROOT` in the F4 harness (`test_form_check_invariants.py:33`, `:283-284`) changes only
  text that holds the placeholder, and no older fixture holds it.

## Out-of-Scope Observations

- `Paths` (`test_form_check.py:274`) repeats the `self.setUp()`-inside-a-subtest-loop pattern of
  the first review's Minor 6 (now also at `test_form_check.py:396`). It works; if Minor 6 is
  fixed, this second occurrence should be fixed with it.
- The first review's Minor items 3–5 and 7 (the part-map template error exiting 1, the refusal of
  every `:` and `\`, the quadratic de-duplication, missing sections at line 0) are not in this
  round's scope. Nothing in the fix diff changes them.

## Deliberate break repeated

| Invariant | Break | Command (cwd the worktree at `d79f692`) | Exit | Detected | Output |
|---|---|---|---|---|---|
| `guidelines-check-code-path/1` | `refused`: the two lines refusing a path that starts with `/` removed (`form_check.py:611-612`), the same removal as in the first review | `python -B gate/run_tests.py product-guidelines --record <scratch>/break2.jsonl` | 1 | **yes**: the invariant's record went from fail 1 / pass 3 (unbroken baseline at `d79f692`, `FAILED (failures=93)`, the expected S3 reds) to fail 2 / pass 2. Newly failing: F4 `CodePath.test_a_path_out_of_the_repository_is_reported_though_its_remainder_is_tracked` and ordinary `Paths.test_a_path_refused_for_its_form_whose_remainder_git_tracks_is_an_error` | `.runs/task-cycles/product-guidelines-styleguide/reports/slice-2-break-guidelines-check-code-path-2.txt` |

`form_check.py` was restored and compared byte for byte (`True`), and the worktree showed no change
before it was removed.

## Verdict

**I1 ADDRESSED, I2 ADDRESSED; no new breakage in the fix diff (one latent prefix collision noted,
Minor). Task quality: Approved** — the two Important findings of the first review are closed, and
the break that went undetected is now caught. Minor items 3–7 of the first review stay open as
Minor, as they were.

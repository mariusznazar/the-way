# Slice 2 task review (spec + quality): coding template and the form check's two forms

Reviewer: task reviewer (opus), Superpowers 6.4.1 task-reviewer template + cycle contract.
Diff: `18317a8..334ef34` (`slice-2-review-package.diff`), read once in full in three passes (template, form_check.py, tests).

### Spec Compliance

- ✅ Spec compliant. Every brief item is in the diff: the template (spec §4.1–§4.5, C3, C4, C5, C12, C13, C14, C18, C19), and form_check.py §5.2 items 1, 2 and 6. Items 3–5 are left for S3/S4 as planned.
  - Checked: both fenced blocks equal spec §4.1/§4.2 byte for byte. I recomputed this myself: `re.findall` on the spec and on `product-guidelines/coding/template.md` gives `True`.
  - Checked: the sentence "its *Invariant* names at least one invariant" stands in each form section (`coding/template.md:52-56`, `:99-102`).
  - Checked: no tool name in the template. Grep for 20 linter, formatter and audit names returned nothing; 63 `WAY-` citations.
  - Checked: no line over 100 characters.
- ✅ form_check.py:
  - Item 1: `discipline_form` (`form_check.py:375`) and `of_a_kind`; `check_parts` (`:943`, `:984`); kind-form selection in `check_file` (`:1118`).
  - Item 2: `check_tables` (`:852`), `read_roles` on a *Role* column (`:393`), `read_coding_words` (`:417`).
  - Item 6: `requires_invariant` is read for each section separately in `discipline_form`.
  - The docstring lists the new findings as errors of `guidelines-form`, plus the new exit-2 cause. `PROGRAM`, the options and the codes are unchanged.
- ✅ Tests:
  - The fixtures moved to `observability` (`test_form_check.py:142-145` and four uses). No `as_coding` or no-template coding fixture is left (grep).
  - Every ordinary test the brief names is present: kind names (`Coding`, `:425`), rows and headers (`Tables`, `:465`), template words with exit 2 (`TemplateWords`, `:566`).
- ⚠️ Cannot verify from the diff alone:
  1. **End-state statement.** The template states what the product's copy of `guidelines-form` carries (kind index, exemplar, test cases; `coding/template.md:192-198`, C14). The form check does that only after S3/S4. Carry this to S3/S4 review: each named check must land.
  2. **Python version.** The harness runs Python 3.13.16; the repository declares 3.14. Not run on 3.14.
  3. **The 3 Minor items carried from S1** (template promises for S4) are unaffected by this slice and stay with S4.

### Deliberate breaks (cycle addition)

I did not write these checks. Each break makes the invariant's sentence false in a scratch worktree at `334ef34` under the scratchpad (`git worktree add`, then removed and pruned).

Command for each: `python3 -B gate/run_tests.py product-guidelines --record <scratch>.jsonl`, exit 1 each time. I compared the failures by name with the executor's GREEN run (`slice-2-product-guidelines.txt`).

| Break | Sentence made false | Newly failing test citing the invariant | Record | Output |
|---|---|---|---|---|
| **form-select:** `check_file` selects the kind form on `startswith("coding")` without the hyphen, so `coding.md` is held to the kind form | `guidelines-check-form/1`: a required rule (standing check) that a file lacks or holds out of order is reported | `CodingForm.test_a_missing_or_misplaced_standing_check_rule_is_reported`, all 4 subtests; also `CodingFixtures`, `CodingForm.test_a_general_file_with_no_kinds_of_code…`, `…dropped_by_a_departing_decision_passes` | `fail` for `guidelines-check-form/1` (and carrier, via fixtures) | `slice-2-break-form-select.txt` |
| **form-name:** `check_parts` accepts `rest is not None` with no `IDENTIFIER.fullmatch` | `guidelines-check-form/1`: every file whose name and *Discipline* disagree | `CodingForm.test_a_coding_file_whose_name_and_discipline_disagree_is_reported` (`coding-.md`, `coding-Endpoint.md`, `coding--x.md`); the ordinary `Coding.test_a_name_whose_kind_is_no_identifier_is_an_error` also fails | `fail` for `guidelines-check-form/1` | `slice-2-break-form-name.txt` |
| **carrier-kind:** `of_a_kind` built by `parse_form` alone, so `requires_invariant` stays False | `guidelines-check-carrier/1`: a rule naming no invariant where the discipline's template requires one (file of a kind) | `CodingCarrier.test_a_coding_rule_naming_no_invariant_is_reported` [a rule of a kind] | `fail` for `guidelines-check-carrier/1` | `slice-2-break-carrier-kind.txt` |
| **carrier-general:** `form.requires_invariant = False` for coding after reading the words | the same sentence, for the general file | `CodingCarrier.test_a_coding_rule_naming_no_invariant_is_reported`, 3 general-file subtests; also `TemplateWords.test_each_form…` | `fail` for `guidelines-check-carrier/1` | `slice-2-break-carrier-general.txt` |

The tests caught every break. No other test changed result. The S3/S4 RED set is the same as the executor's.

### Weakest point and sharpness (WAY-164, WAY-48)

- **Weakest-point finding** (`slice-2-weakest.txt`): every rule cites a decision; no tool, no value. I agree.
  - The 13 uncited units are sub-items of a citing bullet, or section introductions, as in the styleguide template.
  - The only numerals are the ordered-list markers.
- **Sharpness inputs** are confirmed from the diff:
  - Parts touched: `product-guidelines` only.
  - Trust-boundary file: `form_check.py`; `installation/install.py` is untouched.
  - No irreversible operation.
- **WAY-48 regular expressions.**
  - The only new pattern, `\*Status\*: one of (.*?);`, reads the-way's own template (`form_check.py:417-433`).
  - Kind names reuse the existing, anchored `IDENTIFIER.fullmatch` (`:152`, `:984`). Its inner `+` within `*` is separated by a literal `-`, so matching is unambiguous and linear. It is not new.
  - Rows are split with `str.split`.
- **WAY-48 crafted input** is checked against spec §5.3 bullets 2 and 3:
  - Covered here: `coding-.md`, `coding--a.md`, `coding-A.md`, `coding-a.md.md`, `Coding-a.md` (errors), and `coding-a/b.md` (warned, not read).
  - Covered here: `|` in backticks, too few cells, too many, `||`, a separator in the middle, three off-by-one-space headers with a padded control, and a 1 MiB row of bars finishing in under 30 s.
  - Left to S3, whose brief lists them (`slice-3-brief.md:29`): a name differing by case or by a Unicode look-alike, and two `exemplar` rows or none.

### Executor's concerns, judged

1. **Stricter separator row, also for styleguides.** This is sound. In GitHub-flavoured Markdown, a header with no delimiter row is no table, and a dash row among the rows is no separator. Spec §5.3 lists "a separator row in the middle" as crafted input. Valid styleguide fixtures still pass (`Fixtures`, `ColourPair`). Not a finding; see Minor 1 for the tests.
2. **The template describes the end state.** Spec §4.3 (C14) requires that statement. Not a finding; carried as ⚠️ 1.
3. **WAY-207 and WAY-200 citations.**
   - WAY-207 is the decision that turning a rule off is a change of the adopting decision. Spec §4.3 cites WAY-207 for invariant 2, including C4, so the citation follows the spec.
   - WAY-200's audit judges every file with its status. It is the decision behind the C13 sentence, since rulings are not decisions (WAY-171 asks for a decision).
   - Not findings.
4. **Check renamed `check_tables`.** No consumer of the check name exists: I grepped `gate/`, `installation/` and the repository's `.py` files for `check_roles` and `check_tables` outside `form_check.py`, and found no hits beyond an unrelated fixture string. Not a finding.

### Strengths

- **The template.** It follows spec §4 closely and cites throughout, including C3, C4, C5, C12/C18/C19 and C14. Both forms are verbatim, and its §4.4 and §4.5 text is complete.
- **Clean decomposition** in `form_check.py`:
  - `discipline_form` removes the earlier inline duplication and serves both forms.
  - `read_roles` keeps the old fail-safety: I probed a copy of the styleguide template with *Role* renamed, and with *Kind* renamed. Each raised `TemplateError`.
  - `check_tables` and `check_roles` separate the generic table checks from the styleguide's own.
- **The coding fixtures** are built to stay valid through S3/S4 (index row, exemplar decision, good/bad pair). Helpers `line_of` and `replaced` assert a single occurrence, so a fixture edit cannot silently miss.
- **TemplateWords.**
  - It tests each structural word.
  - It asserts that the command exits 2, pinned by the message so that a failed borrow cannot pass it.
  - It tests that each form reads its own demand for an invariant.
- **The evidence** is complete and legible:
  - RED ordinary run (`slice-2-red-ordinary.txt`).
  - GREEN run in which only the named S3/S4 tests fail, with matching jsonl verdicts.
  - Form check `pass` and `unchecked`.
  - Part-map guard exit 0.
  - Installation: only the 4 `NAMES` tests fail (C24).
  - Gate: 98 OK.
  - No warnings or noise in the outputs.

### Issues

#### Critical (Must Fix)

None.

#### Important (Should Fix)

None.

#### Minor (Nice to Have)

1. **Two new error branches of `check_tables` are untested** (`form_check.py:876-878`, `:888-890`):
   - a header with no row after it at all;
   - a header followed directly by a data row.

   `test_a_separator_row_among_the_rows_is_an_error` (`test_form_check.py:502`) covers only the middle-separator branch. Removing either branch would fail no test. Fix: two more cases in `Tables`.
2. **The docstring says a row is split "as Markdown reads a row"** (`form_check.py:845-849`, docstring at `:42-43`), but `table_cells` also splits on an escaped `\|`. GitHub-flavoured Markdown reads `\|` as a literal bar, even in a code span. A product writing `` `a\|b` `` in a cell therefore gets a false "wrong number of cells" error.
   - This fails safe, and the splitting predates this slice. The slice's new claim is what overstates it.
   - Fix: narrow the wording to unescaped bars, or treat `\|` as a literal. If the code changes, add a test.
3. **The C13 sentence leaves out "the form check asks no completeness"** (`coding/template.md:178-180`). Spec §4.3 states it. "Takes no row until the guidelines are refreshed or extended" implies it, but a product author reading only the template could expect the form check to demand rows.
4. **The `read_roles` restructuring has no ordinary test** (`form_check.py:393-414`). Its new `TemplateError` ("requires the rule … but gives no table of roles") and the column demand on a styleguide template copy are untested. I probed both by hand (see Strengths); a test in the style of `TemplateWords` would pin them.
5. **Docstring reflow left a ragged short line**: "tracks. A decision is named by a number" (`form_check.py:52`). Cosmetic.
6. **Weak message assertions in `TemplateWords`** (`test_form_check.py:597-618`). The assertions for the words `Kind` and `File` are always true, because the error message names `Kinds of code` or `Files of this kind`. The `assertRaises` still detects a dropped column check, so this is only a weak assertion.

### Assessment

**Task quality:** Approved

**Reasoning:** The template matches spec §4 verbatim where required and cites a decision for every rule. The form check adds the two forms, per-form invariant demand, generic table checks and template words with a clean decomposition, and leaves the command surface unchanged. All four deliberate breaks of `guidelines-check-form/1` and `guidelines-check-carrier/1` were caught by tests citing them. The remaining items are Minor: coverage and wording.

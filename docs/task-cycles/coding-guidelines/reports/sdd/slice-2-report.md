# Slice 2 report: the coding template, and the form check reads its two forms

**Status:** DONE_WITH_CONCERNS. **Commit:** `334ef34` on `claude/gallant-albattani-3k15lc`
(parent `18317a8`), not pushed. **Python:** 3.13.16 (`python3`); the repository declares 3.14.

## What I implemented

- **`product-guidelines/coding/template.md`** (new). It covers spec §4:
  - **Opening:** the two files (WAY-167), binding only through an adopting decision (WAY-193),
    each rule citing its decision (WAY-171), and the common rules standing in
    `product-guidelines/template.md`.
  - **`## Required form`:** the §4.1 block, byte for byte. Below it, each rule's fields with the
    sentence "its *Invariant* names at least one invariant …" (WAY-171, WAY-196); the standing
    checks in order or dropped by `none —` (WAY-202); the example rule (WAY-196); *Applies to*
    (WAY-208); *When to read* (WAY-212); `## Kinds of code` (WAY-167, WAY-212).
  - **`## Required form of a kind`:** the §4.2 block, byte for byte, with the same sentence and the
    `<kind>` identifier (WAY-167).
  - **`## What each section carries`** (§4.3), including:
    - C3: suppressions count as breaks;
    - C4: both ways of keeping the blocking list;
    - C5: the *Part* of each standing-check invariant;
    - C13: no row needed for a later file;
    - C14: what the product's copy of `guidelines-form` carries;
    - C12, C18, C19: the standing checks' test cases.
  - **`## The tools of the standing checks`** (§4.4) and **`## Writing the files`** (§4.5).
  - It names no tool and holds no value.
- **`product-guidelines/form_check.py`** (spec §5.2 items 1, 2, 6):
  - **Two forms (item 1).** `read_templates` reads an optional `## Required form of a kind` into
    `Form.of_a_kind`, using `discipline_form`, shared by both forms. `check_file` holds a file
    `<discipline>-…` of such a discipline to the kind form. `check_parts` accepts
    `<discipline>-<kind>.md` when `<kind>` fully matches the existing `IDENTIFIER`. Any other name
    gets an error naming `guidelines/coding.md` and `guidelines/coding-<kind>.md`.
  - **Invariant demand (item 6).** `requires_invariant` is read from each form's own section.
  - **Tables (item 2).**
    - `read_roles`: a table of roles is one with a *Role* column. It must have its columns, the
      *Kind* list and the rule `Each role in its meaning`. A template that requires that rule but
      gives no table of roles raises `TemplateError`.
    - New `check_tables` runs on every table the template gives. It reports: a section with no
      table; a header that is not the columns; no separator row right under the header; a
      separator row anywhere else; a row whose cell count differs from the columns.
    - `check_roles` now reads `check_tables`' rows for the role tables only.
    - `table_cells` takes off one bar at each end, not every bar.
  - **Template words.** `read_coding_words` reads back from the coding template the kind form,
    `Kinds of code`, `Files of this kind`, their columns (`Kind`/`File`/`When to read`,
    `File`/`Status`/`Decision`) and the *Status* list (`exemplar`, `copy`, `do not copy`).
    Any missing word raises `TemplateError`, and the command exits 2.
  - The docstring lists the new findings, all errors of `guidelines-form/1`, and the new exit-2
    cause. `PROGRAM`, the command, its options and exit codes are unchanged.
- **`product-guidelines/test_form_check.py`:**
  - `as_coding` becomes `as_observability`, and the four uses (`:264`, `:274/278`, `:288`, `:364`)
    now use `guidelines/observability.md`.
  - New coding fixtures: a general file and `coding-endpoint.md`, with decision ABC-06 (`a7f9c135`)
    and invariant `endpoint-handler` (`8c2ca199`). They are written to stay valid through S3/S4:
    there is an index row, an exemplar row whose decision names the path and the kind in
    backticks, and a good/bad pair.
  - New classes: `Coding` (3 tests), `Tables` (6) and `TemplateWords` (3).

## TDD evidence

- **RED, ordinary tests.** Command:
  `python3 -B -m unittest test_form_check.Coding test_form_check.Tables test_form_check.TemplateWords test_form_check.Runs test_form_check.References`
  run from `product-guidelines/`. Result: 28 tests, 20 failures and 3 errors; the moved
  `observability` tests (Runs, References) passed. Output: `slice-2-red-ordinary.txt`.
  - Every Coding/Tables failure has one cause: the error
    `guidelines/coding-endpoint.md:0: error: the file's name does not agree with its *Discipline* `coding``,
    or no table error being reported.
  - The 3 TemplateWords errors are `FileNotFoundError`, because there was no coding template yet.
- **RED, F4.** At `18317a8` all 23 F4 tests were red (`slice-2-baseline-product-guidelines.txt`,
  `.jsonl`; exit 1, 88 tests, 89 failures).
- **GREEN.** `python3 -B gate/run_tests.py product-guidelines --record …/slice-2-product-guidelines.jsonl`
  at `334ef34` exits 1 (100 tests, 76 failing subtests). All 47 tests of `test_form_check.py` pass.
  The only failures are the S3/S4 tests listed below.

## Checks run

All outputs are in `docs/task-cycles/coding-guidelines/reports/sdd/`.

| Check | Exit | Result | Output |
|---|---|---|---|
| `python3 -B gate/run_tests.py product-guidelines --record …` | 1 | expected: only the S3/S4 tests below fail; `guidelines-check-form/1` and `guidelines-check-carrier/1` record only `pass` | `slice-2-product-guidelines.txt`, `.jsonl`, `.exit` |
| `python3 -B product-guidelines/form_check.py --record .runs/guidelines-form.jsonl` | 0 | `pass` | `slice-2-form-check.txt` |
| `python3 -B product-guidelines/form_check.py --merge-onto none --record .runs/guidelines-reference.jsonl` | 0 | merge check `unchecked`, same-commit check `pass` | `slice-2-form-check-reference.txt` |
| `python3 -B elements/part-map/format_guard.py foundations/part_map.md --base none` | 0 | 0 errors, so no file is unclaimed; `product-guidelines/coding/template.md` is tracked, and `product-guidelines/**` is the only pattern that claims it | `slice-2-part-map-guard.txt` |
| `python3 -B gate/run_tests.py installation --record …` (after the commit) | 1 | expected: only the 4 `NAMES` tests fail (RED until S11, C24); `test_styleguide_installation` passes, form check of `HEAD` included | `slice-2-installation.txt`, `.jsonl`, `.exit` |
| `python3 -B gate/run_tests.py gate --record …` | 0 | 98 tests OK | `slice-2-gate.txt`, `.jsonl`, `.exit` |
| Manual: every heading and column of §4.1–§4.2 verbatim | — | both blocks equal spec §4.1/§4.2 byte for byte; the headings, columns, *Status* values and backticked *File* cells match the F4 fixtures | `slice-2-manual-verbatim.txt` |
| Weakest point (below) | — | holds | `slice-2-weakest.txt` |

### Still RED, by name

These belong to S3 and S4.

- **Kind index (S3):**
  - `KindIndex.test_a_kind_file_no_row_names_is_reported`
  - `KindIndex.test_a_row_naming_no_file_git_lists_is_reported`
  - `KindIndex.test_a_row_whose_kind_is_not_its_files_kind_is_reported`
  - `KindIndex.test_a_row_whose_when_to_read_is_empty_is_reported`
  - `KindIndex.test_a_kind_file_with_no_general_file_is_reported`
- **Exemplar (S3):**
  - `Exemplar.test_a_kind_file_with_no_exemplar_row_or_more_than_one_is_reported`
  - `Exemplar.test_a_row_whose_status_is_off_the_list_is_reported`
  - `Exemplar.test_a_row_whose_file_is_out_of_the_repository_or_untracked_is_reported`
  - `Exemplar.test_a_row_other_than_the_exemplar_naming_a_decision_is_reported`
  - `Exemplar.test_an_exemplar_row_whose_decision_does_not_designate_it_is_reported`
- **Test cases (S4):**
  - `ExampleFiles.test_a_rule_naming_an_invariant_without_its_good_or_bad_case_is_reported`
  - `ExampleFiles.test_a_rule_naming_two_invariants_without_the_cases_of_one_is_reported`
  - `ExampleFiles.test_a_second_case_of_one_kind_for_an_invariant_is_reported`
  - `ExampleFiles.test_a_case_naming_an_invariant_its_rule_does_not_name_is_reported`
  - `ExampleFiles.test_a_case_whose_path_is_out_of_the_repository_is_reported`
  - `ExampleFiles.test_a_line_that_would_open_a_fence_inside_a_case_is_reported`
  - `ExampleFiles.test_another_fenced_block_in_a_rule_carrying_cases_is_reported`

### Now green, against the F4 RED list

- `CodingFixtures.test_the_valid_coding_fixtures_pass`. It can pass already, because S3/S4 add
  errors only for broken fixtures.
- `CodingForm.test_a_missing_or_misplaced_standing_check_rule_is_reported`
- `CodingForm.test_a_standing_check_dropped_by_a_departing_decision_passes`
- `CodingForm.test_a_general_file_with_no_kinds_of_code_is_reported`
- `CodingCarrier.test_a_coding_rule_naming_no_invariant_is_reported`
- `ExampleFiles.test_a_case_whose_path_names_no_file_yet_passes`. This is an S4 control that only
  asks the valid files to pass, so it turns green early.

**Unchecked:** none of the commands above. Python 3.14 behaviour is not checked (the harness has
3.13.16).

## Changed files (`git diff --numstat 18317a8..HEAD`)

```
253	0	product-guidelines/coding/template.md
177	58	product-guidelines/form_check.py
327	8	product-guidelines/test_form_check.py
```

## Sharpness inputs

- **Parts touched:** `product-guidelines` only (`product-guidelines/**`).
- **Trust-boundary file touched:** `product-guidelines/form_check.py`.
- **No new regular expression on product input.** The one new pattern, `\*Status\*: one of (.*?);`,
  reads the-way's own template, like the existing `*Kind*` pattern, and has no nested repetition.
- **Kind names reuse `IDENTIFIER`.** I reuse the existing `IDENTIFIER`
  (`[a-z0-9]+(?:-[a-z0-9]+)*`, already applied to product words) on one file-name component. Its
  group always starts with `-`, so matching stays linear. ASCII alone is accepted, so a Unicode
  look-alike is refused.
- **Rows are split with `str.split`.**
- **Crafted input covered by tests:**
  - kind names `coding-.md`, `coding--a.md`, `coding-A.md`, `coding-a.md.md`, `Coding-a.md`
    (errors) and `coding-a/b.md` (a warning, not read);
  - rows with a `|` in backticks, too few cells, too many, `||`, a separator in the middle;
  - headers off by one space (an inner space, a missing space, a missing column), and the padded
    header as a control;
  - a 1 MiB row of `|`, finishing under 30 s.
- **Irreversible operations:** none.

## Choices I settled (how to make what is settled), with evidence

1. **The coding words are keyed on the discipline named `coding`** (`CODING`), because the index
   and exemplar checks of S3 are coding-specific (spec §5.2 items 3–4 name `guidelines/coding.md`).
   Another discipline giving a kind form is not held to these words.
2. **A table of roles is a table with a *Role* column.** A template requiring
   `Each role in its meaning` without one raises `TemplateError`. This keeps the old fail-safety: a
   styleguide template that loses its roles table, or a column of it, still stops the run.
3. **Any `<discipline>-…` file of a discipline with a kind form is held to the kind form**, even
   when its `<kind>` is malformed. The name error is reported separately, which spares a misnamed
   kind file a flood of errors from the general form.
4. **A separator row must stand right under the header.** One anywhere else is an error, and so is
   a missing one. Before, a dash row anywhere was skipped silently, so this is new behaviour for
   styleguides too, though only on crafted input.
5. **A `|` inside backticks splits a cell, as GitHub-flavoured Markdown reads a row.** Such a row is
   therefore reported as having the wrong number of cells. `table_cells` now removes one outer bar
   at each end, where it used to remove all of them, so an empty last cell written `||` is no
   longer lost.
6. **Brief items left to S3.** Two §5.3 inputs from the brief's bullets 2 and 3 belong to the index
   and exemplar checks, and S3's brief lists them: a name differing from an index row only by case
   or a Unicode look-alike, and two `exemplar` rows or none. I did not write them here.

## Weakest point (WAY-164)

- **Requirement:** "each rule citing its decision, no value, no tool named as the-way's choice"
  (brief, template).
- **Check:** a script lists every paragraph and list item of the template outside fenced code that
  has no `WAY-NN` citation, searches for 19 common tool names, and collects the numerals in the
  prose. I then read each uncited unit against its parent bullet.
- **Result:** 13 of 57 units are uncited. All of them are sub-items of a bullet that cites, or
  section introductions; the styleguide template treats both the same way. No tool name appears,
  and the only numerals are the ordered-list markers 1–3.
- **Evidence:** `slice-2-weakest.txt`.

## Self-review findings

- Lines of the three files are under 100 characters. I rewrapped four lines and amended the commit,
  then reran every check at `334ef34`.
- Both template blocks equal the spec's. The sentence on the invariant demand appears once per form
  section, and the form check reads the two separately (shown by
  `TemplateWords.test_each_form_of_a_discipline_reads_its_own_demand_of_an_invariant`).

## Concerns

1. **Check name moved in the record.** "Holds no table" and header errors of the roles table are now
   recorded under `check_tables`, no longer under `check_roles`. Nothing reads the check name.
2. **The template describes the end state.** It states what the product's copy of `guidelines-form`
   carries (kind index, exemplar, test cases), but the form check does that only after S3/S4.
3. **One S4 control is green early:** `ExampleFiles.test_a_case_whose_path_names_no_file_yet_passes`
   (see above).
4. **Citations to review.** I cite WAY-207 for the C4 sentence ("the skill names which way the tool
   allows") and WAY-200 for the C13 sentence ("a file added after that audit takes no row"). These
   are the decisions closest to those rulings; the rulings themselves are not decisions.

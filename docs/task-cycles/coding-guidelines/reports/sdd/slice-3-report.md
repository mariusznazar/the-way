# Slice 3 report: the form check's index of kinds and the files of a kind

**Status:** DONE_WITH_CONCERNS. **Commit:** `0607656` on `claude/gallant-albattani-3k15lc`
(parent `334ef34`), not pushed. **Python:** 3.13.16 (`python3`); the repository declares 3.14.

## What I implemented

All in `product-guidelines/form_check.py` (spec §5.2 items 3 and 4):

- **`Foundation.bindings`** keeps each decision's binding sentences, from its latest version, with
  `None` for a repeal. `read_foundation` fills it.
- **`Foundation.names_in_backticks(key, word)`** answers "do the binding sentences, whitespace
  collapsed, hold `` `word` ``" (plain substring search, per the spec).
  - For a word with no backtick the question is answered from the set of pieces between
    consecutive backticks of the collapsed text. That set is split once per decision and cached.
  - This gives the same answer as substring search: `` `P` `` with no backtick in P is a substring
    exactly when P lies between two consecutive backticks. It also keeps a file of many exemplar
    rows from searching a large log once per row.
  - A word holding a backtick falls back to plain `in`.
- **New helpers:**
  - `kind_of(path)` gives the `<kind>` of a one-level `guidelines/coding-<kind>.md`.
  - `code_path(cell)` gives the content of a cell that is exactly one code span.
  - `row_path(...)` reports a *File* that is not one path in backticks, or that `refused()` rejects.
    Paths are never given to git.
- **`check_exemplar`** runs in `check_file` for a form that carries *Status* values (the coding
  form of a kind). It reports:
  - each *Status* not on the template's list;
  - each *File* that is not one backticked path, is refused, or is not in the one list
    `git ls-files` gives (`tracked()`);
  - a non-exemplar row whose *Decision* is not `—`;
  - a second `exemplar` row, at its line, naming the first;
  - no `exemplar` row, at the section heading, or line 0 when the section is missing;
  - on each exemplar row: no decision named; a decision not in force (not held, or repealed); a
    decision whose binding sentences lack the *File* or the kind in backticks.
- **`check_kind_index`** runs in `run()` after the per-file loop, only when the coding template
  exists and a coding file is listed. In `guidelines/coding.md` it reports, at the row's line:
  - an empty *When to read*;
  - a bad or refused *File*;
  - a *File* that is no `guidelines/coding-<kind>.md`;
  - a *Kind* other than the file's `<kind>`;
  - a *File* naming no tracked file.

  In each tracked kind file it reports one of these:
  - git tracks no `guidelines/coding.md`;
  - `guidelines/coding.md` is not read;
  - no row names this file.
- **Other changes:**
  - `check_file` returns its tables.
  - Every finding is an error of `guidelines-form/1`, under the checks `check_exemplar` and
    `check_kind_index`.
  - No completeness is asked (C13).
  - The fingerprint of the exemplar's decision is checked by the existing `check_references`, as
    every reference is.
  - The docstring lists the new findings. `PROGRAM`, the options and the exit codes are unchanged.

In `product-guidelines/test_form_check.py` I added the helper `crafted()`, the decisions ABC-07
(v1 `cc24fd66`, v2 repeal) and ABC-08 (`5047a97d`, path outside backticks), and the classes
`Watched`, `KindIndex` (6 tests) and `FilesOfAKind` (12 tests).

## TDD evidence

- **RED (F4).** At `334ef34` all 5 KindIndex and 5 Exemplar tests fail. This matches the S2
  report and my own run at base, which failed with 100 tests and 76 failures.
- **RED (ordinary).** Command, run from `product-guidelines/`:
  `python3 -B -m unittest test_form_check.KindIndex test_form_check.FilesOfAKind`.
  It exited 1: 16 tests, 20 failing subtests (`slice-3-red-ordinary.txt`).
  - It includes `KindIndex.test_a_kind_file_no_row_names_is_an_error`, which shows that a kind file
    missing from the index passed.
  - Every failure was a missing error or an exit 0. I fixed one harness fault first: an ASCII
    encode of `—`.
- **GREEN.**
  - The same command after the change: 16 tests OK.
  - The full suite at `0607656` (below): only the 7 ExampleFiles tests (S4) fail.
- **Coverage tests that passed when written.** Two tests added after GREEN passed on first run,
  because the behaviour they check was already there:
  - `FilesOfAKind.test_a_stale_fingerprint_of_the_exemplar_s_decision_is_an_error` checks existing
    behaviour of `check_references` on the table cell (spec item 4, "as every reference is").
  - `FilesOfAKind.test_a_file_of_the_kind_the_table_leaves_out_passes` is the C13 control.

## Checks

All outputs are under `docs/task-cycles/coding-guidelines/reports/sdd/`.

| Check | Exit | Result | Output |
|---|---|---|---|
| `python3 -B gate/run_tests.py product-guidelines --record …/slice-3-product-guidelines.jsonl` | 1 | 118 tests, 37 failing subtests, all in the 7 ExampleFiles tests. Record: `guidelines-check-kind-index/1` and `guidelines-check-exemplar/1` only `pass`; form, carrier, colour-pair, reference-target, stale-reference and code-path only `pass`; example-files `fail` | `slice-3-product-guidelines.txt`, `.jsonl`, `.exit` |
| `python3 -B product-guidelines/form_check.py --record .runs/guidelines-form.jsonl` | 0 | pass; the-way holds no `guidelines/` | `slice-3-form-check.txt` |
| `python3 -B product-guidelines/form_check.py --merge-onto none --record .runs/guidelines-reference.jsonl` | 0 | the merge check is `unchecked` | `slice-3-form-check-reference.txt` |
| `python3 -B gate/run_tests.py elements/decisions --record …` | 0 | 169 OK | `slice-3-decisions.txt`, `.jsonl`, `.exit` |
| `python3 -B gate/run_tests.py relation-model --record …` | 0 | 19 OK | `slice-3-relation-model.*` |
| `python3 -B gate/run_tests.py gate --record …` | 0 | 98 OK | `slice-3-gate.*` |
| Weakest point (below) | — | confirms the reading | `slice-3-weakest.txt` |

**Turned green, by name:**

- `KindIndex.test_a_kind_file_no_row_names_is_reported`
- `KindIndex.test_a_row_naming_no_file_git_lists_is_reported`
- `KindIndex.test_a_row_whose_kind_is_not_its_files_kind_is_reported`
- `KindIndex.test_a_row_whose_when_to_read_is_empty_is_reported`
- `KindIndex.test_a_kind_file_with_no_general_file_is_reported`
- `Exemplar.test_a_kind_file_with_no_exemplar_row_or_more_than_one_is_reported`
- `Exemplar.test_a_row_whose_status_is_off_the_list_is_reported`
- `Exemplar.test_a_row_whose_file_is_out_of_the_repository_or_untracked_is_reported`
- `Exemplar.test_a_row_other_than_the_exemplar_naming_a_decision_is_reported`
- `Exemplar.test_an_exemplar_row_whose_decision_does_not_designate_it_is_reported`

**Still RED for S4, by name:**

- `ExampleFiles.test_a_rule_naming_an_invariant_without_its_good_or_bad_case_is_reported`
- `ExampleFiles.test_a_rule_naming_two_invariants_without_the_cases_of_one_is_reported`
- `ExampleFiles.test_a_second_case_of_one_kind_for_an_invariant_is_reported`
- `ExampleFiles.test_a_case_naming_an_invariant_its_rule_does_not_name_is_reported`
- `ExampleFiles.test_a_case_whose_path_is_out_of_the_repository_is_reported`
- `ExampleFiles.test_a_line_that_would_open_a_fence_inside_a_case_is_reported`
- `ExampleFiles.test_another_fenced_block_in_a_rule_carrying_cases_is_reported`

**Unchecked:** behaviour on Python 3.14 (the harness has 3.13.16). I did not run the
`installation` suite, which the brief does not name; S11 owns its 4 RED `NAMES` tests.

## Crafted input covered (spec §5.3, WAY-48)

- **Index *File* and kind-table *File*:** absolute, UNC, Windows UNC, `..`, `\`, a drive (with
  and without a slash), BEL, a zero-width space, `:(literal)` and `:!` pathspec magic, and a 200 KiB
  path.
  - Each runs in-process with `subprocess.run` recorded and sockets refused. Every row is
    reported at its line, no path reaches any git argument, and git is asked `ls-files`. Each
    finishes in under 30 s; the actual time is about 1 s.
- **Index rows:**
  - a row differing from its file only by case (`coding-Endpoint.md`), or by a Cyrillic `е`: the
    row is an error and the file has no row;
  - a row naming a tracked non-kind file (`guidelines/coding.md`, `src/api/orders.ts`);
  - a *File* not in backticks, as `` `` ``, or with trailing text;
  - an unreadable general file (over 1 MiB): the kind file is an error.
- **Exemplar table:**
  - two `exemplar` rows, or none;
  - a kind file lacking `## Files of this kind` (C32): both the missing section and the missing
    exemplar are reported;
  - a decision naming the path only outside backticks;
  - a row saying `src/api/orders.tsx` where the decision says `` `src/api/orders.ts` ``;
  - `XYZ-06` (another log's prefix);
  - a repealed ABC-07;
  - a stale fingerprint;
  - a 1 MiB row of `|`, and a row whose cell is about 1 MiB of backticks: each errors in under
    30 s.
- **No new regular expression.** Cells are split with `str.split`. The binding search uses
  `str.split("`")` and set membership, so cost is linear.

## Changed files (`git diff --numstat 334ef34..HEAD`)

```
216	3	product-guidelines/form_check.py
334	0	product-guidelines/test_form_check.py
```

## Sharpness inputs

- **Parts touched:** `product-guidelines` only.
- **Trust-boundary file touched:** `product-guidelines/form_check.py`.
  - Product paths in table cells are shape-checked by the existing `refused()` and compared with
    the one cached `git ls-files` list. They are never opened and never passed to git.
  - Values are printed through `shown()`.
- **Irreversible operations:** none.

## Choices settled (how to make what is settled), with evidence

1. **"git lists" in `guidelines-check-kind-index` is read as what git tracks** (`git ls-files`,
   the existing `tracked()`), for all three clauses.
   - F4 forces this. `test_a_row_naming_no_file_git_lists_is_reported` asks for an error when the
     row's file exists untracked. `test_a_kind_file_with_no_general_file_is_reported` ("the general
     file untracked") asks for an error when `coding.md` exists untracked.
   - A mixed reading, where untracked kind files are listed but `coding.md` must be tracked, would
     be incoherent.
   - Messages and the docstring therefore say "git tracks".
2. **A *File* cell must be exactly one code span.**
   - Spec §4.3 and the template give "a path in backticks". C32 confirms this, and §5.2 item 2 has
     the tables checked "for what §4.3 gives them".
   - A bare path is an error rather than accepted.
3. **A *File* of the exemplar table must be a tracked file, not a directory.** The template says
   "the path of the file … names something git tracks".
4. **Placement of errors:**
   - Row findings at the row's line.
   - The second exemplar row at its own line, naming the first.
   - "No exemplar" at the section heading, or line 0 when the section is missing.
   - Index findings for a kind file in that file's report, at line 0.
   - A failure of `git ls-files` in the run's own `guidelines` report.
5. **No exemplar row is reported whenever the table's rows are unknown:** the section is missing,
   dropped, or holds no readable table. The invariant's sentence ("holds no row … whose *Status* is
   `exemplar`") is then literally true, and this fails closed. The structural error stands beside
   it.
6. **An exemplar row naming two decisions:** each must be in force and must designate the
   exemplar.
7. **The 200 KiB path is not refused for its length.** It is reported as naming no tracked file.
   No path of a file ever reaches git, so "refused before git sees it" holds for every path.
   Adding a length rule to the shared `refused()` would also change `## Where in code`, which
   this slice does not own.
8. **The index check runs only when the coding template exists and a coding file is listed.**
   Otherwise there is no extra git call.

## Weakest point (WAY-164)

- **Requirement:** "every `guidelines/coding-<kind>.md` git lists named by a row of `## Kinds of
  code`" (brief, spec §5.2 item 3), read against the task's aim that an agent finds every kind
  file from the general file.
- **Check:** a manual script (`/tmp/claude-0/-home-user/ac1b534a-8705-5f4d-8b69-597c339e545d/scratchpad/weakest.py`).
  - Actor: me.
  - Method: it builds the ordinary coding fixtures, adds `guidelines/coding-job.md` with no row,
    and runs the form check once with the file untracked and once with it committed.
- **Observed** (`slice-3-weakest.txt`):
  - Untracked: no index error, and the run exits 1 only for that file's own exemplar error.
  - Tracked: `guidelines/coding-job.md:0: error: no row of the table under ``## Kinds of code`` …
    names this file`.
- **Conclusion:** the requirement holds for every committed kind file, which is what the gate
  checks. A kind file written but not yet added escapes the index check until it is added. This is
  the price of choice 1, which F4 forces.

## Self-review

- No line over 100 characters in the changed code.
- The F4 file is untouched (read-only).
- No foundation file was changed.
- `check_tables` already excludes malformed rows from the rows the new checks read, so a row with
  the wrong cell count gets one error, not several.

## Concerns

1. **The untracked kind file** (weakest point and choice 1): a reviewer may judge that "git lists"
   should include files that are untracked but not ignored. F4's fixtures rule that out for rows
   and for the general file.
2. **The exemplar's stale fingerprint** is an error of `guidelines-reference-current/1` (by
   `check_references`), not of `guidelines-form/1`. This follows spec item 4 ("checked as every
   reference is"). A run with no option prints it but records the checks of form only, as it does
   for every reference.
3. **The S2 ⚠️ about the template's end-state promise** (`coding/template.md:192-198`): the kind
   index, the *Status* list, the one exemplar and its decision, and *File* tracked now land. The
   test cases remain for S4.

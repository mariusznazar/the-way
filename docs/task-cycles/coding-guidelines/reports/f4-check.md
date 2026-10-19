# F4 check-author report — coding guidelines

**Status:** done. **Commit:** `64344a3` on `claude/gallant-albattani-3k15lc` (parent `05e44b1`), not pushed.

## What I read and what I did not

Read: the `guidelines-*` entries and `gate-guidelines-example-evidence/1` in `foundations/invariants.md`
at `05e44b1`, plus the old carrier sentence (`git show 235b0b4:…`); WAY-167, 168, 196, 198, 199, 202 and 212
in full, and WAY-03, 08, 65, 69; spec §4.1, §4.2 and §5.1 only; `product-guidelines/template.md`,
`product-guidelines/styleguide/template.md`; the existing `test_form_check_invariants.py` and
`installation/test_install.py`; the `--help` output and module docstring of `form_check.py`; its
`guidelines-form-check-command` entry in the part map; the citation rule in `gate/run_tests.py`.

Not read: spec §5.2, §5.3, §9 or any other spec section (I saw the spec's heading list once, while
finding §4.1, §4.2 and §5.1. It named the skill `maintain-coding-guidelines` at
`product-guidelines/coding/SKILL.md`, which is what `NAMES` now holds); `plan.md`; other agents'
reports; `reports/design*.md`; the body of `form_check.py`. I ran the form check once on the valid
coding files and once on a misnamed file to see its current report lines
(`f4-valid-coding-at-05e44b1.txt`).

`gate-guidelines-example-evidence/1` has method `TODO`, so I wrote no check for it.

## Commands, exit codes, outputs (Python 3.13.16)

| Run | Command | Exit | Output |
|---|---|---|---|
| baseline at `05e44b1` | `python3 -B gate/run_tests.py product-guidelines --record …/f4-baseline-product-guidelines.jsonl` | 0 (61 tests OK) | `f4-baseline-product-guidelines.txt`, `.jsonl` |
| baseline at `05e44b1` | `python3 -B gate/run_tests.py installation --record …/f4-baseline-installation.jsonl` | 0 (33 tests OK) | `f4-baseline-installation.txt`, `.jsonl` |
| after the change | `python3 -B gate/run_tests.py product-guidelines --record …/f4-product-guidelines.jsonl` | 1 (88 tests, 89 failing subtests/tests) | `f4-product-guidelines.txt`, `.jsonl`, `.exit` |
| after the change | `python3 -B gate/run_tests.py installation --record …/f4-installation.jsonl` | 1 (33 tests, 3 failures, 1 error) | `f4-installation.txt`, `.jsonl`, `.exit` |

All outputs are in `docs/task-cycles/coding-guidelines/reports/`.

**What passed at `05e44b1` still passes.** All 26 cited tests of `test_form_check_invariants.py`
give the same `pass` as at baseline (compared record by record), and so do the 35 tests of
`test_form_check.py`. In `installation`, only the four tests that read `NAMES` fail.

## RED list (by test name)

`product-guidelines/test_form_check_invariants.py`, 23 tests:

- `CodingFixtures.test_the_valid_coding_fixtures_pass`
- `CodingForm.test_a_missing_or_misplaced_standing_check_rule_is_reported`
- `CodingForm.test_a_standing_check_dropped_by_a_departing_decision_passes`
- `CodingForm.test_a_general_file_with_no_kinds_of_code_is_reported`
- `CodingCarrier.test_a_coding_rule_naming_no_invariant_is_reported`
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
- `ExampleFiles.test_a_rule_naming_an_invariant_without_its_good_or_bad_case_is_reported`
- `ExampleFiles.test_a_rule_naming_two_invariants_without_the_cases_of_one_is_reported`
- `ExampleFiles.test_a_second_case_of_one_kind_for_an_invariant_is_reported`
- `ExampleFiles.test_a_case_naming_an_invariant_its_rule_does_not_name_is_reported`
- `ExampleFiles.test_a_case_whose_path_is_out_of_the_repository_is_reported`
- `ExampleFiles.test_a_case_whose_path_names_no_file_yet_passes`
- `ExampleFiles.test_a_line_that_would_open_a_fence_inside_a_case_is_reported`
- `ExampleFiles.test_another_fenced_block_in_a_rule_carrying_cases_is_reported`

Why each is red: a check is missing, never a harness fault. None fails on a fixture-building
assertion. Each red `…_is_reported` fails on "no error … that the valid files lack", and each red
`…_passes` fails on exit 1. The cause is the one error today's form check gives the valid coding
files: `guidelines/coding-endpoint.md:0: error: the file's name does not agree with its
*Discipline* `coding``. It is red until the slices that write `product-guidelines/coding/template.md`
and the form check's coding, kind-index, exemplar and test-case checks.

`installation/test_install.py`, the 4 tests that read `NAMES`:
`test_preview_apply_rerun_and_preserve_foundation` (cites installation invariants; now `fail`),
`test_wrapper_sends_the_skill_to_the_product_case_of_where_the_way_lies` (error: path
`product-guidelines/coding/SKILL.md` does not exist), `test_guidance_names_no_commit_and_covers_the_product_rules`,
`test_warns_before_writing_paths_git_ignores`. They are red until the slice that writes the skill
and its entry in `installation/install.py`.

**Four new tests pass today, by design.** Each checks behaviour today's form check already has, or
the absence of an error:

- `CodingCarrier.test_a_coding_rule_naming_no_decision_is_reported`: the first clause of the carrier
  sentence already holds for every discipline.
- `CodingForm.test_a_standing_check_dropped_without_a_departing_decision_is_reported`: today the
  error comes from the rule lacking its fields. Once the template makes the rule droppable, it must
  come from the drop text. Both clauses belong to `guidelines-check-form`, and the red control
  (`…dropped_by_a_departing_decision_passes`) pins the pair.
- `CodingForm.test_a_coding_file_whose_name_and_discipline_disagree_is_reported`: today's name rule
  already rejects these names, and the new kind naming must keep rejecting them.
- `ExampleFiles.test_a_rule_naming_only_guidelines_form_needs_no_cases`: the exemption; today's check
  ignores blocks.

## Each test: invariant, clause, fixture

Fixtures: `CODING` (`guidelines/coding.md`) and `CODING_ENDPOINT` (`guidelines/coding-endpoint.md`)
use the verbatim headings, header lines, table columns (`Kind | File | When to read`,
`File | Status | Decision`) and *Status* values of §4.1 and §4.2. Every rule carries *Decision*,
*Invariant*, *Good* and *Bad*, followed by one `good`/`bad` case per invariant it names
(`lint-clean`, `format-clean`, `audit-clean`, `endpoint-validates`, and the pair `endpoint-handler` ·
`endpoint-location`). The foundation gains decisions ABC-10 to ABC-18 (ABC-09 stays absent, as the
reference tests require), seven invariants (including the product's copy of `guidelines-form`) and
`src/api/{schema,handler}.ts` and `src/api/{orders,users,legacy}/route.ts`. Each fingerprint was
computed once with `relation-model/fingerprint.py` and written out as a literal. The exemplar
decision ABC-13 wraps its backticked path and kind over lines, which tests the "whitespace
collapsed" clause in the valid case.

| Test | Invariant | Clause | Fixture / break |
|---|---|---|---|
| `Fixtures.test_the_valid_fixtures_pass` (existing; gains a citation) | form, carrier, colour-pair, reference-target, stale-reference, code-path, **example-files** | valid files raise no error | styleguide now carries 2 good + 2 bad cases |
| `CodingFixtures.test_the_valid_coding_fixtures_pass` | form, carrier, kind-index, exemplar, example-files | valid coding files pass, alone and beside the other disciplines, with and without `--merge-onto none` | `CODING_FILES` |
| `CodingForm.test_a_missing_or_misplaced_standing_check_rule_is_reported` | form | required rule lacking or out of order | Linter, Formatter or Dependency audit removed; Formatter before Linter (fragment: the rule name) |
| `…standing_check_dropped_without_a_departing_decision_is_reported` | form | a drop with text other than `none —` + decision + fingerprint | `none — <reason>`, `none`, `none — ABC-18`, bare reason |
| `…standing_check_dropped_by_a_departing_decision_passes` | form | control (WAY-202) | `none — ABC-18@1fff448b` |
| `…general_file_with_no_kinds_of_code_is_reported` | form | required section lacking | general file alone, no `## Kinds of code` (fragment `Kinds of code`) |
| `…coding_file_whose_name_and_discipline_disagree_is_reported` | form | name and *Discipline* disagree | `coding-.md`, `coding-Endpoint.md`, `coding--x.md`, each indexed by a row, plus TESTING/STYLEGUIDE texts under coding names and CODING as `testing.md` (fragment `Discipline`) |
| `CodingCarrier.test_a_coding_rule_naming_no_invariant_is_reported` | carrier | no invariant in a file whose template requires one | Linter `none`; Linter naming a decision only; a further general rule `none`; a kind's rule `none` (each without its cases) |
| `CodingCarrier.test_a_coding_rule_naming_no_decision_is_reported` | carrier | *Decision* names no decision | Formatter `none`; kind rule naming an invariant only |
| `KindIndex.test_a_kind_file_no_row_names_is_reported` | kind-index | file listed, no row | row removed (error in either file) |
| `…row_naming_no_file_git_lists_is_reported` | kind-index | row's *File* lists nothing | row for `coding-job.md`, absent / untracked (at the row's line) |
| `…row_whose_kind_is_not_its_files_kind_is_reported` | kind-index | *Kind* ≠ file's kind | `handler`, `endpoints`, `Endpoint`, empty (at the row's line) |
| `…row_whose_when_to_read_is_empty_is_reported` | kind-index | empty *When to read* | `\|  \|`, `\| \|` (at the row's line) |
| `…kind_file_with_no_general_file_is_reported` | kind-index | kind file, no `coding.md` listed | alone; beside styleguide and testing; `coding.md` untracked (error in kind file, `coding.md` or `guidelines`) |
| `Exemplar.test_a_kind_file_with_no_exemplar_row_or_more_than_one_is_reported` | exemplar | zero or more than one `exemplar` | exemplar row demoted; empty table; two exemplar rows both naming ABC-16, whose sentence names both paths and the kind, so that only the count is wrong |
| `…row_whose_status_is_off_the_list_is_reported` | exemplar | *Status* off the list | `copied`, `do-not-copy`, empty, `example` on the copy row |
| `…row_whose_file_is_out_of_the_repository_or_untracked_is_reported` | exemplar | *File* absolute, `..`, drive, UNC, untracked | 10 paths on the copy row (not the exemplar row, so no decision is asked to name them) |
| `…row_other_than_the_exemplar_naming_a_decision_is_reported` | exemplar | non-exemplar *Decision* not `—` | ABC-13, `none`, empty |
| `…exemplar_row_whose_decision_does_not_designate_it_is_reported` | exemplar | decision not held, repealed, absent; binding lacks *File* or kind in backticks | ABC-09, ABC-04 (repealed), `—`, ABC-14 (kind only), ABC-15 (kind bare), ABC-17 (path bare), ABC-10 (neither) |
| `ExampleFiles.test_a_rule_naming_an_invariant_without_its_good_or_bad_case_is_reported` | example-files | exactly one good and one bad per named invariant, in every discipline | kind rule without good / bad / both; Linter without cases; the styleguide's role rule without cases; TESTING's rule naming `lint-clean` without cases |
| `…rule_naming_two_invariants_without_the_cases_of_one_is_reported` | example-files | a pair for each named invariant | either invariant's pair, or one case of it, removed |
| `…second_case_of_one_kind_for_an_invariant_is_reported` | example-files | exactly one | two good cases; two bad cases |
| `…case_naming_an_invariant_its_rule_does_not_name_is_reported` | example-files | block's identifier not named by *Invariant* | a pair for `lint-clean`, `endpoint-handler`, `guidelines-form`, `missing-check` |
| `…case_whose_path_is_out_of_the_repository_is_reported` | example-files | path absolute, `..`, drive, UNC | 9 paths |
| `…case_whose_path_names_no_file_yet_passes` | example-files | control: a path that names no file is allowed | `src/api/carts/route.ts` |
| `…line_that_would_open_a_fence_inside_a_case_is_reported` | example-files | inner fence-opening line | `~~~`, `~~~ts`, ```` ```ts ````, three spaces + ```` ```ts ````, two spaces + `~~~`, four backticks, bare ```` ``` ```` |
| `…another_fenced_block_in_a_rule_carrying_cases_is_reported` | example-files | every other fenced block | ```` ```ts ````, no info string, `sample …`, `good <id>` with no path, `~~~ts` |
| `…rule_naming_only_guidelines_form_needs_no_cases` | example-files | the exemption | styleguide background rule naming `guidelines-form` alone without cases; naming it beside `background-pair` with only that pair |

Every test cites its invariant as `# invariant: <identifier>/1` in its body (WAY-65). No expected
value is computed by the code under test (WAY-69).

## Changed files

- `product-guidelines/test_form_check_invariants.py`: +701 / −49.
  - The styleguide fixture gains its cases, and the existing tests' `with_line` numbers follow
    (31→39, 32→40, 36→44, 42→58, 44→60, 46→62, 70→86, 78→94). `with_line` checks each line's text.
  - Two Carrier cases that set the background rule's *Invariant* aside now also drop its cases, so
    no case names an invariant the rule no longer names.
  - `errors()` and `assert_reported()` accept a tuple of paths.
  - New: `assert_reported_anew()`, `baseline_errors()`, `case()`, `rule()`, `line_of()`, and the
    coding fixtures and test classes.
- `installation/test_install.py`: +2 / −1. `NAMES` gains `("product-guidelines/coding/SKILL.md", "maintain-coding-guidelines")`.

## Choices, the alternative rejected, and the cost if wrong

1. **The differential assertion.** Coding tests count only an error that the valid coding files,
   run with the same options, do not give in the same file with the same message. Rejected: plain
   `assert_reported`. Every kind-file test would pass today on the name error, never for its own
   reason. Cost if wrong: none once the valid coding test is green, because the baseline is then
   empty. Until then, these tests are red by construction.
2. **No line asserted for blocks, missing rows or file-level errors.** Lines are asserted only where
   the sentence points at a table row: kind-index rows, *Files of this kind* rows. Rejected: lines
   for blocks, which could be the opening line, the inner line or the rule's heading. Cost: a little
   less precision. A wrong line in a row test would turn one of them red after the implementation;
   then the line belongs to the row, which I consider the natural reading.
3. **Table cells.** *File* paths are written in backticks; *Kind* and *Status* values bare;
   non-exemplar *Decision* is `—`. Rejected: bare paths. Cost if the template S2 writes sets bare
   paths: every coding test goes red on the valid fixture, which shows at once and is fixed by
   editing the three row constants.
4. **Fragments.**
   - `"Linter"`, `"Formatter"`, `"Dependency audit"` and `"Kinds of code"`, as the existing styleguide
     tests do for missing rules and sections.
   - `("Discipline", "discipline")` for the name test, taken from today's message.
   - Cost: an implementation that words these errors without those words turns the matching test red.
5. **"Left open to the end of the file" is not checked.** That is the clause of `guidelines-check-example-files`
   about a block never closed. Such a block swallows `## Examples` and `## Where in code`, so the
   missing-section errors would make any assertion pass by accident. I left the clause unchecked
   rather than write a test that passes for the wrong reason.
6. **The kind-file-section form clause is not checked either.** A kind file lacking `## Files of this kind`
   would also fire the exemplar check (no exemplar row), so it cannot be isolated. I check the
   general file's `## Kinds of code` instead, with the general file alone.
7. **The skill name in `NAMES`** comes from the spec heading list I saw (see "What I read"). If C24
   names it differently, edit the one tuple entry.

## Questions for the orchestrator

1. `NAMES` already lacks `lead-project` and `maintain-styleguide`, which `install.py` installs. I
   added only the coding skill, as C24 scopes it. Should the missing two be added in this cycle or
   noted as debt?
2. Is the *File* cell of both coding tables meant to hold the path in backticks (my reading of
   WAY-212 "by its path in backticks" and the form's "paths in backticks")? If the template S2
   writes says bare, choice 3 needs one edit.
3. Choices 5 and 6 leave two clauses unchecked. Does the reviewer's deliberate break need to cover
   them, or should they stay recorded as unchecked?

## Turn 2 — return to the foundation step (ruling C34)

**What went wrong.** The S4 code reviewer broke `guidelines-check-example-files/1` on purpose: a
rule whose *Invariant* names `guidelines-form` beside another invariant was exempted as a whole.
No test caught it. My "beside another" subtest in
`test_a_rule_naming_only_guidelines_form_needs_no_cases` was only a clean control, and no test
asserted that the other invariant's cases are still required.

**Fix.** Commit `dfa9e15` on `claude/gallant-albattani-3k15lc` (parent `1bff1ae`), not pushed. It
changes only `product-guidelines/test_form_check_invariants.py` (+34/−0). It adds
`ExampleFiles.test_a_rule_naming_guidelines_form_beside_another_without_the_others_cases_is_reported`,
which cites `guidelines-check-example-files/1`.

The clause it checks: the rule must give exactly one good and one bad case for each invariant it
names other than `guidelines-form`, and the exemption covers `guidelines-form` alone. It has five
subtests:

- styleguide rule with *Invariant* `guidelines-form · background-pair`:
  - no case of `background-pair`
  - no good case only
  - no bad case only
- styleguide rule with `background-pair · guidelines-form` (the exempt invariant named second), no case of the other
- coding rule of a kind with `guidelines-form · endpoint-validates`, no case of `endpoint-validates`

Each subtest is asserted with `assert_reported_anew` in the changed file: it needs exit 1, an error
the valid files don't give, and `fail` for `guidelines-form/1` in the record.

**Run.** `python3 -B gate/run_tests.py product-guidelines --record …/f4-fix-product-guidelines.jsonl`
on `1bff1ae` plus this change: exit 0, 137 tests OK, the new test included (`pass`). Output files:
- `f4-fix-product-guidelines.txt`, `.jsonl` and `.exit`
- `f4-fix-sample-output.txt`: the form check's report for the first subtest. It gives two errors
  at line 40, no good and no bad `background-pair` case, which confirms the test fails for the
  sentence's reason.

**Not done.** I did not re-run the reviewer's break against the new test, because that would mean
reading or changing the form check's body. The new test asserts exactly the behaviour that break
removes, so the reviewer can re-apply it to confirm it now fails.

## Turn 3 — the kind-index sentence now says "git tracks" (commit 355a240)

**Verdict:** no citing check has to change, because none expects a different value. One control is
missing, on the side the new wording makes explicit. I recommend adding it (exact text below).
Nothing was edited or committed in this turn.

**What I read:** the new sentence of `guidelines-check-kind-index/1` at `355a240`, its old and new
text in `return-step.md` (§ "`guidelines-check-kind-index/1` — edited in place" and its note to me),
and my `KindIndex` and `CodingFixtures` tests. My grep of `return-step.md` also printed the
neighbouring rows of its candidates table. I did not act on them.

**Each clause against the checks that cite it:**

| Clause of the new sentence | Check (`test_form_check_invariants.py`) | Still exact? |
|---|---|---|
| a kind file git tracks that no row names | `KindIndex.test_a_kind_file_no_row_names_is_reported` (line 1146): the kind file is tracked and the row removed | yes |
| a row whose *File* names no file git tracks | `KindIndex.test_a_row_naming_no_file_git_lists_is_reported` (line 1153): subtests for an absent target and an **untracked** target, both reported | yes, and now exact: under "git lists" the untracked subtest was open to a reading that counts untracked files; under "git tracks" untracked means absent |
| *Kind* not the file's kind, *When to read* empty | `…kind_is_not_its_files_kind…` and `…when_to_read_is_empty…`: the files are tracked | not affected by the edit |
| a kind file git tracks where git tracks no `guidelines/coding.md` | `KindIndex.test_a_kind_file_with_no_general_file_is_reported` (line 1185): alone, beside other disciplines, and "the general file untracked", all reported | yes. The last subtest is the one the return step's deliberate break targets |
| valid files raise no error | `CodingFixtures.test_the_valid_coding_fixtures_pass` (line 1021): both files tracked | yes |

**The missing control.** Every check that cites the invariant covers what must be reported. None
covers the files the new wording keeps out of the clause: a file `guidelines/coding-<kind>.md`
that git does not track. A form check that counted such a file, as unindexed or as lacking its
general file, would over-report and still pass every test. That is a break of the new sentence,
and today nothing would catch it.

I ran both cases read-only through the test harness on the current code. Both exit 0 with no
error, with and without `--merge-onto none`. Output: `f4-turn3-untracked-controls.txt`.

**Proposed addition** (append to `class KindIndex`, after
`test_a_kind_file_with_no_general_file_is_reported`). It is green on the current code:

```python
    def test_a_kind_file_git_does_not_track_is_no_error(self):
        """The control of the tests above: a file of a kind standing in the working tree but not
        tracked by git is no file of the sentence, so no row is asked to name it and no general
        file is asked to stand beside it."""
        # invariant: guidelines-check-kind-index/1
        general = replaced(CODING, KINDS_ROW + "\n", "")
        cases = (
            ("no row names it", {CODING_FILE: general}),
            ("no general file", {TESTING_FILE: TESTING}),
        )
        for name, files in cases:
            for options in ((), ("--merge-onto", "none")):
                with self.subTest(name, options=options):
                    self.assert_clean(self.check(
                        files, options, untracked={CODING_ENDPOINT_FILE: CODING_ENDPOINT}))
```

A deliberate break for the reviewer: make the kind-index check count untracked files of
`guidelines/`. Both subtests above must then fail.

**Optional, cosmetic:** rename `test_a_row_naming_no_file_git_lists_is_reported` to
`test_a_row_naming_no_file_git_tracks_is_reported`, so the name follows the sentence. Its body and
expected values stay. The rename changes the check's id in run records (fine before `main`).

### Turn 3, applied (ruling C40)

Commit `28b42a2` on `claude/gallant-albattani-3k15lc` (parent `f34e477`), not pushed. It changes only `product-guidelines/test_form_check_invariants.py` (+18/−2):

- adds `KindIndex.test_a_kind_file_git_does_not_track_is_no_error`, exactly as proposed above;
- renames `test_a_row_naming_no_file_git_lists_is_reported` to
  `test_a_row_naming_no_file_git_tracks_is_reported`;
- rewords the docstring of `test_a_kind_file_with_no_general_file_is_reported` from "Git lists" to
  "Git tracks".

Bodies and expected values are unchanged.

Run: `python3 -B gate/run_tests.py product-guidelines --record …/f4-turn3-product-guidelines.jsonl`
exits 0 with 138 tests OK. Both kind-index tests named above pass. Output:
`f4-turn3-product-guidelines.txt`, `.jsonl`, `.exit`.

## Turn 4 — settlement of assessment remark I3

**Commit:** `a839ea7` on `claude/gallant-albattani-3k15lc` (parent `8242720`), not pushed. It
changes only `product-guidelines/test_form_check_invariants.py` (+43/−0).

**What I read:** remark I3 of `reports/assessment.md` and `reports/assessment-settlement.md`. My
extraction of I3 ran past it into the Minor remarks M1–M6. I did not act on them.

**Isolating the clause F4 left unchecked.** I first ran the form check read-only on a file whose
last case lost its closing line (`f4-turn4-open-block-probe.txt`). The swallowed sections are
reported at line 0 ("the section `## Examples` is missing", and the same for `## Where in code`).
The open block is reported at its own opening line. So the clause can be isolated:

- the case taken is the file's last, so no later fence closes it and no line inside it would open
  one;
- the test asks for an error at that opening line;
- the message must contain "end of the file", the sentence's words;
- the error must be one the valid files do not give (`assert_reported_anew`).

F4's earlier reason (choice 5) no longer holds.

| Test | Invariant | Clause | Fixture / break |
|---|---|---|---|
| `ExampleFiles.test_a_case_left_open_to_the_end_of_the_file_is_reported` | `guidelines-check-example-files/1` | "every such block left open to the end of the file" | subtests: the last case of `coding-endpoint.md` (`bad endpoint-location`, line 63) and the last case of the styleguide (`bad background-pair`, line 50), each without its closing line. Guard: no fence follows that case in the valid file |
| `KindIndex.test_a_row_naming_a_tracked_file_of_no_kind_is_reported` | `guidelines-check-kind-index/1` | a row "whose *Kind* is not the `<kind>` of the file its *File* names", for a tracked file with no `<kind>` | one row added beside the valid endpoint row, with *File* `guidelines/testing.md`, `guidelines/styleguide-web.md`, `guidelines/coding.md` or `src/api/orders/route.ts`; all four files are tracked. Asserted at the row's line (15) in `coding.md` |

Evidence from the current code is in `f4-turn4-kind-row-probe.txt`. For example:
"`guidelines/coding.md:15: error: the path `guidelines/testing.md` of *File* names no file
`guidelines/coding-<kind>.md``".

**Run:** `python3 -B gate/run_tests.py product-guidelines --record …/f4-turn4-product-guidelines.jsonl`
exits 0, 140 tests OK, both new tests `pass`. Output: `f4-turn4-product-guidelines.txt`, `.jsonl`,
`.exit`.

**Deliberate breaks for the reviewer:**

1. Open case: make the test-case check stop reporting a block that reaches the end of the file
   (for example, treat the end of the file as closing it). Both subtests of
   `test_a_case_left_open_to_the_end_of_the_file_is_reported` must fail. The missing-section
   errors at line 0 then remain, and they must not satisfy the test.
2. Row of no kind: make the kind-index check accept a row whose *File* names any tracked file,
   comparing *Kind* only when the file is of the form `guidelines/coding-<kind>.md` (that is, drop
   the "names no file `guidelines/coding-<kind>.md`" report). All four subtests of
   `test_a_row_naming_a_tracked_file_of_no_kind_is_reported` must fail.

# Slice 4 review: the form check of test cases (`0607656..1bff1ae`)

### Spec Compliance

- ✅ Spec compliant: spec §5.2 item 5 and §5.3 bullets 4, 5 and 7 are met, with C11, C12, C18, C21 and C33. All of it is in `product-guidelines/form_check.py:925-1046` and is called from `check_file` at `form_check.py:1494`.
  - **Good and bad cases.** Each invariant the rule names, other than `guidelines-form`, needs one good and one bad case. A missing case is reported at *Invariant* (`:1037-1046`). A second case of the same kind is an error.
  - **Unnamed invariant.** A case naming an invariant the rule does not name is an error, and so is a case naming `guidelines-form`.
  - **Paths.** Each case path goes through `refused()` (`:1202`), which refuses absolute paths, `..`, a drive, a UNC prefix, `\`, `:` and characters that are not printable.
  - **Info string.** It is read from the opening fence only (`Fence.info`, `:522-539`).
  - **Malformed test case.** Any other block of the rule is reported at its opening line. That covers a block standing among the fields, a tilde or four-backtick fence, and an info string of the wrong form. It also covers the C21 former closing line.
  - **Open to the end.** A block left open to the end of the file is reported at its opening line.
  - **Fence lines inside a case (C33).** A line inside a case that starts with three backticks or three tildes after any whitespace is reported. Lines are cut into the pieces `splitlines` gives.
  - **Rules naming only `guidelines-form`.** They are exempt (`:968`).
  - **Records.** Every finding is recorded under `guidelines-form/1`.
  - **Unchanged.** `PROGRAM`, the options and the exit codes did not change. The diff adds no regular expression (`str.split`). Nothing opens a case path, and nothing gives one to git or writes one.
- ✅ The promise in the common template's "Test cases of a rule" (`product-guidelines/template.md:94-133`) now exists. Each report it says "the form check reports" is now produced:
  - the pair for each invariant;
  - a path holding `..`, a drive, `\`, `:` or a leading `/`, through `refused()`;
  - the limit of 1048576 bytes, which existed before and is now tested with cases (`test_form_check.py` `test_a_file_of_cases_just_over_one_mebibyte_is_refused_unread`);
  - a line starting with a fence after any leading whitespace;
  - the bare-fence malformed case at the former closing line;
  - every fenced block of such a rule being a case.
- ✅ The promise in the coding template's section on the product's copy of `guidelines-form` (`product-guidelines/coding/template.md:189-195`) is complete. "The test cases of each rule with their paths" was the item still missing, and `check_cases` now gives it.
- ✅ The end-to-end run (`slice-4-e2e.txt`) shows exit 0, 0 errors, no dead path and no import. It covers both form-check runs and `check_instructions.py` on a product filled from the coding template. Its two controls each exit 1 at the expected line.
- ✅ The record (`slice-4-product-guidelines.jsonl`) holds only `pass` lines. The suites, product-guidelines with 136 tests and gate with 98, have exit 0 and output with no warnings.
- ⚠️ Cannot verify from the diff: behaviour on Python 3.14, the version the repository declares. The executor ran 3.13.16. The controller should run the product-guidelines suite on 3.14 before merge.

### Deliberate break (`guidelines-check-example-files/1`, from its sentence in `foundations/invariants.md:2233-2235`)

**How:**
- Scratch worktree: `git worktree add <scratchpad>/review-1bff1ae 1bff1ae`.
- Each break was run with `python3 -B gate/run_tests.py product-guidelines --record <scratchpad>/slice-4-break-<name>.jsonl`.
- The tree was restored after each break.
- The worktree was then removed (`git worktree list` shows only the checkout, which is untouched at `1bff1ae`).
- Each output file holds the run, its exit code and the break's diff.

| Break (sentence clause made false) | Exit | Test citing the invariant fails? | Output |
|---|---|---|---|
| "every line inside such a block that would open a fence": the inner check reads the line without stripping its leading whitespace (`text = piece`) | 1 | **Yes.** `ExampleFiles.test_a_line_that_would_open_a_fence_inside_a_case_is_reported` failed on the subtests `   ```ts` and `  ~~~`; 13 ordinary subtests failed too | `slice-4-break-indented-inner-fence.txt` |
| "every rule … whose *Invariant* names an invariant other than `guidelines-form`": a rule naming `guidelines-form` beside another invariant is exempted (`required = [] if FORM_IDENTIFIER in named else named`) | 1 | **No.** Only the ordinary `TestCases.test_a_rule_naming_guidelines_form_needs_no_case_and_takes_none_of_it` [beside another, with a pair of it] failed | `slice-4-break-form-beside-exempt.txt` |
| "every such block left open to the end of the file": the open-block report turned off | 1 | **No.** Only the ordinary `TestCases.test_a_case_left_open_to_the_end_of_the_file_is_an_error_at_its_opening_line` failed. This gap is known and accepted by C32 (3) | `slice-4-break-open-to-end.txt` |

The second break goes undetected by every test that cites the invariant. That is Important finding 1.

### Strengths

- **One fence reader.** `fenced_blocks` (`form_check.py:522-539`) reads fences once. `fenced_lines` and `check_cases` both derive from it, so the code flags and the cases cannot disagree about where a block ends.
- **The executor's weakest-point work is real.** The split at `\n` against `splitlines` mismatched `check_instructions.py`'s `FENCE` (`instruction-files/check_instructions.py:57`). The fix reads lines in `splitlines` pieces, and an ordinary test pins it. My first break shows that test failing on all 7 line-break characters.
- **Linear cost.** Blocks are assigned to rules with `bisect` (`:956-960`). Values from the file are printed through `shown()`. The 1 MiB info-string tests bound both time and output.
- **WAY-48 crafted inputs are covered in process.** `run_sealed` patches `os.open`, `os.lstat`, `os.stat` and `builtins.open`, refuses sockets and records git's arguments. Every crafted path from S3, the valid path, a path of 200 KiB, a path of 1 MiB and a file just over the limit are checked unopened and unseen by git.
- **Tests name what they catch.** Each new test names the break it catches, and the C21 test pins both the malformed-case line and the fact that the shortened good case still counts.

### Issues

#### Critical (Must Fix)

None.

#### Important (Should Fix)

1. **No test citing the invariant catches the exemption of a rule that names `guidelines-form` beside another invariant.**
   - **Where:** `product-guidelines/test_form_check_invariants.py:1311`, `:1394`.
   - **The break:** under it (above, `slice-4-break-form-beside-exempt.txt`), a rule whose *Invariant* reads `guidelines-form@… · endpoint-handler@…` with no case passes. That makes the invariant's sentence false.
   - **Why the invariant tests miss it:** the "beside another" subtest of `ExampleFiles.test_a_rule_naming_only_guidelines_form_needs_no_cases` is a clean control only.
   - **Why the ordinary tests barely catch it:** the ordinary test at `test_form_check.py:1271` catches it only through the subtest that adds a `guidelines-form` pair. No test has the direct negative, a rule naming `guidelines-form` beside another invariant without the other's pair.
   - **Scope:** the code of this slice is correct. The gap is in the F4 invariant test file, which is outside this slice's change list, so it is graded Important there.
   - **Fix:** in `ExampleFiles`, add a subtest "beside another, without the other's cases" to `test_a_rule_naming_two_invariants_without_the_cases_of_one_is_reported` or to the `guidelines-form` test. It is an invariant-test change, so it takes its own independent assessment.
   - **Inside this slice:** add the same negative subtest to `TestCases.test_a_rule_naming_guidelines_form_needs_no_case_and_takes_none_of_it` (Minor on its own).

#### Minor (Nice to Have)

1. **Broken wrap in the module docstring.**
   - **Where:** `product-guidelines/form_check.py:82-85`.
   - **What:** after "A path of a case may name a file the product does not hold. A" come the lines "decision is" and "named by a number", then the old line "with the prefix of the product's log…". The report says the docstring was rewrapped, but it was not.
   - **Fix:** reflow the paragraph to the file's width.
2. **A field-like line after the cases moves the end of the fields.**
   - **Where:** `form_check.py:978` (`last_field`).
   - **What:** `shared.parse_fields` (`elements/common/guard_shared.py:64-78`) takes any `- **Name:**` line of the rule's prose as a field. Prose such as `- **Note:** …` after the cases moves `last_field` past them, and each case is then reported as a malformed case "before the rule's fields end".
   - **Impact:** a false positive on an odd input, never a false pass.
   - **Fix (optional):** take the last line among the template's four fields (`form.fields`).
3. **Executor concern 1: a rule naming `guidelines-form` alone, with fenced blocks, passes unchecked.** I accept this reading.
   - Spec §5.2 item 5 says such a rule "needs no blocks".
   - The invariant's scope is a rule naming another invariant.
   - The template's bullet at `template.md:129-133` describes what the rule gives, and unlike the path and fence bullets it promises no report.
   - It adds no exposure beyond what any illustrative block under `## Examples` already has.
   - No change is needed. If the orchestrator reads the template otherwise, that is a ruling.
4. **Executor concern 2: a case closed by four backticks is reported at its closing line.** I accept this.
   - §5.3 lists the input without an expected report.
   - The template's "outer fence of a case is three backticks" covers both fences.
   - The closing line is the precise place for the report.
   - The case still counts, so the missing-case report does not fire twice (the test asserts this).
5. **Executor concern 3: only an ordinary test covers a block left open to the end.** This is confirmed by my third break. It is accepted by C32 (3), so it is not a new finding.
6. **Executor concern 4: a tab-indented bare fence closes a case.** This is pre-existing in the shared reader and outside the scope of this slice.
   - **Where:** `form_check.py:536`. Here `line.lstrip(" ")` counts no indent for a tab or a no-break space, while `strip()` removes it.
   - **Why it is no unprotected path:** `check_instructions.py` toggles on the same line, and the case's real closing line then opens a block that is reported as malformed.
   - **Side issue:** the docstring's "after at most three spaces" (`:72-74`) slightly over-states the closing rule.
7. **Small polish.**
   - `Fence.closing` is annotated `int` but holds `None` (`form_check.py:519`).
   - `check_cases` parses each rule's fields a second time (`:966`) after `check_rules` already did. The report acknowledges this, and it is acceptable for a separate record entry.

### Assessment

**Task quality:** Approved

**Reasoning:** The check meets spec §5.2 item 5 and §5.3 with the C11, C18, C21 and C33 rulings. It is linear, writes no regular expression and opens no case path, and its ordinary crafted-input tests caught each of my three breaks. The one Important finding is a missing negative case in F4's invariant tests, outside this slice's change list: no test citing the invariant fails when a rule naming `guidelines-form` beside another invariant is exempted. It should be fixed by an invariant-test change with its own assessment, not by reworking this slice.

## Re-review of fix round 1 (`1bff1ae..d743c2e`: `dfa9e15` F4 check author, `d743c2e` S4 executor)

### Finding Verdicts

- **Important 1: no test citing `guidelines-check-example-files/1` caught a rule naming `guidelines-form` beside another invariant being exempted from cases.** ADDRESSED.
  - **Invariant test (`dfa9e15`, by the check author per C34 / WAY-69).** `product-guidelines/test_form_check_invariants.py:1410-1442` adds `ExampleFiles.test_a_rule_naming_guidelines_form_beside_another_without_the_others_cases_is_reported`, which cites `# invariant: guidelines-check-example-files/1`. It has five subtests:
    - a styleguide rule with no case, no good case or no bad case of `background-pair`;
    - `guidelines-form` named second;
    - a coding rule of a kind with no case of `endpoint-validates`.
    Each subtest is asserted with `assert_reported_anew`.
  - **Ordinary test (`d743c2e`).** `product-guidelines/test_form_check.py:1291-1299` adds the subtest "beside another, with no case of the other". It expects exit 1, a missing `good` and a missing `bad` `endpoint-handler` error at the *Invariant* line, and no `guidelines-form` case asked for.
  - **Rebreak.**
    - Setup: my break `slice-4-break-form-beside-exempt` (`required = [] if FORM_IDENTIFIER in named else named`, `form_check.py:968`), applied in a scratch worktree at `d743c2e`.
    - Command: `python3 -B gate/run_tests.py product-guidelines --record <scratchpad>/slice-4-fix1-rebreak.jsonl`.
    - Result: exit 1, `Ran 137 tests`, `FAILED (failures=7)`.
    - The test citing the invariant failed on all 5 subtests.
    - The ordinary test failed on 2 subtests, the new one and "with a pair of it".
    - Output: `slice-4-fix1-rebreak.txt`. The worktree has been removed, and the checkout is untouched at `d743c2e`.
  - **Fix evidence.**
    - `slice-4-fix1-product-guidelines.exit` is 0.
    - `.txt` shows `Ran 137 tests … OK`.
    - `.jsonl` holds 0 `fail` lines.

### New Breakage in the Fix Diff

None. The fix adds tests only. `form_check.py` is unchanged, and no existing assertion was weakened: the docstring of `test_form_check.py:1271` gained a sentence, and nothing was removed.

### Out-of-Scope Observations

None new. The Minor findings 1–7 of the first review remain as recorded, and none of them blocks.

### Verdict

**Fix round:** All findings addressed, no new Critical/Important breakage.

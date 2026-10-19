# Slice 4 report: the form check of test cases, and a filled product end to end

**Status:** DONE_WITH_CONCERNS. **Commit:** `1bff1ae` on `claude/gallant-albattani-3k15lc`
(parent `0607656`), not pushed. **Python:** 3.13.16 (`python3`); the repository declares 3.14.

## What I implemented

All in `product-guidelines/form_check.py` (spec §5.2 item 5, C18, C21, C33):

- **One reading of fences.** `fenced_blocks(lines)` gives every fenced block as `Fence(opening,
  fence, info, closing)`, where `closing` is `None` for a block left open to the end. It reads
  fences exactly as the old `fenced_lines` did. `fenced_lines(lines, blocks)` now derives the
  per-line code flags from those blocks. `Document` keeps both (`fences`, `code`). The info string
  is taken from the opening fence only.
- **`check_cases`** runs in `check_file` for every discipline and records under
  `product-guidelines/form_check.py::check_cases`, citing `guidelines-form/1`.
  - It skips dropped rules.
  - It reads *Invariant* with the same reference token the carrier check uses
    (`invariants_named`).
  - It acts only on rules that name an invariant other than `guidelines-form`.
  - Each fenced block is assigned to the rule it opens in with `bisect`, so the cost stays linear
    in the file.
- **`check_rule_cases`** reports, each as an error of `guidelines-form/1`:
  - **Missing case.** No `good <identifier> <path>` case, or no `bad` one, for an invariant the
    rule names, reported at the *Invariant* line.
  - **Malformed test case,** at the block's opening line. This covers a block that:
    - stands before the rule's last field;
    - is opened by anything but exactly three backticks (tildes, four backticks);
    - has an info string that is not exactly three words split by single spaces (`good` or `bad`,
      an identifier, a non-empty path), as `good x  a.ts b.ts`, `GOOD …`, `good` alone or none
      leave it;
    - is opened by the case's own former closing line after a bare fence closed the case early
      (C21).
  - **Left open,** at the opening line, for any block of the rule left open to the end of the
    file.
  - **Second case,** at its opening line, naming the line of the first.
  - **Unnamed invariant.** A case naming an invariant the rule does not name. A case naming
    `guidelines-form` in a rule that names it beside another invariant gets its own message.
  - **Refused path:** any case path the existing `refused()` rejects.
  - **Closing fence.** A case closed by anything but three backticks, at the closing line.
  - **Fence line inside a case** (C33): a line that, after any leading whitespace (`str.lstrip`,
    the same set as check_instructions' `\s`), starts with three backticks or three tildes,
    reported at that line.
    - The line is read in the pieces `str.splitlines` gives, as `check_instructions.py` reads it
      (see the weakest point below).
    - A line that closes the case under the form check's Markdown reading (three spaces of indent
      at most) is the case's end, not a line inside it.
    - So a bare three-backtick line yields the C21 malformed case. A four-space-indented bare
      fence is reported as a line inside the case.
  - The shortened good case of C21 still counts as that invariant's good case.
- **What it never does:**
  - It opens no case path, gives none to git and writes none.
  - It adds no regular expression: info strings are split with `str.split`.
- **Docstrings.** The module docstring lists the new findings. `PROGRAM`, the options and the exit
  codes are unchanged.

In `product-guidelines/test_form_check.py`:

- **New class `TestCases(Watched)`**, 18 tests, with fixtures `CASES_INVARIANTS`, which adds
  `endpoint-location` (`f58796ac`) and `guidelines-form` (`7196030f`). Both fingerprints were
  checked with `relation-model/fingerprint.py`.
- **`run_sealed()`** records every path given to `os.open`, `os.lstat`, `os.stat` and `open`, as
  well as git's arguments, with sockets refused.
- **One existing fixture fixed.** The `testing.md` fixture of
  `References.test_an_invariant_after_a_merge_is_the_branch_s_where_its_sentence_changed_there`
  names `fixture-named`, so it now gives a pair (`FIXTURE_CASES`). It was correctly reported by the
  new check.

## TDD evidence

- **RED (F4).** At `0607656` the 7 `ExampleFiles` tests fail: 118 tests, 37 failing subtests. My
  run (`slice-4-red-f4.txt`, tail only) matches S3's full output, `slice-3-product-guidelines.txt`,
  which lists all 7 by name.
- **RED (ordinary).**
  - Command: `cd product-guidelines && python3 -B -m unittest test_form_check.TestCases`, with the
    17 new tests on the unchanged code.
  - Result: exit 1, 47 failing subtests (`slice-4-red-ordinary.txt`). Among them is
    `test_a_rule_naming_an_invariant_with_no_case_is_an_error`, where a rule with no blocks
    passed.
  - Every failure is an exit 0 where 1 is expected, or a missing error or record line. None is a
    harness fault.
  - Six tests passed while RED. Each checks existing or allowed behaviour:
    - the over-1 MiB refusal (`read_untrusted`);
    - the 1 MiB path;
    - the 200 KiB path;
    - the `guidelines-form`-alone and `guidelines-form`-beside controls.
- **GREEN.** Same command after the change: 17 tests OK. F4 `ExampleFiles`, `Fixtures` and
  `CodingFixtures`: 11 tests OK.
- **Second cycle, weakest point.**
  - RED: `test_a_fence_after_a_line_break_python_splits_lines_on_inside_a_case_is_an_error` failed
    7 of 7 subtests (exit 0 each).
  - GREEN after reading lines in `splitlines` pieces: 18 tests OK.

## Checks

All outputs are in `docs/task-cycles/coding-guidelines/reports/sdd/`. Every
check below was run on `1bff1ae`.

| Check | Exit | Result | Output |
|---|---|---|---|
| `python3 -B gate/run_tests.py product-guidelines --record …/slice-4-product-guidelines.jsonl` | 0 | 136 tests OK; record only `pass`, `guidelines-check-example-files/1` 11× `pass` | `slice-4-product-guidelines.txt`, `.jsonl`, `.exit` |
| `python3 -B product-guidelines/form_check.py --record .runs/guidelines-form.jsonl` | 0 | pass (the-way holds no `guidelines/`) | `slice-4-form-check.txt` |
| `python3 -B product-guidelines/form_check.py --merge-onto none --record .runs/guidelines-reference.jsonl` | 0 | `check_merged_references` `unchecked`, as expected | `slice-4-form-check-reference.txt` |
| `python3 -B gate/run_tests.py gate --record …/slice-4-gate.jsonl` | 0 | 98 tests OK | `slice-4-gate.txt`, `.jsonl`, `.exit` |
| End to end (below) | 0 / 0 / 0 | no error, no dead path, no import | `slice-4-e2e.txt`, `slice-4-e2e-make_product.py` |
| Deliberate breaks of my own (4) | — | each break turns tests red | `slice-4-breaks.txt` |
| Weakest point (below) | 0 with the change, 1 without | 0 mismatches against 105 | `slice-4-weakest.txt`, `slice-4-weakest.py` |

**Turned green, by name (F4 RED list):**

- `test_a_rule_naming_an_invariant_without_its_good_or_bad_case_is_reported`
- `…two_invariants_without_the_cases_of_one_is_reported`
- `…second_case_of_one_kind_for_an_invariant_is_reported`
- `…case_naming_an_invariant_its_rule_does_not_name_is_reported`
- `…case_whose_path_is_out_of_the_repository_is_reported`
- `…line_that_would_open_a_fence_inside_a_case_is_reported`
- `…another_fenced_block_in_a_rule_carrying_cases_is_reported`

With them the whole `product-guidelines` run passes.

**End to end** (`slice-4-e2e.txt`): a temporary product built by `slice-4-e2e-make_product.py`.

- **What it holds:**
  - a part map of four parts;
  - a log ABC-01…04, where ABC-04 designates `` `src/api/orders/route.ts` `` of the kind
    `` `endpoint` ``;
  - invariants `lint-clean`, `format-clean`, `audit-clean`, `endpoint-validates`,
    `endpoint-handler` and `guidelines-form`;
  - `guidelines/coding.md` with the three standing checks kept, each with its pair;
  - `guidelines/coding-endpoint.md` with exemplar, copy and do-not-copy rows and two rules. One
    rule names `endpoint-handler` beside `guidelines-form` and gives the pair of the first only;
  - a root `AGENTS.md` naming `guidelines/coding.md`.
- **Results:**
  - `form_check.py --record`: exit 0, 0 errors in every report.
  - `--merge-onto none`: exit 0, 1 unchecked.
  - `check_instructions.py <product>`: exit 0, 0 error, 0 warn, 2 info. It followed
    `guidelines/coding.md`.
  - A variant naming `guidelines/coding-endpoint.md` too: exit 0.
- **Two controls on the same product:**
  - removing the `bad lint-clean` case gives exit 1 at *Invariant*;
  - an indented `~~~` inside a case gives exit 1 at that line.

**Deliberate breaks** (`slice-4-breaks.txt`; the tree was restored with `git checkout` after
each):

- Inner-fence check off: 22 failing subtests, F4 5 of 7.
- Missing-case report off: 25 failing.
- `refused()` on case paths off: 20 failing, F4 9 of 9.
- Open-block report off: 1 failing (the ordinary test only, as C32 foresaw).

**Not run:**

- `installation`, which the brief does not name. Its 4 `NAMES` tests stay RED until S11. Its only
  use of the form check runs it on a product with no guidelines and on one with no header lines,
  which this change does not touch.
- Behaviour on Python 3.14.

## Crafted input covered (spec §5.3 bullets 4, 5, 7, and the carried items)

- **Fences:**
  - a fence left open to the end, at its opening line;
  - a tilde fence and a four-backtick opening (malformed);
  - a four-backtick fence closing three, at that line;
  - fence-opening lines inside a case: `~~~`, `~~~ts`, ```` ```ts ````, three spaces +
    ```` ```ts ````, four spaces + ```` ``` ````, eight spaces + `~~~ts`, a tab + ```` ```ts ````,
    two spaces + `~~~`, and a no-break space + ```` ```ts ````;
  - the same after `\r`, ` `, ` `, `\x85`, `\x0b`, `\x0c` and `\x1c`;
  - a bare fence inside a `good` case, reported as a malformed case at the former closing line,
    with the good case still counting;
  - an info string on a closing fence, reported as a line that opens a fence.
- **Info strings:** `good`; `good <id>`; `good x  a.ts b.ts`; three-word-plus forms; `GOOD`; an
  identifier that is no identifier; `sample …`; `ts`; none.
- **Invariants named:**
  - a block naming an invariant the rule does not name: `endpoint-location`, `lint-clean`,
    `guidelines-form`;
  - a rule naming two invariants with the pair of one only, and its control with both;
  - a second case of one kind;
  - a block before the fields end;
  - `guidelines-form` alone without blocks, alone with blocks, beside another invariant with only
    the other's pair (all pass), and beside another with a pair of it (error).
- **Size and paths:**
  - a 1 MiB info string, as a path (passes, unopened) and as an identifier (reported, printed cut);
  - a file just over 1048576 bytes of cases, refused unread with no path seen;
  - every crafted path of S3's `crafted()` as a case path, each refused at the opening line. The
    200 KiB relative path passes.
  - The valid path is never given to git, opened or looked at. Each run takes under 30 s (about
    1 s) with no socket.

## Changed files (`git diff --numstat 0607656..HEAD`)

```
192	18	product-guidelines/form_check.py
390	3	product-guidelines/test_form_check.py
```

## Sharpness inputs (from the diff)

- **Parts touched:** `product-guidelines` only (`product-guidelines/**`).
- **Trust-boundary file touched:** `product-guidelines/form_check.py`, which the part map names as
  the part's trust boundary (WAY-48).
  - No new file read, git call, socket or write.
  - No new regular expression.
  - Every new loop is linear in the file: blocks are assigned with `bisect`, each line belongs to
    at most one block, and the `seen` dictionary is constant-time.
  - Values from the file are printed through `shown()`.
- **Irreversible operations:** none. Nothing pushed.

## Questions and choices (each settled as a choice of how; none open)

1. **A rule naming `guidelines-form` alone, with fenced blocks, passes unchecked.**
   - Evidence: spec §5.2 item 5 and `guidelines-check-example-files/1` scope the check to rules
     naming an invariant other than `guidelines-form`. Spec §5.2 says such a rule "needs no
     blocks". The template's "with no test-case blocks" describes what the rule gives, and §5.2
     gives the form check no finding for it.
   - The ordinary test pins this reading ("alone, with blocks" passes).
   - In a rule naming `guidelines-form` beside another invariant, a `guidelines-form` case is
     reported, since it is not one of "those two forms" (S1 review minor 3).
   - If the orchestrator reads the template as asking the check to report blocks in a
     `guidelines-form`-only rule, that is a few lines and one test flip.
2. **A case's closing fence other than three backticks is reported** at its line. This reads the
   template's "the outer fence of a case is three backticks" as covering both fences. It is the
   defined report for §5.3's "a fence of four backticks closing three".
3. **Indentation.** An opening fence with up to three spaces of indentation counts as a case,
   following the form check's existing Markdown reading. Lines inside a case are judged after any
   leading whitespace (C33). The difference is handled on purpose, as the dispatch asked: a line
   that the Markdown reading takes as the closing fence ends the case; any other line starting
   with a fence after any whitespace is an error.
4. **Info-string words.** The info string is stripped and split on single spaces into exactly
   three non-empty words. A tab inside it makes it malformed, or makes the path refused as not
   printable.
5. **Several errors for one block.** A malformed block left open gets both errors at its opening
   line. Missing cases are reported at *Invariant*, not at the heading.

## Weakest point (WAY-164)

**Requirement:** C33, as the template states it. A case the form check accepts keeps
`instruction-files/check_instructions.py` in step, so that script switches between code and text
on no line of the case's text.

**Why it was weak:** the form check splits a file only at `\n`, while `check_instructions.py`
uses `str.splitlines()`. That also breaks lines at `\r`, `\x0b`, `\x0c`, `\x1c`–`\x1e`, `\x85`,
` ` and ` `. So a case line `x ```ts` passed the first version of my check while
check_instructions toggled on it.

**Check:**
- `slice-4-weakest.py` is a seeded fuzz of 20,000 cases. Inner lines are built from every Unicode
  whitespace character, every `splitlines` break, backticks, tildes and text.
- For each case it runs `Document` and `check_cases` in process and counts check_instructions'
  `FENCE` toggles over the case's span.
- A case with no finding must toggle exactly on its opening and closing lines.

**Result:**
- With a copy of the code that reads lines whole: 105 mismatches, exit 1.
- After the fix: 0 mismatches over 14,914 clean cases, exit 0.
- The fix is pinned by the ordinary test named above.

## Self-review findings

- The module docstring and `check_cases` docstring were rewrapped to the file's width. The new
  lines of code stay within 99 characters; the long lines awk shows in the test file are UTF-8
  byte counts of the copied `GUIDELINES_FORM` sentence.
- `fenced_lines` changed signature. Its only caller is `Document`.
- `check_cases` re-reads each rule's fields instead of sharing them with `check_rules`. The cost is
  a few lines of duplication, kept so that its record entry stays separate.

## Concerns

1. Choice 1 (`guidelines-form`-only rule with blocks passes) is a reading. The reviewer should
   confirm it.
2. **The open-to-end clause.** F4 left the clause "every such block left open to the end of the
   file" without an invariant test (C32). Only the ordinary test catches its break, as
   `slice-4-breaks.txt` shows.
3. **Tab before a fence.** Under the existing Markdown reading, a tab-indented bare ```` ``` ````
   closes a case. CommonMark would count the tab as four columns and not close it. Behaviour is
   consistent with `check_instructions.py`, which toggles on it too, so nothing is unprotected.
   But it is a quirk of the shared fence reader that I did not change.

## Fix round 1 (review finding: cases still due beside `guidelines-form`)

**Commit:** `d743c2e` on top of `dfa9e15` (the check author's invariant-test commit). It changes
`product-guidelines/test_form_check.py` only: +12/−1. No code changed, because the test showed no
defect.

**What changed.** `TestCases.test_a_rule_naming_guidelines_form_needs_no_case_and_takes_none_of_it`
gains the subtest "beside another, with no case of the other".

- **Input.** The rule's *Invariant* reads `guidelines-form@7196030f · endpoint-handler@8c2ca199`
  and all its cases are removed.
- **Expected.** Exit 1, with a "gives no `good endpoint-handler <path>`" error and a "gives no
  `bad endpoint-handler <path>`" error, both at the *Invariant* line. No case of
  `guidelines-form` is asked for.
- **Docstring.** It names the break this catches: naming `guidelines-form` taken as exempting the
  whole rule.

**Tests:**
- The test passes on the S4 code (1 test OK).
- Deliberate break, with the tree restored afterwards: a rule naming `guidelines-form` taken as
  exempt whatever else it names. The new subtest fails, beside the existing "with a pair of it"
  subtest (`slice-4-fix1-break.txt`).

**Command:**
`python3 -B gate/run_tests.py product-guidelines --record …/slice-4-fix1-product-guidelines.jsonl`
gives exit 0, 137 tests OK, and no `fail` line in the record. Output:
`slice-4-fix1-product-guidelines.txt`, `.jsonl` and `.exit`, in this folder.

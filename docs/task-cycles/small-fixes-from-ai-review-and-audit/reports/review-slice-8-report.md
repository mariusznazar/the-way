PASS f52c565772f125fe5ebb17f0a0fb98ee7e56fe6e

# Review of slice 8

Range: `ca55d4e880c7f7f3b3b8b3863d93e335b90c35b9..f52c565772f125fe5ebb17f0a0fb98ee7e56fe6e`, one
commit (`f52c5657`). `git rev-parse HEAD` in the worktree is that head. Files changed:
`process-audit/SKILL.md` (+52/-12) and `process-audit/audit_count.py` (+22/-8), and no other.

## Findings

### Critical

none

### Important

none

### Minor

1. **`process-audit/SKILL.md:244-254`: the text says Q2 of a version is the sums, but the rows
   for each version do not show the sums.** The bullet "*The rows per version* ... a series of the
   count of remarks shows Q1 and Q2 of each version" is followed by "Q2 of a group is the sum of
   the slices planned and the sum of the slices returned too large over the cycles whose plans are
   read, with `yes`, `no` or `unknown` as the answer those sums give". The definition of a group
   includes a version ("Q1 of a group of cycles — a version, a whole series, one side of a
   comparison"). But the row of a version that `version_analysis.py:1026-1035` writes under
   `COUNT_HEADER` (`audit_report.py:73-80`) holds *Plans read* and the Q2 answer only. It has no
   *Slices planned* and no *Slices returned too large*, while the image
   (`COUNT_IMAGE_HEADER`, `audit_report.py:57-64`) and each side of a comparison have both. So a
   session that reads the skill looks for sums in the rows of the versions that are not there. The
   wording follows WAY-417 word for word, which is why the text and that code differ: the code that
   writes the version rows belongs to slice 6 and lies outside this range. A fix in the text would
   say that the rows of a version give *Plans read* and the answer of Q2, and the image and the
   sides also give the sums. I grade it Minor because nothing here would lead a human to a wrong
   conclusion: the sums are missing from the result, and no wrong figure is shown.
   Evidence: `audit_report.py:57-64`, `73-80`; `version_analysis.py:1016-1035`.

2. **`process-audit/SKILL.md:276-277`: "the series whose rows give nothing but `unknown`" no
   longer fits a series of the count of remarks.** Q1 is now always the three numbers
   (`series_summary.py:91-97`). So the Q1 cell of a version is never the word `unknown`, even when
   every cycle of the version answers unknown (`yes 0 · no 0 · unknown 3`). Read literally, the
   sentence never groups a series of the count of remarks. Read for its intent, it groups the series
   whose cycles answer nothing. The slice changed the form of Q1 in this same paragraph and left
   this sentence as it was. A clause such as "for Q1, a series whose every version reads
   `yes 0 · no 0 · unknown n`" would settle it. Minor: the session can still tell what the sentence
   means.

3. **`process-audit/audit_count.py:201`, and also `:157` and `:160`: docstring lines over the
   width of 100 that the rest of the text keeps.** Line 201 is 146 characters long. The added text
   ends at "The count reads" on line 200, and the old line ("these measures and shows them with a
   median and a comparison for each version, because the numbers lie in the records of cycles,
   which the session") was joined into one long line without rewrapping. Lines 157 and 160 are
   101 and 104 characters. The formatter does not reflow strings and the linter does not enforce
   the width here: the base already had docstring lines of 158 and 172 characters, and the tests
   pass. So this is layout only. Minor.

No finding contradicts a settlement, and none blocks.

## What was verified

- **Trust boundary, `process-audit/audit_count.py`:** no line of its code changed.
  - The syntax trees of the base and the head, without the module docstring, are equal. I took
    `git show` of both versions and compared `ast.dump` of each tree with its first statement
    removed: `code equal: True`, `doc differs: True`.
  - `git diff -U0` gives three hunks, at head lines 146-160, 193-194 and 197-201. The docstring
    closes at line 354. No comment or code line lies in any hunk.
- **The docstring is now true against the code.**
  - Image of a series of the cost: its cycles, the cycles with a known cost, and their median
    (`cost_image`).
  - Image of a series of the count of remarks: its cycles, Q1, the plans read, and Q2
    (`count_image`). The docstring folds the two sums into "Q2", as WAY-417 defines Q2.
  - An image has no Q3 and no *Falls*.
  - A comparison has two sides, before and after. Each side shows what the image shows, and Q3 or
    *Falls* stands beside the side after only (`side_rows`, `NO_ANSWER`).
  - Q1 of a group is `yes n · no n · unknown n` (`q1_text`).
  - Q3 in a comparison compares the median after with the median before (`falls_between`).
  - For the gate times, a comparison exists only where runs compared stand on both sides of the
    total (`gate_comparison`, `series_summary.py:303`).
  - The rest of the docstring is unchanged.
- **Point 4 of step 3 against the task (points 6 and 7, and the answers at lines 56-74):**
  - The image and the comparison come first, and the rows of the versions come last.
  - Each series is taken one at a time, with the line that says why it begins where it does.
  - The rule "a number of one kind of series is never set beside a number of the other" stays. The
    rule against comparing one week with the week before stays in the rules of working
    (`SKILL.md:74-77`).
  - Q1, Q2 and Q3 are worded as WAY-417 words them.
  - Comparisons cover only the fixed issues with a fix commit, in the order of the register
    (`version_analysis.py:1006`, `compare_series`).
  - A version that git cannot place stands on neither side, and *Unknown values* gives the reason
    (`fix_sides`).
  - The count of remarks gives the two sides and no answer of its own (`count_comparison`).
  - The text says a change with no fixed issue in the register gets no comparison, as WAY-339 and
    the answer at task line 61 settle.
- **The sentence added to "Measures are compared inside a series only" (`SKILL.md:61-65`)** says
  what task point 7 asks. "Those files and dates" points back to the list in the sentence before.
  "Only" makes the limit a necessary condition, which is correct: another change of those files
  between two versions also splits the series.
- **Against WAY-339 *Verification* (violates):** the text does not give the image Q3 or a fall. It
  does not use dates to place cycles before or after a fix, and it gives no comparison to a change
  that has no fixed issue. WAY-350: runs not compared are shown apart and never compared.
- **Guidelines:** `coding.md` and `coding-measuring-report.md`. The only code change is the
  docstring, so the rules on linter, formatter, size, start and end of a script, and missing
  fields are not touched beyond Minor 3. No invariant test changed.
- **The author's own-work check** names the riskiest requirement correctly: that the text says
  exactly what slices 6 and 7 write. Its reading of the writers did not catch Minor 1 (no sums in
  the rows of the versions) or Minor 2.

## Declined to judge

- `process-audit/version_analysis.py:1026-1035`: the row of a version in a series of the count of
  remarks has no sums of slices, which WAY-417 calls Q2 of every group. That is code of slice 6,
  outside this range. I record it only as the cause of Minor 1, and whether the code departs from
  WAY-417 is for the review of that slice or of the whole change.
- `process-audit/audit_count.py:128` ("in which the answers Q1 and Q2 are compared") and `:338`
  ("the section *Measure versions* gives them per version"): these lie outside the two paragraphs
  the slice may change, and they are not wrong enough to matter here.
- `process-audit/SKILL.md:154-160`, the opening of step 3 ("*Measure versions* gives their medians
  per version ... series by series"). It does not mention the image or the comparisons. The slice
  names point 4 only, and the author left this sentence as it was on purpose.

## Checks run

- `git rev-parse HEAD` / `git rev-parse f52c5657`: both `f52c565772f125fe5ebb17f0a0fb98ee7e56fe6e`.
- `git log ca55d4e8..f52c5657`, `git diff ca55d4e8..f52c5657`, `git diff --stat`: exit 0, one
  commit, two files.
- AST comparison of `process-audit/audit_count.py` at base and head with the docstring removed
  (`python -B -I -c` with `ast.parse`/`ast.dump`): exit 0, `code equal: True`.
- `git diff -U0 ca55d4e8..f52c5657 -- process-audit/audit_count.py | grep '^@@'`: three hunks, all
  inside the docstring, which ends at line 354.
- `awk` length scan of the docstring at base and head: exit 0. It found the lines over 100 named
  in Minor 3.
- `python -B gate/run_tests.py process-audit`: exit 0, 342 tests OK.
- `python -B gate/run_tests.py agent-instructions`: exit 0, 53 tests OK.
- `git status --short` after the runs: empty, so the worktree was unchanged.
- Not run: the full gate, which is the cycle's own run, and a rendered result of the count on a
  test repository. I compared the text with the writers by reading them.

## Reaches beyond the handoff

- `process-audit/version_analysis.py:880-1044` (`fix_sides`, `compare_series`,
  `process_versions`, `count_rows`, `cost_rows`). I needed it to check three claims of the text:
  that a comparison is made only for each fixed issue of the register in its order, that a
  version git cannot place stands on neither side, and that the rows of a version give Q1 as
  numbers. The two files the handoff names do not decide those claims.
- `process-audit/audit_count.py:120-210` and `:325-354`, the rest of the docstring around the
  changed paragraphs. I read them to confirm that nothing else in the docstring contradicts the
  new paragraphs and to find where the docstring ends.

## Working copies

- `.runs/review-slice-8/` held
  the base and head copies of `audit_count.py` for the AST comparison and the logs of the two test
  runs. I removed it with `rm -rf` on its full path, and it is gone. Nothing remains.

**Unread material:** `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md` lines 37-38,
56-74 and 111-112, read as the handoff quotes them word for word, not by opening the file. The
plan's *Foundation entries* Rows 1-3, read as the entries in `foundations/decisions.md` (WAY-339
8607-8758, WAY-417 8995-9038), as the handoff directs. Everything else named was read whole:
WAY-339, WAY-350, WAY-417, both invariants, the part-map entry, both guideline files,
`process-audit/audit_report.py` and `process-audit/series_summary.py`.

**Searches not found or unclear:**

- The handoff gives WAY-350 as `8759-8795`, and the slice's *Read* gives `8747-8783`. WAY-350
  stands at 8760-8795. I read it whole there.
- None other.

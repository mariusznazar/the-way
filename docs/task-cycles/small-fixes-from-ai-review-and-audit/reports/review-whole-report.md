FAIL f52c565772f125fe5ebb17f0a0fb98ee7e56fe6e

# Review of the whole change — small-fixes-from-ai-review-and-audit

Range `268b2b074691a331ed8db136343b4060bdd44539..f52c565772f125fe5ebb17f0a0fb98ee7e56fe6e`, 12
commits, 30 files. `git rev-parse HEAD` in the worktree printed the head given. Trust boundary: yes
(`task-cycle/gate_times.py`, `process-audit/audit_count.py`); irreversible operation: none.

## Findings

### Critical

none

### Important

#### I1 — The foundation check reports 12 errors at the head, so the test of the invariant `own-foundation-check-report` fails and the gate is red

- **Place:** the `decision:` lines of `process-audit/test_process_versions.py` at lines 1745,
  1765, 1778, 1975, 1991, 2013, 2050, 2080, 2095, 2129, 2159 and 2176.
- **What is wrong:** each of these lines cites a decision by a quotation the foundation check
  refuses: a passage of the *Verification* and not of a binding sentence (1745 `WAY-417 "the rows of
  the versions of a series give Q1 as a word while its image"`, 1975 `WAY-417 "on each side of a
  comparison before and after a fix"`), a quotation with an ellipsis (1765 `WAY-417 "The answer Q1
  of the audit ... is given for each group of cycles"`), a sentence of WAY-339 quoted as WAY-417's
  (1778), a quotation that does not begin a sentence (1991, 2050, 2080, 2095, 2129), a quotation
  broken over two lines (2013, 2159) and text after the quotation (2176). `elements/common/
  foundation_check.py` lists all twelve and ends with exit code 1.
- **Why it matters:** the invariant `own-foundation-check-report` (method `test`) says the check,
  run with no switch on the-way as a commit leaves it, reports no error; its test
  `elements/common/test_foundation_check.py:2504`
  (`FoundationCheckTest.test_the_way_foundation_check_reports_no_error`) fails at the head, so
  `python -B gate/run_tests.py elements/common`, and the full gate, fail. No slice from 6 on ran
  the foundation check or the `elements/common` directory; the slice checks named
  `process-audit` and `agent-instructions` only. The change cannot be merged with a red gate.
- **Evidence:** `python -B elements/common/foundation_check.py` at the head: exit 1, `12 errors`
  (the twelve lines above). The same check at `3b34de03` (slice 5): `0 errors`; at `0ee90d8e`: 2;
  at `29a1c6ae`: 3; at `ca55d4e8`: 12. The invariant's test at the head: exit 1, `FAILED
  (failures=1)`; at the base: exit 0.
- **Slice:** spans slice 6 (`0ee90d8e`, `29a1c6ae`: lines 1745, 1765, 1778) and slice 7
  (`ca55d4e8`: the other nine).
- **Fix direction:** each `decision:` line quotes, on its line, the start of a binding sentence of
  the decision it names, word for word and with nothing after the closing quote; for WAY-417 the
  sentences begin "The answer Q1 of the audit, whether a contradiction", "The answer Q2 of such a
  group", "The answer Q3, whether the median cost" and "The image of a series, which sets no two
  groups"; for WAY-339 "The audit shows each series as an image of all its cycles" and "That
  comparison is made for each fixed issue of the register". Then run the check and
  `python -B gate/run_tests.py elements/common`.

Contradiction: yes — invariant `own-foundation-check-report`

#### I2 — WAY-417, which the change writes, says that Q2 of every group, a version included, is the two sums with their answer; the row of a version gives the answer alone

- **Place:** `foundations/decisions.md:9002-9004` (WAY-417, the Q2 sentence);
  `process-audit/version_analysis.py:1016-1035` (`count_rows`) with
  `process-audit/audit_report.py:73-80` (`COUNT_HEADER`); the texts that repeat the sentence,
  `process-audit/SKILL.md:244-254` and `process-audit/audit_report.py:176-179`.
- **What is wrong:** WAY-417 reads "The answer Q2 of such a group is the sum of the slices planned
  and the sum of the slices returned too large over its cycles, with the answer that those sums
  give", and "such a group" is each of "the cycles of one version of the process, the cycles of a
  whole series, the cycles on one side of a comparison". The image and each side of a comparison
  give *Slices planned* and *Slices returned too large*; the row of a version gives *Plans read* and
  the answer, with no sums. The skill and the result's own prose then tell the reader that Q2 of a
  group, a version among them, is the two sums, and a reader of the rows of the versions finds no
  sums. The entry also says "over its cycles" where the code sums over the cycles whose plans are
  read.
- **Why it matters, and why Important:** WAY-263 — the change's files fail to do what an entry the
  change itself writes requires. The task's answer gives Q2 as "sumy odcinków planowanych i zbyt
  dużych z odpowiedzią z tych sum, jak dziś dla wersji", and the plan's slice 6 keeps "the Q2 and Q3
  cells ... of the versions as they are", so the rows of the versions follow the task and WAY-417's
  sentence states it more broadly than the task settles. The review of slice 8 graded the text side
  Minor and left the code against WAY-417 to this review; nothing shows a wrong figure, but the
  entry and the code disagree.
- **Evidence:** WAY-417 at `foundations/decisions.md:8998-9004`; the version row written at
  `version_analysis.py:1026-1035` holds six cells, `[commit, day, cycles, Q1, plans read, answer]`;
  the image (`series_summary.py:151-165`) and the sides of a comparison (`count_comparison`,
  `series_summary.py:262-270`) hold the sums. The test
  `test_the_rows_of_the_versions_stay_and_give_q1_as_numbers_of_their_cycles`
  (`test_process_versions.py:1744-1762`) asserts the six cells of a version row.
- **Slice:** spans the plan's *Foundation entries* (`a946862b`, the Q2 sentence of WAY-417) and slice
  6 (`0ee90d8e`, the rows of the versions); slice 8 (`f52c5657`) repeats the sentence in the skill.
- **Fix direction, two ways:** (a, recommended) narrow the sentence of WAY-417 to what the task
  settles — the answer Q2 of a group is the answer that the sum of the slices planned and the sum of
  the slices returned too large over its cycles whose plans are read give, and the image of a series
  and each side of a comparison show the two sums beside it — and bring `process-audit/SKILL.md`
  and the prose of `audit_report.py` in line; no code and no test changes. (b) Add the two sums as
  columns of the row of a version: one form in every row, but a change of the result that the task
  did not ask for and of the expected values of every test of a version row of the count.

Contradiction: yes — WAY-417

### Minor

Every Minor finding below lies within the task unless it says otherwise.

1. **`task-cycle/gate_times.py:233-248` (`Times.nested`, the cap `taken = min(lines, directories,
   surplus)`) — from the review of slice 2, M1, kept.** The planned rule lets each earlier summary
   line take up to its own `<m>` lines, while a nested run in a failure message has only `<m> - 1`
   lines at the start of a line (its first directory stands after text); two directories that each
   print a nested run (the review's case A gave `[['other', '0.002'], ['gate1', '0.001'], ['b',
   '0.600']]` for expected `other 0.002`, `gate1 0.500`, `gate2 0.600`), or a nested output cut off
   before its summary line beside a whole one (case C), are misread as point 8 says they must not
   be. Minor: in the-way only `gate/` prints a nested runner output, so the case cannot arise today,
   and the rows concerned are of failed runs, which WAY-350 does not compare. It is a defect of the
   rule the plan mandates; the direction the slice review gives (start a nested run after the last
   line of its segment that holds `== ` after text) changes the planned rule.
2. **`task-cycle/gate_times.py:75`, `:165`, `:167`, `:205-209` (`PIECES_KEPT = 100`,
   `Piece.own`, `Piece.after`) — from the review of slice 2, M2, kept.** The ceiling of memory for
   crafted output grew about four times (100 pieces keeping two copies of a `Ran` time of up to
   `LINE_LIMIT` each, where 50 blocks kept one). It stays bounded, as the plan requires; cutting the
   kept seconds at a length no real time reaches, or keeping one string where both fields come from
   one line, would bring it back.
3. **`task-cycle/gate_times.py:82-84` (`SUMMARY` uses `\d`) — from the review of slice 2, M3,
   kept.** A crafted summary line with Unicode digits (`٣ tests in ٣ directories; every directory
   passed`) is read as a summary line and takes a real directory as nested; the effect is a wrong row
   of a crafted output, no failure and no change of the exit code. `[0-9]{1,9}` would match what
   the runner prints and nothing else, as `RAN` (`:80`) does.
4. **`process-audit/SKILL.md:276-277` — from the review of slice 8, Minor 2, kept.** "the series
   whose rows give nothing but `unknown`" no longer fits a series of the count of remarks, whose Q1
   cell is always three numbers (`yes 0 · no 0 · unknown 3`); read literally it never groups such a
   series. A clause such as "for Q1, a series whose every version reads `yes 0 · no 0 · unknown n`"
   settles it.
5. **`process-audit/audit_count.py:201`, `:157`, `:160` — from the review of slice 8, Minor 3,
   kept.** Docstring lines of 146, 101 and 104 characters, line 201 an old line joined without
   rewrapping. Layout only. The same holds for the new string at `process-audit/audit_report.py:176`
   (over 100 characters) and for the Markdown files of point 9 after the rename:
   `elements/common/reaching_another_skill.md:6` is one line of 533 characters and `:3` of 131, and
   the replaced paragraph of each of the 15 skills has a line of 107 to 115 characters (the longer
   path was put in by a substitution, not rewrapped); `task-cycle/skill/return_step.md:9-11` is
   rewrapped so that line 11 holds three words.
6. **The review of slice 8, Minor 1 (`process-audit/SKILL.md:244-254`, Q2 of a version as the
   sums), is taken into I2** and is not a finding of its own here.
7. **`process-audit/series_summary.py:273-293` (`mechanism_comparison`) — from the report of
   executor 7, a concern graded here.** A comparison of the mechanism measures stands wherever cycles
   stand on both sides of a fix, also where no cycle on either side gives a value, and then it writes
   15 pairs of rows of `0` and `unknown` for that issue, in each such series, and 15 unknown values
   (grouped by `unknown_field` into 15 pairs). The task asks for a comparison "w każdej serii, w
   której po obu stronach poprawki stoją cykle", so the code follows it word for word; but a reader
   of a register with many fixed issues gets many tables of nothing, the noise the task's *Need*
   names. A version with no value already gets one row with `—`; the same for a comparison, or a
   comparison only where a value stands on both sides, would cut it.
8. **`process-audit/audit_report.py:181-182` — the prose says "*Unknown values* says why an answer
   is unknown", but an unknown Q2 or median of an image, and an unknown Q2 of a side of a comparison
   of the count, give no line of *Unknown values*** (only the rows of the versions and the verdicts
   of the comparisons do: `count_image` drops `PlanSums.why`, `series_summary.py:155-165`). The
   reason follows from the versions' own lines, so a reader can find it; the sentence says more than
   the result holds.
9. **`process-audit/test_audit_count.py:304` (`AuditCountCase.section`) — from the report of
   executor 6, graded here.** The base helper reads every table line under a series heading, which
   is wrong for a series that now opens with an image; its only users are in
   `process-audit/test_process_versions.py`, where `VersionsCase.section` (`:91`) overrides it. A
   helper of the shared test case that no test can use as it stands.
10. **`foundations/part_map.md:67-75` (`elements-common`) — the part answers for "the way of working
    shared by foundation-entry skills", while `elements/common/reaching_another_skill.md` now serves
    the nine skills of `project-level`, `product-guidelines` and `foundation-review` as well.** The
    plan's *Choices* leaves it to the return step (WAY-11 compares the part map of the touched
    parts with the code); named here so that the return step does not miss it.

No Minor finding lies outside the task.

## Out of scope

none beyond **Declined to judge**.

## Declined to judge

- `process-audit/audit_count.py:128` ("A series of the count of remarks, in which the answers Q1 and
  Q2 are compared") and `:338` ("the section *Measure versions* gives them per version"): outside the
  paragraphs the task and the plan change, and still true enough of what the result holds.
- `process-audit/SKILL.md:154-160`, the opening of step 3: it names the rows per version and not the
  image or the comparisons; point 6 of the task names point 4 of step 3 only.
- The number of git calls of the comparison (executor 7's concern 2): one `merge-base
  --is-ancestor` per pair of a version and a fix, cached across the four kinds; not measured on the
  real register, and the count runs at night, so no requirement of the task reaches it.
- The three pointers to `hand_over.md` in `project-level/plan/skill/` (`SKILL.md:81`,
  `assign_entries.md:15`, `existing_plan.md:14`): they name `project-level/plan/skill/hand_over.md`,
  a file that exists and is no part of point 9 (executor 4's first concern, withdrawn by the rename).

## Against the task, point by point

- Points 1–3 (`elements/environment-facts/template.md:109-113`, `task-cycle/skill/return_step.md:7-11`,
  `task-cycle/record_template.md:204-207`): the wordings stand character for character as the task's
  "będzie" gives them; WAY-84, WAY-11, WAY-33 and `elements/common/way_of_working.md` are unchanged.
- Point 4: the image of each series of the four kinds stands under the series' heading and before
  its rows per version (`audit_report.series_lines`), with no Q3 and no fall; Q1 of a version is the
  three numbers, and the line of *Unknown values* for a version's Q1 is gone while each cycle's own
  reason stays. Q2: see I2.
- Point 5: a comparison for each issue whose *Fate* is `fixed` (the register refuses one whose *Fix*
  is no full hash, `problem_register.py:148`), inside each series, the side decided by
  `Ancestry.holds` and never a date, a version git cannot place on neither side with its reason;
  Q3 for the cost, the fall for the mechanism measures and the gate times over the runs compared,
  the count of remarks with the two sides and no verdict; for the gate times only where runs
  compared stand on both sides of the total.
- Points 6–7 (`process-audit/SKILL.md:52-77`, `:225-296`): the image and the comparisons first, the
  rows per version after; the limit of the comparison for the count of remarks stated.
- Point 8: `task-cycle/gate_times.py` reads the nested runner output as the plan gives and
  `task-cycle/test_gate_times.py` holds the case (`NestedRunTest`); see Minor 1–3.
- Point 9: the hand-over stands once in `elements/common/reaching_another_skill.md`, the 15 skills
  name it, `git grep "read as a file, not called"` finds it alone outside the generated entry
  points; WAY-127's *Verification* line is reworded and its binding paragraphs are unchanged; the
  orchestrator's one session (`reports/point9-check-tool-calls.txt`) read
  `elements/decisions/skill/SKILL.md`, the shared file and `elements/invariants/skill/SKILL.md` by
  its path, with no call of the skill tool. It says nothing of the other fourteen skills.
- *Settlements to record*: rows 1 and 2 stand as the two sentences of WAY-339
  (`foundations/decisions.md:8628-8634`), row 3 as WAY-417; see I2 for WAY-417's Q2 sentence.
- Slices without a review of their own, judged here: the plan's *Foundation entries*, slice 1 (the
  moved block is byte for byte the base's lines 4227-5709, the kept file differs from the base only
  by two trailing blank lines, 238 test methods before and after), slices 3, 4 and 5 (prose, as
  above), slices 6 and 7 (I1, I2, Minor 7–9). The executors' own-work checks named the right weak
  points but none ran the foundation check, which would have caught I1.

## The structure of the code

`python -B task-cycle/change_file_sizes.py` (exit 0): `process-audit/version_analysis.py` 1056 →
1067, `process-audit/audit_report.py` 558 → 657, `process-audit/series_summary.py` new, 325,
`task-cycle/gate_times.py` 335 → 450, `process-audit/audit_count.py` 871 → 885 (docstring only).
The size invariant's test passes on the base and on the head, so nothing was pushed over a
threshold. The largest functions the diff reaches: `audit_report.versions_lines` 59 → 80 lines (its
prose), `measure_versions_lines` 59 → 70, `version_analysis.mechanism_rows` 50 → 52, `gate_rows`
49 → 50, `process_versions` 45 → 48; under 110. No function lost its last user
(`contradiction_of` and `too_large_of` were removed with their callers); the test helper of Minor 9
is the one piece left with no use as it stands. No finding of structure beyond it.

## Checks run

- `git rev-parse HEAD` → `f52c565772f125fe5ebb17f0a0fb98ee7e56fe6e`; `git log` and `git diff
  268b2b07..f52c5657` → exit 0.
- `python -B task-cycle/change_file_sizes.py 268b2b07… f52c5657…` (reviewed worktree) → exit 0.
- `python -B -m unittest discover -s agent-instructions -p "test_size_invariant.py"` in a worktree
  of the base → exit 0, 4 tests OK; in a worktree of the head → exit 0, 4 tests OK.
- `python -B elements/common/foundation_check.py` at the head → exit 1, 12 errors (I1); the same
  at `3b34de03`, `0ee90d8e`, `29a1c6ae`, `ca55d4e8` → 0, 2, 3 and 12 errors.
- `python -B -m unittest test_foundation_check.FoundationCheckTest.test_the_way_foundation_check_reports_no_error`
  (from `elements/common/`) at the head → exit 1, `FAILED (failures=1)`; at the base → exit 0.
- `python -B -m unittest discover -s task-cycle -p "test_gate_times.py"` at the head → exit 0, 38
  tests, `OK (skipped=1)`.
- `python -B agent-instructions/skill_entry_points.py` at the head → exit 0, `entry points are
  current`.
- `python -B gate/run_tests.py product-guidelines` at the head → exit 0, 14 tests OK.
- `python -B gate/run_tests.py agent-instructions` at the head → exit 0, 53 tests OK (linter,
  formatter, size, script imports).
- `python -B gate/run_tests.py process-audit` at the head (the worktree `head2`) → exit 0, `Ran 342
  tests`, `OK` (the invariant `audit-series-script-paths` and the new tests of slices 6 and 7
  among them; 525 s, run in the background).
- AST of `process-audit/audit_count.py` without its module docstring, base against head
  (`python -B -I astcmp.py`) → exit 0, `code equal: True`: no code of the trust boundary changed.
- `git diff 268b2b07..f52c5657 -- task-cycle/gate_times.py` searched for the registry, `main` and the
  exit code: no line of them changed, so `gate-times-refuses-impossible-entry` and
  `command-runner-passes-exit-code` keep their code; their tests pass in the run above.
- A script comparing slice 1's two files at `bcd8e551` with the base file (`python -B -I moved.py`)
  → exit 0, the moved block found whole, 238 test methods before and after.
- A scan of the added Markdown lines over 100 characters (`git diff -U0` with `awk`) → exit 0, the
  lines of Minor 5.
- Not run: the full gate, the cycle's own run; the whole `elements/common` directory, whose failing
  test I ran alone.

## Reaches beyond the handoff

- WAY-386, WAY-388 and WAY-389, read whole as they stand between the exemplars I opened (WAY-385,
  WAY-387, WAY-390, WAY-391); no bearing found.
- `process-audit/problem_register.py:142-152` (`check_issue`) and `process-audit/audit_report.py:
  315-319` (`table`): to check crafted issue names at the comparison's cells and values.
- `gate/run_tests.py:161-165`: the form of the summary line `SUMMARY` reads.
- `elements/common/test_foundation_check.py:2495-2520`: the test of `own-foundation-check-report`.
- `the author's global rule file for commits` and `scripts.md`, the user's rules, which the
  session's hooks gave before the worktrees and the scripts.

## Working copies

- `.runs/review-whole/base` and
  `.../review-whole/head`, `.../review-whole/head2`, worktrees of the base and the head (the second
  head made for a clean run of `process-audit`, since the first was moved through four commits for
  the bisection of I1 while a run stood in it; that run's result was discarded):
  each removed with `git worktree remove --force`, then `git worktree prune`; `git worktree list`
  names none of them.
- `.../review-whole/index.md`, `sections.md` (the index of my selection), `sizes.py`, `astcmp.py`,
  `moved.py`, `b_tac.py`, `s1_tac.py`, `s1_tpv.py`, `pa.out`, `pa2.out`: removed with the directory
  `.runs/review-whole/` by
  `rm -rf` on its full path. Nothing remains. The reviewed worktree is clean and its HEAD is the
  head given.

## Unread material

Decisions of the index of my selection (25 listed in full, 202 by heading) read whole: 23 —
WAY-11, WAY-33, WAY-35, WAY-84, WAY-127, WAY-256, WAY-330, WAY-337, WAY-339, WAY-344, WAY-350,
WAY-385, WAY-386, WAY-387, WAY-388, WAY-389, WAY-390, WAY-391, WAY-401, WAY-404, WAY-405, WAY-416,
WAY-417. The others listed in full (WAY-73, WAY-82, WAY-85, WAY-90, WAY-113, WAY-120, WAY-150,
WAY-265, WAY-368, WAY-370) were read through their binding sentences in the index.

- WAY-02 (how a test cites a decision by a `decision:` line), which bears on I1: not opened; I took
  the rule from the foundation check's own messages.
- WAY-161, WAY-263, WAY-363, WAY-365 and WAY-409, which bear on grading: read through the method
  (`task-cycle/review/SKILL.md`), which restates them, not opened.
- Guideline files: none — `guidelines/coding.md`, `coding-command-runner.md`,
  `coding-measuring-report.md`, `coding-shared-module.md` and `testing.md` read whole.
- `process-audit/test_process_versions.py` (2214 lines) and `process-audit/test_series_summary.py`:
  read the changed assertions, the new tests' citations and the first 200 lines of the second, not
  every new test whole.

## Searches not found or unclear

- WAY-417 "with the answer that those sums give" against the task's "jak dziś dla wersji": unclear
  whether the task asks the row of a version to show the sums; read as not, which is why I2
  recommends narrowing the entry.
- Executor 7's report says the mechanism comparison gives "15 pairs in *Unknown values* for each
  fixed issue and series"; `unknown_field` groups the issue's name out (`FIX_ISSUE`), so the pairs
  are 15 in all, each with up to three examples — a claim of the report I found inexact.

# Findings to fix — the whole change

The blocking findings of the review of the whole change (`reports/whole-change-review-report.md`, head `1923ef446867b1b17a9ef749d9c811b1e2906c06`), then the Minor findings of that review within the task, copied word for word from the reviewer's report (WAY-161). The findings outside the task's scope (O1 to O6) are not part of this fix.

## Blocking

**I1. `process-audit/SKILL.md:197` — "The date starts a new series of measures" now says more than WAY-339 does.**
Comes from slice 8 (`49ab2fa..1923ef4`, commit `1923ef4`), which rewrote the series bullet at `process-audit/SKILL.md:50-64` and
left this sentence; the base text of the sentence is the same, so it is also a spill of the entry change `a030dbf`.
- What is wrong: the sentence is in a file this change changed and repeats WAY-339, which this change changed
  (`foundations/decisions.md:11193-11233`), without its qualification. After this change a date of the register's list of classes
  starts a new series of the cost and of nothing else: `instrument_series` (`audit_count.py:2297-2310`) consults one script
  only, and the test `test_the_reviewer_the_stage_script_and_the_list_of_classes_split_no_series_of_measures` asserts it. A
  session that follows line 197 tells the human that adding a class resets the series of the mechanism measures and of the
  gate times, which the count does not do.
- Why it matters: WAY-263 grades as Important a finding that a changed file repeats a changed entry while broadening it or
  dropping a qualification; the effect is a wrong account of series boundaries at the very point the human weighs a class.
- Evidence: `grep -n "starts a new series" process-audit/SKILL.md` gives line 197; the rules bullet at lines 50-64 names the
  class date only among the splits of the cost and says nothing of it for the measures.
- Fix direction: write "of the cost" (and, if wanted, that it starts none of the mechanism measures or gate times, as line 61
  says of a new price list).

**I2. WAY-344 as changed requires exit 1 for a field the code deliberately reads as absent: the two time lines of `stages.md`.**
Comes from none of the eight slices as an error of work: it is a gap of the plan's *Foundation entries* row 6 (the entry carries
no carve-out) joined to slice 5 (`8a8f636..0e75a4b`), which the plan told to read the pair as it does. The plan's mandate does
not lower the grade.
- Place: `process-audit/audit_count.py:1618-1630` (`has_working`, `has_waiting`: neither line is "an earlier form", exactly one is
  a missing field) against `foundations/decisions.md:11336-11357` (WAY-344): a field is "any named thing the script looks for
  data by in the file — a section heading, a row label, a table column or a JSON key"; the rule binds "the whole reading of each
  file whose way of reading the change reworks — every field of that file"; the count "gives the values that need a missing
  field as unknown, writes its result and ends with exit code 1 and a line `Error:` that names the file and the field".
- What is wrong: this change reworks the reading of `stages.md`, the two time lines are fields of it (a row label), and a copy
  with neither gives their values unknown and exit 0. The entry has no sentence for an earlier form of a file, and WAY-352 makes
  only the table of tokens by model first-class. So the code does not do what the entry requires. The plan's *Choices* row
  (`plan.md:391`) records the reason: 86 of 93 copies lack the lines, so the strict reading gives every future count exit 1
  for good. I judge the code right and the entry incomplete; the grade follows WAY-263.
- Why it matters: the next agent that compares a change with WAY-344, which this entry's *Verification* tells it to do, reads
  `process-audit/audit_count.py` as violating it, and a later "fix" of the code would end the weekly count with exit 1 on every
  run, making that exit code carry no signal.
- Evidence: `test_neither_time_line_is_the_earlier_form_and_no_missing_field` (`process-audit/test_audit_count.py`, class
  `StagesForms`) pins the behaviour; `git diff 2292f33..HEAD -- foundations/decisions.md` shows no sentence about a form of a
  file lacking a field.
- Fix direction: say in WAY-344 (or WAY-352, which `Relations` can then name) that a field an earlier form of a file never had
  is not missing where the file's other signs name that form, and that a file of the earlier form gives its values unknown
  with no `Error:`; then the choice stands in the foundation. This words an approved decision a little wider, so by WAY-114 it
  belongs in the request's list for the human, which the orchestrator carries.

## Minor, within the task

M1. `process-audit/price_list.md:9` ("a new list with another date starts a new series of measures (WAY-339)") and
`process-audit/problem_register.md:65` ("Each date in *Added* or *Withdrawn* starts a new series of measures") no longer match
WAY-339 as changed: both start a series of the cost only. They are unchanged files, so WAY-263 does not reach them; they are for
the return step's comparison of the entries the change edits with the files (`agent-instructions/README.md`, "Make the change"),
and the fix is the same "of the cost" as I1.

M2. `process-audit/audit_count.py:214-218` (module docstring, slice 6 M3 still holding): the exit-1 sentence still reads "or a field
missing in a `stages.md`" though the count also ends with exit 1 for `mechanism_measures.md` and `gate_times.md`
(`audit_count.py:2886-2896`), and the docstring's account of the result (lines 205-212) does not name the sections *Mechanism
measures* and *Gate runs* or the reading of the two files, while it does carry the *Measure versions* paragraph (lines 123-137).
The docstring is the command's contract; `process-audit/SKILL.md` is right.

M3. No foundation entry records the registry of running gates: `~/.the-way/gate_runs/`, the six-hour and one-day limits, the
file names (`task-cycle/gate_times.py:17-23`, `task-cycle/skill/SKILL.md:71-74`). WAY-349 and WAY-350 give the count of other runs
and not where it is kept; the foundation-entries agent flagged the same (`foundation-entries-report.md`, "Searches not found",
question 1). A sentence in WAY-350, or in WAY-140's reading, would let a reviewer check the exception against an entry instead of
the plan's *Choices*.

M4. `task-cycle/gate_times.py:131-134` and `:231-236` (`Times.line`, `rows`; slice 3): no cap on the number of blocks a run keeps
or on the length of a directory cell (the line bound is 1 MiB, `LINE_LIMIT`). A gate that prints 200,000 lines `== dirN` each
followed by a `Ran` line, run by `python -B task-cycle/gate_times.py --output <file> --registry <dir> -- python -c ...`, exits
0 and appends a 12,289,123-byte file in 0.9 s; the audit reads no copy file over `MAX_BYTES` (4 MiB, `audit_count.py:261`), so
that cycle's gate runs all become unknown, and the bytes are committed with the record. The product's own gate is no stranger
(choice (c)), so this is not blocking, but the handoff asked for crafted input at this reading and the audit already caps at 500
runs and 50 directories; a cap in the writer of the same order keeps the file readable.

M5. `task-cycle/skill/SKILL.md:134-136` (slice 4): step 4's `--output ../task-cycles/<task-slug>/gate_times.md` reaches the
worktree's record directory only from a checkout directly under the worktree's `.runs/`, and the sentence about the checkout
says "under the worktree's ignored `.runs/`" without saying directly. From a deeper checkout the script makes a stray directory
and the base run is lost from the record, silently. The executor's own-work check named the same (`slice-4-report.md`, "Own-work
check"). Say "directly under" in the instruction that places the checkout.

M6. `task-cycle/record_template.md:99-101` (slice 4): the new sentence is two lines of well over 100 columns beside text kept near
100; polish only.

M7. `process-audit/audit_count.py:367` (`GATE_CODE = [0-9]{1,3}`; slice 6 M1 still holding): the writer writes the child's exit
code as `str(code)` (`gate_times.py:231-232`), and on Windows, the author's system, a crashed or interrupted gate ends with
codes such as 3221225786; the reader turns the cell into `unknown` with the reason "not a whole number". The value is lost, not
mis-stated, and the reason is wrong. Widen the pattern; no test gives a code above 255.

M8. `process-audit/audit_count.py:1489-1500` (`read_gate`, slice 6 M2 still holding): the table is read to its first line that does
not begin with `|`; a run after a blank line is dropped without a row in *Unknown values*. And `:1587-1592` (slice 6 M4): the
two optional files stand in the `try` of the required ones, so a git failure on `gate_times.md` blanks `cycle.md` and
`stages.md` that were read.

M9. `task-cycle/cycle_measures.py:279-300` (`codex_subagents`, slice 2 Minor 1 and choice (f)): the search reads the first line of
every rollout under the Codex home, so one unreadable first line anywhere in the home ends every Codex cycle's measures with exit
2 and nothing written; `cycle_stages.py:443-452` reads only rollouts modified since the orchestrator's first turn. The floor
would keep the loud failure for every file that could be a subagent. Slice 2 Minor 2 as well (`:295`): a second rollout with an
id already found is dropped without a word.

M10. `process-audit/audit_count.py:2273-2285` area and `:1295-1315` (slice 5 Minor 2 and 3): a file with neither the heading nor
a `Model` table gives two `Error:` lines, one per field, where the plan says once "the `Error:` line names both" and once "one
`Error:` per field"; and every missing column puts the same reason twice in *Unknown values* (once for *Cost*, once for *Fix
rounds share*). Both defensible, tested as they are; the plan's two sentences should agree.

M11. Polish still in the final tree: `process-audit/audit_count.py:38`, `:143`, `:190`, `:216` (129 characters), `:1412`, `:2112`,
`:2328` run to 102 to 129 columns (slice 5 Minor 1); `task-cycle/cycle_measures.py:109-118` `read_time` says "in UTC" while it
attaches UTC to a naive time and leaves another offset as it is (slice 1 M1, correct comparison, wrong docstring);
`task-cycle/test_cycle_measures.py` helper `assert_error_names(self, transcript, code_expected, field)` takes a code every caller
sets to 2 (fix review M-b); the meta file's `RecursionError` branch (`cycle_measures.py:202`) has no test of its own, the
meta test gives a long number (fix review M-a); one blank line before `class CodexTest` (slice 2 Minor 3); "unknown" is held twice
in `Call` and in `Agent.cache_known` (slice 2 Minor 3).

M12. Slice 1 M2, in part still holding: no test pairs rewrites over two interleaved agents, or takes the orchestrator's first,
middle and last call over two sessions of one tool (`test_cycle_measures.py` has `MixedCycleTest` for two tools); I read
`rewrites`/`report` and both are right.

FAIL 1923ef446867b1b17a9ef749d9c811b1e2906c06

# Review of the whole change — audit numbers: cost from older stage reports, measures script, gate times

Method: `review-change`, variant the whole change (`task-cycle/review/SKILL.md`, `task-cycle/review/whole_change.md`).
Range `2292f334d5499f45b68b00c477cd76a2effd7537..1923ef446867b1b17a9ef749d9c811b1e2906c06`, 13 commits (`git log`);
`git rev-parse HEAD` is `1923ef446867b1b17a9ef749d9c811b1e2906c06`, the head given. The worktree, its index and its
branch were not changed (`git status --short` empty after every command). The product's gate was not run.

Counts: blocking 2 (Important), Minor within the task 12 (M1 to M12), Minor or other findings outside the task 6 (O1 to O6), Critical 0.

## Changed files (`git diff --numstat 2292f33..1923ef4`, added / removed)

| File | + | - |
|---|---|---|
| `foundations/decisions.md` | 227 | 23 |
| `foundations/part_map.md` | 1 | 0 |
| `process-audit/SKILL.md` | 37 | 12 |
| `process-audit/audit_count.py` | 707 | 51 |
| `process-audit/test_audit_count.py` | 873 | 9 |
| `task-cycle/cycle_measures.py` (new) | 505 | 0 |
| `task-cycle/test_cycle_measures.py` (new) | 702 | 0 |
| `task-cycle/gate_times.py` (new) | 299 | 0 |
| `task-cycle/test_gate_times.py` (new) | 276 | 0 |
| `task-cycle/skill/SKILL.md` | 31 | 13 |
| `task-cycle/skill/blocked_finding.md` | 1 | 1 |
| `task-cycle/skill/reserved_return.md` | 2 | 1 |
| `task-cycle/record_template.md` | 3 | 2 |

Acceptance 1 holds: `git diff --quiet 2292f33 HEAD -- task-cycle/cycle_stages.py task-cycle/change task-cycle/plan
task-cycle/review task-cycle/spec` exits 0. Acceptance 2 holds: `TREE_PATHS` (`process-audit/audit_count.py:318-319`) is
unchanged text, the only changed line that names it is the call in `Ancestry.changed`, and the real-history run below
gives the same cost series as the unit tests (`ProcessVersions`) expect. No invariant test is changed by the range.

## Against the task: every required outcome

| Required | Met by | Verdict |
|---|---|---|
| To do 1: cost from the table of tokens by model, same prices and formula, older form known by its own signs, share unknown with a reason, a missing field gives cost unknown, result written, exit 1 and an `Error:` naming file and field | `audit_count.py` `stage_table`, `section_table`, `older_table`, `priced_older`, `cost_at`, `main` (`lacking`); tests `Cost`, `StagesForms` | met; see I2 for the time lines |
| To do 2: new script in `task-cycle/`, one file of numbers: calls (all, orchestrator, each subagent), first/middle/last context per agent, mean, orchestrator mean, share above 200 thousand, cache written 5 minutes and 1 hour per agent, rewrite tokens and calls for orchestrator and subagents, Codex unknown | `task-cycle/cycle_measures.py`; hand-worked tests; Codex tests | met; hand figures recomputed by the slice reviewers; rewrite formula equals WAY-351's worked example (`min(50,000-30,000; 25,000)=20,000`) |
| To do 3: instruction and record template name the file and the step | `task-cycle/skill/SKILL.md` step 12, `blocked_finding.md`, `reserved_return.md`, `task-cycle/record_template.md:99-101`, cleaning list in "The record before it is committed" | met |
| To do 4: gate run through a new script on every run, base included, whole time, time of each directory in any order, other gate runs at the same time, file in the record; instruction and template name them | `task-cycle/gate_times.py`; `SKILL.md` steps 2, 4, 10 | met; see M5, M6 |
| To do 5: the count reads both files, one section of values per cycle, per version the median of each measure and whether it falls against the previous version of the same series, gate times only over runs with no other gate and the rest apart, new series only at a change of an instrument, a missing field gives unknown, exit 1 and an `Error:` | `read_measures`, `read_gate`, `instrument_series`, `mechanism_rows`, `gate_rows`, `measures_lines`, `gate_lines`, `measure_versions_lines`; `MeasureVersions` tests | met; "each measure" is read as each cycle-level measure, see choice (d) |
| To do 6: the audit session's instruction puts the measures before the human | `process-audit/SKILL.md` rules, step 2, step 3, matters 1 and 4 | met; see I1 |
| Settlements to record rows 1 to 8 | WAY-347 (row 1), WAY-348 (row 2), WAY-339 in place (row 3), WAY-349 (row 4), WAY-350 (row 5), WAY-344 in place (row 6), WAY-351 (row 7), WAY-352 (row 8); part map `task-cycle` trust boundary | each row has its entry; the entries say what the code does except as I2 gives; `foundation_check.py --skip-test-citations` exits 0 |

Fidelity to the sources: the settlements' wording (the rewrite definition of the verification, the 2 thousand floor,
the 30% shrink, the series only by instrument, the runs with no other gate) is carried into the entries and the code
unaltered; I found nothing invented. WAY-350's "15 to 16 minutes ... 23 to 40" is the task's own measurement.

## Judgment of the orchestrator's choices (a) to (f)

- **(a) The count of other gate runs rests on empty files under `~/.the-way/gate_runs/`.** Holds. WAY-140 (`foundations/decisions.md:3900-3949`)
  reserves to a human an effect "on a server, in DNS, on keys or on an external account"; an empty file in the user's own
  `~/.the-way/` that the script writes and prunes is none of them, and `task-cycle/skill/SKILL.md:71-74` names it as the one
  exception to "writes nothing outside the worktree". WAY-320 keeps in `locations.json` the places a user chooses; the registry
  is a fixed place of the process's own state, written with `~`, so `tracked-file-private-paths` passes. The weakness is that no
  foundation entry says the registry exists: see M3.
- **(b) An absent time line in `stages.md` is an earlier form; exactly one of the two is a missing field.** The behaviour is the
  right one (86 of 93 copies in the-way's own history have neither line, so reading every absence as a missing field would end
  every count with exit 1), but WAY-344 as changed does not carry the carve-out: finding I2.
- **(c) `task-cycle/gate_times.py` is not a trust boundary.** Holds. WAY-48 (`foundations/decisions.md:1200-1228`) records
  boundaries at code that takes in what the product does not control, "never at a script that only checks the product's own
  files"; the output of the product's own gate is the product's. The script still cleans what it writes (`cell`), caps a
  line, and the audit reads its file as untrusted; the one gap is M5.
- **(d) The audit shows cycle-level values only.** An acceptable reading of "the median of each measure": subagent names differ
  between cycles, so a per-agent median has no meaning, and the table `## Agents` stays in the file of each cycle's copy. The
  task is silent on it and the cost is real (a reader who wants one subagent's contexts opens the file); it is recorded only in
  the plan's *Choices*, so the request should put it before the human. Not graded as a finding.
- **(e) The task's name is fixed in step 2, before the first gate run.** Holds against WAY-147
  (`foundations/decisions.md:4169-4197`): the plan's name where there is a plan, the cycle's name otherwise, and step 5 keeps it.
  One weakness in the path given for step 4's run: M6.
- **(f) The strict form on a broken first line of an unrelated Codex rollout.** Within the task and WAY-344 (loud, never a
  missing subagent counted as nothing), so not blocking, but it makes every Codex cycle's measures fail for the age of the
  Codex home; `task-cycle/cycle_stages.py:443-452` already bounds the same search by the modification time. M9.

## Findings

### Critical

none

### Important (blocking, within the task)

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

### Minor, within the task (the cycle can cut these into the findings file of the fix)

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

### Minor or other findings outside the task (counts as out of scope; not fixed by the cycle)

O1. A failed run enters the gate median (`process-audit/audit_count.py:2374-2388`, `gate_values`; slice 7 Minor 1): a run with exit
2 that stops before the directories has a small total and can make *Falls* read `yes`. The task and WAY-350 name one criterion,
the count of other gate runs, so this is a design point for the task's author, not a defect of the change. The *Exit code*
column of *Gate runs* shows such runs.

O2. Rows of *Measure versions* are not capped by distinct directory names (`audit_count.py:2374-2392`, slice 7 Minor 2): linear in
what slice 6 already bounds (500 runs by 50 directories per file) but unbounded in the number of cycles; a total cap is a design
choice.

O3. On the real history of this checkout (scratch run below), *Measure versions* is 850 lines of rows that all read `unknown` (21
versions by 15 measures, and 56 gate rows), and *Unknown values* gains one row for each of them (840 `Measure falls` and 56 `Gate
time falls` rows; the 500-row cap there is the register's only). The plan's *Choices* ("one row per version and measure") chose this;
until cycles carry the new files, the section *Unknown values* of the count is mostly these rows and matter 1 of the session
(`process-audit/SKILL.md:150-164`) reads them. A row per series for a version with no value at all would keep the sections short.

O4. A transcript line of gigabytes would be read whole by `for line in handle` (`cycle_measures.py:126`; slice 1 M3). No cap is asked.

O5. `cycle_measures.py` exits 2 with nothing written, and the instruction (`task-cycle/skill/SKILL.md:458-466`) says nothing of what
the orchestrator does then; the audit reads the absent file as "an earlier form" (`audit_count.py:1413-1418`), a wrong reason for a
cycle whose script failed. The task asks only that the instruction name the file and the step.

O6. A cycle that changes an instrument is counted under the version it ran on, which holds the old script, while its own copy of
the file is written by the new one (WAY-343's price, `foundations/decisions.md:11310-11335`); the first measured cycle, and each
later cycle that changes `cycle_measures.py` or `gate_times.py`, sits in the series of the instrument it replaced. The task fixes
both rules, so I set it aside.

## The Minor and out-of-scope findings of the slice reviews, graded here

| Slice review | Finding | In the final tree | Graded here |
|---|---|---|---|
| slice 1 | M1 docstring "UTC" | holds | M11, within |
| slice 1 | M2 no test of interleaved agents or of two sessions | holds in part | M12, within |
| slice 1 | M3 output ties, no cap on a line | ties equal `cycle_stages.py`; no cap | O4, outside |
| slice 1 fix | M-a, M-b | hold | M11, within |
| slice 2 | 1 strict reading of an unrelated rollout | holds | M9, within |
| slice 2 | 2 duplicate id dropped | holds | M9, within |
| slice 2 | 3 blank line, unknown held twice | holds | M11, within |
| slice 5 | 1 long docstring lines | holds, more lines | M11, within |
| slice 5 | 2 one `Error:` per field or one naming both | holds | M10, within |
| slice 5 | 3 reason doubled in *Unknown values* | holds | M10, within |
| slice 5 | outside: `process-audit/SKILL.md:143-145` stale | fixed by slice 8 (`process-audit/SKILL.md:150-164` now right) | closed |
| slice 6 | M1 exit code of four digits | holds | M7, within |
| slice 6 | M2 rows after a blank line | holds | M8, within |
| slice 6 | M3 module docstring | holds | M2, within |
| slice 6 | M4 git failure on an optional file | holds | M8, within |
| slice 7 | 1 failed run in the median | holds | O1, outside |
| slice 7 | 2 rows not capped by distinct directory | holds | O2, outside |
| slice 7 | 3 line count in the report | no effect | none |

## The slices with no review of their own, judged as slices (WAY-136, WAY-164)

- **Slice 3, `gate_times.py` (`036d24a..7916a21`).** The requirements of the plan are met: command form, exit code passed on,
  own failures `Error: gate_times.py:` with exit 2 found before the command starts, output relayed as it comes
  (`test_output_is_passed_on_unchanged_with_error_output_joined`), blocks and the first `Ran` line in any order, `unknown` and
  `—`, the registry rule with its limits, the default registry under the home directory, no import of the-way, one subprocess.
  The format it reads is the real one: `gate/run_tests.py:92-112` writes `== <directory>` then the child's unittest report, whose
  `Ran N tests in X s` line the runner's own `RAN` also reads. The executor's own-work check (the own entry is never counted;
  removing the token exclusion fails three tests) fits the requirement that fails most easily. Where it is weakest is the
  reading of real output, and the tests use made-up output only; I compared the format by reading `gate/run_tests.py` and could not
  run the real gate (forbidden). Finding: M4.
- **Slice 4, instruction and template (`7916a21..8a8f636`).** Every run of the gate named goes through the script (steps 2, 4, 10
  and the reruns), the slug is known to the base run, the registry exception is named, `cycle_measures.py` stands beside
  `cycle_stages.py` at step 12, step 9's stop, `blocked_finding.md` and `reserved_return.md`, and the template names the two files
  with the step that makes each. No line of the excluded directories changed. The own-work check named the weakest requirement
  (the path of the base run) and settled it by hand only; findings M5, M6.
- **Slice 8, `process-audit/SKILL.md` (`49ab2fa..1923ef4`).** The sections, the `Error:` line, the series rule and matter 4 match
  the code (checked against `audit_count.py:2556-2578`, `:2636-2662`, `:2886-2896`); matter 1's stale sentence is now right. The
  own-work check read the text against the script and missed the one sentence the slice did not touch: I1.
- **Slice 1's range also holds the foundation entries (`a030dbf`), reviewed here as the review of slice 1 covered only what its
  scripts had to match.** WAY-347 to WAY-352 and the two entries changed in place read as above; the part-map line names
  `task-cycle/cycle_measures.py`. Findings I2, M3.

## Declined to judge

- Whether `agent-instructions/README.md` ("Check the change") should say that the-way's own gate runs through
  `task-cycle/gate_times.py`: the task names the instruction and template of the cycle only; outside the task.
- How the human should word matter 4's questions in the session, and the thresholds the audit might later use to call a median
  "falling" meaningfully: the task asks for the median and the comparison only.
- Whether a Codex rollout of real use has the `token_usage_record` entries the script reads: the form is the one
  `cycle_stages.py` already reads; I have no real Codex rollout.

## Checks run

| Command | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `1923ef446867b1b17a9ef749d9c811b1e2906c06` |
| `python -B elements/common/foundation_check.py --skip-test-citations` | 0 | `0 errors` |
| `python -B -m unittest discover -s task-cycle -p "test_cycle_measures.py"` | 0 | 43 tests OK |
| `python -B -m unittest discover -s task-cycle -p "test_gate_times.py"` | 0 | 17 tests OK |
| `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` | 0 | 172 tests OK in 238 s |
| `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` | 0 | 1 test OK |
| `python -B -m unittest discover -s elements/part-map -p "test_cross_part_imports.py"` | 0 | 39 tests OK |
| `python -B -m unittest discover -s gate -p "test_skills_reach_the_way_sessions.py"` | 0 | 2 tests OK |
| `python -B -m unittest discover -s task-cycle -p "test_remarks_check.py"` | 0 | 59 tests OK |
| `python -B instruction-files/check_instructions.py .` | 0 | 0 error, 0 warn, 3 info |
| `git diff --quiet 2292f33 HEAD -- task-cycle/cycle_stages.py task-cycle/change task-cycle/plan task-cycle/review task-cycle/spec` | 0 | no change |
| `git diff 2292f33..1923ef4 -- process-audit/audit_count.py` searched for `TREE_PATHS` | 0 | only the call in `Ancestry.changed`; the assignment is unchanged |
| scratch: `python -B process-audit/audit_count.py --locations <locations file in the scratchpad, results directory in the scratchpad>` over this checkout | 0 | 75 cycles in 1 of 1 repositories; no `Error:`; all 21 series of the cost as before; *Mechanism measures*, *Gate runs*, *Measure versions* written (all `unknown`: no cycle holds the files yet) |
| scratch: `python -B task-cycle/gate_times.py --output <file in the scratchpad> --registry <dir in the scratchpad> -- python -c <200,000 blocks>` | 0 | a 12,289,123-byte file (M4) |

Not run: the product's gate (by instruction); the tests of the slices against the base to see them fail (the slice reviewers
and executors report them; I did not repeat them); mutation runs; the real gate through `gate_times.py` (it is the full gate);
any real Codex rollout or nested Claude Code subagent transcript (none to hand). The files of the measures script and of the gate
script were not run against a real cycle's sessions by me; the slice 1 reviews report a real run on a session transcript, exit 0.

## Reaches beyond the handoff

- `agent-instructions/README.md` whole, as the repository's `AGENTS.md` directs.
- `the author's rules file on scripts`, before my scratch scripts (the user's rule).
- `gate/run_tests.py:1-140`, for the format `gate_times.py` reads, and `task-cycle/cycle_stages.py` by search (`token_usage_record`,
  `parent_thread_id`, lines 443-452), for the Codex discovery bound.
- `process-audit/problem_register.md:55-70` and `process-audit/price_list.md:5-12`, found by searching the repository for "new
  series" (M1); they are unchanged files.
- `foundations/decisions.md`, selected by "Reading the foundation": WAY-09, 21, 33, 34, 35, 38, 44, 48, 71, 89, 136, 140, 147,
  148, 150, 160 to 164, 255, 263, 297 to 299, 308, 309, 320, 328, 330 to 352 (counts below); `foundations/invariants.md` the five
  with Part `every` that the change reaches; `foundations/glossary.md` the entries gate, part, part map, slice, cost of an
  occurrence.
- The scratchpad of this session, which already held the files of earlier sessions: I used `loc.json` as the model of my own
  locations file and let the count read the `register.md` there (read by the count only); I read nothing else of theirs.

## Unread material

Counts of section 1 for decisions: the selection by *Scope* of the touched parts (`task-cycle`, `process-audit`, and `decisions`
and `part-map` for the entries the change writes) holds 187 decisions. **52 read whole, 135 by title only.**

- Read whole: WAY-09, 21, 33, 34, 35, 38, 44, 48, 71, 89, 136, 140, 147, 148, 150, 160, 161, 162, 163, 164, 255, 263, 297, 298,
  299, 308, 309, 320, 328, 330 to 352 (the 23 of the audit's part and of the change itself).
- Run through by title, all 135 others (the listing of the 187 titles with their scopes was read in full); every one whose title
  points to a bearing on the change was opened, and I found none left unopened that bears on it. Not run through by title: none.
- Decisions that bear on the change and stayed unread: none known; WAY-286 to WAY-292 (the request's description) bear on the
  cycle's next step, not on this change.
- Guideline files: none exist for the-way (`ls guidelines` finds no directory; WAY-328 departs from the coding and testing guidelines
  for its own parts, and the handoff says none is missing); none unread.
- Foundation other than decisions: `foundations/part_map.md` read whole. Invariants: read whole `tracked-file-private-paths`,
  `script-language`, `script-imports`, `script-subprocesses`, `cross-part-imports`; the others with Part `every`
  (`foundation-file-kinds`, `foundation-change-merge-route`, `repository-file-location`, `return-step-record`,
  `derived-file-content`, `ci-checking-commands`, `outbound-link-reach`, `map-reference-target`, `test-method-citation`,
  `skill-entry-points`, `instruction-file-imports`, `record-copy-image-files`) and `record-copy-image-check`, `element-directory-contents`,
  `skill-rule-source`, `generated-overview` were read by name only: the change reaches them only through checks that ran green
  (`foundation_check.py`, the skills-reach test, the cross-part test) and no image or entry point was touched. Glossary: the five
  entries named above read whole, the other titles only.
- Code: `process-audit/audit_count.py` read as the diff whole plus the functions it leans on (`header_fields`, `table_cells`,
  `read_file`, `median_of`, `cell`, `table`, `main`), not all 2,900 lines; `task-cycle/cycle_measures.py` and
  `task-cycle/gate_times.py` read whole; `task-cycle/test_gate_times.py` read whole; `task-cycle/test_cycle_measures.py` and
  the 873 added lines of `process-audit/test_audit_count.py` read by test name and by the slice reports, bodies not read except
  the ones named above; `task-cycle/skill/SKILL.md` read for lines 20-155 and the diff, not the rest; `task-cycle/record_template.md`
  read as the diff.
- Reports: the review reports named in the handoff and the reports of slices 3, 4, 8 and of the foundation entries read whole;
  the planner's report, the executors' reports of the reviewed slices and every handoff other than mine not read.

## Searches not found or unclear

- WAY-344 carries no sentence about a field an earlier form of a file never had; I looked for one in WAY-344, WAY-352 and WAY-294
  and found none (I2).
- No foundation entry records the registry of gate runs (M3).
- The handoff's "(b) an absent time line is an earlier form" has no basis in the task text, which speaks of fields of "either
  form" of the cost; I read it as the orchestrator's choice on the plan's *Choices* row 391.
- The location of the checkout that step 4's base run uses is not fixed by any instruction (M5).

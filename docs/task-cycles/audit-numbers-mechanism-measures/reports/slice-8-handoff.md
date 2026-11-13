# Handoff — slice 8

Delegation: the person who requested this cycle (Mariusz) has delegated intermediate choices to the orchestrator.
Your questions go to the orchestrator, never to the human; no answer of the orchestrator is the human's approval.

Worktree (work from its root): `the task's worktree`
Branch `task/audit-numbers-mechanism-measures`. The slice's base is the current HEAD, `49ab2fa`
(`git rev-parse HEAD`); the task's base is `2292f334d5499f45b68b00c477cd76a2effd7537`. The-way is the top-level
repository (no product, no `.the-way`). Class of model of this executor: `cheaper`.

Method: `make-change`, in its variant "a slice, or the retry of a slice". Read whole `task-cycle/change/SKILL.md`,
and a file it names (`task-cycle/change/slice.md` included) only when the step or variant that names it comes.
Boundary: this slice only, its commits on the task branch (git add by path, never `-A`), then return. Do not run
the product's gate (`gate/run_tests.py`); run the slice's own focused checks named in its section, each with its
command and exit code in your report. Write each test before the code it covers where the slice changes behaviour.
Another slice's files you do not touch.

Paths:
- frozen task: `.runs/task-cycles/audit-numbers-mechanism-measures/task.md`
- plan: `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md` (you need not open it: your section is below)
- spec: none
- your report: `.runs/task-cycles/audit-numbers-mechanism-measures/reports/slice-8-report.md`

Answers of the start of the cycle: trust boundary yes (this change adds a reader of session records and changes
`process-audit/audit_count.py`, the trust boundary of `process-audit`: crafted input at every reading must be
survived — missing fields, malformed lines, bars and control characters in text that reaches a cell, huge files);
irreversible operation no. Checks failing on the base: none (the whole gate passed on the base). The foundation
check `python -B elements/common/foundation_check.py --skip-test-citations` is NOT yours to fix beyond this slice's files.

The slice, copied word for word from the plan:

### Slice 8 — The audit session's instruction puts the measures before the human

- **Goal:** `process-audit/SKILL.md` leads the session through the new numbers. In *Rules of working*, the rule on series gains what the
  count does for the mechanism measures and the gate times: a new series only at a change of the script that measures them, the
  instruction of the cycle, of the reviewer and of the author starting none, and no number of one series set beside a number of
  another. Step 2's account of exit code 1 gains the `Error:` lines that name the file of a cycle's copy and the field it lacks, which
  the result's *Unknown values* also name. Step 3's list of the sections of the count gains `Mechanism measures`, `Gate runs` and
  `Measure versions`. Matter 1's sentence that a `stages.md` of an earlier form gives no cost is brought to what the count does now (the older
  form gives the cost and leaves its share of the fix rounds unknown). Matter 4 gains the measures: for each series, one at a time, the
  rows of the version tables quoted with their header row, then what follows from them and what does not, then one open question
  for the human with no recommendation; the gate times of runs with another gate are shown apart as the count shows them and
  never compared; a measure is material and never a priority, as the rules of the skill already say of the other numbers. The step that
  writes the result's note keeps working unchanged. The skill's description is unchanged, so the skill's entry points are not regenerated.
- **Change:** `process-audit/SKILL.md`
- **Read:** `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:37-37` To do, item 6 · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:46-51` Questions to settle, whether the count reads the new numbers · `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md:266-298` Slice 6 — The count reads the measures file and the gate times of each cycle and shows their values · `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md:300-335` Slice 7 — Series by instrument, the median of each measure per version and the comparison with the previous version · `foundations/decisions.md:11193-11217` WAY-339 · `foundations/decisions.md:11238-11259` WAY-341 · `foundations/part_map.md:114-123` process-audit · `instruction-files/kind_skill.md` · `instruction-files/changing.md` · Foundation entries rows 2, 3
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B instruction-files/check_instructions.py .` exits as it does on the base and lists no finding on `process-audit/SKILL.md` that it did not list there; `python -B -m unittest discover -s gate -p "test_skills_reach_the_way_sessions.py"`
- **Depends on:** Slice 7

Passages of the task and the plan its *Read* names, copied word for word:

#### `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:37-37` To do, item 6

6. Instrukcja sesji audytu (`process-audit/SKILL.md`) kładzie te miary przed Mariuszem na sesji.

#### `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:46-51` Questions to settle, whether the count reads the new numbers

- Czy cotygodniowe liczenie audytu ma czytać nowe liczby (plik miar z punktu 2 i czasy bramki z punktu 4) i pokazywać je w swoim wyniku, czy to zadanie tylko zaczyna je zbierać w zapisach cykli?
  - Answer: Czyta je i pokazuje razem z medianami każdej wersji procesu i porównaniem z poprzednią wersją tej samej serii (wariant pełny).
  - Not chosen:
    - tylko zbierać w zapisach cykli — liczby leżą w katalogach cykli, do których sesja audytu nie zagląda, a porównanie „przed i po” trzeba robić ręcznie
    - czytać i pokazywać wartości każdego cyklu, bez median i porównań wersji — „sam na oko to nic nie porównam sensownie”
  - Source: Mariusz, 2026-11-12: „wolę wariant pełny, bo sam na oko to nic nie porównam sensownie”

#### `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md:266-298` Slice 6 — The count reads the measures file and the gate times of each cycle and shows their values

### Slice 6 — The count reads the measures file and the gate times of each cycle and shows their values

- **Goal:** `process-audit/audit_count.py` reads, from the last copy of each cycle, the files `mechanism_measures.md` and
  `gate_times.md` as the plan's Slice 1 and Slice 3 give their form, keeps the values on the cycle, and writes two sections of
  the result, `## Mechanism measures` and `## Gate runs`, after `## Cost` and before `## Process versions`. No series, median or comparison
  is made here (Slice 7).
  *Reading.* A copy with no such file gives its values unknown with the reason that the copy holds none, an earlier form,
  and no `Error:`. A file that is there is read by its labels: in `mechanism_measures.md` each line label of the form, found
  once, and the table `## Agents` is no needed field; in `gate_times.md` the six columns of the table's header row. A
  needed field the file lacks — a label never written, a column absent — gives every value of that file unknown, the result
  written, and exit code 1 with an `Error:` line that names the file of the copy and the field, joining Slice 5's mechanism
  (the row 6 of the settlements). A label written twice, a value that is not what its label gives, or a row of the table with
  the wrong number of cells is no missing field: the value, or the run, is unknown with a reason in *Unknown values*, and the
  count goes on. `unknown` written by the script is read as unknown. Work and size are bounded as the other readings are: a
  file over the limit already used for the copy's files is not read; at most a fixed number of runs per file and of
  directories per run are read, and the rest give unknown with that reason; every text from a file reaches the result
  as the cells of the result are written, one line, bars escaped, and cut.
  *Sections.* `## Mechanism measures`: one row per cycle with the columns `Repository`, `Record` and one for each cycle-level
  line of the file, named as its label, `unknown` where it is unknown; the per-agent table stays in the file. `## Gate runs`: one
  row per run — `Repository`, `Record`, `Started (UTC)`, `Exit code`, `Total seconds`, `Other gate runs at the same time` and
  `Directories`, a cell listing each directory with its seconds. A cycle with no run has no row there. A line before each
  table says which script writes the file and that `unknown` is never zero.
  *Tests* (`process-audit/test_audit_count.py`, in classes whose names hold `Measures`): a cycle with both files read against values worked out by hand; a copy
  without them; the last copy read where a later copy differs; for each of the two readings one test that gives the file
  without a field and asserts exit code 1, the result written, that cycle's values `unknown` and the `Error:` line naming the
  file and the field; a doubled label and a malformed value giving unknown with no `Error:`; a crafted file — bars, control
  characters, very many runs and directories — breaking no cell and costing bounded work.
- **Change:** `process-audit/audit_count.py` · `process-audit/test_audit_count.py`
- **Read:** `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:36-36` To do, item 5 · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:46-51` Questions to settle, whether the count reads the new numbers · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:63-68` Questions to settle, the gate times between versions · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:116-125` Settlements to record · `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md:30-100` Slice 1 — The measures script, for Claude Code sessions · `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md:132-184` Slice 3 — The script that runs the gate and records its times · `foundations/decisions.md:11320-11397` WAY-344 · `foundations/decisions.md:10868-10917` WAY-328 · `foundations/decisions.md:1026-1051` WAY-38 · `foundations/invariants.md:86-95` tracked-file-private-paths · `foundations/part_map.md:114-123` process-audit · `foundations/part_map.md:231-239` External context · Foundation entries rows 2, 6 · `foundations/decisions.md:11166-11192` WAY-338 · `foundations/decisions.md:11294-11319` WAY-343
- **Model:** cheaper
- **Risk:** trust boundary — `process-audit/audit_count.py`, which reads the copies of the cycles' records from git history, untrusted input
- **Checks:** `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k Measures` — the new tests fail before the slice and pass after; `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` once at the end of the slice; `git diff 2292f334d5499f45b68b00c477cd76a2effd7537 HEAD -- process-audit/audit_count.py` shows no changed line in the assignment of `TREE_PATHS`; `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` after the slice's commit
- **Depends on:** Slice 5 · Slice 1 · Slice 3 · Foundation entries rows 2, 6

#### `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md:300-335` Slice 7 — Series by instrument, the median of each measure per version and the comparison with the previous version

### Slice 7 — Series by instrument, the median of each measure per version and the comparison with the previous version

- **Goal:** `process-audit/audit_count.py` groups the versions of the process into series of the mechanism measures and series of the
  gate times, each by the change of its own instrument alone, and writes the section `## Measure versions` with the median of each
  measure of each version and whether it falls against the previous version of the same series. The series of the cost, `TREE_PATHS`
  and the section `## Process versions` stay exactly as they are.
  *Series.* The mechanism measures' series begin at a version whose `task-cycle/cycle_measures.py` differs from the previous version's;
  the gate times' series at one whose `task-cycle/gate_times.py` differs — by the same test as the reviewed files' test (`git diff
  --quiet`; exit 1 or any failure counts as changed). Neither a new price list, nor a date of the register's list of classes, nor
  a change under `task-cycle/change`, `task-cycle/plan`, `task-cycle/review`, `task-cycle/spec` or of `task-cycle/cycle_stages.py`
  splits them. The cycles in no version stand in no series, as for the cost. Each series is its own subsection.
  *Mechanism measures per version.* A long table with the columns `Version (commit)`, `Measure`, `Cycles with a value`, `Median` and
  `Falls`: a row for each cycle-level measure of the file of Slice 1 (each label's name as `Measure`). The median is of the values
  of the version's cycles that give one, by the rule the median of the cost uses; `Falls` is `yes` where the median is lower than the
  previous version's median of the same measure in the same series, `no` otherwise, and `unknown` where the version is the first of
  its series or either median is not known, each unknown with its reason in *Unknown values*.
  *Gate times per version.* The same long table with `Measure` the total time of the run and the time of each directory that any
  run of the version has, and the columns `Version (commit)`, `Measure`, `Runs with no other gate`, `Median (seconds)`, `Falls`,
  `Runs with another gate or an unknown count` and `Median of those (seconds)`. Runs are taken together over all the cycles of the
  version. The median and `Falls` take only the runs whose count of other gates is `0`; the runs with another gate, or with the
  count `unknown`, are counted and their median shown in the last two columns and are never compared, and a version in which no
  run was alone has no comparison (`unknown`, with that reason). A directory's median takes the runs that give its time.
  The section opens with lines that say how the series are made and that a number of one series is never set beside a number of
  another. A median that is a half is written with its decimal; values are kept as `Decimal`.
  *Tests* (`process-audit/test_audit_count.py`, in a class whose name holds `MeasureVersions`, on the helpers of `ProcessVersions`): a change of `task-cycle/cycle_measures.py` starts
  a mechanism series and not a gate series, and the other way round; a change of `task-cycle/review/…`, of `task-cycle/cycle_stages.py`
  or of the price list starts a series of the cost and none of the measures; a change of the two instruments does not split the
  series of the cost (the criterion that adding the scripts starts no new series of cost); medians and `Falls` worked by hand
  for three versions of one series, over an even and an odd number of cycles; the gate table with runs alone, runs with another
  gate and a count unknown, the apart columns never entering the comparison; a version with no cycle that gave a value.
- **Change:** `process-audit/audit_count.py` · `process-audit/test_audit_count.py`
- **Read:** `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:36-36` To do, item 5 · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:39-42` Acceptance criteria · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:52-56` Questions to settle, what starts a new series · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:63-68` Questions to settle, the gate times between versions · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:116-125` Settlements to record · `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md:30-100` Slice 1 — The measures script, for Claude Code sessions · `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md:132-184` Slice 3 — The script that runs the gate and records its times · `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md:266-298` Slice 6 — The count reads the measures file and the gate times of each cycle and shows their values · `foundations/decisions.md:11193-11217` WAY-339 · `foundations/decisions.md:11238-11259` WAY-341 · `foundations/decisions.md:10990-11013` WAY-331 · `foundations/decisions.md:10868-10917` WAY-328 · `foundations/invariants.md:86-95` tracked-file-private-paths · `foundations/part_map.md:114-123` process-audit · Foundation entries rows 2, 3, 5 · `foundations/decisions.md:11166-11192` WAY-338 · `foundations/decisions.md:11294-11319` WAY-343
- **Model:** same — the series, median and comparison logic of a 2200-line file at a trust boundary, which must leave the series of the cost untouched
- **Risk:** trust boundary — `process-audit/audit_count.py`, which reads the copies of the cycles' records from git history, untrusted input
- **Checks:** `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k MeasureVersions -k ProcessVersions` — the new tests fail before the slice and pass after; `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` once at the end of the slice; `git diff 2292f334d5499f45b68b00c477cd76a2effd7537 HEAD -- process-audit/audit_count.py` shows no changed line in the assignment of `TREE_PATHS`; `git diff --quiet 2292f334d5499f45b68b00c477cd76a2effd7537 HEAD -- task-cycle/cycle_stages.py task-cycle/change task-cycle/plan task-cycle/review task-cycle/spec` exits 0; `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` after the slice's commit
- **Depends on:** Slice 6 · Foundation entries rows 2, 3, 5

Foundation entries of its *Read*, by identifier with the current range in the worktree (read each whole; the
current ranges hold where they differ from the plan's):

- `foundations/decisions.md:11193-11233` WAY-339
- `foundations/decisions.md:11254-11275` WAY-341
- `foundations/part_map.md:115-124` process-audit
- `foundations/decisions.md:11519-11548` WAY-348 (written by the foundation-entries agent of this change)
- `foundations/decisions.md:11193-11233` WAY-339 (written by the foundation-entries agent of this change)

Files and ranges of code or tests to read (as its *Read* names them; read each as far as you need):

- `instruction-files/kind_skill.md`
- `instruction-files/changing.md`

Foundation entries of this change already written (commit `a030dbf`): WAY-347 to WAY-352, WAY-339 and WAY-344 changed
in place, and the trust boundary of `task-cycle` in `foundations/part_map.md` naming `task-cycle/cycle_measures.py`.

Notes from the orchestrator: (1) Slices 5–7 are committed (`0e75a4b`, `0964b52`, `9209ecb`, `49ab2fa`); read the section titles and lines the count now writes in `process-audit/audit_count.py` (`## Mechanism measures`, `## Gate runs`, `## Measure versions`, and the lines that open each section) so that the instruction's words match what the count writes; the sections' opening lines in the result say how the series are made. (2) The sentence at `process-audit/SKILL.md:143-145` (a `stages.md` of an earlier form gives no cost) is stale since slice 5 — the plan's Matter 1 edit brings it to what the count does now: the earlier form gives the cost from the table of tokens by model and leaves its share of the fix rounds unknown. (3) The gate times of runs with another gate beside are shown apart and never compared; a gate run alone enters the comparison whatever its exit code. (4) Do not change the skill's description (entry points are not regenerated); keep the plain-language and instruction-file rules of `instruction-files/kind_skill.md` and `instruction-files/changing.md`; run the two checks of the slice. (5) The step that writes the result's note keeps working unchanged.

Return as `make-change` gives for a slice: status, commits (the slice's range from its base to its head), a one-line
check result naming what failed or did not run, the report path; in the report: each check with its command and exit
code, the own-work check, **Unread material** and **Searches not found or unclear** (each `none` where none), every
reach beyond this handoff, and the choices you made.

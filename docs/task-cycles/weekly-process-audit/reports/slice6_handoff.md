# Handoff — executor of slice 6 (`make-change`: "a slice, or the retry of a slice")

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator, and the
orchestrator answers your questions. Nothing here is that person's approval. Your questions go to the
orchestrator, never to the human.

## Where you work

- Worktree (work from its root, read every file from it): `the worktree of the task`, branch `task/weekly-process-audit`.
- Base of this slice: `7bb25c3`. The slices before yours and the foundation entries are in the history before it.
- The product is the-way itself: methods live in the worktree.
- Method: `task-cycle/change/SKILL.md`; you make "a slice, or the retry of a slice". Read it whole, then `task-cycle/change/slice.md` whole,
  and any other file they name only when the step that names it comes.
- Report path: `docs/task-cycles/weekly-process-audit/reports\slice6_report.md`.

## Answers of the start

- Trust boundary: yes — the change adds a command that reads files from outside the repository (cycle records, `stages.md`,
  the register of problems, the price list, the locations file). Crafted input at that boundary is checked by the review.
- Irreversible operation: no. Never write into the user's real `~/.the-way` or the user's places named by the locations file
  from a test or a check: tests use temporary directories and temporary locations files.
- Product guidelines: the-way has none; do not look for them.

## Inputs

- Frozen task (read the passages the slice's *Read* names): `.runs/task-cycles/weekly-process-audit/task.md`.
- Plan: `.runs/task-cycles/weekly-process-audit/plan.md` — your slice's section is copied below word for word;
  read nothing else of the plan except "Foundation entries" rows your slice names (copied below).
- The foundation entries "row N" of the plan are decisions of `foundations/decisions.md`: row 1 = WAY-329, row 2 = WAY-330,
  row 3 = WAY-331, row 4 = WAY-332, row 5 = WAY-333, row 6 = WAY-334, row 7 = WAY-335, row 8 = WAY-336, row 9 = WAY-337,
  row 10 = WAY-338, row 11 = WAY-339, row 12 = WAY-340 (renumbered after the target branch took WAY-327 and WAY-328); "WAY-09 changed" is WAY-09 as it stands now.

## Current ranges (these hold where they differ from the numbers in the section below)

WAY-38 foundations/decisions.md:1025-1050
WAY-48 foundations/decisions.md:1199-1228
WAY-332 foundations/decisions.md:10909-10931
WAY-334 foundations/decisions.md:10952-10972
WAY-336 foundations/decisions.md:10995-11035
WAY-338 foundations/decisions.md:11056-11080
script-language foundations/invariants.md:106-115
script-imports foundations/invariants.md:116-125
script-subprocesses foundations/invariants.md:126-135

## Your slice, word for word from the plan

### Slice 6 — The measures of each process version, series kept apart

- **Goal:** `process-audit/audit_count.py` gives for each version of the process — the cycles
  grouped by their *Process pin* — the median of the cycle cost at constant prices, and the answers
  to three questions about simplifying the rules of the spec and the plan: did a contradiction with
  the product's settlements come out only after code was written (the record's *Discarded attempt*
  for an open design choice, or a review round whose blocking finding names a foundation entry);
  did more than one in three slices of the plans come back as too large (the record's *Plan* and
  *Slices returned too large*); does the cycle cost fall (the median against the previous version
  in the same series). A series starts anew with a new price list (Slice 4), a change of the
  register's list of classes (Slice 1), and a change, between two pins, of the form of a stage's
  report — in the methods under `task-cycle/change/`, `task-cycle/plan/`, `task-cycle/review/` and
  `task-cycle/spec/` — or of the reviewer's instructions under `task-cycle/review/`; the result never
  compares numbers of two series directly and shows them apart (Foundation entries row 10). An
  answer the records cannot give is `unknown` with its reason. The records stay untrusted input,
  with tests of crafted input. Name in your report how the versions are grouped and how a change of
  a report's form is told from another change of those files.
- **Change:** `process-audit/audit_count.py` · `process-audit/test_audit_count.py`
- **Read:** `.runs/task-cycles/weekly-process-audit/task.md:23-36` To do ·
  `.runs/task-cycles/weekly-process-audit/task.md:91-108` Settlements to record · Foundation entries
  row 4 · Foundation entries row 8 · Foundation entries row 10 · `foundations/decisions.md:1192-1220`
  WAY-48 · `foundations/decisions.md:1018-1042` WAY-38 · `foundations/invariants.md:106-134`
  script-language · script-imports · script-subprocesses · `foundations/glossary.md:97-101` open design choice · `foundations/glossary.md:145-149`
  slice · `task-cycle/record_template.md`
- **Model:** cheaper
- **Risk:** trust boundary — `process-audit/audit_count.py` reads the cycle records of repositories
  the user names
- **Checks:** first a failing test: cycles of two pins in one series and one cycle after a new price
  list, from which the command gives each version's median, compares the first two and does not
  compare across the series · `python -B gate/run_tests.py process-audit` ·
  `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` exits 0 · a run of
  the command on this repository with stdin closed, with its exit code in the report
- **Depends on:** Slice 4 · Slice 5 · Foundation entries row 4 · row 8 · row 10

## The plan's Foundation entries (for the rows your slice names), word for word

## Foundation entries

| Entry | Kind | From | What depends on it |
|---|---|---|---|
| Row 1 — the-way gives the template of the register of problems; the audit reads the register a locations entry names; the user's own tool fills it and the user adapts the template | decision | *Settlements to record* row 1 | Slice 1 · Slice 5 · Slice 7 |
| Row 2 — the audit is a part of its own with its own directory, apart from the task cycle | decision | *Settlements to record* row 2 | Slice 1 · Slice 7 |
| Row 3 — the audit's results lie in the user's place outside every repository, named by a locations entry | decision | *Settlements to record* row 3 | Slice 3 · Slice 7 |
| Row 4 — four levels of weight, and a list of classes the template starts and the audit widens | decision | *Settlements to record* row 4 | Slice 1 · Slice 5 · Slice 6 |
| Row 5 — the audit counts problems, not remarks: one problem reported by several stages is one | decision | *Settlements to record* row 5 | Slice 1 · Slice 5 |
| Row 6 — whether a fix works is settled by the cycles whose the-way version holds it, not by a date | decision | *Settlements to record* row 6 | Slice 5 |
| Row 7 — how often an issue comes back is material for the human to weigh; the audit sets no priority from it | decision | *Settlements to record* row 7 | Slice 5 · Slice 7 |
| Row 8 — a cycle's cost is its cost at constant prices from a dated price list and the share of fix rounds in it, with no denominator of task size | decision | *Settlements to record* row 8 | Slice 2 · Slice 4 · Slice 6 |
| Row 9 — a cycle's time is the agents' working time without the wait for the human, and apart the wait for tools | decision | *Settlements to record* row 9 | Slice 2 · Slice 3 |
| Row 10 — a new price list, or a change of a stage report's form, of the list of classes or of the reviewer's instructions, starts a new series; measures compare within a series and a process version | decision | *Settlements to record* row 10 | Slice 4 · Slice 6 · Slice 7 |
| Row 11 — the audit replays no frozen earlier tasks on an old and a new process version | decision | *Settlements to record* row 11 | Slice 7 |
| Row 12 — the audit runs weekly, apart from the weekly review; the counting runs unattended on the night from Friday to Saturday, and a weekly backlog task starts the session | decision | *Settlements to record* row 12 | Slice 3 · Slice 7 |
| WAY-09 changed — the list of the repository's directories gains the audit part's directory, and the sentence of what a directory must hold gains what that one holds | decision | *To do* item 1 | Slice 1 |
| WAY-38 changed — its *Scope* gains `process-audit`, whose command is a script of the-way | decision | *To do* items 1 and 3, through WAY-21 | Slice 3 |
| WAY-89 changed — its *Scope* gains `process-audit` | decision | *To do* items 1 and 3, through WAY-21 | Slice 3 |
| WAY-320 changed — its *Scope* gains `process-audit`, whose skill and command read the locations file | decision | *To do* item 6, through WAY-21 | Slice 3 · Slice 5 · Slice 7 |

The rows and the changes name the part `process-audit`, whose part-map entry Slice 1 writes with the
first file of its directory (`task-cycle/plan/SKILL.md`: a change to the part map for a file the
change adds belongs to the slice that adds the file). Until Slice 1 is made,
`python -B elements/common/foundation_check.py --skip-test-citations` reports the references to that
part, and only those; after Slice 1 it reports nothing.

## Notes of the orchestrator

- Slices 1–5, the correction and the merge of the target branch are made and reviewed (head `7bb25c3`). Read `process-audit/audit_count.py` and
  `process-audit/test_audit_count.py` as they stand, whole, before you change them, and the reports `reports/slice4_report.md`,
  `reports/correction_report.md`, `reports/slice5_report.md` and `reports/slice5_fix_report.md` for what the result already holds (`## Cycles`,
  `## Cost` with the cost at constant prices and the share of fix rounds, `## Problems by cycle` with *Refused rows*, the fixed and open issues,
  `cell()`, `--today`, the resolution of a pin in the-way's checkout by `git rev-parse --verify`).
- **Numbering:** the audit's decisions are WAY-329…WAY-340 (the plan's "row n" = WAY-(328+n)); the plan's text that names a "WAY-3xx" is out of
  date by two. The series decision is WAY-338, the cost decision WAY-336.
- **Binding choices of the orchestrator (record as autonomous choices; name any you cannot hold):**
  1. A *version of the process* is the full commit of the-way that a cycle's *Process pin* resolves to in the-way's checkout (slice 5 resolves
     pins already; reuse it). Cycles whose pin is `unknown`, unresolvable or ambiguous stand in one row apart, "no version", with the reason, and are in
     no series.
  2. Versions are ordered by the committer date of the pin commit (`git log -1 --format=%ct`, converted without raising; a value that cannot be
     read puts the version in "no version"), ties by the full hash. The order is the order of the result's rows within a series.
  3. A **series** is a run of consecutive versions (in that order) between which none of these changes: (a) the date of the price list the cost was
     priced by (slice 4 reads the list's date); (b) the register's list of classes (the dates of *Added* and *Withdrawn* of *Classes*); (c) the tree
     of the-way under the paths `task-cycle/change`, `task-cycle/plan`, `task-cycle/review`, `task-cycle/spec` and `task-cycle/cycle_stages.py`
     between the two pins (`git diff --quiet <earlier> <later> -- <those paths>` in the-way's checkout; exit 1 = changed; any other failure =
     treat as changed). Choice (c) is deliberately conservative: any change of those files splits the series, though not every change alters the form of
     a stage report or the reviewer's instructions; it errs toward fewer comparisons, never a false one. Name this in the docstring and the report.
  4. Measures are never compared across series: each series is its own section of the result, and no cell sets a number of one series beside a
     number of another (WAY-338). A series with a single version has no "previous version".
  5. Per version: the number of cycles, the number with a known cost, and the **median of the cost at constant prices** of the cycles with a known cost
     (`unknown` where none is known). Use `Decimal`; the median of an even count is the mean of the two middle values; write with the digits the *Cost*
     table writes.
  6. The three questions per version, each `yes`, `no` or `unknown` with a reason, never guessed:
     (Q1) did a contradiction with the product's settlements come out only after code was written — read from the record's item *Discarded attempt*
     (`none` = no; text that names an open design choice = yes; any other text, or the item missing or doubled = unknown); where the record has no
     discarded attempt but its *Review rounds* name a round, answer `unknown`, because the findings are not in the record;
     (Q2) did more than one in three slices of the plans come back as too large — slices made = the first integer before the word `slices` in the
     record's item *Plan* (`none on the one-author route` = no plan, left out), too large = the entries of *Slices returned too large* (`none` = 0, a
     list = its entries; anything unreadable = unknown); the answer is `yes` when the sum of too-large slices over the sum of planned slices of the
     version's cycles is above one third, `no` when not, `unknown` where no cycle's plan can be read;
     (Q3) does the cost fall — the median cost of this version against the previous version *in the same series*: `yes` (lower), `no` (not lower),
     `unknown` (no previous version in the series, or an unknown median).
     Name in the report how you read each item, the forms of the archive you saw (`git show` of records in the history), and where a reading is
     narrow so that `unknown` is common.
  7. The record's items are read as slice 5 reads them (a doubled item is `unknown`).
- **Lessons of the trust-boundary reviews** (slices 3, 4 and 5 failed on these): no regular expression that backtracks on a long run of spaces, dashes or
  colons; every number or date taken from untrusted text goes through a conversion that cannot raise on a huge or out-of-range value and gives
  `unknown` with a reason; every cell written to the result passes `cell()`; a cap on every read and on the length of a text copied into the result; a
  failure of one row, cycle or version is `unknown` for it, never an abort; a value from a record or the register is never given to git as an option
  (`--end-of-options`); a refused or unreadable row is shown as unknown or `at least n`, never as zero; work and output bounded by input size (no
  quadratic grouping over a big register or many cycles — use a dictionary). Tests cover each.
- Checks: temporary locations files, registers and directories as in the earlier tests; the run on this repository with stdin closed uses a temporary
  locations file naming this worktree as a repository, with a temporary register and results directory; give the exit code and the first lines of the
  result, including how many versions and series it found.
- Do not touch the *Cost* section's rules or the stage report's form.

## Report

Return your status (`done`, `done with concerns`, `questions`, `returned`, `reserved`, `blocked`), your commits, a one-line
check result naming what failed or did not run, the report path, your questions and concerns, each reach beyond this
handoff, **Unread material** (what this handoff names that stayed unread or was read in part, or `none`) and
**Searches not found or unclear** (or `none`), with each check you ran as its command and exit code, and the own-work check
`make-change` requires. Commit your work with `git add <paths>` (never `git add -A`), messages in English.

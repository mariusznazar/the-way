# Handoff — executor of slice 5 (`make-change`: "a slice, or the retry of a slice")

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator, and the
orchestrator answers your questions. Nothing here is that person's approval. Your questions go to the
orchestrator, never to the human.

## Where you work

- Worktree (work from its root, read every file from it): `the worktree of the task`, branch `task/weekly-process-audit`.
- Base of this slice: `9cf2633`. The slices before yours and the foundation entries are in the history before it.
- The product is the-way itself: methods live in the worktree.
- Method: `task-cycle/change/SKILL.md`; you make "a slice, or the retry of a slice". Read it whole, then `task-cycle/change/slice.md` whole,
  and any other file they name only when the step that names it comes.
- Report path: `docs/task-cycles/weekly-process-audit/reports\slice5_report.md`.

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
WAY-89 foundations/decisions.md:2022-2046
WAY-320 foundations/decisions.md:10420-10485
WAY-329 foundations/decisions.md:10833-10862
WAY-332 foundations/decisions.md:10909-10931
WAY-333 foundations/decisions.md:10932-10951
WAY-334 foundations/decisions.md:10952-10972
WAY-335 foundations/decisions.md:10973-10994
WAY-336 foundations/decisions.md:10995-11035
script-language foundations/invariants.md:106-115
script-imports foundations/invariants.md:116-125
script-subprocesses foundations/invariants.md:126-135

## Your slice, word for word from the plan

### Slice 5 — Problems and issues from the register

- **Goal:** `process-audit/audit_count.py` reads the register of problems at the place its
  locations entry names (Slice 3), in the form of `process-audit/problem_register.md` (Slice 1), and
  gives: for each cycle, its problems by class and by weight, one problem that several stages
  reported counted once (Foundation entries row 5); for each issue whose fix is in place, the
  problems of that issue in the cycles whose *Process pin* holds the fix's commit — the fix an
  ancestor of the pin in the-way's history — and apart in the cycles whose pin does not hold it,
  never by a date (row 6); for each open issue, the number of cycles in which its problem came back
  and the number of days it has waited. It gives no ranking and no priority from how often an issue
  comes back (row 7). A problem whose cycle no named repository holds, or a pin or a fix commit
  the-way's history lacks, gives `unknown` with its reason. The register is untrusted input, with
  tests of crafted input as in Slice 3. Name in your report which repository of the-way answers
  whether a pin holds a fix, and from what date the days of waiting count.
- **Change:** `process-audit/audit_count.py` · `process-audit/test_audit_count.py`
- **Read:** `.runs/task-cycles/weekly-process-audit/task.md:23-36` To do ·
  `.runs/task-cycles/weekly-process-audit/task.md:38-65` Questions to settle ·
  `.runs/task-cycles/weekly-process-audit/task.md:91-108` Settlements to record · Foundation entries
  row 1 · Foundation entries row 4 · Foundation entries row 5 · Foundation entries row 6 · Foundation
  entries row 7 · `foundations/decisions.md:1192-1220` WAY-48 ·
  `foundations/decisions.md:10321-10384` WAY-320 · `foundations/decisions.md:1018-1042` WAY-38 ·
  `foundations/decisions.md:1991-2014` WAY-89 · `foundations/invariants.md:106-134`
  script-language · script-imports · script-subprocesses ·
  `task-cycle/record_template.md:1-15` Cycle record ·
  process-audit/problem_register.md as Slice 1 made it
- **Model:** cheaper
- **Risk:** trust boundary — `process-audit/audit_count.py` reads the user's register of problems
- **Checks:** first a failing test: a temporary repository of the-way with a fix commit and two pins,
  one holding it, and a register with one issue whose problem stands in a cycle of each pin, from
  which the command gives the two counts apart · `python -B gate/run_tests.py process-audit` ·
  `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` exits 0 · a run of
  the command with a test register and stdin closed, with its exit code in the report
- **Depends on:** Slice 1 · Slice 4 · Foundation entries row 1 · row 4 · row 5 · row 6 · row 7

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

- Slices 1–4, the correction and the merge of the target branch are made and reviewed (head `9cf2633`). Read `process-audit/audit_count.py` and
  `process-audit/test_audit_count.py` as they stand, whole, before you change them; and `process-audit/problem_register.md` (the register's four
  tables; you read the one the user fills). Read the reports `reports/slice3_report.md`, `reports/slice3_fix_report.md`,
  `reports/slice4_report.md` and `reports/correction_report.md` for the shapes you build on (the `## Cycles` and `## Cost` tables of the result,
  `cell()`, the reading of records, and the cycle identification by folder and first commit).
- **Numbering:** the decisions of the audit are WAY-329…WAY-340 (the plan says "row n" = WAY-(328+n)); the plan's text that names "WAY-3xx" for the
  audit's rows is out of date by two. Use the numbers of the log as it stands.
- **Binding choices of the orchestrator (record as autonomous choices; name any you cannot hold):**
  1. The register is read from the file the entry `problem_register` under `the-way` names (slice 3 already checks that it exists). Parse the four
     tables of the template by their headings and header rows, as its section "What the counting command reads" gives. A malformed table, an unknown
     class or weight, an issue name that is in no row of *Issues*, a doubled name, a `Fix` that is no 40-character commit, a date that is no date:
     the row is refused with a reason, `unknown` for what depends on it, never an abort of the run; a table missing altogether is an `Error:` of the
     register (exit 2 only where the register itself cannot be read at all, as for the other entries).
  2. A problem belongs to the cycle named by its *Repository* and *Record*. The cycle is found among the cycles the command read, by the folder and the
     commit (a later copy of the same cycle counts as the same cycle, as slice 3 settled). A problem whose cycle no named repository holds gives
     `unknown` with the reason; it is not dropped.
  3. Per cycle: the problems by class and by weight; a problem reported by several stages is one row of the register, so count rows (WAY-333).
  4. Whether a pin holds a fix: the repository of the-way (the checkout `the_way_checkout` finds, as slice 3 settled) answers with
     `git merge-base --is-ancestor <fix> <pin>`; a pin written as a short hash is resolved in that checkout with `git rev-parse --verify` (a
     value that begins with `-` is never given to git as an option; use `--end-of-options` or refuse it); a pin or fix commit the checkout lacks, an
     ambiguous short hash, or a pin written `unknown` gives `unknown` for that cycle's side of the comparison with the reason.
  5. For each issue whose *Fate* is `fixed`: the problems of that issue in cycles whose pin holds the fix, and apart those in cycles whose pin does not
     hold it, never by date (WAY-334); cycles with an unknown pin are counted apart as unknown. For each issue that is `open`: the number of cycles in
     which a problem of the issue stands, and the days it has waited — the days from the date of the earliest commit named in the *Record* column
     among the issue's problems to the day of the run. The day of the run is an option `--today YYYY-MM-DD` (default: today in UTC), so that the same
     input and the same `--today` give the same bytes. An issue `dropped` is counted apart and gives no waiting. Name this choice in the report.
  6. No ranking and no priority from how often an issue comes back (WAY-335): the issues are listed in the order of the register, never sorted by
     count or by waiting.
  7. A cycle committed twice and counted once must count its problems once.
- **Lessons of the trust-boundary reviews** (slices 3 and 4 failed on these): no regular expression that backtracks on a long run of spaces, dashes or
  colons; every number or date taken from untrusted text goes through a conversion that cannot raise on a huge or out-of-range value and gives `unknown`
  with a reason; every cell written to the result passes `cell()`; a cap on every read and on the length of a text copied into the result; a failure of
  one row or cycle is `unknown` for it, never an abort. The register is the user's own file, yet it is read as untrusted. Tests cover each.
- The result keeps its form: add the tables you need (for example `## Problems by cycle`, `## Fixed issues`, `## Open issues`), deterministic, UTF-8, LF.
- Checks: temporary locations files and directories as in the tests of slices 3 and 4; the run on this repository with stdin closed uses a temporary
  locations file with a temporary register (a copy of the template with one row of each kind) and a temporary results directory; give the exit code and
  the first lines of the result.
- The correction changed the *Cost* section and the stage report's form; do not touch them.

## Report

Return your status (`done`, `done with concerns`, `questions`, `returned`, `reserved`, `blocked`), your commits, a one-line
check result naming what failed or did not run, the report path, your questions and concerns, each reach beyond this
handoff, **Unread material** (what this handoff names that stayed unread or was read in part, or `none`) and
**Searches not found or unclear** (or `none`), with each check you ran as its command and exit code, and the own-work check
`make-change` requires. Commit your work with `git add <paths>` (never `git add -A`), messages in English.

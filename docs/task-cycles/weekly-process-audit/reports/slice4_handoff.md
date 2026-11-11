# Handoff — executor of slice 4 (`make-change`: "a slice, or the retry of a slice")

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator, and the
orchestrator answers your questions. Nothing here is that person's approval. Your questions go to the
orchestrator, never to the human.

## Where you work

- Worktree (work from its root, read every file from it): `the worktree of the task`, branch `task/weekly-process-audit`.
- Base of this slice: `116f319`. The slices before yours and the foundation entries are in the history before it.
- The product is the-way itself: methods live in the worktree.
- Method: `task-cycle/change/SKILL.md`; you make "a slice, or the retry of a slice". Read it whole, then `task-cycle/change/slice.md` whole,
  and any other file they name only when the step that names it comes.
- Report path: `docs/task-cycles/weekly-process-audit/reports\slice4_report.md`.

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
- The foundation entries "row N" of the plan are decisions of `foundations/decisions.md`: row 1 = WAY-327, row 2 = WAY-328,
  row 3 = WAY-329, row 4 = WAY-330, row 5 = WAY-331, row 6 = WAY-332, row 7 = WAY-333, row 8 = WAY-334, row 9 = WAY-335,
  row 10 = WAY-336, row 11 = WAY-337, row 12 = WAY-338; "WAY-09 changed" is WAY-09 as it stands now.

## Current ranges (these hold where they differ from the numbers in the section below)

WAY-38 foundations/decisions.md:1025-1050
WAY-48 foundations/decisions.md:1199-1228
WAY-89 foundations/decisions.md:1998-2022
WAY-334 foundations/decisions.md:10798-10820
WAY-336 foundations/decisions.md:10841-10865
script-language foundations/invariants.md:106-115
script-imports foundations/invariants.md:116-125
script-subprocesses foundations/invariants.md:126-135

## Your slice, word for word from the plan

### Slice 4 — The cost of a cycle at constant prices

- **Goal:** `process-audit/price_list.md` holds the price list with its date: for every model the
  cycles' `stages.md` name, its price per million tokens of input, of cached input and of output,
  each taken from the provider's published price page with the page's address and the date it was
  read, never from memory; a model whose price no page gives stands with no price. The command
  `process-audit/audit_count.py` gives for each cycle its cost at the list's prices and the share of
  that cost spent on rounds of fixes after a review — the fix of a review's blocking findings and
  the review of that fix, as the record's *Review rounds* and *Events* name them, tied to the stages
  of `stages.md` — with no denominator of task size (Foundation entries row 8). A model the list
  lacks, or a `stages.md` without each stage's tokens by model and kind, gives `unknown` with its
  reason, never a cost of zero. The list's date marks the series a cost belongs to, so that a new
  price list starts a new series (Foundation entries row 10). The record and `stages.md` stay
  untrusted input, as in Slice 3, with tests of crafted input. Name in your report how the command
  recognises the stages of a fix round.
- **Change:** `process-audit/price_list.md` · `process-audit/audit_count.py` ·
  `process-audit/test_audit_count.py`
- **Read:** `.runs/task-cycles/weekly-process-audit/task.md:23-36` To do ·
  `.runs/task-cycles/weekly-process-audit/task.md:91-108` Settlements to record · Foundation entries
  row 8 · Foundation entries row 10 · `foundations/decisions.md:1018-1042` WAY-38 ·
  `foundations/decisions.md:1192-1220` WAY-48 · `foundations/invariants.md:106-134` script-language ·
  script-imports · script-subprocesses · `task-cycle/record_template.md` ·
  `task-cycle/cycle_stages.py`
- **Model:** cheaper
- **Risk:** trust boundary — `process-audit/audit_count.py` reads the cycle records and `stages.md`
  of repositories the user names
- **Checks:** first a failing test: a record with one fix round and a `stages.md` whose stages use
  two models, from which the command gives the cost and the share of the fix round at a test price
  list · `python -B gate/run_tests.py process-audit` ·
  `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` exits 0 · a run of
  the command on this repository with stdin closed, with its exit code in the report
- **Depends on:** Slice 3 · Foundation entries row 8 · row 10

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

- Slices 1–3 are made and reviewed (head `116f319`). Read `process-audit/audit_count.py` and `process-audit/test_audit_count.py` as they
  stand, whole, before you change them, and the slice 2 and 3 reports for the shapes you build on:
  `.runs/task-cycles/weekly-process-audit/reports/slice2_report.md` (what `stages.md` now holds) and `slice3_report.md` and
  `slice3_fix_report.md` (the result's form, `cell()` and the reading of records).
- **Lessons of the trust-boundary review of slice 3** (it failed on these; the same reviewer-type will review you): never build a
  regular expression that backtracks on a long run of spaces, dashes or colons; every number or date taken from untrusted text goes
  through a conversion that cannot raise on a huge or out-of-range value and gives `unknown` with a reason; every cell written to
  the result passes the existing `cell()` (a bar is written `\x7c`); every new read has a size cap; a failure of one cycle is
  `unknown` for that cycle, never an abort of the run. Tests cover each.
- **Prices:** the orchestrator has read them from the providers' pages; they are in
  `.runs/task-cycles/weekly-process-audit/reports/prices_fetched.md` with the page addresses and the date read (2026-11-11). Copy
  them into `process-audit/price_list.md` exactly, keeping each page's address and the date, a table per provider; do not add a model
  or a price from memory. A model of `stages.md` the list lacks gives `unknown`, as the plan says. The list's date (the date the
  list was read, as a line the command parses) marks the series a cost belongs to (WAY-336).
- **Cache writes:** `cycle_stages.py` folds Claude Code's cache-creation tokens into *Input* (orchestrator's choice Q9): the cost
  prices them as input and the docstring of the cost says so, as an approximation.
- **Which price columns:** *Input* in `stages.md` includes the part read from a cache; the cost therefore prices
  (input − cached input) at the input price, cached input at the cached-input price and output at the output price. Check how
  `stages.md` defines its columns (its own header text) before you rely on it, and say in your report what you found.
- **Fix rounds:** name in your report how you recognise the stages of a fix round. The record's *Events* rows name the stage and
  the report (`review_*`, `*_fix_*` report names; a fix's handoff names "the fix of a review's findings"), and `stages.md` rows carry
  the stage names the orchestrator gave; where a cycle's stages cannot be tied to the rounds, the share is `unknown` with the reason.
- The result file keeps its form from slice 3; extend it with the columns/tables you need and keep determinism.
- Checks: use temporary locations files and temporary directories as in slice 3's tests; the run on this repository with stdin
  closed uses a temporary locations file and results directory.

## Report

Return your status (`done`, `done with concerns`, `questions`, `returned`, `reserved`, `blocked`), your commits, a one-line
check result naming what failed or did not run, the report path, your questions and concerns, each reach beyond this
handoff, **Unread material** (what this handoff names that stayed unread or was read in part, or `none`) and
**Searches not found or unclear** (or `none`), with each check you ran as its command and exit code, and the own-work check
`make-change` requires. Commit your work with `git add <paths>` (never `git add -A`), messages in English.

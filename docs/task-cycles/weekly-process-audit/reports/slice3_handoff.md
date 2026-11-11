# Handoff — executor of slice 3 (`make-change`: "a slice, or the retry of a slice")

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator, and the
orchestrator answers your questions. Nothing here is that person's approval. Your questions go to the
orchestrator, never to the human.

## Where you work

- Worktree (work from its root, read every file from it): `the worktree of the task`, branch `task/weekly-process-audit`.
- Base of this slice: `876710c`. The slices before yours and the foundation entries are in the history before it.
- The product is the-way itself: methods live in the worktree.
- Method: `task-cycle/change/SKILL.md`; you make "a slice, or the retry of a slice". Read it whole, then `task-cycle/change/slice.md` whole,
  and any other file they name only when the step that names it comes.
- Report path: `docs/task-cycles/weekly-process-audit/reports\slice3_report.md`.

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

WAY-48 foundations/decisions.md:1199-1228
WAY-49 foundations/decisions.md:1229-1252
WAY-38 foundations/decisions.md:1025-1050
WAY-89 foundations/decisions.md:1998-2022
WAY-107 foundations/decisions.md:2417-2454
WAY-140 foundations/decisions.md:3850-3900
WAY-260 foundations/decisions.md:7974-8004
WAY-296 foundations/decisions.md:9418-9439
WAY-320 foundations/decisions.md:10328-10393
WAY-329 foundations/decisions.md:10690-10711
WAY-335 foundations/decisions.md:10821-10840
WAY-338 foundations/decisions.md:10886-10954
tracked-file-private-paths foundations/invariants.md:86-95
script-language foundations/invariants.md:106-115
script-imports foundations/invariants.md:116-125
script-subprocesses foundations/invariants.md:126-135
cross-part-imports foundations/invariants.md:328-337

## Your slice, word for word from the plan

### Slice 3 — The counting command: the cycles of the named repositories and their times

- **Goal:** `process-audit/audit_count.py` exists. It finds the place of the register of problems
  and the place of the audit's results through entries of the locations file under `the-way`
  (WAY-320; the reading as `project-level/backlog_place.md` gives it), and where the file, the
  key, the entry or its path is missing it names the missing entry in an `Error:` line and exits
  non-zero without asking anything, so that the skill of Slice 7 asks the human. It takes the
  repositories whose cycles it reads as the user names them. It runs with no human: no prompt, git
  with its terminal prompt off, nothing read from stdin, so that a system scheduler can start it on
  the night from Friday to Saturday (Foundation entries row 12). It finds every cycle record
  committed in the history of each repository — the copy under `docs/task-cycles/<task-slug>/` that
  one commit adds and the next removes (`task-cycle/record_template.md`; `project-level/plan_state.py`
  reads such archived copies) — and identifies each cycle by its repository and the commit that adds
  the record, as the register of Slice 1 does. For each cycle it gives: the version of the-way the
  cycle ran on (the record's *Process pin*); the number of its process remarks (the entries under
  *Process remarks on the-way*; it may reuse the cutting of `task-cycle/remarks_check.py`); the
  agents' working time without the wait for tools, and the wait for tools, from the cycle's
  `stages.md` as Slice 2 gives it. A record or a `stages.md` in an earlier form that lacks a value
  gives `unknown` for it, never zero. It writes its result into the place of the audit's results,
  never into a repository, in a form that later slices extend and the skill reads. Every record,
  `stages.md` and the locations file is untrusted input: text from them stays within one line of
  output, as `display` in `project-level/plan_state.py` keeps it; no path taken from them is
  followed beyond what git lists; nothing of them is run. Its tests give crafted input — control
  characters, a record path that leaves its directory, a malformed table, a missing or a doubled
  field. The docstring gives the usage and the exit codes. In the part map, the part's *Trust
  boundary* names `process-audit/audit_count.py`, and its *Depends on* names every part whose file
  the command imports. Name in your report the entries read from the locations file, how the user
  names the repositories, and the shape of the result.
- **Change:** `process-audit/audit_count.py` · `process-audit/test_audit_count.py` ·
  `foundations/part_map.md`
- **Read:** `.runs/task-cycles/weekly-process-audit/task.md:23-36` To do ·
  `.runs/task-cycles/weekly-process-audit/task.md:38-65` Questions to settle ·
  `.runs/task-cycles/weekly-process-audit/task.md:67-71` Context ·
  `.runs/task-cycles/weekly-process-audit/task.md:77-80` Human actions · Foundation entries row 3 ·
  Foundation entries row 9 · Foundation entries row 12 · Foundation entries WAY-38 changed ·
  Foundation entries WAY-320 changed · `foundations/decisions.md:1018-1042` WAY-38 ·
  `foundations/decisions.md:1192-1220` WAY-48 · `foundations/decisions.md:1222-1245` WAY-49 ·
  `foundations/decisions.md:1991-2014` WAY-89 · `foundations/decisions.md:2410-2446` WAY-107 · `foundations/decisions.md:3843-3892` WAY-140 ·
  `foundations/decisions.md:7967-7996` WAY-260 · `foundations/decisions.md:9411-9431` WAY-296 ·
  `foundations/decisions.md:10321-10384` WAY-320 · `foundations/invariants.md:86-94`
  tracked-file-private-paths · `foundations/invariants.md:106-134` script-language · script-imports ·
  script-subprocesses · `foundations/invariants.md:328-336` cross-part-imports ·
  `task-cycle/record_template.md` · `task-cycle/remarks_check.py` · `task-cycle/cycle_stages.py` ·
  `project-level/plan_state.py` · `project-level/backlog_place.md` · process-audit/problem_register.md
  as Slice 1 made it
- **Model:** strongest — it sets the shape of the command's result, the entries it reads from the
  locations file and the way it finds cycle records in the history of repositories, on which
  Slices 4 to 7 build.
- **Risk:** trust boundary — `process-audit/audit_count.py` reads the cycle records and `stages.md`
  of repositories the user names, and the user's locations file
- **Checks:** first a failing test: a temporary git repository with a commit that adds a record copy
  and the next that removes it, from which the command gives the cycle with its *Process pin* and
  its number of remarks · `python -B gate/run_tests.py process-audit` ·
  `python -B gate/run_tests.py elements/part-map` · after committing,
  `python -B elements/common/foundation_check.py` exits 0 ·
  `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` exits 0 · a run of
  the command on this repository with stdin closed, as its usage gives, with its exit code and the
  result's first lines in the report
- **Depends on:** Slice 1 · Slice 2 · Foundation entries row 3 · row 9 · row 12 · WAY-38 changed ·
  WAY-320 changed

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

- Slices 1 and 2 are made: the template `process-audit/problem_register.md` (commit `4443973`; four tables *Classes*, *Weights*,
  *Issues*, *Problems*; *Repository* is "the name of the product's repository, as your locations file names it among its keys";
  *Record* is the commit that adds the copy of a cycle's record) and `task-cycle/cycle_stages.py` (commit `876710c`; `stages.md`
  now gives the wait for tools apart, each stage's start time and its tokens by model and kind). Read both as they stand.
- **Binding choices of the orchestrator for the shape (recorded as autonomous choices; name any you cannot hold in your report):**
  1. The repositories are named by keys of the locations file: a key (a product's name, as in the register's *Repository* column)
     whose object has an entry `repository` — the path of that product's checkout on the user's disk. The command takes
     `--repository <key>` (repeatable) to name the ones it reads; with none given it reads every key that has a `repository`
     entry. The-way's own checkout (needed by later slices to ask whether a version holds a fix) is the entry `repository` of the
     key `the-way`; where it is missing the command uses the checkout the script lies in.
  2. The register of problems and the audit's results are entries of the key `the-way`: `problem_register` (the file) and
     `audit_results` (a directory). Name them in a constant and in the docstring.
  3. The command takes `--locations <file>` (default `~/.the-way/locations.json`), so that tests and checks never read or write
     the user's real file or places.
  4. For a cycle of the-way's own history, whose record says `Process pin: not applicable (the-way itself)`, the version of
     the-way the cycle ran on is the commit in the record's line `Target branch and base`; `unknown` where neither is readable.
  5. No surface entry is written for the command (WAY-49): a user's scheduler relies on its path and arguments, but no pinned
     product does. Do not add one.
  6. A cycle committed more than once (after a correction) counts once, identified by its folder `docs/task-cycles/<task-slug>/`
     and the first commit that adds a copy, with the later commits noted in the result.
- The result file: UTF-8, LF line ends, deterministic (the same input gives the same bytes), written in the audit's results
  directory under a dated name, plus a stable name the skill reads (`latest`). Choose the form so that Slices 4–6 can extend it
  and a person can read it; name it in your report.
- Git is read-only here: only `git log`, `git show`, `git cat-file`, `git rev-parse` and similar, with `GIT_TERMINAL_PROMPT=0`
  and without a pager; never a command that changes a repository (WAY-38's invariant `script-subprocesses` bounds what the
  script may run — read it).
- `stages.md` of an earlier form has no wait column; the value is `unknown`, never zero.
- Tests: crafted input is part of the slice's work — control characters, a record path leaving its directory, a malformed table,
  a missing or doubled field, an unreadable or oddly encoded file, a locations file with a wrong type for an entry.
- The part-map change you make: the part's *Trust boundary* names `process-audit/audit_count.py`; its *Depends on* names every
  part whose file the command imports or reads by path. Write it through the project skill `the-way-update-part-map`.
- The "run on this repository with stdin closed" check: use a temporary locations file that names this worktree as a
  repository and a temporary directory for the results; give the exit code and the first lines of the result.
- Report one more thing: the cache-creation tokens that `cycle_stages.py` folds into *Input* (slice 2's concern) bear on the cost
  of slice 4 only; do nothing about them here.

## Report

Return your status (`done`, `done with concerns`, `questions`, `returned`, `reserved`, `blocked`), your commits, a one-line
check result naming what failed or did not run, the report path, your questions and concerns, each reach beyond this
handoff, **Unread material** (what this handoff names that stayed unread or was read in part, or `none`) and
**Searches not found or unclear** (or `none`), with each check you ran as its command and exit code, and the own-work check
`make-change` requires. Commit your work with `git add <paths>` (never `git add -A`), messages in English.

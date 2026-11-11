# Handoff — executor of slice 1 (`make-change`: "a slice, or the retry of a slice")

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator, and the
orchestrator answers your questions. Nothing here is that person's approval. Your questions go to the
orchestrator, never to the human.

## Where you work

- Worktree (work from its root, read every file from it): `the worktree of the task`, branch `task/weekly-process-audit`.
- Base of this slice (start of its range): `e3825a82386a61930a86f8517fc0c5f422fc2833`; the foundation entries (commit `1adca16`) are the first commits of its range, and your work starts from HEAD `1adca16`.
- The product is the-way itself: methods live in the worktree.
- Method: `task-cycle/change/SKILL.md`; you make "a slice, or the retry of a slice". Read it whole, then `task-cycle/change/slice.md` whole,
  and any other file they name only when the step that names it comes.
- Report path: `docs/task-cycles/weekly-process-audit/reports\slice1_report.md`.

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

WAY-09 foundations/decisions.md:222-306
WAY-40 foundations/decisions.md:1051-1076
WAY-41 foundations/decisions.md:1077-1098
WAY-42 foundations/decisions.md:1099-1122
WAY-44 foundations/decisions.md:1123-1173
WAY-48 foundations/decisions.md:1199-1228
WAY-103 foundations/decisions.md:2316-2337
WAY-320 foundations/decisions.md:10328-10393
WAY-327 foundations/decisions.md:10636-10665
WAY-328 foundations/decisions.md:10666-10689
WAY-330 foundations/decisions.md:10712-10734
WAY-331 foundations/decisions.md:10735-10754
WAY-336 foundations/decisions.md:10841-10865
repository-file-location foundations/invariants.md:26-35
tracked-file-private-paths foundations/invariants.md:86-95
map-reference-target foundations/invariants.md:146-155

## Your slice, word for word from the plan

### Slice 1 — The audit part and the template of its register of problems

- **Goal:** The repository holds the directory `process-audit/` of a new part `process-audit`, with
  the template of the register of problems, `process-audit/problem_register.md`, and the part map
  holds the part's entry, written through the-way's skill `update-part-map`. The template gives, for
  each problem: the cycle record it comes from (the repository and the commit that adds the record's
  copy, as `task-cycle/record_template.md` has the copy committed), the stages that reported it, its
  class, its weight, the issue it belongs to, that issue's fate and, for an issue whose fix is in
  place, the commit of the-way that holds the fix. It carries the starting list of classes
  (confirmation; a check not run or uncertain; an ambiguity settled by an agent's choice; a gap in
  the product's foundation; a known problem left; a stale reference in a task or a plan; a remark
  about the process) and the scale of weight (no problem, Minor, Important, Critical — the cycle
  review's scale with a level zero), in a form that the counting command `process-audit/audit_count.py`
  of later slices reads, a change of the list of classes included, since such a change starts a
  new series (Foundation entries row 10). It says that the user's own tool fills the register, that
  the user adapts the template, that one problem reported by several stages is one problem, and that
  the register lies in the user's place a locations entry names, never in a repository. The part's
  entry: its sentence names what the part answers for — the audit of whether the process gets
  better, cheaper and faster across cycles: the register's template, the price list, the counting
  command and the skill of the weekly session; *Files* `process-audit/**`; *Depends on*
  `task-cycle · project-level` (the form of the cycle record, the reading of a locations entry);
  *Trust boundary* none, since the command it will name does not exist yet (Slice 3 names it). The
  template holds no absolute path, no note link and no name of a person or a product. Name in your
  report the shape the template takes.
- **Change:** `process-audit/problem_register.md` · `foundations/part_map.md`
- **Read:** `.runs/task-cycles/weekly-process-audit/task.md:23-36` To do ·
  `.runs/task-cycles/weekly-process-audit/task.md:38-65` Questions to settle ·
  `.runs/task-cycles/weekly-process-audit/task.md:91-108` Settlements to record · Foundation entries
  row 1 · Foundation entries row 2 · Foundation entries row 4 · Foundation entries row 5 · Foundation
  entries row 10 · Foundation entries WAY-09 changed · `foundations/decisions.md:1044-1165` WAY-40 ·
  WAY-41 · WAY-42 · WAY-44 · `foundations/decisions.md:1192-1220` WAY-48 ·
  `foundations/decisions.md:2309-2329` WAY-103 · `foundations/decisions.md:10321-10384` WAY-320 ·
  `foundations/invariants.md:26-34` repository-file-location · `foundations/invariants.md:86-94`
  tracked-file-private-paths · `foundations/invariants.md:146-154` map-reference-target ·
  `task-cycle/record_template.md`
- **Model:** strongest — it settles the shape of the register that users' tools fill and that
  Slice 5 parses.
- **Risk:** none
- **Checks:** after committing, `python -B elements/common/foundation_check.py` exits 0 ·
  `python -B gate/run_tests.py elements/part-map` ·
  `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` exits 0
- **Depends on:** Foundation entries row 1 · row 2 · row 4 · row 5 · row 10 · WAY-09 changed

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

- Slice 1 is the first slice after the foundation entries (commit `1adca16`, WAY-327…WAY-338 and WAY-09 changed). The
  foundation check reports exactly the references to the part `process-audit` until your part-map entry exists; after it,
  `python -B elements/common/foundation_check.py` must exit 0 — that is your first check to see failing and then passing
  (record both runs).
- Write the part-map entry through the project skill `the-way-update-part-map` (its `SKILL.md` in
  `.claude/skills/the-way-update-part-map/` points to the file under `elements/part-map/`). Its `Depends on` lists only parts
  whose files the directory will import or read; the later slices add what their code needs.
- WAY-09 as changed says what `process-audit/` must hold before it reaches the main branch; your template satisfies the part
  of it that is yours, the rest comes with the later slices of this one request.
- Shape of the register template: the plan leaves it to you; the command of Slice 5 will parse it. Choose a form a script can
  read without ambiguity (a Markdown table with a header row of fixed column names is the form of the other files of the-way
  that scripts read). Name it in your report. The template is a document the user copies and adapts: write what each column
  means and which values it may hold, in English, with no name of a person or a product and no path.
- The new directory contains no test yet; `python -B gate/run_tests.py elements/part-map` checks the part-map entry's form.

## Report

Return your status (`done`, `done with concerns`, `questions`, `returned`, `reserved`, `blocked`), your commits, a one-line
check result naming what failed or did not run, the report path, your questions and concerns, each reach beyond this
handoff, **Unread material** (what this handoff names that stayed unread or was read in part, or `none`) and
**Searches not found or unclear** (or `none`), with each check you ran as its command and exit code, and the own-work check
`make-change` requires. Commit your work with `git add <paths>` (never `git add -A`), messages in English.

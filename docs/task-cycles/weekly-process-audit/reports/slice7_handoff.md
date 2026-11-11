# Handoff — executor of slice 7 (`make-change`: "a slice, or the retry of a slice")

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator, and the
orchestrator answers your questions. Nothing here is that person's approval. Your questions go to the
orchestrator, never to the human.

## Where you work

- Worktree (work from its root, read every file from it): `the worktree of the task`, branch `task/weekly-process-audit`.
- Base of this slice: `2e7168c`. The slices before yours and the foundation entries are in the history before it.
- The product is the-way itself: methods live in the worktree.
- Method: `task-cycle/change/SKILL.md`; you make "a slice, or the retry of a slice". Read it whole, then `task-cycle/change/slice.md` whole,
  and any other file they name only when the step that names it comes.
- Report path: `docs/task-cycles/weekly-process-audit/reports\slice7_report.md`.

## Answers of the start

- Trust boundary: the command of slices 3–6 is one; this slice writes prose and entry points and touches no code of it.
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

WAY-103 foundations/decisions.md:2340-2361
WAY-107 foundations/decisions.md:2441-2478
WAY-113 foundations/decisions.md:2602-2655
WAY-127 foundations/decisions.md:3208-3274
WAY-140 foundations/decisions.md:3874-3924
WAY-256 foundations/decisions.md:7815-7925
WAY-265 foundations/decisions.md:8153-8180
WAY-320 foundations/decisions.md:10420-10485
WAY-329 foundations/decisions.md:10833-10862
WAY-330 foundations/decisions.md:10863-10886
WAY-331 foundations/decisions.md:10887-10908
WAY-335 foundations/decisions.md:10973-10994
WAY-338 foundations/decisions.md:11056-11080
WAY-339 foundations/decisions.md:11081-11100
WAY-340 foundations/decisions.md:11101-11169
tracked-file-private-paths foundations/invariants.md:86-95
skill-entry-points foundations/invariants.md:261-270

## Your slice, word for word from the plan

### Slice 7 — The skill of the weekly audit session

- **Goal:** `process-audit/SKILL.md`, the skill `audit-process`, leads the weekly audit session with
  the human, a session of its own apart from any weekly review (Foundation entries row 12). It finds
  the place of the audit's results and the register through their locations entries as
  `project-level/backlog_place.md` ("Resolve an entry of the locations file") gives, asking the human
  where an entry is missing; reads the latest result of the counting command
  `process-audit/audit_count.py`; shows the human the issues to weigh — what came back after a fix,
  what still waits and for how long, what each process version's measures and three answers show
  within a series — never giving an issue priority from how often it comes back alone (row 7) and
  never comparing two series directly (row 10); and writes the audit's result into the place of the
  audit's results, never into a repository (row 3). It says that the user's own tool fills the
  register from the template, which the user adapts (row 1); that the counting runs unattended on
  the night from Friday to Saturday, started by a system scheduler the human sets up, and that a
  weekly task the human adds to the backlog starts the session (row 12; both are human actions,
  WAY-140); and that no set of frozen earlier tasks is replayed (row 11). It is written for any
  builder who adopts the-way (WAY-103): "the human", no person's name, no absolute path and no note
  link. Each step every use comes to stays in `SKILL.md` (WAY-256). After writing the skill, run
  `python -B agent-instructions/skill_entry_points.py --write`, handle any obsolete output path it
  reports for removal, and commit all of its output; never edit that output by hand. `README.md`
  names `process-audit/` among the repository's directories and among the directories that hold a
  skill.
- **Change:** `process-audit/SKILL.md` · `.claude/skills/the-way-*/SKILL.md` ·
  `.agents/skills/the-way-*/SKILL.md` · `README.md`
- **Read:** `.runs/task-cycles/weekly-process-audit/task.md:17-21` Need ·
  `.runs/task-cycles/weekly-process-audit/task.md:23-36` To do ·
  `.runs/task-cycles/weekly-process-audit/task.md:38-65` Questions to settle ·
  `.runs/task-cycles/weekly-process-audit/task.md:77-80` Human actions ·
  `.runs/task-cycles/weekly-process-audit/task.md:110-112` Out of scope · Foundation entries row 1 ·
  Foundation entries row 2 · Foundation entries row 3 · Foundation entries row 7 · Foundation entries
  row 10 · Foundation entries row 11 · Foundation entries row 12 · `foundations/decisions.md:2309-2329`
  WAY-103 · `foundations/decisions.md:2410-2446` WAY-107 · `foundations/decisions.md:2571-2624` WAY-113 ·
  `foundations/decisions.md:3177-3242`
  WAY-127 · `foundations/decisions.md:3843-3892` WAY-140 · `foundations/decisions.md:7776-7885`
  WAY-256 · `foundations/decisions.md:8114-8140` WAY-265 · `foundations/decisions.md:10321-10384`
  WAY-320 · `foundations/glossary.md:79-83` human action · `foundations/invariants.md:86-94`
  tracked-file-private-paths · `foundations/invariants.md:261-269` skill-entry-points ·
  `foundation-review/SKILL.md` · `project-level/backlog_place.md` · process-audit/audit_count.py
  and process-audit/problem_register.md as Slices 1 to 6 made them
- **Model:** same — it writes a skill of the process that leads a session with the human and has to
  agree with the command's result, the register and the user's places set by Slices 1 to 6.
- **Risk:** none
- **Checks:** `python -B agent-instructions/skill_entry_points.py` lists nothing to create or
  change · `python -B gate/run_tests.py gate` · `python -B gate/run_tests.py agent-instructions` ·
  after committing, `python -B elements/common/foundation_check.py` exits 0 ·
  `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` exits 0
- **Depends on:** Slice 1 · Slice 6 · Foundation entries row 1 · row 2 · row 3 · row 7 · row 10 ·
  row 11 · row 12

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

- Slices 1–6, the correction and the merge of the target branch are made and reviewed (head `2e7168c`). Your slice writes the skill that leads the weekly audit
  session. **Read, whole, before you write:** `process-audit/audit_count.py` (its module docstring: usage, options, exit codes, the entries it reads,
  the result's tables and what `unknown` and `at least n` mean), `process-audit/problem_register.md`, `process-audit/price_list.md`, and the reports of
  the slices that built them (`reports/slice3_report.md`, `reports/slice5_report.md`, `reports/slice5_fix_report.md`, `reports/slice6_report.md`,
  `reports/correction_report.md`). The skill must say what the command really does, not what the plan said: take every option, entry name, table
  and column from the code and run `python -B process-audit/audit_count.py --help` and one run on temporary files to see the result.
- **Writing a skill of the-way:** read `instruction-files/SKILL.md` and, whole, `instruction-files/kind_skill.md` and `instruction-files/writing.md`
  (how a skill is written and what its `description` is), and `foundation-review/SKILL.md` as the nearest existing skill of the same kind (a session with
  the human of one repository's review, that reads a count and writes a result). Do not copy its vocabulary: write the new skill's own words. The
  `description` starts "Use when …" and names the trigger (the weekly audit of the process) in a sentence, as the other skills do.
- **Numbering:** the audit's decisions are WAY-329…WAY-340 (the plan's "row n" = WAY-(328+n)); the plan's text that names a "WAY-3xx" is out of date
  by two. Cite the numbers of the log as it stands.
- **What the skill says (the orchestrator's list; the plan's Goal is binding, and these fill it in):**
  1. The skill is for any builder who adopts the-way (WAY-103): "the human"; no person's name, no absolute path, no note link, no product name.
  2. It finds the places by the locations file as `project-level/backlog_place.md` ("Resolve an entry of the locations file") gives: the entries
     `problem_register` and `audit_results` under `the-way`, and under each product's key `repository`. The command takes `--locations FILE`
     (default `~/.the-way/locations.json`), `--repository KEY` (repeatable), `--prices FILE`, `--today YYYY-MM-DD`; it exits 0 with the result, 1 with the
     result and a repository unread, 2 with an `Error:` line and nothing written. Where an entry is missing, the skill asks the human where it is and
     offers to add it to the locations file (WAY-320, WAY-113: one question, with the options and a recommendation).
  3. The session: run (or read the latest result of) the counting command; read `count-latest.md` in the results place; show the human the matters to
     weigh — what came back after a fix (fixed issues: problems in cycles whose version holds the fix, apart from those without), what still waits and
     for how long (open issues), what each version's measures and three answers show within its series — **material, not ranking**: never a priority from
     how often an issue comes back (WAY-335), never a comparison of two series (WAY-338), unknown stays unknown and `at least n` stays `at least n`.
     Show each matter as the guidance of the user's own rules asks of an agent that puts material before the human: the quoted rows, what follows, one
     question (read the rule in the user's instruction files only if the repository gives one; do not name it).
  4. It writes the audit's result — what the human decided to weigh and the matters it set aside — into the audit's results place as a dated note
     (`audit-<date>.md`) beside the counts, never into a repository (WAY-331).
  5. It says that the user's own tool fills the register from the template and that the user adapts the template (WAY-329); that the counting runs
     unattended on the night from Friday to Saturday, started by a system scheduler the human sets up, and that a weekly task the human adds to the backlog
     starts the session (WAY-340; both are human actions, WAY-140 — the skill names them and does neither); that no set of frozen earlier tasks is
     replayed (WAY-339); and that the share of fix rounds and the other measures give `unknown` for a cycle whose record or stage report is in an
     earlier form (a record's *Review rounds* in the form `task-cycle/record_template.md` gives; `stages.md` with the column *Files named*).
  6. Each step every use comes to stays in `SKILL.md` (WAY-256); a variant's file is named where the step names it (WAY-265). A file beside the skill
     only for what is read in some uses — this skill has no variants, so most likely none.
- **Entry points:** after writing the skill run `python -B agent-instructions/skill_entry_points.py --write`, handle any obsolete output path it
  reports for removal, and commit all of its output (the entry points under `.claude/skills/` and `.agents/skills/`); never edit that output by hand.
  Run `python -B agent-instructions/skill_entry_points.py` (no `--write`) afterwards: it must list nothing to create or change. The installer's
  list of skills (`installation/install.py`) is NOT changed: the audit reads the cycles of several repositories and the history of the-way, not one product
  (plan, *Choices*); if the gate's tests of `installation` or `gate` demand it, return `questions` instead of changing it.
- **README:** `README.md` names `process-audit/` among the repository's directories (line about 121, where `foundation-review/` is described) and among
  the directories that hold a skill (line about 129), in the form of its neighbours; change nothing else in `README.md`.
- **Checks:** `python -B agent-instructions/skill_entry_points.py` lists nothing to create or change; `python -B gate/run_tests.py gate`;
  `python -B gate/run_tests.py agent-instructions`; `python -B gate/run_tests.py installation` (the installer reads the skills of the-way);
  after committing, `python -B elements/common/foundation_check.py` exits 0; `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths`
  exits 0; `python -B instruction-files/check_instructions.py` on the new skill if that script takes a path (read its docstring) with its exit code.
  A skill is prose: the check that shows the skill works is a dry read — read it once as the agent who runs the session would and name in the report
  each step you could not follow from the text alone.

## Report

Return your status (`done`, `done with concerns`, `questions`, `returned`, `reserved`, `blocked`), your commits, a one-line
check result naming what failed or did not run, the report path, your questions and concerns, each reach beyond this
handoff, **Unread material** (what this handoff names that stayed unread or was read in part, or `none`) and
**Searches not found or unclear** (or `none`), with each check you ran as its command and exit code, and the own-work check
`make-change` requires. Commit your work with `git add <paths>` (never `git add -A`), messages in English.

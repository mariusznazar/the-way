# Handoff — the return step (`make-change`: the return step of the planned route; not a slice, not a fix)

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator. Nothing here is that person's approval. Your questions go to the
orchestrator; a question that needs the human comes back as status `blocked`, as `task-cycle/skill/foundation_step.md` gives.

## Where you work

- Worktree (work from its root, read every file from it): `the worktree of the task`, branch `task/weekly-process-audit`,
  HEAD `51cae12`. The range of your commits starts there.
- Method: `task-cycle/change/SKILL.md` whole (you take no row of its table: you are the agent of the return step); `task-cycle/skill/foundation_step.md` whole and
  `task-cycle/skill/return_step.md` whole (what the return step compares and writes); and the project skill of an element when you write an entry of it
  (`the-way-record-decision`, `the-way-record-glossary-term`, `the-way-record-invariant`, `the-way-record-environment-fact`, `the-way-update-part-map`, each
  `SKILL.md` in `.claude/skills/`, which points to the file under `elements/`).
- Report path: `docs/task-cycles/weekly-process-audit/reports\return_step_report.md`.

## Inputs

- The frozen task (whole): `.runs/task-cycles/weekly-process-audit/task.md`; the plan (whole): `.runs/task-cycles/weekly-process-audit/plan.md`. Its decisions are
  numbered two lower than the log now: the audit's decisions are WAY-329…WAY-340 (the plan's "row n" = WAY-(328+n)).
- The change: `git diff 52f8164..HEAD` is what the request will change in `foundations` (`52f8164` is the target branch as merged in; the rest of
  `git diff e3825a8..HEAD` came in from it). Its parts: `process-audit` (new; `process-audit/audit_count.py`, `process-audit/SKILL.md`,
  `process-audit/problem_register.md`, `process-audit/price_list.md`, tests), `task-cycle` (`cycle_stages.py` and its tests, `record_template.md`, one sentence
  of `skill/SKILL.md`), `decisions` (the log), `part-map`, `agent-instructions` (generated entry points), and `README.md`.
- The cycle's slices and reviews are in `.runs/task-cycles/weekly-process-audit/reports/` (slice reports, review reports, `whole_fix_report.md`,
  `review_whole_report.md`, `review_whole_fix_report.md`); read a report only where a comparison needs it.

## What to do

1. **Compare the foundation with the code.** The entries the change writes or changes: WAY-329…WAY-340 (new), WAY-09, the Scope of WAY-38, WAY-89, WAY-320 and
   WAY-328, WAY-336 (edited by the correction); the entries the task names (its *Decisions in play*: WAY-09, WAY-103, WAY-140, WAY-260, WAY-296, WAY-320); the part
   map of `process-audit` and `task-cycle` (its trust boundaries, *Depends on*, *External context*); and the entries a search of the whole foundation finds (WAY-33
   in `elements/common/way_of_working.md`, "2. Search the foundation": the search is yours: entries that name or are named by the audit, the stage report, the
   cycle record's form, the locations file, the price list, the decision on what a request's description holds). Compare each with the files of the repository as
   they stand and correct, in the same change, what no longer matches: the decisions were written before the code and before the correction (the tie of a turn to
   its fix round by the findings file; the series rule; the class list widened by the skill; the trust boundary of `cycle_stages.py`).
2. **Write what the return step writes** (`task-cycle/skill/return_step.md`): an environment fact for each source outside the product that the change rests on and
   the foundation does not hold — decide for the price pages of the providers that `process-audit/price_list.md` cites and for what the stage report reads from
   the transcripts of Claude Code and Codex (the layout of their session files; whether it is already an environment fact: search `foundations/environment_facts.md`)
   — through `the-way-record-environment-fact`; a word the change uses in a meaning for which WAY-95 gives it an entry — the words "issue" (the task's *sprawa*:
   the one matter that like problems of several cycles make) and "series" (a run of consecutive versions of the process between which no measure changed its
   basis) were flagged by the foundation step, the writer of the register template and the reviews — through `the-way-record-glossary-term` (read WAY-95, WAY-97, WAY-99
   and the element's skill to decide whether each word meets the bar; if one does not, say why in the report); a row of *Settlements to record* or a projected entry
   the code makes true that the foundation step missed; and a choice that binds after the merge (WAY-36) — among the cycle's choices the questions table holds, the
   ones that bind later users are: the entries of the locations file the audit reads (`problem_register`, `audit_results`, and `repository` under a product's key),
   the options of the counting command, the form of `Review rounds` in the record, the new column *Files named* of the stage report, the version of the-way given
   to a cycle of its own history, the conservative series rule, the reading of the *Plan* item (one standalone figure before `slices`), the findings file as the
   tie of a turn to its fix round with at least two turns. Decide for each whether it already stands in a decision (then write nothing: say where) or binds later
   work and so needs a decision, as the foundation step's rules give; WAY-327 and WAY-328 of the log are the target branch's and are not yours to change except the
   Scope sentence of WAY-328 that the part adds. An invariant only for a rule the task, a decision or the human sets (the task carries none).
3. **Do not touch** the target branch's files beyond what a comparison finds wrong in the task's own files, the code (only the foundation and the part map; where a
   comparison shows that the code is wrong and the decision right, return that as a finding in your report, do not change code), or the Minor findings the reviews left
   (m4 of the review of the whole change is yours only in the sense of item 2 above). No entry is deferred: one this request does not write is neither proposed nor listed
   for later.
4. The foundation check must report 0 errors after your commits; the part-map tests and `python -B gate/run_tests.py elements/decisions elements/glossary elements/invariants
   elements/environment-facts` (or the directories that hold tests of those elements) must pass; run them as command and exit code, long commands in the background,
   waiting in stretches under four minutes. Do not run the full suite.
5. Commit with `git add <paths>`, messages in English. If you change nothing, say so and commit nothing.

## Report

As `make-change` and `foundation_step.md` give: status (`done`, `done with concerns`, `questions`, `blocked`), commits, a one-line check result, questions, concerns, each
reach beyond this handoff, **Unread material**, **Searches not found or unclear**, the own-work check; for each entry you write or change, one sentence of its meaning in
English and one in the task document's language, marked `row <n>`, `projected` or `the cycle's`; and the headings of the cycle record's *Return step*, one line each:
Foundation compared with code (what no longer matched and its correction, or none); Decisions written or changed; Invariants written or changed; Environment facts;
Glossary terms; Part-map changes; Projected entries written whole or in part; Rows of *Settlements to record* written.

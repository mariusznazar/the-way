# Handoff to the planner

You are the planner of one task cycle of the-way. Work from the worktree root
`the task's worktree` (branch `task/decision-log-second-round`, base `ec7929d`).
The person who requested this cycle has delegated intermediate choices to the orchestrator; nothing you write
is anyone's approval. Write no code and change no tracked file. Your outputs are `plan.md` and `plan-size.md`
in `.runs/task-cycles/decision-log-second-round/` and your report.

## Method and stage

- Method: `task-cycle/plan/SKILL.md` (`plan-task`). Read it whole; read a file it names only when the step
  or variant that names it comes.
- Stage: the plan of slices for a ready task. No spec was written: the task has no open design choice
  (see Answers). The change is made by one executor per slice, one after another, each slice reviewed or
  judged by the review of the whole change as the plan marks.
- Boundary: you return after the plan and its size report; you do not start a slice.

## The frozen task

`.runs/task-cycles/decision-log-second-round/task.md`. Read its first 490 lines whole (the section
"Notatka sprzed doprecyzowania" and below is the material the document came from, not the task). It is in
Polish; its table of assessments, *To do* and *Questions to settle* bind. The text of the rules to write
is quoted there in English where it is to be English.

Answers of step 4: trust boundary — no; irreversible operation — no; no open design choice; route — planned
slices.

Reconciliation of the task with its sources (Q1 in the record): its sections *Decisions in play* and
*Settlements to record* read `TODO` because they waited for the human's acceptance of the table of
assessments. The table is accepted ("Przyjęte przez Mariusza 2026-11-14 w komplecie"): groups A, D, E as
the table says; group B stays in the log; group C leaves the log for the element templates, as group A does;
group F stays. Read the decisions in play as: WAY-293, WAY-19, WAY-02, WAY-100, WAY-90, WAY-27, WAY-29 as the
task names them, and every entry of groups A, C, D, E that leaves the log or becomes a sentence of another
entry. The answers to questions 2 and 3 of *Questions to settle* are the settlements the cycle writes
(the addition to WAY-100 in the exact words the task gives; the rule of `derives from WAY-100`).
The table was made on `foundations` `f4af75d` with 331 entries; the log has grown since (WAY-374, WAY-375
and any later entry): an entry the table does not name stays in the log. Check every identifier of the table
against the log as it stands now, and report any that no longer matches.

## What to read (selected by the orchestrator)

- `elements/common/way_of_working.md`, `elements/common/rules.md` (the withdrawn-identifier rule),
  `elements/decisions/template.md`, `elements/common/skill/read.md`, `elements/common/skill/task_variant.md`,
  `elements/common/foundation_check.py` (what it reports about a reference to an entry that is not in the log).
- `foundations/decisions.md`: the decisions in play above; for the planning of withdrawals, the
  withdrawn-numbers list and how the first round withdrew entries (git log of `foundations/decisions.md`,
  the commits of the merged request #37, `f0b2130`, show the form of a withdrawal).
- `foundations/part_map.md` for the parts the change touches; `foundations/invariants.md` for the invariants
  that `derive from` an entry that leaves the log (for example the invariants named in the table's
  explanations: project-definition-form, instruction-file-imports, cross-part-imports, generated-overview).
- For To do 6: `task-cycle/spec/` (the step that asks about existing code), `foundations/decisions.md` WAY-29.
- Guideline files of the-way's own parts, if the part map names any for the files you plan to change.

## What the plan must cover

Every item of *To do* 1–6, every settlement above, and the following facts of the task:

1. Withdrawing an entry means: it leaves `foundations/decisions.md`, its number goes to the list of
   withdrawn numbers (with a successor where *To do* 3 says), the rule it stated stays in the skill or
   template of the table's "Miejsce" column with one sentence of its reason, and every reference to the
   withdrawn number anywhere in the repository (other entries, invariants, tests, skills, templates,
   comments, scripts) is repointed or removed (WAY-02). `python -B elements/common/foundation_check.py`
   must pass on the result. Decide and write in the plan how references to a withdrawn number in
   tests and invariants are handled and name the files; find them by searching the repository for each
   number (the table has about 150 numbers: use a script outside the repository tracked files, in your
   own `.runs/planner/` directory).
2. For groups A and C the rule must really stand in the "Miejsce" file with its one-sentence reason: where
   the file already states the rule and its reason, nothing is added; where the reason is missing, add one
   sentence. The plan lists, per slice, which files get an added sentence — the planner finds that by
   reading the file for each entry; the table's "Pewność" `m`/`l` marks the entries most worth a check.
   Where the planner finds that an entry marked for withdrawal holds a choice the "Miejsce" file does not
   state and cannot state in one sentence, it does not decide: it lists the entry under a heading
   "Entries to return to the human" and the orchestrator will keep it in the log and say so in the request.
3. *To do* 4: the 23 decisions with `derives from WAY-100` (WAY-121, 128–133, 137–140, 142–144, 146, 147,
   164, 173, 256, 268, 270, 273, 280) and any decision that adopts a practice from outside without the
   relation: each, by the pattern of the addition to WAY-100. Some of these entries are themselves
   withdrawn by the table (for example WAY-128–133 are in group B and stay; WAY-280 is in group B and
   stays; others are in group A); settle the order so no slice edits an entry another slice withdraws, and
   note where an entry that leaves the log makes its *To do* 4 item void. Group B entries stay in the
   log and some are in this list: they get the pattern. The slice with these rewrites reads each such
   decision's *Based on*, *Rationale* and *Rejected* whole. The sources a decision cites are not to be
   invented: the pattern uses what the decision already says; where a decision says nothing of what it
   takes, the plan leaves the sentence as `TODO` for the orchestrator rather than the executor writing
   it from memory — except where the cited source is a file in the repository or a public address the
   decision quotes.
4. *To do* 5 and 6: the addition to WAY-100, the reference from the decisions template, the pointer in
   `read.md`, the recovered-decisions rule of the decisions template and WAY-29, and the question in the
   `task-cycle/spec/` step. These are small slices of their own and come first, since *To do* 4 uses the
   addition to WAY-100.
5. The order of the slices, with the dependencies: rule changes first; then `derives from WAY-100` pattern
   (so the rewritten entries are not withdrawn later); then withdrawals by group, partitioned by the part
   of the "Miejsce" file so that a slice's files are disjoint from the others' (a slice is limited by the
   reading limit of `task-cycle/slice_size.py`; run it as `plan-task` gives).
6. Every withdrawal slice's *Checks* are focused: `foundation_check.py` and the tests of the directories its
   files belong to; none runs the gate (WAY-160).

## Questions

Questions go to the orchestrator in your report. Do not ask the human.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed.
The files that a product's own tools and tests make by themselves are no working copy of the agent
and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a
worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside
its report what the report needs, and states in the report where each copy stood and that it was
removed. Where a removal fails, the agent finishes all the same and names in the report the
remainder, with its full path and the reason it stayed.

Your directory for working copies and scripts: `.runs/planner/`.

## Report

Write your full report to `.runs/task-cycles/decision-log-second-round/reports/planner-report.md`, with the
sections `plan-task` gives, including **Unread material** and **Searches not found or unclear**. Return the
status, the one-line check result, the report path and the plan's path.

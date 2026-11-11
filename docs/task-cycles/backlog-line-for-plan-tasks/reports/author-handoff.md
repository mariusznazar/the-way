# Handoff — the whole change as the one author

You are the one author of a the-way task cycle. The person who requested the cycle has delegated
intermediate choices to the orchestrator, who sends you this; the orchestrator's answers below are
provisional and are not that person's approval. Do not ask the human anything: send questions to
the orchestrator in your report with status `questions`.

## Variant, worktree, method

- Variant of `make-change`: **the whole change as the one author**.
- Work only in the worktree `the task's worktree root`
  (branch `task/backlog-line-for-plan-tasks`, base `52f8164a354ee1a704af0d58add2f3be8e4f0247`).
  Run commands from its root. Never `cd` to the main checkout. This is the-way itself: there is no
  `.the-way` here, the process root is the worktree.
- Method: read `task-cycle/change/SKILL.md` whole, and a file it names only when the step or variant
  that names it comes.
- Foundation step: you write the foundation entries the task carries as
  `task-cycle/skill/foundation_step.md` gives; read it whole. You read the skill of an element when
  you write an entry of that element. You do not take the return step now: the orchestrator resumes
  you for it later with its own handoff.
- No handoff asks you to run the product's gate (`python -B gate/run_tests.py`); the orchestrator
  runs it. Run focused checks of the directories you change, e.g.
  `python -B gate/run_tests.py <directory>`, and
  `python -B elements/common/foundation_check.py` as its own docs give; name each with its command
  and exit code in the report.
- Commits: explicit paths (`git add <path>…`, never `-A`/`.`), English messages, on the task branch.
  Read `agent-instructions/README.md` for the-way's own working rules.

## The task

Read whole the frozen task: `docs/task-cycles/backlog-line-for-plan-tasks/task.md` (original in
the author's private notes; do not quote its path anywhere in a tracked file). It carries
`Status: ready for cycle`, `Project relation: independent`, five *Settlements to record* rows that
settle the decisions you write, and one question carried to the cycle (the `🆔` identifier).
No spec, no plan.

## Answers of the orchestrator

- Trust boundary: no. Irreversible operation: no. The `task-rules` entry in `~/.the-way/locations.json`
  was a human action placed before the cycle and is done; never read it into, or write its path or
  the locations file's content into, any file of the repository (WAY-320).
- Open design choice: none. Reserved choice: none. Route: one author without a plan.
- Q1 — the identifier `🆔`: the task's *Questions carried to cycle* leaves to you how a refiner
  derives it. Its constraints: the form comes from the task place's rules (lower-case letters, digits
  and `-`, unambiguous in the whole place), the task's name in the plan is WAY-147's name
  (unique in the plan only), and the refiner of a dependent task writes `⛔ <id of the other task>`
  before the other task's line exists, so the identifier must be computable from the plan and the
  task's plan name alone. The orchestrator's autonomous choice to start from: the plan's file name
  without extension, joined by `-` to the task's name in the plan, lower-cased, any character outside
  lower-case letters, digits and `-` turned into `-`. Make it, name it in your report as a choice of
  your own with its alternative and cost if wrong, or return `questions` if it does not hold. The
  skill text states the derivation without naming the vault or the rulebook's contents: the form is
  what the task place's rules give, the derivation is the-way's.
- Take the two forms (the status of a new line, the move to ready, the dependency fields) from the
  task place's rules, never from words the-way writes at the product (task settlement row 3). In
  the-way's skills name the rules by the entry `task-rules` under the product's name in the locations
  file, and handle a missing entry or file as `project-level/backlog_place.md` handles a missing
  place; extend that file for `task-rules`.

## What to read (selected by the orchestrator)

Foundation entries by identifier — decisions: WAY-154, WAY-107, WAY-320, WAY-144, WAY-147,
WAY-101, WAY-124, WAY-134, WAY-140, WAY-152, WAY-153, WAY-155, WAY-156, WAY-313, WAY-314, WAY-315,
WAY-328; invariants: `project-plan-form`, `project-plan-state-evidence`, `skill-entry-points`,
`instruction-file-imports`, `foundation-file-kinds`, `return-step-record`,
`tracked-file-private-paths`. Each whole, and further entries they link to as far as the work needs.
Also whole: `foundations/part_map.md` and `foundations/glossary.md`. Parts touched: `decisions`,
`project-level`, `agent-instructions` (and `elements-common` / `glossary` if your search of the
foundation finds entries there to correct). Files named by the task: `project-level/task/skill/orchestrated_mode.md`,
`project-level/task/skill/read_sources.md`, `project-level/task/skill/final_review.md`,
`project-level/lead/skill/SKILL.md` (steps 3.1 and 4), `project-level/lead/conversation_template.md`
("Ownership and turns"), `project-level/backlog_place.md`, and `AGENTS.md` (section `## Backlog`).
Because you edit skills and an instruction file, read `instruction-files/SKILL.md` and follow it for
those edits. The-way has no product guidelines directory; WAY-328 departs from coding and testing
guidelines for the-way's own code, and no part of this task has a user interface.
If you reach a part this list does not cover, name the reach in your report.

## Boundaries

- Do what the task's *To do* items 1–6 and *Settlements to record* rows 1–5 require, no more. The
  *Out of scope* item stands. Do not touch the other agents' prohibitions the task names as out of
  scope (`project-level/lead/answering.md`, `project-level/skill/delegated_mode.md`).
- Edit decisions in place (WAY-07). The decisions you change are WAY-154 (rows 1, 2, 5), WAY-107
  (rows 3, 4) and WAY-320 (the new entry name `task-rules`); WAY-144 stays unchanged, its cost
  accepted in the task. Keep the human-facing meaning sentences and the mark the foundation step
  gives in your report.
- A change that adds, renames or moves a skill or changes its description runs
  `python -B agent-instructions/skill_entry_points.py --write`; none is expected here.
- `AGENTS.md` of the-way: the `## Backlog` section names the `task-rules` entry in place of the
  present sentence about moving the line to Ready (task item 6).
- No absolute path or note link in any tracked file.

## Report

Write your full report to
`docs/task-cycles/backlog-line-for-plan-tasks/reports/author-report.md`
as the method gives it, including **Unread material** (what this handoff names that stayed unread
or was read in part, or `none`), **Searches not found or unclear** (each thing looked for and not
found or unclear, or `none`) and your own-work check. Return status, commits, a one-line check
result naming what failed or did not run, and the report's path.

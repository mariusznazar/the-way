# Dispatch 06 — implementation plan (task cycle step 8)

You are the planner of one the-way task cycle. The orchestrator (the session that sent you) runs the
cycle under Mariusz's delegation; you do not contact Mariusz; questions go back to the orchestrator
in your final message; nothing you or the orchestrator approves is Mariusz's approval.

## Method and boundary

Use Superpowers 6.4.1 `writing-plans`, read in full from
`C:\Users\Mariusz\.claude\plugins\cache\claude-plugins-official\superpowers\6.4.1\skills\writing-plans\SKILL.md`
(and the files it links). Write the plan as
`C:\Storage\repos\the-way-instruction-files-part\.runs\task-cycles\instruction-files-part\plan.md`,
in place of the skill's default location — the only file you write. Your boundary is the finished
plan: stop before execution; do not offer or start an execution mode; do not commit; do not edit the
worktree. You may run experiments only in a scratch clone under
`C:\Users\Mariusz\AppData\Local\Temp\claude\C--Storage-repos-the-way\821bfb3e-7677-4acf-bd0e-ab8a94541c58\scratchpad\plan\`
(e.g. `git clone C:\Storage\repos\the-way-instruction-files-part <scratch>` and work there) to confirm
that commands run and tests are found. Return a report as the text of your final message: the plan's
task list, the commands you confirmed, open questions, deviations from the spec.

## Inputs

- The reviewed spec (binding for this plan): `…\instruction-files-part\spec.md` — revision 3; §14 and
  §15 list the changes made under review. Read it in full.
- Frozen task and run brief: `…\frozen_task.md`, `…\reports\run_brief.md`.
- Reviews the spec answered: `…\reports\report_02_spec_review.md`, `report_04_spec_recheck.md`, and
  the rulings `dispatch_03_spec_revision.md`, `dispatch_05_spec_revision_2.md`.
- Process root (binding rules, element skills, templates, guards): `C:\Storage\repos\the-way-process`
  at 252152a — `task-cycle/skill/SKILL.md` (read the section "Execute, verify and review" and steps
  9–12, so the plan fits them), `agent-instructions/README.md`, the element skills
  `elements/<element>/skill/SKILL.md` and `elements/common/way_of_working.md`.
- Task worktree (where execution will happen): `C:\Storage\repos\the-way-instruction-files-part`,
  branch `task/instruction-files-part` at 252152a. Prototype files: commit af585e3 (branch
  `task/instruction-files`, worktree `C:\Storage\repos\the-way-instruction-files`).
- For form: the PR #8 plan, `git -C C:\Storage\repos\the-way show 27be21e:docs/task-cycles/the-way-skills-in-the-way/plan.md`
  (run with `MSYS_NO_PATHCONV=1` in Git Bash). Follow its shape where it fits; it is not binding.

## What the plan must hold

- A task 0 that the orchestrator runs: the starting-point commit (prototype files from af585e3 into
  `instruction-files/`, `skill/SKILL.md` moved to `SKILL.md`, with the part map entry, as spec §7).
- **The foundation step before dependent code** (WAY-01, WAY-03; task-cycle skill "Before dependent
  implementation"): one brief per element agent, each reading its element's skill from the process
  root, in the order the spec sets (glossary term → facts with watches → decisions incl. WAY-09 edit
  and WAY-127 narrowing → invariants with fingerprint renewals → part map), each with what to write,
  the guard command to run, and what it reports back (fingerprints, guard output, search findings
  under WAY-33). Every new or changed entry's *Approved by* reads `Mariusz, merge of <request link>`.
- **The invariant checks by an agent other than the sentences' author and the code's author**
  (WAY-69): its brief gives only the invariants' sentences and methods, the test template and a test
  file of the same kind as form — never the code's reasoning. These tests are read-only afterwards.
- **Code tasks** for the subagent-driven execution (Superpowers `subagent-driven-development`, with
  `test-driven-development` for behaviour): each a meaningful unit with its files, its failing test
  first, the commands that show red and green, and its focused checks. Cover the check script's four
  fixes, the crafted-input table (spec §4.6), the root-layout change (R18/A20), the skill text, the
  principles and loading account rewrite, the README lines, the Cursor measurement (V1–V5 with the
  negative control, spec §4.4; how the implementer records the result; what is written if it cannot
  run), and the entry points (`python -B agent-instructions/skill_entry_points.py --write`) with the
  flow *Parts* change.
- Where the foundation step and code meet: the order, and what is red in between (e.g. the flow test
  before the entry points exist), stated so a red intermediate result is not misread.
- **The checks of spec §8** as a final task: every command, the expected results including known
  warnings and the known false `WARN` on `AGENTS.md:20`, the by-hand fingerprint recomputation with
  `relation-model/fingerprint.py`, the deliberate breaks of the two invariant tests (run by the code
  reviewer, WAY-69), the second WAY-33 search against the `foundations` tip, the acceptance greps.
- Commits by explicit paths only, never `git add -A`; English commit messages in the repository's
  style (`type(scope): Subject`), each ending with the line
  `Claude-Session: https://claude.ai/code/session_01NcSfTaYPmi5KV9LwkzJLjZ`.
- Exact commands that run in Git Bash on Windows (Python 3.14 is `python`); `MSYS_NO_PATHCONV=1`
  before any `git show <ref>:<path>`.

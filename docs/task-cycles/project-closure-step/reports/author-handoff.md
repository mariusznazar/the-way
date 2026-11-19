# Handoff — the one author of the change (task `project-closure-step`)

## Who delegates and what you do

The orchestrator of the task cycle dispatches you as the one author of one change, without a plan.
The person who requested the cycle has delegated intermediate choices to the orchestrator; no human
is in the loop before the request. Ask the orchestrator, never the human. Any answer it gives is the
orchestrator's choice, never the human's approval.

You make the whole change: the code, the tests, and the foundation entries the task carries (the
foundation step). You return before any review. You do not run the product's gate: its run is the
orchestrator's or CI's. You do run the focused checks of your own work — the tests of the
directories you change (`python -B gate/run_tests.py <directory>`) and the check of the foundation
(`python -B elements/common/foundation_check.py`) — and report each with its command and exit code.

## Worktree and method

- Worktree: `the task's worktree`, branch `task/project-closure-step`,
  base `cb5feab98c697354ae79a8f559b950fbf10d0030`. Work from its root. The-way is here its own
  process: every path below is a path in this worktree. Commit on this branch, adding files by path
  (`git add <path> …`, never `git add -A`, `.` or `commit -a`); commit messages in English; after
  your first commit check the author address with `git log --format='%h %ae'`.
- Method of the stage: `task-cycle/change/SKILL.md` (`make-change`), variant "the whole change as the
  one author". Read that file whole, and a file it names only when the step or variant that names it
  comes. Read `task-cycle/skill/foundation_step.md` whole for the foundation step.
- Your directory for working copies: `.runs/author/`.
- Your report: `.runs/task-cycles/project-closure-step/reports/author-report.md`, as `make-change`
  gives the report (including **Unread material**, **Searches not found or unclear** and the
  own-work check).
- `cycle.md` and the other files of the cycle's record directory — other agents' handoffs, reports and
  findings — are not yours to read unless this handoff names them. It names the frozen task only.

## Working copies (word for word from the cycle's skill)

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed,
except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
says, to the place the product's foundation settles for screenshots, and into the agent's directory
only where no such place is settled. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
`git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed.

## The task

The frozen task, to read whole: `.runs/task-cycles/project-closure-step/task.md` (path in this
worktree). It is written in Polish; its text for the foundation entries stands in English, and your
report keeps one sentence of each entry's meaning in English and one in Polish (the task document's
language), as `foundation_step.md` gives. Its sections: *To do* items 1–7 are the change; *Questions
to settle* hold the answers and what was not chosen; *Settlements to record* rows 1–6 are the
foundation entries; *Decisions in play* names the decisions it touches; *Out of scope* limits it.

Its `Project relation:` is `independent`: there is no project plan and no projected entry to carry.
The task's line in the author's private notes is no concern of yours; you write nothing outside this
worktree. The notes the task names (the plans and notes of `loop2` in the author's vault) are
background in its *Context*; do not read or change them — the closure step you write reads such
files at the user's product, never in this repository. Every behaviour the task requires stands in
its *To do*; if a point there is ambiguous, read *Questions to settle* and the decisions below
before you ask.

## Answers of step 4

- Trust boundary: **yes**. `project-level/plan_check.py` and `project-level/plan_state.py` are trust
  boundary files of the part `project-level` (the plan is a file from outside), and you change both.
  Treat the status line and the table rows as crafted input: a malformed date, a closed plan with a
  row in another state, a `done — goal delivered in task <n>` row pointing at a dropped task, a
  `Status:` line twice, trailing spaces. Say in your own-work check what you tried.
- Irreversible operation: **no**.
- Open design choice: none was found at the start. The choices a spec would hold are settled by the
  task. How to make what the task and the foundation settle — the wording of the step's file, the
  regular expression of the new status, the messages of the scripts — is yours; name each such choice
  in your report. If you meet a choice the task and the foundation do not settle, return `returned`
  with a report and no code (WAY-135).
- Reserved choice: none (no language, framework, library, store of data, way of logging in or place
  to run is needed).
- Checks already failing on the base: none. The base is a merge commit with the tree of its second
  parent, and the merged request's CI run passed in both checks.
- The change does not move the pin and is not a plan member.

## What to read

Foundation entries (read each whole, with its *Rejected*, since the change edits or goes near it):

- Decisions of the task's *Decisions in play*: WAY-142 (the change edits its first sentence in
  place), WAY-145, WAY-146, WAY-118, WAY-153, WAY-107.
- Decisions of the same area the change reaches: WAY-143 (what a plan task ends with), WAY-147 (the
  name of a plan task), WAY-230 (two tasks that realize the same projected entry), WAY-126 (how a
  projected entry enters the foundation: the closure's check of a withdrawn task's entry rests on
  it), WAY-134 (how a task carries what refinement settles: your foundation entries), WAY-140
  (outside the repository), WAY-256 and WAY-265 (where a fragment or the file of a variant of a skill
  stands — the closure step is one such file), WAY-344 (a missing field a script reads), WAY-385
  (size: a function at most 110 lines, a script file at most 1200, counted on formatted code;
  `plan_check.py` is 986 lines and `plan_state.py` 703 — a change that adds to a function or file
  over its threshold begins with a move out), WAY-379, WAY-380, WAY-382 (code discipline).
- Invariants: `project-plan-form`, `project-plan-check`, `project-plan-state-evidence`,
  `project-plan-state-subprocesses`, `project-readiness-check`, `skill-entry-points`,
  `ruff-blocking-rules`, `formatter-layout`, `function-and-file-size`, `script-language`,
  `script-imports`, `script-subprocesses`, `foundation-change-merge-route`, `return-step-record`.
  Row 4 of *Settlements to record* goes to an invariant: find, by the invariants' skill, whether it
  extends `project-plan-check` / `project-plan-form` or stands as a new entry, and keep the test
  that cites it as that skill gives.
- The part map `foundations/part_map.md` (read whole; the part `project-level`) and the glossary
  `foundations/glossary.md` (whole). Select further decisions by the part map's parts with
  `elements/common/decision_index.py` as `elements/common/way_of_working.md`, "Reading the
  foundation", gives, run with the output file in `.runs/author/`.

Guidelines: `guidelines/coding.md` whole, `guidelines/coding-check.md` (the kind of
`plan_check.py`) and `guidelines/coding-measuring-report.md` (the kind of `plan_state.py`), and
`guidelines/testing.md` whole.

Code and files: `project-level/lead/skill/SKILL.md` and its sibling files
(`project-level/lead/skill/*.md`, `project-level/lead/*.md`), `project-level/plan/template.md`,
`project-level/plan_check.py`, `project-level/plan_state.py`, their tests
(`project-level/test_plan_check.py`, `test_plan_state.py`, `test_plan_state_invariant.py`,
`test_plan_state_subprocesses_invariant.py`), `project-level/task_line.md`,
`project-level/backlog_place.md`, `project-level/task/template.md`. Search the repository for every
other reader or writer of the plan's `Status:` line and of the lead skill's closing stop (for
example the plan skill, `task-cycle/skill/plan_member.md`, `process-audit/`, `installation/`,
`agent-instructions/`) and change each one the new state reaches, or say in the report why it needs
no change.

## Boundaries and rules of the repository

- Read `AGENTS.md` and `agent-instructions/README.md` of this worktree first. In particular:
  a change that changes a skill's description (the lead skill's `description` is to change) runs
  `python -B agent-instructions/skill_entry_points.py --write` and commits what it writes; the gate's
  tests report a skill a session would not see.
- The step of closing a project that you write is a file beside the lead skill, read only when the
  step comes (WAY-256, WAY-265): follow those decisions for how the skill points to it. It must say,
  as the task requires: the condition of start, the three places for a withdrawn task, what travels
  with the task, the content of the closure entry, the status `closed YYYY-MM-DD`, the preview before
  any write and the acceptance, and that the definition stays untouched (*To do* 1–7).
- Write only what the task asks. Do not touch the plans, notes or definition of `loop2` and write
  nothing outside this worktree.
- The decision text, the invariant's test, and any wording of the skill and the template that other
  files quote must stay in step: where your change rewords a sentence that a test holds by a line
  `decision:` or `invariant:`, change the test with it.
- Return `returned` with no code if the change proves too large for one agent (report where the size
  lies) or meets an open design choice. Return `blocked` with the question only for a fact or
  permission no source supplies.

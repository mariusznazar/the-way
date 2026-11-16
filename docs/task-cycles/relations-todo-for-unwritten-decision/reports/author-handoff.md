# Handoff — the one author, the whole change

You are the one author (agent type `the-way-author`) of a task cycle of the-way. The person who requested this cycle has delegated intermediate choices to the orchestrator; no answer here is that person's approval.

- Worktree (work only here): the task's worktree, `the task's worktree`, branch `task/relations-todo-for-unwritten-decision`, base `30c947f686b3d304f5a952cb6efe547762cfa247` (target branch `foundations`). Work from the worktree's root; the ignored `.runs/` of that root holds this cycle's files.
- Method: read `task-cycle/change/SKILL.md` whole; your variant is "the whole change as the one author". Read `task-cycle/skill/foundation_step.md` whole for the foundation step (you rewrite two decisions, WAY-71 and WAY-126, with your code), and the files of an element when you write an entry of that element, as `foundation_step.md` gives (`elements/decisions/skill/SKILL.md`, `elements/decisions/template.md`, `elements/common/rules.md`, `elements/common/way_of_working.md`). Read each other file a method names only when its step comes.
- Frozen task: `.runs/task-cycles/relations-todo-for-unwritten-decision/task.md` (read it whole; its *To do* items 1–6, *Questions to settle* with their answers, *Decisions in play* and *Out of scope* bind; *Settlements to record* holds none). No spec, no plan.
- Route: one author without a plan. Stage boundary: make the whole change, commit it, return. You do not run the product's full gate (`python -B gate/run_tests.py` without a directory) — that run is the orchestrator's alone (WAY-160). Run the tests of the directories you change with `python -B gate/run_tests.py <directory>` (`elements/common`, and `task-cycle` for the request template's tests), and the foundation check `python -B elements/common/foundation_check.py`. You do not start the return step; the orchestrator resumes you for it.
- Answers of step 4: trust boundary **no**; irreversible operation **no**; no human action stands in the cycle. Open design choice: none — if you meet one, return `returned` with no code.
- Two corrections of the task's own text that the orchestrator found against the current sources (record them as read, change nothing for them):
  1. The task says the-way has no `guidelines/` directory. It has one now: `guidelines/coding.md`, `guidelines/coding-check.md`, `guidelines/testing.md`. Read those three whole before you change code or a test (`foundation_check.py` is of the kind `check`).
  2. The task's *Decisions in play* names WAY-37 and WAY-32 as entries that stay as they are. Both are withdrawn (table "Withdrawn identifiers" of `foundations/decisions.md`): their rules stand in `elements/common/way_of_working.md` and `elements/decisions/template.md`. They stay unchanged; where your sentence for WAY-126 (To do 5) would point at them, name the file, never the withdrawn identifier.
- Foundation entries to read whole (selected by "Reading the foundation"): WAY-71 and WAY-126 (`foundations/decisions.md`, the entries the task changes — WAY-71's *Rejected* too), WAY-17, WAY-07, WAY-33, WAY-114, WAY-287; the invariants of the parts `elements-common` and `decisions` that your foundation step's search finds; `foundations/part_map.md`. The orchestrator's index of the decisions of the parts `elements-common` and `decisions` stands at `.runs/orchestrator/index.md`; it locates, it does not replace the entries.
- Guideline files to read whole: `guidelines/coding.md`, `guidelines/coding-check.md`, `guidelines/testing.md`.
- Files the task names that you change (read each whole before changing it): `foundations/decisions.md` (WAY-71, WAY-126 only), `elements/common/rules.md`, `elements/decisions/template.md`, `elements/common/foundation_check.py`, `elements/common/test_foundation_check.py`, `task-cycle/skill/request_template.md` (item 16). Search the repository for the places that quote the sentences you change (a search for `TODO` with `Relations`, WAY-71 and the form `TODO — <the decision, and where it is expected>` is the start), and change a test and the sentence it quotes together.
- Report: write your full report to `.runs/task-cycles/relations-todo-for-unwritten-decision/reports/author-report.md` (the name starts with the role), by the report form `task-cycle/change/SKILL.md` gives: status, commits, checks with command and exit code, the own-work check, **Unread material**, **Searches not found or unclear**, working copies. For each new test also say, as the testing guidelines ask, the break it catches and that you saw it failing once. Return its status, commits, a one-line check result and the report path.
- Commit messages in English; `git add` by path, never `git add -A`/`.`/`commit -a`. Do not push.
- Your directory for working copies: `.runs/author/`.

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

# Handoff — the one author

You are the one author of this change in a task cycle of the-way, with no plan and no spec. The
person who requested the cycle has delegated intermediate choices to the orchestrator; no human is
available during the cycle. Where you have a question, return `questions` to the orchestrator; never
seek human approval.

## Where and what

- Worktree (work from its root): `the root of the worktree`
- Branch: `task/weak-point-in-every-decision-question`; target branch `foundations`; base `bfb2e10`
  (the current head of the branch when you start).
- Method: `task-cycle/change/SKILL.md` (`make-change`), variant **the whole change as the one
  author**. Read that `SKILL.md` whole; read a file it names only when the step or variant that names
  the file comes.
- The foundation step: `task-cycle/skill/foundation_step.md` — read it whole. Each decision entry is
  written by `elements/decisions/skill/SKILL.md`, read whole when you write it.
- Stage and boundary: make the whole change with its foundation entries and its own checks, commit,
  and return at its end. The return step, the review and the product's full gate are not yours: the
  orchestrator runs the gate (do not run `python -B gate/run_tests.py` with no directory); focused
  runs of single directories (`python -B gate/run_tests.py <directory>`) and
  `elements/common/foundation_check.py` are yours.
- Frozen task, to be read whole: `.runs/task-cycles/weak-point-in-every-decision-question/task.md`
  (copy of the task document as accepted on 2026-11-15; it is in Polish, the files of the-way are in
  English, so write every file in English as its neighbours are). It settles every choice of the
  change: *To do* 1–7, the answered *Questions to settle* and *Settlements to record* rows 1–8. There
  is no open design choice and no reserved choice; if you find one, return `returned` with no code.
- Answers of step 4 of the cycle: the change touches no trust boundary (the files that the part map
  marks as one, `task-cycle/cycle_stages.py` and `process-audit/audit_count.py`, are not changed) and
  holds no operation that cannot be undone.
- Directory for your working copies: `.runs/author/` (under the worktree's ignored `.runs/`).
- Report path: `.runs/task-cycles/weak-point-in-every-decision-question/reports/author-report.md`.
  Write the report as `task-cycle/change/SKILL.md` gives, with **Unread material**, **Searches not
  found or unclear** and the own-work check.

## What to read

- Foundation entries, by identifier, in `foundations/decisions.md`, each whole with its *Rationale*
  and *Rejected*: **WAY-113** (the decision this change edits in place, WAY-07), **WAY-123**,
  **WAY-100**, **WAY-33**, **WAY-114**, **WAY-120**, **WAY-315**, **WAY-174**, **WAY-155**, and the row
  for WAY-327 in the table "Withdrawn identifiers" of the same file (its rule now stands in
  `task-cycle/skill/request_template.md`). The orchestrator's index of the decisions of the parts the
  change touches, for locating further ones, is `.runs/task-cycles/weak-point-in-every-decision-question/index_work.md`; select your own through
  "Reading the foundation" in `elements/common/way_of_working.md` where the foundation step or your
  method asks you to.
- Parts the change touches: `elements-common`, `project-level`, `task-cycle`, `foundation-review`,
  `process-audit`, `product-guidelines`, and `decisions` for the entry; read their part-map entries
  and the invariants whose *Part* names them or `every`.
- The files *To do* names, each read whole before it is edited: `elements/common/way_of_working.md`,
  `task-cycle/skill/request_template.md`, `process-audit/SKILL.md` and the template of the audit's
  note it names, `project-level/skill/rounds.md`, `elements/common/skill/definition_variant.md`.
- *To do* 4 asks you to search the tracked Markdown files of the whole repository for the places that
  restate what a question of decision gives (ways, cost, recommendation) instead of pointing to "How
  a skill asks" — the listed ones are a start and not complete (`git grep -n` over `*.md`). Decide
  each place yourself by the rule: the text is changed where it restates the rule, left alone where
  it already points to "How a skill asks", and a decision that restates the rule is reconciled
  through the one search of the whole foundation of WAY-33. Name in the report each place you
  changed and each you looked at and left, with the reason.
- Guidelines of the product: the-way holds none for these files; the request template and the
  skills are read as instruction files — `instruction-files/` holds the rules for how instruction
  files are written if you need them.

## Checks to run before you return

- `python -B elements/common/foundation_check.py` from the worktree root (`--skip-test-citations`
  only where the foundation step says it applies), until it passes.
- `python -B task-cycle/request_check.py` has a test directory; run `python -B gate/run_tests.py
  task-cycle`, `... elements`, `... project-level`, `... foundation-review`, `... process-audit`,
  `... product-guidelines` and `... instruction-files` — each directory whose tracked files you
  changed or whose tests read the files you changed — and any other directory a failure points to.
  Record each command and its exit code in the report.
- Commits: one or several on the task branch, English messages, `git add` by path (never `-A`).

## Working copies

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

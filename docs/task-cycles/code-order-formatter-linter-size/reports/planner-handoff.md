# Handoff — planner (stage: plan-task)

## Delegation

The person who requested this cycle has delegated every intermediate choice of it to the orchestrator.
You work for the orchestrator. You never ask the human; questions go back to the orchestrator in your
report, with the ways open and what each costs. Never label an answer as the human's approval.

## Where you work

- The worktree and the process root: `the worktree's root`
  (branch `task/code-order-formatter-linter-size`, base `d69fb20b`). Work from its root. The-way is
  the repository itself: there is no pin and no `.the-way` directory.
- Your directory for working copies: `.runs/planner/` of the worktree (rule below).
- Your plan: `.runs/task-cycles/code-order-formatter-linter-size/plan.md`; the size report
  `.runs/task-cycles/code-order-formatter-linter-size/plan-size.md`; your report:
  `.runs/task-cycles/code-order-formatter-linter-size/reports/planner-report.md`.
- `cycle.md` and the other files of the record directory — other agents' handoffs, reports and
  findings — are not yours to read, except the files this handoff names.

## Your method and stage

- Method: `task-cycle/plan/SKILL.md` of this worktree (`plan-task`). Read it whole; read a file it
  names, one beside it included, only when the step or variant that names the file comes.
- Stage and boundary: you write the plan of the one task below — the foundation entries written before
  any code and the change divided into slices, each made by an agent of its own — and its size
  report, and you return. You write no code, no test and no foundation entry. The orchestrator reviews
  the plan before any slice is made.

## The task

- The frozen task, read whole: `.runs/task-cycles/code-order-formatter-linter-size/task.md`
  (frozen from the task document as it stood on 2026-11-19). Its *Project relation:* is `independent`;
  its *Human actions* are `none`. There is no spec: the cycle found no open design choice, because the
  five rows of its *Settlements to record* carry the entries the change writes and the `.git-blame-ignore-revs`
  line follows from the change with no way left open. The task's *Questions carried to cycle* are
  choices of how to make what the task settles: put each into the slice that meets it, with the ways
  open and your recommendation, under the slice's *Choices*; do not return an open design choice for
  them unless reading the code shows an entry the change needs beyond the five rows.
- Answers of step 4 of the cycle: **a trust boundary is touched** — the change reformats, fixes linter
  faults in and splits files the part map names as trust boundaries (`task-cycle/cycle_stages.py`,
  `task-cycle/cycle_measures.py`, `task-cycle/gate_times.py`, `process-audit/audit_count.py`,
  `process-audit/record_items.py`, `installation/install.py`, `instruction-files/check_instructions.py`,
  `project-level/readiness_check.py`, `project-level/plan_check.py`, `project-level/plan_state.py`); it is
  meant to change no behaviour at a boundary. Mark each slice that touches such a file with the risk
  *trust boundary*; a slice's review then also runs crafted input and compares verdicts, exit codes and
  messages before and after. **No operation that cannot be undone.**
- Known hazard: the one place whose usual linter fix changes behaviour is TRY004 in
  `task-cycle/cycle_stages.py` (`raise ValueError(value)` in a `try` block that catches `ValueError`
  and turns it into a missing-field error; replacing it with `TypeError` would crash the script
  instead of exit code 2). The slice that fixes it names how it keeps the behaviour without turning
  the rule off (WAY-380: a comment that turns a rule off has no effect).
- Hard order the cycle has set: the reformatting stands in a commit of its own with no other change,
  because its hash goes to `.git-blame-ignore-revs`; the splitting of functions and files follows it,
  because the thresholds count formatted code. Decide where the linter fixes and the other items
  stand relative to the reformatting commit, and say why (WAY-205, WAY-51). The one author of a slice
  never changes the reformatting commit, and no slice may make a commit that mixes the reformatting
  with another change.
- The sizes of the code at the base, for cutting: 79 of the 79 `.py` files but one differ from the
  formatter's layout; at line width 100, 11 functions are over 110 lines and 2 files over 1200
  (`process-audit/audit_count.py`, about 3600 lines; `task-cycle/cycle_stages.py`, about 1270). Take
  exact numbers from the commands the method gives, not from these.
- The tool: Ruff 0.17.1 stands at `the Ruff of the quality environment of the main checkout` (the
  main checkout's quality environment; `ruff.toml` of the worktree pins `required-version`).
  The task asks for `ruff format` with line width 100 and the other settings default, for `.py`
  files only.

## What you read, by identifier and path

Foundation (read each whole, as the method says; the index of the decisions in play is at
`.runs/orchestrator/index.md` of the worktree, binding sentences and *Scope* only):

- Decisions: WAY-382, WAY-385 (the task changes both), WAY-379, WAY-380, WAY-381, WAY-205, WAY-51,
  WAY-16, WAY-08, WAY-03, WAY-233, WAY-95, WAY-145, WAY-350 — in `foundations/decisions.md`; also
  WAY-135, WAY-136, WAY-229 and WAY-160 of the cycle's own decisions, as the method needs them.
- Invariants in `foundations/invariants.md`: `ruff-blocking-rules`, `function-and-file-size`,
  `map-reference-target`, `test-method-citation`, `gate-times-refuses-impossible-entry`,
  `cross-part-imports`, `script-language`, `script-imports`, `repository-file-location`,
  `derived-file-content`.
- Part map `foundations/part_map.md` (whole; it is short). Glossary `foundations/glossary.md`
  (whole; the entry `entry` matters for item 8). Environment facts `foundations/environment_facts.md`
  and the fact `ruff-default-rules`, where it stands.
- Guidelines, each whole: `guidelines/coding.md`, `guidelines/testing.md`, and the kind files
  `guidelines/coding-check.md`, `guidelines/coding-shared-module.md` and
  `guidelines/coding-measuring-report.md`, which the splitting of `process-audit/audit_count.py` and
  `task-cycle/cycle_stages.py` and the foundation test concern; `product-guidelines/coding/template.md`
  (the rule *Formatter*) and `product-guidelines/reading.md`.
- Elements for the entries: `elements/common/way_of_working.md`, `elements/common/rules.md`,
  `elements/decisions/template.md`, `elements/invariants/template.md`, `elements/glossary/template.md`
  and their `SKILL.md`.
- Files: `agent-instructions/test_linter_invariant.py`, `agent-instructions/test_size_invariant.py`,
  `agent-instructions/README.md` (section "Installing the linter"; the paragraph that opens "Two
  invariants of the foundation of the-way"), `elements/common/test_foundation_check.py`,
  `elements/common/foundation_check.py`, `task-cycle/test_remove_merged_worktrees.py`,
  `task-cycle/remove_merged_worktrees.py`, `installation/README.md`, `ruff.toml`.

Reach beyond this selectively, as the method says, and name each reach in your report.

## What to put in the plan beyond the method's own content

- Each slice's *Read*: decisions by identifier, invariants by identifier, guideline files whole and
  the passages of the task (word for word as the method gives).
- Cover every item of *To do* 1–8, both acceptance criteria and every row of *Settlements to record*
  (rows 1–5), and say where each lands.
- The plan's *Foundation entries* — which decisions and invariants change or are written, the new
  invariant of the formatter and the new invariant of the full check of the foundation — placed as
  the method says. Decisions 382 and 385 are changed in place (WAY-07); the number of any new decision
  is the next free one.
- Checks of a slice are focused checks that can run (`python -B gate/run_tests.py <directory>`, a
  script, `ruff check`, `ruff format --check`), never a run of the full gate: no handoff tells an
  agent to run the product's gate; its run is the orchestrator's or CI's.
- Where a slice would put an expected failure on or take it off a test, say which tests and which
  invariants it concerns (WAY-51, WAY-233).
- **Model of each slice**: say `cheaper`, `same` or `strongest` with a reason for any other than
  `cheaper`. The strongest model the session allows is Opus.
- The part map's `repository` files gain `/.git-blame-ignore-revs`; the commit that adds the file holds
  the hash of the reformatting commit, which is known only after that commit; plan for the
  ordering (the file's commit comes after, and the orchestrator checks the hash against `git log`).

## Working copies (word for word)

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

Your directory is `.runs/planner/`.

## Your return

Return: your status (`done`, `done with concerns`, `questions`, `returned` or `reserved`), your commits
(none expected: you write only the plan and its size report, which are ignored files), a one-line
check result (the size script's command and exit code), and the report's path. The report holds your
**Unread material** (what this handoff names that stayed unread or was read in part, or `none`),
**Searches not found or unclear** (each thing looked for and not found or unclear, or `none`), your
reaches beyond this handoff, and your working copies.

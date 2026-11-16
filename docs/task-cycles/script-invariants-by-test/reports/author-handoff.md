# Handoff — the one author

## Delegation

The person who requested this cycle delegated the intermediate choices to the orchestrator of the
cycle. Your go-aheads are the orchestrator's, never the human's approval. Ask no human anything: send
a question back to the orchestrator in your report with the status `questions`, `blocked` or
`returned` as your method gives them.

## Where and what

- Worktree: `the root of the task's worktree`, branch `task/script-invariants-by-test`,
  base `604907c88d9973ccf2dbf697e3ce7e1f358fa81c`. Work from the worktree's root; commit on this branch only.
  Commit by explicit path (`git add <file> <file>`), never `git add -A`, `git add .` or `git commit -a`;
  write commit messages in English.
- This is the-way itself: the-way is the repository you change, and the process root is the worktree.
- Method of your stage: `task-cycle/change/SKILL.md`, read whole. Your variant, in the words of its row:
  "the whole change as the one author". Read a file the method names, one beside it included, only
  when the step or variant that names it comes.
- Foundation step: `task-cycle/skill/foundation_step.md`, read whole; the `SKILL.md` of an element
  (`elements/invariants/skill/SKILL.md` for the entries of `foundations/invariants.md`) when you write
  an entry of it. A skill that a file names by its name alone is the `SKILL.md` whose frontmatter
  `name:` is that name; you have no skill tool and read it as a file.
- Frozen task, read whole: `docs/task-cycles/script-invariants-by-test/task.md` (the task document
  as it stood when the cycle began; approved settlements dated 2026-11-14). There is no spec and no
  plan: the task leaves no open design choice and the change fits one agent.
- Stage and boundary: you make the whole change — the four tests, the four edits of `foundations/invariants.md`,
  and what the foundation step gives — commit it, return to the orchestrator before any review, and wait
  to be resumed for a fix and for the return step.
- The directory of your working copies: `.runs/author/` of the worktree.
- Your report: `docs/task-cycles/script-invariants-by-test/reports/author-report.md`.
- `cycle.md` and the other files of `docs/task-cycles/script-invariants-by-test/` — other agents'
  handoffs, reports and findings — are not yours to read unless this handoff names them.
- You do not run the product's full gate. Run the focused checks of the directories you change as
  `python -B gate/run_tests.py <directory>`, and `python -B elements/common/foundation_check.py` on the
  finished change (without `--skip-test-citations`). The full gate is the orchestrator's alone (WAY-160).

## Answers of the orchestrator at start

- Trust boundary: no. Irreversible operation: no. Open design choice: none. Reserved choice: none.
- Your class: `same` (the orchestrator's own), because the test of `script-imports` reuses the reach of
  the import reader of `elements/part-map/test_cross_part_imports.py` and each of the four tests must be
  seen failing once (WAY-08).
- The orchestrator's judgment on the walk through the running product (`task-cycle/change/walkthrough.md`):
  the change writes tests and foundation entries and alters nothing a user sees in a running product.
  State your own judgment in the report as the method gives it.
- Question Q1 (the orchestrator's autonomous choice): the task's *Decisions in play* names WAY-328, which the
  log on this base lists as withdrawn (the coding guidelines and the testing guidelines of the-way are written;
  successors WAY-379 and WAY-392). The task need not wait for guidelines and you follow them.
- Question Q2 (the orchestrator's autonomous choice): the task's *Context* says git tracks only `.md`, `.py`,
  `.gitignore`, `.gitattributes` and `.python-version`. On this base git also tracks
  `.github/workflows/tests.yml`, `requirements-quality.in`, `requirements-quality.txt` and `ruff.toml`.
  Row 1 of *Settlements to record* decides it: the test reports a file of a kind outside the list, and the
  author of the change adds a kind that is no script to the list in the test, with a comment giving the reason.
  Add these four kinds that way, and state in your report, for each, why it is no script. Where you hold
  one of them to be a script, return that as a question.
- The test names: a change that alters an invariant test names it in its request (WAY-03); give the
  names of each test you write or change in your report.

## What you read, by the orchestrator's selection

Foundation entries, by identifier (read each decision whole, from its heading to the next heading, with its
rationale; entries in `foundations/decisions.md`, `foundations/invariants.md`, `foundations/environment_facts.md`,
`foundations/glossary.md`, `foundations/part_map.md`):

- Decisions the task names: WAY-38, WAY-89, WAY-09, WAY-08, WAY-61 (WAY-328 is withdrawn: Q1).
- Decisions that bear on the invariants, their tests and the files: WAY-03, WAY-44, WAY-60, WAY-62, WAY-63,
  WAY-69, WAY-321, WAY-344.
- Decisions that adopt the guidelines for the-way's own code and tests: WAY-379, WAY-385, WAY-392, WAY-393,
  WAY-394, WAY-395, WAY-399, WAY-401.
- Invariants: `python-version-declared`, `script-language`, `script-imports`, `element-directory-contents`,
  `cross-part-imports`, and each other invariant whose *Part* reads `every` or names a part you touch.
- Environment facts: `python-stdlib-modules`, `git-path-patterns`.
- Glossary: the terms `repository test`, `files test` and the terms your tests use.
- The part map, whole (`foundations/part_map.md`): the part a test file belongs to, and the parts a file may import
  from, follow from it. A test belongs to the part it tests (WAY-44); where it stands is your choice, within
  that and within `cross-part-imports`, and you name it and its reason in the report.

Guidelines of the parts you touch, each whole: `guidelines/coding.md` and `guidelines/testing.md`. A file
`guidelines/coding-<kind>.md` only where the kind of code you add matches its row (for example `shared-module`
where you factor out a module other scripts import).

The elements' templates, `elements/common/rules.md` and `elements/common/way_of_working.md` are read as the
element's skill gives it for the entry you write.

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

## What the report holds

As `task-cycle/change/SKILL.md` gives it, with the status line, commits, each check with its command and exit
code, the own-work check (WAY-164), **Unread material** and **Searches not found or unclear** (each `none`
where nothing), reaches beyond this handoff's selection, and the working copies line. Besides: the part you put
each test file in and why; for each of the four tests, the failing run you saw (the behaviour you broke for a moment,
the command and the output's line that shows red) and the passing run after; for each kind you added to the
list of `script-language`, why it is no script; the tests you wrote by name; and, for each row of
*Settlements to record*, the place where it is written.

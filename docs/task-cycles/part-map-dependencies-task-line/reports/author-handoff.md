# Handoff — the one author of the change

## Delegation

The person who requested this cycle delegated the intermediate choices of the cycle to the
orchestrator. Nothing here is that person's approval; the person reviews the request. Do not ask
the human anything: return `questions` to the orchestrator, which answers from the task, its
sources, the foundation and the code.

## Where you work

- Worktree: `the root of the task's worktree`, branch
  `task/part-map-dependencies-task-line`, base `c2541ed6ef1aca0e5509cc9a929f377d97a108bc`. Work
  from its root. Commit on this branch only, with `git add <path>…` by path, never `git add -A`.
  Commit messages are in English, in the style of `git log`.
- Your directory for working copies: `.runs/author/` of the worktree.
- Your full report: `docs/task-cycles/part-map-dependencies-task-line/reports/author-report.md`.
- the-way is the top-level repository here; there is no pinned the-way and no `.the-way`. Read
  `agent-instructions/README.md` (the way of working on the-way before `main`) and the root
  `AGENTS.md`.

## Method and stage

- Method: `task-cycle/change/SKILL.md` (`make-change`), variant "the whole change as the one
  author". Read that `SKILL.md` whole, and a file it names, one beside it included, only when the
  step or variant that names the file comes.
- Stage and boundary: make the whole change the task requires, the foundation entries it carries
  with the code they go with, in one author's work; take the own-work check; commit; return with the
  report. No plan, no spec exists. You do not run the product's gate (`python -B gate/run_tests.py`
  with no directory): the orchestrator runs it. Run the focused checks of the directories you
  change (`python -B gate/run_tests.py <directory>`) and `python -B elements/common/foundation_check.py`
  as `elements/common/way_of_working.md` step 4 gives it. You do not take the return step, which
  follows as a separate stage when you are resumed for it, and you do not open the request.
- Foundation step: read `task-cycle/skill/foundation_step.md` whole for the entries the task
  carries; it names the `SKILL.md` of an element, which you read whole when you write an entry of
  that element (the decisions template and skill for WAY-107, the invariants template and skill for
  the four invariants, the glossary's, the part map's).

## The task

- Frozen task, read it whole: `docs/task-cycles/part-map-dependencies-task-line/task.md` (the
  author's note in Polish; it is the task document, approved with its settlements accepted
  2026-11-15; its *Project relation* is `independent`). Everything the foundation and the code
  hold is written in English: write the entries, the code and the comments in English; the lines
  the code prints or matches stay as the code already has them.
- Its seven items of *To do* are your change. *Settlements to record* rows 1–7 are the entries or
  sentences you write; each row's "Goes to" says where. A row's settlement is settled: write it, do
  not re-decide it. *Questions carried to cycle* are yours to settle in the making: the wording of
  the glossary entry, of the four invariants, of the changed sentence of WAY-107 with its
  *Verification* and *Rationale*, and of the two sentences of the `project-level` part; and how each
  of the four tests finds the writing side (a literal text in a file, a path git tracks, a pattern of
  a tag) and to which part each test belongs (a test belongs to the part it tests, WAY-44; name your
  choice and its reason in the report).
- Answers of the cycle's start (step 4): the change touches no trust boundary (the files the part
  map names as one are not to change; where one does after all, name it in the report); it holds no
  operation that cannot be undone; no open design choice stands; no reserved choice; one author
  without a plan, class `same`.
- Checks failing before the change: none (the base's tree equals that of the merge's second parent,
  whose final gate passed; one timing test of the `gate` directory,
  `test_by_default_every_directory_runs_at_the_same_time`, is known to be flaky).
- No product guidelines (`guidelines/`) stand in this repository; there is nothing to read of that
  kind.

## What to read of the foundation (selected by the orchestrator, WAY-150)

- The index of the decisions the change reaches, written for you:
  `.runs/orchestrator/index.md` — 36 decisions in full, the rest by heading. Open whole only those
  the work changes or goes against or whose binding sentences leave open what to do: of the task's
  *Decisions in play* WAY-107 (the one the task changes — read its *Verification*, *Rationale*,
  *Rejected* and every field), WAY-225, WAY-51, WAY-11, WAY-44, WAY-95, WAY-293, WAY-300 and
  WAY-339; WAY-07, WAY-12, WAY-22, WAY-97 and WAY-99 and WAY-314 by their binding sentences, and
  each decision that a test you alter holds by a line `decision:` (WAY-02, WAY-150). The task names
  WAY-329 (withdrawn, no longer a decision of the log; see the table of withdrawn numbers in
  `foundations/decisions.md`) and a review of the foundation of 2026-11-14 (a private note; its
  P26 and P6 are carried by the task's text, you need not and cannot open it).
- The part map whole (`foundations/part_map.md`), the glossary whole (`foundations/glossary.md`),
  the invariants whole (`foundations/invariants.md`), in particular `cross-part-imports`,
  `map-reference-target`, `test-method-citation`, `derived-file-content` and
  `project-plan-state-evidence`; the templates and rules the skills name.
- The code the task names: `elements/part-map/test_cross_part_imports.py`,
  `project-level/plan_state.py` and its test, `process-audit/audit_count.py` and its test,
  `task-cycle/review_reminder.py` and its test, `elements/common/foundation_check.py`,
  `foundation-review/SKILL.md`, `product-guidelines/template.md`, `task-cycle/skill/reserved_return.md`,
  `task-cycle/skill/blocked_finding.md`, `elements/part-map/template.md`.
- The task's *Context* lists where each of the ten reaches stands; it was checked on `21ecb62` and
  the base is later, so check each against the files before you rely on it, and where one differs
  name the difference in the report.

## Rules that bind this change and that the task alone does not say

- The part map says which dependency is allowed; the test `cross-part-imports` holds Python imports
  to it. A test you write must itself import only what its part's *Depends on* allows after the
  change to the map (a test may import a helper of a part of test helpers). A test that reads the
  *writing* side of a dependency reads it as text or through git, not by importing it, unless the
  part's *Depends on* allows the import.
- An invariant whose method is `test` is cited by a comment line `invariant: <identifier>` in a file
  git tracks other than Markdown (`test-method-citation`); a test that holds a sentence of a
  decision carries a line `decision:` (WAY-12). An invariant's test is seen failing once, then
  passing, as WAY-08 and `make-change` give; report both runs with their commands and exit codes.
  No invariant gets `Violated: yes` (WAY-51).
- WAY-107 is changed in place (WAY-07); its *Verification* and *Rationale* must agree with the
  new sentence. Where the change makes another foundation entry say something false, correct it in
  the same change, as `agent-instructions/README.md` ("Make the change") and
  `elements/common/way_of_working.md` step 2 give; a finding you cannot settle by correcting an
  entry goes back to the orchestrator in your report.
- The check of the foundation must end with 0 errors; run
  `python -B elements/common/foundation_check.py` without `--skip-test-citations` once the tests
  are written. A new part-map dependency must not make `elements/part-map/test_cross_part_imports.py`
  or any other test fail.
- The glossary term needs the word's meaning to differ from what a reader who knows the field takes
  it to mean (WAY-95); search the English text of the tracked files for the word you choose and
  rewrite each use whose meaning moves (WAY-97, WAY-99); the glossary entry's *Not* lists what the
  word no longer carries elsewhere.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed.

## Report

Write the full report to the path above, as `task-cycle/change/SKILL.md` gives it, and return its
status, your commits, a one-line check result naming what failed or did not run, and the report's
path. The report holds the own-work check, each check with its command and exit code, **Unread
material** (what this handoff names that stayed unread or was read in part, or `none`), **Searches
not found or unclear** (each thing you looked for and did not find or found unclear, or `none`) and
your working copies.

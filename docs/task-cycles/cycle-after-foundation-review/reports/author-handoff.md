# Handoff — the one author, whole change

You are the one author of this change, dispatched by the orchestrator of the task cycle of the-way.
The person who requested the cycle has delegated the intermediate choices to the orchestrator; no
answer of yours or of the orchestrator is that person's approval. You make the whole change: its
text, its foundation entries and their checks. You do not run the product's gate (the orchestrator
does), you do not open a request and you do not review your own work as a reviewer would.

## Where you work

- Worktree (your working directory, the root of the repository): `.`,
  branch `task/cycle-after-foundation-review`, base `739c8139bc7f2e74ef0f4c2f0a76a4352614cfd6`
  (the head of `foundations`). Commit on this branch, by path (`git add <file> <file>`, never
  `git add -A` or `git add .`); commit messages in English, imperative, as the repository's
  history does. The record directory `.runs/task-cycles/cycle-after-foundation-review/` is ignored
  by git and is the orchestrator's; read the files named below and write only your report there.
- Method: read `task-cycle/change/SKILL.md` whole. Your variant is, in the words of its row:
  **"the whole change as the one author"**. Read a file that skill names only when the step that
  names it comes.
- The foundation step: read `task-cycle/skill/foundation_step.md` whole when you write or change a
  foundation entry (the decisions of this change), and the `SKILL.md` of an element at the path it
  gives when you write an entry of that element. This is the one place the change writes entries: it
  edits six existing decisions in place.
- The frozen task: `.runs/task-cycles/cycle-after-foundation-review/task.md`, read whole. It is a
  `ready for cycle` task, independent of any project. Its *To do* items 1–11 are the change; its
  *Settlements to record* (7 rows, accepted 2026-11-15) and *Questions to settle* settle every
  choice. Do not widen the task; do not make a choice the task settles another way.
- No spec and no plan exist: the task leaves no open design choice, and the change fits one
  agent.
- Agent directory for working copies: `.runs/author/` (see "Working copies" below).
- Report path: `.runs/task-cycles/cycle-after-foundation-review/reports/author-report.md`.

## The two questions of the start (answers of the orchestrator)

- The change touches no trust boundary (no file the part map names as one).
- The change holds no operation that cannot be undone: it words rules about a script that removes
  directories; it does not change or run that script (`task-cycle/remove_merged_worktrees.py`). You
  run it never.

## What to read

Foundation entries, each whole (a decision from its `###` heading to the next heading of any level, a
file of the other foundation files from its `##` heading to the next `##`):

- The decisions the task names in *Decisions in play*: WAY-13, WAY-25, WAY-375, WAY-376, WAY-261,
  WAY-243 and WAY-289, in `foundations/decisions.md`. Each has a `Relations`, `Based on` or
  `Verification` that links further decisions; read those the change needs, in particular those
  WAY-375 derives from (WAY-140, WAY-153, WAY-373), WAY-300 and WAY-233, which WAY-261 and WAY-243 name,
  and WAY-148 where the request template's wording of a correction names it.
- The part map, `foundations/part_map.md`: the parts of the files you change are `decisions`
  (`foundations/decisions.md`), `task-cycle` (`task-cycle/skill/SKILL.md`,
  `task-cycle/skill/correction.md`, `task-cycle/skill/request_template.md`) and
  `agent-instructions` (`agent-instructions/README.md`).
- The invariants whose *Part* names `every`, `decisions`, `task-cycle` or `agent-instructions`, in
  `foundations/invariants.md`, as "Reading the foundation" step 3 in
  `elements/common/way_of_working.md` gives; those that bear on your files in particular:
  `foundation-file-kinds`, `foundation-change-merge-route`, `derived-file-content`,
  `tracked-file-private-paths`, `skill-rule-source`, `return-step-record`,
  `blocked-request-wording`, `blocked-request-label`, `review-tag-pattern`, `test-method-citation`.
- The glossary, `foundations/glossary.md` (short; read whole). The entry *human action* stays as
  it is; do not edit the glossary for it.
- The decisions template and skill for the element you edit: `elements/decisions/template.md`,
  `elements/decisions/skill/SKILL.md`, `elements/common/rules.md`, and
  `elements/common/way_of_working.md`, as `task-cycle/skill/foundation_step.md` directs.
- This repository has no `guidelines/` directory: no product guidelines apply to it.
- `agent-instructions/README.md` (the integration route of the-way while it has no `main`), whole.

Every file you change, whole, before you change it. A file the dispatch did not name that you
reach, name in your report as a reach.

## The change

The eleven items of the frozen task's *To do*, as the task words them. Where they say "Zapisać w
WAY-375 `narrows WAY-13` w *Relations* i w zdaniu wiążącym obszar", WAY-25 gives the form: the one
that prevails names the other in *Relations* as `narrows`, and its binding sentences state the area
where it prevails. The area the task names is: removing the cycle's own, merged directories.

Notes the orchestrator adds, none of which changes the task:

- Items 1–4 edit WAY-375 and WAY-376 in place (WAY-07: edit an existing decision in place); item 5
  edits the *Verification* of WAY-13; item 6 the decision WAY-261 and the paragraph of
  `task-cycle/skill/SKILL.md` it names (step 10 of the skill); items 7–11 edit the files the task
  names. WAY-243, the testing template and the glossary stay unchanged.
- A test may hold the sentence of a decision by a line `decision: WAY-nn`, or hold a wording an
  invariant states; where you reword a binding sentence, find such a test (the search the foundation
  step gives, and `elements/common/foundation_check.py` lists the invariants that read `test`
  whose sentence a change rewords while no file citing them changes) and keep it true. Run
  `python -B elements/common/foundation_check.py` from the root of the worktree; the full run,
  without `--skip-test-citations`, when the change is made.
- Lines of `foundations/decisions.md` and of the skill files stay within 100 columns, as the
  history's last commits keep them (rewrap a line you lengthen).
- No absolute path to a place on a disk and no note link in double square brackets goes into a file
  of the repository; `task-cycle/private_paths_check.py` checks the tracked files.
- Do not run `python -B gate/run_tests.py` without a directory: the whole gate is the
  orchestrator's run. Run the tests of one directory (`python -B gate/run_tests.py <directory>`)
  for the directories your change reaches: at least `elements/common`, `task-cycle`,
  `agent-instructions` and `process-audit`, and `installation` only if a file it checks changes.
  Run `python -B agent-instructions/skill_entry_points.py` only if a description of a skill
  changes (the task changes none).
- Do the foundation step with the code, as `task-cycle/skill/foundation_step.md` gives, and report
  each foundation entry you write or change with its meaning sentence and its mark.

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

Your directory is `.runs/author/`.

## What you return

Return before any review, with: status (`done`, `done with concerns`, `questions`, `returned`,
`reserved` or `blocked`), your commits, a one-line check result naming what failed or did not run,
and the path of your report. In the report, as `task-cycle/change/SKILL.md` gives: the checks with
their commands and exit codes, the own-work check, your reaches, **Unread material** (what this
handoff names that stayed unread or was read in part, or `none`) and **Searches not found or
unclear** (each thing you looked for and did not find or found unclear, or `none`), and your working
copies. Commit your work before you return; leave the worktree clean.

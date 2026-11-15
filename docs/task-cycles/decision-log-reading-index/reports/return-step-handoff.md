# Handoff: the return step, task `decision-log-reading-index`

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator; no answer it
gives is the human's approval. You never ask the human. The cycle has one human contact, the request.

## What you do

- Worktree (your working directory): `the task's worktree`, branch
  `task/decision-log-reading-index`, head `e82cbab6ea2d63939f85c9dcb6edbd74e6df517b`, base
  `21ecb627f885de438e2209d7ff5c137b1e1b9d83`. Nobody else writes in this worktree while you work.
- Your stage: the return step. Read `task-cycle/skill/return_step.md` whole, and `task-cycle/skill/foundation_step.md` whole
  (the return step writes as the foundation step writes); read `task-cycle/change/SKILL.md` whole for how a change is
  committed and reported (your dispatch takes none of its variant rows); for an entry you write or correct follow the `SKILL.md`
  of its element by the path `foundation_step.md` gives (read as files; the cycle's types have no skill tool).
- The change you compare: the range `21ecb62..e82cbab` (`git diff 21ecb62..e82cbab`): the foundation entries of the plan
  (WAY-150, WAY-18, WAY-21, WAY-287, WAY-339 edited in place; the log divided into 28 topical sections), five slices (the
  index script `elements/common/decision_index.py`, the comparison script `elements/common/compare_log_entries.py`, the reading
  rule and the template, the reviewer/report/request-template wording, the measure in `task-cycle/cycle_measures.py`) and two
  fix rounds. Their reports are in `.runs/task-cycles/decision-log-reading-index/reports/` (`foundation-entries-report.md`,
  `executor-1-report.md` … `executor-5-report.md`, `fix-whole-report.md`).
- The frozen task: `.runs/task-cycles/decision-log-reading-index/task.md`, read whole; its *Decisions in play*, its 7 rows of
  *Settlements to record* and its *Out of scope* bind. The plan: `.runs/task-cycles/decision-log-reading-index/plan.md`.
- Rows written, for your report: rows 1, 2, 3, 5 and 6 are sentences of WAY-150; row 4 a sentence of WAY-18; row 7 a sentence of
  WAY-339 (the successor of the withdrawn WAY-347). The orchestrator checked these at the plan's review; verify them again
  by comparing each row with the entry as it stands.
- Compare the foundation entries the change edits, those the task names (*Decisions in play*: WAY-150, 18, 21, 326, 347, 05, 12, 02,
  52, 33 — 326 and 347 are withdrawn; their rules stand in `task-cycle/skill/SKILL.md` and in WAY-339), those the search of the foundation
  found, and the part map's entries of `decisions`, `elements-common` and `task-cycle` with the files, as `return_step.md` gives;
  correct in the same change whatever no longer matches. Pay particular attention to: the part map's descriptions of what the parts
  answer for and their files (two new scripts in `elements/common/`); `foundations/glossary.md` for a word the change uses in a meaning
  its entry does not give (for example "index", "topical section"); the `Withdrawn identifiers` table; and any other file that still
  says the log has no topical sections or that a reader reads by title.
- You write no code. Commit your work, if any, by `git add <paths>`, messages in English, imperative; commit nothing where nothing
  has to change. Do not run the product's full gate (the orchestrator runs it on the tree you leave); run
  `python -B elements/common/foundation_check.py` after any change.
- Report: `.runs/task-cycles/decision-log-reading-index/reports/return-step-report.md`, a file at that exact path, as `return_step.md`
  gives it, with **Unread material** and **Searches not found or unclear**, the working copies line and the lists the record's
  *Return step* needs: foundation compared with code; decisions, invariants, environment facts, glossary terms, part-map changes and
  projected entries written or changed; rows of *Settlements to record* written.

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

Your directory for working copies: `.runs/return-step/`.

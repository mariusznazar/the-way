# Handoff — review of the whole change

## Delegation

The person who requested this cycle delegated the intermediate choices of the cycle to the
orchestrator. Nothing here is that person's approval. Do not ask the human: return `questions` to
the orchestrator.

## What you review

- Worktree: `the root of the task's worktree`, branch
  `task/part-map-dependencies-task-line`. Work from its root. Read-only: you commit nothing and
  change no tracked file.
- Range: the whole change, base `c2541ed6ef1aca0e5509cc9a929f377d97a108bc` to head `af76148`
  (confirm `git rev-parse HEAD`). One commit by the one author, no plan, no slices, no spec. Your
  report's first line is `PASS <sha>` or `FAIL <sha>`.
- Method: `task-cycle/review/SKILL.md` (`review-change`), the review of the whole change. Read it
  whole, and `whole_change.md` beside it when its step comes.
- Your directory for working copies: `.runs/review-whole/` of the worktree. Your report:
  `docs/task-cycles/part-map-dependencies-task-line/reports/review-whole-report.md`. Write the
  index of your selection of decisions to `.runs/review-whole/index.md` (a file no commit takes).
- the-way is the top-level repository: no pinned the-way, no `.the-way`; read
  `agent-instructions/README.md`. There is no `guidelines/` directory in this repository; no
  product guidelines exist to read.
- The frozen task, read whole: `docs/task-cycles/part-map-dependencies-task-line/task.md`.
  Judge the change against its seven items of *To do*, its seven rows of *Settlements to record*,
  its *Decisions in play* and the answers it holds under *Questions to settle*. It is in Polish; the
  files of the change are in English.
- The author's report (a set of claims, not evidence):
  `docs/task-cycles/part-map-dependencies-task-line/reports/author-report.md`.
- Answers of the cycle's start: no trust boundary is to be touched (check that no file the part map
  names as a boundary changed; the new tests only read a constant of two of them); no operation
  that cannot be undone; no open design choice; no reserved choice; one author, class `same`. No
  check fails on the base.

## Gaps of the author that you judge

The author's report says what it left unread or read in part. You judge the change against these
and read them yourself:

- WAY-107, which the change rewrites in place: the author's reading of the decisions skill's
  `decide_entry.md` and `elements/decisions/skill/read.md` and `projected.md` and of
  `elements/decisions/examples.md` is not recorded, and the author read `elements/part-map/examples.md`
  and `first_map.md` not at all. Check that the rewritten entry, its two paragraphs of binding
  sentences (WAY-05 allows one to three sentences for each part of the answer), its *Verification*,
  *Rationale* and *Rejected* keep the form `elements/decisions/template.md` gives.
- WAY-339's *Rationale* and *Rejected* were not read by the author, who changed its *Verification*
  to name a new invariant; WAY-44, WAY-51 were read in part. Check the decisions whose
  *Verification* the change edits (WAY-153, WAY-300, WAY-339, WAY-167).
- The change also rewords "allowed dependencies" to "allowed imports" in
  `elements/part-map/template.md` and `elements/invariants/examples.md`, which no row of the task
  names; the author gives WAY-97 as its reason. Judge whether it is within the task.
- The author made `project-level`'s part sentence two sentences while `elements/part-map/template.md`
  says one sentence for a part; the task asks for two. Judge.
- The invariants `blocked-request-line` and `guidelines-file-place` carry a *Derives from* the task
  does not name (WAY-153, WAY-167). Judge whether they hold.
- The author did not open each of the 274 lines that use the word `dependency` (WAY-97, WAY-99);
  judge whether a use of the glossary term in another meaning than its entry gives remains.

## What you select

You select your own foundation and guidelines by "Reading the foundation" in
`elements/common/way_of_working.md`, from the parts the change touches (`decisions`, `part-map`,
`glossary`, `invariants`, `project-level`, `process-audit`, `task-cycle`, `elements-common`), and
state in your report how many decisions you read whole. Check also that each of the ten
dependencies of *To do* 1 stands in the part map and that nothing else moved there; that each of
the four tests fails when its reading side or its writing side changes alone (break each for a
moment in your working copy under `.runs/review-whole/`, never in the worktree, and name the
command and exit code); and the correctness of the four tests (do not take the author's table as
evidence).

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed.

## Report

Return the first line of the report, the changed files with their line counts, the checks you ran
with commands and exit codes, your **Unread material** (or `none`) and **Searches not found or
unclear** (or `none`), and your working copies, in the report at the path above. You do not run the
product's whole gate (`python -B gate/run_tests.py` with no directory); the orchestrator does.

# Handoff — the one author of the change (task slug `small-fixes-after-prs-117-121`)

You are the one author, without a plan, of the whole change of one task of the-way. The orchestrator
of the task cycle dispatches you; the person who started the cycle has delegated intermediate
choices to the orchestrator, so every answer in this handoff is the orchestrator's, never the
human's approval. Do not ask the human anything; your questions go to the orchestrator in your
return.

## Where and what

- Worktree (work only here, from its root): `the task's worktree`, branch `task/small-fixes-after-prs-117-121`, base commit `b6b3416`.
- Method: read `task-cycle/change/SKILL.md` of the worktree whole, the variant **"the whole change as the one author"**, and a file it names only when the step or variant that names it comes. You have no skill tool; a skill that a file names by its name alone is read as a file (`task-cycle/skill/foundation_step.md` gives the paths).
- Stage and boundary: you make the whole change, write its foundation entries (the foundation step, `task-cycle/skill/foundation_step.md`, read whole) and return before review. You do **not** run the product's gate (`python -B gate/run_tests.py` without a directory): that run is the orchestrator's. Focused checks are yours, including `python -B gate/run_tests.py <directory>` for one directory and `python -B elements/common/foundation_check.py`. The return step is a later stage the orchestrator gives you separately. You dispatch no agent.
- The frozen task (read whole): `docs/task-cycles/small-fixes-after-prs-117-121/task.md`. Its *To do* items 1, 2, 5–20 are yours (3 and 4 are marked withdrawn / moved; make nothing for them). Its *Settlements to record* table rows 1–9 are all settled; `task-cycle/skill/foundation_step.md` says how a row goes to its place. The task has no spec and no plan.
- Report path: `docs/task-cycles/small-fixes-after-prs-117-121/reports/author-report.md`.
- Your directory for working copies: `.runs/author/` (directly under `.runs/` of the worktree).
- No git operation outside the worktree. Commit with `git add <path> <path>…` by explicit paths (never `-A`, `.` or `-a`), messages in English. Make several commits, one per coherent group of items (for example: the gate test; `foundation_check.py` with its test; decisions and their templates; the skills). Do not push.

## Answers of step 4

- Trust boundary: no (no file of the change is a trust boundary of the part map).
- Irreversible operation: no.
- Open design choice: none. Reserved choice: none. Route: one author without a plan.

## Choices already made for you (record them in your report's questions part where you use them)

- Q1 — the task text is stale on one point: **WAY-328 is withdrawn** (`foundations/decisions.md`, "Withdrawn identifiers"; successors WAY-379 and WAY-392). The guidelines of the-way's own code and tests are written and bind this change: read `guidelines/coding.md`, `guidelines/coding-check.md` (the kind of `foundation_check.py`) and `guidelines/testing.md` whole before you change code or a test. Do not edit WAY-328.
- *To do* 20 changes `task-cycle/skill/SKILL.md` and WAY-229, which already says "the strongest that the cycle's session lets its agents use"; make the change the item states (strongest of the models the session's settings allow, `availableModels`, not the strongest name of the family) in WAY-229 and in the two steps of the skill that repeat it (the step of the review of the whole change, "Then the review of the whole change", and step 11), and keep the other places of the foundation that repeat the sentence consistent (WAY-33 search).
- The task's sub-items "Questions carried to cycle": the technique of the fix of the trial module (one file per process, or an explicit lock) and the wording of each clause are yours to choose, the smallest that fulfils the item; name the choice in your report. After the technique is chosen, check how the tests that read the order of lines (`--jobs 1`, the limit of jobs) still see the lines.
- *To do* 1 and 2: the fix must keep `test_by_default_every_directory_runs_at_the_same_time` failing when the directories run one after another, and its 120-second wait limit. Per the task's settled question, add no permanent test of the loss of lines.
- *To do* 8 and 19 change `elements/common/foundation_check.py` and its test file; *To do* 8 also touches the description of `list_invariants`. The two items 8 and 19 touch the same file the later cycle of another task (the author's task note on the scripts after the foundation review) will change; no dependency, do only what the items say.
- WAY-344, WAY-60, WAY-61, WAY-139 and WAY-229 change in place (WAY-07, no new number, no withdrawal). Keep each decision's *Verification* and *Rationale* in agreement with the change (the items say so for WAY-139).
- *To do* 12: the clause goes into WAY-60 and the template of invariants, not into WAY-56 (withdrawn).

## What to read (the orchestrator's selection, WAY-150, WAY-213)

- The frozen task whole (above) and `task-cycle/skill/foundation_step.md` whole.
- The index of decisions of the parts you touch (`gate`, `elements-common`, `decisions`, `invariants`, `project-level`, `task-cycle`, `product-guidelines`) and of the sections "Decision entries and the decision log", "Invariants", "Scripts and the gate", "The course of a task cycle", "Task refinement and readiness", plus the decisions of the task's *Decisions in play*: `docs/task-cycles/small-fixes-after-prs-117-121/decision_index_orchestrator.md`. Open whole, as `elements/common/way_of_working.md` "Reading the foundation" gives, the decisions you change — WAY-139, WAY-344, WAY-60, WAY-61, WAY-229 — and WAY-134, WAY-172, WAY-173, WAY-17, WAY-321, WAY-62, WAY-160, WAY-142, WAY-114 (the item and settlement that cites each), and any decision the index shows binding on a sentence you write. `elements/common/way_of_working.md` "Reading the foundation" and "Search the foundation" (WAY-33): read both whole before you write an entry.
- Invariants the work reaches (WAY-62): those whose *Part* names a touched part or `every`, and every one a test you change cites with `invariant:`; each whole.
- The part map `foundations/part_map.md` whole and the glossary `foundations/glossary.md` for the terms you use.
- The templates and skills of the elements you write: `elements/decisions/template.md` and `elements/decisions/skill/SKILL.md`; `elements/invariants/template.md`; `elements/common/rules.md`.
- Guidelines (each whole): `guidelines/coding.md`, `guidelines/coding-check.md`, `guidelines/testing.md`.
- Every file you change, whole, before you change it.

Where you need a file this list does not name, reach for it selectively and name that reach in your report.

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

## Return

Write the full report to the report path as `task-cycle/change/SKILL.md` gives (including **Unread material**, **Searches not found or unclear**, the own-work check, each check with its command and exit code, the working copies line). Return its status, its commits, a one-line check result, the report's path, your questions and concerns, and the reaches beyond this handoff.

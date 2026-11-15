# Handoff — review of the whole change (task slug `small-fixes-after-prs-117-121`)

You review the whole change of one task of the-way as an agent that did not make it. The
orchestrator of the task cycle dispatches you; the person who started the cycle delegated its
intermediate choices to the orchestrator, so nothing here is the human's approval. Ask the human
nothing; questions go to the orchestrator in your return.

## Where and what

- Worktree (read-only for you; work from its root): `the task's worktree`, branch `task/small-fixes-after-prs-117-121`.
- Method: read `task-cycle/review/SKILL.md` whole, **the whole change** variant, then `task-cycle/review/whole_change.md` as it says; read a further file it names only when its step comes.
- Range: base `b6b3416` to head `e9aea95` (confirm `git rev-parse HEAD` is `e9aea95`). Five commits of one author: `ac3c96f` (move of file/git reading out of `foundation_check.py` into the new `elements/common/foundation_source.py`), `677ad78` (gate test), `52b122b` (decisions and templates), `76c2bd2` (`foundation_check.py`, its tests, README), `e9aea95` (skills).
- Route: one author without a plan; no spec; no plan; no slices. The task carries no pin move. Answers of step 4: trust boundary no; irreversible operation no. So there is no slice with a review of its own: you judge the whole change.
- The frozen task (read whole): `docs/task-cycles/small-fixes-after-prs-117-121/task.md`. Its *To do* items 1, 2, 5–20 are the change (3 and 4 are withdrawn or moved); rows 1–9 of *Settlements to record* are settled and its *Acceptance criteria* concern the description of the request, which the orchestrator writes later. Check the coverage of every item and every row, and source fidelity (each quoted text of an item against the file).
- The author's report (claims to verify, not evidence): `docs/task-cycles/small-fixes-after-prs-117-121/reports/author-report.md`. The author's handoff, which holds the orchestrator's choices: `docs/task-cycles/small-fixes-after-prs-117-121/reports/author-handoff.md`.
- No Minor or out-of-scope findings come from earlier reviews: none.
- You select your own foundation and guidelines by "Reading the foundation" in `elements/common/way_of_working.md` and `product-guidelines/reading.md`. The change touches the parts `gate`, `elements-common`, `decisions`, `invariants`, `project-level`, `product-guidelines`, `task-cycle` and `agent-instructions`; it changes five decisions in place (WAY-139, WAY-344, WAY-60, WAY-61, WAY-229), the rationale of WAY-160, and adds a file under `elements/common/`. WAY-328 is withdrawn (successors WAY-379, WAY-392): the guidelines of the-way's own code and tests (`guidelines/coding.md`, its kind files and `guidelines/testing.md`) bind the code and test files of this change.
- Information the orchestrator verified: the author could not verify the sentence in the rationale of WAY-229 that a request for a model outside the allowed list gets the session's own model. The task's source for it is the record of a session (`the session record that item 20 of the task names (a Claude Code session record of the author's, outside the repository)`): eight requests carry `"model":"fable"` and every reply of the reviewer is `claude-sonnet-5-5`. This is a log of one session, not a statement of the harness's documentation; judge the sentence's fit as you judge any claim.
- Also the cycle's own rule on what a gate run is: you run no full gate (`python -B gate/run_tests.py` without a directory); the orchestrator runs it, after a start signal of the person who started the cycle. You may run focused checks, `python -B gate/run_tests.py <directory>` and `python -B elements/common/foundation_check.py`, in your working copy where you need them.
- Report path: `docs/task-cycles/small-fixes-after-prs-117-121/reports/review-whole-report.md`. Your directory for working copies: `.runs/review-whole/` (directly under `.runs/` of the worktree).
- Mark in your report, for each blocking finding, that it comes from no slice (no plan); list the Minor findings within the task separately from those you mark outside the task's scope. Report in the form `review-change` gives, first line `PASS <sha>` or `FAIL <sha>`.

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

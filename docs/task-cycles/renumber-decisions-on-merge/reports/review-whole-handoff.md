# Handoff — review of the whole change

## Delegation
The cycle's orchestrator runs this task for the human, who delegated every intermediate choice to it. Nothing here is the human's approval. Ask the human nothing; questions go to the orchestrator in your report with the status `questions`.

## Where you work
- Worktree: `the root of the task's worktree`, from its root; branch `task/renumber-decisions-on-merge`. Read-only: you change no tracked file and make no commit.
- Your directory for working copies: `.runs/review-whole/`.
- Your report: `.runs/task-cycles/renumber-decisions-on-merge/reports/review-whole-report.md`; its first line is `PASS <sha>` or `FAIL <sha>` (or `questions`).

## Your method
Read `task-cycle/review/SKILL.md` (`review-change`) of this worktree whole, and take the variant "the whole change". You have no skill tool: read a method and every skill it names by path. You select your own foundation and guidelines by the parts of the change, as that method and "Reading the foundation" in `elements/common/way_of_working.md` give.

## What you review
- Range: base `1feb483cbb5a6538a475d6e42629441ba563d7f8` to head `34db2685` (one commit by the one author). Read the full diff of the range.
- The frozen task: `.runs/task-cycles/renumber-decisions-on-merge/task.md`, whole. It is an independent task; *Settlements to record* rows 1 and 2 and the four *To do* items are what the change must carry out, and *Questions to settle* answers 1-4 are settled.
- The author's report: `.runs/task-cycles/renumber-decisions-on-merge/reports/author-report.md`. Its *Choices* list four points to judge: row 2 written as a second paragraph of WAY-403 and not an entry of its own; the procedure placed in a new section of `task-cycle/skill/SKILL.md` that step 12 points to; the renumbering commit placed in the merge review's range, and an earlier reconciliation's conversion row rewritten with the rest; the examples of WAY-403 written with bare numbers.
- No spec, no plan, no slices: one author, one commit, no review of its own before yours.
- Trust boundary: no. Irreversible operation: no. The task did not move any pin.

## Facts the orchestrator found that the task does not say
- WAY-306, WAY-357 and WAY-328, named in the task's *Decisions in play*, are withdrawn in the log since the task was accepted (table of withdrawn identifiers at the end of `foundations/decisions.md`): WAY-306's rule now stands in `task-cycle/skill/correction.md`, WAY-357's in `task-cycle/record_template.md`, WAY-328 ended (WAY-379 and WAY-392 stand after it). A link of the change to one of them as a live decision is a finding.
- The next free number at the base is WAY-403. WAY-293 says a rule in one skill is an entry of the log only where it carries a choice with a real cost; row 1 of the task settles that this rule is an entry.

## A gap carried to you
The author read WAY-135 only to its first paragraph. Read WAY-135 whole, and judge whether it bears on the change (the cycle wrote no spec for this task).

## What the checks showed
The author ran, all exit 0: `python -B elements/common/foundation_check.py --skip-test-citations` (0 errors), `python -B gate/run_tests.py` on `task-cycle` (534), `product-guidelines` (14), `agent-instructions` (37), `elements/common` (257), `installation` (62). Nobody ran the product's full gate; its final run is CI's. Do not run it; you may run focused checks of the directories the change touches, and `python -B task-cycle/change_file_sizes.py` as the method gives.

## Working copies (word for word)
An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed, except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md` says, to the place the product's foundation settles for screenshots, and into the agent's directory only where no such place is settled. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed.

## What your report must hold
As the method gives, with the grades of each finding, `file:line` anchors, the **Unread material** section and the **Searches not found or unclear** section (each `none` or the items), the checks you ran with command and exit code, how many decisions you read whole, and the working copies.

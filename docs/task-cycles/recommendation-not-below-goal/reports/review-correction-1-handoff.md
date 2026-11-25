# Handoff — the review of correction 1 (`review-change`)

## Delegation

The person who requested this cycle has delegated the intermediate choices of the cycle to the
orchestrator. No answer or go-ahead here is that person's approval. You are the reviewer of the whole change, resumed; grade and scope of every finding are yours.

## Where and what

- Worktree: `the task's worktree`, branch `task/recommendation-not-below-goal`. Read only. You are the reviewer of the whole change (second dispatch), resumed.
- Method: `task-cycle/review/SKILL.md`, the review of a correction made for the human's remarks; read `fix.md` as it says and follow it. The remarks stand in place of a findings file.
- Range: from `e5a69f85` (the head you last reviewed carried the same code as `3130f1d9`; `8f29f4f1` and `e5a69f85` only add and remove the record's copy) to `e08834e4317de5961519bed739b02f49b7a89d0f`. Compute the diff yourself and confirm `git rev-parse HEAD`.
- The human's remarks: `.runs/task-cycles/recommendation-not-below-goal/reports/correction-1-remarks.md` — read whole; they bind. They answer your finding I1 with way a in a wording of the relation they give, and accept the request's items 3 and 4 (the place of the new paragraph and the eleven added words). The author's report: `.runs/task-cycles/recommendation-not-below-goal/reports/author-correction-1-report.md` — claims to verify, not evidence. Frozen task: `.runs/task-cycles/recommendation-not-below-goal/task.md`.
- What the correction did, per the author: WAY-166 only — a third sentence in its binding paragraph, the relation `narrows WAY-113`, its *Verification*, *Rationale* and *Rejected* aligned, marked `the cycle's` with an added pair of examples; nothing else of the foundation touched. Judge: whether the change is what the remarks give and no more (the cycle must not widen them), whether I1 is closed — that is, whether WAY-113's paragraph and WAY-166 now hold together in the case you found, and in the neighbouring cases (the technology step in `project-level/technology/settle.md`, the template in `project-level/definition_template.md`, the risk tests and the answer "you choose"), with a precedence recorded as WAY-25 gives it — whether the size limits and `foundation_check.py` hold, and whether the correction brings a new finding. A new Critical or Important finding counts as one that remains; a Minor finding does not block.
- Run no gate. Record each check you run with its command and exit code. `cycle.md` and the other files of the record directory are not yours to read.

## Report

Write the report to `.runs/task-cycles/recommendation-not-below-goal/reports/review-correction-1-report.md`; its first line is `PASS <sha>` or `FAIL <sha>`. Return that line, your checks and the path. It holds **Unread material**, **Searches not found or unclear** (each `none` where nothing), the state of I1 after the correction and any new finding and, for every blocking finding, the mark `Contradiction: yes` or `no`. The report file is the input of the cycle's scripts; if the write is refused all the same, return the report whole.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. In a product, a worktree or checkout made to run checks gets its `.the-way`
populated, and the dependencies those checks need installed as the product's own rules give,
before they run; otherwise they fail for that reason. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed,
except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
says, to the place the product's foundation settles for screenshots, and into the agent's directory
only where no such place is settled. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
`git worktree prune` — keeps in `reports/` beside its report what the report needs, the input and
command of a probe that shows a finding among them, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed. It
removes a copy, as any directory, by its path written out in full in the command, never through a
shell variable: an empty variable turns the removal on the directory the shell stands in.

Your directory for working copies: `.runs/review-whole-2/` (the same as before).

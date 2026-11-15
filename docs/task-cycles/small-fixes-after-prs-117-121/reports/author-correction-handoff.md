# Handoff — a correction for the human's remarks (task slug `small-fixes-after-prs-117-121`)

You are the one author of this change, resumed for a correction after the review of its request
(`task-cycle/skill/correction.md`). The orchestrator dispatches you; the person who started the
cycle delegated intermediate choices to the orchestrator; nothing here is the human's approval beyond
the remarks themselves, which bind. Ask the human nothing; questions go to the orchestrator.

- Worktree: `the task's worktree`, branch `task/small-fixes-after-prs-117-121`. The head is `aefe984` (the record's pair of commits `cd9bacc` and `aefe984` stands on it; the target branch brought nothing new, so there was no merge). The correction's range runs from `aefe984`.
- Method: `task-cycle/change/SKILL.md`, variant **"a correction for the human's remarks"**; read the part of it that variant names.
- The human's remarks (they bind; the file holds them word for word): `docs/task-cycles/small-fixes-after-prs-117-121/reports/correction-1-remarks.md`. In short, three things to make: (1) the rule in `task-cycle/skill/request_template.md` (the item of the top part that lists the entries the human did not see at the task, and the lower part's *Foundation entries*, as the rule needs): an entry marked `the cycle's` because of an added pair of examples quotes that pair word for word under its entry in the description; (2) finding r1 — the sentence of `agent-instructions/README.md` on the listing says it covers an invariant whose *Method* reads `test`; (3) finding r2 — the row *sentence* of `elements/invariants/template.md` says the listed line names the invariant and the field only, not whether a citing file changed. The findings r1 and r2 are in `docs/task-cycles/small-fixes-after-prs-117-121/reports/review-return-report.md` in the reviewer's words, with suggested wording; the wording of the fix is yours.
- The frozen task, for what the task asked: `docs/task-cycles/small-fixes-after-prs-117-121/task.md`. The human's answer widens the task by item (1), which the task's items 17 and 18 did not carry; write it as the human's remark asks and no wider: the rule concerns an entry that is `the cycle's` by an added pair (the same marking `task-cycle/skill/foundation_step.md` gives), not an entry marked for another reason, and not a link.
- After the change, search the foundation once for entries that state what section 6 of the description gives (WAY-33): in particular the decision on what the request puts before the human (the passage near `foundations/decisions.md:1223`, WAY-114 and the decisions that name the section) and any skill or template that repeats "one plain sentence of its meaning". Correct a mismatch where the correction needs it. A correction that would change the meaning of an approved decision beyond what the remark settles goes to the orchestrator as a question; a clarification of what the description shows, which the remark asks, does not.
- Repeat of the return step for what the remarks touch only: compare the README and the invariants template rows you change with `elements/common/foundation_check.py` at `list_invariants`, and the entries you change or find with the files; report what no longer matched and its correction. `task-cycle/skill/return_step.md`, read as for the earlier return step.
- Do not run the full gate (the orchestrator's run, after a start signal of the day advisor). Run the focused checks of what you change, with command and exit code (for the template and README: `python -B gate/run_tests.py task-cycle`, `agent-instructions`, `product-guidelines`, `elements/common`, and `python -B elements/common/foundation_check.py`). Commit by explicit paths, English messages, no push.
- Report path: `docs/task-cycles/small-fixes-after-prs-117-121/reports/correction-1-report.md`; it holds, as before, **Unread material**, **Searches not found or unclear**, the own-work check, the working copies, and for each remark how it was made. Your directory for working copies: `.runs/author/`.

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

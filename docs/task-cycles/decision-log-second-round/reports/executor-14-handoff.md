# Handoff to the executor of slice 14

You make slice 14 of the plan of one task cycle of the-way, as "a slice, or the retry of a slice" under `make-change`. The person who requested the cycle delegated intermediate choices to the orchestrator; nothing you write is anyone's approval. Work from the worktree root `the task's worktree` (branch `task/decision-log-second-round`). Commit your slice on that branch with `git add <path>` by path, an English commit message in the style of `git log --oneline`; never push; never run the product's gate (`python -B gate/run_tests.py` without a directory); change no file outside your slice's *Change*.

- Method: `task-cycle/change/SKILL.md` (`make-change`), whole, then `slice.md` beside it for how to read the plan and the task. Variant: "a slice, or the retry of a slice".
- Frozen task: `.runs/task-cycles/decision-log-second-round/task.md` (lines 1-490 are the task; Polish). Plan: `.runs/task-cycles/decision-log-second-round/plan.md` (your section is copied below, word for word, and holds).
- Answers of step 4: trust boundary no; irreversible operation no; no spec.

## What changed since the plan was written

The agent of the foundation entries has made its commits (`8d04d89`, `e643371`, `ece1f71`, `208f63c`, `5c10ee4`). The numbers a slice removes have left `foundations/decisions.md`. The plan's line ranges name lines of the base `ec7929d`, not of the log as it stands now: find an entry by its heading `### WAY-NN` in `foundations/decisions.md` as it stands (for an entry that stays or was changed), and for an entry that left the log by `git show ec7929d:foundations/decisions.md` (read the entry whole there). Where the plan's section and the log disagree, the log as it stands holds for what stays, and the base for what left.

**Ten entries stay in the log though the human's table lists them for withdrawal: WAY-93, WAY-94, WAY-97, WAY-263, WAY-287, WAY-294, WAY-295, WAY-297, WAY-363, WAY-364.** Where your section says to remove one of these numbers or to add a sentence of reason for it, do neither: leave the reference and the file as it is for that entry. (A number that stays is no error of the foundation check.) Group-D numbers (WAY-292, 317, 323, 347, 358, 369) went into WAY-288, 316, 309, 339, 357 (withdrawn) and 368: repoint as your section says.

Never invent a reason: a sentence of reason is written from the *Rationale* of the entry that left, read at the base. Where the entry's *Rationale* gives none, or the rule is not in the file and cannot be stated in a sentence, do not guess: state it in your report as a finding and leave the place unchanged.

## Your slice (copied word for word from the plan)

### Slice 14 — Guidelines: coding settle, task document, trial run and template

- **Goal:** Once made, no file of this slice names a number of a decision that left the log in the foundation entries (rows F4 and F5), each rule listed below stands in its file with one sentence of its reason, and the sentence around each removed number reads as before. A number is removed with its brackets; the sentence it stood after stays and keeps its full stop. A reference to a decision that stays in the log (any number not listed below) is left as it is. A sentence of reason is one sentence, written from the *Rationale* of the withdrawn entry that the slice reads: it says why the rule is as it is, names no file, count or measurement the entry does not give, and is placed where the rule stands. Where a rule is only partly in the file, the missing sentence of the rule is added first, then its reason. Make no other change. These are the lines of the base; find a number by searching the file for it.
  Files:
  - `product-guidelines/coding/settle.md` — remove WAY-200 (line 35); WAY-201 (line 36); WAY-202 (line 20, 93); WAY-207 (line 27, 99); WAY-210 (line 11, 87); WAY-271 (line 43, 110); WAY-272 (line 135, 139); WAY-275 (line 56, 137); WAY-277 (line 14); WAY-278 (line 43); WAY-279 (line 43); WAY-363 (line 90) · add one sentence of the reason of WAY-277 line 14 (end of the sentence '... a decision of its own in the product's log (WAY-277).' before 'Where that library meets the test') — and the file lacks part of the rule itself: settle.md:10-17 states: question of the task put to the human by new_tools.md, 'a library chosen is a decision of its own in the product's log (WAY-277)', and reserved choice goes to settle-technology (WAY-268). Missing in settle.md: log 9111-9112 'a cycle th… (add that first) · add one sentence of the reason of WAY-279 line 43-45 (the bullet '... the product's one decision on the rules on failures and logs ...' before 'It takes:').
  - `product-guidelines/coding/task_document.md` — remove WAY-271 (line 20); WAY-277 (line 21); WAY-279 (line 20).
  - `product-guidelines/coding/trial_run.md` — remove WAY-281 (line 23).
  - `product-guidelines/coding/template.md` — remove WAY-76 (line 323); WAY-86 (line 144, 317); WAY-171 (line 24, 68, 91, 120, 124, 172, 269, 288, 293, 296, 345); WAY-191 (line 325); WAY-200 (line 261); WAY-202 (line 65, 68, 75, 144, 157, 162, 172); WAY-207 (line 149, 152, 329); WAY-208 (line 80); WAY-211 (line 343); WAY-271 (line 72, 174, 186); WAY-272 (line 197); WAY-275 (line 208, 210); WAY-277 (line 344); WAY-279 (line 181, 274, 293, 296); WAY-310 (line 289); WAY-363 (line 78) · add one sentence of the reason of WAY-202 line 68 (the bullet 'The three standing checks ... none - <PREFIX-NN>') — and the file lacks part of the rule itself: template.md:66-68 and 12-14 state the three standing checks, the departure by a decision with reason (`none - <PREFIX-NN>`), and the invariants (template.md:145-146, 157-158, 163-165). Not in template.md: 'which is complete only once it holds, for each of the… (add that first) · add one sentence of the reason of WAY-207 line 152 (end of the Linter bullet, '... holds the configuration to the decision (WAY-207).') — and the file lacks part of the rule itself: template.md:148-152 states 'a fault of one file is fixed in that file', 'Turning a rule that blocks off in the linter's configuration is a change of the adopting decision' and the review keeps the configuration to the decision; settle.md:25-27 adds 'approved… (add that first) · add one sentence of the reason of WAY-271 line 172 (before 'The rules on failures and logs' bullet), or at line 176 end of its first paragraph · add one sentence of the reason of WAY-272 line 197 (end of the 'Recording a failure' bullet) · add one sentence of the reason of WAY-275 line 210 (end of the 'Business events' bullet).
- **Change:** `product-guidelines/coding/settle.md` · `product-guidelines/coding/task_document.md` · `product-guidelines/coding/trial_run.md` · `product-guidelines/coding/template.md`
- **Read:** `.runs/task-cycles/decision-log-second-round/task.md:33-40` To do
  · `foundations/decisions.md:9771-9810` WAY-293
  · `foundations/decisions.md:6199-6233` WAY-202 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:6428-6462` WAY-207 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:8865-8897` WAY-271 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:8899-8936` WAY-272 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:9021-9056` WAY-275 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:9106-9134` WAY-277 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:9168-9204` WAY-279 (leaves the log in the foundation entries; read at the base ec7929d)
- **Model:** cheaper — a settled pattern carried into text
- **Risk:** none
- **Checks:** `python -B elements/common/foundation_check.py` — the lines it prints for the files of this slice's *Change*: none; the exit code stands at 1 until the last slice, from the lines of files of slices not yet made
- **Depends on:** rows F4 · F5 of the foundation entries

## Checks

Run the checks your section lists and nothing else of the gate. `python -B elements/common/foundation_check.py` still lists lines for the files of slices not yet made: your check is that it lists none for your *Change* files. Report each check as a command and its exit code. A `gate/run_tests.py <directory>` that says `no test found` has no tests: say so.

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

Your directory for working copies: `.runs/executor-14/`.

## Report

Write your full report to `.runs/task-cycles/decision-log-second-round/reports/executor-14-report.md` with: status (`done`, `done with concerns`, `questions`, `returned`, `blocked`), commits, each check with command and exit code, your own-work check (`make-change` section 3), the reasons you added (file and sentence, with the entry you wrote it from), entries you left under the "stay" rule above, **Unread material**, **Searches not found or unclear**, working copies and where they stood. Return the status, commits, one-line check result and the report path.

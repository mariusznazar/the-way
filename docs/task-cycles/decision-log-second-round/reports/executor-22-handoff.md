# Handoff to the executor of slice 22

You make slice 22 of the plan of one task cycle of the-way, as "a slice, or the retry of a slice" under `make-change`. The person who requested the cycle delegated intermediate choices to the orchestrator; nothing you write is anyone's approval. Work from the worktree root `the task's worktree` (branch `task/decision-log-second-round`). Commit your slice on that branch with `git add <path>` by path, an English commit message in the style of `git log --oneline`; never push; never run the product's gate (`python -B gate/run_tests.py` without a directory); change no file outside your slice's *Change*.

- Method: `task-cycle/change/SKILL.md` (`make-change`), whole, then `slice.md` beside it for how to read the plan and the task. Variant: "a slice, or the retry of a slice".
- Frozen task: `.runs/task-cycles/decision-log-second-round/task.md` (lines 1-490 are the task; Polish). Plan: `.runs/task-cycles/decision-log-second-round/plan.md` (your section is copied below, word for word, and holds).
- Answers of step 4: trust boundary no; irreversible operation no; no spec.

## What changed since the plan was written

The agent of the foundation entries has made its commits (`8d04d89`, `e643371`, `ece1f71`, `208f63c`, `5c10ee4`). The numbers a slice removes have left `foundations/decisions.md`. The plan's line ranges name lines of the base `ec7929d`, not of the log as it stands now: find an entry by its heading `### WAY-NN` in `foundations/decisions.md` as it stands (for an entry that stays or was changed), and for an entry that left the log by `git show ec7929d:foundations/decisions.md` (read the entry whole there). Where the plan's section and the log disagree, the log as it stands holds for what stays, and the base for what left.

**Ten entries stay in the log though the human's table lists them for withdrawal: WAY-93, WAY-94, WAY-97, WAY-263, WAY-287, WAY-294, WAY-295, WAY-297, WAY-363, WAY-364.** Where your section says to remove one of these numbers or to add a sentence of reason for it, do neither: leave the reference and the file as it is for that entry. (A number that stays is no error of the foundation check.) Group-D numbers (WAY-292, 317, 323, 347, 358, 369) went into WAY-288, 316, 309, 339, 357 (withdrawn) and 368: repoint as your section says.

Never invent a reason: a sentence of reason is written from the *Rationale* of the entry that left, read at the base. Where the entry's *Rationale* gives none, or the rule is not in the file and cannot be stated in a sentence, do not guess: state it in your report as a finding and leave the place unchanged.

## Your slice (copied word for word from the plan)

### Slice 22 — Task cycle: the request template, the author and the plan skill

- **Goal:** Once made, no file of this slice names a number of a decision that left the log in the foundation entries (rows F4 and F5), each rule listed below stands in its file with one sentence of its reason, and the sentence around each removed number reads as before. A number is removed with its brackets; the sentence it stood after stays and keeps its full stop. A reference to a decision that stays in the log (any number not listed below) is left as it is. A sentence of reason is one sentence, written from the *Rationale* of the withdrawn entry that the slice reads: it says why the rule is as it is, names no file, count or measurement the entry does not give, and is placed where the rule stands. Where a rule is only partly in the file, the missing sentence of the rule is added first, then its reason. Make no other change. These are the lines of the base; find a number by searching the file for it.
  Files:
  - `task-cycle/skill/request_template.md` — remove WAY-49 (line 297, 465); WAY-163 (line 508); WAY-219 (line 231, 453); WAY-286 (line 7, 156, 163, 356); WAY-290 (line 24); WAY-291 (line 51); WAY-317 (line 179); WAY-318 (line 180); WAY-326 (line 251); WAY-327 (line 15, 344, 361); WAY-358 (line 327); WAY-367 (line 451) · WAY-292 line 159, repoint:WAY-288: '(WAY-288, WAY-292)' becomes '(WAY-288)'; WAY-288 holds the block question. · WAY-317 line 320, repoint:WAY-316: Item 13 'No screenshot of a changed screen (WAY-317)' points to WAY-316, whose paragraph will hold the no-place case. · add one sentence of the reason of WAY-286 line 7, after the opening paragraph "... Every request of a cycle, blocked, reserved or corrected, has this one skeleton (WAY-286, WAY-287)." (lines 3-7); alternatively after line 163 · add one sentence of the reason of WAY-290 line 24, after the sentence that ends "and judges no content (WAY-290)." (lines 22-24) · add one sentence of the reason of WAY-291 line 52, after item 1 of "An error you hold wrong." (items at lines 53-64 start at 53); or after line 58 · add one sentence of the reason of WAY-318 line 180 (the sentence ending 'leave logs and outputs in the reports') · add one sentence of the reason of WAY-327 line 361 (end of the bullet on the fifth part, '... has no steps (WAY-327).').
  - `agent-instructions/README.md` — remove WAY-286 (line 79); WAY-290 (line 83); WAY-291 (line 84).
  - `task-cycle/change/SKILL.md` — remove WAY-262 (line 147) · add one sentence of the reason of WAY-262 line 147, the end of the own-work bullet "when a check failed and passed when run again, both runs as command and exit code (WAY-262);" (lines 146-147).
  - `task-cycle/change/ui_check.md` — remove WAY-219 (line 8); WAY-317 (line 14); WAY-318 (line 16) · add one sentence of the reason of WAY-219 line 9 (end of the first bullet, '... Reading code shows no rendered appearance.').
  - `task-cycle/plan/SKILL.md` — add one sentence of the reason of WAY-264 line 136, after the sentence that ends "*Change* names the command's source only when that slice changes it." (lines 127-136).
- **Change:** `task-cycle/skill/request_template.md` · `agent-instructions/README.md` · `task-cycle/change/SKILL.md` · `task-cycle/change/ui_check.md` · `task-cycle/plan/SKILL.md`
- **Read:** `.runs/task-cycles/decision-log-second-round/task.md:33-40` To do
  · `foundations/decisions.md:9771-9810` WAY-293
  · `foundations/decisions.md:6888-6920` WAY-219 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:8452-8467` WAY-262 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:8496-8531` WAY-264 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:9436-9471` WAY-286 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:9679-9711` WAY-290 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:9713-9744` WAY-291 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:9746-9769` WAY-292 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:10755-10790` WAY-317 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:10792-10817` WAY-318 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:11177-11230` WAY-327 (leaves the log in the foundation entries; read at the base ec7929d)
- **Model:** same — rules of the cycle are missing in part and every cycle reads them
- **Risk:** none
- **Checks:** `python -B elements/common/foundation_check.py` — the lines it prints for the files of this slice's *Change*: none; the exit code stands at 1 until the last slice, from the lines of files of slices not yet made · `python -B gate/run_tests.py task-cycle` · `python -B gate/run_tests.py agent-instructions` · `python -B agent-instructions/skill_entry_points.py` (nothing to write: no frontmatter changes)
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

Your directory for working copies: `.runs/executor-22/`.

## Report

Write your full report to `.runs/task-cycles/decision-log-second-round/reports/executor-22-report.md` with: status (`done`, `done with concerns`, `questions`, `returned`, `blocked`), commits, each check with command and exit code, your own-work check (`make-change` section 3), the reasons you added (file and sentence, with the entry you wrote it from), entries you left under the "stay" rule above, **Unread material**, **Searches not found or unclear**, working copies and where they stood. Return the status, commits, one-line check result and the report path.

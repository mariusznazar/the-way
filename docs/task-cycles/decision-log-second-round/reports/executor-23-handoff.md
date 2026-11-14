# Handoff to the executor of slice 23

You make slice 23 of the plan of one task cycle of the-way, as "a slice, or the retry of a slice" under `make-change`. The person who requested the cycle delegated intermediate choices to the orchestrator; nothing you write is anyone's approval. Work from the worktree root `the task's worktree` (branch `task/decision-log-second-round`). Commit your slice on that branch with `git add <path>` by path, an English commit message in the style of `git log --oneline`; never push; never run the product's gate (`python -B gate/run_tests.py` without a directory); change no file outside your slice's *Change*.

- Method: `task-cycle/change/SKILL.md` (`make-change`), whole, then `slice.md` beside it for how to read the plan and the task. Variant: "a slice, or the retry of a slice".
- Frozen task: `.runs/task-cycles/decision-log-second-round/task.md` (lines 1-490 are the task; Polish). Plan: `.runs/task-cycles/decision-log-second-round/plan.md` (your section is copied below, word for word, and holds).
- Answers of step 4: trust boundary no; irreversible operation no; no spec.

## What changed since the plan was written

The agent of the foundation entries has made its commits (`8d04d89`, `e643371`, `ece1f71`, `208f63c`, `5c10ee4`). The numbers a slice removes have left `foundations/decisions.md`. The plan's line ranges name lines of the base `ec7929d`, not of the log as it stands now: find an entry by its heading `### WAY-NN` in `foundations/decisions.md` as it stands (for an entry that stays or was changed), and for an entry that left the log by `git show ec7929d:foundations/decisions.md` (read the entry whole there). Where the plan's section and the log disagree, the log as it stands holds for what stays, and the base for what left.

**Ten entries stay in the log though the human's table lists them for withdrawal: WAY-93, WAY-94, WAY-97, WAY-263, WAY-287, WAY-294, WAY-295, WAY-297, WAY-363, WAY-364.** Where your section says to remove one of these numbers or to add a sentence of reason for it, do neither: leave the reference and the file as it is for that entry. (A number that stays is no error of the foundation check.) Group-D numbers (WAY-292, 317, 323, 347, 358, 369) went into WAY-288, 316, 309, 339, 357 (withdrawn) and 368: repoint as your section says.

Never invent a reason: a sentence of reason is written from the *Rationale* of the entry that left, read at the base. Where the entry's *Rationale* gives none, or the rule is not in the file and cannot be stated in a sentence, do not guess: state it in your report as a finding and leave the place unchanged.

## Your slice (copied word for word from the plan)

### Slice 23 — Task cycle: the review skill

- **Goal:** Once made, no file of this slice names a number of a decision that left the log in the foundation entries (rows F4 and F5), each rule listed below stands in its file with one sentence of its reason, and the sentence around each removed number reads as before. A number is removed with its brackets; the sentence it stood after stays and keeps its full stop. A reference to a decision that stays in the log (any number not listed below) is left as it is. A sentence of reason is one sentence, written from the *Rationale* of the withdrawn entry that the slice reads: it says why the rule is as it is, names no file, count or measurement the entry does not give, and is placed where the rule stands. Where a rule is only partly in the file, the missing sentence of the rule is added first, then its reason. Make no other change. These are the lines of the base; find a number by searching the file for it.
  Files:
  - `task-cycle/review/SKILL.md` — remove WAY-170 (line 78); WAY-219 (line 92); WAY-220 (line 116); WAY-221 (line 117); WAY-297 (line 127); WAY-363 (line 133); WAY-364 (line 138) · WAY-317 line 95, repoint:WAY-316: '(WAY-316, WAY-317)' becomes '(WAY-316)'; WAY-316 names the product with no place settled (log 10741-10742). · add one sentence of the reason of WAY-220 line 116, after the sentence "Grade an appearance finding by its effect on the user, neither Minor because it is visual nor blocking because it is visible (WAY-220)." (lines 115-116) · add one sentence of the reason of WAY-221 line 117, after the sentence "A departure from a guideline example blocks only through the consequence you name for the user or for the code (WAY-221)." (lines 116-117) — and the file lacks part of the rule itself: Stands: review/SKILL.md:116-117 "A departure from a guideline example blocks only through the consequence you name for the user or for the code (WAY-221)." Not in the target: "or from the part of an exemplar no script checks" and "Binding rules and their inva… (add that first) · add one sentence of the reason of WAY-297 line 127, after the sentence that ends "is graded as the paragraph above gives (WAY-297)." (lines 123-127) · add one sentence of the reason of WAY-363 line 133 (the sentence ending '... graded as any other finding (WAY-363).') · add one sentence of the reason of WAY-364 line 138 (the sentence ending '... as the paragraph on WAY-263 above gives (WAY-364).').
  - `task-cycle/review/whole_change.md` — remove WAY-362 (line 33); WAY-363 (line 49, 52) · add one sentence of the reason of WAY-362 line 33 (the sentence ending '... a name that stopped being true (WAY-362).').
- **Change:** `task-cycle/review/SKILL.md` · `task-cycle/review/whole_change.md`
- **Read:** `.runs/task-cycles/decision-log-second-round/task.md:33-40` To do
  · `foundations/decisions.md:9771-9810` WAY-293
  · `foundations/decisions.md:6923-6943` WAY-220 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:6946-6970` WAY-221 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:9948-9986` WAY-297 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:10755-10790` WAY-317 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:12408-12438` WAY-362 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:12440-12487` WAY-363 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:12489-12529` WAY-364 (leaves the log in the foundation entries; read at the base ec7929d)
- **Model:** same — grading rules of the reviewer are missing in part
- **Risk:** none
- **Checks:** `python -B elements/common/foundation_check.py` on this repository, exit code 0 (every earlier slice is made) · `python -B gate/run_tests.py task-cycle` · `python -B agent-instructions/skill_entry_points.py` (nothing to write: no frontmatter changes)
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

Your directory for working copies: `.runs/executor-23/`.

## Report

Write your full report to `.runs/task-cycles/decision-log-second-round/reports/executor-23-report.md` with: status (`done`, `done with concerns`, `questions`, `returned`, `blocked`), commits, each check with command and exit code, your own-work check (`make-change` section 3), the reasons you added (file and sentence, with the entry you wrote it from), entries you left under the "stay" rule above, **Unread material**, **Searches not found or unclear**, working copies and where they stood. Return the status, commits, one-line check result and the report path.

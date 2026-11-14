# Handoff to the executor of slice 7

You make slice 7 of the plan of one task cycle of the-way, as "a slice, or the retry of a slice" under `make-change`. The person who requested the cycle delegated intermediate choices to the orchestrator; nothing you write is anyone's approval. Work from the worktree root `the task's worktree` (branch `task/decision-log-second-round`). Commit your slice on that branch with `git add <path>` by path, an English commit message in the style of `git log --oneline`; never push; never run the product's gate (`python -B gate/run_tests.py` without a directory); change no file outside your slice's *Change*.

- Method: `task-cycle/change/SKILL.md` (`make-change`), whole, then `slice.md` beside it for how to read the plan and the task. Variant: "a slice, or the retry of a slice".
- Frozen task: `.runs/task-cycles/decision-log-second-round/task.md` (lines 1-490 are the task; Polish). Plan: `.runs/task-cycles/decision-log-second-round/plan.md` (your section is copied below, word for word, and holds).
- Answers of step 4: trust boundary no; irreversible operation no; no spec.

## What changed since the plan was written

The agent of the foundation entries has made its commits (`8d04d89`, `e643371`, `ece1f71`, `208f63c`, `5c10ee4`). The numbers a slice removes have left `foundations/decisions.md`. The plan's line ranges name lines of the base `ec7929d`, not of the log as it stands now: find an entry by its heading `### WAY-NN` in `foundations/decisions.md` as it stands (for an entry that stays or was changed), and for an entry that left the log by `git show ec7929d:foundations/decisions.md` (read the entry whole there). Where the plan's section and the log disagree, the log as it stands holds for what stays, and the base for what left.

**Ten entries stay in the log though the human's table lists them for withdrawal: WAY-93, WAY-94, WAY-97, WAY-263, WAY-287, WAY-294, WAY-295, WAY-297, WAY-363, WAY-364.** Where your section says to remove one of these numbers or to add a sentence of reason for it, do neither: leave the reference and the file as it is for that entry. (A number that stays is no error of the foundation check.) Group-D numbers (WAY-292, 317, 323, 347, 358, 369) went into WAY-288, 316, 309, 339, 357 (withdrawn) and 368: repoint as your section says.

Never invent a reason: a sentence of reason is written from the *Rationale* of the entry that left, read at the base. Where the entry's *Rationale* gives none, or the rule is not in the file and cannot be stated in a sentence, do not guess: state it in your report as a finding and leave the place unchanged.

## Your slice (copied word for word from the plan)

### Slice 7 — Foundation review and instruction files

- **Goal:** Once made, no file of this slice names a number of a decision that left the log in the foundation entries (rows F4 and F5), each rule listed below stands in its file with one sentence of its reason, and the sentence around each removed number reads as before. A number is removed with its brackets; the sentence it stood after stays and keeps its full stop. A reference to a decision that stays in the log (any number not listed below) is left as it is. A sentence of reason is one sentence, written from the *Rationale* of the withdrawn entry that the slice reads: it says why the rule is as it is, names no file, count or measurement the entry does not give, and is placed where the rule stands. Where a rule is only partly in the file, the missing sentence of the rule is added first, then its reason. Make no other change. These are the lines of the base; find a number by searching the file for it.
  Files:
  - `foundation-review/SKILL.md` — remove WAY-301 (line 34, 88); WAY-302 (line 12, 62, 78); WAY-303 (line 56); WAY-304 (line 15, 38, 56); WAY-305 (line 51); WAY-354 (line 51, 62, 78) · add one sentence of the reason of WAY-301 step 7, first bullet (line 88, after '(WAY-301).' is removed): the sentence on the tag name, annotated, on the checked commit, also when the review changed nothing · add one sentence of the reason of WAY-302 the sentence ending line 14 of the opening paragraph ('It changes nothing in the foundation or the code: a proposal the human accepts becomes a task ... through that task's cycle (WAY-14).').
  - `foundation-review/proposals.md` — remove WAY-302 (line 33); WAY-354 (line 28) · add one sentence of the reason of WAY-354 line 28 (end of 'Decisions that describe a transitional state', after the sentence 'The entry of the decision is not changed and gains no field').
  - `foundation-review/remarks.md` — remove WAY-303 (line 10); WAY-304 (line 5) · add one sentence of the reason of WAY-303 line 5 (end of the opening paragraph, after '(WAY-304)' is removed); the sentence that no other review reads these remarks goes with it — and the file lacks part of the rule itself: Missing sentence of the entry: "No other periodic review reads these remarks." (log 10207-10208; Verification 'violates: a weekly review of the same remarks runs beside the review of the foundation'). remarks.md:19-20 says only that a remark about the process… (add that first) · add one sentence of the reason of WAY-304 line 5 (end of the opening paragraph, after '(WAY-304)' is removed).
  - `foundation-review/weak_points.md` — remove WAY-305 (line 20); WAY-354 (line 34) · add one sentence of the reason of WAY-305 line 28 (end of the paragraph 'Run the check a weak point lacks...'), or after line 20 for the listing.
  - `foundation-review/with_the_human.md` — remove WAY-302 (line 34); WAY-354 (line 20, 34).
  - `instruction-files/SKILL.md` — remove WAY-257 (line 101).
  - `instruction-files/judging.md` — remove WAY-257 (line 17); WAY-311 (line 30) · add one sentence of the reason of WAY-311 line 30 (end of the paragraph on a fragment that goes to several places and on a proposal).
- **Change:** `foundation-review/SKILL.md` · `foundation-review/proposals.md` · `foundation-review/remarks.md` · `foundation-review/weak_points.md` · `foundation-review/with_the_human.md` · `instruction-files/SKILL.md` · `instruction-files/judging.md`
- **Read:** `.runs/task-cycles/decision-log-second-round/task.md:33-40` To do
  · `foundations/decisions.md:9771-9810` WAY-293
  · `foundations/decisions.md:10142-10167` WAY-301 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:10169-10199` WAY-302 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:10201-10236` WAY-303 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:10238-10268` WAY-304 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:10270-10296` WAY-305 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:10521-10546` WAY-311 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:12101-12138` WAY-354 (leaves the log in the foundation entries; read at the base ec7929d)
- **Model:** cheaper — a settled pattern carried into text
- **Risk:** none
- **Checks:** `python -B elements/common/foundation_check.py` — the lines it prints for the files of this slice's *Change*: none; the exit code stands at 1 until the last slice, from the lines of files of slices not yet made · `python -B gate/run_tests.py instruction-files` · `python -B agent-instructions/skill_entry_points.py` (nothing to write: no frontmatter changes)
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

Your directory for working copies: `.runs/executor-7/`.

## Report

Write your full report to `.runs/task-cycles/decision-log-second-round/reports/executor-7-report.md` with: status (`done`, `done with concerns`, `questions`, `returned`, `blocked`), commits, each check with command and exit code, your own-work check (`make-change` section 3), the reasons you added (file and sentence, with the entry you wrote it from), entries you left under the "stay" rule above, **Unread material**, **Searches not found or unclear**, working copies and where they stood. Return the status, commits, one-line check result and the report path.

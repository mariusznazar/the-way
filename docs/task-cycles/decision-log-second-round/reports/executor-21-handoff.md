# Handoff to the executor of slice 21

You make slice 21 of the plan of one task cycle of the-way, as "a slice, or the retry of a slice" under `make-change`. The person who requested the cycle delegated intermediate choices to the orchestrator; nothing you write is anyone's approval. Work from the worktree root `the task's worktree` (branch `task/decision-log-second-round`). Commit your slice on that branch with `git add <path>` by path, an English commit message in the style of `git log --oneline`; never push; never run the product's gate (`python -B gate/run_tests.py` without a directory); change no file outside your slice's *Change*.

- Method: `task-cycle/change/SKILL.md` (`make-change`), whole, then `slice.md` beside it for how to read the plan and the task. Variant: "a slice, or the retry of a slice".
- Frozen task: `.runs/task-cycles/decision-log-second-round/task.md` (lines 1-490 are the task; Polish). Plan: `.runs/task-cycles/decision-log-second-round/plan.md` (your section is copied below, word for word, and holds).
- Answers of step 4: trust boundary no; irreversible operation no; no spec.

## What changed since the plan was written

The agent of the foundation entries has made its commits (`8d04d89`, `e643371`, `ece1f71`, `208f63c`, `5c10ee4`). The numbers a slice removes have left `foundations/decisions.md`. The plan's line ranges name lines of the base `ec7929d`, not of the log as it stands now: find an entry by its heading `### WAY-NN` in `foundations/decisions.md` as it stands (for an entry that stays or was changed), and for an entry that left the log by `git show ec7929d:foundations/decisions.md` (read the entry whole there). Where the plan's section and the log disagree, the log as it stands holds for what stays, and the base for what left.

**Ten entries stay in the log though the human's table lists them for withdrawal: WAY-93, WAY-94, WAY-97, WAY-263, WAY-287, WAY-294, WAY-295, WAY-297, WAY-363, WAY-364.** Where your section says to remove one of these numbers or to add a sentence of reason for it, do neither: leave the reference and the file as it is for that entry. (A number that stays is no error of the foundation check.) Group-D numbers (WAY-292, 317, 323, 347, 358, 369) went into WAY-288, 316, 309, 339, 357 (withdrawn) and 368: repoint as your section says.

Never invent a reason: a sentence of reason is written from the *Rationale* of the entry that left, read at the base. Where the entry's *Rationale* gives none, or the rule is not in the file and cannot be stated in a sentence, do not guess: state it in your report as a finding and leave the place unchanged.

## Your slice (copied word for word from the plan)

### Slice 21 — Task cycle: the orchestrator skill, the record and the correction

- **Goal:** Once made, no file of this slice names a number of a decision that left the log in the foundation entries (rows F4 and F5), each rule listed below stands in its file with one sentence of its reason, and the sentence around each removed number reads as before. A number is removed with its brackets; the sentence it stood after stays and keeps its full stop. A reference to a decision that stays in the log (any number not listed below) is left as it is. A sentence of reason is one sentence, written from the *Rationale* of the withdrawn entry that the slice reads: it says why the rule is as it is, names no file, count or measurement the entry does not give, and is placed where the rule stands. Where a rule is only partly in the file, the missing sentence of the rule is added first, then its reason. Make no other change. These are the lines of the base; find a number by searching the file for it.
  Files:
  - `task-cycle/skill/SKILL.md` — remove WAY-158 (line 449); WAY-159 (line 276, 409, 468); WAY-220 (line 485); WAY-221 (line 485); WAY-286 (line 582); WAY-290 (line 582); WAY-296 (line 86); WAY-298 (line 130); WAY-325 (line 263); WAY-326 (line 263, 277, 409); WAY-367 (line 155) · add one sentence of the reason of WAY-158 line 450, the sentence of step 9 that ends "never to change a reviewer's grade or scope." (lines 448-450) — and the file lacks part of the rule itself: The orchestrator half stands: task-cycle/skill/SKILL.md:448-450 "For progression use the changed files with their line counts and the review's first line (WAY-158); read the evidence only when a question about a finding needs it, never to change a reviewer's… (add that first) · add one sentence of the reason of WAY-159 line 469, the sentence of step 10 that ends "by the agent that owns them." (lines 467-469) · add one sentence of the reason of WAY-298 step 4, line 133 (the sentence ending 'where it cannot fast-forward, stop and say so.') · add one sentence of the reason of WAY-325 line 269 (the sentence ending 'saying why it bears on nothing the agent judged.') · add one sentence of the reason of WAY-326 line 279 (the sentence ending '`none` is an answer, a missing section is not.') · add one sentence of the reason of WAY-349 line 459 (step 10, the sentence 'The gate's output passes through unchanged.') · add one sentence of the reason of WAY-367 line 156 (step 4, the sentence 'If it is, do not run the gate on the base.').
  - `task-cycle/skill/blocked_finding.md` — remove WAY-163 (line 10) · add one sentence of the reason of WAY-163 line 10, after the sentence that ends "has not accepted (WAY-163)." (sentence begins line 6/7) — and the file lacks part of the rule itself: Stands in blocked_finding.md:7-10 (gate run at once, record written, "make no further slice, no return step and no reconciliation with the target branch on code its review has not accepted") and :18-19. Missing from the target: (a) the entry's "the request na… (add that first).
  - `task-cycle/skill/correction.md` — remove WAY-163 (line 46); WAY-306 (line 10, 32); WAY-357 (line 35, 54); WAY-358 (line 54) · add one sentence of the reason of WAY-306 line 32 (the sentence ending 'run them again.'); the same sentence is also carried by step 12 of task-cycle/skill/SKILL.md:535-538, which correction.md points to — and the file lacks part of the rule itself: Entry sentence not in the target: 'the reviewer's range is the commits of the merge the dispatch gives'. correction.md:29-32 and SKILL.md:535-538 state the question and the named entries, and SKILL.md:480-483 lists the reconciliation review under 'The end of… (add that first).
  - `task-cycle/skill/spec_review.md` — add one sentence of the reason of WAY-307 line 7 (the sentence ending 'comparing the two.').
  - `task-cycle/record_template.md` — remove WAY-317 (line 166); WAY-357 (line 215); WAY-358 (line 225) · add one sentence of the reason of WAY-357 line 226 (end of the paragraph on the corrections, '... which stay the last item of the record.') — and the file lacks part of the rule itself: Entry sentence not in the target files: 'the title of the commit that adds a copy of the record holds no cause.' record_template.md:214-226 and correction.md:52-63 state the one line per correction, its place before the process remarks and the file of remarks… (add that first).
  - Beside the files: WAY-358 (group D, withdrawn with the withdrawn WAY-357 as successor) gave what causes the line of a correction gives; check that `task-cycle/record_template.md` says it, and where it does not, add that sentence of the rule from the binding sentences of WAY-358 read at the base, with one sentence of its reason; the measure its *Rejected* quotes is not copied.
- **Change:** `task-cycle/skill/SKILL.md` · `task-cycle/skill/blocked_finding.md` · `task-cycle/skill/correction.md` · `task-cycle/skill/spec_review.md` · `task-cycle/record_template.md`
- **Read:** `.runs/task-cycles/decision-log-second-round/task.md:33-40` To do
  · `foundations/decisions.md:9771-9810` WAY-293
  · `foundations/decisions.md:4829-4856` WAY-158 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:4858-4886` WAY-159 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:5078-5114` WAY-163 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:9988-10046` WAY-298 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:10298-10337` WAY-306 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:10339-10363` WAY-307 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:11103-11133` WAY-325 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:11135-11175` WAY-326 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:11943-11974` WAY-349 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:12211-12238` WAY-357 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:12602-12642` WAY-367 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:12240-12279` WAY-358 (leaves the log in the foundation entries; read at the base ec7929d)
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

Your directory for working copies: `.runs/executor-21/`.

## Report

Write your full report to `.runs/task-cycles/decision-log-second-round/reports/executor-21-report.md` with: status (`done`, `done with concerns`, `questions`, `returned`, `blocked`), commits, each check with command and exit code, your own-work check (`make-change` section 3), the reasons you added (file and sentence, with the entry you wrote it from), entries you left under the "stay" rule above, **Unread material**, **Searches not found or unclear**, working copies and where they stood. Return the status, commits, one-line check result and the report path.

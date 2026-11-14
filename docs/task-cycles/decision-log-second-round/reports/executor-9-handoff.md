# Handoff to the executor of slice 9

You make slice 9 of the plan of one task cycle of the-way, as "a slice, or the retry of a slice" under `make-change`. The person who requested the cycle delegated intermediate choices to the orchestrator; nothing you write is anyone's approval. Work from the worktree root `the task's worktree` (branch `task/decision-log-second-round`). Commit your slice on that branch with `git add <path>` by path, an English commit message in the style of `git log --oneline`; never push; never run the product's gate (`python -B gate/run_tests.py` without a directory); change no file outside your slice's *Change*.

- Method: `task-cycle/change/SKILL.md` (`make-change`), whole, then `slice.md` beside it for how to read the plan and the task. Variant: "a slice, or the retry of a slice".
- Frozen task: `.runs/task-cycles/decision-log-second-round/task.md` (lines 1-490 are the task; Polish). Plan: `.runs/task-cycles/decision-log-second-round/plan.md` (your section is copied below, word for word, and holds).
- Answers of step 4: trust boundary no; irreversible operation no; no spec.

## What changed since the plan was written

The agent of the foundation entries has made its commits (`8d04d89`, `e643371`, `ece1f71`, `208f63c`, `5c10ee4`). The numbers a slice removes have left `foundations/decisions.md`. The plan's line ranges name lines of the base `ec7929d`, not of the log as it stands now: find an entry by its heading `### WAY-NN` in `foundations/decisions.md` as it stands (for an entry that stays or was changed), and for an entry that left the log by `git show ec7929d:foundations/decisions.md` (read the entry whole there). Where the plan's section and the log disagree, the log as it stands holds for what stays, and the base for what left.

**Ten entries stay in the log though the human's table lists them for withdrawal: WAY-93, WAY-94, WAY-97, WAY-263, WAY-287, WAY-294, WAY-295, WAY-297, WAY-363, WAY-364.** Where your section says to remove one of these numbers or to add a sentence of reason for it, do neither: leave the reference and the file as it is for that entry. (A number that stays is no error of the foundation check.) Group-D numbers (WAY-292, 317, 323, 347, 358, 369) went into WAY-288, 316, 309, 339, 357 (withdrawn) and 368: repoint as your section says.

Never invent a reason: a sentence of reason is written from the *Rationale* of the entry that left, read at the base. Where the entry's *Rationale* gives none, or the rule is not in the file and cannot be stated in a sentence, do not guess: state it in your report as a finding and leave the place unchanged.

## Your slice (copied word for word from the plan)

### Slice 9 — Process audit: the skill, the register and the tests

- **Goal:** Once made, no file of this slice names a number of a decision that left the log in the foundation entries (rows F4 and F5), each rule listed below stands in its file with one sentence of its reason, and the sentence around each removed number reads as before. A number is removed with its brackets; the sentence it stood after stays and keeps its full stop. A reference to a decision that stays in the log (any number not listed below) is left as it is. A sentence of reason is one sentence, written from the *Rationale* of the withdrawn entry that the slice reads: it says why the rule is as it is, names no file, count or measurement the entry does not give, and is placed where the rule stands. Where a rule is only partly in the file, the missing sentence of the rule is added first, then its reason. Make no other change. These are the lines of the base; find a number by searching the file for it.
  Files:
  - `process-audit/SKILL.md` — remove WAY-332 (line 76); WAY-333 (line 197); WAY-335 (line 70); WAY-336 (line 38, 43); WAY-340 (line 67); WAY-341 (line 9, 28); WAY-346 (line 43); WAY-348 (line 58) · WAY-341 line 30, delete-line: Line 30 is only '(WAY-341).'; end line 29 with a full stop. · add one sentence of the reason of WAY-332 line 78, the end of the bullet 'The results lie outside every repository' (lines 76-78) · add one sentence of the reason of WAY-335 line 72, the end of the bullet 'Whether a fix works is read from the version, never from the date' (lines 70-72) · add one sentence of the reason of WAY-340 line 69, the end of the bullet 'No frozen earlier tasks are replayed ...' (lines 67-69) · add one sentence of the reason of WAY-341 line 9, after the clause 'in one session of its own, apart from any weekly review (WAY-341).'.
  - `process-audit/problem_register.md` — remove WAY-333 (line 67, 83); WAY-334 (line 18); WAY-335 (line 110); WAY-345 (line 23, 96) · add one sentence of the reason of WAY-333 line 67, after the sentence ending '... the problem is never given the nearest class instead (WAY-333).' in the paragraph 'The list widens' (lines 65-71) · add one sentence of the reason of WAY-334 line 18, after the sentence 'A problem that several stages of one cycle report is one problem: one row, which names every stage that reported it (WAY-334).' · add one sentence of the reason of WAY-345 line 98, after 'Adapt the meanings, never the levels.' (end of the section 'Costs of an occurrence', lines 96-98) · add one sentence of the reason of WAY-359 line 63, after the bullet 'A correction's pair `item · defect` ... take the pair `remark · defect` and the line `Defect introduced by:`.' (lines 61-63).
  - `process-audit/test_audit_count.py` — remove WAY-332 (line 674); WAY-333 (line 1715); WAY-334 (line 1715); WAY-335 (line 1715); WAY-336 (line 1715); WAY-341 (line 2456); WAY-347 (line 1451); WAY-348 (line 2785); WAY-349 (line 1451, 1638).
- **Change:** `process-audit/SKILL.md` · `process-audit/problem_register.md` · `process-audit/test_audit_count.py`
- **Read:** `.runs/task-cycles/decision-log-second-round/task.md:33-40` To do
  · `foundations/decisions.md:9771-9810` WAY-293
  · `foundations/decisions.md:11378-11398` WAY-332 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:11400-11424` WAY-333 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:11426-11444` WAY-334 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:11446-11465` WAY-335 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:11611-11629` WAY-340 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:11631-11651` WAY-341 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:11826-11860` WAY-345 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:12281-12316` WAY-359 (leaves the log in the foundation entries; read at the base ec7929d)
- **Model:** cheaper — a settled pattern carried into text
- **Risk:** none
- **Checks:** `python -B elements/common/foundation_check.py` — the lines it prints for the files of this slice's *Change*: none; the exit code stands at 1 until the last slice, from the lines of files of slices not yet made · `python -B gate/run_tests.py process-audit` · `python -B agent-instructions/skill_entry_points.py` (nothing to write: no frontmatter changes)
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

Your directory for working copies: `.runs/executor-9/`.

## Report

Write your full report to `.runs/task-cycles/decision-log-second-round/reports/executor-9-report.md` with: status (`done`, `done with concerns`, `questions`, `returned`, `blocked`), commits, each check with command and exit code, your own-work check (`make-change` section 3), the reasons you added (file and sentence, with the entry you wrote it from), entries you left under the "stay" rule above, **Unread material**, **Searches not found or unclear**, working copies and where they stood. Return the status, commits, one-line check result and the report path.

# Handoff to the executor of slice 13

You make slice 13 of the plan of one task cycle of the-way, as "a slice, or the retry of a slice" under `make-change`. The person who requested the cycle delegated intermediate choices to the orchestrator; nothing you write is anyone's approval. Work from the worktree root `the task's worktree` (branch `task/decision-log-second-round`). Commit your slice on that branch with `git add <path>` by path, an English commit message in the style of `git log --oneline`; never push; never run the product's gate (`python -B gate/run_tests.py` without a directory); change no file outside your slice's *Change*.

- Method: `task-cycle/change/SKILL.md` (`make-change`), whole, then `slice.md` beside it for how to read the plan and the task. Variant: "a slice, or the retry of a slice".
- Frozen task: `.runs/task-cycles/decision-log-second-round/task.md` (lines 1-490 are the task; Polish). Plan: `.runs/task-cycles/decision-log-second-round/plan.md` (your section is copied below, word for word, and holds).
- Answers of step 4: trust boundary no; irreversible operation no; no spec.

## What changed since the plan was written

The agent of the foundation entries has made its commits (`8d04d89`, `e643371`, `ece1f71`, `208f63c`, `5c10ee4`). The numbers a slice removes have left `foundations/decisions.md`. The plan's line ranges name lines of the base `ec7929d`, not of the log as it stands now: find an entry by its heading `### WAY-NN` in `foundations/decisions.md` as it stands (for an entry that stays or was changed), and for an entry that left the log by `git show ec7929d:foundations/decisions.md` (read the entry whole there). Where the plan's section and the log disagree, the log as it stands holds for what stays, and the base for what left.

**Ten entries stay in the log though the human's table lists them for withdrawal: WAY-93, WAY-94, WAY-97, WAY-263, WAY-287, WAY-294, WAY-295, WAY-297, WAY-363, WAY-364.** Where your section says to remove one of these numbers or to add a sentence of reason for it, do neither: leave the reference and the file as it is for that entry. (A number that stays is no error of the foundation check.) Group-D numbers (WAY-292, 317, 323, 347, 358, 369) went into WAY-288, 316, 309, 339, 357 (withdrawn) and 368: repoint as your section says.

Never invent a reason: a sentence of reason is written from the *Rationale* of the entry that left, read at the base. Where the entry's *Rationale* gives none, or the rule is not in the file and cannot be stated in a sentence, do not guess: state it in your report as a finding and leave the place unchanged.

## Your slice (copied word for word from the plan)

### Slice 13 — Guidelines: shared template, reading, audit, and the coding skill files

- **Goal:** Once made, no file of this slice names a number of a decision that left the log in the foundation entries (rows F4 and F5), each rule listed below stands in its file with one sentence of its reason, and the sentence around each removed number reads as before. A number is removed with its brackets; the sentence it stood after stays and keeps its full stop. A reference to a decision that stays in the log (any number not listed below) is left as it is. A sentence of reason is one sentence, written from the *Rationale* of the withdrawn entry that the slice reads: it says why the rule is as it is, names no file, count or measurement the entry does not give, and is placed where the rule stands. Where a rule is only partly in the file, the missing sentence of the rule is added first, then its reason. Make no other change. These are the lines of the base; find a number by searching the file for it.
  Files:
  - `product-guidelines/audit_end.md` — remove WAY-187 (line 153); WAY-281 (line 22); WAY-282 (line 49, 71, 88); WAY-283 (line 103); WAY-285 (line 110) · WAY-281 line 6, rewrite: Range names withdrawn entries; rewrite to cite only the numbers of the range that stay (WAY-280, and WAY-284 if kept) or drop the parenthesis. · WAY-282 line 6, rewrite: Range names withdrawn entries; rewrite to cite only the numbers of the range that stay (WAY-280, and WAY-284 if kept) or drop the parenthesis. · WAY-283 line 6, rewrite: Range names withdrawn entries; rewrite to cite only the numbers of the range that stay (WAY-280, and WAY-284 if kept) or drop the parenthesis. · WAY-285 line 6, rewrite: Range names withdrawn entries; rewrite to cite only the numbers of the range that stay (WAY-280, and WAY-284 if kept) or drop the parenthesis. · add one sentence of the reason of WAY-281 ## Merge into causes, after the paragraph ending at line 23 ('Tell each cause in one sentence of its effect on the user or the owner.') — and the file lacks part of the rule itself: audit_end.md lacks the sentence 'A reformatting of the code is no finding.' (log 9258); it stands in product-guidelines/coding/trial_run.md:24 'The formatter's count never enters the list: a reformatting is no finding.' The merge, one-cause-per-finding, place… (add that first) · add one sentence of the reason of WAY-282 ## Order, after the first paragraph (line 89) · add one sentence of the reason of WAY-283 ## The top of the list, after line 105 ('With fewer than three causes it holds all of them.') — and the file lacks part of the rule itself: audit_end.md does not say that the list of files marked `do not copy` stands apart from the limit (log 9342 'The list of files marked `do not copy` stands apart from this limit.'); it stands in product-guidelines/coding/kinds.md:18-19 'The `do not copy` list… (add that first) · add one sentence of the reason of WAY-285 ## Go back, after the first paragraph ending at line 111 ('...before the set of proposals is complete. A cause takes the form of the discipline that found it:') or after line 123 (Checked:….
  - `product-guidelines/reading.md` — remove WAY-183 (line 30); WAY-214 (line 4); WAY-217 (line 46); WAY-218 (line 4, 95) · WAY-200 line 88, rewrite: Say the comparison and exemplar selection of existing files go through maintain-coding-guidelines, which judges each file, compares and proposes the exemplar; drop 'under WAY-200'. · add one sentence of the reason of WAY-217 line 48 (end of the paragraph 'A current decision of the product's log that departs from a discipline's guidelines applies only ...').
  - `product-guidelines/template.md` — remove WAY-169 (line 112); WAY-170 (line 13, 72, 109); WAY-171 (line 39, 70, 72, 73, 75, 79, 97, 100, 123) · add one sentence of the reason of WAY-169 line 112 (end of the bullet '**A changed entry brings its rules along.**') · add one sentence of the reason of WAY-170 line 13 (end of the opening paragraph, after 'or holds as withdrawn (WAY-170).').
  - `product-guidelines/coding/SKILL.md` — remove WAY-200 (line 131); WAY-209 (line 131); WAY-210 (line 72); WAY-266 (line 100); WAY-277 (line 73) · add one sentence of the reason of WAY-210 line 70 ('... never a second linter beside it, and a way of writing log lines the product or its language already gives raises no question.') · add one sentence of the reason of WAY-266 line 100 (end of the section '## 0. Read'); the same sentence stands at styleguide/SKILL.md:74 and testing/SKILL.md:91.
  - `product-guidelines/coding/hand_back.md` — remove WAY-202 (line 8); WAY-279 (line 12).
  - `product-guidelines/coding/kinds.md` — remove WAY-200 (line 5); WAY-201 (line 5); WAY-281 (line 17) · WAY-200 line 8, rewrite: Say what the comparison is: judge every existing file of the kind, compare, propose the exemplar with copy / do not copy per file, the human approving the designating decision. · WAY-201 line 9, rewrite: Drop 'under WAY-201': the sentence ends 'and no audit' (SKILL.md:127-128 says the comparison, 'being no audit, has no such end'). · add one sentence of the reason of WAY-200 line 9, the sentence ending 'no audit' (the comparison of existing code); alternative: SKILL.md after line 132 ('A new kind' bullet), where the first-file half stands — and the file lacks part of the rule itself: kinds.md holds the comparison for a kind whose files exist (kinds.md:5-16: 'judge every file of it the product holds, compare them, and propose: its exemplar ... `do not copy` for each file ... and `copy` for every other file'). Missing in kinds.md: 'the exem… (add that first) · add one sentence of the reason of WAY-201 line 11 (end of the bullet 'its exemplar, with one sentence of what the product gains by it').
  - `product-guidelines/coding/new_tools.md` — remove WAY-210 (line 7); WAY-211 (line 7).
  - `product-guidelines/coding/recognize.md` — remove WAY-208 (line 4); WAY-209 (line 18); WAY-210 (line 15); WAY-278 (line 36); WAY-279 (line 36) · add one sentence of the reason of WAY-208 line 4 (the first bullet, '... however small (WAY-208).') · add one sentence of the reason of WAY-209 line 18 (the bullet 'no code: the starting set of step 2 ...') — and the file lacks part of the rule itself: First half stands: recognize.md:17-18 'no code: the starting set of step 2, so that the general file with its standing checks comes into being before the first task that writes the product's code'. Second half ('the file of a kind of code comes into being wit… (add that first) · add one sentence of the reason of WAY-278 line 36 (end of the bullet 'At a refresh, before step 2, look in `guidelines/coding.md` for the required headings ...').
  - `product-guidelines/coding/research.md` — remove WAY-211 (line 15).
  - `product-guidelines/coding/starting_set.md` — remove WAY-209 (line 4); WAY-210 (line 4); WAY-211 (line 4, 9) · add one sentence of the reason of WAY-211 line 13 (end of the bullet about research at the first guidelines and at every extension; 'At a refresh, do no research ...').
  - Beside the files: WAY-312 stays in the log and its first sentence (a rule of guidelines lists no state and repeats no decision or value) leaves for `product-guidelines/template.md`, which already states it near the bullet that opens "A rule lists no state and repeats no decision or value"; check that the bullet carries one sentence of its reason, and add it from the *Rationale* of WAY-312 where it does not. Do not remove the references to WAY-312 and WAY-274 there: both entries stay.
- **Change:** `product-guidelines/audit_end.md` · `product-guidelines/reading.md` · `product-guidelines/template.md` · `product-guidelines/coding/SKILL.md` · `product-guidelines/coding/hand_back.md` · `product-guidelines/coding/kinds.md` · `product-guidelines/coding/new_tools.md` · `product-guidelines/coding/recognize.md` · `product-guidelines/coding/research.md` · `product-guidelines/coding/starting_set.md`
- **Read:** `.runs/task-cycles/decision-log-second-round/task.md:33-40` To do
  · `foundations/decisions.md:9771-9810` WAY-293
  · `foundations/decisions.md:5426-5453` WAY-169 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:5455-5486` WAY-170 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:6144-6171` WAY-200 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:6173-6197` WAY-201 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:6464-6487` WAY-208 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:6489-6514` WAY-209 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:6516-6554` WAY-210 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:6556-6588` WAY-211 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:6828-6848` WAY-217 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:8561-8585` WAY-266 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:9136-9166` WAY-278 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:9252-9285` WAY-281 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:9287-9334` WAY-282 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:9336-9366` WAY-283 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:9404-9434` WAY-285 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:10548-10604` WAY-312 (stays in the log; its first sentence leaves it in row F7)
- **Model:** cheaper — a settled pattern carried into text
- **Risk:** none
- **Checks:** `python -B elements/common/foundation_check.py` — the lines it prints for the files of this slice's *Change*: none; the exit code stands at 1 until the last slice, from the lines of files of slices not yet made · `python -B agent-instructions/skill_entry_points.py` (nothing to write: no frontmatter changes)
- **Depends on:** rows F4 · F5 · F7 of the foundation entries

## Added by the orchestrator for this slice (from the foundation entries' turn 3)

`product-guidelines/template.md` must also gain the first sentence of the former WAY-312, which the log no longer holds as binding text, with one sentence of its reason: add "A rule lists no state of the product's code or of the product and repeats neither a decision of the product's log nor a value taken from a configuration file, so that what remains is what the author of the code is to do." and, in one sentence, its reason: a sentence that lists what the code or the product is today goes stale, and a sentence that repeats a decision or a configuration value is a second copy that drifts. Place them where the template says what a rule holds. The rest of the former WAY-312 (the ban on rewriting known practices and the audit steps) stays a decision of the log.

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

Your directory for working copies: `.runs/executor-13/`.

## Report

Write your full report to `.runs/task-cycles/decision-log-second-round/reports/executor-13-report.md` with: status (`done`, `done with concerns`, `questions`, `returned`, `blocked`), commits, each check with command and exit code, your own-work check (`make-change` section 3), the reasons you added (file and sentence, with the entry you wrote it from), entries you left under the "stay" rule above, **Unread material**, **Searches not found or unclear**, working copies and where they stood. Return the status, commits, one-line check result and the report path.

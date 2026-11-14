# Handoff to the executor of slice 15

You make slice 15 of the plan of one task cycle of the-way, as "a slice, or the retry of a slice" under `make-change`. The person who requested the cycle delegated intermediate choices to the orchestrator; nothing you write is anyone's approval. Work from the worktree root `the task's worktree` (branch `task/decision-log-second-round`). Commit your slice on that branch with `git add <path>` by path, an English commit message in the style of `git log --oneline`; never push; never run the product's gate (`python -B gate/run_tests.py` without a directory); change no file outside your slice's *Change*.

- Method: `task-cycle/change/SKILL.md` (`make-change`), whole, then `slice.md` beside it for how to read the plan and the task. Variant: "a slice, or the retry of a slice".
- Frozen task: `.runs/task-cycles/decision-log-second-round/task.md` (lines 1-490 are the task; Polish). Plan: `.runs/task-cycles/decision-log-second-round/plan.md` (your section is copied below, word for word, and holds).
- Answers of step 4: trust boundary no; irreversible operation no; no spec.

## What changed since the plan was written

The agent of the foundation entries has made its commits (`8d04d89`, `e643371`, `ece1f71`, `208f63c`, `5c10ee4`). The numbers a slice removes have left `foundations/decisions.md`. The plan's line ranges name lines of the base `ec7929d`, not of the log as it stands now: find an entry by its heading `### WAY-NN` in `foundations/decisions.md` as it stands (for an entry that stays or was changed), and for an entry that left the log by `git show ec7929d:foundations/decisions.md` (read the entry whole there). Where the plan's section and the log disagree, the log as it stands holds for what stays, and the base for what left.

**Ten entries stay in the log though the human's table lists them for withdrawal: WAY-93, WAY-94, WAY-97, WAY-263, WAY-287, WAY-294, WAY-295, WAY-297, WAY-363, WAY-364.** Where your section says to remove one of these numbers or to add a sentence of reason for it, do neither: leave the reference and the file as it is for that entry. (A number that stays is no error of the foundation check.) Group-D numbers (WAY-292, 317, 323, 347, 358, 369) went into WAY-288, 316, 309, 339, 357 (withdrawn) and 368: repoint as your section says.

Never invent a reason: a sentence of reason is written from the *Rationale* of the entry that left, read at the base. Where the entry's *Rationale* gives none, or the rule is not in the file and cannot be stated in a sentence, do not guess: state it in your report as a finding and leave the place unchanged.

## Your slice (copied word for word from the plan)

### Slice 15 — Guidelines: the styleguide

- **Goal:** Once made, no file of this slice names a number of a decision that left the log in the foundation entries (rows F4 and F5), each rule listed below stands in its file with one sentence of its reason, and the sentence around each removed number reads as before. A number is removed with its brackets; the sentence it stood after stays and keeps its full stop. A reference to a decision that stays in the log (any number not listed below) is left as it is. A sentence of reason is one sentence, written from the *Rationale* of the withdrawn entry that the slice reads: it says why the rule is as it is, names no file, count or measurement the entry does not give, and is placed where the rule stands. Where a rule is only partly in the file, the missing sentence of the rule is added first, then its reason. Make no other change. These are the lines of the base; find a number by searching the file for it.
  Files:
  - `product-guidelines/styleguide/SKILL.md` — remove WAY-266 (line 74).
  - `product-guidelines/styleguide/audit.md` — remove WAY-185 (line 19); WAY-187 (line 3) · add one sentence of the reason of WAY-187 line 9 (end of the bullet 'Audit in both directions', 7-9) and after line 15 (the running-product fallback, 12-15).
  - `product-guidelines/styleguide/new_tools.md` — remove WAY-185 (line 7); WAY-186 (line 7).
  - `product-guidelines/styleguide/recognize.md` — remove WAY-183 (line 4); WAY-185 (line 17, 22) · add one sentence of the reason of WAY-183 line 7 (end of the first bullet, after 'an admin panel added to a backend included') · add one sentence of the reason of WAY-185 line 22, end of the bullet 'Extend what exists.' (21-22).
  - `product-guidelines/styleguide/research.md` — remove WAY-186 (line 16).
  - `product-guidelines/styleguide/settle.md` — remove WAY-80 (line 16); WAY-86 (line 12); WAY-191 (line 16, 18, 25) · WAY-80 line 18, rewrite: 'with its source as WAY-80 gives it' -> 'with its source in the form the environment-facts template gives (section Source)'; keep (WAY-191). · WAY-189 line 29, rewrite: Drop 'WAY-189 gives': 'the three first invariants, each with its test in the product's suite: no value ... , visible focus ..., and contrast ...' (list already on lines 29-31). · add one sentence of the reason of WAY-191 line 18, end of the 'Accessibility' bullet (11-18).
  - `product-guidelines/styleguide/starting_rules.md` — remove WAY-184 (line 4, 17); WAY-186 (line 4, 8) · add one sentence of the reason of WAY-184 line 4-5, the opening sentence 'For the first styleguide, with or without screens, and at every refresh or extension' (state the timing there) or line 17 (the width bullet) — and the file lacks part of the rule itself: The timing sentence is not stated as a rule in starting_rules.md or recognize.md: "the styleguide of a user interface comes into being before that user interface's first screen". Only SKILL.md:3 (description: 'created before its first screen') and recognize.m… (add that first) · add one sentence of the reason of WAY-186 line 12 (end of the research bullet, 10-12) or line 9 (preferences bullet, 6-9).
  - `product-guidelines/styleguide/task_document.md` — remove WAY-182 (line 8); WAY-192 (line 17) · add one sentence of the reason of WAY-192 line 17, end of the 'apply `maintain-instruction-files` for two changes' bullet (11-17).
  - `product-guidelines/styleguide/template.md` — remove WAY-169 (line 162); WAY-170 (line 20, 99); WAY-171 (line 22, 60, 65, 68, 89, 150, 167, 181); WAY-176 (line 78, 89, 92, 97, 150, 157, 161, 181); WAY-177 (line 121, 151); WAY-178 (line 128); WAY-180 (line 138, 151); WAY-182 (line 133, 180); WAY-183 (line 8); WAY-189 (line 94, 101, 105, 107, 111, 113, 116); WAY-191 (line 107, 111, 116); WAY-192 (line 70) · add one sentence of the reason of WAY-176 bullet '**`## Roles`**' (line 78) and its sub-bullets *Role* (79-80) / *Text on it* (84-85), or the rule bullet 'Every background with its text' (95-97) · add one sentence of the reason of WAY-177 line 123, end of bullet 'States of shared controls' (117-123) · add one sentence of the reason of WAY-178 line 128-130, end of bullet 'A fault of one screen is fixed in its component' (124-130) · add one sentence of the reason of WAY-180 line 141, end of bullet 'The kitchen-sink page' (136-141) · add one sentence of the reason of WAY-182 line 135, end of bullet 'Every value with its source' (131-135).
- **Change:** `product-guidelines/styleguide/SKILL.md` · `product-guidelines/styleguide/audit.md` · `product-guidelines/styleguide/new_tools.md` · `product-guidelines/styleguide/recognize.md` · `product-guidelines/styleguide/research.md` · `product-guidelines/styleguide/settle.md` · `product-guidelines/styleguide/starting_rules.md` · `product-guidelines/styleguide/task_document.md` · `product-guidelines/styleguide/template.md`
- **Read:** `.runs/task-cycles/decision-log-second-round/task.md:33-40` To do
  · `foundations/decisions.md:9771-9810` WAY-293
  · `foundations/decisions.md:1994-2054` WAY-80 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:5682-5714` WAY-176 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:5716-5739` WAY-177 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:5741-5762` WAY-178 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:5764-5785` WAY-180 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:5787-5809` WAY-182 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:5811-5830` WAY-183 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:5832-5854` WAY-184 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:5856-5894` WAY-185 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:5896-5937` WAY-186 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:5939-5971` WAY-187 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:5973-6003` WAY-189 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:6005-6037` WAY-191 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:6039-6075` WAY-192 (leaves the log in the foundation entries; read at the base ec7929d)
- **Model:** cheaper — a settled pattern carried into text
- **Risk:** none
- **Checks:** `python -B elements/common/foundation_check.py` — the lines it prints for the files of this slice's *Change*: none; the exit code stands at 1 until the last slice, from the lines of files of slices not yet made · `python -B agent-instructions/skill_entry_points.py` (nothing to write: no frontmatter changes)
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

Your directory for working copies: `.runs/executor-15/`.

## Report

Write your full report to `.runs/task-cycles/decision-log-second-round/reports/executor-15-report.md` with: status (`done`, `done with concerns`, `questions`, `returned`, `blocked`), commits, each check with command and exit code, your own-work check (`make-change` section 3), the reasons you added (file and sentence, with the entry you wrote it from), entries you left under the "stay" rule above, **Unread material**, **Searches not found or unclear**, working copies and where they stood. Return the status, commits, one-line check result and the report path.

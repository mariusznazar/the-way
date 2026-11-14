# Handoff to the executor of slice 17

You make slice 17 of the plan of one task cycle of the-way, as "a slice, or the retry of a slice" under `make-change`. The person who requested the cycle delegated intermediate choices to the orchestrator; nothing you write is anyone's approval. Work from the worktree root `the task's worktree` (branch `task/decision-log-second-round`). Commit your slice on that branch with `git add <path>` by path, an English commit message in the style of `git log --oneline`; never push; never run the product's gate (`python -B gate/run_tests.py` without a directory); change no file outside your slice's *Change*.

- Method: `task-cycle/change/SKILL.md` (`make-change`), whole, then `slice.md` beside it for how to read the plan and the task. Variant: "a slice, or the retry of a slice".
- Frozen task: `.runs/task-cycles/decision-log-second-round/task.md` (lines 1-490 are the task; Polish). Plan: `.runs/task-cycles/decision-log-second-round/plan.md` (your section is copied below, word for word, and holds).
- Answers of step 4: trust boundary no; irreversible operation no; no spec.

## What changed since the plan was written

The agent of the foundation entries has made its commits (`8d04d89`, `e643371`, `ece1f71`, `208f63c`, `5c10ee4`). The numbers a slice removes have left `foundations/decisions.md`. The plan's line ranges name lines of the base `ec7929d`, not of the log as it stands now: find an entry by its heading `### WAY-NN` in `foundations/decisions.md` as it stands (for an entry that stays or was changed), and for an entry that left the log by `git show ec7929d:foundations/decisions.md` (read the entry whole there). Where the plan's section and the log disagree, the log as it stands holds for what stays, and the base for what left.

**Ten entries stay in the log though the human's table lists them for withdrawal: WAY-93, WAY-94, WAY-97, WAY-263, WAY-287, WAY-294, WAY-295, WAY-297, WAY-363, WAY-364.** Where your section says to remove one of these numbers or to add a sentence of reason for it, do neither: leave the reference and the file as it is for that entry. (A number that stays is no error of the foundation check.) Group-D numbers (WAY-292, 317, 323, 347, 358, 369) went into WAY-288, 316, 309, 339, 357 (withdrawn) and 368: repoint as your section says.

Never invent a reason: a sentence of reason is written from the *Rationale* of the entry that left, read at the base. Where the entry's *Rationale* gives none, or the rule is not in the file and cannot be stated in a sentence, do not guess: state it in your report as a finding and leave the place unchanged.

## Your slice (copied word for word from the plan)

### Slice 17 — Project level: definition, task and plan templates, the task line

- **Goal:** Once made, no file of this slice names a number of a decision that left the log in the foundation entries (rows F4 and F5), each rule listed below stands in its file with one sentence of its reason, and the sentence around each removed number reads as before. A number is removed with its brackets; the sentence it stood after stays and keeps its full stop. A reference to a decision that stays in the log (any number not listed below) is left as it is. A sentence of reason is one sentence, written from the *Rationale* of the withdrawn entry that the slice reads: it says why the rule is as it is, names no file, count or measurement the entry does not give, and is placed where the rule stands. Where a rule is only partly in the file, the missing sentence of the rule is added first, then its reason. Make no other change. These are the lines of the base; find a number by searching the file for it.
  Files:
  - `project-level/definition_template.md` — remove WAY-108 (line 36, 75, 92, 127, 204, 226); WAY-109 (line 114, 118); WAY-110 (line 122); WAY-112 (line 216); WAY-115 (line 326, 329); WAY-116 (line 277); WAY-117 (line 359) · WAY-72 line 35, rewrite: Brackets '(WAY-72 for the entries; WAY-108)' (lines 35-36) lean on the number for 'for the entries': keep '(WAY-108)' only, or say in words that the entries are English by rules.md 'Language'. · WAY-108 line 85, delete-line: Line is only 'WAY-108.' after the status table. · WAY-108 line 110, delete-line: Line is only 'WAY-108.' after the section table. · add one sentence of the reason of WAY-108 the paragraph 'The text of the definition, its title included, is in the language the human opened the conversation in...' (lines 33-36, section 'Where it stands, and in what language'); th… · add one sentence of the reason of WAY-109 the bullet '**Background, Success and Risks** hold what the human answered...' (lines 112-114); a second sentence may follow the '**A frame of success**' bullet (lines 115-118) · add one sentence of the reason of WAY-110 the bullet '**A deadline** appears under "Inputs and constraints" only when the human names one...' (lines 119-122) · add one sentence of the reason of WAY-116 the first paragraph of 'Projected foundation changes' (lines 274-277, '... whose every field is known before the code (WAY-116).') — and the file lacks part of the rule itself: Missing: 'and environment facts only where a projected decision or invariant rests on them' (decisions.md:2964-2966). Template 274-276 lists 'environment facts' with no condition; only elements/common/skill/definition_variant.md:25 says 'a fact a settlement r… (add that first).
  - `project-level/task_line.md` — remove WAY-329 (line 36).
  - `project-level/task/template.md` — remove WAY-115 (line 202); WAY-353 (line 239); WAY-356 (line 103) · add one sentence of the reason of WAY-353 the paragraph 'Where the document points at a place to change in a file...' (lines 236-241, ending 'which say which text the line meant.') · add one sentence of the reason of WAY-356 the sentence ending 'a missing line means that the task was not assessed, never `none`.' (lines 112-113) — and the file lacks part of the rule itself: Missing in the task files: 'and a problem of the class `defect-found-after-merge` in the register of problems, which counts it' (decisions.md:12173-12174). That half stands in process-audit/problem_register.md:53 and :123-129, not in template.md or draft.md. (add that first).
  - `project-level/plan/template.md` — remove WAY-156 (line 115).
- **Change:** `project-level/definition_template.md` · `project-level/task_line.md` · `project-level/task/template.md` · `project-level/plan/template.md`
- **Read:** `.runs/task-cycles/decision-log-second-round/task.md:33-40` To do
  · `foundations/decisions.md:9771-9810` WAY-293
  · `foundations/decisions.md:1867-1888` WAY-72 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:2700-2726` WAY-108 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:2728-2746` WAY-109 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:2748-2767` WAY-110 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:2962-2984` WAY-116 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:12069-12099` WAY-353 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:12171-12209` WAY-356 (leaves the log in the foundation entries; read at the base ec7929d)
- **Model:** cheaper — a settled pattern carried into text
- **Risk:** none
- **Checks:** `python -B elements/common/foundation_check.py` — the lines it prints for the files of this slice's *Change*: none; the exit code stands at 1 until the last slice, from the lines of files of slices not yet made · `python -B gate/run_tests.py project-level`
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

Your directory for working copies: `.runs/executor-17/`.

## Report

Write your full report to `.runs/task-cycles/decision-log-second-round/reports/executor-17-report.md` with: status (`done`, `done with concerns`, `questions`, `returned`, `blocked`), commits, each check with command and exit code, your own-work check (`make-change` section 3), the reasons you added (file and sentence, with the entry you wrote it from), entries you left under the "stay" rule above, **Unread material**, **Searches not found or unclear**, working copies and where they stood. Return the status, commits, one-line check result and the report path.

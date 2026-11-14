# Handoff to the executor of slice 19

You make slice 19 of the plan of one task cycle of the-way, as "a slice, or the retry of a slice" under `make-change`. The person who requested the cycle delegated intermediate choices to the orchestrator; nothing you write is anyone's approval. Work from the worktree root `the task's worktree` (branch `task/decision-log-second-round`). Commit your slice on that branch with `git add <path>` by path, an English commit message in the style of `git log --oneline`; never push; never run the product's gate (`python -B gate/run_tests.py` without a directory); change no file outside your slice's *Change*.

- Method: `task-cycle/change/SKILL.md` (`make-change`), whole, then `slice.md` beside it for how to read the plan and the task. Variant: "a slice, or the retry of a slice".
- Frozen task: `.runs/task-cycles/decision-log-second-round/task.md` (lines 1-490 are the task; Polish). Plan: `.runs/task-cycles/decision-log-second-round/plan.md` (your section is copied below, word for word, and holds).
- Answers of step 4: trust boundary no; irreversible operation no; no spec.

## What changed since the plan was written

The agent of the foundation entries has made its commits (`8d04d89`, `e643371`, `ece1f71`, `208f63c`, `5c10ee4`). The numbers a slice removes have left `foundations/decisions.md`. The plan's line ranges name lines of the base `ec7929d`, not of the log as it stands now: find an entry by its heading `### WAY-NN` in `foundations/decisions.md` as it stands (for an entry that stays or was changed), and for an entry that left the log by `git show ec7929d:foundations/decisions.md` (read the entry whole there). Where the plan's section and the log disagree, the log as it stands holds for what stays, and the base for what left.

**Ten entries stay in the log though the human's table lists them for withdrawal: WAY-93, WAY-94, WAY-97, WAY-263, WAY-287, WAY-294, WAY-295, WAY-297, WAY-363, WAY-364.** Where your section says to remove one of these numbers or to add a sentence of reason for it, do neither: leave the reference and the file as it is for that entry. (A number that stays is no error of the foundation check.) Group-D numbers (WAY-292, 317, 323, 347, 358, 369) went into WAY-288, 316, 309, 339, 357 (withdrawn) and 368: repoint as your section says.

Never invent a reason: a sentence of reason is written from the *Rationale* of the entry that left, read at the base. Where the entry's *Rationale* gives none, or the rule is not in the file and cannot be stated in a sentence, do not guess: state it in your report as a finding and leave the place unchanged.

## Your slice (copied word for word from the plan)

### Slice 19 — Project level: plan reading and the project skill

- **Goal:** Once made, no file of this slice names a number of a decision that left the log in the foundation entries (rows F4 and F5), each rule listed below stands in its file with one sentence of its reason, and the sentence around each removed number reads as before. A number is removed with its brackets; the sentence it stood after stays and keeps its full stop. A reference to a decision that stays in the log (any number not listed below) is left as it is. A sentence of reason is one sentence, written from the *Rationale* of the withdrawn entry that the slice reads: it says why the rule is as it is, names no file, count or measurement the entry does not give, and is placed where the rule stands. Where a rule is only partly in the file, the missing sentence of the rule is added first, then its reason. Make no other change. These are the lines of the base; find a number by searching the file for it.
  Files:
  - `project-level/plan/skill/read.md` — remove WAY-151 (line 6); WAY-218 (line 13).
  - `project-level/plan/skill/reading_definition_and_plan.md` — remove WAY-151 (line 4) · add one sentence of the reason of WAY-151 the first paragraph (lines 3-4, 'The original definition and plan remain authoritative, and every check runs on them whole ...').
  - `project-level/skill/SKILL.md` — remove WAY-112 (line 36, 39); WAY-156 (line 29).
  - `project-level/skill/delegated_mode.md` — remove WAY-156 (line 8).
  - `project-level/skill/first_write.md` — remove WAY-112 (line 11).
  - `project-level/skill/idea.md` — add one sentence of the reason of WAY-112 the third bullet (lines 8-9, 'Give back your understanding ... and wait for the human to confirm or correct it.').
  - `project-level/skill/read_foundation.md` — remove WAY-111 (line 7) · add one sentence of the reason of WAY-111 the first bullet (lines 5-7, 'Select and read the product's current foundation ... before a diff exists (WAY-111, WAY-150).').
  - `project-level/skill/rounds.md` — remove WAY-112 (line 9).
- **Change:** `project-level/plan/skill/read.md` · `project-level/plan/skill/reading_definition_and_plan.md` · `project-level/skill/SKILL.md` · `project-level/skill/delegated_mode.md` · `project-level/skill/first_write.md` · `project-level/skill/idea.md` · `project-level/skill/read_foundation.md` · `project-level/skill/rounds.md`
- **Read:** `.runs/task-cycles/decision-log-second-round/task.md:33-40` To do
  · `foundations/decisions.md:9771-9810` WAY-293
  · `foundations/decisions.md:2769-2794` WAY-111 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:2796-2821` WAY-112 (leaves the log in the foundation entries; read at the base ec7929d)
  · `foundations/decisions.md:4587-4619` WAY-151 (leaves the log in the foundation entries; read at the base ec7929d)
- **Model:** cheaper — a settled pattern carried into text
- **Risk:** none
- **Checks:** `python -B elements/common/foundation_check.py` — the lines it prints for the files of this slice's *Change*: none; the exit code stands at 1 until the last slice, from the lines of files of slices not yet made · `python -B gate/run_tests.py project-level` · `python -B agent-instructions/skill_entry_points.py` (nothing to write: no frontmatter changes)
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

Your directory for working copies: `.runs/executor-19/`.

## Report

Write your full report to `.runs/task-cycles/decision-log-second-round/reports/executor-19-report.md` with: status (`done`, `done with concerns`, `questions`, `returned`, `blocked`), commits, each check with command and exit code, your own-work check (`make-change` section 3), the reasons you added (file and sentence, with the entry you wrote it from), entries you left under the "stay" rule above, **Unread material**, **Searches not found or unclear**, working copies and where they stood. Return the status, commits, one-line check result and the report path.

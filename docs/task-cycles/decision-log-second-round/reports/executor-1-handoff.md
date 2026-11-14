# Handoff to the executor of slice 1

You make slice 1 of the plan of one task cycle of the-way, as "a slice, or the retry of a slice" under `make-change`. The person who requested the cycle delegated intermediate choices to the orchestrator; nothing you write is anyone's approval. Work from the worktree root `the task's worktree` (branch `task/decision-log-second-round`). Commit your slice on that branch with `git add <path>` by path, an English commit message in the style of `git log --oneline`; never push; never run the product's gate (`python -B gate/run_tests.py` without a directory); change no file outside your slice's *Change*.

- Method: `task-cycle/change/SKILL.md` (`make-change`), whole, then `slice.md` beside it for how to read the plan and the task. Variant: "a slice, or the retry of a slice".
- Frozen task: `.runs/task-cycles/decision-log-second-round/task.md` (lines 1-490 are the task; Polish). Plan: `.runs/task-cycles/decision-log-second-round/plan.md` (your section is copied below, word for word, and holds).
- Answers of step 4: trust boundary no; irreversible operation no; no spec.

## What changed since the plan was written

The agent of the foundation entries has made its commits (`8d04d89`, `e643371`, `ece1f71`, `208f63c`, `5c10ee4`). The numbers a slice removes have left `foundations/decisions.md`. The plan's line ranges name lines of the base `ec7929d`, not of the log as it stands now: find an entry by its heading `### WAY-NN` in `foundations/decisions.md` as it stands (for an entry that stays or was changed), and for an entry that left the log by `git show ec7929d:foundations/decisions.md` (read the entry whole there). Where the plan's section and the log disagree, the log as it stands holds for what stays, and the base for what left.

**Ten entries stay in the log though the human's table lists them for withdrawal: WAY-93, WAY-94, WAY-97, WAY-263, WAY-287, WAY-294, WAY-295, WAY-297, WAY-363, WAY-364.** Where your section says to remove one of these numbers or to add a sentence of reason for it, do neither: leave the reference and the file as it is for that entry. (A number that stays is no error of the foundation check.) Group-D numbers (WAY-292, 317, 323, 347, 358, 369) went into WAY-288, 316, 309, 339, 357 (withdrawn) and 368: repoint as your section says.

Never invent a reason: a sentence of reason is written from the *Rationale* of the entry that left, read at the base. Where the entry's *Rationale* gives none, or the rule is not in the file and cannot be stated in a sentence, do not guess: state it in your report as a finding and leave the place unchanged.

## Your slice (copied word for word from the plan)

### Slice 1 — Decisions template: the pointer to WAY-100 and the sources of a recovered decision; the reading skill points to it

- **Goal:** Once made: (a) in `elements/decisions/template.md`, the bullet that opens "The question names a choice someone could answer otherwise" points to WAY-100 for how a decision that adopts a practice from outside names it, and copies no wording of that rule (the rule stands in WAY-100 as row F1 leaves it; WAY-35); (b) the section "Recovered decisions" of the same template says that the description of the commit, or of the merged request, that brought the shape of the code is a source an agent quotes with the identifier of the commit, and that the agent looks there before it writes `unknown` (WAY-29 as row F2 leaves it); (c) the rule of the closed list of two relation types, whose number WAY-32 leaves the log, stands in the template with one sentence of its reason and the number is removed; (d) in `elements/common/skill/read.md`, the bullet that opens "Read in each element template what makes something an entry of it" also sends the reader to that rule of the decisions template, with the one fact that a list of what is taken from sources is no candidate for a decision, and holds no wording of the rule of its own. Make no other change.
  Files:
  - `elements/decisions/template.md` — remove WAY-32 (line 207) · add one sentence of the reason of WAY-32 line 207, end of the first bullet of 'Relations and precedence' (the bullet ending '(WAY-32).').
  - `elements/common/skill/read.md` — as the goal says.
- **Change:** `elements/decisions/template.md` · `elements/common/skill/read.md`
- **Read:** `.runs/task-cycles/decision-log-second-round/task.md:33-40` To do
  · `.runs/task-cycles/decision-log-second-round/task.md:429-433` Questions to settle, question 2 (answer a)
  · `foundations/decisions.md:2466-2488` WAY-100 (as row F1 leaves it)
  · `foundations/decisions.md:908-941` WAY-29 (as row F2 leaves it)
  · `foundations/decisions.md:641-667` WAY-19
  · `foundations/decisions.md:9771-9810` WAY-293
  · `foundations/decisions.md:981-1000` WAY-32 (leaves the log in the foundation entries; read at the base ec7929d)
- **Model:** same — the wording of the rule is read by every product that writes a decision
- **Risk:** none
- **Checks:** `python -B elements/common/foundation_check.py` — the lines it prints for the files of this slice: none (the lines for the files of slices not yet made stand) · `python -B gate/run_tests.py elements/common` · `python -B gate/run_tests.py elements/part-map`
- **Depends on:** Foundation entries rows F1 and F2 (the addition to WAY-100 and the changed WAY-29)

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

Your directory for working copies: `.runs/executor-1/`.

## Report

Write your full report to `.runs/task-cycles/decision-log-second-round/reports/executor-1-report.md` with: status (`done`, `done with concerns`, `questions`, `returned`, `blocked`), commits, each check with command and exit code, your own-work check (`make-change` section 3), the reasons you added (file and sentence, with the entry you wrote it from), entries you left under the "stay" rule above, **Unread material**, **Searches not found or unclear**, working copies and where they stood. Return the status, commits, one-line check result and the report path.

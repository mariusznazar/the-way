# Handoff — review of the whole change — decisions-log-after-foundation-review

## Delegation

The human who requested this cycle delegated every intermediate choice to the orchestrator; you ask
no human. You review as an agent that did not make the change. You alone grade and scope your
findings.

## What you review

- Variant of `review-change`: **the whole change**. Method: `task-cycle/review/SKILL.md` in the worktree, read whole; then `whole_change.md` beside it, as that file's section 1 gives, and the other files only when the step that names them comes.
- Worktree (read-only; work from its root): `the task's worktree`, branch `task/decisions-log-after-foundation-review`.
- Range: base `0dae56b` to head `dfe14f7` (six commits: `ffa9a44`, `b58ff96`, `a9384de`, `63ed3e4`, `3020643`, `dfe14f7`). Compute the diff yourself.
- Route: one author without a plan; no spec; no slices; so the whole range is judged by you only.
- Frozen task, read whole: `.runs/task-cycles/decisions-log-after-foundation-review/task.md` (accepted 2026-11-15; *To do* 1–19, *Questions to settle*, *Settlements to record* rows 1–11, *Decisions in play*).
- Author's report (claims to verify, not evidence): `.runs/task-cycles/decisions-log-after-foundation-review/reports/author-report.md`.
- The author returned `done with concerns`. Its concerns, which you judge:
  1. WAY-140 (item 19.6): the author wrote a clause into the first **binding sentence** of WAY-140 ("nor is the removal of the repository's own working directories that stand outside its directory (WAY-375)") where the item asked for a pointer to WAY-375 and says no item of 19 changes what an entry binds. Judge whether this is a change of what the entry binds, what the frozen task allows, and whether the pointer could have been given without it.
  2. Item 19.19 (part map, `product-guidelines`): the author found the sentence already correct at the base and made no change. Verify.
  3. `claude-code-imports` (item 12): the author added a passage about `CLAUDE.md` files in the hierarchy above the working directory loading at launch, with a source passage from § Choose where to put CLAUDE.md files.
  4. Three new facts for WAY-255 (item 15), one with no archived copy; and the archived copies chosen for the other facts.
  5. WAY-363's *Rationale* still says "the same chance in the grade …" (item 14 names *Rejected* only).
  6. The sentence "the audit of the process shows what the version after the change costs" in WAY-229's *Rationale*, for which the author found no decision holding that fact.
  7. WAY-229's *Rejected* was widened with ways the row's source keeps; WAY-229's last sentence now says every other reviewer works on no class cheaper than the orchestrator's.
- Trust boundary: no. Operation that cannot be undone: no. Class of your review: the strongest available; the cycle has decided that.

## What to check especially

- Every item of *To do* 1–19 and each row 1–11 of *Settlements to record*, against the diff, for completeness and for the meaning the source gives; for an item the author calls already true, verify it.
- WAY-05's limits on each entry the change rewrites: one to three binding sentences per paragraph, no file, script or count in the author-written *Rationale*/*Rejected* of a decision, and the rest of WAY-05 as the entry gives it. The author states it did not open WAY-05, WAY-09, WAY-52, WAY-173, WAY-25, WAY-36, WAY-71, WAY-114, WAY-134, WAY-135 and WAY-136 whole; you open those you need for your judgment.
- WAY-229: "the strongest class available" with one meaning in the whole entry; no model name and no tool-setting name introduced; the two reviews run on it; `task-cycle/skill/SKILL.md` at the two places the task names; any other place in the repository that states the class of a review (search it yourself).
- Items that only rewrap lines (19.x "przewinąć"): compare by words — a rewrap changes no word. A word-level comparison of the old and the new text (for instance `git diff --word-diff` or a small script in your own directory under `.runs/`) is the evidence.
- Environment facts (items 11, 12, 15, 19.21, 19.22): every quoted fragment stands word for word in the page it cites, as the page reads today (read the page; copy nothing from memory), and the facts' dependants (WAY-85, 127, 129, 132, 141, 255 and the invariant `installation-claude-guidance`) still read true against them.
- The renamed invariant `elements-pending-marker`: no use of the old identifier is left anywhere (`git grep` over tracked files), and the test citing it is unchanged except the citation and docstring.
- That nothing outside the task's items was changed (compare the file list with the items).
- You run no full gate (the orchestrator's run); run `python -B elements/common/foundation_check.py` and the focused tests of the directories you consider at risk.

## Your directory and report

- Your directory for working copies: `.runs/review-whole/` directly under `.runs/` of the worktree.
- Report path: `.runs/task-cycles/decisions-log-after-foundation-review/reports/review-whole-report.md`; its first line `PASS <sha>` or `FAIL <sha>`, the sha being the reviewed head. Minor findings the change itself makes within the task are listed as `review-change` gives, so that the orchestrator can send them to a fix.

## Working copies (word for word from `task-cycle/skill/SKILL.md`)

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed,
except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
says, to the place the product's foundation settles for screenshots, and into the agent's directory
only where no such place is settled. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
`git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed.

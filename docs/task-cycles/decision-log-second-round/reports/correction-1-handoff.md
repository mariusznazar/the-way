# Handoff to the agent of correction 1

You make "a correction for the human's remarks" under `make-change` for one task cycle of the-way, on the open request #126. Work from the worktree root `the task's worktree` (branch `task/decision-log-second-round`, head `f080288`; the code the request carries is `9c24d0d`, the commit `7ec7c54` and its removal `f080288` hold only the record). Commit by path (`git add <path>`), an English message, never push, never run the product's whole gate (`python -B gate/run_tests.py` without a directory).

- Method: `task-cycle/change/SKILL.md` whole (the row "a correction for the human's remarks": the human's remarks bind; the report holds each remark as made, and how).
- The human's remarks, word for word: `.runs/task-cycles/decision-log-second-round/reports/correction-1-remarks.md`. The part you make is exactly two things; the rest of the remarks (let through items 1 and 12; one task for items 4-11) is the orchestrator's and changes no file of yours:
  1. **Put back the entry WAY-202** ("Which standing checks must a product's coding guidelines settle, and from when do they bind?") into `foundations/decisions.md`, as it stood at the base `ec7929d` (`git show ec7929d:foundations/decisions.md`, the entry whole from its heading `### WAY-202 —` to the next heading), at its place in the numbering; remove its row from the list *Withdrawn identifiers* (the number is no longer withdrawn). It stays like the ten entries that stay (WAY-93, 94, 97, 263, 287, 294, 295, 297, 363, 364). Then restore everything that the withdrawal changed only because the entry left: the references `(WAY-202)` in the files the slices changed (find them with `git grep -n "WAY-202" ec7929d -- . ':!docs'` and compare with `git diff ec7929d HEAD` of each file; at the base they stood in `product-guidelines/coding/hand_back.md`, `settle.md` and `template.md`), and the relations `derives from WAY-202` / `narrows WAY-202` that row F6 removed or repointed in staying entries (at the base: the entries at lines 6258, 6398 and 6788 of the log, and the prose references at lines 6811, 12351, 12369), and the row of the withdrawn list of WAY-196 that already names WAY-202. Where a sentence of reason was added to a file only because WAY-202 left (the withdrawal's replacement for the entry), remove it together with restoring the reference, so the file reads as it read at the base for this rule; where a sentence also serves another rule, keep it. Judge each place by reading, and say in the report what you restored and what you kept and why. `python -B elements/common/foundation_check.py` must exit 0 afterwards (with the one expected `listed:` line for `tracked-file-private-paths`).
  2. **Complete the two notes of the guidelines** named in the remarks: (a) `product-guidelines/styleguide/starting_rules.md`, line 3, which opens with a reason ("A first screen built with no rules is the screen every later one copies.") and has no rule after it: add the rule it explains — when a styleguide comes into being (the timing rule of the removed WAY-184, `git show ec7929d:foundations/decisions.md`, its binding sentences) — in one sentence, written from the entry at the base; (b) `product-guidelines/coding/SKILL.md`, "A new kind", line 133, which holds the first-file rule of the removed WAY-200 with no sentence of its reason: add one sentence of the reason, from the *Rationale* of WAY-200 at the base. Nothing is written from memory: take the words from the entries at the base; where an entry gives no such sentence, add none and say so.
- Own-work check (WAY-164): read each rule you touch against its entry at the base.
- Checks (focused only): `python -B elements/common/foundation_check.py`; `python -B gate/run_tests.py <directory>` for each directory whose files you change and which holds tests (say where a directory holds none); `python -B agent-instructions/skill_entry_points.py` if a skill changes.
- Do not change anything the remarks do not name.

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

Your directory for working copies: `.runs/correction-1/` (remove its files one by one by path before you return; no recursive delete).

## Report

Write your report to `.runs/task-cycles/decision-log-second-round/reports/correction-1-report.md`: status, commits, for each of the two remarks what you did, the places restored and kept, each check with command and exit code, the own-work check, **Unread material**, **Searches not found or unclear**, working copies. Return the status, commits, one-line check result and the report path.

# Remarks of the human, correction 2

Source: the comment https://github.com/mariusznazar/the-way/pull/127#issuecomment-6893342618 on the request, written by the human (through the day advisor) on 2026-11-15 and read by the orchestrator with `gh api repos/mariusznazar/the-way/issues/comments/6893342618`. Word for word:

---

Mariusz's answer to the blocking item (written down by the day advisor)

1. (a) Allow the dependency: remove the debt record (the invariant `installation-instruction-files-dependency`) and add the instruction-file checker's part to the installer part's list of allowed dependencies in the part map, citing settlement 5 of the task. Then run what has not run on the final code: the comparison of the foundation with the code, a merge with the target branch if it moved, and the wait for the CI run.

---

Also given with the request to run this correction, as the input of the cycle's skill (the same instruction the human gave for the earlier runs): before the full run of the tests (step 10), write that it is about to start and wait for the signal "start" from the day advisor.

## What it binds

- The answer "fix it as the finding says" to item 1 of the request's description (kind 1, the blocking finding that remained after the review of its fix). The correction: remove the invariant `installation-instruction-files-dependency` from `foundations/invariants.md`; add `instruction-files` to the *Depends on* of `installation` in `foundations/part_map.md`, citing settlement 5 of the frozen task; nothing else.
- Then what has not run on the final code: the return step (the foundation compared with the code), the reconciliation with the target branch (`origin/foundations` had not moved from `7f5c5a5` when the correction began: `git rev-list --left-right --count HEAD...origin/foundations` gave 21 0, so no merge), and the wait for the CI run on the last head.

## Second part of correction 2: the human's answer to the question of the return step

Source: the comment https://github.com/mariusznazar/the-way/pull/127#issuecomment-6893500004 on the request, written by the human (through the day advisor) on 2026-11-15 and read by the orchestrator with `gh api repos/mariusznazar/the-way/issues/comments/6893500004`. Word for word:

---

Mariusz's answer to the question of the return step of correction 2 (written down by the day advisor)

1. Yes: allow the dependency. Add the part `repository` to the allowed dependencies of the part that holds the CI file (`.github/workflows/tests.yml` reads `/.python-version`), the same way as `instruction-files` for `installation`.
2. The two prose mentions in `installation/README.md` (the workflow file and `.the-way/.python-version`) are not a dependency: the code of `installation` does not read those files. No change.

Do it in correction 2, after merging `origin/foundations` (it moved to 9cbc6b2 with #132), then the return step on the final code, and before the full gate write that it is about to start and wait for the day advisor's signal.

---

What it binds: (1) add `repository` to the *Depends on* of `agent-instructions` in `foundations/part_map.md`, with the human's answer cited in the commit message (the map has no field for a citation); (2) no change for the two mentions in `installation/README.md`. The merge of `origin/foundations` (`9cbc6b2`) was made first (`cde07dd`); the return step runs again on the final code.

Recorded sources and kinds of correction 2: `item 1 · defect`; `remark · defect` (the return step found the reach of the CI file to `.python-version` as the part-map template requires *Depends on* to cover every reach, and the CI file came with this task).

First recorded source and kind: `item 1 · defect` (the finding named a reach the task's settlement 5 asked for, and the part-map template requires *Depends on* to cover every reach, so the missing allowance was required by the task and the foundation).

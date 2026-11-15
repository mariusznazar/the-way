# Handoff: review of the fix of the review of the merge (correction 1)

You are the reviewer of the merge `3eacbc1` (your report `reports/review-merge-report.md`, `FAIL`), resumed to review the fix of your two blocking findings, once. You did not make the change. Read-only on the repository; your own working copy is `.runs/review-fix-merge/` under the task's worktree `the worktree of the task`. No full gate (the orchestrator's); single directories one at a time.

## The range

`7d00a48..dcb1a19`: one commit, `dcb1a19` "Defer the CI rule to WAY-261 and record that installation reaches instruction-files", by the author of the correction, on `7d00a48` (the correction that you do not review again: its own review, `reports/review-correction-1-report.md`, is `PASS`). Five files: `foundations/decisions.md`, `foundations/invariants.md`, `task-cycle/skill/SKILL.md`, `task-cycle/skill/correction.md`, `agent-instructions/README.md`. The author's report: `reports/author-fix-merge-report.md`. Your findings, as the author received them: `reports/review-merge-findings.md`. Read from your own clone of `dcb1a19`, not from the worktree's working tree.

## What to judge

1. Finding 1: that each place the finding names (WAY-160, step 12 of `task-cycle/skill/SKILL.md`, `task-cycle/skill/correction.md`, `agent-instructions/README.md`) now defers to the second paragraph of WAY-261 for a check outside the task's scope that passes when run again, with no new rule, nothing widened and no place left that says a red CI result is always fixed; that the five places now agree with each other and with WAY-261, WAY-243 and WAY-161 and with step 10.
2. Finding 2: the orchestrator bound the author to the route WAY-225 gives and not to your first option (adding `instruction-files` to `installation`'s *Depends on*), because WAY-225 says a dependency the code holds and the map does not allow is recorded as an invariant the product does not meet, "never by rewriting the allowed dependencies of a part to fit the code", and the part-map template says *Depends on* names what a part may depend on, "not those its code reaches for today". The author wrote the invariant `installation-instruction-files-dependency` (`Violated: yes`, *Method* `review`, *Derives from* WAY-225 · WAY-51) in `foundations/invariants.md`. Judge: that this entry is a sound way to record the reach and in the form `elements/invariants/template.md` and its skill give; that the check of allowed imports (`cross-part-imports`, `elements/part-map/test_cross_part_imports.py`) reads it as intended and is neither relaxed nor changed in a way that lets another reach pass; that the choice of *Method* `review` for a sentence about any reach holds against "A test checks what its sentence is about"; and, if you hold that route wrong, say so with the evidence.
3. That the fix introduced no new Critical or Important finding. A Minor finding that remains, or a new one, does not block and goes to the request's list. Your Minor finding 3 stays unfixed by design.
4. The foundation check on the corrected tree (`python -B elements/common/foundation_check.py` without `--skip-test-citations`) and the tests of the directories whose files changed (`elements/part-map`, `elements/common`, `task-cycle`, `agent-instructions`), one at a time.

The author's gap, carried to you: it did not read WAY-11 whole in this fix, and did not use the "Reading the foundation" selection; select your own as your method gives.

## Your report

`reports/review-fix-merge-report.md`, first line `PASS <sha>` or `FAIL <sha>` (the sha of `dcb1a19`); findings with grades and places; the checks with command and exit code; **Unread material**; **Searches not found or unclear**; working copies and their removal. No secrets or personal data.

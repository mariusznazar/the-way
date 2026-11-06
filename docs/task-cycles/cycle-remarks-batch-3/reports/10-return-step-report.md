# Report 10 — the return step

**Status:** done. No commit; head stays `c46a0c9666ed977304678a959e19f74c086510a2`, worktree clean.

## Return step fields

- **Foundation compared with code:** compared WAY-298 and its relation (WAY-127), the WAY-291 *Verification* example, the entries the task names (WAY-127, 140, 10, 114, 120, 27, 296, 290, 291, 292), the entries my search found, and the part map of `task-cycle`, `elements-common` and `decisions`, against `task-cycle/skill/SKILL.md` (step 4, step 5), `task-cycle/skill/correction.md`, `task-cycle/request_check.py`, `task-cycle/remarks_check.py`, `task-cycle/record_template.md` and `elements/common/way_of_working.md`. Nothing no longer matches:
  - WAY-298 states the same restart condition as step 4 (restart after a fast-forward, which happens only where the checkout stands behind) and `correction.md` ("where something came in"); WAY-127 (read the skill from the checkout the session works in) is consistent with it; WAY-140 concerns effects outside the repository and the fast-forward is inside it.
  - WAY-291's rationale ("the check of the block's language counts words, and a correct block can be misread") is still true; its *Verification* example now matches the script (quoted text is not counted). WAY-290 and WAY-292 say nothing of what the measure counts, so they hold.
  - WAY-27: no file of the repository now names the private script (`grep cycle_remarks_digest` finds nothing); the other places that name the nightly review (`foundations/decisions.md:8765`, `:8925`, `:8960`) use "the nightly review of cycles", the name the changed files use.
  - WAY-10, 114, 120 against the new sentence in `way_of_working.md` and `elements/common/critique/SKILL.md:20-22`: all say the review of the change reads the entries and the human accepts at the gate, with the task document or at the merge.
  - WAY-296 and the check of WAY-294 against `record_template.md` and `remarks_check.py`: the form is unchanged; only the name of the reading review changed.
  - Part map: no file added, removed or moved; `task-cycle/**` and `elements/common/**` keep their claims; the responsibility sentences of the three parts are unchanged by the change.
- **Decisions written or changed:** none in the return step (WAY-298 and the WAY-291 edit were written in the change).
- **Invariants:** none written; no invariant derives from WAY-298, and none is required by the task or a decision.
- **Environment facts:** none; the change rests on no source outside the product.
- **Glossary terms:** none; "remote target branch" and "entry point" are used in their plain meaning, and the glossary search found no entry used against its meaning.
- **Part-map changes:** none.
- **Projected entries:** none (independent task).
- **Rows of *Settlements to record* written:** row 1 — written in the foundation step as WAY-298 (changed once by the fix, `c46a0c9`, which added the condition "where something came in" for the correction's restart; the condition is marked in report 07 for the human). Nothing missed.

## Checks

- `python -B elements/common/foundation_check.py` -> exit 0, `0 errors`.
- Not run: the product's gate (the handoff says not to).

## Searches not found or unclear

- none

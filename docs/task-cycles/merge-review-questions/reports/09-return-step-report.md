# Return step report — merge-review-questions

**Status:** done. **Commits:** none (nothing no longer matched; head stays `a5d6d5f`). Working tree clean (`git status --short` empty).

Read at head: `task-cycle/skill/return_step.md` (the version the change edited) and `task-cycle/skill/foundation_step.md`, whole.

## Return step (fields of the record's *Return step* section)

- **Foundation compared with code:** none no longer matched.
  - WAY-306 (written by the change, row 1) against step 12 of `task-cycle/skill/SKILL.md:415-420`: the fresh reviewer, the question whether the two sides hold together, the entries of the merge that bear on the touched parts named in the dispatch (WAY-150), the range of the merge, and the ending by WAY-162 (the file `task-cycle/review/SKILL.md` carries the range and the dispatch-named reading, unchanged) all match.
  - WAY-307 (row 2) against `task-cycle/skill/spec_review.md:6-8`, `task-cycle/spec/SKILL.md:18-20` and `task-cycle/spec/review.md:18-20`: the copy `spec-reviewed.md` beside the spec on `FAIL`, and the comparison by the reviewer of the revision with each earlier finding's resolution, match. `task-cycle/spec/design.md` (the designer's duty to remove contradictions, cited in *Rejected*) is unchanged.
  - Named by the task (*Decisions in play*): WAY-150 (the orchestrator selects for the merge reviewer's handoff; only the reviewer of the whole change selects for itself) matches step 12 and `task-cycle/review/SKILL.md:29-33`; WAY-162 (the reconciliation with the target branch is one of the reviews it lists) matches `task-cycle/skill/SKILL.md:364-373`; WAY-11 (names a word used in a meaning for which WAY-95 gives an entry, no term used against its entry) matches the edited `return_step.md`; WAY-135 (a spec, its review) is silent on a revision, so it is not contradicted.
  - Found by the search of the foundation: a grep of `task-cycle`, `elements`, `foundations` for "revis", "review the merge", "merge the current", "reconciliation with the target branch" finds no other text describing the merge review's dispatch or a revised spec's reviewer that disagrees. `foundation_check.py` at head: `0 errors`.
  - Part map, `task-cycle` entry: `Files: task-cycle/**`; the change added, moved and removed no file and changed no dependency; matches.
- **Decisions written or changed:** none in this step. Written earlier by the foundation step of the change: WAY-306 and WAY-307.
- **Invariants written or changed:** none. No task, decision or human sets a rule that code could break; the change is skill prose and two decisions.
- **Environment facts:** none. The change rests on no source outside the product.
- **Glossary terms:** none. The change corrects the use of a term against its entry (WAY-11 gives no entry for it), per *To do* 2, in `return_step.md` already. No word of the change takes an entry under WAY-95.
- **Part-map changes:** none.
- **Projected entries written whole or in part:** none; the task carries none.
- **Rows of *Settlements to record* written:** row 1 — WAY-306; row 2 — WAY-307 (both written by the foundation step at `5932216`, reworded at `a5d6d5f` per the fix; none missed by it).

A choice that binds after the merge (WAY-36) and a rule of the questions table: none found; the choices the change made (new decisions rather than additions) stand in `02-author-report.md`.

## Checks

| Command (from the worktree root) | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` (`0 errors`) | 0 |
| `git status --short` (empty) | 0 |

Not run: the whole gate (the orchestrator ran it on `a5d6d5f`), per the handoff.

## Searches not found or unclear

none

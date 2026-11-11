# Return step, again for the correction — guidelines-departure

**Status:** done. **Commits:** none (nothing no longer matched). Head stays `062b772`; worktree clean.

## Checks

- `python -B elements/common/foundation_check.py` — exit 0, "0 errors".
- `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0, "0 errors".
- A set comparison (Python, one run): the *Scope* of WAY-328 against the parts of `foundations/part_map.md` (sections with a **Files:** line) — identical, 16 parts; the three binding sentences hold none of should/will/must/MUST/SHALL.
- Not run: the full gate (the orchestrator's). No test: prose-only correction.

## Return step (fields of the record)

- **Foundation compared with code:**
  - WAY-328 at `062b772`: the third binding sentence ("A separate task that writes the general coding guidelines of the-way's own takes the coding guidelines out of this decision, one that writes its testing guidelines takes the testing guidelines out of it, and once both are written the decision is withdrawn") against WAY-217 (a departure applies only within the scope the decision gives, so a per-discipline end of the departure agrees) and against `product-guidelines/reading.md` ("applies only to the parts and work it expressly covers"; "A scoped departure removes that finding only within its scope") — they match. The *Rationale*, *Verification* and *Rejected* do not speak of the withdrawal, so they agree by silence. Nothing no longer matched.
  - The renumbering by the merge `66cc61d`: the entry is WAY-328 in `foundations/decisions.md`; WAY-327 there is another task's decision (the request's section for the human's decisions). A grep of `*.md` and `*.py` outside `.runs` finds WAY-328 only at its own heading and WAY-327 only in its own entry and in `task-cycle/skill/request_template.md`, where it means that other decision. No file, entry or test refers to the departure by the old number. The old number appears only in this cycle's reports under `.runs/`, which are no part of the tree.
  - The merge changed `elements/decisions/template.md`, `elements/common/rules.md` and `elements/invariants/template.md` (the form of `TODO` in *Based on*; *Origin* never names a task document). WAY-328 against them: *Based on* reads `none` — its only source is the human's answer, a decider's motive, which the template says is no source outside the product, so the `TODO` form does not apply; *Origin* reads `none` and names no task document; *Relations* and *Verification* hold no `TODO`. The foundation check passes. Nothing no longer matched.
  - WAY-215, WAY-217, WAY-209, WAY-244, WAY-173, WAY-09: unchanged by the merge for this purpose (the diff of the merge touches none of their text relevant here; the merge changed other decisions' lines). Compared again with `product-guidelines/reading.md` and the part map: they match, as in the earlier return step.
  - Part map of the touched part (`decisions`): `foundations/part_map.md` was not changed by the merge; its 16 parts equal the *Scope* of WAY-328.
- **Decisions written or changed:** WAY-328 (written in the foundation step, edited in place by the fix of the Minor findings and by the correction; renumbered from WAY-327 by the merge). No other.
- **Invariants written or changed:** none (none is set).
- **Environment facts:** none.
- **Glossary terms:** none.
- **Part-map changes:** none.
- **Projected entries written whole or in part:** none.
- **Rows of *Settlements to record* written:** row 1 — WAY-328; row 2 — WAY-328.

## Unread material

- Read whole: `task-cycle/skill/return_step.md` (current copy, unchanged in text from the earlier read), WAY-328.
- Read in part: `task-cycle/record_template.md` (the *Return step* section only); the merge's diff of `elements/decisions/template.md`, `elements/common/rules.md` and `elements/invariants/template.md` (the diff, not the files whole); the stat of the merge's other files (`task-cycle/*`, the decisions the merge changed) — not read, as they do not touch WAY-328 or the entries the task names (the grep above found no reference).

## Searches not found or unclear

none

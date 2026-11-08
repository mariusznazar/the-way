# Return report — decisions as material at refinement

Status: `done`. Commits: none (nothing needed correcting). Head compared: `d496942`; worktree clean.

## Return step (record form)

- **Foundation compared with code:** compared the entries the change writes or changes (WAY-313, WAY-314, WAY-315, WAY-113, WAY-115, WAY-124, WAY-134, WAY-138, WAY-165, WAY-267, WAY-111), as they stand after the fix of the Minor findings, with the files as they stand now:
  - WAY-113 (the narrowed question, entries of a definition's refinement included) with `elements/common/way_of_working.md` "How a skill asks", `settle.md` sub-step 6, `task_variant.md` step 4, `definition_variant.md` collision move, `lead/skill/SKILL.md` step 5, `orchestrated_mode.md`: same rule everywhere; no mismatch.
  - WAY-115, WAY-124, WAY-134 (row repeating a human choice enters accepted, marked) with `elements/common/skill/SKILL.md` step 3, `build_table.md`, `task_variant.md` and `definition_variant.md` step 2, `find_settlements.md`, `task/template.md`, `orchestrated_mode.md`, `final_review.md` ("no row awaiting the human"): no mismatch.
  - WAY-313, WAY-314, WAY-315 with `resolve_gaps.md`, `carry_foundation.md`, `list.md`, `task_run.md`, `running_product.md`, `settle.md`, `technology/SKILL.md`, `definition_template.md` (Technology section), `task/template.md`; and WAY-315 against the cycle: `task-cycle/skill/SKILL.md` ("a finding that the spec contradicts a decision"), `task-cycle/skill/spec_review.md`, `task-cycle/spec/design.md` already have the author of a spec return the contradiction as WAY-30 gives, which is WAY-315 — no change to the cycle needed.
  - WAY-165 and WAY-267 ("may open", no reservation of the human's word) with `task_run.md` List and Write, `list.md`, `resolve_gaps.md` (logs/failure items of the deployment check, WAY-139): the same "may" in all; no leftover "opens only on the human's word" in any file or entry (grep of `foundations/decisions.md`, `project-level`, `elements`, `task-cycle`, `product-guidelines`).
  - WAY-138 with `task_run.md` ("a choice opened over a decision is no longer held, so it is tested") and `settle.md` sub-step 5: no mismatch.
  - WAY-111 with `project-level/skill/read_foundation.md` (the framing clause): same.
  - Entries the search found and left unchanged (WAY-14, WAY-25, WAY-30, WAY-33, WAY-114, WAY-118, WAY-121, WAY-123, WAY-126, WAY-139, WAY-140, WAY-154, WAY-155, WAY-166, WAY-270): re-read where the fix could touch them; still true. WAY-118 (a change of a projected decision goes through the gate) agrees with WAY-313's exclusion and `resolve_gaps.md`.
  - Part map of `decisions`, `elements-common`, `project-level`: files and dependencies unchanged by the change (no file added, moved or removed; no new import); nothing to correct.
  - What no longer matched and its correction: none.
- **Decisions written or changed:** written WAY-313, WAY-314, WAY-315; changed WAY-113, WAY-115, WAY-124, WAY-134, WAY-138, WAY-165, WAY-267 and WAY-111 (WAY-111 and WAY-138 as the cycle's: the first by the fix of finding 1, a framing clause; the second by the foundation step's search, wording only).
- **Invariants written or changed:** none (no rule of the task, a decision or the human asks for one; no invariant derives from the changed decisions: `grep` of `foundations/invariants.md` for their identifiers finds none).
- **Environment facts:** none (the change rests on no source outside the product).
- **Glossary terms:** none. Checked "material", "consent", "refinement": used in their ordinary meaning, and no entry gives them another.
- **Part-map changes:** none.
- **Projected entries written whole or in part:** none (the task carries none; its project relation is independent).
- **Rows of *Settlements to record* written:**
  - row 1 — WAY-313 (also the reservation removed from WAY-165 and WAY-267)
  - row 2 — WAY-314
  - row 3 — WAY-113 (edit in place)
  - row 4 — WAY-134 (with WAY-115 and WAY-124 in step)
  - row 5 — WAY-315

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — exit 0 ("0 errors"), run on the head compared (no edit made in this step).
- Focused test directories not rerun: no file changed in this step.
- Not run: the full gate (the orchestrator's; it passed on this head).

## Reaches beyond the handoff

- `task-cycle/skill/SKILL.md` (lines 268-278), `task-cycle/skill/spec_review.md`, `task-cycle/spec/design.md`: read by search for "contradict" / "WAY-30" to compare WAY-315 with the cycle; passages only.
- `task-cycle/record_template.md` (*Return step*): read for the form of this record.

## Searches not found or unclear

- none

# Return-step report — plan-partial-foundation

**Status:** done

**Result:** No return-step correction was needed. The frozen task has no settlement rows, projected entries, human actions or open carried questions; its requested code change is the prose update already committed in `90e826a`. The task's out-of-scope `task-cycle/skill/foundation_step.md` remains unchanged.

**Foundation comparison:**

| Category | Comparison with the final change |
|---|---|
| Decisions | WAY-01 is respected: the change is an instruction update on the task branch and does not introduce a projected future state into the foundation. WAY-44 supports placing the part-map update with the slice that adds its file. WAY-126 supports including the part of an entry the task carries that its code makes true, including when the project plan assigns writing the entry elsewhere, and separately including entries assigned by the task's plan item. No decision entry is changed. |
| Invariants | No invariant sentence or test is changed. The task-cycle wording only guides plans; it adds no product behavior. The reviewed whole-change gate passed, including invariant checks. |
| Glossary | No glossary entry is changed. “Projected entry,” “foundation step,” “part map,” “plan item,” and “slice” are used in the meanings their existing entries define. |
| Environment facts | No external source or environment fact is introduced or relied on by the change. |
| Part map | The `task-cycle` entry assigns `task-cycle/**` to that part; the changed skill is already within that pattern. No new file or part-map pattern is added by this change. The instruction now assigns a future part-map change for a new file to the slice adding that file, keeping a pattern and its tracked file together as WAY-44 requires. |

The foundation-step rule for a plan member writing only entries its plan item assigns remains unchanged. The new planning instruction requires the plan to name a carried partial entry even when another plan item owns writing it; this does not authorize the current task to write the other item's entry. This distinction follows the frozen answer to Q1, WAY-126 and `foundation_step.md`.

**Checks and review:**

- `git diff --check HEAD^ HEAD -- task-cycle/plan/SKILL.md` — exit 0.
- `git diff --quiet` — exit 0; no uncommitted tracked changes.
- `git status --short --branch` — exit 0; on `task/plan-partial-foundation`, clean.
- Whole-change review — PASS on `90e826a`, as reported by the orchestrator; no findings.
- `python -B gate/run_tests.py` — exit 0, as reported by the orchestrator: 613 tests in 8 directories, 5 Windows platform skips. I did not rerun the full gate during the return step.
- No other focused test was run: this is prose-only, and the completed gate covers the reviewed commit. The manual own-work scenarios are recorded in the author report.

**Reaches:** Read the return-step and foundation-step instructions named by this dispatch, and used the original author's selected decisions, task-cycle part-map entry and other selected foundation material. No additional foundation entry was needed.

**Searches not found or unclear:** `none`.

**Choices and concerns:** No choice remains open and no concern affects the change. No correction or commit was needed for the return step; the existing commit is `90e826a`.

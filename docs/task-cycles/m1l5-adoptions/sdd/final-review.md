# Final review — m1l5-adoptions, 7335b5f..9692cbb

### Strengths
- Rows 1–5 and To do 1–5 are covered whole: the tie-break placed below WAY-123, with row 1's reason for keeping it in WAY-137's *Rationale*; WAY-138's scope, `held by` exclusion, no backfill, risks shown before the choice and their path to *Rationale*; WAY-139's list sits in the binding sentence; WAY-140 covers both placements, reads, and row 5's proposal rule.
- Fingerprints checked: WAY-100, 122, 123, 125 and 140 carry current values; nothing carries `WAY-124@` (WAY-31).
- The new entries fit the template; the `violates` examples target the misreadings the rows name (filter, weight, risks in *Based on*).

### Issues

**Important**

1. `project-level/task/skill/SKILL.md:80-81` — "the list WAY-139 holds". In a product, step 1 reads only the *product* foundation. WAY-139 lives in the-way's own log, and no skill names that path, so an agent following the text literally cannot find the list. Fix: name it as WAY-139 in `<the-way>/foundations/decisions.md`. The list keeps its one home.
2. `foundations/decisions.md:4157-4159` (WAY-138 *Review when*) — `check by: 2026-12-31` does not come from row 2, which gives only the condition. WAY-24 says such a date moves only on the approver's acceptance. The condition also contains its own outcome ("and the tests then narrow…"), which makes it partly self-fulfilling. Fix: name the date in the request's *What this request settles* for Mariusz to accept. Keep only the observable state in the field. The narrowing already stands in *Rationale*.

**Minor**

3. `project-level/technology/SKILL.md:108-129` — no step says where the risks are written. Step 0 resumes only from `.runs/technology/<choice>.md`, and step 6's "not tested again" then leaves a resumed table with no risks. Fix: write the risks into that file in step 5.
4. `task-cycle/skill/SKILL.md:49-53` — the sentence citing WAY-140 is followed by "The one exception", so the backlog write reads as an exception to a decision that has none. Fix: one clause saying the write is the cycle's own record, not an effect of the task.

### Deferred minors: triage
- Slice 1, step 5 as one paragraph: **leave**. It reads correctly, and fix 3 covers resuming.
- Slice 1, "nor a decision already written": **leave**. It repeats the `held by` rule and has no wrong reading.
- Slice 2, "add an item … or offer the split": **fix**. As written, the agent can choose alone. WAY-139 gives the split to the human, so it should read "add an item and offer the split".
- Slice 2, placeholder at `task/template.md:47`: **fix**. Add `TODO` and `or none`, which the section rule uses. Its width is cosmetic.
- Slice 3, step 12 sentence: **fix**. Suggested wording: "except a blocked request, one waiting for human actions in the cycle included, which stays a draft".
- Slice 3, step 4 "joins that list": **fix**. When no in-cycle action was named, there is no list. State that the request then opens as a blocked draft listing the effect.

### Orchestrator ruling (backlog write)
Upheld. WAY-140 binds "a task's effect", and the write records the cycle without serving the outcome. WAY-107 only says where the backlog stands. Fix 4 makes this visible in the text.

### Declined to judge
- Item 6 (the mapping table outside the repository): outside the cycle by the task.
- Decisions-guard, entry-point and test results: taken as reported; not re-run.
- WAY-122's *Rationale* ("weighed by its consequences alone"): the plan's choice is defensible, and settling it belongs to the independent assessment.

### Assessment
**Ready to merge?** With fixes
**Reasoning:** The meanings are complete and the foundation stays consistent. Issue 1 leaves WAY-139's check unreachable in a product, and issue 2 puts a date the human never set into a binding field. Both are one-line fixes.

### Spec Compliance
- ✅ Spec compliant. Checked against WAY-137/1 and WAY-138/1 (`foundations/decisions.md:4090-4173`), WAY-122/1 (`:3440`), WAY-123/1 (`:3499`) and frozen-task rows 1-2:
  - `project-level/definition_template.md:197-203` states WAY-137 completely: place to run only; tie of "no consequence differs" and "more than one simplest and cheapest"; the three properties; decides nothing else, no filter, no weight. Nothing added.
  - `project-level/definition_template.md:204-216` states WAY-138 completely: recommended option only; constraint-settled choice included; no foundation-held choice and no written decision tested; three named tests; hypotheses with no source that the critique does not strike; in the table beside the option before the choice; the choosing human takes the risks; they reach *Rationale* beside the lacks, marked as hypotheses. The Review-when scope is correctly left in the decision, not copied. No contradiction with WAY-120/122/123: the WAY-123 bullet is untouched apart from moving the pointer "`settle-technology` leads that." to the end of the new bullet.
  - `project-level/technology/SKILL.md:102-119` (step 5), `:121-` (step 6, line 149 in the diff) and step 7 carry the order of work: recommendation, tie-break, one fresh agent per wave, critique told the risks are hypotheses, table with risks beside the option. Step 7 sends the risks with the lacks to *Rationale*. This matches brief items 1-5.
  - `elements/decisions/skill/SKILL.md:77-79` places lacks and accepted risks in *Rationale*, never *Based on*. Consistent with `elements/decisions/template.md:51-54`, which allows author prose in *Rationale*.
- Checked: step numbering in the technology skill is unchanged. The other "step 5" references (`project-level/technology/SKILL.md:32`, `project-level/skill/SKILL.md:30,92,97,121`) are `define-project` steps, so they still hold.
- Checked: one home per fact holds. The skill says "by the template's rule" for the tie-break and does not restate it.
- ⚠️ Cannot verify from diff: the suites and entry-point check (taken from the implementer, not re-run, as instructed).

### Strengths
- The template holds the rules and the skill holds the order, with decision identifiers cited as the surrounding text does.
- The tester is told to test only the recommended option, and the critique is told not to strike the risks. Both are the two ways WAY-138's *violates* cases are most easily broken.
- No rule is added beyond the decisions. No description changed.

### Issues
#### Critical (Must Fix)
None.

#### Important (Should Fix)
- `project-level/technology/SKILL.md:155` (step 6, last sentence: "A choice the human leaves unanswered goes into the next table") with step 5 (`:108`, "for the wave ... every choice of the wave"). A carried choice has a passed comparison and sits in a later table, but step 5 never says what happens to its risks. Read literally, a tester "for the wave" may skip it, so the choice would reach the human with no risks beside the recommended option. That breaks WAY-138 ("shown before the human chooses"). The other reading, testing it again, costs a second tester run and may give different risks. Fix: one clause in step 6 or 5, for example "its risks, already shown, stand beside it again; it is not tested again". That follows WAY-138 (the recommended option is tested once before the choice) and adds no rule. The implementer's first concern is real, and the fix is one sentence.

#### Minor (Nice to Have)
- `project-level/technology/SKILL.md:102-119`: step 5 is now one paragraph with five actions (form, tie-break, test, contradiction critique, show). It stays correct, but a reader resuming mid-step cannot find the seam. Splitting into nested bullets "a.-e." under step 5 keeps the numbering that other text refers to. This answers the second concern: the numbering argument is sound, but nested bullets avoid it.
- `project-level/technology/SKILL.md:111`: "nor a decision already written" is always true inside a wave, since the wave holds only open choices. It restates WAY-138 faithfully, so it is harmless and could stay.

### Assessment
**Task quality:** Needs fixes
**Reasoning:** The text states WAY-137 and WAY-138 faithfully and adds nothing beyond them. One gap remains: the skill is silent on whether a choice carried to the next table shows its risks beside the recommended option, and that gap can break the "shown before the human chooses" rule. A one-sentence fix closes it.

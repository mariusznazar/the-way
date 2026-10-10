# Review of the settlement commits d0f6e5b..a683701

### Rows applied
- 4: applied, `foundations/decisions.md:4183`
- 6: applied, `foundations/decisions.md:4223-4224`; the skill pointer is at `task-cycle/skill/SKILL.md:50-52`
- 9: applied, `foundations/decisions.md:4212`
- 11: applied. The readiness sentence is gone from WAY-140. WAY-124 holds it at `:3545-3546` and carries `WAY-140@a9310508` at `:3557`
- 12: applied, `foundations/decisions.md:4257-4265`
- 13: applied, `foundations/glossary.md:98-103`; WAY-124 `:3545,3576-3577`; WAY-140 `:4222-4269`
- 14: applied, `foundations/decisions.md:4148` and `project-level/technology/SKILL.md:120`. `project-level/definition_template.md:216` already used the wording
- 15: applied, `elements/decisions/template.md:55-57` and `elements/decisions/skill/SKILL.md:77-78`
- 19: applied, `foundations/decisions.md:4226-4228`, but the wording is ambiguous (Important 2)
- 20: applied, `foundations/decisions.md:4105` and `project-level/technology/SKILL.md:107`
- 23: applied, `project-level/task/template.md:46-49`
- cut 2: applied, `task-cycle/skill/SKILL.md:21`. Step 4 (`:71-75`) and step 13 (`:279-282`) still hold the rule. No file cites the skill's lines
- cut 3: applied, `project-level/technology/SKILL.md:111`. WAY-138 keeps the rule at `:4135`
- The rejected rows 3a, 5 and 16 show no change. The orchestrator's rulings are all met.

### Issues
**Critical:** none.

**Important**
1. `foundations/glossary.md:100` together with `foundations/decisions.md:4221-4222`.
   - **What is wrong:** the definition reads "an effect … that only a human makes". The words "only a human makes" are WAY-140's rule. WAY-96 says a definition holds no rule; this is the same test the orchestrator applied to "names and places". WAY-140's binding part no longer says the effect is "made only by a human". It now says the effect "is a human action", and the prohibition lives only in the definition.
   - **Why it matters:** row 4 of the frozen task ("nie zapada w cyklu bez człowieka") now stands in the glossary. The task template still cites WAY-140 for it (`project-level/task/template.md:96-97`). There is a second problem: the genus "effect" makes later uses read oddly. With the definition put in place of the term, "a human action whose effect the code needs" (`:4260`) becomes an effect of an effect.
   - **Fix:** give the definition the genus of an act, for example "A human action is a step of a task outside the product's repository that a human performs". Put "is made only by a human, through a human action the task document names …" back into WAY-140's first sentence.
2. `foundations/decisions.md:4227-4228`.
   - **What is wrong:** "and the request opens as a blocked draft where the document places no human action in the cycle" stands as a clause of its own. Read literally, every task with no in-cycle human action opens a blocked draft.
   - **Why it matters:** the entry now diverges from the skill's clearer wording (`task-cycle/skill/SKILL.md:74-75`, "listing that effect"). A level-2 verification compares work against the entry, not the skill.
   - **Fix:** "…joins that list for the human to place, and the request opens as a blocked draft listing it even where the document places no human action in the cycle."

**Minor**
3. `foundations/decisions.md:4228-4229`.
   - **What is wrong:** "The human places each human action while the task is refined" now contradicts found effects, which the human places at the request.
   - **Fix:** write "each human action the task document names".
4. `foundations/decisions.md:4226` and `:4259`.
   - **What is wrong:** "an effect the cycle finds" describes something the term covers but does not use the term. WAY-97 asks for the term instead.
   - **Fix:** once issue 1 is fixed, write "a human action the cycle finds that the task document does not name".
5. `project-level/task/template.md:46` and `:96-100`.
   - **What is wrong:** the template uses "action" alone for "human action". "action" also carries other meanings in the files ("security-sensitive action"). The glossary template says such uses are written as the whole term (WAY-99).
   - **Why it matters:** no row of the settlement names this file for row 13, so it is outside what was ordered.
   - **Fix:** raise it as a follow-up.

### Declined to judge
- Whether "human action" passes WAY-95's threshold (settled by row 13).
- The correctness of the fingerprint values (the applier reports none stale).
- Whether "its number of steps" keeps the Polish ambiguity.

### Assessment
**Ready?** With fixes. Every row is applied without extras. Two problems remain: the new glossary definition carries WAY-140's prohibition and has the wrong genus, and the found-effect clause can be read as blocking every request.

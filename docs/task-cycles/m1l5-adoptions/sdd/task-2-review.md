### Spec Compliance
- ✅ project-level/task/template.md:46-48 — new `## Human actions` section, always present, between
  Questions carried to cycle and Decisions in play; placements before the cycle (done / not done)
  and in the cycle (frozen rows 3-5, To do 4).
- ✅ template.md:110-121 — rule under "What each section carries" restates WAY-140 faithfully: effect
  on a server, DNS, keys, external account; read stays with the agent; proposal rule (account, key,
  database vs deployment, DNS to a new address); human places; ready only when every before-cycle
  action is done (WAY-124); blocked draft request for in-cycle actions; `none`; older documents
  name none. Nothing added except the `TODO` marker for an unplaced action (see Minor).
- ✅ WAY-139's list is not copied anywhere; SKILL.md:33-37 points to it (To do 3, row 3).
- ✅ SKILL.md:28-32 — names each outside effect as a human action, proposes placement by the
  template's rule, human places, asking per "How a skill asks" (no contradiction with WAY-113).
- ✅ SKILL.md:33-37 — deployment-skill check only when the outcome deploys or changes how/where the
  product runs; none for other tasks (matches WAY-139 verification).
- ✅ SKILL.md:62-64 — step 6 requires every action placed and every before-cycle action done
  before `Status: ready for cycle`.
- ✅ Implementer's concerns: (1) the older-document sentence is limited to the new section: correct,
  matches the settlement. (2) A not-done before-cycle action keeps `Status: waiting for human`: sound.
  WAY-124 makes the task not ready, the template (line 67) has only the three statuses, and this one
  is the existing "needs the human" status. (3) A missing item becomes a To do item and the split is
  offered: within WAY-139 ("gains an item ... or the human splits"); the whole draft is shown at
  step 6, so the human can still cut it.
- ⚠️ Cannot verify from diff: that no other file enumerates the template's sections (the
  task-cycle's reading of the task document, other docs). Implementer reports suites green.

### Strengths
- Each fact has one home: the list in WAY-139, the rule in the template, the skill points to both.
- Citations (WAY-124, WAY-139, WAY-140) sit on the sentences they support.
- The check is scoped, so unrelated tasks are not burdened.

### Issues
#### Critical
None.
#### Important
None.
#### Minor
- SKILL.md:33-37 — "add an item to *To do* ..., or offer the human to split" reads as two
  alternatives, so it is unclear whether the item is added first and the split offered beside it
  (the implementer's stated behaviour) or the human picks. Fix: one clause, e.g. "add an item to
  *To do* for that work and offer the human to split it into a task of its own".
- template.md:47 — placeholder line is 102 columns (limit ~100) and does not show `none` (other
  sections write "or none" in the placeholder), nor the `TODO` placement the rule at line 117
  introduces. Fix: shorten, e.g. `- <action outside the repository, or none> — <placement | TODO>`
  with the three placements left to the rule.
- template.md:117 — `TODO` for an unplaced action is a marker the settlement does not name; it is
  consistent with the template's `Answer: TODO` and step 6 needs some marker, so only mention it in
  the placeholder (above).

### Assessment
**Task quality:** Approved
**Reasoning:** Both files state WAY-139, WAY-140 and WAY-124 faithfully with the list kept in one home and no contradiction with WAY-113 or WAY-134. Only wording and column nits remain.

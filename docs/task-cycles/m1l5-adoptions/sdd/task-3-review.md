### Spec Compliance
- ✅ task-cycle/skill/SKILL.md:15-21 (hunk at old 46-48): the human action in the cycle sits beside the decision reserved to a human; no stop midway; blocked draft; "performs it at the request" matches WAY-140.
- ✅ SKILL.md step 1: `ready for cycle` plus every action placed before the cycle done (WAY-124); in-cycle actions read and handed to step 4. Matches WAY-124/WAY-140.
- ✅ SKILL.md write-scope paragraph: writes stay in the worktree/repository, reads outside stay with the agent (WAY-140). The WAY-107 backlog exception is kept unchanged.
- ✅ SKILL.md step 4: old "external side effect ... rules reserve its authorization" replaced by WAY-140's rule (prepare what the repository allows, blocked draft listing in-cycle actions, unnamed found effect joins the list for the human to place). Irreversible and security-sensitive staging kept.
- ✅ SKILL.md steps 12-13: such a request stays a draft and lists the actions "each as the task document names it" plus found ones. Consistent with WAY-125 (single human contact) and WAY-13/WAY-135 (untouched).
- ✅ task-cycle/record_template.md Request handoff: one new line, matching the request contents of step 13.
- ✅ No new rule: the cycle never decides placement; found effects go to the human "to place", which respects WAY-140's "agent alone decides" violation.
- ⚠️ Cannot verify from diff: that the gate's wording checks (task-cycle 41, gate 98, entry points) pass; taken from the implementer.

### Strengths
- Each fact has one home: the full rule is in step 4; line 15-21, step 12 and step 13 only point to it.
- Wording keeps WAY-140's split (before the cycle vs in the cycle) without restating the proposal mechanism, which belongs to refinement.
- Small diff; the record template line mirrors step 13.

### Issues
#### Critical
None.
#### Important
None.
#### Minor
- SKILL.md step 12 (new text): "a request the cycle marks `blocked`, one that waits for human actions in the cycle (step 4) among them, which stays a draft" is hard to parse. Fix: "except a request the cycle marks `blocked`, among them one that waits for human actions in the cycle (step 4); it stays a draft."
- SKILL.md step 4 (new text): "joins that list" presumes a list exists. If the task names no in-cycle action and the cycle finds only an unnamed effect, the sentence does not say the request is then a blocked draft. Step 13 ("Where the request waits for human actions") covers it only by implication. Fix: one clause, e.g. "... joins that list, or opens it".

### Judgement of the implementer's two concerns
- Backlog write (request link and state into the backlog entry, possibly outside the repository): not a WAY-140 conflict. WAY-140 governs a task's effect on a server, DNS, keys or an external account; the backlog write is the cycle's own bookkeeping, settled by WAY-107 and a named exception in the same paragraph. Leaving it unchanged is correct; folding it into WAY-140 would add a rule. No change needed.
- Placement `TODO`: the template says `TODO` is a missing answer and never makes a task look ready, and the cycle requires `ready for cycle` (step 1). A document with an unplaced action is therefore not ready, and the cycle must not place it itself. The diff needs no extra sentence; adding one would restate the readiness gate. No change needed.

### Assessment
**Task quality:** Approved
**Reasoning:** The text states WAY-140 and WAY-124 faithfully at every point the brief lists, adds no rule and contradicts nothing in WAY-125/13/135. Only two minor wording points remain.

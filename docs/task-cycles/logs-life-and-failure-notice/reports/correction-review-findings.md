# Findings to fix — correction review `FAIL 94d20f3`

The blocking finding of `reports/correction-review.md`, in the reviewer's words. Its Minor findings are not yours to fix.

## Important (blocking)

### C1. The correction keeps an item `— held by` on a silent decision, which WAY-165 names as a violation with no limit to a definition

- **Place:** `project-level/technology/task_run.md:52-57` ("the list shown to the human keeps the item
  `— held by`") against `foundations/decisions.md:4480-4481` and `:4459-4461`.
- **What is wrong:** WAY-165, an entry this change writes, says with no qualification that an entry leaving
  part of a matter unanswered "does not settle that matter", and gives as a violation "a logs item stays
  `— held by` or `— projected` on a decision silent on the record's life". The new text has a run at a task
  do exactly that, and says the silent decision "holds the choice too". `— held by` means settles, by both
  marker tables: "a decision of the product's foundation settles the choice"
  (`project-level/definition_template.md:204`, `project-level/task/template.md:148`). The file and the entry
  therefore say opposite things of the same item at a task.
- **Why it matters:** WAY-263 grades this Important: the change's files do what the entry forbids. The
  human's decision is right and the file carries it; the entry is what no longer agrees. An agent or a
  reviewer who compares a run at a task with WAY-165 finds the run's correct behaviour listed as a violation,
  and it meets two rules, WAY-165 and WAY-267, with no precedence between them, which WAY-25 says no agent
  settles. The author's report says WAY-165 says "nothing of opening a decision at a task beyond what the file
  now says"; the violating example and the binding clause do, since neither is limited. The handoff asked for
  this check: "WAY-165, WAY-270 and WAY-139, where one of them states or implies what you correct, say the same
  as the file; change one only where it departs."
- **Evidence:** the passages above. `foundation_check` cannot see it, and no test pins this text.
- **Fix in one line:** limit WAY-165's own clause and its violating example to a list of a project definition,
  or say in the clause that at a run at a task such a decision opens only on the human's word (WAY-267); then
  WAY-267 stays as it is, no `narrows` is needed, and WAY-165's meaning sentence for the request changes.


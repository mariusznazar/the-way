# Findings to fix — review of the whole change, task `testing-guidelines`

Source: `reports/whole-review.md` (first line `FAIL 3bd9e37b60cb4c91613dddfa517c445841016688`), the
blocking finding in the reviewer's words, copied from its section "### Important":

### Important

1. **Two decisions this change writes collide on who fixes the first test of a level, with no
   precedence recorded (WAY-25).** Comes from no slice alone: from the plan's *Foundation entries*
   (WAY-242 and the WAY-218 edit in `57917c3`, against WAY-238 in `4f207dd`, by the spec's ruling C4),
   carried into slice 3 (`2b5b1c0`) and slice 4 (`467a2af`).
   - WAY-238 (`foundations/decisions.md:6528-6531`) binds: "The author of a change chooses, in the
     task's cycle, which behaviour gets a permanent test and at which level … while a task's
     refinement holds no plan of tests"; its *Verification* marks as violating "a task's document
     lists the tests its change is to add" (`:6550-6551`). This is row 8 and Q7, the human's.
   - WAY-242 (`foundations/decisions.md:6678-6679`) binds: "where it has none, the task that writes
     its first test designates that test, approved in the task's refinement", and its complying
     example is "the task that writes a product's first end-to-end test designates that test, its
     document carrying the decision" (`:6688-6689`). WAY-218 (`:5868-5870`, `:5881-5882`) places that
     designation in the project breakdown. The skill's "A new level"
     (`product-guidelines/testing/SKILL.md:162-164`) has refinement settle "the level, its recipe and
     the path the test takes"; `product-guidelines/reading.md:77-79`,
     `project-level/task/skill/SKILL.md:170-172` and `project-level/plan/skill/SKILL.md:121-123` route
     it there.
   - What goes wrong: to apply WAY-242, the refinement (or the breakdown) has to decide that the task
     writes a test at a given level, and at which path — the choice WAY-238 gives the cycle's author
     and the list of tests WAY-238 names as a violation. An agent refining such a task meets two
     binding entries that pull opposite ways; WAY-25 forbids it to settle that itself. The coding
     analogue it was modelled on (WAY-200, WAY-216) has no such collision, because the kind of a file
     follows from the requirement, while the level of a test is the cycle's choice.
   - Why it lies within the task: rows 8 and 12 are both the task's; the collision is between entries
     the change writes, and "contradictions between the new or edited entries" is part of this review.
   - Evidence: the quoted lines; `foundation_check.py` passes because it checks references, not
     meaning.
   - Ways out, for the orchestrator to choose (the first two stay within row 8 and row 12; the third
     records a precedence, which WAY-25 gives to a human): (a) WAY-242's "where it has none" clause
     approves the designation in refinement only where the task's required behaviour itself is a
     test of that level, and otherwise, where the cycle's author chooses a level with an empty
     *Exemplar*, at a blocked draft request as WAY-172 already provides — the skill's "A new level",
     the reading bullet and the two project-level bullets follow; (b) the first test's designation
     left to the cycle's request under WAY-172 alone, refinement naming no test; (c) WAY-242
     `narrows WAY-238` with its area in a binding sentence, recorded by the human.


# The review of the spec

Step 7 of `implement-task`, read when the designer returns `done` with the spec.

Have a fresh agent other than the designer review the spec with `write-spec` (`task-cycle/spec/SKILL.md`) against the frozen
task and the foundation entries its handoff names. On `FAIL` keep the spec as `spec-reviewed.md`
beside it; the designer revises the spec once and the reviewer reviews the revision once,
comparing the two. The designer revises the spec in its own file, which no commit holds, so without
the copy the reviewer of the revision would compare it with the earlier text from memory. Settle a
finding left after that as step 6 settles a
question, and record the settlement in `spec.md` under *Decisions*, where the planner and the
author read it; a finding that the spec contradicts a decision goes as the foundation step gives
(WAY-30). A spec may name the foundation entries the change will write; the foundation step or
the return step writes them. Then judge the route again from the task in the light of the spec,
as step 4 does — one author where the change fits, planning where it needs division — and record
the reason; a spec alone requires no plan, and an earlier plan no longer binds.

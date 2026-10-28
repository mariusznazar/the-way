# The review of the spec

Step 7 of `implement-task`, read when the designer returns `done` with the spec.

Have a fresh agent other than the designer review the spec with `write-spec` against the frozen
task and the foundation entries its handoff names. On `FAIL` the designer revises the spec once
and the reviewer reviews the revision once. Settle a finding left after that as step 6 settles a
question, and record the settlement in `spec.md` under *Decisions*, where the planner and the
author read it; a finding that the spec contradicts a decision goes as the foundation step gives
(WAY-30). A spec may name the foundation entries the change will write; the foundation step or
the return step writes them. Then judge the route again from the task in the light of the spec,
as step 4 does — one author where the change fits, planning where it needs division — and record
the reason; a spec alone requires no plan, and an earlier plan no longer binds.

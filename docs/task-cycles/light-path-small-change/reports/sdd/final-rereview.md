### Finding Verdicts
- **Important 1: WAY-125/1 does not confine "touch of the foundation" to the executor's work** - ADDRESSED. `foundations/decisions.md:3566-3571` now reads "or whose touch of the foundation while that agent makes it needs a choice the task leaves open, changes the meaning of an approved decision, contradicts a current entry or writes or changes an invariant or an invariant test, is discarded ..." (the C10 wording exactly). Complies example (`:3598-3600`) reads "or whose touch of the foundation while the agent makes it writes an invariant, is discarded", matching C10. The "while that agent makes it" limit now covers all four listed conditions, so a return-step invariant (step 11) is no longer a discard trigger. It also agrees with the skill's switch window (`task-cycle/skill/SKILL.md:121-122`).

### New Breakage in the Fix Diff
None. The diff touches only `foundations/decisions.md` (4+/2-), wording only. The rewrap leaves short lines, as the plan's rewrap rule allows. The report records a new fingerprint (`f4d471cc`), no carriers of `WAY-125@`, guard exit 0 and decisions/gate tests OK. These are unverified claims; I did not re-run them.

### Out-of-Scope Observations
None.

### Verdict
**Fix round:** All findings addressed, no new Critical/Important breakage.

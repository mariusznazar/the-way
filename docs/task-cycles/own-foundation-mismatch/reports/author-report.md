# Author report

**Status:** done

**Files changed:**

- `foundations/decisions.md` — 27 lines added, 0 removed; adds WAY-263, a review grade rule for departures from a foundation entry the same change writes or changes.
- `task-cycle/review/SKILL.md` — 4 lines added, 0 removed; tells reviewers to grade the specified mismatches as Important and points to WAY-263.

**Commit:** `876482ee4545749f7e3daa8e8c3a3c607f1682fc` (`docs: grade foundation mismatches as important`).

**Checks:**

- `python -B elements/common/foundation_check.py` — exit code 0; 0 errors.
- `git diff --check` — exit code 0.
- Manual comparison of the task's accepted settlement with WAY-263 and the Grade section — the binding rule and the skill cover both direct departures (doing what the entry forbids or omitting what it requires) and a changed account that broadens the entry or drops a qualification; both include entries the change writes or changes.
- Permanent tests — none written; the change clarifies reviewer instructions and decision prose, which have no testable program behaviour.
- `python -B gate/run_tests.py` — not run; the orchestrator owns the full suite run for this cycle.

**Own-work check:** The requirement most likely to be missed was that a repeated account in another changed file must count alongside code that directly contradicts an entry, including when it drops a qualification. I compared the settled task wording against both the skill sentence and WAY-263's binding sentence and verification examples. Both cases are covered, and WAY-263 includes both newly written and changed entries. The manual check showed no missing case.

**Foundation search and reaches:** After settling the proposed entry's meaning from the task, I searched the whole `foundations/` directory for existing grading rules, accounts that repeat entries, and the new identifier. The search found no existing entry that states this criterion and no prior WAY-263. It found existing material in WAY-07, WAY-35, WAY-64, WAY-135, WAY-145, WAY-148, WAY-169 and WAY-171; I read each finding whole. These searches showed no collision requiring precedence and no dependent foundation rule to correct. WAY-161, WAY-220 and WAY-221 were read whole for the grading rule's parent and nearby criteria. The repository's decision skill also required the decision template, shared rules and writing method, which I read before drafting.

**Choices:** The wording follows the accepted settlement: direct mismatch and a restatement that broadens or drops a qualification are Important; both entries written and changed are included; the rule is its own decision derived from WAY-161. I did not change WAY-161. The rejected alternatives and their costs are recorded in WAY-263's *Rejected* field.

**Searches not found or unclear:** No existing WAY-263 or foundation decision covering this grading criterion was found. No other unresolved or unclear item arose.

**Problems:** None.

PASS f5ae96fb216e0550254bee40646afc46acfd56db

# Review of the return step's commit — guidelines-skills-batch

Range: base `2c46cb75cbcf30e5d495dda9dfe2f919ef0325fc` to head `f5ae96fb216e0550254bee40646afc46acfd56db` (`git rev-parse HEAD` confirms it). One commit, `f5ae96f`, two files:
`product-guidelines/coding/SKILL.md` (3 lines) and `product-guidelines/testing/SKILL.md` (5 lines). Reviewed as section 2 of `task-cycle/review/SKILL.md` gives, against the task (items 17, 18, 19), WAY-282 and WAY-247, and the three files the handoff names.

## Counts

Blocking 0, Minor 0, out of scope 0.

## What the diff does

It replaces one clause in the summary sentence of "Where the skill works" in each skill.

- coding: old "where its audit stops for the testing skill's, to its step 3" becomes "in a task that carries the testing guidelines too, to its step 3 while the testing skill has not led its matters, as `hand_back.md` gives."
- testing: the same with "coding guidelines" and "coding skill".

## Do the two corrected sentences say what the hand_back.md files and audit_end.md say?

- `product-guidelines/coding/hand_back.md:19-26` (the "In a task that carries the testing guidelines too (WAY-247)" item): hands back to step 3, not step 4, "while `maintain-testing-guidelines` has not led its matters in this task, also where it has no audit". The corrected coding sentence has the same condition (a task that carries the other guidelines, the other skill has not led), the same target (step 3), and drops the old audit-only trigger. Match.
- `product-guidelines/testing/hand_back.md:10-16`: the mirror of the above for the coding skill. Match with the corrected testing sentence.
- `product-guidelines/audit_end.md:52-56` ("Who hands back to step 4"): "A skill hands back to step 3 while the other discipline's skill has not led its matters in this task, also where that discipline has no audit." Same condition. Match.
- Both sentences keep "hands back to its step 4" as the first way and defer the details to `hand_back.md` ("as `hand_back.md` gives"). The separated-work case (hand_back "Where the audit stopped and the human has since separated the work", WAY-282) ends at step 4 as well, so it needs no clause of its own in the summary: after the separation the task no longer carries the other discipline's guidelines, and the new wording is conditioned on "a task that carries ...".
- The two sentences are symmetric and say the same thing for each discipline.
- Task item 19 asks for exactly this rule ("while the second discipline has not led its matters, also where it has no audit"). Item 17 and 18 concern audit_end/hand_back text, not this summary, and are not contradicted. WAY-282 (separation closes the list; the audit that stopped is the last one) and WAY-247 (one task may carry both; each skill leads its matters) are not restated differently by the two sentences: neither is mentioned, and the clause does not widen or narrow them.
- A search of all `*.md` and `*.py` files outside `.runs` and `foundations/decisions.md` for "audit stops", "stopped for", "stops for", "has not led" finds no other place that still states the old audit-only trigger. The remaining hits (`audit_end.md:52,55,61,170,206`, both `hand_back.md`) are the rule itself or the stopped-audit description, consistent with the new wording. `styleguide/SKILL.md:30` hands back to step 4 only and has no joined-task case; unchanged and correct.

## Findings

None.

## Declined to judge

- The return step's report claims about other decisions (WAY-216, WAY-240, WAY-310, WAY-311 and the rest of its list) and about the open questions in `author.md`: they are outside this commit, which changes only the two summary sentences. Whole-change review `reviews/review-whole.md` covers them.
- Whether `coding/SKILL.md` and `testing/SKILL.md` keep "only through the task document" (the earlier out-of-scope finding O1 that the return step names): not touched by this commit.

## Checks run

- `git rev-parse HEAD` — `f5ae96fb216e0550254bee40646afc46acfd56db`, exit 0 (matches the handoff's `f5ae96f`).
- `git diff 2c46cb7..HEAD --stat` and the full diff — exit 0; two files, 5 insertions, 3 deletions, as the handoff says. `git log 2c46cb7..HEAD --oneline` — one commit.
- `python -B instruction-files/check_instructions.py .` — "0 error, 1 warn, 3 info" (the warn is the dead path `_zadania\` in the root `AGENTS.md:21`, which this commit does not touch). The exit status printed in my shell was that of the piped `tail`; the script's own summary reports 0 errors.
- `python -B elements/common/foundation_check.py` — "0 errors", exit 0 (via `PIPESTATUS`).
- `python -B agent-instructions/skill_entry_points.py` — "entry points are current", exit 0 (via `PIPESTATUS`); the skills' descriptions are not changed by the commit.
- Manual check: the repository-wide search above for the old trigger wording, and a line-by-line comparison of the four texts (two corrected sentences against both `hand_back.md` items and `audit_end.md:52-56`).
- `git status --short` — clean (no change to the reviewed worktree).
- Not run: the unit tests and the full gate (the commit changes prose of two skill files; the return step reports them as passing, and the full suite is the cycle's own run).

## Reaches beyond the dispatch

- `product-guidelines/audit_end.md` whole (the handoff names it; I read it fully for the "A task joining code and tests" section), `foundations/decisions.md` entries WAY-282 and WAY-247 (as the handoff directs), and sections 5 "Hand back" and the "route of one kind" bullets of both `SKILL.md` files, to see that no other sentence in the same files restates the old trigger. Found none.
- The return step's report `reports/return-step-report.md`, read whole, as the claims to verify.

## Searches not found or unclear

none

# Fix report — Minor findings of the review of the whole change

**Status:** done

**Commit:** `a5d6d5f` (fix range `3601aba..a5d6d5f`). One file: `foundations/decisions.md` +8 −10. No skill file touched; the five sentences of *To do* 1–4 and `task-cycle/skill/spec_review.md` are unchanged. Not pushed.

## Finding 1 — fixed

- WAY-306 *Rationale*: removed "and no automatic check finds that"; the sentence now states the risk only ("a merge can bring in a rule or code that the change goes against, or that meets the change at a seam neither side shows alone").
- WAY-307 *Rationale*: "one more file kept with the spec, which reaches the record of the cycle with the rest of its directory" became "The price taken: the cost of keeping the copy."
- Check: `grep` of the diff shows both phrases gone; `foundation_check.py` 0 errors.

## Finding 2 — fixed as the cycle's call gives, with no word in `spec_review.md`

WAY-307 *Verification* now says only what the skill texts say: `complies` — the spec stays beside the revision as `spec-reviewed.md`, and the reviewer of the revision compares the revision with it and says for each earlier finding whether it is resolved; `violates` — the designer revises in place and no copy of the spec as reviewed is kept, or the reviewer of the revision judges it without comparing it with the spec as reviewed. The claims about "the dispatch names both" and "the dispatch leaves the reviewer to find the earlier version" are gone. The reviewer's method (`task-cycle/spec/SKILL.md:18-20`) keeps the dispatch rule. I held that this can be done without a word in `spec_review.md`, so it is unchanged.
WAY-307's *Rejected* still says the unchosen way "depends on the orchestrator writing the path of the copy into the dispatch"; that is the task's own question-3 *Not chosen* text, a way not chosen, not a claim about `spec_review.md`. Left as is.

## Checks

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` (`0 errors`) | 0 |
| `python -B gate/run_tests.py task-cycle` (151 tests, OK) | 0 |

Not run: the whole gate (the orchestrator runs it); `elements/common` tests (the fix touches only prose of two entries; the foundation check covers their form).

## Own-work check

Requirement most likely unmet: the fix must stay as small as the findings ask and not change the rule of either decision. Check: `git diff 3601aba` over the commit shows 8 insertions and 10 deletions, all in the *Rationale* of WAY-306, the *Verification* and *Rationale* of WAY-307; binding sentences, *Scope*, *Relations* and *Rejected* are untouched. Result: as stated.

## Searches not found or unclear

none

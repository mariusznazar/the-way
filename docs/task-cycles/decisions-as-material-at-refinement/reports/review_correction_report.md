PASS c8bf864ff75c2575be9d692906c552f0087ea06f

# Review of the correction for the human's remarks

Reviewer: `review-change`, review of a correction (`task-cycle/review/fix.md`), the reviewer of the whole change resumed. Range `ff395cf82bce445339f47c495a917a01f70e8fc4..c8bf864ff75c2575be9d692906c552f0087ea06f` (one commit `c8bf864`, `foundations/decisions.md`, +13/-9). `git rev-parse HEAD` returned `c8bf864ff75c2575be9d692906c552f0087ea06f`, matching. No file was changed by this review; `git status --short` was empty after the checks.

Counts: new Critical 0, new Important 0, new Minor 0. Remarks carried out: all (one remark, item 4).

## The remarks

The human's words: "przyjmuję punkty 1–3, poprawmy punkt 4 w tym requeście". Items 1-3 stay as they stand; item 4 (my Minor finding of the review of the fix: the *Rationale* of WAY-113 still says the full question stays "where an entry is written", and the *Verification* names only a task's refinement) is to be fixed.

- **Item 4, *Rationale* — made.** The sentence now reads "Where an entry is written outside such a refinement or a cycle runs, the answer is about to bind, so the question stays; the entries written during a refinement, such as the projected entries of a definition, wait for the person's acceptance of the whole document or at the gate, so they follow the rule of the refinement." It agrees with the binding sentence of WAY-113 ("...holds as well for the entries written during that refinement; in a task's cycle and where an entry is written outside such a refinement it is asked as above") and with `elements/common/way_of_working.md:36-42` ("How a skill asks", same two sentences). The reason it gives (acceptance of the whole document or at the gate) matches the earlier sentence of the same *Rationale* ("the person reads the whole document at its acceptance") and WAY-118 for the definition.
- **Item 4, *Verification* — made.** *Complies* now reads "in the refinement of a task or a project definition, the entries written during it included, an answer that changes a decision, or that follows a loose remark, is written as given, while an answer that contradicts a sentence the person said earlier gets one question quoting that sentence"; *violates* adds the definition and "for an entry written during it too". Both clauses say what the binding sentence says, no more broadly and without dropping its qualification (the earlier sentence of the person quoted).
- **Items 1-3 unchanged — confirmed.** `git diff ff395cf..HEAD -U0` has three hunks, all at lines 2555-2582 (the *Verification* and *Rationale* of WAY-113); the binding sentence of WAY-113 (lines about 2536-2545) and every other entry are untouched, and no file besides `foundations/decisions.md` changed.

## What the correction broke

Nothing. The *Rejected* of WAY-113 ("at refinement no question at all ...; at refinement no question only where the answer changes a decision, otherwise as before") is still true and was left alone. The edit added no line over 100 characters.

## Other places with the stale reading

`grep -rniE "where an entry is written|an entry is written" --include=*.md` over the worktree outside `.runs/`: `elements/common/way_of_working.md:40` and `foundations/decisions.md:2544` and `:2574` carry the corrected reading; `foundations/decisions.md:30` and `:2625` and the three `product-guidelines/*/SKILL.md` lines speak of other things (when an entry is written relative to code; where the writing is described). No file still carries the stale reading.

## Declined to judge

- Whether the full gate passes: the orchestrator runs it.

## Checks run

In `the root of the task's worktree`:

- `git rev-parse HEAD` — `c8bf864ff75c2575be9d692906c552f0087ea06f`.
- `git diff ff395cf..HEAD` read whole; `git diff ff395cf..HEAD -U0 | grep '^@@'` — three hunks, none in the binding sentence.
- `git diff ff395cf..HEAD --check` — exit 0.
- `python -B elements/common/foundation_check.py` — exit 0, "0 errors".
- `python -B gate/run_tests.py elements/common` — exit 0, 109 tests OK.
- Added-line length check (`awk 'length($0)>101'` on the added lines) — no line.
- The grep above for the stale phrase.
- Not run: the `project-level` and `task-cycle` tests (no file of those parts changed; the author reports `task-cycle` OK), the full gate.

## Reach beyond the handoff

none (WAY-113 whole and `way_of_working.md` "How a skill asks" were read in the earlier reviews of this change and re-read here at head).

## Searches not found or unclear

none

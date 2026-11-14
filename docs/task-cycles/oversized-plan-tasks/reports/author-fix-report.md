# Fix report: the three Minor findings of the whole-change review

**Status:** done
**Commit:** `4e3c4cf` Tighten the size wording the whole-change review flagged (branch `task/oversized-plan-tasks`, on top of `44c1d99`).

## Files changed

| File | Added | Removed |
|---|---|---|
| `foundations/decisions.md` (WAY-146, *Rejected*) | 3 | 3 |
| `project-level/plan/skill/cut_tasks.md` | 2 | 2 |
| `project-level/plan/skill/critique_plan.md` | 2 | 1 |

## Answers to the findings

1. **Finding 1 (decisions.md, *Rejected*, the threshold item): fixed.** The case figure and its measurement are removed; the threshold item now states the reason only: "a threshold fitted to one case would stop a task that is right to stand, and each false alarm forces a split, a whole cycle, or a mechanism of exceptions, where size is only a signal (WAY-13)". Chosen over adding a provenance clause, which is the longer way. The entry's binding sentence, Verification and Rationale are unchanged.
2. **Finding 2 (cut_tasks.md): fixed.** The first sentence now reads "A task too large is put to the human to split, and its size chooses nothing else (WAY-13)." The later sentences of the bullet are unchanged and agree with it: the author never splits for size alone; the critique judges size; the human settles any split before the plan is handed over (WAY-146).
3. **Finding 3 (critique_plan.md): fixed.** The sentence now says the author hands the critic the size test, its text, with the request: "the author hands the critic that test, its text, with the request."

## Consistency (WAY-263)

The WAY-146 binding sentence, `cut_tasks.md`, `critique_plan.md` and `project-level/plan/template.md` (paragraph at lines 184–189) all state the same test (goal joins two or more effects, each checkable alone in the running product and merged before the others) and the same routing (human settles the split; the author does not split for size alone). The fix did not touch the binding sentence, so no sentence of the other three needed a change. Read and compared by hand.

## Checks run

- `python -B elements/common/foundation_check.py` (repo root): exit 0, "0 errors".
- `python -B -m unittest discover -s project-level -p "test_*.py"`: exit 0, 275 tests, OK. Output in `a file in the session's scratchpad, not kept`.

Not run: the gate (`gate/run_tests.py`), per the handoff.

## Own-work check

- Requirement most likely missed: finding 1's fix must still keep the reason that a one-case threshold stops a right task, and must not leave a dangling reference to the removed case. Check: read the edited item in `foundations/decisions.md` (lines 4225–4228) and grep the WAY-146 entry for the figures "one third" and "five" and "36".
- Result: the item keeps the reason and the cost (each false alarm forces a split, a whole cycle, or exceptions). The grep `grep -n "one third\|five of\|36%\|5 z 14\|more than a third" foundations/decisions.md` (exit 0) finds the threshold itself at line 4225 ("set at one third"), which stays as the rejected option, and no case figure in the WAY-146 entry; the two other hits (lines 10358–10359) are unrelated entries.
- Requirement: finding 2's new first sentence must not contradict the cut's "author never splits for size alone". Result: consistent (both say the human settles the split).

## Unread material

- `foundations/decisions.md`: read the WAY-146 entry (lines 4177–4236) whole in this fix; the rest of the file is not read, as in the author report.
- `task-cycle/change/fix.md`: read whole (the variant names it).
- Findings file and fix handoff: read whole.

## Searches not found or unclear

- None for this fix. The earlier open items (WAY-13 and WAY-33 tails not read) remain as recorded in `reports/author-report.md`.

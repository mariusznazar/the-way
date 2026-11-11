# Correction report — the human's remark "popraw w tym PRze"

**Status:** done
**Commit:** `062b772` on `task/guidelines-departure` (base `66cc61d`). One file: `foundations/decisions.md`, WAY-328 only, +3 / -2 lines. Worktree clean.

## Checks

- `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0, "0 errors" (run twice: after the edit and after re-wrapping its first line to the entry's width).
- Not run: the gate (the cycle's); no test, the change is prose of one entry.

## The sentence as written

Third binding sentence of WAY-328 (now one sentence long, the entry keeps three binding sentences):

"A separate task that writes the general coding guidelines of the-way's own takes the coding guidelines out of this decision, one that writes its testing guidelines takes the testing guidelines out of it, and once both are written the decision is withdrawn."

Reasons:
- The orchestrator's choice of meaning, followed as given: the departure is per discipline (WAY-217 applies a departure to the work it expressly covers), so writing one discipline's guidelines ends the departure for that discipline only, and the decision goes when both are written.
- It names exactly the two disciplines the decision covers, so a styleguide of the-way cannot read as withdrawing it (the finding's first case), and one of the two being written no longer withdraws the other's departure (second case).
- Present tense; no *must/should/will*, no capital keywords; names no stage, no file, no count.
- It keeps row 1's meaning ("osobne zadanie je napisze i tę decyzję wycofa"): a task that has written the guidelines ends the departure; no value invented.

## What else I checked

- *Rationale*, *Verification* examples and *Rejected* do not speak of the withdrawal (the exit clause left the *Rationale* in the earlier fix), so none needed to change to agree; I changed nothing else, as the handoff says. Cost if the human wanted an example: one `complies` line (a task that writes the testing guidelines of the-way leaves the coding departure standing) can be added.
- A search for other mentions of WAY-328 in `*.md` and `*.py` outside `.runs` and the entry itself found none that speak of its withdrawal.
- Not touched, as the handoff says: the question of whether the departure releases a first file of a new kind of code (WAY-216).

## Unread material

none — the handoff and WAY-328 read whole.

## Searches not found or unclear

none

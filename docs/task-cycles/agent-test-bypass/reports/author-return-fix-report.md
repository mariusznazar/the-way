# Author report — the fix of the return step's finding

**Status:** done. **Commit:** `b91fe896`, a revert of `91f6c884` made with `git revert`, so the history keeps the attempt (1 file, 2 added, 9 removed). I hold the finding right and contested nothing.

## The finding and how the fix meets it

The finding (Important, `Contradiction: yes`): the return step added to the *Rejected* of WAY-410 and WAY-409 ways that no *Not chosen* of the task and no statement of the human holds, which WAY-134 and the decisions' template forbid for a decision written from a row or marked `the cycle's`, and it settled on its own a collision between WAY-100 and WAY-134 that WAY-25 reserves to the human. I agree: I took WAY-100 as "the more specific" rule, but neither it nor WAY-134 contains the other and no relation orders them; and the departure was no mismatch with the code, so the return step had no remit for it. Several of the added sentences were also not held by the facts (the card's system prompt, the transcript monitors, the card's monitoring of edit cycles) or inexact ("fourth strategy" for recording extra states, which is the third in the fact).

The fix reverts `91f6c884`. WAY-410 ends again "…has no other way out than the workaround." and WAY-409 "…but the first case passes the review unseen." I wrote nothing of the WAY-100 / WAY-134 collision into any entry; it is the reviewer's finding 2, for the human in the request.

## Checks (command and exit code)

- `git diff --quiet 1a17406a HEAD` — exit 0: the tree equals the tree the first fix left, for every file, `foundations/decisions.md` included.
- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- Not run: the full gate; the focused run of `task-cycle` (the revert leaves the tree identical to `1a17406a`, whose run was exit 0).

## Own-work check

- Requirement most likely not met: that the fix removes both clauses and nothing else, so that the entries stand as the review of the whole change and of its fix accepted.
- Check: the empty diff against `1a17406a` above, which is stronger than a search for the two clauses, since it also shows that no other line moved.
- Showed: empty (exit 0). Before the revert, `git diff --stat 1a17406a HEAD` listed `foundations/decisions.md` with 9 added and 2 removed lines, which is the added clauses.

## Reaches beyond the handoff

None. I read the handoff and the findings file whole; I did not open `reports/review-return-report.md` (the findings sufficed).

## Unread material

`reports/review-return-report.md` (named by the handoff as readable): not read.

## Searches not found or unclear

`none`

## Working copies

None made; `.runs/author-return-fix/` was not created, so nothing remains.

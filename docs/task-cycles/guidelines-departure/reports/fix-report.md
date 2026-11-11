# Fix report — Minor findings of the review of the whole change

**Status:** done

**Commit:** see the commit that follows `7442841` on `task/guidelines-departure` ("Fix the Minor findings of the review of the whole change: the reason, the exit and the rejected way of the departure, and the wrapping"). One file: `foundations/decisions.md`, WAY-327 only. Worktree clean.

## Checks

- `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0, "0 errors".
- Not run: the product's gate (the cycle's), no test written (prose-only change to an entry).

## Per finding

1. *Rejected*, row 2's way — fixed: one clause added at the end of *Rejected*: "a decision with no sentence that adds a new part to its *Scope* — the first script in a new part would raise the question of missing guidelines again." Taken from row 2's *Source* ("bez tego zdania pierwszy skrypt w nowej części znów stawia pytanie o brak wytycznych"); no file name or count.
2. *Rationale*, the reason — fixed: the *Rationale* now opens with the reason, from the task's *Not chosen* (a): the-way departs rather than writes its own guidelines because that is a large task of its own whose gain lies mostly in code and tests that already exist and would have to be cleaned, while every task of the-way with code or tests waits for it. The old opening sentence about the whole-the-way scope follows it.
3. Exit clause — fixed by moving it into a binding sentence (row 1's own clause, so dropping it would lose the row's meaning): third binding sentence "A separate task that writes guidelines of the-way's own withdraws this decision." It follows row 1 ("osobne zadanie je napisze i tę decyzję wycofa"); I dropped the prose version, including my own "or narrows", which row 1 does not give. The entry now has three binding sentences, the template's maximum; the sentence has no *should*/*will*/capital keywords.
4. Wrapping — fixed: the whole *Rationale* paragraph re-wrapped to the width of the rest of the entry, no one-line stub.

## Unread material

none — I read the findings file and `task-cycle/change/fix.md` whole and the current text of WAY-327 (which I wrote); the task's rows were read in my earlier work.

## Searches not found or unclear

none

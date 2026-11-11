# The human's remarks on request #97, second correction (2026-11-11, in the session that ran the cycle)

The remarks bind. They are recorded from the conversation, in their substance.

## S1. The mixed value (N-1 of the review of the first correction): fix it in this request, by route 1

The human answered "poprawmy to jeszcze" (let us fix it too) to the open item N-1 of the request, and
"tak, 1" (yes, route 1) to the orchestrator's question. Route 1, as put to the human:

- A mixed value — an invariant that rests on a fact the foundation holds and on one it lacks — is
  written with the known entries standing as they do now and the missing one as the last item of the
  value, a descriptive `TODO`:
  `Rests on: python-stdlib-modules · TODO — a second fact, from the vendor`.
- The description of that `TODO` runs to the end of the value, so a comma or a ` · ` inside it breaks
  nothing.
- A bare `TODO` in the last position, `python-stdlib-modules · TODO`, is an error with the hint to name
  what is missing, as a bare `TODO` as the whole value already is.
- The known entry stays checked as a reference (WAY-17: every link is written).
- The same in all three fields: an invariant's *Rests on* and *Derives from*, a decision's *Based on*.
- Corrections to WAY-71, `elements/common/rules.md`, both templates, the example of WAY-287 and item 15
  of `task-cycle/skill/request_template.md`; tests for each of the three fields.
- Rejected by the human with the orchestrator: the whole value `TODO — …` with the known fact moved into
  its description — the script would stop checking that reference.

## S2. What does not change

Everything the first correction settled stands (the three fields, the whole-tree reading of item 15,
`TODO` rejected in *Relations* and *Origin*, the order of the gate). After this correction the request
no longer asks about the mixed case (its item 6 goes).

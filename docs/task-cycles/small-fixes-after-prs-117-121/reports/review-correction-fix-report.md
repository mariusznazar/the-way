PASS 5cb2e1fcc28645f2af7f790bc672a131f208daa6

# Review of the fix of I1 (review of correction 1) — task `small-fixes-after-prs-117-121`

Head `5cb2e1f`, confirmed by `git rev-parse HEAD`; `git rev-list 5cb2e1f..HEAD` is empty and the tree is clean,
so the fix range is empty, as the handoff says. The fix is the corrected account in
`docs/task-cycles/small-fixes-after-prs-117-121/reports/correction-1-fix-report.md`.

## The finding

**I1 — fixed.**

- Mark: WAY-114 is now `the cycle's` (`correction-1-fix-report.md:13`), with the reason that no row carries it
  and the remark settles the template's rule, not this entry's wording or examples. That is the mark
  `task-cycle/skill/foundation_step.md:30-34` gives.
- Quotation: the two clauses (`correction-1-fix-report.md:17-18`) match `foundations/decisions.md` at
  `5cb2e1f` word for word: *complies* `:1240-1242` "and an entry that gained a pair of examples the row did not
  give has the pair there word for word"; *violates* `:1246-1247` "an entry marked as the cycle's for an added
  pair of examples reaches the merge with the pair not shown".
- Meaning sentences: the English one ("The lower part of the request's description shows, under an entry
  marked as the cycle's because of a pair of examples its writer added, that pair word for word, so that the
  human merges the examples … having seen them") and the Polish one are true of what correction 1 changed in
  WAY-114's binding sentence `:1226-1228`; the report also names the *Rejected* addition `:1258-1260`, which is
  no example.

## The claim that only WAY-139, WAY-60 and WAY-114 carry an added pair

- WAY-344: right that it no longer carries one. At `5cb2e1f` its *Verification* holds the base-copy case only
  in the clause tests hold ("that the check of the foundation lists an invariant whose sentence the change
  reworded and whose copy at the commit the branch left lacks its *Method* or its *Part*…"); the complies and
  violates clauses on the copy at the base, which I quoted in I2 of the whole-change review, are gone.
- WAY-229: the claim does not hold as stated — see m1. Its *Verification* gained, in `52b122b`, an appended
  *complies* clause ("…, the orchestrator taking it from the models the session's settings allow") and a new
  *violates* clause ("a review is asked for on the strongest model of the family while the session's settings
  keep that model out"). Those are the same kind of addition as WAY-114's: clauses the writer appended to an
  existing pair. Calling WAY-229's "changes of existing examples" and WAY-114's "an added pair" draws a line
  the rule does not draw.

## New findings

### Critical / Important

none

### Minor, within the task

**m1 — WAY-229's two added example clauses should be quoted under it too, the *complies* one with the *violates* one.**
Place: `correction-1-fix-report.md:26` ("WAY-229's two clauses are changes of existing examples reported
earlier. No entry other than these three carries an added pair") against `foundations/decisions.md` WAY-229
*Verification* at `5cb2e1f` (the two clauses quoted above). The handoff says the orchestrator will quote the
*violates* clause in any case. That leaves the *complies* clause, which is short and only qualifies an
existing example, so leaving it out costs little. Still, the rule of `task-cycle/skill/request_template.md:301-306`
and `:498-501` reads the same for both. Suggest quoting both clauses under WAY-229 in *Foundation entries*. Blocks nothing.

### Outside the scope

none

## Declined to judge

- The request's description itself — it does not exist yet for this round (handoff).

## Checks run

| Check | Result |
|---|---|
| `git rev-parse HEAD`; `git rev-list 5cb2e1f..HEAD \| wc -l`; `git status --short` | `5cb2e1f`; 0; clean |
| manual: WAY-114 *Verification* `foundations/decisions.md:1236-1248` against the report's two quotations | word for word |
| manual: `git diff b6b3416..5cb2e1f -- foundations/decisions.md`, every *Verification* hunk (WAY-114, WAY-60, WAY-344, WAY-139, WAY-229) | WAY-344 holds no added pair now; WAY-229 holds two appended clauses (m1) |

No test or gate run: no file changed.

## Working copies

none made. `.runs/review-correction/` stands empty from the previous round.

## Unread material

none

## Searches not found or unclear

none

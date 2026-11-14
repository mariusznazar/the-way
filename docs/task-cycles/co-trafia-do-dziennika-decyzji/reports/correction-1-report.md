# Report of correction 1 (the stale citations of WAY-168)

**Status:** done

Head at the start: `306a122959b3d2e72d76ad3a2d01a2bd1655f9b4` (confirmed with `git rev-parse HEAD`). Commit: `7a5fea4` "Cite WAY-173 for a field that binds only through a decision of the product". The worktree is clean.

## Places changed

Both changed from WAY-168 to WAY-173, one word each, nothing else touched:

1. `foundations/decisions.md`, *Rationale* of WAY-241 (line 7645): "A field binds only where a decision of the product carries it (WAY-173)".
2. `product-guidelines/testing/template.md:229`: "a field naming no decision stands as an example (WAY-241, WAY-173)".

**Which I took and why: cite WAY-173, in both places.** WAY-173 says the rules a template of a discipline carries bind a product only through a decision of the product's log adopting them. That is the sentence in WAY-241's *Rationale* ("a field binds only where a decision of the product carries it, so the template's defaults ... are proposals a product adopts or departs from"), so the citation fits it exactly; WAY-241 already *derives from* WAY-173. In the template line the citation sits behind the rule "a field that binds ends with the identifier of the product's decision that carries it; a field naming no decision stands as an example"; the first part is WAY-173's, the second is WAY-241's own, and the pair `(WAY-241, WAY-173)` names both. I did not drop the citation, because the sentence in both places is something WAY-173 says. WAY-168 stays cited elsewhere for what it still says.

No binding sentence, *Verification* or other word was changed; the *Rationale* edit changes no binding sentence, so no decision is "changed" for the check (confirmed: `0 errors`).

## The search (once, `foundations/`, `elements/`, `product-guidelines/`, `task-cycle/`)

`grep -rn "WAY-168"` over `*.md` and `*.py` there gave about 60 places. I read the context of each that could carry the stale sentence ("a rule that names no decision is an example"):

- Left, with the reason: `product-guidelines/template.md:91-94` ("What holds no rule is an example ... A rule with *Decision* `none` binds, so it is a rule, not an example (WAY-168)") — it states the current sentence of WAY-168, and WAY-168 still says "what the guidelines hold that states no rule is an example". `product-guidelines/coding/template.md:266` and `:298`, `product-guidelines/testing/template.md:259` ("nothing here binds (WAY-168)", "may stand under `## Examples`") — the same current sentence. `foundations/decisions.md` 5467, 5657, 5948, 5953, 6017, 7382, 8842, 10525, 10528 — they cite WAY-168 for the fields beside a rule, for the review reading what a test cannot, or for a rule that carries a decision; none says a rule naming no decision is an example. The rest of the places cite WAY-168 for a rule's invariant, its uses or its decision, and say nothing of an example.
- Found: only the two above. Withdrawn WAY-179 in the list of withdrawn numbers ("an example of a template needs no decision (WAY-168)") is a record of a withdrawn entry, not a live rule; left, since it names the old rule on purpose as the reason of a withdrawal.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` : exit 0, `0 errors`.
- `python -B gate/run_tests.py elements/common` : exit 0, 199 tests OK.
- `python -B gate/run_tests.py product-guidelines` : exit 1, "no test found in product-guidelines" — the directory holds no test, so there is nothing to run; this is the report the handoff expects, not a failure.
- The gate with no directory: not run (the orchestrator's alone).

## Own-work check

The requirement most likely not met: only the two places the remarks name are corrected, and no other place keeps the stale sentence. Check: the grep above over the four directories and the reading of each candidate's context; it showed no further place. A second check: `git diff 306a122..HEAD` shows two changed lines, one word each.

## Questions and concerns

none. Item 1's first part (the form of the `decision:` error), item 2 (the fresh reviewer's reading of the 24 decisions) and items 3-9 call for no change from me; I did not read those decisions.

## Reach beyond the dispatch

none beyond reading WAY-241, WAY-173 and WAY-168 whole, `reports/return-review-report.md` m1 and the context of the WAY-168 citations found by the search.

## Unread material

none

## Searches not found or unclear

none

PASS 8571691effd77b70b96293f3184ac700c4ca7784

# Review of the correction's two commits (`306a122..8571691`)

Method: `task-cycle/review/SKILL.md` and `fix.md`, read whole. The range is two commits, `7a5fea4` and `8571691`; `git rev-parse HEAD` is `8571691effd77b70b96293f3184ac700c4ca7784`; the worktree is clean. I computed `git diff 306a122..HEAD` and `git log` myself. Not read: the fix agent's reports (`correction-1-report.md`, `correction-1-fix-report.md`) beyond what the diff shows; I took no claim from them without the diff.

## The remarks and findings the correction answered

- **Human's remark 1, second part (the two citations of WAY-241): made.** `foundations/decisions.md` WAY-241 *Rationale* now reads "A field binds only where a decision of the product carries it (WAY-173)", and `product-guidelines/testing/template.md:229` reads "a field naming no decision stands as an example (WAY-241, WAY-173)". WAY-173 says what both places say: a rule a template of the-way carries binds a product only through a decision of the product's log that adopts it. I searched the repository outside `.runs/` for WAY-168 beside "example", "names no decision" and "no decision": the only hits left are the withdrawn WAY-179 row ("an example of a template needs no decision (WAY-168)", about a template example, still what WAY-168 says: what states no rule is an example) and rules under `## Examples` that cite WAY-168 for "nothing here binds" (`testing/template.md:259`, `coding/template.md:266`, `:298`), which WAY-168 still says. No other place cites WAY-168 for "a rule that names no decision is an example".
- **I1 (READMEs): fixed.** `README.md:84-88` now says "each decision that a change adds or whose binding sentences it alters and that nothing holds" and "each invariant that reads `test` whose sentence a change rewords while no file citing it changes". `agent-instructions/README.md:13-17` says "the invariants that read `test` whose sentence a change rewords while no file citing them changes". The first now matches WAY-12 and WAY-03 and the docstring of `foundation_check.py`. The second sentence of `agent-instructions/README.md` says "reports the decisions that nothing holds", with no error/listing split; it states no condition and is not broader than WAY-12 (which says the check reports them, an error for some and a listing for the rest). Same sentence read in `elements/invariants/template.md:170` and `elements/decisions/template.md` row of *binding sentences*: already qualified, unchanged.
- **I2 (altered test, not only line): fixed.** `task-cycle/skill/request_template.md:304-306` (kind 7) and `:456-458` (lower part) now say "each test that holds a sentence of a decision by a line `decision:`, where the change adds, drops or alters the test or its line". WAY-03's *Verification* (`foundations/decisions.md:103-111`) says the same in *complies* and *violates* ("weakens a test that holds a sentence of a decision by a line `decision:`, or drops its line, and its request is silent"). WAY-03's binding paragraphs are unchanged (`git diff` shows only the *Verification* lines), so no binding sentence changed and the human's acceptance is not reached. I searched the repository outside `.runs/` for "adds, drops", "drops or alters", "drops the line" and "alters the line": the only hits are these three places; no other place states the old line-only condition. The script's docstring says nothing of the request.

## Review of the correction's diff

- The request template's form is unchanged: same headings, the same kind numbers (7 keeps its place between 6 and 10), no group moved. Only two sentences inside kinds 7 and the lower part changed.
- No binding sentence of any decision changed in the range (`git diff` of `foundations/decisions.md` shows WAY-03 *Verification* and WAY-241 *Rationale* only), so `check_held` has nothing new to hold; WAY-03 stays held by its `tests:` clause and the lines `decision:` of the tests (unchanged). The reworded *Verification* is not read by the script (only the invariants named and the pair of lines).
- The one nuance, Minor and not blocking: WAY-03's binding sentence says a change that "alters" a test names it; the template and the *Verification* also name a test the change "adds" or whose line it "drops". That is wider than the binding sentence, in the safe direction (the request names more), and was already so before the correction for the line; it is the human-visible side of a change, not a loss. No grade above Minor; no action.
- Nothing else in the range: no code, no test, no change to a README beyond the two sentences.

## Findings

none (no new Critical or Important finding in the range; one Minor nuance above, stated, not a defect).

## Declined to judge

- My Minor findings m1-m5 and the finding o1 outside the task (they go to the request's list, as the handoff says).
- The first part of the human's remark 1 (let through).

## Checks run

- `python -B elements/common/foundation_check.py` at `8571691`: exit 0, output `0 errors`, no `listed:` line.
- `git diff 306a122..HEAD` read whole (two commits, 6 files); `git status --short` clean.
- Not run: `python -B -m unittest elements.common.test_foundation_check` again (no code or test changed in the range; it passed at `306a122` with 180 tests); the gate (not mine).

## Reaches beyond the dispatch

- `product-guidelines/{styleguide,testing,coding}/template.md` (the lines that cite WAY-168 near "example") and `foundations/decisions.md:12775` (WAY-179 row): to answer whether another place cites WAY-168 for the old sentence.
- `foundations/decisions.md:83-112` (WAY-03 whole) and `elements/common/foundation_check.py` lines 95 and 741 (its citations of WAY-03).

## Unread material

none of the dispatch: the handoff, `fix.md`, `review/SKILL.md` and the diff of the range were read whole. The fix agent's two reports were not read (claims to verify, and the diff answers them).

## Searches not found or unclear

none.

PASS 82d64319fea198b287a42f2eb8a91468b2ad15d0

# Review of the fix (c76debc..82d6431) — own-measurement-in-decision

`git rev-parse HEAD` is `82d64319fea198b287a42f2eb8a91468b2ad15d0`, the head given; worktree clean.
One commit. Counts: blocking 0, Minor 0 new, out of scope 0.

## Changed files (lines before, after, change; `task-cycle/change_file_sizes.py c76debc 82d6431`)

| File | Before | After | Change |
|---|---|---|---|
| `foundations/decisions.md` | 12582 | 12587 | +5 (77 added, 72 removed; the rest is rewrap) |
| `elements/decisions/template.md` | 248 | 248 | +0 (1 added, 1 removed) |

## Each finding of the findings file

1. **Blocking: the decisions template restated WAY-90 differently — fixed.** The sentence now reads
   "A measurement whose report a reader can open at an address is a citation, and a fact where the
   point above asks for one (WAY-90)" (`elements/decisions/template.md:54-55`). It no longer puts the
   open-report measurement on the quoting side. The three texts now agree: WAY-90's rationale ("a
   citation like any other, and follows the first sentence"), the environment facts template
   (`elements/environment-facts/template.md:59-60`, "a citation, and a fact where this section asks for
   one", unchanged) and the decisions template. All three say the same for the closed record (result
   in *Rationale* or *Rejected* with conditions, the sentence that it is the product's own, no fact).
   "The point above" is the *Based on* point immediately before the new one, where the fact rule is
   written, so the reference holds.
2. **Minor: WAY-256 — fixed.** The sentence stands in *Rationale* (`foundations/decisions.md:8023`,
   after the five to fifteen percent) and in *Rejected* (8063-8064, as a parenthesis after the
   estimate). It says "estimate", as the entry does. The entry no longer matches WAY-90's "violates"
   example.
3. **Minor: WAY-90 names no price — fixed.** `foundations/decisions.md:2100-2102`: "The price: a
   measurement of the product's own agents leaves no fact for the search of WAY-33 to find, so when the
   model it measured is replaced nothing flags the decision that rests on it; a finding of others about
   agents or models still gets its fact, as WAY-17 asks." It states the cost and keeps WAY-17 true; I
   read WAY-17 whole earlier and it is consistent.
4. **Minor: WAY-229 *Rejected* — fixed.** `foundations/decisions.md:6955-6957`: "(the same measurement,
   this product's own, whose record is not open to a reader of this repository)" after "got a PASS in
   both".
5. **Minor: wrapping — fixed, no word beyond findings 2-4.** I ran the word diff myself:
   `git diff --word-diff=porcelain --word-diff-regex='[^[:space:]]+' -U0 c76debc..82d6431 --
   foundations/decisions.md`. It shows exactly: the price sentence of WAY-90 added; "both;" turned into
   "both (the same measurement, this product's own, whose record is not open to a reader of this
   repository);" in WAY-229; the WAY-256 *Rationale* sentence added; "files;" turned into "files (the
   estimate is this product's own, and its record is not open to a reader of this repository);" in
   WAY-256 *Rejected*. No other token added or removed. Every one of the 14 changed hunks lies in a
   `*Rationale:*` or `*Rejected:*` paragraph at indent 0 (WAY-90 two, WAY-229, 255, 256 two, 309, 319,
   323 two, 350, 353, 364, 368), so no binding sentence, *Scope*, *Based on* or *Verification* moved.
   No added line is over 100 characters (a script reading the diff in UTF-8). The orphan line of
   WAY-368 is gone (that paragraph is among the rewrapped hunks).

## New findings in the fix diff

None. I read the price sentence, the three new clauses and the template sentence in place for a new
contradiction with WAY-27, WAY-05, WAY-80 and WAY-17: none. The new clause in WAY-256 says "estimate",
which is true to the entry, and says no more than the sentence of the others. The links grep over the
whole change (c76debc's base to head, added lines) finds no URL, note link or absolute path.

## The two invariants, read whole

- `outbound-link-reach` (`foundations/invariants.md`; method: review; derives from WAY-27): "No file git
  tracks contains a link into a repository that a reader not signed in to its host cannot open, or
  into a private note collection." The change and the fix add no link of any kind: the added lines
  contain no `http`, no `[[` and no drive path. The sentences point to nothing; they say a record is
  closed. Not broken.
- `tracked-file-private-paths` (method: test; derives from WAY-320, 309, 323, 324): no tracked file
  other than four named scripts contains an absolute path or, in a Markdown file, a note link. The test
  `python -B -m unittest task-cycle.test_tracked_files_private_paths` passes on the head (1 test OK).
  Not broken.

## Checks run (from the worktree root)

| Command | Exit | Result |
|---|---|---|
| `git rev-parse HEAD`; `git log c76debc..82d6431`; `git diff` of the range | 0 | head as given; one commit |
| `git diff --word-diff=porcelain --word-diff-regex='[^[:space:]]+' -U0 c76debc..82d6431 -- foundations/decisions.md` | 0 | only the words listed under finding 5 |
| A throwaway script (scratchpad) mapping each hunk to its entry, field and indent | 0 | 14 hunks, all *Rationale*/*Rejected*, indent 0 |
| A throwaway script counting added lines over 100 characters in UTF-8 | 0 | 0 |
| `python -B elements/common/foundation_check.py --skip-test-citations` | 0 | `0 errors` |
| `python -B task-cycle/private_paths_check.py foundations/decisions.md` and `... elements/decisions/template.md` | 0, 0 | `checked: 1 files, 0 listed` each |
| `python -B -m unittest task-cycle.test_tracked_files_private_paths` | OK | 1 test |
| `python -B task-cycle/change_file_sizes.py c76debc 82d6431` | 0 | table above |

Not run: the full gate (the orchestrator's). A first attempt at a token-level diff of the whole file in
Python (difflib) did not finish in two minutes and I stopped it; the git word diff above is the check.

## Unread material

The findings file and the fix report: read whole. The two invariants: read whole. WAY-17: read whole in
the earlier review; this review reread no other decision whole and read the edited passages of WAY-90,
WAY-229 and WAY-256 only (the entries I read whole earlier are unchanged except at those passages). The
rewrapped paragraphs of WAY-255, 300, 309, 319, 323, 350, 353, 364 and 368: checked by the word diff and
the hunk map, not reread for sense (no word changed). `reports/author-fix-report.md`: read whole.

## Searches not found or unclear

None.

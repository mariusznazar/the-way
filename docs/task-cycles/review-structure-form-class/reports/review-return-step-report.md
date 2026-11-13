PASS b596eec

# Review of the return step's commit, `review-structure-form-class`

Range `c6af26a..b596eec`, one commit, one file: `product-guidelines/coding/template.md`. `git rev-parse HEAD` is `b596eec5bd31322382c5c19d77c78619ad28db0f`, as given.

Counts: blocking 0, Minor 0, out of scope 0.

## Findings

None.

## What I compared

- The corrected sentence (template, bullet on the six rules, line 69-72): "The six required rules ... follow the standing checks in the order above, and the rule of size below and then the product's further rules follow those; a product that already has further rules takes the six in between when it adds them (WAY-271). A file of a kind holds none of the six."
  - Against WAY-355 (read whole): the rule of size stands "after the six rules on failures and logs" and, in *Verification*, `### Size of a function and a file` after `### Logging scope` with "the product's further rules follow it". The sentence says the same order: standing checks, six, rule of size, further rules.
  - Against WAY-271 (read whole): it requires the six "after the rules of its standing checks", each under its own heading. Its *Verification* says "the product's further rules follow them". That stays true with the rule of size between, since "follow" does not mean "immediately follow"; the author's decision to leave WAY-271 unchanged is sound. The sentence cites WAY-271 for the six and their place after the checks, which WAY-271 gives.
  - Against WAY-278 (read whole): it concerns only how the rules reach a product (an ordinary extension); the commit says nothing against it.
  - Against the template's other bullets and its fenced block: the headings run `### Linter`, `### Formatter`, `### Dependency audit`, the six, `### Size of a function and a file`, `### <further rules of the whole product>`. The next bullet ("The required rule ... follows the six, and the product's further rules follow it; ... takes it in between when it adds it") agrees with the corrected sentence. "Takes the six in between" now reads as between the standing checks and what follows them. For a product with further rules, the six therefore go before the rule of size and the further rules, and the rule of size goes between the six and the further rules. No contradiction.
- The re-wrap of the rule-of-size bullet: a word-level diff (`git diff --word-diff=porcelain`) of the whole file shows one added phrase, "rule of size below and then the" in the corrected sentence, and no other changed word. The re-wrapped bullet keeps every word, including "(WAY-355, WAY-173)" and `none — <PREFIX-NN>`. It also removes one over-long line (the earlier line was longer than the wrap of its neighbours).
- Sibling templates: `product-guidelines/styleguide/template.md:65` and `product-guidelines/testing/template.md:90` say "The product's further rules follow ...", with no rule of size in their discipline; unaffected.
- The author's report claims: the correction and the re-wrap are as it states; the checks it names were re-run by me where the handoff asked (below).

## Declined to judge

none

## Checks run

- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- `python -B task-cycle/private_paths_check.py product-guidelines/coding/template.md` — exit 0, `checked: 1 files, 0 listed`.
- `git diff --word-diff=porcelain --word-diff-regex='[^[:space:]]+' c6af26a b596eec -- product-guidelines/coding/template.md` — only the one added phrase above.
- `git status --short` in the reviewed worktree — empty.
- Not run: the whole gate and `gate/run_tests.py` (the handoff excludes them).

## Reaches beyond the dispatch

- `grep -rn "further rules" --include=*.md` over the worktree, excluding `.runs` and `decisions.md`: to see whether another file states the order of the six and the further rules. Only the three templates above; no other file to correct.
- Read `foundations/decisions.md` lines of WAY-355, WAY-271, WAY-278 and WAY-279 (WAY-279 only in passing, as it lies next to WAY-278); the handoff named the first three.

## Unread material

none

## Searches not found or unclear

none

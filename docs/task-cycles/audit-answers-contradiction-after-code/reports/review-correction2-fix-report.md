PASS 5a39a328346ad9a8d12e37732f52a86a164e3d17

# Review of the fix of correction 2 — audit-answers-contradiction-after-code

Range: `17065c8b9b2349b4f5953ac98a15285e3d221787..5a39a328346ad9a8d12e37732f52a86a164e3d17`, one commit
(`5a39a328`), four files. `git rev-parse HEAD` in the worktree gives the head named in the handoff.
Method: `task-cycle/review/fix.md` (review of a fix); the findings file
`reports/review-correction2-findings.md` (I-1, I-2) bounds the review.

Counts: 0 blocking, 2 Minor (one within the fix diff, one outside it), 0 out of scope.

## Findings of the findings file

**I-1 — fixed.** Each of the five places now says what `discarded_reason` does (it counts
`reason: ` followed by a backtick, `REASON_START`, whatever word stands in the backticks):
- WAY-405's binding sentence (`foundations/decisions.md:8116-8120`): "holds no second `reason: ` followed
  by a backtick ... read for such a second `reason: ` alone, whatever word stands after the backtick, so
  that a second attempt written in them with no backtick after the `reason: ` or with its reason in other
  words is not read".
- WAY-405's *Verification* (`:8134-8137`): "unknown where it holds a second `reason: ` followed by a
  backtick, a word that is no marker included".
- `process-audit/audit_count.py:155` and `:162-163`; `process-audit/record_items.py:15-17` (module
  docstring), `:216-221` (`discarded_reason`) and `:257-260` (`discarded_reasons`).

Probes at the head: B1 (`  - reason: open design choice` under a plain first attempt) `no`; B2 (the same
beside the colon) `no`; B6 (`reason:` with no space before the backtick) `no` — each a second attempt with
no backtick after `reason: `, not read, as the sentence now says. B3 (`  - reason: \`budget\``) and B4
(`reason: \`size\` and reason: \`budget\``) unknown, "holds more than one reason" — a word that is no marker
included, as the *Verification* now says. The test that cited the sentence against the code,
renamed `test_a_later_line_is_a_detail_unless_it_holds_a_second_reason_opening_in_backticks`
(`process-audit/test_record_items.py:235-271`), now holds what its cited sentence says, adds B3 and B4,
and fails under both mutations that make the code depart from the new wording (below).

**I-2 — fixed.** WAY-404's *Verification* (`foundations/decisions.md:8076-8083`) now reads "the record
holds the item once and it gives the marker `open design choice`, so that a yes stands over an unknown of
any other part of the record, save that the marker does not stand over a doubled item, over which the
mark of an entry alone stands, ... unknown where an entry carries no mark or the item is doubled and no
yes stands". Probes at the head: C1, C2, C4 (the item doubled, one copy with the marker, rounds marked
`no`, unmarked or missing) unknown, "more than once"; C3 (doubled, a round marked `yes`) `yes`; Y1-Y3
(the marker with *Review rounds* missing, doubled or unmarked) `yes`; Y4 (a second copy inside a code
fence, not an item) `yes`; Y5 (item missing, round `yes`) `yes`. Each is what the clause says. The test,
renamed `test_a_yes_stands_over_an_unknown_but_the_marker_not_over_a_doubled_item`
(`process-audit/test_record_items.py:392-422`), adds the doubled item with a `yes` round (yes) and with
rounds `none`, unmarked and `no` (unknown); it fails when the marker is let stand over a doubled item.

## New in the fix diff

### Minor

**m-1 (within the fix diff). Three new lines break the wrapping of their paragraphs.**
`foundations/decisions.md:8120` (WAY-405's binding paragraph, a line of about 125 characters where the
log wraps at 100), `process-audit/audit_count.py:155` (143 characters) and `:163` (130 characters), in
docstrings wrapped at 100. No rule of `ruff.toml` checks line length (no `E501` among the rules that
block), and the foundation check passes, so nothing breaks; it is style. Rewrap the three paragraphs
when next touched.

## Outside the fix diff

**m-2 (Minor, outside the fix diff). `discarded_reasons`' docstring still says "the reason of an entry
that reads `none` or holds two markers is None"** (`process-audit/record_items.py:253-254`). For an entry
of a list of entries the code gives None for a second `reason: ` followed by a backtick, whatever its word
(`- reason: \`size\`; reason: \`budget\`` → SEVERAL → None), the same narrower wording I-1 named for the
text of one attempt, here in the entries form. It stood at `17065c8b` too; with my earlier M-1 of the
review of correction 2 (WAY-405's *Verification* on an entry of two reasons) it goes to the request's
list. It does not reopen the review.

## Nothing else changed

- Code unchanged: the syntax trees with docstrings left out of `process-audit/record_items.py` and
  `process-audit/audit_count.py` are equal at `17065c8b` and `5a39a328` (both `True`).
- Tests: two tests renamed and extended in `process-audit/test_record_items.py`; no subtest removed (the
  diff removes only the two old `def` lines and one comment line, rewritten).
- Trust boundary `process-audit/record_items.py`: code unchanged; a line of 200,000 `reason: \`` read in
  0.02 s with no error.
- Other places with the old sentences: a search of the repository (`.runs/` apart) for `second marker`,
  `two markers`, `holds no other`, `whatever else the record holds`, `wherever the unknown` and `reason in
  other words` finds only the fixed places, unrelated uses (`installation/README.md:98`,
  `installation/test_install.py:47`, `task-cycle/request_check.py:33`, `foundations/decisions.md:2252`),
  the docstring of m-2, `record_items.py:19` ("the other two markers", true) and two test comments
  (`test_record_items.py:220`, `:285`) that speak of a second marker in a case where it is one.

## Declined to judge

none

## Checks

All in detached worktrees under `.runs/review-correction-2-fix/`:
- `python -B elements/common/foundation_check.py` (without `--skip-test-citations`), head — exit 0,
  `0 errors`.
- `python -B gate/run_tests.py task-cycle`, head — exit 0, `Ran 534 tests in 123.111s`, `OK (skipped=2)`.
- `python -B gate/run_tests.py process-audit`, head — exit 0, `Ran 276 tests in 392.508s`, `OK`.
- `python -B -I .runs/review-correction-2-fix/check.py wt prev out.txt` — exit 0: the syntax-tree
  comparison, the probes quoted above, and three mutations of `record_items.py` in the worktree of
  `17065c8b` with the head's `test_record_items.py`: `REASON_START` without the backtick → exit 1,
  `test_a_later_line_is_a_detail_unless_..._in_backticks` fails; a second reason counted only where it is
  one of the three markers → exit 1, the same test fails; the marker read where the item is doubled
  (`if not items:` for `if len(items) != 1:`) → exit 1,
  `test_a_yes_stands_over_an_unknown_but_the_marker_not_over_a_doubled_item` and
  `test_a_missing_or_doubled_item_gives_unknown_with_its_reason` fail; restored → exit 0, OK.
- Not run: the product's full gate (by the handoff).

## Reaches beyond the dispatch

- `ruff.toml` and `guidelines/coding.md` (*Linter*): whether the long lines of m-1 break a blocking rule
  (they do not).

## Working copies

Under `.runs/review-correction-2-fix/`:
detached worktrees `wt` (`5a39a328`) and `prev` (`17065c8b`, where the head's test module was copied for
the mutations), the script `check.py`, and the outputs `out.txt`, `pa.log`, `tc.log`. Both worktrees removed with `git worktree remove --force` (exit 0 each),
then `git worktree prune`, and the directory deleted; `git worktree list` names neither, and the
reviewed worktree is clean. No remainder; nothing kept in `reports/` (the probe answers stand in this
report).

## Unread material

- `process-audit/test_record_items.py`: read in the fix diff and the two tests changed, not whole.
- `process-audit/audit_count.py`: read in the docstring passage changed (lines 145-165), not whole; no
  executable line changed.
- WAY-404 and WAY-405 read whole at the head (as in the review of correction 2, the changed sentences
  re-read in the diff and at their lines).

## Searches not found or unclear

none

PASS f5100d7819e3ba91795e6f1a7fb0720db7337ceb

# Review of the fix of the return step after correction 2 — audit-answers-contradiction-after-code

Range: `9547acd470f7a05cba43193ab9bf4b2e56a12e22..f5100d7819e3ba91795e6f1a7fb0720db7337ceb`, one commit
(`f5100d78`, "Say that the mark of a round is read only where Review rounds is held once and in its
form"), five files: `foundations/decisions.md` +9/-6, `process-audit/SKILL.md` +6/-4,
`process-audit/audit_count.py` +11/-8 (docstring), `process-audit/record_items.py` +5/-3 (docstrings),
`process-audit/test_record_items.py` +21/-1. `git rev-parse HEAD` in the reviewed worktree gives the
head named in the handoff. Method: `task-cycle/review/fix.md` (review of a fix); the findings file
`reports/review-correction2-return-findings.md` (I-1 alone) bounds the review.

Counts: 0 blocking, 1 Minor (within the fix diff), 0 out of scope.

## Findings of the findings file

**I-1 — fixed.** Each of the four places now says that the mark of an entry of *Review rounds* is read
only where that item is held once and in its form, and that a *Review rounds* not read gives no yes,
over which the marker `open design choice` alone stands:
- WAY-404's *Verification* (`foundations/decisions.md:8076-8086`): "yes where an entry of the item
  *Review rounds* carries the mark of a contradiction, that item being held once and in its form (no
  entry in neither form, no findings file named twice, nothing beside its colon), or the record holds
  the item *Discarded attempt* once and it gives the marker `open design choice`, so that each yes
  stands over the unknown that the other item gives and over that of an unmarked round, while a
  *Review rounds* that is not read gives no yes, nor does a doubled *Discarded attempt*, ... unknown
  where an entry carries no mark, or an item is missing, doubled or not read, and no yes stands".
- `process-audit/SKILL.md:225-231`: "an entry of *Review rounds*, held once and in its form, says
  `contradiction yes` ...; each `yes` stands over the `unknown` that the other item gives, but a *Review
  rounds* that is not read (doubled, with an entry in neither form, with a findings file named twice or
  with text beside its colon) gives no `yes` of its own, nor does a doubled *Discarded attempt*".
- `process-audit/audit_count.py:159-162`: the self-contradicting "stands over every unknown" is gone;
  "Each yes stands over the unknown that the other item gives, but the mark of an entry is read only
  where *Review rounds* is held once and in its form (...), and the marker only where *Discarded
  attempt* is held once."
- `process-audit/record_items.py:24-26` (module docstring) and `:285-286` (`read_contradiction`).

The four conditions named for "in its form" are every way `rounds_item` and `read_rounds` give None
for an item that exists (`record_items.py:95-158`: more than one opener, text beside the entries, an
entry in neither form, a findings file twice; no entries and not `none` gives no entry to carry a
mark). Probes of every claim of the new sentences at the head (`check.py`, *Discarded attempt* `none`
unless said):
- the marker's yes over an unmarked round (P1), over a missing *Review rounds* (P4) and over an unread
  one holding a `yes` entry (P12): `yes`;
- the round's yes over a doubled *Discarded attempt* (P2), a missing one (P3), one with no marker (P10)
  and an unmarked round of the same item (P9): `yes`;
- the round's `yes` in an unread item: `none` beside the colon with the entry under it (P6), an entry
  naming `notes/b.md` beside it (P8): unknown, "does not give its entries";
- the marker in a doubled *Discarded attempt* with rounds marked `no` (P5): unknown, "more than once";
- both items unread (P11): unknown.
Each is what the sentences say. The findings file's R1-R4, R6 and R7 are now held by the test (below).

Other places: a search of the repository (`.runs/` apart) for `stands over`, `contradiction yes` (in
`*.md`), `an entry that says \`yes\``, `mark of an entry alone`, and for sentences where the audit or the
count reads or takes a mark of *Review rounds*, finds only the four places above, WAY-404's binding
sentence (`foundations/decisions.md:8068-8071`, "takes from that mark, with the marker ... whether a
contradiction ... came out" — it claims no yes over an unread item), and unrelated uses of "stands
over" (the rule of size). The template's item *Review rounds* (`task-cycle/record_template.md:57-`)
says how an entry is written, not how it is read.

## New in the fix diff

### Minor

**m-1 (within the fix diff). One line of the re-wrapped Q1 docstring is 155 characters long.**
`process-audit/audit_count.py:164` ("round of any record, older or newer, where a fix round's entry
carries no mark; with its own reason where *Discarded attempt* opens with no marker and does"), in a
docstring wrapped at 100. The fix re-wrapped two of the long lines that m-1 of
`reports/review-correction2-fix-report.md` named (`:155`, now `:155-156`; and the old `:165`), and
joined two lines into this one, so the picture of that finding changes: one long line remains, at a new
place. The author's report says the over-long line of the first draft was "fixed before the run"; this
one stayed. No rule of `ruff.toml` checks line length and the checks pass; style only.

## Nothing else changed

- No executable line changed: the syntax trees with docstrings left out of
  `process-audit/record_items.py` and `process-audit/audit_count.py` are equal at `9547acd4` and
  `f5100d78` (both `True`).
- The test: `test_each_yes_stands_over_the_unknown_of_the_other_item_but_an_unread_item_gives_no_yes`
  (`process-audit/test_record_items.py:392-442`, renamed, still cites WAY-404) keeps every earlier
  subtest and adds five unread forms of *Review rounds* holding a `contradiction yes` entry (doubled with
  the mark in either copy, an entry in neither form, a findings file twice, text beside the colon), each
  with *Discarded attempt* `none`, `size` and `reserved choice` (unknown, "does not give its entries")
  and with the marker (`yes`), and the well-formed control (`yes`). It holds what the *Verification*
  says, and it fails when the code behind it breaks: five mutations of `record_items.py`, in a worktree
  of `9547acd4` with the head's test module — a doubled item read from its first copy, a findings file
  twice allowed, text beside the entries allowed, an entry in neither form skipped, and an unread
  *Review rounds* returning unknown before the marker is read — each exit 1 with this test among the
  failures; restored, exit 0, `OK`, the file equal to the original.
- The comment that opens the test (`:394-397`) still says "the yes wins in every pairing" and "A doubled
  item *Discarded attempt* is the one unknown that its own marker does not stand over"; read with the
  new comment at `:416-419`, it is about the pairings above it, and nothing a reader would act on.
- Known Minor findings: m-1 and m-2 of the review of the return step (the entry with a second reason;
  the template's "since") and M-1, m-2 of the earlier reviews — untouched by this fix, as the handoff
  says; m-1 of `reports/review-correction2-fix-report.md` — see m-1 above.

## Declined to judge

- An entry `contradiction yes` written deeper than the first entries of *Review rounds* (probe P7, under
  an entry marked `no`, answers `no`): it is a detail of the entry above it, not an entry, by
  `rounds_item`'s "the ones at its first indent"; no sentence of the fix speaks of it and the finding did
  not name it, so it is outside this fix's bounds.

## Checks

All in detached worktrees under `.runs/review-correction-2-return-fix/`:
- `python -B elements/common/foundation_check.py` (without `--skip-test-citations`), head — exit 0,
  `0 errors`.
- `python -B gate/run_tests.py process-audit`, head — exit 0, `Ran 276 tests in 848.646s`, `OK`.
- `python -B gate/run_tests.py task-cycle`, head — exit 0, `Ran 534 tests in 227.026s`, `OK (skipped=2)`.
- `python -B -I .runs/review-correction-2-return-fix/check.py wt prev out.txt` — exit 0: the syntax-tree
  comparison (`True`, `True`), the probes P1-P12 quoted above, and the five mutations (each exit 1,
  restored exit 0).
- Not run: the product's full gate (by the handoff); `ruff` (not part of the focused checks).

## Reaches beyond the dispatch

- `ruff.toml` is not re-read: whether a long line breaks a blocking rule is taken from the earlier fix
  review's reach (no `E501`), as the file is not in the range.

## Working copies

Under `.runs/review-correction-2-return-fix/`:
detached worktrees `wt` (`f5100d78`) and `prev` (`9547acd4`, where the head's `test_record_items.py` was
copied for the mutations), the scripts `check.py` and `probe_head.py`, and the outputs `out.txt`,
`pa.log`, `tc.log`. Both worktrees removed with `git worktree remove --force` (exit 0 each), then `git
worktree prune`, and the directory deleted (`Test-Path` gives `False`); `git worktree list` names
neither, and the reviewed worktree is clean. No remainder.
Nothing kept in `reports/`: the probe answers stand in this report.

## Unread material

- `process-audit/test_record_items.py`: read at lines 1-50 and the changed test (392-442), not whole.
- `process-audit/audit_count.py`: read in the Q1 docstring passage and the diff, not whole; no executable
  line changed.

## Searches not found or unclear

- Another place in the repository that says a round's yes stands over every unknown: none (searches
  above; positive control: the same search found the four fixed places).

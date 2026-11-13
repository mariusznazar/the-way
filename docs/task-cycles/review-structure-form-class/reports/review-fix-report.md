PASS c6af26a

# Review of the fix — review-structure-form-class

Range `5353268..c6af26a` (`a47195b`, `cd54d5a`, `c6af26a`; 8 files, +83 / -24). `git rev-parse HEAD` =
`c6af26ac55958de51c25850ca935d3b11f229016`, the head given. Method: `task-cycle/review/fix.md`, bounded by
`reports/fix-findings.md` (I1, M1-M5).

## Each finding of the findings file

- **I1 — fixed.** All four places now take the exceptions out of the condition, and agree with the rule's invariant ("other
  than those the decision's exceptions name") and WAY-355's *Verification* ("where other code stands over"):
  - WAY-355 binding (`foundations/decisions.md:11797-11798`): "Where code other than the exceptions of the product's decision
    stands over a threshold, the rule's invariant is marked violated until that code is cleaned (WAY-51)."
  - `product-guidelines/coding/template.md:241-242`: "Where code other than those exceptions stands over a threshold when the
    rule enters, the invariant is marked violated until that code is cleaned (WAY-51)".
  - `product-guidelines/coding/settle.md:81-82` and `:113-115`: the meaning of a threshold said to the human, and the
    invariants bullet, "over a threshold that the exceptions, settled before this, do not name". The order holds: the
    exceptions stand in "What it settles", above the bullet on invariants.
  - `product-guidelines/coding/trial_run.md:30-31`: "Once the exceptions are settled, where code they do not name stands over a
    threshold, step 4 proposes the rule's invariant marked violated (WAY-51)."
  - Other uses: a search for "violated" over `product-guidelines/coding/*.md`, `task-cycle/review/whole_change.md`,
    `task-cycle/plan/SKILL.md`, `task-cycle/change/SKILL.md` and WAY-355 to WAY-360 finds no other sentence that sets a
    condition for the mark; the rest (WAY-358 and WAY-360 rationale and *Rejected*, `whole_change.md:44`) speak of an
    invariant already marked, and `template.md:153` is the linter's.
- **M1 — fixed.** WAY-359 *Rationale* now reads "(the conditions of the measurement stand in WAY-229)".
- **M2 — fixed.** `template.md:75` "It is none of the three standing checks (WAY-202)" and `:223` "It is none of the three
  standing checks"; the glossary's meaning stays whole. `template.md:245` "as a standing check's does" uses the glossary's
  sense and is right.
- **M3 — fixed.** `product-guidelines/audit_end.md:53-55` names "the rules on failures and logs and of the rule of size, with the
  questions to the human they bring".
- **M4 — fixed.** `task-cycle/review/whole_change.md:33-34`: "the first in the reviewed worktree, which it changes in nothing,
  and the second in separate worktrees".
- **M5 — fixed.** Three new tests cover the type change, the `|` escape and the backtick fence; `code_span` now also fences
  the rename note. Each test fails when its behaviour breaks (mutations below).

## What the fix itself broke

Nothing Critical or Important. `code_span` (`task-cycle/change_file_sizes.py:181-187`): a run of backticks gets a longer
fence, an edge backtick gets padding on both sides (CommonMark strips one space from each side), and `\|` is the GFM escape
of a bar in a table cell, code spans included. The rename note now comes from `Entry.renamed_from`, and the counter matches
`note == "renamed"`; both are tested. The new tests build entries with `update-index --cacheinfo` from a blob written
outside the repository's working tree.

### Minor (new in the fix)

**N1. Rewrapped lines left over-long** — `foundations/decisions.md:11969-11970` (124 and 141 characters),
`product-guidelines/coding/template.md:75`, `:223`, `:243`, `product-guidelines/audit_end.md:55`,
`task-cycle/review/whole_change.md:33`: the fix inserted words without rewrapping the paragraph, as the files around them wrap
near 100 characters. Polish only; nothing reads differently.

## Checks

| Command | Exit | Result |
|---|---|---|
| `python -B gate/run_tests.py task-cycle` | 0 | 383 tests, OK |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B task-cycle/change_file_sizes.py 5353268 c6af26a` | 0 | 8 rows; each change column equals `git diff --numstat` added minus removed; +59 in all |
| `git status --porcelain` in the reviewed worktree after the runs | 0 | empty |

Mutations of a copy of the head's script in the session's scratchpad, each run against the head's test file with
`python -B -m unittest -q test_change_file_sizes` (script `mutate.py` in the scratchpad, written to a file to avoid the shell
halving backslashes): unbroken OK; no `|` escape — 1 failure; fence not longer than the run — 1 failure; no padding — 1
failure; `type changed` turned into `modified` — 1 failure; rename note without a code span — 1 failure; rename counted as
modified — 1 failure.

Not run: the whole gate (the orchestrator's run), `instruction-files` and `agent-instructions` (the fix changes no skill's
description and no instruction file; the handoff names only the two above).

## Unread material

none — `fix.md`, the findings file, the fix report and the whole fix diff read whole.

## Searches not found or unclear

none

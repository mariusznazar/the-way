PASS e5ae875

# Review of the return step's commit, e5ae875 (base 31f7507bce088ecf6ee825889bfada949076db68)

`git rev-parse HEAD` in the worktree gave `e5ae8753a4d48407a7cb4643590024ca249fec30`, the head given. One commit in the range. Findings: 0 blocking, 1 Minor, 0 out of scope.

## Findings

### Blocking (Critical, Important)

none

### Minor

1. `foundations/decisions.md:6818-6819` (WAY-300 *Verification*, the violating example) — the example "the count starts at the merge of the review's own change" still describes a part the tests hold.
   - What: the clause `tests:` says the tests hold "the count of merges to the main branch since the nearest review tag, from the start of the history where none stands". The tests `test_only_the_merges_after_the_nearest_review_tag_count` and `test_without_a_tag_every_merge_since_the_start_of_history_counts` check where the count starts, and a count that started at some merge of the review's own change instead of the tag would fail the first. WAY-12 and `task-cycle/skill/return_step.md` keep the pair "only for the part no test holds".
   - Why it matters little: the example overlaps what the tests hold and contradicts nothing, so an agent that compares a change with it is told the same as the test says. Graded Minor for that reason.
   - Evidence: the diff of the commit removes only the complying example on merges of the main branch into task branches, and leaves this one. Whether the example is held depends on reading it as the count's start (script) and not as a rule of the cycle's wording; I could not settle that from the entry, so I name it and leave the choice to the orchestrator.

## Checks of the points the handoff names

- Lines `decision:` (six lines, five tests of `task-cycle/test_review_reminder.py`, comments only, no code in the diff): each gives `WAY-300` and a start of a sentence of its binding sentences — "At the end of every task cycle the orchestrator counts the merges" (first sentence) and "The reminder blocks nothing, the threshold is one number" (second sentence of the first paragraph). Held by the tests where they stand: the three tests of the count since the nearest tag, the test of the main branch's merges into task branches, the 59/60 threshold test (count and threshold), and the no-tag test (the end of the second sentence, "a repository with no review tag counts from the start of its history"). No line is longer than 100 columns.
- Check that the checker reads them: in my own worktree of `e5ae875` I changed one letter of the second quotation, and `python -B elements/common/foundation_check.py` gave `2 errors` ("the quotation stands in no binding sentence of `WAY-300`", at `task-cycle/test_review_reminder.py:91` and `:136`). That copy is removed.
- Clause `tests:`: names in words what the tests hold (the count since the nearest review tag, from the start of the history where none stands, the main branch's merges into task branches left out; the reminder line turning to yes at the threshold and not one merge before it; one threshold). No path, no test name, no number ("one" is a word and no figure). It matches WAY-12, which asks for the parts of the sentences in words with no path, name or number.
- Pair of examples: the example "the count leaves out the merges of the main branch into task branches" left it, because a test holds it; the cycle's and the request's examples remain (a reminder with no open line, with an open line, an unreadable backlog, a repository with no tag and a count below the threshold). The violating examples that concern the cycle and the request (stops the merge, urges, writes in the first request only, adds a line to the backlog, a product's own number) are not held by a test. Minor finding 1 above is the one exception I could not settle.
- WAY-300's other wording: `git diff -w --word-diff=porcelain 31f7507..e5ae875 -- foundations/decisions.md` shows no change of a word outside *Verification*; the rewrapped paragraph differs by line breaks only. *Rationale* and *Rejected* are whole.
- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- `python -B task-cycle/test_review_reminder.py` — exit 0, 11 tests OK.
- Against `task-cycle/skill/return_step.md`: the commit applies its passage on a pair of examples and the clause `tests:`; it adds no entry, no invariant, nothing the task excludes, and no code. `git status --short` of the reviewed worktree is clean.
- A changed invariant test: none changed.

## Declined to judge

- The lines of WAY-300 *Rejected* over 100 columns: the fix review's Minor finding, which the handoff gives to the cycle's request list, and the return step left them by the handoff. Set aside as outside this commit.

## Reach beyond the dispatch

- `foundations/decisions.md` WAY-300 whole, WAY-12 whole, `foundations/invariants.md` `test-method-citation` (read from line 166), `task-cycle/skill/return_step.md` whole, `task-cycle/test_review_reminder.py` whole, `task-cycle/review_reminder.py` line 48 (`THRESHOLD`) and lines 115-116 — to judge the lines `decision:` against what the tests assert.
- The decision index of my selection (parts `decisions`, `task-cycle`, `foundation-review`, plus WAY-300 and WAY-12) written by `elements/common/decision_index.py` to `.runs/review-return/index.md`; read: the WAY-12 and WAY-300 entries and the lines of the index that mention a pair of examples or a clause.

## Working copies

- `.runs/review-return/wt` (detached worktree of `e5ae875`, for the one-letter check): removed with `git worktree remove --force`, then `git worktree prune`; `git worktree list` no longer shows it.
- `.runs/review-return/index.md` (my index of decisions): a file, not a copy of the tree; stays in the ignored `.runs/`.

## Unread material

The index `.runs/review-return/index.md` (863 lines): I read the entries WAY-12 and WAY-300 whole and searched the rest for the words "pair of examples" and "clause", reading no other decision of it. The part map entries `decisions`, `task-cycle` and `foundation-review` and the guideline files were not read: this commit changes no code and no guideline, and the check of what it touches rests on WAY-12 and the invariant. The return step's report was read whole; the task (`task.md`) was not read.

## Searches not found or unclear

- none. The handoff's "selection of the foundation as `way_of_working.md` gives it" was applied by the script call above; `decision_index.py` takes `--decision WAY-300`, not `--decision 300` (the latter reports "no decision 300"), which the method text, "`--decision NUMBER`", does not show.

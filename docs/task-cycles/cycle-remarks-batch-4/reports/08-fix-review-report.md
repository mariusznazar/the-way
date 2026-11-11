PASS 5841ed7bd951a79a07e49bf5afb01773111a6bcc

# Review of the fix, cycle `cycle-remarks-batch-4`

Variant: a fix (`task-cycle/review/fix.md`, read whole). Range `0d59ce9e4b4e5cd76029c405b878f94cb33df56f..5841ed7`
(`git rev-parse HEAD` = `5841ed7bd951a79a07e49bf5afb01773111a6bcc`; one commit; `git diff 0d59ce9..HEAD` and
`git log --stat` computed myself). Findings file `reports/05-fix-findings.md`, fix report
`reports/06-fix-report.md`, handoff `reports/07-fix-review-handoff.md`, all read whole. The orchestrator's
rulings of the handoff bound the review (I-1 by widening item 15; M-5 the WAY-287 example only; M-6 by
rewording the rationale; M-3 docstring only; M-4 not in the fix).

## Each finding of the findings file

- **I-1 (blocking): fixed.** The request template and the foundation now say the same thing:
  `task-cycle/skill/request_template.md:249-254` (item 15) gives an item for each descriptive `TODO` in an
  invariant's *Rests on* on the tree after the change, whether the change writes, keeps or does not
  remove it, and says a request carries it as long as an old gap stands; WAY-287's binding sentence
  (`foundations/decisions.md:9076-9078`) reads "that stands on the main branch after the change (WAY-71)";
  its rationale (`:9117-9120`) says a `TODO` standing once the change is merged is a gap the merge
  accepts and "while an old gap stands, every request carries it"; WAY-71 (`:1681-1682`) and
  `elements/common/rules.md:20-22` ("a change that leaves one there puts it before the human") are
  unchanged and now agree with the wide reading, since "leaves" = does not remove. The task's sentences
  for To do 6 are untouched (`git diff` shows neither file). A grep of the repository for "diff of the
  invariants", "entry it edits", "does not touch is not", "not the change's" finds no remaining
  narrowing text. The cost the fix takes on (one item in *For you to decide* of every request while an
  old descriptive `TODO` stands) is the orchestrator's ruling and is named in the fix report; the-way
  itself holds no `TODO` in *Rests on*, so it costs the-way nothing today.
- **M-1: fixed.** `task-cycle/skill/SKILL.md:48-50`: "Run the product's gate on that commit as step 10
  gives, at once; ...", rewrapped within 100 columns.
- **M-2: fixed.** `SKILL.md:326-327`: "run the gate on the change as step 10 gives (at once, since no
  return step runs), run `task-cycle/cycle_stages.py`, ..." with the clause set off and the line
  rewrapped; the short line after "The authors' focused checks are not" in step 10 (`:360-364`) is
  rewrapped. No line the fix adds to `SKILL.md` exceeds 100 columns.
- **M-3: fixed (docstring only, as ruled).** `elements/common/foundation_check.py:39-44` now says that
  only a value that begins with `TODO` is read as a missing fact, that a `TODO` item after other facts
  (`clock-tick · TODO`) is not reported, and that the dash after `TODO` is not required. This matches
  what I measured in the first review (`git-state · TODO` gives no bare-`TODO` error; `TODO the store`
  passes). The check itself is unchanged.
- **M-5 (the WAY-287 *Verification* example only): fixed.** `foundations/decisions.md:9093-9105` has a
  *complies* example (a request whose merged tree holds `Rests on: TODO — the store of documents, once a
  task chooses it`, written by the change or standing from before, names the invariant's rule and the
  missing store in the section) and a *violates* example (the section reads `none` while a descriptive
  `TODO` stands on the merged tree). The examples agree with the binding sentence and item 15. The
  *Scope* and *Relations* part of M-5 was outside the task and is not in the fix, as ruled.
- **M-6: fixed.** WAY-160's rationale now ends "The price is that a failure of the gate comes after the
  return step." (`:4582`); the sentence that stated the fix-of-a-failed-gate rule in prose is gone, and
  the *complies* sentence is the task's. The rule stays only in `SKILL.md:361-362`, as ruled; WAY-05's
  concern (a rule that binds later work in prose) no longer applies to WAY-160, at the price I named in
  the first review: no entry holds that rule, so a later edit of step 10 could drop it without
  contradicting an entry. That was one of the two fixes I offered and the ruling chose it.
- M-4: not in the fix, as ruled; remains for the human (a decision about *Based on*). Not a finding of
  this review.

No finding is contested by the author with evidence.

## New findings in the fix diff

none. I looked at what the fix itself could have broken:

- WAY-287's three places and item 15 say one thing; I read them side by side (binding sentence,
  *Verification*, rationale, template item). The binding sentence's "the cycle's choices ... (WAY-71)"
  list and the remark that `none` means nothing else waits stay true.
- The WAY-287 binding paragraph was reflowed; the reflow changes no word other than the three of the
  fix, and the long line that begins "else in the request waits for the human's yes. A blocked request
  ..." was already one line of the same length before the fix (cosmetic, not new).
- One line the fix adds to `decisions.md` is 101 columns (the *complies* example, `:9096`); the file holds
  longer lines already and states no limit for it. Cosmetic, not a finding.
- No code path changed: `foundation_check.py` differs only in its docstring, so the tests of the first
  review still stand.

## Checks

| Command | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `5841ed7bd951a79a07e49bf5afb01773111a6bcc` |
| `git status --short` (reviewed worktree) | 0 | clean |
| `python -B gate/run_tests.py task-cycle` | 0 | 238 tests, OK |
| `python -B gate/run_tests.py elements/common` | 0 | 122 tests, OK |
| `python -B gate/run_tests.py instruction-files` | 0 | 104 tests, OK (5 skipped) |
| `python -B gate/run_tests.py agent-instructions` | 0 | 18 tests, OK |
| `python -B elements/common/foundation_check.py .` (reviewed worktree) | 0 | 0 errors |
| Added lines of `git diff 0d59ce9..HEAD -U0` over 100 columns | n/a | two: the long WAY-287 line that was long before the fix, and a 101-column line of the new *complies* example |
| grep of the repository for the narrowing phrases of item 15 and for "sends the return step back" | n/a | no hit outside the record and `docs` |

Not run: the full gate (the orchestrator's).

## Declined to judge

- The *Scope* and *Relations* of WAY-71 and WAY-287 (the other half of M-5): outside the task, left for
  the human, as ruled.
- Whether *Based on* may read `TODO` on the main branch (M-4): outside the fix.
- Whether a request carrying the same item for as long as an old gap stands is the right trade: the
  orchestrator's ruling, which the fix report states with its cost.

## Unread material

The fix diff, the findings file, the fix report, the handoff and `fix.md`: read whole. The entries the
fix writes (WAY-287 whole, WAY-160's rationale and WAY-71 whole) read whole in the first review and
again at the changed places. No new foundation selection was made for this review: the method bounds a
fix review by the findings file, and the 64 decisions read whole and 109 by title in the amendment to
`reports/04-review-report.md` stand. Nothing of this review stayed unread.

## Searches not found or unclear

none

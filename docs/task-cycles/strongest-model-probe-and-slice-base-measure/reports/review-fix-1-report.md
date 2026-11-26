PASS 15bf941a7e5039bcf0b915794afc56912a4285cb

# Review of fix 1 — strongest-model probe and slice base measure

Range: `60561fba1ca0cbb4d0045f8f407c9cd3f5292d0e..15bf941a7e5039bcf0b915794afc56912a4285cb` (one commit).
`git rev-parse HEAD` in the worktree gives `15bf941a7e5039bcf0b915794afc56912a4285cb`, the head named.
Bounded by `reports/review-whole-findings.md` (I-1, I-2 blocking; M-1 to M-4 Minor within the task) and
the author's `reports/author-fix-1-report.md`. The author contests no finding.

Counts: blocking 0, Minor 0 new, out of scope 0.

## Each finding

- **I-1 — fixed.** WAY-229 paragraph 2 (`foundations/decisions.md:6625-6632`) now reads "In every
  cycle, and again in every later session of its orchestrator, before that session's first dispatch
  of the strongest class, the orchestrator fixes that model by a probe", and every dispatch of the
  class runs on the model fixed "in the session". The *Verification* names a later session's probe
  under *complies* and "a later session of the cycle dispatches the class on the model an earlier
  session fixed, with no probe of its own" under *violates*. In `task-cycle/skill/SKILL.md:448-469` the
  sentence "a session that continues the cycle, a correction's, reads them there" is gone, the probe
  runs "in every cycle and again in every later session of its orchestrator, a correction's included",
  and the model is never taken "from the model an earlier session fixed". The record's *Strongest
  class* (`task-cycle/record_template.md:38-41`) gives the tries per session. `git grep "reads them
  there"` finds nothing. The extension to later sessions follows the reason of the task's answer to
  question 1 and adds nothing the task rules out.
- **I-2 — fixed.** The exception now reads "save a test that an earlier slice's *Goal* announces and
  the slice's own *Checks* hold" in WAY-136's binding paragraph 3 (`foundations/decisions.md:6402-6404`),
  in its *Verification* under *complies* (`6434-6436`) and *violates* (`6447-6448`), in step 9
  sub-step 4 of `task-cycle/skill/SKILL.md:512-513`, and in `task-cycle/change/slice.md:25-27` ("a test
  that an earlier slice's *Goal* announced as left failing, with your slice as the one that repairs
  it, and that your slice's *Checks* hold"). This is *To do* 3's "poza testem z *Checks*
  kawałka-właściciela" and the answer to question 3. A search for the old wording ("a test of the
  slice's *Checks*", "test of your slice's *Checks*", "save a test of the slice's own") finds nothing.
- **M-1 — fixed.** `task-cycle/skill/SKILL.md:455-459` says how the probe's row is found where the tool
  does not name it by its description (by its start in the section of start times, which
  `cycle_stages.py` writes as `## Stages: start, waiting for tools and tokens by model` with a *Start*
  column), and that a model of the candidate's family, an older version included, matches the
  candidate; only a model of another family is a substitution (`SKILL.md:462-463`).
- **M-2 — fixed.** `task-cycle/plan/SKILL.md:189-191`: "its *Goal* names each such test file and the
  slice that makes it pass; the plan writes the same test into the *Checks* of that slice, and no
  slice between the two holds it in its *Checks*."
- **M-3 — fixed.** Binding sentence (`decisions.md:6399-6400`) and *Verification* (`6430`) both say
  the *Checks* of that slice "hold the tests of that file".
- **M-4 — fixed.** Step 12 (`SKILL.md:702-703`) now says "here and in each stop that runs the script",
  and each stop names the step: the question about a test (`SKILL.md:328-329`), a slice failed twice
  (`SKILL.md:530-531`), `task-cycle/skill/blocked_finding.md:15-16` and
  `task-cycle/skill/reserved_return.md:55-57`.

## What the fix itself might break

Nothing found. The fix restates no rule elsewhere in the old words (searches below); WAY-229's
*Rationale* and *Rejected* still agree with the per-session probe; the three references to "the model
the probe fixed" (`SKILL.md:488`, `552`, `616`) read, in a correction's session, as that session's
probe. The binding paragraphs stay within the foundation check's limits. Several rewrapped lines run
past 100 columns (for example `SKILL.md:329`, `decisions.md:6432`, `6450`); the file already holds many
such lines and no check governs it, so I raise no finding.

## Declined to judge

none

## Checks

| Command | Exit | Result |
|---|---|---|
| `git rev-parse HEAD`; `git log` and `git diff 60561fba..HEAD` (full diff, 7 files) | 0 | head as named; one commit |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B instruction-files/check_instructions.py` | 0 | `0 error, 0 warn, 5 info` |
| `python -B gate/run_tests.py task-cycle` | 0 | `OK (skipped=2)` |
| `git grep -n -i "reads them there\|test of the slice's \*Checks\*\|test of your slice's \*Checks\*\|test of its own \*Checks\*\|save a test of the slice's own\|file's tests"` | 1 | no match: no old wording left |
| Manual: `task-cycle/cycle_stages.py:425-530` | — | the section of start times with a *Start* column exists, as M-1's fix relies on |

## Reaches beyond the dispatch

- `task-cycle/cycle_stages.py:425-530` — to check that the section of start times named by the fix of
  M-1 exists.

## Working copies

`.runs/review-fix-1/` held the
log of the test run; removed. No worktree made.

## Unread material

none — the findings file's findings, the fix report and the full diff of the range were read; the
foundation selection of the review of the whole change (`reports/review-whole-decision-index.md`, 4
decisions read whole) stands for this review, and the two entries the fix changes, WAY-136 and
WAY-229, were read again in the diff.

## Searches not found or unclear

none

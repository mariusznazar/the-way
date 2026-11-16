PASS 1a17406aa30fdc0925b79db12c5af3325edfa956

# Review of the fix — agent-test-bypass

Range `c8eef488..1a17406a`, one commit `1a17406a` ("Fix the review's findings: carry both cases of a
question about a test in every restatement"); `git rev-parse HEAD` is
`1a17406aa30fdc0925b79db12c5af3325edfa956`; the worktree is clean. Four files changed:
`foundations/decisions.md`, `task-cycle/change/SKILL.md`, `task-cycle/skill/SKILL.md`,
`task-cycle/skill/request_template.md`.

Counts: 0 blocking, 1 Minor (outside the fix diff, within the task), 0 out of scope.

## The findings of the findings file

**I1 (Important, Contradiction: yes) — fixed.**
- `task-cycle/skill/SKILL.md:20-24`: the early stop now names both cases — "a test that contradicts
  the requirement, or that it cannot pass by code that meets the requirement for every input, is
  settled by no source (WAY-410)" — and the next sentence carries the exception: a failed test is no
  reason to ask the human "save the question about a test that no source settles".
- `task-cycle/skill/request_template.md:570`: the first line reads "a test contradicts the
  requirement, or no general code passes it, and neither the task, the spec, the decisions nor the
  invariants settle which holds" — both cases and all four sources of WAY-410; the ways open now
  give a pair for each case.
- My own search (not the author's script): `grep` for "contradict", "general code", "for every
  input", "question about a test" and "WAY-410" over `task-cycle/skill/SKILL.md`,
  `request_template.md`, `correction.md`, `blocked_finding.md`, `record_template.md`,
  `change/SKILL.md`, `change/fix.md`, `change/slice.md`, `review/SKILL.md`, `review/fix.md` and the
  agent types. Every restatement of the trigger names both cases (`SKILL.md:20-21`, `:311-313`,
  `:472-474`; `request_template.md:570`; `change/SKILL.md:49`, `:91-93`, `:147`); every naming of
  the sources names the four (`SKILL.md:311-316`, `change/SKILL.md:99-100`, the template's first
  line); the other hits name the kind only ("a question about a test", kind 2, `correction.md`) or
  are the unrelated mark of contradiction with the settlements. No narrower restatement remains.

**M1 — fixed.** `SKILL.md:324-328`: "The stages that have not run on this code — of the review of the
whole change, the return step and the reconciliation with the target branch — are named in the
request as not run. Where the question comes in a correction, the request is already open: it
returns to a draft marked `blocked`, and its description is rewritten as the template's variant for
a question about a test gives." `correction.md:57-59` and `:73-76` already give the way on and the
no-wait for CI.

**M2 — fixed.** WAY-409 *Rejected* (`foundations/decisions.md:7393-7395`) now reads "no case is known
in the 83 task cycles of the process's author (his own record, not open to a reader of this
repository)" — the task's figure, the WAY-90 statement, no register and no date.

**M3 — fixed.** Sub-step 4 of step 9 (`SKILL.md:472`, "the paragraph on a question about a test"),
the list of the record's copies (`SKILL.md:811-812`) and the template row (`request_template.md:570`,
"A question about a test is answered otherwise") now name the paragraph that holds the rule.

## The two edits beyond the findings

- `task-cycle/change/SKILL.md:47-50`, section 1: "the expected value of a test that the requirement
  contradicts, or a test you cannot pass by general code, is the case of section 2". A narrower
  pointer I did not report, brought in line with WAY-410; correct, no finding.
- `SKILL.md:472-478`, the no-retry reason: "a stronger class does not settle what the requirement
  is" replaces "does not remove the contradiction", true of both cases; correct. It leaves the
  Minor finding below.

## Findings

### Minor

**N1. `foundations/decisions.md:6957-6959` (WAY-410, *Rationale*) — the reason for no retry is given for the first case only.**
The *Rationale* reads "A slice's executor gets no retry on a class higher because a stronger model
does not remove a contradiction in the requirement". The fix widened the same reason in the skill
to both cases ("a stronger class does not settle what the requirement is", `SKILL.md:475-476`), so
the skill now gives a reason the decision does not. For the second case — no general code passes
the test, no contradiction seen — the decision's prose gives no reason why a stronger model would
not help. Prose, not a binding sentence, and the binding sentence covers both cases, so no reader
is led to a wrong act; Minor. Suggested wording: "because a stronger model does not settle what the
requirement is". Within the task; it lies outside the fix diff (the sentence stood unchanged in
`c8eef488`), so by `review/fix.md` it does not reopen the review.

## New findings in the fix

none Critical or Important.

## Declined to judge

none

## Checks

- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- `python -B .runs/task-cycles/agent-test-bypass/reports/author-fix-restatement-check.py .` — exit 0,
  "restatements failing: 0" (the author's pattern check; my own search above is the check I rely on).
- `python -B -m unittest discover -s task-cycle -p test_request_check.py` — exit 0, 74 tests OK (the
  form check's tests, whose template test reads `request_template.md`).
- Manual: the fix diff read whole; the `grep` search of I1 above; WAY-409 and WAY-410 read whole.
- Not run: the full gate (the cycle's run); the whole `task-cycle` directory (the fix changes no
  script or test; the one test that reads a changed file ran).

## Reaches beyond the dispatch

- `task-cycle/skill/correction.md` lines 55-76 — to judge M1's correction sentence against the way on
  that file gives.

## Working copies

- `.runs/review-fix/` held the outputs of the three
  checks; removed. Nothing kept; nothing remains.

## Unread material

- none. The handoff, `review/fix.md`, the findings file, the fix report, the fix diff, WAY-409 and
  WAY-410 whole were read; `task.md` was read whole in the review of the whole change and not again.

## Searches not found or unclear

none

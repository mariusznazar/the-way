PASS 7f69096

# Review of the fix of C1 — logs-life-and-failure-notice

Range `94d20f3..7f69096`, one commit touching `foundations/decisions.md` alone, WAY-165 alone. `git rev-parse
HEAD` is the head given. Bounded by `reports/correction-review-findings.md` as `task-cycle/review/fix.md`
gives. The author contests nothing.

Counts: 0 blocking, 2 Minor, 0 out-of-scope. The Minor findings of the earlier reviews were not to be fixed
and stand as written there.

## C1: fixed

The defect was that WAY-165 named as a violation, with no limit to a definition, what `task_run.md` now has a
run at a task do. On the new head:

- The binding clause says an entry leaving part of a matter unanswered "does not settle that matter at a project
  definition, while in a run at a task (WAY-267) it holds the choice like any decision, which opens only on the
  human's word" (`foundations/decisions.md:4460-4462`).
- The violating example is limited to "a logs item of a definition's list" (`:4482-4483`).
- A complying example gives the run at a task, "the item over such a decision stays `— held by` until the human's
  word opens it" (`:4477-4478`), and a violating one gives an agent opening it with no word of the human
  (`:4483-4484`).
- `task_run.md:52-57` and WAY-165 now say the same of the same item, and the marker tables' "settles" no longer
  meets an unlimited "does not settle". WAY-165 and WAY-267 no longer collide, so WAY-25 asks for no precedence;
  WAY-267 is untouched, as the human decided.

The binding part keeps three sentences. A definition's behaviour does not change: the template
(`project-level/definition_template.md:174`), `list.md:23-26` and `running_product.md` speak of a definition, or
send a run at a task to `task_run.md`, and a search finds no other account of the clause.

## What the fix itself broke

No Critical or Important finding. I considered one and graded it Minor (1 below).

## Minor

1. `foundations/decisions.md:4458-4462`: the entry of the clause includes "a projected decision of a definition", so
   "it holds the choice like any decision, which opens only on the human's word" also reads on a projected decision,
   which WAY-267 (`:7718`) and `task_run.md:59` say no run reopens at all, whatever the human's word. The two do not
   collide: "opens only on" states a condition and grants nothing, and WAY-267 is the stricter and explicit one, so an
   agent following either reaches spec D6's second reading. "Like any decision" is the loose part. Writing "a decision
   of the foundation" in the second half of the sentence would end it.
2. Form: lines the fix leaves unwrapped, `foundations/decisions.md:4484` (131 characters) and `:4499` (105).

## Note for the request

WAY-165's meaning changes: the Polish sentence in `reports/correction-fix.md` replaces the one in `reports/author.md`.
The task's Context says a logs decision silent on the record's life does not settle the matter, with no limit; that
is now limited to a definition, by the human's decision "poprawmy to", which the request should carry beside the
entry. On the first correction review's Minor 1: with WAY-165 saying a silent decision holds the choice at a task,
a reserved choice is less likely to arise over one, so the seam with `reserved_choices.md` narrows. The rest of that
Minor stands.

## Declined to judge

none

## Checks

- `python -B elements/common/foundation_check.py .`: exit 0, "0 errors".
- `python -B agent-instructions/skill_entry_points.py`: exit 0, "entry points are current".
- `git diff --check 94d20f3..7f69096`: exit 0.
- Manual: read the diff whole against `task_run.md`, the marker tables, WAY-267 and spec D6. Search of
  `project-level` and the foundation files for "does not settle", "settles nothing", "does not hold it" and "holds
  the choice".
- `python -B gate/run_tests.py project-level`: exit 0, 268 tests OK.
- Not run: the full gate, the cycle's own.

## Reaches beyond the dispatch

WAY-267 and `project-level/technology/task_run.md`, to judge the projected case of Minor 1.

## Searches not found or unclear

none

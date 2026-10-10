# Final fix report — m1l5-adoptions

Commit: `d0f6e5b` on `task/m1l5-adoptions` (on top of `9692cbb`).
Files: `foundations/decisions.md`, `project-level/task/skill/SKILL.md`,
`project-level/task/template.md`, `project-level/technology/SKILL.md`,
`task-cycle/skill/SKILL.md`. Line endings stay LF; no added line passes 100 columns.

## Fixes

1. `project-level/task/skill/SKILL.md:81-82` — the check now names "the list WAY-139 holds, in
   `<the-way>/foundations/decisions.md`". The skill already names the-way's root as `<the-way>`
   (line 30, `<the-way>/project-level/readiness_check.py`). The list stays only in WAY-139.
2. `foundations/decisions.md:4156-4157` — WAY-138 *Review when* now reads "the tests run on
   choices other than a place to run give no risk that the comparison of their choice did not
   already show · check by: 2026-12-31". The clause "and the tests then narrow to a place to run"
   is cut. The narrowing already stands in *Rationale* at line 4171-4172 ("Every choice the
   project settles is tested until the tests show they find nothing outside a place to run"), so
   nothing was added there. Binding sentences untouched: fingerprint of WAY-138's binding part is
   `414f7dbd` before and after (`relation-model/fingerprint.py`). The date `2026-12-31` is for
   Mariusz to accept in the request's *What this request settles*.
3. `project-level/technology/SKILL.md:112-113` — step 5: "Write the risks the tests give into the
   choice's report, `.runs/technology/<choice>.md`, so that a resumed step finds them, as step 6
   needs."
4. `task-cycle/skill/SKILL.md:52-54` — "The one exception, the cycle's own record and not an
   effect of the task (WAY-140): in the task's source entry in the backlog …".
5. `project-level/task/skill/SKILL.md:82-84` — "add an item to *To do* for that work and offer
   the human to split it into a task of its own, which step 1 then handles (WAY-139)". The
   orchestrator's line reference (33-37) pointed at the backlog bullet; the wording sits here.
6. `project-level/task/template.md:47` — placeholder now
   `- <action outside the repository, or none> — before the cycle, <done|not done> | in the cycle | TODO`
   (100 columns), using the rule's words `before the cycle` with `done` or `not done`,
   `in the cycle`, `TODO` and `none`.
7. `task-cycle/skill/SKILL.md:266-268` — step 12: "except a request the cycle marks `blocked`, one
   waiting for human actions in the cycle (step 4) included, which stays a draft".
8. `task-cycle/skill/SKILL.md:75-78` — step 4: "…joins that list, for the human to place; where
   the task document places no action in the cycle, the request opens as a blocked draft listing
   that effect."

## Checks

| Command | Exit | Result |
|---|---|---|
| `python -B gate/run_tests.py project-level` | 0 | 81 tests OK |
| `python -B gate/run_tests.py task-cycle` | 0 | 41 tests OK |
| `python -B gate/run_tests.py elements/decisions` | 0 | 169 tests OK |
| `python -B gate/run_tests.py gate` | 0 | 98 tests OK |
| `python -B elements/decisions/format_guard.py --base none --merge-onto none` | 0 | 0 errors, 10 warnings (5 passed check-by dates: WAY-03, 21, 52, 55, 69; 5 `<request link>` placeholders), 5 unchecked |
| `python -B agent-instructions/skill_entry_points.py` | 0 | entry points are current; no `description` changed |

The guard leaves fingerprints unchecked with `--merge-onto none`; they were checked by hand
(fix 2). Only WAY-138's *Review when* changed in the log, so no other fingerprint can change.

## Concerns

- Fix 6 uses `<done|not done>` without spaces to stay within 100 columns.
- Fix 8's new sentence leaves a short ragged line ("effect. Create a new task"), like the
  step's other lines; not rewrapped to keep the diff small.

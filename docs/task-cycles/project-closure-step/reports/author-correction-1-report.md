# Author report — correction 1 (task `project-closure-step`)

**Status:** done. Variant: a correction for the human's remarks. Start head `935109fb`; head after
`4101de84`. Worktree `the task's worktree`, branch `task/project-closure-step`.

## The remark that asked for work (item 2) and what was done

The check refuses a closed plan where following "delivered in another task" never reaches a task that is done.
Items 1 and 3 are let through and 4 to 12 accepted: nothing changed for them; no Minor finding of the reviews was
touched; the check was not widened to the other states of a closed plan.

## Commits

| Commit | What |
|---|---|
| `43e9c4a7` | `plan_check.py`: the delivery check; `test_plan_check.py`: its tests |
| `4101de84` | the sentence of the invariant `project-plan-check`, the plan template, `closure.md` section 1, the lead skill's step-1 bullet, regenerated entry points |

## Files changed

- `project-level/plan_check.py`: new `delivery_ends(by_number)` and `LOOP`; `check_closed` rewritten around
  them (the plan stands at 1081 lines, under 1200); the docstring's `closed` item says it.
- `project-level/test_plan_check.py`: eight new tests in `Closed`.
- `foundations/invariants.md` (`project-plan-check`), `project-level/plan/template.md` (header bullet, the states
  passage, "What the check decides"), `project-level/lead/skill/closure.md` (section 1),
  `project-level/lead/skill/SKILL.md` (step-1 bullet), and the two generated entry points (`.claude/` and
  `.agents/`, same description, regenerated: `entry points are current`).

## How the check follows deliveries, and how it reports

`delivery_ends` settles every task once, with no recursion: it walks `done — goal delivered in task <n>` from a
task, remembers the tasks on the walk, and gives the whole walk the end it reached — the state of the task whose
row is no delivery, `loop` where it comes back to a task on the walk or to one already settled as `loop` (so a
tail leading into a loop and a shared tail are `loop` too), or nothing where it meets a task the plan lacks or a
task delivered in itself (those stay findings of `form`). The work is the number of rows, not their square; a
thousand-row chain is a test.

**Reporting: one finding for each row on a chain that fails, each at its own line** (the same as the check reports
every other row), not one for the row at the start. Reason: the closing and the human meet the finding at the row
they will correct, and a loop has no start; a finding for the start alone would hide the other rows of the loop and
of the chain into it, which are each a delivery nobody made. The message tells whether the deliveries "run in a
loop" or "end in a dropped task"; the message for a row delivered directly in a dropped task is the one it had
before. A row whose chain ends in a row in another state (for example `in cycle`) is not reported for the
delivery: that other row is reported at its own line, as before.

Kept as before: a delivery in a task the plan lacks or in the task itself is `form` alone; a chain that reaches a
`done` task passes; the check runs only in a plan whose first `Status:` line reads `closed`.

## Tests (invariant `project-plan-check`, in `Closed`)

- the pair (tasks 2 and 3 delivered by each other): two findings, each at its row;
- a loop of three, four and seven tasks: one finding at each row of the loop;
- a chain leading into a loop (4 in 3, 5 in 4, with 2 and 3 in each other): findings at 2, 3, 4 and 5;
- a chain of deliveries ending in a done task passes; ending in a dropped task: each row of it (the new finding
  for the first, the earlier one for the second);
- a delivery in the task itself stays `form` alone (cites `project-plan-form`);
- the loop in a plan that is draft or handed over: no finding;
- a chain of a thousand rows: done at its end passes, a loop at its end gives 999 findings, with no recursion.

Failing on the code before the correction, then passing (both runs as command and exit code):

| Run | Command | Exit |
|---|---|---|
| Before (tests of the correction, code of `935109fb`) | `python -B gate/run_tests.py project-level` | 1, 7 failures: the pair, the loops of 3, 4 and 7, the chain into a loop, the chain into a dropped task, the thousand-row loop (log `reports/correction-1-before.log`) |
| After | `python -B gate/run_tests.py project-level` | 0 (log `reports/correction-1-after.log`) |

The three new tests that pass on the base code (a chain ending in a done task, the self-delivery and the
non-closed plan) protect what must not change; they are not claimed to have failed. `test_plan_state.py` needs no
case: the reader runs this check as it runs the rest and its behaviour on a closed plan with a finding is the one
already tested (exit 1, `fail: closed`); nothing in it is new.

## Other checks (command and exit code)

- `python -B gate/run_tests.py product-guidelines`: exit 0.
- `python -B gate/run_tests.py agent-instructions` (formatter, linter, sizes, entry points): exit 0.
- `python -B elements/common/foundation_check.py`: exit 0, `0 errors`.
- `python -B agent-instructions/skill_entry_points.py --write`: `entry points are current` (the description of the
  lead skill is unchanged, so the generator wrote nothing new).
- `ruff format` and `ruff check` on `project-level/*.py` (the Ruff of the main checkout's environment): exit 0, 0.

## Own-work check

Requirement most likely unmet: *a closed plan whose "delivered by" rows lead nowhere to a done task passes, whatever
the crafted shape*. Beyond the tests above I ran crafted rows through `plan_check.check` in a working script: a
delivery in a task the plan lacks (one `form` finding, no `closed`), two rows sharing a number, and a row whose
number is no number: none crashed, and the findings were those of `form`, `dependencies`, `entries` and
`questions` the earlier checks give for such rows. Mutations in my head that a test catches: not remembering the
walk (the thousand-row test is slow only by the clock, and the loops would be found anyway; the
no-recursion promise rests on the code and on the test finishing at all), skipping the tail of a chain into a loop
(the chain test), treating a self-delivery as a loop (the self test), running the check in a plan not closed (the
status test), reporting the start row only (the pair and the loop tests count each row).

## The places that state the rule (search of the whole foundation, WAY-33)

Found and changed: the invariant `project-plan-check` (now: "a task's goal is delivered in another task and
following the deliveries from task to task never reaches a task that is done, because they end in a dropped task or
run in a loop"); the plan template (the header bullet, the passage on states, and "What the check decides"); `closure.md`
section 1 and the step-1 bullet of the lead skill. Found and left: WAY-142's sentence ("delivered in another task"),
which summarises the states and does not restate the dropped-target rule; WAY-411 to WAY-415, WAY-145, WAY-146,
WAY-153 and the part map, none of which restates it; `task-cycle/skill/plan_member.md` ("counts only through that
task's delivery"), which a chain to a done task satisfies. No decision sentence changed, so no test line
`decision:` is touched; the invariant's tests carry `invariant: project-plan-check`.

## Choice of the cycle: the closing holds such a row too

`closure.md` section 1 and the lead skill's step 1 now hold a row `done — goal delivered in task <n>` whose
deliveries never reach a `done` task — ending in a dropped task or running in a loop — as they held a row delivered
in a dropped task: the closing does not start, the agent tells the human which row and that its deliveries end in
a dropped task or run in a loop, and shows no preview; the row is reconciled with the human first, as the plan
template gives. Rejected: leaving the closing to meet the finding only at its last check (the human would accept a
preview built on scope of a task nobody made, the harm item 2 names). **Cost if wrong:** a plan where a human
means a chain that the check now refuses is held at the closing until the human reconciles the rows, one more turn;
the check itself would have refused the same plan after the preview.

## Entries changed (marked, one sentence in English and one in Polish)

| Entry | Marker | Meaning, English | Znaczenie, po polsku |
|---|---|---|---|
| invariant `project-plan-check` (sentence extended) | the cycle's | In a closed plan the check also rejects a goal delivered in another task when following the deliveries never reaches a done task. | W planie zamkniętym kontrola odrzuca też cel dostarczony w innym zadaniu, gdy podążanie za dostawami nigdy nie dociera do zadania zrobionego. |

The extension is carried by the human's remark 2 of the request, not by a row of *Settlements to record*, so it is
marked `the cycle's`. No pair of examples was added; no decision, glossary term, environment fact or part-map entry
was written or changed.

## Reaches beyond the handoff

none beyond what it named: the remarks file and the correction handoff were read; the files of the search above
were read by their passages.

## Working copies

`.runs/author/` held the two gate logs and a crafted-input run; the directory was deleted whole and made again
empty before I returned; the two logs are kept in `reports/` as `correction-1-before.log` and
`correction-1-after.log`. No remainder.

## Unread material

none.

## Searches not found or unclear

none. (The handoff names the loop as "of any length" and the chain "with or without rows leading into it"; both
are covered. A row whose chain ends at a non-final state is reported only at that state's own row: the handoff
does not ask for more and says not to widen the check to the other states.)

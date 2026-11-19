PASS 4101de849b2dfcf8de87d7c05d2d2209922f26d6

# Review of correction 1 — task `project-closure-step`

Reviewed: the correction made for the human's remarks on request 150, range
`935109fba7458cef123b1e2b749a32f48902b34b..4101de84` (two commits, `43e9c4a7` and `4101de84`, six files).
`git rev-parse HEAD` gave `4101de849b2dfcf8de87d7c05d2d2209922f26d6`, the head of the handoff. Method:
`task-cycle/review/SKILL.md` with `task-cycle/review/fix.md`. Read-only: nothing of the reviewed worktree, its
index or its branch was changed.

Changed files of the range (`git diff --numstat`): `foundations/invariants.md` +3 −2,
`project-level/lead/skill/SKILL.md` +4 −4, `project-level/lead/skill/closure.md` +9 −6,
`project-level/plan/template.md` +8 −5, `project-level/plan_check.py` +44 −4,
`project-level/test_plan_check.py` +82 −0.

## The remarks, each as made or not

- **Item 2 (fix in this request): made.** A closed plan in which following
  `done — goal delivered in task <n>` never reaches a `done` task is refused: `delivery_ends` and the third
  branch of `check_closed` (`project-level/plan_check.py:882-900`, `:931-940`) report every row of a loop of any
  length, every row of a chain that leads into a loop, and every row of a chain that ends in a dropped task. The
  test for the pair is `Closed.test_two_tasks_delivered_by_each_other_are_reported_each_at_its_row`; the test for
  a longer loop is `Closed.test_a_loop_of_three_or_more_tasks_is_reported_at_each_row_of_it` (3, 4 and 7 tasks).
  Both fail on the code of `935109fb` and pass on `4101de84` (checks 6 below). An end-to-end run of the whole
  check on 20 000 random closed plans found no plan that passes while some delivery never reaches a done task,
  where the code of the base lets 1006 of 17 319 such plans pass (check 10).
- **Items 1 and 3 (let through, no task): not touched.** The diff changes nothing of the closing step beyond the
  condition under which it starts (`closure.md` section 1, the last bullet of step 1 of the lead skill); section 3
  of `closure.md`, where the existing task document stands, is as it was.
- **Items 4–12 (accepted): not touched as far as the diff shows.** The remarks file does not carry their text
  (see *Searches not found or unclear*); every hunk of the range is about the delivery rule.

The choice Q5 of the orchestrator — the closing does not start on a row whose deliveries never reach a done
task — is judged sound against *To do* 2 and 5 of the task. *To do* 5 makes the check refuse such a closed plan,
and section 7 of `closure.md` requires that the check find nothing after the closing writes; a closing that
started on such a row would show the human a preview and then write a plan the check refuses. The choice extends
the earlier one for a row delivered in a dropped task by the same reasoning and writes nothing; its cost is one
more turn with the human. `closure.md:13-27` and `SKILL.md:88-93` say the same thing as the check.

## Findings

### Critical

none

### Important

none

### Minor

**1. The thousand-row test names a break it does not catch.**
Place: `project-level/test_plan_check.py:1164-1167`.
What is wrong: the comment reads "Break caught: following the deliveries recursively, which a long chain of
crafted rows would overflow, or following each from its start, which would take a million steps." The first half
holds. The second does not: the test asserts no bound on steps or time, so a follow that walks each row from its
own start passes it.
Why it matters: `delivery_ends` promises in its docstring (`plan_check.py:885-886`) that "each task is settled
once ... so crafted rows cannot make it run long", and `plan_check.py` is a trust boundary file. A later rewrite
that loses the shared `ends` keeps every test green; on a chain of 16 000 rows that is 128 million steps where
the present code takes 0.01 s (check 7). The testing guidelines have the author name the break each test catches
(`guidelines/testing.md`, "Choosing the level"), and a reader of this comment believes the linear follow is
protected.
Evidence: the mutant `each_from_its_start` of check 9 (each row followed from its start with its own set of
visited rows, no shared `ends`): `python -B -m unittest test_plan_check` gives exit 0, 142 tests OK. The mutant
`recursive` gives exit 1 with an error in this test, so the first half of the comment is true. The author's
report says the same of its own check ("the no-recursion promise rests on the code and on the test finishing at
all").
A way to fix it: strike the second half of the comment, or assert the behaviour directly, for example by
counting the reads of the rows through a mapping that counts its `get` calls and comparing with a small multiple
of the number of rows.

**2. A row whose State cell reads `loop` is taken for a loop of deliveries.**
Place: `project-level/plan_check.py:879` (`LOOP = "loop"`), `:895` (`ends[current] = task.state`), `:931-938`.
What is wrong: `ends` holds in one value either the raw text of a State cell or the mark of a loop, and the mark
is the string `loop`, which a State cell can hold. For the rows 2 `done — goal delivered in task 3`, 3
`done — goal delivered in task 4`, 4 `loop`, the check prints at rows 2 and 3 "the deliveries from this task
never reach a task that is done: they run in a loop", which is untrue: they end at row 4, whose state is off the
list. With `blocked` in the place of `loop`, rows 2 and 3 get no finding and only row 4 is reported.
Why it matters: only the wording and the count of findings on a malformed row. The plan is refused either way
(row 4 has its `form` and its `closed` finding, exit 1), so no plan passes wrongly; a human who reads the two
findings looks for a loop that is not there.
Evidence: check 8, the plans `state_loop` (4 findings, two of them "run in a loop" at lines 11 and 12) and
`state_blocked` (2 findings, both at line 13).
A way to fix it: a mark no cell can equal (`LOOP = object()`), compared by identity. The constant also stands
between two functions, while the other constants of the file stand at its head.

**3. The comment of an untouched test now says the opposite of the rule.**
Place: `project-level/test_plan_check.py:1058`.
What is wrong: "Task 3 is delivered by task 2, which is done, and task 2's own delivery is not asked." After the
correction the check does ask for the delivering task's own delivery where its row is a delivery too. In this
test task 2 is `done`, so the test itself is right and stays green; only the sentence misleads a reader about
the rule.
Evidence: the line stands unchanged in the range; `plan_check.py:882-900` follows the delivering task's delivery.
The line lies outside the diff; the correction made it stale.

**4. The header bullet of the plan template says "from each" without saying each of what.**
Place: `project-level/plan/template.md:71-72`.
What is wrong: "... and following the deliveries of its rows from task to task reaches a `done` task from each."
Read word for word, "each" is each row of the plan, and a `dropped — approved by human` row reaches no done
task. The other three statements of the rule in the range name the rows exactly (`template.md:117-121`,
`template.md:199-201`, the invariant). No behaviour depends on the bullet; a reader settles it from the passage
on states forty lines below.
A way to fix it: "... and following the deliveries from each row `done — goal delivered in task <n>` reaches a
`done` task."

**5. One line of the lead skill is left 154 characters long.**
Place: `project-level/lead/skill/SKILL.md:93`.
What is wrong: the changed bullet keeps its four lines by joining its last sentence onto the line before it;
the other lines of the bullet are wrapped near 100. It renders the same and no check reads the width of a
Markdown line (line 119 of the same file is 158 characters long), so this is layout alone.

### Outside the task's scope

**6. A task number of more than 4300 digits ends the check with a traceback, not a finding.**
Place: `project-level/plan_check.py:569` (`int(delivered.group("task"))`), and the same conversion at `:546` and
`:524`.
What is wrong: a State cell `done — goal delivered in task 999…9` with 5000 digits matches `DELIVERED_IN`, and
`int` raises `ValueError: Exceeds the limit (4300 digits) for integer string conversion`. The command prints a
traceback and exits 1; `plan_state.py` calls `plan_check.check` and gets the exception.
Why outside: the line is not in the range, and the behaviour is the same on the code of `935109fb`; it entered
with commit `7c52c947`, before this task. It goes beyond the correction and beyond the task; it is named here
because the handoff asks for crafted input at this trust boundary. The exit code is still 1, so the plan is not
taken as passing.
Evidence: check 8, the plan `huge_delivery_number`, at head and at base.

## Declined to judge

- The text of items 4–12 of the remarks: accepted by the human, and not carried by the remarks file, so no
  comparison of the diff with each of them was made.
- Whether the check should also report, at the delivered row, a chain that ends in a row in another state, in a
  task the plan lacks or in a task delivered in itself: the handoff says the check is not widened to the other
  states, and each such plan is already refused at the row where the chain ends (`closed` or `form`).
- Whether the closing step works on a real project: item 1, let through.
- The sentence of WAY-146 that lists what the script checks and does not name the closed plan: it stood so
  before the correction and belongs to what items 4–12 accepted or to the review of the whole change.

## What the review looked at beyond the findings

- **The follow itself.** Each task enters `ends` once; a walk stops at a task already settled or already on the
  walk, so the work is in step with the number of rows and nothing recurses. A walk that comes back to itself
  marks all of it as a loop, tail included; a walk that reaches a settled task takes that task's end, `None`
  (a task the plan lacks, a task delivered in itself) included. Rows without a readable number stay out of the
  map and get no finding of `closed` for a delivery, while their number is a finding of `form`. Two rows holding
  one number: the later one stands in the map, and the earlier one is a finding of `form`.
- **Against the foundation.** The invariant `project-plan-check` (`foundations/invariants.md:262-276`) says what
  the code does: its two cases, a dropped end and a loop, are the two the third branch of `check_closed`
  reports, and a direct delivery in a dropped task is the first of them. WAY-142 and WAY-146 are not changed and
  are not contradicted. No invariant test was changed; eight tests were added to `Closed`, six citing
  `project-plan-check`, one citing `project-plan-form`, one a passing case with no citation, as the two passing
  cases above it.
- **Against the guidelines.** Formatter, linter and size hold (check 4); `plan_check.py` stands at 1081 lines
  and its longest touched function at 39, under the thresholds of WAY-385. No expected value of a test comes
  from the code under test: the rows come from `line_of` over the test's own text. No existing test was changed
  or weakened.
- **Code made for a test.** None: the follow is general, and the random oracle of check 7 agrees with it on
  60 000 sets of rows no test uses.
- **A reserved choice.** None taken.
- **The author's own-work check.** The requirement it names — a closed plan whose deliveries lead nowhere to a
  done task passes, whatever the crafted shape — is where the change is weakest, and its check, crafted rows
  through `plan_check.check`, would catch it unmet. The report holds no walk through the running command; the
  change alters what a user of `plan_check.py` sees, and check 8 ran the command on plan files.
- **The author's claims.** Seven failures before and none after: confirmed (check 6). "The plan stands at 1081
  lines": confirmed. "Entry points are current": confirmed by the tests of `agent-instructions`; the two
  generated entry points are not in the range, though the report lists them under the files changed.

## Checks

Run from `the task's worktree` unless a directory is given.

1. `git rev-parse HEAD` — exit 0, `4101de849b2dfcf8de87d7c05d2d2209922f26d6`; `git status --short` empty before
   and after the review.
2. `python -B gate/run_tests.py project-level` — exit 0, 302 tests OK.
3. `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
4. `python -B gate/run_tests.py agent-instructions` — exit 0, 52 tests OK (formatter, linter, sizes, entry
   points).
5. `python -B gate/run_tests.py product-guidelines` — exit 0, 14 tests OK.
6. In a copy of `project-level` of `935109fb` with the test file of `4101de84`:
   `python -B -m unittest test_plan_check` — exit 1, 7 failures (the pair; the loops of 3, 4 and 7; the chain
   into a loop; the chain ending in a dropped task; the thousand-row test). In a copy of `4101de84`: exit 0, 142
   tests OK.
7. `python -B crafted.py head/project-level` (my script, through `plan_check.check` and `check_closed`) — exit
   0, every expectation held:
   - loops of 2, 3, 4, 5, 9 and 50 rows, a loop written backwards, two loops apart, a loop over every task of
     the plan: a `closed` finding at each row of each loop and nowhere else;
   - a loop with a tail, the tail's rows before and after the loop in the table, and tails shared by several
     rows: every row of tail and loop reported, each with "run in a loop";
   - a chain ending in a done task: none; ending in a dropped task: each row, the direct one with the earlier
     message; shared tails, one to a dropped task and one to a done task: only the first reported;
   - a chain ending in `in cycle`, `ready for cycle`, `to refine`, `waiting for human`: one finding, at that row;
   - delivery in the task itself, a tail into such a row, a task the plan lacks, a chain into it: `form` alone;
     task 0, a leading zero, a full-width digit, trailing words, a negative number: `form` and `closed` at that
     row;
   - two rows holding one number, a number that is no number: refused by `form`, no crash;
   - the same rows under `Status: draft` and `Status: handed over 2026-10-06`: no finding; a handed-over line
     followed by a closed one: `form` alone; `closed` on no calendar date: the rows reported, with `form`;
   - CRLF: the same findings at the same lines as LF, for the pair, the tail and the dropped chain;
   - chains of 1000, 4000 and 16 000 rows ending in a done task, a loop and a dropped task: 0, n − 1 and n − 2
     findings, `check_closed` in 0.0006 s to 0.018 s, in step with the rows; a chain of 16 000 written
     backwards, in both orders of rows: 0.012 s;
   - an oracle that follows each row by itself, on 60 000 random sets of 1 to 9 rows (deliveries, a task the
     plan lacks, self-delivery, rows without a number, other states, shuffled): 0 mismatches.
8. `python -B crafted_cli.py head/project-level work` (my script; it writes plan files and runs
   `python -B plan_check.py <plan>`) — exit 0. The command's own exit codes: the pair, LF and CRLF, exit 1 with
   two `closed` findings at lines 11 and 12, the rows of tasks 2 and 3; the pair in a handed-over plan exit 0;
   a chain to a done task exit 0; a chain to a dropped task exit 1 with "end in a dropped task" at row 2 and
   "delivered in task 4, which is dropped" at row 3; `state_loop` and `state_blocked` as finding 2 gives;
   `huge_delivery_number` a traceback and exit 1, the same with the code of the base.
9. `python -B mutate.py head/project-level head/relation-model mutants` (my script: nine copies, one change of
   `plan_check.py` each, `python -B -m unittest test_plan_check` on each) — exit 0. Caught, exit 1: the tail of a
   chain into a loop not reported (1 test); a recursive follow (1 error, the thousand-row test); a delivery in
   the task itself read as a loop (1); an end in a dropped task not reported (1); a loop not reported (4 tests);
   every walk taken for a loop (10); the closed check run in every plan (77); the finding put at the named
   task's row (2). Not caught, exit 0: each row followed from its own start — finding 1.
10. `python -B property.py head/project-level` (my script, 20 000 random closed plans through the whole check) —
    exit 0: 2681 plans whose deliveries hold, none with a `closed` finding; 17 319 that do not hold, none
    without a finding. The same on the copy of the base: exit 1, 1006 of the 17 319 pass.
11. `git diff --check 935109fb..4101de84` — exit 0.

Not run: the whole gate, as the handoff gives. `ruff` was not run by itself; the tests of `agent-instructions`
run the formatter and the linter.

## Reaches beyond the dispatch

- `foundations/decisions.md`, WAY-142, WAY-146, WAY-379, WAY-382 and WAY-385, each whole: the pointers of the
  handoff.
- `foundations/invariants.md`, the entries `project-plan-form` and `project-plan-check`, each whole.
- `guidelines/coding.md`, `guidelines/coding-check.md` and `guidelines/testing.md`, each whole.
- `project-level/plan_check.py`, `project-level/lead/skill/closure.md` and `project-level/lead/skill/SKILL.md`
  whole; `project-level/plan/template.md` lines 60–129 and 180–209; `project-level/test_plan_check.py` lines
  1–30, 154–270 and the class `Closed`: the reach of the diff.
- `project-level/plan_state.py` lines 620–679: to see that the reader runs `plan_check.check` and holds no
  second copy of the closed check.
- A search of `foundations/decisions.md` lines 5258–5425 (WAY-411 to WAY-415) for a sentence on deliveries, of
  `foundations/part_map.md` and `foundations/glossary.md` for the closing, and `task-cycle/skill/plan_member.md`
  lines 1–11: to check the author's claim that no other place restates the rule. None does.
- `git log -S"int(delivered.group" -- project-level/plan_check.py`: to date the conversion of finding 6.

## Working copies

All in `.runs/review-correction-1/` of the reviewed worktree: copies of `project-level` and `relation-model` at
the head and at the base (`git archive`), nine mutated copies, the plan files of check 8, four scripts of mine
(`crafted.py`, `crafted_cli.py`, `mutate.py`, `property.py`) and three logs. The directory was removed whole
before I returned. One file was made outside it by mistake, the log of check 2 at `%TEMP%\gate_pl.log`, and was
removed right after the run. No remainder.

## Unread material

none. Of the record directory I read only the files the handoff names: the handoff, the remarks, the author's
report of the correction and `task.md`.

## Searches not found or unclear

- The text of items 4–12 of the remarks is not in `correction-1-remarks.md`, which says only that they are
  accepted; whether the correction touches what one of them accepts could be judged only from the diff, which
  holds nothing but the delivery rule.
- The handoff refers to "the same paragraph on working copies as in the earlier handoffs"; those handoffs are
  not mine to read, so I followed the three things the handoff itself says: make nothing outside the directory,
  remove it before returning, state it in the report.
- No rule on the width of a line of a skill's Markdown was found in the tests or the guidelines (finding 5 is
  therefore layout alone).

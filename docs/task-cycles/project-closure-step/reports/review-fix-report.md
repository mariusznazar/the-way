PASS d4cfe7105964f38e11db4f4bd6db91136bafe8f7

# Review of the fix of the review's findings — task `project-closure-step`

Range: from the reviewed head `ee85f143fd43c01a94f46511680a8c2f3cb87db9` to
`d4cfe7105964f38e11db4f4bd6db91136bafe8f7` (`git rev-parse HEAD` gives it), three commits `95d42e9a`,
`836be8a0`, `d4cfe710`, 11 files. The findings file `reports/review-whole-fix-findings.md` bounds the
review: I1 to I5 and the Minor findings 1 to 9. Paths below are relative to the root of the worktree.

Result: each of the five blocking findings is fixed, each of the nine Minor findings is fixed, one of
them (Minor 8) with a remainder of two words. The fix diff holds no new Critical or Important finding.
Four Minor notes, new in the fix diff or remaining, go to the request's list.

## The findings of the file

| Finding | Verdict | Evidence on the new head |
|---|---|---|
| I1 | fixed | `project-level/lead/skill/SKILL.md` lines 88–93: the last bullet of step 1 now holds the instruction itself — "Where a row stands in another state, `in cycle` and `ready for cycle` among them, or is delivered in a dropped task, the closing does not start: tell the human which row, by its number and name, and in which state, or in which dropped task, holds it." An agent with a row that is not final meets it without opening `closure.md`. |
| I2 | fixed | The condition of reading in `SKILL.md` (lines 88–90) and of starting in `closure.md` (lines 13–16) is now "`done`, `dropped — approved by human` or `done — goal delivered in task <n>` with a task n that is not dropped"; `closure.md` lines 18–22 holds such a row as a row in another state and has it "reconciled with the human before any preview, as the plan template gives". Nothing is counted, shown or written on a row the check of a closed plan would refuse. The plan template says the same at lines 68–72 and 117–119. |
| I3 | fixed | `closure.md` lines 46–56: "Then read the text of what the search finds and compare it with the projected change", with the reason, and a third result, "an entry stands under that identifier or term and does not hold the projected change: write that it stands at the commit without the change, and which part is missing"; the doubtful hit now also covers a hit that cannot be told "to hold the change". |
| I4 | fixed | `foundations/decisions.md` lines 5352–5359 (WAY-414): the binding sentences now give the key for every kind ("by the question the heading of a decision holds or by the identifier or term of any other entry"), the comparison, the third result and the doubtful hit; the *Rationale* (5379–5382) no longer says that every heading is a question. The passage the author's report quotes is word for word the text of the entry. Compared in both directions with `closure.md` lines 43–56: every result and the comparison the entry names are in the file, and every result of the file is in the entry. One key of the file is named in the entry's example and not in its binding sentence; see note 1 below. |
| I5 | fixed | `closure.md` lines 76–79: "the closing makes no second document in silence: the preview shows the existing document, with its path, its `Status:` and its `Project relation:`, and asks the human which document stands. The existing document is changed only as the human says in the preview." Lines 72–75: the line links the new document "only where those rules allow it and the preview shows it". Lines 88–90: the section in the note and the new document refer to the existing document, a new document under *Context*. Lines 126–127: the preview holds "each existing task document of section 3 with its question". The pair of examples of WAY-415 (lines 5407–5414) carries the case. |
| Minor 1 | fixed | (a) `project-level/test_plan_state.py` line 516 asserts that the output holds no `repository:` line; with `return 0` removed after the `closed:` line of `plan_state.py`, the test now fails (run below). (b) `project-level/test_plan_check.py` lines 1083–1092, `Closed.test_the_first_status_line_decides_whether_the_plan_is_closed`, a row `in cycle` under each order of the two lines; with `closed_date` reading the last line, it fails (run below). (c) The comment at lines 503–506 gives exit code 0 as the one of a closed plan. (d) The author's report is corrected: the two tests pass on the base code and are held by mutation. |
| Minor 2 | fixed | `closure.md` lines 36–39: one case, "each projected entry whose `Written by` cell names it, even where a finished task also realizes the entry". |
| Minor 3 | fixed | `project-level/task_line.md` lines 3–5 name the closing among the readers; lines 29–32 say that the project orchestrator makes the line and that it "carries no identifier derived from the plan and no dependencies, as the line of a task that belongs to no plan does". |
| Minor 4 | fixed | WAY-415, lines 5396–5398: the decision prevails "for the first body only; once a refiner has taken the document up, its body is the refiner's"; the sentence no longer says that WAY-154 governs the refinement. |
| Minor 5 | fixed | `closure.md` lines 104–107: "four nested items, each of the last three reading `none` where nothing is to list. The words `project closed` and the labels before each colon are markers kept in English; the rest is in the language of the plan"; the last label reads `projected entries a dropped task was to write`. |
| Minor 6 | fixed | `project-level/plan/template.md` lines 117–119 name the three states. |
| Minor 7 | fixed | `closure.md` lines 61–62: "The closing writes the move itself, only after the acceptance of section 6." |
| Minor 8 | fixed, with a remainder | The state is "dropped" in the skill's description, the part map, `closure.md`, the template and WAY-411 to WAY-415, and the third place is "given up for good". Two words stayed: note 2 below. |
| Minor 9 | fixed | `project-level/plan/template.md` line 198 cites the check of a closed plan to "WAY-142, WAY-146". |

The author contested no finding.

## The two choices of the orchestrator and the passage of WAY-414

1. **Q3 (I2).** The fix carries it out, and it agrees with the task: *To do* 2 gives the three states as
   the condition without which the closing does not start ("dopiero wtedy"), and a further hold does not
   go against it; it is the condition that row 4 and *To do* 5 have the check report in a closed plan,
   now tested before the preview. How the human settles such a row is left to the human, as the plan
   template gives ("reconcile the plan before treating it as a satisfied dependency"); the author names
   that in the report.
2. **Q2 (I5).** The fix carries out the reading I named and settles nothing in the human's place: it
   asks. It agrees with row 6 (no second line, no second section), with *To do* 6 (the whole shown
   before any write) and with WAY-413. Note 3 below is what it leaves open.
3. **WAY-414.** The added passage is an addition to row 5 (the key of the four kinds without a question,
   the comparison, the third result) and the author marks it the cycle's, with the passage quoted word
   for word and the two new examples named. The table of meanings earlier in the author's report still
   gives WAY-414 the one sentence of the first round ("by the entry's question", two results); the
   sentence the request puts before the human has to give the entry as it now reads.

## Minor notes for the request's list (none blocks)

1. New in the fix diff, within the task — `foundations/decisions.md` lines 5352–5354 against
   `project-level/lead/skill/closure.md` lines 44–46. For a change of a current decision the file
   searches by "its number"; the binding sentence of WAY-414 gives a decision "the question the heading
   … holds" and the identifier to "any other entry". The heading of such a change holds both
   (`<PREFIX>-<NN> — <question>`), both lead to the same decision, the comparison follows either way,
   and the entry's own complying example speaks of "a change to a current decision whose number stands
   without the change", so I grade it Minor and not a restatement of the entry: a reader of the binding
   sentence alone would search by the question and reach the same result. Naming the number in the
   sentence would close it.
2. Remaining of Minor 8, within the task — `foundations/decisions.md` line 5271 (WAY-411, "moves the
   tasks the human withdrew") and line 5321 (WAY-412, *Rejected*: "only two places, a task of its own
   or dropped"), where "dropped" is the third place, which every other line now calls "given up for
   good".
3. New in the fix diff, within the task — `project-level/lead/skill/closure.md` lines 76–79 and 85–97.
   Where the human answers that the existing document stands, the file does not say where the goal, the
   questions and the entries travel, nor whether that document takes `refining` and `source only`: "The
   existing document is changed only as the human says in the preview". WAY-415 gives the body of a
   document a refiner has taken up to the refiner (lines 5396–5398 and its violating example), so the
   human's word in the preview could ask of the closing what the entry gives to a refiner. The preview
   shows whatever is proposed before it is written, and the case is one the request puts before the
   human, so nothing is written unseen.
4. Outside the fix diff — `project-level/task_line.md` line 15 still reads "Where the task has no line
   in the task place, a refiner makes one. This is the one place of the rule", sixteen lines above the
   new item that has the project orchestrator make one at the closing. The new item is in the same
   section, so the reader meets both.

## What the fix itself changed, and broke nothing

- Code: one line of `project-level/plan_state.py` (the help of the first argument). The crafted inputs
  of the first review, run again on the new head, give the same 156 lines of output as on `ee85f143`.
- Tests: one invariant test added, `Closed.test_the_first_status_line_decides_whether_the_plan_is_closed`
  (cites `project-plan-check`), and one assertion added to a reader test; to be named in the request
  with the others (WAY-03). Its expected values come from the description of `closed_date` ("the first
  `Status:` line") and from the template ("It stands once"); no code is made for the test's input, and
  no assertion of an earlier test is weakened.
- The skill's description changed by one word; the two entry points are regenerated and current.
- The heading of WAY-412, WAY-414 and WAY-415 changed by the word "dropped"; references go by number.
- No function or file grew over a threshold: no script but the one line above changed.

## Declined to judge

- How the human settles a row delivered in a dropped task (by changing the row, or by naming the task
  that delivered the goal): the task does not say, and the file leaves it to the human.
- Minor 10 of the first review (rows delivered in a ring): outside the task and not in the findings
  file.

## Checks

| Check | Command or method | Result |
|---|---|---|
| Head of the range | `git rev-parse HEAD` | exit 0, `d4cfe7105964f38e11db4f4bd6db91136bafe8f7` |
| Whitespace of the fix diff | `git diff --check ee85f143..d4cfe710` | exit 0 |
| Sizes of the changed files | `python -B task-cycle/change_file_sizes.py ee85f143 d4cfe710` | exit 0 |
| Tests of the directory | `python -B gate/run_tests.py project-level` | exit 0, 294 tests |
| Foundation check | `python -B elements/common/foundation_check.py` | exit 0, `0 errors` |
| Linter, formatter, size and entry-point tests | `python -B gate/run_tests.py agent-instructions` | exit 0, 52 tests |
| Dead pointers of the skills | `python -B gate/run_tests.py product-guidelines` | exit 0, 14 tests |
| Entry points current | `python -B agent-instructions/skill_entry_points.py` | exit 0, `entry points are current` |
| Tracked private paths | `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` | exit 0 |
| Mutation: `closed_date` reads the last `Status:` line | in a worktree of the head, `reversed(preamble)`, `python -B -m unittest test_plan_check` | exit 1: caught by the new test (1 failure of 134 tests) |
| Mutation: the reader goes on after the `closed:` line | in the same worktree, `return 0` removed, `python -B -m unittest test_plan_state.Command.test_a_closed_plan_is_reported_closed_and_proposes_nothing` | exit 1: caught (both subtests fail) |
| Crafted input at the trust boundary, again | `python -B review-whole-crafted-inputs.py <worktree of the head> <output> <scratch directory>` and `diff` with `review-whole-crafted-inputs.txt` | exit 0 and 0: the same output as on the reviewed head |

Not run: the whole gate, by the handoff.

## Changed files of the fix (lines before → after)

`.agents/skills/the-way-lead-project/SKILL.md` 15 → 15; `.claude/skills/the-way-lead-project/SKILL.md`
15 → 15; `foundations/decisions.md` 11575 → 11586; `foundations/part_map.md` 297 → 297;
`project-level/lead/skill/SKILL.md` 202 → 204; `project-level/lead/skill/closure.md` 136 → 150;
`project-level/plan/template.md` 203 → 205; `project-level/plan_state.py` 709 → 709;
`project-level/task_line.md` 68 → 73; `project-level/test_plan_check.py` 1309 → 1320;
`project-level/test_plan_state.py` 1033 → 1035. I changed no file of the worktree.

## Reaches beyond the handoff

None beyond what the first review reached: I read `closure.md` on the new head whole, the entries
WAY-411 to WAY-415 on the new head whole, and the changed lines of the other files in the diff.

## Working copies

Under `.runs/review-whole/`: a worktree of the head (`head`), in which the two mutations were made and
taken back, removed with `git worktree remove --force` and `git worktree prune`; the scratch directory
of the crafted inputs, their output and the logs of the runs, all deleted; the directory stands empty.
Nothing new is kept in `reports/` but this report. No remainder.

## Unread material

The fix section of the author's report, the findings file, the handoff and `task-cycle/review/fix.md`
were read whole, and the fix diff whole. Not read again on the new head: the files the fix did not
change, and of the changed files `project-level/lead/skill/SKILL.md`, `project-level/plan/template.md`,
`project-level/task_line.md` and the two test files beyond the lines of the diff and their neighbours.
No decision was opened beyond WAY-411 to WAY-415; the selection of the first review stands.

## Searches not found or unclear

- What the closing does where the human answers that the existing document stands: not in the file
  (note 3).
- Leftovers of the earlier word: searched `project-level/`, `foundations/` and the entry point for
  `withdrawn`, `withdrew` and `dropped for good`; the one hit that belongs to the change is line 5271
  of the decisions (note 2). The other use of note 2 was found by reading WAY-412.

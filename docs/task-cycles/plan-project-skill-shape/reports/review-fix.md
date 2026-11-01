PASS 1fa823e32d04a6cd55b23d05603915e81efbf0c4

# Review of the fix: plan-project in the WAY-256 shape

Fix range `db3845c..1fa823e` (one commit, 2 lines of `existing_plan.md`), with the regenerated
`reports/assessment.md` and `reports/word-counts.md`. `git rev-parse HEAD` gives
`1fa823e32d04a6cd55b23d05603915e81efbf0c4`, the head given. Bounded by `reports/findings.md`
(`task-cycle/review/fix.md`).

Blocking: 0. New Minor: 2. Out of scope: 2 (the lines of Declined to judge). Minor findings 2 to 5
of `reports/review.md` stand for the request; the fix did not change them and I did not judge them
again.

W = `C:/Storage/repos/the-way/.runs/worktrees/plan-project-skill-shape`.
C = `W/.runs/task-cycles/plan-project-skill-shape`.

## Finding 1: fixed

The defect was one instruction given two effects. It no longer exists:

- **The sentence.** `W/project-level/plan/skill/existing_plan.md:15-16` now reads "a session that has
  not been through `read.md` beside this skill (step 1) yet goes through it before it goes on". An
  agent cannot read that as seeing the file and leaving it. The wording follows the precedent
  `W/product-guidelines/testing/SKILL.md:79-81`.
- **Step 1.** `W/project-level/plan/skill/SKILL.md:48-49`, unchanged, now agrees: a session that went
  through `read.md` at step 0 had it read and has nothing left, and a session that did not does all
  of it. The empty step of routes 4, 5a and 7 is gone, since the work was done at step 0.
- **`C/reports/assessment.md:81`.** "does not make step 1 run" is gone; the line says the session
  carries `read.md` out. Searched for the rejected reading in both materials: no line left. The hits
  for "not run", "not read" and "step 1 runs" are other matters (`word-counts.md:7`, `:196`, `:246`,
  `:376`, and quotes of the base).
- **`C/reports/word-counts.md`.** The rule stands at `:8-9`, the route notes at `:148` and `:335`,
  routes 3 and 6 are counted with step 1 carried out in both states, the literal base stands beside
  them at `:26-31`, and `:41-42` correct the range and say what the task's 170 words cover.

Both horns of the finding are closed: routes 3 and 6 no longer stand on the outcome question 3 turned
down, and the same reading now holds on routes 3, 4, 5a, 5b, 6 and 7.

## The fix compared by what it selects and switches off

Old "has not read ... reads it"; new "has not been through ... goes through it". Only the verb moved,
twice; the condition "whichever step the plan goes on from" and the reason are unchanged. Checked with
the diff and with my own clause comparison: 144 clauses of the base, the same 3 not verbatim, 36 new,
the one changed clause being this sentence.

- **Selects:** every session on an existing plan that has not done step 1. Against the old words it
  adds only a session that read the file without carrying it out. Nothing else enters.
- **Switches off:** a resumed draft, a hand-over turn or a narrow turn passing step 1. Against the
  literal base that is a route added: the base sent a resumed draft past step 1. It is the one the
  task's question 3 chose and choice C4 of the cycle states, and `assessment.md:81` and
  `word-counts.md:9`, `:28` say so openly. It is within To do 5, which the first acceptance criterion
  exempts.
- **Loses:** nothing. No sentence moved, and no pointer changed.
- **Collisions checked:** `read.md:3-5` has a finding return the definition and the breakdown wait.
  With a definition changed after its gate, `existing_plan.md:7-9` already sends it there. With the
  gate passed anew, the check reports nothing. `lead/skill/SKILL.md:29-30` already has every dispatched
  actor repeat the foundation reading. No contradiction.

No new Critical or Important finding.

## Figures, recomputed from the files

Commits 2f51e6c and 1fa823e exported, my own script, then the two routes by hand.

| Route | Skill text after | Total after | Before, step 1 in both | Change | Before, literal | Change |
|---|---|---|---|---|---|---|
| 3 | 1949 | 6502 | 6897 | -5.7% | 5264 | +23.5% |
| 6 | 1730 | 6871 | 7485 | -8.2% | 5852 | +17.4% |

All hold. So do: 183 per-file figures and all sums and percentages of the 8 route versions, 0 differ;
`existing_plan.md` 187; the twelve files 3047; 5b +703 (+30.0%); 1774 = 141 + 492 + 1141; the ranges
-26.2% to +30.0% and -8.2% to +9.4%. The task's own figures at `word-counts.md:43` are unchanged. One
figure does not hold: finding 6.

Order: `existing_plan.md` written 09:25:40, `word-counts.md` 09:26:26, `assessment.md` 09:26:34,
commit 09:28:09.

## The walk, with the new sentence

**Route 3, resume of a draft from step 5.** `SKILL.md`; step 0: template, "How a skill asks"; plan
named, `existing_plan.md` and the reading file; `plan_check.py`; inventories; the draft goes on from
step 5; before it goes on the session goes through `read.md`: readiness check, the definition by the
reading file it already holds, the foundation, the product's files as far as needed, the guidelines.
Then step 5, whose list gives what steps 2-4 left; steps 6, 7. Falls away: `cut_tasks.md`,
`guideline_tasks.md`, `assign_entries.md` unless a pair is reported, `place_questions.md`,
`delegated_mode.md`. Rule not reached: none. A guidelines finding met here, with step 2 finished, has
`SKILL.md:53-58` in view, which names the file and the condition.

**Route 4, human's correction, a split.** Step 0 as above, with `read.md` gone through there. Step 1:
"unless step 0 had you read it", nothing left, and nothing lost. Step 2: `cut_tasks.md`, whose
guidelines condition can now be judged, the reading being done. Steps 3, 5, 6, 7; step 4 where a
question moves. Falls away as before. Rule not reached: none.

## Minor

### 6. One figure the fix changed stands stale, and its table omits it

**Anchor:** `C/reports/assessment.md:30` (row L52-L58), `C/reports/fix.md:28-38`, `C/reports/author.md:19`.

**To paste:** The row says "cost: 185 words of the file"; `existing_plan.md` now has 187 words, and the
fix's table of replaced figures does not list it.

**Why I report it:** The fix added two words and the generator holds this figure as text. Nothing
depends on it, and every other figure was regenerated. Cost of the fix: one number and one table row.
Left: the request carries 185 here and 187 in `word-counts.md`.

### 7. The rule's evidence covers less than the figure it justifies, and a few small slips

**Anchor:** `C/reports/word-counts.md:9`, `:148`, `:335`; `C/reports/fix.md:13`;
`C/tools/verify_counts.py`.

**To paste:** The rule cites 14 of 14 readiness checks and 11 of 14 foundation reads for counting step
1 in the state "before", but `product-guidelines/reading.md` is counted there too, and no recorded
session reached the product's `guidelines/`. Say so.

**Why I report it:**

- The task's Context says none of the 14 sessions reached `guidelines/`. So the 1141 words of
  `reading.md` in the state "before" are what the text asks, not what the evidence shows, and
  `fix.md:13` "adds no route that a session ... did not take" overstates for that reading. The
  like-for-like figures -5.7% and -8.2% hold, because both states count the same words, and the
  literal reading gives the other bound, so no conclusion moves. I recommended counting both states
  in finding 1 without this remark; half a sentence closes it.
- `word-counts.md:9` says "the table above" of a table that stands below; `:148` and `:335` say "the
  rule below" of a rule that stands above.
- `verify_counts.py` did not change, so it compares no figure of the new section `:26-31`, nor the
  comparison's prose. The acceptance criterion asks it to compare each stated figure. I recomputed
  them all and they hold, and the generator builds the section's figures from the same counts; the
  gap is in the helper, not in a number. The same held of the comparison's prose at the first review,
  where I passed that criterion.

## Declined to judge

- Whether "goes through" needs an entry of its own in the foundation: the task's question 3 says the
  pointer gets no row of *Settlements to record*, and the stronger verb is the return step's to weigh.
- Whether `author.md`'s route notes should be edited rather than replaced by the table in `fix.md`:
  the fix's handoff asks for the table, and the request's form is the orchestrator's.

## Checks run

| Command or method | Exit | Result |
|---|---|---|
| `git rev-parse HEAD`, `git show --stat 1fa823e`, `git diff db3845c..1fa823e` | 0 | head as given; one file, 2 lines; nothing else tracked changed |
| `git status --short`, `git ls-files --eol` on the file | 0 | clean; LF |
| `python -B <scratchpad>/rv/check_counts.py` (own) | 0 | 183 file figures, 8 route versions, 0 differ |
| hand computation of routes 3 and 6, both readings, and 1774 and 703 (own script) | 0 | as in the table |
| `python -B <scratchpad>/rv/check_assessment.py` (own) | 0 | 34 rows, 0 bad, 179 lines each once, words sum 2344 |
| `python -B <scratchpad>/rv/compare_all.py` (own) | 0 | 144 clauses, 3 not verbatim, 36 new |
| `python -B tools/verify_counts.py reports/word-counts.md` (author's, second reading) | 0 | 279 compared, 0 differ |
| search of both materials for the rejected reading and for stale figures | n/a | no reading left; one figure, finding 6 |
| search for `existing_plan` in every Python file of the repository | 1 (no match) | no test or script reads the changed file by name |
| manual: routes 3 and 4 | n/a | above |

Not run: the whole gate (the orchestrator's). `gate/run_tests.py project-level` was not repeated: the
fix report gives exit 0, the fix is two lines of Markdown no test reads, and the gate on the new head
is the orchestrator's next run. `foundation_check.py` and `check_instructions.py` were not repeated:
the fix touches neither `foundations/` nor a root instruction file.

The review changed nothing in the reviewed worktree beyond this report.

## Reach beyond the dispatch

`C/cycle.md:68` (choice C4) and `C/tools/word_counts.py`, to see what the choice says and how the new
figures are made. The task's *Context* in `C/task.md`, already read, for finding 7.

## Searches not found or unclear

none

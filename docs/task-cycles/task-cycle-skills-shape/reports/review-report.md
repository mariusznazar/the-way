PASS 7369993885567d683ef7b7a8b08933318c21ed4d

# Review of the whole change — task `task-cycle-skills-shape`

- Range: `cf11541f039649db3a76aa5aaa2d7cce2cc48f34..7369993885567d683ef7b7a8b08933318c21ed4d`, 12 commits
  (`git log cf11541..HEAD` lists 12 commits; the handoff says 13) and 67 files. `git rev-parse HEAD` gives
  `7369993885567d683ef7b7a8b08933318c21ed4d`, which is the head I was given. The worktree is clean.
- Method: `review-change`, read from `.runs/the-way-base/task-cycle/review/SKILL.md`. That copy is
  byte-identical to `cf11541` (checked with `git show cf11541:<path> | diff -q - .runs/the-way-base/<path>`
  for the five files I compared).
- Blocking findings: **0**. Minor: **5**. Out of scope: **4** (2 findings and 2 lines of Declined to judge).

## What I checked against the task

| Task item | Result | Evidence |
|---|---|---|
| To do 1: WAY-125, and `implement-task` stops telling stage agents to read everything at the start | met | `foundations/decisions.md:2839-2875`. `task-cycle/skill/SKILL.md:61-66` (step 3). The handoff paragraph at `:124-145`: "no handoff tells it to read at the start every file its method names". A grep for "what it names, whole" or "every file it names" in the process text finds nothing outside the two *violates*/*Rejected* lines of WAY-127. |
| To do 2: the exception in WAY-256 and `kind_skill.md` | met | `foundations/decisions.md:7250-7303`; `instruction-files/kind_skill.md:16-21`. The rule stands only there, as WAY-258 requires: `grep "one instruction" instruction-files/` finds only `kind_skill.md`. |
| To do 3: the generator's sentence, its test, and all entry points regenerated | met | `agent-instructions/skill_entry_points.py:175-177` and `test_skill_entry_points.py:53-54`. `skill_entry_points.py` prints `entry points are current`. The 42 entry points each change one line; `git diff ... \| sort \| uniq -c` shows each pair the same. |
| To do 4: each of the five skills judged and rebuilt | met, with Minor M1 and M2 | Slice reports 7–11, (a) tables with WAY-257's two answers in every row. Files beside the skills: change `slice.md`, `fix.md`, `ui_check.md`; spec `design.md`, `review.md`; plan `too_large.md`; review `whole_change.md`, `fix.md`; skill `plan_member.md`, `spec_review.md`, `planning.md`, `foundation_step.md`, `return_step.md`, `blocked_finding.md`, `correction.md`. |
| To do 5: `make-change` in the example's layout, rows 5, 9 and 22 in `SKILL.md` | met | `task-cycle/change/SKILL.md:19-26`. Two departures from the example's layout line are named, with reasons, in the Slice 7 report, rows 15 and 19: the insets about a slice stay in place. |
| To do 6: the request shows the tables, word counts and proposals | not judgeable at this head | The request is not written yet. The material exists in sections (a)–(c) of slice reports 7–11. |
| To do 7: agents read their methods from the base copy | met | Every `*-handoff.md` names `.runs/the-way-base/`, and the base copy matches `cf11541`. |
| Acceptance criterion 1: Python changes only in the sentence and the assertion | met | `git diff --stat cf11541..HEAD -- '*.py'` lists two files, +5 −3, which are the sentence and `DECISION_ENTRY`. |
| Acceptance criterion 2: no rule disappears or changes meaning beyond To do 1–3 | met | My own sentence comparison over all five skills (see Checks). Every line it prints is a heading merged with its paragraph, a pointer, a row of the table of variants, a reworded clause that keeps its meaning, or one of the To do 1 changes in `implement-task`. |
| Settlements rows 1–3 | met | WAY-125, WAY-127 and WAY-256 as cited above. |
| Questions carried to the cycle | answered | The foundation step and the return step now stand in files beside the skill, named by the handoff (`SKILL.md:137-141`, `:237-241`, `:314-316`). `record_template.md` was judged for its place only (Slice 11, row 45). |

For each file beside a skill, I checked that its pointer stands at the step or variant that needs it:

- `grep` finds each file named in its skill's `SKILL.md`, and `ls` shows no unnamed file.
- No file beside a skill points to another file beside it.
- The full paths in `implement-task` resolve: `task-cycle/skill/<file>.md` in the pinned the-way.

How I judged the slices that had no review of their own:

- **Foundation entries, Slices 1 and 2–6.** Each matches its *Goal*. Slice 2's own-work check is the right one: the phrases the gate test requires, which the gate run confirms. The assertion was seen failing first, and I repeated that as a mutation check (below).
- **Slices 7–11.** Each executor's own-work check is the sentence comparison. That fits where these slices are weakest, a lost sentence. It does not catch the second weakness, a pointer placed at a moment the agent passes by. I checked that one by hand, pointer by pointer.

Choices I weighed and accept, with no finding:

- **C19: WAY-125 covers every file a method names, not only a file beside it.** That is wider than settlement row 1. But To do 1 itself says "wszystko, co metoda wymienia", and the other files the stage skills name are read at their step anyway: `product-guidelines/reading.md` and `elements/common/way_of_working.md`.
- **The base clause "with the element skills it names" became "the skill of an element when it writes an entry of that element".** This is the To do 1 change applied to the handoff paragraph, as Slice 11's report says.

## Findings

### Critical

None.

### Important

None within the task.

### Minor

**M1. `task-cycle/skill/SKILL.md:37-60` (moving the pin, step 2) and `:253-295` (step 9, sub-steps 1–5 of the planned route) stay in `SKILL.md`, though only one route needs each.** Slice 11 commit `7369993`.

- What is wrong: these are about 900 words, several instructions each, that a one-author cycle with no pin move reads without needing them. To do 4 places such fragments in a file beside the skill. WAY-256's *violates* line also names "a step keeps several instructions only one variant needs".
- The executor's reasons, Slice 11 report, *Choices* 1:
  - moving the pin names `installation/README.md`, which would become a second level;
  - the one-author bullet borrows its rules on model classes from sub-step 2.
- My judgement: the first reason holds under the plan's *Common* point 5. The second can be met by a meaning-preserving rewording that keeps only the shared class sentence in `SKILL.md`. That is the kind of rewording the task's fifth answer allows.
- Why it is Minor: nothing is lost (acceptance criterion 2 holds), the choice is named, and the layout is the cycle's to make (task, *Questions to settle* 3). The human sees it in the request.
- Recommended: the request lists it beside Slice 11's proposals (b) 1–2.

**M2. `make-change`'s slice variant now reads more than before: 1 820 words against 1 777.** Slice 7 commit `9b776fe`.

- What is wrong: the most frequent use of `make-change` in a planned cycle reads 43 more words, not the roughly 1 650 the example predicted.
- Evidence: Slice 7 report, 7c (`wc -w`: `SKILL.md` 1619, `slice.md` 201).
- Causes:
  - the table rows describe what each file holds;
  - the stub of section 4 (`SKILL.md:93-95`) repeats the pointer the table already gives;
  - the two insets about a slice stay in place.
- Why it is Minor: WAY-256 places fragments by need, never by word count, and no rule is lost. But the measured cycle on `loop2` will show no gain for this skill, and the request should say so plainly rather than through the example's estimate.
- Recommended: show the +43 in the request's table as it is.

**M3. Step 13 of `implement-task` (`task-cycle/skill/SKILL.md:384-385`) says "*Questions*: only those the foundation step allows", but step 13 does not name `foundation_step.md`.** Slice 11.

- What is wrong: the paragraph at `:237-241` tells the orchestrator to read that file only when an agent returns `blocked` with a question, or at step 7. An orchestrator writing the request with no blocked return has the rule's name but not its conditions.
- Why it is Minor: in practice questions for the human come only from blocked returns, which do trigger the reading.
- Recommended: add "and at step 13" to the read triggers at `:239-241`.

**M4. `make-change`'s table of variants (`task-cycle/change/SKILL.md:19-26`) gives no case for a dispatch that names none of its rows.** Slices 7 and 11.

- What is wrong: two dispatches have no row — the agent of the plan's *Foundation entries* and a fresh agent of the return step. `implement-task:136-137` now tells the orchestrator to name their stage instead. But `make-change` still opens with "Your dispatch says which of these you make", which such an agent cannot satisfy.
- The base had the same gap without the table. Both slice reports name it.
- Recommended: in a later change, add a row or one sentence for "a stage your dispatch names that has no row: no file of this table".

**M5. Wording left by Slice 2** (commit `61cc5ab`):

- `AGENTS.md:10-12` leaves the short line "session works in. Use only these: a" in the paragraph's wrapping.
- In the generator's sentence (`agent-instructions/skill_entry_points.py:175-177`, and so in all 42 entry points), "not all of them at the start" has no plural noun before it ("read a file it names …").

Both are polish and change no meaning.

### Out of scope

**O1 (Important, outside the task). Product entry points still say "Read the files it references inside `.the-way`", with no word on when.** This is in `installation/install.py:136`, in `skill_wrapper`, and `installation/README.md:57` describes it.

- What a person running a cycle in a product meets: the orchestrator reaches `implement-task` through this entry point. It is told to read the files the skill references, which now include its seven files beside it, possibly all at the start. This is the same doubt the task's first question raised about the-way's own entry points.
- Why it matters: the measured cycle on `loop2`, which is meant to show this series' gain, runs in a product through this entry point.
- Why it is out of scope: acceptance criterion 1 allows no other Python change, and WAY-127 governs only the-way's own entry points.
- Recommended: a task of its own before the measured cycle on `loop2`, or a note in the request that the measurement is confounded until then.

**O2 (Minor, carried from Slice 10's proposal). The return `review-change` asks for lacks the one-line check result.** `implement-task:170-172` and WAY-148 expect a "one-line check result naming what failed or did not run". `review-change` (`task-cycle/review/SKILL.md`, section 4, last paragraph) returns only the first line, the counts and the path. This was there before the change, and Slice 10 reported it as a proposal with no edit.

## Declined to judge

- The content of `task-cycle/record_template.md`: the plan's Slice 11 *Goal* judges its place only.
- Whether each "remove" or "reword" proposal in slice reports 8–11 is right: they are proposals for the human in the request, with no edit made.

## Checks

| Check | Command or method | Result |
|---|---|---|
| Head | `git rev-parse HEAD` | `7369993…`, exit 0 |
| Clean tree | `git status --short` | empty |
| Entry points current | `python -B agent-instructions/skill_entry_points.py` | `entry points are current`, exit 0 |
| Instruction files | `python -B instruction-files/check_instructions.py .` | 0 errors, 1 warning (`AGENTS.md:21` `_zadania\`, older than this change), exit 0 |
| Foundation | `python -B elements/common/foundation_check.py` | `0 errors`, exit 0 |
| Focused tests | `python -B gate/run_tests.py task-cycle` | 41 tests OK, exit 0 |
| | `python -B gate/run_tests.py agent-instructions` | 18 tests OK, exit 0 |
| | `python -B gate/run_tests.py instruction-files` | 104 tests OK (5 skipped), exit 0 |
| | `python -B gate/run_tests.py gate` | 18 tests OK, exit 0 |
| Mutation of the changed test | In a detached scratch worktree of `7369993`, the base `skill_entry_points.py` restored, then `python -B -m unittest discover -s agent-instructions -p test_skill_entry_points.py`; the scratch worktree was removed afterwards | 3 failures, exit 1. The restored head passes. The assertion catches the sentence breaking. |
| Python scope | `git diff --stat cf11541..HEAD -- '*.py'` | 2 files, +5 −3, as acceptance criterion 1 allows |
| Whitespace | `git diff cf11541..HEAD --check` | nothing, exit 0 |
| Frontmatter | `git diff cf11541..HEAD -- task-cycle/*/SKILL.md \| grep '^[-+](name\|description):'` | nothing changed |
| Private links | `grep -rn -E "Storage\|The Brain\|_zadania\|Notes/" task-cycle/` | nothing, exit 1 |
| Sentence comparison | The plan's pipeline, run by me for each of the five directories: base `SKILL.md` against `cat task-cycle/<dir>/*.md`, with `comm -23` and `comm -13` | Every line it printed is accounted for as described under acceptance criterion 2 above |
| Pointer placement | Manual: each file beside a skill against the step that names it, and against who reads it at that step | All are named at their step or variant; exceptions M3 and M4 |
| Outside citations of renumbered sections | `git grep` for section and step numbers of `write-spec`, `review-change`, `plan-task` and `make-change` outside `.runs` | none; `installation/README.md:82` cites step 2 of `implement-task`, whose numbers 1–14 are kept |
| Base copy | `git show cf11541:<f> \| diff -q - .runs/the-way-base/<f>` for 5 files | same |

Not run:

- the whole `gate/run_tests.py`, which is the orchestrator's run (handoff);
- To do 6, since the request does not exist yet.

## Reaches beyond the dispatch

- **`installation/install.py:120-141` and `installation/README.md:57`.** Why: to see how a product's entry point tells a session to read a skill's files. Finding O1.
- **Environment fact `claude-skill-nested-references` (`foundations/environment_facts.md:186`), and WAY-258 and WAY-129 whole.** Why: to check how deep the new files' references go, and the form of their pointers.
- **The invariant `skill-entry-points` (`foundations/invariants.md:241-249`).** Why: to check that no invariant test changed. The invariant's test, `gate/test_skills_reach_the_way_sessions.py`, is unchanged.
- **"Reading the foundation" (`elements/common/way_of_working.md:58-83`).** Why: my own selection.
- **My selection was narrower than that procedure gives.** By *Scope*, the parts `task-cycle`, `instruction-files` and `agent-instructions` name 79 decisions. I read whole the ones the change writes or cites, or that the task names under *Decisions in play*: WAY-125, WAY-127, WAY-129, WAY-256, WAY-257 and WAY-258. I located others by searching for the phrases the change alters ("what it names", "reads the method", "files it references"). I did not read every decision of those parts whole. A conflict with an unread decision that uses none of those phrases is therefore unchecked.
- **The foundation-step report (`reports/foundation-report.md`).** Why: for C19 and its search under WAY-33.
- **`reports/gate-7369993.log`, its last lines.** Why: to see what the orchestrator had already run.

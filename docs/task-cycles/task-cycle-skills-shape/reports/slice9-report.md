# Slice 9 report — `plan-task` judged and rebuilt

- **Status:** `done with concerns` — the concerns are the doubt on `:116`/`:170` (*Choices and
  doubts*, point 3, with the "reword" proposals of (b)) and the choice of point 1; neither blocks
  the slice.
- **Commit:** `00d000eda3d629fffe43392f95b6dfb6c74b67a5` — "Rebuild plan-task by its judgment:
  too_large.md for the planner after an attempt or slice proved too large (WAY-256)", on
  `task/task-cycle-skills-shape`, on top of the slice's base `bf75d1c`. Not pushed.
- **Files changed** (`git diff --numstat cf11541 -- task-cycle/plan/`, the same from `bf75d1c`):
  - `task-cycle/plan/SKILL.md` +6 −15
  - `task-cycle/plan/too_large.md` +19 −0 (new)

Method: `make-change` from `.runs/the-way-base/task-cycle/change/SKILL.md`; judged with
`.runs/the-way-base/instruction-files/SKILL.md` in the mode judge, kind skill, with `judging.md`,
`kind_skill.md` and `tool_loading.md` of that copy, and the one-instruction exception of WAY-256
(as changed in `40f0fd3`) as the plan's *Common to the rebuild slices*, point 1, gives.

## Who reads the skill and in which variants

Only the planner reads `plan-task`; a slice's executor never reads it (it gets its section of the
plan in its handoff). Variants from the skill's text (`task-cycle/plan/SKILL.md:21-27`, `:47-49`,
`:186-196` at `cf11541`) and from `task-cycle/skill/SKILL.md` (step 8 `:221-237`; returns
`:246-255`; handoffs `:144-148`; statuses `:176`):

| Agent | Variant | Dispatched by | Recognises its variant |
|---|---|---|---|
| planner | a first plan from the frozen task | step 8 | yes — the dispatch gives the task and no spec, report or plan |
| planner | a plan after a reviewed spec (first, or after an earlier plan or a discarded attempt) | step 7 → step 8 ("any reviewed spec") | yes — the dispatch gives the reviewed spec |
| planner | after a one-author attempt proved too large | `:248-251` ("dispatch the planner at step 8 with … the report") | yes — the dispatch gives the attempt's report |
| planner | after a planned slice proved too large | `:253-255` ("have the planner split that slice") | yes — the dispatch gives the slice's report and the plan |
| planner | resumed with answers after `questions` | `:176-185` | not a reading variant: it resumes the variant it was in |

## (a) Judgment table

Lines are of `task-cycle/plan/SKILL.md` at `cf11541` (the slice's base `bf75d1c` holds the same
file). Ground: no session records were searched (plan, *Common*, point 2); each ground is the
decision or step of the cycle the fragment carries.

| # | Fragment | When an agent needs it / does it recognise that moment (WAY-257) | Verdict | Reason | Ground |
|---|---|---|---|---|---|
| 1 | `:1-4` frontmatter, the description | every use — the entry points `the-way-plan-task` are generated from it; in the cycle the handoff names the method / no moment to recognise | keep | the trigger and the source of the entry points; the plan keeps it unchanged | step: WAY-127 |
| 2 | `:6-13` "Writes the plan of one task's change…" — the picture of the whole | every use / no moment | keep | the picture of the whole stays in `SKILL.md` | WAY-256, WAY-136 |
| 3 | `:15-19` where the-way lies, `slice_size.py` there, skills by prefix | every use (step 4 runs the script) / no moment | keep | common | WAY-127 |
| 4 | `:21-27` the planner is a fresh agent; writes only the plan file; never code, test, entry or the human | every use / no moment | keep | picture of the whole and the planner's boundary; names the variants | WAY-136, WAY-148 |
| 5 | `:29-31` heading `## 1. Read`, the dispatch | every use / no moment — it is what tells the planner its variant | keep | common | WAY-148 |
| 6 | `:32-35` the frozen task whole and the spec where one was written; the spec binds where it settles more, the task where they differ | every use (the binding sentence only where a spec exists) / yes — the dispatch gives the spec | keep | the task's reading is common; the spec's clause is one instruction inside a common sentence, and moving it would split a sentence of the base | WAY-148; step 8 of the cycle; WAY-256 (exception) |
| 7 | `:36-40` what the dispatch names: sources, foundation, guideline files; guidelines missing; the styleguide's order-of-work example | every use (the styleguide sentence only for a product with a styleguide) / yes — the guideline file is in the dispatch | keep | common; the styleguide sentence is one instruction of one condition, kept by the exception | WAY-150, WAY-213; WAY-256 (exception) |
| 8 | `:41-44` reach beyond the dispatch, named in the report | every use, when something is missing / yes — the gap shows during the work | keep | common | WAY-150, WAY-213 |
| 9 | `:45-46` the code and tests the change touches, read to cut slices | every use / no moment | keep | common | WAY-136 |
| 10 | `:47-48` "After a one-author attempt proved too large, its report; the whole attempt … has been discarded." | only the planner after a one-author attempt proved too large / yes — the dispatch gives the attempt's report | move → `too_large.md` (`## Read`) | one variant's reading; it goes with row 22 behind one pointer that stands where it stood, so the planner reads it at the same step | WAY-136; `task-cycle/skill/SKILL.md:248-251` |
| 11 | `:48-49` "After a planned slice proved too large, its report and plan; the slices already made remain…" | only the planner after a slice proved too large / yes — the dispatch gives the slice's report | move → `too_large.md` (`## Read`) | as row 10, with row 23 | WAY-136; `task-cycle/skill/SKILL.md:253-255` |
| 12 | `:51-58` step 2, find an open design choice; return without a plan | every use / yes — the choice shows in reading the code | keep | common | WAY-135 |
| 13 | `:60-63` heading `## 3. Write the plan`, the form's lead-in | every use / no moment | keep | common; `slice_size.py:10` names this file as the form's place | WAY-136; `task-cycle/slice_size.py:10` |
| 14 | `:65-100` the fenced form of the plan | every use / no moment | keep, word for word | the slice's *Goal*; read by `slice_size.py` | `task-cycle/slice_size.py:10` |
| 15 | `:102-109` *Foundation entries* | every use (a planner splitting one slice keeps the table) / no moment | keep | common to every plan written | WAY-69, WAY-136 |
| 16 | `:110-115` a slice is narrow; its section is all its agent gets of the plan | every use / no moment | keep | common | WAY-148, WAY-136 |
| 17 | `:116-137` *Change* and *Read*; "*Read* is the whole reading of the slice's agent besides those files…"; its four kinds; paths | every use / no moment | keep (doubt 3; "reword" proposal (b) 1) | common; the sentence speaks of the material a handoff carries, and its list of four kinds names no method file | WAY-148, WAY-150, WAY-12, WAY-62, WAY-213 |
| 18 | `:138-143` *Model* | every use / no moment | keep | common | WAY-229 |
| 19 | `:144-148` *Risk* | every use / no moment | keep | common | WAY-48, WAY-13, WAY-136 |
| 20 | `:149-162` *Checks*, order, no code, *Coverage*, *Choices* | every use / no moment | keep | common | WAY-160, WAY-136 |
| 21 | `:164-172` step 4, the size script; "Since *Read* is the whole reading…" | every use / no moment | keep (doubt 3; "reword" proposal (b) 2) | common | WAY-136 |
| 22 | `:174-184` step 5, return | every use / no moment | keep | common | WAY-148 |
| 23 | `:186` heading `## Writing the plan again` | the planner of a re-planning variant / yes | move → `too_large.md` (`## Writing the plan again`) | goes with rows 25–26; the after-spec bullet leaves it (row 24) | — |
| 24 | `:188-190` "After a reviewed spec, only if the orchestrator selects planning again: write a new plan from the spec and task; nothing of an earlier plan binds. The same size judgment can instead send the settled change to one author without a plan." | only the planner after a reviewed spec / yes — the dispatch gives the spec | keep in `SKILL.md` (one-instruction exception), moved to step 1 where its pointer would stand (`SKILL.md:47-49` after) | one instruction (the second sentence instructs nothing); moved out, a pointer or a pointer's condition would replace it; a plan after a spec is a common variant, which would otherwise also read the two too-large variants | WAY-256 (exception); step 7 of the cycle |
| 25 | `:191-193` after a one-author attempt proved too large: attempt gone; divide from the task, any spec and its report | only that variant / yes — the dispatch gives the attempt's report | move → `too_large.md` | with row 10 the variant has two instructions against one pointer | WAY-136; `task-cycle/skill/SKILL.md:248-251` |
| 26 | `:194-196` after a slice proved too large: its code gone; split that slice, keep those made, run the script again | only that variant / yes — the dispatch gives the slice's report | move → `too_large.md` | several instructions of one variant | WAY-136; `task-cycle/skill/SKILL.md:253-255` |

Added by the rebuild (rewordings of *Common*, point 4 — a pointer and a file header, no rule):

- `SKILL.md:50-52`, step 1: "After a one-author attempt or a planned slice proved too large, read
  `too_large.md` and follow it: whose report you read, what of the attempt or of the plan stands,
  and how you write the plan again." — in place of the base `:47-49`; its condition names the
  moment as the planner meets it, the report in its dispatch.
- `too_large.md:1-4`, title and purpose ("# Planning after a change proved too large …"), in the
  form Slices 7 and 8 gave the files beside a skill.

Layout after the rebuild (one level deep; `too_large.md` points to no other file):

```
task-cycle/plan/
  SKILL.md      picture of the whole; 1. Read (common; the after-spec bullet, row 24; the pointer
                to too_large.md); 2. open design choice; 3. the form, unchanged, and its fields;
                4. size; 5. return
  too_large.md  Read (the attempt's or the slice's report); Writing the plan again (the two
                too-large variants)
```

**Form: a pointer at step 1, not a table of variants.** The first plan needs nothing beyond the
common text, the plan after a spec one instruction, and the two too-large variants one shared file:
two bullets carry that. A table of variants would add a row for the first plan with nothing in it
and, as Slice 7 measured, about 150 words to `SKILL.md`, more than the whole variant text it routes.
Way rejected: a table like `make-change`'s. Cost if wrong: one more pointer style among the five
skills; the change to a table is mechanical.

## (b) "Remove" and "reword" proposals (no edit)

No session records were searched (plan, *Common*, point 2); neither proposal rests on a mistake
seen, so by "When to add a rule" each is listed as **not recommended** unless the orchestrator
takes the handoff's concern (below) as its ground. Neither is a condition of "When to remove a
rule".

1. **Reword `:116-117`** (row 17), after: "*Read* is the whole reading of the slice's agent besides
   those files and its method, since its handoff carries what *Read* names — …". Reason: with
   WAY-125 as changed, the slice's agent reads `make-change` and the files its steps name at their
   step; the added words say that *Read* does not list them, so a planner does not put a method's
   files into *Read* and a handoff built from it does not tell the agent to read them at the start
   (WAY-125, *Verification*, violates). Ground: carried decision WAY-125.
2. **Reword `:170-171`** (row 21), after: "Since *Read* is the whole reading of the slice's agent
   besides its method, the size it reports is what that agent reads besides its section of the plan
   and its method." Reason and ground as in 1; `slice_size.py` counts no method.

## (c) Words read before and after

Commands (in the worktree, after the commit):

```
git show cf11541:task-cycle/plan/SKILL.md | wc -w                         -> 2178
wc -w task-cycle/plan/SKILL.md                                           -> 2089
cat task-cycle/plan/SKILL.md task-cycle/plan/too_large.md | wc -w        -> 2247
wc -w task-cycle/plan/*.md  -> 2089 SKILL.md, 158 too_large.md
```

| Agent | Variant | Reads | Before | After | Change |
|---|---|---|---|---|---|
| planner | a first plan | `SKILL.md` | 2178 | 2089 | −89 (−4%) |
| planner | after a reviewed spec | `SKILL.md` | 2178 | 2089 | −89 (−4%) |
| planner | after a one-author attempt proved too large | `SKILL.md`, `too_large.md` | 2178 | 2247 | +69 (+3%) |
| planner | after a planned slice proved too large | `SKILL.md`, `too_large.md` | 2178 | 2247 | +69 (+3%) |

The gain is small because almost the whole skill is common to every plan: step 3 alone, the form
and its fields, is most of it and every variant writes a plan. The two rare too-large variants pay
the pointer and the file header (about 70 words) so that the common ones shed about 120 words of
variant text.

## (d) Sentence comparison

Commands, outputs under `.runs/task-cycles/task-cycle-skills-shape/reports/`:

```
git show cf11541:task-cycle/plan/SKILL.md | tr -d '\r' | tr '\n' ' ' | tr -s ' ' | sed 's/\([.!?]\) /\1\n/g' | sort > slice9-before.txt   (exit 0)
cat task-cycle/plan/*.md | tr -d '\r' | tr '\n' ' ' | tr -s ' ' | sed 's/\([.!?]\) /\1\n/g' | sort > slice9-after.txt                     (exit 0)
comm -3 slice9-before.txt slice9-after.txt > slice9-comm.txt                                                                              (exit 0)
```

`slice9-comm.txt` holds 8 lines; each is accounted for:

| comm line | Side | Accounted for by |
|---|---|---|
| 1 `- After a one-author attempt or a planned slice proved too large, read \`too_large.md\` …` | after | the pointer (added, above) |
| 2 `- After a one-author attempt proved too large, its report; …` | before | row 10 (line 6 is its after side) |
| 3 `- After a one-author attempt proved too large: its whole attempt, … (WAY-136).` | before | row 25 (line 7 is its after side) |
| 4 `- After a reviewed spec, only if the orchestrator selects planning again: …` | after | row 24 — the same sentence, now the first of its bullet in step 1 (line 8 is its before side) |
| 5 `# Planning after a change proved too large What the planner reads, …` | after | title and purpose of `too_large.md` |
| 6 `## Read - After a one-author attempt proved too large, its report; …` | after | row 10 — the same sentence behind `too_large.md`'s heading `## Read` |
| 7 `## Writing the plan again - After a one-author attempt proved too large: …` | after | rows 23 and 25 — the same heading and sentence, now in `too_large.md` |
| 8 `## Writing the plan again - After a reviewed spec, …` | before | rows 23 and 24 — the heading left with rows 25–26; the sentence stands in step 1 (line 4) |

Every other sentence of the base stands word for word in `SKILL.md` or `too_large.md`.

## (e) Contradictions with `task-cycle/skill/SKILL.md`

None found, read against `:128-196`, `:198-255` and the hits of the search named under reaches.
Checked in particular: the planner's statuses `done`, `done with concerns`, `questions`, `returned`
(`:176`) match step 5; `plan.md` and `plan-size.md` in the record's directory (step 8) match
`:25` and step 4; "where it returns an open design choice instead, continue at step 6" matches
step 2; the planner reads the whole frozen task (`:144`) as step 1 says; the *Read* the planner
proposes and the orchestrator checks (`:146-148`, step 8) match `:116-137`; the too-large returns
(`:248-255`) match `too_large.md`. One observation, not a contradiction: step 8 dispatches the
planner with "the checks the move of the pin carried (step 2)", which `plan-task` step 1 does not
name; its first bullet, "what it names for you to read", covers it.

## Checks

| Check | Command | Exit | Result |
|---|---|---|---|
| sentence comparison | the three commands of (d) | 0, 0, 0 | 8 lines, each accounted for in (d) |
| file named at its step | `grep -n 'too_large.md' task-cycle/plan/SKILL.md` | 0 | `50:` step 1 |
| | `ls task-cycle/plan/` | 0 | `SKILL.md too_large.md` — the file `SKILL.md` names beside it |
| frontmatter and form unchanged | `git diff cf11541 -- task-cycle/plan/SKILL.md` | 0 | hunks `@@ -44,9 +44,12 @@` and `@@ -182,15 +185,3 @@` only; lines 1–4 and the fenced form (`:65-100`) untouched |
| entry points | `python -B agent-instructions/skill_entry_points.py` | 0 | `entry points are current` |
| no private links | `grep -rn -E "Storage\|The Brain\|_zadania\|Notes/" task-cycle/plan/` | 1 | prints nothing |
| focused gate | `python -B gate/run_tests.py task-cycle` | 0 | 41 tests OK; log `reports/slice9-gate-task-cycle.log` |
| whitespace | `git add -N task-cycle/plan/too_large.md && git diff --check` | 0 | prints nothing |
| check script of the method | `python -B .runs/the-way-base/instruction-files/check_instructions.py .` | 0 | 0 errors, 1 warning: `AGENTS.md:21` `_zadania\` does not exist — the root file's backlog link, outside this slice |

Not run: the full gate (the orchestrator's run, per the handoff). No test was written: the change
moves prose that instructs agents and writes no code (task, *Questions to settle* 3; `make-change`
section 2, "Test behaviour, not text").

## Own-work check (`make-change` section 3)

- **Requirement most likely not met:** acceptance criterion 2 — no rule disappears or changes
  meaning; each fragment stands in `SKILL.md` or in a file beside it that the step needing it
  names — with the risk that a moved fragment is read later than before.
- **Check:** the sentence comparison of (d); `grep -n 'too_large.md'`; and the pointer's place
  read against the base: it stands where the moved reading lines (`:47-49`) stood, so the
  too-large planner reads its report at step 1 as before, and the instructions of "Writing the plan
  again" arrive at step 1, earlier than any step that uses them.
- **Showed:** only the pointer, the file header and the headings' new neighbours differ; every
  moved sentence reappears whole; the after-spec sentence stays in `SKILL.md`.

## Reaches beyond the dispatch

- `grep -n "plan-task\|planner" task-cycle/skill/SKILL.md` — every place that dispatches the
  planner beyond the named ranges; hits at `:11`, `:67`, `:101` (lists and the one author's class)
  besides those inside `:128-255`. Nothing outside the named ranges dispatches it.
- `grep -rn "Writing the plan again\|plan/SKILL.md"` over the repository, `.runs/` aside, and over
  `foundations/*.md` — whether anything cites the moved section; hits: the entry points, the
  installer and its test, and `slice_size.py:10`, all by path only. Nothing cites the section.
- `task-cycle/change/SKILL.md:15-45`, `task-cycle/change/slice.md` (head), `task-cycle/spec/SKILL.md:14-50`
  and `slice8-report.md` — for the form Slices 7 and 8 gave a pointer and a file beside a skill.

## Choices and doubts

1. **The after-spec bullet (row 24) stays in `SKILL.md`, moved to step 1.** It is one instruction
   of one variant, so WAY-256's exception keeps it "where its pointer would stand"; the pointer of
   the variants stands at step 1. Way rejected: the whole section "Writing the plan again" moved
   into one file with one pointer — the four words "a reviewed spec, or" in the pointer's condition
   instead of the 45-word bullet, as Slice 8 moved one-instruction fragments with a step whose
   pointer stood anyway; it would have made the common after-spec planner read the two too-large
   variants (about 110 words) besides. Cost if wrong: one instruction the first-plan planner does
   not need stays in its text. A second way rejected: the bullet left in place under an end section
   `## Writing the plan again` of one bullet — the heading would then hide that the two too-large
   variants also write the plan again.
2. **One file for both too-large variants**, not one each: one pointer for the common planner
   instead of two; each rare variant reads the other's few lines. Name: `too_large.md`, after the
   moment it serves.
3. **Doubt on `:116` and `:170`** ("*Read* is the whole reading of the slice's agent"), as the
   handoff asked. The sentences are addressed to the planner, not to the slice's agent, which never
   reads `plan-task`; `:116` speaks of what the handoff carries and lists four kinds of material, of
   which none is a method, and the base already had the agent read its method beside *Read*. So I
   read them as not forbidding the slice's agent the files its method's steps name, and kept them
   word for word. The words that would rule the reading out ("besides … its method") are a change
   of text *Common*, point 6 does not allow here; they stand as proposals (b) 1–2 for the
   orchestrator to carry to the request or to settle.
4. **The pointer's wording** "what of the attempt or of the plan stands" covers "the slices already
   made remain" and "the whole attempt … has been discarded"; it adds no rule.

No adaptation of `make-change` section 4 was needed; no invariant test changed.

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


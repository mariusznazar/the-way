# Slice 8 report — `write-spec` judged and rebuilt

- **Status:** `done with concerns` — the concerns are the two doubts under *Choices and doubts*
  (points 1 and 2); neither blocks the slice.
- **Commit:** `bf75d1cc3f59ab3144dc362b4932f3658e71d7fe` — "Rebuild write-spec by its judgment:
  design.md for the designer, review.md for the reviewer (WAY-256)", on `task/task-cycle-skills-shape`,
  on top of the slice's base `9b776fe`. Not pushed.
- **Files changed** (`git diff --numstat cf11541 -- task-cycle/spec/`):
  - `task-cycle/spec/SKILL.md` +10 −73
  - `task-cycle/spec/design.md` +63 −0 (new)
  - `task-cycle/spec/review.md` +24 −0 (new)

Method: `make-change` from `.runs/the-way-base/task-cycle/change/SKILL.md`; judged with
`.runs/the-way-base/instruction-files/SKILL.md` in the mode judge, kind skill, with `judging.md`,
`kind_skill.md` and `tool_loading.md` of that copy, and the one-instruction exception of WAY-256 as
the plan's *Common to the rebuild slices*, point 1, gives.

## Who reads the skill and in which variants

From the skill's own text (`task-cycle/spec/SKILL.md:18-19` at `cf11541`: "The dispatch: whether you
write or review") and from `task-cycle/skill/SKILL.md` (steps 6–7, `:205-220`; handoffs `:144`,
`:178`, `:181`):

| Agent | Variant | Dispatched by | Recognises its variant |
|---|---|---|---|
| designer | a new spec | step 6 | yes — the dispatch says "write" |
| designer | after a discarded attempt | step 6 ("after a discarded attempt, that attempt's report") | yes — the dispatch carries the attempt's report |
| designer | resumed with answers, or revising after `FAIL` | step 6 (resume), step 7 ("the designer revises the spec once") | yes — the resume message or the findings |
| reviewer | the spec | step 7 | yes — the dispatch says "review" |
| reviewer | the revised spec | step 7 ("the reviewer reviews the revision once") | yes — the dispatch carries the earlier findings |

## (a) Judgment table

Lines are of `task-cycle/spec/SKILL.md` at `cf11541` (the slice's base `9b776fe` holds the same file).
Ground: no session records were searched (plan, *Common*, point 2); each ground is the decision or
step of the cycle the fragment carries.

| # | Fragment | When an agent needs it / does it recognise that moment (WAY-257) | Verdict | Reason | Ground |
|---|---|---|---|---|---|
| 1 | `:1-4` frontmatter, the description | every use — the entry points `the-way-write-spec` are generated from it; in the cycle the handoff names the method / no moment to recognise | keep | the trigger and the source of the entry points; the plan keeps it unchanged | step: WAY-127 |
| 2 | `:6-11` "Writes, or reviews, the spec…" — the picture of the whole | every use / no moment | keep | the picture of the whole stays in `SKILL.md` | WAY-256, WAY-135 |
| 3 | `:13-14` where the-way lies | every use (reaching the foundation; now also the files beside the skill) / no moment | keep | common | WAY-127 |
| 4 | `:18-19` the dispatch: write or review, the open choice, the spec path, the report path | every use / no moment — it is what tells the agent its variant | keep | common; the line every variant row below relies on | WAY-148 |
| 5 | `:20` the frozen task document whole | designer and reviewer alike (`task-cycle/skill/SKILL.md:144`) / no moment | keep | common to both agents | step 6–7 of the cycle; WAY-148 |
| 6 | `:21-23` what the dispatch names (WAY-150): passages, entries by identifier, guideline files whole | every use / no moment | keep | common | WAY-150, WAY-213 |
| 7 | `:24-25` after a discarded attempt, the report of the agent that met the choice | only the designer after a discarded attempt / yes — the dispatch carries that report | keep in place (one-instruction exception) | one instruction with its reason; a file beside the skill would replace it with one pointer and add a file; it is a reading of step 1, so moving it into `design.md` would also move it out of its step | WAY-256 (exception); WAY-135; step 6 of the cycle |
| 8 | `:26-27` the code the choice depends on — read to design, not to write | the designer surely; the reviewer possibly (to see where a builder would have to guess) / yes | keep | common as far as can be told; see doubt 2 | WAY-135 (step 6's "ways open") |
| 9 | `:29-33` reaching beyond the dispatch, named in the report | every use, when something is missing / yes — the gap shows during the work | keep | common | WAY-150, WAY-213, WAY-148 |
| 10 | `:35` heading `## 2. Settle the design` and `:37-38` restate the requirements, apart from the assumptions | only the designer / yes — the dispatch says "write" | move → `design.md` (`## Settle the design`) | guidance of one variant; several instructions | step 6 of the cycle |
| 11 | `:39-45` questions to the orchestrator in batches, status `questions`, never the human, never widen the task | only the designer / yes | move → `design.md` | as row 10 | WAY-148; step 6 of the cycle |
| 12 | `:46-47` weigh two or three ways, leave out unneeded features | only the designer / yes | move → `design.md` | as row 10 | WAY-135 |
| 13 | `:48-49` units behind interfaces | only the designer / yes | move → `design.md` | as row 10 | step 6 of the cycle |
| 14 | `:51-67` heading `## 3. Write the spec` and the form of `spec.md` | only the designer / yes | move → `design.md` (`## Write the spec`) | as row 10 | step 6 of the cycle ("It writes `spec.md`") |
| 15 | `:69-76` what each section of the spec holds | only the designer / yes | move → `design.md` | as row 10 | step 6–7 of the cycle (*Decisions* read by the planner and the author) |
| 16 | `:78-79` no code in the spec | only the designer / yes | move → `design.md` | as row 10 | WAY-135; step 6 ("before any plan or code") |
| 17 | `:81-86` the four checks before return | only the designer / yes | move → `design.md` | as row 10 | step 6 of the cycle |
| 18 | `:88-98` heading `## 4. Review a spec`, read as the builder, report only what would make the build go wrong (four kinds) | only the reviewer / yes — the dispatch says "review" | move → `review.md` (`## Review a spec`) | guidance of one variant; several instructions | step 7 of the cycle |
| 19 | `:100-103` skip wording and style; first line `PASS` or `FAIL`; the review of a revised spec | only the reviewer (the last sentence only the reviewer of a revision) / yes | move → `review.md` | moves with its step; the revision's sentence is part of the review step whose pointer stands anyway, so no pointer is added for it | step 7 of the cycle; `task-cycle/skill/SKILL.md:178` |
| 20 | `:105` heading `## 5. Return` | every use / no moment | keep, renumbered `## 4. Return` | the step numbers follow the new layout; no file names the old number (searched, see reaches) | — |
| 21 | `:107-110` the designer's report and status `done` | only the designer / yes | move → `design.md` (`## Return`) | several instructions of one variant | WAY-148; step 6 of the cycle |
| 22 | `:110-111` the reviewer's report and its first line | only the reviewer / yes | move → `review.md` (`## Return`) | one instruction, but `review.md` exists for row 18, so the move adds no pointer | WAY-148; step 7 of the cycle |
| 23 | `:111` "Each gives the orchestrator its paths, and nothing more (WAY-148)." | every use / no moment | keep, reworded without change of meaning: "The designer and the reviewer each give the orchestrator their paths, and nothing more (WAY-148)." | its antecedents (rows 21–22) moved out of the paragraph; the subject is spelled out | WAY-148 |
| 24 | `:111-112` the boundary is the reviewed spec: return before any plan, slice or code | every use / no moment | keep | common | WAY-135; step 6–7 of the cycle |

Added by the rebuild (rewordings of *Common*, point 4 — pointers and headings, no rule):

- `SKILL.md` `## 2. Design and write the spec`, `:37-39`: "As the designer, writing the spec or
  revising it, read `design.md` and follow it: how to settle the design and send your questions, the
  form of `spec.md`, the four checks before you return, and what your report holds."
- `SKILL.md` `## 3. Review a spec`, `:43-44`: "As the reviewer of a spec or of its revision, read
  `review.md` and follow it: what to report, what to skip, and the first line of your report."
- The title and one-line purpose of each file beside the skill: `design.md:1-4` ("# Designing a
  spec …") and `review.md:1-3` ("# Reviewing a spec …"), in the form Slice 7 gave `slice.md` and
  `fix.md`.

Layout after the rebuild (one level deep; neither file beside the skill points to another):

```
task-cycle/spec/
  SKILL.md    picture of the whole; 1. Read (common, row 7 kept); 2. pointer to design.md;
              3. pointer to review.md; 4. Return (common: paths only, the boundary)
  design.md   Settle the design; Write the spec (form, sections, no code, four checks); Return (designer)
  review.md   Review a spec (what to report, what to skip, PASS/FAIL, revised spec); Return (reviewer)
```

I put the pointers at the steps that need them rather than in a table of variants at step 1, as
Slice 7 did for `make-change`: here each variant is a whole step, so the step headings keep the
picture of the whole and the pointers cost two sentences instead of a table. Way rejected: a table of
variants at step 1 — consistent with `make-change`, but about 60 words more and it would empty
steps 2–3 out of `SKILL.md`. Cost if wrong: a reader comparing the five skills meets two pointer
styles; the change to a table is mechanical.

## (b) "Remove" and "reword" proposals

None. No fragment meets a condition of "When to remove a rule" (`judging.md`) on the grounds
available — no session records were searched — and the one rewording (row 23) changes no meaning.

## (c) Words read before and after

Commands (in the worktree, after the commit):

```
git show cf11541:task-cycle/spec/SKILL.md | wc -w                         -> 1066
cat task-cycle/spec/SKILL.md task-cycle/spec/design.md | wc -w           -> 993
cat task-cycle/spec/SKILL.md task-cycle/spec/review.md | wc -w           -> 662
wc -w task-cycle/spec/*.md  -> 527 design.md, 196 review.md, 466 SKILL.md
```

| Agent | Variant | Before | After | Change |
|---|---|---|---|---|
| designer | a new spec | 1066 | 993 | −73 (−7%) |
| designer | after a discarded attempt | 1066 | 993 | −73 (−7%) |
| designer | resumed, or revising after `FAIL` | 1066 | 993 | −73 (−7%) |
| reviewer | the spec | 1066 | 662 | −404 (−38%) |
| reviewer | the revised spec | 1066 | 662 | −404 (−38%) |

Each agent reads `SKILL.md` whole and the one file its step names (WAY-125 as changed in `40f0fd3`).
The designer gains little because nearly the whole skill is its own; the reviewer no longer carries
the design, the spec's form, the four checks and the designer's report.

## (d) Sentence comparison

Commands, outputs under `.runs/task-cycles/task-cycle-skills-shape/reports/`:

```
git show cf11541:task-cycle/spec/SKILL.md | tr -d '\r' | tr '\n' ' ' | tr -s ' ' | sed 's/\([.!?]\) /\1\n/g' | sort > slice8-before.txt   (exit 0)
cat task-cycle/spec/*.md | tr -d '\r' | tr '\n' ' ' | tr -s ' ' | sed 's/\([.!?]\) /\1\n/g' | sort > slice8-after.txt                     (exit 0)
comm -3 slice8-before.txt slice8-after.txt > slice8-comm.txt                                                                              (exit 0)
```

`slice8-comm.txt` holds 17 lines; each is accounted for:

| comm line | Side | Accounted for by |
|---|---|---|
| 1 `# Designing a spec What the designer …` | after | title and purpose of `design.md` (pointer file header) |
| 2 `# Reviewing a spec What the reviewer …` | after | title and purpose of `review.md` |
| 3 `## 5.` | before | row 20, the step renumbered (`## 4.` remains on both sides) |
| 4 `## Return The designer writes the spec …` | after | row 21 — the same sentence, preceded by the heading of `design.md`'s `## Return` |
| 5 `## Return The reviewer writes its report …` | after | row 22 — the same sentence, preceded by `review.md`'s `## Return` |
| 6 `## Review a spec As the reviewer, read the spec …` | after | row 18 — the same sentence; the heading lost its number `4.` in `review.md` |
| 7 `## Settle the design - Restate …` | after | row 10 — the same sentence; the heading lost its number `2.` in `design.md` |
| 8 `## Write the spec Write \`spec.md\` in this form …` | after | row 14 — the same sentence; the heading lost its number `3.` in `design.md` |
| 9 `Design and write the spec As the designer, … read \`design.md\` …` | after | the pointer of step 2 with its heading |
| 10 `Each gives the orchestrator its paths, …` | before | row 23, reworded |
| 11 `Return The designer and the reviewer each give …` | after | row 23, the rewording, behind the heading `## 4. Return` |
| 12 `Return The designer writes the spec …` | before | row 21 (its heading prefix `## 5.` split off; line 4 is its after side) |
| 13 `Review a spec As the reviewer of a spec … read \`review.md\` …` | after | the pointer of step 3 with its heading |
| 14 `Review a spec As the reviewer, read the spec …` | before | row 18 (line 6 is its after side) |
| 15 `Settle the design - Restate …` | before | row 10 (line 7 is its after side) |
| 16 `The reviewer writes its report …` | before | row 22 (line 5 is its after side) |
| 17 `Write the spec Write \`spec.md\` in this form …` | before | row 14 (line 8 is its after side) |

Every other sentence of the base stands word for word in `SKILL.md`, `design.md` or `review.md`.

## (e) Contradictions with `task-cycle/skill/SKILL.md`

None found, read against `:128-196` and `:198-220` and the hits of the search named under reaches.
Checked in particular: the designer's statuses `questions` / `done` and the reviewer's `PASS` /
`FAIL` (`:178`) match `design.md` and `review.md`; the boundary "before any plan or code" (step 6)
matches `SKILL.md`'s `## 4. Return`; the single revision and its single review (step 7) match the
reviewer's sentence on a revised spec. One observation, not a contradiction: `:134` "For a review, it
gives the range to review and the author's report" is worded for code reviews; the spec's reviewer
reads what its dispatch names (row 6), so a designer's report given to it is covered.

## Checks

| Check | Command | Exit | Result |
|---|---|---|---|
| sentence comparison | the three commands of (d) | 0, 0, 0 | 17 lines, each accounted for in (d) |
| files named at their step | `grep -n 'design.md' task-cycle/spec/SKILL.md` | 0 | `37:` step 2 |
| | `grep -n 'review.md' task-cycle/spec/SKILL.md` | 0 | `43:` step 3 |
| | `ls task-cycle/spec/` | 0 | `design.md review.md SKILL.md` — every file `SKILL.md` names beside it |
| frontmatter unchanged | `git diff cf11541 -- task-cycle/spec/SKILL.md` | 0 | first hunk `@@ -32,81 +32,18 @@`; lines 1–4 untouched |
| entry points | `python -B agent-instructions/skill_entry_points.py` | 0 | `entry points are current` |
| no private links | `grep -rn -E "Storage\|The Brain\|_zadania\|Notes/" task-cycle/spec/` | 1 | prints nothing |
| focused gate | `python -B gate/run_tests.py task-cycle` | 0 | 41 tests OK; log `reports/slice8-gate-task-cycle.log` |
| whitespace | `git diff --check` (new files added with `git add -N` first) | 0 | prints nothing |
| check script of the method | `python -B .runs/the-way-base/instruction-files/check_instructions.py .` | 0 | 0 errors, 1 warning: `AGENTS.md:21` `_zadania\` does not exist — the root file's backlog link, outside this slice |

Not run: the full gate (the orchestrator's run, per the handoff). No test was written: the change
moves prose that instructs agents and writes no code (task, *Questions to settle* 3; `make-change`
section 2, "Test behaviour, not text"); its behavioural test — an agent of each variant working
from the rebuilt skill — is not a check of this slice.

## Own-work check (`make-change` section 3)

- **Requirement most likely not met:** acceptance criterion 2 — no rule disappears or changes
  meaning; each fragment stands in `SKILL.md` or in a file beside it that the step needing it names.
- **Check:** the sentence comparison of (d), plus the two `grep -n` checks.
- **Showed:** only headings, the two file headers, the two pointers and the rewording of row 23 differ;
  every moved sentence reappears whole in `design.md` or `review.md`, and each file is named at the
  step of the agent that needs it.

## Reaches beyond the dispatch

- `grep -n "write-spec\|spec\.md\|designer" task-cycle/skill/SKILL.md` — to find every place that
  dispatches `write-spec` beyond the ranges named; hits at `:11`, `:67` (lists of methods) besides
  those inside `:128-220`. Nothing outside the named ranges dispatches it.
- `grep -rn "spec/SKILL.md\|write-spec.*\(step\|section\) [0-9]\|four checks"` over the repository
  (outside `.runs/`) — to see whether anything cites the skill's step numbers before renumbering
  `## 5. Return`. Hits: the entry points (by path only), `installation/install.py:38` and
  `installation/test_install.py:31` (by path only). Nothing cites a step number.
- `task-cycle/change/slice.md`, `fix.md` (heads) and the pointer lines of
  `task-cycle/change/SKILL.md` in the worktree — for the form Slice 7 gave a file beside a skill
  (title, purpose line, sections), so that `design.md` and `review.md` follow it.
- `git diff cf11541 -- instruction-files/kind_skill.md` — the exception's wording since Slice 1,
  which the handoff names.

## Choices and doubts

1. **The pointer of step 2 names "revising it".** The base text says nothing of the designer's
   revision after `FAIL` (step 7 of the cycle does); the pointer's condition names that moment so
   that a designer resumed with findings recognises it reads `design.md`. It adds no rule — the
   reviser follows the same steps as before — but it is a word the base did not have. Way
   rejected: "As the designer, read `design.md`" alone; cost if wrong: a reviser dispatched fresh
   might not take itself for "the designer". Recommended answer: keep it.
2. **Row 8 (the code the choice depends on) kept in step 1.** Its wording ("read to design, not to
   write") points at the designer, so `design.md` was a candidate; whether the reviewer uses it is
   not settled by the text, so by the handoff's note it stays in place. Cost of keeping: one
   instruction a reviewer may not need.
3. **Row 7 kept in place** by the one-instruction exception, although `design.md` exists and moving
   the sentence there would add no pointer. Kept because it is a reading of step 1 and WAY-256's
   exception keeps such a fragment "where its pointer would stand"; moving it would change when the
   designer reads the attempt's report (at step 2 instead of step 1). Cost: one instruction in the
   reviewer's text.
4. **Rows 19 and 22** — one-instruction sentences of a sub-variant (the reviewer of a revision; the
   reviewer's return) moved into `review.md` with their step: the exception bounds one instruction
   against the pointer that would replace it, and here the step's pointer stands anyway, so no
   pointer replaces them.

No adaptation of `make-change` section 4 was needed; no invariant test changed.

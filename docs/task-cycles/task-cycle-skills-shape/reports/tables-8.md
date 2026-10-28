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


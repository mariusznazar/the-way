FAIL e66e8e790b370f1f04baf8cc73a6f9913cef2fe2

# Review of the whole change — guidelines-skills-batch

Range: `05534d381b95a4e2692875263dd0d8875097b89d..e66e8e790b370f1f04baf8cc73a6f9913cef2fe2` (two commits,
21 files), one-author route, no plan, no slices, no spec. `git rev-parse HEAD` = the given head.

Counts: blocking 1 (Important), Minor within the task 8, out of scope 2.

## Findings

### Critical

none

### Important (blocking, within the task)

**I1. Testing skill: no step settles the exemplar of a level that has no recipe yet — this
coverage was there before the change and the change removed it** (items 10 and 15).

- Place: `product-guidelines/testing/SKILL.md:107-108`, `product-guidelines/testing/new_level.md:3-8`,
  `product-guidelines/testing/settle.md:16-17`, against
  `project-level/task/skill/guideline_findings.md:44-48` and `product-guidelines/reading.md:83-86`.
- What is wrong: at the base, step 3 of `testing/SKILL.md` read `new_level.md` "where the task's
  required outcome is itself the first test of a level" (any level), and `new_level.md` had step 4
  settle "the level, its recipe and that the task's first test of it becomes the exemplar". The
  change adds a condition to step 3 that item 10 did not ask for: `new_level.md` is now read only for
  "a level whose recipe already stands with an empty *Exemplar*". `new_level.md` itself now applies
  only to a recipe "already [standing] in `guidelines/testing.md`". For a level with no recipe,
  which is now an extension, nothing in the testing skill settles that the task's first test becomes
  the exemplar:
  - `settle.md:16-17` names only "each level with tests" (a new level has none) and "a new level of
    step 3 (`new_level.md`)", which step 3 no longer reads for this case;
  - `starting_set.md` and `audit.md` say nothing about designating an exemplar.
- Why it matters: the change's own new paragraph in `guideline_findings.md:44-48` requires exactly
  this designation in *To do* "through `maintain-testing-guidelines`" ("the extension of the testing
  guidelines with that level's recipe, and that this test becomes the level's exemplar"), and WAY-242
  approves a designation only in refinement. So the shared reading sends the task to the testing
  skill for something the testing skill no longer leads. In practice the agent leading the testing
  guidelines extends them with the level's recipe and never asks the human about the exemplar. The
  task goes to the cycle with the level's *Exemplar* left empty, against the `guideline_findings.md`
  paragraph. The words "which takes step 2 as well" in `recognize.md:24-25` and `new_level.md:7-8`
  still read as if the new-level case also applies, so the files contradict each other on this path.
- Evidence: `git show 05534d3:product-guidelines/testing/SKILL.md` lines 103-105 ("the first test
  of a level, read `new_level.md`") against head `SKILL.md:107-108`; a grep for `exemplar` across
  `product-guidelines/testing/*.md` (other than the template) finds no other place that settles it.
- Fix direction (not binding): let the new-level route, or the `settle.md` bullet, also cover a level
  that the same task's extension adds: step 2 and step 4 propose its recipe, and the task's first
  test of it becomes the exemplar. `new_level.md` still writes no recipe of its own.

### Minor (within the task)

**M1. `product-guidelines/coding/template.md:276` — the row for `### Recording a failure` keeps
"nothing else", and the sentence about what stays sits in the wrong column** (item 9, fifth
sub-item). The item asks that the row say it "zamiast „nothing else”" (instead of "nothing else").
The row now reads "nothing else; each rule that stays keeps the meaning of every word it takes from
this one, …" in the column *Goes with it*, while *Stays* still says "the rest". The meaning is
clear, but the column *Goes with it* now holds a statement about what stays, and the literal ask
(replace "nothing else") is not met. Better: *Goes with it* gives what really goes, and the rule
that kept rules keep the meaning of "failure" and "expected refusal" stands under *Stays*.

**M2. `foundations/decisions.md:9735-9736` (WAY-311, *Rationale*) — the weak point the human
accepted is changed** (row 3, question 3). The source's weak point is: "dwa zdania więcej w pliku
czytanym przy każdej ocenie, a odejście od kolejności zostaje bez zmiany" (two more sentences in a
file read at every judgement, and the departure from the order of sections stays). The entry
instead says "the table grows by a row for every part and every proposal, in a file read at every
judgement". That is a different cost, and it drops the cost the human knowingly accepted: the
order of sections is left unfixed. The decision template forbids naming a file or a count in the
author's prose (`elements/decisions/template.md:53-57`). That explains why the wording changed, but
not why the second half is gone. Proposed: "two more sentences in the skill's file on judging, read
at every judgement, and a departure from the order of the sections stays as it is." This is
non-binding prose, so it is Minor; it is still a source-fidelity departure.

**M3. `project-level/task/skill/guideline_findings.md:14` and `:58` — a bare `read_sources.md`**
(item 16). The remark behind the item was that an agent reads this file from step 5 of a guidelines
skill (`product-guidelines/coding/` or `testing/`). That agent sees "files beside this skill" there,
and a bare file name gives it no place: the file is `project-level/task/skill/read_sources.md`, and
no `read_sources.md` lies beside the guidelines skills. Write the full path, as the same file does
for `product-guidelines/...` paths, or "beside this file".

**M4. `product-guidelines/coding/SKILL.md:129-131` — the definition of "touches" is the author's,
not the source's** (item 6, row 5). "…only those the kind touches, which are those whose tool reads
the language of the kind's files". The task and row 5 give "dotyka" with no definition. The
definition fits the row's second clause, but it is a binding rule of the skill that WAY-216 does
not carry: its binding sentence says only "only those the kind touches". It also leaves the audit
of dependencies undecided, because that check reads manifests and lockfiles, not a language (the
author's open point 1). Either WAY-216 states the criterion in its binding sentence, accepted at
the merge, or the skill drops the clause and leaves "touches" to the agent's judgement, as WAY-216's
*Rationale* already admits ("whether a check reads a kind's language is the agent's judgement").

**M5. `foundations/decisions.md:7017` (WAY-240 *Scope*) — still only `product-guidelines`, though
the decision now `narrows WAY-95` and is restated in `elements/glossary/template.md:54-56`** (item 14,
row 1). An agent working on the glossary part selects decisions by *Scope* (WAY-21, "Reading the
foundation" step 2). It finds WAY-95 (Scope: glossary, …) but not WAY-240, which now governs which
glossary entries a test level takes. Adding `glossary` to the *Scope* closes this.

**M6. `instruction-files/judging.md:27-30` — the new paragraph cites no decision.** It carries
WAY-311, written in the same change. The neighbouring rules of the same list cite theirs (WAY-257 at
`:17`). Without the citation, a reader of the skill cannot find the rationale and the rejected ways
(the script that checks the shape of a judgement). Add "(WAY-311)".

**M7. `product-guidelines/styleguide/SKILL.md:38` against `:40-46` — the table row "Never writes … a
meaning the task did not settle (WAY-172)" stands above a paragraph whose second way has the cycle
"propose the decision on the branch"** (item 1). Read side by side, a reader may take the row to
forbid what the paragraph allows. The author noticed and left the row; one clause ("except as a
decision proposed at a blocked draft request") would remove the doubt.

**M8. `product-guidelines/coding/settle.md:27-29` — the second trial run "as `trial_run.md` gives"
also groups reports into causes of the audit's list** (`trial_run.md`, last bullet), after step 3
has already ordered that list (item 5; the author's open point 2). As written, the rerun's causes
either join the list after its order was made, or are silently dropped. The item asks only for the
split to rest on the chosen set. "run the trial again on the chosen one, for the split alone" would
keep the list as step 3 left it.

### Out of scope

**O1. `product-guidelines/coding/SKILL.md:46` and `product-guidelines/testing/SKILL.md:45` still say
"A meaning reaches the code only through the task document".** Item 1 changed only the styleguide
skill. The three sibling skills now say different things about the same WAY-172 route, and the coding
and testing ones omit the blocked-draft way, which their own templates give ("Writing the files",
`coding/template.md:316-317`). This goes beyond the task (item 1 names the styleguide skill alone).
Suggested as a backlog item.

**O2. `product-guidelines/testing/SKILL.md:98` and `:117-118` still point indirectly ("`starting_set.md`
sends you to `research.md`", "`settle.md` sends you to `new_tools.md`").** Item 3 names only the
styleguide and coding skills. The same principle (`instruction-files/SKILL.md`, "points directly and
one level deep") applies. This goes beyond the task.

## Item and settlement check

| Item | Met | Note |
|---|---|---|
| 1 | yes | M7 |
| 2 | yes | |
| 3 | yes | styleguide steps 2 and 4, coding steps 2 and 4; conditions match `starting_rules.md:9-10`, `settle.md:37-38`, `starting_set.md:10-11`; O2 |
| 4 | yes | `coding/settle.md:21-23`, `task_document.md:36` |
| 5 | yes | M8 |
| 6 | yes | M4 |
| 7 | yes | six headings in `recognize.md:30-32` match `coding/template.md:184-215`; `SKILL.md:100-102` |
| 8 | yes | `settle.md:42-44`, `hand_back.md:9-10` (vacuous at the first guidelines, as the task asks) |
| 9 | yes, with M1 | (a) `:200`; (b) `:213-215` agrees with way 1 `:246-248`; (c) `:254-258`; (d) `:274` agrees with WAY-276; (e) M1 |
| 10 | text yes, with I1 | the condition added to `SKILL.md` step 3 drops the coverage of a recipe-less level |
| 11 | yes | |
| 12 | yes | moved to `testing/SKILL.md:65-68` |
| 13 | yes | `recognize.md:21-25` |
| 14 | yes | WAY-240, `settle.md`, `template.md`, glossary template; M5 |
| 15 | yes, with I1 | `reading.md:83-86`, `guideline_findings.md:44-48` |
| 16 | yes | M3 |
| 17 | yes | `audit_end.md:52-58` |
| 18 | yes | `audit_end.md:66-70`, both `hand_back.md`, WAY-282 |
| 19 | yes | `audit_end.md:58-62`, both `hand_back.md`; traced the four orders of the two skills, none is left without a hand-back |
| 20 | yes | M6 |

| Row | Entry | Met | Note |
|---|---|---|---|
| 1 | WAY-240 edited, `narrows WAY-95` | yes | area stated in binding sentences (WAY-25); *Rejected* = question 1's not-chosen ways; M5 |
| 2 | WAY-310 new | yes | *Rejected* = question 2's three ways (row 2's one is among them); weak point as given |
| 3 | WAY-311 new | yes, with M2 | verdicts "keep, move, remove or reword" match `judging.md:16` |
| 4 | WAY-282 edited | yes | rejected way and price as row 4 gives |
| 5 | WAY-216 edited, `narrows WAY-202` | yes | rejected ways as row 5 gives; weak points in *Rationale* are the author's (allowed prose); M4 |

## Declined to judge

- Return step (the handoff excludes it): not reviewed.
- The author's decision not to edit WAY-95 itself: WAY-25 puts the record in the prevailing decision,
  so not a finding.
- Whether rows 2 and 3 should have edited WAY-171 / WAY-257 in place rather than adding WAY-310 /
  WAY-311: the questions are new and the rows chose "decision"; outside what I can fault.

## Checks run

- `git rev-parse HEAD` → `e66e8e790b370f1f04baf8cc73a6f9913cef2fe2` (matches).
- `git diff 05534d3..e66e8e7`, `git log --stat 05534d3..e66e8e7`: read whole.
- `python -B elements/common/foundation_check.py` → "0 errors", exit 0.
- `python -B -m unittest installation.test_coding_guidelines_installation installation.test_testing_guidelines_installation`
  → 4 tests OK, exit 0. These tests install the two changed skills, and the author did not run them.
  `git status --short` afterwards was empty, so the reviewed worktree is unchanged.
- Manual: `git show 05534d3:product-guidelines/testing/SKILL.md` and grep for `exemplar` / `new level`
  across `product-guidelines/testing/*.md` (I1); grep of `research.md|new_tools.md|staged_cleaning.md|trial_run.md`
  across the three skills (item 3); grep of `read_sources` across the repository (M3); grep of
  `WAY-310|WAY-311|judging.md` (M6).
- Not run: the full gate (the cycle's own run).

## Reaches beyond what I selected

Selection: part map entries `product-guidelines`, `instruction-files`, `project-level`, `glossary`,
`decisions`. I read whole the decisions the change writes (WAY-216, WAY-240, WAY-282, WAY-310,
WAY-311) and, as their links and the task's *Decisions in play* need, WAY-95, WAY-25, WAY-257,
WAY-272. Of the remaining decisions in play I used the task's quotations. I did not read whole every
one of the 87 decisions whose *Scope* names `product-guidelines`, so the foundation selection is
narrower than "Reading the foundation" asks. The repository has no `guidelines/`.

- `elements/common/way_of_working.md` "Reading the foundation", to select.
- `elements/decisions/template.md:50-74, 218-226`, for what *Rationale* and *Rejected* may hold
  (M2, row checks).
- WAY-21, for M5.
- `project-level/task/skill/read_sources.md` whole (item 16, M3).
- `product-guidelines/coding/trial_run.md`, `starting_set.md`, `settle.md`, `task_document.md`,
  `recognize.md`, `SKILL.md`; `product-guidelines/testing/starting_set.md`, `recognize.md`,
  `settle.md`, `new_level.md`; `product-guidelines/styleguide/starting_rules.md`, `settle.md:30-42`;
  `product-guidelines/reading.md:60-95`; `coding/template.md:170-318`, to judge the items in place.
- `installation/test_*_guidelines_installation.py`, found by searching for tests that touch the
  changed skills.

## Searches not found or unclear

- The author's open point 3 (who starts the return of a stopped audit after the work is separated):
  `hand_back.md` "return here" with `refine-task` leading the conversation is enough; no source names a
  trigger. Not a finding.
- The author's open point 4 ("in its own text" for the meaning a kept rule takes): it follows from way
  3 of the departures; the task does not say where the meaning stands. Only the column issue (M1)
  is a finding.
- The author's open point 5: a proposal row in `judging.md` has no verdict among the four, and neither
  question 3 nor WAY-311 gives one. Left unclear; the source settles nothing more.
- The author's open point 6 (the reads of the other skill's step 1 stay): it agrees with item 17. Not
  a finding.
- Item 8 at "the first guidelines": `guidelines/coding.md` does not exist then, so the clause is
  vacuous. The task asks for it; it does no harm.
- `check_instructions.py` does not read `product-guidelines/**` (the author's point 8); the skill
  texts were checked by reading only.

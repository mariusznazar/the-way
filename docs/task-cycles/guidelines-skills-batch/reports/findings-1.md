# Findings to fix — review of the whole change (reviewer's words, cut from review-whole.md)

Reviewed head: e66e8e790b370f1f04baf8cc73a6f9913cef2fe2

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

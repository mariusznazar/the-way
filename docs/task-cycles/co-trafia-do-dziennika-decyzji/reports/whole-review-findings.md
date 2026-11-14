# Findings of the review of the whole change that the fix takes

Cut word for word from `reports/whole-review-report.md` (the review's first line is `PASS 39d702a61fce67962c5788dbac8636dc5c6e67ae`). Every finding here is Minor and within the task's scope; none blocks. The reviewer's ids are kept.

### M1. The foundation check reads every non-Markdown file of the base through one git process each, for a result that the base side never changes

- Place: `elements/common/foundation_check.py:759-763` (`list_invariants`: `git ls-tree -r` of the base, then `at_commit` per file).
- Slice: 4 (`12286a5`).
- What: when at least one invariant reading `test` has a reworded sentence, the script starts one `git show` for every non-Markdown file the base holds, only to learn which files cited the invariant at the base. I traced the cases: a file that cites at the base and is unchanged also cites now, and a file that changed or was deleted is in `changed` and so excludes the listing in either set; the set of citing files at the base changes no result. The slice 4 executor says the same (no test fails on its removal). The executor of slice 4 also says the cost is only on a candidate; that is right, but a candidate is the ordinary case of the change this entry exists for.
- Why it matters: measured here, 62 non-Markdown files cost 5.2 s with `subprocess.run(["git","show",...])` (about 0.08 s each) and the whole run of the script rose from 1.3 s to 6.0 s when I reworded `fingerprint-definition`. A product with a thousand non-Markdown files would pay about 80 s, five thousand about 400 s, on every run of its gate while such a rewording stands. The spec (D1) names `git grep` for this reading.
- Evidence: `python -B elements/common/foundation_check.py` in a detached worktree of the head, 1.3 s clean and 6.0 s with the sentence of `fingerprint-definition` reworded (listed line printed, exit 0).
- To settle: drop the base-side set (the test `test_citing_file_deleted_is_a_change_and_not_listed` keeps its value through `changed`), or read the base with one `git grep` call.

### M2. The docstring of the script calls the report of an uncited invariant "the last report named below"

- Place: `elements/common/foundation_check.py:11`.
- Slice: 3 and 4 (`ea2d186`, `12286a5`) added two reports after it, in the same docstring.
- What: "The switch `--skip-test-citations` skips the last report named below, the invariant that reads `test` and has no citing line." The report of decisions that nothing holds and the listing of a reworded invariant now stand after it (lines 78-93). A reader who takes "last" literally takes the switch to skip the listing too; WAY-321, which the change does not alter, says the switch skips that one report only.
- Why it matters: a name that stopped being true (WAY-362); the code skips only the one report (checked: `check_held` and `list_invariants` run before and apart from `if not skip_test_citations`, and `test_skip_switch_skips_nothing_of_the_decisions_nothing_holds` protects it).
- To settle: replace "the last report named below" with "the report named at line 66" or with the words of the report.

### M3. The decision skill points "the switch of step 3" and means step 4.3 of the shared way of working

- Place: `elements/decisions/skill/SKILL.md:41`.
- Slice: 6 (`64cd4ad`).
- What: the added bullet says the run "right after the entry is written ... and the switch of step 3 does not skip that report". Step 3 of this skill is "Draft", which names no switch; the switch is passed in step 4.3 of `elements/common/way_of_working.md` (also WAY-321).
- Why it matters: a reader of the skill looks for the switch in the wrong step.
- To settle: write "the switch of the run in step 4 of `way_of_working.md`" or name `--skip-test-citations`.

### M4. The task template does not give the values of the column *Goes to* that spec D5 lists

- Place: `project-level/task/template.md:203-210`; also `elements/common/skill/task_variant.md:26-28`.
- Slice: 7 (`f20a62c`).
- What: D5 gives the cell values (`sentence of <PREFIX-NN>`, `skill or instruction file: <name or path>`, `guidelines: <discipline>`, `data or code: <place>`, and `decision`, `invariant`, `glossary term`, `environment fact` as before). The template lists the places in words and says "each named as those questions name it"; the questions name places, not a form of cell. Only `product-guidelines/template.md:114` writes `guidelines: <discipline>`. The executor chose this to avoid copying the questions (its report says so).
- Why it matters: two writers of a table write the cell two ways; the foundation step must read the cell as a place. No script reads it, so nothing breaks today. The task's own text (*To do* 2) is met.
- To settle: write the four value forms once in the paragraph of "Settlements to record" (they are values, not the questions).

### M5. Row 1's threshold sentence stands in the template and in no entry of the log

- Place: `foundations/decisions.md:390` (WAY-11) against `elements/decisions/template.md:148-149`.
- Slice: none (foundation entries step, `d629ed8`).
- What: row 1 of *Settlements to record* is accepted as a decision (change of WAY-11) and reads "wpisem zostaje tylko to, co przeszło wszystkie, i tylko tam, gdzie ktoś, kto decyzji nie zna, zrobiłby inaczej, a test, który go zatrzyma, nie powie mu dlaczego". WAY-11 binds "only where it passes all of them" and does not carry the second half. The agent of the foundation entries says so in its report (choice 1). The template carries the sentence (as *To do* 1 asks), so no agent works wrongly, but the log's entry is narrower than the row the human accepted, and the sentence has no one-line reason beside it in the template.
- Why it matters: the row's meaning is to be written whole (WAY-134); a reader of the log does not find the threshold.
- To settle: add the threshold to a binding sentence of WAY-11 (the entry is held by its pair, so the check passes) or record by a decision of the human that the template alone carries it.

### M6. The lower part of the request description is not extended for a guidelines rule the cycle found

- Place: `task-cycle/skill/request_template.md:291-297` (kind 6, done) and `:449-452` (*Foundation entries*, not done).
- Slice: 9 (`39d702a`).
- What: D7 says a rule the cycle found itself is named in kind 6 and in *Foundation entries* of the lower part. Slice 9 extended kind 6 and, in the lower part, only the invariant listing and the tests with `decision:`; the plan's Goal for slice 9 also named only kind 6.
- Why it matters: the lower part is the full list of what the human is shown; a rule found by the cycle is absent from it. Small, since kind 6 reaches the human.
- To settle: one clause in the lower part, or a note that the lower part lists entries and a rule with *Decision* `none` is no entry.

### M7. Kind 7 says "without the switch" where the switch it means is not named

- Place: `task-cycle/skill/request_template.md:436-441`.
- Slice: 9. The executor raised it as a concern (report, "Concern and question").
- What: the spec's word "switch" is `--skip-test-citations`. The template names none.
- To settle: write "without `--skip-test-citations`".

### M8. The step for a row that goes outside the log says nothing of how it is written there

- Place: `task-cycle/skill/foundation_step.md:7-13` and `task-cycle/skill/return_step.md:14-18`.
- Slice: 7 and 6.
- What: the foundation step still says "Each is written by following the pinned `SKILL.md` of its element", and lists the five elements; a row that goes to a skill, to guidelines or to the product's data has no `SKILL.md`. `decide_entry.md:5-9` says what to do for a rule that the questions send elsewhere (written in the same change, a guidelines rule as the guidelines template gives it), but a writer of the foundation step does not read that file for such a row. `return_step.md` says "go to the place the questions ... give it", without the sentence that no entry is written there (*To do* 3: "nie powstaje wpis"). Nothing is wrong in either sentence; the rule is implicit.
- Why it matters: a row going to a skill or to code reaches the writer with no named way to write it.
- To settle: one sentence in `foundation_step.md` ("a row whose column names no element is written in its place by the rule of that place, in the same change as the code") and "no entry is written" in `return_step.md`.

### M9. WAY-134 and WAY-115 now say different things about the column; WAY-134's *Rejected* cites a rule of WAY-19 that this change rewrote

- Place: `foundations/decisions.md:2836` (WAY-115, "its kind"), `:3611` onward (WAY-134, "in place of its kind"), `:3710` (WAY-134 *Rejected*: "a new rule beside an existing one is a new question (WAY-19)").
- Slice: none (foundation entries step).
- What: WAY-115 binds the table to show "its kind"; WAY-134, which derives from WAY-115, replaces the kind by the place in task mode, with no relation recording the precedence between the two. The spec judged WAY-115 to need no change. Separately, WAY-19 no longer says "a new rule next to an existing decision is a new question" (it now says a part that cannot change apart from an entry is its sentence), and WAY-134's *Rejected* still quotes the old rule as its argument against folding the rule into WAY-29. The argument still holds (WAY-29's question is independent), but its parenthetical reads the old WAY-19.
- Why it matters: a reader compares two entries that disagree on one word; WAY-25 asks for a recorded precedence where two applicable decisions collide.
- To settle: add "narrows" or reword "its kind" in WAY-115 to "its kind or its place"; reword the clause of WAY-134's *Rejected*.

### M10. WAY-17 still reads as a closed chain

- Place: `foundations/decisions.md:578` (WAY-17, unchanged; its *Verification* reads `none`, so the script lists it).
- Slice: none.
- What: "Every link of the chain fact → decision → invariant → test is written ..., and none is optional ... a check names its invariant". A test that holds a decision's sentence by `decision:` names the decision, with no invariant between. The spec says to leave WAY-17 alone unless the foundation step found the chain stated as closed; it is stated so.
- Why it matters: small; the entries WAY-12, WAY-22 and the template state the new path.
- To settle: one clause in WAY-17 (this makes it a changed decision; it then needs a pair of examples or the same would stop the gate, as spec D2 warns).

### M11. The docstring of `README.md`/script and the decision log carry lines over the width

- Place: `foundations/decisions.md:5221` (WAY-167 rationale, broken line), `foundations/decisions.md:3711ff` (WAY-134, short and long lines mixed), `task-cycle/skill/foundation_step.md:9` and `:19`, `task-cycle/skill/request_template.md:437` and `:450`, `product-guidelines/template.md:12` (the word "and" alone on a line), `product-guidelines/template.md:353`.
- Slice: foundation entries step, 7, 8, 9.
- What: reflow left lines of 100-170 characters and one orphan word. Cosmetic, no sentence read wrongly.
- To settle: reflow.

### M14. `decide_entry.md` words "where the first yes is not the log" although question 4 ends in no place

- Place: `elements/decisions/skill/decide_entry.md:5-9`.
- Slice: 6.
- What: "Where the first 'yes' is not the log, no entry is written, and the rule goes to the place that answer names". Question 4 ("only the lack of a feature") names no place; it is not written. Question 5 is a "yes" that is the log. The sentence after it covers 5 and the template covers 4, so no agent works wrongly.
- To settle: "or, where it is question 4, is not written".

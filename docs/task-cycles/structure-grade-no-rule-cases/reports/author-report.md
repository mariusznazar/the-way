# Author report — structure-grade-no-rule-cases

**Status:** done

## Commits

- `5554f5d` — Grade a structure finding as Minor in every product without a size rule

Branch `task/structure-grade-no-rule-cases`, on the base `1be9057`. One commit, made by path (`git add` of the two files).

## What changed

What the task's *To do* items 1–4 asked for, in two files.

1. `task-cycle/review/SKILL.md`, section 3, the sentence starting "A finding about the structure of code that lies below the threshold of the rule of size" (now lines 126–131). Its clause for a product without a rule of size now reads "whatever the reason: for example, the product departed from the rule by a decision, it has no coding guidelines at all, or its guidelines were written before the rule existed." The three cases are examples of every such product, not a closed list. Stat of this file in the commit: 4 lines added, 3 removed.
2. `foundations/decisions.md`, entry WAY-363 (heading at line 12131), edited in place (WAY-07):
   - binding sentence: the same "whatever the reason ... for example" wording, with the third case (guidelines written before the rule) added; the sentence about the reviewer's scope now starts a new sentence;
   - *Verification*, complies bullet: "or a product that departed from the rule of size by a decision, or whose guidelines were written before the rule and hold none of it, grades the finding Minor";
   - *Rationale*: the last sentence ("The reviewer still judges the scope of each finding ...") rewrapped from a 163-character line to the entry's width (task *To do* 4). The text is unchanged.
   - *Rejected* and *Scope* are unchanged; they already speak of "a product with no rule of size" in general terms.
   - Also re-wrapped the binding paragraph and the complies bullet, which had to change.

Stat of `foundations/decisions.md` in the commit: 12 lines added, 10 removed (16 added and 13 removed across both files).

## Not changed, and why

- `task-cycle/review/whole_change.md`, last bullet of "The structure of the code the change leaves": already reads "Where that heading holds `none —`, or the product's guidelines hold no such rule, there is no such test ... a finding of structure is Minor (WAY-363)". The third case (guidelines predating the rule) falls under "the product's guidelines hold no such rule", so the three cases already get the same grade. Acceptance criterion checked by reading; no edit.
- `task-cycle/plan/SKILL.md` (about line 182), `task-cycle/change/SKILL.md` (about line 56): general wording ("Where the product's guidelines hold no rule of size"), unchanged.
- `product-guidelines/coding/settle.md` (line 89–90) and `product-guidelines/coding/template.md` (line 78): both say a reviewer's structure finding "is then always Minor" for a product that departs from the rule by a decision with its reason. That is the decision case, which stays correct; neither says the other two cases are graded differently. Not changed.
- WAY-360 "Rejected" sentence about "the same chance in the grade": not touched, per the boundary.

## Checks

| Check | Command | Exit |
|---|---|---|
| Foundation check | `python -B elements/common/foundation_check.py` | 0 (prints "0 errors") |
| Tests of the changed review skill's directory | `python -B gate/run_tests.py task-cycle` | 0 (394 tests, OK) |
| Tests of the decisions directory | `python -B gate/run_tests.py foundations` | 1 — "no test found in foundations" (the directory has no tests; not a failure of the change) |

Not run: the whole gate (the orchestrator runs it). No test was written or changed: the change is prose and the task calls for no invariant test. No mutation check applies to prose; the own-work check below stands in for it.

## Own-work check (section 3)

- Requirement the change most likely does not meet: the three cases must get the same grade, in the review skill, in the binding sentence and in the whole-change last bullet, with the Verification and Rationale no longer pointing to the narrower two-case scope.
- Check: grep for "rule of size", "no coding guidelines", "departed from the rule" across the foundation and the task-cycle elements (done in the WAY-33 search below), then reading each hit.
- Result: the review skill sentence and the binding sentence now both name all three cases as examples; the whole-change bullet already covers the third case through "the product's guidelines hold no such rule". The grep found no other statement of the two-case scope. Weakest point: the whole-change bullet does not name the pre-rule case in words, so a reader who reads "hold no such rule" narrowly (only `none —`) could still miss it; I judged the wording general enough and did not edit it, since the task's *To do* did not list that file.

## Foundation search (WAY-33)

Ran after the wording was settled. Searched the whole repository, excluding `.runs/`, for "WAY-363", "WAY-360", "rule of size", "no coding guidelines", "departed from the rule", and "structure". Hits read in context:

- `foundations/decisions.md`: WAY-360, WAY-361, WAY-362, WAY-364, WAY-365, WAY-328 mention the rule of size or the structure of code. None states the two-case scope, and none conflicts with the three-case wording. WAY-365 has its own rule "Where the product's guidelines hold no rule of size ... nothing of this applies", which is consistent. WAY-364's Relations/Verification are unaffected.
- `task-cycle/review/whole_change.md`, `task-cycle/plan/SKILL.md`, `task-cycle/change/SKILL.md`, `task-cycle/change_file_sizes.py`: consistent, see above.
- `product-guidelines/coding/settle.md`, `template.md`, `hand_back.md`, `recognize.md`, `trial_run.md`, `task_document.md`: consistent with the change (they describe the decision case or the general rule).

Nothing needed a change beyond the two files. No question for the human.

## Reaches beyond the dispatch

- `elements/decisions/skill/SKILL.md`, `read.md`, `decide_entry.md` and `elements/decisions/template.md` read whole for the edit in place; `elements/decisions/examples.md` read (one line, WAY-03); `elements/common/rules.md` read whole (no rule violated: English, no version, no `TODO`, identifiers unchanged). `elements/common/way_of_working.md` read only its "Reading the foundation" section (lines 58–101); its other sections not read.
- `foundations/decisions.md`: WAY-07 and WAY-33 read whole; WAY-161 read in its first 60 lines only (of a longer entry); WAY-328 read in its first 30 lines (its Rationale and Rejected not read); WAY-360, WAY-361, WAY-362, WAY-364 read whole; WAY-363 read whole.
- `product-guidelines/coding/settle.md` and `template.md`: read only the lines named by the handoff plus the grep hits.
- `elements/decisions/skill/projected.md`: not read (projected mode not used).
- The decision log's full *Scope* search for `task-cycle` and `product-guidelines` (way_of_working step 2) was not run as a whole; the topical search above replaced it. Those decisions are the ones the topical search found.

## Unread material

- `elements/decisions/skill/projected.md` — not needed (projected mode unused).
- `elements/common/way_of_working.md` — sections other than "Reading the foundation" (lines 1–57 and 102–161), not read.
- `foundations/decisions.md`: WAY-161 beyond line 4753; WAY-328 beyond its first paragraph; the full task-cycle-scope decision list (not all decisions read — only the topical ones).
- `product-guidelines/coding/settle.md` and `template.md`: read only the lines named.

## Searches not found or unclear

- `gate/run_tests.py foundations` reports "no test found in foundations" (exit 1). The foundations directory has no tests; the handoff asked for the tests of the directories changed, and I took this as no test to run. The orchestrator should judge whether that is the intended reading.
- Nothing else looked for was unclear.

## Choices

- Wording of the examples: "for example, ... or ... " inside the binding sentence, so that the three cases read as examples of "every such finding", as the task asked. Way rejected: naming the pre-rule case only in *Verification* or *Rationale*, which would leave the binding sentence narrow (the defect the task reports). Cost if wrong: a reader may read the examples as a closed list; low, since the binding sentence says "every such finding".
- Did not edit `whole_change.md`: the cost of leaving it is a reader who reads "hold no such rule" narrowly; the cost of editing it is touching a file outside the task's *To do*. I judged the first smaller and recorded it above.

## Adaptations of section 4 and changed invariant tests

None.

## Problems observed

None beyond the note on `gate/run_tests.py foundations` above.

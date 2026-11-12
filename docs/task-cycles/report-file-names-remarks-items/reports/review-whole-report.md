PASS 172bc71c41b81cca6b6f31261550e64f121b4570

# Review of the whole change: report-file-names-remarks-items

Range `55afa8e57aa1b83c77108576a36642722e0dda15`..`172bc71c41b81cca6b6f31261550e64f121b4570` (`git rev-parse HEAD` matches), commits `0f34dc1` and `172bc71`, one author, no plan, no spec, no slice reviews. Diff computed with `git diff 55afa8e..HEAD`.

Counts: blocking 0, Minor 5 (all within the task), out of scope 0.

## Task items and settlements

- Item 1 (the naming rule): met. The sentence at `task-cycle/skill/SKILL.md:144-149` follows the WAY-148 handoff sentence and matches the task's wording word for word (compared against the quoted block in *To do* item 1, character by character).
- Item 2 (thematic break): met. `split_items` (`task-cycle/remarks_check.py:164-169`) treats a line matching `RULE` (`---`, `***`, `___`, spaced forms) as a part, like a sub-heading. Docstring now reads "a sub-heading and a thematic break are no items" (line 29, word for word).
- Item 3 (bold label only at the start of a paragraph): met. `opens_paragraph` (`remarks_check.py:189`) and the condition at `:245`. The cases the task lists (start of file, after a blank line, heading, rule, a line that itself starts with bold, a line with a list marker) are all covered. The docstring (lines 19-21) carries "at the start of a paragraph, of a list item, or after a line opening with another bold label" word for word. One case beyond the task's list: the line right after a closing code fence opens a section (`:195-197`, commit `172bc71`). I judge it consistent with the task: it keeps the earlier behaviour for a case the task does not mention, and it follows from "start of a paragraph". Not a finding.
- Item 4 (report without the section gives no item, exit 0): met in behaviour (unchanged) and recorded in WAY-294 (see below).
- Item 5 (four cases): all four exist in `task-cycle/test_remarks_check.py`: `test_a_thematic_break_in_a_section_is_no_item` (heading-form section, five spellings, with and without text after), `test_a_bold_label_on_a_second_line_of_a_paragraph_opens_no_section`, `test_two_bold_labels_on_consecutive_lines_are_both_read`, `test_a_report_without_the_section_gives_no_item_and_exit_zero` (asserts exit 0, empty stderr, empty listing, the `checked:` line). An extra test covers the code-fence case.
- Questions 1 and 2: answers carried out as the task gives them (exception in WAY-294, not in WAY-344; the naming rule built from the stage or role).
- Out of scope respected: the diff touches no reading of `cycle.md` (`remark_blocks`, `opens_block` untouched) and no other file reading; the order of the sections in reports is untouched.
- Settlements to record row 1: WAY-294 states "a report without the section gives no item and does not end the script with an error, which narrows WAY-344 for the reports this script reads" in its binding sentences (`foundations/decisions.md:9504-9506`), `Relations: derives from WAY-260 · narrows WAY-344` (`:9510`), Verification example `report-planner.md` became `planner-report.md` (`:9518`), complies and violates clauses for the case added, Rationale and Rejected extended. Checked against `elements/decisions/template.md`: three binding sentences (limit is 1-3), present tense, no forbidden normative words, `narrows` with the area stated in the binding sentence (WAY-25), *Rejected* holds both ways of the task's *Not chosen* with their reasons and no counts, the entry is edited in place with no history of the change (WAY-07). `python -B elements/common/foundation_check.py foundations`: exit 0, "0 errors".
- WAY-344's duty for the reworked reading: the change reworks the reading of reports; the only field the script reads from a report is the section, and the no-section case is the exception the task settles; no other file or part of the script was reworked. The duty is met by the exception and its test (item 5, case 4). `cycle.md` reading unchanged.

## Verification by differential run

I ran the old script (`55afa8e`) and the new `section_items` over 416 report `.md` files found under the `.runs/task-cycles` and `.runs/worktrees` folders of the author's checkout (script in the scratchpad, `python -B -I`). Three files differ, all as intended:
- `unread-material/.../author_report.md`: the old script listed a lone `---` as an item; the new one does not.
- `unread-material/.../review_whole_report.md`: a mention of the label in the middle of a sentence's continuation line was an item; no longer.
- `retain-failed-checks/.../reconciliation-report.md`: a label on the continuation line of a list item under another heading opened a section and listed four unrelated sentences; no longer.
No file lost a real item.

## Findings

### Minor (all within the task)

1. `task-cycle/remarks_check.py:26-27`: the docstring still says "a section inside fenced code, and a report with no section are not read". A report with no section is read and gives no item, as the same change now states in WAY-294. A reader of the script's description gets the older reading. The author flagged this line and left it. Fix: "... a section inside fenced code, and a report with no section give no item".
2. `foundations/decisions.md:9539-9541` (WAY-294 *Rationale*): "the cycle's reports also hold the orchestrator's own files, which never have one". The task's *Context* says only that the files without a section are "in most cases" the orchestrator's (and once a stage report), so "never" is stronger than the source (WAY-263 spirit: restating more broadly). The next sentence of the same Rationale speaks of "a task document" (`:9543-9545`), which is how the decision was placed rather than why it holds (template: Rationale tells no process of reaching the decision). Fix: drop "which never have one" (or say "which need not have one") and cut the sentence about the task document.
3. `task-cycle/test_remarks_check.py` (tests of `opens_paragraph`): two of its conditions are not protected by any test. In a scratch copy, removing the `RULE.fullmatch(before)` clause and, separately, the `HEADING.fullmatch(before)` clause left `python -B -m unittest task-cycle.test_remarks_check` at exit 0. The task asks for four cases and they exist; a label right after a heading and right after a rule are listed in *To do* item 3 as cases that must open a section, so a regression there would pass silently. Fix: one test with `# T\n**Searches not found or unclear:** x\n` and one with `---\n**Searches ...` / `text\n\n---\n**Searches ...`.
4. `task-cycle/test_remarks_check.py:478,487`: the fixture file is still called `report-planner.md`, the name the same change removes from the WAY-294 example and which the new skill rule forbids for subagent reports. It is only a fixture and works; renaming to `planner-report.md` would keep the test and the decision in step. The author flagged this.
5. `task-cycle/skill/SKILL.md:149`: the new sentence was inserted in the middle of the handoff paragraph, and the line it leaves, "text. The handoff gives the user's delegation, the worktree, the method of the stage by the path of its `SKILL.md` in the pinned the-way, the stage and its boundary, the paths", is now about 170 characters, against the 100-character wrap of the neighbouring lines. Polish only.

### Blocking

none.

### Out of scope

none.

## Declined to judge

- Whether the Claude Code refusal covers exactly the four words (the task's *Context* records the test of 2026-11-12 on 11 names): I took it as the task's source and did not repeat the experiment.
- The task's own text, its settlements and the cycle's choices (frozen): not judged, only compared with the change.

## Checks run

- `git rev-parse HEAD` -> `172bc71c41b81cca6b6f31261550e64f121b4570`, exit 0.
- `python -B gate/run_tests.py task-cycle`: exit 0, 291 tests OK (run in the worktree).
- `python -B -m unittest task-cycle.test_remarks_check`: exit 0, 58 tests OK.
- `python -B elements/common/foundation_check.py foundations`: exit 0, "0 errors".
- Differential run, old versus new `section_items`, over 416 reports (above): 3 differences, all intended.
- Mutation run in a scratch copy under the scratchpad (`...\scratchpad\mut2`), two mutants of `opens_paragraph`: both survive (Minor finding 3).
- Not run: the full gate (the cycle's own run), `python -B -m unittest elements.common.test_foundation_check` (author's run accepted for the foundation check, and `foundation_check.py` re-run above).
- Changed invariant tests: none.

## Reaches beyond the handoff

- `foundations/part_map.md` (the `task-cycle` entry, lines 93-101): to judge the part and trust boundary (`cycle_stages.py`, untouched).
- `foundations/invariants.md`: headings screened (`grep`); read the sections of `script-language`, `tracked-file-private-paths`, `skill-entry-points` titles only; the change adds no import, no private path and no skill description change, and the task-cycle gate tests (which include the entry-points checks) pass.
- `task-cycle/skill/SKILL.md:205-222` and `:488-512`: to verify the claim of WAY-294's Rationale that a stage report lacking the section returns to its agent, and that the skill's description of the script does not contradict the exception (it says "judges no content", nothing about missing sections).
- `elements/common/rules.md` read whole (89 lines), `foundations/glossary.md` read whole (179 lines; no entry of the change's words), `elements/decisions/template.md` read whole.
- The `retain-failed-checks` and `unread-material` worktrees' reports, to examine the three differences.

## Unread material

- Decisions of my selection: the log holds 302 decisions. Read whole: 5 (WAY-30, WAY-260, WAY-294, WAY-295, WAY-344). Read in part: 2 (WAY-148 and WAY-328, each to the middle of *Rejected*; their binding sentences, Scope, Relations, Verification and Rationale read). By title only: I did not run through all 302 titles; I screened them by a keyword search of titles (`report|script|section|remark|exception|name|read|heading|cycle record`) and looked at the 55 titles it returned; the rest I did not see. Of those titles, these bear on the change's topic and stayed unopened: WAY-38 (language of the scripts), WAY-296 (form of the process remarks; the change does not touch the reading of `cycle.md`), WAY-326 (the **Unread material** section), WAY-308 and WAY-309 (cited as precedent by the author; WAY-308's relation line seen only in `grep`), WAY-157 (named in the task's *Context*, not located in the log by title, probably withdrawn), WAY-125 (methods of the task cycle).
- `foundations/invariants.md` (356 lines): read by headings only (the 38 headings), plus the grep lines; not whole. `foundations/part_map.md`: the `task-cycle` entry only. These are the invariants of the touched part by the author's list; none concerns remarks checking.
- Guidelines: none selected (WAY-328: the-way holds its own code and tests to no product guidelines, and `product-guidelines/reading.md` was not needed).
- `task-cycle/skill/SKILL.md` read in the passages named above, not whole.

## Searches not found or unclear

- The task's *Context* cites a decision WAY-157 about the way of waiting for an agent; I did not find it among the 55 titles screened (probably withdrawn); not pursued, it does not bear on the change.
- Whether the line after a closing code fence should open a section was not named by the task; I judged it consistent (above), but the task is silent, so the question stays open for the human only if they want that case excluded.
- Line numbers in the task's *Context* (`remarks_check.py:149`, `:186`, `:205`, `:1-48`) are from `55afa8e` and do not match the head; used by name.

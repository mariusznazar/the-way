PASS 8dae4be92c7869e708ff66025b58b4b235878e4d

# Review of the decisions the whole-change review left unread

Range `55afa8e..8dae4be` (`git rev-parse HEAD` = 8dae4be92c78...). Files: `foundations/decisions.md`
(WAY-294), `task-cycle/remarks_check.py`, `task-cycle/test_remarks_check.py`, `task-cycle/skill/SKILL.md`.
Task read whole. Result: 0 blocking, 2 Minor, 0 out of scope.

## Decisions read

- WAY-38 (`foundations/decisions.md:1026`), whole. The diff adds no import and no subprocess call; the code
  added is `re`-based string handling in an existing standard-library-only script. No contradiction.
- WAY-125 (`:3151`), whole. The change to `task-cycle/skill/SKILL.md` adds a rule on file names only. It does
  not tell any agent to read a method or a file at the start, and it leaves intact the sentence of the same
  paragraph that reads a named file only when its step comes. No contradiction.
- WAY-294 (`:9495`), whole, the changed decision. Its *Verification* says that a report with no section
  lists nothing and that the script exits 0 when no other report lists an item; the code and the new test
  `test_a_report_without_the_section_gives_no_item_and_exit_zero` do that. The *Violates* clause (exit 2 at
  a report with no section) matches no path in the code: no new `sys.exit(2)`. The added *Rationale* sentence
  that a stage report lacking the section is returned to its agent matches `task-cycle/skill/SKILL.md:213-216`.
  The *Rejected* additions give the two alternatives of the task's question 1. The *Relations* line
  "narrows WAY-344" matches the content. The example name is now `planner-report.md`, and the test of the
  command uses the same name. No contradiction.
- WAY-296 (`:9589`), whole. The change does not touch the form of the remarks or the reading of the remarks
  block (`RemarkBlockTest` untouched). No contradiction.
- WAY-308 (`:10023`) and WAY-309 (`:10089`), whole. The added lines of the range hold no absolute path and no
  `[[...]]` link (grep of the added lines of the diff, no hit); the new test and decision text use relative
  file names only. No contradiction.
- WAY-326 (`:10787`), whole. The script reads only **Searches not found or unclear** and never **Unread
  material**; the change keeps that separation. The new reading of a label after a line opening with another
  bold label is the form the decision's two sections produce (`**Unread material:** ...` then
  `**Searches ...:**`), and the test `test_two_bold_labels_on_consecutive_lines_are_both_read` covers it. The
  returning of a report without **Unread material** is untouched. No contradiction.
- WAY-344 (`:11316`), whole, read because WAY-294 now narrows it (not on the handoff list). The change
  reworks the reading of the report sections, so the decision would require exit 2 for a missing section and
  a test for it; WAY-294 now records the exception, which is the escape the task chose (question 1) and which
  the decision's own *Verification* wording would otherwise count as a breach. The rule's remaining demand,
  a test that gives a report without the field, is met by the new command test (it asserts exit 0 and no item,
  the behaviour WAY-294 now states). The exception is stated in the decision that carries the script, as WAY-30
  needs. No contradiction.
- WAY-157: there is no `### WAY-157` heading. The decision exists only as a row of the table of withdrawn
  decisions (`foundations/decisions.md:11426`): "withdrawn: how the orchestrator waits for an agent is a step of
  the task-cycle skill and binds no other work". The new file-name rule of `task-cycle/skill/SKILL.md:144-149`
  is the same kind of thing (a workaround of one orchestrator step, with its reason in the sentence, no
  decision) and the change adds no decision or environment fact for it. No contradiction.

## Findings

### Minor 1 — `task-cycle/skill/SKILL.md:149`, a reflowed line left far longer than its neighbours

The edit moved text into a 172-character line (`... and the report path. The agent reads that ...`), where the
file wraps at about 100. Effect: none on behaviour, but the next edit of that paragraph produces a noisy diff.
Evidence: `awk '{print length}'` on lines 144-152 gives 98, 99, 82, 92, 97, 99, 94, 172, 99. I found no
line-length check in `gate`, `agent-instructions` or `task-cycle` scripts (grep), so nothing fails. Within the task.

### Minor 2 — `task-cycle/remarks_check.py:190-200` (`opens_paragraph`) and `:246`, a label on the line right after a list item is not read

A report written as

    **Unread material:**
    - a
    **Searches not found or unclear:**
    - x

yields no items (run: `section_items(...)` returns `[]`; before the change it returned `['x']`). The label
line follows a list item with no blank line, so it counts as a lazy continuation of the item, which is how
Markdown reads it, and the task's data names this case as the one remaining false report it chooses not to
read ("jako dalszy ciąg punktu listy", 1 of 19 labels). The cost lies in the other direction from the task's
estimate: a report that really means the label as a section and writes it in this form now has its items
silently unread, where before the script listed them. WAY-294's purpose is that no item is passed over
unseen. The task fixes the rule, so this is not a defect of the change, only a tradeoff worth the
orchestrator's attention; it is stated nowhere in the script's description (`remarks_check.py:19-20`).
Within the task; Minor.

## Declined to judge

- Whether the Claude Code write-block on file names (the reason of the rule in `SKILL.md`) still holds: it was
  tested by the task's author on a named version; I did not repeat it.
- The reader-of-plan-state and other decisions not on the handoff list, beyond WAY-344.

## Checks

- `git rev-parse HEAD` -> 8dae4be92c7869e708ff66025b58b4b235878e4d (matches the head given).
- `python -B gate/run_tests.py task-cycle` -> exit 0 (292 tests OK).
- Scratch run of `remarks_check.section_items` on three inputs (label right after a list item, an indented
  label after an item, a label after a blank line) -> `[]`, `[]`, `['x']`.
- Grep of the added lines of the diff for `[[` and drive-letter paths -> no hit.
- Grep of `task-cycle`, `foundations`, `agent-instructions`, `elements` for `report-<name>.md` names -> only
  the counter-example in `SKILL.md:147` and `task-cycle/test_image_files_check.py:80` (a test fixture name
  `report-png.md`, not in the range and not a subagent write).

## Reaches beyond the dispatch

- WAY-344, read whole: WAY-294 now narrows it and the handoff list did not name it.
- Lines 11405-11430 of `foundations/decisions.md` (table of withdrawn decisions), to find WAY-157.

## Unread material

none of the handoff's decisions stayed unread: WAY-38, WAY-125, WAY-294, WAY-296, WAY-308, WAY-309, WAY-326
read whole; WAY-157 has no entry beyond its row in the withdrawn table, read in full. I did not read the
whole-change review report or the other files of `reports/` (not asked).

## Searches not found or unclear

- A `### WAY-157` heading in `foundations/decisions.md`: not found; the decision appears only as a withdrawn-table
  row (`:11426`) and in the task's *Context*. The handoff says to report this.
- A check in `gate` for the line length of skill files: not found, so Minor 1 is only polish.

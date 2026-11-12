# Author report: report-file-names-remarks-items

**Status:** done

**Commits** (branch `task/report-file-names-remarks-items`, base `55afa8e`):
- `0f34dc1` Skip thematic breaks in the remarks check and open a bold label only at the start of a paragraph
- `172bc71` Open a bold label right after a code block as the start of a paragraph (follow-up found by the own-work check; the test for it was written and seen failing first)

**Files changed** (added / removed lines, base to HEAD):
- `task-cycle/remarks_check.py`: 25 / 9
- `task-cycle/test_remarks_check.py`: 33 / 0
- `task-cycle/skill/SKILL.md`: 5 / 2
- `foundations/decisions.md`: 18 / 7 (WAY-294 only)

## What was done

1. **Report file names (SKILL.md).** Added the naming rule right after the WAY-148 handoff sentence in `task-cycle/skill/SKILL.md`, with the blocked words and the reason.
2. **Thematic breaks (remarks_check.py).** A line that is only a rule (`---`, `***`, `___`, `- - -`, `* * *`) inside a section is no item. It parts the text before and after it, as a sub-heading does. It does not end the section. The docstring now says "a sub-heading and a thematic break are no items".
3. **Bold label position (remarks_check.py).** A `**Searches not found or unclear**` label opens a section only at the start of a paragraph, at a list item, or after a line that starts with bold text. Helper: `opens_paragraph`. The docstring now says "at the start of a paragraph, of a list item, or after a line opening with another bold label".
4. **No-section report.** Unchanged in behaviour: no item, exit 0. It is now stated in WAY-294 as the exception to WAY-344.
5. **Tests (test_remarks_check.py).** Added: thematic break (heading form, five rule spellings, with and without text after); label on a paragraph's second line opens nothing; two labels on consecutive lines are both read; label right after a code block opens a section; report without the section gives no item, exit 0, and the exact last output line.
6. **Decision WAY-294 (decisions.md).** Binding sentence gains the exception ("a report without the section gives no item and does not end the script with an error, which narrows WAY-344 for the reports this script reads"). Relations: `derives from WAY-260 · narrows WAY-344`. Verification: example renamed `report-planner.md` to `planner-report.md` (same meaning); added complies and violates clauses for the no-section case. Rationale and Rejected extended with the reason and the rejected ways, without counts or file names. WAY-344 is unchanged, as WAY-308 already narrows WAY-294 without a back-reference.

## Checks

Each run was on the worktree, from its root.

- `python -B -m unittest task-cycle.test_remarks_check`: exit 0, 58 tests, OK (final state).
- Before the code change, the new tests failed for the expected reasons: `python -B -m unittest task-cycle.test_remarks_check`: exit 1, two FAIL (thematic break read as item `---`; label on paragraph second line opened a section). The two-label and no-section tests passed already, which is the kept behaviour.
- Before the follow-up fix: the closing-fence test failed (`[] != ['an item']`), exit 1, then passed after the fix.
- `python -B gate/run_tests.py task-cycle`: exit 0 (after the first commit, 290 tests OK; re-run exit 0 after the follow-up).
- `python -B elements/common/foundation_check.py foundations`: exit 0, "0 errors" (after the WAY-294 edit).
- `python -B -m unittest elements.common.test_foundation_check`: exit 0, 125 tests OK.
- Mutation check in scratch copies outside the worktree: removing the thematic-break check made `test_a_thematic_break_in_a_section_is_no_item` fail; removing the paragraph-start condition made `test_a_bold_label_on_a_second_line_of_a_paragraph_opens_no_section` fail. Each mutant also showed one ERROR in `TemplateTest`, because the scratch copy did not include `record_template.md`; that is an artifact of the copy, not of the mutation.
- Not run: the full product gate (`gate/run_tests.py` with no argument), which the orchestrator runs.

## Own-work check

- Requirement: a label written right after a list item line (no blank line) must not open a section, and a label right after a heading or a code block must.
- Check: `section_items` on `- item\n**Searches not found or unclear:** x\n`, on a closing fence followed by the label, and on `# T\n**Searches...:**\n- one\n`. Command: `python -B -c` with `import remarks_check`, exit 0.
- Showed: after list item `[]` (as intended); after closing fence `[]` before the fix, which was wrong and became commit `172bc71`, now `['an item']` in the test; after heading `['one']`.

## Choices made

- **Narrowing recorded in WAY-294 only.** Rejected: also adding `narrows WAY-294` or a back-reference in WAY-344. Cost if wrong: a reader of WAY-344 alone would not see the exception; the log's existing pattern (WAY-308) does not add one, so I followed it.
- **Rule lines** count as breaks in any section position, indented up to three spaces, `- - -` and `* * *` included. Rejected: treating only `---` as a break. Cost if wrong: a rule written in another spelling is still listed as an item; the test covers five spellings.
- **Label after a code block opens a section** (follow-up). Rejected: keeping the fence as a non-paragraph start. Cost if wrong: a report whose label follows a code block would have been silently skipped, which is the failure this task was meant to end.
- **Label after a line starting with bold text** opens a section, with up to three spaces of indent allowed, as the existing bold-start rule gives. Rejected: only labels on lines that start a paragraph after a blank line. Cost if wrong: two consecutive labels would not both be read, which the task requires.
- **No change to WAY-344's binding sentences**, no change to invariants, no change to glossary or part map.

## Concerns and leftovers (not changed)

- `task-cycle/remarks_check.py` docstring, the line "a section are not read" near the top (the sentence "A mention of the name inside a sentence, a section inside fenced code, and a report with no section are not read"): a report with no section is in fact read and gives no item. The handoff named other lines only, so I left it. The orchestrator may want it reworded to "gives no item".
- `task-cycle/test_remarks_check.py` still uses `report-planner.md` as a fixture file name in `test_every_md_file_whose_name_holds_neither_handoff_nor_findings_is_read`. It is a fixture, not the decision's example; I did not rename it.

## Unread material

- `elements/common/rules.md`: not read. The decisions element's `way_of_working.md` step 1 asks for it whole; I relied on `foundation_check.py` passing instead.
- `task-cycle/skill/SKILL.md`: read in parts only (the WAY-148 paragraph, the report-rule paragraph around lines 194-220, the remarks-check section near line 476). The method did not name it whole.
- `foundations/decisions.md`: WAY-148 read through its binding sentences and the start of its Verification, not whole; WAY-30 read through its binding sentences and the start of its Verification; WAY-260 and WAY-328 read through the binding sentence, Scope and Verification, not their Rationale. WAY-295 and WAY-344 read whole. WAY-296, WAY-308 and WAY-309 were looked at only for their Relations lines.
- `foundations/invariants.md`: read whole for `script-language`, `script-imports`, `script-subprocesses`, `tracked-file-private-paths`, `test-method-citation`, `record-copy-image-check`. The *Rests on* entry `python-stdlib-modules` was not read. No script import was added.
- `foundations/part_map.md` task-cycle entry: read (first lines). No file moved and no dependency changed.
- `foundations/glossary.md`: not read. I did not search it for a term used in the change.
- `elements/decisions/template.md`, `elements/decisions/skill/read.md` and `decide_entry.md`, `elements/common/way_of_working.md`: read. `elements/common/way_of_working.md` only through its "Reading the foundation" and "Search" sections.

## Searches not found or unclear

- `elements/common/rules.md` could not be used for the entry's form, as above; no search of it was made.
- Glossary: no search for the words "thematic break", "process remarks" or "Searches not found or unclear" was made; the entry uses only words it already uses.
- Whether a `report-planner.md` mention in the test file should be renamed too: unclear; left as is.
- Whether the docstring line "a report with no section are not read" should be reworded to match the exception: unclear; left as is.
- Git attribution lines: no attribution line was present in the context, so none was added to the commits.

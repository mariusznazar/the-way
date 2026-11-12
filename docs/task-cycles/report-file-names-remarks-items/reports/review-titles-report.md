PASS 8dae4be92c7869e708ff66025b58b4b235878e4d

# Review of the decision titles the whole-change review screened by keyword

Range `55afa8e..8dae4be`; `git rev-parse HEAD` = 8dae4be92c7869e708ff66025b58b4b235878e4d. Files of the
range: `foundations/decisions.md` (WAY-294), `task-cycle/remarks_check.py`, `task-cycle/test_remarks_check.py`,
`task-cycle/skill/SKILL.md`. Task read whole earlier. Result: 0 blocking, 0 Minor, 0 out of scope.

## Titles read

`grep -n "^### WAY-" foundations/decisions.md` -> 302 headings (the count matches the whole-change report's 302).
All 302 titles read, one by one, from the printed list.

## Decisions opened whole (beyond the 7 of the earlier report and WAY-344/148/260/295/328/30)

- WAY-05 (`foundations/decisions.md:124`) — how a decision entry is written. Bears on the wording of the added
  sentences of WAY-294. The added binding sentence is in the present tense and checkable; the added *Rationale*
  names no file, script or count and does not tell how the decision was reached; the file names in *Verification*
  are in a field, not in the prose. No contradiction.
- WAY-07 (`:163`) — an entry is edited in place and holds only its current wording. WAY-294 is rewritten in
  place; no second entry, no version. No contradiction.
- WAY-18 (`:518`) — a link between entries is written at one end only. "narrows WAY-344" stands only in WAY-294;
  WAY-344 is left unchanged. No contradiction.
- WAY-22 (`:591`) and WAY-36 (`:977`) — decision or invariant, decision or plan. The exception is a rule that
  binds after the merge, so it belongs in the log; the file-name rule is a step of the orchestrator in the skill,
  with its reason in the sentence, as the task's *Context* says. No contradiction.
- WAY-25 (`:645`) — what settles a collision. WAY-294 now names WAY-344 in *Relations* as `narrows` and its
  binding sentence states the area ("for the reports this script reads"), as the rule needs; WAY-344 does not
  narrow WAY-294 back. Whether the request quotes the human's passages that give the outcome is the request's
  business, not in this range. No contradiction.
- WAY-32 (`:862`) — closed list of relation types. `narrows` is used for a decision deliberately gone against in
  a narrower area, which is what WAY-294 does. No contradiction.
- WAY-71 (`:1684`) and WAY-72 (`:1737`) — fields of an entry, language. All fields of WAY-294 stay filled
  (*Relations*: "derives from WAY-260 · narrows WAY-344"); the text is English. No contradiction.
- WAY-130 (`:3374`) — when a rule enters an instruction file. The file-name rule of `SKILL.md` carries a step of
  the activity the skill leads, and the task names the mistake and its records (7 of 58 cycles). No contradiction.
- WAY-256 (`:7886`) — where a fragment of a skill stands. The rule is one instruction in the step every cycle
  reaches (writing the handoff), so it stays in `SKILL.md`. No contradiction.
- WAY-263 (`:8160`) — a restatement of a changed entry that broadens it or drops a qualification is Important.
  Compared the other restatements of WAY-294's rule with the entry: the script's description
  (`remarks_check.py:19-30`: "a report with no section gives no item"), `task-cycle/skill/SKILL.md:495-499`
  (unchanged, does not state the forms), and the new text of WAY-294. They agree. No contradiction.
- WAY-290 (`:9362`) and WAY-291 (`:9396`) — the script that checks the form of the request's description and what
  happens when it errs; opened as the nearest analogue of a check script and of a script's exception. Not
  contradicted; they give no rule about the remarks script.
- WAY-313, WAY-314, WAY-315 (`:10262`, `:10299`, `:10332`) — a decision as material for refinement, consent to a
  change of a decision, from when a decision binds. The change of WAY-294 and the exception to WAY-344 come from
  the accepted task (question 1, answered by the human), i.e. made at refinement, before the cycle; in the cycle
  nobody departs from a decision on their own. No contradiction.
- WAY-323 (`:10642`) — what the private-path script takes for a path or note link; opened because it shares the
  cycle's checks on the record. Unrelated to the range. The added lines hold no absolute path and no note link.
- WAY-325 (`:10755`) — the orchestrator's reaction to unread material. Not changed by the range and not
  contradicted by the new text of WAY-294.
- WAY-343 (`:11290`) — which version a cycle of the-way ran on. Not touched.
- WAY-159 (`:4621`) — the orchestrator relies on a command and exit code. The range changes nothing here.
- WAY-298 (`:9651`) — a cycle on the-way itself starts from the current rules. Not touched.

Read whole (earlier, in the first report): WAY-38, 125, 294, 296, 308, 309, 326, 344, and the row of WAY-157.

## Titles read but not opened (judged to bear nothing on the change)

All other titles: the part map, invariants, glossary, environment facts, project definition and plan, technology
step, guidelines (coding, tests, styleguide, failures and logs), mutation tools, audits of skills of guidelines,
the request's description (WAY-286..293), foundation review (WAY-300..305), screenshots (WAY-316..319), the
audit of the process (WAY-329..342), WAY-148/150/160..164 of the review loop. Two points I chose not to open
whole although their titles are near the topic: WAY-128/131/133 (instruction files loaded into every session —
`SKILL.md` is not loaded into every session) and WAY-259 (an installed skill entry point; the change adds no
skill and changes no description). WAY-150 (what skills read of the foundation) was named in the dispatch's
Unread list of the earlier review as screened; its text concerns what a reviewer reads, not what the change writes.

## Findings

None. A check of consumers of the changed script, not asked for by a decision: `process-audit/audit_count.py`
imports `remarks_check` but uses only `fenced_flags`, `indent_of`, `reads_none` and `split_lines`, none of which the
range changes (`git diff` touches `split_items`, adds `opens_paragraph`, edits `section_items`). So the audit's
counts do not move.

## Checks

- `git rev-parse HEAD` -> 8dae4be92c7869e708ff66025b58b4b235878e4d.
- `grep -n "^### WAY-" foundations/decisions.md | wc -l` -> 302.
- `python -B elements/common/foundation_check.py --skip-test-citations .` -> exit 0, "0 errors" (identifiers,
  relations and references of the decision log are valid with `narrows WAY-344`).
- `python -B gate/run_tests.py process-audit` -> exit 0 (124 tests OK).
- grep of the repository (outside `.runs`) for other restatements of the script's section rules and for
  `remarks_check` users -> `process-audit/audit_count.py`, its test, `task-cycle/record_template.md:192,198`
  (about the remarks block, not the sections), `task-cycle/test_private_paths_check.py:126` (a file name in a
  fixture). None restates the changed rules.

## Unread material

- 302 titles read. Opened whole beyond the earlier set: WAY-05, 07, 18, 22, 25, 32, 36, 71, 72, 130, 256, 263, 290,
  291, 298, 313, 314, 315, 323, 325, 343, 159 (22 decisions). Read by title only and not opened: the remaining
  decisions, the groups listed above.
- Titles near the topic that I chose not to open, for the orchestrator to weigh: WAY-128, WAY-131, WAY-133 (instruction
  files loaded into every session; `SKILL.md` is not one), WAY-259 (installed skill entry point; no skill added and
  no description changed), WAY-150 (what skills read of the foundation; not what the change writes).
- WAY-148, 260, 295, 328, 30 were read earlier by others, as the coordinator says; I did not reread them here.
- Invariants, part-map entries and glossary entries: not part of this dispatch; not read.

## Searches not found or unclear

- None unclear. The earlier Minor 2 (`remarks_check.py:190-200`, a label right after a list item is not read)
  stays as reported in `review-gap-report.md`; no decision of the 302 titles bears on it.

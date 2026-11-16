# Correction 1 — report

**Status:** done. **Commit:** `d7323f17` (10 files, +219 −176) on the head `4d7ad796`.

## What the remark binds, and the word chosen

Item 2: after the change, "entry" in the-way's English text is to mean only an entry of the foundation. The places
that named an item of a list under an item of a cycle's record "entry" now say **"sub-item"**.

- Why not "row": the lists are bullet lists nested under an item of the record (`- Discarded attempt:`, `- Review rounds:`,
  `- Process remarks on the-way:`), not tables; "row" stays for the lines of the record's tables (Slices, Events, the
  questions table), where the text already says "row".
- Why not "item": the record already calls its own top-level lines "items" ("the record's item *Review rounds*", "a line at
  the left margin ends the item"); "an item of the item" would read as the top-level line itself. A list item under one is
  therefore a "sub-item".
- Where a plain word names the thing exactly, I used it: "its copy in the remarks" (WAY-309's rationale: "a report's item and
  its copy in the remarks").
- Nothing in these places needs a word that no plain word covers; nothing for the description to flag beyond the choice of
  "sub-item" itself.

## Places changed (file; before → after; why)

All "entry"/"entries" → "sub-item"/"sub-items" (with "an" → "a") unless said; each is an item of a list nested under an
item of the record.

- `task-cycle/record_template.md`: *Discarded attempt* ("one entry for each attempt"), *Review rounds* (two "one entry for
  each", two "opening the entry as written here"), the line of *Process remarks on the-way* ("the entries under this line"),
  the paragraph on the remarks' form ("the entries indented under it … every line of an entry indented under the entry").
- `task-cycle/skill/SKILL.md`: "The entry of the round in the record's *Review rounds*"; the two passages on *Discarded
  attempt* ("an entry of its own … rewritten as an entry too", for `open design choice` and for `size`); the process-remarks
  steps ("as an entry in the form", "item as an entry of its own", "as an entry of your own", "no second entry").
- `task-cycle/skill/correction.md` and `task-cycle/skill/reserved_return.md`: the same *Discarded attempt* sentence.
- `process-audit/SKILL.md`: the description of how the answers of Q1 read the record (seven uses).
- `process-audit/audit_count.py`: module docstring (the *Remarks* figure, *Fix rounds*, Q1 and Q2) and the docstrings and
  messages of `remarks_count` and `read_too_large`: "the item `Process remarks on the-way` holds no sub-items under it …",
  "reads neither none nor a sub-item per slice", and the reason `the sub-item of a round does not say whether there was a
  contradiction`.
- `process-audit/record_items.py`: its docstrings and comments, and the messages of the reading of *Review rounds* and
  *Discarded attempt* ("holds text beside its sub-items", "does not give its sub-items, so whether a review round found a
  contradiction is not known", "is no sub-item or stands at another indent than its sub-items …", "a sub-item of the item
  … opens with no marker …", "a sub-item for each round").
- `foundations/decisions.md` (the word only; every sentence keeps its meaning): WAY-309 (the remarks: "appends no
  sub-item", "appends a second sub-item", "its copy in the remarks"), WAY-337 (*Review rounds* "takes a sub-item for a
  review", its *Verification* and *Rejected*), WAY-404 (the mark in "the sub-item of the round", its *Verification*,
  *Rejected*), WAY-405 (*Discarded attempt*: "each sub-item under the item", "Where the lines are sub-items at one indent
  alone and nothing stands beside the colon", *Verification*).
- Tests: `process-audit/test_record_items.py` and `process-audit/test_audit_count.py`: the constants and the expected
  substrings of the messages above (`BESIDE`, `SILENT`, "does not give its sub-items", "beside its sub-items", the reason of the
  contradiction), comments, test data labels, and the quotes of the clauses `# decision: WAY-337 / WAY-404 / WAY-405 "…"`,
  changed together with the decisions they quote. **Changed expected values** (rule "Changing an existing test"): cause
  — the messages of the script name the record's items, which the correction renames (the remark of the human, item 2);
  evidence — `reports/correction-1-remarks.md`; no assertion weakened or removed; input handling of `audit_count.py` and
  `record_items.py` unchanged.
- Lines the rename lengthened over 100 columns were broken again (no word changed), except `# decision:` quote lines and
  lines already over 100 before.

Code names stay: `ROUND_ENTRY`, `REVIEW_ENTRY`, `discarded_entries`, the variables `entry`/`entries`, `entry_path`,
`REGISTER_ENTRY` and the like.

## Kinds of "entry" left, with file and reason (for the orchestrator to tell the human)

1. **Entry of the foundation** (decisions, invariants, terms, facts, part-map entries; "projected entry"; the plan's table of
   projected entries and its heading `Entry`; the request's section *Foundation entries*): the meaning the word keeps. Many files.
2. **Item of a plan's log of changes**: `foundations/decisions.md:3814` (WAY-145: "an entry in the plan's log of changes")
   and `project-level/lead/skill/SKILL.md:81` ("their change-log entries"). It is a list of a project plan, not of the cycle's
   record, so it is outside the human's remark and the handoff ("do not widen"). **It is a use of "entry" that is no entry of the
   foundation**; the claim "entry means only an entry of the foundation" stays false until these two are changed too. Cost: two
   one-word edits, in a decision (WAY-145) and a skill. Say so in the description and let the human decide.
3. **Entry of the registry of runs of the gate**: `task-cycle/gate_times.py` (docstring, "deletes the entries that are too old"),
   `foundations/invariants.md` `gate-times-refuses-impossible-entry`, `foundations/decisions.md` (the same registry, "an entry
   whose times cannot be"). A line of a file of the script's own, not of the record or the foundation. Not in the human's remark.
4. **Entries of the output of a tool**: `git worktree list` (`task-cycle/remove_merged_worktrees.py`), git trees
   (`process-audit/audit_count.py`, `tree_entries`), session transcripts (`task-cycle/cycle_stages.py`,
   `cycle_measures.py`, their tests), `change_file_sizes.py` (class `Entry`, code names). Names in code and words of another
   field.
5. **Entry of the decision log in a script that compares or indexes the log** (`elements/common/compare_log_entries.py`,
   `decision_index.py`, `foundation_check.py`): the foundation's entries.
6. **A generic "entry" in a list of kinds of source**: `project-level/lead/conversation_template.md:77` ("file/entry/section"),
   `project-level/lead/answering.md:23` ("file/section/entry or line"): a place in a source of any kind (a note, a decision,
   a ticket), not the record. Left; could be changed to "passage" if the human wants the claim to hold for these too.
7. **"entry point"** (skill entry points, `.claude/skills/`, `.agents/skills/`): another word, kept.
8. **Test data holding the word as the text of a record**: `process-audit/test_record_items.py` (`entries none`, a text
   of a discarded attempt: foundation entries).

## Glossary decision

None added. "sub-item" is an ordinary word of the field and a reader who knows the field reads every sentence above right, so
WAY-95 gives it no entry; "row" and "item" are not new words either. The entry `entry` is unchanged (*Not:* none) and now
holds for the record's lists too, apart from kinds 2, 3, 4 and 6 above. I wrote no entry, so `elements/glossary/skill/SKILL.md`
was not followed.

## Checks (command, exit code)

- `python -B gate/run_tests.py process-audit` — 0 (276 tests)
- `python -B gate/run_tests.py task-cycle` — 0 (skipped 2, as before)
- `python -B gate/run_tests.py product-guidelines` — 0
- `python -B gate/run_tests.py gate` — 0
- `python -B gate/run_tests.py elements/common` — 0 (270 tests)
- `python -B elements/common/foundation_check.py` — 0, "0 errors"
- `python -B agent-instructions/skill_entry_points.py --write` — "entry points are current" (no skill description changed)
- Not run: the full gate; `project-level` and `agent-instructions` runs (no file there changed).

## Own-work check (WAY-164)

The requirement most likely missed: a use of "entry" for an item of the record's lists left in a file I did not think of.
Check: `git grep -n -i -w "entry|entries"` over every tracked file but the generated entry points and the decision log, then
over the log, filtered to lines that also hold `round|attempt|remark|record|stage report|sub-item`: what remains is foundation
entries, code names (`ROUND_ENTRY`, `discarded_entries`, `entries`, `entry` as variables), `test_remarks_check.py` (`cycle_with(*entries)`
and "glossary entry"), and the kinds listed above. A second check: the `# decision:` quotes of the tests equal the sentences of
the decisions as changed (the tests of `process-audit` and `foundation_check.py` pass).

## Unread material

- `task-cycle/change/SKILL.md`, the handoff and the remarks: read whole. WAY-95, WAY-97, WAY-99 were read in the first part of
  this cycle (the task's text of them); I did not reread them whole. The decisions I changed (WAY-309, WAY-337, WAY-404, WAY-405)
  were read at the passages changed, not whole. `guidelines/coding.md` and `guidelines/testing.md` read whole in the first
  part. `task-cycle/remarks_check.py` was searched, holds no use of the word, not read whole.

## Searches not found or unclear

- The handoff lists `task-cycle/skill/blocked_finding.md` and `task-cycle/skill/foundation_step.md`: neither holds a use of
  "entry" for an item of the record (the second holds only foundation entries).
- The handoff says "about 13 places": the search found more (about 120 lines, because the audit's scripts and tests and four
  decisions name the same items).

## Working copies

`.runs/author-correction/` held my scripts (`lines.py`, `wrap2.py`, the edit scripts), the outputs of the runs and a list
of paths. Removed before this return; nothing remains.

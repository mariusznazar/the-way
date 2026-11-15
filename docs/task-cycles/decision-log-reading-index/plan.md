# Plan — the way: how an agent reads the decision log — a generated index instead of titles, the log divided into topics, a measure before and after

- Task: `.runs/task-cycles/decision-log-reading-index/task.md`
- Spec: none
- Base: 21ecb627f885de438e2209d7ff5c137b1e1b9d83

How the change is divided. Every edit of `foundations/decisions.md` — the entries the rows below
change and the division of the log into sections — is foundation work made by the agent of the
plan's *Foundation entries* before Slice 1, never a slice: the log is 721 002 characters, which
`task-cycle/slice_size.py` reads whole for any slice that changes it, and that alone is over the
limit of one slice. The slices change files outside `foundations/`, save `foundations/part_map.md`,
whose sentence of `elements-common` the slice that adds a script changes. After the division every
entry of the log stands on other lines than at the base: the ranges of `foundations/decisions.md`
in *Read* are the entries' lines at the base 21ecb62, the address of each entry is its identifier,
and an agent finds it in its own tree by its heading `### WAY-NN —`.

The task was written on a log of 331 decisions (`foundations` at `f4af75d`); at the base the log
holds 198, and two decisions the task names were withdrawn since: WAY-326, whose rule stands in
`task-cycle/skill/SKILL.md` (the paragraph of the stage reports, the sentence "A decision the
reviewer of the whole change read by title as WAY-150 gives is no gap"), and WAY-347, whose rule is
the second paragraph of WAY-339. Row 7 of *Settlements to record* therefore goes to WAY-339, and
*To do* 4's "WAY-326" is that paragraph of `task-cycle/skill/SKILL.md`.

## Foundation entries

| Entry | Kind | From | What depends on it |
|---|---|---|---|
| F1 — WAY-150: an agent that selects reads the index of its selection of decisions and opens whole only the decisions the work changes, goes against or proposes another answer to (that one with its rejected options), those the task or the work's source names and those whose binding sentences leave open what the work has to do; the reviewer of the whole change reads the index of its whole selection and states how many decisions it read whole | change of a decision's binding sentences, *Verification* examples, rationale and *Rejected* (the rejected "a separate maintained index" is taken in the form of an index made on demand, which does not drift; the maintained file stays rejected, as question 1 gives) | Settlements row 1; question 0 | Slices 3, 4 |
| F2 — WAY-150: the index is no file of the repository; a script of the-way writes on demand the index of the selected decisions — number, question, binding sentences, *Scope* | change of a decision (a paragraph of WAY-150) | Settlements row 2; question 1 | Slices 1, 3 |
| F3 — WAY-150: in a log with topical sections the agent picks the sections of the work's topics and reads the index of their decisions, runs through the questions of the decisions outside those sections whose *Scope* names a touched part, and opens those that point to a bearing on the work | change of a decision (a paragraph of WAY-150) | Settlements row 3; question 2 | Slices 1, 3, 4 |
| F4 — WAY-18: the log has topical sections, with the numbers unchanged; a new entry stands at the end of the section of its topic, and where none fits, in a new section at the end of the log, which the request names; "with no view generated from it" stays true, since the index is no file | change of a decision's binding sentences, examples, rationale and *Rejected* | Settlements row 4; question 3 | F10; Slices 2, 3, 4 |
| F5 — WAY-150: a decision whose sentence a test the work alters holds by a line `decision:` joins the selection and is read whole | change of a decision (a sentence of WAY-150) | Settlements row 5; *To do* 3 | Slice 3 |
| F6 — WAY-150: in a log without topical sections the selection stays by the product's parts, and the index takes the place of reading the decisions whole | change of a decision (a sentence of WAY-150) | Settlements row 6; *To do* 7 | Slices 1, 3 |
| F7 — WAY-339, its second paragraph (the successor of the withdrawn WAY-347): the measures of context use count, for each agent of the cycle, the bytes of the decision log and of the index that entered its context and how many times | change of a decision's paragraph and its examples | Settlements row 7; question 4 | Slice 5 |
| F8 — WAY-287: the item of the incomplete reading of the review of the whole change follows the reading F1 gives — a reviewer that did not read the index of its whole selection, or named a decision bearing on the change as unread — in place of the reading by title | change of a decision's binding sentence, examples and rationale, which follows from F1 | *To do* 4 ("from every place of the-way that describes it today"); consequence of F1 | Slice 4 |
| F9 — WAY-21: its rationale and *Rejected*, which refuse topics ("Topics cannot be derived from changed files"; "topics — cannot be derived from a change"), give the selection by topic beside the selection by *Scope*, which stays as the safeguard; the binding sentence does not change | change of a decision's rationale and *Rejected* only | *Decisions in play* (WAY-21); *To do* 7; question 2; *Acceptance criteria* | Slice 3 |
| F10 — the division of the-way's decision log into 20–30 topical sections, each with a heading and one sentence of what it covers, the entries' numbers and text unchanged | edit of the log's form; no entry's text changes | *To do* 5; question 3; F4 | Slices 1, 2 |

The agent of the foundation entries writes F1–F9 through `record-decision`, as the task's rows and
its *Decisions in play* give them, and F1, F2, F3, F5 and F6 in one change of WAY-150, each part
of another question a paragraph of its own as WAY-05 gives; it brings each changed decision's
*Verification* examples into line with its new sentences — WAY-150's "reports "40 read whole, 111
by title only"" and WAY-287's "ran through none of the other 111 by title" among them — so that
each stays held as WAY-12 gives, and runs `elements/common/foundation_check.py --skip-test-citations`
after them. The acceptance criterion names the rejected options of WAY-150, WAY-18 and WAY-21 that
the change takes in: the entries' *Rejected* and rationale say it, and the request names it.

Then it makes F10 as one commit of its own that changes only the order of the entries, the section
headings with their sentences and, where it has to, the log's opening paragraph; the list of
withdrawn identifiers stays last and unchanged. Each section is a heading `## <topic>` followed by
its one sentence; no section is named "Withdrawn identifiers". The assignment of each entry is read
off the entry's own question and *Scope* — its heading and its `- **Scope:**` lines — and never
guessed from its number; inside a section the entries keep their relative order. 20–30 sections
over 198 entries gives some 7–10 entries each. It checks its own division, in its directory for
working copies, by comparing each entry of the log before the commit with the same entry after it,
and runs the foundation check again. Its report gives the list of sections — heading, sentence,
number of entries and the numbers it holds — the commit of the division and the commit before it,
for Slice 2 and the request.

The edits of the files that restate the rules come after: the reading rule
(`elements/common/way_of_working.md`, "Reading the foundation"), the decisions template ("Where
entries go") and the two files of `project-level/lead/` that restate "whole selected entries" in
Slice 3; the reviewer's instruction (`task-cycle/review/SKILL.md`), the stage reports' paragraph of
`task-cycle/skill/SKILL.md` that holds WAY-326's rule, and the request template
(`task-cycle/skill/request_template.md`, item 14 and the lower part's **Foundation entries**) in
Slice 4; WAY-339's measure in `task-cycle/cycle_measures.py` in Slice 5.

## Slices

### Slice 1 — The index script

- **Goal:** a script of the-way, `elements/common/decision_index.py`, writes to a file the agent
  names the index of the decisions it selects from a product's decision log, with its tests in
  `elements/common/test_decision_index.py`, and the sentence of `elements-common` in
  `foundations/part_map.md` names the script among what the part answers for. The script works on
  the log of any product, run from the product's pinned copy of the-way as from the-way itself,
  with sections and without them: it takes the product's root as an optional positional argument,
  the working directory by default, and reads `foundations/decisions.md` under it, reading a
  byte-order mark and CRLF line endings as well as LF. Its selection is given by switches:
  `--part ID` (repeatable) selects the decisions whose *Scope* names the part as a whole item, read
  as the reading rule reads *Scope* today (each `- **Scope:**` line with its indented continuation
  lines, items joined by `,` or ` · `); `--section HEADING` (repeatable) selects every decision of
  that topical section, a section being a `## ` heading of the log other than "Withdrawn
  identifiers", named by its heading's text; `--decision NUMBER` (repeatable) adds a decision by its
  number; `--output PATH` names the file it writes, in UTF-8. For each selected decision the index
  gives its number, its question as its heading gives it, its binding sentences — every paragraph
  before its first field, not the first only, as the check's `binding` reads them (WAY-05) — and
  its *Scope*. Where `--section` and `--part` are both given, the index adds after the decisions of
  the sections the headings alone — number and question — of the decisions outside those sections
  whose *Scope* names a given part. The switch `--sections` writes instead the list of the log's
  sections, each with its heading, its sentence and the number of its entries. The index opens with
  one fixed title line that holds the script's name, which Slice 5 recognises in a tool's output,
  and states how many decisions it lists in full and how many by heading alone; the docstring names
  that line, the usage and the exit codes. Exit code 0 when it has written the file; 2 with
  `Error: <message>` on stderr and nothing written for a log it cannot read, a section the log does
  not hold, a number the log does not hold, a selection given no switch, and — WAY-344 — a decision
  that lacks *Scope* or a heading of the log's form, the message naming the file, the entry and the
  field. The script reuses the reading functions of `elements/common/foundation_check.py` (`blocks`,
  `fields`, `binding`) by import, rather than copying them, and needs no git. Each reading the
  script makes has one test that gives the log without a field it needs and asserts the message
  that names it (WAY-344); the tests build their logs in temporary directories, with no absolute
  path in a tracked file.
- **Change:** `elements/common/decision_index.py` · `elements/common/test_decision_index.py` ·
  `foundations/part_map.md`
- **Read:** `.runs/task-cycles/decision-log-reading-index/task.md:33-42` To do ·
  `.runs/task-cycles/decision-log-reading-index/task.md:56-66` Questions to settle (questions 1 and
  2) · `.runs/task-cycles/decision-log-reading-index/task.md:123-135` Settlements to record ·
  WAY-150 as Foundation entries F1–F3, F5, F6 leave it · WAY-18 as F4 leaves it ·
  `foundations/decisions.md:158-207` WAY-05 · `foundations/decisions.md:268-335` WAY-09 ·
  `foundations/decisions.md:1093-1117` WAY-38 · `foundations/decisions.md:8245-8356` WAY-344 ·
  `foundations/part_map.md:65-75` elements-common · `foundations/invariants.md:86-94`
  tracked-file-private-paths · `foundations/invariants.md:116-144` script-language, script-imports,
  script-subprocesses · `foundations/invariants.md:348-356` cross-part-imports ·
  `elements/common/way_of_working.md:58-100` Reading the foundation ·
  `elements/common/foundation_check.py:1-160` · `elements/common/foundation_check.py:236-345` ·
  `elements/common/foundation_check.py:974-989` · `elements/common/test_foundation_check.py:1-30`
- **Model:** cheaper
- **Risk:** none
- **Checks:** first a failing test of the index of a two-section log;
  `python -B -m unittest discover -s elements/common -p test_decision_index.py`; on the-way itself,
  after F10, `python -B elements/common/decision_index.py --sections --output
  .runs/<the executor's directory>/sections.md` lists 20–30 sections, and `python -B
  elements/common/decision_index.py --part task-cycle --output .runs/<the executor's
  directory>/index.md` writes an index whose count matches the decisions whose *Scope* names
  `task-cycle`; `python -B elements/common/foundation_check.py --skip-test-citations` reports no
  error the slice caused
- **Depends on:** F2 · F3 · F6 · F10

### Slice 2 — The comparison of a log's entries, and the check on a log with sections

- **Goal:** a script of the-way, `elements/common/compare_log_entries.py`, with its tests in
  `elements/common/test_compare_log_entries.py`, compares the entries of two copies of a product's
  decision log, given as two file paths: an entry is a block a `### <PREFIX>-<NN> — ` heading
  opens, from its heading to the line before the next heading of any level, without the blank lines
  at its end, keyed by its identifier, and the block of `## Withdrawn identifiers` where it stands
  is compared the same way. It reports each entry that stands in one copy only, each that stands
  twice in a copy, and each whose bytes differ, with the first line that differs; exit code 0 when
  every entry is the same byte for byte, 1 when it reports any, 2 with `Error: <message>` for a copy
  it cannot read or that holds no entry (WAY-344, with one test of it). Its docstring says that it
  serves the division of a log into sections, the-way's or a product's. The sentence of
  `elements-common` in `foundations/part_map.md` names it among what the part answers for. In
  `elements/common/test_foundation_check.py` one test pins that the check reads a log with topical
  sections: the fixture's log divided into two `## ` sections passes as the undivided one does, and
  an error in an entry of the second section is reported at its own line — the check needs no change
  for it, and the slice changes `elements/common/foundation_check.py` only where that test fails.
  With the script the slice confirms the division of F10: the log at the commit before the division
  against the log at the division's commit, both named in the report of the agent of the foundation
  entries, ends with exit code 0, and the slice's report gives the command and its output for the
  request.
- **Change:** `elements/common/compare_log_entries.py` ·
  `elements/common/test_compare_log_entries.py` · `elements/common/test_foundation_check.py` ·
  `foundations/part_map.md`
- **Read:** `.runs/task-cycles/decision-log-reading-index/task.md:33-42` To do ·
  `.runs/task-cycles/decision-log-reading-index/task.md:67-72` Questions to settle (question 3) ·
  WAY-18 as F4 leaves it · `foundations/decisions.md:209-236` WAY-07 ·
  `foundations/decisions.md:1093-1117` WAY-38 · `foundations/decisions.md:8245-8356` WAY-344 ·
  `foundations/invariants.md:86-94` tracked-file-private-paths ·
  `foundations/invariants.md:116-144` script-language, script-imports, script-subprocesses ·
  `elements/common/foundation_check.py:236-251` · `elements/common/foundation_check.py:345-358` ·
  `elements/common/foundation_check.py:416-455` · `elements/common/migrate_foundation.py:133-150`
- **Model:** cheaper
- **Risk:** none
- **Checks:** first a failing test of an entry whose text differs;
  `python -B -m unittest discover -s elements/common -p test_compare_log_entries.py`;
  `python -B -m unittest discover -s elements/common -p test_foundation_check.py`;
  `git show <commit before the division>:foundations/decisions.md > .runs/<the executor's
  directory>/before.md` and `git show <division commit>:foundations/decisions.md > .runs/<the
  executor's directory>/after.md`, then `python -B elements/common/compare_log_entries.py
  .runs/<the executor's directory>/before.md .runs/<the executor's directory>/after.md` exits 0
- **Depends on:** Slice 1 · F4 · F10

### Slice 3 — The reading rule and the template of the log

- **Goal:** "Reading the foundation" in `elements/common/way_of_working.md` gives the reading of
  F1, F2, F3, F5 and F6, and the decisions template gives F4. In "Reading the foundation", step 2
  has the agent that selects run the script of Slice 1 (elements/common/decision_index.py, with its
  usage in its docstring) for its parts — in a log with sections for the sections of the work's
  topics, chosen from the list `--sections` gives, with its parts for the headings outside them —
  read the index, and open whole only the decisions F1 names, those named by the task's *Decisions
  in play* or the work's source among them, and the decisions whose sentence a test the work alters
  holds by a line `decision:` (F5), which it adds to the selection as it adds the invariants such a
  test cites; in a log without sections the selection stays by parts and the index stands in for
  the whole reading (F6). The script's search by parts replaces the search of `- **Scope:**` lines
  by hand. The reviewer of the whole change reads the index of its whole selection and states in
  its report how many decisions it read whole; the reading by title and "no other agent skims" leave
  the rule, and only the run through the headings of the decisions outside the work's sections
  stays (F3). The range of an entry read whole runs from its heading to the next heading of any
  level, since a section heading can follow an entry. The invariants, the part map's entries, the
  glossary and the templates are read as before. In `elements/decisions/template.md`, "Where
  entries go" gives F4 — the log may have topical sections, each a `## ` heading with one sentence;
  a new entry goes at the end of the section of its topic, or in a new section at the end of the
  log, before the list of withdrawn numbers, which the request names — and "Withdrawn numbers" keeps
  that list after the last entry. In `project-level/lead/skill/SKILL.md` and
  `project-level/lead/answering.md`, "whole selected entries" is brought into line with the
  method, so that no file restates whole reading of every selected decision. No entry is worded
  here; the slice carries the entries' meaning into these files and cites them by number.
- **Change:** `elements/common/way_of_working.md` · `elements/decisions/template.md` ·
  `project-level/lead/skill/SKILL.md` · `project-level/lead/answering.md`
- **Read:** `.runs/task-cycles/decision-log-reading-index/task.md:33-42` To do ·
  `.runs/task-cycles/decision-log-reading-index/task.md:44-46` Acceptance criteria ·
  `.runs/task-cycles/decision-log-reading-index/task.md:50-72` Questions to settle (questions 0–3)
  · `.runs/task-cycles/decision-log-reading-index/task.md:79-91` Context ·
  `.runs/task-cycles/decision-log-reading-index/task.md:123-135` Settlements to record · WAY-150 as
  F1–F3, F5, F6 leave it · WAY-18 as F4 leaves it · WAY-21 as F9 leaves it ·
  `foundations/decisions.md:37-81` WAY-02 · `foundations/decisions.md:158-207` WAY-05 ·
  `foundations/decisions.md:420-476` WAY-12 · `foundations/decisions.md:622-653` WAY-19 ·
  `foundations/decisions.md:972-1003` WAY-33 · `foundations/decisions.md:1246-1266` WAY-52 ·
  `elements/decisions/skill/SKILL.md` · `elements/decisions/skill/decide_entry.md` ·
  `elements/common/rules.md`
- **Model:** same — it rewrites the shared reading method that every skill of the-way follows,
  and carries it into the files of three parts
- **Risk:** none
- **Checks:** `python -B elements/common/foundation_check.py --skip-test-citations` reports no error
  the slice caused; `python -B -m unittest discover -s elements/common -p test_*.py`; a run of the
  method on this task's parts with the script of Slice 1, its commands and counts in the report
- **Depends on:** Slice 1 · F1 · F2 · F3 · F4 · F5 · F6 · F9

### Slice 4 — The reviewer, its report and the request

- **Goal:** the reading by title as the main reading leaves every file of `task-cycle` that
  describes it today, and they give the reading of F1 and F3 and the item of F8. In
  `task-cycle/review/SKILL.md`, section 1 has the reviewer of the whole change select by "Reading
  the foundation", read the index of its whole selection, open whole the decisions that method names
  and count how many it read whole, for its report; the paragraph **Unread material** opens, in the
  review of the whole change, with how many decisions of the index it read whole, and goes on with
  each decision that bears on the change and stayed unread and each guideline file it did not read
  whole. In `task-cycle/skill/SKILL.md`, the sentence "A decision the reviewer of the whole change
  read by title as WAY-150 gives is no gap" becomes the same for a decision the reviewer knows from
  the index (the rule that stood in WAY-326). In `task-cycle/skill/request_template.md`, item 14 of
  the top part follows F8 — an item where the reviewer did not read the index of its whole selection
  or named a decision bearing on the change as unread, with how many decisions of the index it read
  whole — and the lower part's **Foundation entries** names each topical section of the decision
  log that the change opens, with its sentence (F4).
- **Change:** `task-cycle/review/SKILL.md` · `task-cycle/skill/SKILL.md` ·
  `task-cycle/skill/request_template.md`
- **Read:** `.runs/task-cycles/decision-log-reading-index/task.md:33-42` To do ·
  `.runs/task-cycles/decision-log-reading-index/task.md:79-91` Context ·
  `.runs/task-cycles/decision-log-reading-index/task.md:123-135` Settlements to record · WAY-150 as
  F1–F3, F5, F6 leave it · WAY-18 as F4 leaves it · WAY-287 as F8 leaves it ·
  `elements/common/way_of_working.md` · `task-cycle/review/whole_change.md`
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B -m unittest discover -s task-cycle -p test_request_check.py`;
  `python -B -m unittest discover -s task-cycle -p test_remarks_check.py`; a search of
  `task-cycle/` for "by title" and "title only" finds nothing that describes the reading by title
- **Depends on:** Slice 3 · F1 · F3 · F4 · F8

### Slice 5 — The measure of the log and the index in each agent's context

- **Goal:** `task-cycle/cycle_measures.py` counts, for each agent of the cycle, how many bytes of
  the decision log and of the index entered its context and how many times (F7), in four columns
  added to the end of the table of agents — the log's bytes, the log's reads, the index's bytes, the
  index's reads — with no new line among the cycle-level lines before `## Agents`, which
  `process-audit/audit_count.py` reads by their labels. The recognition, which settles the task's
  first question carried to the cycle: in a Claude Code transcript a read is a block `tool_use` of
  an assistant line paired by its id with the block `tool_result` of a later line; it is a read of
  the log where a text value of the tool's input — a file path, a search path, a shell command —
  names a path ending in `foundations/decisions.md`, with `\` taken as `/`, and a read of the index
  where the text of the result holds the index's title line that Slice 1 fixes; its bytes are the
  UTF-8 bytes of the result's text as the transcript holds it, its text blocks joined, nothing else
  counted. What stays approximate, said in the docstring: a search or a command over a directory
  that holds the log without naming it is not counted; a command naming the log counts its whole
  output, other files' lines included; a result the tool cut or kept in a file counts what the
  transcript holds; a copy of the log under another path (the-way's own log in a product's
  `.the-way/` is counted, since it ends with that path) or passages of it in a handoff are not
  counted. A Codex agent is read by the same rules on its rollout's records of a tool call and its
  output where the slice's agent can confirm their form from a real rollout under the Codex home,
  copying no content of it into a test; where it cannot, the four figures of a Codex agent are
  `unknown`, never zero, as its cache figures are. The reading of the transcript is reworked, so
  each field the new reading needs — the tool block's id, name and input, the result's
  `tool_use_id` and content — ends the run with exit code 2 and a message naming the file, the line
  and the field where it is missing (WAY-344), with one test of it; a result whose id no `tool_use`
  of the agent names is not counted and is no error. The transcript is untrusted input (the part
  map's trust boundary): a content that is no string or list, a list of blocks that are no objects,
  a huge text or a deeply nested line end the reading with exit code 2 or are not counted, never
  with a traceback, and nothing from a transcript reaches the file except through `cell`. The tests
  give hand-worked figures for a transcript with a Read of the log, a shell command naming it, a
  Read of the index and a search elsewhere, with relative paths only. The docstring says what is
  counted and what stays approximate. `process-audit/audit_count.py` and its test stay as they are:
  a change of the script starts a new series of these measures by itself (WAY-339).
- **Change:** `task-cycle/cycle_measures.py` · `task-cycle/test_cycle_measures.py`
- **Read:** `.runs/task-cycles/decision-log-reading-index/task.md:33-42` To do ·
  `.runs/task-cycles/decision-log-reading-index/task.md:73-77` Questions to settle (question 4) ·
  `.runs/task-cycles/decision-log-reading-index/task.md:93-96` Questions carried to cycle ·
  `.runs/task-cycles/decision-log-reading-index/task.md:123-135` Settlements to record · WAY-339 as
  F7 leaves it · `foundations/decisions.md:1093-1117` WAY-38 · `foundations/decisions.md:1170-1198`
  WAY-48 · `foundations/decisions.md:8245-8356` WAY-344 · `foundations/part_map.md:94-104`
  task-cycle · `foundations/part_map.md:117-127` process-audit · `foundations/part_map.md:243-250`
  External context · `foundations/invariants.md:86-94` tracked-file-private-paths ·
  `foundations/invariants.md:116-144` script-language, script-imports, script-subprocesses ·
  `process-audit/audit_count.py:129-145` · `process-audit/audit_count.py:179-185` ·
  `process-audit/audit_count.py:644-665` · `task-cycle/skill/SKILL.md:548-570` · the docstring of
  elements/common/decision_index.py, made by Slice 1, for its title line
- **Model:** same — the orchestrator's change at the plan's review (WAY-229): the slice reworks the
  reading of transcripts in a file the part map names as a trust boundary and must hold crafted
  input to exit code 2 or to uncounted, never a traceback; a failed `cheaper` executor would cost a
  retry and a second review of the boundary
- **Risk:** trust boundary — `task-cycle/cycle_measures.py`, which reads session transcripts from
  outside the repository
- **Checks:** first a failing test of a transcript with one Read of the log;
  `python -B -m unittest discover -s task-cycle -p test_cycle_measures.py`;
  `python -B -m unittest discover -s process-audit -p test_audit_count.py`
- **Depends on:** Slice 1 · F7

## Coverage

| What the task requires | Slices or entries |
|---|---|
| Outcome: the reviewer of the whole change and the authors read the index of their selection instead of knowing decisions by title or reading too much | F1–F3, F5, F6; Slices 1, 3, 4 |
| *To do* 1 — the index script, with tests, on any product's log, with sections and without | Slice 1; F2 |
| *To do* 2 — the reading rule and WAY-150: the index, and whole reading of the kinds named | F1; Slice 3 |
| *To do* 3 — decisions held by a `decision:` line of an altered test join the selection and are read whole | F5; Slice 3 |
| *To do* 4 — the reviewer reads the index of every selected decision and states how many it read whole; the reading by title leaves the rule, the reviewer's instruction, **Unread material**, WAY-326's rule and the request template | F1, F8; Slice 3 (the rule), Slice 4 (the instruction, the report, `task-cycle/skill/SKILL.md`, the request template) |
| *To do* 5 — 20–30 sections, numbers and text unchanged, confirmed by a comparing script; the request shows the list with counts and sentences and the script's result | F10 (the division and its list); Slice 2 (the script and its run); Slice 1 (`--sections` gives the counts); the request, by the orchestrator |
| *To do* 6 — the template and WAY-18: sections, a new entry at the end of its section or in a new section at the end, named in the request | F4; Slice 3 (template); Slice 4 (request template) |
| *To do* 7 — the selection by topic with the run through the headings outside the sections; a log without sections stays by parts | F3, F6, F9; Slices 1, 3 |
| *To do* 8 — `cycle_measures.py` counts the log's and the index's bytes and reads per agent; WAY-347's rule (now WAY-339) gets it | F7; Slice 5 |
| *To do* 8 — the measure "before" on the last game cycle and the last the-way cycle, in the request | the orchestrator, after Slice 5 (see the note below the table) |
| *Acceptance criteria* — the request names, at WAY-150, WAY-18 and WAY-21, the rejected option the change takes in | F1, F4, F9 (the entries say it); the request, by the orchestrator |
| Question carried to cycle 1 — how the measure recognises a read of the log or the index | Slice 5 (its *Goal* settles it and names what stays approximate) |
| Question carried to cycle 2 — where the sessions of the "before" measure come from | the orchestrator (see the note below the table) |
| Settlements row 1 | F1 |
| Settlements row 2 | F2 |
| Settlements row 3 | F3 |
| Settlements row 4 | F4 |
| Settlements row 5 | F5 |
| Settlements row 6 | F6 |
| Settlements row 7 | F7 (WAY-339, the successor of WAY-347) |

The "before" measure is the orchestrator's and no slice runs it. It needs, once Slice 5 is made:
the session id or transcript path of the orchestrator of the last task cycle of the game product and
of the last task cycle of the-way that ran before this change, with their subagents' transcripts
still beside them under the Claude Code home (or their rollouts under the Codex home); a run of the
extended `task-cycle/cycle_measures.py` of this branch on each, with `--output` to a file under
`.runs/task-cycles/decision-log-reading-index/`; and, in the request, the four new columns of each
agent of the two runs, with the name of each cycle measured.

## Choices

| Choice | Way rejected | Cost if wrong |
|---|---|---|
| The edits of the entries and the division of the log (F10) are made by the agent of the foundation entries before Slice 1, the division as one commit of its own | the division as a slice after the scripts — the size script reads the 721 002 characters of the log whole for any slice that changes it, over the limit of one slice; the orchestrator may give F10 to a second agent of the foundation entries after F1–F9 | one agent carries rewrites of five decisions and the assignment of 198 entries; the ranges in *Read* point to the base, and each slice finds its entries by heading |
| The comparing script is a committed, tested script in `elements/common/`, run by Slice 2 on the division made before it | a throwaway script of the agent that made the division — it would confirm its own work, and the division of the game's log in its own task would write it again | a script and its tests kept in the-way for a use that may come once more |
| The index script and the comparing script stand in `elements/common/`, beside the check whose reading functions they import | `elements/decisions/` — the map allows its import from `elements/common/`, but the reading method that runs the index lives in `elements/common/`, and the scripts that read a product's whole log would stand apart from the check whose functions they share | a reader of `elements/decisions/` does not find the scripts of its log there; the part map's sentence names them |
| The index script takes its selection by switches (`--part`, `--section`, `--decision`, `--sections`) and reads `foundations/decisions.md` under the root it is given, without git | the selection read from a list of changed files through the part map — that is the reading rule's step 1, which the agent makes; a run through git — the index needs nothing from history | an agent names the parts itself, as today |
| The index script takes no list of altered tests; the reading rule has the agent find the `decision:` lines of the tests the work alters, as it finds their `invariant:` lines, and name their numbers by `--decision` | a switch reading the test files — a second reader of `decision:` lines beside the check | one search by hand per change, as for invariants |
| The measures of the log and the index are four columns at the end of the table of agents, and no cycle-level line is added | new cycle-level lines — `process-audit/audit_count.py` reads those lines by label, and a label beginning with an existing label and " and " is read as that label; adding them to the audit's labels would make every earlier file a missing field | the weekly audit does not show the new measure until a later task adds it with the earlier form read as unknown |
| `process-audit/audit_count.py`, its tests and its fixture of the measures file stay as they are | the fixture's header brought to the new columns — its file is 183 489 characters, and the audit reads no column of the table | the fixture shows the table of agents of the earlier form |
| A read of the log is recognised by a path ending in `foundations/decisions.md` in the tool's input, and a read of the index by its title line in the tool's output | recognition of the log by its content — a handoff or report quoting an entry would count; recognition of the index by its path — the agent chooses the path | reads through a directory search and passages carried in handoffs go uncounted, as the docstring says |
| The handoffs keep naming foundation entries by identifier, each read whole; F1's index binds the agent that selects | an index carried into each handoff — the task settles the reading of the agent that selects (rows 1 and 3: "its selection") and nothing of a handoff | an executor's handoff stays the size the orchestrator's choice gives it |
| WAY-150, WAY-18, WAY-287 and WAY-339 stay held by their pairs of examples, brought into line with their new sentences | a line `decision:` in the new tests holding a sentence of WAY-150 — a test of a script cannot hold a rule of reading | none beyond today's |
| 20–30 sections, as *To do* 5 and question 3 give, of some 7–10 entries each over the 198 entries the log holds today | "po kilkanaście" (11–19 entries each) — it was counted on the 331 entries of `f4af75d`, and over 198 it gives 11–18 sections, below the range the answer to question 3 gives | the human may ask at the merge for fewer, larger sections; the comparing script makes a second division cheap to confirm |
| `elements/common/migrate_foundation.py`, `installation/install.py` and `elements/common/foundation_check.py` do not change; Slice 2's test pins that the check reads a log with sections | a change of each consumer of the log's form — the check closes an entry at any heading, the migration cuts at headings of every level up to the third and keeps a section's text, and the installer writes a log with no entry | a consumer found later that reads entries only up to the next `###` would take a section heading into an entry; the comparing script would show it |

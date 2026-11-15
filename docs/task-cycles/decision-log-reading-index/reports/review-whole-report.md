FAIL 55f1a24ddcece1ba8c48a5e27595a34072939359

# Review of the whole change — task `decision-log-reading-index`

- Range: `21ecb627f885de438e2209d7ff5c137b1e1b9d83..55f1a24ddcece1ba8c48a5e27595a34072939359`
  (`git rev-parse HEAD` in the worktree gave `55f1a24ddcece1ba8c48a5e27595a34072939359`; tree clean).
- Method: `task-cycle/review/SKILL.md` and `task-cycle/review/whole_change.md` at the head, read whole;
  the foundation selected by "Reading the foundation" in `elements/common/way_of_working.md` as the
  change rewrote it, with `elements/common/decision_index.py`.
- Read whole: the handoff, the frozen task, the plan, the reports of the foundation agent (with Fix
  1) and of the executors of slices 1–4, and the diff of every file of the range except the 15 127
  lines of the division commit `104e126`, which I checked by script (see Checks).

Blocking: 1 (Important). Minor: 6, of which 1 outside the task. Out of scope: 1 (the Minor one
outside the task) and the 4 lines of *Declined to judge*.

## Findings

### Important

**I1 — WAY-150 now leaves a decision that a selected entry links to unread beyond the index, while
its own example and the reading rule read it whole.** Comes from the plan's *Foundation entries*:
Fix 1, `dbdfdad` (F1, WAY-150), meeting slice 3, `3cec41a`, which kept step 3 of the reading rule as
it stood. It spans the foundation work and slice 3.

- Where:
  - `foundations/decisions.md:1474-1481` (WAY-150, first paragraph, second sentence): "Of the
    decisions it selects, whoever selects reads the index and opens whole only the decisions the
    work changes, goes against or proposes another answer to […] those whose sentence a test the
    work alters holds by a line `decision:` and those whose binding sentences leave open what the
    work has to do; each selected entry that is no decision — an invariant, an entry of the map of a
    touched part, or an entry other than a decision that these link to — it reads whole". The first
    sentence puts "the entries these link to as far as the work needs" into the selection, so a
    decision an invariant derives from, or a decision another selected decision names in
    *Relations*, is a selected decision: known from the index, opened whole only if it falls in one
    of the five kinds.
  - `foundations/decisions.md:1511-1516` (WAY-150's complying example): "reads whole the invariants
    naming `gate` or `every` and the entries they link to" — the entries an invariant links to are
    its *Derives from* decisions and *Rests on* facts, so the example reads those decisions whole.
  - `elements/common/way_of_working.md:113-117` (step 3, unchanged by slice 3): "and the entries
    these and the decisions of step 2 link to — *Relations*, *Based on*, *Verification*, *Derives
    from*, *Rests on* — as far as the work needs them, each whole." Step 2's switches add to the
    index only the decisions of *Decisions in play*, of the work's source and of `decision:` lines
    (`way_of_working.md:95-97`), so a linked decision never reaches the index; step 3 has it read
    whole instead. That contradicts step 2's own "Open whole only …" (`way_of_working.md:98-107`).
- Why it matters: WAY-150's binding sentence and the reading rule that restates it now say two
  things about the same decisions. An agent following `way_of_working.md` reads whole every
  decision that a selected decision or invariant links to — for this change, WAY-150 alone links
  WAY-21, WAY-33 and WAY-148 — which WAY-150's "opens whole only" forbids; an agent or reviewer
  comparing with WAY-150 holds such a decision to the index, which the rule never puts it in. That
  is the rule file restating the entry the change writes "differently, more broadly" (WAY-263), and
  a complying example that does what its sentence forbids, which no longer holds the sentence as
  WAY-12 asks of a pair of examples. Before `dbdfdad` WAY-150 read "it reads every other selected
  entry whole", which matched step 3 and the example; the fix report calls its change "wording
  only", but on linked decisions it changed the meaning.
- Evidence: the three passages above, at the head. `python -B elements/common/foundation_check.py`
  passes (exit 0), since no check reads this.
- What would fix it (one of two, the first smaller): (a) in WAY-150's second sentence, read whole
  the entries the selected entries link to as far as the work needs, decisions included, as step 3
  and the example say — for example "each selected entry that the index does not carry — an
  invariant, an entry of the map of a touched part, or an entry these link to as far as the work
  needs — it reads whole"; or (b) keep WAY-150, add the linked decisions to the index in step 2
  (`--decision`), drop "and the decisions of step 2 … each whole" for decisions in step 3, and
  rewrite the complying example. Variant (a) keeps the plan's sentence for slice 3 ("The
  invariants, the part map's entries, the glossary and the templates are read as before") true.

### Minor

**m1 (within the task) — a line too large for memory ends `cycle_measures.py` with a traceback and
exit 1, not exit 2.** `task-cycle/cycle_measures.py:209-212`, `json_lines` catches `ValueError` and
`RecursionError` from `json.loads`, not `MemoryError`. Slice 5's *Goal* says "a huge text or a deeply
nested line end the reading with exit code 2 or are not counted, never with a traceback", and step 12
of `task-cycle/skill/SKILL.md:563-566` handles only an exit 2 with an `Error:` line. Minor: it needs
a single line that exhausts memory, and the transcript's writer is Claude Code or Codex. This is
review-5's M1, which I grade the same.

**m2 (within the task) — a subtest that asserts nothing.** `task-cycle/test_cycle_measures.py:1174-1177`,
`test_an_output_that_is_no_text_is_not_counted` loops over `(5, {"text": "a"}, None)` and, for
`None`, `continue`s before any assertion; the other two values assert. Drop `None` from the tuple
(its case is tested at `test_a_missing_field_of_a_call_or_an_output_ends_with_exit_2_naming_it`).
Review-5's M2; Minor, since the test as a whole still fails when the behaviour breaks.

**m3 (within the task) — step 12 describes the measures without the log and the index.**
`task-cycle/skill/SKILL.md:560-562`: "run `task-cycle/cycle_measures.py` … it counts the context
and the prompt cache of the cycle's agents." WAY-339's second paragraph (`foundations/decisions.md:7286-7291`)
now names, for each agent, the bytes and reads of the decision log and of the index, and *To do* 8
is about exactly that count. The sentence is not false, only short; an orchestrator reading it does
not learn that the file holds the measure the request's "before" figures come from. Slice 5's
executor reported it; the file is slice 4's.

**m4 (within the task) — a `--part` that no decision names gives an index silently empty of it.**
`elements/common/decision_index.py:109-128`: `python -B elements/common/decision_index.py --part
no-such-part --output …` exits 0 with "Listed in full: 0. Listed by heading alone: 0." With
`--section` given, a misspelled part drops, without a sign, the headings of the decisions outside
the sections — the safeguard F3 and WAY-21's rationale keep "so that a decision of another topic
that governs a touched part" is not lost. An error would be wrong (a new part may have no decision
yet), but a line in the index or on stderr naming each given part that no *Scope* names would show
the typo. Minor: a reasonable user's expectation the plan's list of exit codes does not cover.

**m5 (within the task) — lines past the files' width.** `project-level/lead/answering.md:9` (137
characters; slice 3 rewrapped the line before it and left this one long: "revisions checked. Expand
to the complete source units needed for each question. Unreadable sources are obstacles, not
negative evidence."); `project-level/lead/skill/SKILL.md:35-36` leaves "a large definition/plan by"
as a short line; `task-cycle/cycle_measures.py:83` (124 characters, review-5-fix's N2). Polish.

**m6 (outside the task) — slice 4's own-work check does not reach the requirement it names.**
`reports/executor-4-report.md`, "Own-work check": the requirement named is that the reviewer might
skip the run through the questions outside the topic sections and under-count; the check is a grep
for "by title" and two unit suites, which cannot catch that (WAY-164). I read the slice's three
files against F1, F3 and F8 and the requirement is met, so nothing in the files needs a change; this
is a remark on how the slice was made, outside the task's scope.

### Graded findings of the slice reviews (the dispatch's list)

- M1 (review-5) — m1 above, Minor, within the task.
- M2 (review-5) — m2 above, Minor, within the task.
- N1 (review-5-fix), the `type` of a block or payload not checked — no finding: the plan has
  "anything … that is no tool block is not counted", and a block without `type` is such a block;
  the docstring (`task-cycle/cycle_measures.py:82-83`) says so.
- N2 (review-5-fix), `task-cycle/cycle_measures.py:83` at 124 characters — part of m5.

## Against the task

- *To do* 1 — the script: `elements/common/decision_index.py` with 15 tests; number, question,
  every paragraph before the first field (WAY-05) and *Scope*; selection by part, section and
  number; with and without sections; BOM and CRLF read; root positional, from a pinned copy. Met.
- *To do* 2, 3, 6, 7 — WAY-150 and WAY-18 through the foundation step, the reading rule and the
  template: met, save I1.
- *To do* 4 — the reading by title leaves the rule (`way_of_working.md:108-112` keeps only the
  negation), the reviewer's instruction (`task-cycle/review/SKILL.md:28-33`, `:170-175`), the rule
  that stood in WAY-326 (`task-cycle/skill/SKILL.md:274-276`) and the request template
  (`task-cycle/skill/request_template.md:258-267`); a search of the tree for "by title", "title
  only", "skim", "whose title" and "no topical sections" finds only WAY-150's *Rejected*, the
  negation in the rule and a test fixture (see *Declined to judge*). Met.
- *To do* 5 — 28 sections, 4–10 entries each; my own run of `compare_log_entries.py` on `dae85e1`
  against `104e126` exits 0 with 198 entries the same byte for byte, and on base against head
  reports exactly WAY-18, WAY-21, WAY-150, WAY-287 and WAY-339. Outside the entries the division
  adds only the 28 headings and their sentences (3 lines outside entries before, 90 after). Met in
  the commits; the list and the output in the request are the orchestrator's.
- *To do* 8 — `cycle_measures.py` counts the four figures per agent; WAY-339 (the successor of the
  withdrawn WAY-347) carries the measure. A run on this cycle's own sessions exits 0 and fills the
  four columns. The "before" figures are the request's.
- Rows 1–7 of *Settlements to record*: row 1 WAY-150 ¶1, row 2 ¶2, row 3 ¶3, row 5 ¶1, row 6 ¶3,
  row 4 WAY-18 ¶2, row 7 WAY-339 ¶2 — each says what its row says; I1 is about an addition of Fix 1
  beyond row 1, not a departure from the row.
- *Acceptance criteria*: the entries carry it — WAY-150's *Rejected* keeps "a separate maintained
  index" only as a file of the repository and its rationale says why the on-demand index cannot
  drift; WAY-18's rationale gives the order by topic over the order of writing; WAY-21's *Rejected*
  now reads "topics in place of scope". Naming them in the request is the orchestrator's.
- *Out of scope* holds: the game's log is not touched, the log is not split into two files, no
  entry was judged for the template (AIR-518). The change touches only the files the plan names.

## Slices without a review of their own (WAY-136, WAY-164)

- Foundation entries `dae85e1`, `104e126`, `0023a28` and Fix 1 `dbdfdad`: entries against the rows
  as above; WAY-21's measured share ("about half", dated, with its method) stands within WAY-05's
  allowance for a measurement, so the foundation agent's concern 1 is no finding. I1 comes from Fix 1.
  Own-work check (search for the reading by title and the three entries' *Rejected*) fits the
  acceptance criterion and would catch it unmet.
- Slice 1 `0023a28..30c5b1b`: claims verified (no-binding-sentence decision prints nothing; I
  compared WAY-150 and WAY-18 with F1–F6 myself). Own-work check (BOM and CRLF give the same index)
  fits a requirement the handoff names and would catch it. m4.
- Slice 2 `30c5b1b..cea78e5`: claims verified (only `### PREFIX-NN — ` headings are entries; CRLF
  against LF differs, as "byte for byte" says). The two tests in `test_foundation_check.py` pin the
  check on a sectioned log; the second asserts the error at line 24, which only the inserted headings
  give. Own-work check fits and found two bugs.
- Slice 3 `cea78e5..3cec41a`: the two additions beyond the slice's text (the index as a reader in
  the template's table; "Withdrawn numbers" in a sectioned log) agree with WAY-150 and WAY-18 and
  are no finding. Its executor raised the face-value contradiction that led to Fix 1. Own-work check
  (search for the restated whole reading) fits. I1 (step 3 kept), m5.
- Slice 4 `dbdfdad..4ef3fcb`: the three files give F1, F3, F4 and F8. m3, m6.
- Slice 5 `4ef3fcb..55f1a24`: reviewed by its own review; I checked the trust boundary again (see
  Checks). m1, m2, m5 (N2).

## The structure of the code the change leaves

`python -B task-cycle/change_file_sizes.py 21ecb62 55f1a24` (exit 0): `task-cycle/cycle_measures.py`
529 → 741, `task-cycle/test_cycle_measures.py` 799 → 1280, four new files of 167–324 lines, the log
9189 → 9419. The-way has no `guidelines/coding.md` and no rule of size (WAY-328), so there is no
test of size to run on the base and the head, and a finding of structure is Minor (WAY-363). The
functions the diff reaches in `cycle_measures.py` (`ReadCounter`, `read_claude_blocks`,
`read_codex_record`, `result_text`) are each under 40 lines; `read_calls` was renamed
`read_claude_agent`, and no code is left without a user. No finding.

## Declined to judge

- The handoffs and the plan's *Read* still name every decision "Reading the foundation" selects for
  a slice, each whole (`task-cycle/plan/SKILL.md:146-151`, `task-cycle/skill/SKILL.md:238-242`),
  though the task's *Need* names authors who get too much to read: the task's rows bind the agent
  that selects ("its selection"), and the plan's *Choices* keep the handoffs as they are; outside
  the task.
- `task-cycle/test_remarks_check.py:204`, the fixture "**Unread material:** a decision, read by title
  only": input of the remarks check, which describes no reading; outside *To do* 4.
- The request's own content — the list of sections with counts and sentences, the comparison's
  output, the "before" measure on the last game cycle and the last the-way cycle, and the naming of
  the three reversals at WAY-150, WAY-18 and WAY-21 — is written after this review, outside the range.
- Sections of 4–10 entries where the task says "po kilkanaście wpisów": the plan's choice on a log
  of 198 entries (the task counted 331), where 20–30 sections of 11 or more cannot both hold; the
  request should put it before the human with the list.

## Checks

| Command (from the worktree's root) | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `55f1a24…`, as given |
| `python -B elements/common/decision_index.py --sections --output .runs/review-whole/sections.md` | 0 | 28 sections |
| `python -B elements/common/decision_index.py --output .runs/review-whole/index2.md --section "Decision entries and the decision log" --section "How skills write and read the foundation" --section "Scripts and the gate" --section "The part map and derived files" --section "The work of a cycle's agents" --section "Review of a change" --section "The request and the human" --section "Process audit" --part elements-common --part decisions --part part-map --part project-level --part task-cycle --decision WAY-02 --decision WAY-03 --decision WAY-52 --decision WAY-339 --decision WAY-287` | 0 | 57 in full, 99 by heading: 156 |
| the same without the `--decision` switches (first run) | 0 | 55 in full, 101 by heading |
| `python -B elements/common/decision_index.py --output … --decision WAY-326` | 2 | `Error: foundations/decisions.md: no decision WAY-326` |
| `python -B elements/common/decision_index.py --output … --part no-such-part` | 0 | empty index (m4) |
| `python -B elements/common/compare_log_entries.py <dae85e1 log> <104e126 log>` | 0 | 198 entries the same byte for byte |
| `python -B elements/common/compare_log_entries.py <21ecb62 log> <55f1a24 log>` | 1 | 5 reports: WAY-18, 21, 150, 287, 339 |
| a script of mine listing the lines outside entries, before and after the division | 0 | 3 lines before, 90 after: headings and sentences only |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B gate/run_tests.py elements/common` | 0 | 231 tests OK |
| `python -B gate/run_tests.py task-cycle` | 0 | 474 tests OK |
| `python -B gate/run_tests.py process-audit` | 0 | 182 tests OK |
| `python -B gate/run_tests.py project-level` | 0 | 275 tests OK |
| `python -B task-cycle/change_file_sizes.py 21ecb62 55f1a24` | 0 | table above |
| `python -B task-cycle/cycle_measures.py --output .runs/review-whole/real_measures.md` (this cycle's sessions, from `CLAUDE_CODE_SESSION_ID`) | 0 | real transcripts read; the four columns filled for every agent |
| crafted transcripts through `cycle_measures.py` (a script of mine): a user line whose `message` is a string; a `content` that is an object; a `tool_use` id that is an object; a `tool_use_id` that is `true`; a text block whose `text` is an object; a result of nested lists; an input nested 900 deep; a result of 200 000 text blocks; a `type` that is a list; a byte that is no UTF-8 | 2 / 0 | every case ended with exit 2 and an `Error:` line naming file, line and field, or with exit 0 and the block not counted; no traceback |
| searches of the tree for "by title", "title only", "skim", "whose title", "no topical sections", "in the order the entries were written", "at its end", "end of the log", "last entry", "read whole", "Reading the foundation" | — | read at each hit; see *Against the task* and I1 |
| search of the new and changed scripts, tests and rule files for absolute paths and note links (with a positive control) | — | none |

Not run: the full gate (the orchestrator's, as the handoff gives).

## Reaches beyond the dispatch

- `elements/common/foundation_check.py:240-342` (`blocks`, `fields`, `located`, `binding`), to judge
  how the two new scripts read entries and sections.
- `task-cycle/skill/SKILL.md:236-280` and `:540-580`, `task-cycle/plan/SKILL.md:143-152`,
  `process-audit/SKILL.md:50-69` and a search of `process-audit/audit_count.py` for
  `mechanism_measures`: for *To do* 4, m3 and whether the audit reads the table of agents (it reads
  only the cycle-level lines).
- The files that point to "Reading the foundation" (`project-level/lead/answering.md`,
  `project-level/skill/read_foundation.md`, `project-level/technology/start.md`,
  `project-level/plan/skill/read.md`, `project-level/task/skill/read_sources.md`,
  `project-level/task/skill/carry_foundation.md`, `elements/*/skill/read.md`,
  `elements/part-map/skill/SKILL.md`, `elements/invariants/skill/SKILL.md`), the passage at each
  hit, for a restated whole reading.
- `foundations/invariants.md:1-205` and `:271-377`: the invariants whose *Part* names a touched part
  or `every`, and `map-reference-target` and `test-method-citation`, which the altered tests cite.
- `task-cycle/test_cycle_measures.py:236-565` and `:1160-1190`, and `elements/common/test_foundation_check.py`'s
  added tests, to judge the tests.
- `the user's private rule file on writing scripts`, the user's rule before writing a script.

## Working copies

All in `.runs/review-whole/` of the task's worktree: the sections list and the two indexes, the
logs of `21ecb62`, `dae85e1`, `104e126` and `55f1a24` and a diff of `dae85e1`, `outside.py` and its
output, `crafted.py` with its transcripts and results in `crafted/`, the measures of this cycle's
sessions, and the outputs of the test runs and the foundation check. The whole directory was
removed before return (`test -e .runs/review-whole` false); nothing was kept in `reports/`, since the
figures this report needs stand in it. The tracked tree stayed clean (`git status --short` empty). No
worktree, clone or screenshot was made.

## Unread material

- Decisions of the index of my selection read whole: 24 of 156 — WAY-02, WAY-03, WAY-04, WAY-05,
  WAY-07, WAY-12, WAY-17, WAY-18, WAY-19, WAY-21, WAY-22, WAY-33, WAY-35, WAY-52, WAY-113, WAY-114,
  WAY-120, WAY-148, WAY-150, WAY-287, WAY-330, WAY-337, WAY-339, WAY-350. I ran through the 99
  headings outside the eight sections I chose and opened WAY-03, WAY-07, WAY-114, WAY-148 and WAY-09
  from them.
- WAY-09 read in part: its binding sentences, fields, examples, rationale and the start of
  *Rejected* (lines 11-74); the rest of *Rejected* was not read. It bears on the change only through
  where the new scripts stand, which its examples settle.
- No decision that bears on the change stayed unread.
- Guideline files: the-way has none, so none was read.
- The division commit `104e126` was not read line by line; I checked it by the comparison and the
  listing of lines outside entries above.
- Not read: the plan's record and the orchestrator's Q1–Q8 (the handoff excludes them), the
  handoffs of the other stages, `reports/review-5-*.md` and `reports/executor-5*.md` beyond what the
  handoff quotes.

## Searches not found or unclear

- The reading rule gives no way to put into the index a decision that a selected entry links to;
  whether such a decision is read whole or by its index line was unclear between WAY-150 and step 3
  (this is I1).
- `elements/common/way_of_working.md` step 2 says to add with `--decision` "the decisions the task's
  *Decisions in play* … names"; two of those the task names here, WAY-326 and WAY-347, are withdrawn,
  and the script ends with exit 2 for them. The rule does not say what to do with a withdrawn number
  named by a task; I left them out, as the plan does.
- `task-cycle/review/whole_change.md` asks for the run of the size test "in a worktree of the base and
  in one of the head"; with no rule of size in the-way there is none to run, as its last sentence
  allows — clear on reading, noted for the count of checks.

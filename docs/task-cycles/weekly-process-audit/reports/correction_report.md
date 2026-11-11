# Correction report — the tie of a subagent turn to its fix round

**Status:** done with concerns

## The human's two points, and how the correction makes each

1. **"Zgadzam się z propozycją" — `0.0%` only where the record plainly says there was no round.**
   The word rule (`report` and `fix` in a path, `fix`/`review` in a stage name) is gone, and with it
   the reading of *Events*. The rounds are read from one place, the record's item `Review rounds`, in
   a fixed form: `- Review rounds: none`, or nothing after the colon and one entry per round opening
   ``findings `reports/<file>.md` ``. The share is `0.0%` only where the item reads `none` (read by
   `remarks_check.reads_none`, as the remarks item is) and no subagent turn was given a findings
   file. A record that tells its rounds in prose — the archive's form, the reviewer's
   `reports/fix.md` case — now gives `unknown` ("names no findings file"), not `0.0%`
   (`Cost.test_rounds_written_in_prose_leave_the_share_unknown_not_zero`).
2. **"Jak wiemy co jest do zrobienia, to trzeba to zrobić" — the tie made in this request.**
   `task-cycle/cycle_stages.py` now writes, for each subagent turn, the files of `reports/` that the
   message starting the turn names (column *Files named*), and `process-audit/audit_count.py`
   gives the share as a real figure: the cost of the turns given a findings file of a round the
   record names, each turn once, over the cycle's cost. A cycle whose dispatches follow the new rule
   of `task-cycle/skill/SKILL.md` gets a number: the end-to-end test runs `cycle_stages.py` on
   Claude Code transcripts, commits its `stages.md` with a record in the template's form, and the
   audit gives `15.8%`, worked by hand (`Cost.test_the_stage_report_cycle_stages_writes_gives_the_share`).

## Commits

The range is `5f2c155..9cf2633`.

- `b43558a` Write the files of reports/ each subagent turn was given into the stage report
  (`task-cycle/cycle_stages.py` +137/−14, `task-cycle/test_cycle_stages.py` +199/−0)
- `9cf2633` Give the share of fix rounds from the turns given each round's findings file
  (`process-audit/audit_count.py` +187/−158, `process-audit/test_audit_count.py` +226/−95,
  `task-cycle/record_template.md` +11/−6, `task-cycle/skill/SKILL.md` +4/−1,
  `foundations/decisions.md` +26/−8)

## What changed

- `task-cycle/cycle_stages.py`: per turn, the `reports/<name>.md` names in the message that starts it
  (Claude Code: the user line that starts the turn; Codex: the first message the rollout gives the
  turn — the user's, an `event_msg` `user_message`, or an `agent_message` addressed to the agent).
  Text is data: one pattern `reports[\/]+` + a run of `[A-Za-z0-9_.-]` taken whole (no
  backtracking), then in Python: at most 120 characters, ends `.md`, no `..`, starts with a letter,
  digit or `_`; each name once; at most 20 per turn, with a warning beyond. Written as
  `reports/<name>`, joined by `, `, through `cell()`, in a new last column *Files named* of the
  section *Stages: start, waiting for tools and tokens by model*. Empty for no name and for the
  orchestrator's rows; `unknown` where the message cannot be read. The docstring says the column is
  a form of the report of its own that starts a series of the audit's measures (WAY-338).
- `process-audit/audit_count.py`: reads both forms of the section (with and without the column);
  `review_rounds` reads the item's form; `fix_rounds_share` computes the share. Unknown, with the
  reason, where: the item is missing, doubled, holds prose, holds text beside entries, names a
  findings file twice, or an entry does not open with its findings file; `stages.md` has no column
  (earlier form); a cell is not a list of files of `reports/`; a findings file the record names is
  named by fewer than two subagent turns (the fix and the review of that fix); a turn was given a
  findings file the record does not name. Round count = number of findings files named. Removed:
  `report_paths`, `record_rounds`, `stage_kind`, the *Events* constants. Also: an `orchestrator`
  stretch with `—` costs zero (said in the docstring and in the result's *Cost* paragraph); a
  subagent row with `—`, or a section where every row is `—`, leaves the cost `unknown`; a doubled
  item is `unknown`, as the pin and the remarks item are.
- `task-cycle/record_template.md`: the item `Review rounds` reads `none`, or one entry per fix round
  — a slice's round included — opening ``findings `reports/<file>.md` ``.
- `task-cycle/skill/SKILL.md` (one sentence, in the passage that gives the fix its findings file):
  the message that dispatches or resumes the fix, and the one of the review of that fix, names the
  findings file by its path in `reports/`, besides the handoff, and no other message does (WAY-336).
- `foundations/decisions.md` WAY-336, edited in place through `the-way-record-decision`: what a fix
  round is, how a turn is tied to it, when the share is `0.0%` and when unknown; *Scope* gains
  `task-cycle`; *Verification*, *Rationale* and *Rejected* follow. WAY-338 unchanged: its sentence
  that a change of the form of a stage report starts a new series stays true.

## Checks

These ran on the tree that was committed. The files did not change between the run and the commits.

| Command | Exit | Result |
|---|---|---|
| `python -B gate/run_tests.py process-audit` | 0 | 72 tests OK (243 s) |
| `python -B -m unittest discover -s task-cycle -p test_cycle_stages.py` | 0 | 41 tests OK |
| `python -B gate/run_tests.py task-cycle` (covers the record template, `test_remarks_check.TemplateTest`) | 0 | 278 tests OK |
| `python -B elements/common/foundation_check.py` | 0 | 0 errors (also with `--skip-test-citations` after the decision edit: 0 errors) |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 | 279 files, 0 listed. An earlier run gave exit 1: my test held an absolute Windows path, which I replaced with a relative one |
| `python -B process-audit/audit_count.py --locations <scratchpad>/corr/locations.json <&-` (a temporary locations file naming this worktree as `the-way`'s `repository`, with a temporary register and results directory) | 0 | 71 cycles in 1 of 1 repositories. 70 have *Cost* `unknown` (68 with an earlier-form `stages.md`, 2 with no `stages.md`). One cycle, this cycle's committed copy, is priced at `19.405272`, and its share is `unknown` because "the item `Review rounds` names no findings file" (it is written in prose) |
| `python -B task-cycle/cycle_stages.py b065500f-249b-4808-a8bf-172d19a2724a --output <scratchpad>/corr/stages_final.md` | 0 | one warning, about the correction's own turn (a tool call with no result yet, because it was running); the column is shown below |

Not run: the full suite (WAY-160).

### Tests written first

- `task-cycle/test_cycle_stages.py`: 8 new tests (`ClaudeFilesNamedTest` 5, `CodexFilesNamedTest` 3).
  `python -B -m unittest discover -s task-cycle -p test_cycle_stages.py` with `Row.named` and
  `MAX_FILES_NAMED` added as stubs and nothing else: exit 1, 7 failures, each at its assertion (the
  eighth, the orchestrator's rows naming nothing, passed on the stub's empty default). After the
  code: exit 0, 41 tests.
- `process-audit/test_audit_count.py` `Cost`: `python -B -m unittest test_audit_count.Cost` on the
  head's code: exit 1, 21 failures of 23. Most of them fail because the head refuses the new form
  of the section (cost `unknown`), so that run shows the form change, not each rule. Each guard was
  then broken one at a time and its test run (scratch `mutate.py`, file restored and compared byte
  for byte): `..` in a name, text beside entries, a findings file twice, fewer than two turns
  (`< 2` → `< 1`), a turn counted once per file instead of once, an orchestrator `—` row, a doubled
  item, a findings file the record does not name — each: exit 1, its test failed. The reviewer's
  own run on `9392230` showed the prose record giving `0.0%`; on this head it gives `unknown`.
- The end-to-end test: with the column header in `cycle_stages.py` renamed for a moment
  (`Files named` → `Files given`), it failed (exit 1); restored, `cmp` identical.

### What the new column shows for this cycle's fix rounds

`python -B task-cycle/cycle_stages.py b065500f-249b-4808-a8bf-172d19a2724a --output <scratchpad>/stages_final.md`, exit 0:

| # | Turn | Files named |
|---|---|---|
| 15 | Make slice 3 — turn 2 (the fix of slice 3) | `reports/slice3_fix_handoff.md` |
| 17 | Review slice 3 — turn 2 (the review of that fix) | `reports/review_slice3_findings.md, reports/slice3_fix_report.md, reports/review_slice3_fix_report.md` |
| 23 | Make slice 4 — turn 2 (the fix of slice 4) | `reports/slice4_fix_handoff.md` |
| 25 | Review slice 4 — turn 2 (the review of that fix) | `reports/review_slice4_findings.md, reports/slice4_fix_report.md, reports/review_slice4_fix_report.md` |

The two fix turns do not show their findings file: the messages that resumed them named it bare,
"The findings are in review_slice3_findings.md beside it", not by its path in `reports/`. The
reviews of the fixes named it by path. So with this cycle's dispatches each findings file is named
by one turn, and the audit would give `unknown` ("named by 1 subagent turn(s)"), not a share that
leaves the fix out. That is exactly what the new rule of the skill closes for later cycles. Every
other turn shows the handoff its prompt named; the price fetcher's turn names nothing (empty cell).

## Own-work check (WAY-164)

- **Requirement most likely unmet:** "the share must be a real figure in a cycle that follows the
  new form" — the writer and the reader are two scripts in two parts; a mismatch of column name,
  cell form or path form between them would leave every cycle `unknown` while each part's own tests
  pass.
- **Check:** `Cost.test_the_stage_report_cycle_stages_writes_gives_the_share` — `cycle_stages.py` run
  as a process on Claude Code transcripts whose fix and review-of-fix messages name the findings file,
  its output committed with a record in the template's form, the audit run.
- **What it showed:** `0.014250`, `1`, `15.8%` (hand-worked: 2250 of 14250), no unknown reason; with
  the column renamed in the writer, the test fails.

## Choices, with the way rejected and its cost if wrong

1. **The record's form:** entries under `Review rounds`, each opening ``findings `reports/<file>.md` ``,
   and `none` alone for no round. Rejected: findings paths anywhere on the line — the line also
   names review and fix reports, so a path alone does not say which file is the findings file. Cost
   if wrong: a record written loosely gives `unknown` (safe).
2. **A slice's round is an entry of `Review rounds` too** (the template used to keep slice rounds in
   the Slices table only). Without it, slice rounds — most of a planned cycle's fixes — would be
   left out of the share. Cost: one more line per slice round in the record.
3. **At least two turns per findings file** (the fix and the review of that fix). Not in the
   handoff's list; it is the "record and stages disagree" case for a round. Without it, this very
   cycle's form (fix turns naming the findings file only in their handoff) would give a share that
   silently leaves the fixes out. Cost if wrong: a round whose fix and review ran in one turn of one
   agent would be `unknown` — the skill never does that.
4. **`0.0%` cross-check by the word `findings`.** With `none`, a turn given a file whose name holds
   `findings` makes the share `unknown`; a turn given a findings file the record does not name does
   too. This is the only use of a word, and it can only turn a figure into `unknown`; the word is the
   one WAY-294 already uses to tell a findings file. Rejected: no cross-check — then `none` beside a
   real fix gives `0.0%` silently.
5. **The column in the per-model section** (the table the audit reads), repeated on each model row
   of a stage; the audit groups rows by `#` and counts a turn once. Rejected: the first table (one
   row per stage) — the audit would have to read and join a second table.
6. **Only the message that starts a turn is read**, not a skill's text or a coordinator message
   inside a running turn: a loaded skill can name `reports/` paths in its examples.
7. **Codex:** the reader takes the turn's first inbound message; a message with an encrypted part
   names files `unknown`. Checked on a real rollout on this machine (Codex 0.163.0, multi-agent v2):
   `spawn_agent`/`followup_task`/`send_message` carry the message encrypted, and the subagent's
   `agent_message` holds an `encrypted_content` part. So with today's Codex every subagent turn reads
   `unknown`, and a Codex cycle with a fix round gets a share `unknown` ("named by 0 subagent
   turn(s); the message of N turn(s) could not be read"); a Codex cycle with `none` gets `0.0%`.
   No warning is raised for an encrypted message, since it is read as the tool writes it.

## Questions

None that block. One for the orchestrator to decide (not a blocker): see concern 1.

## Concerns

1. **Codex cycles cannot get a non-zero share** while Codex encrypts messages between agents (above,
   choice 7). A Codex orchestrator could make it hold by naming the findings file in something the
   rollout keeps in plain text (for example, the fix agent's first command reading it), but that is
   a different tie and not built here. Recommended: leave it `unknown` and name it to the human.
2. **Should `task-cycle`'s part-map entry name `task-cycle/cycle_stages.py` as a trust boundary?**
   The reviewer called reading the prompt "a new trust boundary". The script already read
   transcripts (models, descriptions, tool names) before this change; the new reading follows the
   same rule (text is data, through `cell()`, names in a narrow form). I did not touch the part map.
   Recommended: no change; the orchestrator decides.
3. **This cycle's own record** (`.runs/task-cycles/weekly-process-audit/cycle.md`) still writes
   `Review rounds` in prose; it is the orchestrator's file, and its copy will need the new form if
   its share is to be read. The run on this worktree shows the committed copy of this cycle (the
   one cycle with a priced cost, `19.405272`) gives `unknown` for that reason.
4. `remarks_check.HEADING` (used by `remarks_count`, not by my code) has a lazy `.*?` followed by
   `[ \t]*` at the end; a line of a few spaces, `#`, then a long run of blanks and one other
   character may cost time quadratic in its length. I avoided it in `review_rounds` and did not
   measure or change the existing use. Outside this correction.

## Reaches beyond the handoff

- `foundations/decisions.md` WAY-294 (whole) and its line in `task-cycle/remarks_check.py` — to see
  how the cycle already tells a findings file (by `findings` in the name); used for choice 4.
- WAY-03 (the decision skill's example) and WAY-334, read whole for the record-decision step;
  `elements/decisions/template.md`, `elements/common/rules.md`, `elements/common/way_of_working.md`,
  `elements/decisions/skill/read.md`, `decide_entry.md`, `examples.md` — the skill's step 1.
- `foundations/part_map.md` entries `process-audit` and `task-cycle` — concern 2.
- The transcripts of this session's subagents of slices 3 and 4 (user lines only) and one Codex
  rollout pair on this machine (`~/.codex/sessions/2026/10/29`, `.../10/30`) — to see how each tool
  writes the message that starts a turn (choice 7 and the column's result above).
- `task.md` of this cycle (grep for fix round / share / series; one line read) and `cycle.md`
  (grep for `Review rounds`) — to see how this cycle's record writes its rounds.

## Unread material

- `task-cycle/skill/SKILL.md`: read the passages around the fix's findings file (lines 150–174) and
  "The end of a code review" (370–427) only, as the handoff asked; not the rest.
- `foundations/decisions.md`: the decisions of the scope `task-cycle` were not all read (WAY-336's
  *Scope* now names `task-cycle`); I read those the search for "fix round", "findings file" and
  "round of fixes" found, by the lines found, not each whole beyond WAY-294, WAY-334, WAY-336–338.
- `review_slice4_report.md` (the first review of slice 4): not read; the handoff named the fix review.

## Searches not found or unclear

- A plain-text copy of the message a Codex orchestrator sends a subagent (multi-agent v2): searched
  the orchestrator's `spawn_agent`, `send_message` and `followup_task` arguments and the subagent's
  first items; every message body is encrypted.
- Whether the "record and the stages disagree" case of the handoff meant more than a findings file
  named on one side only: unclear; I read it as that plus a round named by fewer than two turns
  (choice 3).
- Where in the record the rounds of slices are meant to stand once the share needs them: the
  template kept them in the Slices table; resolved by choice 2.

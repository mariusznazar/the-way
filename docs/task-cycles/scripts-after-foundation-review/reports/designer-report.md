# Designer report — spec of `scripts-after-foundation-review` (the route of the cache writes)

Status: done. Spec: `.runs/task-cycles/scripts-after-foundation-review/spec.md`.

## Questions sent and answers

None. Every point that could have been a question was settled by the task, the foundation or the
smallest reading; the readings that carry weight are named under *Unclear* below so that the
orchestrator can overrule them.

## The choice settled

Route: two columns, *Cache write (5 minutes)* and *Cache write (1 hour)*, appended after *Files
named* in the detailed section of `stages.md`, written by `task-cycle/cycle_stages.py`, read by
`process-audit/audit_count.py`. *Input* keeps its meaning (it holds the writes); the columns are the
parts the audit prices apart.

Ways weighed (full reasons in spec D1):

- A, through `cycle_measures.py` / `mechanism_measures.md`: lost. Its figures are per agent with no
  model and no stage row; the fix-round share needs the cost of each turn, so it would need a copy of
  the windows and ownership logic of `cycle_stages.py`; and it makes `cycle_measures.py` a second
  script that measures the cost (a change of it would have to split the cost series, which WAY-339
  forbids today).
- B, a second table or section of `stages.md`: lost. Needs a join of two tables by key, three more
  fields for WAY-344, new refusal cases, no gain over columns in a table whose rows already are the
  stage and the model.
- C, columns in the detailed table: chosen. Cost per row and model without a join; an earlier form is
  a prefix of the next, as *Files named* was added.
- D, *Input* made to exclude the writes: lost (one word, two meanings by form).
- E, a third script: lost (a new path for the series, a new reading, no gain).

What the choice costs (spec D1): the tokens written to the cache are counted by two scripts (a test
across them is asked); the reading of a Claude Code transcript by `cycle_stages.py` comes under
WAY-344 (exit 2 on a missing field, fixtures need the new field, an old transcript without
`cache_creation` ends the script, the step 12 text of `task-cycle/skill/SKILL.md` has to name
`cycle_stages.py` beside the two scripts it already names for exit 2); WAY-339 says the opposite
today.

## Foundation sentences made untrue (spec D3)

- WAY-339, second paragraph "… are never columns of the stage report", and its *violates* line "a
  change adds a column of context or cache use to the stage report", and the *Rationale* sentence on
  a column for cache use ending the comparison of the cost. Wording asked: cache-use measures stay in
  their own file and never become columns; the tokens written by lifetime are columns only as an
  input of the cost, counted by `cycle_stages.py`, the script that measures the cost; *Rejected*
  gains ways A and B.
- WAY-344: the list of earlier forms read with no `Error:` gains the form without the two columns; one
  of the pair alone is a missing field (as for one of the two time lines); *Verification* complies
  and violates and the *Rationale* sentence on the price gain the same. The rule for a reading a
  change reworks needs no change; it binds the reading of the transcript.
- WAY-337: not made untrue; unchanged.
- No other entry: searched `foundations/` for cache write, stage report, `cycle_stages`,
  `cycle_measures`, price list and "never columns". Hits are WAY-255 and WAY-368 (agents' cache
  lifetime), and the withdrawn WAY-338, WAY-351, WAY-352 whose rules stand in the scripts. The
  invariant `audit-series-script-paths` and the part map are unchanged.

## What the route requires of each script (spec D2, D4, D5)

- `cycle_stages.py`: the two counts per response, from `message.usage.cache_creation`, into the
  columns; Codex rows write `0` and `0`; a Warning where the lifetimes do not add up to
  `cache_creation_input_tokens`; the whole Claude Code transcript reading under WAY-344 with one test
  (exit 2, names the field); one test across the two scripts on the same transcript; it is the one
  script that splits the cost series.
- `audit_count.py`: three forms of the detailed header, each a prefix of the next; both write columns
  absent is the earlier form with the same cost, no `Error:`, no new `unknown`, same exit code; one of
  them alone is a missing field (cost `unknown`, result written, exit 1, `Error:` names the column); a
  row is priced input less cached less writes at the input price, the writes at their own prices,
  with `unknown` where the sum exceeds the input or a lifetime with writes has no price (`—` in a write
  column means no price for that lifetime only); the older table of tokens by model is left alone; the
  tests listed in D5.
- Price list: the column in every table (OpenAI with `—`), the audit requires both write columns in
  every table (exit 2 naming `--prices` and the column), new date, description without the "not
  priced" sentence but keeping the earlier-form approximation; prices only from the page.
- Also: `process-audit/SKILL.md` list of forms, and `task-cycle/skill/SKILL.md` step 12 exit-2 sentence.

## Where the series of the cost is split

A change of `cycle_stages.py` splits it (task row 3, as the task says); this route makes no second
script measure the cost, so a change of `cycle_measures.py` splits no cost series and the code needs
no new entry for it. This task's price list and `cycle_stages.py` change land in one version, so the
cost and the remark-count series both begin there and the approximation of the earlier form is never
compared with the new form.

## The four checks

1. Placeholders, TBD, empty section: none found.
2. Contradictions: one found and fixed (the spec said it asked for no import between the two scripts
   while *Left to the maker* allowed one; now it says it asks none and leaves one to the maker; and
   "neither reads the other" became "neither takes its figures from the other's file"). The spec does
   not contradict the task (checked the rows 3, 5, 7, 8 and the settlements 3, 4, 5) or the foundation
   entries read; where it contradicts WAY-339 as it stands, the entry is named with its new wording.
3. Scope: one change, the route and what it requires; the other items of the task stay with the
   task. The part of it that is large is the strict reading of the Claude Code transcript in
   `cycle_stages.py` (the plan may make it a slice of its own).
4. Two readings: the "reworks a reading" of WAY-344 (adding one field counts) and the missing-field
   case of one write column alone were picked and written down; the rest picked: exit code 2 of
   `cycle_stages.py` for a missing field, `0` for a Codex row, a Warning (not an error) for lifetimes
   that do not sum.

## Reaches beyond the dispatch

- `task-cycle/skill/SKILL.md` lines 556–585 (step 12): to see how the orchestrator runs
  `cycle_stages.py` and what it does on exit 2; found the sentence that names only
  `cycle_measures.py` and `gate_times.py`.
- `foundations/decisions.md` lines 5815–5845 (WAY-255) and 9349–9525 (withdrawn identifiers), by
  search hits: to see if an entry speaks of cache writes or of the table the cost is counted from.
- `process-audit/SKILL.md` lines 56–60, 145–147, 170–172, by search: it lists the forms of `stages.md`.
- `git log -S` and `git show` of commits `5619839` and `269d7be`: for the reason of the fold of the
  writes into *Input* (design.md); none is given.
- `task-cycle/test_cycle_stages.py` and `process-audit/audit_count.py` search hits, as named below.
- `task.md` whole (a frozen task; the skill asks for it).

## Unread material

- `.runs/task-cycles/scripts-after-foundation-review/plan.md` (Slice 2): not read; the handoff said it
  does not bind and the list copied in the handoff was enough.
- Foundation entries WAY-337, WAY-339, WAY-344, WAY-330, WAY-350, WAY-38, WAY-07, WAY-135: read whole.
  Invariants `audit-series-script-paths`, `script-language`, `script-imports`, `script-subprocesses`:
  read whole. `part_map.md` entries `task-cycle` and `process-audit`: read whole. `glossary.md`: read
  whole.
- `task-cycle/cycle_stages.py`: read lines 1–200 (module description and types), 222–250, 500–630
  (Claude Code reading), 674–772 (rows), 855–1004 (report and `main`); the Codex reading only the
  lines of `Usage(` at about 436–440; not read: 250–500 (Codex agent), 630–674, 772–855.
- `task-cycle/cycle_measures.py`: read lines 1–270 (description, types, `read_response`) and 560–700
  (measures, report); not read: 270–560, 700–end.
- `process-audit/audit_count.py`: read lines 1–260, 300–360, 801–1054, 1245–1335 (to `add_cost`'s
  start); not read: 260–300, 360–800, 1054–1245, 1335–end (the other readings, the series code, the
  result writer).
- `process-audit/price_list.md`: read whole.
- Tests: by name only, `task-cycle/test_cycle_stages.py`; the tests of `audit_count.py` and of
  `cycle_measures.py` were not opened.

## Searches not found or unclear

- Not found: a reason for folding the writes into *Input* in the description of commit `5619839`; the
  spec writes none and keeps the fold.
- Unclear, not checked (no check may be run at this stage): that every assistant line of a real Claude
  Code transcript holds `message.usage.cache_creation` and that its two lifetimes always add up to
  `cache_creation_input_tokens`. `cycle_measures.py` is strict about the first and runs in every
  cycle, which suggests it, but I did not read a transcript. The spec asks the maker to prove it on a
  real session and chooses a Warning for the second.
- Unclear: whether WAY-344's "a change that reworks how a script reads a file" covers adding one
  field to the reading. I read it as yes from its *violates* line ("checks the field it added and
  leaves the other fields of that file unchecked"), which is the costly reading (the whole transcript
  reading of `cycle_stages.py`). If the orchestrator reads it as no, the spec's D4 "WAY-344 for the
  transcript" and its test shrink, but a lenient new read of a missing `cache_creation` as zero then
  counts as reading an absence as an empty value, which the same entry forbids.
- Unclear: whether `process-audit/audit_count.py` is meant to require the two write columns in every
  price table (spec D2, so OpenAI's table gets `—` cells), or to allow a table without them. I chose
  the first as the only one that keeps WAY-344's "a missing column ends with an error".
- Unclear: the price of the 1-hour write and any new `—` cells come from the Anthropic page; I read
  no page.

## Working copies

None made: no worktree, clone, script or screenshot; nothing to remove. `.runs/designer/` was not
created.

## Revision (after the spec review, FAIL with F1 and F2)

The reviewed text stays in `spec-reviewed.md`. Only `spec.md` D4 and D3 (WAY-344 paragraph) changed.

### What I found in the code (`task-cycle/cycle_stages.py`, `read_claude_agent`, lines 502-582, and its helpers 224-225, 477-499, 789-811)

The orchestrator's answer is confirmed, with additions:

- `timestamp`: `if "timestamp" not in entry: continue` (line 516) skips the line before its type is
  looked at. Stays lenient. Added from the code: a `timestamp` that is present but no time reaches
  `parse_time` (`datetime.fromisoformat`) with no catch, so today it ends the script with an
  uncaught `ValueError`, not with `Error:`. The spec asks exit 2 naming the field for that case.
- `message.model`: `message.get("model")`; `<synthetic>` skipped (line 537); a missing model gives a
  record with `None`, which `add_by_model` files under `unknown`, and `find_warnings` (line 809)
  writes "response(s) name no model". Stays lenient; the warning stays.
- `message.id`: `message.get("id") or entry.get("uuid")` (line 541). Stays lenient.
- `message.stop_reason`: `if message.get("stop_reason"):` (line 555). Stays lenient.
- `message`: read as `entry.get("message") or {}` (line 535), `content` through `content_blocks` and
  `is_text` with `or {}`, so both are lenient today; the spec makes `message` and `message.content`
  of a `user` or `assistant` line with a timestamp needed, as the orchestrator's answer says and as
  `cycle_measures.py` does; a content that is neither string nor list and a block that is no object
  stay no error.
- `usage`: `message.get("usage") or {}` and `usage.get(name, 0)` for the four counts (lines
  557, 575-580), all lenient today; the spec makes `usage` with the four counts and the two
  lifetimes of `cache_creation` needed for every non-synthetic assistant line.
- Content blocks: `tool_use` with no `id` goes to the unrecognised calls (line 553-554), `name`
  falls back to the block type (547), `tool_result` with no `tool_use_id` leaves the call with no
  result and a warning (523, 262-265), `text` guarded by `isinstance` (498-499). Stay lenient.
- `type`, `isMeta`: `entry.get`; not needed.

### What changed in the spec

- D4 "WAY-344 for the transcript": "at least" list replaced by a closed list of needed fields (three
  items) and a list of fields that stay as they are, each with why; the model of the check is
  `cycle_measures.py` except where the list differs, and the list governs.
- D4 "The test": the one test as before, plus a pin of the lenient list (no model with its warning
  and `unknown`, `null` `stop_reason` on early lines, a line with no `timestamp`, `uuid` instead of
  `id`, all read as today, exit 0), so a build that makes a lenient field strict fails.
- D3 WAY-344: added the sentence that for the form without the two write columns the cost is
  given as the approximation (writes inside *Input*, priced as input), no value is made `unknown`
  by the missing columns, and the values `unknown` for that form are only those that truly need a
  field it lost; the list of earlier forms and the *complies* line carry that wording, with the older
  table of tokens by model named as the precedent.
- Everything else is as before. The *Foundation entries* section needed no change (WAY-344 is already
  rewritten in place for this route).

### Unread material (revision)

- `task-cycle/cycle_stages.py`: now also read 200-280 (helpers), 474-500, 788-812 besides the earlier
  ranges; not read: 280-474 (Codex agent reading), 630-674, 772-788.
- `reports/spec-review-report.md`: read whole. `spec-reviewed.md`: not opened (the spec was edited in
  place and I remember its earlier text).
- Real transcripts: not read. The review's finding that `stop_reason` is `null` on early lines is
  taken from the review, not verified by me.
- The unread material of the first report stands as listed above.

### Searches not found or unclear (revision)

- Unclear, not verified: that every `user` and `assistant` line with a `timestamp` in real transcripts
  holds `message` and `message.content` (the review saw none without in two files), and that every
  non-synthetic assistant line holds a full `usage`, including early lines of one response. If
  either fails in real data, the needed list would end real cycles with exit 2; the maker proves it
  on a real session before the step is done (as the first report asked).
- Unclear: whether a `message.content` of `null` occurs on a user line of real data; the spec treats it
  as a missing field, which `cycle_measures.py` does too.
- The unclear points of the first report stand.

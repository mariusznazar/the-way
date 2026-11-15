# Spec — the way: skrypty po przeglądzie fundamentu — brakujące pole, kontrole tekstów i ich testy, liczenie audytu

- Task: `.runs/task-cycles/scripts-after-foundation-review/task.md` (frozen)
- Open choice: through which file and script the audit count receives, for each stage row and each
  model, the tokens written to the prompt cache of each lifetime (5 minutes and 1 hour), so that
  *To do* 7 can price each lifetime at its own price. This spec settles that route, the foundation
  sentences it makes untrue, and what it requires of each script. It settles nothing else of the
  task.

## Intent

*To do* 7 asks that the cost of a cycle in the audit price the cache writes of 5 minutes and of
1 hour each at its own price. Today the audit cannot: `task-cycle/cycle_stages.py` adds
`cache_creation_input_tokens` into *Input*, so a write is priced as plain input. The split exists
in the Claude Code transcripts (`usage.cache_creation.ephemeral_5m_input_tokens` and
`ephemeral_1h_input_tokens`), and the task leaves open how it reaches the count. The spec chooses
the route: two new columns in the detailed section of `stages.md`, written by
`task-cycle/cycle_stages.py`, read by `process-audit/audit_count.py`.

## Goals and non-goals

Goals:

- The cost of a cycle prices each stage row, for each model, with its cache writes of each lifetime
  at the price of that lifetime, so the share of the cost in fix rounds (WAY-337) stays a per-row
  figure.
- A copy of an earlier form (no split) gives the cost it gives today, with no line `Error:`, no new
  `unknown` and no change of the exit code.
- A Codex row is a row with no writes to price, never `unknown`.
- Every foundation sentence the route makes untrue is named here with the wording the foundation
  step gives it.

Non-goals:

- The other *To do* items, and the settled choices of the task (the two exceptions of WAY-344, the
  two kinds of series, the unknown measure of a tool the cycle changes, the new column of the price
  list, the price itself, read by the cycle from the Anthropic page). The spec says how the route
  touches them, nothing more.
- Any change of `task-cycle/cycle_measures.py` and of `mechanism_measures.md`: its cache figures stay
  `unknown` for a Codex agent, and no series of the mechanism measures starts.
- A price for a model that no page prices, a price of a call by its size, a price of batch or of
  fast mode (the price list already says it does not do these).

## Constraints

- The task: *To do* 7 (each lifetime priced at its own price; the price-list column *Cache write
  (1 hour)* with the price read from the Anthropic page, a new list date, a description of the
  columns without the sentence "Cache writes (*Cache write (5 minutes)*) are not priced: …"); *To do*
  8 and the settlement of the series (the series of the cost is split only by a new price list and a
  change of the script that measures the cost, `task-cycle/cycle_stages.py`); *Questions to settle* 3
  (the break of the cost series comes with this task anyway); *Settlements to record* 5.
- WAY-337: the cost is shown as an amount at the prices of one dated list and as the share of fix
  rounds, a turn put in a round by the findings file its message names; so the cost must be known for
  each stage row.
- WAY-339 and WAY-344 as they stand now; the foundation step rewrites them in place (WAY-07) for the
  task's own rows and for this route as *Foundation entries* below says.
- WAY-344, for each reading the change reworks: the whole reading of that file, every field of it,
  no other file, and one test that gives the file without a field and asserts the failure that names
  it. Reading that a change reworks includes a reading to which the change adds one field (the
  *violates* line of WAY-344: "a change that reworks the reading of a file checks the field it added
  and leaves the other fields of that file unchecked").
- WAY-38 and the invariants `script-language`, `script-imports`, `script-subprocesses`: Python, the
  standard library, no program other than git and the interpreter. A script may import another
  tracked Python file; this spec does not ask for an import between the two scripts and leaves one to
  the maker (*Left to the maker*).
- Trust boundary (`part_map`): `task-cycle/cycle_stages.py` and `process-audit/audit_count.py` read
  untrusted files (transcripts, the copy of `stages.md`, the price list). A number that reaches a
  file or a result is made in the script from a whole number it read; the text of a transcript
  reaches the report only through `cell`, and a figure that is no non-negative whole number is no
  figure.
- The audit reads copies of `stages.md` of every earlier form from git history (WAY-344): a
  heading-less detailed section with the older table of tokens by model, the detailed section
  without the two time lines, the detailed section without *Files named*. The older table of tokens
  by model has exactly the header *Model*, *Total tokens*, *Input*, *Cached input*, *Output*, and the
  audit refuses it with another header. It is therefore left as it is.
- Code as it stands: the detailed section already holds one row for each stage and model, with
  *Input*, *Cached input*, *Output* and *Files named*; `Row.by_model` of `cycle_stages.py` already
  keeps the usage of each row by model; `read_claude_agent` reads a Claude Code transcript leniently
  (`usage.get(…, 0)`, a line with no `timestamp` skipped); `cycle_measures.py` already reads the
  split strictly, per call, per agent, with no model and no stage row.
- The reason the writes are folded into *Input*: the commit that brought the reading, `5619839`
  ("Count the time, models and tokens of each stage of a cycle run"), gives none; the spec writes
  none and keeps the fold (see D1).

## Decisions

### D1. The route: two columns of the detailed section of `stages.md`, written by `cycle_stages.py`

The detailed section (*Stages: start, waiting for tools and tokens by model*) gains, after *Files
named*, the columns *Cache write (5 minutes)* and *Cache write (1 hour)*: for each row, for each
model of it, the tokens the model's responses wrote to the cache at each lifetime, as whole numbers
in the same form as the other token cells. *Input* keeps its meaning and its figure: input tokens,
cache writes and cache reads together. The two new columns are the parts of *Input* that the audit
prices apart; *Cached input* is the part it prices at the cache-read price.

The names are the names of the price-list columns, so that one name finds one thing on both sides.
The columns come last so that the positions of every earlier column, *Files named* included, stay
where they are and each earlier form is a prefix of the next one.

Ways weighed:

- **A. Through the file of the measures, `task-cycle/cycle_measures.py` into
  `mechanism_measures.md`.** It already reads both lifetimes strictly. Rejected. Its figures are per
  agent and carry no model and no stage row; the fix-round share needs the cost of each turn, and a
  subagent that the author resumes has several turns, so the file would have to carry turns, with
  the windows and the owner of nested subagents that `cycle_stages.py` computes. That is the second
  copy of the logic of the stages, or a measures file that reads the stage report. It also makes a
  second script that measures the cost: a change of `cycle_measures.py` would have to split the
  series of the cost, which the WAY-339 sentence "a change of the script that counts those measures
  starts a new series of those measures and none of the cost" forbids today and which would make
  every change to the mechanism measures end the comparison of the cost. If wrong: the cost of a
  turn is wrong or unknown for the cycles that matter, and the series of the cost splits at the
  wrong commits.
- **B. A second table or section of `stages.md`, keyed by stage number and model.** Rejected. It
  leaves the detailed table's form alone, but the audit would have to join two tables by key, a row
  in one and not in the other becomes a new refusal, the heading, the table and its columns are three
  more fields of a reading that WAY-344 checks, and nothing is gained over columns in the table whose
  rows already are the stage and the model. If wrong: a cycle whose two tables disagree costs
  `unknown`, and the join is a place for a wrong figure.
- **C. Columns in the detailed table (chosen).** Each row carries its own writes, so cost per row and
  model needs no join, and an earlier form is the same table without the last columns, which is how
  *Files named* was added. If wrong: the columns are a form of the stage report that the foundation
  step words and the audit reads, and taking them away again costs one more form, since the copies
  already written keep them.
- **D. *Input* made to exclude the writes, or the two columns replacing a part of *Input*.**
  Rejected. The same word *Input* would mean two things in copies of two forms, and a reader that
  does not know the form prices the writes twice or not at all. If wrong: a wrong figure that looks
  right.
- **E. A third script or a file of its own for the split.** Rejected. A new script path for the series
  of the cost and a new reading for WAY-344, with no gain over C.

The price of C, which the foundation step and the maker pay: (a) the tokens written to the cache are
now counted by two scripts, `cycle_stages.py` for the cost and `cycle_measures.py` for the measures
of cache use; (b) the reading of a Claude Code transcript by `cycle_stages.py` comes under WAY-344
(D4); (c) WAY-339 says today that these tokens "are never columns of the stage report" (D3).

### D2. What the audit does with the columns

**The form of the detailed section.** The audit knows three forms of the header of the detailed
table, each a prefix of the next: the columns it needs (`#`, `Stage`, `Start`, `Waiting for tools`,
`Model`, `Input`, `Cached input`, `Output`); those and *Files named*; those, *Files named* and the
two columns of the writes, in that order. A header of another form is refused with a reason, as it
is today.

**Missing field.** The two columns of the writes are a pair. A table that has neither is the earlier
form, read as today: no `Error:`, the same cost, the same exit code, and no new `unknown`. A table
that has one and not the other has a missing field: the cost is `unknown` with the reason, the
result is written, the run ends with exit 1 and the `Error:` line names the file and the column
that is missing, as for one of the two time lines. The columns are never missing when neither
stands, as *Files named* is never.

**The cost of a row.** For a row of the form with the writes, the cost is: the input that is neither
a cache read nor a write, at the *Input* price; the cache read at the *Cached input* price; the writes
of 5 minutes at the *Cache write (5 minutes)* price; the writes of 1 hour at the *Cache write (1
hour)* price; the output at the *Output* price. A row whose cached input and writes together exceed
its input gives the cost `unknown` with a reason, as a cached input above its input does today. A row
of an earlier form is priced exactly as today.

**Prices.** The price list gains the column *Cache write (1 hour)*; the audit reads both write
columns of every table of the list as it reads the other three: a table that lacks one of them ends
the run with exit 2 and an `Error:` that names the option `--prices` and the column, never the path.
A cell of a write column is a number or `—`. A `—` in a write column means no price for that
lifetime: a model so marked is priced as long as the row holds no writes of that lifetime, and a row
that holds some has the cost `unknown`, with the reason, and not a price borrowed from another
column. A `—` in *Input*, *Cached input* or *Output* stays what it is today, a model with no price at
all. The OpenAI table gets both columns with `—`: OpenAI gives no price of a write, and a Codex row
has none to price.

**Codex rows.** A Codex rollout gives no cache write, and OpenAI charges none apart. The report
writes `0` in both columns of a Codex row, and the audit prices the row as a row with no writes: its
cost is what it is today. It is never `unknown` for this reason, so no Codex cycle loses its cost.
The cache figures of `mechanism_measures.md` stay `unknown` for Codex (they measure cache use; the
spec leaves them alone). A row that has no token usage keeps the model `—` or `unknown` and zero
counts, as today, the new cells included.

**The older table of tokens by model.** It is read as it is read today and has no writes: those
copies are priced as input, an approximation. The module description and `process-audit/price_list.md`
say that for the earlier forms, and say the new form prices each lifetime apart.

### D3. The foundation sentences the route makes untrue

The foundation step words these; the spec says what each must hold.

**WAY-339.** Second paragraph, "the tokens written to the cache and the tokens written to it again
… are counted by a script of their own into a file of their own in the cycle's record, and are never
columns of the stage report": untrue as it stands, since the stage report gains columns of tokens
written to the cache. The entry must keep the measure and separate the use:

- The measures of how a cycle's agents use context and the prompt cache stay counted by their own
  script into their own file and never become columns of the stage report; the tokens written
  again, the number of calls, the sizes of contexts and the bytes of the decision log are of this
  kind.
- The stage report holds, for each stage and model, the tokens written to the cache by lifetime,
  only because the cost is priced from them (WAY-337); they are an input of the cost, not a measure
  of cache use. They are counted by the script that measures the cost, `task-cycle/cycle_stages.py`;
  the script of the cache-use measures counts the same tokens for its own file, and neither takes
  its figures from the other's file.
- Where the entry says which script measures the cost: `task-cycle/cycle_stages.py`. The sentence
  that the series of the cost starts only with a new price list or a change of that script is the one
  the task's *To do* 5 writes; this route adds no second script to it.
- *Verification*, *violates*: "a change adds a column of context or cache use to the stage report"
  becomes a sentence that still forbids a column of a measure of context or cache use and lets stand
  the columns of tokens written to the cache by lifetime that the cost is priced from; *complies*
  gains a case: the cost series splits at the version that brings these columns, and the series of
  the mechanism measures does not.
- *Rationale*: the sentence that a column added for cache use "would end the comparison of the cost
  of cycles across the change, while a file of its own changes no form of the report" must say that
  the columns that are here have this price, taken on purpose, because the cost needs them per stage
  and model and the file of the measures cannot give that (D1 A). *Rejected* gains way A and way B of
  D1 with their reasons.

**WAY-337.** Its sentences stay true: the cost is an amount at the prices of one dated list and the
share of fix rounds, and the share still counts a turn once through the findings file its message
names. The foundation step changes nothing of it; the settlement of the task that prices each
lifetime goes to code and data (*Settlements to record* 5), not to this entry.

**WAY-344.** It lists the earlier forms of `stages.md` that the count reads with no `Error:`: "a stage
report that has no heading of its detailed section and holds a table of tokens by model, … one that
has neither of its two time lines, … one whose detailed section has no column *Files named*". The
step must add: one whose detailed section has neither of the two columns of the cache writes. The
entry's sentence goes on "and which gives the values that need that field as unknown", so for this
form it must also say what is unknown and what is not: the cost of a report without the two columns
needs no field it lacks, so it is given, as the approximation that it has always been (the cache
writes inside *Input*, priced as input), and no value is made `unknown` by the missing columns; the
values that are `unknown` for this form are only those that truly need a field it lost. (The older
table of tokens by model already has this property: its cost is given and its share of fix rounds is
`unknown`.) The list of earlier forms in the entry and its *complies* line carry this wording. It must
say what the count does with one that has only one of the two columns: a missing field, with the
`Error:` line, the way it does for one of the two time lines. *Verification*: *complies* gains the
earlier form without the write columns, read with no `Error:` and with its cost given as that
approximation, no value made `unknown` by the missing columns; *violates* gains the count that reads a report
with one of the two write columns and not the other as the earlier form, and a count that ends with an
`Error:` for a report that has neither. The sentence of the rule for a reading a change reworks needs
no change: it binds the reading of the Claude Code transcript by `cycle_stages.py` (D4) as it binds
any. The entry's *Rationale* sentence "a stage report that has lost its two time lines, its detailed
section while a table of tokens by model remains, or the column *Files named* … is read as the
earlier form" gains the two columns.

**Other entries.** The search of `foundations/` for "cache write", "stage report", `cycle_stages`,
`cycle_measures`, `price_list` and "never columns" finds no other sentence that the route makes
untrue: WAY-255 and WAY-368 speak of cache lifetime of agents, WAY-351 (withdrawn, its rule in
`cycle_measures.py`) of the tokens written again, WAY-338 and WAY-352 (withdrawn, their rules in the
scripts) of the time and of the table the cost is counted from, whose rules stand in the module
descriptions of the scripts that change (D4, D5). The invariant `audit-series-script-paths` names the
paths that start a series of the mechanism measures and of the gate times; this route adds none and
changes none. The part map keeps its entries (`cycle_stages.py` is already a trust boundary of
`task-cycle`, `audit_count.py` of `process-audit`).

### D4. What the route requires of `task-cycle/cycle_stages.py`

- **New data.** For each response of a Claude Code transcript, the tokens of each lifetime from
  `message.usage.cache_creation.ephemeral_5m_input_tokens` and `ephemeral_1h_input_tokens`, summed
  into the usage of the row and the model like the other counts, and written in the two new
  columns of the detailed section, after *Files named*, with the names of the price-list columns.
  The usage record that the script sums gains the two counts; *Input*, the line "Tokens in all", the
  whole-cycle table by model and the first table keep their figures and their columns. The text that
  describes the report (the module description and the paragraph above the section) says that *Input*
  holds the writes and what the two columns are.
- **A Codex row** writes `0` in both columns: a Codex record gives no write and none is priced. No
  warning, no `unknown`.
- **A warning, not a guess.** Where the two lifetimes of a response do not add up to its
  `cache_creation_input_tokens`, a `Warning:` line names the transcript; the figures are written as
  read, exit 0. The audit prices whatever lies in *Input* beyond cached input and the two columns
  at the *Input* price, so the difference is an approximation of no more than that remainder.
- **WAY-344 for the transcript.** The change reworks how `cycle_stages.py` reads a Claude Code
  transcript, so the whole reading of that transcript, every field the script reads of it and no
  other file, is checked: a missing field ends the script with exit code 2 and a message that names
  the transcript, the line and the field. The fields are a closed list, taken from
  `read_claude_agent` of `cycle_stages.py` as it stands (the module the maker reads; the list is not
  "at least"):

  *Needed* — the fields the reading cannot go on without, each a missing field when absent (a
  `null` is absent) and, for a count, also when it is no non-negative whole number:
  1. of every `user` or `assistant` line that has a `timestamp`: `message` and `message.content`
     (a content that is neither a string nor a list, and a block that is no object, are no error and
     are read as today, as no text and no block);
  2. of every `assistant` line whose `message.model` is not `<synthetic>`: `message.usage`, and in it
     `input_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens`, `output_tokens` and
     `cache_creation` with `ephemeral_5m_input_tokens` and `ephemeral_1h_input_tokens` (the last
     three being the field the route adds);
  3. the `timestamp` of such a line, where it is present, has to be a time: today a value that is no
     time ends the script with an uncaught error, and it ends it with exit code 2 and a message that
     names the field instead.

  *Stay as they are* — read with a fallback or a warning, no missing field, and for these the
  reading does not change:
  - a line with no `timestamp` is skipped before its type is looked at, as today (the first
    statement of the loop of the reading);
  - `type` of a line: one that is absent or is none of `user` and `assistant` is a line the reading
    does not use; `isMeta` absent means false;
  - `message.model`: absent or `null` gives a record with no model, counted under the model
    `unknown`, with the existing warning "response(s) name no model", and the audit prices that row
    `unknown`; a response whose model is `<synthetic>` is skipped before its usage is read, as today;
  - `message.id`: absent, the line's `uuid` stands for it, as today;
  - `message.stop_reason`: absent or `null` (it is `null` on early lines of one response) leaves the
    state of the turn as it was, as today;
  - of a content block: a `tool_use` with no `id` is a call of a type the reader does not recognise
    (its wait `unknown`, with the existing warning), `name` absent falls back to the block's `type`,
    a `tool_result` with no `tool_use_id` pairs with no call (the call has no readable result, with
    the existing warning), and a `text` that is no string gives no text.

  No field outside the two lists is read from the transcript. The model for the form of the check,
  including what is no error, is the module description of `task-cycle/cycle_measures.py`; where
  that model and this list differ, this list governs. The reading of a Codex rollout and of
  `agent-<id>.meta.json` is not reworked by this route and stays as it is. The exit code
  description of `cycle_stages.py` (today "0 … 1 with `Error:` otherwise") says exit 2 for a missing
  field and exit 1 for the rest.
- **The test.** One test of the reading of a Claude Code transcript: it gives the transcript without
  a needed field (the one the route adds, `message.usage.cache_creation`, is the natural choice) and
  asserts exit code 2 and that the message names the field. Because that one test cannot tell a build
  that keeps the lenient fields from one that makes them strict, a second test, or the tests that
  exist, pins the list that stays as it is: a transcript with a response that names no model (the
  warning, the model `unknown`), early lines of a response with `stop_reason` `null`, a line with no
  `timestamp`, and a response with a `uuid` and no `id` read as today, ending with exit 0. The
  existing fixtures of the Claude Code tests that lack the needed fields gain them. A test that the
  detailed table of a Claude Code stage holds the two columns with the figures of the two lifetimes
  of its responses, one that a Codex row holds `0` and `0`, and one that a Claude Code row with a
  model of two lifetimes in one row keeps the two apart.
- **One test across the two scripts.** The same Claude Code transcript given to `cycle_stages.py` and
  `cycle_measures.py` gives the same tokens written at each lifetime in the totals of both, so the
  two counts of one figure cannot part unnoticed.
- **The series of the cost.** `cycle_stages.py` is the script whose change splits the series of the
  cost (task *To do* 5). This route needs no second script for it: the series of the cost does not
  split on a change of `cycle_measures.py`, which this route does not touch.
- **Orchestrator step.** `task-cycle/skill/SKILL.md` (step 12) already says what to record where
  `cycle_measures.py` or `gate_times.py` ends with exit code 2 and an `Error:` line. `cycle_stages.py`
  now can end with exit 2, so that sentence names it too; the file is never written by hand.

### D5. What the route requires of `process-audit/audit_count.py` and of the price list

- **Form and reading** as D2. The reader of the detailed section (`section_table`, the form of its
  header) knows the three forms; the row type holds the two counts, zero for the earlier forms; the
  price reader and its table of prices hold the two write prices of a model, each a number or no
  price; the function that prices a row prices the writes of each lifetime as D2 says and is the one
  function used for all rows of the newer form; the older table is priced by what prices it today.
- **The module description** is changed where it says "Cache writes are inside *Input* … priced as
  input: an approximation": it says that this holds for the earlier forms, and what the newer form
  does. The paragraph that lists the fields of `stages.md` under WAY-344 gains the two columns as
  a pair that is never missing when both are absent. The description of the price list gains the new
  column and the rule for `—` in a write column.
- **The split of the series** is the task's *To do* 5 and 6 and is not changed by this route; the
  route puts `cycle_stages.py` (and no other script) in the list of what splits the cost series, and
  leaves the list that splits the series of the number of remarks as the task defines it. The
  version that holds this task's change starts both new series at once (a new price list and a new
  `cycle_stages.py`); the earlier cycles are in earlier series, are never compared with the new
  ones, and are priced as before, so the approximation of the earlier form never enters a comparison.
- **The tests.** One test of the reading of `stages.md` for each of the cases that the route adds
  to a reading already tested: a copy of the earlier form without the write columns gives the cost it
  gave before, no `Error:`, no new `unknown`, the same exit code; a copy with one write column and
  not the other gives the cost `unknown`, writes the result, ends with exit 1 and the `Error:` line
  that names `stages.md` and the column; a copy of the newer form prices a row that holds writes of
  both lifetimes with each at its price (a case with figures that tell the 5-minute price from the
  1-hour price), a Codex row with zero writes at the old price, a model with `—` in a write column
  and writes that make the cost `unknown`, a model with `—` and no writes that is priced, and a
  row whose cached input and writes together exceed its input as `unknown`. One test of the reading
  of the price list: a table without the column *Cache write (1 hour)* ends with exit 2 and an
  `Error:` that names the option `--prices` and the column.
- **`process-audit/price_list.md`** gains the column *Cache write (1 hour)* in each table, a new
  `List date`, and a description of the columns that tells the use of each, including that the writes
  of the newer form are priced apart and the older forms priced as input. The price of each model
  comes from the Anthropic page the list names, read by the cycle on the day of the list, as *To do* 7
  says; no price is written from memory, and a model for which the page gives none is `—`.
- **`process-audit/SKILL.md`**, where it lists the forms of `stages.md` that the count reads (the
  passage that says the share of fix rounds is `unknown` where `stages.md` has no column *Files
  named*), is brought to the same list of forms.

## Foundation entries

- **WAY-339** — decision, rewritten in place (WAY-07), by the task's *To do* 5, 8 and settlements 3
  and 4, and, for this route, as D3 says: the tokens written to the cache are columns of the stage
  report only as an input of the cost and as the cache-use measure stay in the file of the measures;
  `cycle_stages.py` is the script that measures the cost and records these columns; the *violates*
  and *complies* lines and the *Rationale* and *Rejected* follow.
- **WAY-344** — decision, rewritten in place, by the task's *To do* 1–3 and settlements 1 and 2, and,
  for this route, as D3 says: the list of the earlier forms of `stages.md` gains the form without the
  columns of the cache writes; one of the two columns alone is a missing field; *Verification* and
  *Rationale* follow.
- **WAY-337** — decision, unchanged: the route makes none of its sentences untrue.
- No new decision, invariant, glossary term, environment fact or part-map entry follows from the
  route.

## Left to the maker

- The names of the types and functions, the exact position of the new count in the usage record, and
  whether the reading of the transcript's usage reuses code of `cycle_measures.py` by import
  (permitted by `script-imports`) or stands alone.
- The full list of the fields of the Claude Code transcript that `cycle_stages.py` reads and the exact
  boundary between a missing field and a line the reading does not use, taken from the code and from
  the model in `cycle_measures.py`.
- How the price table keeps "no price for this lifetime" apart from "no price at all" in code.
- The wording of every reason and of every `Error:` line, within what D2 and D5 fix: the file, the
  column, the option `--prices` and never a path.
- The order of the slices: the foundation step first (WAY-339 and WAY-344 as above), then
  `cycle_stages.py` with its tests, then the audit and the price list, since the audit reads what the
  report writes. The price page must be read before the list is written.

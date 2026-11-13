# Plan — the way: liczby audytu — koszt ze starszych zapisów cykli, miary liczone skryptem przy zamknięciu cyklu, czas bramki według katalogu

- Task: .runs/task-cycles/audit-numbers-mechanism-measures/task.md
- Spec: none
- Base: 2292f334d5499f45b68b00c477cd76a2effd7537

## Foundation entries

The plan names the entries; the agent of the entries words them by `task-cycle/skill/foundation_step.md`
and the skill of the element. Each row of *Settlements to record* of the task is a row here by its
number.

| Entry | Kind | From | What depends on it |
|---|---|---|---|
| Row 1 — the mechanism measures are counted by a script of their own into a file of their own, never as new columns of the stage report | new decision | Settlement row 1 | Slice 1 · Slice 2 · Slice 6 |
| Row 2 — the weekly count reads the mechanism measures and the gate times of the cycles' copies and shows them with the median of each version of the process and the comparison with the previous version of the same series | new decision | Settlement row 2 | Slice 6 · Slice 7 · Slice 8 |
| Row 3 — only a change of the instrument that measures them starts a new series of the mechanism measures and of the gate times; WAY-339 changed in place, the series of the cost staying as it is | change of WAY-339 in place | Settlement row 3 | Slice 7 |
| Row 4 — the orchestrator runs the product's gate through a script of the process that records the time of the run and of each test directory into a file of the cycle's record | new decision | Settlement row 4 | Slice 3 · Slice 4 |
| Row 5 — the audit compares gate times only over runs during which no other gate run by the script was going, and shows the rest apart | new decision | Settlement row 5 | Slice 3 · Slice 7 |
| Row 6 — a file of a cycle's copy that the count reads from git history and that lacks a field gives its values unknown, the result is written and the count ends with exit code 1 and an `Error:` line naming file and field; WAY-344 changed in place | change of WAY-344 in place | Settlement row 6 | Slice 5 · Slice 6 |
| Row 7 — the tokens written again to the prompt cache are counted by the definition of the verification | new decision | Settlement row 7 | Slice 1 · Slice 2 |
| Row 8 — the cost of a cycle whose stage report has no detailed section is counted from the table of tokens by model at the same price list, and the share of the fix rounds is unknown for it | new decision | Settlement row 8 | Slice 5 |
| Part map — the entry `task-cycle`: the trust boundary gains `task-cycle/cycle_measures.py`; the part's two new scripts and their two files named where the entry's text calls for it | part-map change | the cycle's answer on the trust boundary; the new scripts | Slice 1 · Slice 2 · Slice 3 |

No invariant is written or changed: none of the eight rows is an invariant, and the change reaches no
invariant that its tests cite.

## Slices

### Slice 1 — The measures script, for Claude Code sessions

- **Goal:** the script `task-cycle/cycle_measures.py` and its tests exist, and for the sessions of Claude Code
  they write the file of the cycle's mechanism measures. The script stands on its own: it imports no
  file of the-way, `task-cycle/cycle_stages.py` included, so that the script is the one instrument of
  these measures; it uses the standard library alone.
  *Command.* `python -B task-cycle/cycle_measures.py [SESSION ...] [--output PATH] [--codex-home DIR]
  [--claude-home DIR]`: SESSION, the two homes and the default of the session running the command are
  taken as `task-cycle/cycle_stages.py` takes them (a transcript path or a session id; the homes from
  `CODEX_HOME` and `CLAUDE_CONFIG_DIR`, else `~/.codex` and `~/.claude`; without SESSION, the session
  named in `CLAUDE_CODE_SESSION_ID` or `CODEX_SESSION_ID`, with an error where both or neither is set).
  The text goes to PATH, its directory made if it is absent, or to stdout. Exit code 0 when the
  file is written; 2 with `Error: <message>` on stderr and nothing written, for every failure: a
  session that cannot be found or read, a line that is not JSON, a needed field that is missing.
  *What is read.* The transcript of each session given — an orchestrator's — and each
  `<transcript without .jsonl>/subagents/agent-<id>.jsonl` beside it. An agent is one transcript; a
  subagent that another subagent started is an agent of its own. A subagent is named
  `<description> (<agentType>)` from its `agent-<id>.meta.json`, and by its id where the file or those
  keys are missing: the name is a label and no field the script needs. A call is a model response of
  an agent: a Claude Code response is written over several lines sharing the `id` of its message, so
  each id counts once, from the line with the most `output_tokens`; a response whose model is
  `<synthetic>` is no call. The calls of an agent are in the order of their time. A call's needed
  fields are `message.usage.input_tokens`, `.cache_read_input_tokens`, `.cache_creation_input_tokens`,
  `.output_tokens` and `.cache_creation.ephemeral_5m_input_tokens` and `.ephemeral_1h_input_tokens`;
  where one is missing — never read as zero — the script ends with exit code 2 and an `Error:` line
  that names the transcript file and the field.
  *Measures.* The context of a call is its `input_tokens`, its cache read and its cache write
  together. The middle call of n calls is the one at zero-based position (n-1)//2. A cache write again
  is counted per agent over each two consecutive calls, the earlier P and the later C: what P held in
  the cache (its read and its write) and C did not read, at most what C wrote — that is
  min(max(0, P.read + P.write - C.read), C.write) — and it counts only where it is above 2000 tokens
  and where C's context is not 30% or more below P's context (C's context times 10 is not at most P's
  context times 7); a call that passes both is a call with a cache write again. Means are rounded
  half up to a whole token; a share to one decimal, half up; where nothing can be averaged the value is
  `unknown`, never zero.
  *The file* is Markdown, UTF-8, LF line ends, the same bytes for the same input. It opens with the
  heading `# Measures of the cycle run`, then the lines below, each exactly once, in this order, then
  a table under the heading `## Agents`. Values are whole numbers with no separator, a share is
  `<n.n>%`, and a value that cannot be given is `unknown`.
  - `- Calls in all: ` (all agents) · `- Calls of the orchestrator: ` · `- Calls of subagents: `
  - `- Mean context per call: ` (all calls) · `- Mean context per call of the orchestrator: `
  - `- Share of the context in calls above 200000 tokens: ` — the context of the calls with a
    context above 200000 tokens over the context of all calls, all agents
  - `- Context of the orchestrator's first call: ` · `- Context of the orchestrator's middle call: ` ·
    `- Context of the orchestrator's last call: ` — the calls of the orchestrator's sessions taken
    together in the order of their time
  - `- Cache written, 5 minutes: ` · `- Cache written, 1 hour: ` — the sums over all agents
  - `- Cache written again by the orchestrator: ` · `- Calls of the orchestrator with a cache write
    again: ` · `- Cache written again by subagents: ` · `- Calls of subagents with a cache write
    again: ` — each summed over the agents it names, the rewrite taken within one transcript
  The table `## Agents` has the columns `Agent`, `Tool`, `Calls`, `First call`, `Middle call`,
  `Last call`, `Cache written, 5 minutes`, `Cache written, 1 hour`, `Cache written again` and `Calls with
  a cache write again`: one row per agent, the contexts of its first, middle and last call, the
  orchestrator's session as `orchestrator <session id>`, the tool `Claude Code`. A cell of the agent's
  name is text from a transcript: written on one line with each bar replaced.
  *Tests* (`task-cycle/test_cycle_measures.py`, written first, on small transcripts made in the test and
  the form `task-cycle/test_cycle_stages.py` gives, with no absolute path in any text): each line of the
  file against figures worked out by hand for a small cycle; the rewrite's four edges (the threshold
  of 2000, the shrink of exactly 30%, the minimum with the write, the first call of an agent counting
  no rewrite); a response over several lines counting once; a synthetic response skipped; a nested
  subagent as an agent of its own; the share above 200000; the first, middle and last call; the
  same bytes on a second run; the script's text importing no module of the repository. For the
  reading of a transcript, one test that gives a response without one of its needed fields —
  `cache_creation` — and asserts exit code 2 with an `Error:` line naming the transcript file and the
  field, and nothing written (WAY-344).
- **Change:** `task-cycle/cycle_measures.py` · `task-cycle/test_cycle_measures.py`
- **Read:** `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:28-33` To do, item 2 · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:74-78` Questions to settle, the definition of the tokens written again · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:116-125` Settlements to record · `foundations/decisions.md:11320-11397` WAY-344 · `foundations/decisions.md:10868-10917` WAY-328 · `foundations/decisions.md:1026-1051` WAY-38 · `foundations/invariants.md:106-115` script-language · `foundations/invariants.md:116-125` script-imports · `foundations/invariants.md:126-135` script-subprocesses · `foundations/invariants.md:328-337` cross-part-imports · `foundations/invariants.md:86-95` tracked-file-private-paths · `foundations/part_map.md:93-102` task-cycle · `foundations/part_map.md:231-239` External context · Foundation entries rows 1, 7 and the part-map row · `task-cycle/cycle_stages.py` · `task-cycle/test_cycle_stages.py:1-30` · `task-cycle/test_cycle_stages.py:225-247`
- **Model:** cheaper
- **Risk:** trust boundary — `task-cycle/cycle_measures.py`, which reads session transcripts, untrusted input by the part map's External context
- **Checks:** `python -B -m unittest discover -s task-cycle -p "test_cycle_measures.py"` fails on the base before the script exists and passes after; `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` after the slice's commit; `python -B -m unittest discover -s elements/part-map -p "test_cross_part_imports.py"`; `git diff --quiet 2292f334d5499f45b68b00c477cd76a2effd7537 HEAD -- task-cycle/cycle_stages.py task-cycle/change task-cycle/plan task-cycle/review task-cycle/spec` exits 0
- **Depends on:** Foundation entries rows 1, 7 and the part-map row

### Slice 2 — The measures script, for Codex sessions

- **Goal:** `task-cycle/cycle_measures.py` also reads Codex sessions, and its tests cover them. A session
  whose first line is a `session_meta` is a Codex orchestrator's rollout; a rollout that names a
  `parent_thread_id` is not given as a session. Its subagents are found as `task-cycle/cycle_stages.py` finds
  them: rollouts under `<codex home>/sessions` whose `session_meta` names the orchestrator's id, or the id
  of a subagent already found, as `parent_thread_id`; a subagent's name is its `agent_path`, else its
  `agent_nickname`, else its id. A forked subagent's rollout repeats its parent's history, so an agent's
  calls are only the `token_usage_record` entries whose `payload.thread_id` is the agent's own id, in the order
  of their time; the usage is read from `payload.usage`. The context of a Codex call is its
  `input_tokens`, which already holds the part read from the cache. Codex's record of a session gives no write to
  the cache, so for an agent of Codex the cache written (5 minutes and 1 hour), the cache written again
  and the calls with a cache write again are `unknown`, never zero; the first, middle and last call, the calls and
  the means are given. In the lines of the file, a value summed over agents is `unknown` where any
  agent it sums has it unknown: the lines of the cache written, and the orchestrator's or the
  subagents' lines of the cache written again. The table `## Agents` gives the tool `Codex` and `unknown` in those
  cells. A Codex call's needed fields are `payload.usage.input_tokens` and the `payload.thread_id` of the
  entry, and a rollout's `session_meta` needs `payload.id`; where one is missing, exit code 2 and an
  `Error:` line naming the rollout file and the field. Sessions of both tools may be named together; a
  cycle's measures then sum over both. Tests: a Codex orchestrator with two subagents, one of them
  forked and repeating history; the `unknown` cells and lines; a mixed Claude Code and Codex cycle; and, for the
  reading of a rollout, one test that gives a token usage entry without `input_tokens` and asserts exit code 2
  with an `Error:` line naming the file and the field (WAY-344).
- **Change:** `task-cycle/cycle_measures.py` · `task-cycle/test_cycle_measures.py`
- **Read:** `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:28-33` To do, item 2 · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:116-125` Settlements to record · `foundations/decisions.md:11320-11397` WAY-344 · `foundations/decisions.md:10868-10917` WAY-328 · `foundations/decisions.md:1026-1051` WAY-38 · `foundations/invariants.md:116-125` script-imports · `foundations/invariants.md:328-337` cross-part-imports · `foundations/invariants.md:86-95` tracked-file-private-paths · `foundations/part_map.md:93-102` task-cycle · `foundations/part_map.md:231-239` External context · Foundation entries rows 1, 7 and the part-map row · `task-cycle/cycle_stages.py:274-470` the Codex reading · `task-cycle/cycle_stages.py:619-642` finding and reading a session · `task-cycle/test_cycle_stages.py:32-125` the Codex fixtures
- **Model:** cheaper
- **Risk:** trust boundary — `task-cycle/cycle_measures.py`, which reads session transcripts, untrusted input by the part map's External context
- **Checks:** `python -B -m unittest discover -s task-cycle -p "test_cycle_measures.py"` — the Codex tests fail before the slice and pass after; `python -B -m unittest discover -s elements/part-map -p "test_cross_part_imports.py"`
- **Depends on:** Slice 1

### Slice 3 — The script that runs the gate and records its times

- **Goal:** the script `task-cycle/gate_times.py` and its tests exist. The script uses the standard library alone and
  imports no file of the-way. It starts a gate, relays its output, and appends what the run took to a file.
  *Command.* `python -B task-cycle/gate_times.py --output PATH [--registry DIR] -- COMMAND [ARG ...]`:
  COMMAND is the gate the product declares, given by the orchestrator as an argument vector and run with no
  shell in the current directory, its error output joined to its output. Everything the command prints is
  passed on to stdout unchanged and as it comes; the script keeps no copy of it beyond the lines it reads for the
  times. The exit code is the command's own. The script's own failures — no command, no `--output`, an
  output that cannot be appended, a command that cannot be started — end with a first line beginning
  `Error: gate_times.py:` on stderr and exit code 2, and are all found before the command is started where
  they can be; an exit code of 2 that comes with no such line is the gate's own.
  *The times.* The total is the wall time of the run, in seconds to three decimals. The output is read as
  `gate/run_tests.py` writes it: a line `== <directory>` opens a block, and the first line `Ran <n> test(s) in
  <seconds>s` after it, before the next `== ` line, gives that directory's time, kept as printed. No
  order of the directories is assumed, and text before the first `== ` line belongs to no directory. A
  block that holds no such line gives its directory the time `unknown`, never zero. This reading takes a
  stream, not a file; the unknown time is its protection against a missing field (WAY-344).
  *Runs at the same time.* The count of the other gate runs by this script going on at the same time on the
  machine is kept in a directory, default `~/.the-way/gate_runs/` (`--registry DIR` names another, as the
  tests do). Each run makes there an empty file named with its start and a random token, written as
  `<start in milliseconds since the epoch>_running_<token>.run`, and on its end renames it to
  `<start>_<end>_<token>.run`; the registry holds names and no content. At the run's end, the others are the
  entries other than its own whose interval met the run's interval: an entry with an end counts where it
  started before this run ended and ended after this run started; one still running counts where it
  started before this run ended and no more than six hours ago. Entries that ended more than a day ago, and
  running entries more than six hours old, are deleted when a run starts; a file whose name has another form is
  left alone and counted for nothing. Where the directory cannot be made or listed, the run goes on, `Warning:`
  is written to stderr, and the count is `unknown`, never zero.
  *The file* is Markdown, UTF-8, LF line ends. Where the file is missing or empty the script writes first
  the heading `# Gate runs of the cycle`, a line saying that each row is one run by this script and times
  are seconds, and the header row of a table with the columns `Started (UTC)`, `Exit code`, `Total seconds`,
  `Other gate runs at the same time`, `Directory` and `Directory seconds`; every run then appends rows to
  that table, one row for each directory it printed, the first five cells repeated in each, or one row
  with `—` in the last two cells where it printed none. `Started (UTC)` is `YYYY-MM-DD HH:MM:SS.mmm`, so
  that rows of one run share it; `Other gate runs at the same time` is a whole number or `unknown`;
  the `Directory` cell is written on one line with each bar replaced; `Directory seconds` is the time as
  printed or `unknown`.
  *Tests* (`task-cycle/test_gate_times.py`, written first, on commands that are Python one-liners printing
  made-up gate output, never the real gate): the rows for a made-up run with the directories out of
  alphabetical order; a block with no `Ran` line giving `unknown`; text before the first block; a run
  with no block giving the one row with `—`; the exit code passed on; the output passed on unchanged;
  the heading and the table header written once over two runs; the count of others for a registry made in the test
  with entries running, ended inside the run, ended before it, stale and named in another form; an unusable
  registry giving `unknown` with the gate still run; the default registry under the home directory of the
  process, with the home set to a temporary directory in the test's environment; the script's text importing no module of
  the repository and starting no program other than the command.
- **Change:** `task-cycle/gate_times.py` · `task-cycle/test_gate_times.py`
- **Read:** `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:35-35` To do, item 4 · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:57-68` Questions to settle, the source of the times and the runs at the same time · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:87-89` Context · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:116-125` Settlements to record · `foundations/decisions.md:4651-4689` WAY-160 · `foundations/decisions.md:11320-11397` WAY-344 · `foundations/decisions.md:10868-10917` WAY-328 · `foundations/decisions.md:1026-1051` WAY-38 · `foundations/invariants.md:116-125` script-imports · `foundations/invariants.md:126-135` script-subprocesses · `foundations/invariants.md:328-337` cross-part-imports · `foundations/invariants.md:86-95` tracked-file-private-paths · `foundations/part_map.md:93-102` task-cycle · `foundations/part_map.md:124-132` gate · `foundations/part_map.md:188-194` test-runner-command · `foundations/glossary.md:67-72` gate · Foundation entries rows 4, 5 and the part-map row · `gate/run_tests.py`
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B -m unittest discover -s task-cycle -p "test_gate_times.py"` fails on the base before the script exists and passes after; `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` after the slice's commit; `python -B -m unittest discover -s elements/part-map -p "test_cross_part_imports.py"`
- **Depends on:** Foundation entries rows 4, 5 and the part-map row

### Slice 4 — The cycle's instruction and record template name the two scripts and their files

- **Goal:** the instruction of the cycle and the record template say that the cycle runs the gate through
  `task-cycle/gate_times.py` and writes the measures with `task-cycle/cycle_measures.py`, and name the two files. In
  `task-cycle/skill/SKILL.md`: every run of the product's gate — step 2's run on the commit that moved the
  pin, step 4's run of the checks on the base, step 10's run, and the reruns of steps 9 and 12 that step 10
  governs — goes through `gate_times.py`, with `--output .runs/task-cycles/<task-slug>/gate_times.md` and the
  product's declared gate command after `--`; the orchestrator records that command and the script's exit
  code, which is the gate's, as before; WAY-160 stands: the run is the orchestrator's alone and no handoff
  or plan names it. Step 4 runs before step 5 names `<task-slug>`: the instruction settles that the name is
  known to the base run (the naming moved before it, or the run's file the one step 5 names), and the file
  lies in the cycle's record directory, which the script makes if it is absent and which the instruction names by a path that
  reaches the worktree's record directory from where the gate runs, since step 4's run may stand in a separate checkout of the base. The base-state run is
  named as one of the runs. Where step 12 runs `task-cycle/cycle_stages.py`, the next command is
  `task-cycle/cycle_measures.py` with `--output .runs/task-cycles/<task-slug>/mechanism_measures.md`,
  naming the same sessions, in the same step; the places that run `cycle_stages.py` — step 9 sub-step 4's
  stop, `task-cycle/skill/blocked_finding.md` and `task-cycle/skill/reserved_return.md` — name the new
  command beside it. The sentence that the cycle writes nothing outside the task's worktree gains the one
  exception: the script's registry of running gates, a directory of empty files under the user's
  `~/.the-way/`, which holds no content of the cycle. `The record before it is committed` stays as it is:
  it copies the whole record directory, and the two files go with it; the instruction says so where it
  names `stages.md`. In `task-cycle/record_template.md`, the sentence that lists the files of the
  record's directory gains `mechanism_measures.md` and `gate_times.md`, each with the step that creates it.
  No word of `task-cycle/cycle_stages.py`, `task-cycle/change`, `task-cycle/plan`, `task-cycle/review` or
  `task-cycle/spec` changes. The description of the skill `implement-task` is unchanged, so the skill's entry points are not
  regenerated.
- **Change:** `task-cycle/skill/SKILL.md` · `task-cycle/skill/blocked_finding.md` · `task-cycle/skill/reserved_return.md` · `task-cycle/record_template.md`
- **Read:** `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:34-35` To do, items 3 and 4 · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:116-125` Settlements to record · `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md:30-100` Slice 1 — The measures script, for Claude Code sessions · `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md:132-184` Slice 3 — The script that runs the gate and records its times · `foundations/decisions.md:4651-4689` WAY-160 · `foundations/decisions.md:4198-4265` WAY-148 · `foundations/decisions.md:10023-10088` WAY-308 · `foundations/decisions.md:10089-10139` WAY-309 · `foundations/part_map.md:93-102` task-cycle · `instruction-files/kind_skill.md` · `instruction-files/changing.md` · Foundation entries rows 1, 4
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B instruction-files/check_instructions.py .` exits as it does on the base and lists no finding on the four files that it did not list there; `python -B -m unittest discover -s task-cycle -p "test_remarks_check.py"`; `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` after the slice's commit
- **Depends on:** Slice 1 · Slice 3

### Slice 5 — The count reads the cost from either form of the stage report, and ends with exit code 1 on a missing field

- **Goal:** `process-audit/audit_count.py` gives a cycle's cost from the section `Stages: start, waiting for tools and
  tokens by model` where `stages.md` has it, as before, and from the table of tokens by model where it has not;
  and a field a form needs that `stages.md` lacks gives the cost of that cycle unknown, the result written
  and exit code 1 with an `Error:` line naming the file and the field. The series of the cost stay as they
  are: `TREE_PATHS` is not edited, and no other condition of a series changes.
  *Forms.* The newer form is known by the heading of the section and read as it is read today. The older form
  is known by its table: the table whose header row's first cell is `Model`, the columns of which are `Model`,
  `Total tokens`, `Input`, `Cached input` and `Output`, found exactly once; found twice, the cost is unknown with
  a reason and no `Error:`. Its rows are priced by the price list as the rows of the newer form are: the input
  less its cached input at the *Input* price, the cached input at the *Cached input* price, the output at the
  *Output* price; a model the list gives no price for, a model `unknown`, a cached input above its input, or a
  token count that is no number leave the cost unknown with a reason. The older form's share of the
  cost in fix rounds is `unknown` with a reason that the form gives no turns; the number of fix rounds is still
  read from the record where the record gives it, as for the newer form. A cycle in the older form is never
  put beside one of the newer form: the series' rule is as it is.
  *Missing fields* (WAY-344 as the row 6 settles it; the whole reading of `stages.md` is reworked, so every
  field of the file is under the check): a field is missing where the form the file's own signs name needs
  it and the file has no such name. The newer form needs the columns `#`, `Stage`, `Start`, `Waiting for tools`,
  `Model`, `Input`, `Cached input` and `Output` in the table of its section — a heading with no table at all misses the
  table — and `Files named` is never a missing field: the section without it is the earlier form of the section, and the
  share is unknown as today. The older form needs the columns `Input`, `Cached input` and `Output` of its table, `Model`
  being its sign. A file with neither the heading nor a table with first cell `Model` misses the section and the table, and
  the `Error:` line names both. The times: a file that has neither the line `- Working time without waiting for tools:`
  nor the line `- Waiting for tools:` is an earlier form, read as today with those two values unknown and no `Error:`;
  a file that has one of them misses the other. A form that has every field but in another order, or with another
  column beside them, misses none and is refused with a reason as today. Each missing field puts a line in the result's
  *Unknown values* and one `Error: repository `<key>`: cycle `<folder>`: the file `stages.md` of the copy lacks the field
  `<field>`` on stderr after the result is written; text from the records is cut and escaped as the command does for every
  other reason; the exit code is 1, joining the cases that give it now. The module's docstring and the lines of the
  result that describe the cost are brought to this.
  *Tests* (`process-audit/test_audit_count.py`, the new ones in the class `Cost`, in `Times` or in a class whose name holds `StagesForms`): the tests that give the cost of an earlier form as unknown are changed to
  what the row 8 settles; new tests: the older form priced by hand at a test price list; its share unknown with the reason;
  its rounds read from the record; a model with no price; the newer and the older form of one version
  not put in one comparison — the series of the cost unchanged, with a test that a change of
  `task-cycle/cycle_measures.py` or `task-cycle/gate_times.py` between two versions does not split the series of the cost
  while a change of `task-cycle/cycle_stages.py` still does; and for each reading of `stages.md`
  — the newer form's table, the older form's table, the two time lines — one test that gives the file without a field and
  asserts exit code 1, the result written with the cost unknown, and the `Error:` line naming the file and the field.
- **Change:** `process-audit/audit_count.py` · `process-audit/test_audit_count.py`
- **Read:** `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:27-27` To do, item 1 · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:39-42` Acceptance criteria · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:69-73` Questions to settle, the report that fits neither form · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:84-86` Context · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:116-125` Settlements to record · `foundations/decisions.md:11125-11165` WAY-337 · `foundations/decisions.md:11193-11217` WAY-339 · `foundations/decisions.md:11320-11397` WAY-344 · `foundations/decisions.md:10990-11013` WAY-331 · `foundations/decisions.md:10868-10917` WAY-328 · `foundations/decisions.md:1026-1051` WAY-38 · `foundations/invariants.md:116-125` script-imports · `foundations/invariants.md:328-337` cross-part-imports · `foundations/invariants.md:86-95` tracked-file-private-paths · `foundations/part_map.md:114-123` process-audit · `foundations/part_map.md:231-239` External context · Foundation entries rows 6, 8 · `foundations/decisions.md:11166-11192` WAY-338 · `foundations/decisions.md:11294-11319` WAY-343 · `task-cycle/cycle_stages.py:858-954` the stage report · `process-audit/price_list.md`
- **Model:** same — a rework of the reading rules of a 2200-line file at a trust boundary, where the rules interlock
- **Risk:** trust boundary — `process-audit/audit_count.py`, which reads the copies of the cycles' records from git history, untrusted input
- **Checks:** `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k Cost -k Times -k StagesForms -k ProcessVersions` — the new tests fail on the base and pass after; `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` once at the end of the slice; `git diff 2292f334d5499f45b68b00c477cd76a2effd7537 HEAD -- process-audit/audit_count.py` shows no changed line in the assignment of `TREE_PATHS`; `git diff --quiet 2292f334d5499f45b68b00c477cd76a2effd7537 HEAD -- task-cycle/cycle_stages.py task-cycle/change task-cycle/plan task-cycle/review task-cycle/spec` exits 0; `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` after the slice's commit
- **Depends on:** Foundation entries rows 6, 8

### Slice 6 — The count reads the measures file and the gate times of each cycle and shows their values

- **Goal:** `process-audit/audit_count.py` reads, from the last copy of each cycle, the files `mechanism_measures.md` and
  `gate_times.md` as the plan's Slice 1 and Slice 3 give their form, keeps the values on the cycle, and writes two sections of
  the result, `## Mechanism measures` and `## Gate runs`, after `## Cost` and before `## Process versions`. No series, median or comparison
  is made here (Slice 7).
  *Reading.* A copy with no such file gives its values unknown with the reason that the copy holds none, an earlier form,
  and no `Error:`. A file that is there is read by its labels: in `mechanism_measures.md` each line label of the form, found
  once, and the table `## Agents` is no needed field; in `gate_times.md` the six columns of the table's header row. A
  needed field the file lacks — a label never written, a column absent — gives every value of that file unknown, the result
  written, and exit code 1 with an `Error:` line that names the file of the copy and the field, joining Slice 5's mechanism
  (the row 6 of the settlements). A label written twice, a value that is not what its label gives, or a row of the table with
  the wrong number of cells is no missing field: the value, or the run, is unknown with a reason in *Unknown values*, and the
  count goes on. `unknown` written by the script is read as unknown. Work and size are bounded as the other readings are: a
  file over the limit already used for the copy's files is not read; at most a fixed number of runs per file and of
  directories per run are read, and the rest give unknown with that reason; every text from a file reaches the result
  as the cells of the result are written, one line, bars escaped, and cut.
  *Sections.* `## Mechanism measures`: one row per cycle with the columns `Repository`, `Record` and one for each cycle-level
  line of the file, named as its label, `unknown` where it is unknown; the per-agent table stays in the file. `## Gate runs`: one
  row per run — `Repository`, `Record`, `Started (UTC)`, `Exit code`, `Total seconds`, `Other gate runs at the same time` and
  `Directories`, a cell listing each directory with its seconds. A cycle with no run has no row there. A line before each
  table says which script writes the file and that `unknown` is never zero.
  *Tests* (`process-audit/test_audit_count.py`, in classes whose names hold `Measures`): a cycle with both files read against values worked out by hand; a copy
  without them; the last copy read where a later copy differs; for each of the two readings one test that gives the file
  without a field and asserts exit code 1, the result written, that cycle's values `unknown` and the `Error:` line naming the
  file and the field; a doubled label and a malformed value giving unknown with no `Error:`; a crafted file — bars, control
  characters, very many runs and directories — breaking no cell and costing bounded work.
- **Change:** `process-audit/audit_count.py` · `process-audit/test_audit_count.py`
- **Read:** `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:36-36` To do, item 5 · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:46-51` Questions to settle, whether the count reads the new numbers · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:63-68` Questions to settle, the gate times between versions · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:116-125` Settlements to record · `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md:30-100` Slice 1 — The measures script, for Claude Code sessions · `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md:132-184` Slice 3 — The script that runs the gate and records its times · `foundations/decisions.md:11320-11397` WAY-344 · `foundations/decisions.md:10868-10917` WAY-328 · `foundations/decisions.md:1026-1051` WAY-38 · `foundations/invariants.md:86-95` tracked-file-private-paths · `foundations/part_map.md:114-123` process-audit · `foundations/part_map.md:231-239` External context · Foundation entries rows 2, 6 · `foundations/decisions.md:11166-11192` WAY-338 · `foundations/decisions.md:11294-11319` WAY-343
- **Model:** cheaper
- **Risk:** trust boundary — `process-audit/audit_count.py`, which reads the copies of the cycles' records from git history, untrusted input
- **Checks:** `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k Measures` — the new tests fail before the slice and pass after; `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` once at the end of the slice; `git diff 2292f334d5499f45b68b00c477cd76a2effd7537 HEAD -- process-audit/audit_count.py` shows no changed line in the assignment of `TREE_PATHS`; `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` after the slice's commit
- **Depends on:** Slice 5 · Slice 1 · Slice 3 · Foundation entries rows 2, 6

### Slice 7 — Series by instrument, the median of each measure per version and the comparison with the previous version

- **Goal:** `process-audit/audit_count.py` groups the versions of the process into series of the mechanism measures and series of the
  gate times, each by the change of its own instrument alone, and writes the section `## Measure versions` with the median of each
  measure of each version and whether it falls against the previous version of the same series. The series of the cost, `TREE_PATHS`
  and the section `## Process versions` stay exactly as they are.
  *Series.* The mechanism measures' series begin at a version whose `task-cycle/cycle_measures.py` differs from the previous version's;
  the gate times' series at one whose `task-cycle/gate_times.py` differs — by the same test as the reviewed files' test (`git diff
  --quiet`; exit 1 or any failure counts as changed). Neither a new price list, nor a date of the register's list of classes, nor
  a change under `task-cycle/change`, `task-cycle/plan`, `task-cycle/review`, `task-cycle/spec` or of `task-cycle/cycle_stages.py`
  splits them. The cycles in no version stand in no series, as for the cost. Each series is its own subsection.
  *Mechanism measures per version.* A long table with the columns `Version (commit)`, `Measure`, `Cycles with a value`, `Median` and
  `Falls`: a row for each cycle-level measure of the file of Slice 1 (each label's name as `Measure`). The median is of the values
  of the version's cycles that give one, by the rule the median of the cost uses; `Falls` is `yes` where the median is lower than the
  previous version's median of the same measure in the same series, `no` otherwise, and `unknown` where the version is the first of
  its series or either median is not known, each unknown with its reason in *Unknown values*.
  *Gate times per version.* The same long table with `Measure` the total time of the run and the time of each directory that any
  run of the version has, and the columns `Version (commit)`, `Measure`, `Runs with no other gate`, `Median (seconds)`, `Falls`,
  `Runs with another gate or an unknown count` and `Median of those (seconds)`. Runs are taken together over all the cycles of the
  version. The median and `Falls` take only the runs whose count of other gates is `0`; the runs with another gate, or with the
  count `unknown`, are counted and their median shown in the last two columns and are never compared, and a version in which no
  run was alone has no comparison (`unknown`, with that reason). A directory's median takes the runs that give its time.
  The section opens with lines that say how the series are made and that a number of one series is never set beside a number of
  another. A median that is a half is written with its decimal; values are kept as `Decimal`.
  *Tests* (`process-audit/test_audit_count.py`, in a class whose name holds `MeasureVersions`, on the helpers of `ProcessVersions`): a change of `task-cycle/cycle_measures.py` starts
  a mechanism series and not a gate series, and the other way round; a change of `task-cycle/review/…`, of `task-cycle/cycle_stages.py`
  or of the price list starts a series of the cost and none of the measures; a change of the two instruments does not split the
  series of the cost (the criterion that adding the scripts starts no new series of cost); medians and `Falls` worked by hand
  for three versions of one series, over an even and an odd number of cycles; the gate table with runs alone, runs with another
  gate and a count unknown, the apart columns never entering the comparison; a version with no cycle that gave a value.
- **Change:** `process-audit/audit_count.py` · `process-audit/test_audit_count.py`
- **Read:** `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:36-36` To do, item 5 · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:39-42` Acceptance criteria · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:52-56` Questions to settle, what starts a new series · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:63-68` Questions to settle, the gate times between versions · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:116-125` Settlements to record · `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md:30-100` Slice 1 — The measures script, for Claude Code sessions · `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md:132-184` Slice 3 — The script that runs the gate and records its times · `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md:266-298` Slice 6 — The count reads the measures file and the gate times of each cycle and shows their values · `foundations/decisions.md:11193-11217` WAY-339 · `foundations/decisions.md:11238-11259` WAY-341 · `foundations/decisions.md:10990-11013` WAY-331 · `foundations/decisions.md:10868-10917` WAY-328 · `foundations/invariants.md:86-95` tracked-file-private-paths · `foundations/part_map.md:114-123` process-audit · Foundation entries rows 2, 3, 5 · `foundations/decisions.md:11166-11192` WAY-338 · `foundations/decisions.md:11294-11319` WAY-343
- **Model:** same — the series, median and comparison logic of a 2200-line file at a trust boundary, which must leave the series of the cost untouched
- **Risk:** trust boundary — `process-audit/audit_count.py`, which reads the copies of the cycles' records from git history, untrusted input
- **Checks:** `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k MeasureVersions -k ProcessVersions` — the new tests fail before the slice and pass after; `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` once at the end of the slice; `git diff 2292f334d5499f45b68b00c477cd76a2effd7537 HEAD -- process-audit/audit_count.py` shows no changed line in the assignment of `TREE_PATHS`; `git diff --quiet 2292f334d5499f45b68b00c477cd76a2effd7537 HEAD -- task-cycle/cycle_stages.py task-cycle/change task-cycle/plan task-cycle/review task-cycle/spec` exits 0; `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` after the slice's commit
- **Depends on:** Slice 6 · Foundation entries rows 2, 3, 5

### Slice 8 — The audit session's instruction puts the measures before the human

- **Goal:** `process-audit/SKILL.md` leads the session through the new numbers. In *Rules of working*, the rule on series gains what the
  count does for the mechanism measures and the gate times: a new series only at a change of the script that measures them, the
  instruction of the cycle, of the reviewer and of the author starting none, and no number of one series set beside a number of
  another. Step 2's account of exit code 1 gains the `Error:` lines that name the file of a cycle's copy and the field it lacks, which
  the result's *Unknown values* also name. Step 3's list of the sections of the count gains `Mechanism measures`, `Gate runs` and
  `Measure versions`. Matter 1's sentence that a `stages.md` of an earlier form gives no cost is brought to what the count does now (the older
  form gives the cost and leaves its share of the fix rounds unknown). Matter 4 gains the measures: for each series, one at a time, the
  rows of the version tables quoted with their header row, then what follows from them and what does not, then one open question
  for the human with no recommendation; the gate times of runs with another gate are shown apart as the count shows them and
  never compared; a measure is material and never a priority, as the rules of the skill already say of the other numbers. The step that
  writes the result's note keeps working unchanged. The skill's description is unchanged, so the skill's entry points are not regenerated.
- **Change:** `process-audit/SKILL.md`
- **Read:** `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:37-37` To do, item 6 · `.runs/task-cycles/audit-numbers-mechanism-measures/task.md:46-51` Questions to settle, whether the count reads the new numbers · `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md:266-298` Slice 6 — The count reads the measures file and the gate times of each cycle and shows their values · `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md:300-335` Slice 7 — Series by instrument, the median of each measure per version and the comparison with the previous version · `foundations/decisions.md:11193-11217` WAY-339 · `foundations/decisions.md:11238-11259` WAY-341 · `foundations/part_map.md:114-123` process-audit · `instruction-files/kind_skill.md` · `instruction-files/changing.md` · Foundation entries rows 2, 3
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B instruction-files/check_instructions.py .` exits as it does on the base and lists no finding on `process-audit/SKILL.md` that it did not list there; `python -B -m unittest discover -s gate -p "test_skills_reach_the_way_sessions.py"`
- **Depends on:** Slice 7

## Coverage

| What the task requires | Slices or entries |
|---|---|
| To do 1 — cost from the table by model where the section is missing; share unknown with a reason; a missing field gives the cost unknown, the result and exit 1 with `Error:` naming file and field | Slice 5 · rows 6, 8 |
| To do 2 — a new script in `task-cycle/` writing the measures of calls, context, cache writes and rewrites, with Codex unknown, to a file of its own | Slice 1 (Claude Code) · Slice 2 (Codex) · rows 1, 7 |
| To do 3 — the instruction and the record template name the file and the step; the file goes into the record's copy with the rest | Slice 4 |
| To do 4 — the gate run through a new script that records the time of the run, of each directory and the other gate runs, for every run, the base's included; the instruction and the template name them | Slice 3 (the script) · Slice 4 (instruction and template) · rows 4, 5 |
| To do 5 — the count reads both files, shows each cycle's values, the median of each measure per version, the comparison with the previous version of the series, the gate times of runs alone apart from the others, a new series only at an instrument change, a missing field giving unknown with exit 1 | Slice 6 (reading, per-cycle sections, missing field) · Slice 7 (series, medians, comparison) · rows 2, 3, 5, 6 |
| To do 6 — the session's instruction puts the measures before the human | Slice 8 · row 2 |
| Acceptance 1 — no change to `task-cycle/cycle_stages.py`, `task-cycle/change`, `task-cycle/plan`, `task-cycle/review`, `task-cycle/spec` | no slice changes any of them; the check `git diff --quiet` on them stands in Slices 1, 5 and 7 |
| Acceptance 2 — the series of the cost unchanged; the new scripts and files start none | `TREE_PATHS` not edited (Slices 5, 6 and 7 check it); the test of Slice 5 and of Slice 7 that a change of either script leaves the series of the cost whole |
| Settlement row 1 | entry row 1 · Slice 1 · Slice 2 |
| Settlement row 2 | entry row 2 · Slices 6, 7, 8 |
| Settlement row 3 | entry row 3 (WAY-339 changed in place) · Slice 7 |
| Settlement row 4 | entry row 4 · Slices 3, 4 |
| Settlement row 5 | entry row 5 · Slices 3, 7 |
| Settlement row 6 | entry row 6 (WAY-344 changed in place) · Slices 5, 6 |
| Settlement row 7 | entry row 7 · Slices 1, 2 |
| Settlement row 8 | entry row 8 · Slice 5 |
| Part map — the trust boundary and the new scripts | the part-map entry · Slices 1, 2, 3 |

## Choices

| Choice | Way rejected | Cost if wrong |
|---|---|---|
| Names: the scripts `task-cycle/cycle_measures.py` and `task-cycle/gate_times.py`, the files `mechanism_measures.md` and `gate_times.md` in the cycle's record directory | longer names that repeat the part; a single script for both | a rename across eight slices, the instruction and the count |
| The measures script imports nothing of the-way, `task-cycle/cycle_stages.py` included, and repeats its session discovery, so that the script alone is the instrument whose change starts a series | importing the readers of `cycle_stages.py` — a change there, which starts a series of the cost, would then change the measures with no series at all, against acceptance 1 | the discovery of sessions and the reading of the two transcript forms are kept in two places; a change of a tool's transcript form has to be made in both |
| An agent is one transcript; a nested subagent is an agent of its own; the orchestrator's sessions are taken together for the cycle's counts and the first, middle and last call, and the rewrite is taken within one transcript | folding a nested subagent into the subagent the orchestrator started, as the stage report does | the numbers per subagent differ from the stage report's stages, which count nested ones in their parent |
| The middle call of n calls is the one at position (n-1)//2; means round half up to a whole token; a share has one decimal | the median position n//2; a mean with decimals | a figure off by one call or one token against the hand analyses of 12 November 2026, which the task's "before" values come from |
| The measures file is cycle-level label lines plus a per-agent table `## Agents`; Codex gives `unknown` in cells and in the sums that include it | one table only; zero for Codex | the audit reads fixed labels, so a change of a label is a change of the instrument; a Codex cycle shows `unknown` for the sums, not a partial figure |
| The gate-times file is one flat table with a row for each directory of each run, the first five cells repeated | one row per run with the directories in one cell; a second file for the directories | a longer file, the same total; a parser that groups rows by the start time |
| The gate script takes the command after `--`, returns the command's own exit code, and ends its own failures with `Error: gate_times.py:` and exit code 2 before the command starts where it can | a script that finds the gate itself; a code of 3 for its own failures | the gate's own exit code 2 (a directory that is not one, or git unable to list files) is told from the script's by the first line only |
| Runs at the same time are kept in a registry of empty files whose names carry the start and the end, at `~/.the-way/gate_runs/`, with six hours as the longest a running entry counts and a day as the longest an ended one is kept; an unusable registry gives `unknown` and the gate still runs | a lock file with the process id (a check of a process by id is not safe in the standard library on Windows); the system temporary directory (a session may set its own, hiding the others); a file in the cycle's record (invisible to other worktrees); an error where the registry is unusable (a fifteen-minute gate lost for a bookkeeping file) | a gate killed without ending counts as running up to six hours; sessions under another user or another home do not see each other; the registry is a write outside the repository, which the instruction names as its one exception |
| The count reads `stages.md` under the rule of missing fields for the fields of the cost of both forms and for the pair of time lines (neither line is the earlier form and gives unknown, one without the other is a missing field) | every absent time line as a missing field (86 of the 93 copies of the-way's own history have no such lines, so every count would end with exit 1 for good); the fields of the cost only | a stage report with one of the two time lines and not the other, which no copy in the-way's own history has, ends the count with exit 1 |
| A file of the copy that is absent is no missing field: its values are unknown with the reason that it is an earlier form, and no `Error:` | an `Error:` for an absent file | a cycle from before the scripts would end every count with exit 1 |
| A missing field makes every value of that file unknown; a malformed value, a doubled label or a row of the wrong shape makes only that value or that run unknown, with a reason and no `Error:` | an `Error:` for every malformation | a count shows more `unknown` than a stricter reading would, and exits 0 on a crafted file |
| The mechanism measures and the gate times each have their own series, each split by its own instrument only | one series for both, split by either script | a change of the gate script splits the mechanism series too, and fewer comparisons are made |
| A mechanism measure's median is of the cycles of the version; a gate measure's median is of the runs of the version, pooled over its cycles, taking only runs alone; the version tables are long, one row per version and measure | a median of per-cycle medians; wide tables with a column for each measure | the gate median is pulled by a cycle with many runs |
| The count shows the cycle-level values of the measures file and the orchestrator's first, middle and last context; the per-agent rows of the file are not set into the result | one row per agent per cycle in the result; medians of the subagents' first, middle and last calls | a reader of the audit who wants the figures of one subagent opens the file of the cycle's copy |
| The number of fix rounds of an older-form cycle is read from the record as for the newer form; only its share is unknown | the rounds unknown too | a cycle shows a number of rounds beside an unknown share |
| `task-cycle/gate_times.py` is not named a trust boundary in the part map; `task-cycle/cycle_measures.py` is | both named | the gate script's slice gets no review of its own; its reading of the output of the product's gate rests on the audit's own untrusted reading of the file it writes |

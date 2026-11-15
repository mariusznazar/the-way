FAIL bb84a50c88b6d01b4ba3d805c5fbab7b2483e20b

# Review of slice 2, task `scripts-after-foundation-review`

Range `879a14c20a4f49015bf310021f51294f78e3c1ec..bb84a50c88b6d01b4ba3d805c5fbab7b2483e20b`, one commit (`bb84a50`); `git rev-parse HEAD` in the worktree is `bb84a50c88b6d01b4ba3d805c5fbab7b2483e20b`. Files: `task-cycle/cycle_stages.py`, `task-cycle/test_cycle_stages.py`, `task-cycle/skill/SKILL.md`.

Counts: 1 blocking (Important), 3 Minor, 1 out of scope.

## What I confirmed

- The list of D4 is implemented as the slice gives it. `read_claude_agent` (`task-cycle/cycle_stages.py:574`) skips a line with no `timestamp` key first, then a line whose `type` is not `user` or `assistant`, then checks the time, `message` and `message.content` of the line; an `assistant` line whose model is not `<synthetic>` gets `message.usage` and its four counts, each a non-negative whole number (a `bool` refused). `type`, `isMeta`, `message.model`, `message.id`, `message.stop_reason` and the content blocks stay lenient. `message.usage.cache_creation` is not read (Slice 3). A `null` is a missing field (`required`, line 511).
- `MissingFieldError` gives exit 2 in `main` with `Error: <path>:<line>: no field <field>`, naming transcript, line and field; the module description holds the closed list, what stays lenient and the exit-code paragraph (2 for a missing field, 1 for the rest). The orchestrator step in `task-cycle/skill/SKILL.md` (step 12) now names `task-cycle/cycle_stages.py`.
- The Codex rollout reading and `agent-<id>.meta.json` read no new field.
- The new test `test_a_needed_field_that_is_missing_ends_the_script_with_exit_code_2_naming_it` is red on the base (a copy of the base with the head's test file: `AssertionError: 2 != 0`, the missing count read as zero) and green on the head. The pin test `test_the_fields_that_stay_lenient_read_as_they_always_did` is green on both, as it should be. The pin test holds the model-less response with the warning, `stop_reason` `null` early lines, a line with no `timestamp`, a `uuid` with no `id`, a `tool_use` with no `id` or name, a `tool_result` with no `tool_use_id` and a `text` that is no string; it asserts exit 0 and the figures, so it fails if a lenient field is made strict.
- The tests assert the exact message, not only the exit code, and the table test checks every needed field and each count against five wrong shapes. No existing test was changed or weakened (the diff of the test file only adds). WAY-03: no invariant test, and no test holding a sentence of a decision by a line `decision:`, changed.
- Real transcripts: the script run on the 60 most recent real Claude Code transcripts under `~/.claude/projects` (with their subagents): exit 0 for all 60. No `"timestamp": null` appears in any transcript on this disk (search over `~/.claude/projects/**/*.jsonl`).
- Invariants: Python, standard library only, no subprocess added (`script-language`, `script-imports`, `script-subprocesses`); WAY-38 not touched (no product command run).

## Findings

### Important (blocking)

**1. A user line whose `message.content` is a number, a boolean or an object still ends the script with a stack trace, where the slice and the spec say it is read as no text.**
`task-cycle/cycle_stages.py:546-551` (`is_text`), called at line 600 for every `user` line that passes the new checks. `is_text` takes `content = message.content`, and where it is not a string it runs `bool(content) and isinstance(content[0], dict)`: for `content: 5` or `true` that is `TypeError: 'int' object is not subscriptable`, for `content: {"a": 1}` it is `KeyError: 0`.
The spec (`spec.md`, D4 item 1) says: "a content that is neither a string nor a list, and a block that is no object, are no error and are read as today, as no text and no block", and the module description the change itself writes says the reading checks nothing more than its list. The change checks `message.content` for being present (so `content: 5` passes the new check as a present field) and then crashes on it in the very next step. The handoff names the trust boundary: "a crash with a stack trace" is the thing to look for, and the executor's report claims crafted input cannot crash the script and its own tests of crafted input (`test_a_crafted_value_neither_crashes_the_script_nor_breaks_the_report`) do not reach this value.
Evidence: a scratch run on the head, a transcript of a `user` line `{"type":"user","timestamp":"2026-10-06T09:00:00Z","message":{"content":5}}` and a good answer: exit 1, last stderr line `TypeError: 'int' object is not subscriptable`; the same with `true` (`TypeError: 'bool' ...`) and with `{"a": 1}` (`KeyError: 0`); `content: ["x", 1]` and `content: []` read with exit 0 (the lenient list case works). The crash is already in the base (the spec's "as today" is wrong for this value), but the slice's goal and the spec's sentence say the value is read as no text, and the slice reworks exactly this reading; a test with these three contents on a user line would be red on the head. Fix: make `is_text` return false for a content that is neither a string nor a list (and for a list whose first element is no object), and add the case to the tests.

### Minor

**2. A count of about 4300 digits passes the check as a whole number and then, summed over responses, ends the script with a stack trace.** `task-cycle/cycle_stages.py:517-521` (`required_count`) accepts any non-negative `int`; the sum goes into `number()`, which formats it with `f"{value:,}"`. Evidence: three responses of `output_tokens` = 9 * 10^4299 (4300 digits each, which `json.loads` accepts): exit 1 with `ValueError: Exceeds the limit (4300 digits) for integer string conversion`. A count of 10^400 alone, and of 3 * 10^4000, runs with exit 0. The executor named this as a residual. The spec sets no upper bound, and the contrivance (a transcript made for it, no real source) keeps it Minor; the cheapest remedy is to reject a count of more than a stated number of digits as "not a whole number" in `required_count`, or to name the residual as a decision.

**3. The shared line reader of the Codex reading changed.** `numbered_lines`/`read_lines` (`cycle_stages.py:251-270`) now also catch `UnicodeDecodeError`, `RecursionError`, `MemoryError` and any `ValueError`, and `read_session` refuses a first line that is no object, for the Codex rollout too (exit 1 with `Error:` instead of a trace). The slice says the reading of a Codex rollout "does not change". No field is checked and no Codex test changed, so it is no breach of WAY-344 (no new missing field is read for another file), but it is a change nobody asked for in a file the slice fences off; the executor disclosed it (choice 5). Harmless; named so the human sees it.

**4. The edited line of step 12 in `task-cycle/skill/SKILL.md` is 122 characters long** (the paragraph around it is wrapped at about 100; the line starts "with exit code 2 and an `Error:` line, record the command, ..."). Rewrapping the paragraph would keep the file's form. No rule of an invariant is broken.

### Out of scope

**5. `agent-<id>.meta.json` that is valid JSON but no object (a list) still crashes at `meta.get`** (`cycle_stages.py`, `read_claude_session`). The task says the reading of that file does not change; the executor named it. Beyond the task, so not blocking.

## Declined to judge

- A null `timestamp` ends the script with exit 2 and a skip is for the absent key only (executor choice 2): the spec reads both ways ("a null is absent" and "a line with no `timestamp` is skipped"), no real transcript on this disk holds one, and either reading is defensible; I took the executor's reading as the one the spec's sentence 3 of D4 ("where it is present, has to be a time") supports, and I did not grade it.
- A naive time taken as UTC and a time shown in UTC for a non-`Z` offset: a decision the executor named (choice 3); effect on real transcripts nil (they carry `Z`).
- Control characters and a right-to-left mark in a model name reach the report (`cell` escapes the pipe and newline, nothing else): the report is a Markdown file the orchestrator reads, nothing unescaped breaks a table; no effect on exit codes; not in this slice's list.
- The check of the other half of D4 for Slice 3 (`cache_creation` and its lifetimes): not in this slice by its goal.

## Checks run (command, exit code)

- `python -B -m unittest discover -s task-cycle -p "test_cycle_stages.py"` in the reviewed worktree: exit 0, `Ran 60 tests ... OK`.
- `python -B -m unittest discover -s task-cycle -p "test_cycle_measures.py"`: exit 0, `Ran 87 tests ... OK`.
- On the base (`879a14c`, in a detached worktree of mine) with the head's `task-cycle/test_cycle_stages.py` copied in: `python -B -m unittest discover -s task-cycle -p "test_cycle_stages.py" -k test_a_needed_field_that_is_missing`: failed (`AssertionError: 2 != 0`); `-k test_the_fields_that_stay`: `OK`.
- Scratch probes (a script of mine in `.runs/review-2/`, run with `python -B`): 15 crafted transcripts for content kinds, a huge count, a sum of huge counts, a list in `stop_reason`/`isMeta`, a pipe and newline in prompt text, a `reports/../..` name, a weird model; results in findings 1 and 2; the rest exit 0 with no trace.
- Real transcripts: the script on the 60 most recent `~/.claude/projects/*/*.jsonl`: exit 0 for all 60.
- I ran no run of the whole gate (WAY-160).

## Reaches beyond the dispatch

- `~/.claude/projects/**/*.jsonl` (real transcripts, through the script, and a search for a `null` timestamp), for the check of a line shape the fixtures may lack.
- `a rule or note file of the author's, outside the repository` and `...\rules\scripts.md`, which the session hooks asked for before a `git worktree add` and a scratch script.
- `foundations/part_map.md:109` for the trust boundary line (inside the dispatched range 101-112, nothing beyond).

## Working copies

`.runs/review-2/` held a detached worktree of `879a14c` (`.runs/review-2/base`, with the head's test file copied into it), the scratch scripts `probe.py`, `probe2.py`, `real.py` and the output `real.md`. All removed (`git worktree remove --force`, `git worktree prune`, `rm -rf .runs/review-2`); nothing remains. The reviewed worktree, its index and branch were not changed (`git status --short` is empty).

## Unread material

None of the dispatch left unread by design except: the spec outside the two ranges the handoff names (`spec.md:57-61`, `265-327` read whole) and the plan outside the slice text copied in the handoff; `task.md:134` read; `foundations/decisions.md:2741-2901` WAY-344 read whole; WAY-38 (`2545-2570`), `foundations/invariants.md:116-145` and `foundations/part_map.md:101-112` I did not read whole — I read WAY-344 whole and used the invariants and WAY-38 as the standard-library, no-subprocess and no-quiet-pass checks above; `task-cycle/cycle_measures.py:1-110` I did not read (the executor's report and the spec describe the model; the handoff's check that its tests pass was run).

## Searches not found or unclear

- `"timestamp": null` in any real transcript: not found (none on this disk).
- Unclear: whether a `null` timestamp ends the script or is skipped as no timestamp (see Declined to judge).
- Unclear: the spec's "as today" for a content that is neither a string nor a list; the base crashes on it (finding 1), so "as today" and "no error" disagree; I took "no error, as no text" as the requirement.

PASS 49be48583a8d3866723b51e18e4284e691a574dc

# Review of the fix of slice 4 — range `ced0fd9..49be485` (one commit, `49be485`)

`git rev-parse HEAD` is `49be48583a8d3866723b51e18e4284e691a574dc`, the head given; the tree was clean.
Method: `task-cycle/review/SKILL.md`, variant the fix of earlier findings (`fix.md`). Bound by
`reports/slice-4-findings.md` (one blocking finding, Important 1) and the fix report.

Files changed: `task-cycle/cycle_stages.py` (+51 −20; 1178 lines at the head), `task-cycle/test_cycle_stages.py` (+75 −0; 1673 lines at the head). Together
`git diff --stat ced0fd9 49be485`: 126 insertions, 20 deletions.

## The finding of the findings file

### Important 1 — fixed

Each place of the finding no longer reads the field as empty or crashes; each now ends with exit 2,
`Error: <rollout>:<line>: …`, no result file. Observed on the head by the tests and by my own crafted
rollouts:

- `thread_id` of every token record: `codex_tokens` (`cycle_stages.py:394-401`) reads it with the new
  `required_text` before telling own from another's thread. A record with no `thread_id` ends the run
  at its line; it is no longer skipped.
- `turn_id` of a token record of the agent's own thread: needed, and read before any line's `turn_id`
  is used as a key; the `KeyError: None` is gone. A `turn_id` that is no text or empty ends the run
  naming it. A record of another thread needs only its `thread_id` (my probes: a record of another
  thread with no `turn_id`, and one with no `usage`, read with exit 0, as the description says and
  as the forked-rollout test holds).
- `payload.id` of the first line `session_meta`: checked in `codex_meta` (`:330-341`), which both
  `read_codex_agent` and `codex_subagent_paths` call, with the line number of the first non-blank
  line; the `KeyError` is gone at both reads.
- `timestamp` of every line whose `payload` is an object: `required_time` at `:432`. Absent, `null`,
  an integer, a list, lowercase `z`, empty, an impossible date and an overflow now end with exit 2;
  before they were skipped (absent) or crashed.

The description at the head of the script says what the reading needs and what stays a fallback, and
the exit-code paragraph names the Codex fields; both match the code (checked line against line).

The fields the first review set apart as a documented fallback (`payload.model`, `payload.type`, the
call fields, `agent_path`, `agent_nickname`, `parent_thread_id`, a `payload` that is no object) stay
and are named in the description.

## Findings in the fix diff

No Critical or Important finding. Considered and cleared:

- `elif record:` (`:487`): `record` is a tuple or None, so a record of the own thread always enters,
  and the branch sits at the end of the chain where `token_usage_record` was; no other branch takes
  that kind.
- The id check in `codex_meta` now applies to every rollout under the home that starts with a
  `session_meta` and passes the date filter, not only to this session's: a stranger's rollout whose
  first line lacks `id` ends the run with exit 2 naming it. The executor named this as a choice; it
  follows WAY-344 (the file is read for its `id`) and is the same file the script already
  reads. Not a finding.
- A line with an object `payload` and no `timestamp` is no longer skipped (the Claude half skips
  it). The executor's reason stands: skipping would lose a token record's tokens, the symptom of
  cause 3. Not a finding.
- `codex_meta` takes the first entry of the `numbered_lines` generator and leaves it open; the
  file handle closes when the generator is collected. No effect.

### Minor 1 (new, in the neighbourhood, does not block) — A line of a Codex rollout that is no JSON object still ends in a stack trace

`task-cycle/cycle_stages.py:427` (`entry.get("payload")`) and `:335` (`entry.get("type")` in
`codex_meta`): a line that is a JSON list gives `AttributeError` (observed with my probe). The same
at `ced0fd9`; the executor named it and it is not a field of the file. Not covered by the findings
file, so it does not reopen the review. The description at the head still promises exit 1 for "the
rest, such as … a line that is not JSON"; a line that is JSON but no object does neither.

### Minor 2 (carried, does not block)

The Minor findings of the first review remain as they were: the docstring of `MissingFieldError`
(`:133`, "A Claude Code transcript …"), the helpers `required*` under the heading `# Claude Code`
(`:536` on; `required_text` joined them there), and no Codex test of the count `10**15 - 1`. None is
in the findings file; none blocks.

## Declined to judge

- The size of `read_codex_agent` and of the file against WAY-385, and TRY004 at `cycle_stages.py:598`
  (a line the fix did not write): as in the first review, outside the task.

## Checks run (command and exit code)

- `python -B task-cycle/test_cycle_stages.py` — exit 0 (87 tests, OK).
- The new tests on the code before the fix: in a worktree of my own, `ced0fd9`'s `cycle_stages.py`
  against the head's tests, `python -B task-cycle/test_cycle_stages.py CodexFieldsTest` — exit 1
  (`failures=6, errors=13`); log kept at `reports/review-4-fix-previous-code-run.log`. Restored: passes.
- Mutations at the head, each restored by `git checkout`: `thread_id` read with `payload.get` —
  `CodexFieldsTest` fails (`failures=6`); the id check of `codex_meta` removed — fails
  (`failures=3, errors=4`); the `timestamp` read made lenient with a default — fails
  (`failures=2, errors=8`); the `turn_id` read made lenient — fails (`failures=5, errors=1`).
- A scratch run of crafted rollouts through `cycle_stages.main` (script in my directory, removed):
  token record of another thread without `turn_id` or without `usage` — exit 0; `timestamp` null on
  an own token record — exit 2 `…:5: no field timestamp`, no output; a turn unknown to any other line
  — exit 0 (with the existing warning); a line that is a list — `AttributeError` (Minor 1).
- `python -B process-audit/test_audit_count.py Cost.test_the_stage_report_cycle_stages_writes_gives_the_share` — exit 0.
- `python -B task-cycle/test_request_check.py` — exit 0.
- `<ruff> check --config ruff.toml --no-cache --ignore-noqa task-cycle/cycle_stages.py task-cycle/test_cycle_stages.py` — exit 1, one report: TRY004 at `cycle_stages.py:598`, not a line the fix wrote.
- `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0.
- Not run: the full gate.

## Reach beyond the dispatch

- `task-cycle/cycle_stages.py` `first_line`, `numbered_lines`, `codex_subagent_paths` (`:275-300`,
  `:526-556`): to check what `codex_meta` now does for each rollout of the home and for an empty one.
- `foundations/decisions.md` WAY-344 whole, read in the first review, reused.

## Unread material

- `reports/executor-4-fix-failing-run.log`: not read; I reran the failing check myself.
- `task-cycle/cycle_stages.py` lines 600-950 and 990-1178 (the Claude Code reader and the report
  writing): not read; the fix touched only the lines the diff shows.
- `task-cycle/test_cycle_stages.py`: the diff whole; the rest as in the first review.

## Searches not found or unclear

- none

## Working copies

A worktree of `49be485` at `.runs/review-4f/wt` with a scratch script and logs beside it: removed with
`git worktree remove --force` and `git worktree prune`, then `.runs/review-4f/` removed; `.runs/`
holds only `task-cycles/`. The log of the check on the previous code stands in `reports/`. No remainder.

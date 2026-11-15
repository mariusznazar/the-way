PASS 879a14c20a4f49015bf310021f51294f78e3c1ec

# Review 1 — slice 1 and the foundation entries of the plan, task `scripts-after-foundation-review`

Range `7f5c5a56f67d9ff40554240594ca0bde59773cb3..879a14c20a4f49015bf310021f51294f78e3c1ec` (`git rev-parse HEAD` is the head). Commits: da9d816 (WAY-339, WAY-344, one wording of WAY-321), bfb774c (glossary term *Markdown file*, five uses of "Markdown" that meant `.md` alone), 879a14c (the slice). Method `task-cycle/review/SKILL.md`, variant: the review of a slice.

Blocking findings: 0. Minor: 3 (all in scope or marked below). Out-of-scope findings: 1.

## Findings

### Critical

none

### Important

none

### Minor

1. **Out of scope, pre-existing: a crafted rollout beside the orchestrator's gives a stack trace.** `task-cycle/cycle_stages.py:455-456` (`codex_subagent_paths`) and `:277` (`codex_meta`). Where the orchestrator has no turn the search now has no lower bound, so every `rollout-*.jsonl` under `home/sessions` is read by `codex_meta`. I ran `cycle_stages.py <idle rollout> --codex-home <home>` at the head with one extra rollout in the home:
   - `session_meta` with `parent_thread_id` and no `id` -> exit 1, `KeyError: 'id'` (line 456);
   - first line a JSON array (`[1,2]`) -> exit 1, `AttributeError: 'list' object has no attribute 'get'` (line 277);
   - `session_meta` whose payload is an array -> exit 1, `AttributeError` (line 455);
   - an empty rollout and a non-JSON first line -> exit 1 with a clean `Error:` line (correct).
   The same four inputs crash the base too, and also with a lower bound whenever the stray file is newer than the floor, so the slice did not introduce them and the task's *To do* 4 (the epoch call) does not reach them; the cost of the slice is only that the unbounded search reads more files. No write outside the places the script writes, no command run, no input text reaching the table. Slice 2 reworks the reading of a transcript and is where the checks of a rollout's first line belong (WAY-344: the invariant of reading fields). Not blocking: the task asks for no tolerance of malformed rollouts.
2. **Minor, polish: lines over 100 characters in the foundation entries.** Added lines of `foundations/decisions.md` (WAY-321 line 1893, WAY-339 *Rationale* and *Rejected*, one line of WAY-344 *Rejected*), `foundations/invariants.md` (`test-method-citation`, `guidelines-file-place` are single-line entries, so these two are expected) and `elements/decisions/template.md:233` are 101-113 characters where the files wrap at 100. The foundation check passes (`0 errors`); no reader reads it wrongly. Only the lines in the decisions file that the commits re-wrapped partially are worth fixing at the next edit of those entries.
3. **Minor, coverage: the *Verification* of WAY-339 gives the unknown of a changed measuring tool only for the script that records the gate times.** `foundations/decisions.md`, WAY-339 *complies* and *violates*: the sentence of the rule names four tools (the cost script, the script of the measures of context and cache use, the script that records the gate times, the test runner), the example lines name one. A reader of the entry still finds the rule whole in the binding paragraph, so no sentence is read wrongly; a line for the cost script would match task row 4 (`cycle_stages.py`, `cycle_measures.py`, `gate_times.py`, `gate/run_tests.py`) as written. The tests of the audit are for the later slices.

## The slice against its goal and the task (*To do* 4)

- `task-cycle/cycle_stages.py:468-474`: `since = min((start ...), default=None)`; `codex_subagent_paths(home, root, since: datetime | None)` computes `floor = None if since is None else since.timestamp() - 1` and skips the `stat` comparison where `floor is None`. This is the form of `codex_subagents` in `task-cycle/cycle_measures.py:506-541` (checked line by line). A search with a turn keeps its floor unchanged. No other `fromtimestamp` is left in the module (grep). Nothing else of the reading changed (diff: 8 added, 5 removed lines in the module).
- The test `CodexTest.test_an_orchestrator_with_no_turn_finds_its_subagents_where_the_epoch_is_refused` (`task-cycle/test_cycle_stages.py:226-250`): an orchestrator rollout with `session_meta` only, a subagent rollout with one turn, and `cycle_stages.datetime` replaced by a subclass whose `fromtimestamp(0)` raises `OSError(22, "Invalid argument")`. The failure of the base does not depend on the time zone of the machine, as the goal asks; the report of the executor says how, and I saw it. It asserts the key of the subagent found and its turn, so it passes for the behaviour and not for the code's own value. A fix that left a floor of `None` unguarded would fail it with `AttributeError`.
- Foundation: `script-language`, `script-imports`, `script-subprocesses` (WAY-38) — the change imports only `datetime` and `unittest.mock` and runs no program; part map `task-cycle` trust boundary: `cycle_stages.py` — crafted input checked as finding 1. No reserved choice taken. No invariant test or `decision:` line changed in the slice.

## The foundation entries against the task (rows 1-4 and 8) and spec D3

- Row 1 (a table of weights or of the costs of an occurrence without a level): WAY-344 third binding sentence says result written, dependent values unknown, exit code 1, `Error:` naming the level; *complies* and *violates* lines carry it; *Rationale* gives why; *Rejected* holds 1.1 a. Met.
- Row 2 (`repository` entry): WAY-344 says it is no missing field and the count takes the checkout where its script lies, for that entry alone; *Rejected* holds 1.3 a and c. Met. (The row asks the entry to word the exception; the task's *To do* 2, the generator of copies at exit code 2, is code and gets no exception: *Rejected* holds 1.2 b. Met.)
- Row 3 (two kinds of series): WAY-339 first paragraph, with the price named in *Rationale* ("the audit cannot tell 'the reviewer found more' from 'the process got dearer'") and *Rejected* a and b with the 14/34/134 numbers. Met; the comparison sentence ("each measure only within a series of its own kind") is in the binding text. WAY-07 is respected (edited in place).
- Row 4 (a cycle that changes a measuring tool): WAY-339 lists the four tools of *To do* 8 by role and gives their measures as unknown with the reason; *Rejected* holds 4 a. Met (finding 3).
- Row 8 (the term *Markdown file*): `foundations/glossary.md:199-203`, "a file whose name ends in `.md`, `.markdown`, `.mdx` or `.mdc`, in any letter case", *Not: none*. The sentences of WAY-320 and of the invariant `tracked-file-private-paths` are unchanged, as the settlement says. The five corrected uses each say what the code behind them does: `foundation_check.py:762,770,958` test `.md` alone, `instruction-files/check_instructions.py:53` has `POINTED_SUFFIXES = (".md", ".mdc")`. No stray use of "Markdown" meaning `.md` alone was found in `foundations/` or `elements/*/template.md` beyond what the foundation report names as left on purpose (the later slices' code).
- Spec D3 for WAY-339: the measures of context and cache use stay in their own file; the exception for the tokens written to the cache by lifetime is named as an input of the cost, counted by `cycle_stages.py` and by the other script for its own file, neither taking from the other's file; *violates*/*complies* gain the lines the spec asks; *Rationale* names the price of the columns; *Rejected* gains A and B of D1 with their reasons; the script of the cost is named `task-cycle/cycle_stages.py`. Met. WAY-337 is untouched, as D3 says.
- Spec D3 for WAY-344: the form with neither cache-write column is read as an earlier form with the cost given as the approximation and no value unknown for the missing columns; one column of two is a missing field with `Error:`; *complies* and *violates* lines and the *Rationale* sentence carry it. The list of earlier forms stands in a sentence beside the first, not inside it (the foundation report names this as a choice to keep the sibling task's merge apart); no reader reads it wrongly.
- Invariant `audit-series-script-paths`: not changed, as D3 says the route changes none. WAY-339 now has the cost series start at a change of `task-cycle/cycle_stages.py`; that path is not under the invariant (it names the measures of context and cache use and the gate times only). The spec settled this; recorded here only as a fact for the whole-change review.
- Entries written ahead of the code: `audit_count.py` and `price_list.md` do not yet do what WAY-339/344 say; this is the plan's order (later slices), not a departure of the range.

## WAY-03: invariants whose sentence changed

The foundation check lists, at the head, two invariants whose sentence the range rewords while no file citing it changed:
- `test-method-citation` (`foundations/invariants.md`; test `elements/common/test_foundation_check.py`, citing line near 1545) — "other than a Markdown file" is now "whose name does not end in `.md`", the same rule;
- `guidelines-file-place` (test `elements/common/test_guidelines_place.py`) — "a Markdown file directly in `guidelines/`" is now "a file whose name ends in `.md` directly in `guidelines/`", the same rule.
No invariant test and no line `decision:` was changed in the range; no test cites a sentence of WAY-339, WAY-344 or WAY-321 by a line `decision:` (git grep). The request must name the two invariants.

## Declined to judge

- The invariant `audit-series-script-paths` not covering `cycle_stages.py` as a path that starts a series of the cost — the spec's D3 settled it; a matter for the whole-change review.
- Malformed first lines of rollouts (finding 1) — beyond the task's *To do* 4; Slice 2 reworks that reading.
- Whether the code of `audit_count.py`, `price_list.md`, `agent_type_copies.py` and the other scripts does what the entries now say — later slices.

## Checks run

- `python -B -m unittest discover -s task-cycle -p "test_cycle_stages.py"` in a worktree of the base `7f5c5a5` with the head's test file copied in: exit 1, 50 tests, 1 error, the new test, `OSError: [Errno 22] Invalid argument` at `cycle_stages.py:468` (the epoch call) — red for the right reason.
- The same command in a worktree of the head `879a14c`: exit 0, 50 tests, OK.
- `python -B elements/common/foundation_check.py .` in a worktree of the head: exit 0, `0 errors`, the two `listed:` lines above; on the base: exit 0, `0 errors`.
- Crafted input, five hand-made rollouts beside an idle orchestrator rollout, run through `cycle_stages.py` of the head (`--codex-home` a directory of mine under `.runs/review-1/`): results in finding 1, all exit 1; none wrote a file other than reading.
- Read of the diff of the range: `git diff 7f5c5a5..879a14c` and `git log` (3 commits, 7 files); `git grep` for tests that cite `decision:` WAY-339/344/321 (none) and for remaining uses of "Markdown" in the foundation.
- Not run: the whole gate (WAY-160).

## Reach beyond the dispatch (section 1)

- `.runs/task-cycles/scripts-after-foundation-review/spec.md:87-136` (D1, to check the *Rejected* ways A and B that D3 names) — the dispatch gave D3 only.
- `task-cycle/cycle_measures.py:506-541` (named by the slice) and `elements/common/foundation_check.py:762,770,958`, `instruction-files/check_instructions.py:53` — to check that each correction of a use of "Markdown" says what the code does.
- `foundations/invariants.md:398-407` (`audit-series-script-paths`) — to check whether WAY-339's rewrite reaches it.

## Working copies

Two detached worktrees (`.runs/review-1/base`, `.runs/review-1/head`) and a scratch directory with the hand-made rollouts and a script (`.runs/review-1/craft`, `craft_run.py`, `decisions.diff`, the two foundation-check outputs) stood under `.runs/review-1/` of the task's worktree. Removed with `git worktree remove --force` and `git worktree prune`, and the directory deleted; no remainder. The reviewed worktree, its index and branch were not changed (`git status` clean, HEAD `879a14c`).

## Unread material

none — the handoff, `task-cycle/review/SKILL.md`, the whole task, the spec lines 87-136 and 175-255 (D1 and D3), the foundation entries WAY-38, `script-language`, `script-imports`, `script-subprocesses` and the part-map entry `task-cycle` were read whole; the entries WAY-339 and WAY-344 were read as the diff of the range (every changed hunk, with its context) and not whole as new text beyond it; the plan was not read (the dispatch copies the slice).

## Searches not found or unclear

- `.runs/task-cycles/scripts-after-foundation-review/plan.md` was named "only what is copied below" and was not opened; nothing from it was missing for the review.
- The handoff names "rows 1-4 and 8 of the task"; the task's *To do* list has numbered items and its *Settlements to record* table has numbered rows. I read them as the rows of *Settlements to record* (1-4 and 8, matching the foundation report's `row N` labels). Unclear in the handoff, not in the task.

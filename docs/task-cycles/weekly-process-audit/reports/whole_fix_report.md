# Report — fix of the findings of the review of the whole change (`make-change`, "the fix of a review's findings")

**Status:** done with concerns

Range: `a5ebc88..51cae12`, branch `task/weekly-process-audit`, worktree `.runs/worktrees/weekly-process-audit`.

## Commits

| Commit | Concern |
|---|---|
| `4c77187` | B4 — `task-cycle/cycle_stages.py` recorded as the trust boundary of `task-cycle` |
| `851f761` | B1, B2, S4-7 (stage report side), Corr-M3 — `task-cycle/cycle_stages.py` and its tests |
| `5e69608` | B3, B5 (skill), m3 (skill) — `process-audit/SKILL.md`, `process-audit/problem_register.md` |
| `8f2c89a` | m5 — wrap of WAY-09's paragraph and of `task-cycle/skill/SKILL.md:167-168` |
| `766a66a` | a test text of `851f761` rewritten without a drive path (the tracked private paths check listed it) |
| `51cae12` | B5 (result), m1, m2, m3 (result), S3-M1 to S6-M4, Corr-M1, Corr-M2, Corr-M4, S4-7 (audit side) — `process-audit/audit_count.py` and its tests |

## Files changed (added / removed lines, `a5ebc88..51cae12`)

| File | + | − |
|---|---|---|
| `foundations/decisions.md` | 25 | 25 (reflow of WAY-09's first paragraph only; `git diff --word-diff` shows no word changed) |
| `foundations/part_map.md` | 1 | 1 |
| `process-audit/SKILL.md` | 32 | 11 |
| `process-audit/audit_count.py` | 236 | 124 |
| `process-audit/problem_register.md` | 6 | 3 |
| `process-audit/test_audit_count.py` | 368 | 14 |
| `task-cycle/cycle_stages.py` | 93 | 27 |
| `task-cycle/skill/SKILL.md` | 2 | 2 |
| `task-cycle/test_cycle_stages.py` | 129 | 0 |

## Findings, one by one

| Finding | Outcome | How, and the check that shows it |
|---|---|---|
| B1 | fixed, `851f761` | Rule in the reader, said in the docstring: a call with no result that no later entry of its transcript follows — no result of any call, no message to the agent, no other response of its model (Claude Code: another message id), in Codex no non-call response item and no `task_started`/`user_message`/`task_complete` — is cut off by the end of the transcript: it is no wait and makes nothing `unknown` (its time lies after the agent's last entry). A call with no result followed by any of those stays `unknown`. This covers the call that runs the script on its own live session in the orchestrator's transcript *and* in a subagent's (the orchestrator's own call is often an `Agent` call, already no wait; the open `Bash` call sits in the subagent that runs the script). No sentence of step 12 was needed. Tests: `ClaudeWaitTest.test_a_call_the_transcript_ends_in_is_no_wait_and_no_unknown`, `..._parallel_calls_of_the_last_response_...`, `..._before_a_later_entry_stays_unknown` (later result, later message, later response), `CodexWaitTest.test_a_call_the_rollout_ends_in_...`, `..._before_a_later_item_stays_unknown` (later output, later message, end of turn). On this session (below): the warning for the call running the script is gone (3 → 2 calls with no readable result); the two left are calls cut by the computer's crash in slices 5 and 6, followed by the coordinator's resume message, so the totals stay `unknown` for that other, real reason. |
| B2 | fixed, `851f761` | `files_named` drops the full stops that end the name (`rstrip(".")`) before its checks. Test `ClaudeFilesNamedTest.test_a_name_ending_its_sentence_is_read_without_the_mark_that_ends_it`: full stop, comma, closing backtick, bracket `)`, `]`, double and single quote, `...`, colon; and `reports/.md.`, `reports/x.md.bak.`, `reports/notes.` stay out. |
| B3 | fixed, `5e69608` | Skill: the opening says the session changes nothing in any repository and in the register only the list of classes, on the human's yes; matter 1 says how a row refused for its class shows (`row <n>` of *Problems*, reason `the class is not in the list of classes`) and sends it to the new paragraph **A class the list lacks** (`process-audit/SKILL.md:149-159`): the session reads the row in the register, puts a new class before the human (name, meaning, the day of the session), and on the yes adds `\| <name> \| <meaning> \| <YYYY-MM-DD> \| none \|` to *Classes* in the register the entry `problem_register` names — never in a repository — changing nothing else; adding a class gives no problem a class (WAY-329); offer to run the count again. The note of step 4 gains *Classes added*. The template says the same (`process-audit/problem_register.md:11-13`, `:53-57`). Prose: no test. |
| B4 | fixed, `4c77187` | Through `the-way-update-part-map` (`elements/part-map/skill/SKILL.md`, `decide_entry.md`, `write.md`, the template's *Trust boundary*, WAY-48 read): `task-cycle` *Trust boundary* reads `task-cycle/cycle_stages.py`; nothing else of the map changed. The search of the foundation for `cycle_stages`/transcripts found no entry that waits for it. `python -B elements/common/foundation_check.py --skip-test-citations` → 0 errors, exit 0. |
| B5 | fixed, `5e69608` (skill), `51cae12` (result) | Both now say once: "WAY-338 starts a new series at a new price list, or at a change of the form of a stage report, of the list of classes or of the instructions of the reviewer. The count splits more often than that: at a new price list, at a date of the register's list of classes, and at any change of the files of the-way under `task-cycle/change`, `plan`, `review`, `spec` or of `task-cycle/cycle_stages.py`, whatever the change, so that it compares less and never across a change WAY-338 names." The computation is unchanged. |
| m1 | fixed, `51cae12` | A commit that adds the copies of several cycles is no key of the index; a problem (or refused row) naming it goes to *Unknown values* ("its Record is a commit that adds the records of more than one cycle…") and each of those cycles' counts read `at least n`. Test `RegisterCount.test_a_record_that_adds_the_records_of_two_cycles_names_neither` (the reviewer's scratch p1 case). |
| m2 | fixed, `51cae12` | The errors of the locations file and the price list name `--locations` / `--prices`, never the path; the skill's sentence "never a path" is now true. Tests `Locations.test_a_missing_file` (path absent from stderr), `Locations.test_a_price_list_that_is_missing_or_wrong_is_named_by_its_option_not_its_path`. |
| m3 | fixed, `5e69608`, `51cae12` | Header "Cycles in which its problems stand"; skill matter 3 the same. |
| m4 | left (reason) | The finding names no sentence read wrongly and leaves the glossary to the return step (WAY-95); the handoff says to fix only such a sentence. I found none either in the sentences I wrote: "issue" is defined where the skill and template use it, and the new series sentence cites WAY-338's own words. |
| m5 | fixed, `8f2c89a` | WAY-09's first paragraph reflowed to the file's width (no word changed; `foundation_check` 0 errors); `task-cycle/skill/SKILL.md:167-168` rewrapped. |
| S3-M1 | fixed, `51cae12` | `ValueError` after `JSONDecodeError` → `Error: the locations file (--locations) is not JSON: it holds a number too long to read`, exit 2. Test `Locations.test_a_number_too_long_to_read_is_not_json_and_no_traceback`. |
| S3-M2 | fixed, `51cae12` | Git runs with every `GIT_*` variable of the environment dropped (then the three it sets) and `-c log.showSignature=false`. Test `Run.test_git_reads_the_named_checkout_whatever_git_variables_the_run_inherits` (GIT_DIR/GIT_WORK_TREE of another repository). |
| S3-M3 | fixed, `51cae12` | The refusal checks the checkout of the-way too, read or not. Test `Locations.test_a_result_directory_inside_the_way_not_read_in_the_run`. |
| S3fix-M | fixed, `51cae12` | Docstring: "a bar and the text `\x7c` then read alike". |
| S4-3 | fixed, `51cae12` | A stage or model name is cut to 200 characters before it enters a reason (also the doubled key of the locations file and a doubled model of the price list). Test `Cost.test_a_stage_or_model_name_reaches_a_reason_short_and_inside_one_cell` (2,000,000-character names with `\|`, a control character and `\x7c`: result < 100,000 bytes, one *Cost* row of four cells, no control character). |
| S4-4 | fixed, `51cae12` | A price cell that is neither a number nor `—` refuses the list (exit 2, nothing written); `—` still leaves the model unpriced. Tests `Cost.test_a_wrong_price_list_refuses_the_run_with_nothing_written` (`1e9` subtest), `Cost.test_a_price_cell_written_as_a_dash_leaves_its_model_unpriced`. |
| S4-5 | fixed, `51cae12` | `Times.times_of` asserts the record's *Process pin* and *Remarks* columns read the pin and `0`, so a stray `unknown` of either fails every time test. |
| S4-6 | fixed, `51cae12` | Tests added: crafted stage and model names in reasons (above); price list with a non-number cell, a doubled `List date`, an invalid `List date`, an oversized list; `Cost.test_a_section_of_stages_written_twice_leaves_the_cost_unknown`. |
| S4-7 | fixed, `851f761`, `51cae12` | `cycle_stages.py` writes the model `unknown` (zero counts) for a row whose transcript holds no token usage at all — for orchestrator rows, where any orchestrator transcript holds none — and `—` only where usage was read and the stage has none; the stages paragraph and the docstring say so. The audit gives such a row a cost `unknown` with its own reason. Tests `CodexWaitTest.test_a_stage_with_no_usage_reads_apart_from_one_whose_usage_was_not_read`, `Cost.test_a_stage_whose_usage_was_not_read_leaves_the_cost_unknown`. |
| Corr-M1 | fixed in part, `51cae12`; the rest contested | Fixed: a subagent turn whose cell reads `unknown` makes the share `unknown`, under `none` and under named rounds alike (such a turn may be a fix or its review). Test `Cost.test_a_subagent_turn_whose_message_was_not_read_leaves_the_share_unknown`. Contested: (a) no upper bound on the turns naming a findings file — a fix agent resumed after `questions` is a third legitimate turn of the round (`task-cycle/skill/SKILL.md:165-168` has the resuming message name the file), so a bound of two would turn true rounds `unknown`; the same paragraph's rule that no other message names it is what keeps stray mentions out; (b) a fix turn given a findings file without the word `findings` cannot be told without a guess from names, which WAY-336's *violates* forbids. Both rest on the record's word, as the reviewer says. |
| Corr-M2 | fixed, `51cae12` | `priced` uses `is_orchestrator_row`. Test `Cost.test_an_orchestrator_row_of_parallel_work_with_no_token_usage_costs_nothing`. |
| Corr-M3 | fixed, `851f761` | Codex user messages whose parts open with `# AGENTS.md instructions`, `<environment_context>` or `<user_instructions>` are skipped; the turn's message is the next one. Test `CodexFilesNamedTest.test_the_injected_instructions_before_the_prompt_are_not_the_turns_message`. On two real Codex rollouts on this disk, subagent turns that read `` (the AGENTS.md text) now read `unknown` (their real first message is an encrypted `NEW_TASK`), as the finding foresaw. |
| Corr-M4 | fixed, `51cae12` | Rows of one `#` that differ in stage name or *Files named* make the share `unknown` with the reason. Test `Cost.test_rows_of_one_turn_that_disagree_leave_the_share_unknown`. |
| S5-2 | fixed, `51cae12` | Each cycle keeps the date of every copy; an open issue waits from the earliest date of the copies its problems' *Record* names. Test `RegisterCount.test_an_open_issue_waits_from_the_copy_its_problem_names` (10 days, not 20). |
| S5-3 | fixed, `51cae12` | The problems are grouped by issue once (no issues × problems scan); *Unknown values* lists at most 500 values from the register and one row saying how many more. Test `RegisterCount.test_a_register_far_larger_than_a_real_one_lists_its_unknown_rows_in_part`. The grouping has no test of its own: only time shows it, and a timing test would be flaky. The `merge-base` calls stay one per distinct pin and fix, bounded by cycles × fixed issues. |
| S5-4 | fixed, `51cae12` | Tests added: ambiguous short hash (two real blobs sharing seven characters, found by hashing), *Problems whose cycle is not read* of *Fixed* and *Dropped issues*, a short pin resolved by `--disambiguate`, a shallow clone of the-way lacking the fix, a doubled heading and a doubled header row of the register. |
| S5fix-M1 | fixed, `51cae12` | *Problems with an unknown pin* and *Problems whose cycle is not read* read `at least n` beside a refused row too; two existing expectations changed accordingly (behaviour changed, no assertion weakened). |
| S5fix-M2 | fixed, `51cae12` | Docstring names *Refused rows* / `at least n`. |
| S6-M1 | fixed, `51cae12` | The count is the figure just before the word (`8 slices`), bounded pattern. Test `ProcessVersions.test_the_count_of_slices_is_the_figure_just_before_the_word`. |
| S6-M2 | fixed in part, `51cae12`; second half contested | A text naming an open design choice beside a word that may deny it (`no`, `not`, `none`, `nor`, `never`, `without`) is `unknown`. Test `ProcessVersions.test_a_discarded_attempt_that_denies_a_design_choice_is_not_read_as_one`. Contested: an old-form record with both items `none` whose slice review blocked on a foundation entry — the record itself says no round, and nothing in it tells otherwise; the reviewer found no such record in the archive. |
| S6-M3 | fixed, `51cae12` | Where a plan of a version is not read, Q2 is `unknown` with the reason "the plans of n cycle(s) are not read…". Two existing tests were split so that the sum and the exact third are still tested on fully read versions (`test_the_slices_of_every_plan_of_a_version_are_summed`, `test_a_third_is_not_above_a_third`, `test_unknown_reads_stay_unknown`). On the-way's history this changed no cell (diff of the result against `a5ebc88`'s: four prose lines only). |
| S6-M4 | fixed, `51cae12` | Docstring lists `diff`. |

## Checks (command and exit code)

| Command | Exit | Note |
|---|---|---|
| `python -B -m unittest discover -s <scratch with a5ebc88's cycle_stages.py> -p test_cycle_stages.py` (new tests, old code) | 1 | failing run first: 7 failures — B1 ×3 (Claude, parallel, Codex), B2 ×2 subtests, Corr-M3, S4-7 |
| `python -B -m unittest discover -s process-audit -p test_audit_count.py` (new tests, old code) | 1 | failing run first: 32 failures, each for its finding (plus the time tests' first form of the S4-5 assertion and a doubled `List date` written below the heading — both test errors, corrected before the code) |
| `python -B -m unittest discover -s task-cycle -p test_cycle_stages.py` | 0 | 49 tests |
| `python -B -m unittest discover -s process-audit -p test_audit_count.py` | 0 | 118 tests, 153.6 s |
| `python -B gate/run_tests.py process-audit` | 0 | 118 tests, 165.9 s, run in the background |
| `python -B gate/run_tests.py elements/part-map` | 0 | 39 tests |
| `python -B agent-instructions/skill_entry_points.py` | 0 | "entry points are current" (the description of `process-audit/SKILL.md` is unchanged) |
| `python -B elements/common/foundation_check.py` | 0 | 0 errors |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 | 282 files, 0 listed (a first run listed two lines of my new test, fixed in `766a66a`) |
| `python -B process-audit/audit_count.py --locations <temporary> --today 2026-11-11 < /dev/null`, temporary locations naming this worktree as `repository` under `the-way`, a temporary copy of the template as register and a temporary results directory | 0 | 72 cycles, 20 series, 131,149 bytes; the same run of `a5ebc88`'s script on the same input differs in four prose lines only |
| `python -B task-cycle/cycle_stages.py b065500f-249b-4808-a8bf-172d19a2724a --output <scratchpad>/live_after.md`, and `a5ebc88`'s script the same way | 0, 0 | before: 3 calls with no readable result, among them `Fix the whole-change review findings (general-purpose)` (this run); after: 2, both cut by the crash in slices 5 and 6 and followed by the coordinator's resume message |

The full suite was not run (the cycle runs it).

## Own-work check

Requirement most likely not met: B1's "the totals are no longer `unknown` for that reason" on a real live session, since a rule that passes crafted transcripts could miss how Claude Code really writes the live call (other line types after it, the call inside a subagent). Check: the run of the old and the new script on this very session, above. It showed the live call's warning gone and the remaining `unknown` from two crash-cut calls with a later message, which the rule rightly keeps `unknown`. A second risk, that B1's rule would also drop real lost results in Codex rollouts, was checked on two real rollouts of this disk: the waits and warnings of both are unchanged.

## Choices made

- B1: the rule is general (any call its transcript ends in), not tied to the live session's id: comparing with `CLAUDE_CODE_SESSION_ID` would miss the subagent that runs the script and a session named by path. Rejected: the session-id rule. Cost if wrong: a session stopped in a call (crash, kill) counts that call's wait as zero; that time lies after the agent's last entry, outside the working window, so neither total moves.
- S4-7: fixed in the stage report (the model `unknown`) rather than by parsing `stages.md`'s warnings in the audit. Cost if wrong: earlier `stages.md` files keep the old `—` meaning.
- Corr-M1 and S6-M3 make more values `unknown` (Codex cycles' share, versions with a part of their plans unread); a wrong figure is the worse error, by the docstring's own rule.
- S5-3: a cap of 500 listed values; the counts themselves are untouched.

## Reaches beyond the dispatch

- `foundations/decisions.md` WAY-329, WAY-331, WAY-332, WAY-333, WAY-335, WAY-336, WAY-337, WAY-338, WAY-340 (title), WAY-48, WAY-09 — read whole as entries, because the findings cite them (B3, B5, B4, m5).
- `.runs/task-cycles/weekly-process-audit/task.md` whole and `plan.md:225-264` (slice 6) — to see whether the task settles Q2 on a part of the plans (S6-M3); it does not.
- `task-cycle/record_template.md` lines with *Plan*, *Discarded attempt*, *Slices returned too large* — for S6-M1.
- The part-map skill's files: `elements/part-map/skill/SKILL.md`, `decide_entry.md`, `write.md`, `elements/part-map/template.md` *Trust boundary*, `elements/common/way_of_working.md` steps 2–4 — B4, as the handoff asks.
- Real transcripts on this disk (this session and two Codex rollouts), read only — to see what follows a live call and what Codex injects (B1, Corr-M3).

## Unread material

- `.runs/task-cycles/weekly-process-audit/reports/review_whole_report.md` — read only its section list and the *Checks run* rows of the scratch runs (lines 290-306); the handoff says to read it only where a finding needs it.
- `foundations/decisions.md` — read by entry (WAY-09 and those above), not whole; the file is the foundation log and `make-change` reads foundation entries whole, never the whole file.
- `elements/common/way_of_working.md` — read steps 2–4 (lines 103-164), not *Reading the foundation* (lines 59-102), which the part-map skill names at its step 1; I read the complete part map instead, which that step requires for this element.

## Searches not found or unclear

- `task-cycle/cycle_stages.py:read_codex_session` — an orchestrator rollout with no turn (no token usage and no `item_completed` of its own thread) makes `datetime.fromtimestamp(0).timestamp()` raise `OSError` on Windows: exit 1 with a traceback. Seen while writing the S4-7 test; not in the findings, so not fixed.
- Whether WAY-332's "a session of the audit … adds a class to the list" means the session writes the register or proposes it to the user's tool: the reviewer's direction gave both; the handoff settled writing it on the human's yes.

## Concerns

- The traceback above (`read_codex_session`, `since` defaulting to a naive epoch) is a defect of the trust boundary B4 now records; a later change should give it a check.
- On this session's transcript the totals stay `unknown` because of the two calls cut by the crash; the cycle's `stages.md` will carry that warning, for that real reason.
- Corr-M3's fix makes Codex subagent turns read `unknown` files wherever the dispatching message is encrypted, so a Codex cycle's share of fix rounds will be `unknown`; that is the true state of what the rollout lets be read.

## Questions

none

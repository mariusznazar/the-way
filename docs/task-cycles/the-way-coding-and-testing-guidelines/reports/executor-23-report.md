# Executor report — slice 23: the two pointers in `AGENTS.md`

**Status:** done

**Commits:** `be9b44d` on branch `task/the-way-coding-and-testing-guidelines` (base `b47e1b2`).

**Check result:** all three focused checks exit 0; the handoff's literal `check_instructions.py AGENTS.md …` form exits 2 (its first argument is the root directory), so I ran it with `.` as the root.

## Files changed

- `AGENTS.md`: +5 / -0. A new section `## Guidelines` at the end of the file, below `## Backlog`, with two lines:
  - `- Before you change the-way's code, read `guidelines/coding.md`.`
  - `- Before you write or change a test, read `guidelines/testing.md`.`

## What was done

- The two lines follow the pointer form of `instruction-files/SKILL.md` ("Before X, read `path`"), name the file by its path in backticks, and carry the condition of the task (changing the-way's code; writing or changing a test).
- Neither line names a `guidelines/coding-<kind>.md` file or holds a command. Per WAY-212 and WAY-16, the kind files are left to the table of `guidelines/coding.md`.
- `AGENTS.md` of the-way holds no installer block (no block markers in the file), so "outside any block of the installer" holds trivially.
- No `@` import was added (WAY-129, `instruction-file-imports`).

## Checks

| Check | Command | Exit code | Result |
|---|---|---|---|
| Instruction checker, repository root (after the change) | `python -B instruction-files/check_instructions.py .` | 0 | 0 error, 0 warn, 5 info; the info lines now include `guidelines/coding.md` (162 lines) and `guidelines/testing.md` (270 lines), which the pointers make reachable |
| Instruction checker, `--file` form on `guidelines/coding.md` | `python -B instruction-files/check_instructions.py . --file guidelines/coding.md` | 0 | exit 0 |
| Instruction checker, literal form from the handoff | `python -B instruction-files/check_instructions.py AGENTS.md guidelines/coding.md guidelines/testing.md` | 2 | not a valid call: the first argument is the root directory; not a failure of the change |
| Test of instruction files | `python -B agent-instructions/test_instruction_files.py` | 0 | before and after the change |
| Foundation check | `python -B elements/common/foundation_check.py` | 0 | before and after the change (`0 errors`) |
| Grep for `coding-` and `@` in `AGENTS.md` | `grep -n "coding-\|@" AGENTS.md` | 0 | no hit on the new lines; the only hit is an existing line 17 (`python -B agent-instructions/agent_type_copies.py --write`), not part of this change |

No new test was written and no invariant's test was added: the change is prose, so the checks above are the test. The gate (`gate/run_tests.py` without a directory) was not run, as the handoff forbids.

## Own-work check (`make-change` section 3)

- **Requirement:** the two pointers name `guidelines/coding.md` and `guidelines/testing.md` by path in backticks, each with its condition, and name no `guidelines/coding-<kind>.md` file and no command.
- **Check:** read the two lines of `AGENTS.md` and grep as above; run the instruction checker, which follows backticked `.md` names in the root `AGENTS.md`, so the two files are checked too.
- **Showed:** exit 0 from the checker, the two files reported as info (sizes only, no finding); no kind file and no command on the new lines.

## Working copies

None made. No worktree, clone or script was created; `.runs/executor-23/` was not needed.

## Questions and concerns

- None requiring an answer before the review.
- The handoff's `Checks` line gives a literal command that cannot run as written (exit 2). The plan's `Checks` line has the same form. The orchestrator may want to correct the form in the plan; the real form is `check_instructions.py .`.
- The handoff's *Read* ranges were used, not the plan's (they differ by a few lines; the handoff says it refreshed them).
- **Weakest point:** whether an agent that changes the-way's code recognises the moment "before you change the-way's code" as the one the pointer names. WAY-128 asks for the condition as the agent meets it; I judged that the root `AGENTS.md` loads at session start for Claude Code, Codex and Cursor (per `instruction-files/tool_loading.md`), so the line is seen in every session. This was not measured in a session. Check: a session that changes a file under `elements/` reads `guidelines/coding.md` after the pointer; not run.

## Unread material

- `foundations/decisions.md` WAY-212, WAY-16, WAY-128, WAY-129 and `foundations/part_map.md:155-173` and `foundations/invariants.md` ones named in the handoff: read whole.
- `guidelines/coding.md` and `guidelines/testing.md`: not read by me (named by the pointers only; the checker reported their sizes).
- The Scope list of the decisions on instruction files (WAY-130, WAY-131, WAY-133, WAY-256, WAY-258, WAY-265, WAY-254, WAY-386, plus those with Scope `instruction-files, agent-instructions`): read by heading only, to check for a conflict with the pointer form; not read whole. No conflict was seen.
- Foundation entry E17 (the plan's *Depends on*): not read.
- `task-cycle/change/SKILL.md`, `slice.md`, `instruction-files/SKILL.md`, `tool_loading.md`, `changing.md`, `kind_main_file.md`: read whole. `plan.md`: read from line 1 to 40 and from 909 to end (slice 23 and the orchestrator's additions); the rest not read.
- Invariants read whole: `repository-file-location`, `derived-file-content`, `ci-checking-commands`, `tracked-file-private-paths`, `map-reference-target`, `instruction-file-imports`, `root-claude-md-import`, `guidelines-file-place`. Not read: `script-language`, `script-imports`, `script-subprocesses`, `cross-part-imports`, `test-method-citation`, and the others, since slice 23 adds no Python file (the handoff's additions apply to Python-adding slices).
- Reach beyond the handoff: `a file of the author's private notes` (read before the commit, as the user's global instructions require). The commit hook `rules-on-demand` blocked the first commit attempt once and asked for a retry; the retry went through.

## Searches not found or unclear

- The plan's and the handoff's `Checks` command form (see above): unclear, resolved by running the checker with `.` as root.
- The "installer block" in `AGENTS.md`: not found in the file; the phrase is satisfied vacuously.
- No decision named a fixed wording for the two lines beyond WAY-212's example (`Before you change the product's code, read `guidelines/coding.md``); I used the same shape for the-way.

# Fix report — the Minor findings of the whole-change review (cycle `cycle-subagent-types`)

**Status:** done

**Commit:** `b0ab508` (range `2245f08..b0ab508`). The worktree is clean.

## Findings

| Finding | Outcome | How, or the evidence |
|---|---|---|
| M1 (WAY-255: the author's waits keep to four minutes) | contested, left as written | The reviewer itself recommends leaving it and naming it in the request. It is the author's addition, not a rule of To do 6; it keeps the waits as they are today and follows from the page quote the entry carries (the `1h` is ignored while a subscription spends usage credits). Changing it would let the author wait long on the strength of an hour that Claude Code may not grant. Goes to the request's list as the reviewer's. |
| M2 (WAY-369: 10.5k "measured", paired with 21,759) | fixed | The *Rationale* now reads "starting without them lowers the start by about eleven thousand tokens, to 10.5 thousand, a figure whose conditions — version, model, tools — are not recorded"; the word "measured" and the pairing with the first probe's figure are gone. The *Rejected* line keeps the row's own wording. |
| M3 (lines past the column) | fixed | Every added line of `foundations/decisions.md` (WAY-255 binding paragraph, *Rationale*, *Rejected*; WAY-368, WAY-369, WAY-370 in full), `foundations/part_map.md` (`installation-command`) and `task-cycle/record_template.md` (the `- Author:` bullet and the sentence I added to the Events paragraph) is now at most 100 characters: checked by reading `git diff -U0 715ae20` of the three files as UTF-8 and counting, 0 lines over 100. Only the blocks that held a long added line were rewrapped, so the rest of each paragraph keeps its breaks. Lines 101–105 of my additions in other files (`README.md`, `task-cycle/skill/SKILL.md` two lines, `task-cycle/change/SKILL.md`, `task-cycle/skill/return_step.md`, `installation/README.md`) are not named by the finding and were left. |
| M4 (a bare skill name in `planning.md`, `spec_review.md`, `correction.md`, `return_step.md`) | fixed | One parenthesis with the method file's path at the first mention in each file: `plan-task` (`task-cycle/plan/SKILL.md`) in `planning.md`; `write-spec` (`task-cycle/spec/SKILL.md`) in `spec_review.md`; `make-change` (`task-cycle/change/SKILL.md`) in `return_step.md`; in `correction.md` `review-change` (`task-cycle/review/SKILL.md`) and `make-change` (`task-cycle/change/SKILL.md`). The second mention of `review-change` there (line 38) and of the names in `task-cycle/skill/SKILL.md` stay labels, which step 3 defines. |
| M5 (the sentences say "has no skill tool" without condition) | fixed | `task-cycle/plan/SKILL.md`: "Where the planner has no skill tool, as in the cycle's types, a skill this file or a file it reads names is the `SKILL.md` whose frontmatter `name:` is that name, read as a file under the same root." `task-cycle/skill/foundation_step.md`: "the writer reads it as a file where it has no skill tool, as the cycle's types have none (WAY-368)." |
| M6 (names in `install.py` that stopped being exact) | fixed | The docstring of `plan()` now says "the entry points and agent definitions it deletes". A new function `is_agent_definition(path)` (a file directly in `.claude/agents`) names the kind once; `owned()`, the DELETE message and the loop that removes an emptied directory use it in place of `path.name == "SKILL.md"`. No change of behaviour. `install.py` grew by 7 lines net (12 added, 5 removed). The growth of the file is the reviewer's own Minor reading under WAY-328 and WAY-363, and nothing beyond it. |
| M7 (the README row and WAY-368 state "starts without the list of skills") | contested, not changed | The orchestrator's handoff reports that the probe has run on Claude Code 2.1.325 and `claude-sonnet-5-5`: an agent of each type reported no list of skills and no Skill tool, while a `general-purpose` agent of the session reported both. The statements are true for the route `disallowedTools: Skill`; no change of the definitions or of the entries is called for. The probe's figures go into the request's description, not into a file. |
| M8 (how the orchestrator knows its session has the types) | fixed | `task-cycle/skill/SKILL.md` now reads "Where the agent types that your dispatch tool offers hold no such type — another harness, or a session started before `.claude/agents/` held the definitions — dispatch the stage as you would without them, and write in the record's row of that dispatch that it ran without its type and why (WAY-370)." |

Not touched, as the handoff says: the reviewer's two out-of-scope notes (the junction in `check_parents`, the duplicate name).

## Checks (command and exit code)

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B gate/run_tests.py task-cycle` | 0 | OK (run on `b0ab508`) |
| `python -B gate/run_tests.py agent-instructions` | 0 | OK |
| `python -B gate/run_tests.py instruction-files` | 0 | OK |
| `python -B gate/run_tests.py installation` | 0 | 56 tests OK in 875 s (run on `b0ab508`) |

Not run: the product's full gate (the orchestrator's).

## Own-work check

- **Requirement most likely not met:** the fix of M6 changes the code of the installer's trust boundary, and a wrong `is_agent_definition` would send an agent definition to the skill rule (or the other way) in the own-file check, the DELETE message or the removal of an emptied directory. Check: the mutation of the new function, below, run on the tests that exercise those three places.
- Mutation of `is_agent_definition`, the selected tests of `installation/test_agent_types_installation.py` (the stale delete, the kept directory, the refusals, the moved pin; `-k gone -k lacks -k directory_of_the_definitions -k not_the_installers -k moved_pin`): `return False` makes 3 fail, `return True` makes 2 fail (exit 1 each); `install.py` restored, `git status --short` prints nothing.

## Reaches beyond the handoff

None. I read `task-cycle/change/fix.md` as the method says.

## Unread material

None of what this handoff names. The reviewer's full report `reports/whole-review-report.md` was not opened (the handoff says to read it only if a finding needs it; none did).

## Searches not found or unclear

none

PASS b0ab508

# Review of the fix — cycle `cycle-subagent-types`

Variant: the fix of earlier findings (`task-cycle/review/fix.md`, `task-cycle/review/SKILL.md`). Range `2245f08..b0ab508`, one commit `b0ab508` ("Fix the Minor findings of the whole-change review …"); `git rev-parse --short HEAD` printed `b0ab508`; the worktree was clean. Read-only; I changed nothing tracked (scratch products only under the scratchpad).

Changed files of the fix (`git diff --stat`): `foundations/decisions.md` (rewraps, one rationale rewording), `foundations/part_map.md`, `installation/install.py` (+12 −5), `task-cycle/plan/SKILL.md`, `task-cycle/record_template.md`, `task-cycle/skill/SKILL.md`, `correction.md`, `foundation_step.md`, `planning.md`, `return_step.md`, `spec_review.md`; 11 files, +91 −79.

## Each finding of the findings file

- **M1 — contested, left as written: keep the declination.** It is my own recommendation ("leave it, naming it in the request"). The WAY-255 text is unchanged in meaning (only rewrapped). It must be named in the request, which the fix report says it will do.
- **M2 — fixed.** WAY-369 *Rationale* now reads "starting without them lowers the start by about eleven thousand tokens, to 10.5 thousand, a figure whose conditions — version, model, tools — are not recorded". "Measured" and the pairing with the first probe's 21,759 are gone; the figure carries its missing conditions, as I suggested. The *Rejected* line keeps the row's own wording ("the start falls to 10.5 thousand tokens"), which is the task's.
- **M3 — fixed for the three files and the lines it named; see N1 for what the fix itself added.** I measured every added line of the fix diff: the lines of `foundations/decisions.md`, `foundations/part_map.md`, `task-cycle/record_template.md` (the `- Author:` bullet and the Events sentence) are within 100 columns (the two "101" my awk counted in `decisions.md` and `part_map.md` hold an em dash of three bytes, so they are 99 characters; the third "101", the docstring of `is_agent_definition`, is a byte count too: it is ASCII and truly 101, see N2). The earlier 122, 173 and 187-column lines of WAY-369 and WAY-368 are rewrapped.
- **M4 — fixed.** One parenthesis with the method file's path at the first mention in each file: `plan-task` (`task-cycle/plan/SKILL.md`) in `planning.md`, `write-spec` (`task-cycle/spec/SKILL.md`) in `spec_review.md`, `make-change` (`task-cycle/change/SKILL.md`) in `return_step.md`, and in `correction.md` `review-change` and `make-change` with their paths. The second mention of `review-change` in `correction.md` stays a label, which step 3 defines; that agrees with my finding ("one clause in each file").
- **M5 — fixed.** `task-cycle/plan/SKILL.md`: "Where the planner has no skill tool, as in the cycle's types, a skill this file or a file it reads names is the `SKILL.md` whose frontmatter `name:` is that name, read as a file under the same root." `task-cycle/skill/foundation_step.md`: "the writer reads it as a file where it has no skill tool, as the cycle's types have none (WAY-368)". Both now true in the fallback too.
- **M6 — fixed.** The `plan()` docstring says "the entry points and agent definitions it deletes". `is_agent_definition(path)` (`path.parent.as_posix().endswith("/" + AGENT_DIRECTORY)`) names the kind once, and `owned()`, the DELETE message and the removal of an emptied directory use it in place of `path.name == "SKILL.md"`. Behaviour is unchanged: I traced the three call sites and tried them (below). No new reach: a path the installer writes is a foundation file (own branch earlier in `plan()`), a skill entry point `<target>/.claude|.agents/skills/the-way-x/SKILL.md` (parent ends in `/the-way-x`) or an agent definition `<target>/.claude/agents/<name>.md` (parent ends in `/.claude/agents`). A skill directory could not be named `agents` under `.claude` by the installer.
- **M7 — contested, not changed: consistent with my finding.** My M7 was "not a defect of the files today; a dependency on the probe the orchestrator must keep". The handoff reports that the orchestrator's probe on Claude Code 2.1.325 / claude-sonnet-5-5 showed agents of both types without a skills list and without a Skill tool (25,321 and 25,369 tokens at the first call against 37,109 for a general-purpose agent). With that result the statements "starts without the list of skills" in `installation/README.md` and WAY-368 are true for the route `disallowedTools: Skill`, and no change is called for. I did not rerun the probe (it needs a fresh session, as the handoff says it ran). `git grep` for the three probe figures in tracked files: no hit, so no probe figure went into the repository, as the handoff requires. The probe's result belongs in the request's description (the acceptance criterion).
- **M8 — fixed.** `task-cycle/skill/SKILL.md`: "Where the agent types that your dispatch tool offers hold no such type — another harness, or a session started before `.claude/agents/` held the definitions — dispatch the stage as you would without them, and write in the record's row of that dispatch that it ran without its type and why (WAY-370)." The orchestrator is told where to look.

## New findings in the fix (all Minor, within the task; none blocks)

N1. Minor. The fix added over-long lines in the same files where M3 was fixed: `task-cycle/skill/SKILL.md` line 209 (the M8 sentence, 135 columns), `task-cycle/skill/correction.md` lines 29 and 37 (131 and 123 columns), `task-cycle/skill/foundation_step.md` line 19 (130), `task-cycle/skill/planning.md` line 8 (120), `task-cycle/skill/spec_review.md` line 5 (124). They are the lines of M4, M5 and M8 inserted without rewrapping the paragraph, so the finding M3 reopens for them in layout only. The author's report says only the lines that held a long added line in `decisions.md`, `part_map.md` and `record_template.md` were rewrapped and names these as not in the finding; they are lines the fix itself wrote. Layout only; no test fails on them.

N2. Minor. `installation/install.py`, docstring of `is_agent_definition` (second line, 101 columns): one column over the 100 of the file's other lines. Layout only.

N3. Minor, remark. `task-cycle/record_template.md`: the Events sentence now ends "…and why." on its own line and the next line "Name handoff and report paths and input and output commits, so work" is short; the paragraph reads correctly, only the break is odd. No action.

No Critical, no Important finding. Out of scope: nothing new; O1 (a Windows junction at `.claude` is followed by `check_parents`, shared with the skills' entry points) and O2 (a stray `the-way-ghost.md` with another type's name) of my earlier report stand and were not asked to be fixed; the fix did not touch them (`check_parents` is unchanged in the diff).

## Trust boundary: crafted inputs rerun against the fixed installer

The fix touches `installation/install.py`, so I reran the cases that `is_agent_definition` bears on, using scratch products and `python -B installation/install.py <product> --url <worktree> [--apply]` from this worktree at `b0ab508`:

| Input | Result on the fixed installer |
|---|---|
| a CRLF copy of an own definition `the-way-stage.md`; a stale own `the-way-gone.md`; a lookalike `the-way-mine.md` (no mark); `the-way-ghost.md` whose header names `the-way-author`; a product's own `reviewer.md` (preview) | `REPLACE .claude/agents/the-way-stage.md`, `CREATE .claude/agents/the-way-author.md`, `DELETE .claude/agents/the-way-gone.md (its agent type is no longer in the-way)`; nothing else listed |
| the same product with `--apply`, answer `y` (exit 0) | `reviewer.md`, `the-way-mine.md` and `the-way-ghost.md` remain; `the-way-gone.md` deleted; `the-way-author.md` and `the-way-stage.md` written; `.claude/agents/` stays |
| a directory at `.claude/agents/the-way-author.md`, `--apply` | exit 1, `Error: Existing integration file differs: …\.claude\agents\the-way-author.md`, nothing written |
| a directory named `.claude/agents/the-way-dir.md` (a name no type owns), preview | no `DELETE` line (a directory is not an own definition) |
| `.claude/agents` a symlink to a directory outside the product, `--apply` | exit 1 (printed `Error: Parent path is not a regular directory: …\.claude\agents`); the outside directory holds only its file `k.txt` |
| a stale own skill entry point `.claude/skills/the-way-oldskill/SKILL.md`, preview and `--apply` | `DELETE .claude/skills/the-way-oldskill/SKILL.md (its skill is no longer in the-way)`; the emptied skill directory is removed (`oldskill` count 0 under `.claude/skills`); the agents directory of the product stays |

The delete message ("skill" vs "agent type") and the removal of an emptied directory (only for a skill's own directory) are the two behaviours the helper decides; both correct. The new test file (below) covers the stale delete, the kept directory, the refusals and the moved pin.

## Checks I ran (command and exit code)

| Command | Exit | Result |
|---|---|---|
| `git rev-parse --short HEAD`; `git status --short` | 0 | `b0ab508`; clean |
| `git diff 2245f08..b0ab508` (read whole) | 0 | 11 files |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B gate/run_tests.py agent-instructions` | 0 | 25 tests OK |
| `python -B installation/test_agent_types_installation.py` | 0 | 12 tests OK in 128.6 s |
| scratch-product runs of `installation/install.py` (table above) | as shown | as shown |
| a column count over the added lines of the diff (awk on `git diff -U0`) | 0 | the long lines of N1 and N2; the two "101" of `decisions.md` and `part_map.md` are multibyte |
| `git grep` for the three probe figures in tracked files | 1 (no hit) | none stored |

Not run, and why: the full gate (the orchestrator's); the full `installation` directory (about 8 to 15 minutes; the author reports 56 tests OK on `b0ab508` in 875 s, and the new file, which exercises the changed helper, I ran myself); `task-cycle` and `instruction-files` directories (the fix changes prose only there; the author reports them OK on `b0ab508`; I did not repeat them); the orchestrator's probe (it ran in its own session).

## Reaches beyond the handoff

- `task-cycle/review/SKILL.md`, `task-cycle/review/fix.md`: the method, as the handoff says.
- A column count over the fix diff and a `git grep` for the probe figures: to check M3 and the "no probe figure in the repository" condition.
- Scratch products under the scratchpad for the crafted-input reruns (the handoff asked for them).

## Unread material

Read whole: the handoff, the findings file, the fix report, the whole fix diff, `task-cycle/review/fix.md`, `task-cycle/review/SKILL.md` (already read in the first review). The fix touches the same files as my first review, whose selection I carry; I did not re-read the foundation entries beyond the changed WAY-255, WAY-368, WAY-369 passages (read in the diff with their surroundings) and the part-map `installation-command` entry (read in the diff). No decision was run through by title again in this review (the fix review reads only what the fix changed). The unscreened rest of the decision log and the files named unread in my first report stay as that report states. Not read: `reports/whole-review-report.md` only as my own earlier text, from memory of this session.

## Searches not found or unclear

none

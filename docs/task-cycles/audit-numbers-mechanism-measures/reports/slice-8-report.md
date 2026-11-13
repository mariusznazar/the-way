# Slice 8 report — The audit session's instruction puts the measures before the human

**Status:** done

**Commits:** `49ab2fa..1923ef4` (one commit)
- `1923ef4` Put the measures and the gate times before the human in the audit session

**Files changed:** `process-audit/SKILL.md` (+37, −12). No other file touched. The skill's description is unchanged, so the entry points were not regenerated.

**Check result:** both slice checks pass; nothing failed or was left unrun.

## Method

`make-change`, variant "a slice, or the retry of a slice". Read `task-cycle/change/SKILL.md` and `task-cycle/change/slice.md`, `instruction-files/kind_skill.md` and `instruction-files/changing.md`. The product's gate was not run.

## Checks

| Check | Command | Exit code | Result |
|---|---|---|---|
| Instruction check, before the edit | `python -B instruction-files/check_instructions.py .` | 0 | 0 error, 0 warn, 3 info; no finding on `process-audit/SKILL.md` |
| Instruction check, after the edit | same | 0 | output byte-identical to the base run |
| Skill reach test | `python -B -m unittest discover -s gate -p "test_skills_reach_the_way_sessions.py"` | 0 | Ran 2 tests, OK (before and after) |

No test was written: the slice changes prose that instructs an agent, and the slice's checks name no new test. No failing run occurred, so no run pair needs recording.

## Own-work check

- **Requirement:** the new text must name the sections, the `Error:` line and the series rule exactly as `process-audit/audit_count.py` writes them, and must not claim a series split the count does not make.
- **Check (read against the script):** the section titles `## Mechanism measures` (script line 2640), `## Gate runs` (2656), `## Measure versions` (2560) and the series headings `### Mechanism measures, series N` / `### Gate times, series N` (in `measure_versions_lines`) match the skill text. The `Error:` line format `the file \`<file>\` of the copy lacks the field \`<field>\`` (script line 1282, printed at line 2891) matches the skill's description. The script paths `task-cycle/cycle_measures.py` and `task-cycle/gate_times.py` (script lines 379-380) exist and are the ones the series test uses. The series rule matches WAY-339 as it now stands (a change of the instructions of the cycle, reviewer or author starts no measure series).
- **Result:** no mismatch found. This was a reading check, not a script check.

## What the edit does

1. *Rules of working*, the series bullet: the cost series keep their rule; the mechanism measures and the gate times get the script-only split rule (WAY-348, WAY-350); no number of one series, nor of the measures or gate times beside the cost.
2. Step 2, exit code 1: names the copy's missing field, the `Error:` line's content, and that *Unknown values* names the same file and field.
3. Step 3: the section list gains *Mechanism measures*, *Gate runs*, *Measure versions*, each introduced in one plain sentence.
4. Matter 1: the stale sentence about `stages.md` of an earlier form is brought to what the count gives now (earlier form: no times, the cost from its table of tokens by model, the fix-round share `unknown`).
5. Matter 4: the series of *Measure versions* follow in the same matter, one series at a time, rows quoted with their header, then what follows and what does not, then one open question with no recommendation; gate runs with another gate shown apart and never compared; a measure is material, never a priority.

The step that writes the note is unchanged.

## Unread material

- The task passages (`task.md:37`, `:46-51`, `:63-68`, `:116-125`) and plan passages (Slices 1, 3, 5-7) were not opened in the worktree. Their text was taken from the handoff's copies, as the handoff allows. Not read: `task.md` and `plan.md` as whole files, plan Slice 1 and Slice 3 except through the handoff's copies.
- Foundation entries read whole: WAY-339 (current, `foundations/decisions.md` 11193-11240), WAY-341 (11254-11282), WAY-348 (about 11519-11548), the `process-audit` part in `foundations/part_map.md` (114-123). Not read, because not on my list: WAY-344, WAY-347, WAY-349, WAY-350, WAY-352 and the other entries of commit `a030dbf`. The handoff's "foundation entries rows 2, 3" refers to a table in the plan that my handoff does not carry, so I could not check it.
- `instruction-files/kind_skill.md` and `instruction-files/changing.md` read whole.
- `process-audit/audit_count.py` read in the parts that write the sections, the errors and the docstring (lines 1-230, 350-362, 379-380, 1276-1284, 1440-1452, 2505-2680, 2680-2900). Not read: the rest of the 2900-line file.

## Searches not found or unclear

- `Grep` on `foundations/` for `WAY-348` and for the `WAY-347`-`WAY-352` headings returned no match, while `git grep` on HEAD finds them (`foundations/decisions.md`). The `Read` tool on `foundations/decisions.md` also returned a view with 11506 lines, while `wc -l` on the worktree file gives 11709, and its line numbers for WAY-339 and WAY-340 were offset from the file on disk. I used `sed` and `git show` for the foundation text. The cause was not verified; the tool views of that file may be stale.
- `git status` was clean before the edit and after the commit.

## Reaches beyond the handoff

- `git show a030dbf` and `git grep ... HEAD` to find the WAY-347-352 entries, because the foundation search did not find them: to confirm the identifiers the handoff named exist at HEAD. No entry was edited.
- `python -B instruction-files/check_instructions.py .` and the skill reach test: the handoff's checks.

## Choices made

- The series rule went into the existing *Measures are compared inside a series only* bullet, not into a new bullet, so the rule stays with the other series rules. Cost if wrong: a longer bullet; the bullet is still one paragraph.
- The matter 4 addition is inside matter 4, not a fifth matter, as the handoff's "Matter 4 gains the measures" says. Rejected: a fifth matter, which would change the order of the matters the human sees. Cost if wrong: a longer matter 4.
- Matter 1's sentence is split in two (no times and no cost on one side, the earlier form's table on the other) rather than rewritten as a list. Cost if wrong: none for the agent.
- Commit message in English, imperative, as the branch's recent history; no attribution line was given in the system reminder, so none added.
- Adding files by path: only `process-audit/SKILL.md`.

## Problems observed

- None in the product. The tool-view mismatch on `foundations/decisions.md` (above) is the only oddity; I could not verify its cause.

# Slice 7 report: the skill of the weekly audit session

**Status:** done with concerns (the concerns are choices of mine beyond the handoff's list; see Choices and Concerns)

## Commits (base `2e7168c`)

| Commit | What |
|---|---|
| `94a4f4e` | Add the skill that leads the weekly audit of the process: `process-audit/SKILL.md`, `README.md`, and the generator's output (2 new entry points `the-way-audit-process`, 44 existing entry points regenerated) |
| `a5ebc88` | Say which date of a count shows the scheduler did not run (`process-audit/SKILL.md`, one passage found in the dry read) |

Files changed, whole range (`git diff --numstat 2e7168c HEAD`, 48 files): `process-audit/SKILL.md` +159/-0; `README.md` +7/-3; the generator's output under `.claude/skills/` and `.agents/skills/`: 2 new `the-way-audit-process/SKILL.md`, and 22 skills x 2 changed by one line each (the entry point's list of the-way skills gained `audit-process`; written only by `skill_entry_points.py --write`, never by hand). The generator reported no obsolete output path.

## What the skill says (taken from the code, run on temporary files)

Skill `audit-process`, `process-audit/SKILL.md`, no variant file (every step is one every use comes to, WAY-256). Sections: what the audit rests on (register from the template filled by the user's own tool and adapted by the user, WAY-329; counting unattended on the night from Friday to Saturday started by a scheduler the human sets up, a weekly backlog task starting the session, both human actions the skill names and does neither, WAY-340, WAY-140); rules of working (no priority from returns, WAY-335; no comparison across series nor week to week, WAY-338; no replay, WAY-339; fix by version not date, WAY-334; `unknown` and `at least n` kept; results outside every repository, WAY-331, WAY-320); step 1 find the places (entries `problem_register`, `audit_results`, `repository` as `project-level/backlog_place.md` gives; ask with ways, costs, recommendation, WAY-113); step 2 get the latest count (the options `--locations`, `--repository`, `--prices`, `--today`; exit 0, 1, 2; `count-<date>.md`, `count-latest.md`); step 3 the matters one at a time (what the count could not read; what came back after a fix; what still waits; what each version shows, series by series); step 4 write `audit-<date>.md` beside the counts.

Every section, column, option, entry name and exit code the skill names was checked against `process-audit/audit_count.py` (counts of each name in the code: all present), and the real run below.

## Checks

| Command | Exit | Result |
|---|---|---|
| `python -B agent-instructions/skill_entry_points.py` (after `--write`, and again after the last commit) | 0 | `entry points are current` (before `--write` it listed the new pair to create and 44 to change, all by the added name in the list) |
| `python -B agent-instructions/skill_entry_points.py --write` | 0 | wrote 46 files, no obsolete path reported |
| `python -B gate/run_tests.py gate` (after `94a4f4e`, and after `a5ebc88`) | 0 | 20 tests OK both times |
| `python -B gate/run_tests.py agent-instructions` (after `94a4f4e`, and after `a5ebc88`) | 0 | 18 tests OK both times |
| `python -B gate/run_tests.py installation` (after `94a4f4e`) | 0 | 44 tests OK (237 s); no change of `installation/install.py` was needed |
| `python -B elements/common/foundation_check.py` (after `94a4f4e`, after `a5ebc88`) | 0 | 0 errors |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` (after `94a4f4e`, after `a5ebc88`) | 0 | 282 files, 0 listed |
| `python -B instruction-files/check_instructions.py .` | 0 | 0 error, 0 warn, 3 info; it checks the repository's root instruction files and what they name, not this skill |
| `python -B process-audit/audit_count.py --locations <scratchpad>/s7/locations.json --today 2026-11-11 </dev/null` (temporary locations file: `the-way` with `repository` set to this worktree, a copy of the template as register, a temporary results directory) | 0 | `Wrote count-2026-11-11.md and count-latest.md: 72 cycles in 1 of 1 repositories.`; sections as the skill lists them; 20 series |
| the same command with a locations file whose `the-way` holds no `problem_register` | 2 | `Error: the locations file holds no entry `problem_register` under `the-way``, as the skill's step 2 says |
| the same command with a locations file that does not exist | 2 | `Error: the locations file <path> does not exist`: this error does name the path it was given (the `--locations` argument), not a path held by an entry |
| `python -B process-audit/audit_count.py --help` | 0 | options as the skill lists them |
| grep of the skill for a person's name, a drive-letter path, `/Users`, `[[` | none found | no name, absolute path or note link |

Not run: the full suite (WAY-160); `gate/run_tests.py process-audit` — no code of that part changed in this slice. Nothing was written into the user's real `~/.the-way` or places; all runs used the scratchpad.

## Own-work check (WAY-164)

- **Requirement most likely unmet:** "the skill says what the command really does", and "written for any builder: no person's name, no absolute path, no note link" — a skill can name a column, option or exit that the code does not have, or carry the author's setting.
- **Check:** counted each name of the skill in `audit_count.py` (sections, columns *Days waiting*, *Refused rows*, *Files named*, *Begins at this version*, entries, file names); ran the command on temporary files and read its section headings and the first rows of the tables; ran its two error cases; grepped the skill for names and paths; ran the private-paths check on the committed tree.
- **What it showed:** every name present in the code; the real result has the sections the skill names; exit 2 and its line as described; no name or path; check exits 0.
- **Dry read** (the skill read once as the agent who runs the session). Steps I could not follow from the text alone:
  1. The staleness test of the latest count (step 2): "older than the last night" did not say which date; the date is the UTC day of the run. Fixed in `a5ebc88`.
  2. Step 3 matter 1 asks for the kinds of `unknown` and how many cycles each touches: the agent has to count rows of *Unknown values* by its *Value* column; the skill does not say so and I left it (a count over a table is within what an agent does).
  3. Which products to read: the skill says "each product whose cycles the audit reads" in step 1 and step 2 says the command reads every key with an entry `repository`; an agent can take it as every such key. Left as it is.
  4. The "recommendation" in step 1 is asked for, but nothing says what to recommend for a missing place; it depends on the human's disk.
  5. The skill does not say how to set up the scheduler or the weekly task (a human action, WAY-140), only what runs and what the human does.

## Choices (the way rejected and the cost if wrong)

1. **The session notes a correction of the register and does not make it.** The skill says the register is the user's own tool's to change, and the session writes the correction in the result. Rejected: the session editing the register. Cost if wrong: one sentence changes; the register is the user's file filled by their tool (WAY-329).
2. **The session reads the newest earlier note `audit-<date>.md`** only to say that a matter was weighed or set aside before. Rejected: no reading of earlier notes, which leaves the human to re-weigh blind. Cost if wrong: one sentence; it reads no measure of an earlier week, so WAY-338 is kept.
3. **The note holds *Weighed*, *Set aside*, *Not reached* and the register corrections**, shown to the human and written on the human's yes. The handoff gave "what the human decided to weigh and the matters it set aside" only; the other two are mine. Rejected: a note of the two lists alone, which loses the unreached matters of an interrupted session.
4. **Running the command from the session needs the human's yes**, since it replaces the same day's two count files.
5. **Matters are open questions of assessment, with no recommendation** (WAY-113: a question of assessment stays open); the one question of step 1 about a missing place gives ways, costs and a recommendation. I did not name the user's own rule for putting material before the human, as the orchestrator said.
6. **Series whose rows are all `unknown`** go together in one matter instead of one by one: the count of the-way's own history has 20 series, most of them without an answer.
7. **No "the-way- prefix" sentence for other skills**, since the skill names no other skill; the paragraph of where the-way lies follows `foundation-review/SKILL.md`.

## Questions

None.

## Concerns

- **The skill lives in the-way, and its entry point stops in a product** (the generated text says to stop where a product pins the-way), as for the other skills; the installer's list of skills is unchanged, as the handoff says. The skill's paragraph still says what the root is "in a product" (`.the-way`), copying the form of `foundation-review/SKILL.md`. If the audit is meant to run only from the-way's own checkout, that sentence is spare.
- **Slice 6's concern about the key `the-way`** (the-way's own cycles resolve their pins only under the key `the-way` with its `repository` entry) is stated in the skill only as "under `the-way` the entry `repository` is the checkout of the-way, which holds the-way's own cycles and the history the process versions are read from". I did not verify the cause Slice 6 saw, so I did not state more.
- **The first result is mostly `unknown`** (70 of 71 costs, Q3 everywhere, 20 series for 53 versions in the-way's own history, per Slice 6). The skill says so in matter 1 and in the series matter; the human will see it at the first session.
- **A count run by the skill writes into the user's results place**; I did not test it against the user's real place (handoff forbids it).
- Windows: the dry runs used a temporary locations file with drive-letter paths inside the scratchpad; the skill itself holds none.

## Reaches beyond the handoff

- `foundations/decisions.md` WAY-334 whole (`10952-10972`), read to cite it in the skill; the handoff's list for this slice does not name it.
- `agent-instructions/skill_entry_points.py` (first 60 lines) and `.claude/skills/the-way-review-foundation/SKILL.md` (first 20 lines), to see what the generator produces and why the 44 existing entry points change.
- `task-cycle/record_template.md` (lines 1-12 and a grep of *Review rounds*), to name the form of the record's item.
- `the user's rule file on scripts`, read before the heredoc that wrote the temporary locations file.
- The user's scratchpad `.../scratchpad/s7/` for temporary files and logs.

## Unread material

- `process-audit/audit_count.py`: read lines 1-600 and 1560-2017 whole; lines 600-1560 (the readers of the price list, register, cycles and the analysis) not read; I took the docstring, the writer and the tables from the parts read and the real result.
- `foundation-review/SKILL.md`, `instruction-files/SKILL.md`, `kind_skill.md`, `writing.md`, `project-level/backlog_place.md`, `process-audit/problem_register.md`, `process-audit/price_list.md`, the reports of slices 3, 5, 5 fix, 6 and the correction, the task passages `15-70` and `76-115`, and WAY-103, 107, 113, 127, 140, 256, 265, 320, 329, 330, 331, 334, 335, 338, 339, 340, `glossary.md` human action, the two invariants: read whole.
- `instruction-files/tool_loading.md`, `judging.md`, `changing.md`, `placing.md`, `kind_main_file.md`, `kind_path_rule.md`: not read; no mode of them applies to writing a skill beyond `kind_skill.md`.
- `.runs/task-cycles/weekly-process-audit/plan.md` and `price_list`: not read beyond the handoff's copy and the file above.

## Searches not found or unclear

- Foundation entry row 2 (WAY-330) and the plan's Foundation entries rows for WAY-09, WAY-38, WAY-89: not needed beyond the handoff's copy; nothing unclear.
- The plan's "WAY-3xx" numbers are two out of date; I cited the log's numbers (WAY-329, 331, 334, 335, 338, 339, 340).
- Whether the user's own rule for putting material before the human has a name a skill may use: the orchestrator said not to name it; I wrote it in the skill's own words (rows quoted, what follows, one question).

# Author report: settle-technology in the shape of WAY-256

**Status:** done with concerns (the concerns are listed under "Concerns"; none blocks the review).

**Commit:** `c2e70f9` (`mariusznn@gmail.com`, the private address), on `task/technology-skill-shape`, base `525cde1`. Worktree clean after it.

Variant: the whole change as the one author. Not pushed, no request opened, full gate not run, return step not started.

## Files changed

All in `project-level/technology/`; 7 files, +203 and -132 lines.

| File | Lines | Words | What it is |
|---|---|---:|---|
| `SKILL.md` | +17 -132 | 468 | picture of the whole, location, the rule that the step writes into the definition only, the report name rule, a pointer for each step, the re-gate sentence |
| `start.md` | +24 | 293 | step 0, Start or resume |
| `list.md` | +30 | 373 | step 1, List the choices (without the look) |
| `running_product.md` | +15 | 178 | the look at the logs, the interface and the development data |
| `settle.md` | +69 | 886 | step 2 as the leader does it: waves, critique, show, choose, write |
| `research.md` | +37 | 446 | the research agent's work (old 2.1 from "Each finds", 2.2, 2.3), alone readable |
| `close.md` | +11 | 102 | step 3, Close |

The description line is unchanged, so the generated entry points stay current. No Python and no other tracked file changed. The foundation step: the task carries no *Settlements to record* (`none`), so nothing is written; `task-cycle/skill/foundation_step.md` was read.

## Checks (command, exit code)

Run from the worktree. Scripts and their outputs lie under `.runs/task-cycles/technology-skill-shape/checks/` (not tracked).

| Check | Command | Exit | Result |
|---|---|---:|---|
| rule preservation | `python -B .runs/task-cycles/technology-skill-shape/checks/preservation.py .runs/task-cycles/technology-skill-shape/checks/preservation_result.txt` | 0 | 71 pieces of the old text: 51 stand word for word in the new files, 20 are listed with their exact new wording in `checks/make_changes.py` (each found in the new files), 0 problems |
| preservation, negative control | same, after changing `never choose alone` to `choose alone` in `settle.md` (restored) | 1 | 1 problem reported, so the check fails when a sentence changes |
| reach on the five routes | `python -B .runs/task-cycles/technology-skill-shape/checks/reach.py .runs/task-cycles/technology-skill-shape/checks/reach_result.txt` | 0 | 77 assertions, 0 failed |
| reach, negative control | same, after replacing `running_product.md` by `XX.md` in `start.md` (restored) | 1 | the two resuming routes fail, as they should |
| word counts | `python -B .runs/task-cycles/technology-skill-shape/checks/make_counts_report.py .runs/task-cycles/technology-skill-shape/reports/word-counts.md` | 0 | see `word-counts.md` |
| assessment | `python -B .runs/task-cycles/technology-skill-shape/checks/make_assessment.py .runs/task-cycles/technology-skill-shape/reports/assessment.md .runs/task-cycles/technology-skill-shape/checks/assessment_template.md` | 0 | 37 rows; every one of the 156 non-blank lines of the old file is in a row |
| entry points | `python -B agent-instructions/skill_entry_points.py` | 0 | `entry points are current` |
| instruction check | `python -B instruction-files/check_instructions.py .` | 0 | 0 error, 1 warn (`dead-path AGENTS.md:21 _zadania\`, unchanged file), 3 info |
| tests of `project-level` | `python -B gate/run_tests.py project-level` | 0 | 267 tests OK (run twice, before and after the last edit of `research.md`) |
| tests of `agent-instructions` | `python -B gate/run_tests.py agent-instructions` | 0 | 18 tests OK |
| tests of `instruction-files` | `python -B gate/run_tests.py instruction-files` | 0 | 104 tests OK, 5 skipped |
| line endings | `python -c` counting `\r` bytes in the seven files | 0 | 0 in each (the Write tool wrote CRLF, converted to LF with `sed -i 's/\r$//'` before the commit) |

Not run: `python -B gate/run_tests.py` over all directories (the orchestrator's). No test was written first: the change is prose, no behaviour of code changes, and no invariant's test changed.

What the checks do not show: how an agent behaves with the new files. They show that text is preserved and reachable, not that an agent follows the pointers (task question 4).

## The own-work check (section 3 of the method)

Requirement most likely unmet: acceptance criterion 1 and 3 together, that no rule is lost and each named case reaches a reader who really reads a file with it. Checks: `preservation.py` (every sentence-sized piece of the old file stands in the new files word for word or is listed with its exact new wording, and that wording is found) and `reach.py` (per route, the named fragments are in files that route reads). Both passed on the first full run after the listing was complete; a first run of `preservation.py` listed 25 unmatched pieces, which were headings glued to sentences (script bug, fixed by dropping headings) and 20 real rewordings, which I listed by hand; `reach.py` first reported 3 failures that were my script counting `definition_template.md` as a file beside the skill (fixed). Both scripts fail on their negative control.

Walked by hand:

- A resumed leader that skips "List the choices": reads `SKILL.md`, which gives it the report name rule (`.runs/technology/<choice>.md`, `SKILL.md`), the foundation rule and the step 0 pointer; reads `start.md`; with a list written, `SKILL.md` step 0 and the bullet of `start.md` both send it to `running_product.md` for the look; adds an item and reads `list.md` to show the list. With an open item it reads `settle.md`; the critique instruction is named at sub-steps 4 and 5 and in `SKILL.md` step 2, so a resume in which every report already reads `critique: passed` still reads it at "Show". With no open item, it goes to `close.md` and never reads the critique instruction.
- The research agent with its file alone: `research.md` says where the-way and `definition_template.md` lie, what the leader gives, that the step writes into the definition only and never the product's foundation, what `(WAY-122)` is, the report name rule, and the meaning of "an agent's way to the running product". It names no wave, no critique line, no step number, no other file of the skill. The reach check asserts that none of those words occur in it.

## Searches not found or unclear

- Environment facts `single-rule-compliance`, `instruction-density-accuracy`, `claude-skill-nested-references`, the glossary, and the guidelines (empty selection) were not read as files: the handoff lists them, but their content is quoted in `instruction-files/SKILL.md` and in WAY-256 and WAY-258, which I read whole. If the review needs a glossary reading of a term, it was not done here.
- The Claude Code session records were not searched again; the task's Context states there is no invocation of the skill there.
- The text the leader gave its research agents in the Codex run is encrypted in the rollout; read from `brief.md:13` instead.
- No record shows an agent missing a rule of the skill (details in the assessment, section 2).
- The handoff says the task's Context line "Skrypt serii `skill_carry_cost.py` liczy każdy plik .md": I did not look for that script; it belongs to the next real use.

## Reach beyond the handoff

- `git log --follow` of the skill, `git show 2a8954e:project-level/technology/SKILL.md | grep` (the pinned text of the real run): why the report name has no ground in that run.
- `grep` in `project-level/readiness_check.py` and its tests for step numbers of this skill: none are named.
- `installation/install.py:20-60` and `installation/README.md:57`, `.claude/skills/the-way-settle-technology/SKILL.md`: the entry point and the list of skills.
- `elements/common/critique/{SKILL,prepare,check,settle}.md` word counts only (the author does not read them for the change).

## Choices (name, rejected way, cost if wrong)

1. **Files beside the skill and their names:** `start.md`, `list.md`, `running_product.md`, `settle.md`, `research.md`, `close.md`. Rejected: step 0, 1 and 3 left in `SKILL.md` (against question 7 of the task); one file for steps 0 and 1 (the look would have to be read whole by a resumed leader, together with the listing procedure). Cost if wrong: one file more or fewer to keep.
2. **The look in its own file, `running_product.md`,** with a one-instruction pointer in `list.md` and a bullet in `start.md`. It is needed on two ways of using the skill (a new list and any resume with a list), and acceptance criterion 3 asks that it reach both resumes. Rejected: the look inside `list.md` with resuming leaders reading `list.md` whole (about 370 words more on every resume). Cost if wrong: a seventh file.
3. **`list.md` is read on a resume only when the look adds an item** (it holds the naming rule and the way to show the list, which the resume sentence "show the list again as step 1 does" needs). `SKILL.md` step 0 says so. Rejected: reading it on every resume (+373 words on both resuming routes). Cost if wrong: a leader that adds an item without reading `list.md` names it badly; the pointer is in `start.md` at that bullet.
4. **The leader does not read `research.md`.** It gives the path to each agent; `SKILL.md` step 2 says so. Rejected: telling the leader to read it too (+446 words on the routes with open choices; question 3 of the task described the leader needing to rewrite rules or point to the leader's file, not to read the agent's). Cost if wrong: the leader cannot vouch for what it handed over.
5. **The report name rule stands in `SKILL.md` and in `research.md`** (also a sentence of the foundation rule, same two places). Rejected: one copy and a pointer: the research agent does not read `SKILL.md`, and the leader does not read `research.md`. Cost if wrong: two copies to keep in step (said in the assessment, section 4).
6. **The critique pointer is in `SKILL.md` step 2 and, with the path, at sub-steps 4 and 5 of `settle.md`.** Rejected: a bare "following `critique`" (reading would depend on the earlier text); the pointer in `start.md` (reads it at step 0, the thing To do 3 removes).
7. **Second person in `research.md`** (`Find`, `give`, `read off`, `say`, `write ... and end`) instead of "the agent finds". Rejected: third person with "the agent is you" (verbatim, but the reader has to translate). Cost: 9 rewordings, all listed in `checks/make_changes.py` and in the assessment.
8. **Gloss added in `research.md`:** the three matters (logs, interface, development data) after "an agent's way to the running product"; "A reference such as (WAY-122) names the decision of the-way that sets the rule beside it; you need not open it"; and the location sentences. These are the only new statements in it. They state no new rule.
9. **Stub items 2 and 3 in `settle.md`** (`Weigh`, `Consequences`: "The research agent's work, in `research.md`") keep the numbering that `settle.md` refers to (`sub-step 6`). Rejected: renumbering 1, 2, 3, 4. Cost: 30 words.
10. **Step numbers in the moved files are replaced by the step's name and file** ("the step "Close" (`close.md` beside this file)"), since a file read by its path alone has no numbering of the whole. Two numbers are left on purpose: `define-project step 5` (another skill's step, unchanged) and `its step 4.1` (a step of `record-decision` and the shared way of working).
11. **`definition_template.md` and `way_of_working.md` are named with their paths** (`project-level/definition_template.md`, `elements/common/way_of_working.md`) in the moved files. The intro of `SKILL.md` keeps the old `definition_template.md` plain name, as it stood.

The change of the list of what the leader gives the research agent (To do 2): the new last item is "the path of the file `research.md`, beside this file, which holds the agent's work". One more sentence in `settle.md` item 1, "The agent finds the options, weighs them, compares their consequences and writes the comparison to the choice's report", is connective text and states no rule. The change of the moment of reading (To do 3): the critique instruction leaves the reading of step 0 (`start.md`) and is read when the first critique comes (`SKILL.md` step 2; `settle.md` sub-steps 4 and 5).

## References named from elsewhere

All still read true after the change; none changed.

- `project-level/skill/SKILL.md:139` "Run `settle-technology` with this definition": true.
- `installation/README.md:57` lists `settle-technology` among the entry points: true, description unchanged.
- `elements/decisions/skill/projected.md:6` "for a technology choice `settle-technology` hands over": true (`settle.md` sub-step 7 hands each choice to `record-decision`).
- `project-level/definition_template.md` lines 104, 152, 243 and 300 (the skill "writes it", "leads that", "projects"): true.
- `installation/install.py:34` maps the name to `project-level/technology/SKILL.md`: the file still exists.
- The numbered steps of the old skill were named from no other file (searched in `readiness_check.py`, its tests, the template and the other skills).

## Concerns

1. **The leader with a new list and open choices reads 172 words more after the change** (6628 before, 6800 after; the other three leader routes read 297 to 1918 fewer, the research agent 1676 fewer). Cause: a pointer for every step in `SKILL.md` and a one-line introduction in each file, both of question 7 of the task; the research text no longer reaches the leader. Question 4 of the task expected "almost as much"; this is a little more. A shorter introduction line in each file would save about 90 words; I kept it so a file read by its path alone says whose step it is.
2. **Proposal 5.1 of the assessment, reading only the template sections the skill uses, saves 387 words, not about 800.** The task's figure of about 800 does not match the sections of the template at `525cde1`; the assessment gives the section list and bounds. Not recommended.
3. Two sentences stand twice on purpose (foundation rule, report name rule): `SKILL.md` and `research.md`.
4. The assessment's section 2 notes that the real run used text of 1335 words, older than the judged text, so it shows the behaviour of the agent only in part.

## Problems as observed

- The Write tool writes CRLF in this environment; the first `git diff` warned `CRLF will be replaced by LF` for `SKILL.md`. Converted before the commit and checked as above.
- Python's `pathlib.write_text` also writes CRLF on Windows; no tracked file was written that way after the conversion (the checks that read the files are line-ending independent).

## Reports for the request

- `.runs/task-cycles/technology-skill-shape/reports/assessment.md`: the table of To do 4 (37 rows, every non-blank line of the old file), the mechanical check, the records searched and three proposals (template reading, restated weighing rules, the preference question), each with the cost of leaving and of making it; the template-reading proposal is judged by `instruction-files/judging.md`.
- `.runs/task-cycles/technology-skill-shape/reports/word-counts.md`: the five routes before and after, file lists and the bounds of the sections.

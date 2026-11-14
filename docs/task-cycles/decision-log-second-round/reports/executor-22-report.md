# Report of executor 22

**Status:** done

**Commits:** `0a5bb91` — Remove the withdrawn decision numbers from the request template, the change skill files and the plan skill and give each rule its reason.

**Files changed** (added/removed lines from `git diff --stat`): `task-cycle/skill/request_template.md` (62 lines touched), `agent-instructions/README.md` (5), `task-cycle/change/SKILL.md` (4), `task-cycle/change/ui_check.md` (10), `task-cycle/plan/SKILL.md` (3); 48 insertions, 36 deletions in all.

## Checks

- `python -B elements/common/foundation_check.py` exit 1; its 8 lines name only `task-cycle/review/SKILL.md` (a file of a slice not yet made); none names a file of this slice's *Change*.
- `python -B gate/run_tests.py task-cycle` exit 0 (440 tests).
- `python -B gate/run_tests.py agent-instructions` exit 0 (25 tests).
- `python -B agent-instructions/skill_entry_points.py` exit 0 ("entry points are current").
- The full gate was not run (not in my section).

## Own-work check

Requirement most likely missed: a number of a withdrawn entry left behind in a place the line ranges of the base no longer match. Check: `grep -nE "WAY-(49|163|219|262|264|286|290|291|292|317|318|326|327|358|367)\b"` over the five files, exit 1 (no match). A second most likely miss: a full stop or space lost when a bracket was removed; one was found at step 2 of the template ("write what is missing" lost its full stop) and fixed before the commit; the diff was read whole after that.

## Reasons added (file, place, entry read at base `ec7929d`)

- `task-cycle/skill/request_template.md`, after the opening paragraph: "The skeleton puts the same thing in the same place in every request, so the human finds it without reading the rest." — WAY-286 *Rationale*.
- Same file, step 3 after "judges no content.": "The check runs before the request opens, since an agent writing from the template can lose or move a section or a group, and nobody would notice until the human reads the request; the content is left to the agent that writes it, since a script cannot judge whether it is complete and true." — WAY-290 *Rationale* (one sentence with a semicolon).
- Same file, "An error you hold wrong", item 1: "A cycle that corrected until the script passed would remove the block the human reads with nothing saying so, or would never open the request." — WAY-291 *Rationale*.
- Same file, "What you will see": "A screenshot is read at a glance in the description, while logs and outputs are read in the reports by the agents and the humans who check closely, where they already stand." — WAY-318 *Rationale*.
- Same file, end of the fifth-part bullet: "The steps stand in the item so that the human has them where the request asks the question, and does not have to ask the agent or look for them in the lower part." — WAY-327 *Rationale*.
- `task-cycle/change/SKILL.md`, own-work bullet: "since the passing rerun alone would hide the failure from the orchestrator, which relies on the report instead of rerunning focused checks" — WAY-262 *Rationale*.
- `task-cycle/change/ui_check.md`, first bullet: "States beyond the default are easy to omit, and looking at both the states and the screenshot catches different faults before review." — WAY-219 *Rationale*.
- `task-cycle/plan/SKILL.md`, after "*Change* names the command's source only when that slice changes it.": "Each such slice runs the command so that the files it generates stand present for that slice's review and the committed output agrees with its sources." — WAY-264 *Rationale*.

## Numbers removed, repointed

Removed with brackets: WAY-49 (2), 163, 219 (2 in template, 1 in ui_check), 262, 286 (4 in template, 1 in README), 290 (template, README), 291 (template, README), 317 (line 179 template, ui_check), 318 (template, ui_check), 326, 327 (3), 358, 367. Repointed: WAY-292 in "(WAY-288, WAY-292)" became "(WAY-288)"; item 13 "(WAY-317)" became "(WAY-316)" (WAY-316 as it stands holds the no-place paragraph, read at `foundations/decisions.md:7738`).

## Entries left under the "stay" rule

No number of the ten that stay (WAY-93, 94, 97, 263, 287, 294, 295, 297, 363, 364) was in a place my section changes except WAY-287 and WAY-295, which stayed as they were in the template (`WAY-287` in "(WAY-326, WAY-287)", "(WAY-287, WAY-358)" and the like; `WAY-295` in items 10, the variants table and *Checks*). Other numbers still in the five files (WAY-03, 12, 51, 114, 140, 150, 160, 161, 162, 164, 172, 213, 253, 255, 261, 269, 274, 288, 289, 300, 308, 309, 316, 319, and others) were not in my section and were left as they were.

## Findings and notes

- Rule coverage: every rule of my section is in its file; none needed an added sentence of the rule itself.
- The plan's section for WAY-327 line 15 and 344 and for WAY-317 line 179 asked only for removal; no reason was added there.
- A hook (rules-on-demand) refused the first commit call and asked to read the git rules; the commit was repeated unchanged after that.

## Reach beyond the dispatch

None. I read `foundations/decisions.md` only at the base entries and at WAY-316 and the entry list headings of WAY-03, 12, 51, 287, 288, 295 (to check they stay). Base copy of the log was written to `.runs/executor-22/base.md` for reading.

## Unread material

WAY-293 (`foundations/decisions.md:7171` as it stands) was named by the handoff's *Read* list and I did not read it: no removal or reason in my section depends on it. WAY-49, 163, 326, 358, 367 were not read at the base: my section only removes their numbers and adds no reason for them. WAY-292 and WAY-317 were read whole at the base.

## Searches not found or unclear

None.

## Working copies

`.runs/executor-22/`: `base.md` (the log at `ec7929d`) and `fc.txt` (output of the foundation check). Both removed before return.

"""Write assessment.md beside this script: the judgement of project-level/skill/SKILL.md at dfd50e5.

The quote of each row is taken from the base by its line range, so it is literal. The script stops
with exit code 1 when a nonblank line of the base stands in no row or in two, or when a unit of a
row's quote (a part between '. ' or '; ', whitespace normalised, list markers dropped) is missing
from the file its row names as the new place and is not one of the units reworded on purpose
(EXPECTED of compare_sentences.py). Prints only ASCII.
"""
import os
import re
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import compare_sentences as cs  # noqa: E402

REPO = cs.REPO
BASE = cs.BASE
NL = chr(10)
LINK = "https://github.com/mariusznazar/the-way/blob/" + BASE + "/project-level/skill/SKILL.md#L%d-L%d"
SEARCHED = ("Mistake: not found in the records searched (above the table).")

EVERY = "Every use: `SKILL.md` is read whole, by the entry points (WAY-127, WAY-259) and by an agent given its path."
NO_MOMENT = "No moment to recognise: it is read with `SKILL.md`, before step 0."
HELD = "No moment to recognise: a rule kept while working, and `SKILL.md`, which holds it, is read whole at the start."

ROWS = [
    (1, 4, "Every use: the description is how a human's request or an orchestrator's choice matches the skill, and the entry points are generated from it.",
     "No moment to recognise: Claude Code and Codex list the description in every session.",
     "KEEP. Carried: WAY-127, WAY-259 and the invariant `skill-entry-points`; the task leaves the description unchanged, so `skill_entry_points.py` reports the entry points current. " + SEARCHED,
     "`SKILL.md`, unchanged.", ["SKILL.md"]),
    (6, 14, EVERY + " It is the picture of the whole: the two steps the skill leads, the step it hands on, and where the form of a definition and the way of asking stand.",
     NO_MOMENT,
     "KEEP, with the last sentence's \"cited below\" made \"cited below and in the files beside this skill\" (fix of finding M-1): the decisions are now cited in the files beside too; and the template named by its path, `project-level/definition_template.md` (proposal 5, applied by correction 1, at the human's request on request #85). Carried: WAY-256 (`SKILL.md` keeps the picture of the whole) and WAY-35 (the form stands in the template, the way of asking in the shared part). " + SEARCHED,
     "`SKILL.md`, lines 6-15.", ["SKILL.md"]),
    (16, 20, "Every step that runs a script of the-way (`<the-way>/...`) or hands work to another skill: steps 5, 6 and 7, and step 0 for an approved definition.",
     HELD,
     "KEEP, with \"each skill named below\" made \"each skill named below or in the files beside this skill\" (fix of finding M-1; proposal 6 for the other skills of the series): `critique`, `find-foundation-entries`, `settle-technology` and `plan-project` are now named in the files beside. A rule of working across the steps (WAY-256). Carried: WAY-127 (where the-way lies; the prefix). " + SEARCHED,
     "`SKILL.md`, lines 17-21.", ["SKILL.md"]),
    (22, 23, "Every step: none writes the foundation; step 5 and step 7 come nearest, writing projected entries.",
     HELD,
     "KEEP. A rule of working across the steps. Carried: WAY-106. " + SEARCHED,
     "`SKILL.md`, unchanged.", ["SKILL.md"]),
    (25, 25, "A turn `lead-project` dispatches; the dispatches name this section.",
     "Yes: the orchestrators' dispatches name the section \"Delegated definition change and gate\" and step 7 (task, Context).",
     "KEEP in `SKILL.md`, above the pointer to the variant's file (task To do 2). " + SEARCHED,
     "`SKILL.md`, unchanged heading.", ["SKILL.md"]),
    (27, 34, "Only a turn `lead-project` dispatches through a refinement conversation path (one variant).",
     "Yes: the dispatch names the section and a conversation file; the pointer keeps the condition of the base's first sentence word for word (\"When `lead-project` dispatches a definition edit or step 7 through a refinement conversation path\").",
     "MOVE to the variant's file, word for word (task question 2); the first sentence's condition stays in `SKILL.md` as the condition of the pointer. Ground: cost, the variant leaves the text of every other use; carried WAY-156. " + SEARCHED,
     "`delegated_mode.md`, lines 6-13, after an orientation line (fix of finding M-2); pointer `SKILL.md` section \"Delegated definition change and gate\".", ["delegated_mode.md"]),
    (36, 40, "The dispatched turn, before and at step 7.3. The first sentence (the orchestrator's own edit) is the orchestrator's rule, which the dispatched agent does not act on.",
     "Yes, as the row above.",
     "MOVE to the variant's file, word for word, except the first sentence: REMOVE it, the orchestrator's own rule, which `project-level/lead/skill/SKILL.md:206-207` and WAY-156 hold (proposal 1, applied by correction 1, at the human's request on request #85). Carried: WAY-156, WAY-120. " + SEARCHED,
     "`delegated_mode.md`, lines 15-17, the first sentence removed; the 7.3 limb also in `readiness_gate.md` lines 6-9.", ["delegated_mode.md"]),
    (41, 45, "The dispatched turn, at steps 7.3 and 7.4.",
     "Yes, as the rows above; at step 7 the agent meets `readiness_gate.md`'s sentence for a dispatched turn, which names this file.",
     "MOVE to the variant's file, word for word but \"blocks the gate\" read \"blocks the readiness gate\" (proposal 4, applied inside this skill by correction 1, at the human's request on request #85). Reaches step 7 through the opening sentence of `readiness_gate.md` (task criterion 4). Carried: WAY-156, WAY-118. " + SEARCHED,
     "`delegated_mode.md`, lines 17-22; the approval limb also in `readiness_gate.md` lines 6-9.", ["delegated_mode.md"]),
    (47, 51, "The dispatched turn, while the readiness gate is pending and at its end.",
     "Yes, as the rows above.",
     "MOVE to the variant's file, word for word but \"the pending gate\" and \"that gate\" read with \"readiness gate\" (proposal 4, applied inside this skill by correction 1, at the human's request on request #85). Repeats `project-level/lead/skill/SKILL.md:214-218` in part; kept (proposal 2). Carried: WAY-156. " + SEARCHED,
     "`delegated_mode.md`, lines 24-28.", ["delegated_mode.md"]),
    (53, 53, EVERY, NO_MOMENT,
     "KEEP: the heading of the step every use begins with. " + SEARCHED,
     "`SKILL.md`, unchanged.", ["SKILL.md"]),
    (55, 56, "Step 0, every use.",
     "Yes: step 0 is where every use begins.",
     "KEEP in `SKILL.md`: one instruction of step 0, which a pointer would only replace (WAY-256), with the template named by its path, `project-level/definition_template.md` (proposal 5, applied by correction 1, at the human's request on request #85). The template is still read in full at step 0 (task question 1). Carried: WAY-113 (\"How a skill asks\"). " + SEARCHED,
     "`SKILL.md` step 0.", ["SKILL.md"]),
    (57, 63, "Step 0, where an existing definition is named: routes 2 to 5 of question 4 and the dispatched turn.",
     "Yes: the agent knows whether a definition was named. The base's condition \"When the human names an existing definition\" becomes the pointer's, with \"in a dispatched turn, the definition its conversation file names\" added (see the report, conditions compared).",
     "MOVE to the variant file of step 0; the jumps to steps 5, 6 and 7 name those steps' files, and \"after the gate\" reads \"after the readiness gate\" (proposal 4, applied inside this skill by correction 1, at the human's request on request #85). Carried: WAY-112 (resume from the status line), WAY-118 (a changed approved definition goes through the gate again). " + SEARCHED,
     "`existing_definition.md`, lines 6-12; pointer `SKILL.md` step 0.", ["existing_definition.md"]),
    (64, 70, "Step 0, an existing definition with no `## Technology` section (route 5).",
     "Yes: once the definition is read whole, the missing heading shows; the readiness check reports it too.",
     "MOVE to the variant file of step 0, word for word but \"through the gate again\" read \"through the readiness gate again\" (proposal 4, applied inside this skill by correction 1, at the human's request on request #85); \"go on at step 6\" names `technology.md`. Carried: WAY-121, WAY-118. " + SEARCHED,
     "`existing_definition.md`, lines 13-19.", ["existing_definition.md"]),
    (71, 71, "Step 0, a new definition.",
     "Yes: the agent knows that no definition was named.",
     "KEEP in `SKILL.md`: one instruction. " + SEARCHED,
     "`SKILL.md` step 0, unchanged.", ["SKILL.md"]),
    (73, 73, "Step 1; no file names it by number.", "Yes.",
     "KEEP the heading in `SKILL.md`, with the pointer to the step's file. " + SEARCHED,
     "`SKILL.md` step 1.", ["SKILL.md"]),
    (75, 75, "Step 1 only: a definition from an idea (route 1).",
     "Yes: the human brings the idea at the start.",
     "MOVE to the file of step 1. Ground: the step of the activity this skill leads. " + SEARCHED,
     "`idea.md`, line 5.", ["idea.md"]),
    (76, 77, "Step 1 only.", "Yes.",
     "MOVE to the file of step 1. Ground: the step of the activity. " + SEARCHED,
     "`idea.md`, lines 6-7.", ["idea.md"]),
    (78, 79, "Step 1 only, before the first write.", "Yes.",
     "MOVE to the file of step 1. Carried: WAY-112 (the goal confirmed before the first write). " + SEARCHED,
     "`idea.md`, lines 8-9.", ["idea.md"]),
    (80, 80, "Every step that asks the human or writes the definition: steps 0 (the question on reopening), 1 to 7 and the dispatched turn (task criterion 5).",
     HELD,
     "MOVE, word for word, to \"Rules that hold across the steps\" in `SKILL.md`: a rule of working some steps need stays in `SKILL.md` (WAY-256). Repeats the rule of language of `definition_template.md:31-34`, read whole at step 0; kept (proposal 3, row a). " + SEARCHED,
     "`SKILL.md` \"Rules that hold across the steps\", first item.", ["SKILL.md"]),
    (82, 82, "Step 2; no file names it by number.", "Yes.",
     "KEEP the heading in `SKILL.md`, with the pointer. " + SEARCHED,
     "`SKILL.md` step 2.", ["SKILL.md"]),
    (84, 86, "Step 2 only (route 1).", "Yes: step 2 follows the confirmed understanding.",
     "MOVE to the file of step 2. Carried: WAY-111, WAY-150. " + SEARCHED,
     "`read_foundation.md`, lines 5-7.", ["read_foundation.md"]),
    (87, 89, "Step 2 only.", "Yes.",
     "MOVE to the file of step 2. Carried: WAY-111, WAY-30. " + SEARCHED,
     "`read_foundation.md`, lines 8-10.", ["read_foundation.md"]),
    (90, 90, "Step 2 only, a product with an empty foundation.", "Yes: the selection finds nothing.",
     "MOVE to the file of step 2. " + SEARCHED,
     "`read_foundation.md`, line 11.", ["read_foundation.md"]),
    (92, 92, "Step 3; no file names it by number.", "Yes.",
     "KEEP the heading in `SKILL.md`, with the pointer. " + SEARCHED,
     "`SKILL.md` step 3.", ["SKILL.md"]),
    (94, 96, "Step 3 only.", "Yes: the goal is confirmed and the file has to be written somewhere.",
     "MOVE to the file of step 3. Repeats where the template keeps the place (`definition_template.md:19-30`) only as a pointer; kept (proposal 3, row b). " + SEARCHED,
     "`first_write.md`, lines 5-7.", ["first_write.md"]),
    (97, 100, "Step 3 only.", "Yes.",
     "MOVE to the file of step 3. Carried: WAY-112. " + SEARCHED,
     "`first_write.md`, lines 8-11.", ["first_write.md"]),
    (102, 102, "Step 4; no file names it by number, and step 7.1 sends findings back to it.", "Yes.",
     "KEEP the heading in `SKILL.md`, with the pointer. " + SEARCHED,
     "`SKILL.md` step 4.", ["SKILL.md"]),
    (104, 105, "Step 4 only.", "Yes.",
     "MOVE to the file of step 4. Carried: WAY-112 (the largest gaps first). " + SEARCHED,
     "`rounds.md`, lines 5-6.", ["rounds.md"]),
    (106, 108, "Every step that changes the definition after its first write: steps 4 to 7, the existing definition resumed and the dispatched turn (task criterion 5).",
     HELD,
     "MOVE to \"Rules that hold across the steps\" in `SKILL.md`, opened by \"Once the definition is written (step 3),\" and \"into the definition\" read \"into it\" (see the report, new sentences). Carried: WAY-112. " + SEARCHED,
     "`SKILL.md` \"Rules that hold across the steps\", third item.", ["SKILL.md"]),
    (109, 109, "Step 4 only: Background, Success and Risks are asked in the rounds.", "Yes.",
     "MOVE to the file of step 4. Repeats `definition_template.md:110-112`; kept (proposal 3, row d). Carried: WAY-109. " + SEARCHED,
     "`rounds.md`, line 7.", ["rounds.md"]),
    (110, 111, "Step 4 only.", "Yes.",
     "MOVE to the file of step 4, \"Three moves\" read \"Two moves\": its third move stands in `SKILL.md` (row of line 117). Carried: WAY-112. " + SEARCHED,
     "`rounds.md`, lines 8-9.", ["rounds.md"]),
    (112, 113, "Step 4 only (\"through the rounds\").", "Yes.",
     "MOVE to the file of step 4. Carried: WAY-112. " + SEARCHED,
     "`rounds.md`, lines 10-11.", ["rounds.md"]),
    (114, 116, "Step 4 only (\"through the rounds\").", "Yes.",
     "MOVE to the file of step 4. Carried: WAY-112. " + SEARCHED,
     "`rounds.md`, lines 12-14.", ["rounds.md"]),
    (117, 117, "Every step that asks the human or writes the definition (task criterion 5).",
     HELD,
     "MOVE to \"Rules that hold across the steps\" in `SKILL.md`, capitalised as an item of its own, with WAY-112 cited beside it. Carried: WAY-112 (\"reads what product files can answer\"). " + SEARCHED,
     "`SKILL.md` \"Rules that hold across the steps\", second item.", ["SKILL.md"]),
    (118, 118, "Step 4, where the rounds ask about inputs and constraints.", "Yes.",
     "MOVE to the file of step 4. Points to `definition_template.md:117-120`; kept (proposal 3, row e). Carried: WAY-110. " + SEARCHED,
     "`rounds.md`, line 15.", ["rounds.md"]),
    (119, 120, "Step 4 only.", "Yes: an answer binds beyond the project.",
     "MOVE to the file of step 4. " + SEARCHED,
     "`rounds.md`, lines 16-17.", ["rounds.md"]),
    (121, 122, "Step 4 only.", "Yes.",
     "MOVE to the file of step 4. Carried: WAY-121. " + SEARCHED,
     "`rounds.md`, lines 18-19.", ["rounds.md"]),
    (123, 123, "Step 4 only.", "Yes.",
     "MOVE to the file of step 4. Points to `definition_template.md:122-130`. " + SEARCHED,
     "`rounds.md`, line 20.", ["rounds.md"]),
    (124, 125, "Step 4, at its end.", "Yes: the readiness check and the definition show which sections hold `TODO`.",
     "MOVE to the file of step 4. " + SEARCHED,
     "`rounds.md`, lines 21-22.", ["rounds.md"]),
    (127, 127, "Step 5; `project-level/technology/start.md:8` returns to \"`define-project` step 5\".", "Yes: the heading carries the number.",
     "KEEP the heading in `SKILL.md`, with the pointer (task To do 2). " + SEARCHED,
     "`SKILL.md` step 5.", ["SKILL.md"]),
    (129, 131, "Step 5 only (routes 1 and 2).", "Yes.",
     "MOVE to the file of step 5. " + SEARCHED,
     "`find_entries.md`, lines 5-7.", ["find_entries.md"]),
    (132, 133, "Step 5 only.", "Yes.",
     "MOVE to the file of step 5. Repeats `definition_template.md:332-333`, adding \"ask for none\"; kept (proposal 3, row g). " + SEARCHED,
     "`find_entries.md`, lines 8-9.", ["find_entries.md"]),
    (134, 134, "Step 5 only.", "Yes.",
     "MOVE to the file of step 5. Carried: WAY-121. " + SEARCHED,
     "`find_entries.md`, line 10.", ["find_entries.md"]),
    (135, 135, "Step 5, at its end.", "Yes.",
     "MOVE to the file of step 5. " + SEARCHED,
     "`find_entries.md`, line 11.", ["find_entries.md"]),
    (137, 137, "Step 6; `project-level/technology/close.md:10-11` returns to `define-project`, a finding of the readiness check \"to `define-project`, which names where\".", "Yes.",
     "KEEP the heading in `SKILL.md`, with the pointer to `technology.md` and, for a finding of the readiness check at this step, to `readiness_gate.md`, whose 7.1 names where (fix of finding I-1). " + SEARCHED,
     "`SKILL.md` step 6.", ["SKILL.md"]),
    (139, 140, "Step 6 only (routes 1, 2 and 5).", "Yes.",
     "MOVE to the file of step 6: with the next item, two instructions, so no exception of one instruction. Carried: WAY-121. " + SEARCHED,
     "`technology.md`, lines 5-6.", ["technology.md"]),
    (141, 143, "Step 6, when `settle-technology` returns.", "Yes: `project-level/technology/close.md` returns the agent to `define-project`, which sets `ready for gate`.",
     "MOVE to the file of step 6. Repeats the status table of `definition_template.md:80` as a pointer; kept (proposal 3, row h). " + SEARCHED,
     "`technology.md`, lines 7-9.", ["technology.md"]),
    (145, 145, "Step 7; named by number in `project-level/lead/skill/SKILL.md:208`, `project-level/plan/skill/existing_plan.md:9` and the orchestrators' dispatches (\"step 7.3\").",
     "Yes: the heading carries the number a dispatch or a critic's rules name.",
     "KEEP the heading in `SKILL.md`, with the pointer to the step's file, not read again where step 6 had it read, and to the variant's file (WAY-265; task To do 2, question 3). " + SEARCHED,
     "`SKILL.md` step 7.", ["SKILL.md"]),
    (147, 151, "Step 7.1 and again at 7.4; also step 6, where the readiness check that `technology.md` runs, or `settle-technology` hands back, reports a finding (`project-level/technology/close.md:6-10`).", "Yes: a finding of the check is the moment, at step 6 as at step 7.",
     "MOVE to the file of step 7, which `SKILL.md` names at step 6 for a finding and at step 7 unless step 6 had it read (WAY-256, text two steps consult; fix of finding I-1); each finding sent back to step 4, 5 or 6 names that step's file (task criterion 5). Carried: WAY-118 (the gate blocks). " + SEARCHED,
     "`readiness_gate.md`, item 1 (lines 11-16).", ["readiness_gate.md"]),
    (152, 162, "Step 7.2.", "Yes.",
     "MOVE to the file of step 7, word for word but \"the gate\" read \"the readiness gate\" twice (proposal 4, applied inside this skill by correction 1, at the human's request on request #85). Carried: WAY-118 (the one search of the whole foundation). " + SEARCHED,
     "`readiness_gate.md`, item 2 (lines 17-27).", ["readiness_gate.md"]),
    (163, 171, "Step 7.3. In a dispatched turn the variant changes it: the critique is requested through the conversation and the list reaches the human through the orchestrator.",
     "Yes; in a dispatched turn, the opening sentence of `readiness_gate.md` names the change and the variant's file.",
     "MOVE to the file of step 7, word for word. Carried: WAY-120, WAY-114. " + SEARCHED,
     "`readiness_gate.md`, item 3 (lines 28-36).", ["readiness_gate.md"]),
    (172, 176, "Step 7.4. In a dispatched turn the variant has the agent wait for the approval the orchestrator records.",
     "Yes, as the row above.",
     "MOVE to the file of step 7, word for word. Its last sentence repeats `definition_template.md:335-336`; kept (proposal 3, row i). Carried: WAY-118. " + SEARCHED,
     "`readiness_gate.md`, item 4 (lines 37-41).", ["readiness_gate.md"]),
    (177, 180, "Step 7.5.", "Yes.",
     "MOVE to the file of step 7, word for word. Carried: WAY-142. " + SEARCHED,
     "`readiness_gate.md`, item 5 (lines 42-45).", ["readiness_gate.md"]),
    (182, 183, "Step 0 (an approved definition that changed), the dispatched turn, and every step that changes an approved definition (task criterion 5).",
     HELD,
     "MOVE to \"Rules that hold across the steps\" in `SKILL.md`, word for word but \"the gate\" read \"the readiness gate\" twice (proposal 4, applied inside this skill by correction 1, at the human's request on request #85). Also stated by `definition_template.md:359-362` and, for step 0, by the base's lines 62-63; kept (proposal 3, row j). Carried: WAY-118. " + SEARCHED,
     "`SKILL.md` \"Rules that hold across the steps\", fourth item.", ["SKILL.md"]),
]

HEADER = """# Assessment of project-level/skill/SKILL.md at dfd50e5

Judged by the skill `instruction-files` in the mode judge, with the file of the kind skill
(`instruction-files/SKILL.md`, `judging.md`, `kind_skill.md`, `tool_loading.md`). Tools in use:
Claude Code and Codex, through the project entry points `.claude/skills/the-way-define-project/` and
`.agents/skills/the-way-define-project/` in the-way and the installed ones in a product; Cursor
through the shared layout. Sessions start in the-way's checkout or worktree, or in a product that
pins the-way (`loop2` is the one whose runs the task's Context records). The base is commit
dfd50e5 (`project-level/skill/SKILL.md` is identical at 2754675, the cycle's base). The permalink
of each range is `https://github.com/mariusznazar/the-way/blob/dfd50e513c09bebe9d09d74209cd28612565da83/project-level/skill/SKILL.md#L<a>-L<b>`.
In a quote the line breaks are shown as `<br>`; every nonblank line of the file stands in exactly
one row, which `make_assessment.py` beside this file checks, together with the new place of each
row. Line numbers of the files after the rebuild are those of the head of the task branch after
correction 1.

## 1. The check script

- Command: `python -B instruction-files/check_instructions.py . --file <each of the ten files of
  project-level/skill/>` in the worktree; exit code 0; `0 error, 1 warn, 12 info`.
- `WARN dead-path AGENTS.md:21` - the root `AGENTS.md` names `_zadania\\`, a folder of the author's
  private notes. Claude Code, Codex and Cursor all load the root `AGENTS.md`, so in each an agent
  that cannot open the folder asks the human, as the file says. It stands on the base, unchanged.
- On the base, `INFO dead-path project-level/skill/SKILL.md:13` and `:55` (the base file checked from
  a copy of its tree): `definition_template.md` is a name relative to a place the sentence gives.
  After correction 1 (proposal 5) the skill names `project-level/definition_template.md` and the
  script reports no such line.
- `INFO size` lines: `AGENTS.md`, `CLAUDE.md`, `agent-instructions/README.md`, and each new file
  beside the skill. None says that something was not read or not checked.

## 2. The table

Records searched for the mistakes the fragments are kept for: the git history of the file
(`git log --follow`, 14 commits), the remarks of PRs #16, #19, #23, #35, #69 and #82 (`gh pr view
<n> --comments` and the review comments, searched for `define-project` and the file's path; only
PR #69 holds hits, all quoting `plan-project`'s table), and the task's Context. No mistake of an
agent working by this skill was found in them; the ground of each verdict is therefore the decision
or step it carries, or its cost.

Columns: *Needed* is when an agent needs the fragment; *Recognised* is whether an agent recognises
that moment when it comes (WAY-257); the verdict is keep, move, remove or reword, with its reason
and ground; *New place* is where the fragment stands after the rebuild. The rebuild applied no
verdict that changes what a rule says; the verdicts \"remove\" and \"reword\" that would change it
stand as proposals after the table (task To do 6). At the human's request on request #85
(correction 1), proposals 1, 5 and 6 are applied, and proposal 4 inside this skill only; the rows
they touch say so.

| Fragment | Needed | Recognised | Verdict, reason, ground | New place |
|---|---|---|---|---|
"""


def main():
    base = subprocess.run(["git", "-C", REPO, "show", BASE + ":project-level/skill/SKILL.md"],
                          capture_output=True, check=True).stdout.decode("utf-8")
    lines = base.split(NL)
    if lines and lines[-1] == "":
        lines = lines[:-1]
    errors = []
    seen = {}
    for a, b, *_ in ROWS:
        for i in range(a, b + 1):
            seen.setdefault(i, []).append((a, b))
    for i, ln in enumerate(lines, 1):
        if ln.strip() and len(seen.get(i, [])) != 1:
            errors.append("line %d stands in %d rows" % (i, len(seen.get(i, []))))
        if not ln.strip() and i in seen and (i == seen[i][0][0] or i == seen[i][0][1]):
            errors.append("row %s opens or ends on a blank line" % (seen[i][0],))
    files = {}
    for a, b, needed, rec, verdict, place, targets in ROWS:
        quote = NL.join(lines[a - 1:b])
        for t in targets:
            if t not in files:
                with open(REPO + "/project-level/skill/" + t, encoding="utf-8", newline="") as f:
                    files[t] = cs.norm(" ".join(cs.ITEM.sub("", x) for x in f.read().split(NL)))
        for u in cs.units(quote if a > 1 else "---" + NL + "x" + NL + "---" + NL + quote):
            if u in cs.EXPECTED:
                continue
            if not any(u in files[t] for t in targets):
                errors.append("L%d-L%d: unit not in %s: %s" % (a, b, targets, u[:60]))
    out = [HEADER.rstrip(NL)]
    for a, b, needed, rec, verdict, place, targets in ROWS:
        quote = "<br>".join(lines[a - 1:b])
        out.append("| [`L%d-L%d`](%s)<br>%s | %s | %s | %s | %s |" % (
            a, b, LINK % (a, b), quote, needed, rec, verdict, place))
    out.append("")
    with open(os.path.join(HERE, "proposals.md"), encoding="utf-8", newline="") as f:
        out.append(f.read().rstrip(NL))
    out.append("")
    with open(os.path.join(HERE, "assessment.md"), "w", encoding="utf-8", newline=NL) as f:
        f.write(NL.join(out))
    print(len(ROWS), "rows;", len(errors), "errors")
    for e in errors:
        print("  ", e.encode("ascii", "replace").decode("ascii"))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

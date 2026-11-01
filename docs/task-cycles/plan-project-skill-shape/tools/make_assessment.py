"""Build reports/assessment.md: the judgement table of the base SKILL.md of plan-project.

Each quote is cut from the file at the base commit, so it is literal (line breaks shown as <br>);
coverage and overlap of the nonblank lines are checked before writing, and each row's declared
places are checked against the rebuilt files: every sentence of the quote that stands verbatim in
the rebuilt corpus must stand in a declared place.
"""
import re
import subprocess
import sys

REPO = "C:/Storage/repos/the-way/.runs/worktrees/plan-project-skill-shape"
BASE = "2f51e6c31f5911ac8a0292a80a4f599bd4bd0092"
PATH = "project-level/plan/skill/SKILL.md"
LINK = f"https://github.com/mariusznazar/the-way/blob/{BASE}/{PATH}"
DIR = "project-level/plan/skill/"
NL = chr(10)
OUT = "C:/Storage/repos/the-way/.runs/worktrees/plan-project-skill-shape/.runs/task-cycles/plan-project-skill-shape/reports/assessment.md"

SRC = ("Records searched: the git history of the file (11 commits, `git log --follow`), the remarks of "
       "PRs #50, #52, #59, #60, #62 and #64 (`gh pr view <n> --comments`, grep for plan-project, "
       "the section names and the file path), the task's Context")
NOMIST = "Mistake: not found in the records searched (see above the table)."
EVERY = "Every use, from the first line; SKILL.md is read whole."
YES_WHOLE = "Yes - no moment to recognise: SKILL.md is read whole by every use."

# (start, end, needed, recognised, verdict+reason+ground, new place text, places)
ROWS = [
    (1, 4, EVERY + " The description is how the skill is matched; the entry points are generated from it.",
     "Yes - it is the way in itself.",
     "KEEP. Carried: WAY-127 and WAY-259 (the entry points read this file) and the invariant skill-entry-points. The description is unchanged, so `skill_entry_points.py --write` changes nothing. " + NOMIST,
     "`SKILL.md`, unchanged.", ["SKILL.md"]),
    (6, 12, EVERY + " The sentence 'The decisions that set its rules are cited below.' is an orientation line.",
     YES_WHOLE,
     "KEEP. The picture of the whole (WAY-256) and the statement that the form of a plan lives in the template and the way of asking in the shared part, so this skill restates neither (WAY-35). The last sentence is proposed for removal below (proposal 1). " + NOMIST,
     "`SKILL.md`, unchanged.", ["SKILL.md"]),
    (14, 18, EVERY + " It says where the files named in the steps lie; every step file uses `<the-way>` and the `the-way-` prefix defined here.",
     YES_WHOLE,
     "KEEP. A rule that holds across the steps: it defines `<the-way>` that the commands of steps 0, 1, 5 and 6 use, and the project-skill naming. Carried: WAY-127 and WAY-259 (an entry point reads the skill from the checkout the session works in). It also covers the files beside the skill, which are named by pointers that say 'beside this skill'. " + NOMIST,
     "`SKILL.md`, unchanged.", ["SKILL.md"]),
    (20, 21, "Every step: what the breakdown writes and never writes.",
     YES_WHOLE,
     "KEEP. A rule that holds across all the steps (the breakdown writes nothing in the foundation or the definition and no task document). Carried: WAY-106. " + NOMIST,
     "`SKILL.md`, unchanged.", ["SKILL.md"]),
    (23, 28, "Only a turn dispatched by `lead-project` through a refinement conversation path (11 of the 14 recorded uses); the opening sentence says what that turn reads first and that the workflow below is followed with the routing differences.",
     "Yes - the dispatch names the conversation file; the pointer in `SKILL.md` repeats the words 'dispatches you through a refinement conversation path'.",
     "MOVE the sentences of lines 25-28 whole and unchanged to `delegated_mode.md` (the sentence 'follow this workflow with these routing differences' is unchanged, task question 1). The heading 'Delegated work while leading a plan' stays in `SKILL.md` with one new pointer that names the file and the condition (WAY-256, WAY-265, the task's Context: orchestrators repeat the heading in their dispatches). Ground: a variant that only one kind of use needs, carried decision WAY-256; cost: 277 words of the file in the 3 uses that are not dispatched. " + NOMIST,
     "`delegated_mode.md` (the sentences); `SKILL.md` keeps the heading and the pointer.", ["delegated_mode.md"]),
    (30, 33, "Only a dispatched turn: while the turn edits the plan.", "Yes - same moment as the row above.",
     "MOVE to `delegated_mode.md`, unchanged. The file is read at the start of a dispatched turn, so the bullet is held at every step; it is a routing rule of the turn, not of one step. Carried: WAY-156. " + NOMIST,
     "`delegated_mode.md`, first bullet.", ["delegated_mode.md"]),
    (34, 37, "Only a dispatched turn: at every step where the workflow asks the human, which is step 5 and step 7 (handover) and the questions arising in steps 2-4.",
     "Yes for the turn; for the steps 5-7 files the opener of `write_and_check.md` and `hand_over.md` and the pointer in `SKILL.md` name this file at the step. Without them a delegated agent reading 'Ask the human' in step 5 would ask (the trap of a rule that holds on several steps).",
     "MOVE to `delegated_mode.md`, unchanged; it reaches steps 5 and 7 through the first sentence of `write_and_check.md` and of `hand_over.md` ('ask nothing of the human yourself', 'show the human nothing yourself') and through the pointers of steps 5-7 in `SKILL.md` (WAY-265). Carried: WAY-156, WAY-145. " + NOMIST,
     "`delegated_mode.md`, second bullet; reached at steps 5 and 7 by `write_and_check.md` and `hand_over.md`.", ["delegated_mode.md"]),
    (38, 40, "Only a dispatched turn, at step 6.",
     "Yes for the turn; at step 6 the first sentence of `critique_plan.md` ('do not run `critique` yourself') and the pointer of step 6 in `SKILL.md` name it.",
     "MOVE to `delegated_mode.md`, unchanged; it reaches step 6 through the first sentence of `critique_plan.md` and the pointer in `SKILL.md`. Without them a delegated agent reading 'Run `critique` once' would run it and start a child agent (the bullet before forbids). Carried: WAY-156, WAY-120. " + NOMIST,
     "`delegated_mode.md`, third bullet; reached at step 6 by `critique_plan.md`.", ["delegated_mode.md"]),
    (41, 46, "Only a dispatched turn that rechecks the plan after the definition's new gate; it starts at step 0 and completes all affected steps.",
     "Yes - the dispatch says the plan is rechecked against the newly approved definition.",
     "MOVE to `delegated_mode.md`, unchanged. Its condition 'start at step 0' relies on step 0 reaching the existing-plan file for such a turn: see the row for lines 52-58. Carried: WAY-156. " + NOMIST,
     "`delegated_mode.md`, fourth bullet.", ["delegated_mode.md"]),
    (48, 51, "Step 0 in every use: the template and the way of asking are read in full before anything is done.",
     YES_WHOLE,
     "KEEP in `SKILL.md`, with the step 0 heading. Two reads of one instruction each, needed by every use (the template: 1881 words; 'How a skill asks'); a file of their own would trade one instruction for one pointer (WAY-256, the exception). Carried: WAY-35. " + NOMIST,
     "`SKILL.md`, step 0, first bullet.", ["SKILL.md"]),
    (52, 58, "Step 0 only when an existing plan is named: a plan to resume, to correct or to recheck.",
     "Yes for a human who names a plan; for a dispatched turn the plan is named by its conversation file, so the pointer in `SKILL.md` says 'by the human or in a dispatched turn by its conversation file' (see the note below the table).",
     "MOVE to `existing_plan.md`; the pointer in `SKILL.md` names the file with the condition. Rewordings in this row, each meaning-preserving: 'read it by \"Reading the definition and plan\" below' became a pointer to `reading_definition_and_plan.md`; the single bullet is split into a paragraph and bullets. The condition of the pointer is widened in words from 'the human names an existing plan' to 'an existing plan is named, by the human or in a dispatched turn by its conversation file': in the base a dispatched turn applied this bullet by the section 'Delegated work' (its bullets 1 and 4 presuppose an existing plan and a step 0 recheck), so the selection is the same; the reviewer is asked to confirm it. Ground: a variant (resume, correction or recheck) that a fresh breakdown does not need (1 of the 14 recorded uses was one); cost: 185 words of the file (WAY-256). " + NOMIST,
     "`existing_plan.md`; the pointer, with the condition, in `SKILL.md` step 0.", ["existing_plan.md"]),
    (59, 61, "Step 0 when `plan_check.py` reports two tasks realizing one entry with no order; also step 3 (settling) and step 7 (the plan check again, and showing the items).",
     "Yes - the report of the script names the pair.",
     "MOVE to `existing_plan.md`, with pointers to `assign_entries.md` and `hand_over.md` added in the sentence ('as step 3 gives it (`assign_entries.md` beside this skill)'). The same finding is now also stated in `assign_entries.md` (last bullet) and `hand_over.md` (second bullet), so a session that comes to step 3 or step 7 without the file of step 0 has it (task acceptance; the trap of a fragment needed at several places). Line 59 opens with the end of the previous sentence ('rather than reopen the same gate.'), which is in the previous row. Carried: WAY-230, WAY-146. " + NOMIST,
     "`existing_plan.md` (third bullet); `assign_entries.md` (last bullet); `hand_over.md` (second bullet).", ["existing_plan.md", "assign_entries.md", "hand_over.md"]),
    (62, 62, "Step 0, every use that names no existing plan.", YES_WHOLE,
     "KEEP in `SKILL.md`, step 0. One instruction; the pointer replaces nothing. " + NOMIST,
     "`SKILL.md`, step 0, third bullet.", ["SKILL.md"]),
    (64, 69, "Step 1, and a session working on an existing plan before it goes on (question 3).",
     "Yes - the step heading and its pointer; for an existing plan the last bullet of `existing_plan.md`.",
     "MOVE to `read.md`; the heading stays in `SKILL.md` with a pointer. The reference 'by \"Reading the definition and plan\" below' is reworded to a pointer to `reading_definition_and_plan.md` (meaning-preserving). Ground: a step's procedure (WAY-256); WAY-151 is cited. " + NOMIST,
     "`read.md`; the pointer in `SKILL.md` step 1.", ["read.md"]),
    (70, 77, "Step 1 (reading the foundation, the product's files, the guidelines).",
     "Yes - same as the row above.",
     "MOVE to `read.md`. Carried: WAY-150, WAY-218, WAY-214 (through `product-guidelines/reading.md`). The sentence 'keep what it finds missing or uncertain in the working evidence' is the moment that selects `guideline_tasks.md` at step 2; the condition in `SKILL.md` step 2 says 'the reading ... in step 1 found ... missing or uncertain'. " + NOMIST,
     "`read.md`.", ["read.md"]),
    (79, 79, "The reading is needed at step 0 (an existing plan) and step 1.", "Yes.",
     "MOVE: the heading becomes the title of `reading_definition_and_plan.md`, the file the steps 0 and 1 name (WAY-256, some steps need it, not all: consulted text). The incoming reference of `project-level/lead/skill/SKILL.md` is changed to this file (task To do 4).",
     "`reading_definition_and_plan.md`, title.", ["reading_definition_and_plan.md"]),
    (81, 83, "Every step that runs a check: step 0, 1, 5, 6 and 7, also a dispatched turn that only runs the checks.",
     "Yes - the agent meets it at each run of `readiness_check.py` or `plan_check.py`.",
     "KEEP in `SKILL.md`, as the first paragraph of 'Rules that hold across the steps' (task To do 3): a rule of working the agent keeps at every check, so it must not stand in a file of one step. The reading file opens with a sentence that repeats its content as a pointer ('every check runs on them whole, as `SKILL.md` gives'), for a reader that comes to the file from `lead-project`. Carried: WAY-151. " + NOMIST,
     "`SKILL.md`, 'Rules that hold across the steps'.", ["SKILL.md"]),
    (85, 94, "Steps 0 and 1 when the work is chosen: the inventories of a definition and of a plan.",
     "Yes - the agent meets it when it starts to read a definition or a plan.",
     "MOVE to `reading_definition_and_plan.md`. Text consulted at steps 0 and 1 (a procedure), so it is a file each of the two steps names and step 1 has it read unless step 0 did (WAY-256); `SKILL.md` names it at both steps (WAY-265). Carried: WAY-151. " + NOMIST,
     "`reading_definition_and_plan.md`, first two bullets.", ["reading_definition_and_plan.md"]),
    (95, 101, "Steps 0 and 1: choosing what to read in full for the work.", "Yes.",
     "MOVE to `reading_definition_and_plan.md`. Carried: WAY-151. " + NOMIST,
     "`reading_definition_and_plan.md`, third bullet.", ["reading_definition_and_plan.md"]),
    (102, 104, "Steps 0 and 1 when the cut or a question's interpretation might change; and before an edit of a resumed plan (steps 2-7 of a resumed plan).",
     "Yes - the agent meets it at each doubt about the cut and before each resumed edit; the sentence 'Before a resumed edit, read every other row ...' is a reading instruction, applied when the edit is about to be made.",
     "MOVE to `reading_definition_and_plan.md`. Judged a procedure of reading, not a rule that the agent keeps in writing steps: every session that resumes or corrects a plan passes `existing_plan.md`, which has the reading file read at step 0, and every fresh breakdown reads it at step 1, so the sentences are in the session before any step 2-4 edit; the sentence 'A new complete breakdown processes ...' (lines 104-106), which is a rule kept during steps 2-4, stays in `SKILL.md` (next row). Line 104 ends with the first words of that sentence ('A new complete'). This is the boundary judgement WAY-256 leaves to the row; the reviewer is asked to confirm it (weakest point). Carried: WAY-151. " + NOMIST,
     "`reading_definition_and_plan.md`, last bullet.", ["reading_definition_and_plan.md"]),
    (105, 106, "Steps 2, 3 and 4 of a new breakdown (each step covers every scope item, projected entry and exact question), and every later whole-plan check.",
     "Yes - the agent meets it while it cuts, assigns and places.",
     "KEEP in `SKILL.md`, as the second paragraph of 'Rules that hold across the steps': a rule of working kept during steps 2-4 (task acceptance: the sentence reaches steps 2-4). Carried: WAY-151. " + NOMIST,
     "`SKILL.md`, 'Rules that hold across the steps'.", ["SKILL.md"]),
    (108, 114, "Step 2 in every use.", "Yes - the step heading and its pointer.",
     "MOVE the two bullets to `cut_tasks.md`; the heading stays in `SKILL.md`. Carried: WAY-143, WAY-13. " + NOMIST,
     "`cut_tasks.md`, first two bullets.", ["cut_tasks.md"]),
    (115, 127, "Step 2 only when the reading of the guidelines in step 1 found a styleguide, general coding file or testing guidelines missing or uncertain, or the approved scope has a task create the first file of a kind of code, work on a kind that has files but no index entry, make the first test of a level, or extend existing guidelines. None of the 14 recorded uses reached the product's `guidelines/` directory.",
     "Yes - the agent holds the findings of the guidelines reading ('keep what it finds missing or uncertain') when it cuts; the condition in `SKILL.md` and in `cut_tasks.md` is worded by those findings and by the five matters of the bullet.",
     "MOVE to `guideline_tasks.md`, unchanged (one bullet of many instructions, with a condition of its own; the exception for one instruction does not keep it). `cut_tasks.md` points to it at the place of the bullet and `SKILL.md` names it at step 2 with the same condition (WAY-265). Selects: missing guidelines, the first file of a kind, an existing kind without an index entry, a level's first test, an extension. Its sentence 'Follow step 5 for questions or work beyond the approved definition, never silently enlarge it' reaches `write_and_check.md` (list 'from step 2'). Ground: a variant not used by the base's 14 recorded uses (cost: 176 words of the file); carried: WAY-218, WAY-247, WAY-200, WAY-242. " + NOMIST,
     "`guideline_tasks.md`; the pointer, with the condition, in `cut_tasks.md` and `SKILL.md`.", ["guideline_tasks.md"]),
    (128, 136, "Step 2 in every use; its last bullet when something the cut seems to need is not in the definition.",
     "Yes.",
     "MOVE to `cut_tasks.md`. The last bullet reaches `write_and_check.md` in the list 'from step 2' (task acceptance); the original stays here, where the agent meets the moment. Carried: WAY-147, WAY-144, WAY-145. " + NOMIST,
     "`cut_tasks.md`, last three bullets.", ["cut_tasks.md"]),
    (138, 143, "Step 3 in every use; the second bullet when an entry has no task making it true.", "Yes.",
     "MOVE to `assign_entries.md`; the heading stays. The second bullet reaches `write_and_check.md` in the list 'from step 3'. Carried: WAY-142, WAY-126. " + NOMIST,
     "`assign_entries.md`, first two bullets.", ["assign_entries.md"]),
    (144, 149, "Step 3 when two tasks realize one entry; steps 0 and 7 when `plan_check.py` reports such a pair.",
     "Yes - the script's report names the pair.",
     "MOVE to `assign_entries.md`, unchanged; steps 0 and 7 reach it by the sentences of `existing_plan.md` and `hand_over.md` (previous rows). Carried: WAY-230. " + NOMIST,
     "`assign_entries.md`, third bullet.", ["assign_entries.md"]),
    (151, 159, "Step 4 in every use.", "Yes.",
     "MOVE to `place_questions.md`; the heading stays. Carried: WAY-142, WAY-145. " + NOMIST,
     "`place_questions.md`, first bullet.", ["place_questions.md"]),
    (160, 163, "Step 4 when a move changes which task writes an entry, or a question arises only in the breakdown; and step 5 (where the question is asked).",
     "Yes.",
     "MOVE to `place_questions.md`, unchanged; both sentences reach `write_and_check.md` in the list 'from step 4', including the marker `— definition: none` (task acceptance). Carried: WAY-145. " + NOMIST,
     "`place_questions.md`, last two bullets; restated in `write_and_check.md`.", ["place_questions.md"]),
    (165, 171, "Step 5 in every use.", "Yes.",
     "MOVE to `write_and_check.md`; the heading stays. Carried: WAY-142, WAY-146. " + NOMIST,
     "`write_and_check.md`, first two bullets.", ["write_and_check.md"]),
    (172, 175, "Step 5 in every use that has something to ask; also a resume at step 5, which has not read steps 2-4.",
     "Yes.",
     "MOVE to `write_and_check.md`. The generic list 'questions that arose ..., moves ..., a task or an entry' is kept as written, and the lines of steps 2-4 that send a matter here are stated again as the list 'What steps 2-4 send here' in the same file, so that a session that did not read steps 2-4 asks them (task acceptance). Carried: WAY-145. " + NOMIST,
     "`write_and_check.md`, third bullet and the list under it.", ["write_and_check.md"]),
    (177, 188, "Step 6 in every use that runs the critique (not a dispatched turn: it requests it).",
     "Yes.",
     "MOVE to `critique_plan.md`; the heading stays. The file begins with a sentence that switches the run off for a dispatched turn (which the base's 'Delegated work' did, bullet 3). Carried: WAY-120, WAY-146, WAY-151. " + NOMIST,
     "`critique_plan.md`, first bullet.", ["critique_plan.md"]),
    (189, 192, "Step 6 after the critique's report.", "Yes.",
     "MOVE to `critique_plan.md`, unchanged. Carried: WAY-120, WAY-146. " + NOMIST,
     "`critique_plan.md`, last two bullets.", ["critique_plan.md"]),
    (194, 200, "Step 7 in every use that hands a plan over.", "Yes.",
     "MOVE to `hand_over.md`; the heading stays. The file begins with a sentence for a dispatched turn and carries the finding about two tasks on one entry (second bullet). Carried: WAY-230. " + NOMIST,
     "`hand_over.md`, first bullet.", ["hand_over.md"]),
    (201, 205, "Step 7, when the human gives a word; its last sentence in a dispatched turn.", "Yes.",
     "MOVE to `hand_over.md`, unchanged. Carried: WAY-152, WAY-147. " + NOMIST,
     "`hand_over.md`, last bullet.", ["hand_over.md"]),
]

PROPOSALS = [
    ("1", "reword", "lines 11-12 `The decisions that set its rules are cited below.`",
     "Remove the sentence. It names no rule and nothing is lost: every rule cites its decision in brackets.",
     "Left: 9 words in every use. Made: the reader no longer learns, before the steps, that the brackets are decisions; a meaning-neutral cut, listed because the task accepts only meaning-preserving changes."),
    ("2", "remove", "lines 144-149 the item format `- YYYY-MM-DD — side by side: tasks <n>, <m> on \"<entry>\" — <why>` and its reason rule, repeated in `project-level/plan/template.md:162-168`",
     "Remove the format from the skill and point to the template, which step 0 reads in full.",
     "Left: the format repeated in `assign_entries.md`, and two places to keep equal when the format changes. Made: the instruction at the moment of assigning loses its worked format; an agent that skimmed the template writes the item wrongly and `plan_check.py` reports it."),
    ("3", "remove", "lines 184-188 the list of what the critique judges, repeated in `project-level/plan/template.md:184-188`",
     "Remove the list from the step 6 request and point to the template section 'What the check decides, and what the critique judges'.",
     "Left: the list repeated in `critique_plan.md`, and a drift risk. Made: the request to the critic is built from a section the author has to find; if the author forgets it, the critic judges less than WAY-146 asks."),
    ("4", "remove", "lines 110-114 and 128-134 the rules that a task ends with something checkable (template `Goal`, line 83), that a technical element enters with the first task that uses it (template `Preparatory`, line 86), that every task of a new plan reads `to refine` (template line 94) and what `Depends on` constrains (template lines 84, 109)",
     "Remove these restatements from `cut_tasks.md` and rely on the template read at step 0.",
     "Left: the rules repeated in `cut_tasks.md`. Made: the cut loses its rules at the moment of cutting; the template holds them as column rules, not as a sequence, and the cut would rest on the agent applying a table's cell."),
    ("5", "reword", "lines 160-163 `stands with — definition: none` repeated in `project-level/plan/template.md:146-147` and now restated in `write_and_check.md`",
     "Keep the rule once, in the template, and let the step 4 and step 5 files point to it.",
     "Left: three places say it (template, `place_questions.md`, `write_and_check.md`). Made: a change of the marker is made in one place; the cost is a pointer at each of the two steps."),
    ("6", "reword", "the widened condition of the pointer in `SKILL.md` step 0 ('by the human or in a dispatched turn by its conversation file')",
     "State it in `delegated_mode.md` instead, as a fifth bullet, so the selection of `existing_plan.md` is the dispatch's own.",
     "Left: the condition is in `SKILL.md` and relies on the reviewer accepting it as meaning-preserving. Made: a new sentence in the delegated file, which the task keeps unchanged (question 1)."),
]

CHECK_SCRIPT = """\
- Command: `python -B instruction-files/check_instructions.py .` in the worktree; exit code 0; output identical to the same command on the base tree exported from 2f51e6c (line endings aside).
- `WARN dead-path AGENTS.md:21 `_zadania\\` does not exist` - the root `AGENTS.md` names a folder of the author's private notes. Claude Code, Codex and Cursor all load the root `AGENTS.md`, so in each of them an agent that cannot open the folder asks the human, as the file says. It stands on the base and is not changed here.
- `INFO size` lines: `AGENTS.md` 22 lines, 195 words; `CLAUDE.md` 1 line, 1 word; `agent-instructions/README.md` 78 lines, 721 words. None says that something was not read or not checked.
- The script reads only the root files and what they name; it does not read the skill files of `project-level/plan/skill/`, so its output is the same before and after the rebuild."""

CONTRA = """\
No contradiction between files that load together. The rebuilt files were checked for two things: (a) the steps name each other with the same words as before ('step 3', 'step 5', `define-project` step 7), and every file named exists; (b) the opening sentence of `write_and_check.md`, `critique_plan.md` and `hand_over.md` for a dispatched turn agrees with the bullets of `delegated_mode.md` (no question to the human, the critique requested through the file, the handover returned through the conversation)."""


def git_base():
    return subprocess.run(["git", "-C", REPO, "show", f"{BASE}:{PATH}"], capture_output=True,
                          check=True).stdout.decode("utf-8")


def norm(text):
    text = NL.join(l for l in text.split(NL) if not l.startswith("#"))
    text = re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", text, flags=re.M)
    return re.sub(r"\s+", " ", text).strip()


def sentences(text):
    return [p for p in re.split(r"(?<=[.!?;:])\s+", norm(text)) if p]


def main():
    base = git_base().split(NL)
    nonblank = {i + 1 for i, l in enumerate(base) if l.strip()}
    seen = {}
    errors = []
    prev_end = 0
    for r in ROWS:
        s, e = r[0], r[1]
        if s <= prev_end:
            errors.append(f"overlap at {s}")
        prev_end = e
        for n in range(s, e + 1):
            if n in nonblank:
                if n in seen:
                    errors.append(f"line {n} twice")
                seen[n] = r
    for n in sorted(nonblank - set(seen)):
        errors.append(f"line {n} in no row")
    corpus = {}
    for name in sorted(set(p for r in ROWS for p in r[6])):
        with open(f"{REPO}/{DIR}{name}", encoding="utf-8", newline="") as f:
            corpus[name] = norm(f.read())
    allcorp = ""
    import glob
    for fn in glob.glob(f"{REPO}/{DIR}*.md"):
        with open(fn, encoding="utf-8", newline="") as f:
            allcorp += " " + norm(f.read())
    notes = []
    for r in ROWS:
        for sen in sentences(NL.join(base[r[0] - 1:r[1]])):
            if sen in allcorp and not any(sen in corpus[p] for p in r[6]):
                errors.append(f"lines {r[0]}-{r[1]}: sentence stands elsewhere than the declared places: {sen[:70]}")
            if sen not in allcorp:
                notes.append(f"lines {r[0]}-{r[1]}: reworded: {sen[:80]}")
    out = ["# Assessment of project-level/plan/skill/SKILL.md at 2f51e6c", "",
           "Judged by the skill `instruction-files`, mode judge, kind skill (`instruction-files/judging.md`, "
           "`instruction-files/kind_skill.md`). Tools in use: Claude Code and Codex through the project "
           "entry points, Cursor through the shared layout; sessions start in the-way's checkout or in a "
           "product that pins it. The base is commit 2f51e6c; the permalink of each range is "
           f"`{LINK}#L<a>-L<b>`. In a quote the line breaks are shown as `<br>`; every nonblank line of "
           "the file stands in exactly one row. Where a quoted range opens or ends mid-sentence, the row "
           "says so.", "",
           "## 1. The check script", "", CHECK_SCRIPT, "",
           "## 2. The table", "", SRC + ".", "",
           "Reading of the columns: *Needed* is when an agent needs the fragment; *Recognised* is whether "
           "an agent recognises that moment when it comes (WAY-257); the verdict is one of keep, move, "
           "remove, reword with its reason and its ground; *New place* is where the fragment stands after "
           "the rebuild. Verdicts of this table that change a rule's meaning would be proposals, not "
           "applied (task To do 9); none of the rows below does, and the proposals stand after the "
           "table.", "",
           "| Fragment | Needed | Recognised | Verdict, reason, ground | New place |",
           "|---|---|---|---|---|"]
    for r in ROWS:
        s, e, needed, rec, verdict, place, _ = r
        quote = NL.join(base[s - 1:e])
        quote_cell = f"[`L{s}-L{e}`]({LINK}#L{s}-L{e})<br>" + quote.replace("|", "&#124;").replace(NL, "<br>")
        words = len(quote.split())
        out.append(f"| {quote_cell} | {needed} | {rec} | {verdict} Words in the base: {words}. | {place} |")
    out += ["", "Rows whose verdict is keep stand in `SKILL.md`; rows whose verdict is move stand in the "
            "file named in the last column, and the heading of a step stays in `SKILL.md` with its pointer.",
            "", "## 3. Contradictions between files that load together", "", CONTRA, "",
            "## Proposals that change the meaning of a rule (not applied)", "",
            "Each proposal is listed once, with what happens if it is left and what it costs if it is "
            "made. The repetitions between the skill and `project-level/plan/template.md` are 2-5.", ""]
    for num, kind, where, what, cost in PROPOSALS:
        out += [f"{num}. **{kind}** - {where}. Proposal: {what} {cost}"]
    out += ["", "## Text added that no base line carries", "",
            "Each new sentence, with what it switches off (the comparison cannot see this):", ""]
    ADDED = [
        ("`SKILL.md`, 'Delegated work' pointer", "reads `delegated_mode.md` first when dispatched through a refinement conversation path", "Nothing for a turn not dispatched; it switches off no item of the file's bullets because the file is read whole."),
        ("`SKILL.md`, step 0 pointer", "reads `existing_plan.md` and the reading file when an existing plan is named, by the human or by the conversation file", "Switches off nothing; it selects the dispatched turn that the base's 'Delegated work' already sent through the existing-plan bullet. 'Otherwise begin with step 1' now covers a session that names no plan."),
        ("`SKILL.md`, step 1 pointer", "reads `read.md` and the reading file, each unless step 0 had them read", "Switches off a second reading of the same files, as WAY-256 gives; a session that skipped step 0 reads them there."),
        ("`SKILL.md`, step 2 pointer", "reads `cut_tasks.md`; reads `guideline_tasks.md` under the five-matter condition", "Switches off `guideline_tasks.md` for a breakdown whose reading found nothing missing or uncertain and whose scope has none of the five matters; in the base the bullet had no effect then either."),
        ("`SKILL.md`, steps 3-7 pointers; steps 5-7 add 'in a dispatched turn it points to `delegated_mode.md` for what changes'", "reads the step's file", "Nothing; the clause for steps 5-7 adds a route to the delegated file for a dispatched turn, which the base reached through the section at the top."),
        ("`existing_plan.md`, last bullet", "a session that has not been through `read.md` goes through it, that is carries it out, before going on, whichever step the plan goes on from", "a draft resume that skips step 1 altogether (the base's text sent a resumed draft from the first unfinished step, past step 1); it switches off nothing else. The session that went through `read.md` here has nothing left to do at `SKILL.md` step 1, whose pointer reads 'unless step 0 had you read it' with the meaning every `Read <file>` pointer of `SKILL.md` has, to carry the file out."),
        ("`existing_plan.md`, pointers for the finding about two tasks", "names `assign_entries.md` and `hand_over.md` for steps 3 and 7", "Nothing."),
        ("`reading_definition_and_plan.md`, first sentence", "points to `SKILL.md`'s rules for the authority of the originals", "Nothing."),
        ("`cut_tasks.md`, third bullet", "reads `guideline_tasks.md` under the condition of `SKILL.md`", "Nothing beyond the row for lines 115-127."),
        ("`assign_entries.md`, last bullet; `hand_over.md`, second bullet", "settles a `plan_check.py` finding about two tasks on one entry as step 3 gives it", "Nothing; the bullet restates lines 59-61 at the place where the agent meets the finding."),
        ("`write_and_check.md`, opener and list 'What steps 2-4 send here'", "a dispatched turn asks nothing itself; lists the matters steps 2-4 send to step 5", "Switches off asking the human directly in a dispatched turn (the base's bullet 2 did); the list switches off nothing, it restates lines 125-126, 135-136, 142-143, 160-163."),
        ("`critique_plan.md`, opener", "a dispatched turn requests the critique instead of running it", "Switches off 'Run `critique` once' for a dispatched turn (the base's bullet 3 did)."),
        ("`hand_over.md`, opener", "a dispatched turn shows the human nothing itself", "Switches off 'Show the human' for a dispatched turn (the base's last sentence of step 7 and bullet 2 did)."),
    ]
    for where, what, off in ADDED:
        out.append(f"- {where}: {what}. Switches off: {off}")
    with open(OUT, "w", encoding="utf-8", newline=NL) as f:
        f.write(NL.join(out) + NL)
    print("rows", len(ROWS), "errors", len(errors))
    for x in errors:
        print("ERR", x)
    with open(OUT.replace("assessment.md", "assessment_notes.txt"), "w", encoding="utf-8", newline=NL) as f:
        f.write(NL.join(notes) + NL)


if __name__ == "__main__":
    main()

"""Builds reports/assessment.md: the table of rows over the old SKILL.md (commit 525cde1), every
non-blank line in a row, fragments quoted literally from git. Writes the file given as argv[1]."""
import html
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
BASE = "525cde1dd53c474f56ea0ece289cb60e868aa90d"
OLD = subprocess.run(["git", "-C", str(ROOT), "show", f"{BASE}:project-level/technology/SKILL.md"],
                     capture_output=True, text=True, encoding="utf-8", check=True).stdout.split("\n")

URL = f"https://github.com/mariusznazar/the-way/blob/{BASE}/project-level/technology/SKILL.md"

# Recurring answers.
ALWAYS = "Throughout the skill, from the first read of its description and picture."
ALWAYS_R = "Yes: the description and the first paragraphs are read with SKILL.md whatever the route."
START = "At the start and when resuming from the definition's Technology section."
START_R = "Yes: the pointer of step 0 in SKILL.md names it in the words of the situation (start, resume, a list already written)."
LIST = "When the Technology section reads TODO and the list is made."
LIST_R = "Yes: the pointer of step 1 names the situation by what the section reads (TODO)."
RP = "When the look at the logs, the interface and the development data is taken: a new list for a project with behaviour a user sees, or any list already written."
RP_R = "Yes: SKILL.md points to it from step 0 (a list is written) and from step 1 (behaviour a user sees); start.md and list.md point to it again at the sentence that takes the look."
SETTLE = "When an open choice is to be settled: after the list is confirmed, or on a resume with an open item."
SETTLE_R = "Yes: the pointer of step 2 names it by the list holding an open choice, and start.md points to it at the resume bullet that resumes the step."
RES = "By the research agent, when it researches one choice."
RES_R = "Yes for the agent: the leader gives it the file's path with the choice; it reads that file as its whole work. The leader does not read it."
CLOSE = "When no open choice is left."
CLOSE_R = "Yes: the pointer of step 3 names it by the list holding no open choice; start.md and list.md point to it where they go to that step."

# (first line, last line, needed, recognised, verdict+reason+ground); line numbers of the old file.
ROWS = [
    (1, 4, ALWAYS, ALWAYS_R,
     "Keep. The description is the way in and is named from elsewhere (installation/README.md:57, the generated entry points); unchanged, so the entry points stay current (skill-entry-points, derived-file-content). Ground: carried decision WAY-127."),
    (6, 6, ALWAYS, ALWAYS_R, "Keep. Title of the picture of the whole (WAY-256)."),
    (8, 16, ALWAYS, ALWAYS_R,
     "Reword the last clause only: `this skill holds the order of the work.` becomes `this skill holds the order of the work and the rules that hold across it, and a file beside it holds the work of each step.` The old clause would claim the steps' work for SKILL.md; the sentence before it still names where each rule stands. No rule changes. Ground: carried decision WAY-256 (the picture of the whole and the pointers stay)."),
    (18, 22, ALWAYS, ALWAYS_R,
     "Reword `each skill named below` to `each skill named in this skill or in a file beside it`. The prefix rule holds across steps and stays here, and the files beside the skill now name `define-project`, `record-decision` and `critique` too. Meaning of the rule unchanged. Ground: carried decision WAY-127."),
    (24, 25, "Across all steps, and by the research agent, which writes a report only.", "Yes in SKILL.md (read by the leader first). The research agent never reads SKILL.md, so the same sentence stands again in research.md.",
     "Keep in SKILL.md and copy word for word into research.md (acceptance criterion 4). The one sentence stands in two files, because two readers need it and only one of them reads SKILL.md. Ground: carried decision WAY-106."),
    (27, 27, ALWAYS, ALWAYS_R, "Keep as heading `## 0. Start or resume`; the step's text becomes a pointer in SKILL.md."),
    (29, 30, START, START_R,
     "Move to start.md. Two changes: (a) `elements/common/critique/SKILL.md` leaves the reading of this step and is read when the first critique of step 2 comes (To do 3, authorised); (b) `definition_template.md` becomes `project-level/definition_template.md`, still read in full. Ground: carried step of the skill (step 0); cost saved on routes without step 2: 831 words of the critique instruction."),
    (31, 32, START, START_R, "Move to start.md unchanged. A step's procedure of several instructions (WAY-256, question 7). Ground: carried decision WAY-121."),
    (33, 35, START, START_R, "Move to start.md unchanged. Carried decision WAY-150 and the section `Reading the foundation` of way_of_working.md, which stays read in step 0."),
    (36, 36, START, START_R,
     "Move to start.md; reword `begin with step 1` to `begin with the step \"List the choices\" (list.md beside this file)`, because a file read by its path has no step numbers. Meaning unchanged."),
    (37, 40, "On any resume where a list is written, including a list with no open item.", "Yes: start.md names it in the bullet for a list; SKILL.md step 0 adds the pointer to running_product.md for the same case.",
     "Move to start.md; the look it takes moves to running_product.md and `step 1 gives` becomes `running_product.md beside this file gives`. This is the case acceptance criterion 3 names: the look reaches both ways of resuming. Ground: carried decision WAY-121 (the look adds items before the gate)."),
    (41, 45, START, START_R,
     "Move to start.md; `Then show the list, ask whether it still holds, and resume step 2` becomes two instructions, `Then show the list and ask whether it still holds; where the human adds or changes an item, follow the step \"List the choices\" (list.md beside this file) for it` (so the human's change reaches the rules of list.md) and `Then resume the step ...`; `resume step 2` becomes `resume the step \"Settle the open choices\" (settle.md beside this file)`. The report directory `.runs/technology/` stays named here, and its naming rule reaches the leader through SKILL.md (acceptance criterion 3). Ground: carried step (resume)."),
    (46, 46, START, START_R, "Move to start.md; `go to step 3` becomes `go to the step \"Close\" (close.md beside this file)`. One instruction, but it sits in a step whose other bullets move; a pointer inside the bullet list costs the same."),
    (48, 48, ALWAYS, ALWAYS_R, "Keep as heading; text becomes a pointer."),
    (50, 54, LIST, LIST_R, "Move to list.md unchanged. Procedure of the step (WAY-256, question 7). Ground: carried decision WAY-121."),
    (55, 62, RP, RP_R,
     "Move to running_product.md; list.md keeps one instruction in its place: `Then, where the project brings behaviour a user sees in the running product, take the look ... that running_product.md beside this file gives, and list each matter as it says.` Two ways of using the text (new list; resume) need it, so it stands apart rather than in one of them. Ground: carried decisions WAY-121, WAY-165."),
    (63, 66, LIST, LIST_R, "Move to list.md unchanged. Ground: carried decision WAY-121. A resumed leader reads list.md for this rule when the look adds an item or the human adds or changes one at the question whether the list still holds (SKILL.md step 0 and start.md say so)."),
    (67, 71, LIST, LIST_R, "Move to list.md unchanged. Ground: carried decision WAY-121 and invariant project-technology-record."),
    (72, 73, LIST, LIST_R, "Move to list.md unchanged. Ground: carried decision WAY-108 (status line)."),
    (74, 78, LIST, LIST_R, "Move to list.md unchanged. Ground: carried decisions WAY-112, WAY-113."),
    (79, 79, LIST, LIST_R, "Move to list.md; `go to step 3` becomes `go to the step \"Close\" (close.md beside this file)`."),
    (81, 81, ALWAYS, ALWAYS_R, "Keep as heading; text becomes a pointer."),
    (83, 87, SETTLE, SETTLE_R, "Move to settle.md unchanged. Waves are the leader's. Ground: carried decision WAY-122."),
    (89, 91, SETTLE, SETTLE_R,
     "Move to settle.md; the list of what the research agent gets gains one item, the path of research.md (To do 2, authorised; this is the change of the list the request names). The sentence `The agent finds the options, weighs them, compares their consequences and writes the comparison to the choice's report.` is new connective text, so the leader knows what comes back; it states no new rule. Ground: carried decision WAY-122."),
    (91, 96, RES, RES_R,
     "Move to research.md; `Each finds` / `gives` become `Find` / `give` because the file addresses the agent. Meaning unchanged. Ground: carried decision WAY-122; cost: these 340 words are read by every reader of the old SKILL.md, including the leader on routes with no open choice."),
    (97, 103, RES, RES_R, "Move to research.md; `the agent reads off` becomes `read off`. Ground: carried decision WAY-122."),
    (104, 111, RES, RES_R,
     "Move to research.md; `the agent says` / `it also says` become imperatives. The rule on the report name stands here word for word and again in SKILL.md, where the leader reads it (acceptance criterion 3). A sentence naming `an agent's way to the running product` gains a gloss: `the logs, the interface or the development data, the three matters the template's Technology section names`, so the agent knows the term with only its file. Ground: carried decisions WAY-123, WAY-166."),
    (112, 117, "Once a comparison of the wave is written.", "Yes: the sub-step is named `Critique` and the leader reads settle.md at step 2. The critique instruction is read at this sub-step, and SKILL.md step 2 says so.",
     "Move to settle.md; `following critique` gains `whose file is elements/common/critique/SKILL.md`, so the reading is named where it is needed (To do 3, authorised). Ground: carried decisions WAY-120, WAY-122."),
    (118, 131, "When every comparison of the wave reads `critique: passed`; also on a resume in which sub-step 4 falls away because every report already reads it.", "Yes: the sub-step is named `Show`; the critique instruction is read here if sub-step 4 did not need it (SKILL.md step 2 says `the first critique of a comparison or of a table`).",
     "Move to settle.md; `as step 6 needs` becomes `as sub-step 6, Choose, needs` (a file read alone has no step numbering of the whole skill). Ground: carried decisions WAY-123, WAY-137, WAY-166, WAY-138."),
    (132, 139, "Same moment as the row above: the critique of the table and the showing of the wave.", "Yes, as above.",
     "Move to settle.md; `following critique` gains the path of the critique instruction, as in sub-step 4. Ground: carried decisions WAY-120, WAY-138, WAY-113, WAY-123."),
    (140, 149, "When the human is to choose.", "Yes: the sub-step is named `Choose`.",
     "Move to settle.md; `the question way_of_working.md asks after a choice` becomes `the question the section \"How a skill asks\" of elements/common/way_of_working.md asks after a choice`, because the bare name does not resolve from a file beside the skill. Ground: carried decisions WAY-113, WAY-123, WAY-138."),
    (150, 158, "After the human chooses.", "Yes: the sub-step is named `Write`.", "Move to settle.md unchanged. Ground: carried decisions WAY-117, WAY-138."),
    (160, 160, ALWAYS, ALWAYS_R, "Keep as heading; text becomes a pointer."),
    (162, 162, CLOSE, CLOSE_R, "Move to close.md unchanged. Ground: invariant project-technology-record."),
    (163, 165, CLOSE, CLOSE_R,
     "Move to close.md; `back to step 2` / `step 1` become `back to the step \"Settle the open choices\" (settle.md beside this file)` / `\"List the choices\" (list.md beside this file)`. Ground: carried invariants project-readiness-gate, project-technology-record."),
    (166, 166, CLOSE, CLOSE_R, "Move to close.md unchanged."),
    (168, 170, "On a resume or a return after approval of the definition; a rule that holds across the steps.", "Yes: it stays at the end of SKILL.md, read first.",
     "Keep in SKILL.md. One instruction, and a rule across steps. Ground: carried decision WAY-118."),
]


def cell(lines, first, last, cut_from=None, cut_to=None):
    chunk = OLD[first - 1:last]
    if cut_to is not None:  # first part of a shared line
        i = chunk[-1].index(cut_to)
        chunk[-1] = chunk[-1][:i].rstrip()
    if cut_from is not None:  # second part of a shared line
        i = chunk[0].index(cut_from)
        chunk[0] = chunk[0][i:]
    body = "<br>".join(html.escape(l).replace("|", "&#124;") for l in chunk)
    return f"[{first}-{last}]({URL}#L{first}-L{last}): <code>{body}</code>", " ".join(chunk).split()


def words(chunk):
    return len(chunk)


out = []
covered = set()
for first, last, needed, recog, verdict in ROWS:
    kw = {}
    if (first, last) == (89, 91):
        kw = {"cut_to": "Each finds the options"}
    if (first, last) == (91, 96):
        kw = {"cut_from": "Each finds the options"}
    quoted, toks = cell(OLD, first, last, **kw)
    n = len(toks)
    for ln in range(first, last + 1):
        covered.add(ln)
    out.append(f"| {quoted} | {needed} | {recog} | {verdict} ({n} words) |")

nonblank = {i + 1 for i, l in enumerate(OLD) if l.strip()}
missing = sorted(nonblank - covered)
extra = sorted(ln for ln in covered if ln not in nonblank)
assert not missing, missing
print("rows", len(ROWS), "nonblank lines", len(nonblank), "uncovered", missing, "blank inside rows (fine)", len(extra))

text = pathlib.Path(sys.argv[2]).read_text(encoding="utf-8")
table = "\n".join(out)
header = ("| Fragment (literal, with line range at 525cde1) | Needed when | Will the agent recognise that moment? | Verdict, reason and ground |\n"
          "|---|---|---|---|\n")
pathlib.Path(sys.argv[1]).write_text(text.replace("@@TABLE@@", header + table), encoding="utf-8", newline="\n")

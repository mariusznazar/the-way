"""Build reports/assessment.md: the judgement table of the base SKILL.md of maintain-styleguide.

Each quote is cut from the file at the base commit, so it is literal; coverage and overlap of the
nonblank lines are checked before writing.
"""
import subprocess
import sys

REPO = "C:/Storage/repos/the-way/.runs/worktrees/styleguide-skill-shape"
BASE = "525cde1dd53c474f56ea0ece289cb60e868aa90d"
PATH = "product-guidelines/styleguide/SKILL.md"
LINK = f"https://github.com/mariusznazar/the-way/blob/{BASE}/{PATH}"
NL = chr(10)
SG = "product-guidelines/styleguide/"

ALWAYS = "Every use, from the first line; SKILL.md is read whole."
SEEN = "Yes - no moment to recognise: SKILL.md is read whole by every use."

# (start, end, needed, recognised, verdict+reason+ground, new place)
ROWS = [
    (1, 6, ALWAYS + " The description is how the skill is matched, and the entry points are generated from it.",
     "Yes - it is the way in itself.",
     "KEEP. Needed in every use; carried: the entry points generated from this file (WAY-127, invariant skill-entry-points). Nothing in it belongs to one step.",
     "SKILL.md, unchanged."),
    (8, 16, ALWAYS, SEEN,
     "KEEP. The picture of the whole and the statement that the skill restates no rule of the templates; carried: WAY-35 (an element's skill holds only its order of work) and WAY-256 (SKILL.md keeps the picture of the whole).",
     "SKILL.md, unchanged."),
    (18, 22, ALWAYS + " It says where the files named below lie.", SEEN,
     "KEEP, with one sentence added (not a rule: the pointer condition for the files beside the skill, that they are read when the step or variant that names them comes). Carried: WAY-127 and WAY-259 (a named file is read when its step or variant comes).",
     "SKILL.md; the added sentence is new text, listed in the sentence comparison."),
    (24, 31, "Every use, at its start: where the skill runs and how it hands back to refine-task.", SEEN,
     "KEEP. Picture of the whole; carried: WAY-107, WAY-215. Mentions steps 1, 2, 3, 4 of refine-task, which every step relies on.",
     "SKILL.md, unchanged."),
    (33, 36, "Every step: what this skill writes and never writes, and what the cycle's author writes.", SEEN,
     "KEEP. A rule that holds across all steps (the skill never writes the foundation, the styleguide or code); carried: WAY-01, WAY-28, WAY-69, WAY-172. Its columns are one table, not separable instructions.",
     "SKILL.md, unchanged."),
    (38, 41, "Every step that settles a meaning: step 1 (which interface), 2, 3 and 4.", SEEN,
     "KEEP. A rule across steps: a meaning reaches the code only through the accepted task document; carried: WAY-172, WAY-124.",
     "SKILL.md, unchanged."),
    (43, 46, "The first sentence: at every step that writes into the task document (steps 1 to 4). The heading and the list below it: when the document's content is written and checked, step 4 and step 5.",
     "Yes for the sentence (SKILL.md is read whole). For the list: yes - the step 4 and step 5 pointers name `task_document.md` beside this skill.",
     "SPLIT. The sentence stays: it is one instruction that holds across steps, and its wording says 'the task document' for 'the document' (meaning-preserving reword, the section no longer gives 'document' a referent). The heading goes with the list, below. Ground: carried decision WAY-256 (rules that hold across the steps stay).",
     "The sentence: SKILL.md, section 'Rules that hold at every step'. The heading: `task_document.md`."),
    (48, 50, "Step 4 (writing the answers into the task document) and step 5 (the check). Not before: steps 1 to 3 write their own entries as their text says.",
     "Yes - the step 4 pointer names the file; step 5 points to it again.",
     "MOVE. Needed at two steps only; the list as a whole has several instructions, so the exception does not keep it in SKILL.md. Cost: about 330 words out of the text read at steps 1 to 3. Carried: WAY-256.",
     "`task_document.md`."),
    (51, 53, "As above (an item of the same list).", "As above.",
     "MOVE with its list. The item is one instruction, but it is one of seven that the same moment needs; splitting it from them would give a pointer per item (WAY-256, the exception reaches no further than one instruction against one pointer). Carried: WAY-182.",
     "`task_document.md`."),
    (54, 55, "As above.", "As above.",
     "MOVE with its list (two one-instruction items; same ground as the row before).",
     "`task_document.md`."),
    (56, 62, "As above.", "As above.",
     "MOVE with its list. Carried: WAY-192.",
     "`task_document.md`."),
    (63, 64, "As above, and only for a product's first guidelines: the condition is in the item's own words.", "As above; the item states its own condition.",
     "MOVE with its list. One instruction with its own condition, which rides along on every use of the file; kept there on purpose: moving it to a file of its own would trade one instruction for one pointer (WAY-256 exception). Carried: WAY-167.",
     "`task_document.md`."),
    (65, 65, "As above, and only where an audit ran (step 3): the condition is in the item's own words.", "As above; the item states its own condition.",
     "MOVE with its list; one instruction, the same reason as the row before. Carried: WAY-187.",
     "`task_document.md`."),
    (66, 68, "As above (step 4 writes the answers; step 5 checks them).", "As above.",
     "MOVE. Carried: WAY-134.", "`task_document.md`."),
    (69, 71, "As above.", "As above.",
     "MOVE. The entries it asks for come from steps 2 and 3, but they are written into the document with the other entries at step 4.",
     "`task_document.md`."),
    (72, 74, "Step 5 of refine-task builds the settlements; this skill's step 4 and 5 know what to leave to it.", "As above.",
     "MOVE. Carried: the hand-over to refine-task step 5.", "`task_document.md`."),
    (76, 84, "Only when refine-task runs in orchestrated mode (a styleguide task of a project plan led by lead-project), from step 1 on, since step 1 may ask the human which interface.",
     "Yes - refine-task's own orchestrated mode is the moment (it is dispatched with a conversation-file path); the pointer says so.",
     "MOVE. A variant: the whole section applies in one variant of the skill and to none of the others. Cost: about 100 words out of every non-orchestrated use. Carried: WAY-154, WAY-155, WAY-256.",
     "`orchestrated_mode.md`; SKILL.md keeps the heading and a pointer saying when to read it."),
    (86, 91, "Step 0, bullet 1, by file. Both templates: the styleguide template at step 2 (the starting set covers roles, states and focus, which that template defines; research questions come from them), the template of guidelines at step 4 (departures from the template, the form of the guidelines file). refine-task's `SKILL.md` and the task template: already read by refine-task at its steps 1 and 2. 'How a skill asks': read by refine-task step 1. 'Critique before collective review' and critique `SKILL.md`: at the first critique, step 2 where research ran, else step 4.",
     "Yes - each is named at the step that needs it, as a pointer in SKILL.md or in the step's file.",
     "SPLIT, by file. Both templates MOVE to steps 2 and 4 (neither is needed at step 1; the styleguide template is needed already at step 2, which is the task's weak point, checked: step 2 names roles, states and focus); the two templates were 3300 words read at the start of every run, also one that ends at step 1. The second reading of refine-task's `SKILL.md`, the task template and 'How a skill asks' is REMOVED: the frozen task's To do 2 accepts it (it is not a proposal; no rule is lost, the text was read at refine-task's steps 1 and 2). The critique files MOVE to the first critique. Ground: cost (about 6000 words read at the start) and carried decisions WAY-127, WAY-259 (a file is read when the step that names it comes), WAY-256.",
     "Step 2 pointer in SKILL.md (styleguide template); step 4 pointer in SKILL.md (template of guidelines); `research.md` and `settle.md` (critique files); SKILL.md step 0 states what refine-task has read and is not read again."),
    (92, 92, "Step 1, after the user interface is named: it is what the product has for the interface that the step reads off. A product with no interface ends before it.",
     "Yes - it opens the step's second bullet.",
     "MOVE. Needed for the recognition, not before it; a product without an interface (route 7) no longer reads it. Cost: product's files, not counted. Carried: WAY-185. REWORD (meaning-preserving): the bullet now reads 'every file under `guidelines/` that `refine-task` did not read at its step 1', because refine-task step 1 already read whole the guidelines of the parts the task touches (`read_sources.md:28`, `product-guidelines/reading.md:40`), on a refresh or an extension the styleguide itself; the set of files read after step 1 is the same, so this is no change of the rule (the frozen task's To do 2) and is not P1. See also proposal P1 (not applied), which narrows the reading and is a different change.",
     "`recognize.md`, second bullet."),
    (93, 96, "Step 1, after the interface is named: UI technology and role-meaning decisions serve steps 1, 2 and 4; the agent's way to the running product serves only step 3.",
     "Yes for both: step 1 and step 3 name them.",
     "SPLIT and MOVE. The sentence's selection method, the section 'Reading the foundation' of `way_of_working.md` (492 words), is read at refine-task step 1 already (not read again; same selection); its second reading is counted in the before figures of `word-counts.md`. What it adds - the decisions that settle the technology of the user interface, and those that give a role its meaning, a value its source or the styleguide a departure - goes to step 1 (read once, they stay in context for steps 2 and 4). The decisions on the agent's way to the running product go to step 3, since only the audit opens screens that way; a run without an audit no longer reads them. Meaning preserved; the citation WAY-165 stays with the agent's way (it is that decision's matter). Carried: WAY-150, WAY-165.",
     "`recognize.md` (technology and role decisions); `audit.md` (agent's way)."),
    (98, 106, "Step 1: to name the interface and to end where there is none.", "Yes - step 1.",
     "MOVE. The step is one procedure, a moment reached on every route; WAY-256 as the task's question 2 settles it places each step's procedure beside the skill, also where every run reaches it. Carried: WAY-183, WAY-185, WAY-121.",
     "`recognize.md`."),
    (107, 109, "Step 1.", "Yes - step 1.", "MOVE, as the row before. Carried: WAY-185.", "`recognize.md`."),
    (110, 112, "Step 1, at its end: it sets the mode that steps 2 and 3 follow.", "Yes - step 1.",
     "MOVE, as the row before. The mode it gives is what the step 3 pointer in SKILL.md refers to ('where the user interface has screens').", "`recognize.md`."),
    (113, 114, "Step 1; the question it records is settled at step 4.", "Yes - step 1.",
     "MOVE, as the row before. Carried: WAY-185, WAY-121.", "`recognize.md`."),
    (116, 118, "Step 1 sets refresh or extension; step 2 acts on it (research or not).", "Yes - step 1.",
     "MOVE. Defines the two words at the moment the mode is set; a rule that holds on two steps is placed in the file of the first, where the mode is decided, and step 2 states its own consequence (research, no research) in its own file. Carried: WAY-251.",
     "`recognize.md`."),
    (120, 127, "Step 2, on every route that reaches it: the first styleguide, a refresh, an extension.", "Yes - step 2.",
     "MOVE. Procedure of one step. Carried: WAY-184, WAY-186.", "`starting_rules.md`."),
    (128, 137, "Step 2, only for the first styleguide where the human has no preference, and at every extension. Not at a refresh, nor where the human has a preference.",
     "Yes - the condition is the moment the agent meets after the preference question, and `starting_rules.md` states it at that place.",
     "SPLIT. The research instructions (split into questions, fresh agents, sources, report paths) MOVE: a variant; cost about 210 words (the file) out of every run without research. The sentence on the refresh (do no research, use the accepted styleguide) and the condition stay in `starting_rules.md`, since every run reaches them. Carried: WAY-186, WAY-251.",
     "`research.md`; the condition and the refresh clause in `starting_rules.md`."),
    (138, 143, "Step 2, only where research ran, once the reports are in.", "Yes - it follows the research in the same file.",
     "MOVE with the research (reword: 'Where research ran' became 'Once the reports are in', since the file is read only where research ran; plus the pointer 'before the first critique of the session, read critique SKILL.md', replacing the step 0 read of that file). Carried: WAY-186, WAY-120.",
     "`research.md`."),
    (144, 147, "Step 2, every run that reaches it.", "Yes - step 2.", "MOVE. Carried: WAY-174, WAY-184.", "`starting_rules.md`."),
    (148, 149, "Step 2.", "Yes - step 2.", "MOVE. Carried: WAY-184.", "`starting_rules.md`."),
    (151, 153, "Step 3, only where the user interface has screens.",
     "Yes - the mode step 1 gives names it, and the step 3 pointer in SKILL.md repeats the condition.",
     "MOVE. A step reached only by runs with screens. Carried: WAY-187.",
     "`audit.md`; the condition stays in SKILL.md at the step 3 pointer."),
    (155, 157, "Step 3.", "Yes.", "MOVE with the step. Carried: WAY-187.", "`audit.md`."),
    (158, 158, "Step 3.", "Yes.", "MOVE with the step. One instruction in a list of five; kept with the step so that the step is one file. Carried: WAY-187.", "`audit.md`."),
    (159, 161, "Step 3.", "Yes.", "MOVE with the step. Carried: WAY-187, WAY-165.", "`audit.md`."),
    (162, 165, "Step 3, its end.", "Yes.", "MOVE with the step. Carried: WAY-187.", "`audit.md`."),
    (166, 168, "Step 3, and step 4 where the human settles the palette.", "Yes.",
     "MOVE with the step. Meaning kept; step 4's 'put every choice to the human' (a rule at every step) covers the palette at step 4. Carried: WAY-185, WAY-29.",
     "`audit.md`."),
    (170, 177, "Every step in which the skill asks the human a choice: the identifier of the interface at step 1, the preferences at step 2, the choices at step 4. Not step 4 alone.",
     "Yes - SKILL.md is read whole.",
     "KEEP, moved from step 4 to the section 'Rules that hold at every step' of SKILL.md. A rule that holds on several steps, placed in the file of one of them, would silently stop reaching the others (the trap of the same kind of work); WAY-174 binds the skill's every question, not those of step 4. The step heading stays as a step-4 pointer. Carried: WAY-174, WAY-113, WAY-256.",
     "SKILL.md, 'Rules that hold at every step'."),
    (178, 183, "Step 4, only for a new tool or library left as a technology question of the task (step 1 records it).",
     "Yes - the agent recorded the question itself at step 1; `settle.md` names the condition.",
     "MOVE. A variant with a condition of its own that would ride along on every use if it stayed in the step's file; several instructions (show by consequences, recommend with the weak point, keep the preferred tool, leave the choice). Carried: WAY-185, WAY-186, WAY-123, WAY-121.",
     "`new_tools.md`; one pointer in `settle.md`."),
    (184, 189, "Step 4, every run.", "Yes - step 4.", "MOVE with the step. Carried: WAY-173.", "`settle.md`."),
    (190, 197, "Step 4, every run.", "Yes - step 4.", "MOVE with the step. Carried: WAY-86, WAY-191, WAY-80. See proposal P2 (not applied).", "`settle.md`."),
    (198, 204, "Step 4, every run.", "Yes.", "MOVE with the step. Carried: WAY-60, WAY-191.", "`settle.md`."),
    (205, 207, "Step 4.", "Yes.", "MOVE with the step. Carried: WAY-168.", "`settle.md`."),
    (208, 210, "Step 4.", "Yes.", "MOVE with the step. Carried: WAY-189.", "`settle.md`."),
    (211, 215, "Step 4.", "Yes.", "MOVE with the step. Carried: WAY-60.", "`settle.md`."),
    (216, 219, "Step 4, only where the human chooses to clean the screens as tasks touch their styles rather than in one clean-up.",
     "Yes - the human's choice is the moment, and `settle.md` names it in the item's place.",
     "MOVE. A fragment with a condition of its own inside a list that every run reads (the trap of the same kind of work); two instructions (mark the invariant violated; say that only the review holds the line), so the exception does not keep it. Carried: WAY-51.",
     "`staged_cleaning.md`; one pointer in `settle.md`."),
    (220, 220, "Step 4.", "Yes.", "MOVE with the step. One instruction in a list; the item stays with the list that gives its context.", "`settle.md`."),
    (221, 222, "Step 4, once the set of proposals is complete.", "Yes.",
     "MOVE with the step, with the pointer to the critique files added ('read that section and, unless step 2 read it, critique SKILL.md'), which replaces the read at step 0. Carried: WAY-120.", "`settle.md`."),
    (223, 224, "Every step that asks the human a question and writes the answer: steps 1, 2 and 4.", "Yes - SKILL.md is read whole.",
     "KEEP, moved to 'Rules that hold at every step' (one instruction that holds across steps; in the file of step 4 it would not reach steps 1 and 2). Carried: refine-task step 3, WAY-134.", "SKILL.md, 'Rules that hold at every step'."),
    (226, 229, "Step 5, the end of every run that reaches it.", "Yes - step 5.",
     "MOVE. Two instructions (check, hand back), so the exception does not keep them. The reference to the section 'What reaches the task document' became 'what `task_document.md` beside this skill names'; the meaning is the same. Carried: WAY-172.",
     "`hand_back.md`."),
    (230, 232, "Step 5.", "Yes.", "MOVE with the step. Carried: WAY-134.", "`hand_back.md`."),
]

PROPOSALS = [
    ("P1", 92, 92, "A reword that changes the rule's meaning: read from the product's `guidelines/` only the file for the part the task covers and the index of the coding guidelines, instead of every file under it.",
     "The skill reads every file under `guidelines/` and the root `AGENTS.md`. Refine-task already read the guidelines of the parts the task touches (by `product-guidelines/reading.md`), so the wider reading may repeat that and add what the interface does not need; it costs the product's words and differs by product. The agent recognises the moment (step 1).",
     "Not applied: it changes what the rule reads; the frozen task accepts keep, move and meaning-preserving rewordings only. NOT RECOMMENDED: ground 'mistake' not found - the history of the file (11 commits, `git log --oneline -- product-guidelines/styleguide/SKILL.md`) and the remarks of PRs #50, #51 and #52 (`gh pr view <n> --comments`) hold no remark on this bullet; the ground is a cost only."),
    ("P2", 190, 197, "A reword that changes the rule's meaning: propose the decision adopting WCAG only where the product's log holds none, so that a refresh of an adopted styleguide does not propose it again.",
     "The accessibility bullet runs on every route that reaches step 4, a refresh with unchanged screens included, where a decision adopting WCAG already stands in the product's log.",
     "Not applied: it changes when the skill proposes a decision. NOT RECOMMENDED for now: not found in the same records as P1, and in the decision WAY-191 the proposal is stated without a condition on what the log already holds."),
]


def esc(text):
    return (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace("|", "&#124;"))


def quote(lines, s, e):
    body = "<br>".join(esc(l) for l in lines[s - 1:e])
    return f"[{PATH}:{s}-{e}]({LINK}#L{s}-L{e}): <code>{body}</code>"


def main(out):
    base = subprocess.run(["git", "-C", REPO, "show", f"{BASE}:{PATH}"], capture_output=True,
                          check=True).stdout.decode("utf-8")
    lines = base.split(NL)
    if lines and lines[-1] == "":
        lines.pop()
    covered = {}
    for i, (s, e, *_r) in enumerate(ROWS):
        for n in range(s, e + 1):
            if n in covered:
                raise SystemExit(f"line {n} is in rows {covered[n]} and {i}")
            covered[n] = i
    missing = [n for n, l in enumerate(lines, 1) if l.strip() and n not in covered]
    if missing:
        raise SystemExit(f"nonblank lines not in any row: {missing}")
    outl = ["# Assessment of `maintain-styleguide`", "",
            f"Base: `{PATH}` at commit {BASE[:7]} ({len(lines)} lines). Mode judge, kind skill, by "
            "`instruction-files/judging.md` and `instruction-files/kind_skill.md`. Each quote is "
            "the whole of the lines named, cut from the file at the base; a blank line inside a "
            "quote shows as an empty line break.", "",
            "Tools: Claude Code and Codex through the project entry points; Cursor through the "
            "shared layout. Sessions start in the-way's checkout or in a product that pins it. "
            "The frozen task accepts keep, move and meaning-preserving rewordings; a remove or a "
            "reword that changes a rule's meaning stands as a proposal and is not applied.", "",
            "Records searched for the mistakes the fragments are kept for: the git history of the "
            "file (`git log --oneline -- product-guidelines/styleguide/SKILL.md`, 11 commits), and "
            "the remarks of PRs #50, #51 and #52 (`gh pr view <n> --comments`; #51 has no "
            "comment and no review; #50 and #52 hold assessment tables of other files, and the "
            "only rows that mention a styleguide are about another file). No mistake that any "
            "fragment of this file was added for was found in them; where a row's ground is a "
            "mistake it says so, otherwise the ground is a carried decision or a cost.", ""]
    def block(title, path):
        with open(f"{path}", encoding="utf-8", newline="") as f:
            body = f.read().rstrip()
        return ["## " + title, "", "```", body, "```", ""]
    outl += block("1. Check script, before (base, `python -B instruction-files/check_instructions.py .`)",
                  OUTDIR + "check_instructions_before.txt")
    outl += block("1. Check script, after (this change, the same command, exit code 0)",
                  OUTDIR + "check_instructions_after.txt")
    outl += ["The check script follows the files the root `AGENTS.md` names; it does not reach this "
             "skill, so the warning on `AGENTS.md:21` (the folder `_zadania`, in the author's "
             "private notes) stands on the base and is not part of this change. It means the "
             "same in all three tools: a pointer to a folder not in the repository. The paths "
             "named by the rebuilt files were checked by hand, see the author's report.", ""]
    outl += ["## 2. Contradictions between files that load together", "",
             "Before: (a) `instruction-files/kind_skill.md:11` and `:13` give two answers for a "
             "fragment of one step that every use reaches ('every use needs it - it stays in "
             "`SKILL.md`' and 'only one step ... needs it - it stands in a file beside the "
             "skill'); WAY-256 gives the second. (b) Step 0 of the base skill (`:88-91`) tells the "
             "session to read all its files at the start, against WAY-127 and WAY-259, which have "
             "an entry point read a named file when the step that names it comes, and it has "
             "refine-task's `SKILL.md` and template read a second time. After: (a) is settled by "
             "the change to `kind_skill.md` (the first answer now says 'every step needs it', the "
             "second 'also where every use of the skill comes to that step'); (b) is settled by "
             "the pointers at steps 2 and 4 and the sentence at step 0. No other contradiction "
             "was found between `SKILL.md`, the files beside it, the two templates it names and "
             "`kind_skill.md`.", ""]
    outl += ["## 3. The table", "",
             "| Fragment (literal, whole, lines on 525cde1) | Needed when | Will the agent recognise "
             "that moment? | Verdict, reason and ground | New place |", "|---|---|---|---|---|"]
    for s_, e_, needed, rec, verdict, place in ROWS:
        outl.append("| " + " | ".join([quote(lines, s_, e_), esc(needed), esc(rec), esc(verdict),
                                       esc(place)]) + " |")
    outl += ["", "## Proposals (not applied)", "",
             "| No. | Fragment | Proposed change | Needed when / recognised | Verdict, reason and ground |",
             "|---|---|---|---|---|"]
    for no, s_, e_, change, when, verdict in PROPOSALS:
        outl.append("| " + " | ".join([no, quote(lines, s_, e_), esc(change), esc(when),
                                       esc(verdict)]) + " |")
    outl += ["", "Listed once more: " + "; ".join(f"{p[0]} (lines {p[1]}-{p[2]}): {p[3]}"
                                                  for p in PROPOSALS), ""]
    with open(out, "w", encoding="utf-8", newline=NL) as f:
        f.write(NL.join(outl) + NL)
    print(len(ROWS), "rows;", len(covered), "lines covered")


OUTDIR = "C:/Storage/repos/the-way/.runs/worktrees/styleguide-skill-shape/.runs/task-cycles/styleguide-skill-shape/reports/"

if __name__ == "__main__":
    main(sys.argv[1])

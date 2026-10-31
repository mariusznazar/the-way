"""Build reports/assessment.md: the judgement table of the base SKILL.md of maintain-testing-guidelines.

Each quote is cut from the file at the base commit, so it is literal; coverage and overlap of the
nonblank lines are checked before writing.
"""
import subprocess
import sys

REPO = "C:/Storage/repos/the-way/.runs/worktrees/testing-skill-shape"
BASE = "00c0a747272a9a179b7a855f256daff985ea2ee1"
PATH = "product-guidelines/testing/SKILL.md"
LINK = f"https://github.com/mariusznazar/the-way/blob/{BASE}/{PATH}"
NL = chr(10)
SCRATCH = "C:/Users/Mariusz/AppData/Local/Temp/claude/C--Storage-repos-the-way/2ccd66d4-d0c4-460a-9f99-587b25362648/scratchpad/"

ALWAYS = "Every use, from the first line; SKILL.md is read whole."
SEEN = "Yes - no moment to recognise: SKILL.md is read whole by every use."
NOMIST = "No mistake found for it (see the records searched)."

# (start, end, needed, recognised, verdict+reason+ground, new place)
ROWS = [
    (1, 4, ALWAYS + " The description is how the skill is matched, and the entry points are generated from it.",
     "Yes - it is the way in itself.",
     "KEEP. Needed in every use; carried: the entry points generated from this file (WAY-127, invariant skill-entry-points). Nothing in it belongs to one step. The description is unchanged, so `skill_entry_points.py --write` changes nothing.",
     "SKILL.md, unchanged."),
    (6, 16, ALWAYS, SEEN,
     "KEEP. The picture of the whole and the statement that the skill restates no rule of the templates; carried: WAY-35 (an element's skill holds only its order of work) and WAY-256 (SKILL.md keeps the picture of the whole).",
     "SKILL.md, unchanged."),
    (18, 22, ALWAYS + " It says where the files named below lie.", SEEN,
     "KEEP, with one sentence added (a pointer condition, not a rule: the files beside the skill are read when the step or variant that names them comes). Carried: WAY-127 and WAY-259.",
     "SKILL.md; the added sentence is listed under 'Text added that no base line carries'."),
    (24, 35, "Every use, at its start: where the skill runs and how it hands back to refine-task.", SEEN,
     "KEEP. Picture of the whole; carried: WAY-107, WAY-215, WAY-247 (the sentence that one task may carry coding and testing guidelines together stays here, as the task requires). Mentions steps 1, 2, 3 and 4 of refine-task, which every step relies on.",
     "SKILL.md, unchanged."),
    (37, 40, "Every step: what this skill writes and never writes, and what the cycle's author writes.", SEEN,
     "KEEP. A rule that holds across all steps (the skill never writes the foundation, the testing guidelines, tests or code); carried: WAY-01, WAY-28, WAY-08, WAY-172. Its columns are one table, not separable instructions.",
     "SKILL.md, unchanged."),
    (42, 45, "Every step that settles a meaning: 1 (a part missing from the map), 2, 3 and 4.", SEEN,
     "KEEP. A rule across steps: a meaning reaches the code only through the accepted task document; carried: WAY-172, WAY-124.",
     "SKILL.md, unchanged."),
    (47, 47, "The heading of the list that is written into the task document: step 4 (the answers) and step 5 (the check).",
     "Yes - the step 4 and step 5 pointers in SKILL.md name `task_document.md`.",
     "MOVE with its list (the heading is the title of the file; incoming wording 'What reaches the task document' in step 5 now reads 'what `task_document.md` names'). Carried: WAY-256.",
     "`task_document.md`."),
    (49, 50, "Every step that writes into the task document: steps 1 to 4 (and 2 for the research report paths).",
     SEEN,
     "KEEP, moved to the section 'Rules that hold across the steps' of SKILL.md: a rule of working that several steps keep must not stand in the file of one of them, or it stops reaching the others (task Question 2; WAY-256). REWORD (meaning-preserving): 'the document' became 'the task document', since the sentence no longer sits under the heading that gave 'document' its referent. Carried: WAY-256.",
     "SKILL.md, 'Rules that hold across the steps'."),
    (52, 61, "Step 4 (writing the answers into the task document) and step 5 (the check). Not steps 1 to 3: step 1 says itself that *To do* gains a part of the map, and step 3 says itself what stays in *Context*.",
     "Yes - the pointers at steps 4 and 5 name the file.",
     "MOVE. A list consulted at two steps only, with several instructions, so the exception does not keep it in SKILL.md. Cost: about 364 words out of the text read at steps 1 to 3. Carried: WAY-256, WAY-245, WAY-16, WAY-44, WAY-08, WAY-61. " + NOMIST,
     "`task_document.md`."),
    (62, 63, "As above, and only for a product's first guidelines: the condition is in the item's own words.",
     "As above; the item states its own condition.",
     "MOVE with its list. One instruction with a condition of its own, which then rides along on every use of the file; kept there on purpose, because a file of its own would trade one instruction for one pointer (WAY-256 exception). Carried: WAY-167.",
     "`task_document.md`."),
    (64, 64, "As above, and only where an audit ran (step 3): the condition is in the item's own words.",
     "As above; the item states its own condition.",
     "MOVE with its list; one instruction with its own condition, same reason as the row before. Carried: WAY-250.",
     "`task_document.md`."),
    (65, 72, "As above (step 4 writes the answers; step 5 checks them).", "As above.",
     "MOVE. Carried: WAY-134.", "`task_document.md`."),
    (73, 76, "As above.", "As above.",
     "MOVE. The entries come from steps 2 and 3, but they are written into the document with the other entries at step 4. Carried: WAY-250.",
     "`task_document.md`."),
    (77, 80, "Step 5 of refine-task builds the settlements; this skill's steps 4 and 5 know what to leave to it.", "As above.",
     "MOVE. Carried: WAY-134, WAY-44.", "`task_document.md`."),
    (82, 90, "Only when refine-task runs in orchestrated mode (a testing-guidelines task of a project plan led by lead-project), from step 1 on, since step 1 may put a question to the human.",
     "Yes - refine-task's own orchestrated mode is the moment (the refiner is dispatched with a conversation-file path); the pointer says so in those words, and the person who brought the case about is the project orchestrator, not the agent.",
     "MOVE. A variant: the whole section applies in one variant of the skill and to none of the others. Cost: about 98 words out of every non-orchestrated use. Carried: WAY-154, WAY-155, WAY-256.",
     "`orchestrated_mode.md`; SKILL.md keeps the heading and a pointer saying when to read it, before step 1."),
    (92, 98, "Step 0, bullet 1, by file. `product-guidelines/template.md` and `product-guidelines/testing/template.md`: the general template at step 4 (the decision adopting the template, departures, form of the guidelines file); the testing template at step 2 (the starting set and the recipes), at step 3 (charges measured against its rules) and at step 4 - on every route, also the route of 'A new level', which skips step 2. `project-level/task/skill/SKILL.md`, `project-level/task/template.md` and the section 'How a skill asks': already read by refine-task at its steps 1 and 2. The section 'Critique before collective review': step 4. `elements/common/critique/SKILL.md`: at the first critique, step 2 where research ran, else step 4.",
     "Yes - each is named at the step that needs it, as a pointer in SKILL.md (templates), in the research file or in `settle.md` (critique).",
     "SPLIT, by file. Both templates MOVE to the steps that use them (a rule across steps 2, 3 and 4 as the task's Question 2 and WAY-256 give: the step names the file, a later step has it read unless an earlier one did; the testing template is read before the first step that uses it on every route, the 'A new level' route included). The second reading of refine-task's `SKILL.md`, the task template and 'How a skill asks' is REMOVED: the frozen task's To do 2 accepts it (no rule is lost; the text was read at refine-task's steps 1 and 2), and the sentence ending step 0 (WAY-266) sends a session that did not read them to refine-task's steps 1 and 2. 'Critique before collective review' and critique `SKILL.md` MOVE to the critique they serve. Ground: cost (the base reads about 7800 words of other files at the start of every run) and carried decisions WAY-127, WAY-259, WAY-256, WAY-266. " + NOMIST,
     "SKILL.md steps 2, 3 and 4 (templates, with 'unless an earlier step did'); `research.md` and `settle.md` (critique files); SKILL.md step 0 states what refine-task has read and is not read again, and sends a session that did not read it to refine-task."),
    (99, 99, "Step 1, in the second bullet after the parts are named: it is what the product has for its tests that the step reads off. refine-task read of the root `AGENTS.md` only the section `## Backlog` (`read_sources.md:17`) and of `guidelines/` only the files whose *Applies to* names a touched part (`product-guidelines/reading.md:40`).",
     "Yes - it is the second bullet of step 1, after the parts are named, so recognition still comes first (WAY-248).",
     "MOVE. Needed for the recognition, not before it. REWORD (meaning-preserving): the root `AGENTS.md` is read whole, 'of which refine-task read only the section `## Backlog`', and the files of `guidelines/` are those 'that refine-task did not read at its step 1' - the set read after step 1 is the same as in the base. Carried: WAY-248. See proposal P1 (not applied), which narrows the reading and is a different change.",
     "`recognize.md`, second bullet."),
    (100, 104, "Step 1, after the parts are named: the decisions that settle the technology and those that adopt a tool, level, exemplar or exclusion serve steps 1, 2, 3 and 4; the trust boundaries serve steps 3 and 4 (and step 4 on every route).",
     "Yes - step 1.",
     "SPLIT and MOVE. The selection method, the section 'Reading the foundation' of `way_of_working.md` (492 words), is read by refine-task at its step 1 already and is not read again; what this sentence adds - the technology decisions, the decisions on a test tool, level, exemplar, exclusion or departure from the testing template, and the trust boundaries (WAY-48) - goes to step 1 as 'besides what refine-task selected', read once and kept in context for steps 2 to 4. Reading the boundaries at step 1 and not at step 3 is chosen because step 4 needs them on every route, the 'A new level' route included. Meaning preserved. Carried: WAY-150, WAY-48.",
     "`recognize.md`, second bullet."),
    (106, 112, "Step 1, first bullet: to name the parts that have tests.", "Yes - step 1.",
     "MOVE. The step is one procedure, a moment reached on every route; the task's Question 8 (WAY-256 unchanged) places each step's procedure beside the skill, also where every use reaches it. Carried: WAY-246, WAY-248, WAY-44.",
     "`recognize.md`, first bullet (the order of WAY-248 is kept: the parts are named before anything is read)."),
    (113, 115, "Step 1.", "Yes - step 1.", "MOVE, as the row before. Carried: WAY-248.", "`recognize.md`."),
    (116, 119, "Step 1, at its end: it sets the mode that steps 2 and 3 follow.", "Yes - step 1.",
     "MOVE, as the row before. Carried: WAY-244. The mode it gives is what the step 2 and step 3 pointers in SKILL.md refer to.", "`recognize.md`."),
    (120, 120, "Step 1, at its end: the mode of a task whose outcome is a test.", "Yes - step 1; the pointer at step 3 in SKILL.md names the same moment.",
     "MOVE, with REWORD (meaning-preserving, from the frozen task's To do 3 and `product-guidelines/reading.md:77-78`): the line named only 'the first test of a level' and the section 'A new level'. It now says that a level whose recipe already stands with an empty *Exemplar* takes the new-level case and no step 2, and that a level with no recipe is an extension (WAY-251) and takes step 2 as well. No further mode is added: the sentence on a level the cycle chooses is not a mode (see the row of lines 174-179). Carried: WAY-242, WAY-251.",
     "`recognize.md`; the step 3 pointer in SKILL.md."),
    (121, 122, "Step 1.", "Yes - step 1.", "MOVE, as the row before. Carried: WAY-249, WAY-251.", "`recognize.md`."),
    (123, 125, "Steps 1, 2 and 4: step 1 decides the mode by it, step 2 proposes recipes and a preferred tool, step 4 settles recipes and technology questions.", "Yes - SKILL.md is read whole.",
     "KEEP, moved from step 1 to the section 'Rules that hold across the steps' of SKILL.md, unchanged. A rule of working that three steps keep must not stand in the file of the first (task Question 2; WAY-256); `starting_set.md` and `settle.md` do not restate it. Carried: WAY-248, WAY-121, WAY-256.",
     "SKILL.md, 'Rules that hold across the steps'."),
    (127, 129, "Step 1 sets refresh or extension; step 2 acts on it (research or not) and step 3 audits again.", "Yes - step 1.",
     "MOVE. Defines the two words at the moment the mode is set; step 2 states its own consequence (research or no research) in its own file. Carried: WAY-251.",
     "`recognize.md`."),
    (131, 134, "Step 2, on every route that reaches it: the first guidelines, a refresh, an extension. Not the 'A new level' route.", "Yes - step 2; the pointer says which uses reach it.",
     "MOVE. Procedure of one step. Carried: WAY-244, WAY-249.", "`starting_set.md`."),
    (136, 139, "Step 2, on every route that reaches it.", "Yes - step 2.",
     "MOVE, with one sentence added: 'Word it as \"How to show\" in `SKILL.md` gives.' The preference question is a question in the sense of that rule, and the task requires 'How to show' to reach it (acceptance criteria); the rule itself stays in SKILL.md. Carried: WAY-249, WAY-174.",
     "`starting_set.md`."),
    (140, 150, "Step 2: the condition (the first guidelines where the human has no preference, every extension) and the refresh clause on every run that reaches step 2; the research instructions only where research runs - not at a refresh, nor where the human has a preference.",
     "Yes - the condition is the moment the agent meets after the preference question, and `starting_set.md` states it at that place.",
     "SPLIT. The research instructions (split into questions, fresh agents, sources, report paths) MOVE: a variant; cost about 232 words out of every run without research. The condition and the refresh clause stay in `starting_set.md`, since every run reaches them. Carried: WAY-249, WAY-251. See the row on the choice of Question 3.",
     "`research.md`; the condition and the refresh clause in `starting_set.md`; SKILL.md step 2 names `research.md` too."),
    (151, 156, "Step 2, only where research ran, once the reports are in.", "Yes - it follows the research in the same file.",
     "MOVE with the research. REWORD (meaning-preserving): 'Where research ran' became 'Once the reports are in', since the file is read only where research runs; plus a sentence 'Before the first critique of the session, read `elements/common/critique/SKILL.md`', which replaces the read at step 0. Carried: WAY-249, WAY-120.",
     "`research.md`."),
    (158, 160, "Step 3, only where the product has tests and step 1 gave the audit.", "Yes - the mode step 1 gives names it, and the step 3 pointer in SKILL.md repeats the condition.",
     "MOVE. A step reached only by runs with tests. Carried: WAY-250. The heading stays in SKILL.md as the pointer; line 160 is the first line of `audit.md`.",
     "`audit.md`; the condition stays in SKILL.md at the step 3 pointer."),
    (162, 171, "Step 3 (audit).", "Yes.", "MOVE with the step. Carried: WAY-242, WAY-250.", "`audit.md`."),
    (172, 173, "Step 3 (audit); the boundaries are also needed at step 4, whose own text asks for an invariant for each.", "Yes.",
     "MOVE with the step. Carried: WAY-250, WAY-235.", "`audit.md`."),
    (174, 179, "The first sentence: step 3, only where the task's required outcome is itself the first test of a level, not on an audit run. The last sentence (where the level of a task's tests is its cycle's choice): step 4, where the exemplars of every route are settled.",
     "Yes for the first (step 1 sets the mode and the pointer at step 3 names it); yes for the last (it stands in the exemplar item of `settle.md`, which every route reads).",
     "SPLIT. The first sentence MOVEs to `new_level.md`, a variant with a condition of its own that would ride along on every audit run if it stayed in `audit.md`, and that the 'A new level' route must reach without the audit (task acceptance criteria). The last sentence moves unchanged to the exemplar item of `settle.md`: its condition ('the level of a task's tests is its cycle's choice') holds on every route that has tests to write, so it cannot stand in a file read only on the new-level route; it is a move the task accepts. Carried: WAY-242, WAY-241, WAY-238, WAY-172. See P2 (not applied) on the clause that the recipe 'comes into being' with the test.",
     "`new_level.md` (first sentence; SKILL.md step 3 names it); `settle.md`, exemplar item (last sentence)."),
    (180, 183, "Step 3 (audit): a choice found in the product's tests.", "Yes.",
     "MOVE with the step; the rule that every choice goes to the human at step 4 is in SKILL.md ('How to show'). Carried: WAY-29.", "`audit.md`."),
    (185, 185, "Step 4.", "Yes.", "KEEP the heading in SKILL.md as the pointer of step 4.", "SKILL.md, the step 4 pointer."),
    (187, 194, "Every step in which the skill puts a choice to the human: the preference question at step 2, the choices at step 4, and step 1 where the identifier of a part is a question. Not step 4 alone.",
     "Yes - SKILL.md is read whole.",
     "KEEP, moved from step 4 to the section 'Rules that hold across the steps' of SKILL.md. A rule of working that several steps keep (task Question 2; WAY-256) placed in the file of one of them silently stops reaching the others; the task's acceptance criteria require it at the preference question of step 2. The step 4 pointer names it by `settle.md`'s use of it; step 2's file points to it by name. Carried: WAY-174, WAY-113, WAY-256.",
     "SKILL.md, 'Rules that hold across the steps'; `starting_set.md` points to it."),
    (195, 200, "Step 4, only for a new tool or library left as a technology question of the task (step 1 records it).",
     "Yes - the agent recorded the question itself at step 1; `settle.md` names the condition.",
     "MOVE. A variant with a condition of its own that would ride along on every use if it stayed in the step's file; several instructions (show by consequences, recommend with the weak point, keep the preferred tool, leave the choice). Carried: WAY-248, WAY-249, WAY-123, WAY-121. See the row on the choice of Question 3.",
     "`new_tools.md`; one pointer in `settle.md`; SKILL.md step 4 names `new_tools.md` too."),
    (201, 221, "Step 4, every run.", "Yes - step 4.",
     "MOVE with the step. REWORD (meaning-preserving): 'a new level of \"A new level\"' became 'a new level of step 3 (`new_level.md`)', since the section no longer carries that name; the last sentence of lines 174-179 lands in the exemplar item, unchanged. Carried: WAY-173, WAY-240, WAY-226, WAY-232, WAY-241, WAY-242, WAY-237, WAY-235, WAY-236, WAY-252.",
     "`settle.md`."),
    (222, 235, "Step 4, every run.", "Yes.", "MOVE with the step. Carried: WAY-168, WAY-235, WAY-61, WAY-08, WAY-48, WAY-51.", "`settle.md`."),
    (236, 242, "Step 4, when a choice is proposed.", "Yes.", "MOVE with the step. Carried: WAY-237, WAY-235, WAY-228.", "`settle.md`."),
    (243, 244, "Step 4, once the set of proposals is complete.", "Yes.",
     "MOVE with the step, with the pointer to the critique files added ('Read that section and, unless step 2 did, `elements/common/critique/SKILL.md`'), which replaces the read at step 0. Carried: WAY-120.",
     "`settle.md`."),
    (245, 246, "Every step that asks the human a question and writes the answer: steps 1, 2 and 4.", "Yes - SKILL.md is read whole.",
     "KEEP, moved to 'Rules that hold across the steps' (one instruction that holds across steps; in the file of step 4 it would not reach steps 1 and 2). Carried: refine-task step 3, WAY-134, WAY-256.",
     "SKILL.md, 'Rules that hold across the steps'."),
    (248, 251, "Step 5, the end of every run that reaches it.", "Yes - step 5.",
     "MOVE. Two instructions (check, hand back), so the exception does not keep them. REWORD (meaning-preserving): the reference to the section 'What reaches the task document' became 'what `task_document.md` beside this skill names'. Carried: WAY-172.",
     "`hand_back.md`; SKILL.md step 5 names it and `task_document.md`."),
    (252, 254, "Step 5.", "Yes.", "MOVE with the step. Carried: WAY-134.", "`hand_back.md`."),
]

CHOICE_ROWS = [
    ("Q3. A step's file points on to a variant file, and SKILL.md names that file at the step too (task Question 3; WAY-265). Fragments concerned: lines 140-156 (research, row 'lines 140-150' and 'lines 151-156') and lines 195-200 (new tools); quoted in those rows, not again here.",
     "Whenever a run reaches step 2 or step 4: the step's file says when the variant is read.",
     "Yes - the pointer in SKILL.md at the step names the file and its condition ('where the human has no preference at the first guidelines, and at every extension', 'for each new tool or library left as a technology question'), in the words an agent meets the moment in; the step's file repeats the condition at the place where the agent needs the file.",
     "CHOICE, applied. The base has no layout of this kind. Two levels as in the styleguide skill (SKILL.md names only the step's file) were rejected by the task: they leave the layout at odds with the rule of references one level deep. Variants left in the step's file were rejected too: every run would carry about 232 words of research and 69 of new tools it does not use. Cost kept: the file name stands in two places and about 30-45 words more stand in SKILL.md. Ground: the environment fact `claude-skill-nested-references`; carried: WAY-256, WAY-265, WAY-258. The audit and the new-level case are not an instance of this choice: SKILL.md names both files directly at step 3, so neither agent reads the other's file.",
     "`starting_set.md` -> `research.md`; `settle.md` -> `new_tools.md`; both also named in SKILL.md."),
]

ADDED = [
    ("SKILL.md, step 0, last sentences", "A session that has not read them in this conversation - it opened this skill directly, or resumed the work in a new one - goes through `refine-task` steps 1 and 2 first (WAY-266).",
     "Task Question 4 and To do 6; the wording is the task's, with the decision cited. The same sentence ends step 0 of `product-guidelines/styleguide/SKILL.md`."),
    ("SKILL.md, step 0, the list of what refine-task read", "Added 'the guidelines of the parts the task touches': refine-task reads them by `product-guidelines/reading.md:40` (task To do 2).",
     "True of refine-task's step 1; keeps step 1 of this skill from reading them again."),
    ("SKILL.md, steps 1 to 5", "Pointers 'read `X.md` beside this skill' with the condition of each, 'in full unless step 2 did' for the testing template (steps 3, 4), 'unless an earlier step did' (step 4) and 'unless step 4 did' (step 5) for `task_document.md`.",
     "Task To do 2, 3 and 5; WAY-256, WAY-265."),
    ("`recognize.md`, mode list", "The new-level mode as in the row of line 120 (the recipe standing with an empty *Exemplar*; no recipe, an extension).", "Task To do 3."),
    ("`starting_set.md`", "'Word it as \"How to show\" in `SKILL.md` gives.'", "Task acceptance criteria."),
    ("`research.md`", "'Before the first critique of the session, read `elements/common/critique/SKILL.md`.'", "Replaces the read at step 0; task To do 2."),
    ("`settle.md`", "'Read that section and, unless step 2 did, `elements/common/critique/SKILL.md`.'", "Replaces the read at step 0; task To do 2."),
]

PROPOSALS = [
    ("P1", 99, 99, "A reword that changes the rule's meaning: read from the product's `guidelines/` only the file for the part the task covers and the index of the coding guidelines, instead of every file under it, and the root `AGENTS.md` by its sections.",
     "Step 1. refine-task already read the guidelines of the parts the task touches (`product-guidelines/reading.md:40`), so the wider reading may repeat that and add what testing does not need; it costs the product's words and differs by product. The agent recognises the moment (step 1).",
     "Not applied: it changes what the rule reads; the frozen task accepts keep, move and meaning-preserving rewordings only. NOT RECOMMENDED: ground 'mistake' not found in the records searched, and the ground is a cost only."),
    ("P2", 174, 179, "A reword that adds meaning: 'the level's recipe comes into being with it, or, where the recipe already stands with an empty *Exemplar*, takes its exemplar with it'.",
     "Step 3, new-level case. The route of a recipe that already stands (`product-guidelines/reading.md:77-78`) reads 'the level's recipe comes into being with it', which is true only of a level with no recipe, the extension route. The agent recognises the moment (step 3).",
     "Not applied: it adds a case to the rule's wording, beyond keep, move and meaning-preserving rewordings. RECOMMENDED for the human's decision at the request: the sentence as it stands can be read as saying that the recipe is written even where it stands; ground: a cost of misreading, mistake not found in the records searched."),
]


def esc(text):
    return (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace("|", "&#124;"))


def quote(lines, s, e):
    body = "<br>".join(esc(l) for l in lines[s - 1:e])
    return f"[{PATH}:{s}-{e}]({LINK}#L{s}-L{e}): <code>{body}</code>"


def block(title, path):
    with open(path, encoding="utf-8", newline="") as f:
        body = f.read().rstrip()
    return ["## " + title, "", "```", body, "```", ""]


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
    outl = ["# Assessment of `maintain-testing-guidelines`", "",
            f"Base: `{PATH}` at commit {BASE[:7]} ({len(lines)} lines, 3042 words). Mode judge, kind "
            "skill, by `instruction-files/judging.md` and `instruction-files/kind_skill.md`. Each quote "
            "is the whole of the lines named, cut from the file at the base; a blank line inside a "
            "quote shows as an empty line break. `kind_skill.md` at the base does not answer the "
            "case of a fragment some steps need, not all; the fragments of that kind are judged by "
            "the wording of Question 2 of the frozen task (task Question 9), which this change "
            "writes into `kind_skill.md` as its third answer (WAY-256).", "",
            "Tools: Claude Code and Codex through the project entry points; Cursor through the "
            "shared layout. Sessions start in the-way's checkout or in a product that pins it. "
            "The frozen task accepts keep, move and meaning-preserving rewordings; a remove or a "
            "reword that changes a rule's meaning stands as a proposal and is not applied.", "",
            "Records searched for the mistakes the fragments are kept for: the git history of the "
            "file (`git log --oneline -- product-guidelines/testing/SKILL.md`, 5 commits: 2b5b1c0, "
            "a2f1165, a6453b7, 5d1ebb8, c6ee066, by their messages) and the remarks of PRs #50, "
            "#51, #52, #59 and #60 (`gh pr view <n> --comments`; the pull-request comments and "
            "reviews of each through `gh api repos/mariusznazar/the-way/pulls/<n>/comments` and "
            "`/reviews` hold nothing; #51 has no comment at all; #50, #52, #59 and #60 hold "
            "assessment tables of other files and the cycle's remarks, and none of their texts "
            "mentions this skill or its file). No mistake that any fragment of this file was added "
            "for was found in them; where a row's ground is a mistake it says so, otherwise the "
            "ground is a carried decision or a cost.", ""]
    outl += block("1. Check script, before (base, `python -B instruction-files/check_instructions.py .` on an export of 00c0a74)",
                  SCRATCH + "check_before.txt")
    outl += block("1. Check script, after (this change, the same command, exit code 0; the output is identical)",
                  SCRATCH + "check_after.txt")
    outl += ["The check script follows the files the root `AGENTS.md` names; it does not reach this "
             "skill, so the warning on `AGENTS.md:21` (the folder `_zadania\\`, in the author's "
             "private notes) stands on the base and is not part of this change. It means the same in "
             "all three tools: a pointer to a folder not in the repository. The paths named by the "
             "rebuilt files were checked by hand and by `tools/verify_reports.py`, see the "
             "author's report.", ""]
    outl += ["## 2. Contradictions between files that load together", "",
             "Before: (a) `instruction-files/kind_skill.md:11` and `:13` give two answers for a "
             "fragment, 'every step needs it' and 'only one step or one variant needs it', and none "
             "for a fragment that some steps need, not all, such as the testing template (steps 2, "
             "3, 4) or the critique instruction (2, 4). (b) Step 0 of the base skill (`:94-104`) "
             "tells the session to read all its files at the start, against WAY-127 and WAY-259, "
             "which have an entry point read a named file when the step that names it comes, and "
             "it has refine-task's `SKILL.md`, the task template and two sections of the way of "
             "working read a second time. (c) `product-guidelines/reading.md:77-78` limits the "
             "case of a level's first test to a recipe that stands with an empty *Exemplar*, while "
             "the base skill's line 120 and its section 'A new level' speak of 'the first test of "
             "a level' and of a recipe that 'comes into being with it'. After: (a) is settled by "
             "the third answer of `kind_skill.md` (WAY-256); (b) by the pointers at steps 2 to 5 "
             "and the sentence ending step 0 (WAY-266); (c) in the mode list of `recognize.md` "
             "(the new-level case and the extension), except that the sentence 'the level's recipe "
             "comes into being with it' in `new_level.md` stands as in the base and is proposal P2. "
             "No other contradiction was found between `SKILL.md`, the files beside it, the two "
             "templates it names and `kind_skill.md`.", ""]
    outl += ["## 3. The table", "",
             "| Fragment (literal, whole, lines on 00c0a74) | Needed when | Will the agent recognise "
             "that moment? | Verdict, reason and ground | New place |", "|---|---|---|---|---|"]
    for s_, e_, needed, rec, verdict, place in ROWS:
        outl.append("| " + " | ".join([quote(lines, s_, e_), esc(needed), esc(rec), esc(verdict),
                                       esc(place)]) + " |")
    outl += ["", "## The choice of Question 3 (a row of its own)", "",
             "| Choice | Needed when | Will the agent recognise that moment? | Verdict, reason and ground | New place |",
             "|---|---|---|---|---|"]
    for ch, needed, rec, verdict, place in CHOICE_ROWS:
        outl.append("| " + " | ".join([esc(ch), esc(needed), esc(rec), esc(verdict), esc(place)]) + " |")
    outl += ["", "## Text added that no base line carries", "",
             "| Where | Text | Ground |", "|---|---|---|"]
    for w, t, g in ADDED:
        outl.append("| " + " | ".join([esc(w), esc(t), esc(g)]) + " |")
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


if __name__ == "__main__":
    main(sys.argv[1])

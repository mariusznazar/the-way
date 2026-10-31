"""Build reports/assessment.md: the judgement table of the base SKILL.md of maintain-coding-guidelines.

Each quote is cut from the file at the base commit, so it is literal; coverage and overlap of the
nonblank lines are checked before writing.
"""
import subprocess
import sys

REPO = "C:/Storage/repos/the-way/.runs/worktrees/coding-skill-shape"
BASE = "f86fd71f3cb72a9eb1620c388af44bbd1198fb4a"
PATH = "product-guidelines/coding/SKILL.md"
LINK = f"https://github.com/mariusznazar/the-way/blob/{BASE}/{PATH}"
NL = chr(10)
BS = chr(92)
R = "C:/Storage/repos/the-way/.runs/task-cycles/coding-skill-shape/reports/"

ALWAYS = "Every use, from the first line; SKILL.md is read whole."
SEEN = "Yes - no moment to recognise: SKILL.md is read whole by every use."
NOMIST = "Mistake: not found in the records searched (see above)."
D4 = "Steps 4 and 5 (step 4 writes the answers into the task document; step 5 checks them)."
R4 = "Yes - the pointers at steps 4 and 5 name the file."
CRIT = "Step 4, and step 2 where research ran."

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
     "KEEP. Picture of the whole (task acceptance criteria: stays in SKILL.md); carried: WAY-107, WAY-215, WAY-247 (the sentence that one task may carry coding and testing guidelines together stays here). Mentions steps 1, 2, 3 and 4 of refine-task, which every step relies on.",
     "SKILL.md, unchanged."),
    (37, 40, "Every step: what this skill writes and never writes, and what the cycle's author writes.", SEEN,
     "KEEP. A rule that holds across all steps (the skill never writes the foundation, the coding guidelines, code); carried: WAY-01, WAY-28, WAY-08, WAY-172. The table is one fragment, not separable instructions.",
     "SKILL.md, unchanged."),
    (42, 45, "Every step that settles a meaning: 1 (a part missing from the map), 2, 3 and 4.", SEEN,
     "KEEP. A rule across steps: a meaning reaches the code only through the accepted task document; carried: WAY-172, WAY-124.",
     "SKILL.md, unchanged."),
    (47, 47, D4, R4,
     "MOVE with its list: the heading is the title of the file. Incoming references: SKILL.md steps 4 and 5 and `hand_back.md` name `task_document.md`; the section 'Writing the files' of `product-guidelines/coding/template.md`, which product task documents name through the first *To do* item, is not moved. Carried: WAY-256.",
     "`task_document.md`, heading."),
    (49, 50, "Every step that writes into the task document: steps 1 to 4 (step 2 for the paths of the research reports).", SEEN,
     "KEEP, moved to 'Rules that hold across the steps' of SKILL.md: a rule of working that several steps keep must not stand in the file of one of them, or it stops reaching the others (WAY-256). REWORD (meaning-preserving): 'the document' became 'the task document', since the sentence no longer sits under the heading that gave 'document' its referent.",
     "SKILL.md, 'Rules that hold across the steps', first bullet."),
    (52, 55, D4, R4,
     "MOVE. The first item of a list consulted at two steps, with several instructions, so the exception does not keep it in SKILL.md. Cost: the whole list is about 489 words out of the text read at steps 1 to 3. Carried: WAY-256, WAY-171. " + NOMIST,
     "`task_document.md`, first item."),
    (56, 58, D4, R4, "MOVE with its list. Carried: WAY-256. " + NOMIST, "`task_document.md`."),
    (59, 60, D4 + " Only where the task brings a formatter to code it would rewrite: the condition is in the item's own words.",
     "As above; the item states its own condition.",
     "MOVE with its list. One instruction with a condition of its own, which then rides along in a file read at steps 4 and 5 on every route; kept there because a file of its own would trade one instruction for one pointer (WAY-256, the exception). Carried: WAY-205.",
     "`task_document.md`."),
    (61, 62, D4, R4, "MOVE. Carried: WAY-08, WAY-61.", "`task_document.md`."),
    (63, 66, D4, R4, "MOVE. Carried: WAY-212, WAY-16.", "`task_document.md`."),
    (67, 69, D4, R4, "MOVE. Carried: WAY-44.", "`task_document.md`."),
    (70, 71, D4 + " Only for a product's first guidelines: the condition is in the item's own words.",
     "As above; the item states its own condition.",
     "MOVE with its list; one instruction with its own condition, same reason as two rows above. Carried: WAY-167.",
     "`task_document.md`."),
    (72, 72, D4 + " Only where an audit ran (step 3): the condition is in the item's own words.",
     "As above; the item states its own condition.",
     "MOVE with its list; one instruction with its own condition. The item names step 3 for what the audit calls for.",
     "`task_document.md`."),
    (73, 79, D4, R4, "MOVE. Carried: WAY-134.", "`task_document.md`."),
    (80, 84, D4 + " The evidence comes from steps 2 and 3 but is written with the other entries.", R4,
     "MOVE. Carried: WAY-204, WAY-200, WAY-201.", "`task_document.md`."),
    (85, 88, "Step 5 of refine-task builds the settlements; this skill's steps 4 and 5 know what to leave to it.", R4,
     "MOVE. Carried: WAY-134, WAY-44.", "`task_document.md`."),
    (90, 90, "Before step 1, on the one condition below: the heading of the variant.", "Yes - the heading stays in SKILL.md with the pointer.",
     "KEEP, as the heading of the pointer. Carried: WAY-265's rule that a variant is named in SKILL.md.",
     "SKILL.md."),
    (92, 99, "Only when refine-task runs in orchestrated mode (a coding-guidelines task of a project plan led by lead-project), from step 1 on, since step 1 may put a question to the human.",
     "Yes - the case is brought about by the project orchestrator, which dispatches the refiner with a conversation-file path; the pointer says so in those words, as the pointers of the testing and styleguide skills do.",
     "MOVE. A variant: the whole section applies in one variant of the skill and to none of the others. Cost: about 113 words out of every non-orchestrated use. Carried: WAY-154, WAY-155, WAY-256. Task question 2: its own file, not merged with the other two disciplines'.",
     "`orchestrated_mode.md`; SKILL.md keeps the heading and a pointer saying when to read it, before step 1."),
    (101, 101, ALWAYS, SEEN, "KEEP, the heading of step 0, whose text is reworded (next rows).", "SKILL.md."),
    (103, 107, "By file. `product-guidelines/template.md` and `product-guidelines/coding/template.md`: the general template at step 4; the coding template at step 2, at step 3 (`trial_run.md`, `kinds.md`) and at step 4 - on every route, also 'A new kind' and the route of one kind, which skip step 2. `project-level/task/skill/SKILL.md`, `project-level/task/template.md` and 'How a skill asks': already read by refine-task at its steps 1 and 2. 'Critique before collective review': step 4. `elements/common/critique/SKILL.md`: at the first critique, step 2 where research ran, else step 4.",
     "Yes - each is named at the step that needs it: the templates by a pointer in SKILL.md, the critique files in `research.md` and `settle.md`.",
     "SPLIT, by file. The two templates MOVE to the steps that use them (WAY-256: the step names the file; a later step has it read unless an earlier one did; the coding template is read before the first step that uses it on every route). The second reading of refine-task's `SKILL.md`, the task template and 'How a skill asks' is REMOVED as task To do 2 accepts: no rule is lost, the text was read at refine-task's steps 1 and 2, and the sentence ending step 0 (WAY-266) sends a session that did not read it there. 'Critique before collective review' and the critique `SKILL.md` MOVE to the critique they serve. Ground: cost (the base reads about 7200 words of other files at the start of every run) and carried decisions WAY-127, WAY-259, WAY-256, WAY-266. " + NOMIST,
     "SKILL.md steps 2, 3, 4 (templates); `research.md` and `settle.md` (critique files); SKILL.md step 0 states what refine-task read and sends a session that did not read it to refine-task."),
    (108, 108, "Step 1, after the parts are named. refine-task read of the root `AGENTS.md` only the section `## Backlog` (`read_sources.md:17`) and of `guidelines/` only the files whose *Applies to* names a touched part (`product-guidelines/reading.md:40`).",
     "Yes - it is the second bullet of step 1, after the parts are named, so recognition still comes first (WAY-210).",
     "MOVE. Needed for the recognition, not before it. REWORD (meaning-preserving): the root `AGENTS.md` is read whole, 'of which refine-task read only the section ## Backlog', and the files of `guidelines/` are those 'that refine-task did not read at its step 1': the set read after step 1 is the same as in the base. See proposal P2 (not applied), which narrows the reading. " + NOMIST,
     "`recognize.md`, second bullet."),
    (109, 112, "Step 1: the decisions that settle the product's technology and those that adopt a standing check, a set of rules or an exemplar serve steps 1 to 4.",
     "Yes - second bullet of step 1.",
     "MOVE. REWORD (meaning-preserving): 'besides what refine-task selected at its step 1', since refine-task has already selected the foundation by 'Reading the foundation' (task To do 2: only the entries added at step 0 come in). Carried: WAY-150. " + NOMIST,
     "`recognize.md`, second bullet."),
    (114, 114, "Step 1.", "Yes.", "KEEP, the heading of step 1.", "SKILL.md."),
    (116, 119, "Step 1, first: naming the parts that hold code.", "Yes - first bullet of step 1.",
     "MOVE. Carried: WAY-208, WAY-210 (recognition comes before anything else). Order of step 1 kept: the parts are named first.",
     "`recognize.md`, first bullet."),
    (120, 123, "Step 1, after the reading.", "Yes.", "MOVE. Carried: WAY-210, WAY-231.", "`recognize.md`, third bullet."),
    (124, 130, "Step 1, to give the mode on which steps 2 to 5 depend; modes combine.",
     "Yes - the pointer at step 1 says the file gives the mode of the work.",
     "MOVE with the fifth mode added by task To do 9 (listed under 'Text added that no base line carries'); the four modes are unchanged. The fifth mode is compared with the base by what it selects: a kind whose files exist, with no index row, where `guidelines/coding.md` stands and the task neither refreshes nor extends; the base reaches no step for it. Carried: WAY-216, WAY-209.",
     "`recognize.md`, mode list."),
    (131, 133, "Every step: rules go to the linter the product runs; a new tool is a technology question (also step 4, and the route 'A new kind').", SEEN,
     "KEEP, moved to 'Rules that hold across the steps' of SKILL.md: it holds in steps 1, 2 and 4 and on every route, so it must not stand in the file of one step (task acceptance criteria). Carried: WAY-210, WAY-121.",
     "SKILL.md, 'Rules that hold across the steps'."),
    (135, 137, "Step 1 (to give the mode) and step 2 (to decide on research).", "Yes - they follow the mode list.",
     "MOVE. Carried: WAY-251. Cost: 45 words out of steps 3 to 5.", "`recognize.md`, last paragraph."),
    (139, 139, "Step 2.", "Yes.", "KEEP, the heading of step 2.", "SKILL.md."),
    (141, 142, "Step 2: before the first code, for code that has no coding guidelines yet, and at every refresh or extension.",
     "Yes - the pointer at step 2 names all three conditions, and says that 'code that has no coding guidelines yet' means the product's code with no `guidelines/coding.md`, not a kind of code without a file of its own (task acceptance criteria).",
     "SPLIT. The sentence stays whole as the opening of `starting_set.md` (WAY-209, WAY-210, WAY-211); the pointer at step 2 in SKILL.md carries its conditions in the words an agent meets the moment in. Compared by what each selects: the three conditions are the base's three, no route added or lost.",
     "`starting_set.md`, opening; SKILL.md step 2 pointer."),
    (144, 147, "Step 2, first: the question of the human's preferences.", "Yes - the first bullet of `starting_set.md`.",
     "MOVE; one sentence added, 'Word it as \"How to show\" in SKILL.md gives' (task acceptance criteria: How to show reaches the question of preferences). Carried: WAY-211.",
     "`starting_set.md`, first bullet."),
    (148, 156, "Step 2. The condition of research and the rule of the refresh: step 2 on every route that reaches it. The procedure of research: only where research runs (first guidelines without a preference, every extension).",
     "Yes - the pointer at step 2 and `starting_set.md` both name `research.md` with its condition (WAY-265).",
     "SPLIT. The condition, the refresh sentence (lines 149-150) and a connective MOVE to `starting_set.md` (task acceptance criteria: the refresh sentence stands there, not in `research.md`); 'Give each standing check to a fresh agent ...' to its report path MOVES to `research.md` (a variant). Cost: `research.md` is 197 words (with the row below), out of every run that does no research. Carried: WAY-211, WAY-251, WAY-256, WAY-265. " + NOMIST,
     "`starting_set.md` second bullet; `research.md`, first paragraph."),
    (157, 162, "Only where research ran: the critique of its reports.", "Yes - `research.md` is read where research runs.",
     "MOVE. REWORD (meaning-preserving): 'Where research ran' became 'Once the reports are in', since the file is read only where research runs. Sentence added: 'Before the first critique of the session, read elements/common/critique/SKILL.md' (replaces the read at step 0; task To do 2). Carried: WAY-211, WAY-120.",
     "`research.md`, last paragraph."),
    (163, 165, "Step 2 on every route that reaches it, also where preferences supplied the tool and no research ran: a product with no code.",
     "Yes - it is the last bullet of `starting_set.md`, which every route of step 2 reads.",
     "MOVE to `starting_set.md`, not `research.md` (task acceptance criteria): the rule reaches the route with the human's preference, on which there is no research. Carried: WAY-204.",
     "`starting_set.md`, last bullet."),
    (167, 167, "Step 3.", "Yes.", "KEEP, the heading of step 3.", "SKILL.md."),
    (169, 169, "Step 3, the condition of the trial run and of the kinds.", "Yes.",
     "REWORD (meaning-preserving). The condition 'where the product has code' stays at the head of `trial_run.md` and `kinds.md`; SKILL.md step 3 combines it with what step 1 gave (code and no guidelines, or a refresh or extension: both files; the route of one kind: `kinds.md` alone). It no longer governs 'A new kind' (task acceptance criteria).",
     "`trial_run.md`, `kinds.md`; SKILL.md step 3 pointer."),
    (171, 176, "Step 3, where step 1 gave the trial run: code and no guidelines, or a refresh or extension. Not on the routes of no code, 'A new kind' and one kind.", "Yes - the pointer at step 3 names the file and the condition.",
     "MOVE. A variant. Cost: about 249 words out of every run with no trial run. Carried: WAY-204, WAY-256. " + NOMIST,
     "`trial_run.md`."),
    (177, 182, "As above.", "As above.", "MOVE. Carried: WAY-204.", "`trial_run.md`."),
    (183, 186, "As above.", "As above.", "MOVE. Carried: WAY-205.", "`trial_run.md`."),
    (187, 196, "Step 3, where step 1 gave the audit of every kind, or the comparison of one kind (To do 9). Not on 'A new kind' or the route of no code.",
     "Yes - the pointer at step 3 names the file and the conditions.",
     "MOVE; one sentence added for the route of one kind, at 'the audit covers every one of them' (task To do 12): the comparison covers that kind alone and is no audit under WAY-201. Cost: about 195 words out of runs with no kinds step. Carried: WAY-200, WAY-201, WAY-198, WAY-256. " + NOMIST,
     "`kinds.md`."),
    (197, 199, "Step 3, on the route 'A new kind': the task that creates the first file of a kind of code, also in a product with no code.",
     "Yes - the mode list of step 1 and the paragraph at step 3 say it in the same words.",
     "KEEP in SKILL.md: one instruction of one variant, which would otherwise stand in a file with a pointer to it (WAY-256, the exception). Its condition does not depend on 'Where the product has code:' (task acceptance criteria): the first file of a kind can arise in a product with no code (WAY-200, WAY-209). Carried: WAY-200, WAY-209.",
     "SKILL.md step 3."),
    (200, 202, "Step 3, and step 4 (proposals): on every route that proposes, also 'A new kind' and the route of one kind.", SEEN,
     "KEEP, moved to 'Rules that hold across the steps' of SKILL.md (task acceptance criteria: it reaches every route). A rule of working across steps. Carried: WAY-29.",
     "SKILL.md, 'Rules that hold across the steps'."),
    (204, 204, "Step 4.", "Yes.", "KEEP, the heading of step 4.", "SKILL.md."),
    (206, 215, "Steps 2 (the question of preferences), 4 (each choice) and, in a weaker sense, the new tools.", SEEN,
     "KEEP, moved to 'Rules that hold across the steps' of SKILL.md (a rule of working that the agent keeps at steps 2 and 4, so it must not stand in the file of step 4; task acceptance criteria). Carried: WAY-174, WAY-113.",
     "SKILL.md, 'Rules that hold across the steps'."),
    (216, 221, "Step 4, only for each new tool or library left as a technology question of the task.", "Yes - `settle.md` and SKILL.md step 4 name the file with that condition (WAY-265).",
     "MOVE. A variant. Cost: about 69 words out of every run with no new tool. Carried: WAY-210, WAY-211, WAY-123, WAY-121, WAY-256, WAY-265, WAY-268. " + NOMIST,
     "`new_tools.md`; named in `settle.md` and in SKILL.md step 4."),
    (222, 236, "Step 4 (and step 5 reads it back through the task document).", "Yes - `settle.md`.",
     "MOVE. The procedure of one step. Carried: WAY-202, WAY-203, WAY-204, WAY-206, WAY-198, WAY-199, WAY-200, WAY-201, WAY-173. On the route of one kind only the item about the kind's exemplar applies (task To do 10); `settle.md` says so in its opening. " + NOMIST,
     "`settle.md`."),
    (237, 252, "Step 4.", "Yes - `settle.md`.", "MOVE. Carried: WAY-168, WAY-202, WAY-203, WAY-205, WAY-207, WAY-198, WAY-61. " + NOMIST, "`settle.md`."),
    (253, 260, "Step 4, when a choice is proposed.", "Yes.", "MOVE. Carried: WAY-204, WAY-206.", "`settle.md`."),
    (261, 262, "Step 4, once the set of proposals is complete.", "Yes.",
     "MOVE. REWORD (meaning-preserving): adds 'Read that section and, unless step 2 did, elements/common/critique/SKILL.md', replacing the read at step 0 (task To do 2). Carried: WAY-120.",
     "`settle.md`, last bullet."),
    (263, 264, "Steps 1 to 4: every step that puts a question to the human.", SEEN,
     "KEEP, moved to 'Rules that hold across the steps' of SKILL.md: a rule of working across steps. Carried: WAY-113.",
     "SKILL.md, 'Rules that hold across the steps'."),
    (266, 266, "Step 5.", "Yes.", "KEEP, the heading of step 5.", "SKILL.md."),
    (268, 270, "Step 5.", "Yes - the pointer at step 5 names `hand_back.md`.",
     "MOVE. REWORD (meaning-preserving): '\"What reaches the task document\"' became '`task_document.md` beside this skill', since that section is now a file. Carried: WAY-202, WAY-256. Contradiction with the route 'A new kind' stays as proposal P1.",
     "`hand_back.md`."),
    (271, 274, "Step 5.", "Yes.", "MOVE. Carried: WAY-256.", "`hand_back.md`."),
]

ADDED = [
    ("SKILL.md, after 'This skill lives in', last sentence", "The files beside this SKILL.md hold what one step or one variant of the work needs; each is read when the step or variant that names it comes, not at the start.",
     "A pointer condition; as in the testing and styleguide skills. WAY-127, WAY-259."),
    ("SKILL.md, 'Rules that hold across the steps', last bullet", "The route of one kind: steps 4 and 5 settle and check only what concerns that kind - its identifier, its exemplar, the status of its files and the rules a script checks of it with their invariants; the task's To do gains `guidelines/coding-<kind>.md` with its row in the index (WAY-216).",
     "Task To do 10 and 11: a rule the agent keeps at steps 3 to 5, so it stays in SKILL.md. Holds on the fifth mode only."),
    ("SKILL.md, 'Orchestrated mode'", "'which a project orchestrator dispatched with a conversation-file path'", "The words an agent meets the case in; as in the testing and styleguide skills."),
    ("SKILL.md, step 0", "The list of what refine-task read adds 'the guidelines of the parts the task touches' and drops the second reading; the sentence 'A session that has not read them in this conversation - it opened this skill directly, or resumed the work in a new one - goes through refine-task steps 1 and 2 first (WAY-266).'",
     "Task To do 2 and 5; the sentence is the testing skill's (product-guidelines/testing/SKILL.md:79-81)."),
    ("SKILL.md, steps 1 to 5", "Pointers 'read X.md beside this skill' with the condition of each; 'in full unless step 2 did' / 'unless an earlier step did' for the coding template (steps 3, 4); 'unless step 4 did' for task_document.md (step 5); the pointers to `research.md` and `new_tools.md` also at steps 2 and 4.",
     "Task To do 2, 3, 4 and 5; WAY-256, WAY-265."),
    ("`recognize.md`, mode list", "The fifth mode: a kind of code whose files the product already has, with no row in the index of `guidelines/coding.md`, where that file stands, and the task neither refreshes nor extends the coding guidelines: 'Kinds' of step 3 for that kind alone, with no step 2 and no trial run; where it combines with another mode, the wider mode governs (WAY-216).",
     "Task To do 9 and question 3: a change of meaning, with WAY-216 edited in place."),
    ("`kinds.md`", "'On the route of one kind (...) name that kind alone with its files: this is the comparison WAY-200 gives existing code, covering that kind and no other, and no audit under WAY-201.'", "Task To do 12."),
    ("`starting_set.md`", "'Word it as \"How to show\" in SKILL.md gives.' and the connective 'research each standing check for that technology: read research.md beside this skill.'", "Task acceptance criteria; WAY-265."),
    ("`research.md`", "'Before the first critique of the session, read elements/common/critique/SKILL.md.'", "Replaces the read at step 0; task To do 2."),
    ("`settle.md`, `hand_back.md`, `task_document.md`", "An opening sentence in each. `task_document.md`: on the route of one kind, take from the items below what concerns that kind, as 'The route of one kind' in SKILL.md gives: its file with the index row, the test of each new invariant it settles, its choices and what the comparison found. `settle.md`: settle of the choices and invariants below only what the rule gives; the critique below stands. `hand_back.md`: check only what the rule gives, of the items below. `settle.md` last bullet: 'Read that section and, unless step 2 did, elements/common/critique/SKILL.md.'",
     "Pointers at the moments steps 4 and 5 meet the route, one of them brought about by the mode list and not by the step (instruction-files/SKILL.md, 'Where a rule stands'). The rule itself has one place, SKILL.md; the openings name what they leave standing (the tests of the invariants, the Context of the comparison, the critique)."),
]

PROPOSALS = [
    ("P1", 223, 224, "A reword that changes the rule's meaning (task To do 8): on the route 'A new kind', steps 4 and 5 should settle and check only the standing checks the new kind touches, instead of 'each standing check' (lines 223-224, 269) and the items of *To do* that install and configure the tool of each standing check (lines 63-69). The lines are quoted whole, with line 269 and lines 63-69 listed in the proposal.",
     "Steps 4 and 5 on the route 'A new kind' in a product whose general coding file already stands. On that route the base still says that the task is not ready without a decision for each standing check (line 223-224) and that the hand back checks each (line 269); both were settled when the general file was written. The agent recognises the moment at step 4.",
     "Not applied: it changes what the rule requires; the frozen task accepts keep, move and meaning-preserving rewordings only, and keeps the contradiction as a proposal (task To do 8). RECOMMENDED for the human's decision at the request: an agent on the route either settles checks already settled or departs from the base text. Ground: a cost of misreading; mistake not found in the records searched, and the route has no prior session (the task's Context: no session went through 'A new kind')."),
    ("P2", 108, 108, "A reword that changes the rule's meaning: read from the product's `guidelines/` only the file for the part the task covers and the index of the coding guidelines, instead of every file under it.",
     "Step 1. refine-task already read the guidelines of the parts the task touches (`product-guidelines/reading.md:40`), so the wider reading may repeat that and add what the coding guidelines do not need; it costs the product's words and differs by product. The agent recognises the moment (step 1).",
     "Not applied: it changes what the rule reads. NOT RECOMMENDED: ground 'mistake' not found in the records searched, and the ground is a cost only."),
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
    nwords = len(base.split())
    outl = ["# Assessment of `maintain-coding-guidelines`", "",
            f"Base: `{PATH}` at commit {BASE[:7]} ({len(lines)} lines, {nwords} words). Mode judge, kind "
            "skill, by `instruction-files/judging.md` and `instruction-files/kind_skill.md`. Each quote "
            "is the whole of the lines named, cut from the file at the base; a blank line inside a "
            "quote shows as an empty line break. Every nonblank line of the file stands in exactly "
            "one row (checked by `tools/make_assessment.py`). Verdicts are those of "
            "`judging.md`: keep, move, remove, reword; a split is written as the verdicts of its parts.", "",
            "Tools: Claude Code and Codex through the project entry points; Cursor through the "
            "shared layout. Sessions start in the-way's checkout or in a product that pins it. "
            "The frozen task accepts keep, move and meaning-preserving rewordings, and the changes "
            "of To do 9-13; a remove or a reword that changes a rule's meaning stands as a proposal "
            "and is not applied.", "",
            "Records searched for the mistakes the fragments are kept for: the git history of the "
            "file (`git log --oneline -- product-guidelines/coding/SKILL.md`, 12 commits: c6ee066, "
            "a6453b7, 87b600e, 556bd26, 4e6b53c, 2e11537, 0745539, fc0c946, f34e477, 5a00041, "
            "aaaab9d, d5fd8ca, by their messages), the remarks of PRs #50, #51, #52, #59, #60 and #62 "
            "(`gh pr view <n> --comments`; #51 returns no comment; none of the other five mentions "
            "`product-guidelines/coding/SKILL.md` or the skill by name; #60 and #62 hold assessment "
            "tables of the styleguide and testing skills, whose remarks on reading `guidelines/` are "
            "taken as proposal P2), and the Context of the frozen task. No mistake that any fragment "
            "of this file was added for was found in them; where a row's ground is a mistake it "
            "says so, otherwise the ground is a carried decision or a cost.", ""]
    outl += block("1. Check script, before (base, `python -B instruction-files/check_instructions.py .` on an export of f86fd71)",
                  R + "check_base.txt")
    outl += block("1. Check script, after (this change, the same command, exit code 0; the output is identical)",
                  R + "check_after.txt")
    outl += ["The check script follows the files the root `AGENTS.md` names; it does not reach this "
             "skill, so the warning on `AGENTS.md:21` (the folder `_zadania" + BS + "`, in the author's "
             "private notes) stands on the base and is not part of this change. It means the same in "
             "all three tools: a pointer to a folder not in the repository. The paths named by the "
             "rebuilt files were checked by hand, see the author's report.", ""]
    outl += ["## 2. Contradictions between files that load together", "",
             "Before: (a) Step 0 of the base skill (`:101-112`) tells the session to read all its "
             "files at the start, against WAY-127 and WAY-259, which have an entry point read a "
             "named file when the step that names it comes, and it has refine-task's `SKILL.md`, the "
             "task template and two sections of the way of working read a second time (3391 words). "
             "(b) The mode list of step 1 (`:124-130`) holds no route for a kind whose files the "
             "product has and its index lacks (`product-guidelines/reading.md:83-85`, "
             "`project-level/task/skill/guideline_findings.md:33-35`, WAY-216). (c) The route 'A new "
             "kind' (`:197-199`) against `:223-224`, `:269` and the *To do* items of `:63-69`, which "
             "on that route still speak of every standing check. After: (a) is settled by the "
             "pointers at steps 2 to 5 and the sentence ending step 0 (WAY-266); (b) by the fifth "
             "mode with WAY-216 edited in place (task To do 9-13); (c) stays, as proposal P1. No "
             "other contradiction was found between `SKILL.md`, the files beside it, the two "
             "templates it names and `kind_skill.md`.", ""]
    outl += ["## 3. The table", "",
             "| Fragment (literal, whole, lines on f86fd71) | Needed when | Will the agent recognise "
             "that moment? | Verdict, reason and ground | New place |", "|---|---|---|---|---|"]
    for s_, e_, needed, rec, verdict, place in ROWS:
        outl.append("| " + " | ".join([quote(lines, s_, e_), esc(needed), esc(rec), esc(verdict),
                                       esc(place)]) + " |")
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

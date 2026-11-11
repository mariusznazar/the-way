# Correction-fix report: B1 of the review of the correction (reviewed head 047a9e7)

**Status:** done. One commit, `80126da`, on top of `047a9e7`. Tree clean. `docs/task-cycles/`
untouched. The three Minor findings of the review were not touched.

## The finding

- **B1, fixed** (the reviewer's first fix, as the orchestrator chose). `foundations/decisions.md`,
  WAY-154, edited in place:
  - second binding sentence: after "with the dependencies the plan gives the task," it now says
    "and, as the rules of the task place give, brings the lines of the tasks tied to its task into
    agreement with the plan's dependencies," then continues "at the same time as the other
    refiners of the round and with no queue between their writes". Still three binding sentences.
  - *Verification*, *complies*: a refiner that finds the line of a task waiting on its own task
    without the dependency on it brings that line into agreement as the rules of the task place
    give, and one that finds no line for a tied task makes none.
  - *Verification*, *violates*: a refiner makes the line of a tied task that has none.
  - *Rationale*, the accepted risk: also two refiners that bring the same tied line into agreement
    can leave one write of it; shows afterwards as a task with no line or a line missing a field.
  - Nothing of how a line is handled (find it, one to a task, which fields, read before write, the
    clash) was written into WAY-154, WAY-329 or any skill.
- Width: no added line is longer than 100 characters (character count over `git diff 047a9e7`, one-off
  `python -B` run, exit 0, empty list).
- Mark per the foundation step: WAY-154's added write is **`the cycle's`**, as the added rule in
  WAY-107. Source, named here and not in the entry: the human's remark at the request on item 1 (a
  refiner that knows from the plan that one task depends on another brings the lines to agreement,
  whichever line it is). The meaning of the added write, EN: a refiner also brings the lines of the
  tasks tied to its task into agreement with the plan's dependencies as the rules of the task place
  give. PL: refiner doprowadza też do zgodności z zależnościami z planu linie zadań powiązanych z
  jego zadaniem, tak jak dają to zasady miejsca zadań.

## Return step again (compared with the files)

- **WAY-154** against `project-level/task_line.md` ("The dependencies"), `orchestrated_mode.md:41-43`,
  `lead/conversation_template.md:22-24`, `lead/skill/SKILL.md:105-106` and
  `plan/skill/delegated_mode.md:9-10`: the entry and the files now say the same (the refiner brings
  the lines of tied tasks into agreement as the rules of the task place give; the files point to
  `task_line.md`; the write is the same list). None to correct.
- **WAY-107** against `backlog_place.md`, `AGENTS.md`, `task_line.md` opening paragraph: matches, as
  before the fix. None.
- **WAY-329** against `task_line.md` "The identifier": matches. None.
- **Part map**, `project-level`: still says the part answers for how a task's line is made, given its
  dependencies and moved to ready. The agreement of lines is a part of how a line is made, handled
  by the rules of the place; no change of responsibility. None.
- `product-guidelines/coding/orchestrated_mode.md` and `testing/orchestrated_mode.md` say the skill
  edits "the task's line in the backlog, as `refine-task` gives"; they point to `refine-task`, so
  they cover the tied lines through it. Not touched.

## Checks (command, exit code)

All from the worktree root, on the committed tree.

- `python -B elements/common/foundation_check.py` — exit 0, "0 errors".
- `python -B instruction-files/check_instructions.py .` — exit 0, "0 error, 0 warn, 3 info".
- `python -B task-cycle/test_tracked_files_private_paths.py` — exit 0, "OK".
- Not run, as the handoff says: the `project-level` directory and the full gate.

## Own-work check

- Requirement most likely unmet: that no skill file gives a refiner a write WAY-154 does not give it.
- Check: `grep -rn "tied to\|tied task" foundations project-level product-guidelines --include=*.md`,
  exit 0. The write now stands in WAY-154 (`decisions.md:4449`, `4474`, `4483`) and in the four skill
  files the finding names (`orchestrated_mode.md:42`, `conversation_template.md:23`,
  `lead/skill/SKILL.md:105`, `delegated_mode.md:10`); other hits ("tied to no requirement" and
  similar) are unrelated uses. Before the fix the phrase stood in the four skill files and in no
  entry, which is the defect.
- Second check: `grep -rn "task's line in the backlog" product-guidelines --include=*.md`, exit 0:
  two hits, both `... as \`refine-task\` gives`, so they add no write beyond the one in `task_line.md`.
- A third grep I ran for "refiner ... write/make/edit ... line" over `project-level` and
  `product-guidelines` printed nothing for `project-level`; its exit code is that of `cut`, so I do
  not count the exit as evidence. The two greps above are the evidence.

## Unread material

none. I read the handoff, the findings file, the entry WAY-154 in its present form, and the files I
compared. I did not read `reports/correction-review-report.md` (the findings file carries its section
in the reviewer's words).

## Searches not found or unclear

none.

## Reach beyond the handoff

none. (During editing I made and at once corrected a slip in my own script, a doubled "- " before the
two *Verification* bullets; the committed text has single bullets, as the diff shows.)

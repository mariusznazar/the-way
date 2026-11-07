# Return step report — foundation-review-skill

**Status:** done. Nothing no longer matches; **no commit** (head stays `34a206f`).

## Return step record

- **Foundation compared with code:** WAY-24, WAY-09, WAY-82, WAY-300 to WAY-305, the facts template
  sentence, the task's *Decisions in play* (WAY-24, 37, 11, 14, 120, 140, 215, 82, 161, 289) and
  WAY-286 and WAY-287 (the top part's rules the reminder lives under), and the part-map entries of
  `foundation-review`, `task-cycle`, `installation`, `decisions`, `part-map`, `environment-facts`,
  `agent-instructions`, each read against the files as they stand at `34a206f`:
  - WAY-24 / WAY-300: `foundation-review/SKILL.md` (name `review-foundation`, opens "once the main
    branch holds 30 merges"), `task-cycle/review_reminder.py` (`THRESHOLD = 30`, `>=`, first-parent
    merges, nearest `foundation-review/*` tag, none counts from the start of history),
    `task-cycle/skill/SKILL.md` step 13 and `request_template.md` (the reminder ends *How to merge*,
    names count, tag, skill, blocks nothing, repeats while the count stands). Match.
  - WAY-301: skill step 7 (annotated tag on the checked commit, `-2` and `-3`, put also when nothing
    changed, message of the number of items checked, push on a yes); script finds the tag from the
    given main branch. Match.
  - WAY-302, 303, 304, 305: `SKILL.md` steps 1 to 7, `remarks.md`, `proposals.md`, `weak_points.md`,
    `with_the_human.md` (rhythm, groups, notes, leave, one data file, nothing changed in the
    foundation or code; own repository's requests only; the human names the starting request; weak
    points compared with today and read-only checks). Match.
  - WAY-09: `foundation-review/` named among the directories and holds the skill and the files it
    names; `task-cycle/` holds the script. Match. WAY-82 and the facts template: no longer call the
    review a backlog task. Match.
  - WAY-286 / WAY-287: the reminder names a tag and a skill, no file and no entry identifier, and is
    no item of *For you to decide*; a sample description passed `request_check.py`. Match.
  - WAY-140: the review is a session with the human, not a task's cycle; the agent writes the
    backlog tasks and the data file after the human's decision and pushes the tag on a yes. No
    collision found with WAY-140 (it binds a task's effect); noted as a matter for the reviewer of
    the request, not corrected.
  - Part map: `foundation-review/**` matches the five files (`foundation_check.py`); *Depends on* of
    `foundation-review` (decisions, invariants, glossary, part-map, environment-facts, elements-common,
    project-level) covers what its texts read (`way_of_working.md`, `critique`, the task template,
    `refine-task`); `installation` names the new part (it holds the skill's path); `task-cycle`'s
    sentence still covers the end-of-cycle step and the script; no part needed another change.
- **Decisions written or changed:** none in this step (WAY-24, 09, 82 changed and WAY-300 to 305
  written in the foundation step).
- **Invariants:** none written; no task row, decision or human sets a rule a commit could make false.
- **Environment facts:** none written. No decision of this change cites an outside source in *Based
  on* (all read `none`), and the merge-rate measurement in WAY-300's rationale is a measurement, not a
  source; the behaviour of the two git commands is the task's own *Context*.
- **Glossary terms:** none. "review of the foundation", "reminder", "review tag", "checked commit"
  and "data file" mean what a reader of the field takes them to mean; WAY-95 gives no entry.
- **Part-map changes:** none in this step (the new part and the `installation` dependency were
  written in the foundation step).
- **Projected entries:** none (the task is independent).
- **Rows of *Settlements to record* written:** rows 1 to 7, all written in the foundation step; row 1
  tied to WAY-24 and writes no second entry, rows 2 to 7 are WAY-300 to WAY-305. None missed.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`
- `python -B agent-instructions/skill_entry_points.py` — exit 0, `entry points are current`
- `python -B task-cycle/review_reminder.py origin/foundations` — exit 0, `tag:
  foundation-review/2026-11-06`, `merges: 1`, `reminder: no`
- Not run: the whole gate (the orchestrator's); no test, since nothing was changed.

## Own-work check

Requirement most likely unmet: no entry of the change disagrees with the files it describes after the
fix to WAY-301. Check: reread each entry's binding sentence and *Verification* against the file named
above, and `grep` for every place that names the skill, the tag or the part (`review-foundation`,
`foundation-review`) outside `.runs`, `.claude` and `.agents`: every hit is in an entry, the part map,
the installer, the two READMEs, the script or the template, and each agrees with the others. It
showed no mismatch. Not checked: the skill on a real repository.

## Searches not found or unclear

- Whether WAY-140 reaches the agent's writes of backlog tasks and the data file in a review session
  (outside the repository): I read it as binding a task's cycle, so I found no collision, but the
  decision does not say that a session with the human is outside it.
- The reminder reaches only requests written by a task cycle's orchestrator (WAY-300); the
  before-`main` guide for changes to the-way (`agent-instructions/README.md`) is silent on it. Same
  gap as in my first report; not corrected, since the row binds the cycle.

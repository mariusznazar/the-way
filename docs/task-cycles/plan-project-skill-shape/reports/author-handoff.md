# One-author handoff — plan-project in the WAY-256 shape

The person who requested this cycle delegated intermediate choices to the orchestrator. The human
reviews the request, not this stage. Questions come back to the orchestrator; never ask the human.

## Where you work

- Worktree: `C:/Storage/repos/the-way/.runs/worktrees/plan-project-skill-shape`. Run every command
  there, explicitly (`git -C`, absolute paths). Change nothing in `C:/Storage/repos/the-way` itself
  or outside the repository.
- Branch `task/plan-project-skill-shape`, base `2f51e6c31f5911ac8a0292a80a4f599bd4bd0092`.
- The cycle's directory is
  `C:/Storage/repos/the-way/.runs/worktrees/plan-project-skill-shape/.runs/task-cycles/plan-project-skill-shape/`,
  called `<cycle>` below. It is ignored by git.
- `.runs/base-check` inside the worktree is the orchestrator's checkout of the base, running the
  gate. Leave it alone.
- Every file of the-way you read, you read from this worktree, by its path, not through a project
  skill the session would resolve to another checkout. Skills named below by a bare name are the
  files in this worktree, with no global skill in their place.

## Method and variant

Read `task-cycle/change/SKILL.md` whole and follow it, variant **"the whole change as the one
author"**. Read a file it names when the step or variant that names it comes.

The task carries no row of *Settlements to record* and no projected entry, so you write no
foundation entry. If you find that an entry no longer matches, name it in your report: do not edit
it.

## The task

Frozen task, whole: `<cycle>/task.md`, created 2026-11-01, source commit 2f51e6c. No spec, no plan.
Its *To do*, *Acceptance criteria*, *Questions to settle*, *Decisions in play* and *Out of scope*
are your requirements and are not restated here. Where a figure in the task does not match your own
count, report the difference; never bend the count.

Answers of the cycle's start: no trust boundary is touched; no irreversible operation; no open
design choice. Names and grouping of the files beside the skill that the task does not name are
yours to choose and name. One author, class `cheaper`.

Guidelines: empty selection (task question 7). Only Markdown changes; no Python changes; the
description in the frontmatter does not change.

Answer the cycle gives to a point of the task: remarks of PRs #50–#52, #59, #60, #62 and #64 are
records of mistakes for your judgement, and none of them is applied unless it settles a question of
this task (task *Out of scope*).

## The judgement (To do 1)

Apply the skill of instruction-files from this worktree: `instruction-files/SKILL.md`, mode judge,
kind skill (`instruction-files/judging.md`, `instruction-files/kind_skill.md`), on
`project-level/plan/skill/SKILL.md` at the base. Then change it by that judgement.

Answers to what that skill asks, from the cycle's record:

- Tools: Claude Code and Codex through the project entry points; Cursor through the shared layout.
  Sessions start in the-way's checkout or in a product that pins it (task *Context*).
- Acceptance: the frozen task accepts keep, move and meaning-preserving rewordings, and the one new
  pointer of To do 5 and the sentence of To do 4. A remove, or a reword that changes a rule's
  meaning, is written in the table as a proposal and is not applied (To do 9).
- Records to search for mistakes: the git history of the file, the remarks of PRs #50, #51, #52,
  #59, #60, #62 and #64 (`gh pr view <n> --comments`), and the task's *Context*; name what you
  searched.

Judge each fragment by its own moment. Traps of this kind of work, each met on an earlier skill of
the series:

- a group of lines kept together can hold a fragment with a condition of its own, which then rides
  along on every use;
- a rule that holds on several steps or in several variants, placed in the file of one of them,
  silently stops reaching the others; in one file the agent read it by the way, and after the split
  it needs a pointer at every moment it is needed, also a moment where someone other than the agent
  brought the case about. WAY-256 names which of these stays in `SKILL.md`. The task's criterion
  "Fragment potrzebny w więcej niż jednym miejscu" and the one on the delegated file reaching
  steps 5–7 are cases of it: a step file that tells the agent to ask the human or run the critique,
  read by a delegated agent, must not make it do so;
- a reworded mode or pointer can add a route or lose one while every named sentence stays present.
  An earlier skill gained a mode no source held that way. Compare each reworded condition with the
  base by what it selects, not by its words, and for each new sentence name what it switches off.
  A sentence written to open a file can switch off items below it ("only this") though every old
  sentence still stands: an earlier skill lost an item of its task document that way;
- the rows of your judgement do not place anything: a row can say a rule holds on three steps while
  the text stands in the file of the first. The review compares each row with the place;
- a pointer's condition names the moment as the agent meets it (`instruction-files/SKILL.md`,
  "Where a rule stands"). The pointer is read by an agent that reached `SKILL.md` by its path, so
  "beside this skill" and the step's name must be enough;
- opening sentences and pointers cost more words than they look; an earlier skill grew by 773 words
  against about 400 estimated. Report the real figure against the task's estimates.

An incoming reference to a section or step of this skill must keep working. The step numbers 0–7
stay (WAY-156, `project-level/lead/skill/SKILL.md:214`, `project-level/skill/SKILL.md:49`). The
heading "Delegated work while leading a plan" stays in `SKILL.md` (task *Context*: orchestrators of
`lead-project` repeat it in their dispatches). Inside the skill, steps name each other and
`define-project` step 7. The other files that name this skill are listed in the task's *Context*;
search for references to its sections or steps yourself. Only one sentence of
`project-level/lead/skill/SKILL.md` changes (To do 4).

The closest shapes to follow: `project-level/task/skill/SKILL.md` and the files beside it, which
lie in the same kind of directory, and `project-level/technology/SKILL.md`. Keep their vocabulary
only where it is the same thing.

## Materials the request needs

Write them under `<cycle>/reports/`, never in the tracked tree; any helper script stays under
`<cycle>/tools/`. Helpers of an earlier skill are there as `example_*.py`; adapt them or write your
own, and rest on neither without checking them.

- `assessment.md`: the table of To do 7. One row per fragment, each nonblank line of
  `project-level/plan/skill/SKILL.md` at the base in exactly one row, each quote literal and whole
  with its line range on 2f51e6c (permalink form:
  `https://github.com/mariusznazar/the-way/blob/2f51e6c31f5911ac8a0292a80a4f599bd4bd0092/project-level/plan/skill/SKILL.md#L1-L4`),
  no summaries. Columns: the fragment, when it is needed, whether an agent recognises that moment,
  the verdict with reason and ground, and the fragment's new place. Proposals of To do 9 stand in
  rows of their own kind and are listed once more at the end, each with what happens if it is left
  and what it costs if made, the repetitions between the skill and `project-level/plan/template.md`
  among them. Keep the sections in the order `instruction-files/judging.md` gives, and use its
  verdicts only; earlier assessments were found out of order and using verdicts it does not hold.
  Every statement a row makes about where a rule now stands must hold in the files.
- `word-counts.md`: the routes of task question 4 — seven, the fifth in its two versions — before
  and after, two figures each as that question gives them. Words as `wc -w` counts them, Markdown
  and frontmatter included; of a file read by sections, the sections read. The state "before" is
  2f51e6c. Say beside each route which reading of it you count: which steps run, and whether the
  critique runs. Each route's file list stands in the report, file by file with its word count, so
  that a reader can add it up. Every route is counted to the end of the skill, the last step's file
  included. Compare the results with the estimates in task question 1 (and its correction), and say
  which fall outside them.
- A helper that compares every figure stated in `word-counts.md`, per file and per sum, with the
  files, as the task's last acceptance criterion gives. Run it after your last change to a counted
  file; say so in your report.

## Your own check

Name your weakest point, as the method gives. It is rule preservation: show, with a helper that
compares the base `SKILL.md` with the rebuilt files sentence by sentence, whitespace normalised,
which sentences differ, and account for each difference as a pointer, a table row, a
meaning-preserving rewording or a change of To do 4 or 5. Then read each new sentence for what it
switches off; the comparison cannot see that. Check also each quote of `assessment.md` against the
base, line coverage, and each route's sum. Walk the seven routes through your files by hand as an
agent would, from `SKILL.md` to the file of the last step, and write down for each what it reads and
when, what stays and what falls away; presence of a named text is not enough.

Run `python -B elements/common/foundation_check.py`,
`python -B instruction-files/check_instructions.py .`,
`python -B agent-instructions/skill_entry_points.py --write` (it should change nothing; say so if it
does), `python -B gate/run_tests.py agent-instructions`, `python -B gate/run_tests.py installation`
and `python -B gate/run_tests.py project-level`. Compare the `check_instructions.py` output with the
base. A dead-path warning on `AGENTS.md` for `_zadania\` stands on the base and is not yours. Do not
run the whole gate; its run is the orchestrator's.

## Foundation to read

Read each whole, by "Reading the foundation" in `elements/common/way_of_working.md`:

- Decisions of the task's *Decisions in play*: WAY-256, WAY-257, WAY-265, WAY-151, WAY-156,
  WAY-145, WAY-146, WAY-143, WAY-218, WAY-230, WAY-120, WAY-113, WAY-150, WAY-106, WAY-127, WAY-259.
- Decisions the moved text cites or the placing rests on: WAY-13, WAY-35, WAY-125, WAY-126,
  WAY-142, WAY-144, WAY-147, WAY-152, WAY-200, WAY-242, WAY-247, WAY-266.
- Part map: `project-level`.
- Invariants: project-plan-form, project-plan-check, skill-entry-points, instruction-file-imports,
  repository-file-location, outbound-link-reach.
- Environment fact: `claude-skill-nested-references`.
- Glossary: the terms the moved text uses.

A decision you need beyond these is a reach: read it and name it in your report. State in the report
which of these you read whole and which you did not.

## Commits and report

- Before a script, read `C:\Storage\The Brain\The Brain\.ai\rules\scripts.md`; before a commit,
  `C:\Storage\The Brain\The Brain\.ai\rules\git.md`; before changing a skill,
  `C:\Storage\The Brain\The Brain\.ai\rules\knowledge_artifacts.md`. The skill's files are in
  English, with LF line endings, in the style of the rebuilt skills.
- Commit on the task branch with `git add <paths>`; keep the worktree clean; verify the author
  address with `git log --format='%h %ae'`. Do not push and do not open a request.
- Full report: `<cycle>/reports/author.md`, with each check's command and exit code, every choice
  you made with the way not taken, every reach beyond this handoff, your concerns, and **Searches
  not found or unclear**.
- Return: your status, your commits, a one-line check result naming what failed or did not run, and
  the report's path.

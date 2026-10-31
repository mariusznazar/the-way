# One-author handoff — maintain-coding-guidelines in the WAY-256 shape

The person who requested this cycle delegated intermediate choices to the orchestrator. The human
reviews the request, not this stage. Questions come back to the orchestrator; never ask the human.

## Where you work

- Worktree: `C:/Storage/repos/the-way/.runs/worktrees/coding-skill-shape`. Run every command there,
  explicitly (`git -C`, absolute paths). Change nothing in `C:/Storage/repos/the-way` itself or
  outside the repository, beyond the cycle's own directory below.
- Branch `task/coding-skill-shape`, base `f86fd71f3cb72a9eb1620c388af44bbd1198fb4a`.
- The cycle's directory is `C:/Storage/repos/the-way/.runs/task-cycles/coding-skill-shape/`, called
  `<cycle>` below. It is ignored and lies outside the task's worktree.
- `.runs/base-check` inside the worktree is the orchestrator's checkout of the base, running the
  gate. Leave it alone.
- Every file of the-way you read, you read from this worktree, by its path, not through a project
  skill the session would resolve to another checkout. Skills named below by a bare name are the
  files in this worktree, with no global skill in their place.

## Method and variant

Read `task-cycle/change/SKILL.md` whole and follow it, variant **"the whole change as the one
author"**. Read a file it names when the step or variant that names it comes.

The task carries three rows of *Settlements to record*, so you take the foundation step with your
code: read `task-cycle/skill/foundation_step.md` whole, and `elements/decisions/skill/SKILL.md`
when you write an entry. Select the foundation for that entry as that skill gives.

## The task

Frozen task, whole: `<cycle>/task.md`, accepted 2026-10-31, source commit f86fd71. No spec, no plan.
Its *To do*, *Acceptance criteria*, *Questions to settle*, *Decisions in play*, *Settlements to
record* and *Out of scope* are your requirements and are not restated here. Where a figure in the
task does not match your own count, report the difference; never bend the count.

Answers of the cycle's start: no trust boundary is touched; no irreversible operation; no open
design choice. Names and grouping of the files beside the skill that the task does not name are
yours to choose and name. One author, class `cheaper`.

Guidelines: empty selection (task question 8). Only Markdown changes; no Python changes.

Answers the cycle gives to points of the task:

- Rows 1 and 2 of *Settlements to record* are one edit of WAY-216 in place, in the wording the
  task's *Context* quotes; row 3 is an edit of WAY-266 in place. No new entry. The link
  `narrows WAY-251` is written on WAY-216 only: a decision that another narrows does not name that
  other in its own *Relations* (`foundations/decisions.md`, the decision whose *Verification* says
  so). WAY-251's text does not change.
- The rule of To do 10 holds on the fifth mode only. On the route "A new kind" steps 4 and 5 stay
  as they are, and the contradiction To do 8 names stays a proposal in the request.
- Remarks of PRs #50–#52, #59, #60 and #62 are records of mistakes for your judgement, and none of
  them is applied unless it settles a question of this task (task *Out of scope*).

## The judgement (To do 1)

Apply the skill of instruction-files from this worktree: `instruction-files/SKILL.md`, mode judge,
kind skill (`instruction-files/judging.md`, `instruction-files/kind_skill.md`), on
`product-guidelines/coding/SKILL.md` at the base. Then change it by that judgement.

Answers to what that skill asks, from the cycle's record:

- Tools: Claude Code and Codex through the project entry points; Cursor through the shared layout.
  Sessions start in the-way's checkout or in a product that pins it (task *Context*).
- Acceptance: the frozen task accepts keep, move and meaning-preserving rewordings. Outside To do
  9–13, a remove or a reword that changes a rule's meaning is written in the table as a proposal and
  is not applied.
- Records to search for mistakes: the git history of the file, the remarks of PRs #50, #51, #52,
  #59, #60 and #62 (`gh pr view <n> --comments`), and the task's *Context*; name what you searched.

Judge each fragment by its own moment. Traps of this kind of work, each met on an earlier skill of
the series:

- a group of lines kept together can hold a fragment with a condition of its own, which then rides
  along on every use;
- a rule that holds on several steps or in several variants, placed in the file of one of them,
  silently stops reaching the others; in one file the agent read it by the way, and after the split
  it needs a pointer at every moment it is needed, also a moment where someone other than the agent
  brought the case about. WAY-256 names which of these stays in `SKILL.md`;
- a reworded mode or pointer can add a route or lose one while every named sentence stays present.
  An earlier skill gained a mode no source held that way. Compare each reworded condition with the
  base by what it selects, not by its words;
- a read repeated after `refine-task` is more than the files named: compare each item of step 0
  with `project-level/task/skill/read_sources.md` and `product-guidelines/reading.md` yourself, as
  To do 2 lists them;
- a pointer's condition names the moment as the agent meets it (`instruction-files/SKILL.md`,
  "Where a rule stands"). The pointer is read by an agent that reached `SKILL.md` by its path, so
  "beside this skill" and the step's name must be enough;
- WAY-210 binds the order of step 1: recognition comes before anything else, so a read moved into
  step 1 must not turn that order around.

An incoming reference to a section of this skill must keep working: inside the skill, steps name
"What reaches the task document", "How a skill asks", "Critique before collective review" and
others, and the section "Writing the files" of the template enters product task documents through
*To do* (`product-guidelines/coding/SKILL.md:53–55`) and stays. The other files that name this skill
are listed in the task's *Context*; search for references to its sections or steps yourself.

The closest shape to follow: `product-guidelines/testing/SKILL.md` and the files beside it, then
`product-guidelines/styleguide/SKILL.md`. The task's questions, To do 9–13 and acceptance criteria
say where this skill differs. Keep their vocabulary only where it is the same thing.

## Materials the request needs

Write them under `<cycle>/reports/`, never in the tracked tree; any helper script stays under
`<cycle>/tools/`. Helpers of the earlier skill are there as `example_*.py`; adapt them or write your
own, and rest on neither without checking them.

- `assessment.md`: the table of To do 6. One row per fragment, each nonblank line of
  `product-guidelines/coding/SKILL.md` at the base in exactly one row, each quote literal and whole
  with its line range on f86fd71 (permalink form:
  `https://github.com/mariusznazar/the-way/blob/f86fd71f3cb72a9eb1620c388af44bbd1198fb4a/product-guidelines/coding/SKILL.md#L1-L4`),
  no summaries. Columns: the fragment, when it is needed, whether an agent recognises that moment,
  the verdict with reason and ground, and the fragment's new place. Proposals of To do 8 stand in
  rows of their own kind and are listed once more at the end. Keep the sections in the order
  `instruction-files/judging.md` gives, and use its verdicts only; a remark on the earlier skill's
  assessment found its order and two verdicts out of line. Every statement a row makes about where a
  rule now stands must hold in the files: the review compares each row with the place.
- `word-counts.md`: the seven routes of task question 4, before and after, three figures each as
  that question gives them. Words as `wc -w` counts them, Markdown and frontmatter included; of a
  file read by sections, the sections read. The state "before" is f86fd71. Say beside each route
  which reading of it you count: which steps run, whether research runs, whether the trial run and
  the audit run, whether the critique of step 2 runs. Each route's file list stands in the report,
  file by file with its word count, so that a reader can add it up. Every route is counted to the
  end of the skill, the last step's file included.
- A helper that compares every figure stated in `word-counts.md`, per file and per sum, with the
  files, as the task's last acceptance criterion gives. Run it after your last change to a counted
  file; say so in your report. The report of the earlier skill stood stale at review.

## Your own check

Name your weakest point, as the method gives. It is rule preservation: show, with a helper that
compares the base `SKILL.md` with the rebuilt files sentence by sentence, whitespace normalised,
which sentences differ, and account for each difference as a pointer, a table row, a
meaning-preserving rewording or a change of To do 9–13. Check also each quote of `assessment.md`
against the base, line coverage, and each route's sum. Walk the seven routes through your files by
hand as an agent would, from `SKILL.md` to the file of the last step, and write down for each what
it reads and when, and the same for the conditions of the acceptance criteria that name one route;
presence of a named text is not enough.

Run `python -B elements/common/foundation_check.py`,
`python -B instruction-files/check_instructions.py .`,
`python -B agent-instructions/skill_entry_points.py --write` (it should change nothing; say so if it
does) and `python -B gate/run_tests.py agent-instructions`, and
`python -B gate/run_tests.py installation`. Compare the `check_instructions.py` output with the
base. A dead-path warning on `AGENTS.md` for `_zadania\` stands on the base and is not yours. Do not
run the whole gate; its run is the orchestrator's.

## Foundation to read

Read each whole, by "Reading the foundation" in `elements/common/way_of_working.md`:

- Decisions: WAY-01, WAY-05, WAY-08, WAY-14, WAY-16, WAY-28, WAY-29, WAY-30, WAY-33, WAY-35, WAY-44,
  WAY-51, WAY-61, WAY-100, WAY-107, WAY-113, WAY-120, WAY-121, WAY-123, WAY-124, WAY-125, WAY-127,
  WAY-128, WAY-129, WAY-134, WAY-150, WAY-154, WAY-155, WAY-167, WAY-168, WAY-171, WAY-172, WAY-173,
  WAY-174, WAY-198, WAY-199, WAY-200, WAY-201, WAY-202, WAY-203, WAY-204, WAY-205, WAY-206, WAY-207,
  WAY-208, WAY-209, WAY-210, WAY-211, WAY-212, WAY-213, WAY-214, WAY-215, WAY-216, WAY-217, WAY-228,
  WAY-231, WAY-247, WAY-248, WAY-251, WAY-256, WAY-257, WAY-259, WAY-265, WAY-266, WAY-268.
- Part map: `product-guidelines`, `decisions`.
- Invariants: foundation-file-kinds, foundation-change-merge-route, repository-file-location,
  return-step-record, derived-file-content, outbound-link-reach, skill-entry-points,
  instruction-file-imports.
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
  not found or unclear**. Show the search of the whole foundation WAY-33 asks once the entries are
  settled.
- Return: your status, your commits, a one-line check result naming what failed or did not run, and
  the report's path.

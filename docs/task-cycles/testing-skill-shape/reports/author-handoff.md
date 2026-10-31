# One-author handoff — maintain-testing-guidelines in the WAY-256 shape

The person who requested this cycle delegated intermediate choices to the orchestrator. The human
reviews the request, not this stage. Questions come back to the orchestrator; never ask the human.

## Where you work

- Worktree: `C:/Storage/repos/the-way/.runs/worktrees/testing-skill-shape`. Run every command
  there, explicitly (`git -C`, absolute paths). Change nothing in `C:/Storage/repos/the-way` itself
  or outside the repository.
- Branch `task/testing-skill-shape`, base `00c0a747272a9a179b7a855f256daff985ea2ee1`.
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

Frozen task, whole: `.runs/task-cycles/testing-skill-shape/task.md`, accepted 2026-10-31, source
commit 00c0a74. No spec, no plan. Its *To do*, *Acceptance criteria*, *Questions to settle*,
*Decisions in play*, *Settlements to record* and *Out of scope* are your requirements and are not
restated here. Where a figure in the task does not match your own count, report the difference;
never bend the count.

Answers of the cycle's start: no trust boundary is touched; no irreversible operation; no open
design choice. Names and grouping of the files beside the skill are yours to choose and name. One
author, class `cheaper`.

Guidelines: empty selection (task question 10). Only Markdown changes; no Python changes.

Answer the cycle gives to a point of the task: question 8 says WAY-256 does not change, and row 1 of
*Settlements to record* extends it. They do not collide: question 8 rejects a first-step exception;
row 1 adds the case of question 2, and is written. The rule and the file `kind_skill.md` must agree,
and the third answer in `kind_skill.md` cites the entry that carries row 1 (the row's last column
says why). Rows 2 and 3 are entries too: whichever identifier carries each, the assessment's row on
the choice of question 3 cites row 2's, and the sentence of question 4 at the end of step 0 cites
row 3's, in both skills, as the rules of these skills cite decisions.

## The judgement (To do 1)

Apply the skill of instruction-files from this worktree: `instruction-files/SKILL.md`, mode judge,
kind skill (`instruction-files/judging.md`, `instruction-files/kind_skill.md`), on
`product-guidelines/testing/SKILL.md` at the base. Then change it by that judgement. Until To do 4
is made, `kind_skill.md` does not answer the case of a fragment some steps need: judge it by the
wording of question 2 (task question 9).

Answers to what that skill asks, from the cycle's record:

- Tools: Claude Code and Codex through the project entry points; Cursor through the shared layout.
  Sessions start in the-way's checkout or in a product that pins it (task *Context*).
- Acceptance: the frozen task accepts keep, move and meaning-preserving rewordings. A remove or a
  reword that changes a rule's meaning is written in the table as a proposal and is not applied.
- Records to search for mistakes: the git history of the file and the remarks of PRs #50, #51, #52,
  #59 and #60 (`gh pr view <n> --comments`); name what you searched.

Judge each fragment by its own moment. Traps of this kind of work, each met on an earlier skill of
the series:

- a group of lines kept together can hold a fragment with a condition of its own, which then rides
  along on every use;
- a rule that holds on several steps or in several variants, placed in the file of one of them,
  silently stops reaching the others; in one file the agent read it by the way, and after the split
  it needs a pointer at every moment it is needed, also a moment where someone other than the agent
  brought the case about;
- a read repeated after `refine-task` is more than the files named: compare each item of step 0
  with `project-level/task/skill/read_sources.md` and `product-guidelines/reading.md` yourself, as
  To do 2 lists them;
- a pointer's condition names the moment as the agent meets it (`instruction-files/SKILL.md`,
  "Where a rule stands"). The pointer is read by an agent that reached `SKILL.md` by its path, so
  "beside this skill" and the step's name must be enough;
- WAY-248 binds the order of step 1: recognition comes before anything else, so a read moved into
  step 1 must not turn that order around.

An incoming reference to a section of this skill must keep working. At the base these name its
sections: `product-guidelines/testing/SKILL.md:120`, `:211` and `:250` inside the skill. Search for
others yourself. The name of the section "Writing the file" of the template enters product task
documents through *To do* (`product-guidelines/testing/SKILL.md:53–54`) and stays.

The closest shape to follow: `product-guidelines/styleguide/SKILL.md` and the files beside it, with
`project-level/task/skill/SKILL.md:29–32` for To do 5, which the styleguide does not follow. The
task's Questions 2, 3 and 8 say where this skill must differ from that shape. Keep its vocabulary
only where it is the same thing.

## Materials the request needs

Write them under `.runs/task-cycles/testing-skill-shape/reports/`, never in the tracked tree; any
helper script stays under `.runs/task-cycles/testing-skill-shape/tools/`. Helpers of the earlier
skill are there as `example_*.py`; adapt them or write your own, and rest on neither without
checking them.

- `assessment.md`: the table of To do 7. One row per fragment, each nonblank line of
  `product-guidelines/testing/SKILL.md` at the base in exactly one row, each quote literal and whole
  with its line range on 00c0a74 (permalink form:
  `https://github.com/mariusznazar/the-way/blob/00c0a747272a9a179b7a855f256daff985ea2ee1/product-guidelines/testing/SKILL.md#L1-L4`),
  no summaries. Columns: the fragment, when it is needed, whether an agent recognises that moment,
  the verdict with reason and ground, and the fragment's new place. The choice of question 3 has a
  row of its own. Proposals stand in rows of their own kind and are listed once more at the end. Put
  the output of `check_instructions.py` and the contradictions between files that load together
  before and after the table, as `judging.md` gives.
- `word-counts.md`: the six routes of To do 7, before and after, three figures each as question 6
  gives them. Words as `wc -w` counts them, Markdown and frontmatter included; of a file read by
  sections, the sections read. The state "before" is 00c0a74. A file read twice in "before" counts
  twice; files a counted file sends the session to on the route count in both states, such as the
  files beside `elements/common/critique/SKILL.md` where the route reaches them; the product's own
  files stay out, and you say so. Say beside each route which reading of it you count: which steps
  run, whether research runs, whether the audit runs, whether the critique of step 2 runs. Each
  route's file list stands in the report, file by file with its word count, so that a reader can add
  it up. Every route is counted to the end of the skill, the last step's file included.

## Your own check

Name your weakest point, as the method gives. It is rule preservation: show, with a helper that
compares the base `SKILL.md` with the rebuilt files sentence by sentence, whitespace normalised,
which sentences differ, and account for each difference as a pointer, a table row or a
meaning-preserving rewording. Check also each quote of `assessment.md` against the base, line
coverage, and each route's sum. Walk the six routes through your files by hand as an agent would,
from `SKILL.md` to the file of the last step, and write down for each what it reads and when;
presence of a named text is not enough (task acceptance criteria).

Run `python -B elements/common/foundation_check.py`,
`python -B instruction-files/check_instructions.py .`,
`python -B agent-instructions/skill_entry_points.py --write` (it should change nothing; say so if it
does) and `python -B gate/run_tests.py agent-instructions`. Compare the `check_instructions.py`
output with the base. A dead-path warning on `AGENTS.md` for `_zadania\` stands on the base and is
not yours. Do not run the whole gate; its run is the orchestrator's.

## Foundation to read

Read each whole, by "Reading the foundation" in `elements/common/way_of_working.md`:

- Decisions: WAY-01, WAY-08, WAY-16, WAY-28, WAY-29, WAY-33, WAY-35, WAY-44, WAY-48, WAY-51, WAY-61,
  WAY-100, WAY-107, WAY-113, WAY-120, WAY-121, WAY-123, WAY-124, WAY-125, WAY-127, WAY-128, WAY-129,
  WAY-134, WAY-150, WAY-154, WAY-155, WAY-167, WAY-168, WAY-171, WAY-172, WAY-173, WAY-174, WAY-213,
  WAY-214, WAY-215, WAY-217, WAY-226, WAY-228, WAY-231, WAY-232, WAY-233, WAY-234, WAY-235, WAY-236,
  WAY-237, WAY-238, WAY-239, WAY-240, WAY-241, WAY-242, WAY-243, WAY-244, WAY-245, WAY-246, WAY-247,
  WAY-248, WAY-249, WAY-250, WAY-251, WAY-252, WAY-253, WAY-254, WAY-256, WAY-257, WAY-258, WAY-259.
- Part map: `product-guidelines`, `instruction-files`, `decisions`.
- Invariants: foundation-file-kinds, foundation-change-merge-route, repository-file-location,
  return-step-record, derived-file-content, outbound-link-reach, skill-entry-points,
  instruction-file-imports.
- Environment fact: `claude-skill-nested-references`.
- Glossary: the terms the moved text uses.

A decision you need beyond these is a reach: read it and name it in your report.

## Commits and report

- Before a script, read `C:\Storage\The Brain\The Brain\.ai\rules\scripts.md`; before a commit,
  `C:\Storage\The Brain\The Brain\.ai\rules\git.md`; before changing a skill,
  `C:\Storage\The Brain\The Brain\.ai\rules\knowledge_artifacts.md`. The skill's files are in
  English, with LF line endings, in the style of the rebuilt skills.
- Commit on the task branch with `git add <paths>`; keep the worktree clean; verify the author
  address with `git log --format='%h %ae'`. Do not push and do not open a request.
- Full report: `.runs/task-cycles/testing-skill-shape/reports/author.md`, with each check's command
  and exit code, every choice you made with the way not taken, every reach beyond this handoff, your
  concerns, and **Searches not found or unclear**.
- Return: your status, your commits, a one-line check result naming what failed or did not run, and
  the report's path.

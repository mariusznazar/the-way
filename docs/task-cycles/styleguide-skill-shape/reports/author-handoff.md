# One-author handoff — maintain-styleguide in the WAY-256 shape

The person who requested this cycle delegated intermediate choices to the orchestrator. The human
reviews the request, not this stage. Questions come back to the orchestrator; never ask the human.

## Where you work

- Worktree: `C:/Storage/repos/the-way/.runs/worktrees/styleguide-skill-shape`. Run every command
  there, explicitly (`git -C`, absolute paths). Change nothing in `C:/Storage/repos/the-way` itself
  or outside the repository.
- Branch `task/styleguide-skill-shape`, base `525cde1dd53c474f56ea0ece289cb60e868aa90d`.
- Every file of the-way you read, you read from this worktree, by its path, not through a project
  skill the session would resolve to another checkout.

## Method and variant

Read `task-cycle/change/SKILL.md` whole and follow it, variant **"the whole change as the one
author"**. Read a file it names when the step or variant that names it comes. The task carries no
foundation entry (*Settlements to record*: none), so the foundation step writes nothing.

## The task

Frozen task, whole: `.runs/task-cycles/styleguide-skill-shape/task.md`, accepted 2026-10-30, source
commit 525cde1. No spec, no plan. Its *To do*, *Acceptance criteria*, *Questions to settle*,
*Decisions in play* and *Out of scope* are your requirements and are not restated here. Where a
figure in the task does not match your own count, report the difference; never bend the count.

Answers of the cycle's start: no trust boundary is touched; no irreversible operation; no open
design choice. Names and grouping of the files beside the skill are yours to choose and name. One
author, class `cheaper`.

Guidelines: empty selection (task question 6). The change is Markdown only; no Python changes.

## The judgement (To do 1)

Apply the skill of instruction-files from this worktree: `instruction-files/SKILL.md`, mode judge,
kind skill (`instruction-files/judging.md`, `instruction-files/kind_skill.md`), on
`product-guidelines/styleguide/SKILL.md` at the base. Then change it by that judgement.

Answers to what that skill asks, from the cycle's record:

- Tools: Claude Code and Codex through the project entry points; Cursor through the shared layout.
  Sessions start in the-way's checkout or in a product that pins it (task *Context*).
- Acceptance: the frozen task accepts keep, move and meaning-preserving rewordings. A remove or a
  reword that changes a rule's meaning is written in the table as a proposal and is not applied.
- Records to search for mistakes: the git history of the file and the remarks of PRs #50, #51 and
  #52 (`gh pr view <n> --comments`); name what you searched.

Judge each fragment by its own moment. Two traps of the same kind of work:

- a group of lines kept together can hold a fragment with a condition of its own, which then rides
  along on every use;
- a rule that holds on several steps or in several variants, placed in the file of one of them,
  silently stops reaching the others.

A pointer's condition names the moment as the agent meets it (`instruction-files/SKILL.md`, "Where
a rule stands"). The pointer is read by an agent that reached `SKILL.md` by its path, so "beside
this skill" and the step's name must be enough.

Check for each file of step 0, one by one, which step first needs it; the task's weak point is that
a template may be needed already at step 2 or 3. An incoming reference to a section of this skill
must keep working: search for them, and note `product-guidelines/styleguide/template.md:75`,
`project-level/task/skill/guideline_findings.md:21`, and the task's point on the section name
"Writing the file" at `product-guidelines/styleguide/SKILL.md:50`.

## Materials the request needs

Write them under `.runs/task-cycles/styleguide-skill-shape/reports/`, never in the tracked tree;
any helper script stays under `.runs/task-cycles/styleguide-skill-shape/`.

- `assessment.md`: the table of To do 4. One row per fragment, each nonblank line of
  `product-guidelines/styleguide/SKILL.md` at the base in exactly one row, each quote literal and
  whole with its line range on 525cde1 (permalink form:
  `https://github.com/mariusznazar/the-way/blob/525cde1dd53c474f56ea0ece289cb60e868aa90d/product-guidelines/styleguide/SKILL.md#L1-L4`),
  no summaries. Columns: the fragment, when it is needed, whether an agent recognises that moment,
  the verdict with reason and ground, and the fragment's new place. Proposals stand in rows of
  their own kind and are listed once more at the end. Put the output of `check_instructions.py` and
  the contradictions between files that load together before and after the table, as `judging.md`
  gives.
- `word-counts.md`: the seven routes of To do 4, two figures each, before and after. Words are
  whitespace-separated, Markdown and frontmatter included; of a file read by sections, the sections
  read. Rules of the count, from the cycle's record:
  - every read of the route counts, refine-task's own first reading of a file the skill makes the
    session read again included, in both states; a file read twice in "before" counts twice (task
    question 3); give for each route one more figure without those first reads, so that it can be
    set beside the task's estimate of about 8850 and 5900 words;
  - a file a counted file sends the session to on the route counts in both states, such as the
    files beside `elements/common/critique/SKILL.md` for the author who settles a critique;
  - "pierwszy styleguide, są ekrany" is counted with a human without a preference, so research and
    audit both run; say so beside the route;
  - the product's own files and foundation entries differ by product and are left out of both
    states; say so;
  - each route's file list stands in the report, file by file with its word count, so that a reader
    can add it up.

## Your own check

Name your weakest point, as the method gives. It is rule preservation: show, with a helper that
compares the base `SKILL.md` with the rebuilt files sentence by sentence, whitespace normalised,
which sentences differ, and account for each difference as a pointer, a table row or a
meaning-preserving rewording. Check also each quote of `assessment.md` against the base, line
coverage, and each route's sum.

Run `python -B elements/common/foundation_check.py`,
`python -B instruction-files/check_instructions.py .`,
`python -B agent-instructions/skill_entry_points.py --write` (it should change nothing; say so if it
does) and `python -B gate/run_tests.py agent-instructions`. Compare the `check_instructions.py`
output with the base. A dead-path warning on `AGENTS.md` for `_zadania\` stands on the base and is
not yours. Do not run the whole gate; its run is the orchestrator's.

## Foundation to read

Read each whole, by "Reading the foundation" in `elements/common/way_of_working.md`:

- Decisions: WAY-01, WAY-14, WAY-28, WAY-29, WAY-35, WAY-51, WAY-60, WAY-69, WAY-80, WAY-86,
  WAY-100, WAY-107, WAY-113, WAY-120, WAY-121, WAY-123, WAY-124, WAY-125, WAY-127, WAY-128, WAY-129,
  WAY-134, WAY-150, WAY-154, WAY-155, WAY-165, WAY-167, WAY-168, WAY-172, WAY-173, WAY-174, WAY-176,
  WAY-177, WAY-180, WAY-182, WAY-183, WAY-184, WAY-185, WAY-186, WAY-187, WAY-189, WAY-191, WAY-192,
  WAY-213, WAY-214, WAY-215, WAY-251, WAY-256, WAY-257, WAY-258, WAY-259.
- Part map: `product-guidelines`, `instruction-files`.
- Invariants: outbound-link-reach, repository-file-location, skill-entry-points,
  instruction-file-imports, derived-file-content, foundation-change-merge-route.
- Glossary: the terms the moved text uses.

A decision you need beyond these is a reach: read it and name it in your report.

## Commits and report

- Before a script, read `C:\Storage\The Brain\The Brain\.ai\rules\scripts.md`; before a commit,
  `C:\Storage\The Brain\The Brain\.ai\rules\git.md`; before changing a skill,
  `C:\Storage\The Brain\The Brain\.ai\rules\knowledge_artifacts.md`. The skill's files are in English,
  with LF line endings, in the style of the rebuilt skills, for example
  `elements/decisions/skill/SKILL.md`.
- Commit on the task branch with `git add <paths>`; keep the worktree clean; verify the author
  address with `git log --format='%h %ae'`. Do not push and do not open a request.
- Full report: `.runs/task-cycles/styleguide-skill-shape/reports/author.md`, with each check's
  command and exit code, every choice you made with the way not taken, every reach beyond this
  handoff, your concerns, and **Searches not found or unclear**.
- Return: your status, your commits, a one-line check result naming what failed or did not run, and
  the report's path.

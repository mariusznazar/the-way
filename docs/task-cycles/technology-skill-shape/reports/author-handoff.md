# One-author handoff

The user invoked the-way-implement-task and delegated intermediate choices to the orchestrator; the human reviews the request, not intermediate steps. Questions go to the orchestrator, never to the human. Do not read `cycle.md`.

## Where you work

- Worktree: `C:/Storage/repos/the-way/.runs/worktrees/technology-skill-shape`, branch `task/technology-skill-shape`, base `525cde1dd53c474f56ea0ece289cb60e868aa90d` (on `foundations`). Run every command there. Change nothing in the original checkout or outside the repository; reading outside it is allowed.
- Your method: `task-cycle/change/SKILL.md` in this worktree. Read it whole; read a file it names only when the step or variant that names it comes. Your variant is "the whole change as the one author".
- Stage boundary: make the change and its foundation step (`task-cycle/skill/foundation_step.md`, read it when that stage comes; the task carries no entries, so expect nothing to write, and say so), commit, return before review. Do not push, do not open a request, do not run the full gate: `python -B gate/run_tests.py` over all directories is the orchestrator's. Do not start the return step.

## The task

Frozen task, read whole: `.runs/task-cycles/technology-skill-shape/task.md`, under the worktree. No spec, no plan. Everything required stands in it and is not restated here. Its To do items 1–6, Acceptance criteria and Questions 1–7 bind you; *Out of scope* binds you too.

Answers of step 4: trust boundary no; irreversible operation no; no open design choice (the division and names of the files beside the skill are choices of how to make what the task settles: make them and name them in your report). A choice that would change a rule's meaning beyond To do 2 and 3 is not yours: it stands as a proposal in the assessment (To do 6).

## How to do it

- Judge first: use the skill `the-way-maintain-instruction-files` from this worktree (`instruction-files/SKILL.md`), mode of judging, kind "skill" (`instruction-files/kind_skill.md`), on `project-level/technology/SKILL.md`. Per the task's Context, the judgement searches Codex's session records too. The one real run: `C:\Users\Mariusz\.codex\sessions\2026\10\04\rollout-2026-10-04T18-10-39-01a107ae-806d-71e2-b005-c14a317d7a7f.jsonl.zst`. Python has no `zstandard` module here; the `zstd` command is on the PATH (poppler's binary), so `zstd -dc <file>` decompresses to stdout. Check it works; a row's ground must not be "not found" caused by an unread compressed file. Run outputs of that run: `C:\Storage\repos\loop2\.runs\technology-research\`.
- Then rebuild according to the judgement.
- Line numbers in the task's acceptance criteria refer to `project-level/technology/SKILL.md` at `525cde1`.
- The skill's `description` line and its numbered steps are named from elsewhere: `project-level/skill/SKILL.md:139`, `installation/README.md:57`, `elements/decisions/skill/projected.md:6`, `project-level/definition_template.md` lines 104, 152, 243 and 300, `installation/install.py:34`. Check each still reads true after the change. Where a reference outside `project-level/technology/` would have to change, tell the orchestrator in your report rather than widening the task on your own, unless the reference is simply false after the move.
- `elements/common/way_of_working.md` is named by the skill for "the question `way_of_working.md` asks after a choice" (`SKILL.md:146`) as well as for "How a skill asks" and "Reading the foundation". A plain-name reference to a file must still resolve for an agent that reads a file beside the skill by its path, with no entry point and no `SKILL.md`.
- The file holding the research agent's work must also carry what that agent needs to find the-way's paths and the rule that the step does not write the product's foundation; the task's fourth acceptance criterion is the test of that file. Words `the template's Technology section`, `the definition`, `the choice`, and any other term it uses must be something the leader's list gives it.

## What the task names for the request

Write them as reports, in English, not in the tracked tree. Scripts you need for them stay under `.runs/task-cycles/technology-skill-shape/`; no tracked Python changes.

- `.runs/task-cycles/technology-skill-shape/reports/assessment.md`: the table of To do 4: each fragment quoted literally with its line range at `525cde1`, when it is needed, whether an agent recognises that moment, the verdict; every non-blank line of the file belongs to a row. Below it the proposals of To do 6, each with the cost of leaving it and of making it, the template-reading proposal judged by `instruction-files/judging.md`.
- `.runs/task-cycles/technology-skill-shape/reports/word-counts.md`: the five routes of To do 4, by the counting rule of To do 5, before and after, with the file list of each route; words as whitespace-separated tokens of each whole file (`len(text.split())`), and for the sections of `way_of_working.md` and of `definition_template.md` that the rule counts alone, name how a section's bounds were taken.

An example of the form, and no more than that: task 3's assessment and counts at commit `72b66deea825bffd1b84ffe64a6702f9884dfda5`, `docs/task-cycles/foundation-skills-shape/reports/assessment.md` and `word-counts.md`, read with `git show`.

## What to read

Foundation, each entry whole, from `foundations/`:

- Decisions: WAY-35, WAY-100, WAY-106, WAY-111, WAY-112, WAY-113, WAY-116, WAY-117, WAY-118, WAY-120, WAY-121, WAY-122, WAY-123, WAY-125, WAY-127, WAY-128, WAY-137, WAY-138, WAY-139, WAY-150, WAY-165, WAY-166, WAY-256, WAY-257, WAY-258, WAY-259.
- Invariants: project-technology-record, project-readiness-gate, repository-file-location, outbound-link-reach, derived-file-content, skill-entry-points.
- Part map: the entry `project-level`.
- Environment facts, as WAY-256 links them: single-rule-compliance, instruction-density-accuracy, claude-skill-nested-references; as WAY-258 links.
- Glossary: `foundations/glossary.md`, the terms the skill uses.

Other reading: `agent-instructions/README.md`; `project-level/definition_template.md` whole; `elements/common/critique/SKILL.md` with `prepare.md`, `check.md`, `settle.md` beside it; `elements/common/way_of_working.md`, the two sections the task names; `project-level/skill/SKILL.md` around step 6. Guidelines: empty selection (the task's question 6).

Also, as the user's own instructions require before these acts: `C:\Storage\The Brain\The Brain\.ai\rules\knowledge_artifacts.md` before writing a skill's text, `C:\Storage\The Brain\The Brain\.ai\rules\scripts.md` before any script, one-liners included, `C:\Storage\The Brain\The Brain\.ai\rules\git.md` before committing, `C:\Storage\The Brain\The Brain\Notes\Areas\(A) Claude code\konwencje_skilli_i_commandow.md` before editing a skill. Where they differ from the repository's own rules, the repository's stand.

## Commits

English messages, in the form of the repository's log; `git add` by explicit paths, never `-A`. All files are LF (`* text=auto eol=lf`). After your first commit check `git log -1 --format='%h %ae'`: the address must be the private one (`mariusznn@gmail.com`), which the conditional git config gives to this repository; if it is not, stop and say so. Leave a clean worktree.

## Weakest point to check before you return

Rule preservation and reach, which review of a move cannot take on trust. Make a check of your own that shows: every sentence of the old `SKILL.md` stands in the new files word for word or is listed with its exact new wording and why the meaning holds; and each acceptance criterion's named case in a file that its reader really reads, on each of the five routes. A resumed leader that skips step 1 and an agent reading the research file alone are the cases to walk through by hand.

## Report

Full report: `.runs/task-cycles/technology-skill-shape/reports/author.md`, as your method gives it, with the section **Searches not found or unclear** (`none` where none). Every check carries its exact command and exit code. Short return: status, commits, one line of check results naming what failed or did not run, the report's path.

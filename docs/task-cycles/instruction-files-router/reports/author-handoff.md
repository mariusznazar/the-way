# Author handoff — instruction-files-router

The user invoked the-way-implement-task for the frozen task below and delegated intermediate choices
to the orchestrator; the goal is a reviewable pull request into `foundations`. You are the one
author of a change without a plan. No answer you get from the orchestrator is the human's approval.

## Where and how

- Worktree: `C:/Storage/repos/the-way-wt/instruction-files-router`, branch
  `task/instruction-files-router`, base `0b8c1bd613b94bce290e49aad9eaf1d0b2587b02`, target
  `foundations`. Work from the worktree's root; write nothing outside it.
- Method: read `task-cycle/change/SKILL.md` of this worktree whole, with every file it names, and
  follow it as the one author. Also read `agent-instructions/README.md` (the-way is the top-level
  repository; its integration route applies).
- Stage and boundary: make the change with its foundation step, commit, and return before review.
  You will be resumed later for any fix and for the return step.
- Foundation step: read `task-cycle/skill/SKILL.md`, section "Execute, verify and review", the
  paragraph starting "The foundation step writes" whole, and write each entry through the element
  skill it names in this worktree (`elements/decisions/`, `elements/environment-facts/`, others if
  needed), which selects its own reading by its step 1.
- Frozen task: `.runs/task-cycles/instruction-files-router/task.md` — read it whole. It is in
  Polish; the-way's files are in English. Meaning sentences of foundation entries for the request
  are in Polish (the task document's language).
- Answers of step 4: trust boundary — yes in letter: `instruction-files/check_instructions.py` is
  the part's trust boundary and To do 9 touches only its module docstring; change nothing else in
  that file. Irreversible operation — no. Human actions — none.
- Spec: none. Plan: none. Route reason: rows 1–7 of *Settlements to record* and To do 1–9 settle
  every meaning; the names of the new files and the distribution of today's sections of
  `principles.md` over `SKILL.md`, the kind files and (only if row 5's condition holds) a shared file
  are choices of how to make what the task settles: make them and name each in your report. If you
  meet a genuinely open design choice the task and foundation do not settle, return `returned` with
  no code, as the method gives.
- Guidelines: selection empty (the-way has no `guidelines/`; the task settles that it writes no
  code — the only `.py` edit is a docstring).
- Gate: do not run `python -B gate/run_tests.py` without a directory; the orchestrator runs the
  gate. Run focused checks: `python -B gate/run_tests.py instruction-files`,
  `python -B elements/common/foundation_check.py`,
  `python -B agent-instructions/skill_entry_points.py` (and `--write` after the description changes,
  committing what it writes), `python -B instruction-files/check_instructions.py` where it applies
  to files you change, `git diff --check`.

## What to read

Whole, in this worktree:

- `instruction-files/SKILL.md`, `instruction-files/principles.md`, `instruction-files/tool_loading.md`,
  the head of `instruction-files/check_instructions.py`, `product-guidelines/template.md` around
  line 127.
- Decisions, each whole (heading to next heading, with rationale and *Rejected*): WAY-128, WAY-35,
  WAY-127, WAY-125, WAY-129, WAY-130, WAY-131, WAY-132, WAY-133, WAY-100, WAY-09, WAY-27, WAY-102,
  WAY-192, WAY-212, WAY-245, WAY-254, WAY-19, WAY-07, WAY-30, WAY-33, WAY-114, WAY-134, WAY-36,
  WAY-11, WAY-01.
- Environment facts: `single-rule-compliance`, `instruction-density-accuracy`,
  `context-file-effect`, `claude-code-project-skills`, `claude-code-path-rules`,
  `claude-code-imports`, and any that WAY-128 to WAY-133 rest on.
- Part map: entries `instruction-files`, `agent-instructions`, `decisions`, `environment-facts`,
  `product-guidelines`.
- Invariants whose *Part* is `every` or `instruction-files`, notably `instruction-file-imports` and
  `skill-entry-points`; glossary entries of the terms you use.
- The arXiv source of `instruction-density-accuracy` (https://arxiv.org/abs/2507.11538v1) and the
  Anthropic page quoted in the task
  (https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) for the exact
  words of rows 6 and 7; follow the reading form the environment-facts skill gives.
- User's read-only references, because the change edits a skill and rules (do not edit them):
  `C:/Storage/The Brain/The Brain/Notes/Areas/(A) Claude code/konwencje_skilli_i_commandow.md`,
  `C:/Storage/The Brain/The Brain/.ai/rules/knowledge_artifacts.md`, and before any script
  (including a one-off `python -c` or heredoc) `C:/Storage/The Brain/The Brain/.ai/rules/scripts.md`.

## What to make

Every item of *To do* 1–9 and every row 1–7 of *Settlements to record*, with these points of the
task kept:

- Row 1 changes the meaning of WAY-128's last sentence, as the task's answers record; WAY-35 stays.
  Rows 1–5 are one decision on the new shape of the skill by the human's instruction; where the
  log's form (one decision — one question, WAY-19) requires splitting them, split, and name in your
  report which entry carries row 1 (its number goes to a later map update outside this cycle).
  Row 2 also changes WAY-128's first sentence by the case the task's answer gives.
- The kind file of skills (To do 2) asks of each fragment whether every use of the skill needs it
  or only one step or variant, for every skill, the-way's process skills included.
- The rewritten `instruction-files/SKILL.md` is itself a skill bound by the new criterion for every
  fragment you add or reword: what only one step or variant needs goes to a file beside it that
  that step names; no kind file points to another file.
- `description` of `instruction-files/SKILL.md` says the skill judges skills too; then regenerate
  the entry points with `--write` and commit them.
- Replace "Length has no threshold" by the conclusion of To do 6; give the "one level deep" rule the
  new environment fact as its source, as the maker's recommendation for Claude.
- To do 9: point both references to where the content stands after the change.
- Do not touch the vault, `C:/Storage/repos/the-way-global` or any map note (Out of scope).

Preserve each file's existing line endings (read and write bytes or `newline=''`). Stage by explicit
paths only; commit messages in English. Do not push or open a request.

## Report

Write the full report to
`C:/Storage/repos/the-way-wt/instruction-files-router/.runs/task-cycles/instruction-files-router/reports/author-report.md`:
status, commits, changed paths, each check with its exact command and exit code, the weakest-point
check and what it showed, every reach beyond this handoff, your choices (file names, distribution of
sections, any split of the decision) each with the option rejected, every foundation entry written
or changed by identifier with one Polish meaning sentence, and the mapping of settlement rows 1–7
to entries. Return only: status, commits, a one-line check result naming what failed or did not
run, and the report's path.

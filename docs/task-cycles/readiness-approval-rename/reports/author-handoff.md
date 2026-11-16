# Handoff to the one author — readiness-approval-rename

**The user's delegation.** The person who requested this cycle has delegated intermediate choices to
the orchestrator; no answer or go-ahead the orchestrator gives is that person's approval. Do not ask
the human anything; send questions to the orchestrator in your report (status `questions`).

**Worktree.** `the task's worktree (the repository's root)` (the-way itself; the pin is the
worktree's own files). Branch `task/readiness-approval-rename`, base `4758840fbaf9562db960965c706d8681c3d23a43`.
Work from the worktree's root. Make commits on this branch; use `git add <paths>`, never `git add -A`.
Commit messages in English, in the form of the repository's earlier commits.

**Your stage and variant.** Method: `task-cycle/change/SKILL.md` in the worktree (`make-change`); your
variant is the words of its row: **the whole change as the one author**. Read its `SKILL.md` whole,
and a file it names (`task-cycle/change/*.md`) only when the step that names it comes. You do the
foundation step with your code (`task-cycle/skill/foundation_step.md`, read whole; and the
`SKILL.md` of an element at the path that file gives when you write an entry of that element — here
the glossary: `elements/glossary/skill/SKILL.md`, which is `record-glossary-term`). You stop at your
boundary: the review, the full gate and the return step are the orchestrator's (the return step is a
later turn of yours). **Do not run the product's gate** (`python -B gate/run_tests.py` without a
directory, or any run of every test): its run is the orchestrator's or CI's. Run the focused checks of
the directories you touch, `python -B gate/run_tests.py <directory>`, and `python -B
elements/common/foundation_check.py`.

**Files of the cycle you may read.** `cycle.md` and other files of the cycle's record directory
(`.runs/task-cycles/readiness-approval-rename/`), other agents' handoffs, reports and findings, are not
yours to read, except those this handoff names: the frozen task and this handoff.

**The task (read whole).** `.runs/task-cycles/readiness-approval-rename/task.md` — the frozen task
document (its source is the author's private note; do not copy its path into any file of the
repository). It binds: *To do* 1–11, *Questions to settle* with their answers, *Settlements to record*
rows 1–6, *Decisions in play*, *Out of scope*. The route has no spec and no plan.

**Answers of step 4 of the cycle.**
- Trust boundary: **yes**. The part map names `project-level/readiness_check.py` and
  `process-audit/audit_count.py` as trust boundaries; you edit their section names, status values,
  messages and docstrings. Do not change what they accept beyond the settled rename; keep their
  input handling as it is. Every review will check crafted input at these two files.
- Irreversible operation: **no**.
- Open design choice: **none**. Everything the task leaves is a choice of how to make what it
  settles; make it and name it in your report (the orchestrator enters it in the questions table).
  If you meet a real open design choice, return `returned` with a report and no code.
- Reserved choice: none.

**Foundation to read (by identifier; each whole, an entry running to the next heading).** Select the
rest by "Reading the foundation" in `elements/common/way_of_working.md` for the parts you touch. Named
by the orchestrator:
- Decisions: WAY-99, WAY-95, WAY-97, WAY-34, WAY-114, WAY-117, WAY-118, WAY-126, WAY-27, WAY-107,
  WAY-140, WAY-320, WAY-330, and those the task names as carrying `projected entry` in a binding
  sentence (WAY-106, WAY-116, WAY-124, WAY-134, WAY-142 to WAY-146) and WAY-156, WAY-376 as the task
  lists them.
- Glossary: `foundations/glossary.md` entries `gate`, `entry`, `read off` (each whole), and
  `elements/glossary/template.md`, `elements/glossary/skill/SKILL.md` for the new entry.
- Invariants: `project-readiness-gate` (to be renamed `project-readiness-check`) and every invariant
  or test line that cites it.
- Part map: `foundations/part_map.md`, the parts `project-level`, `process-audit`, `task-cycle`,
  `gate`, `elements-common`, `agent-instructions`, `decisions`, `glossary`, `invariants`.
- Guidelines: `guidelines/coding.md` whole before you change code; `guidelines/testing.md` whole
  before you write or change a test.
- `agent-instructions/README.md` (the guide of work on the-way before `main`).

**What the task asks, summarised only to route you; the task document binds.** Rename the projected
meaning of `gate` (readiness gate → readiness approval, gate record → approval record, bare "the gate"
in that meaning → a phrase of the new name, `ready for gate` → `awaiting approval`, identifier
`project-readiness-gate` → `project-readiness-check`, file name `readiness_gate.md`, section
headings, skill descriptions, script messages); rename the location-file meaning of `entry` to `key`
and "backlog entry" to a phrase with "line"; rephrase the documentation meaning of `read off`; write
one glossary entry `projected entry` with `record-glossary-term`. Search the English text of every file
git tracks, by WAY-97, for each word whose meaning moves; judge each use by its meaning (a sentence
where `gate` means the test command, the part `gate` or its directory stays; `entry` in the meaning of
a foundation entry stays). Names in code (`entry_path`, `REGISTER_ENTRY`) and values of keys inside the
locations file stay. Texts in Polish are not searched. Where a copy of the skill entry points
(`.claude/skills/`, `.agents/skills/`) or the agent-type copies change, regenerate them as `AGENTS.md`
gives (`python -B agent-instructions/skill_entry_points.py --write`, and where a definition in
`task-cycle/agent-types/` changes `python -B agent-instructions/agent_type_copies.py --write`) and
commit what they write.

**Open item for you to settle and name in the report.** The task asks (*To do* 6) that the request's
description tell products to change `## Gate record` → `## Approval record` and the `## Backlog`
wording of their `AGENTS.md`; that is the orchestrator's, written at the request. Do not write it.
The status value `awaiting approval` replaces `ready for gate` in the template, scripts and tests;
the task says `ready for approval` is taken (a turn result), do not use it.

**Another change in flight.** The task "decision log after the foundation review of 2026-11-14"
(not in this worktree) also changes WAY-27 and WAY-320 with the phrase "entry of the locations file"; it is
not merged. Do nothing about it; the cycle that merges second reconciles.

**Searches.** Record in your report, under **Searches not found or unclear**, every thing you looked
for and did not find or found unclear; `none` if nothing. Under **Unread material**, what this handoff
names that stayed unread or was read in part; `none` if nothing.

**Working copies (word for word from `task-cycle/skill/SKILL.md`).** An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed,
except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
says, to the place the product's foundation settles for screenshots, and into the agent's directory
only where no such place is settled. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
`git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed.

Your directory for working copies: `.runs/author/`.

**Report.** Write the full report to `.runs/task-cycles/readiness-approval-rename/reports/author-report.md`
as `make-change` gives it (status, commits, checks each with command and exit code, own-work check,
**Unread material**, **Searches not found or unclear**, working copies, the choices you made). Return
only the status, commits, a one-line check result, and the report's path.

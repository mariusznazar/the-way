# Handoff to the reviewer of the whole change — readiness-approval-rename

**Delegation.** The person who requested this cycle has delegated intermediate choices to the
orchestrator; nothing the orchestrator says is that person's approval. Do not ask the human anything;
put questions in your report (first line `questions`).

**Worktree.** `the task's worktree (the repository's root)` (the-way itself). Work from its
root. You are read-only on the change: do not edit or commit the branch.

**Your stage.** Method: `task-cycle/review/SKILL.md` in the worktree (`review-change`); the review of
the whole change, as that skill gives it. Read its `SKILL.md` whole and a file it names only when the
step that names it comes. Your first line is `PASS <sha>` or `FAIL <sha>`; the report goes to
`.runs/task-cycles/readiness-approval-rename/reports/review-whole-report.md`. Do not run the product's gate
(`python -B gate/run_tests.py` without a directory); run focused checks of the directories you
judge, if you need to (`python -B gate/run_tests.py <directory>`, `python -B elements/common/foundation_check.py`).

**Range.** Base `4758840fbaf9562db960965c706d8681c3d23a43` (merge of PR #146 into `foundations`) to head
`79c9bfb9` — one commit by the one author (59 files, +395 −386). The route has no spec, no plan, no
slices, no slice reviews, and the pin was not moved.

**What you read.** The frozen task whole: `.runs/task-cycles/readiness-approval-rename/task.md` (its
source is the author's private note; copy no path of it into your report). The author's report:
`.runs/task-cycles/readiness-approval-rename/reports/author-report.md`. You select your own foundation
and guidelines by the parts of the change ("Reading the foundation", `elements/common/way_of_working.md`)
and `guidelines/coding.md`, `guidelines/testing.md`. Read the full diff. `cycle.md` and other files of
the record directory are not yours to read.

**Answers of step 4.** Trust boundary: **yes** — the part map names `project-level/readiness_check.py`
and `process-audit/audit_count.py`; the change edits their section name, status value, messages and
docstrings. Check crafted input at these two files: a definition with the old heading `## Gate record` or
the old status `ready for gate` (does it now fail cleanly, as the task intends — nothing accepts it by
accident?), a register read with the renamed key wording, and that nothing else about what they accept or
refuse changed. Irreversible operation: **no**.

**What to check beyond the code** (the task binds all of it):
- Coverage of every *To do* item 1–11 and every row of *Settlements to record* 1–6; source fidelity to
  the task's *Questions to settle* answers (new names `readiness approval`, `approval record`,
  `awaiting approval`, `project-readiness-check`, `key`, "the task's line in the backlog").
- Search by WAY-97 of the English text of tracked files for what remains of the moved meanings:
  projected-meaning `gate` (including bare "the gate", "its gate", "gated"), `entry`/`entries` in the
  sense of a locations-file key, "backlog entry" in the sense of a task's line. Judge uses by meaning:
  `gate` meaning the test command, the part `gate`, its directory and `gate/` stay; `entry` meaning a
  foundation entry stays; `read off` of the tool meaning stays.
- Each decision the change edits keeps its meaning (the task: "znaczenie bez zmian"); the author
  reworded the first clause of WAY-118 ("The readiness gate blocks a definition…" → "The readiness
  approval is blocked by a missing section, …", author's choice 3) — judge whether that keeps the meaning.
- The author changed existing tests in `process-audit/test_audit_count.py` (expected message substrings and
  test names, author's choice 4); judge it against "Changing an existing test" of `guidelines/testing.md`.
- The author's choices 1–8 in its report (file name `readiness_approval.md`, renamed Python names in
  `project-level/`, wording of bare uses, `intermediate human gates` → `intermediate human approvals`,
  `read off` places moved and left, glossary form of `gate`'s *Not* and the new `projected entry` entry,
  a claim of the task's *Context* it did not find).
- The new glossary entry `projected entry`: meaning, form per `elements/glossary/template.md`, `Not`.
- The foundation checks hold (`python -B elements/common/foundation_check.py` exit 0, with tests citing
  the renamed invariant `project-readiness-check`).
- Skill entry points in `.claude/skills/` and `.agents/skills/` regenerated for the changed descriptions
  (`agent-instructions/skill_entry_points.py`).

**Gap the orchestrator carries to you.** The author's *Unread material* says it read whole only WAY-118,
WAY-126, WAY-145, WAY-107 and WAY-320 of the decisions the handoff named, took WAY-99, WAY-95, WAY-97 and
WAY-34 from the text the task quotes, and read the others by passages around search hits; the invariant
`project-readiness-check` was read by heading and sentence, and `foundations/decisions.md`,
`process-audit/audit_count.py`, `process-audit/test_audit_count.py`, `project-level/plan_check.py`,
`task-cycle/skill/SKILL.md`, `project-level/test_plan_state*.py`, `project-level/test_plan_check.py` were
edited from the regions the edits touch. You are the first agent to judge those whole decisions against
the change: read WAY-99, WAY-95, WAY-97 and every decision whose binding sentence the diff touches whole.

**Not yours to grade.** Texts in Polish; files of loop2 and its pin; the request description for
products (To do 6: it is the orchestrator's, written at the request).

**Grades and report.** As `review-change` gives: blocking findings with the slice they come from (none —
no slices), mark any blocking finding that contradicts a settlement with `Contradiction: yes`, Minor and
outside-the-scope findings apart, with the place in the code. Report also **Unread material** and
**Searches not found or unclear** (`none` if nothing), and the checks you ran with command and exit code.

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

Your directory for working copies: `.runs/review-whole/`.

Return only the report's first line, the changed-file counts you judged, a one-line check result and the report path.

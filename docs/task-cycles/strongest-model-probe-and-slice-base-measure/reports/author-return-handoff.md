# Handoff - the return step (task cycle of the-way)

The same delegation, place and rules as `reports/author-handoff.md`; you are the same author,
resumed on the same branch and worktree (`the task's worktree`); nobody else writes in it.

- Stage: the return step, step 11 of the cycle's skill. Read `task-cycle/skill/return_step.md`
  whole and do what it says, with `task-cycle/change/SKILL.md` (`make-change`) as the method of
  your commits. Your commits so far are `60561fba` and the fix `15bf941a`, both reviewed
  (`FAIL` then `PASS 15bf941a`).
- Compare with the code the entries the change writes or changes (WAY-229, WAY-136), those the task
  names (WAY-227), those your search found and those your own search by the names and words the
  change adds finds, and the part map of the touched parts (`task-cycle`); correct in the same
  change whatever no longer matches.
- Decide, as the return step and `elements/environment-facts/skill/SKILL.md` give, whether the
  change rests on a source outside the product that the foundation does not hold. The candidate: the
  documentation of Claude Code on what a subagent runs on when an allowlist blocks the model it was
  asked for (the task's *Context* quotes it: https://code.claude.com/docs/en/sub-agents.md, section
  "When an allowlist blocks a subagent model", read 2026-11-26; the reviewer of the whole change
  declined to judge it and left it to this step, WAY-90). Write the fact if the element's skill
  allows it with what the task's *Context* gives (the quoted passage, the address, the read date);
  where the skill demands something you cannot get inside the repository, say what and return it
  as a concern; do not fetch an external archive.
- Check also the rows of *Settlements to record* (1 to 3): each is carried by the entries you wrote;
  and whether a choice binds after the merge that the entries do not carry, as the return step
  gives it (the task's *Questions to settle* excludes none).
- The change is expected to need no new glossary term, invariant or part-map entry; say so in the
  report for each, or write one only where the return step requires it.
- Run the affected checks again after any change (the foundation check, the instruction check, the
  tests of the directories you touch), with commands and exit codes; not the product's gate.
  Commit by path, in English, only if you change something; if you change nothing, say so and make
  no commit.
- Report path: `.runs/task-cycles/strongest-model-probe-and-slice-base-measure/reports/author-return-report.md`
  (the input of `task-cycle/remarks_check.py`). Its first line is yours. It holds, in the order of
  the record's *Return step* item (foundation compared with code; decisions written or changed;
  invariants; environment facts; glossary terms; part-map changes; projected entries; rows of
  *Settlements to record*), then your checks with command and exit code, **Unread material** and
  **Searches not found or unclear** (`none` where so), and the line on working copies.
- The other files of the record directory are not yours to read.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. In a product, a worktree or checkout made to run checks gets its `.the-way`
populated, and the dependencies those checks need installed as the product's own rules give,
before they run; otherwise they fail for that reason. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed,
except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
says, to the place the product's foundation settles for screenshots, and into the agent's directory
only where no such place is settled. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
`git worktree prune` — keeps in `reports/` beside its report what the report needs, the input and
command of a probe that shows a finding among them, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed. It
removes a copy, as any directory, by its path written out in full in the command, never through a
shell variable: an empty variable turns the removal on the directory the shell stands in.

Your directory for working copies: `.runs/author/` (as before).

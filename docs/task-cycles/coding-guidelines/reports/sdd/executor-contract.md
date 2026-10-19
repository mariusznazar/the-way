# Executor contract — coding guidelines slices (task cycle steps 9–10, SDD 6.4.1)

Applies to every slice executor, in addition to its brief and the Superpowers 6.4.1 implementer
template's rules (you do all the work yourself; you never dispatch a subagent or a reviewer).

- **Delegation.** Mariusz asked for the-way's task cycle to take this task to a pull request; the
  orchestrator holds his delegation. You never ask Mariusz anything; questions go back to the
  orchestrator (status NEEDS_CONTEXT or BLOCKED).
- **Authority.** The frozen task `docs/task-cycles/coding-guidelines/task-frozen.md` binds over the
  reviewed spec `docs/task-cycles/coding-guidelines/spec.md`, which binds over the plan; rulings
  `reports/design-rulings.md` (C1–C21) are applied in the spec; the cycle record's questions table
  (`cycle.md`) holds later rulings (C22–). Your brief is your requirements.
- **Worktree.** `/home/user/the-way`, branch `claude/gallant-albattani-3k15lc`. Change only the
  files your brief names. `product-guidelines/test_form_check_invariants.py` and
  `installation/test_install.py` are **read-only** (invariant tests, WAY-03): if your work needs
  either changed, stop and return BLOCKED with the reason. Foundation files are read-only too.
- **Method.** Superpowers 6.4.1 `test-driven-development` for behaviour changes, read whole from
  `/tmp/claude-0/-home-user/ac1b534a-8705-5f4d-8b69-597c339e545d/scratchpad/superpowers-6.4.1/skills/test-driven-development/SKILL.md`
  (a clone of tag v6.4.1; no installed plugin). Python is 3.13.16 (`python3`; the repository
  declares 3.14) — name it in your report.
- **Open design choice.** If you meet a choice the task, spec and foundation leave open (more than
  one way, none settled), stop: return a report **without code and without a diff** naming the
  choice, where it shows, the ways open and what you found. A choice of how to make what is settled
  is not one: settle it and say so in your report.
- **Too large.** If the slice is more to read or change than you can hold, or its goal splits,
  return a report of where the size lies, without code.
- **Tools.** Edit files with the Edit/Write tools or the shell only; never use the Artifact tool or any publishing or external-posting tool.
- **Commit** your work (one or more commits), message in English describing what the commit holds,
  ending after a blank line with:

      Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
      Claude-Session: https://claude.ai/code/session_01DYywki95VF5wQGh3SzcQZB

  Do not push.
- **Weakest point (WAY-164).** Before returning, name the requirement of your slice, read against
  the task, that your work most likely does not meet; write a check that would catch it (a test, or
  a manual check with method, actor, observed result and evidence), run it, and state in your report
  which requirement, which check and what it showed.
- **Report** to the path the dispatch names: what you implemented; TDD evidence (RED command and
  failing output, GREEN command and passing output) where behaviour changed; every check command
  with its exit code and the path of its complete output saved beside the report
  (`slice-N-<name>.txt`); failed and unchecked checks by name; the changed-file list with added and
  removed line counts for your commit range (`git diff --numstat <base>..HEAD`); the sharpness
  inputs from your actual diff — parts touched (by `foundations/part_map.md`), trust-boundary files
  touched, any irreversible operation; questions and choices with evidence; self-review findings;
  concerns. Then return under 15 lines: status (DONE | DONE_WITH_CONCERNS | BLOCKED |
  NEEDS_CONTEXT), commits, one-line check summary, concerns, report path.

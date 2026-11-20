# Handoff — the review of correction 2

You are the reviewer of the whole change, resumed to review correction 2, made for the human's remarks on
the open request. The person who requested this cycle delegated intermediate choices to the orchestrator; no
answer here is that person's approval.

- Worktree and branch: the task's worktree, `task/decision-length-check`. Read-only: you change no tracked
  file and make no commit. Range of the correction: from `b0bba24d` (the head before correction 2) to
  `fa5d349e` (`git diff b0bba24d..fa5d349e`, `git log b0bba24d..fa5d349e`); confirm `git rev-parse HEAD` is
  `fa5d349e`. Three commits: `02bf399d` (WAY-05), `63436978` (the check and six tests), `fa5d349e` (the
  template and the two READMEs).
- Your method: `task-cycle/review/SKILL.md` and `task-cycle/review/fix.md` (the review of a correction made
  for the human's remarks). The remarks stand in place of a findings file:
  `.runs/task-cycles/decision-length-check/reports/correction-2-remarks.md`. Read them whole: they are what the
  correction must meet — item 1, the limit of 600 words for all the binding sentences of a decision together,
  with the error and the list of the same pattern as the limit of a paragraph, WAY-05, the template, the
  descriptions of what the check reports and tests holding the new sentence by a line `decision:`; item 2, a
  further paragraph that may carry a part of the entry's own question, in WAY-05 and in the template's section
  "Binding sentences", with any entry that says the opposite changed with them. "Not chosen" variants of the
  remarks must not be restored; WAY-05 must stay within all three limits.
- The author's report of the correction: `.runs/task-cycles/decision-length-check/reports/author-correction-2-report.md`;
  its claims are to be verified, not taken as evidence. Its **Unread material** says the author read the
  index of its selection only to its 120th line and opened WAY-05, WAY-12 and WAY-19 whole: the gap is
  yours to close for what the correction touches, as the method gives you the selection of the foundation
  for a correction that writes an entry (select by the parts touched — `decisions`, `elements-common`,
  `agent-instructions`, `repository` — and read what bears on the paragraph and the 600-word rules).
- The question the author left open and you must judge: the remarks say "If WAY-19 or another entry says the
  opposite, change it with them and name it in the request". The author held that WAY-19 does not say the
  opposite and left it unchanged; it changed the bullet of `elements/decisions/template.md` that cites WAY-19
  ("Changing a decision") instead. Read WAY-19, WAY-05 and the template's passages that speak of a part of a
  question and its paragraph or sentence, and say whether any entry still says the opposite of item 2 after the
  change (finding, graded). Your earlier finding on the wording of WAY-19 against WAY-05 (outside the task's
  scope then, `reports/review-correction-1-report.md` is not yours to read again: it is your own finding on the
  name "a part of another question" against "a part of the question the entry answers") now falls within the
  remarks of item 2: judge it again as the remarks put it.
- For the new code, repeat what you did for the first: mutations of the new check caught by the new tests, and
  probes on the real foundation (WAY-344 is the one entry over 600 words today; an added, an altered and an
  unaltered decision over the limit, a different division alone).
- Your directory for working copies: `.runs/review-correction-2/`; remove it before you return. Do not run the
  product's full gate; the focused runs of single directories and the check of the foundation are yours.
- Your report: `.runs/task-cycles/decision-length-check/reports/review-correction-2-report.md`, its first line
  `PASS <sha>` or `FAIL <sha>`, with graded findings (Critical, Important, Minor; Minor within or outside the
  task's scope; a blocking finding marked `Contradiction: yes` where it contradicts the settlements), the
  checks you ran each with command and exit code, **Unread material**, **Searches not found or unclear**, and
  your working copies. The frozen task is `.runs/task-cycles/decision-length-check/task.md`.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed, except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md` says, to the place the product's foundation settles for screenshots, and into the agent's directory only where no such place is settled. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed. It removes a copy, as any directory, by its path written out in full in the command, never through a shell variable: an empty variable turns the removal on the directory the shell stands in.

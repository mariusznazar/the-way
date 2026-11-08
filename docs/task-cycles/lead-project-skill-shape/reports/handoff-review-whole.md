# Handoff — review of the whole change

Delegation: the person who requested this cycle delegated every intermediate choice to the
orchestrator; nothing below is that person's approval. The human reviews the pull request only.

Worktree (read-only for you; work from its root): `the root of the worktree`
Branch `task/lead-project-skill-shape`. You make no change and no commit.

Method: read `task-cycle/review/SKILL.md` whole; the review of the whole change — it names
`whole_change.md`, which you read and follow when its step comes.

Range: base `57795e4e700dad1e5979bbc6c8fc4cd5f66c8da4`, head `038a330` (commits `e98f46b`, `b9e19f7`, `038a330`).
Compute the diff yourself (`git diff 57795e4..038a330`, `git log`). The base of the task's own line
ranges and "before" counts is `a3206c1` (`git show a3206c1:<path>`; on Git Bash on Windows set
`MSYS_NO_PATHCONV=1`); the difference between `a3206c1` and `57795e4` for the lead files is two
reworded lines of `project-level/lead/skill/SKILL.md` (130–134) and three of
`project-level/lead/conversation_template.md`, and the author reports it.

Frozen task (read whole): `.runs/task-cycles/lead-project-skill-shape/task.md`. It is a one-author
change without a plan and without a spec; no slice has a review of its own, so this review judges all
of it. The trust boundary and irreversible-operation answers are both `no`.

Author's report (a set of claims to verify, not evidence):
`.runs/task-cycles/lead-project-skill-shape/reports/author-report.md` — status `done with concerns`; it
holds the assessment table (55 rows), the word counts, the readers outside the skill, the author's checks
with commands and exit codes and the weakest-point check. Row 1 of *Settlements to record* is accepted
and settles its entry; its meaning in the report is sections 1 (English and Polish sentences marked
`row 1`).

What this review must cover, beyond `whole_change.md`:
- Every item of *To do* 1–7, every *Acceptance criterion* and the accepted row 1: say for each whether the
  change carries it and where it is shown.
- The acceptance criterion on the manual walk: walk **roads 1, 4 and 6** of question 5 by hand, from
  `SKILL.md` to the file of the last step, as an agent would (what is read, what stays, what drops out),
  and compare **each row** of the assessment table with the place where the fragment really stands.
  List what you walked and what you found.
- Rule preservation: outside WAY-256 and the places of *To do* 1, no rule disappears or changes its
  meaning; each reworded condition of a variant or pointer is compared with the base and adds no road
  and loses none; each new sentence — the opening lines of the new files included — has its exclusion
  named by the author; check the roads the criterion lists (task return: step 1 at the start and step 1
  repeated after a merge; `settle-technology` run: first and every later turn of a round, also after
  resuming from the conversation files; step 5: the `plan change` result in the paragraph after 3.6 and a
  changed definition in step 0; definition change: step 5 and the recovery of an open gate in step 0).
- The edit of WAY-256: three binding sentences at most (WAY-05); its *Rationale* takes the reason from the
  source of row 1 and its *Rejected* the ways Mariusz did not choose (the task's questions 3 and 11); the
  author reports an estimate ("five to fifteen percent more words") in the rationale — judge it against
  WAY-05; and that the sentences that contradicted row 1 are gone and nothing else of the decision moved.
  Check the one search of the foundation (WAY-33) for a place that still repeats the old rule.
- Limits: nothing changed outside `project-level/lead/skill/`, the WAY-256 edit and the places of
  *To do* 1; the skill's `description` and Python code unchanged; `answering.md`, `conversation_template.md`
  and other skills unchanged.
- Word counts: recompute every number the report gives (`wc -w` in the C locale, before at `a3206c1`,
  after at the head) and report any that disagrees.
- Readers outside the skill that the criterion lists: do they still land on the right text, and what
  does each lose.

Foundation and guidelines: you select your own by the parts the change touches (`decisions`,
`project-level`, `instruction-files`), as `whole_change.md` gives. The-way has no `guidelines/` of its own.

You may run focused checks of the touched directories (`python -B gate/run_tests.py <directory>`,
`python -B elements/common/foundation_check.py`); do not run the whole gate (the orchestrator runs it).
Before writing a script read the author's rules file on writing scripts.

Privacy: the report quotes no personal data of customers or users and no secret.

Report: write the full report to `.runs/task-cycles/lead-project-skill-shape/reports/review-whole-report.md`
as your method gives it (first line `PASS <sha>` or `FAIL <sha>`; each finding graded and marked within or
outside the task's scope; **Searches not found or unclear**; the checks with commands and exit codes).
Return the first line, a short summary, the findings' grades and the report path.

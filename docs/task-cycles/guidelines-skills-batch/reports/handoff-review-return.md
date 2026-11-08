# Handoff — review of the return step's commits (`review-change`)

You are a reviewer who did not make this change. Read-only. Work from the root of the worktree
`.`. Ask the human nothing.

Method: the project skill `review-change`, read
`task-cycle/review/SKILL.md` whole.
This is "the return step's commits", reviewed as its section 2 gives, against the task and the
foundation entries the return step writes or corrects. Not the review of the whole change.

- Range: base `2c46cb75cbcf30e5d495dda9dfe2f919ef0325fc` to head `f5ae96f` (take the full SHA from
  `git rev-parse HEAD` and confirm it; compute `git diff 2c46cb7..HEAD` yourself; one commit,
  two files, `product-guidelines/coding/SKILL.md` and `product-guidelines/testing/SKILL.md`).
- The task (frozen): `docs/task-cycles/guidelines-skills-batch/task.md`.
  The passages that bear on the change: *To do* items 17, 18 and 19, and *Decisions in play*
  WAY-282 and WAY-247 (read their entries whole in `foundations/decisions.md`, heading `### WAY-NN`).
- The return step's report (claims to verify): `...\reports\return-step.md` in the same record
  directory. The text it corrected should agree with `product-guidelines/coding/hand_back.md`,
  `product-guidelines/testing/hand_back.md` and `product-guidelines/audit_end.md`; read the passages
  of those that say where a skill hands back and judge whether the two corrected sentences say the
  same.
- Trust boundary: no. Irreversible operation: no.

Write the full report to `...\reports\review-return.md` (first line `PASS <sha>` or `FAIL <sha>`;
graded findings; checks you ran, each with command and exit code; reaches; and
**Searches not found or unclear**, each item or `none`). Return the first line, the report path and
a one-line result.

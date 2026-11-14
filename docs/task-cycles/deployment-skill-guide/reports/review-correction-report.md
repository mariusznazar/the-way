PASS aa21be7fa4aa23ab64dd0c7b701967f371c2fe74

# Review of the correction — task `deployment-skill-guide`, correction 1

Range: `31120e915a48edcbb3c59ad387b2c7f6ae9f8fc6..aa21be7fa4aa23ab64dd0c7b701967f371c2fe74` (one commit, one author;
`git rev-parse HEAD` is that head). One file: `project-level/task/deployment_skill_guide.md`, +4 -3, two places.
The remarks (`reports/correction-1-remarks.md`) stand in place of a findings file. The two commits between my
earlier head `4e60278` and `31120e9` hold only the cycle's record; `git diff --quiet 4e60278 31120e9 -- project-level foundations`
exits 0, so the code before the range is the code I passed.

Result: the remarks are carried out, nothing else changed, no new Critical or Important finding.

## Each remark

1. **First item, first half — the paragraph on the automation in part 5: made.** `deployment_skill_guide.md:226-229` now
   reads "A skill names that automation too, and the human's merge is what starts the automated deployment; what a
   task changes outside the repository stays the human's (WAY-140)." "A skill says what that automation does too" is
   gone; the one clause on the merge is added; the rest of the paragraph and the WAY-140 sentence are as before.
2. **First item, second half — "60 days": made.** `:343` reads "(2) GitHub disables a scheduled workflow after 60 days
   with no activity in the repository, …"; the `[loop2: …]` marker is off it and the rest of the line is unchanged.
3. **First item, the third matter (WAY-09's list and the part-map sentence): correctly not touched**, as the remark
   says it becomes a task through `/park` after the correction. The diff holds no change to `decisions.md` or
   `part_map.md`.
4. **Second item ("let it through") and the acceptance line:** no code asked, none changed.

Nothing else changed: the diff of the range is the two hunks above (`git diff 31120e9..HEAD`, 4 insertions, 3
deletions). The line break of `:228-229` after "On what the agent" is uneven wrapping left by the edit; cosmetic and
no finding.

## New findings

Critical and Important: none.

Against WAY-139's *Verification* (`foundations/decisions.md:3911-3921`, the guide as a condition a skill must meet):
the new clause says what loop2's automation is started by; it sets no condition on a skill. "A skill names that
automation too" is the wording the remarks ask for and speaks of what a skill does, beside the guide's explicit
statement at `:15-17` and `:31-33` that the guide binds nothing; the Minor reading I raised as N1(a) of the fix review
(a requirement on skills) is not made worse by the change and the human's remarks chose this wording, so I do not
raise it again.

Against WAY-140 (`decisions.md:3973-3976`): the effect outside the repository — the deployment of a merged commit —
is now said to be started by the human's merge, so the automation is the human's act carried on by code the human
merged, and the sentence "what a task changes outside the repository stays the human's" stands beside it without the
gap I named in N1(b) of the fix review. Loop2's source supports the clause: `SKILL.md:13` ("A push to `main` starts
`.github/workflows/deploy.yml`…"), `references/setup_and_secrets.md:336-338` ("every merge deploys automatically …
the human who merges keeps it"). The paragraph quotes no new source text, so no fragment changed. WAY-140 is not
touched.

N2 of the fix review (the wrong marker on "60 days") is fixed by remark 1, second half; the line now says, as the
source does, that it is a rule of GitHub's scheduled workflows, and a reader no longer takes it for a loop2 value.

## Privacy search

I searched the changed text of the correction — the diff of the range, the guide at the head and the commit message —
for the game's public address and for a sender mailbox address in the author's domain (the domain, any address with
`@`, the account name in any form, case insensitive): none found. The correction adds no link.

## Checks run

| Check | Command | Exit |
|---|---|---|
| Head and range | `git rev-parse HEAD`; `git log 31120e9..HEAD`; `git diff --stat 31120e9..HEAD` | 0; head as given, one commit, one file |
| Code before the range is the passed code | `git diff --quiet 4e60278 31120e9 -- project-level foundations` | 0 |
| Foundation form | `python -B elements/common/foundation_check.py` | 0 (0 errors) |
| Private paths, the guide | `python -B task-cycle/private_paths_check.py project-level/task/deployment_skill_guide.md` | 0, 0 listed |
| Invariant `tracked-file-private-paths` | `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 (298 files, 0 listed) |
| Tests of the part | `python -B -m unittest discover -s project-level -p "test_*.py"` (background) | TESTS_RESULT |
| Privacy | `grep -ciE` over the diff, the guide and the commit message | 0 matches each |
| Source of the clause | read of `SKILL.md:13` and `references/setup_and_secrets.md:336-338` from the scratchpad copies of `git show e54f23c0…:<path>` | method; supports the clause |
| Reviewed worktree | `git status --short` | empty |

Not run: the full gate (the cycle's own run).

## Declined to judge

- The task to be saved through `/park` about WAY-09's list and the part-map sentence: the remarks put it outside this
  request.
- Whether the guide's "A skill names that automation too" is wise wording against WAY-139: the human chose it; it was
  graded Minor in the fix review and stays so.

## Reaches beyond the dispatch

None beyond the remarks, the correction report, the diff and the two loop2 passages named above.

## Unread material

The review of a correction is bounded by the remarks and the diff, so I made no new selection of the foundation:
no decisions read in this pass beyond the passages of WAY-139 and WAY-140 cited above (both read whole in the first
review; counts there: 12 decisions whole, 67 by title). Of the guide I read the diff and lines 224-232 and 336-345
of the new head. Loop2 files: only the two passages named. The author's correction report and the remarks: read
whole.

## Searches not found or unclear

- none.

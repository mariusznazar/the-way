# Author correction report — task `deployment-skill-guide`, correction 1

**Status:** done

**Commit:** `aa21be7` on `task/deployment-skill-guide`, on top of `31120e9`; not pushed.

File changed: `project-level/task/deployment_skill_guide.md` (+4 / -3). Nothing else.

## The remarks, each as made

1. **The paragraph on the automation in part 5** (the remark's first item, first half): "A skill says
   what that automation does too" now reads "A skill names that automation too, and the human's merge is
   what starts the automated deployment; what a task changes outside the repository stays the human's
   (WAY-140)." The clause on the merge is the one clause the remark asks for; the rest of the paragraph
   and the WAY-140 sentence are as they were. WAY-140 is not touched.
2. **"60 days"** (first item, second half): the marker `[loop2: …]` is off it; the sentence reads
   "(2) GitHub disables a scheduled workflow after 60 days with no activity in the repository, …", as
   before otherwise.
3. **The third matter** (WAY-09's list and the part-map sentence not naming the guide): not touched, as
   the handoff says; it becomes a task after this correction, outside this request.
4. Items 2 to 6 of the remarks: no code, as the handoff says.

## Checks run

| Check | Command | Exit |
|---|---|---|
| Foundation form | `python -B elements/common/foundation_check.py` | 0 (`0 errors`) |
| Tests of the part | `python -B -m unittest discover -s project-level -p "test_*.py"` | 0 (275 tests, OK) |
| Private paths and note links | `python -B task-cycle/private_paths_check.py project-level/task/deployment_skill_guide.md` | 0 (0 listed) |
| Search for the game's real address and the sender's mailbox domain (strings from the loop2 files) | `grep -rniE` over `project-level` and `foundations/decisions.md` | searched, none found |

Not run: the product's full gate (the orchestrator's). No test was written: the change is prose.

## Own-work check

Requirement most likely not met: that the correction changes only what the remarks ask. Check:
`git diff --stat` before the commit showed one file, 4 insertions and 3 deletions, and the diff holds
the two edits above and no other line. A second requirement, that the new clause says nothing the
guide does not already say about WAY-140: the clause says only that the human's merge starts the
automated deployment, and the WAY-140 sentence after it is unchanged.

## Choices

- The clause on the merge sits in the same sentence as "names that automation too", joined by "and",
  and the semicolon before the WAY-140 sentence stays. Rejected: a new sentence; it would make the
  paragraph run to one more sentence than the remark asks. Cost if wrong: none; the wording binds
  nothing.

## Unread material

- The advisor's remarks: read whole (the file holds three numbered remarks and the acceptance line).
- Nothing else was named for this correction beyond the guide's paragraph and sentence, which I read.

## Searches not found or unclear

- none.

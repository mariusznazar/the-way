# Author fix report — task `deployment-skill-guide`

**Status:** done

**Commit:** `4e60278` on `task/deployment-skill-guide` (fix range `a900916..4e60278`), not pushed.

Files changed: `project-level/task/deployment_skill_guide.md` and `foundations/decisions.md` (WAY-139,
the binding sentences only). `resolve_gaps.md` is unchanged by this fix.

## Findings, each as fixed

- **I1 (fixed).** "How to read a part" no longer says that an answer covers an item. It now says the
  questions help to write an answer, set no condition, and that the list in WAY-139 and the check in
  `resolve_gaps.md` alone decide coverage. Part 7 no longer says "A complete answer is one of two":
  it reads "Two examples of an answer", and the sentence on the refusal is attributed to WAY-139 ("WAY-139
  says that a skill that records the refusal covers the item…"). Part 8's "a complete answer is one of
  three" is left, as the review says it restates WAY-270 and WAY-139. Check: reading the two passages of
  the guide side by side (lines 15-17 and 31-33) shows no sentence of the guide that decides coverage.
- **I2 (fixed).** Part 5 quotes the whole sentence: "Every server or Cloudflare change is the human's,
  [loop2: except deployment started by the existing automation]. The agent prepares the commands. …".
  One paragraph follows, naming the automation the product already has as a third actor beside the
  agent's reads and the human's changes, and keeping "what a task changes outside the repository stays
  the human's (WAY-140)". WAY-140 and loop2 are not changed. I took the review's offer of the
  one-sentence addition (the orchestrator note says to fix as it directs); if the human holds that
  the addition is not wanted, it is a single paragraph to drop.
- **M1 (fixed).** Marked as loop2's own: "players stay signed in", "not above about 100 MB", "both
  containers", the limit of one message per kind in six hours and six in all in 24 hours, the
  scheduled check's "Every five minutes, at minutes that are not the top of the hour," and "up to six
  attempts 20 seconds apart". I also marked "60 days" in the limits of the scheduled check, a value of
  the same kind the review's list did not name.
- **M2 (fixed).**
  - Part 4: the item "3. Restore the Origin Rule…" now comes first, then "This is script
    installation, one deployment and four Cloudflare changes…", as in the source; the introducing
    sentence names the troubleshooting reference.
  - Part 5: "Treat service logs as potentially sensitive…" is a separate fragment, introduced as from
    the section on seeing deployments.
  - Part 7: "The file holds the game's lines…" is a separate fragment, introduced as from the paragraph
    on how an agent reads the record; the loop2 decision number it carried, `(D-252)`, is now shown in
    the fragment and marked as loop2's own (the first version cut it without a `…`).
  - Part 3: "A list of rotations ends the file" is replaced by "The same reference keeps a list of
    rotations…", and the rotation fragment is introduced as from the setup reference.
  - Part 6: the table of exit codes is a separate fragment, introduced as from the section on log
    stages and exit codes; "from its deploy script" is replaced by "a list of the exit codes it
    gives".
  - Two small cuts I found while re-reading against the source, outside the review's list: part 2's
    "The human does everything here." had dropped a decision number of loop2 without a mark; it now
    reads "here (…)." And part 3's rotation step 1 now ends "(…)" where the source has a parenthesis.
- **M3 (fixed).** The binding sentences of WAY-139 now close the list at "…a failure." and a new
  sentence opens the guide ("Beside the list it holds a guide to writing such a skill, with the
  deployment skill of loop2 as its first example, which binds nothing and which the check of the list
  points to."). The first sentence now reads "holds no skill of a product, but the list of…" and the
  paragraph is re-wrapped. The entry stays at three sentences: the list; the guide; the check, whose
  clause "for the items on how to read the logs…" now follows a semicolon instead of starting a
  fourth sentence.
- **M4 (fixed).** Part 2 says the list does not define "a preview of deployments" and that the guide
  reads it as both of two things.

## Checks run

| Check | Command | Exit |
|---|---|---|
| Foundation form | `python -B elements/common/foundation_check.py` | 0 (`0 errors`) |
| Tests of the part | `python -B -m unittest discover -s project-level -p "test_*.py"` | 0 (275 tests, OK) |
| Private paths and note links, the guide and `resolve_gaps.md` | `python -B task-cycle/private_paths_check.py <file>` | 0 for each (0 listed) |
| Private paths, every tracked file | `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 (298 files, 0 listed) |
| Search for the real game address and the sender's mailbox domain | `grep -rniE` over `project-level` and `foundations/decisions.md` | searched, none found |

The unit tests of `project-level` ran on the content of this commit except for one `(…)` added to the
guide just before the commit, which no test reads.

## Own-work check

Requirement most likely not met by the fix: that every quotation of the guide still stands in the source
at `e54f23c0…` in its order, with no number or command changed, and that no real address or mailbox
domain entered.
- Re-ran my scratch comparison of the fragments against the files of the commit: 11 differences, the
  same kinds as before and each explained there (the guide's own sample wordings of the refusal and
  the "no notice" answer; the table, which keeps three rows; the docker command that the script cuts at
  the next paragraph; the adaptation of the copy of a secret named in the guide). One difference of my
  own was the end of rotation step 1 (fixed above, `(…)` added).
- The privacy search above found none.

## Reach beyond the handoff

None beyond the files the findings name; I read the source files of loop2 at the commit again only
for the passages the findings point to (`SKILL.md` 100-117, 268-290; the troubleshooting reference
lines 157-171 through my saved copy).

## Unread material

- `review-whole-report.md`: not read; the findings file carried the evidence each fix needed.
- Loop2 files: as in the first report; nothing new read beyond the passages named above.

## Searches not found or unclear

- none.

## Choices

- I2: kept the one-paragraph addition on the third actor. Rejected: only the whole quotation with the
  mark. Cost if wrong: one paragraph that the human may not want, easily removed.
- M3: kept three sentences by joining the check's second part with a semicolon, rather than add a
  fourth sentence (the template allows one to three).

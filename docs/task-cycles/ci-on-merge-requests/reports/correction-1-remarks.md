# Remarks of the human, correction 1

Source: the comment https://github.com/mariusznazar/the-way/pull/127#issuecomment-6892747048 on the request, written by the human (through the day advisor) on 2026-11-15 and read by the orchestrator with `gh api repos/mariusznazar/the-way/issues/comments/6892747048`. Word for word:

---

Mariusz's decisions on this request (written down by the day advisor)

1. Done by Mariusz on 2026-11-15 at 11:02: the branch rule is set. A repository ruleset `foundations_tests` (id 27308872), enforcement active, targets `refs/heads/foundations`, requires the status check `tests` (source GitHub Actions, integration id 15368), does not require the branch to be up to date before merging, bypass: Repository admin role, mode always; it also restricts deletion and blocks force pushes. Read it yourself with `gh api repos/mariusznazar/the-way/rulesets/27308872` before you write it down.

2. Close it in this request. Read the branch rule now that it exists and write that reading into the decision whose *Based on* holds the open `TODO` for it (WAY-16, rows 1 and 2), the same way the three GitHub facts of this request are written (address, date read, the passage), so that no marked gap is left on the main branch.

3. Let both through (the two tests that fail as root, and a pull request that edits the CI file). No task.

---

Also given with the request to run this correction, as the input of the cycle's skill (the same instruction the human gave for the first run): before each full run of the tests (step 10), write that it is about to start and wait for the signal "start" from the day advisor.

## What each remark binds

1. A done human action (item 1 of the request's description, kind 3). No code. It removes the reason for the `blocked` state of the request.
2. The answer "do it in this request" to item 2 of the description (kind 16, the open `TODO` in the *Based on* of WAY-16). The correction binds: read the rule, write the reading as an environment fact as WAY-84 and the template of the element give it, name the fact in WAY-16's *Based on* in place of the `TODO`.
3. The answer "let it through" to item 3 of the description (kind 8, findings outside the task's scope 1 and 2), no task. No correction; the findings stay in the lower part of the description.

Recorded sources and kinds: `item 16 · not-required` (the foundation allowed the `TODO` while the rule did not exist, and the task document asked for no reading).

Reading of the rule by the orchestrator, 2026-11-15, `gh api repos/mariusznazar/the-way/rulesets/27308872` (the output is in the author's handoff and is quoted word for word by the author's run, not by this note).

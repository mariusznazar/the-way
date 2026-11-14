# Return step report for correction 1

**Status:** done — nothing to change, **no commit**.

Range compared: `8c601d1..e802ec4` (`foundations/decisions.md`, 3 added, 1 removed line: the end of WAY-375's second paragraph). Head stays `e802ec4668f7cb29d4f3f019265289afac5a3209`.

## Comparisons

The sentence now reads that the removal of a checkout git names, also one beside the repository's own directory, is a change to the repository's state and no effect outside the repository in the sense of WAY-140, so the script a cycle runs needs no act of a human, while the first clearing of the directories that gathered before the script, which a task document places as a human action, is the human's act.

| Compared with | Result |
|---|---|
| Glossary, `human action` ("an act outside the product's repository that a task needs and a human performs") | Holds. The script run by the cycle is named as needing no act of a human; the first clearing, which the task needs and a human performs on directories beside the repository, is named a human action. No sentence of the entry reads the glossary word in another meaning now. |
| WAY-140 | Holds, no change. It reserves to a human an effect on a server, DNS, keys or an external account, and says a human action that uses the cycle's code is placed in the cycle; the first clearing is such an action (it runs the script the cycle writes), and the script's own removal is a state of the repository, as row 5 settles. |
| The task's *Human actions* (the one-time clearing in the-way and `loop2`, "in the cycle") | Holds: the sentence calls exactly that clearing the human's act and places it by a task document. |
| WAY-375's *Verification* and *Rationale* | Still agree: the pair says the cycle goes on without a word to the human where the script removed a directory beside the repository's own, and that asking the human first violates the entry; the *Rationale* says the removal stands in the repository's state, not in what WAY-140 keeps for a human. |
| WAY-373, WAY-298 as changed, WAY-376 | They do not speak of the sentence: WAY-373 (remainders of agents' copies), WAY-298 (the two changes outside the task's worktree) and WAY-376 (ignored files) need no change. |
| Skill, templates, script | The correction touched none of them, and none uses the phrase. |

The two Minor findings of the correction's review are for the request's list and I did not touch them.

## Check (command, exit code)

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` (without `--skip-test-citations`) | 0 | `0 errors` |

No full gate; no focused tests (no code or test file in the range).

## Unread material

- none: `task-cycle/skill/return_step.md` known from the earlier return steps and not read again; `reports/correction-1-review-report.md` not opened (the handoff gives its result).

## Searches not found or unclear

- none

## Working copies

None made. Remainder: none.

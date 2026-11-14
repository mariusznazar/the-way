# Correction 1 report — worktrees removed after merge

**Status:** done

**Commit:** `e802ec4` (Say in WAY-375 that the script needs no act of a human and the first clearing is one), on head `8c601d1`. One file: `foundations/decisions.md`. No merge of the target branch was needed (`origin/foundations` has not moved). Not pushed.

## Answer to each remark

- **Item 3 (correct in this request) — changed.** The last sentence of the second paragraph of WAY-375 read "…so it needs no human action", which the glossary's entry reads as contradicting the task's own *Human actions* line. It now reads: "…is a change to the repository's state and no effect outside the repository in the sense of WAY-140, so the script that a cycle runs needs no act of a human; the first clearing of the directories that gathered before the script, which a task document places as a human action, is the human's act." The meaning is the one the handoff asks to keep: removal of a checkout git names, also one beside the repository's own directory, is a change to the repository's state and not an effect in the sense of WAY-140 (row 5); the one-time clearing is the human's act. The glossary, WAY-140 and every other entry are untouched.
  - Search for the phrase in the range `835344f..HEAD` (`git diff 835344f..HEAD` for "human action", "human's act", "no human", "without a word"): the only hit in the added or changed text was that sentence. WAY-376, the changed lines of WAY-298, `task-cycle/skill/SKILL.md`, `record_template.md`, `request_template.md` and the script's docstring and messages do not use it. The other occurrences of "human action" in those files were there before the change and belong to the task cycle's own use, which matches the glossary.
  - *Verification* and *Rationale* of WAY-375 agree with the new sentence: the pair says the cycle goes on "without a word to the human" where the script removed a directory beside the repository's own, and that asking the human before such a removal violates the entry; the *Rationale* says asking the human for each directory would leave the directories where they are, and that the removal is no effect in the sense of WAY-140. Neither mentions the clearing, so neither needed an edit.
- **Item 2 (let through, no task) — nothing to correct.** The unstable test of the number of directories at once belongs to the open collective task named in the remark; this change has no part in it.
- **Item 1 (stays for the human) — nothing to correct.** The one-time clearing in the-way and `loop2` is the human's.

Foundation entry changed, for the request's *Foundation entries*: WAY-375 — `row 2` (carrying rows 4 and 5) — unchanged in meaning: at its start a cycle removes an earlier task's working directory only under the conditions of the entry, touching only checkouts git names and never a branch; this correction only words the line on human action as the remark says.

## Checks (command, exit code)

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` (without `--skip-test-citations`) | 0 | `0 errors` |

The tests that cite WAY-375 by `decision:` lines quote sentences of its first paragraph and "The script touches only the checkouts that" of the second; the changed sentence is none of them, and the check above confirms the quotations still stand. No file of code or tests was touched, so I did not rerun `task-cycle` tests; no full gate.

## Own-work check (WAY-164)

- **Requirement most likely unmet:** the remark's: the new sentence must contradict neither the glossary's "human action" nor the task's listing of the one-time clearing as a human's act, and must keep row 5.
- **Check:** read the glossary entry ("an act outside the product's repository that a task needs and a human performs") against the sentence: the script run by the cycle is named as needing no act of a human; the first clearing, an act on directories outside the repository that the task needs, is named a human action placed by a task document. Row 5's meaning (state of the repository, not a server, DNS, key or account of WAY-140) is kept in the same sentence. `foundation_check.py` run as above.
- **Showed:** consistent; exit 0.

## Unread material

- none: the handoff and the remarks file read whole; `foundations/glossary.md` entry read for the check.

## Searches not found or unclear

- none

## Working copies

None made. `.runs/` holds `task-cycles/` and a file `pp1.txt` that is not mine and that I left. Remainder: none.

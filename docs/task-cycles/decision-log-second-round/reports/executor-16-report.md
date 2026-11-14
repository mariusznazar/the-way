# Report of the executor of slice 16 (Guidelines: testing)

**Status:** done

**Commits:** `7ff41ca` Remove the withdrawn decision numbers from the testing guidelines skill files and give each rule its reason

**Files changed** (37 added, 27 removed lines), all under `product-guidelines/testing/`: `SKILL.md` (+4 -2), `audit.md` (+7 -4), `new_tools.md` (+1 -1), `recognize.md` (+2 -2), `research.md` (+1 -1), `settle.md` (+1 -1), `starting_set.md` (+5 -3), `task_document.md` (+3 -1), `template.md` (+13 -12).

## Checks

- `python -B elements/common/foundation_check.py` — exit 1 (expected until the last slice); it lists 0 lines for any file under `product-guidelines/testing/` (the output was grepped for that path; none).
- `python -B agent-instructions/skill_entry_points.py` — exit 0, "entry points are current".
- Search of `product-guidelines/testing/*.md` for WAY-170, 171, 226, 245, 246, 248, 249, 250, 266, 281 — no match.
- The full gate was not run (not mine). No `gate/run_tests.py <directory>` was run: the slice's *Checks* do not list one.

## Own-work check

Requirement most likely missed: "the sentence around each removed number reads as before, with its full stop". Check: read the whole diff (`git show HEAD -U0`) for each removed bracket. It showed one slip, in `template.md` (`## Where in code`): after removing `(WAY-171)` the sentence before it lost its full stop. I fixed it before the commit; the committed diff holds `copied from them.`. Every other removal keeps the stop or the closing mark of the sentence.

## Reasons added (file, sentence, entry read at the base ec7929d)

- `SKILL.md` (bullet "Extend what exists"), from the *Rationale* of WAY-248: "A tool the product already runs, even a worse one, beats a better one brought in, since its tests and the people working on them already follow it and two tools over one suite split its conventions."
- `audit.md` (before "Where the product has tests:"), from the *Rationale* of WAY-250: "The human who approves the exemplar tests does not judge tests below end-to-end ones, so the audit shows each proposal with what the product gains by it and each fault with its place and its effect." It stands as a line of its own above "Where the product has tests:", since that line ends in a colon that leads the list and a sentence between would cut it from its list.
- `starting_set.md` (end of the second bullet), from the *Rationale* of WAY-249: "New scope needs a check of whether the existing tools fit it, while accepted recipes updated or corrected within their scope need no new comparison."
- `task_document.md` (the *To do* bullet of the pointer), from the *Rationale* of WAY-245: "Without the pointer a session outside the task cycle can miss the testing guidelines, and a path with its condition costs one line;" (the sentence closes with the list's semicolon; the entry's own wording is "a path with its condition costs one line").
- `template.md` (bullet `## When to read`), from the *Rationale* of WAY-246: "The condition serves the pointer of the instruction file and an agent outside the cycle, while the cycle selects the file by the parts of *Applies to* alone, since a condition judged before a diff exists could drop the file from an agent that then writes a test." It does not repeat the entry's reference to WAY-245.

## Entries left under the "stay" rule

None of WAY-93, 94, 97, 263, 287, 294, 295, 297, 363, 364 stands in a file of this slice, so none was met. Every number the slice named (170, 171, 226, 245, 246, 248, 249, 250, 266, 281) has left the log (grep of `^### WAY-NN ` in `foundations/decisions.md` returned 0 for each). No group-D number was in my files.

## Choices

- `audit.md`: reason as a separate line before "Where the product has tests:" rather than folded into the sentence with the colon. Rejected: folding it into that sentence, which changes the sentence around the removed number. Cost if wrong: the reader meets the reason before the condition; a fold is a one-line change.
- `task_document.md`: the reason follows a full stop inside a list item that then ends with a semicolon. Rejected: a "since" clause appended to the instruction, which would read as the reason of "naming no command" too. Cost if wrong: a reword.
- Reasons are not added for rules where the plan lists only a removal (`recognize.md`, `new_tools.md`, `research.md`, `settle.md`, `template.md` apart from `## When to read`).

## Reaches beyond the dispatch

- `git show ec7929d:foundations/decisions.md` saved to `.runs/executor-16/base.md` to read WAY-245, 246, 248, 249, 250 (named by the handoff as read at the base). Read whole: WAY-245, 246, 248, 249, 250. WAY-293 read at `foundations/decisions.md:7171-7215` as it stands.
- I read `settle.md` lines 1-20 only (the line 12 edit); the file was not read whole before the one-token edit there. The edit touched only line 12.

## Unread material

- `foundations/decisions.md` WAY-293 read to the end of what I opened (lines 7171-7215), not past the *Rationale*'s last lines; the part I used is the second paragraph on the form of a rule's reason.
- `settle.md` read to line 20 of 56 (see above).
- `SKILL.md` of the testing skill read from line 55 to 100 (edits at lines 68 and 91), not whole.
- The task passage `task.md:33-40` was read (lines 25-49).
- The ten entries named for removal in other rows and the plan were not opened; the slice did not need them.

## Searches not found or unclear

- None unresolved. The plan's line numbers are those of the base; found each number by search, as the handoff said.

## Working copies

`.runs/executor-16/` held `base.md` (the base log copy) and `fc.txt` (output of the foundation check). Both removed before returning, the directory itself left empty.

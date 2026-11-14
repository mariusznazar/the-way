# Report of the executor of slice 6

**Status:** done

**Commits:** `55ad29a` Remove the withdrawn decision numbers from the invariants and part map templates and give each rule its reason

**Files changed:** `elements/invariants/template.md` (+20 -18 approx.; diff total of both files 46 insertions, 32 deletions) · `elements/part-map/template.md`.

## Checks

- `python -B elements/common/foundation_check.py` — exit 1 (expected until the last slice). It printed 447 lines before the slice and 417 after; lines for `elements/invariants/template.md` and `elements/part-map/template.md`: 30 before, 0 after (`grep -cE` on the saved output).
- `python -B gate/run_tests.py elements/common` — exit 1: 201 tests, 1 failure, `test_the_way_foundation_passes` (`test_foundation_check.py:1529`). It runs the foundation check on the whole repository and fails on lines of files of slices not yet made (first lines: `agent-instructions/README.md:79` `WAY-286`, `:83` `WAY-290`, `:84` `WAY-291`); none of its lines names a file of this slice (0 lines for the two templates). The same cause as the exit code 1 of the check above; no other test failed.
- `python -B gate/run_tests.py elements/part-map` — exit 0: 39 tests, OK.

## Own-work check

Requirement most likely missed: a removed number left behind (a number in a place the line numbers of the plan did not name), or a sentence whose full stop was lost. Check: the foundation check lists no line for the two files (0, above), and `git diff` read for every `WAY-` removed and added: no `(WAY-NN)` removed leaves a dangling space or an empty bracket; one place (`(WAY-49).` on its own line in "## Surfaces") I first left as a lone `.` and fixed before the commit. Numbers added by me: `WAY-08` and `WAY-12` (invariants, both stay in the log, checked with grep), `WAY-61` (stays). No withdrawn number was added.

## Reasons added (file, sentence, entry read at the base `ec7929d`)

Invariants template:
- WAY-56, at the end of the first bullet of "## The sentence" (see choice 1): "One invariant per entry lets the failure of its test, seen once, show that the test catches that rule (WAY-08)." From the *Rationale* of WAY-56.
- WAY-56 pair, same bullet: "What one sentence may join is judged against a pair: "every entry of the log has every field of the template" complies as one entry, and "binding sentences number one to three and contain no *should*" violates as one entry, since it joins two rules (WAY-12)." The pair is that of WAY-56's *Verification*; "since it joins two rules" is mine and reads off the quoted sentence (a count and a ban).
- WAY-65, in "## Method and test" after the citation bullet: "The citation stands at the test because that is where the outcome is given (WAY-61)." From the *Rationale* of WAY-65.
- WAY-68, same section: "A test that flips on one commit is a fault of the test, and a green run again would hide the fault instead of answering it." From the *Rationale* of WAY-68.
- WAY-58, "## Links", bullet "recovered from code": "Without that mark such an entry would read like a chosen rule and hide that its reason was never settled, and the place in the code leads whoever weighs a change to the behaviour." From the *Rationale* of WAY-58.

Part map template:
- WAY-40, end of the bullet on the two kinds of entry in "## Where entries go": "Each kind answers what the other cannot: a part, what it is responsible for and which files are its; a surface, what someone outside relies on." From the *Rationale* of WAY-40.
- WAY-299, new paragraph after the list in "## Allowed dependencies": "This is a duty rather than advice, since a step nothing enforces is the step an agent leaves out, and an import from outside the map then passes merge after merge unseen." From the *Rationale* of WAY-299.
- WAY-49, second bullet of "## Surfaces": "…names the surface in its request, since a broken promise falls on someone who took no part in the change, and the request names it for the agent reviewing the change and the human merging it." From the *Rationale* of WAY-49.
- WAY-45, end of "## Critical flows": "The product's tests run whole on every change, so a flow's test needs no list of parts to be chosen by, and the invariant's *Part* already names where a change can break the flow." From the *Rationale* of WAY-45.
- WAY-42, "## The binding part": "Whatever names an entry relies on what the entry answers for, and the other fields change more often without changing that, so making them binding would send the author to the entries naming it for changes that do not alter the promise." From the *Rationale* of WAY-42.

Numbers removed with their brackets: WAY-64 (3 places), WAY-65 (2), WAY-68 (1), WAY-56 (4 places, with the sentence "in WAY-56's *Verification*" rewritten), WAY-58 (4), WAY-40 (5), WAY-41 (3), WAY-45 (2), WAY-299 (3), WAY-49 (2), WAY-42 (1).

## Choices

1. The plan places the reason of WAY-56 at line 78 (the second bullet, "the sentence is the binding part"). The reason says why one invariant stands in one entry, which is the rule of the first bullet; I put it there, "where the rule stands". Rejected: the plan's place. Cost if wrong: the sentence stands one bullet earlier than the plan's.
2. For WAY-65 the plan allows the line 60 rule or the line 70 rule; I wrote one reason, for the rule of the citation at the test. The either-commit rule (line 70) has none. Cost if wrong: one more sentence from the *Rationale* ("counting either commit keeps a dropped citation or a deleted test among the invariant tests a request names").
3. For WAY-58 the reason stands on the recovered-from-code bullet (line 132 of the plan), not on the closing bullet.
4. For WAY-40 the reason stands on the two-kinds bullet (line 18 of the plan); the *Rationale* sentence on a dependency having no identity beyond its pair of parts (for the line 22 bullet) is not added.
5. For WAY-299 the reason is a separate paragraph after the list, since the paragraph naming the invariant ends with a colon that opens the list.

## Entries left under the "stay" rule

None of WAY-93, 94, 97, 263, 287, 294, 295, 297, 363, 364 stands in the two files; nothing left under that rule. Group-D numbers: none in the two files.

## Findings

- A rule whose reason the *Rationale* does not give, or that is not in the file: none met. The WAY-56 pair needed no addition of rule beyond the plan's wording.

## Reach beyond the dispatch

- `git show ec7929d:foundations/decisions.md` read for WAY-41 and WAY-64 (not in my *Read* list, but their numbers stood in the files; I removed the numbers and added no reason for them, as the plan gives none).
- `grep` of `foundations/decisions.md` for `### WAY-08`, `WAY-12`, `WAY-61` to see they stay.

## Unread material

- `foundations/decisions.md:9771-9810` WAY-293: read the entry as it stands (whole, up to the *Rejected* paragraph; the tail of *Rejected* cut off by the head limit of my command was not read).
- `task.md:33-40`: read (lines 25-49).
- All base entries of the *Read* list (WAY-40, 42, 45, 49, 56, 58, 65, 68, 299): read whole.

## Searches not found or unclear

- none. (The plan's line numbers matched the files, which the foundation entries did not touch.)

## Working copies

`.runs/executor-6/` (base copy of the log `base.md`, outputs of the checks). It is under the ignored `.runs/` and holds no worktree; the files stand there, not removed, as outputs of checks (`base.md`, `check0.txt`, `check1.txt`, `common.txt`, `pm.txt`).

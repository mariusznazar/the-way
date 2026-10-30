PASS c7a4008b48b09d17c76f120608c43e16cf544c33

# Review of the fix: settle-technology in the shape of WAY-256

Fix range `c2e70f9..c7a4008` (one commit, `project-level/technology/SKILL.md` and `start.md`, +4 -3), with the regenerated `reports/word-counts.md` and `reports/assessment.md`. `git rev-parse HEAD` gives the head named. The findings file `reports/findings.md` bounds this review. The Minor and out-of-scope findings of `reports/review.md` stand as they are and are not re-opened.

Counts: 0 blocking, 2 Minor, 0 out of scope. Both Minor notes are new, and neither concerns a tracked file.

## The findings

### 1. A resuming leader whose human changes the list never reaches the rules of the list: **fixed**

The defect no longer exists on `c7a4008`. Walked on the route "leader, resuming, open choices":

- `start.md:20-21`: "Then show the list and ask whether it still holds; where the human adds or changes an item, follow the step "List the choices" (`list.md` beside this file) for it." The pointer now stands at the moment the human answers, in words the leader meets there, and "for it" keeps the work to that item, so the whole list is not listed again.
- `SKILL.md:33-35` gives the same condition under "Where the Technology section holds a list", so it also holds on a resume with no open item, where a human may change the list unasked.
- Cases tried: an added item becomes open and is in "the open items" that `start.md:21-22` resumes with; a change that leaves no open item is carried by `list.md:30` to the step "Close", so "Then resume" sends nobody into an empty step.

`reports/assessment.md` rows `[41-45]` and `[63-66]` now read true of this text, and the conditional line of `reports/word-counts.md:57` and its note at `:72` cover the case.

### 2. The count of the route "leader, resuming, open choices" leaves out `close.md`: **fixed**

`checks/word_counts.py` and `checks/reach.py:20` hold `close.md` on the route, and `reports/word-counts.md:18` and `:66` show it. My recount from `git show` at `c7a4008`: 475 + 314 + 178 + 886 + 96 = 1949, plus 3675 and 831 = 6455, against 6628 = -173. All five rows and the file table of `reports/word-counts.md` recount exactly: 5111, 6828, 6455, 4738, 1621.

`reports/fix.md:31` contests my 6427 as resting on a stale base. I keep it: see note 3. The finding's defect is closed either way.

## What the fix diff itself brought

No new Critical or Important finding.

- Acceptance criterion 1: the only change of meaning is the instruction the finding asked for. The rest of the bullet is word for word, the old sentence split in two. Preservation check: 51 exact, 20 listed, 0 problems.
- Acceptance criterion 2: the new condition is one an agent recognises.
- WAY-256: `SKILL.md` gains a clause of a pointer, and no fragment moves.
- `research.md` and `settle.md` are untouched, so the research agent's reach and To do 2 and 3 do not move.
- The description is unchanged and the entry points are current.
- `assessment.md`: the 37 quotations of `525cde1` still match, and no figure of the earlier counts survives there (`6800`, `+172`, `1676` and `297` are gone; proposal 5.1 reads 6828).

## Minor notes

### 3. `reports/fix.md:31` explains the figures wrongly

**Anchor:** `.runs/task-cycles/technology-skill-shape/reports/fix.md:29`, `:31`

**To paste:** The fix report calls 6427 a figure on a stale base and gives the research row at `c2e70f9` as 1600. 6427 was right at `c2e70f9`: `research.md` already held 467 words there and is on no leader route, and 6455 is 6427 plus the 28 words the fix added to `SKILL.md` and `start.md`.

**Why I report it:** `git show c2e70f9:project-level/technology/research.md | wc -w` gives 467, which my first review's recount also found. The orchestrator's check found the same. `fix.md` does not go into the request, so no figure there is at risk; the note is here so that the explanation is not copied.

### 4. Two "needed when" answers of the assessment no longer cover what the row says

**Anchor:** `.runs/task-cycles/technology-skill-shape/reports/assessment.md:44`, and the row `[74-78]` in the same way

**To paste:** Row `[63-66]` says a resumed leader needs this rule when the look or the human changes the list, yet its columns "Needed when" and "Will the agent recognise that moment?" still give only the new list with `TODO`.

**Why I report it:** WAY-257 has every row show both answers so that a human can dispute them. The row's verdict column gives the resume, so nothing is hidden and no agent acts on this table; the two columns just lag behind it. The same holds for the other rows of `list.md` a resumed leader now reads. One clause in the template of the row would close it.

## Declined to judge

- The Minor and out-of-scope findings of `reports/review.md`, the handoff keeps them as they are.
- The lines of `start.md:12` and `:22`, over the usual width: no effect on a reader.
- How agents follow the new pointer: no run exists (task question 4).

## Checks

| Check | Exit | Result |
|---|---:|---|
| `git rev-parse HEAD c7a4008` | 0 | both the given head |
| `git diff c2e70f9..c7a4008` read whole, with `git diff --name-only` | 0 | two Markdown files |
| `git ls-files --eol project-level/technology/SKILL.md project-level/technology/start.md` | 0 | `i/lf w/lf` |
| `python -B <scratchpad>/check_counts.py`, my own recount from `git show` at `c7a4008` | 0 | every figure of `reports/word-counts.md` right |
| `python -B <scratchpad>/check_assessment.py`, my own check of `reports/assessment.md` | 0 | 37 rows, 0 bad, 0 uncovered lines |
| `python -B .runs/task-cycles/technology-skill-shape/checks/reach.py <scratch file>` | 0 | 82 assertions, 0 failed |
| Read `checks/reach_negative_f1.txt` and `reach_negative_f2.txt` (not rerun) | n/a | 2 and 1 FAIL lines on the named assertions |
| `python -B .runs/task-cycles/technology-skill-shape/checks/preservation.py <scratch file>` | 0 | exact=51, listed=20, problems=0 |
| `python -B .runs/task-cycles/technology-skill-shape/checks/word_counts.py <scratch file>` | 0 | reproduces the five rows |
| `python -B instruction-files/check_instructions.py .` | 0 | 0 error, 1 warn (`dead-path AGENTS.md:21`, unchanged), 3 info |
| `python -B agent-instructions/skill_entry_points.py` | 0 | `entry points are current` |
| `python -B gate/run_tests.py project-level` | 0 | 267 tests OK |
| `python -B gate/run_tests.py agent-instructions` | 0 | 18 tests OK |
| `git show c2e70f9:project-level/technology/research.md`, counted | 0 | 467 words |
| `git status --short` after the tests | 0 | 0 lines |
| Manual: walk of the resuming route through the pointers | n/a | finding 1 closed |

Not run: the full gate (the orchestrator's, as the handoff says); the author's negative controls, which change files. Their outputs were read instead. `foundation_check.py`: no foundation file changed.

## Reaches beyond the dispatch

None beyond the first review's reading; `task-cycle/review/fix.md` is the method.

**Searches not found or unclear:** none

PASS 80126daf0834fc1d5fa589ebaea6e2cdff9db6f5

# Review of the fix of B1 of the correction review (range 047a9e7..80126da)

Range `047a9e7606e90dc164762bebb0c6bc48dcd46eeb..80126daf0834fc1d5fa589ebaea6e2cdff9db6f5`, one commit,
one file (`foundations/decisions.md`), confirmed by `git rev-parse HEAD`. Reviewed as a fix. Paths are
relative to `the task's worktree root`.

Counts: 0 blocking, 1 Minor (new, within the task), 0 out of scope.

## B1 — fixed

B1 said four skill files and `task_line.md` gave a refiner the write of the lines of the tasks tied to
its task, which WAY-154 did not say (WAY-263). On the new head the entry says it:

- **Binding part** (`foundations/decisions.md:4445-4450`): "... the line of its task in the backlog the
  product names (WAY-107), where none stands, with the dependencies the plan gives the task, and, as the
  rules of the task place give, brings the lines of the tasks tied to its task into agreement with the
  plan's dependencies, at the same time as the other refiners of the round and with no queue between
  their writes". It points to the task place's rules and holds none of them.
- **Verification** (`:4470-4483`): a *complies* example (a refiner that finds the line of a task waiting
  on its own task without the dependency on it brings it into agreement as the rules give, and one that
  finds no line for a tied task makes none) and a *violates* item (a refiner makes the line of a tied
  task that has none).
- **Rationale** (`:4495-4498`): the accepted risk now covers two refiners that bring the same tied line
  into agreement and leave one write of it, shown afterwards as a line missing a field.

The files say no more than the entry: `project-level/task/skill/orchestrated_mode.md:41-43`,
`project-level/lead/conversation_template.md:22-24`, `project-level/lead/skill/SKILL.md:105-106` and
`project-level/plan/skill/delegated_mode.md:9-10` give the refiner the same write ("brings the lines of
the tasks tied to it into agreement, as `project-level/task_line.md` gives"), and `project-level/task_line.md:42-47`
carries the one sentence (the task's line and the lines of the tasks it waits on and that wait on it, as
the rules of the task place give; where they do not say how, ask the human once). `grep` for "tied to its",
"tied to it", "tied to them" and "tied task" over `foundations/decisions.md`, `project-level` and
`product-guidelines` (exit 0) finds the entry's three lines and the four skill lines, and nothing more.
`delegated_mode.md`'s citation of WAY-154 now has a sentence to rest on.

## The points the handoff names

- **One to three binding sentences:** WAY-154's first paragraph is three sentences ("Project refinement
  resumes ... or `obstacle`.", "Only a refiner ... where none stands.", "Agent turns ... is done."). The
  second is long and joined by semicolons, as before the fix; within the form (WAY-05).
- **Nothing of how a line is handled entered WAY-154 or a skill:** the added text names no way of finding
  a line, no one-line-to-a-task rule, no field that may change, no read-before-write, no clash rule; it
  says who writes and defers the how to the task place's rules. The sentence "one that finds no line for a
  tied task makes none" is a rule of whose write it is (like "a refiner never moves a line to ready"),
  which the-way alone holds, not of how a line is handled; the human's rule gave the reason (the tied
  task's own refiner makes that line complete).
- **`the cycle's` mark and WAY-114:** the author marks the added write `the cycle's`, with the human's
  remark at the request on item 1 as its source, named in the report and not in the entry (the template
  forbids history in the entry). Under WAY-114 an entry no row carries is accepted at the merge, with the
  request's section for the human's decisions carrying a plain sentence of its meaning; the author gives
  the English and Polish sentences. I cannot see the request's description from this worktree, so that it
  carries the sentence is a claim I did not verify. The entry and the mark agree.
- **No added line over 100 characters:** I scanned every added line of `git diff 047a9e7 80126da -U0`
  (`python -I`, exit 0): none.
- **A changed word or a lost qualification in the rest of WAY-154:** compared word by word against
  `047a9e7` (`difflib` on the whole entry, whitespace ignored, exit 0). Five differences, all
  insertions: the binding clause above; the *complies* clause; the *violates* item; the rationale's
  "or two refiners that bring the same tied line into agreement can leave one write of it"; and "line."
  became "line or a line missing a field." Nothing is replaced or removed. No other entry differs
  (`changed ['WAY-154']`, the same set of entries).

## New finding (Minor, within the task, blocking nothing)

1. **"Tied" is undefined in the entry and the example covers one direction.** `foundations/decisions.md:4449`
   ("the tasks tied to its task") and `:4472-4474`. Only `project-level/task_line.md:42-47` says what
   tied means (the tasks the refiner's task waits on and those that wait on it); the *complies* example
   shows only the line of a task that waits on the refiner's task. A reader of the entry alone takes
   "tied" from the plan's *Depends on* column, which is the right reading, so no wrong write follows.
   Fix at the next touch: "tied to its task by a dependency, in either direction". The glossary holds no
   entry for it; Minor (WAY-297).

## Declined to judge

- The three Minor findings of the correction review: not part of this fix.
- The rules of the task place: private notes, not reviewed, nothing quoted.
- Whether the request's description carries the plain sentence for the human's decisions (WAY-114):
  outside the range and the worktree.

## Checks run

All read-only, from the reviewed worktree, `python -B`; `git status --short` empty.

| Check | Command | Exit |
|---|---|---|
| Foundation identifiers and references | `python -B elements/common/foundation_check.py` | 0 ("0 errors") |
| Instruction files | `python -B instruction-files/check_instructions.py .` | 0 ("0 error, 0 warn, 3 info") |
| Private paths and note links | `python -B task-cycle/test_tracked_files_private_paths.py` | 0 (OK) |
| Word-by-word comparison of the whole entry and of all entries, `047a9e7` against `80126da` | one-off `python -I` with `difflib` | 0 (five insertions, one entry changed) |
| Added lines over 100 characters | one-off `python -I` over `git diff 047a9e7 80126da -U0` | 0 (none) |
| The tied-line write in entries and skills | `grep -rn "tied to its\|tied to it\|tied to them\|tied task" foundations/decisions.md project-level product-guidelines` | 0 (three entry lines, four skill lines) |
| Diff, log, head | `git diff --stat 047a9e7..80126da`, `git log 047a9e7..HEAD`, `git rev-parse HEAD` | 0; one file, one commit, head confirmed |

Not run: the `project-level` directory and the full suite.

## Reaches beyond the dispatch

- `project-level/task_line.md:42-47`, and the four skill passages above, read to compare them with the
  entry. The fix report's list of files agrees.

## Unread material

Decisions: WAY-154 read whole on the new head (the only entry the fix changes). WAY-107, WAY-114 and
WAY-263 not re-read; used as read in the earlier reviews. The fix report and the findings file read whole;
`reports/correction-review-report.md` not re-read (the findings file carries its B1).

## Searches not found or unclear

- A definition of "tied" in the entry, the glossary or the plan template: not found (Minor 1).
- The request's description, for the plain sentence WAY-114 asks for: not in the worktree; unverified.

PASS 5922ffce36e42ef1e6f98f9f04cc49b32e8aff14

# Review of the fix — Minor findings of the whole-change review of WAY-330

Range `4905a56544ff8d9600af406d52afdfcd588e3493..5922ffce36e42ef1e6f98f9f04cc49b32e8aff14`. `git rev-parse HEAD` printed
`5922ffce36e42ef1e6f98f9f04cc49b32e8aff14`, the head given. One commit, one file (`foundations/decisions.md`, +5 -6), both hunks
inside WAY-330. I read the findings file, the fix report and the diff of the range (computed with `git diff <base>..HEAD`).

## Each finding of the findings file

1. WAY-12 sentence in *Rationale*: **remains, as the findings file intends** — the finding's own suggestion was "keep the sentence",
   so no change was due; the request carries it as the cycle's wording. The sentence is unchanged on the head
   (`foundations/decisions.md`, last sentence of *Rationale*). Minor; blocks nothing.
2. *Verification* "violates" example: **fixed.** `foundations/decisions.md:10972-10974` now reads "a new script's reading of a file, or
   a changed script's reworked reading of a file, has no test that gives the file without a field". It carries the qualification of
   the binding sentence (a new script; in a changed script, the reworked reading of a file), so it no longer reaches a reading the
   binding part leaves out. Its grammar differs from the other "violates" items (a state, where they are changes) but it reads
   plainly; not a finding.
3. The writer's own additions (relation, pair of examples, WAY-12 sentence): **remains, as the findings file intends** — the
   suggestion was the naming in the request, no change to the entry. The entry is unchanged there. Minor; blocks nothing.
4. *Rejected*, the clause on a new exit code: **fixed.** The statement "the skills that read exit codes know only 0, 1 and 2" is gone
   (`foundations/decisions.md:11014-11015`); the clause now reads "a new exit code, such as 3 — each skill that reads exit codes would
   have to be extended." It states what a skill would have to do if a code were added, not what the skills hold today, so the defect
   (a statement about the process's tools today that goes false when a code is added) no longer exists.

## The author's dropped tail (beyond my suggestion)

The author cut the clause not only at "each would have to be extended", as I suggested, but also dropped the statement about the
skills, which was the finding's own complaint, and kept the cut at "extended". Judgement:

- Dropping "know only 0, 1 and 2" is right: it was the defect, and my suggestion (cut only the tail after "extended") would have left
  it in the clause. I accept the author's reading of the finding.
- The tail that went with it — "and until then each orchestrator would read an unknown code its own way, in exchange for a signal
  that exit code 2 already gives" — is the other half of the cost the task keeps beside this *Not chosen* way (Q3 (c) in the frozen
  task), and WAY-134 has *Rejected* keep each way with the cost or the reason kept beside it. The tail makes no claim about what the
  skills hold today, so my suggestion did not call for its removal. What is left ("would have to be extended") is a true but weaker
  cost, and the reason that exit code 2 already gives the signal no longer stands in the entry.
- Grade: **new Minor, within the task** (not blocking). Evidence: the task's *Not chosen* for Q3 (c) read against
  `foundations/decisions.md:11014-11015`. Suggested, for a later pass if the human wants the task's wording whole: restore "until then
  each orchestrator would read an unknown code its own way, in exchange for a signal that exit code 2 already gives" after
  "extended"; it states no present fact about the skills. The author named this cost and its remedy in its report, so no hidden
  change.

## Review of the fix diff for what it broke

Both hunks are wording inside WAY-330. No binding sentence, field, relation or *Scope* changed. The first hunk makes the example
consistent with the binding sentence and the second shortens *Rejected*. No new Critical or Important finding. A new Minor: the one
above.

## Checks run

- `python -B elements/common/foundation_check.py` (cwd = the worktree) — exit code 0, output `0 errors`.
- `git rev-parse HEAD` — exit 0, `5922ffce36e42ef1e6f98f9f04cc49b32e8aff14`.
- `git diff 4905a56544ff8d9600af406d52afdfcd588e3493 HEAD --check` — exit 0.
- `git diff` and `git log` of the range — exit 0; one commit, one file.
- `git status --short` of the worktree — clean before this report (I changed no file but this report).
- Not run: `gate/run_tests.py` (the orchestrator's). No test written or changed: the fix is wording in one foundation entry.

## Declined to judge

- Whether WAY-12's wording should be narrowed, and whether `derives from WAY-38` is the best relation: findings 1 and 3 stay with the
  request by the findings file's own suggestion.

## Reaches beyond the dispatch

None beyond reading `task-cycle/review/fix.md` and the frozen task's *Not chosen* of Q3 (c) to judge the dropped tail.

## Unread material

none. The fix diff is two hunks and I read both; the findings file and the fix report I read whole. The frozen task's Q3 (c)
passage I read whole in the earlier review of this cycle. In a fix review I read no decisions beyond WAY-330 and the entries named
by the findings (WAY-05, WAY-12, WAY-134, read whole in the earlier review).

## Searches not found or unclear

none.

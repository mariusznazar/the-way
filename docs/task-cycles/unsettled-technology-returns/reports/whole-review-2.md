PASS 9849f4bef0f909e70c2222ee8cdfbcd305662e33

# Review of the fix — `e21d286..9849f4b`

All three blocking findings are fixed. The fix brought no new Critical or Important finding. The
review is bounded by `reports/whole-review-findings.md`, as `task-cycle/review/fix.md` gives. The
eight Minor findings of `reports/whole-review.md` were not to be fixed and stand as written there.

## The findings

| # | Finding | Result | Contested |
|---|---|---|---|
| 1 | A second run's note lost at a document with a section *Technology* | fixed | no |
| 2 | The pointer in `make-change` fired only once the agent had decided to stop, and a fix's agent lacked the sentence | fixed | no |
| 3 | WAY-267 said more than the files do | fixed | no |

### 1. Fixed

`project-level/technology/task_run.md:27-29` holds the new bullet, before the bullets on a list, and
it fires "whatever the items already there end with". I followed the finding's example through the
new text:

1. The section reads `— settled: ...`, and a closed draft gives the named choice as the note
   (`draft.md:15-18`, `resolve_gaps.md:29-30`).
2. The new bullet fires: the section does not hold that note. The note is written, and *List* adds
   the item `— open`, shows the list and sets `waiting for human`.
3. The next bullet resumes "Settle the open choices" without asking about the same list again.
4. "Where the list holds no open item" does not fire, so *Close* comes only after the item is
   settled, and `final_review.md:7-8` then passes for the right reason.

The milder form, an open item already standing, takes the same route. A run with no new note does
not fire the bullet and goes on as before. A choice refinement takes as its note counts as the run's
note under `task_run.md:20-22`.

### 2. Fixed

`task-cycle/change/SKILL.md:99-106` now opens section 5 with the pointer on its own, with no condition
on returning, in the form of `task-cycle/plan/SKILL.md:63` and `task-cycle/spec/design.md:18`. It also
closes the misreading the finding named: "also where the need looks like a choice of how to make the
change. A reserved choice is no such choice". The carve-out at the first case now follows it, so an
agent meets the pointer first.

The old gate is gone: `git grep` finds neither "Before you return `returned`" nor "the first case"
under `task-cycle`, `project-level` or `foundations`. The one hit for "Before you return" is
`task-cycle/spec/design.md:60`, on the designer's own four checks, which is unrelated.

The finding's *Also* is met: `task-cycle/change/fix.md:11-14` carries the sentence, and the table's
row at `SKILL.md:25` sends a fix's agent there. The row's first cell, which handoffs quote, is
unchanged. The rule is still not copied: the pointer names the moment and the file.

### 3. Fixed

Each clause, against the file it must match:

- "for a task of a project plan, under the same name" (`foundations/decisions.md:7713-7714`) matches
  spec decision 5 and step 5 (`task-cycle/skill/SKILL.md:121-122`), and the plan-only sentence in
  `project-level/lead/skill/SKILL.md:77`. *Verification* and *Rejected* now carry the same limit, so
  an independent task following step 5 breaches nothing.
- "says what did not run and why" (`:7709`) and the *Verification* list match
  `reserved_return.md:73-74`, a stop after a spec or a slice included.
- The lesser clause on the pin matches `reserved_return.md:34`.

The fix also changed *Rationale* and *Rejected* of WAY-267, past the finding's *Fix* line. That is
right: left alone, the *Rejected* line would still have read as a ban on an independent task. The
meaning does not go beyond the finding. A search for the changed wording finds no other restatement
of it. The binding part still has three sentences, and `foundation_check.py` passes.

## What the fix itself brought

No Critical or Important finding. Two Minor notes:

- **A narrow interruption can still lose the choice.** `task_run.md:27-29`. If a run stops after
  writing the note and before writing its item, the section then holds the note, so the bullet does
  not fire on resume, and with no open item the run goes to *Close*, the original defect. `list.md`
  writes the list before it asks, so the two writes normally land together; the text does not say
  so, as the fix's own-work check also found. Testing for "a note with no item" would close it. Not
  Important: it needs an interruption in that gap, and the resumed list still shows the human what
  stands.
- **Section 5's heading no longer fits its first paragraph.** `task-cycle/change/SKILL.md:97-99`. The
  pointer is now also the rule for an agent that is not returning at all, under the heading "When you
  return without code". The stage agent reads the skill whole, so it does meet it, and the pointer
  works as written. Polish only.

## Outside the fix diff

These are notes and reopen nothing.

- **Minor.** `foundations/decisions.md:7706`, "ends with its attempt discarded", has nothing to
  discard for a choice found at step 4 (`reserved_return.md:38-40`), as the fix's report raises. The
  clause is vacuous there rather than false.
- **Out of scope.** A note naming a choice that already stands `— settled` has no written way in
  `task_run.md`; the human can change it through the list. The task does not ask for this.

## Declined to judge

- The fix report's remark that the spec's own short wordings differ from WAY-267 now: the spec is
  frozen, and the finding directed the entry to follow decision 5 and `reserved_return.md`.

## Checks

| Check | Exit code | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `9849f4b`, the head given |
| `python -B elements/common/foundation_check.py .` | 0 | 0 errors |
| `python -B agent-instructions/skill_entry_points.py` | 0 | entry points are current |
| `python -B instruction-files/check_instructions.py . --file project-level/technology/task_run.md --file task-cycle/change/SKILL.md --file task-cycle/change/fix.md` | 0 | 0 errors, 2 warnings: `AGENTS.md:21`, and the product-only path at `task-cycle/change/SKILL.md:102`, which stood in the same words before the fix |
| `python -B -m unittest discover -s task-cycle -p "test_*.py"` | 0 | 42 tests OK |
| `git grep -n -E "Before you return\|the first case\|instead of .returned." -- task-cycle project-level foundations` | 0 | one unrelated hit, `design.md:60` |
| `git grep -n -i -E "same name\|keeps? the (task's )?name\|nothing else ran\|numbers its name" -- task-cycle project-level foundations` | 0 | only WAY-267 and the plan-only sentence bear on this; the other hits are unrelated |
| `git grep -n -c -F "reserved_choices.md" -- task-cycle/change/SKILL.md` | 0 | 2 lines: the path and its product form |
| `git diff --name-only e21d286..9849f4b` | 0 | the four files the fix report names |
| manual: findings 1 to 3 traced through the changed text | not applicable | as above |

Not run: the gate, which is the orchestrator's. `project-level` tests: the fix changes no script there,
and its report gives them at exit 0. No agent was run on the changed texts, so "fixed" for findings 1
and 2 rests on reading and hand trace, not on observed agent behaviour.

## Reaches beyond the dispatch

- `task-cycle/review/fix.md`, named by the method for this review.
- `project-level/technology/task_run.md:24-38`, the text after the fix, read whole for the trace.
- The files read in my first review stood in as context: `list.md`, `draft.md`, `resolve_gaps.md`,
  `final_review.md`, `reserved_return.md`, unchanged by the fix.

## Searches not found or unclear

none

# Fix report — cycle `cycle-remarks-batch-4`, the fix of the whole-change review's findings

**Status:** `done`

**Commit:** `5841ed7` (range `0d59ce9..5841ed7`), files: `elements/common/foundation_check.py`,
`foundations/decisions.md`, `task-cycle/skill/SKILL.md`, `task-cycle/skill/request_template.md`.
The sentence the task gives for WAY-71 and `rules.md` (To do 6) is unchanged.

## Findings

- **I-1 fixed.** `request_template.md` item 15 now reads from "the invariants file of the tree after
  the change": each `TODO — <the fact, with its source>` in an invariant's *Rests on* that stands
  there ("the change writes it, keeps it or does not remove it") is one item, with "Merge with the
  gap?"; the sentence "A `TODO` in an entry the change does not touch is not the change's" is gone,
  and the item says that a request carries one such item for as long as an old gap stands. WAY-287's
  binding sentence now says "that stands on the main branch after the change (WAY-71)" (was "that
  the change leaves"), and its rationale says that a `TODO` standing in *Rests on* once the change is
  merged is a gap the merge accepts, "while an old gap stands, every request carries it". A grep for
  "entry it edits", "does not touch" and "not the change's" finds no remaining narrowing text in the
  repository. **Cost taken on (ruling 1):** one item in *For you to decide* of every request for as
  long as any descriptive `TODO` stands in an invariant's *Rests on* on the tree; and a bare `TODO`
  is an error of the script, so only the descriptive ones can stand.
- **M-1 fixed.** `task-cycle/skill/SKILL.md` line 48 (pin-move run): "as step 10 gives, at once".
- **M-2 fixed.** `SKILL.md` sub-step 9.4: "run the gate on the change as step 10 gives (at once, since no
  return step runs), run `task-cycle/cycle_stages.py`, ..." rewrapped within 100 columns; the short
  line after "The authors' focused checks are not" in step 10 is rewrapped; line 48 rewrapped after
  the added words so it stays within 100 columns.
- **M-3 fixed (docstring only, check unchanged, ruling 4).** `foundation_check.py` docstring now says
  "Only a value that begins with `TODO` is read so: a `TODO` that is an item after other facts, as in
  `clock-tick · TODO`, is not reported, and the dash after `TODO` is not required".
- **M-5 fixed inside the task (ruling 2).** WAY-287 *Verification*: a *complies* example (a request whose
  merged tree holds `Rests on: TODO — the store of documents, once a task chooses it`, written by the
  change or standing from before, names the rule and the missing store in the section) and a
  *violates* example (the section reads `none` while a descriptive `TODO` stands on the merged
  tree). WAY-71's *Scope* and *Relations* untouched, as ruled; the *Scope*/*Relations* part is outside
  the task for the human.
- **M-6 fixed (ruling 3).** WAY-160's *complies* sentence stays as the task gives it; the rationale
  sentence is now the plain "The price is that a failure of the gate comes after the return step."
  The rule stays in step 10 of `SKILL.md`.
- **M-4** not in this fix, as ruled (whether *Based on* may read `TODO`).

## Checks (command and exit code)

- `python -B gate/run_tests.py task-cycle` exit 0 (238 tests)
- `python -B gate/run_tests.py elements/common` exit 0 (122 tests)
- `python -B elements/common/foundation_check.py .` exit 0 ("0 errors")
- Not run: the full gate (the orchestrator's).

## Own-work check

The requirement most likely unmet: that nothing in the repository still narrows the item to "an entry
the change edits". Check: a grep for `entry it edits|does not touch|not the change's` over the
repository outside `.git` and `.runs`; it finds only unrelated hits in other decisions and
guidelines. The second: that WAY-287's three places (binding sentence, rationale, verification) and
item 15 say the same; I read the four texts side by side after the edit.

## Unread material

none (the findings file, handoff and `fix.md` read whole; the files changed were read at the places
changed and, for `decisions.md` WAY-287 and WAY-160, whole in the first run).

## Searches not found or unclear

none

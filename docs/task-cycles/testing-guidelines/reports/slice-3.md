# Slice 3 — report of the executor

- **Status:** done with concerns (two wording choices the orchestrator may want to confirm; nothing blocks)
- **Commit:** `2b5b1c0` Add the skill that leads the work on a product's testing guidelines
  (author `mariusznn@gmail.com`), on `task/testing-guidelines`, base `87b600e`. Worktree clean.

## Files changed

| File | Added | Removed |
|---|---|---|
| `product-guidelines/testing/SKILL.md` (new) | 229 | 0 |
| `README.md` | 5 | 3 |
| `.claude/skills/the-way-maintain-testing-guidelines/SKILL.md`, `.agents/skills/the-way-maintain-testing-guidelines/SKILL.md` (new, generated) | 15 each | 0 |
| the 40 existing entry points (generated; one line each: the sibling list gains `maintain-testing-guidelines`) | 40 | 40 |

44 files in all; no entry point edited by hand.

## Checks

| Command | Exit | Result |
|---|---|---|
| `python -B agent-instructions/skill_entry_points.py --write` | 0 | created the 2 new entry points, changed the 40 existing |
| `python -B agent-instructions/skill_entry_points.py` (before and after the commit) | 0 | `entry points are current`; no directory without a skill printed |
| `git status --short` before the commit | — | 2 new entry-point directories, 40 changed entry points, `?? product-guidelines/testing/SKILL.md`, ` M README.md`; nothing else |
| `python -B gate/run_tests.py agent-instructions` before the commit | 1 | expected: `test_the_tracked_entry_points_are_what_the_generator_produces` compares tracked files, and the new ones were untracked |
| `python -B gate/run_tests.py agent-instructions` after the commit | 0 | 18 tests OK |
| `python -B gate/run_tests.py gate` | 0 | 18 tests OK |
| `python -B gate/run_tests.py instruction-files` | 0 | 104 tests OK, 5 skipped |
| `python -B elements/common/foundation_check.py` | 0 | |
| `git diff --check 4302f72 -- product-guidelines/ README.md` | 0 | printed nothing |

No test was written: the slice is prose for agents and generated files; the generator's own test
(`skill-entry-points`) covers the entry points.

## Own-work check (section 3)

- **Requirement most likely missed:** the skill mirrors `maintain-coding-guidelines` section for
  section with no mode or step the coding skill lacks (plan *Goal*, ruling C4).
- **Check:** a diff of the `## ` headings and the bold step items of both skills.
- **Result:** the same sections in the same order (opening, Where the skill works with its table,
  What reaches the task document, Orchestrated mode, 0–5). Step 3 is "Audit" (as the styleguide's
  and spec D5 name it), with no trial run, since a test tool has no set of rules to try. Its bold
  items are **Levels** / **Trust boundaries** / **A new level** against the coding skill's
  **Trial run** / **Kinds** / **A new kind**; "A new level" mirrors "A new kind". **Trust
  boundaries** is part of the audit WAY-250 gives, not a mode or a step. The four modes in step 1
  match the coding skill's four one for one.
- Also checked: every file path the skill names exists in the-way (the two that do not,
  `guidelines/testing.md` and `.the-way/…`, are product paths); every WAY identifier it cites is a
  heading of the log; no line of prose is longer than 100 characters.

## Reaches beyond the *Read*

- `foundations/decisions.md` WAY-61 (heading and binding sentence, lines 1391–1397) — to cite it
  next to WAY-08 for "the test of each new invariant in the product's suite", as the coding skill
  does. The handoff's current-ranges list names it, but the slice's *Read* does not.
- `installation/install.py:53` and `installation/README.md:61` (grep for `.runs`) — to confirm
  that the product's git ignores `.runs/`, which the table states.
- `README.md` — I read lines 105–135 before editing it. It is a file of the *Change*.
- `plan.md` — one grep for "testing"/"slice" lines, to see that `reading.md` and the installer
  belong to slices 4 and 5. I read no passage beyond the matched lines.

## Choices made within the spec

- **Description** — I took the spec D5's parenthetical word for word. It does not have the coding
  skill's "an exemplar settled for a kind of code" clause (here it would be "an exemplar test
  settled for a level"). Rejected: adding that clause to mirror the coding skill's description.
  Cost if wrong: one more phrase in the description, then a regeneration.
- ***To do*, "write or extend `guidelines/testing.md`"** — the spec says "write". I added "or
  extend", as the coding skill has it, because the refresh and extension modes write into an
  existing file. Cost if wrong: two words.
- **Charges per level** — step 3 gives the three to five charges for each level, because WAY-250
  ("ends, for each level, with a proposed exemplar test … and three to five charges …") and
  settlement row 24 put them inside the per-level clause. Rejected: three to five charges for the
  whole audit. Cost if wrong: an audit of a product with several levels shows more charges than
  intended. This is my first concern: WAY-250's sentence can be read either way.
- **Step 2 research only where the human has no preferences** — the coding skill also researches
  "at every refresh or extension". Following spec D5 and WAY-249, the testing skill does not. It
  still asks for preferences at every refresh. This does not add a step the coding skill lacks.
- **"A new level"** — the level's recipe comes into being with its first test (WAY-242, WAY-241),
  mirroring "its file of guidelines comes into being with it". Step 4 settles the level, its recipe
  and the test's path.
- **The weak point of a violated boundary invariant** is my wording, modelled on the coding skill's
  violated linter invariant: "until then no test guards the boundary and only the review of each
  change touching it keeps that change from letting more through". Spec D5 says only "its weak point
  said when proposed".
- **Plain words per D1** — the skill never uses "refusal invariant" or "oracle" as a term. It says
  "an invariant that the boundary refuses crafted input or unauthorised access" and "a test of its
  refusal". The condition of return of an exclusion reads as part of what its decision allows,
  checked "whenever a change reaches its category" (ruling C11). It is not a review date.
- **Examples in "How to show"** — the first is WAY-174's own example. The second ("a change that
  loosens what a test checks says what changed in the requirement, or the review reads it as hiding
  a fault") is mine, drawn from WAY-233.
- **Starting-set research questions** — the examples (layout and names per level, what the tool
  offers in place of a real dependency, the clock and the seed) are mine, mapped to recipe fields.
  I deliberately left out a property-test library, which is a technology question (WAY-248).

## Concerns

1. WAY-250 can be read either way: three to five charges per level or for the whole audit. The skill
   follows the per-level reading. If the orchestrator reads it the other way, one bullet of step 3
   moves.
2. "Where the skill works" points to `product-guidelines/reading.md` for finding missing testing
   guidelines, and to `installation/README.md` for a product that pinned the-way earlier. Both files
   name the testing discipline only after slices 4 and 5. Until then, the two sentences point to
   text that does not exist yet on the branch.

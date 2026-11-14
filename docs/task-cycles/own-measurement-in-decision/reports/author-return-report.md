# Author report — the return step

**Status:** done
**Commits:** none. Nothing no longer matched, so nothing was changed; the head stays `82d6431`, the worktree is clean.

## Entries compared with the files of the repository

- **Entries the change writes or changes** (21 decisions of `foundations/decisions.md`, found by
  mapping the hunks of `git diff 3c572b9` to their headings): WAY-90, 136, 164, 229, 255, 256, 300,
  308, 309, 316, 319, 320, 323, 350, 352, 353, 362, 364, 368, 369, 371; and the two templates
  `elements/decisions/template.md` and `elements/environment-facts/template.md`.
- **Entries the task names, unchanged:** WAY-27, WAY-05, WAY-80, WAY-33, and WAY-312 (on purpose: its
  fact `shorter-guidelines-trial` has a source that opens). Also WAY-17 and WAY-85, which the search of
  WAY-33 read, unchanged.
- **Part map of the touched parts** (`decisions`, `environment-facts`): `foundations/part_map.md` gives
  them `elements/decisions/**` and `elements/environment-facts/**`; the change adds no file, so the
  map matches.
- **Places outside the decision log that cite or restate WAY-90**, found by searching the repository
  (outside `.runs/`, `foundations/`, `.claude/`, `.agents/`) for `WAY-90`, "would call the decision into
  question", "a finding about agents or models", "every source outside the product", "Based on" in
  `project-level`, `task-cycle`, `instruction-files` and every element skill, and for "measurement":
  - `elements/environment-facts/skill/SKILL.md:44` and `read.md:6` cite WAY-90 by number only, and
    `decide_entry.md` sends the writer to the template's "Which facts are written"; none restates the
    rule. No change.
  - `elements/decisions/skill/SKILL.md:31` ("sort what the source offers as a reason … is no source
    outside the product") and `decide_entry.md`, `read.md`, `projected.md` do not restate the rule of
    which citation becomes a fact; the skill sends the writer to the template, which carries the new
    point. No change.
  - `elements/decisions/examples.md` names WAY-03 only; WAY-03 is not edited.
  - `project-level/technology/settle.md:75`, `project-level/task/template.md`, `task-cycle/skill/
    request_template.md:264`, `elements/invariants/skill/draft.md` mention *Based on* for other
    purposes (a technology choice, a `TODO` line, an invariant's *Rests on*); none states which
    citations become facts or how a measurement is written. No change.
  - No skill file or example restates the old rule.

## What no longer matched, and its correction

None. The two templates and WAY-90 say the same after the fix of the review; the edited decisions all
carry the sentence in the field where their figures stand; the decisions the sentence did not reach
(WAY-312, whose record opens) are consistent with WAY-90's first sentence plus its open-report clause.

## Entries written

- Decisions: none new (WAY-90 and the 20 others were edited by the change before this step).
- Invariants: none. Environment facts: none (by WAY-90's new rule, a measurement of the product's own
  people is written as no fact, and the task asks for none). Glossary terms: none (the words
  "measurement", "record", "reader" are used in their ordinary meaning; "product" is used as the log
  already uses it). Part-map changes: none.

## Checks

| Command (worktree root) | Exit |
|---|---|
| `python -B elements/common/foundation_check.py --skip-test-citations` | 0 (`0 errors`) |
| the search for the rule's wording in the repository files above (Grep) | no restatement found |
| a script mapping the hunks of `git diff 3c572b9 -- foundations/decisions.md` to decision headings | the 21 entries above, none else |

Not run: the full gate; `private_paths_check.py` and `gate/run_tests.py elements/common` (run at the
fix; no file changed since).

## Unread material

- `task-cycle/skill/foundation_step.md` and `task-cycle/skill/return_step.md`: read whole.
- `elements/decisions/skill/projected.md`, `elements/environment-facts/skill/draft.md`, `write.md`,
  `projected.md`: not read whole; the search showed no line on which citations become facts or on a
  measurement. The files of `product-guidelines`, `instruction-files` and `project-level` that mention
  "environment fact": found by search, read at the matching lines only.

## Searches not found or unclear

none.

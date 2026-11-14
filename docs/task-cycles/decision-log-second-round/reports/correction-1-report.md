# Report of correction 1

**Status:** done

**Commits:** `adeb04a` (one commit, on `task/decision-log-second-round`, by path; not pushed). Files: `foundations/decisions.md` (+42/-7 net of the entry: 49 lines touched), `product-guidelines/coding/SKILL.md`, `hand_back.md`, `settle.md`, `template.md`, `product-guidelines/styleguide/starting_rules.md` (59 insertions, 25 deletions in all).

## The remarks as made

1. Item 2: put back WAY-202. 2. Item 3: complete the two notes (the styleguide one that opens with a reason and has no rule; the coding one that has a rule and no sentence of its reason). Items 1, 12 let through and items 4-11 as one task are the orchestrator's; I changed no file for them.

## Remark 1: WAY-202 put back

- The entry, from `### WAY-202 —` to its last line, copied from `git show ec7929d:foundations/decisions.md` lines 6199-6232 and placed before `### WAY-203` (its place in the numbering). Checked by `diff` against the base: identical.
- The row of WAY-202 removed from the list *Withdrawn identifiers*.

**Restored**

| Place | Was at HEAD | Now |
|---|---|---|
| `foundations/decisions.md` WAY-203 *Relations* | `derives from WAY-100` | `derives from WAY-202 · derives from WAY-100` |
| WAY-206 *Relations* | `derives from WAY-60 · derives from WAY-100` | `derives from WAY-202 · derives from WAY-60 · derives from WAY-100` |
| WAY-216 *Relations* | `narrows WAY-251` | `narrows WAY-251 · narrows WAY-202` |
| WAY-216 *Rationale* | `stands decided, so a kind` | `stands decided (WAY-202), so a kind` |
| WAY-360 *Rationale* and *Rejected* (two places) | `...takes the proposal up;` | `...takes the proposal up (WAY-202);` |
| `hand_back.md` | `settled, that` | `settled (WAY-202), that` |
| `settle.md` (two places) | `for each;` and `compares the change with it (WAY-168).` | `for each (WAY-202);` and `(WAY-168, WAY-202)` |
| `template.md` (7 places: the invariants bullet, the three-standing-checks bullet, the rule of size bullet, Linter, Formatter, Dependency audit, "A standing check the product goes without") | the number WAY-202 absent from each bracket | `WAY-202` back at each, in the base wording; where WAY-171 or WAY-86 also stood at the base and was withdrawn on its own, I left that other number out |

**Removed because only WAY-202's leaving added it:** in `template.md`, the three-standing-checks bullet, the two sentences "The task that writes a product's coding guidelines is complete only once ... with the reason." (the rule sentence the withdrawal copied from the entry) and "A product whose code no standing check reads changes its style and takes in a known vulnerability with no signal." (its reason). The bullet reads again as at the base for this rule. Note: the remarks name the sentence of reason; I removed the copied rule sentence too, since it served no other rule and the entry now carries it. If the human wants it kept in the template, one sentence is to be added back.

**Kept:**
- The relation `derives from WAY-100` on WAY-203 and WAY-206 and the WAY-100 wording in their *Rationale*: it serves the withdrawal of WAY-207, not WAY-202.
- The sentences added to the files for WAY-207, 271, 272, 275, 277, 279 (reasons) and every other withdrawn number's removal, including the line reflows they caused in `hand_back.md` (WAY-279) and the other hunks.
- The row of WAY-196 in the withdrawn list (`... the invariants of a standing check in WAY-202 | WAY-168 · WAY-198 · WAY-202`): identical to the base, and now true again; no change needed.
- WAY-202's own *Relations* and cited numbers (WAY-173, WAY-168, WAY-139): as at the base; all three entries stand in the log.

A search of the tracked files at HEAD for `WAY-202` (outside `docs/` and `.runs/`) now finds the entry, the three relations, the three prose references and the WAY-196 row; the files that cited it at the base all cite it again.

## Remark 2: the two notes

- (a) `product-guidelines/styleguide/starting_rules.md` line 3: now "A first screen built with no rules is the screen every later one copies, so the styleguide of a user interface comes into being before that user interface's first screen." The rule is WAY-184's binding sentence ("the styleguide of a user interface comes into being before that user interface's first screen"); the wider-than-the-first-task part of that sentence already stands in the last bullet of the file, so I did not repeat it.
- (b) `product-guidelines/coding/SKILL.md`, "A new kind": after the sentence ending "the rules a script checks of it." I added "A first file built with no exemplar is the file every later one copies." — WAY-200 *Rationale*, "a first file built with no exemplar is the file every later one copies". I rewrapped the next two lines of the bullet to keep them under 100 columns; no word of them changed.

## Checks

- `python -B elements/common/foundation_check.py` — exit 0, "0 errors", with the one expected `listed:` line for `tracked-file-private-paths`.
- `python -B agent-instructions/skill_entry_points.py` — exit 0 (the description of no skill changed).
- `python -B gate/run_tests.py foundations`, `... product-guidelines/coding`, `... product-guidelines/styleguide` — each exit 1 with "no test found": these directories hold no test (the runner's exit 1 for a directory without a test).
- `python -B gate/run_tests.py elements/common` — exit 0, 201 tests OK (not required; run because `foundation_check.py` lives there and reads the log).
- Not run: the whole gate (as the handoff says).

## Own-work check (WAY-164)

Most likely missed: a rule written from memory, not from the entry at the base. Read against the entries at the base (`git show ec7929d:foundations/decisions.md`): WAY-184 (rule sentence and *Rationale*), WAY-200 (*Rationale*), WAY-202 (whole entry, `diff` against the base shows no difference). Each added sentence is the entry's own words; WAY-184's *Verification* and WAY-200's *Rationale* gave a sentence in both cases, so none was left out. The copy of the template's WAY-202 sentences was compared to the base file with `git diff ec7929d -- template.md`: every WAY-202 hunk now shows only the removed WAY-171/WAY-86 numbers.

## Reaches beyond the dispatch

`git grep -n WAY-202` at the base and at HEAD, and `plan.md` line 312 and the report of executor 14 of the record (to see which sentence the withdrawal added to `template.md`). The reading of `scripts.md` and `git.md` (the author's rules) before the first script and commit.

## Unread material

none. (I did not read the whole of `product-guidelines/coding/SKILL.md` or `template.md` beyond the changed passages and their surrounding lines; the handoff names no guideline file to read whole.)

## Searches not found or unclear

- The handoff says the row of WAY-196 "names WAY-202" and could need a change; it is identical to the base, so nothing to restore; I read this as a check to make, not an edit.
- `.runs/task-cycles/decision-log-second-round/reports/correction-1-remarks.md` says "Same ground as items 1, same outcome" for WAY-202; I took the handoff's two parts as the whole of what to do.
- No other file at HEAD names a withdrawn WAY-202 (docs excluded, as the handoff says).

## Choices

- Removed both the reason sentence and the copied rule sentence in `template.md` (above). Rejected: removing only the reason sentence. Cost if wrong: one sentence to put back.
- WAY-203/206 relations keep `derives from WAY-100` beside the restored `derives from WAY-202`. Rejected: dropping WAY-100, which the kept *Rationale* wording still cites.

## Working copies

I made `.runs/correction-1/dl.diff` and `.runs/correction-1/way202.txt` (a diff of the log and the extracted entry). Both removed one by one by path, then the empty directory; nothing remains.

PASS adeb04a2e24495aa7e0ed5190e521998ca152d4e

# Review of correction 1 (`f080288..adeb04a`)

`git rev-parse HEAD` is `adeb04a2e24495aa7e0ed5190e521998ca152d4e`, the head given. One commit in the range. Read-only; nothing changed in the worktree.

## Findings

No Critical, no Important.

### Minor

1. `product-guidelines/styleguide/starting_rules.md:3-4` — the rule sentence drops the entry's qualifier. WAY-184's binding sentence at the base says that the skill `maintain-styleguide` *proposes* that the styleguide of a user interface comes into being before that user interface's first screen. The note says flatly that "the styleguide of a user interface comes into being before that user interface's first screen". A reader of the file may take it for an unconditional rule, not the proposal WAY-184 binds the skill to. The consequence is small: the file is read by that skill, and the decision stays in the log as the source. Not blocking. Evidence: `git show ec7929d:foundations/decisions.md`, WAY-184, first paragraph, against line 3-4 of the file.

## The remarks, each as made or not

- Item 2 (put back the entry): made. Details in the judgement below.
- Item 3, first note (styleguide, a reason with no rule): made. Rule from WAY-184's binding sentence, reason from its *Rationale* ("a first screen built with no rules is the screen every later one copies"), both from the base, none from memory; see Minor 1 for the one qualifier.
- Item 3, second note (coding "A new kind", a rule with no reason): made. The added sentence "A first file built with no exemplar is the file every later one copies." is WAY-200's *Rationale* at the base, word for word. The rewrap of the next two lines of the bullet changes no word (checked by reading both versions).
- Items 1 and 12 let through, items 4-11 for `/park`: no file changed for them.

## Judgement by the handoff's five points

1. **The entry is identical to the base.** The entry cut from `ec7929d:foundations/decisions.md` (lines 6199-6232) and the entry at `adeb04a` from `### WAY-202 —` to the next heading differ only by the blank line my cut kept. Its place is before WAY-203. The row of WAY-202 is gone from *Withdrawn identifiers* (`git diff ec7929d adeb04a` holds no line for that row; at the base there was none). The row of WAY-196, which names WAY-202, is identical to the base and true again.

2. **References.** At the base the 18 lines naming WAY-202 outside `docs/` and `.runs/` were: the entry, three *Relations* (WAY-203, WAY-206, WAY-216), three prose references (WAY-216 *Rationale*, WAY-360 twice), the WAY-196 row, `hand_back.md` (1), `settle.md` (2), `template.md` (7). `git grep -n WAY-202 HEAD` gives the same 18 places. Where the withdrawal of another entry also touched the same line, that change stands: WAY-171 and WAY-86 left out of the brackets in `template.md`, `derives from WAY-100` kept on WAY-203 and WAY-206 beside the restored `derives from WAY-202` (the withdrawal of WAY-207 repointed the *Rationale* of both to WAY-100, which the restored entry does not undo; the base had only WAY-202 and the WAY-60 on WAY-206; the addition is correct and the order is harmless). WAY-216's *Relations* at HEAD, `narrows WAY-251 · narrows WAY-202`, lacks the base's `derives from WAY-200 · derives from WAY-209` because WAY-200 and WAY-209 stay withdrawn, as they should. The correction left the withdrawal of the other entries alone: the other hunks of `git diff f080288 adeb04a` touch only WAY-202 passages, the two notes and the template sentences below.
   - The two sentences removed from `template.md`, the three-standing-checks bullet ("The task that writes a product's coding guidelines is complete only once the product's log holds, for each of the three standing checks, a decision adopting it or departing from it with the reason." and "A product whose code no standing check reads changes its style and takes in a known vulnerability with no signal."): the first is the entry's binding sentence, the second its *Rationale*. The base template held neither (`git show ec7929d:product-guidelines/coding/template.md`); the withdrawal copied them. The rule still stands in the restored entry; in `settle.md` ("the task is not ready without one for each (WAY-202)"), in `hand_back.md` ("each standing check has its adopting or departing decision among the choices settled (WAY-202)") and in the template's own line of a check the product goes without (`none — <PREFIX-NN>` naming the departing decision). Removing both, including the rule sentence the remarks did not name, is right: with the entry back the copy is a duplicate and WAY-263 forbids a restatement that differs. The correction's report names this choice and its cost.

3. **The two notes** hold a rule and a reason each, from the entries at the base (above). One qualifier in Minor 1.

4. **Nothing the remarks do not name changed.** The six files changed are the log (the entry, the three relations, the three prose references, the row), `hand_back.md`, `settle.md`, `template.md` (the WAY-202 hunks and the two sentences), `starting_rules.md` and `SKILL.md` (coding) (the notes). I read every hunk of `git diff f080288 adeb04a`; none lies outside the remarks and the restoration they require.

5. **Checks** below.

## Declined to judge

- The items 4-11 of the remarks (the seven decisions with *Based on* TODO and the seventeen that miss the left-out half of an outside practice): their own task through `/park`, not this correction.
- Whether the entry's *Verification* and the rest of its content are good: restored as it stood at the base and approved there, outside the correction.

## Checks run

| Command | Exit |
|---|---|
| `git diff ec7929d adeb04a` against the withdrawal diff `git diff ec7929d f080288`, file by file for the six files | manual; showed the above |
| entry diff: `git show ec7929d:foundations/decisions.md` lines 6199-6232 against the entry at `adeb04a` | manual; identical |
| `git grep -n "WAY-202"` at `ec7929d` and at HEAD (outside `docs/` and `.runs/`) | 18 and 18 places, same files |
| `python -B elements/common/foundation_check.py` | 0 ("0 errors"; the one expected `listed:` line for `tracked-file-private-paths`, `foundations/invariants.md:86`) |
| `python -B gate/run_tests.py elements/common` | 0 (201 tests OK) |

Not run: the whole gate (the handoff forbids it).

## Reaches beyond the dispatch

- `task-cycle/review/fix.md` (the skill's own file for a correction), `git show ec7929d:foundations/decisions.md` for WAY-184, WAY-200 and WAY-202, and `git show ec7929d:product-guidelines/coding/template.md`: to compare the notes and the template sentences with the base, as the handoff names the base.
- `git grep` for "complete only once", for "standing check" in the added lines of the withdrawal, and for the first-screen sentence in the styleguide files: to find whether the rule or the notes stand elsewhere.

## Unread material

The handoff names no guideline or foundation selection to read whole. I read whole: the three WAY entries named above, the review skill and `fix.md`, the remarks, the correction report. I did not read `task.md` (lines 1-490), `review-whole-report.md` and `review-fix-report.md` beyond the search for their Minor findings, and the whole of the changed guideline files beyond the hunks and their surrounding lines.

## Searches not found or unclear

- `review-whole-report.md` holds its Minor findings in a numbered list I did not read through; I took the two notes from the remarks and the correction's report, not from the list.
- The handoff says to "read the two sentences against the entry and say whether the rule they stated still stands somewhere": done above; no search failed.

## Working copies

none.

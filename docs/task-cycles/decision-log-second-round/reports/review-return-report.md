PASS 9c24d0d35a1faae6eb510f103166492d8861532e

# Review of the return step, range `0364c08..9c24d0d` (one commit)

Worktree `the task's worktree`. `git rev-parse HEAD` is `9c24d0d35a1faae6eb510f103166492d8861532e`, the head given. `git log 0364c08..9c24d0d` holds the one commit. The worktree was clean at the start and I changed nothing.

## The change

`foundations/decisions.md:9064`, one row of *Withdrawn identifiers*. WAY-200 now reads "stands in `product-guidelines/coding/kinds.md` and `product-guidelines/coding/SKILL.md`" (before: `kinds.md` alone). No other line of the range changed.

## Verdict on the change

The edit is correct. WAY-200 at the base (`git show ec7929d:foundations/decisions.md`, "### WAY-200") has two parts.

- **First file of a kind.** "Where a product holds no file of a kind, the exemplar is designated by the task that creates its first file." It stands in `product-guidelines/coding/SKILL.md:133`, "A new kind": "Where the task creates the first file of a kind of code, that file is the kind's exemplar". The fix of the review (`d55625e`, finding 9) removed the same sentence from `kinds.md`, so `kinds.md` alone no longer held it.
- **Product with files.** The skill judges every file, compares them, proposes the exemplar with `copy` / `do not copy`, and the human approves the decision that designates it. It stands whole in `product-guidelines/coding/kinds.md:5-12`: judge every file, compare, propose, human approving, `copy` / `do not copy`.

The verification examples of WAY-200 are covered: nine endpoints judged and compared, and a task that creates a first migration designates it. No live entry or file outside the withdrawn row names WAY-200 (`grep -rn WAY-200` over `foundations/*.md` and every `.md` and `.py` outside `foundations` and `.runs` finds only this row). The row keeps the form of the neighbouring rows, including those `0364c08` corrected for WAY-115, WAY-156 and WAY-184, and its successor stays `none`.

WAY-02 is untouched: the row names files, no fingerprint or version. WAY-25 and WAY-293 are discussed under the choices.

## The two choices (accepted)

1. **No entry for "an entry that `narrows` a staying decision stays in the log".** Accepted. WAY-25's *Rationale* already says "The decision that prevails holds the record". WAY-293's second paragraph decides which entries stay by the test "a choice with a real cost", and the task's table keeps the narrowing entries on that ground, for example WAY-240 "the precedence and the rejected unprecedenced pair carry a cost" and WAY-270. A new entry would restate WAY-25 and WAY-293 and need keeping in step with both. Residual: the statement lives in WAY-25's *Rationale*, not its binding sentences, so a later round could withdraw a narrowing entry by the first paragraph of the test alone. That is not a defect of this change, and no finding follows.
2. **No entry for "the ten kept entries".** Accepted. The ten (WAY-93, 94, 97, 263, 287, 294, 295, 297, 363, 364) are the result of applying WAY-293 to a table, not a rule that binds after the merge. An entry saying "these ten stay" would contradict the next round's own application of WAY-293. WAY-293 requires a skill or template to name each kept decision; the return step's report says it checked that, and I did not repeat that search (listed under Unread material).

## Findings

None blocking. Two Minor.

**1. Minor, in scope, not blocking.** `product-guidelines/coding/SKILL.md:133-139` ("A new kind") holds the first-file half of WAY-200 with no sentence of its reason, and the row now names that file as one place the rule stands. WAY-293 second paragraph requires a rule of a skill to stand "with one sentence of its reason". The reason, "a first file built with no exemplar is the file every later one copies", stands in `product-guidelines/coding/kinds.md:10-12`, which `SKILL.md:125-130` reads in step 3 only on the route of the audit or of one kind. A new kind in a product with coding guidelines runs "A new kind" with no audit, so its reader may not meet the reason. The cause is the fix `d55625e`, not this commit, which names where the rule stands correctly. Evidence: the sentence removed from `kinds.md` by `d55625e` and the text of `SKILL.md:133`.
- If fixed: one clause of reason added to "A new kind". If left: the first-file rule is a statement with no reason, which the next review under WAY-293 may raise again.

**2. Minor, out of the range and out of scope (the row is in `0364c08`, not this range).** The row of WAY-184 names `product-guidelines/styleguide/SKILL.md` and `starting_rules.md`. The timing rule "the styleguide comes into being before the first screen" stands in `SKILL.md` only as the trigger in its `description:` line 3, and `starting_rules.md:3` now holds the reason with no timing sentence beside it. This is the Minor finding of the review of the fix, repeated by the return step's report; the row is correct about where the words stand, and the weakness lies in the files.

## Other rows of the withdrawn list (the ones I could check)

- **WAY-115.** `build_table.md` lost, in `d55625e`, the sentence on the working table and the `Candidates:` line. That sentence stands in `definition_variant.md:26,64-65` and `task_variant.md:56`, and the row names both. Matches.
- **WAY-156.** `route_changes.md` lost the sentence "you change definition text yourself only when…". It stands in `project-level/lead/skill/definition_change.md:10-12`, and the row names that file. Matches.
- **WAY-184.** See finding 2.
- **WAY-41 and WAY-64 (`elements/common/rules.md`).** `b0b7e3a` took out the clause on split or merge of three kinds of entry and kept "Splitting or merging entries gives each entry … a new identifier" and the rule of withdrawn identifiers at `rules.md:57-74`. Both rules still stand there.
- **WAY-207 (`product-guidelines/coding/template.md`).** `26575cd` added the ban on changing the exemplar for one file's sake, with the reason. The rule stands whole.
- **WAY-117 (`elements/common/projected_mode.md`).** `a068f99` took the repeated reason out of four element skills; `projected_mode.md` holds it.
- **WAY-37 (`elements/common/way_of_working.md`).** `27acdf2` removed the duplicate from `environment-facts/skill/read.md`; the row names `way_of_working.md`, which holds the rule.
- **WAY-201.** The row names `kinds.md`, which still holds the proposed exemplar with its sentence, the `do not copy` list with file and line and the `Places:` link; the list of WAY-283 has its own row (`audit_end.md`). Matches.
- **WAY-296, 357 and 358 (`record_template.md`).** `046d779` only added a reason. I did not read the whole template for these rows.

No other row I checked names a place that no longer holds its whole rule.

## Declined to judge

- The empty directories `.runs/executor-*` and `.runs/fc.txt` left by earlier agents (finding 12 of the review of the whole change, named in the return step's report): not a matter of this commit.
- `product-guidelines/styleguide/starting_rules.md:3` as text (Minor of the review of the fix): outside this range; only its effect on the row of WAY-184 is judged (finding 2).
- The "Rationale of WAY-173 still names WAY-100" item of the return step's report: outside the range.
- The 137 withdrawals and the other rows of the list: outside the range.

## Checks

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` | 0 (`0 errors`; one `listed:` line, for `tracked-file-private-paths`, as expected) |

Manual: `git rev-parse HEAD` equals the given head; `git log 0364c08..9c24d0d`; `git show 9c24d0d` (one row); the base text of WAY-200, 184, 115, 156, 41, 64, 207 by `git show ec7929d:foundations/decisions.md`; the diffs of `d55625e`, `b0b7e3a`, `a068f99`, `27acdf2`, `26575cd`, `046d779`, read against the withdrawn rows naming the changed files; `grep` for the places where each removed sentence stands now.
Not run: the whole gate and the other tests (excluded by the handoff).

## Reaches beyond the dispatch

- `task-cycle/review/SKILL.md` whole: the method of this review.
- `product-guidelines/styleguide/SKILL.md`, `starting_rules.md`, `recognize.md` (lines named above), by search and in part: whether WAY-184's timing rule stands anywhere.
- The base text of WAY-184, 115, 156, 41, 64, 207 and the withdrawn list, `foundations/decisions.md:8972-9100`: to judge the other rows.
- WAY-02, WAY-25 and WAY-293 whole at the head, as the handoff named them.
- `.runs/task-cycles/decision-log-second-round/task.md:1-45` and a search of it for "narrow" and kept entries: the choices and To do 2.
- The decisions WAY-216, 247, 251 and 265 by title and row: only to learn that the numbers cited in `coding/SKILL.md` are live (they are).

## Unread material

- `task.md` from line 46 to 490: read only by search (`narrow`, `kept`, `Return step`, `Withdrawn identifiers`) and the table rows found; the lines 1-45 whole.
- The return step's report: read whole. Its claims on WAY-100, 29, 288, 309, 316, 339, 368, 312, 09, the four invariants, the part map and the environment facts: not repeated, since the range holds none of them.
- WAY-93, 94, 97, 263, 287, 294, 295, 297, 363, 364: not read, nor the check that a skill names each.
- The diffs of the other fix and task commits beyond those named above, and the remaining withdrawn rows: not read.
- `product-guidelines/coding/SKILL.md`: read lines 100-158 and the grep results, not the whole file.

## Searches not found or unclear

- A check that holds each row of *Withdrawn identifiers* to the files it names: none found; the comparison above is by reading.
- Whether the timing rule of WAY-184 stands in the styleguide template (`product-guidelines/styleguide/template.md`): not searched there; a search over every `.md` for "first screen" outside the log found only `SKILL.md:3`, `recognize.md:9` and `starting_rules.md:3`.

## Working copies

None made. `.runs/review-return/` not created.

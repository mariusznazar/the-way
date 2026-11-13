PASS faee0f877d899070ba090c4e4d546f6ab5af713c

# Review of the fix of the Minor findings

Range `2c27260`..`faee0f8` (one commit). `git rev-parse HEAD` in the worktree is `faee0f877d899070ba090c4e4d546f6ab5af713c`. Diff computed with `git diff 2c27260..faee0f8` and `git log 2c27260..faee0f8`. It touches three files, the three the findings name, and nothing else (`git diff --name-only`).

Result: 0 blocking findings, 0 new Minor findings, 3 of 3 findings fixed.

## The findings of the findings file

1. **S3, `elements/invariants/template.md:59-60` — fixed.** The sentence now reads "A test stands in a file of code (WAY-61, WAY-321); a Markdown file holds no citing test." WAY-321 (read whole in the first review) says the check reports an invariant that no line `invariant: <identifier>` "in a file git tracks other than Markdown" cites, so the Markdown clause now has a decision that states it. WAY-321 is the one already cited at `:52` of the same file. The reader who opens WAY-61 and WAY-321 finds both clauses.
2. **S9, `elements/part-map/template.md:148-149` — fixed.** "A row names no part and no file." now stands with no cite, and the second sentence keeps its exact `(WAY-48)`. The unconfirmed attribution and the repeated cite are gone; this is the first of the two options the finding gave. It departs from the task's pairing of S9 with WAY-48 for the first sentence, but the task lets the review replace a cite it cannot confirm, and I recommended it. The sentence's sense is unchanged.
3. **Item 5, `elements/environment-facts/template.md:91-94` — fixed.** The sentence now reads: "An invariant whose *Rests on* names a missing fact takes `TODO — <the fact, with its source>` there, and a decision whose *Based on* names a missing source takes `TODO — <what is missing, with its source>`; a change that leaves one there puts it before the human (WAY-71)." These are the two forms WAY-71 and `elements/common/rules.md:20-23` give for those two fields, and the ambiguity of "an entry" in a fact template is gone. It keeps the task's content (an entry that would stand on a missing fact gets `TODO`, a change that leaves it puts it before the human). The author's note that `*Based on*` is split across a line break does not apply to the head: the italic words are whole on their lines.

## What the fix itself changed

Nothing outside the three sentences. No `decision pending` marker added or removed (two remain, S26 and S28, as before). No test or script reads the sentences (the earlier `git grep` stands). The reflowed lines stay within the file width the files use. No new Critical, Important or Minor finding in the fix diff.

## Checks run

| Command (from the worktree root) | Exit |
|---|---|
| `git rev-parse HEAD`, `git log 2c27260..faee0f8 --oneline`, `git diff 2c27260..faee0f8`, `git diff --name-only 2c27260..faee0f8` | 0 |
| `python -B elements/common/foundation_check.py --skip-test-citations` | 0, "0 errors" |
| `git diff --check 2c27260..faee0f8` | 0 |
| `python -B gate/run_tests.py elements/part-map` | 0, "Ran 39 tests ... OK" |
| `git grep -c "decision pending" faee0f8 -- elements` | the two known lines, `environment-facts/template.md` and `invariants/template.md` |

Not run: `gate/run_tests.py` whole (the orchestrator's). `elements/common` tests were run by the author at the fix (144 OK) and by me at the previous head; the fix touches no file of `elements/common/`, so I did not repeat them.

## Unread material

- Whole: WAY-71, WAY-321, WAY-48, WAY-61 (from the first review, not re-read), and `elements/common/rules.md:13-23` (read by grep lines in the first review, read again for lines 17-23 here). Of the fix's own files I read the three diff hunks with their sentences; I did not re-read the whole templates.
- The decisions, invariants, part-map and glossary entries not read in the first review remain unread; the fix does not reach them.
- Guidelines: none apply to these files.

## Searches not found or unclear

- None.

PASS 9c7f9b71

# Review of the fix — decision-length-check

Range `e8b76178..9c7f9b71`, two commits (`67933213`, `9c7f9b71`); `git rev-parse HEAD` gave
`9c7f9b717344eb15f0e41f905746f7fb70790084`. The findings file holds one blocking finding and four
Minor findings within the task. All five are fixed, and the fix diff brings no new finding of any
grade.

## The findings of the findings file

**1 (blocking) — fixed.** Contradiction: yes — WAY-05, second paragraph, as the finding was marked;
the fix removes it.

- `README.md:86-93` now gives the two errors in two sentences. The first ends "…and that nothing
  holds." The second reads "It reports as an error too each paragraph of binding sentences over
  three sentences or 300 words in a decision that a change adds or whose binding sentences it
  alters, a different division of them into paragraphs included." "That nothing holds" no longer
  reaches the error for length, and the division is named in the words of WAY-05
  (`foundations/decisions.md:697-700`). The sentence of what is listed follows unchanged in meaning.
- `agent-instructions/README.md:15-18` adds, after "whose binding sentences it alters", the words
  "a different division into paragraphs counting as an alteration for this report alone". That says
  both that the division counts here and that it does not count for the report of decisions that
  nothing holds, which the same sentence names.

Neither file now says more or less than the entry.

**2 (Minor) — fixed.** `elements/decisions/template.md:121` now says the script "counts the
sentences and the words of each of their paragraphs in every decision, reporting an excess as an
error in one a change adds or alters, a different division into paragraphs included, and listing it
in any other (WAY-05)". It agrees with the code and with the rule fifteen lines below it.

**3 (Minor) — fixed.** `elements/common/test_foundation_check.py:2191` replaces `"d. "` by
`"d.\n"`. Run on the test's paragraph, the expression now gives a text that differs from the
original, with three line breaks and two doubled spaces, and that is the original again once every
run of spaces and line breaks is made one space. The test passes, so it now holds that a line break
alone is no change.

**4 (Minor) — fixed.** `elements/common/foundation_text.py:17` writes `QUOTED` with the escapes
again. `cmp` of that line with the line of `foundation_check.py` at `1b6fe1c1` gives exit code 0,
and the line holds no byte outside ASCII. The move is now unchanged in every line, as its commit
message says.

**5 (Minor) — fixed.** `foundations/part_map.md:67-75`: the sentence of `elements-common` reads
"…with the module that reads the files and git for it and the module that reads the text of an
entry for it, …". It says what `foundation_text.py` is for and names no path; the rest of the
sentence is reflowed with no word changed. No other file repeats the sentence, and the check of the
foundation gives no error on it.

The author contests no finding.

## The fix diff itself

Six files, 19 lines added and 15 removed, every hunk answering one of the five findings. No code of
the script changed beyond the one line of the pattern, which is the base's line; the one test line
changed makes its test stricter, not weaker. I found nothing the fix broke, nothing added beyond
the findings, and no code made to pass a test.

New findings in the fix diff: none.

## Declined to judge

- Finding 6 of the review of the whole change (`guidelines/coding-shared-module.md` does not name
  `elements-common`): outside the task, not in the findings file, not fixed and not reviewed here.

## Checks I ran

All from the root of the reviewed worktree.

| Check | Command | Exit code | Result |
|---|---|---|---|
| The check of the foundation | `python -B elements/common/foundation_check.py` | 0 | `0 errors`, twelve `listed:` lines, as on the reviewed head |
| Tests of `elements/common` | `python -B gate/run_tests.py elements/common` | 0 | 283 tests, OK |
| Tests of `elements/part-map` | `python -B gate/run_tests.py elements/part-map` | 0 | 40 tests, OK |
| Tests of `agent-instructions` | `python -B gate/run_tests.py agent-instructions` | 0 | 52 tests, OK (linter, formatter and size among them) |
| The pattern against the base | `cmp` of the line `^QUOTED` of `git show 1b6fe1c1:elements/common/foundation_check.py` with that of `elements/common/foundation_text.py` | 0 | identical |
| Whitespace errors of the fix | `git diff --check e8b76178..9c7f9b71` | 0 | none |

Manual checks:

- The input of the spacing test, by running its two `replace` calls on the paragraph the test
  builds: the result differs from the original, holds 3 line breaks and 2 doubled spaces, and
  equals the original after normalisation.
- A search of every Markdown and Python file for the changed sentence of the part map ("reads the
  files and git for"): it stands in `foundations/part_map.md` alone, so nothing derived repeats it.

Not run: the product's full gate, which is the orchestrator's or CI's (WAY-160); `installation` and
`product-guidelines`, since the fix changes nothing either reads beyond prose and both passed on
the reviewed head.

## Reaches beyond the dispatch

None. I read what the handoff names and the diff of the range.

## Working copies

`.runs/review-fix/` held the outputs of the
runs and two one-line files for the byte comparison; no worktree was made. The directory is
removed, `git status --short` of the reviewed worktree is empty and `git worktree list` shows no
worktree of mine. Nothing is kept beside this report.

## Unread material

none — I read whole the handoff, `task-cycle/review/fix.md`, the findings file, the author's fix
report and the diff of the range; `task-cycle/review/SKILL.md` and the task document I read whole
in the review of the whole change and did not read again.

## Searches not found or unclear

- none

PASS a8753bb8

# Review of the fix of the finding of correction 2 — decision-length-check

Range `fa5d349e..a8753bb8`, one commit; `git rev-parse HEAD` gave
`a8753bb8e8e8fb3a8bc74450eea7ce3038394932`. The findings file holds one blocking finding. It is
fixed, and the fix diff brings no new Critical or Important finding; one new Minor note.

## The finding of the findings file

**1 (blocking) — fixed.** The three statements of item 2 now say one thing.

- WAY-05, `foundations/decisions.md:686-687`: an entry "may carry a further such paragraph for each
  part of its own question that it sets apart". "Each part" allows several paragraphs, "may" keeps
  them optional, and "such paragraph" keeps each within one to three sentences; the next clause
  holds every paragraph to 300 words and the whole to 600.
- The template, "Binding sentences", `elements/decisions/template.md:138-142`: "Each part of the
  entry's own question, the question of its heading, that the entry sets apart may also have a
  paragraph of its own after the first. Each such paragraph has one to three sentences and at most
  300 words, no limit stands on the number of paragraphs, and the binding sentences of one decision,
  all their paragraphs together, have at most 600 words (WAY-05)."
- The template, the entry form, `elements/decisions/template.md:31-36`: the block for a part of
  another question is again as it stood before correction 2, and a block of its own reads
  "optionally 1–3 binding sentences, at most 300 words, for a part of the question of the heading
  that the entry sets apart, one paragraph for each such part".

All three: several paragraphs allowed, one for each part the entry sets apart, each within the
limits of a paragraph, optional, no limit on their number, the 600 words keeping the length. That
is what item 2 of the remarks says with "each such paragraph", and none of them restores the way
not chosen under item 1, a limit on the number of paragraphs. The template no longer says more
than the entry. "That it sets apart" names the parts the entry itself divides out and carries no
number.

Contradiction: yes, as the finding was marked; the fix removes it.

The author does not contest the finding.

## What the handoff asks me to judge

- **WAY-05 within all three limits, by its words.** Counted with `binding` and `begins_sentence`
  of `elements/common/foundation_text.py` on the file at the head: paragraph 1 has 3 sentences and
  229 words, paragraph 2 has 1 sentence and 72 words, 301 words in all. The limits are 3, 300 and
  600. The check of the foundation gives no line for WAY-05, though this change alters it.
- **The reflow.** A comparison by words of `foundations/decisions.md` over the range shows two
  changes and no other: "a" became "each", and "question," became "question that it sets apart,".
  Every other changed line of the paragraph is layout.
- **The lines `decision:`.** Seventeen lines of `elements/common/test_foundation_check.py` name
  WAY-05, with two quotations. Each still begins a sentence of WAY-05 as it stands, by my own
  comparison and by the check of the foundation, which reads those lines and gives `0 errors`.
- **Anything broken or added beyond the finding.** Two files, 21 lines added and 17 removed, all in
  the three places the finding names. No Python file changed. WAY-19 and the two Minor findings of
  the review of correction 2 are untouched, as the handoff says they are to be.

## New in the fix diff

**Minor.** In the entry form the words "all the binding sentences together at most 600 words" now
stand inside the block that opens with "optionally"
(`elements/decisions/template.md:34-36`). A reader of the form alone could take the limit of the
whole as belonging to that optional paragraph. The section "Binding sentences" below it states the
limit for every decision, so nobody who reads the template is led wrong; a line of its own after
the three blocks would say it more plainly. It blocks nothing.

## Declined to judge

- Findings 2 and 3 of the review of correction 2 (the name WAY-19 gives a part, and "for this
  report alone" in `agent-instructions/README.md`): not in the findings file, not fixed, and both
  stand as they were.

## Checks I ran

All from the root of the reviewed worktree.

| Check | Command | Exit code | Result |
|---|---|---|---|
| The check of the foundation | `python -B elements/common/foundation_check.py` | 0 | `0 errors`, thirteen `listed:` lines as on the reviewed head, none for WAY-05 |
| Tests of `elements/common` | `python -B gate/run_tests.py elements/common` | 0 | 289 tests, OK |
| The words the fix changed in the log | `git diff --word-diff=porcelain fa5d349e a8753bb8 -- foundations/decisions.md` | 0 | the two changes named above |
| Whitespace errors of the fix | `git diff --check fa5d349e..a8753bb8` | 0 | none |

Manual checks:

- A script of my own that reads `foundations/decisions.md` with the readers of
  `foundation_text.py`: the counts of WAY-05 above, and for each of the two quotations of the lines
  `decision: WAY-05` that it begins a sentence of the entry (both true).
- The three statements read side by side against item 2 of the remarks and against the two ways
  not chosen under item 1.

Not run: the product's full gate (WAY-160); `elements/part-map`, `agent-instructions`,
`installation` and `product-guidelines`, since the fix changes no Python file and nothing those
tests read but the two Markdown files that the check of the foundation and `elements/common` cover.

## Reaches beyond the dispatch

None.

## Working copies

`.runs/review-correction-2-fix/` held the output
of the test run, the output of the check and one script for the counts; no worktree was made. The
directory is removed, `git status --short` of the reviewed worktree is empty and
`git worktree list` shows no worktree of mine. Nothing is kept beside this report.
`.runs/fc_final.txt` is not mine and stays.

## Unread material

none — I read whole the handoff, the findings file, the author's report of the fix and the diff of
the range. The remarks, `task-cycle/review/SKILL.md` and `task-cycle/review/fix.md` I read whole in
the earlier reviews of this cycle and did not read again.

## Searches not found or unclear

- none

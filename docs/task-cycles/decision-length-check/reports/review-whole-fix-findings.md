# Findings of the review of the whole change — for the fix

Reviewer's report: `reports/review-whole-report.md`, first line `FAIL e8b76178`. Cut word for word from it: the blocking finding first, then the Minor findings within the task (WAY-161). Finding 6 of the report is outside the task's scope and is not fixed.

## Blocking

**1. Two summaries of the new report restate the second paragraph of WAY-05 differently.**
Slice: none.

- `README.md:86-88` reads: "It reports as an error each decision that a change adds or whose
  binding sentences it alters and that nothing holds, and each paragraph of such a decision's
  binding sentences over three sentences or 300 words". "Such a decision" points back to the whole
  description before it, "that a change adds or whose binding sentences it alters and that nothing
  holds". Read that way, the sentence says a paragraph over a limit is an error only in a decision
  that nothing holds, and the next clause, "the other decisions with a paragraph over those
  limits", then puts an added decision that is held among the listed ones. At best the sentence
  can be read both ways.
- The same sentence, and `agent-instructions/README.md:14-17` ("the paragraphs of binding sentences
  over three sentences or 300 words in a decision a change adds or whose binding sentences it
  alters"), leave out that a different division into paragraphs counts as an alteration. In both
  files the phrase "whose binding sentences it alters" also stands for the check of what holds a
  decision, where a different division does not count, so a reader takes one meaning for both.

What WAY-05 says, as the change writes it (`foundations/decisions.md:697-700`): "in a decision that
a change adds or whose binding sentences it alters, a different division of them into paragraphs
included". What the code does: a held decision over a limit is an error
(`test_a_new_decision_with_four_sentences_in_a_paragraph_is_an_error` uses an entry held by an
invariant; my probe P3 added a fourth sentence to WAY-05, which a pair and tests hold, and got exit
1), and a new division alone is an error (`test_a_different_division_into_paragraphs_counts_as_a_change`;
my probe P6 joined the two paragraphs of WAY-18 with no word changed and got exit 1).

Why it matters: both files are changed by this change and repeat an entry the change writes, one
with a qualification the entry does not have and both without one it has. By WAY-263 that is
Important. The answer "a different division counts" is also one the human gave to a question of
its own in the task. The cost of the fix is one sentence in each file.

Contradiction: yes — WAY-05, second paragraph (row 2 of *Settlements to record*, and the answer
under "Czy inny podział zdań wiążących na akapity…").

## Minor, within the task

**2. The row "binding sentences" of the template's table narrows what the script counts.**
`elements/decisions/template.md:121` says `foundation_check.py` "counts the sentences and the words
of each of their paragraphs in a decision a change adds or alters (WAY-05)". The script counts them
in every decision and lists the others, and the row does not name the division. I grade it Minor
and not as finding 1 because the full account, with the list and the division, stands in the same
file fifteen lines below (`template.md:136-141`), so a reader of the template is not led wrong.

**3. One replacement in a new test changes nothing.**
`elements/common/test_foundation_check.py:2191`, in
`test_a_decision_over_a_limit_whose_spacing_alone_changed_is_listed`:
`long.replace(" ", "  ", 2).replace("e. ", "e.\n")`. The paragraph is
`word well-known, end. word well-known, end. …`; it holds no `e. ` (the sentences end in `d. `), so
the second `replace` matches nothing and the test checks two doubled spaces only, never a line
break. Checked by running the two expressions: equal strings, no line break, zero occurrences. The
test still passes for the right reason, and the shared normalisation of a line break is held by the
older `test_decision_with_only_its_spacing_changed_is_listed`; the line reads as if it tested more
than it does. `"d. "` in place of `"e. "` makes it do what it says.

**4. The move changed how one pattern is written.**
`elements/common/foundation_text.py:17` writes `QUOTED` with the three typographic quotation marks
as characters, where the base wrote them as escapes
(`r"\"[^\"]*\"|[\u201c\u201e][^\u201d]*\u201d"`, `foundation_check.py:169` at `1b6fe1c1`). The
pattern matches the same text: I read the code points of the new pattern as U+201C, U+201E, U+201D,
U+201D, and the older test of the three kinds of marks passes. But the commit message of `0f738707`
and the author's report say the patterns "move unchanged", and it is the one line of the move that
did not (a sorted comparison of the lines removed with the lines of the new module shows no other
difference). The opening and closing marks are hard to tell apart on a screen, which the escapes
avoided.

**5. The part map names one module of the script and the change adds a second.**
`foundations/part_map.md:67-70` says the part `elements-common` answers for "the script that checks
a whole foundation's identifiers, references and assignment of files to parts, … with the module
that reads the files and git for it". After the change the script also has
`elements/common/foundation_text.py`. The sentence is still true and the file is claimed by
`elements/common/**`, so nothing breaks; the return step of an earlier cycle (`4066ae5d`) added the
first module to this sentence, and the return step of this cycle is the place to add the second.

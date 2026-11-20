FAIL fa5d349e

# Review of correction 2 — decision-length-check

Range `b0bba24d..fa5d349e`, three commits (`02bf399d`, `63436978`, `fa5d349e`);
`git rev-parse HEAD` gave `fa5d349e2150ecbc19202e1b595759f517b788e0`. The remarks of
`reports/correction-2-remarks.md` stand in place of a findings file.

One blocking finding, two Minor findings within the correction, none outside it.

The check and its tests are right: the limit of 600 words works as item 1 asks, on the tests and
on the real foundation. What blocks is the wording of item 2: WAY-05 and the template give the
further paragraph for a part of the entry's own question in three ways that do not say the same.

## The remarks

**Item 1, a limit for the whole entry — made.**

- The check: `check_length` adds the words of all the paragraphs and reports more than 600 as an
  error in a decision the change adds or whose paragraphs differ from the base, and as a listed
  line in any other. The message names the decision and the measure with its value
  (`its binding sentences have 601 words in all (at most 600)`).
- WAY-05 carries the limit in both paragraphs of its binding sentences
  (`foundations/decisions.md:684-703`), its `tests:` clause names it, *Rationale* gives the reason
  of the remark and *Rejected* holds both ways not chosen with their reasons.
- The template gives it in the entry form (`elements/decisions/template.md:31-33`), in "Binding
  sentences" (`:133-144`) and in the row of the table of readers (`:122`). The description at the
  head of the script, `README.md:88-93` and `agent-instructions/README.md:14-18` name the new
  report in the places of the earlier one.
- Six tests hold it, each with a line `decision:` that quotes the start of a sentence of WAY-05 as
  it stands; the script accepts each.
- WAY-05 stays within all three limits: paragraph 1 has 3 sentences and 225 words, paragraph 2 has
  1 sentence and 72 words, 297 words in all, counted with the script's own readers; the check gives
  no line for it though this change alters it.
- The entries over a limit today are unchanged. A comparison by words of
  `foundations/decisions.md` over the range shows changed words in WAY-05 alone.

**Item 2, a paragraph for a part of the entry's own question — made in WAY-05 and in the
template's "Binding sentences", with finding 1 on how the three statements of it differ.** No
entry and no other file says the opposite (see "WAY-19 and the other texts" below). No way not
chosen of the remarks is restored, save what finding 1 says of the number of paragraphs.

## Findings

### Important

**1. The three statements of item 2 do not say the same thing.**

- WAY-05, `foundations/decisions.md:686-687`: an entry "may carry a further such paragraph for a
  part of its own question". On its words that is one further paragraph. The clause before it says
  "one paragraph … for each part of another question", so the change from "for each part" to "a
  further … for a part" reads as meant.
- The template, "Binding sentences", `elements/decisions/template.md:135-137`: "A part of the
  entry's own question, the question of its heading, may also have a paragraph of its own after the
  first." Any part may have one, so several paragraphs.
- The template, the entry form, `elements/decisions/template.md:31-32`: "for a part of another
  question this entry answers or for a part of the question of the heading, one paragraph for each
  such part". One paragraph for each part, several, and with no "may": it gives a part of the
  heading's question the same rule as a part of another question.

What the remark says: "A further paragraph may also carry a part of the entry's own question … each
such paragraph stands within the limits of a paragraph". "Each such paragraph" allows several, and
WAY-05 does not carry those words.

Why it matters. The entry is what binds, and its words are the narrowest of the three. The two
tasks that follow this request divide entries at parts of their own question: WAY-344, with 8
sentences and 743 words, needs at least three paragraphs to meet the limit of three sentences, so
two further ones. A reviewer of that task who reads WAY-05 as it stands can object to the second,
which is the state item 2 was to end ("the rule and the entries then say different things and a
reviewer can rightly object"). Read that way, WAY-05 is also a limit on the number of paragraphs
for an entry's own question, a kind of limit the human did not choose under item 1. And the
template, a file of the same change, says more than the entry it restates, which WAY-263 grades
Important.

The sentence of WAY-05 can be read the other way too, as "for any part, a further paragraph"; I
block because the entry form beside it is plainly broader and the next task rests on the
difference. The fix is one wording in the three places: that an entry may carry a further such
paragraph for each part of its own question it sets apart, and an entry form that keeps "may" for
that kind.

Contradiction: yes — item 2 of the remarks ("each such paragraph"), the way not chosen under
item 1 ("a limit on the number of paragraphs of an entry"), and WAY-05 as the correction writes it,
which the template's entry form restates more broadly.

### Minor, within the correction

**2. WAY-19 does not say the opposite of item 2, but its name for a part now reads as the other
kind.** This is the question the handoff asks me to judge.

- WAY-19 (`foundations/decisions.md:879-885`) says "a part of the question an existing entry
  answers is a sentence of that entry where it cannot change without changing that entry". It says
  where such a part stands: in that entry, not under a number of its own. It says nothing of
  paragraphs and does not forbid one. It is not the opposite of item 2, and I agree with the author
  that item 2 does not call for a change of WAY-19.
- What the correction does change is that WAY-05 now has two kinds with two rules: "a part of
  another question that it answers" must have a paragraph of its own, and "a part of its own
  question" may have one. WAY-19's words, "a part of the question an existing entry answers" (in
  its examples "a part of a question that WAY-14 answers"), are in plain English the second kind.
  The template cites WAY-19 at the first kind (`template.md:134-135`: "A part of another question
  that the entry answers, which cannot change without the entry (WAY-19), has its own paragraph").
  So for a rule written into an entry under WAY-19, a reader of WAY-05 and WAY-19 cannot tell
  whether its own paragraph is required or allowed.
- The sentence a reader can read wrongly: `template.md:205-207`, "A part of the question an
  existing entry answers is a sentence of that entry, in a paragraph of its own as "Binding
  sentences" gives". It uses WAY-19's name, says "in a paragraph of its own", and points to a
  section that now holds two rules under two other names. The author's change of this bullet, from
  a bare pointer to "as … gives", is sound as far as it goes, and it is the one text beside WAY-05
  that the request should name as changed for item 2.

Why Minor: both readings allow the paragraph, the difference is only "must" against "may", no check
rests on it, and the template's "Binding sentences" does tell the two kinds apart for a reader who
reads it whole. Before this correction the two names stood for one thing with one rule, so nothing
followed from them. Two ways to end it: the fix of finding 1 names the first kind in WAY-05 by
WAY-19's test, that the part cannot change without the entry; or the request puts the wording of
WAY-19 before the human, since the remarks give leave to change it only where it says the opposite.

**3. "For this report alone" now follows two reports.**
`agent-instructions/README.md:14-18`: "it reports the decisions that nothing holds, the paragraphs
of binding sentences over three sentences or 300 words and binding sentences over 600 words in all
their paragraphs, in a decision a change adds or whose binding sentences it alters, a different
division into paragraphs counting as an alteration for this report alone". Before the correction
"this report" was the one report of length. Now two stand before it, and a reader can take "this
report" as the last alone, the one of 600 words, which would leave the division out of the report
of a paragraph. The likelier reading takes the pair joined by "and" together, which is right; "for
these two reports alone" removes the doubt.

## WAY-19 and the other texts — does any still say the opposite of item 2

I read WAY-19 whole, WAY-05 whole as the head holds it, and every passage of the template that
speaks of a part of a question (`template.md:29-33`, `:133-144`, `:203-209`). I searched every
Markdown and Python file for "part of another question", "part of the question", "own question",
"paragraph of its own", "own paragraph", "paragraph for each", "question of the heading", "another
question" and "two independent questions". Beside WAY-05, WAY-19 and the template, the hits are
`elements/decisions/skill/decide_entry.md:12-13` (two independent questions make two entries),
`foundation-review/weak_points.md:59-60` (a part of one question under a number of its own goes
into the entry that answers the question) and a row of the list of withdrawn numbers; none speaks
of paragraphs.

After the change no entry and no file says that a part of an entry's own question may not have a
paragraph of its own, or that a further paragraph is for a part of another question alone. The pair
of examples of WAY-05 agrees with item 2: its complying entry gives a part of its own question a
second paragraph, and its violating one folds a part of another question into the first.

## The correction's diff

- **The code.** `check_length` (26 lines) builds the lines of the paragraphs over a limit, adds one
  for the whole where its words pass 600, and writes each as an error or a listed line by the one
  test of change that the limit of a paragraph already used. A word is counted as for a paragraph.
  `foundation_check.py` goes from 1111 to 1115 lines, under the 1200 of WAY-385. I found no branch
  or value made for an input of a test.
- **The tests.** Six, with values written out (600, 601, 640, "3 errors") that come from WAY-05 by
  the line `decision:`. Each of fourteen mutations of the changed function was caught (below).
- **The descriptions.** The head of the script, `README.md` and the template's row and second
  bullet of "Binding sentences" say what the code does. The sentence of `agent-instructions/README.md`
  is finding 3.
- **WAY-05 beyond the two items.** Its lines were reflowed to 100 columns; the comparison by words
  shows no word changed but those of the two items. *Rejected* holds the four ways not chosen of
  the remarks with their reasons and leaves out the count the remark quotes ("about half of the
  entries"), as WAY-05 asks of prose. The entry names no date or condition of a review (WAY-24).
- **The author's own-work check.** It names the right weak point, that WAY-05 itself stays within
  the three limits, and its check would catch that unmet; I counted the same figures.

## Checks I ran

All from the root of the reviewed worktree unless a directory is named.

| Check | Command | Exit code | Result |
|---|---|---|---|
| The check of the foundation | `python -B elements/common/foundation_check.py` | 0 | `0 errors`, thirteen `listed:` lines: the twelve of before and a second for WAY-344, "743 words in all (at most 600)"; none for WAY-05 |
| Tests of `elements/common` | `python -B gate/run_tests.py elements/common` | 0 | 289 tests, OK |
| Tests of `elements/part-map` | `python -B gate/run_tests.py elements/part-map` | 0 | 40 tests, OK |
| Tests of `agent-instructions` | `python -B gate/run_tests.py agent-instructions` | 0 | 52 tests, OK (linter, formatter and size among them) |
| Sizes of the changed files | `python -B task-cycle/change_file_sizes.py b0bba24d fa5d349e` | 0 | `foundation_check.py` 1111 to 1115, `test_foundation_check.py` 2452 to 2519 |
| Whitespace errors of the range | `git diff --check b0bba24d..fa5d349e` | 0 | none |
| The words the range changed in the log | `git diff --word-diff=porcelain b0bba24d fa5d349e -- foundations/decisions.md` | 0 | WAY-05 alone, the words of the two items |

Manual checks, in a worktree of `fa5d349e` under `.runs/review-correction-2/`, never in the
reviewed worktree:

- **Fourteen mutations of `check_length` and its limit**, each run against the eighteen tests of
  the limits (`python -B -m unittest test_foundation_check -k …` from `elements/common/`), each
  ending with exit code 1: `>=` for `>` on the whole (1 test fails); a limit of 601 (4) and of 599
  (1); the longest paragraph in place of the sum (5); the first paragraph alone (5); the whole
  dropped where a paragraph is over (1); the whole never reported (5); the joined text compared in
  place of the paragraphs (1); always an error (5); never an error (11); the error at no line (5);
  the whole listed and never an error (4); words counted as runs of letters (6); the paragraphs no
  longer reported (11). Output kept in `reports/review-correction-2-mutations.txt`.
- **Probes on the real foundation**, each an edit of `foundations/decisions.md` in the copy, then
  the script; output kept in `reports/review-correction-2-probes.txt`:
  - P0, nothing changed: exit 0; WAY-344, unaltered, is listed twice, for its paragraph and for
    743 words in all.
  - P1, WAY-344 altered by one word: exit 1, two errors, the paragraph and "744 words in all".
  - P2, the rationale of WAY-344 alone changed: exit 0, both lines still listed.
  - P3, WAY-344 divided in three with no word changed, a different division alone: exit 1, an
    error for "743 words in all" and one for its third paragraph.
  - P4, a decision added with 601 words in three paragraphs, each within its own limits: exit 1,
    one error, "601 words in all", no paragraph named.
  - P5, the same with 600 words: exit 0.
  - P6, a decision added with four paragraphs of 300 words: exit 1, one error, "1200 words in
    all" — the case of the remark's "Why", which the limit of a paragraph alone let through.
- **WAY-05 counted** with `binding` and `begins_sentence` of `foundation_text.py`: (3, 225) and
  (1, 72), 297 in all.

Not run: the product's full gate (WAY-160); `installation` and `product-guidelines`, which read
nothing the correction changes beyond prose; the test of sizes at the base in a worktree of its
own, since the run of `agent-instructions` holds it at the head and the file stands 85 lines under
its threshold.

## Reaches beyond the dispatch

- `foundations/decisions.md`: WAY-99 in part and the binding sentences of WAY-114, for the grade of
  finding 2 and for how the two settlements reach the human.
- `elements/decisions/skill/decide_entry.md` lines 8-24 and `foundation-review/weak_points.md` lines
  52-64: two hits of the search for a text that says the opposite of item 2.

## Working copies

All stood under `.runs/review-correction-2/` and
all are removed; `git worktree list` shows no worktree of mine and `git status --short` of the
reviewed worktree is empty.

- `head\` — a worktree of `fa5d349e`, in which the mutations and the probes ran, each restoring the
  file it changed; removed with `git worktree remove --force`, then `git worktree prune`.
- The diff of the range, the index of my selection, two scripts and the outputs of the runs:
  removed with the directory.
- Kept beside this report: `reports/review-correction-2-probes.txt` and
  `reports/review-correction-2-mutations.txt`.
- `.runs/fc_final.txt` is not mine; it stood there before and I left it.

## Unread material

Of the 111 decisions of the index of my selection for this correction (25 listed in full, 86 by
heading alone; the parts `decisions`, `elements-common`, `agent-instructions` and `repository`) I
opened 2 whole in this review: WAY-05 as the head holds it and WAY-19. Twelve more of the index I
read whole in the review of the whole change, and the range since then changes none of them:
WAY-02, WAY-04, WAY-07, WAY-12, WAY-22, WAY-24, WAY-33, WAY-385, WAY-386, WAY-392, WAY-393 and
WAY-394. I read the binding sentences of the 25 listed in full and ran through the 86 headings.

- WAY-99 and WAY-114: read in part (binding sentences, and for WAY-99 its *Verification* and the
  start of its *Rationale*).
- WAY-18 and WAY-134: binding sentences only; neither speaks of the length of an entry or of what
  a paragraph carries.
- Guideline files: `guidelines/coding.md`, `guidelines/coding-check.md` and `guidelines/testing.md`
  I read whole in the review of the whole change and did not read again; nothing in the range
  changes them.
- `elements/common/test_foundation_check.py`: the six new tests and the helpers they call, read in
  the diff and in the file; the rest not read again.
- `elements/common/foundation_check.py`: the changed description and `check_length` at the head;
  the rest read whole in the review of the whole change.
- `reports/review-correction-1-report.md`: not read, as the handoff says.

Read whole: the handoff, the remarks, the author's report, `task-cycle/review/fix.md`, the diff of
the range, and the template's passages named above.

## Searches not found or unclear

- The handoff calls the finding on the wording of WAY-19 in `reports/review-correction-1-report.md` my own earlier finding and tells me not to read that report again. That review is not in what I hold: I made the review of the whole change and the review of its fix, and no review of correction 1. I judged WAY-19 afresh from the entries and the template (finding 2), so I cannot say whether it agrees with what that report said.
- The remarks file gives as its source a comment on the request "passed on by the day's adviser as a change of scope from the human". I reviewed the correction against the remarks as the handoff gives them and could not check who wrote the comment or the two answers it quotes.

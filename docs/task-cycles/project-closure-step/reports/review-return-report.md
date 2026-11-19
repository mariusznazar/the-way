PASS e9a7a81f68b196e4ede1d4e04764b6d9828b68b3

# Review of the commits of the return step — task `project-closure-step`

Range: from `d4cfe7105964f38e11db4f4bd6db91136bafe8f7` to `e9a7a81f68b196e4ede1d4e04764b6d9828b68b3`
(`git rev-parse HEAD` gives it), one commit, `e9a7a81f`, one file, `foundations/decisions.md`, five lines
changed in three entries (WAY-411, WAY-412, WAY-414). Paths below are relative to the root of the worktree
`the task's worktree`.

Result: no Critical and no Important finding. Three Minor notes, two in the diff of the range and one
outside it. The commit does what the author's report says, and the two notes of the review of the fix that
it answers are both closed.

## What the commit changes, compared with the step's file and the task

| Entry | Change | Verdict |
|---|---|---|
| WAY-414, binding sentence (lines 5352–5355) | "by the question the heading of a decision holds or by the identifier or term of any other entry, which the plan keeps word for word" becomes "by the question the heading of a new decision holds, by the number of the current decision it changes, or by the identifier or term of any other entry, as the plan keeps the heading word for word" | agrees with `project-level/lead/skill/closure.md` lines 43–46 in both directions: the file gives three keys ("for a decision `(new) — <question>`, the decision headings that hold the same question; for a change of a current decision, its number; for any other entry, its identifier or term") and the sentence now gives the same three. "As the plan keeps the heading word for word" agrees with `project-level/plan/template.md` lines 130–131 ("under its heading as the definition's "Projected foundation changes" gives it after `#### `, word for word") and with the forms of heading in `project-level/definition_template.md` lines 328–332. Note 1 of the review of the fix is closed. |
| WAY-411, violating example (line 5271) | "moves the tasks the human withdrew" becomes "moves the dropped tasks" | agrees with the one word of `closure.md` line 8 ("A dropped task is one whose row reads `dropped — approved by human`"). Half of note 2 of the review of the fix is closed. |
| WAY-412, *Rejected* (line 5321) | "only two places, a task of its own or dropped" becomes "a task of its own or given up for good" | agrees with the name of the third place in `closure.md` line 80 and in the entry's own binding sentence (line 5289), and with the way not chosen the task keeps under the question "Dokąd może pójść zadanie wycofane przy zamknięciu…" ("tylko dwa miejsca: samodzielne zadanie albo porzucone"), so the *Rejected* still holds only what the row's source keeps (WAY-134). The other half of note 2 is closed. |

The rest of WAY-414, read whole at the head against `closure.md` section 2: the four results of the file
(absent at the commit; found, a part included, that another task wrote; stands under the identifier or term
without the change; a doubtful hit put to the human in the preview before anything is written) are the
results the entry names, and the entry names none the file lacks. The first paragraph still holds three
binding sentences, as the template of a decision allows. The pair of examples already carried the case of
the number (line 5368), as the author's report says. No line `decision:` of a test quotes WAY-411 to
WAY-415 (the head holds these numbers in `foundations/decisions.md` only), so the changed sentence breaks
no quotation.

Against rows 1, 2 and 5 of the task's *Settlements to record*: rows 1 and 2 are untouched in meaning by the
two changes of a word. Row 5 gives the search "po pytaniu wpisu"; the key of the number for a change of a
current decision goes beyond the words of the row and serves what the row is for, a key the plan keeps word
for word in the heading and not the wording of a sentence. I judge it no contradiction with the row. It is
part of the passage of WAY-414 the cycle marks as its own, and it has to reach the human in the wording of
this head (see the question to the orchestrator below).

## Findings

### Critical

none

### Important

none

### Minor

1. In the diff, within the task — `foundations/decisions.md` lines 5321 and 5355. The two edited lines were
   left unwrapped: line 5321 is 109 characters and line 5355 is 158, while the lines around them in the
   three entries end at or under 100. Nothing reads wrongly and the rendered text is the same; the file
   holds other long lines, so this is form only. Evidence: the lengths measured on the head (check 8).
2. In the diff, within the task — `foundations/decisions.md` lines 5353–5354, "by the number of the current
   decision it changes". The word "it" has two candidates: the projected entry, which is meant, and "a new
   decision", the nearest noun, which gives the reading "the current decision a new decision changes" —
   an entry under `(new) — <question>` that narrows a current decision. The pair of examples (line 5368,
   "for a change to a current decision whose number stands without the change") and `closure.md` lines
   44–46 settle the reading, so a reader who has both is not misled; "by the number of the current decision
   the entry changes" would close it. I cite no sentence a reader acts on wrongly, so it stays Minor.
3. Outside the diff of this range, within the task — `project-level/lead/skill/closure.md` and
   `project-level/lead/skill/SKILL.md` name none of WAY-411 to WAY-415. The file cites WAY-126 (line 52),
   WAY-145 (line 99) and WAY-118 (line 147), and states the five choices the change wrote decisions for —
   the three places (section 3), the write only after the acceptance (section 6), the search at a commit
   (section 2), the document `refining` with `source only` (section 3) — without the number of any.
   WAY-293, second paragraph: a rule of one skill of the-way "is an entry of the log only where it carries
   a choice with a real cost … and the skill or template then names that decision", and its violating
   example reads "a skill states a choice with a real cost and names no decision". The entries and the file
   agree in content, the behaviour of the closing is the same with or without the numbers, and a later
   change of the file finds the entries by the scope `project-level`, so I grade it Minor: what is lost is
   the pointer from the sentence of the skill to the decision that keeps its rejected ways. Adding the five
   numbers at the sentences of `closure.md` that state the choices would close it. This file is unchanged in
   the range; I did not read the review of the whole change, so I cannot tell whether it was raised there.
   Evidence: check 6.

## Declined to judge

- The title of WAY-146, "What checks a project plan before it is handed over?", beside a check that now
  also runs on a closed plan: the task names the entry only for one sentence, the commit does not touch it,
  and the author's report gives that reason.
- Notes 3 and 4 of the review of the fix (where the goal, the questions and the entries travel when the
  human answers that the existing document stands; line 15 of `project-level/task_line.md`): the author
  judged them review findings and no mismatch of an entry with the code, and corrected neither. Both lie
  outside this range and were graded Minor by that review; I did not grade them again.

## The author's report, claim by claim

- "One commit, `foundations/decisions.md` only": true (`git log`, `git diff --stat` of the range).
- The three corrections, word for word: each is in the diff as quoted.
- "`python -B elements/common/foundation_check.py`: exit 0, `0 errors`": reproduced.
- "No test or script changed in this step": true.
- "Matched, no change" for the other entries: I checked WAY-413 and WAY-415 whole against `closure.md`
  sections 3, 4 and 6 and found them in agreement, and the first sentence of WAY-142 against the three
  states. The other entries of that list (WAY-145, WAY-146, WAY-118, WAY-153, WAY-107, WAY-154, the two
  invariants, the part map, the surface) I did not open again: the commit does not touch them and the
  earlier reviews covered them.
- The table of the choices that bind after the merge (Q1 to Q3, all out of the log): the commit writes
  nothing for them, which agrees with the table. Whether Q2 is before the human is the request's matter.

## Question to the orchestrator (no answer needed for the result)

The passage of WAY-414 that the record and the request give as the cycle's own was quoted from the entry at
`d4cfe710`. This commit changed that sentence. The quotation has to be taken again from the head, word for
word: "by the question the heading of a new decision holds, by the number of the current decision it
changes, or by the identifier or term of any other entry, as the plan keeps the heading word for word, and
compares the text of what it finds with the projected change". I recommend replacing the quotation in the
record and in the request before the request is shown. The record is not mine to read, so I did not check
what it holds now.

## Checks

| # | Check | Command or method | Result |
|---|---|---|---|
| 1 | Head of the range | `git rev-parse HEAD` | exit 0, `e9a7a81f68b196e4ede1d4e04764b6d9828b68b3` |
| 2 | Commits and files of the range | `git log --stat d4cfe7105964f38e11db4f4bd6db91136bafe8f7..e9a7a81f` | exit 0: one commit, one file, 5 insertions, 5 deletions |
| 3 | Whitespace of the diff | `git diff --check d4cfe7105964f38e11db4f4bd6db91136bafe8f7..e9a7a81f` | exit 0 |
| 4 | Sizes of the changed files | `python -B task-cycle/change_file_sizes.py d4cfe7105964f38e11db4f4bd6db91136bafe8f7 e9a7a81f` | exit 0: `foundations/decisions.md` 11586 → 11586 |
| 5 | Foundation check | `python -B elements/common/foundation_check.py` | exit 0, `0 errors` |
| 6 | References to the five decisions outside the log | `git grep -n -E "WAY-41[1-5]" e9a7a81f -- . ':!foundations/decisions.md'` and, as the positive control, `git grep -c -E "WAY-41[1-5]" e9a7a81f -- foundations/decisions.md` | the first printed no line (its exit code was not captured, the output went through a pipe); the second: exit 0, 9 lines in the log |
| 7 | Tests of one directory | `python -B gate/run_tests.py elements/common` | exit 0, 271 tests, OK |
| 8 | Length of the edited lines | read the head's `foundations/decisions.md` as UTF-8 and counted characters of each line | line 5271: 82, line 5321: 109, line 5355: 158 |
| 9 | Leftovers of the earlier words | searched `foundations/`, `project-level/` and the two entry points of the lead skill for `withdr`, `dropped for good` and `or dropped` | no hit in WAY-411 to WAY-415 or in the files of the closing but the state `dropped` itself |
| 10 | The reviewed worktree unchanged | `git status --short` after the checks | exit 0, no line |

Not run: the whole gate, by the handoff. No check needed a changed file, so no worktree of the head was
made.

## Changed files of the range (lines before → after)

`foundations/decisions.md` 11586 → 11586. I changed no file of the worktree.

## Reaches beyond the handoff

- `project-level/plan/template.md` lines 126–135 and `project-level/definition_template.md` lines 327–332,
  found by a search for `Projected entries` and `(new)`: to check that the plan keeps the heading of a
  projected entry word for word and which forms a heading takes, for the edited sentence of WAY-414.
- `elements/decisions/template.md`, whole: the form of a decision, for the count of binding sentences and
  the rule of *Rejected* written from a row of the task.
- WAY-126 (lines 3753–3793, to its *Origin*), which WAY-414 cites; WAY-142 (lines 4955–5004), for the
  author's claim on its first sentence; WAY-293 (lines 1046–1080, to the start of its *Rationale*), for
  Minor 3; WAY-413 and WAY-415 whole, beside the three edited entries.
- `task-cycle/skill/return_step.md`, whole: what the return step has to compare and correct, to judge the
  author's report.
- `project-level/lead/skill/SKILL.md` lines 60–95: step 1, for the complying example of WAY-411.
- `gate/run_tests.py` lines 1–40: how the runner takes one directory.

## Working copies

Under `.runs/review-return/`: two files of the diff of the range and the log of the test run. All deleted
and the directory removed. No remainder.

## Unread material

Of the dispatch: none. The handoff, `task-cycle/review/SKILL.md`, the task, the author's report of the
return step, the report of the review of the fix, `closure.md` at the head and the entries WAY-411, WAY-412
and WAY-414 with their *Rejected* were read whole, and the diff whole.

Of my own reaches, not read whole: the *Rationale* and *Rejected* of WAY-126 and of WAY-293, and the
*Rejected* of WAY-142 past its first lines. No guideline file was read: the commit holds no code and no
test, and no finding needed one. `project-level/technology/reserved_choices.md` was not read: the commit
settles no technology.

## Searches not found or unclear

- A rule for the width of a line in a foundation file: searched the `.md` files of `guidelines/`,
  `agent-instructions/`, `elements/common/` and `elements/decisions/` for `100 characters`, `100 columns`,
  `line length`, `wrap at` and `characters wide`, no hit. I did not read `elements/common/rules.md` whole,
  so this is unclear and no proof that none stands; Minor 1 rests on the lines around the edit only.
- Whether the review of the whole change raised the missing numbers of Minor 3: not in the files I may
  read.
- What the record holds as the cycle's passage of WAY-414: the record is not mine to read (the question
  above).

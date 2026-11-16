FAIL 83aa64dbebfcd6f0077a0cd64c204ff494d0cd5d

# Review of the return step — task `walkthrough-in-running-product`

Range `cdbde3d2..83aa64db`, one commit `83aa64db` ("Return step: bring the request template and the
log in line with the walk decisions"); `git rev-parse HEAD` = `83aa64dbebfcd6f0077a0cd64c204ff494d0cd5d`,
as given. Changed files: `foundations/decisions.md` (+24 −23), `task-cycle/skill/request_template.md`
(+5 −5); 30 insertions, 27 deletions in all.

Counts: 1 blocking (Important), 2 Minor, 0 out of scope.

## Findings

### Important

**1. The lower part of the request template still gives the walk's out-of-scope errors as the author's alone, while kind 8, corrected by this commit, and WAY-408 cover the executor of a slice as well.**

Place: `task-cycle/skill/request_template.md:535-536`, the paragraph **Findings outside the task's scope.**:

> each error outside the task's scope that an author's walk through the running product reported,
> with the author's words and where it showed (WAY-408);

This commit changed the sibling sentence of kind 8 (`request_template.md:261-264`) from "its author
reported" to "its author or executor reported", for the reason the author's report gives as its
point 2: "WAY-408 binds the executor of a slice as well". Kind 8 then sends each such error to
"*Findings outside the task's scope* below" — and the paragraph it sends it to still reads "an
author's walk" and "the author's words". The return step's job (`task-cycle/skill/return_step.md`,
first paragraph) is to correct whatever no longer matches the entries the change writes; it found
this mismatch, corrected it in one of the two places that restate the same sentence of WAY-408, and
left the other. The template now says two different things about the same item, and the lower part
restates WAY-408 without its qualification "or the executor of a slice" (WAY-408's first sentence:
"The author of a change or the executor of a slice corrects each case…"; its second paragraph: "An
error outside the task's scope that the walk finds is reported and not corrected, and the description
of the request puts each such error before the human"). WAY-406 makes every executor of a slice that
alters behaviour a user sees walk through its slice (task, row 3 of *Settlements to record*).

Why it matters: the orchestrator of a change made from a plan, writing the lower part, reads that
the list holds errors an *author's* walk reported, with *the author's* words; an error the executor
of slice 2 reported can be left out of the list, or attributed to an author that a planned change
does not have. WAY-263 grades a changed file that restates an entry the change writes "without a
qualification" as Important.

Evidence: the diff of the range (kind 8 changed, lines 533-537 untouched); `git log -L533,537` over
`9cffc9ba..83aa64db` shows the paragraph last changed in `cdbde3d2`, before the return step.

Fix: "each error outside the task's scope that the walk of an author or of the executor of a slice
reported, with its words and where it showed (WAY-408)" or equivalent.

Contradiction: yes — WAY-408 (the error of the walk of "the author of a change or the executor of a
slice" goes before the human), and row 3 of the task's *Settlements to record*.

### Minor

**2. `task-cycle/skill/request_template.md:186-187` names the author's walk alone.** "leave logs and
outputs in the reports, the cases and verdicts of the author's walk through the running product among
them". This is the paragraph on where the traces of a check lie, not a restatement of WAY-408, and a
reader would still leave an executor's cases in its report; but it is the same author-only wording
that the return step corrected in kind 8, and a fix of finding 1 would naturally take it too
("the author's or the executor's walk"). Minor: no sentence that a reader would act on wrongly.

**3. Two lines over the template's width introduced by the commit.** `request_template.md:251`
(160 characters) and `request_template.md:264` (113 characters). Before the commit no prose line of
kind 8 passed the width (a `awk 'length>100'` over the file at `cdbde3d2` and at `83aa64db` shows
these two lines as the only new ones). The same commit re-flowed the log for its width, so the
template's kind 8 is left in the shape the commit corrected elsewhere. Polish; no reader is misled.

## Verification of the author's claims

- **The re-flow changed no word.** Verified: a word-by-word comparison (`str.split()` of each file at
  `cdbde3d2` and at `83aa64db`, `difflib.SequenceMatcher`) gives for `foundations/decisions.md` one
  difference only — the insertion of "or the executor" in the heading of WAY-408 — and for
  `request_template.md` exactly the two intended changes: "feel* (WAY-289):" → "feel, and errors the
  walk found outside the task's scope* (WAY-289, WAY-408):" and the inserted "or executor". The
  re-flowed passages (WAY-121 *violates*, *Rejected*; WAY-406 *Rationale*; WAY-407 *Verification*,
  *Rationale*) are word-identical.
- **Title of kind 8.** Agrees with WAY-408 (errors of the walk outside the scope go under *Fix or let
  through*, with the question of a task, whatever the judgment of what is felt; WAY-408 "narrows
  WAY-289"), with WAY-289 (the felt findings) and with WAY-287 (another decision may add a kind of
  item to a group it names, and the template lists every kind — kind 8 is listed under *Fix or let
  through*, the group WAY-408 names). No script or other file parses the title (searched for
  "Unfixed findings", "will feel", "Skipped steps and unrun" across the worktree: only the template
  and an unrelated sentence of `agent-instructions/README.md:97` on a request without a task cycle).
- **Question of WAY-408** "What does the author or the executor do…": agrees with its first binding
  sentence ("The author of a change or the executor of a slice corrects…") and with WAY-406.
- **"its author or executor reported"** in kind 8: agrees with WAY-408 and WAY-406; but see finding 1
  for the place it was not carried to.
- **No environment fact.** Agrees with WAY-100 (a source a reader cannot open is described in
  *Rationale* and said not to be open, WAY-27); WAY-406's *Rationale* does so for `test-run` and the
  two courses, and *Based on* reads `none`.
- **No glossary term for "walk".** Accepted: used in its ordinary meaning; a finding would be Minor by
  WAY-297 with no misread sentence to cite.
- **Rows 1-11 of *Settlements to record*.** The author's table of where each row went agrees with what
  I read of WAY-406 (rows 1-3), WAY-407 (row 4), WAY-408 and kind 8 (row 5); rows 6-11 I did not
  re-verify against the files outside the range (they passed the review of the whole change,
  `PASS cdbde3d2`, and the return commit does not touch them). No row is missed by the return commit.
- **No invariant, no part-map change.** Accepted: no rule a commit could make false is set by the
  task, a decision or the human; the files touched lie in parts whose entries hold them.

## Declined to judge

none

## Checks

| Command | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `83aa64dbebfcd6f0077a0cd64c204ff494d0cd5d` |
| `git diff cdbde3d2..83aa64db`, `git log --stat cdbde3d2..83aa64db` | 0 | one commit, two files |
| `python -B .runs/review-return/words.py` (word comparison of both files before and after, output to a UTF-8 file) | 0 | differences listed above, none in the re-flowed lines |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B task-cycle/private_paths_check.py foundations/decisions.md` | 0 | `0 listed` |
| `python -B task-cycle/private_paths_check.py task-cycle/skill/request_template.md` | 0 | `0 listed` (a first call with both files as arguments exited 2, "unrecognized arguments"; the script takes one file) |
| `awk 'length($0)>100'` over `request_template.md` at both commits and over the added lines of `9cffc9ba..83aa64db` | 0 | finding 3 |
| `git log -L533,537:task-cycle/skill/request_template.md 9cffc9ba..83aa64db` | 0 | last changed in `cdbde3d2` |

Not run: the tests of `task-cycle` (the author ran them, 534 OK; the commit changes prose only and no
script reads the changed titles), the full gate (the cycle's own run).

## Reaches beyond the dispatch

- WAY-263 (`foundations/decisions.md`, the entry whole) — to grade finding 1.
- WAY-27, WAY-90, WAY-100 (the binding sentences, by search of their headings) — to judge the claim of
  no environment fact.
- `agent-instructions/README.md:88-102` — the only other file with "will feel", to see whether it
  restates kind 8.
- `foundations/glossary.md` — searched for an entry "author" or "executor" (whether "author" covers the
  executor); none.

## Working copies

`.runs/review-return/` in the worktree held `words.py` and its output `words.txt`, and the output of the
foundation check `fc.txt`; removed before returning (`ls .runs/` shows only `orchestrator/` and
`task-cycles/`). No worktree of a commit was made.

## Unread material

- WAY-25, WAY-121, WAY-319: read as far as the range touches them — the re-flowed passages of WAY-121
  (its *violates* and *Rejected*) in the diff; WAY-319 is not touched by the commit; WAY-25 not opened,
  since the commit settles no collision beyond the one WAY-408 already states ("prevails over
  WAY-289").
- `foundations/decisions.md` beyond the entries named: not read, as WAY-150 gives.
- Rows 6-11 of the task's *Settlements to record*: not re-verified against `task-cycle/change/walkthrough.md`,
  `elements/decisions/template.md`, the glossary and `project-level/technology/research.md`, which the
  commit does not touch.

## Searches not found or unclear

- A glossary entry for "author" or "executor" in `foundations/glossary.md`: not found; so whether "the
  author" in the template could be read as covering the executor rests on WAY-406 and WAY-408, which name
  the two apart.
- A script or test that parses the titles of the kinds of the request template: not found (search for
  "Unfixed findings", "Skipped steps and unrun", "Decisions of the task's own sections").

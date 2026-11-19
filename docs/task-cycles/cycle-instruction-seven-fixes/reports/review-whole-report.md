PASS bcaddc2bb505419375b9b4faf4dfa59e188e9b82

# Review of the whole change — cycle-instruction-seven-fixes

Range `0b43a27d..bcaddc2b` (3 commits: `2a0df03c`, `fc88ee2c`, `bcaddc2b`), diff computed by me;
`git rev-parse HEAD` is `bcaddc2b`. Route: one author, no plan, no spec. No trust boundary touched
(`task-cycle/slice_size.py` is not among the files the part map names for `task-cycle`), no
operation that cannot be undone, no reserved choice, no screenshot file in the range, no invariant
test changed.

Counts: blocking 0 · Minor within the task 4 · out of scope 2.

## Coverage of the task

Each point compared word for word with the task's quotation.

| Point | Place | Result |
|---|---|---|
| 1 | `task-cycle/skill/SKILL.md:82-86` | as quoted; the list now ends ", and the registry …" |
| 2 | `task-cycle/skill/SKILL.md:506-510` | as quoted |
| 3 | `task-cycle/skill/SKILL.md:214-218` | as quoted; `task-cycle/remarks_check.py` exists and reads the reports (WAY-294); `## Events` stands in `task-cycle/record_template.md:102` |
| 4(a) | `task-cycle/slice_size.py:19-22`, `:166-196`; `task-cycle/test_slice_size.py:63-92` | the quoted sentence stands in the docstring, with one clause added for the author's choice (a); code and tests agree with it |
| 4(b) | `task-cycle/plan/SKILL.md:154-156` | as quoted |
| 4(c) | `task-cycle/change/SKILL.md:37-38` | as quoted |
| 5 | `elements/decisions/template.md:90-95` | as quoted |
| 6 | `task-cycle/change/SKILL.md:120-123`, `task-cycle/review/SKILL.md:113-116` | as quoted, in both |
| 7(a) | `task-cycle/skill/SKILL.md:367-369` | as quoted, at the end of the paragraph handoffs copy |
| 7(b) | `task-cycle/skill/SKILL.md:835-837` | as quoted |
| row 1 | WAY-136, `foundations/decisions.md:6261-6264` | meaning of the row kept: judgment, not a measure; the plan's order; grouping and reason recorded |
| row 2 | WAY-255, `foundations/decisions.md:6688` | meaning of the row kept, as a clause of the first sentence |
| row 3 | WAY-134, `foundations/decisions.md:5505-5509` | meaning of the row kept |

The rejected variants under *Questions to settle* are not restored: no sentence in WAY-316 or
WAY-140, no measure in point 2, no branch that counts a foundation file without a range as zero
(a changed file with no range still counts whole: scratch run below, slice 2), no sentence on the
orchestrator's side for point 6, no `task-cycle/record_copy.py`. The hunks of
`foundations/decisions.md` lie in WAY-134, WAY-136 and WAY-255 only.

## The two choices the handoff asks me to judge

**(a) A file that *Read* names both whole and by ranges counts whole.** Accepted. The task's
sentence, read by its letter, gives the ranges; but a slice whose *Read* names the file whole has
its agent read it whole, by the sentence of point 4(c) too ("by the ranges your dispatch names"
gives nothing narrower where the dispatch names the whole file), so the whole count is what the
measure is for, and it is how a file of *Read* alone was counted already. The added clause of the
docstring says it, and `test_changed_file_that_read_names_whole_and_by_ranges_counts_whole` holds
it (mutation M2 below).

**(b) The ways "only the skill, the decision unchanged" and "only the two skills" stay out of
*Rejected*.** Accepted as the nearest reading of the sentence of point 5: "how or when an answer
is recorded" names the choice of the place the answer is written to, and the task's own words for
the case are a way of writing the answer down. A concern for the orchestrator stays (see
*Questions and concerns*): in the-way the place of a rule is itself a matter of the product, and
the log holds ways of this sort in *Rejected* already (WAY-148: "a change of the orchestrator's
skill alone, with no change to this decision"; WAY-134: "the rule of rejected options in the
templates alone").

The extension of the *Rejected* of WAY-136 with the criterion taken from a measure is what the
template asks: a way the row's source keeps, with the cost the source gives, nothing added. The
rewording of "a review of every slice" is the reconciliation *Decisions in play* asks for. The
additions to *Verification* and *Rationale* are right to make, since the pair of examples covers
the part of the sentences no test holds; what they do to the marking of the entries is finding 1,
and the reason written into WAY-134 is finding 3.

## Findings

### Minor, within the task

**1. The three entries gained examples and reasons their rows do not give, and the author's report
marks them `row <n>`.** Place: the author's report, section "Foundation step" ("None is marked
`the cycle's`"); the added text at `foundations/decisions.md:5542-5544`, `:5557-5559`,
`:6285-6287`, `:6295-6296`, `:6703-6704`, `:6709-6710`.
`task-cycle/skill/foundation_step.md` says: "a part the writer adds that its row or projected
entry does not give — a pair of examples, a field the projected entry left `TODO` — makes the
entry `the cycle's`, save a pair kept only until a test of the same change holds the sentence …
and the writer keeps in its report the added pair word for word for the description to quote under
the entry". WAY-114 gives as a violation "an entry marked as the cycle's for an added pair of
examples reaches the merge with the pair not shown", and `elements/decisions/skill/SKILL.md` has
the human accept a proposed pair at the merge, "the entry marked as
`task-cycle/skill/foundation_step.md` gives". The author's reason — that it extended the clauses
the decisions had and added no pair standing apart — does not change what was added: for each new
sentence a complying and a violating example that no row gives. Why it matters: the request would
list the three entries as written from rows and show the human none of the examples by which
agents measure later changes. No file of the change is wrong; the correction is the marking and
the quotation in the author's report (and from it the record and the request). The added clauses,
word for word:

- WAY-136, complies: "a change that rewrites many entries of the foundation from many notes has
  the slices without a review of their own reviewed in groups, in the plan's order, the grouping
  and its reason recorded"; violates: "reviews of groups of slices are dispatched with no grouping
  and reason recorded, or by a measure in place of the orchestrator's judgment".
- WAY-255, complies: "and returns its report after reading the result"; violates: "an agent ends
  its turn with a note that it still waits for the tests it started in the background, in place of
  their result".
- WAY-134, complies: "a decision row whose source keeps a way with only the cost of a gate to
  reopen gives that way `no cost to the product known` in the decision's rejected options, and
  leaves out the way that only chose when the answer is recorded"; violates: "the cycle puts in
  the rejected options a way of the process, such as when an answer is recorded, or leaves a way
  whose source keeps no cost without the words `no cost to the product known`".

**2. The first paragraphs of WAY-136 and WAY-134 hold four binding sentences.** Place:
`foundations/decisions.md:6245-6264` and `:5482-5509`. The template gives "One to three sentences
answer the question of the heading, in the first paragraph under it" (WAY-05); both paragraphs had
three at the base, and the author kept WAY-255 at three by writing the rule as a clause, for this
very reason, by its report. The content agrees with the rows and the check of the foundation does
not count sentences, so this is a departure of form with no sentence read wrongly (WAY-364). A
clause joined to the third sentence, as in WAY-255, keeps the form.

**3. The reason written into the *Rationale* of WAY-134 is the author's own, not the task's.**
Place: `foundations/decisions.md:5590-5595`: "A way of the process, such as when an answer is
recorded, is no alternative the product weighed, so listed among the rejected options it would
make the proposer of a later change of the product meet a refusal that never concerned it; a way
whose source gives no cost, or only a cost of the process, stands with the words `no cost to the
product known`, so that its empty cost reads as nothing known to weigh and not as a cost nobody
weighed." The task gives one reason for point 5 and row 3: agents settled these three cases
differently from one cycle to the next (its *Need* and *Context*). The entry now gives another
reason as that of the human's settlement, and a later reader takes a written reason for the one
the decision was made for (the rationale of WAY-29 says so of a reason an agent writes). Its last
clause is also hard to read: "nothing known to weigh" and "a cost nobody weighed" are not told
apart by the words. The additions to the *Rationale* of WAY-136 and WAY-255 do follow the task's
*Need* (one reviewer cannot compare several hundred entries with their sources; a note that the
agent waits in place of the result). The correction is to state in WAY-134 the reason the task
gives, or to leave the reason out.

**4. A wrong number in the comment of a new test.** Place: `task-cycle/test_slice_size.py:64-65`:
"A decision log of 400 010 characters in its first line". The file the test writes holds 400 009
characters (`"x" * 400_000` and `"\none\ntwo\n"`, 9 characters) and its first line 400 000. The
figure of 160 004 tokens and the asserted values (8 characters, 4 tokens, `fits`) are right, so the
test stands; the comment is the source of its values (the rule on test data of
`guidelines/testing.md`) and gives one of them wrongly.

### Out of scope (each goes beyond the task: the task settles this wording)

**5. Minor — "the lead" names the orchestrator by a word the-way uses nowhere else.** Place:
`task-cycle/skill/SKILL.md:508`. The skill addresses its reader as "you", the decisions say "the
orchestrator" (WAY-136 as this change writes it included), and a search of the task-cycle skills
and the glossary finds "the lead" in this one sentence only; a reader can take it for another
actor than the one the rest of the sub-step addresses. The word is the task's, given word for
word and confirmed under its first question, so changing it goes beyond the task.

**6. Minor — the measure and the reading differ for a changed file that is no file of the
foundation.** Place: `task-cycle/slice_size.py:194-196` against `task-cycle/change/SKILL.md:37-38`.
The sentence of point 4(a) counts by its ranges every file of *Change* that *Read* names by
ranges; the sentence of point 4(c) lets the agent read by ranges only "a file of the foundation",
and every other file it changes whole. A plan that names in *Read* a range of a file of code the
slice changes is now measured by the range while its agent reads the whole file. Evidence: scratch
run below, slice 4 — `task-cycle/remove_merged_worktrees.py` in *Change* with `:1-10` in *Read*
counts 548 characters at the head and 25 907 at the base. The task's answer on point 4(c) gives as
its aim that the measure and the reading count the same; both sentences are the task's, so the
difference is a gap of the task and its closing goes beyond it.

## Declined to judge

- The list of exceptions of `task-cycle/skill/SKILL.md:80-87` now holds the screenshot and still
  cites WAY-140, which names no such exception: the task settles that WAY-140 and WAY-316 stay as
  they are and that the human is shown the collision.
- WAY-373 does not state the removal by a path written out in full that point 7(a) puts into the
  paragraph handoffs copy: the task keeps WAY-373 unchanged.
- `task-cycle/review/SKILL.md` (its opening list of the reviews the cycle dispatches) and
  `task-cycle/plan/SKILL.md:171-173` name no review of a group of slices: the task gives the
  sentence to one place of the cycle's skill and to WAY-136, and "as for a slice with a review of
  its own" carries the rest.
- "by the ranges your dispatch names" (point 4(c)) for the one author, whose dispatch names
  entries by identifier and no ranges: the task's wording.
- `task-cycle/skill/foundation_step.md:41-42` restates the rule of *Rejected* without the new
  words and points to the template for it: the task does not name the file, and the pointer holds.
- What the *Rejected* of a new decision holds where every way its source keeps is a way of the
  process and stays out: neither the template's sentence nor row 3 says, and both are the task's.
- The template says "where the source keeps none", after "the cost or the reason", and WAY-134
  says "with no cost": both wordings are the task's (point 5 and row 3).

## The author's own-work check and its judgment on the walk

The requirement the author names — point 4 as a whole — is where the change is weakest, being its
only code, and its check (the real log, a slice with a range and one without, at the base and with
the change) would catch it unmet. My scratch run agrees with its figures (slice 1 fits with the
change and is too large at the base; slice 2 stays too large).

The author's judgment that the change alters no behaviour a user sees is arguable for
`slice_size.py`, a command in a terminal whose printed verdict changes for a class of plans. It
makes no difference to what was checked: the new tests assert on the printed row through `main`,
and the own-work check ran the command itself on the real log, which is what a walk would have
done. No finding.

## Structure of the code the change leaves

`python -B task-cycle/change_file_sizes.py 0b43a27d bcaddc2b`, exit 0: `task-cycle/slice_size.py`
253 → 259 lines, `task-cycle/test_slice_size.py` 191 → 222, `task-cycle/skill/SKILL.md` 893 → 906,
`foundations/decisions.md` 11586 → 11618, `elements/decisions/template.md` 329 → 332,
`task-cycle/change/SKILL.md` 197 → 199, `task-cycle/plan/SKILL.md` 233 → 235,
`task-cycle/review/SKILL.md` 209 → 210. The test of the invariant `function-and-file-size`,
`python -B -m unittest agent-instructions/test_size_invariant.py`, run in a worktree of the base
and in one of the head: 4 tests OK, exit 0, in both; nothing stands over a threshold before or
after. `measure` runs from line 162 to 211. No code is left without a user, and no name stopped
being true (`whole` became a set whose members are the files counted whole).

## Checks I ran

In the reviewed worktree, reading only:

- `git diff 0b43a27d..bcaddc2b`, `git log --stat 0b43a27d..bcaddc2b`, `git rev-parse HEAD` — exit 0.
- `python -B task-cycle/change_file_sizes.py 0b43a27d bcaddc2b` — exit 0.
- The pinned Ruff of the main checkout, on the two changed Python files, with `--no-cache`:
  `ruff check --no-cache --ignore-noqa --config ruff.toml task-cycle/slice_size.py task-cycle/test_slice_size.py`
  — exit 0, "All checks passed!"; `ruff format --check --no-cache --config ruff.toml` on the same
  two files — exit 0, "2 files already formatted". (The author could not run Ruff by hand.)
- Scratch run of `python -B task-cycle/slice_size.py <plan>` on a plan of five slices against the
  real files, and the base's script on the same plan and tree — exit 1 in both (a slice too
  large), as expected:

  | Slice | *Change* | *Read* | Head | Base |
  |---|---|---|---|---|
  | 1 | `foundations/decisions.md` | `foundations/decisions.md:6243-6339` | 8 522 characters, fits | 905 659, too large |
  | 2 | `foundations/decisions.md` | `task-cycle/slice_size.py` | 916 646, too large | 916 646, too large |
  | 3 | `foundations/decisions.md` | `foundations/decisions.md:6631-7250` (a section of the log) | 47 880, fits | 905 659, too large |
  | 4 | `task-cycle/remove_merged_worktrees.py` | `task-cycle/remove_merged_worktrees.py:1-10` | 548, fits | 25 907, fits |
  | 5 | `task-cycle/remove_merged_worktrees.py` | none | 25 907, fits | 25 907, fits |

In a worktree of the head, in my directory:

- `python -B -m unittest task-cycle/test_slice_size.py` — exit 0, 19 tests OK.
- `python -B elements/common/foundation_check.py` — exit 0, "0 errors".
- `python -B gate/run_tests.py task-cycle` — exit 0, 537 tests OK, 2 skipped on Windows.
- `python -B gate/run_tests.py elements/common` — exit 0, 271 tests OK.
- `python -B gate/run_tests.py agent-instructions` — exit 0, 52 tests OK.
- `python -B gate/run_tests.py instruction-files` — exit 0, 105 tests OK, 5 skipped.
- `python -B gate/run_tests.py product-guidelines` — exit 0, 14 tests OK.
- `python -B -m unittest agent-instructions/test_size_invariant.py` — exit 0 in the worktree of the
  head and in that of the base.

Mutations, each on a copy of `slice_size.py` beside a copy of its test file, run with
`python -B -m unittest test_slice_size.py`:

- M1, a changed file always counted whole (the behaviour of the base): 1 failure,
  `test_changed_file_that_read_names_by_ranges_counts_only_those_lines`.
- M2, ranges win over a whole entry of *Read*: 1 failure,
  `test_changed_file_that_read_names_whole_and_by_ranges_counts_whole`.
- M3, a changed file counted only where *Read* names it: 2 failures,
  `test_changed_file_that_read_does_not_name_counts_whole` and `test_slice_within_limits_fits`.
- M4, a changed file dropped as soon as *Read* names any range: 1 failure,
  `test_changed_file_that_read_does_not_name_counts_whole`.

The new tests fail when the behaviour they protect breaks, and their expected values are written
out and derived by hand from the files they write. No code of the script is made for the input of
a test (WAY-409): the branch added is the rule of the task's sentence.

Not run: the full gate, by the handoff; the product's final gate is the CI run on the request.
Not verified by me: that the first new test was seen failing before the code, which the author
reports from a run whose exit code a pipe hid; mutation M1 shows the same failure.

## Reaches beyond the dispatch

- `task-cycle/skill/foundation_step.md`, whole, `elements/decisions/skill/SKILL.md` and
  `elements/decisions/skill/decide_entry.md`, whole — what binds the writer of the three entries,
  for finding 1 and choice (b).
- `task-cycle/change/walkthrough.md`, lines 1-60 — to judge the author's statement on the walk.
- `task-cycle/record_template.md` (a search for *Events*) and the list of `task-cycle/` — the
  table and the script that point 3 names.
- `agent-instructions/test_linter_invariant.py`, lines 60-84, and `ruff.toml` — where the pinned
  Ruff stands, to run it on the changed files.
- WAY-114 and WAY-29, whole — the acceptance of an added pair of examples and the rule on a reason
  an agent writes; WAY-150, whole — for point 4(c).

## Working copies

All stood in `.runs/review-whole/` of the task's worktree and are removed: the worktrees `base`
(`0b43a27d`) and `head` (`bcaddc2b`), each with `git worktree remove --force` and then
`git worktree prune`; the directory `mut` with the mutated copies and the scratch plan; the index
of my selection and the list of sections; the outputs of the test runs. `.runs/` holds
`task-cycles/` alone again, `git worktree list` names no worktree of mine, and the reviewed
worktree is clean at `bcaddc2b`. Nothing is kept in `reports/` beside this report.

## Unread material

Decisions: the index of my selection listed 56 decisions in full and 110 by heading alone (the
sections "The course of a task cycle", "The work of a cycle's agents", "Review of a change", "Task
refinement and readiness", "Decision entries and the decision log" and "The request and the
human", the parts `task-cycle` and `decisions`, and the seven decisions the task names). I read
the index whole and 10 decisions whole: WAY-134, WAY-136, WAY-255, WAY-140, WAY-148, WAY-316,
WAY-373 and WAY-29 of those listed in full, and WAY-114 and WAY-150 of those listed by heading.

Decisions that bear on the change and stayed unread whole: WAY-05 and WAY-12 (the form and the
verification of a decision entry — read as the index gives their binding sentences and through
`elements/decisions/template.md`, read whole); WAY-385 (the thresholds of size — taken from the
test of its invariant, run at the base and at the head); WAY-293 (where a rule of the-way stands
— its binding sentences in the index).

Guidelines: `guidelines/coding.md`, `guidelines/testing.md`, `guidelines/coding-measuring-report.md`
(the kind of `slice_size.py`) and `guidelines/coding-check.md` read whole; the other four kind
files were not selected and not read.

Other material read in part: `foundations/invariants.md`, lines 1-200 and 280-569 (lines 201-279,
invariants of other parts, unread); `elements/common/way_of_working.md`, lines 55-200;
`task-cycle/skill/SKILL.md`, lines 60-109, 196-245, 348-387, 440-559 and 812-891, and the diff;
`task-cycle/plan/SKILL.md`, lines 100-235; `task-cycle/change/SKILL.md`, lines 1-130.
`elements/common/rules.md` and the method files of `instruction-files/` were not read; the tests
of `instruction-files` ran on the changed skills. The glossary, the part-map entries of
`task-cycle` and `decisions`, the task, the author's report, `task-cycle/review/SKILL.md` and
`task-cycle/review/whole_change.md` were read whole. The unread parts of WAY-316, WAY-148 and
WAY-140 that the author names are read here; WAY-03 was not opened (no invariant test changed).

## Searches not found or unclear

- "the lead": searched the task-cycle skills and `foundations/glossary.md` for the word; it stands
  in the new sentence of point 2 alone, and no entry says who it is (finding 5).
- A decision or an invariant that says how `task-cycle/slice_size.py` counts a file: searched
  `foundations/` for `slice_size`, "too large" and "estimated tokens"; found only the withdrawn
  WAY-371, whose rule "stands in `task-cycle/slice_size.py`". The foundation holds nothing to
  compare point 4(a) with.
- Whether the-way's foundation settles a way to its own running product, and whether the printed
  report of `slice_size.py` is "a command in a terminal" in the sense of WAY-406: searched
  `foundations/` and found no sentence on either.
- A rule on the width of a line of Markdown: searched `elements/common/rules.md`,
  `instruction-files/`, `agent-instructions/`, `guidelines/` and `README.md`; none found, so the
  lines the edits left long or short (`task-cycle/skill/SKILL.md:218`,
  `elements/decisions/template.md:95`, `foundations/decisions.md:6311`, `:6331`, `:6725-6726`) are
  no finding.
- Whether "only the skill, the decision unchanged" is "a way of the process rather than of the
  product": the sentence of point 5 does not say what the process is where the product is the-way,
  whose skills and decisions are the product (choice (b)).

## Questions and concerns for the orchestrator

No question holds the review.

1. Finding 1 needs no commit: the author's report is to mark the three entries `the cycle's` and
   keep the added clauses word for word (they stand above), so that the request shows them.
2. Choice (b) rests on a reading of a sentence this same change writes. I recommend that the
   request names it to the human in one sentence: three ways the sources of rows 1 and 2 keep
   ("only the skill, the decision unchanged"; "only the two skills", twice) stay out of the
   *Rejected* of WAY-136 and WAY-255 as ways of how an answer is recorded, while WAY-148 and
   WAY-134 hold ways of the same sort in their own *Rejected*. The cost of the other reading is
   three clauses.
3. Findings 5 and 6 are defects of wording that the task itself gives, and stay for the human.

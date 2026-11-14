PASS 5554f5da9d8be1cf3076ec31bde4e2b14a0d49a8

# Review of the whole change — structure-grade-no-rule-cases

Range `1be90579bf3daa618dd87c06bd56042eabb642c1..5554f5d`, computed by me; `git rev-parse HEAD` is
`5554f5da9d8be1cf3076ec31bde4e2b14a0d49a8`, the head given. `git log` of the range: one commit,
`5554f5d`. Worktree status was clean and I changed no file in it.

Counts: blocking 0, Minor 0, out-of-scope 0.

## Changed files (from the diff and `change_file_sizes.py`)

| File | Diff lines | File lines before -> after |
|---|---|---|
| `foundations/decisions.md` | +12 / -10 | 12493 -> 12495 |
| `task-cycle/review/SKILL.md` | +4 / -3 | 174 -> 175 |

`task-cycle/review/whole_change.md` is not changed (see the criterion below).

## Findings

### Critical, Important

None.

### Minor

None.

## Judgement against the task

- To do 1 (`task-cycle/review/SKILL.md` section 3, lines 126-131): the sentence now says a structure
  finding is Minor "where the product has no rule of size, whatever the reason: for example, the
  product departed from the rule by a decision, it has no coding guidelines at all, or its guidelines
  were written before the rule existed". The three cases stand as examples under "whatever the
  reason", not as a closed list, and the third case is named. Met.
- To do 2 (`foundations/decisions.md` WAY-363, line 12133): the binding sentence carries the same
  wording ("every such finding in a product that has no rule of size, whatever the reason: for
  example, it departed ..., it has no coding guidelines at all, or its guidelines were written before
  the rule existed"), the scope sentence is split off into "The reviewer judges its scope as for any
  finding (WAY-161)", and the closing sentence about a function or file over a threshold is kept.
  The entry is edited in place, with no version and no second entry (WAY-07). Met.
- To do 3: *Verification* "complies" now names the third case ("or whose guidelines were written
  before the rule and hold none of it, grades the finding Minor"). *Rationale* says "Where the
  product has no rule of size ... leaves a finding of structure Minor" and *Rejected* says "where the
  product has no rule of size" — both are general and name no two-case scope. The "violates" bullet
  also says "a product with no rule of size". Nothing points to the narrower scope. Met.
- To do 4: the *Rationale* sentence "The reviewer still judges the scope of each finding ..." is
  rewrapped (lines 12169-12170); the longest line of the entry's body is 101 characters, in step
  with the entry's other lines (the 114-character line is the heading, unchanged). The text of the
  sentence is unchanged. The other wrapped lines I checked (binding paragraph, complies bullet) keep
  words and meaning apart from the intended additions. Met.
- Acceptance criterion, judged by reading the three places:
  - `SKILL.md` section 3: Minor in all three cases, as above.
  - WAY-363 binding sentence: Minor in all three cases, as above.
  - `whole_change.md` last bullet of "The structure of the code the change leaves" (line 45-48):
    "Where that heading holds `none —`, or the product's guidelines hold no such rule, there is no
    such test, the first numbers and the diff are your material, and a finding of structure is Minor
    (WAY-363)." Case by case: a product that departed by a decision holds `none — <PREFIX-NN>` in the
    heading, so it is the first clause; a product with no coding guidelines has guidelines that hold
    no such rule, so it is the second clause; a product whose guidelines predate the rule hold no
    such rule, again the second clause. All three give Minor. The author's left-open point (a reader
    who takes "hold no such rule" as meaning only `none —`) does not hold up: the two clauses are
    joined by "or", and the second clause cannot be read as the first without making it redundant.
    The author's decision not to edit `whole_change.md` meets the criterion and the task's *To do*,
    which lists no edit to that file; the task's Context itself calls that bullet the model.
    The three places now give the same grade in each case.
- Nothing added that nobody asked for: the diff touches only the two files, and in them only the
  binding sentence, the *Verification* bullet, the wrapped lines of the same entry, and the
  sentence of `SKILL.md`. WAY-360's *Rejected* sentence and the other places the task names as
  already general (`plan/SKILL.md`, `change/SKILL.md`, `settle.md`) are untouched, as the task's
  *Out of scope* requires.

## Against the foundation

- WAY-363 (entry the change writes): its binding sentence, *Verification*, *Rationale* and *Rejected*
  agree with each other and with the sentence in `SKILL.md` section 3; WAY-263 does not apply — no
  departure between the entry and the code that does what it says. `SKILL.md` and the entry say the
  same thing without the broader or narrower restatement WAY-263 names.
- WAY-07: met (in-place edit, one entry per number).
- WAY-161: the sentence "judges its scope as for any finding" still points to the scope rule; the
  change does not alter it.
- WAY-360 and WAY-362 (quoted by the task): consistent with the new wording; a product with guidelines
  and no heading breaks WAY-360, and the new example names that transitional state without
  licensing it. The wording "written before the rule existed" is the task's own, and states a present
  fact of the product's guidelines (they hold none of the rule), not a history.
- No invariant test is changed. No reserved choice is taken. No trust boundary, no irreversible
  operation, no user interface (handoff step 4 answers: no).
- Tests: the change is prose and the task calls for no test; none is written or changed. The check
  below shows the foundation form still passes.

## Structure of the code the change leaves

`python -B task-cycle/change_file_sizes.py 1be90579bf3daa618dd87c06bd56042eabb642c1 5554f5d` gives:
`foundations/decisions.md` 12493 -> 12495 (+2), `task-cycle/review/SKILL.md` 174 -> 175 (+1), total
+3 lines. The-way has no rule of size, so no test of the rule exists; the numbers and the diff are my
material. No function, no code that has no user, and no name that stopped being true — the change is
prose.

## Declined to judge

- `foundations/decisions.md` WAY-360 *Rejected*, "the same chance in the grade": the task lists it as
  a separate remark of the earlier review (out of scope per the task).
- `foundations/decisions.md` WAY-362 *Rejected: unknown*: not part of the task, not touched.

## Checks run

| Check | Command | Exit |
|---|---|---|
| Foundation check | `python -B elements/common/foundation_check.py` (in the worktree) | 0, prints `0 errors` |
| Sizes of changed files | `python -B task-cycle/change_file_sizes.py 1be90579bf3daa618dd87c06bd56042eabb642c1 5554f5d` | 0 |
| Diff read in full | `git diff 1be90579bf3daa618dd87c06bd56042eabb642c1..5554f5d`, `git log 1be9057..5554f5d` | 0 |
| Search for the old scope | `grep` over tracked files (not `.runs/`) for "no coding guidelines at all", "departed from the rule by a decision", "no rule of size", "WAY-363"; each hit read | 0; only the two edited places say the three cases; other hits are general or the decision case alone, correct |
| Line widths of WAY-363 | `awk` over lines 12131-12180 of `foundations/decisions.md` | 0; maximum body line 101 |

The whole gate was not run (the orchestrator runs it). Author's `gate/run_tests.py foundations`
result ("no test found in foundations", exit 1) is not a failure of the change: that directory holds
no tests, and I did not repeat it.

## Reaches beyond the dispatch (section 1)

- `foundations/decisions.md` WAY-07 (line 163), WAY-161 (line 4694), WAY-360 (12010), WAY-361 (12065),
  WAY-362 (12100), WAY-365 (12221), read whole: the task's *Decisions in play* and the entries that
  speak of a product with no rule of size; WAY-363 itself whole.
- `elements/common/way_of_working.md` lines 55-105 ("Reading the foundation"): the method of my
  selection.
- `task-cycle/review/whole_change.md` whole: the file `SKILL.md` section 1 names for this review and
  the third place of the acceptance criterion.
- `docs/task-cycles/structure-grade-no-rule-cases/task.md` and `reports/author-report.md` whole.

## Reading added after the verdict (amendment at the coordinator's request)

The head is now `6914b90` (target branch merged; the merge adds WAY-371 and `slice_size.py` and
leaves WAY-363, `task-cycle/review/SKILL.md`, `whole_change.md`, `part_map.md`, `invariants.md`,
`glossary.md` and `product-guidelines/coding/` as at `5554f5d`; checked with `git diff
5554f5d..6914b90` on those paths). I judged what I read only against the reviewed range
`1be9057..5554f5d`. The first line of this report stands: what I read changes no verdict and no grade.

What I read whole, and what it showed:

- WAY-328 whole (`foundations/decisions.md:10933`): the-way departs from the general coding
  guidelines and the testing guidelines under WAY-217 for its own code. It says nothing of the rule
  of size and no grade of a finding. WAY-363's *Verification* cites it only for "this repository
  has no coding guidelines", which stays true. No bearing on the PASS or a grade.
- Invariants, `foundations/invariants.md` whole (356 lines), for the parts the change touches by the
  files it changes (`task-cycle` for `SKILL.md`; `foundations/decisions.md` by the entries the
  change writes, WAY-363, scope `task-cycle, product-guidelines`) and `every`. Those that reach the
  diff: `tracked-file-private-paths` (test) — the diff holds no absolute path and no note link
  (`grep` of the added lines for a drive path found none); `outbound-link-reach` (review) — no link
  added; `skill-entry-points` and `derived-file-content` — the change touches only the body of
  `task-cycle/review/SKILL.md` (lines 126-131), not its frontmatter, so the description and the
  entry point `.claude/skills/the-way-review-change/SKILL.md` (which I read, and which only points to
  `SKILL.md`) need no regeneration; `record-copy-image-check` and `record-copy-image-files` — the
  range holds no image file; `foundation-change-merge-route` and `return-step-record` (review) —
  concern the cycle's merge route and return step, not the content of this range. No invariant is
  violated, no invariant test changed.
- Part map, `foundations/part_map.md` whole (267 lines): `foundations/decisions.md` belongs to
  `decisions` (and, for what it writes, to the parts its entry names); `task-cycle/**` to
  `task-cycle`. The change adds no import and no dependency, so `cross-part-imports` and the *Depends
  on* lines are not reached. No bearing.
- Glossary, `foundations/glossary.md` whole (191 lines): there is no entry for "rule of size",
  "coding guidelines" or "finding", and the change adds none. The entries it uses, "guidelines",
  "binding sentence", "binding part", "foundation" and "transitional state", agree with the changed
  sentences: the pre-rule product of the new example is the transitional state the task's Context
  describes, WAY-363 does not name it so, and no sentence of the change is read wrongly for lack of
  an entry (grade of a missing entry: Minor, WAY-297, and no such sentence exists).
- `product-guidelines/coding/settle.md` whole (148 lines) and `template.md` whole (349 lines):
  `settle.md:89-90` ("with no rule of size, a reviewer's finding about the structure of the product's
  code is always Minor (WAY-363)") is general and agrees with the new wording. `template.md:76-78`
  says that a product that goes without the rule by a decision "reads `none — <PREFIX-NN>`" and that
  a reviewer's finding is then "always Minor"; this is the decision case alone, stays true, and does
  not say the other two cases are graded otherwise. `template.md:12-15` and WAY-360 keep that a
  product departs only by a decision, and a product with guidelines and no heading is the
  transitional state the new example names; the example licenses no omission of the heading and
  WAY-360's *Verification* still lists it as a violation. Neither file needs a change and no finding
  follows. The author's claim in the author report (they speak of the decision case) is confirmed.
- Further decisions opened whole after I corrected my selection (below): WAY-05 (an entry's binding
  sentences describe a present state; the rationale does not tell how the decision was reached),
  WAY-12 (form of *Verification*), WAY-71 (fields), WAY-99 (one word, one meaning), WAY-256 (place
  of a fragment of a skill), WAY-354 (a decision that describes a transitional state). Against WAY-05
  I considered whether "its guidelines were written before the rule existed" in WAY-363's binding
  sentence is history; it states a property of the product's guidelines today (they hold none of the
  rule), as "it departed from the rule by a decision" already did, and the *Rationale* does not tell
  how the decision was reached, so I give no finding. WAY-99: "rule of size" and "guidelines" keep one
  meaning across the changed sentences. WAY-354, 71, 256, 12: no bearing.

## Unread material

- Counts, corrected: my first count of 196 decisions under `task-cycle` or `product-guidelines` in
  *Scope* missed the entries whose *Scope* continues on a second line; the count is **216**. With the
  44 further entries whose *Scope* names `decisions` and neither of those parts, the selection is
  **260**. **Read whole: 14** — of the 216: WAY-363 (the changed entry), 161, 328, 360, 361, 362,
  365, 71, 256; of the 44: WAY-05, 07, 12, 99, 354. **By title only: 246** — the 207 and the 39 that
  remain, whose titles I read in full lists (including the 20 I first missed, among them WAY-33,
  WAY-150, WAY-114 and WAY-134, which concern how a foundation change searches and reads and not the
  grade of a finding). I opened every entry whose title points to the grade of a finding, to a
  product without a rule of size, to a word's meaning or to a transitional state; WAY-263, 297, 364,
  173, 168 I did not open whole: they are cited by the paragraph of `SKILL.md` section 3 that stands
  beside the changed sentence and is not changed, and WAY-173 and WAY-168 by the unchanged
  `template.md` text I read.
- Invariants, part-map entries and glossary entries of the selection: all read whole now (above).
  Guidelines: none exist for the-way (WAY-328); `settle.md` and `template.md` read whole as product
  guidelines material of the touched part, not as guidelines of the-way.
- `elements/common/way_of_working.md`: only the lines 55-105 ("Reading the foundation"); the rest not
  read, not needed for this review.

## Searches not found or unclear

- My first search for the selection parsed multi-line *Scope* fields wrongly and gave 196 instead of
  216 (found and corrected above); I found nothing unclear beyond that.

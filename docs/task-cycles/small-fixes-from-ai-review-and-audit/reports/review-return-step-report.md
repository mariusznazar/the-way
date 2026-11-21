PASS 1eaa3c4faae3e678abbd6774560a6d75607afa1b

# Review of the return step's commits

Range: `5d160f9d75f25c26092815ba98df43c6cc4aa2f6..1eaa3c4faae3e678abbd6774560a6d75607afa1b`, one commit,
`1eaa3c4f` "Name the tests that hold WAY-339 and WAY-417 in their Verification and drop the pair they
hold". `git rev-parse HEAD` printed the head. Files: `foundations/decisions.md` (the *Verification* of
WAY-339 and of WAY-417) and `foundations/part_map.md` (the description of `elements-common`).

## Blocking findings

none

## Minor findings

### M1 — a test comment still points to the pair of examples that the commit removed from WAY-417

- Place: `process-audit/test_series_summary.py:93`:
  `# Five cycles, as the verification of WAY-417 gives: two yes, two no and one unknown.`
- What is wrong: before `1eaa3c4f`, WAY-417's *Verification* held a complying example of "a series of
  five cycles, two of which answer yes to Q1, two no and one unknown". The commit replaced that pair
  with a clause `tests:` (`foundations/decisions.md:9018`-`9027`), so WAY-417's *Verification* no longer
  gives five cycles. The comment now sends a reader to an example that does not exist.
- Why it matters: little. The test still asserts its own values (`yes 2 · no 2 · unknown 1`). But a
  reader who follows the comment finds nothing. The return step should have caught it: its own
  search (return-step report, "Own search") covered only markdown, json, yml and toml files, and this
  is a `.py` file.
- Evidence: `git grep -n -i "verification of WAY-" -- '*.py' '*.md'` outside `foundations/` finds only
  this line.
- Suggested fix: "Five cycles: two yes, two no and one unknown." Or name the sentence of WAY-417 that
  the test holds.

### M2 — the clauses `tests:` name parts held by tests whose line `decision:` names another decision or another sentence

WAY-12 (`foundations/decisions.md:770`-`772`) requires this: "A test that holds a sentence of a decision
carries beside it a line `decision:` that gives the number of the decision and the start of that
sentence". The template says the same at `elements/decisions/template.md:268`-`281`, and adds that the
clause `tests:` is no second copy of the link because "the lines `decision:` find the tests". Every
part the two new clauses name is held by a test that exists and asserts it (checked below). But for
these parts, no line `decision:` that quotes that decision's sentence leads to the test:

- **WAY-339, "the times of the gate on both sides taking only the runs that WAY-350 compares"**
  (`foundations/decisions.md:8668`-`8669`). The only test that holds it is
  `test_the_gate_times_compare_the_runs_compared_and_show_the_others_apart`
  (`process-audit/test_process_versions.py:2012`-`2037`). Its only line is
  `# decision: WAY-350 "The audit compares the times of the gate between versions"`. That WAY-350
  sentence is about one version against the previous one, not about the comparison before and after
  a fix. The tests of the gate comparison in `process-audit/test_series_summary.py:445`-`512` carry no
  line at all.
- **WAY-417, Q1 as numbers in the image of a series and on each side of a comparison**
  (`:9018`-`9021`):
  - Image: held by `process-audit/test_process_versions.py:1709`. Its WAY-417 line quotes "The image of
    a series, which sets no two groups against each other".
  - Sides: held by `process-audit/test_process_versions.py:1974`. Its WAY-417 line quotes "The answer Q2
    of such a group".
  - Only the tests of the version rows (`:1744`, `:1764`) quote the Q1 sentence. The tests
    `Q1Numbers` and `CountImage` in `process-audit/test_series_summary.py:91`-`180` carry no line.
- **WAY-417, Q3 and the fall in the row that sets a version against the previous one**
  (`:9024`-`9025`). Held by:
  - `test_medians_and_falls_of_three_versions_over_an_odd_and_an_even_number_of_cycles` (`:1293`) and
    `test_the_gate_times_take_only_runs_with_no_other_gate_and_show_the_others_apart` (`:1354`), with
    no line `decision:`;
  - the cost Q3 of the version rows at `:1756`-`1762`, whose test's line quotes the Q1 sentence.

  No test quotes the Q3 sentence for the version rows. The only Q3 line is at `:1991`, a comparison
  before and after a fix.

Grade: Minor. The entries agree with the code: each part named is really asserted, and I ran those
tests. The decisions stay held for `foundation_check.py`, because other lines name each of them. The
departure lies in the link lines of tests outside this range, which the clauses written in this range
rely on. This is the analogue of WAY-364's form departure where the content agrees with the code. No
sentence is read wrongly through it.

The consequence: an agent that later changes the gate-times clause of WAY-339, or the Q1 or Q3
sentence of WAY-417, and looks for that sentence's tests by its line `decision:` misses these tests.
And the clause `tests:` then promises a test that the lines do not find.

Fix: add these lines at the tests that hold the parts:
- at `:2012`: `# decision: WAY-339 "The audit shows each series as an image of all its cycles"`;
- at `:1709` and `:1974`: `# decision: WAY-417 "The answer Q1 of the audit, whether a contradiction"`;
- at `:1293` or `:1744`: `# decision: WAY-417 "The answer Q3, whether the median cost"`.

## Answers to the four points of the handoff

1. **Each clause `tests:`.** I read the tests of `process-audit/test_process_versions.py:1608`-`2214`
   and the whole of `process-audit/test_series_summary.py`.
   - **WAY-339's new clause.** Each part has a test:
     - image per kind, with no Q3 and no fall: `:1709`, `:1777`;
     - a comparison for each fixed issue with a fix commit and cycles on both sides: `:1953`, `:2078`,
       `:2109`;
     - version, never date: `:2048`;
     - a version git cannot place stands on neither side: `:2173`;
     - gate times on the runs compared: `:2012` (see M2);
     - open, dropped, no commit, commit missing from the checkout, no fixed issue: `:2157`, `:2093`.
   - **WAY-417's clause.** Each part has a test:
     - Q1 numbers in the version rows: `:1744`, `:1764`;
     - Q1 numbers in the image: `:1709`, `:1836`;
     - Q1 numbers on the sides: `:1974`;
     - Q2 sums in the image and on the sides: `:1709`, `:1974`;
     - Q3 and falls in the version rows: `:1293`, `:1354`, `:1756`;
     - Q3 and falls in the comparison: `:1953`, `:1990`, `:2012`;
     - the image with median and count: `:1709`, `:1836`, and `test_series_summary.py:63`-`292`.
   - **Removed pair parts.** Every removed part is held by one of these tests:
     - WAY-339, complies: median of the cost series and the comparison by versions;
     - WAY-339, violates: date, Q3 or fall in the image, a change with no fixed issue;
     - WAY-417: all of it.
   - **Where the removed parts came from.** `git show 19e5774a:foundations/decisions.md` shows that
     every part removed from WAY-339 was added by this task. Every part left in the pair stood before
     the task, unchanged.
   - `test_series_summary.py` carries no line `decision:`, as M2 notes.
2. **Part map `elements-common`** (`foundations/part_map.md:67`-`68`). No finding.
   - The new words say "the way a skill hands work on to another skill of the-way, which every skill
     that hands work on shares". The file `elements/common/reaching_another_skill.md:3`-`4` makes the
     same universal claim itself: "A skill that hands work on names this file and reads it".
   - 15 skills point to it, across `elements`, `project-level`, `product-guidelines` and
     `foundation-review`. The skills that do not point to it either hand no work on to another skill:
     - `critique`;
     - `maintain-instruction-files`;
     - `audit-process`;
     - or reach another method by its path when the cycle dispatches it, which is not the hand-over
       of WAY-127 (`foundations/decisions.md:3344`-`3348`):
       - `implement-task` and the stage methods, `task-cycle/skill/SKILL.md:70`-`77`;
       - the foundation step, `task-cycle/skill/foundation_step.md:13`-`22`, WAY-368.
   - A purely grammatical note, not graded: "which every skill … shares" could attach to "another
     skill of the-way". The plain reading is the intended one.
3. **The two points the return step put to the orchestrator.**
   - (a) The missing WAY-339 line for the gate-times clause is a finding. It is Minor, M2 above, with
     `Contradiction` not applicable because it is not blocking.
   - (b) "for the times of the gate both take only the runs that WAY-350 compares"
     (`foundations/decisions.md:8632`-`8633`) can be read as "both groups of the comparison" or as
     "the image and the comparison". Both readings are true of the code:
     - the image's median of the compared runs takes only those runs and shows the rest apart
       (`test_series_summary.py:247`-`270`, `test_process_versions.py:1733`-`1740`);
     - each side of the comparison does the same, and its fall is read from the compared runs only
       (`test_process_versions.py:2012`-`2037`, `test_series_summary.py:474`-`507`).

     The *Verification* the step wrote settles the reading as "on both sides". No reading leads an
     agent to wrong code, so this is no finding. I would leave the binding sentence as it is.
4. **No binding sentence changed and no forbidden entry.** The diff touches only the *Verification*
   of WAY-339 and WAY-417 (`foundations/decisions.md:8663`-`8677`, `:9018`-`9027`) and the description
   of one part. Their binding sentences and those of every other entry are unchanged. No entry was
   added. The removal of the pair is the return step's own rule (`task-cycle/skill/return_step.md:18`-`20`)
   and the foundation step's rule for a pair "kept only until a test of the same change holds the
   sentence" (`task-cycle/skill/foundation_step.md:33`-`34`). The correction of the part map falls
   under "the part map of the touched parts". The form of both *Verification* fields follows the
   template (`elements/decisions/template.md:278`-`304`): a clause `tests:` with no path, no test name
   and no number, and WAY-339 keeping its invariant and "For the rest" pair, as WAY-61 does.

## Declined to judge

- WAY-350's own version-against-version gate tests (`process-audit/test_process_versions.py:1354`,
  `:1502`) carry no line `decision:` for WAY-350. That entry is neither written nor corrected by the
  return step, and the lines are not in this range. Out of scope; it is related to M2 only where
  WAY-417 relies on them.
- The `gate_times.py` reading of nested output, and the claim of the return-step report that WAY-350
  matches it. No sentence in this range rests on it.

## Checks run

| Check | Command | Exit code / result |
|---|---|---|
| Head confirmed | `git rev-parse HEAD` | `1eaa3c4faae3e678abbd6774560a6d75607afa1b` |
| Diff and log of the range | `git diff 5d160f9d..1eaa3c4f`, `git log --oneline 5d160f9d..HEAD` | one commit, two files |
| Foundation check at head | `python -B elements/common/foundation_check.py` | 0, `0 errors` |
| Tests that the clause `tests:` rely on (pure) | `python -B -m unittest process-audit/test_series_summary.py` | 0, 49 tests OK |
| Tests that the clause `tests:` rely on (count) | `python -B -m unittest test_process_versions.SeriesImages test_process_versions.SeriesComparisons` (cwd `process-audit`) | 0, 18 tests OK in 51 s |
| The removed pair added by this task | `git show 19e5774a:foundations/decisions.md`, WAY-339 *Verification* | the head's *Verification* equals the task base's plus the new clause `tests:` |
| Stale references to the removed pair | `git grep -n -i "verification of WAY-" -- '*.py' '*.md'` | one hit, M1 |
| Which skills point to the shared hand-over file | grep of `reaching_another_skill` over every tracked `SKILL.md` outside `.claude/` and `.agents/` | 15 point to it; 8 do not (see point 2) |
| Worktree untouched | `git status --short` after the checks | clean |

## Reaches beyond the handoff

- WAY-12, read whole (`foundations/decisions.md:766`-`822`): the rule that a test holding a sentence
  carries the line; needed for M2.
- WAY-127's binding sentences and *Verification* (`:3329`-`3378`): what "hands … on" means, for point 2.
- WAY-61's and WAY-69's *Verification* by search excerpt: the form of the field.
- `task-cycle/skill/SKILL.md` lines 5-20, 60-80 and 220-260, `task-cycle/change/SKILL.md` lines 5-14 and
  `instruction-files/SKILL.md` lines 110-120: whether these skills hand work on (point 2).
- WAY-339's *Verification* at `19e5774a`: which pair parts this task added.
- `process-audit/test_process_versions.py` lines 1285-1300 and 1354-1362: the version-row fall tests.

## Working copies

`.runs/review-return-step/`, holding
only the log of the focused test run. It was removed with `rm -rf` by its full path. No worktree was
made.

**Unread material:**
- `process-audit/test_process_versions.py`: read lines 1600-2214, plus 1285-1300 and 1354-1362 and the
  hits of the `decision:` search; not the whole file.
- `elements/decisions/template.md`: read the section "Verification" (lines 263-304) and the hits of the
  search for "Verification", WAY-61 and WAY-69; not the whole template.
- WAY-61 and WAY-69: only their *Verification* by excerpt, not whole.
- WAY-127: its binding sentences and *Verification*, not its whole *Rationale* and *Rejected*.
- The return step's own unread passages, which I did not read either: the full diff of
  `process-audit/audit_report.py` and `process-audit/version_analysis.py`, and
  `task-cycle/test_gate_times.py`. No sentence of this range rests on them.
- `process-audit/series_summary.py` was not read; its behaviour was judged through its tests, which I
  ran.

**Searches not found or unclear:**
- No line `decision:` in `process-audit/test_series_summary.py`, which the handoff names as a test the
  clauses `tests:` name (M2).
- No line `decision: WAY-339` at the one test that holds WAY-339's gate-times clause (M2).

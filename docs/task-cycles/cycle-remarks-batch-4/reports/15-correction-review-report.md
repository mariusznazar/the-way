PASS 10d443fa64e4b21d6bf63c0140ab6cecf1ab1f96

# Review of the correction made for the human's remarks, cycle `cycle-remarks-batch-4`

Variant: a correction made for the human's remarks (`task-cycle/review/fix.md`, read whole). Range
`14b7680750c48e0c173291fec8223dd7c30b0655..10d443f`; `git rev-parse HEAD` =
`10d443fa64e4b21d6bf63c0140ab6cecf1ab1f96`; one commit; `git diff 14b7680..HEAD` and `git log --stat`
computed myself. The remarks `reports/11-correction-remarks.md` (R1-R3) bind; the handoff
`reports/12-correction-handoff.md` and the report `reports/13-correction-report.md` read whole.

## Each remark

- **R1.1 (WAY-71 *Scope* gains `task-cycle`): made.** `foundations/decisions.md:1688-1689`.
- **R1.2 (the rule that a gate fix's range is compared goes into WAY-160's *violates* example, the
  *complies* sentence untouched): made.** `foundations/decisions.md:4582-4583` adds "the gate fails, its
  fix changes code, and the return step does not compare the fix's range" to the *violates* list; the
  *complies* sentence is not in the diff.
- **R2 (route B): made, with one gap of the script described under N-1.**
  - Same descriptive form in the three fields: WAY-71's binding sentence (`:1678-1685`) and
    `elements/common/rules.md:20-24` carry one sentence with the three forms; the decision template
    (`elements/decisions/template.md:28, 51-55`) gives *Based on* its form and says *Relations* and *Origin*
    never read `TODO`; the invariants template's *Links* bullet (`elements/invariants/template.md:122-127`)
    names both forms and the error for the bare word; its form lines 44-45 already had both.
  - The request shows each gap: WAY-287 (binding sentence `:9088-9094`, *Verification* `:9110-9122`,
    rationale `:9134-9137`) and item 15 of `task-cycle/skill/request_template.md:249-257` cover the three
    fields, on the tree after the change, one item for each gap, "Merge with the gap?".
  - WAY-71's *Rationale* is rewritten for the three fields; the *Rejected* line is added and the two earlier
    ones kept; *Verification* reads true (see (2) below).
  - The script: `elements/common/foundation_check.py:107-113, 409-420, 423-440` (`missing_thing`) reads
    *Rests on*, *Derives from* and *Based on* in whole when the value begins with `TODO`, reports a bare
    `TODO` with the field's hint, and `DECISION_WORDS` (`:116-120`) rejects a value that begins with `TODO`
    in *Relations* and *Origin*. Tests `test_foundation_check.py:636-701`.
- **R3 (what does not change): kept.** Item 15 still covers the whole tree after the change and says a
  request carries the item while an old gap stands; the gate order, steps 10 and 11 and the other items
  are not in the diff (`SKILL.md` untouched; `git diff --stat` shows seven files, none of them).

## The four judgments the handoff asked for

**(1) The script says what the rule says and rejects no entry the rule allows: yes, with one
exception that is a gap in the rule too (N-1).**
- `python -B elements/common/foundation_check.py .` on this tree: exit 0, "0 errors".
- Read-only `python -B elements/common/foundation_check.py <the loop2 checkout>`: exit 1, one error,
  `foundations/invariants.md:1244: *Rests on* reads `TODO` and names no fact`, the bare `TODO` that the
  task's *Out of scope* names for loop2's own update. Nothing about *Based on*, *Derives from*,
  *Relations* or *Origin*. loop2's worktree was not changed (`git status --short` empty).
- The descriptive form in each of the three fields passes with a comma, with ` · `, with a decision
  number or an identifier inside, in backticks, and over two lines; the projected-mode form of the
  invariants skill (`TODO — <the decision's question>, projected in <path>`, `elements/invariants/skill/SKILL.md:60`)
  begins with `TODO` and a description, so it passes. Bare forms fail with the field's hint; values that do
  not begin with `TODO` are read as before (the older tests pass unchanged).
- The new tests fail without the code: the old `foundation_check.py` of `14b7680` with the new test file gives
  `FAILED (failures=15)` (the author reports 14; I count the subtests).

**(2) Each form of `TODO` agrees: yes.** The three forms are the same text in WAY-71's binding sentence,
`rules.md`, the decision template (*Based on*), the invariants template (lines 44, 45 and the *Links*
bullet), WAY-287's *Verification* examples, item 15, and the `MISSING` table of the script
(`foundation_check.py:111-113`): `TODO — <the fact, with its source>` (*Rests on*),
`TODO — <the decision, and where it is expected>` (*Derives from*), `TODO — <what is missing, with its
source>` (*Based on*). WAY-71's *Verification* *complies* examples (`Based on: TODO — <what is missing,
with its source>`, `Derives from: TODO — <the decision, and where it is expected>`) are now true, which
settles M-4 of my first review. The glossary template (`TODO` in *Not*, never on the main branch), the
fact template (*Source* takes no `TODO`) and the part-map template (no `TODO`) say nothing that conflicts,
since the rule speaks only of the three fields.

**(3) The reason WAY-71's *Rationale* gives for *Relations* and *Origin* (`foundations/decisions.md:1709-1711`):
"what an author states about the entry itself when writing it, so a gap there is a field left unfilled,
never a thing the foundation lacks" - true enough and not needed for the rule to stand.** *Origin* names
where the reasoning lives and *Relations* the decisions this one derives from or narrows; both are known to
the author when the entry is written, so a `TODO` in them means the author did not fill the field, which is
what `none` ("a statement, not a blank", `rules.md:18-19`) already forbids. "Never a thing the foundation
lacks" is a little stronger than it must be (a relation to a decision written in the same change is not a
gap, and a relation to one not written has no use), but I find no case where it is false. The sentence is
the author's wording, flagged as such in the report, and the human should read it; it blocks nothing.

**(4) The earlier decisions stand: yes.** Item 15 reads "the invariants file and the decision log of the
tree after the change", "the change writes it, keeps it or does not remove it", "a request therefore carries
one such item for as long as an old gap stands"; WAY-287's binding sentence says "stands on the main branch
after the change". WAY-71 and `rules.md` keep "a change that leaves one there puts it before the human".
WAY-160's *complies* sentence, step 10 and the order of the gate are untouched.

## Findings

### Critical, Important

none.

### Minor

**N-1 (new). A list in *Rests on* or *Derives from* that holds an existing entry and a `TODO` is read the
other way round from the rule: the bare `TODO` item passes, the described one fails for *Rests on*
(`elements/common/foundation_check.py:409-420`, `:427-440`; docstring `:39-46`).** I ran
`foundation_check.py` on a scratch copy of `foundations/` with `script-imports` edited:
`Rests on: python-stdlib-modules · TODO` gives no error; `Rests on: python-stdlib-modules · TODO — a second
fact, from the vendor` gives two errors ("`TODO — a second fact` is no identifier of a fact", "`from the
vendor` is no identifier of a fact"); `Derives from: WAY-38 · TODO — a second decision, expected in the next
task` and `WAY-38 · TODO` give none; `Derives from: TODO` gives the bare-`TODO` error. The rule (WAY-71,
`rules.md:20-24`) gives only the form where the whole value is `TODO — ...`, which leaves unsaid how an
invariant that rests on one fact the foundation holds and one it lacks is to be written; WAY-17 says every
link is written, so dropping the existing fact is not an answer. The script's docstring now documents the
`clock-tick · TODO` half (it was added to the docstring in the fix of the first round). Why it matters: the
one realistic mixed case cannot be written in the described form for *Rests on*, and the bare word, which
the rule forbids, is the form that passes. It is an issue of the rule more than of this diff, and the remarks
did not settle it (R2 says "a value that begins with `TODO`"), so it lies outside the correction and outside
the task; it blocks nothing. Suggested: a decision of the human on mixed values (either read the part after
`·` that begins with `TODO` as a description, or say in the rule that the field holds the whole `TODO — ...`
and the existing fact stands in the description).

### Out of scope

N-1 as said above. Nothing else.

## Declined to judge

- Whether the-way's other products hold a bare `TODO` in *Derives from* or *Based on* (the script now
  rejects it): the-way and loop2 hold none (counted above); a product I cannot read is the human's concern
  at the pin move.
- The wording of the item for the human in the description of the request: the orchestrator's.

## Checks

| Command | Exit | Result |
|---|---|---|
| `git rev-parse HEAD`; `git status --short` (reviewed worktree) | 0 | `10d443f...`; clean |
| `python -B elements/common/foundation_check.py .` | 0 | 0 errors |
| `python -B elements/common/foundation_check.py <the loop2 checkout>` (read-only) | 1 | one error: loop2's bare `TODO` in *Rests on* at `foundations/invariants.md:1244` |
| `python -B gate/run_tests.py task-cycle` | 0 | 238 tests, OK |
| `python -B gate/run_tests.py elements/common` | 0 | 130 tests, OK |
| `python -B gate/run_tests.py instruction-files` | 0 | 104 tests, OK (5 skipped) |
| `python -B gate/run_tests.py agent-instructions` | 0 | 18 tests, OK |
| `python -B gate/run_tests.py installation` | 0 | 44 tests, OK |
| `python -B -m unittest test_foundation_check` with the `14b7680` version of `foundation_check.py` and the new tests (scratchpad copy) | 1 | `FAILED (failures=15)`: the new tests fail without the code |
| `python -B -I mix.py` (scratchpad `a scratch file in the agent session's scratch directory`): five values of *Rests on* and *Derives from* on a scratch copy of `foundations/` | n/a | results under N-1 |
| Manual: the three forms compared across WAY-71, `rules.md`, the two templates, WAY-287, item 15 and the script's `MISSING` table | n/a | agree |

`python -B gate/run_tests.py installation` finished after the report was first written: exit 0, 44 tests,
OK. The full gate is the orchestrator's; I did not run it.

## Reaches beyond the dispatch

- `elements/invariants/skill/SKILL.md:55-62` (the projected form of *Derives from*) and
  `elements/decisions/skill/*.md`, `elements/common/*.md` by a search for `TODO`: to check that no text
  states the old "only in *Rests on*" rule or conflicts with the three forms. None found.
- `elements/common/foundation_check.py:455-505` (how `DECISION_WORDS` is applied) and a search of the
  repository's `*.py` for "Based on" and "Derives from" to find other readers of the two fields
  (`migrate_foundation.py` reads them only for the earlier form).
- `<the loop2 checkout>` (read-only, by the script only).

## Unread material

The remarks, the handoffs, the author's report, the diff, the entries the correction writes (WAY-71,
WAY-160 and WAY-287 whole) and `fix.md`: read whole. The entries named for consistency: WAY-17, WAY-58,
WAY-05, WAY-33 and WAY-263 were read whole in the amendment to `reports/04-review-report.md` and I did
not open them again for this review; `elements/common/rules.md` whole, `elements/decisions/template.md`
lines 20-80 and the invariants template lines 36-56 and 118-130 read, not the whole templates again; the
part-map entries `decisions`, `elements-common`, `task-cycle` read whole in the first review and not again.
No new foundation selection was made for this review: the decisions read in the first review (64 whole,
109 by title) stand.

## Searches not found or unclear

- Whether the rule means that a mixed list (an existing entry and a missing one) may hold a `TODO` item:
  unclear in WAY-71 and `rules.md`; see N-1.

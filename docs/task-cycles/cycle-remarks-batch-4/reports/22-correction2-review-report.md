PASS 1c1e8c80e2fef0f5d04f6671ff49122bb461fc86

# Review of the second correction made for the human's remarks, cycle `cycle-remarks-batch-4`

Variant: a correction made for the human's remarks (`task-cycle/review/fix.md`). Range `98e2d86..1c1e8c8`;
`git rev-parse HEAD` = `1c1e8c80e2fef0f5d04f6671ff49122bb461fc86`; one commit; `git diff 98e2d86..HEAD`
and `git log --stat` computed myself. The remarks `reports/18-correction2-remarks.md` (S1, S2) bind; the
handoff `reports/19-correction2-handoff.md` (not opened: the review handoff `21-...` carries what the
author was asked, and the remarks bind), the author's report `reports/20-correction2-report.md` and the
review handoff `reports/21-correction2-review-handoff.md` read whole.

## Each remark

- **S1 (route 1 for the mixed value, in all three fields): made, with one trap in the script (N-1).**
  - Script: `elements/common/foundation_check.py:219-230` (`todo_item`) finds the first item of the value
    that begins with `TODO`, with ` · ` as the separator and quotation marks masking a ` · ` and a `TODO`
    inside them; `:425-438` (`known_part`) cuts the value before that item, reports a `TODO` with no
    description with the field's hint on the line of that item, and returns the known part, which the
    callers at `:447-460` read exactly as before (identifiers, facts, quoted sources, decision numbers).
    So the known entry stays checked as a reference, the description is read by nothing and runs to the
    end of the value, and a bare `TODO` in the last position is an error, in *Rests on*, *Derives from*
    and *Based on*. Docstring `:39-48` says the same.
  - Words: WAY-71 binding sentence (`foundations/decisions.md:1684-1687`) and `elements/common/rules.md:20-26`
    carry the same added clause; WAY-71 *Verification* has a *complies* case (`Rests on: <the known fact> ·
    TODO — <the missing fact, with its source>`) and a *violates* case (`:1698-1703`); *Rationale* gives the
    reason (every link is written, WAY-17, and a named item stays checked as a reference; `:1714-1717`); both
    templates say it (`elements/invariants/template.md:127-131`, `elements/decisions/template.md:54-58`);
    WAY-287 *Verification* has the mixed case (`:9124-9125`); item 15 of
    `task-cycle/skill/request_template.md:254-256` says a closing `TODO` after known entries is one gap,
    shown with the missing part alone.
  - Tests: 14 new methods for the three fields (`test_foundation_check.py:702-798`): known entry then
    described `TODO` passes (with a comma, with ` · `, with a decision number or a fact-like word in the
    description); known entry then bare `TODO` (three forms) fails with the hint and the line; a known
    entry that does not exist still fails as a reference; `TODO` first reads the rest as description; a
    quoted source with a `TODO` or ` · ` inside is no `TODO` item. With the `98e2d86` version of
    `foundation_check.py` and the new test file: `FAILED (failures=18)`, so the tests do not pass without
    the code.
- **S2 (what does not change): kept.** `git diff` shows no change to WAY-160, to the *Scope*, to the
  rejection of `TODO` in *Relations* and *Origin* (`DECISION_WORDS` untouched), to the whole-tree reading
  of item 15 or to the gate order. The request's item 6 (the mixed case) goes with this correction: the
  orchestrator's to take out of the description, not a file of this range.

## The four judgments the handoff asked for

**(1) The script does what route 1 says in all three fields and rejects nothing the rule allows: yes for
the ` · ` form; the scratch runs are below and N-1 is the trap in the others.** I ran
`foundation_check.py` on a scratch copy of `foundations/` (own git repo; 27 errors of the copy's own, which
I subtracted) with the values of my N-1 and more (script `...\scratchpad\rv\mix2.py`, output
`...\rv\mix2.out`). Results, with `·` for the separator:

| Field | Value | Result |
|---|---|---|
| *Rests on* | `python-stdlib-modules · TODO` | error with hint, line 121 |
| *Rests on* | `python-stdlib-modules · TODO — a second fact, from the vendor` | no error |
| *Rests on* | `python-stdlib-modules · TODO — a second fact · from the vendor` | no error |
| *Rests on* | `TODO — a second fact · python-stdlib-modules` (`TODO` first, more after) | no error (all description) |
| *Rests on* | `python-stdlib-modules · no-such-fact · TODO — x` | `no-such-fact` names no fact (reference still checked) |
| *Rests on* | `python-stdlib-modules ·TODO — tight` (no blank after `·`) | no error |
| *Rests on* | `python-stdlib-modules · "a · TODO b"` (quotes in *Rests on*) | two errors, as quotes are no *Rests on* syntax; as before |
| *Derives from* | `WAY-38 · TODO — the decision on x, expected next` | no error |
| *Derives from* | `WAY-38 · TODO` and `WAY-38 · TODO —` | error with hint, line 122 |
| *Derives from* | `WAY-38 · WAY-999 · TODO — y` | `WAY-999` names no decision of the log |
| *Derives from* | quoted source with `· TODO` inside quotation marks, then `· WAY-38` | no error (no `TODO` item) |
| *Based on* | `python-stdlib-modules · TODO` | error with hint, line 16 |
| *Based on* | `python-stdlib-modules · TODO — the source of the save format, once the vendor answers` | no error |
| *Based on* | quoted source with `· TODO` inside, then `· python-stdlib-modules` | no error |
| *Based on* | quoted source with `, TODO` inside, then `· TODO — more` | no error |
| *Based on* | `TODO — a · TODO` | no error (the second is in the description) |

On the-way: `python -B elements/common/foundation_check.py .` exit 0, "0 errors". Read-only on loop2:
exit 1, one error, the bare `TODO` in *Rests on* at `foundations/invariants.md:1244` that the task names; no
other entry of loop2 is affected (its worktree is unchanged: `git status --short` empty).

**(2) Every place that states the form agrees: yes.** WAY-71 binding sentence and `rules.md` carry the same
clause word for word (the diff shows the same text in both). The templates give the same example
(`<fact> · TODO — <…>`) and the same sentence that the description runs to the end of the value so a comma or
` · ` inside it joins nothing. WAY-287's binding sentence is unchanged ("each descriptive `TODO` ... that
stands on the main branch after the change") and covers the mixed value, its *Verification* and item 15 say
so. The script's `MISSING` table (`foundation_check.py:111-113`) and docstring give the same three forms.
The glossary, fact and part-map rules about `TODO` concern other fields and say nothing conflicting.

**(3) `clock-tick, TODO — x` (a comma, or a newline, before the `TODO` item) leaves a trap: yes, a small one
(N-1).**

**(4) The first round's and the first correction's decisions stand: yes.** Item 15 still reads the whole
tree after the change and says a request carries the item while an old gap stands; the three fields, the
rejection in *Relations* and *Origin*, WAY-71's *Scope*, WAY-160's *violates* example are not in the diff.

## Findings

### Critical, Important

none.

### Minor

**N-1. A bare `TODO` after a comma or a line break instead of ` · ` still passes in all three fields, and
the described one after a comma gives a misleading error
(`elements/common/foundation_check.py:219-230`, `todo_item`; the separator is ` · ` alone).**
Scratch runs (same method as above):
- *Rests on*: `python-stdlib-modules, TODO` gives no error; `python-stdlib-modules` + line break +
  `  TODO` gives no error; `python-stdlib-modules, TODO — a second fact` gives "`TODO — a second fact` is no
  identifier of a fact" (no hint to write the item after ` · `); with a comma inside the description
  (`..., TODO — a second fact, more`) there are two such errors.
- *Derives from*: `WAY-38, TODO` gives no error.
- *Based on*: `python-stdlib-modules, TODO` gives no error.
Why it matters: S1 says a bare `TODO` in the last position is an error "in all three fields", and the rule
(WAY-71, `rules.md`) states the bare word is an error; the form passes silently when the author separates
with a comma, which the script already accepts between facts in *Rests on* (`located` splits on `·`, `,` and
line breaks), so the author who writes `fact-a, fact-b, TODO` is not told. The templates and the rule give
the ` · ` form, and the author's note says the same, so this needs a deviation from the form and is a
trap rather than a defect of the stated rule: Minor. Within the correction (it is about the reading S1
asks for) and it blocks nothing. Fix, for the human's choice: let `todo_item` look for the first item that
begins with `TODO` over the same separators the field's known part is read with (`·`, `,` and line breaks
in *Rests on*; `·` in the other two, where a comma is no separator), or state in the three templates that
the items are joined by ` · ` alone and add an error for a `TODO` standing after a comma.

### Out of scope

none.

## Declined to judge

- Whether the-way's other products hold a mixed or bare `TODO` the script now reads differently: the-way
  and loop2 hold none beyond loop2's known bare `TODO` (counted above); a product I cannot read is for the
  pin move.
- The wording of the request's description (item 15 of the description, the removed item 6): the
  orchestrator's.

## Checks

| Command | Exit | Result |
|---|---|---|
| `git rev-parse HEAD`; `git status --short` (reviewed worktree) | 0 | `1c1e8c8...`; clean |
| `python -B elements/common/foundation_check.py .` | 0 | 0 errors |
| `python -B elements/common/foundation_check.py <the loop2 checkout>` (read-only) | 1 | one error: loop2's bare `TODO` in *Rests on*, `foundations/invariants.md:1244` |
| `python -B gate/run_tests.py elements/common` | 0 | 144 tests, OK |
| `python -B gate/run_tests.py task-cycle` | 0 | 238 tests, OK |
| `python -B gate/run_tests.py instruction-files` | 0 | 104 tests, OK (5 skipped) |
| `python -B gate/run_tests.py agent-instructions` | 0 | 18 tests, OK |
| `python -B gate/run_tests.py installation` | 0 | 44 tests, OK (277 s; I waited for it to finish) |
| `python -B -m unittest test_foundation_check` with the `98e2d86` `foundation_check.py` and the new tests (scratchpad copy) | 1 | `FAILED (failures=18)` |
| `python -B -I mix2.py` (scratchpad `a scratch file in the agent session's scratch directory`): 27 values of the three fields on a scratch copy of `foundations/` | 0 | table under (1) and N-1 |
| Manual: the forms compared across WAY-71, `rules.md`, both templates, WAY-287, item 15, the docstring and the `MISSING` table | n/a | agree |

Not run: the full gate (the orchestrator's).

## Reaches beyond the dispatch

- `elements/common/foundation_check.py:120-160, 400-470` (the field readers `fields`, `located`,
  `based_on`, `unquoted`, and the callers of `known_part`), to see what separators each field is read with.
- `<the loop2 checkout>`, read-only, by the script only.
- The search of the repository for other statements of the rule (grep for `TODO` over `elements`,
  `task-cycle`, `project-level`): none found beyond those the author lists.

## Unread material

The remarks, the author's report, the review handoff, the diff, `fix.md` and the entries the correction
changes (WAY-71 and WAY-287 whole, in the first review and at the changed places now) read. The entries
named for consistency (WAY-17, WAY-160, `rules.md`, the two templates, item 15): WAY-17 and WAY-160 read
whole in the earlier reviews and not again; `rules.md` whole; the templates and item 15 read at the
changed places and the passages around them, not again from the first line. No new foundation selection
was made for this review: the 64 decisions read whole and 109 by title of the amendment to
`reports/04-review-report.md` stand. `reports/19-correction2-handoff.md`: not opened.

## Searches not found or unclear

- Whether the separator of the items of *Rests on* is ` · ` alone or also a comma and a line break:
  the templates give ` · `, the script reads commas and line breaks too for *Rests on* (`located`); see N-1.

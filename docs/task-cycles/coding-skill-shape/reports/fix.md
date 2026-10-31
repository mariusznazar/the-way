# Report of the fix - coding-skill-shape

**Status:** done. **Commit:** `088717a` on `task/coding-skill-shape` (fix base `097123e`), author address
`mariusznn@gmail.com`, worktree clean, not pushed. Files changed: `product-guidelines/coding/task_document.md`,
`product-guidelines/coding/settle.md`, `foundations/decisions.md` (WAY-216 *Rationale* only).

## Finding 1 - outcome: fixed as the review proposed

- `task_document.md:3-5` now reads: on the route of one kind, take from the items below what concerns that kind, as
  "The route of one kind" in `SKILL.md` gives: its file with the index row, the test of each new invariant it settles,
  its choices and what the comparison found. It no longer says "only ... of the items below".
- `settle.md:3-4` now reads: settle of the choices and invariants below only what the rule gives; the critique below
  stands. `hand_back.md` is unchanged ("check only", as the review says it fits).
- Route 6 walked again, `SKILL.md` to `hand_back.md`:
  - Step 1 `recognize.md` gives the one-kind mode. Step 3: coding template, then `kinds.md` alone (one kind, comparison,
    `copy`/`do not copy` with file and line). No `starting_set.md`, `research.md`, `trial_run.md`.
  - Step 4 reads the general template, `settle.md`, `task_document.md`. Of `task_document.md` it **takes**: *To do* - write
    or extend `guidelines/coding.md` (the index row) and `guidelines/coding-<kind>.md`; the test of each new invariant
    the route settles (the rules a script checks of the exemplar); *Questions to settle* - the kind's identifier, exemplar,
    file status, script-checked rules, invariants; *Context* - what the comparison found, each `do not copy` file with file
    and line; *Settlements to record*. It **leaves**: the tool-install item, the one-reformatting item, the root `AGENTS.md`
    pointer, the part-map items, "first guidelines" item, the trial-run evidence and research sources of *Context*, and the
    audit item.
  - Step 4 `settle.md`: it **takes** the kind's exemplar/status/script-rule item, the invariant items for script-checked
    rules and further rules that a cheap test checks, and the **Critique** (the opening says it stands); it **leaves** the
    standing-check adoption decisions (WAY-202), linter/formatter/audit items, the template adoption decision, the
    linter-only invariants, the weak points of no-code and dependency audit, and `new_tools.md` unless a tool is left as a
    question. Step 5 `hand_back.md`: it checks that the document holds what `task_document.md` names *for this kind*, and
    the human's words; it **leaves** the check of the adopting decision of each standing check.
- The invariant test and the `do not copy` places therefore reach the cycle's author, which was the example of the finding.

## Finding 2 - outcome: fixed

The first clause of the WAY-216 *Rationale* ("Research and a trial run answer a new scope ...") is gone. It is replaced
by what rows 2 and question 3 keep: without the third sentence every task that creates a kind's first file could pull
research of all the standing checks; an agent on the comparison goes on improvising and may make a full audit. The
sourced last clause stays ("a task that is an extension for another reason keeps its research (WAY-211)"). Nothing is said
of why a trial run exists. *Verification* and *Rejected* untouched (the "complies/violates" sentence says the comparison
runs no linter's set, as the binding sentence does; the binding sentence is unchanged).

## Checks (command, exit code)

| Check | Result |
|---|---|
| `python -B elements/common/foundation_check.py` | exit 0, 0 errors |
| `python -B instruction-files/check_instructions.py .` | exit 0; output identical to the base's (`check_base.txt` vs `check_after.txt`) |
| `python -B tools/check_assessment.py reports/assessment.md` (after regenerating the assessment) | exit 0, 56 rows, 249 lines, 0 problems |
| `python -B tools/verify_counts.py reports/word-counts.md` (after the last change to a counted file) | exit 0, 346 figures, 0 differ |
| `python -B gate/run_tests.py installation` | see the last line of this report |
| whole gate | not run |

`assessment.md`: the "Text added that no base line carries" row for `settle.md`/`hand_back.md`/`task_document.md` now quotes the
new openings and names what they leave standing. Sentences compared again: still 13 base sentences differ, the same 13.

## Final figures

Words of the changed files: `task_document.md` 509 (was 489), `settle.md` 635 (was 629), `hand_back.md` 113, `SKILL.md` 1499.
Routes, from `word-counts.md` (before step 4 / total / total without the first reading, after):

| Route | After |
|---|---|
| 1 | 8620 / 11267 / 7876 (-22.4%) |
| 2 | 7592 / 11070 / 7679 (-23.7%) |
| 3 | 9064 / 11711 / 8320 (-19.3%) |
| 4 | 8036 / 11514 / 8123 (-20.7%) |
| 5 | 5300 / 10890 / 7499 (-25.0%) |
| 6 | 7607 / 11085 / 7694 (-23.6%) |
| 7 | 8733 / 11380 / 7989 (-21.6%) |

The "before" figures are unchanged (14511 / 14002 to step 4; 14511 total). The text beside the template is now 4136 + 26 = 4162
words.

## Searches not found or unclear

None new. The unclear points of `author.md` stand (the reading of "the wider mode governs" for the one-kind mode with "A new
kind").

`python -B gate/run_tests.py installation` after the fix: exit 0, 44 tests OK.

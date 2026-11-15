PASS 2e834471fdf73c047b5a547ea6b373b70a23724a

# Review of correction 2 (the human's answer (a) to the blocking item)

Range `9a00830..2e83447`, one commit. `git rev-parse HEAD` in my worktree:
`2e834471fdf73c047b5a547ea6b373b70a23724a`, the head given. The tree of `9a00830` equals the tree of
`dcb1a19` (`git rev-parse 9a00830^{tree}` and `dcb1a19^{tree}` agree). Read from a detached
worktree of `2e83447`, never from the task's working tree.

Method: `task-cycle/review/SKILL.md` and `fix.md`. For a correction made for the human's remarks,
the remarks take the findings file's place. Remarks: `reports/correction-2-remarks.md`. Author's
report: `reports/author-correction-2-report.md`, read as claims to check.

## The remark

**Remark 1 (a) — made, as far as it binds code.** The remark: "remove the debt record (the invariant
`installation-instruction-files-dependency`) and add the instruction-file checker's part to the
installer part's list of allowed dependencies in the part map, citing settlement 5 of the task".

- **The invariant is removed.** `foundations/invariants.md` loses the whole entry (heading, sentence,
  five fields), and nothing else.
  - The file is now identical to the target's (`git diff --quiet 7f5c5a5 2e83447 --
    foundations/invariants.md`, exit 0).
  - `git grep -n installation-instruction-files-dependency` at `2e83447` finds nothing (exit 1).
  - No withdrawn identifier is needed. `elements/common/rules.md:59-61` keeps an identifier only
    where the file held it on the commit the branch left the main branch from; "one that never
    reached the main branch may go". This one was written on the branch, in `dcb1a19`.
- **The dependency is allowed in the map.** `foundations/part_map.md:192-194`, part `installation`,
  *Depends on* now ends "… · task-cycle · foundation-review · instruction-files". It keeps the
  file's form: items joined by ` · `, the separator at the line end, the continuation line indented
  two spaces.
- **Nothing else changed.** `git diff --stat 9a00830 2e83447` lists only these two files. No other
  line of either file changed.
- **The citation of settlement 5.** The commit message cites it: "settlement 5 of the task (row 5,
  line 120 of the frozen task document …)". I checked that line: `task.md:120` is row 5, the
  human's choice, which asks that the one command also run `check_instructions.py`.
  - The part map's form has no place for a source. The template's entry form holds *Files*,
    *Depends on* and *Trust boundary* only, and *Depends on* is "`<identifier> · <identifier> |
    none`" (`elements/part-map/template.md`, form of a part).
  - WAY-11 asks the return step to correct the map; it asks for no reason beside an entry.
  - So the commit message is the one place the foundation's forms leave for the citation, and it
    satisfies the remark.
  - The request's *Foundation entries* will name the changed part-map entry by the template's rule
    for the description. That is the orchestrator's, not this commit's.

The rest of the remark (the return step's comparison, a merge if the target moved, the wait for CI)
is the orchestrator's and outside this range.

## My earlier findings

- **Finding 2 of the review of the merge (installation reaches `instruction-files`): resolved.**
  - The map now allows the reach the task meant: `install.py:201`, `installation/README.md:61` and
    `:82-84`, `test_install.py:145-146` and `:161-168`.
  - No recorded rule contradicts settlement 5.
  - The import allowance of `cross-part-imports` for this pair now comes from *Depends on*, a
    deliberate allowance, not from a debt record.
- **Finding 1 (the CI rule deferring to WAY-261): untouched.** `git diff --stat dcb1a19 2e83447`
  lists only `foundations/invariants.md` and `foundations/part_map.md`. None of the five places of
  the CI rule (WAY-160, step 12 of `SKILL.md`, `correction.md`, `agent-instructions/README.md`)
  changed.
- **Not counted here, by design:** my Minor finding 3 of the merge review, and the Minor finding of
  the review of the fix (unwrapped lines).

## The two parts allowing each other

`instruction-files` lists `installation` in its *Depends on* (`foundations/part_map.md:183`), so
`installation` and `instruction-files` now allow each other. This is no finding:

- **No rule forbids it.** Nothing in `elements/part-map/template.md`, `elements/part-map/skill/SKILL.md`,
  the glossary entry "dependency of a part" (`foundations/glossary.md:37-39`), WAY-225, WAY-44 or
  `foundation_check.py` forbids or orders a mutual allowance. A search for `cycl`, `mutual` and
  `each other` there finds no such rule.
- **What *Depends on* means.** It "names the parts this part may depend on" (`template.md:90`), an
  allowance per part, not an order of builds.
- **The map already holds mutual allowances.** `task-cycle` lists `installation` and `project-level`
  (`part_map.md:107-108`), and each of those lists `task-cycle`.

## Findings

None: no Critical, Important or Minor finding in this correction.

## Declined to judge

- Whether `instruction-files`' own reach to `installation` is still real. That line predates the task
  and the merge and is outside this correction.

## Checks

| Check | Command (from the worktree of `2e83447`) | Exit code / result |
|---|---|---|
| Head | `git rev-parse HEAD` | 0; `2e834471fdf73c047b5a547ea6b373b70a23724a` |
| Base tree equals the reviewed fix | `git rev-parse 9a00830^{tree}` against `dcb1a19^{tree}` | 0; equal |
| Range and files | `git log 9a00830..2e83447`; `git diff --stat 9a00830..2e83447`; `git diff 9a00830..2e83447` | 0; one commit, two files, the lines quoted above |
| Invariants file back to the target's | `git diff --quiet 7f5c5a5 2e83447 -- foundations/invariants.md` | 0 (identical) |
| No reference to the removed identifier | `git grep -n installation-instruction-files-dependency` | 1 (no match, as wanted) |
| Nothing of the fix `dcb1a19` changed beyond the two files | `git diff --stat dcb1a19 2e83447` | 0; the same two files |
| Foundation check | `python -B elements/common/foundation_check.py` (without `--skip-test-citations`) | 0; `0 errors` |
| Tests | `python -B gate/run_tests.py elements/part-map` | 0; 39 tests, OK |
| Tests | `python -B gate/run_tests.py elements/common` | 0; 235 tests, OK |

The full gate was not run, as the handoff and the method give.

## Reaches beyond the dispatch

- `elements/common/rules.md:57-66` ("Withdrawn identifiers"): whether the removed identifier must
  stay as withdrawn.
- `foundations/part_map.md:101-108` and `:175-184` (parts `task-cycle` and `instruction-files`):
  for the mutual allowance and its precedent.
- `.runs/task-cycles/ci-on-merge-requests/task.md:120`: the settlement the commit message cites.
- WAY-11 whole: I read it in the review of the fix (`foundations/decisions.md:5386-5431`), and it
  is unchanged in this range. It asks the return step to correct the part map and gives no field
  for a reason.

## Working copies

- A detached worktree of `2e83447` at
  `.runs/review-correction-2/wt`, and the check
  outputs beside it in `.runs\review-correction-2\`: removed (see the return). Nothing was kept in
  `reports/`.

## Unread material

- `elements/part-map/skill/SKILL.md` was read at lines 30-48 only, not whole.
- WAY-44 and WAY-225 were not reopened in this review. I read WAY-225 whole in the merge review, and
  it is unchanged since. WAY-44 was searched for a rule on mutual allowances by word only.

## Searches not found or unclear

- A rule against two parts allowing each other: not found in the part-map template, its skill, the
  glossary, WAY-225, WAY-44 or `foundation_check.py`.
- A place in the part map's form for the source of an allowed dependency: not found. The citation
  stands in the commit message.

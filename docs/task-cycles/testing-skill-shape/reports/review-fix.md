PASS c17f4f83b23824fca5e69b52df785d3b1763c65e

# Review of the fix — maintain-testing-guidelines in the WAY-256 shape

Fix range `5dc4b3b..c17f4f8`, one commit, five files, Markdown only. `git rev-parse HEAD` is the head given, and the worktree is clean. Paths are relative to the worktree `C:/Storage/repos/the-way/.runs/worktrees/testing-skill-shape`. The findings file bounds this review.

Result: all five blocking findings fixed, none contested, no new Critical or Important finding. One new Minor. The Minor findings 6 to 10 of `reports/review.md` stand unfixed, as the method gives (WAY-161); none of them reopens the review.

## The findings

| # | Finding | State | Evidence |
|---|---|---|---|
| 1 | Stale word counts | **fixed** | My own recomputation from `c17f4f8` equals every figure of `word-counts.md`, below. |
| 2 | The mode "tests at a level its cycle chooses" | **fixed** | The clause is gone from `recognize.md:21-22` and `SKILL.md:97-98`. The sentence stands in `settle.md:15-18`. |
| 3 | "Extend what exists" in the file of step 1 | **fixed** | The bullet stands at `SKILL.md:60-62`, verbatim, and no longer in `recognize.md`. |
| 4 | Four binding sentences in WAY-256 | **fixed** | Three now, by my count of the log; WAY-256 left the list of entries above three. |
| 5 | WAY-265's exemption | **fixed** | The exemption is worded by file; the styleguide's step and variant files are unchanged. |

### 1. Word counts

Recomputed with `.split()` from each file at `c17f4f8`, the base `SKILL.md` from `00c0a74`, for every line of every route's lists. No listed count differs from its file, and the summary equals the sums:

| Route | Before: to step 4 / total | After: to step 4 / total | Change | After without the first reading |
|---|---|---|---|---|
| 1 | 14120 / 14120 | 8791 / 11272 | -20.2% | 5956 / 8437 |
| 2 | 13611 / 14120 | 7728 / 11040 | -21.8% | 4893 / 8205 |
| 3 | 14120 / 14120 | 9021 / 11502 | -18.5% | 6186 / 8667 |
| 4 | 13611 / 14120 | 7958 / 11270 | -20.2% | 5123 / 8435 |
| 5 | 13611 / 14120 | 7647 / 10959 | -22.4% | 4812 / 8124 |
| 6 | 14120 / 14120 | 8889 / 11370 | -19.5% | 6054 / 8535 |

The fix report says the new comparison of `verify_reports.py` had no negative case, so I ran one: on a scratch copy of `word-counts.md` with `recognize.md` set to 353, the helper reported the mismatch on the listed lines and "sums consistent False". The comparison works. It prints and still exits 0, so its result has to be read, not taken from the exit code.

`author.md` keeps the old figures, which the fix report marks as superseded. It is no material of the request, so this is no defect, but the request has to take its numbers from `word-counts.md`.

### 2. The extra mode

`recognize.md` now skips step 2 only where the recipe stands with an empty *Exemplar*, as To do 3 and `product-guidelines/reading.md:77-78` give, and a level with no recipe takes step 2. The step 3 pointer holds only the required-outcome condition. The literal condition that held on every route no longer exists:

- An audit agent reaches `new_level.md` only where a task's outcome is a first test, so acceptance criterion 5 holds.
- The cycle's-choice sentence is reached on every route through `settle.md`, which every route reads, so criterion 1 holds for it.
- That sentence matches base lines 177-179 word for word; only its closing full stop became the item's semicolon.

In the base it stood under "Where the product has tests", so it now also stands before an agent with no tests. That widens nothing: WAY-242 binds without that condition, and in the base the agent read it anyway, since `SKILL.md` was read whole.

Assessment rows 120 and 174-179 and the "Text added" row say this. Row 120 keeps "REWORD (meaning-preserving)", which now describes what To do 3 gives.

### 3. "Extend what exists"

The three lines match base lines 123-125 word for word, and my sentence comparison no longer lists them apart. `SKILL.md` is read whole, so the rule stands at steps 1, 2 and 4 on all six routes. Assessment row 123-125 now reads KEEP and no longer claims that steps 2 and 4 restate it.

### 4. Binding sentences

The paragraph of WAY-256 has three sentences. I proposed the semicolon myself and read it again in place: "it" in "not bound by it" could now be taken for the third sentence alone. The entry's *Rationale* and *Rejected* both speak of fragments standing today in general, so the wider meaning stays, and row 1's clause holds. No finding.

### 5. WAY-265's exemption

"A step's file that stands unchanged, with the variant file it points to, is not bound by it." `git diff 00c0a74 c17f4f8` shows `starting_rules.md`, `settle.md`, `research.md`, `new_tools.md` and `staged_cleaning.md` of the styleguide unchanged, so the styleguide skill is outside the entry although its `SKILL.md` changed. That matches row 2. A later change to one of those files brings it in, which is what "rebuilt or changed" asks. The *Rationale*'s last clause matches, and no other file repeats the old wording.

## What the fix itself could have broken

### The walk, again, from `SKILL.md`

The fix touches `SKILL.md`, `recognize.md` and `settle.md`, which every route reads, and `new_level.md` on route 5, so I walked all six. All begin `SKILL.md`, `recognize.md`.

| Route | Files after `recognize.md`, in order | Base rules not reached |
|---|---|---|
| 1 | `testing/template.md`, `starting_set.md`, `research.md`, `critique/SKILL.md` with `prepare.md`, `check.md`, `settle.md`; no step 3; `product-guidelines/template.md`, `testing/settle.md`, `task_document.md`, section "Critique before collective review", `hand_back.md` | none needed |
| 2 | as route 1 without `research.md`; the critique files come at step 4 | none needed |
| 3 | as route 1, with `audit.md` after the critique of step 2; `new_level.md` not read | none |
| 4 | `testing/template.md`, `starting_set.md`, `audit.md`, `product-guidelines/template.md`, `testing/settle.md`, `task_document.md`, the section, the critique files, `hand_back.md` | none |
| 5 | `testing/template.md`, `new_level.md`, `product-guidelines/template.md`, `testing/settle.md`, `task_document.md`, the section, the critique files, `hand_back.md` | `audit.md:17-20` (Minor 7 of the first review, unchanged) |
| 6 | `orchestrated_mode.md` before `recognize.md`, then route 1; research and critiques requested from the project orchestrator | none needed |

The order and condition of each pointer hold. "For either" at `SKILL.md:99` still refers to `audit.md` and `new_level.md`.

### What moved, against the base

My sentence comparison gives 18 base fragments not verbatim, against 17 before. The new one is the cycle's-choice sentence cut at its colon, ending in a semicolon. This agrees with the fix report. The other 17 are those of the first review. Head fragments not in the base: 36; the new ones are the rewording of the step 3 pointer and the `settle.md` item, both read above.

### The assessment

All 44 quotes are still literal, the ranges unchanged, and each of the 227 nonblank base lines stands in exactly one row. `recognize.md` no longer appears as the place of "Extend what exists". The Question 3 row's claim that neither agent reads the other's file is true at this head.

## Minor

### 11. "no step 2" beside "modes combine"

**Anchor:** `product-guidelines/testing/recognize.md:17`, `:21-22`

**To paste:** A task that both extends the guidelines and has a first test of a level with a standing recipe takes two modes, one saying step 2 and one saying no step 2. Consider "and no step 2 for it".

**Why:** Finding 2 removed the case that made this collide on every route. What remains is one rare combination, and To do 3 asks for "no step 2" on the route it names. An agent that took it literally there would skip the research WAY-249 requires at every extension. Most agents would keep step 2, since the mode says "the new-level case", so this does not block.

## Declined to judge

- The sentence on the cycle's choice standing inside a list item of `settle.md` rather than as a bullet of its own, a concern of the fix report: the rule is reached at the moment it serves, so the form is the author's choice.
- `author.md`'s old figures: it is no material of the request.
- The six lines of **Declined to judge** in `reports/review.md` stand as written; the fix touches none of them.

## Checks

| Check | Result |
|---|---|
| `git rev-parse HEAD`, `git log`, `git diff --stat` and `git diff 5dc4b3b..c17f4f8`; `git status --short` | exit 0; head as given, one commit, 5 files, clean |
| `python -I -B elements/common/foundation_check.py` | exit 0, 0 errors |
| `python -I -B instruction-files/check_instructions.py .` | exit 0, 0 error, 1 warn (`AGENTS.md:21`, on the base), 3 info |
| `python -I -B agent-instructions/skill_entry_points.py` | exit 0, entry points are current |
| `python -B -m unittest installation.test_testing_guidelines_installation gate.test_skills_reach_the_way_sessions` | exit 0, 4 tests OK |
| own script: every route's list and sum at `c17f4f8` against the files | exit 0; no difference |
| `wc -w` over `product-guidelines/testing/*.md` | agrees with the fix report: `SKILL.md` 1200, `recognize.md` 363, `settle.md` 654, `new_level.md` 62, the rest unchanged |
| own script: quotes, ranges and coverage of `assessment.md` | exit 0; 44 rows literal, 2 proposal quotes literal, 227 nonblank lines each once |
| own script: sentences of base and head, both directions | exit 0; 18 and 36, read as above |
| own script: binding sentences over the log | exit 0; entries above three: WAY-80 and WAY-229 only, both on the base |
| `python -I -B .../tools/verify_reports.py` | exit 0; 46 quotes, no mismatch, sums consistent, 204 counts, no mismatch |
| negative case: a scratch copy of the helper on a scratch `word-counts.md` with `recognize.md` at 353 | the helper reported the mismatch and "sums consistent False"; exit 0, as it never exits otherwise |
| `git diff --quiet 00c0a74 c17f4f8` on the styleguide's step and variant files | exit 0 for all five |
| `grep` for "cycle chooses" and "whose files stand unchanged" over `product-guidelines`, `foundations`, `instruction-files`, `project-level` | the first stands only in `project-level/plan/skill/SKILL.md:123` and `foundations/decisions.md:5997`, on the base; the second nowhere |
| manual: the walk of six routes; each hunk of the fix read against the base | see above |

**Not run:** the whole gate, by the handoff; it is the orchestrator's run. Behaviour of a real agent on these routes is unverified: the walk reads the text.

## Reaches beyond the dispatch

None: the fix's findings and report, its diff, the materials and the files of the walk. The scratch copies of the negative case lie in the session's scratchpad, not in the worktree.

## Searches not found or unclear

none

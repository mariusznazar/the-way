PASS d32f76d7bcc99401fd31b294c09f7ad581d107f8

# Review of the fix — maintain-styleguide in the WAY-256 shape

Range `802b56de85c63afdb8ba5a42c83bd1f5ea060260..d32f76d`, one commit, d32f76d, one file: `product-guidelines/styleguide/recognize.md`, +2 / -1. `git rev-parse HEAD` is the head given. Bound by `reports/findings.md`, as `task-cycle/review/fix.md` gives.

Blocking: 0. Minor: 2, both in the fix report, not in the commit. Out of scope: 0.

## The findings

### Finding 1, the word counts leave out "Reading the foundation": fixed

The section now stands in every route: twice in each "before" list and once in each "after" list, 21 list entries, as `reports/word-counts.md` shows (22 occurrences of the name with line 7). The first reads are 2835 words. `word-counts.md:7` names the four files and sections and says why the before figure stands about 490 words above the estimate of about 8850; 9334 − 8842 = 492 holds.

I recomputed every figure from the file sizes with my own script, not the author's. All 7 summary rows equal my figures, and all 22 file lists sum to what they state. My figures in the findings file differ from these only in the after columns, by the 9 words the fix adds to `recognize.md` (336 to 345), which is right.

Row `:93-96` of `assessment.md` now names the section and says its second reading is counted. The orchestrator's ruling on finding 8's first point stands stated at `word-counts.md:8`.

### Finding 2, `recognize.md` read again the guidelines `refine-task` read: fixed

`recognize.md:10-11` now reads "every file under `guidelines/` that `refine-task` did not read at its step 1". This is the fix the finding proposed, and To do 2's second half now holds for the guidelines as it does for the foundation. Row `:92-92` of `assessment.md` records it as a meaning-preserving reword and keeps it apart from P1, which stands unapplied.

`SKILL.md:65-69` stays as it was. The finding named it only as the sentence that does not cover the case; the exception now stands where the read stands, as it does for the foundation in the next sentence of the same bullet. No finding is contested.

## What the fix itself did

Nothing broken. Checked for the reword:

- **Meaning:** the set of files read after step 1 is the same on every route.
- **Files only inspected:** `reading.md:39` has refine-task inspect the header of every file and read only some whole. A file whose header alone was seen is one refine-task "did not read", so it is still read at step 1.
- **`AGENTS.md`:** the relative clause attaches to `guidelines/`. Refine-task read only its `## Backlog` section, so it is still read whole on either reading.
- **Direct entry (Minor 6 of the first review):** the clause holds there too; a session that skipped refine-task reads every file.
- **Routes:** the walk of the first review stands. Route 7 ends at `recognize.md:4`, before the changed bullet.

## Minor findings

### 1. The fix report gives 233 lines for the base

**Anchor:** `.runs/task-cycles/styleguide-skill-shape/reports/fix.md:36`.

**To paste:** The base `SKILL.md` has 232 lines, not 233. `assessment.md:3` has it right.

**Why I report it:** The report corrects `author.md:76` and says it is the account the request takes (`fix.md:5`), so the number could reach the request. Python's `split` on the newline gives 233 pieces, the last empty; the file holds 232 newlines. The conclusion it supports, 205 nonblank lines each in exactly one row, holds. Comes from the fix report, not from the commit.

### 2. The composition of the 5900 estimate is findable in the task

**Anchor:** `.runs/task-cycles/styleguide-skill-shape/reports/fix.md:35`, `:51`; `.runs/task-cycles/styleguide-skill-shape/task.md:43`, `:45`.

**To paste:** The task gives about 8270 words on the route with no research and no audit, and about 2350 words already read; their difference is about 5900.

**Why I report it:** `fix.md` says the task records no composition and withdraws the cause it had guessed, which is the honest course. The subtraction is my inference, as the task states it nowhere in one sentence, but its figures fit (8270 − 2350 = 5920, and "−33%" of 8850). On that reading the gap of 726 words to route 2's 6626 is the 509 words beside the critique plus about 217 words the rebuild adds on that route. This changes no figure and need not hold up the request; it only lets the request give a cause where `fix.md` gives none.

## Declined to judge

- The Minor findings 3 to 7 of the first review: not fixed, by design (WAY-161, `fix.md`). They stay as written in `reports/review.md` and go into the request as remarks still open, as `agent-instructions/README.md` gives. Rows `:69-71`, `:110-112` and `:220-220` still name no ground (finding 7).
- `author.md`: left unchanged on purpose, with `fix.md:5` naming `fix.md` as the account where they differ. Its table and "2343 words" are stale; I did not grade that, but the request should quote neither.

## Checks

| Check | Command | Exit |
|---|---|---|
| Foundation | `python -B elements/common/foundation_check.py` | 0, 0 errors |
| Instruction files | `python -B instruction-files/check_instructions.py .` | 0; 0 errors, 1 warning, 3 info, the same as `assessment.md:19-27` |
| Tests of `agent-instructions` | `python -B gate/run_tests.py agent-instructions` | 0 |
| Whitespace | `git diff --check 802b56de85c63afdb8ba5a42c83bd1f5ea060260..d32f76d` | 0 |
| Line endings | `git ls-files --eol product-guidelines/styleguide/recognize.md` | `i/lf w/lf` |
| No Python changed | `git diff --stat 802b56de85c63afdb8ba5a42c83bd1f5ea060260..HEAD -- '*.py'` | empty |
| Worktree untouched | `git status --short` | clean, before and after |
| Recheck of the regenerated materials, my own script | `python -B <scratchpad>/recheck2.py <out>` | 0 |

The recheck: 50 main rows and 2 proposal rows with every quote equal to the base; 205 nonblank lines each in exactly one row; 7 summary rows and 22 lists as stated above; the files that must not change are byte-equal to the base; no stale figure (`2343`, `336`, "three files", the old totals) in `word-counts.md` or `assessment.md`. In its output, ignore the lines "Reading the foundation added": they were written for the first review and now count the section a second time.

Script: `C:\Users\Mariusz\AppData\Local\Temp\claude\C--Storage-repos-the-way\da5f3fbe-3569-48c8-a993-d28779b79354\scratchpad\recheck2.py`, output `C:\Users\Mariusz\AppData\Local\Temp\claude\C--Storage-repos-the-way\da5f3fbe-3569-48c8-a993-d28779b79354\scratchpad\recheck2.txt`.

Not run:

- The whole gate: by the handoff.
- `installation` and `instruction-files` tests: no tracked Python file names `recognize.md` (searched), and the first review ran both on the commit before this one-line Markdown change.
- `python -B agent-instructions/skill_entry_points.py --write`: it writes, and this review is read-only; the skill's description did not change.
- A session of an agent on the rebuilt skill: as in the first review.

## Reaches beyond the dispatch

- `product-guidelines/reading.md:39-43` and `project-level/task/skill/read_sources.md`, read in the first review: to judge "did not read" in the new clause.
- `.runs/task-cycles/styleguide-skill-shape/task.md:43`, `:45`: for Minor 2.

## Searches not found or unclear

- One sentence in the task stating how 5900 was reached: not found; Minor 2 is my inference from its figures.
- GitHub's limit on a request's body, from the first review: now tighter, as `assessment.md` grew to 50929 bytes and `word-counts.md` to 20005; still unverified and from memory.

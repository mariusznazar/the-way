PASS 088717a350812116fb51ed8f04eb7dcf3d4857a2

# Review of the fix: maintain-coding-guidelines in the WAY-256 shape

Fix range `097123e..088717a`, one commit, three files: `foundations/decisions.md` (the *Rationale* of
WAY-216 only), `product-guidelines/coding/task_document.md` and `product-guidelines/coding/settle.md`.
`git rev-parse HEAD` is the head given; the worktree stayed clean. The findings file
`reports/findings.md` bounds this review (`task-cycle/review/fix.md`).

Both blocking findings are fixed, and the fix adds no Critical or Important finding. Three small notes
come from the fix, none blocking. The author contested neither finding.

Paths below without a directory are in
`C:/Storage/repos/the-way/.runs/worktrees/coding-skill-shape/product-guidelines/coding/`.

## Findings of the review of 097123e

### 1. The opening of `task_document.md` dropped items on the route of one kind: fixed

The defect was the exclusive "only ... of the items below". On the new head `task_document.md:3-5` reads
"take from the items below what concerns that kind ...: its file with the index row, the test of each new
invariant it settles, its choices and what the comparison found". The example of the finding now runs
through: nine unindexed endpoints, one rule a script checks with its invariant. *To do* holds the kind's
file with its row and the test (`task_document.md:8-10`, `:16-17`), *Questions to settle* the identifier,
exemplar, status, rule and invariant, *Context* each `do not copy` file with its file and line. "What the
comparison found" maps onto the *Context* item worded for an audit (`task_document.md:35-39`); that the
comparison is no audit does not take it out, since the opening names it.

The same form at `settle.md:3-4` now limits "the choices and invariants below" and says "the critique
below stands", so the critique no longer hangs on a reading, and `reports/word-counts.md:314` counts what
the text says. `hand_back.md:3` is unchanged, as the finding said it could be: To do 10 has step 5 "check
only", and its first check names what `task_document.md` names, which now includes the test.

The new opening goes beyond the words of the rule it cites: `SKILL.md:72-74` gives *To do* the file and
the row, the opening adds the test. These do not collide. "Gains" excludes nothing, and the invariants
are within the rule's first sentence.

### 2. The *Rationale* of WAY-216 held a reason nobody gave: fixed

"Research and a trial run answer a new scope" is gone, and the entry no longer says why a trial run
exists, so nothing there disagrees with `recognize.md:25-26` or WAY-251. By source:

| Clause, `foundations/decisions.md:5969-5972` | Source |
|---|---|
| "every task that creates a kind's first file could pull research of all the standing checks" | row 2: "każde zadanie tworzące pierwszy plik rodzaju mogłoby ściągać badania wszystkich stałych sprawdzeń" |
| "an agent on the comparison goes on improvising and may make a full audit" | question 3, *Not chosen*: "agent na tej drodze dalej improwizuje i może zrobić pełny audyt" |
| "a task that is an extension for another reason keeps its research (WAY-211)" | row 1, the rejected wording |

So no reason of the agent's stands in the entry for a decision the human took (WAY-29). The binding
sentences, *Relations*, *Verification* and *Rejected* did not change.

## The walk of route 6, by my own reading

An agent that reached `SKILL.md` by its path, having read `refine-task` steps 1 and 2.

| Step | Reads | Takes | Leaves |
|---|---|---|---|
| start | `SKILL.md` whole | the rule at `:70-74` | |
| 1 | `recognize.md` | the fifth mode, `:21-24` | |
| 2 | nothing: the conditions of `SKILL.md:99-102` do not hold | | `starting_set.md`, `research.md` |
| 3 | `coding/template.md`, `kinds.md` alone (`SKILL.md:111-113`) | that kind alone; the comparison; `copy` and `do not copy` with file and line | `trial_run.md` |
| 4 | `product-guidelines/template.md`, `settle.md`, `task_document.md` (coding template not again) | of `settle.md`: the item on the kind's exemplar, its status and rules (`:18-20`), the invariant for each rule a script checks (`:37`), the critique (`:47-49`) with its section and `critique/SKILL.md`. Of `task_document.md`: the items above | of `settle.md`: new tools, the standing checks, linter, formatter, audit, adopting the template, their invariants and weak points. Of `task_document.md`: tool install, reformatting, the `AGENTS.md` pointer, the part-map items, first guidelines, trial-run evidence, research sources |
| 5 | `hand_back.md` | that the document holds those items; that no choice stands without the human's words | the check of each standing check's decision, as To do 10 gives; hand back to `refine-task` step 4 stands |

The route holds. The acceptance criterion stands: `kinds.md` read; `starting_set.md`, `research.md` and
`trial_run.md` not read. No rule of the base that the route needs is switched off.

One difference from the author's walk: `fix.md:24-25` has this route take "further rules that a cheap test
checks". `settle.md:37-38` speaks there of further rules "of the whole product", which is not what the
route gives. The text is right; the sentence of the report is not, and it enters no file.

## What the fix changed besides

No new Critical or Important finding. Notes, Minor, each from the fix:

### A. `assessment.md` keeps the old word count of `task_document.md` (new thread)

**Anchor:** `C:/Storage/repos/the-way/.runs/task-cycles/coding-skill-shape/reports/assessment.md:47`

**To paste:** The row still says the list costs "about 489 words"; the file now has 509.

**Why I report it:** 489 was the file with its old opening, and the fix handoff asked that rows be brought
in line. A reader of the request compares this row with the files. Nothing else depends on it, and
`word-counts.md` is right. Fix: write the file's figure, 509.

### B. The new *Rationale* points at a sentence by its position (new thread)

**Anchor:** `C:/Storage/repos/the-way/.runs/worktrees/coding-skill-shape/foundations/decisions.md:5969`

**To paste:** "Without the third sentence" holds only while the entry keeps that order, and the second reason
repeats the words of the *Rejected* five lines below.

**Why I report it:** an edit of the entry can move the sentence, and nothing flags the reference. The
sentence can name its content instead, such as "Without this limit". The repetition costs a line and
misleads nobody. Both are polish; the meaning is sourced.

### C. `fix.md` repeats the stale figures of finding 7 (extends finding 7)

**Anchor:** `C:/Storage/repos/the-way/.runs/task-cycles/coding-skill-shape/reports/fix.md:57` (and `:70`)

**To paste:** `SKILL.md` has 1506 words, not 1499, and the text beside the template is 4169, not 4162, so
it grew by 773 words. Its table of routes is right.

**Why I report it:** the same 7 words as finding 7 of the first review. The risk is the same and only that:
a figure copied from the report into the request. Take the figures from `word-counts.md`.

## Minor findings of the first review

Unchanged by the fix and standing as they were, numbered as in `review.md`: 3 (order of the assessment,
`SPLIT` in its rows), 4 (`:187-196` "Mistake: not found"), 5 (the check of paths the report does not
hold), 6 (P1's quotes and its RECOMMENDED), 7 (figures of the reports; updated by note C) and 8 (the
*Rejected* of WAY-216, lines 5974-5976). They go to the request.

## Declined to judge

- Whether "take from the items below what concerns that kind" is the best wording: it is the wording the
  first review proposed, and I hold it to the defect, not to my taste.
- The issues outside the fix diff that the first review already lists; they do not reopen the review.

## Checks

Scripts are mine, in `C:/Users/Mariusz/AppData/Local/Temp/claude/C--Storage-repos-the-way/41f2056f-3658-4eef-997b-34fd0fc1aa7a/scratchpad/`.

| Command | Exit | Showed |
|---|---|---|
| `git rev-parse HEAD`, `git status --short` | 0 | head as given; empty |
| `git diff 097123e..HEAD`, read whole; `git diff --name-only` | 0 | three files; no `.py`, `.claude`, `.agents` |
| `git diff --check 097123e..HEAD` | 0 | clean |
| `python -B chk_counts.py <cycle>/reports/word-counts.md` | 0 | every figure at the head recomputed: file figures, sections, sums, figures without the first reading, the summary with percentages: 371 compared, 0 differ |
| `python -B <cycle>/tools/verify_counts.py <cycle>/reports/word-counts.md` | 0 | 346 figures, 0 differ |
| `wc -w` on the changed and the rebuilt files | 0 | `task_document.md` 509, `settle.md` 635, `SKILL.md` 1506; eleven files 4169 |
| `python -B chk_assess.py <base SKILL.md> <cycle>/reports/assessment.md` | 0 | 56 rows, 247 nonblank lines each once, quotes and permalinks all equal |
| `python -B chk_sent.py` | 0 | still 13 of 157 base pieces not verbatim; the new pieces are the two openings |
| `python -B elements/common/foundation_check.py` | 0 | 0 errors |
| `python -B instruction-files/check_instructions.py .` | 0 | 0 error, 1 warn, 3 info, as the base |
| Manual: both findings, the walk of route 6, the *Rationale* against rows 1, 2 and question 3 | | above |

Not run: the whole gate, the orchestrator's by the handoff, and `gate/run_tests.py installation` (the
gate covers it, and the fix touches no file it reads beyond the Markdown of the skill, whose description
stayed).

## Reaches beyond the dispatch

None: the files read are those of the first review, the fix report and its handoff.

## Searches not found or unclear

none

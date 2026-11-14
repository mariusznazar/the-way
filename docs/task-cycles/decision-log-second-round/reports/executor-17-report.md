# Report of executor 17

**Status:** done

**Commits:** `06c8e42` on `task/decision-log-second-round` ("Remove the withdrawn decision numbers from the project definition, task and plan templates and the task line file and give each rule its reason").

## Files changed

| File | Added | Removed |
|---|---|---|
| `project-level/definition_template.md` | 24 | 34 |
| `project-level/task/template.md` | 12 | 8 |
| `project-level/plan/template.md` | 2 | 2 |
| `project-level/task_line.md` | 1 | 1 |

Totals of the commit: 39 insertions, 45 deletions.

## Checks

- `python -B elements/common/foundation_check.py` — exit 1, as the handoff says it stands until the last slice; it prints no line for `project-level/definition_template.md`, `project-level/task_line.md`, `project-level/task/template.md` or `project-level/plan/template.md` (grep of its output for those four paths: 0 lines).
- `python -B gate/run_tests.py project-level` — exit 0, 275 tests, OK (run twice, before and after a reflow of two lines).
- Not run: the product's gate without a directory.

## Own-work check

Requirement most likely not met: "the sentence around each removed number reads as before", and "a sentence of reason names no file, count or measurement the entry does not give". Check: read the whole diff (`git diff` of the four files) against the base text; every removed bracket left its sentence with a full stop; no added sentence contains a file name, count or measurement; and `git diff | grep -c '^+.\{101,\}'` printed 0 (no added line over 100 columns). Shown: the diff reads as intended; two added lines that came out long were reflowed.

## Numbers removed

- `definition_template.md`: WAY-72, WAY-108 (lines 35-36, 75, 85, 92, 110, 127, 204, 226 of the base), WAY-109 (114, 118), WAY-110 (122), WAY-112 (216), WAY-115 (326, 329), WAY-116 (277), WAY-117 (359). The two lines holding only `WAY-108.` were deleted with one of their two blank lines. The brackets `(WAY-72 for the entries; WAY-108)` went whole: the sentence says the projected entries are in English as before, and no reference to `rules.md` was added (the handoff's "make no other change"); the language rule for entries stands in `elements/common/rules.md` "Language".
- `task/template.md`: WAY-356 (line 103), WAY-115 (line 202; `(WAY-115, WAY-134)` became `(WAY-134)`), WAY-353 (line 239).
- `plan/template.md`: WAY-156 (line 115).
- `task_line.md`: WAY-329 (line 36).

## Reasons added (file, sentence, entry written from, read at base `ec7929d`)

- `definition_template.md`, "Where it stands, and in what language", after the language paragraph (WAY-108): "The person deciding the project reads its content in the language of the conversation, and fixed structural words let later work resume and check the document." — from the first sentence of the *Rationale* of WAY-108.
- `definition_template.md`, bullet "Background, Success and Risks" (WAY-109): "A fluent draft would make an agent's inference look like the human's decision." — *Rationale* of WAY-109, first sentence.
- `definition_template.md`, bullet "A frame of success" (WAY-109, the second sentence the plan allows): "A condition that could disprove success gives later work a way to judge it." — *Rationale* of WAY-109, second sentence.
- `definition_template.md`, bullet "A deadline" (WAY-110): "A date imposed by the surroundings can constrain the work, while a date invented for planning makes the constraint appear to come from the human." — *Rationale* of WAY-110.
- `definition_template.md`, "Projected foundation changes", first paragraph (WAY-116). First the missing part of the rule: the list now reads "environment facts only where a projected decision or invariant rests on them" (the base entry's wording, and the wording of `elements/common/skill/definition_variant.md`'s line on facts a settlement rests on); then the reason: "Restricting facts to what a projected rule rests on prevents a speculative inventory of the surrounding world." — *Rationale* of WAY-116, second sentence ("proposed rule" became "projected rule" to fit the file's word).
- `task/template.md`, paragraph on `Defect introduced by:` (WAY-356). First the missing half of the rule, after "never the cycle.": "A defect found after a merge is recorded also as a problem of the class `defect-found-after-merge` in the register of problems, which counts it." (the class is in `process-audit/problem_register.md`; the sentence is the base entry's half). Then, after the sentence ending "never `none`.": "A task written before the line was never assessed, which `none` would say it was." — *Rationale* of WAY-356, last sentence. The *Rationale* has also a reason for the register half ("a line alone counts nothing, and a class alone ... would make the review guess which change introduced the defect"); the plan allows one sentence of reason, so I wrote the one that stands at the sentence the plan names. If the orchestrator wants the register half reasoned too, it is one more sentence from the same *Rationale*.
- `task/template.md`, paragraph "Where the document points at a place to change in a file" (WAY-353): "A line number names a place that moves when the file changes, while a heading or a quotation finds it again after the lines have moved." — *Rationale* of WAY-353, first sentence. It stands after the rule sentence and before the sentence on the *Source* under a question, whose reason ("which say which text the line meant") already stood in the file. The *Rationale*'s register counts (80 rows, 45 of 83 cycles) were not carried: they are measurements of a record not open to the reader.

## Entries left under the "stay" rule

None of the ten staying numbers (WAY-93, 94, 97, 263, 287, 294, 295, 297, 363, 364) stands in the four files; nothing was left under that rule. Other references in the four files were not touched: WAY-01, 07, 26, 30, 36, 71, 101, 106, 107, 113, 118, 121-124, 126, 134, 137, 138, 140-147, 154, 155, 165, 166, 230, 267, 269, 270, 313, 314, 316, 320 (the foundation check lists none of them).

## Findings

- None beyond the note on WAY-356 above. No mismatch of the plan and the code: the base line numbers found their numbers by search; the line `WAY-72` is in line 35 as the plan said.
- Every removed bracket stood before a full stop or a colon already, so no stop was added anywhere.

## Reach beyond the dispatch

None. I read `process-audit/problem_register.md` (a grep for `defect-found-after-merge`, lines 56, 132, 138, and its table at lines 50-56) only to name the class correctly; the handoff names it as the place of the missing half.

## Unread material

- `foundations/decisions.md` WAY-293 (named in *Read*): not read; the section of the handoff gave the work in full and no reason or placement here depended on it.
- `foundations/decisions.md` as it stands: not read, per the handoff the numbers' base text was read from `git show ec7929d:foundations/decisions.md` (entries WAY-72, 108, 109, 110, 116, 353, 356 whole; WAY-112, 115, 117, 156, 329 only the heading line, since no reason is added for them). The `.runs/task-cycles/decision-log-second-round/task.md` was read at lines 25-50 only (the handoff's *Read* names lines 33-40).
- `project-level/task_line.md` read whole through `cat`; the other three files whole through Read before the change.

## Searches not found or unclear

None.

## Working copies

`.runs/executor-17/` held `base.md` (the base log), `edit.py`, `edit2.py` (the scripts that made the edits) and `fc.txt` (the foundation check's output). Each was removed by path before return; the directory itself is empty and stays.

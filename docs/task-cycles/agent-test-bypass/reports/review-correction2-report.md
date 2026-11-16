PASS 763a420ea644181f8673147ae92785d72b32e330

# Review of correction 2 — agent-test-bypass

Range `1948ad7a..763a420e`, one commit (`763a420e`, "Correction 2: a row that adopts an outside
practice enters accepted only when it repeats a choice the human made between ways shown"), two
files: `project-level/task/skill/find_settlements.md`, `project-level/task/template.md` (9 added,
7 removed). `git rev-parse HEAD` is `763a420ea644181f8673147ae92785d72b32e330`, the head given.
`git diff --stat 938d6ee9 1948ad7a` is empty, so the tree between the head I last reviewed and this
base did not change. Reviewed as `task-cycle/review/fix.md` gives for a correction: the human's
decision (`reports/correction-2-remarks.md`) takes the findings file's place, then the diff is
reviewed as section 2 of `task-cycle/review/SKILL.md` gives.

Counts: 0 blocking, 0 Minor, 0 out of scope.

## The decision

- **"Add to the sentence in `find_settlements.md:29-30` the condition its twin in `task_variant.md`
  has"** — made. `find_settlements.md:29-30` now reads "A row that adopts a practice from outside
  the product (WAY-100) and repeats a choice the human made between ways shown enters `accepted` as
  the human's choice, like any such row". The condition matches `task_variant.md:33-35` word for
  word ("and repeats a choice the human made between ways shown is built `accepted`"). "Like any such
  row" now compares within the conditioned set and no longer widens it.
- **"a row the agent derived itself waits for the human"** — made. `find_settlements.md:33-34`: "A
  row of such a practice that you derived from the material or from the human's loose words waits
  for the human, as every row you derived does." It agrees with WAY-134 ("the rows the agent derived
  from the material wait for the human", `foundations/decisions.md:5332`; "the human cuts only the
  rows the agent derived", `:5360-5361`). It agrees in words and person with the same file's
  `:24-25` ("the human accepts or rejects only the rows you derived from the material or from the
  human's loose words") and with `elements/common/skill/build_table.md:20-21`, which uses the same
  phrase. The second person is the file's own — it addresses the refiner, as line 24 does.
- **"Check that every other place that states this rule carries the same condition"** — made. My own
  search (below) finds each place that states the state of a row adopting an outside practice
  carrying the condition, and each place that states the state of a derived row agreeing.

## Places that state the state of such a row (my search)

Searched outside `.runs/` for "practice from outside", "rows you derived", "the agent derived",
"you derived", "`waiting`", "row waits", "enters accepted", "built `accepted`", "starts `accepted`",
"already `accepted`":

- A row that adopts an outside practice:
  - `elements/common/skill/task_variant.md:33-35` — conditioned;
  - `project-level/task/skill/find_settlements.md:29-30` — conditioned (this correction);
  - `project-level/task/template.md:222-224` — conditioned (this correction; see below).
- Places that name such a row with no state, so no condition is due:
  - `project-level/task/template.md:149-150` (the question that settles an adoption shows the parts);
  - `elements/decisions/template.md:93-97` (what *Rejected* takes);
  - WAY-134 `foundations/decisions.md:5304-5310` and `:5327-5330`;
  - WAY-100 `:208-210`.
- A row that repeats a choice, or a derived row, in general:
  - `build_table.md:15-21`;
  - `task_variant.md:40-42`;
  - `find_settlements.md:21-25`;
  - `project-level/task/template.md:208-209`;
  - `elements/common/skill/SKILL.md:51`;
  - `project-level/task/skill/orchestrated_mode.md:69`;
  - WAY-134 `:5283-5285`, `:5331-5332`, `:5344-5346`, `:5360-5361`.

  All say a repeating row enters accepted and a derived row waits for the human; none conflicts with
  the new sentences.
- `elements/common/skill/definition_variant.md:27` and `project-level/definition_template.md:286` —
  the definition variant, outside this rule.

The task template's change narrows a sentence that already stood in a context limited to "a
settlement the human chose among ways shown" (`:219`). It changes no meaning and drops nothing WAY-134
asks: a derived row has no question whose ways could carry the parts. One clause stays unconditioned
— "the cycle puts none there that the source does not keep". It stands after the semicolon as a rule
of its own, and the decisions template (`:93-97`) gives it for every row. "Among ways shown" there,
against "between ways shown" in the two skills, is a variation no reader would take differently.

## What the change itself broke

Nothing found. Neither changed sentence repeats the wording of Minor finding 2 of the review of
correction 1 ("the parts the practice leaves out"). In the task template, "the parts it leaves out"
now has the row as its subject, which reads rightly.

## Declined to judge

- Whether a derived row that adopts an outside practice must also get the question that shows the
  parts left out — outside the decision. WAY-134's second paragraph ties the showing to "the question
  that settles it". The author names it as unclear too.

## Checks

- `git rev-parse HEAD` — exit 0, `763a420ea644181f8673147ae92785d72b32e330`.
- `git log 1948ad7a..763a420e --stat` and `git diff 1948ad7a..763a420e` — exit 0; one commit, two
  files.
- `git diff --stat 938d6ee9 1948ad7a` — exit 0, empty.
- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- `python -B gate/run_tests.py project-level` — exit 0, 279 tests, OK.
- Manual: the search above, and the changed sentences read against WAY-134, `task_variant.md`,
  `build_table.md` and the rest of `find_settlements.md`.
- Not run: the full gate (not the reviewer's); `reports/author-correction2-check.py` (my search by
  hand covers what it checks by pattern).

## Reaches beyond the dispatch

None beyond the files the search found, read at the lines named.

## Working copies

None in the worktree. `.runs/review-correction2/` was
never created. The output of the test run stood in
a file `pl.txt` in the session's scratch directory
and was removed.

## Unread material

- `reports/author-correction2-check.py`: not read.
- `elements/common/skill/SKILL.md`, `orchestrated_mode.md`, `definition_variant.md`,
  `project-level/definition_template.md`: only the lines the search found.

## Searches not found or unclear

none

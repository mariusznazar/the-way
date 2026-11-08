PASS ef0195edb7128b30f9768aab89e3b8846d2d8d5e

# Review of the fix — task cycle `test-artifacts`

Fix range `d0d3ce6c913b04481fff652de175eeae37099013..ef0195edb7128b30f9768aab89e3b8846d2d8d5e`
(one commit, `ef0195e`, "Fix the findings of the review of the whole change"); `git rev-parse HEAD`
matches the head given. Bounded by `reports/findings1.md` (I-1..I-3, Minor 1-5) and the fix report
`reports/fix1_report.md`, as `task-cycle/review/fix.md` gives.

Counts: blocking 0; findings remaining 0; new Minor notes 3 (non-blocking); out of scope 0.

## Each finding of the findings file

- **I-1 — fixed.** `foundations/glossary.md` is back to the base wording ("the means through which
  an agent checks behaviour a user sees in a product while it runs"); `git diff f218b55..HEAD --
  foundations/glossary.md` is empty. With the term meaning the means alone, a product that settles
  a browser route but no place for screenshots has a settled way, so WAY-219's "no such way" and
  WAY-317's "way settled, no place" are again two cases, as WAY-317, item 13 of the request template
  and `ui_check.md` use them. No use had been rewritten to the widened meaning, so nothing is left
  behind (`git grep "together with the place where the screenshots"` → no match).
- **I-2 — fixed.** WAY-319 now holds sentence 1 alone; the *Relations* item `derives from WAY-166`,
  the *Verification* clauses about the technology step and the rationale's "seen as a lack in the
  comparison" are gone, and the `project-level/technology/research.md` sentence is removed. `git
  grep -e "cannot check at once" -e "WAY-166 gives for an option"` → no match. What remains is row 6
  as the task states it.
- **I-3 — fixed.** New invariant `record-copy-image-files` (`foundations/invariants.md:328-336`,
  `Method: review`, `Part: every`, derives from WAY-316): "Where {merge-onto} exists, no commit of a
  change against {fork-point} adds a file below `docs/task-cycles/` whose name ends in an image
  extension that `record-copy-image-check` names." It states row 7's property (any image file, not
  only a screenshot) and keeps the check script's own invariant beside it, as
  `elements/invariants/template.md:113-114` asks for a check and the data it reads. WAY-316's
  *Verification* names both. The `{merge-onto}` / `{fork-point}` form follows the template
  (`elements/invariants/template.md:95-101`) and `return-step-record`. Checked against the history it
  speaks of: no image file was ever added below `docs/task-cycles/` (command below, no output).
- **Minor 1 — fixed.** WAY-267 *violates* now lists the four matters
  (`foundations/decisions.md:8095-8096`).
- **Minor 2 — fixed.** The seven named lines are rewrapped; the fix's added Markdown lines over 100
  characters are only `foundations/glossary.md:9` and `foundations/invariants.md:330`, files whose
  entries are written one sentence per line, plus `project-level/technology/task_run.md:73` (101
  characters, from the first commit, one character over). The other long lines in those files are
  older than the change.
- **Minor 3 — fixed.** WAY-316 *Rejected* now says the release attachments and the external file
  store were rejected "as the place the-way would name".
- **Minor 4 — fixed.** `task-cycle/review/SKILL.md:86-90` tells a reviewer that a screenshot it
  takes for the human lies in the product's place, outside the repository, that its report names the
  address, and that with no place settled it keeps none (WAY-316, WAY-317). It writes outside the
  reviewed worktree, so the skill's read-only rule holds.
- **Minor 5 — fixed** (a report claim, no file): the fix report withdraws it, and the I-3 fix no
  longer rests on it.

## New findings in the fix diff

Critical: none. Important: none.

Minor notes (non-blocking, within the task):

1. `foundations/glossary.md:9` against `foundations/decisions.md` WAY-121: with the definition back
   to "the means through which an agent checks", WAY-121 counts the place of the screenshots among
   "four matters of an agent's way to the running product", though a place for evidence shown to the
   human is not quite a means of checking; WAY-270's *Rejected* uses exactly this fit ("the family's
   definition stops fitting, since the matter does not speak of an agent checking behaviour") to keep
   the failure notice out. No sentence the files hold is read wrongly for it, since the place is
   where the screenshots of the agent's check lie. The author names the cost in the fix report.
2. `foundations/invariants.md:330`: because of "Where {merge-onto} exists", `record-copy-image-files`
   binds nothing in the-way until it has a main branch (the same holds for `return-step-record`), and
   for a product's repository the rule stands in WAY-316's "file of a screenshot" and in step 5 of
   `task-cycle/skill/SKILL.md` ("checked for image files, which no copy holds"). Step 5 still runs on
   every copy, so no image passes unchecked in practice.
3. `task-cycle/review/SKILL.md:89-90`: "where the foundation settles none, keep none" does not say,
   as `ui_check.md` does for the author, that the reviewer's report states that no place is settled,
   so the request can tell the human (WAY-317). Today no reviewer step requires a screenshot.

## Declined to judge

none

## Checks

- `git rev-parse HEAD` → `ef0195edb7128b30f9768aab89e3b8846d2d8d5e`; `git log --oneline
  d0d3ce6..HEAD` → one commit.
- `python -B elements/common/foundation_check.py` → `0 errors`, exit 0.
- `python -B agent-instructions/skill_entry_points.py` → `entry points are current`, exit 0.
- `git diff f218b55..HEAD --stat -- foundations/glossary.md` → empty, exit 0.
- `git grep -n -e "cannot check at once" -e "WAY-166 gives for an option" -e "together with the place
  where the screenshots"` → no match, exit 1.
- `git log --diff-filter=A --name-only --format= HEAD -- docs/task-cycles` filtered for the
  invariant's extensions → no output.
- Manual: line lengths of the fix's added Markdown lines (PowerShell pass over `git diff -U0
  d0d3ce6..HEAD`) and of the touched files → Minor 2 above.
- `python -B gate/run_tests.py task-cycle` → 200 tests OK, exit 0.
- `python -B gate/run_tests.py project-level` → 271 tests OK, exit 0.
- `python -B gate/run_tests.py elements/common` → 109 tests OK, exit 0.
- Not run: the full gate (the orchestrator's, by the dispatch).

## Reaches beyond the dispatch

- `elements/invariants/template.md:90-114` and `elements/common/rules.md:71-78` — the meaning of
  `{merge-onto}` / `{fork-point}` and the rule on a check and its data, to judge the new invariant.

## Searches not found or unclear

- Whether an invariant of the-way that holds only "where {merge-onto} exists" is meant to bind
  the-way's task branches while the-way has no main branch: `elements/common/rules.md:76-78` says a
  review reads `{merge-onto}` as `none` there, which reads as no; unclear whether that is intended for
  rules about record copies the-way commits today.

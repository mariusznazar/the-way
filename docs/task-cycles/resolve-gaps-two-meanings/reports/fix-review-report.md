PASS 187bbde67c221a847f53e693d4c75d94f51a3e3a

# Review of the fix: task `resolve-gaps-two-meanings`

Range `9c66ee1..187bbde`, one commit (`187bbde`); `git rev-parse HEAD` of the reviewed worktree is
`187bbde67c221a847f53e693d4c75d94f51a3e3a`, the head given. Files: `foundations/decisions.md`,
`project-level/task/skill/SKILL.md`, `project-level/task/skill/resolve_gaps.md`. I read the findings file, the
handoff, the fix report, the diff of the range, `find_settlements.md` whole and `SKILL.md` section 5.

## Findings of the findings file

- **I-1 — fixed.** WAY-374 (`foundations/decisions.md`, second paragraph) now reads "an ambiguity in the approved
  project definition whose resolution changes the definition goes back to the definition and its readiness gate
  (WAY-118)"; `resolve_gaps.md` (third paragraph of the check) reads "An ambiguity in the approved project
  definition whose resolution changes the definition goes the way the paragraph below on that definition gives
  (WAY-118)". The same condition stands in both, and it is the condition of the paragraph pointed to ("If the
  answer changes the approved project definition or a projected decision of it, route that change", still at
  `resolve_gaps.md`, unchanged). The entry's sentence is no longer broader than WAY-118. The remaining binding
  sentences of the entry and the check, compared again side by side (what to search, what settles it, what counts,
  example and question, answer under *Questions to settle*, no duty and no number, silence), say the same.
- **M-1 — fixed.** `SKILL.md` section 3 is re-wrapped; a count of characters over lines 40-50 shows none over
  100 (line 3, the frontmatter `description`, is unchanged).
- **M-2 — fixed.** A count of characters (Python, not bytes) over `foundations/decisions.md` lines 12880-12944
  shows no line over 100. (A byte count shows some, because of the dashes; not a defect.)
- **M-3 — fixed.** *Rationale* reads "after the model of WAY-99 for a word of the foundation".
- **M-4 — fixed, and the wording is true.** The entry says the candidate glossary term is one "which WAY-95 judges
  there"; the skill says "which step 5 finds and WAY-95 judges there". `SKILL.md` section 5 sends the task to
  `find_settlements.md`, which runs `find-foundation-entries` with the task as caller and rows of *Settlements to
  record* as the mode (WAY-134); that skill's `elements/common/skill/read.md:9-10` makes it read, in each
  element's template, "Which words take an entry" of the glossary's (the passage that holds WAY-95's test), and
  `find_settlements.md` itself names no glossary row but says every settlement that binds after the merge is
  found there and rows of kind glossary term are part of WAY-134's candidate list. So step 5 finds the candidate
  and the shared skill judges it by the glossary template. The claim holds; `find_settlements.md` does not
  name WAY-95 itself, which is not required.
- **M-5 — fixed.** The paragraph is split into three, the question is named "as a question of decision according
  to "How a skill asks" (WAY-113)", which is the section heading of `elements/common/way_of_working.md` the task
  names.

No finding was contested.

## New findings in the fix diff

- Critical, Important: none. The fix touches only the conditions, wording and wrapping above; the decision's
  meaning is changed in one place (I-1, as asked), and no sentence of WAY-95, 99, 113 or 118 is altered by the
  diff (the log gains no line outside WAY-374).
- Minor (new, not blocking, within the task): `project-level/task/skill/resolve_gaps.md` lines of the check hold
  one remaining sentence "The check owes no finding and no number of cases; where it finds none, say nothing of
  it" at the end of the paragraph about the glossary and the definition, now separated from the paragraph that
  states what counts; a reader finds it, but it fits the second paragraph better. Cosmetic.

## Declined to judge

none beyond the first report's two lines (the course's wording, the optional pair of examples).

## Checks run (command, exit code)

- `git rev-parse HEAD` — `187bbde...`, equal to the head given; `git log 9c66ee1..187bbde --oneline` — one commit.
- `git diff 9c66ee1..187bbde` — read whole.
- `python -B elements/common/foundation_check.py` (reviewed worktree) — exit 0, `0 errors`.
- `python -B instruction-files/check_instructions.py .` (reviewed worktree) — exit 0, `0 error, 0 warn, 3 info`.
- `python -B gate/run_tests.py project-level` in a worktree of `187bbde` — exit 0, 275 tests OK.
- Python count of characters per line over the changed ranges — no line over 100.

Not run: other test directories and the whole gate (no file of theirs touched; the cycle's own run).

## Reaches beyond the handoff

`elements/common/skill/read.md`, `task_variant.md`, `build_table.md` (grep and lines 1-25 of `read.md`) to confirm
that the shared skill judges a glossary candidate by the glossary template's "Which words take an entry", for
the check of M-4.

## Unread material

none of the fix's own material. Decisions are not re-selected in this review (the first report's counts stand:
19 read whole, 64 by title only). `find_settlements.md` and `SKILL.md` section 5 read whole as the handoff asks;
`elements/common/skill/SKILL.md`, `task_variant.md` and `build_table.md` not read whole (only grepped).

## Searches not found or unclear

None. (`find_settlements.md` does not name the glossary or WAY-95 by word; the claim of M-4 rests on the shared
skill it calls, `elements/common/skill/read.md`.)

## Working copies

One worktree of `187bbde` at `.runs/review-fix/head`
for the test run; removed with `git worktree remove --force` and `git worktree prune`, and the directory
`.runs/review-fix/` removed. No remainder. The reviewed worktree was not changed (`git status --short` empty).

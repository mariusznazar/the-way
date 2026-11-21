# Report of the fix — the Minor findings of the review of the whole change

**Status:** `done`

Fix range: after `7d063ef278748884de28577f582b2ab0767d068d`. Findings read from
`reports/review-whole-findings.md` (six Minor findings, no blocking finding).

## Commits

1. `90ac8500` — Check that an entry point sends the session to the file, qualify the hiding as Claude Code's
   and say what the invariant test fails on (the invariant's test, the generator's text and test, the 46
   regenerated entry points)
2. `2bd0efde` — Point the paragraphs of the skills at the list of paths in the entry point first, and qualify
   the hiding as Claude Code's (the 15 skill paragraphs; the brief sentence in the lead skill)
3. `f1efc257` — Qualify the hiding as Claude Code's in AGENTS.md, README.md and WAY-127, and add the parts
   WAY-127 governs to its scope

## Each finding

1. **Codex claims — fixed.** The hiding is now stated as Claude Code's wherever the change said it for both
   tools: `AGENTS.md` ("which in Claude Code keeps the model from being offered a skill of the-way and from
   calling one"); WAY-127's sentence ("so that Claude Code offers the model no skill of the-way") and
   *Rationale* ("in Claude Code a request naming a skill without its command brings no skill", "removes them
   from what Claude Code offers the model"); the entry point text, so all 46 entry points ("since Claude
   Code does not offer the entry points of the-way's skills to the model"), and the 15 skill paragraphs
   (same clause); `README.md` ("so a Claude Code session does not call a skill of the-way"). Check: a
   search of the files I changed for "hidden from the model" and "offered" finds no text left that states
   the hiding for Codex; `python -B agent-instructions/skill_entry_points.py` → 0 "entry points are
   current".
2. **The invariant's test checked part of the clause — fixed.** `REQUIRED_WORDS` of
   `gate/test_skills_reach_the_way_sessions.py` gains ``read that skill's `SKILL.md` ``. The check of the
   checker has a new case `eta`, two copies that say "do not call it" and do not send the session to the
   file, expected finding ``its text does not contain read that skill's `SKILL.md` ``, 8 findings in all.
   Failing run (the case written first, the helper unchanged): `python -B gate/run_tests.py gate` → 1,
   `test_problems_reports_a_skill_the_session_does_not_see` failing on the missing finding for `eta` (copy:
   `reports/author-fix-invariant-test-failing-run.txt`). Passing run (words added): same command → 0.
   The invariant test on the real repository (`test_every_skill_reaches_a_session_on_the_way`) passed
   throughout, since the entry points already held the words.
3. **Two ways to find a named skill's file — fixed.** The 15 paragraphs now say: the `SKILL.md` "stands at
   the path that the list of skills in the entry point you were started with gives, or, where you were
   started without one, in the file under that root whose frontmatter has the line `name: <that name>`,
   which a search of the files that git lists as `SKILL.md` finds". The list comes first and the search is
   restricted to what git lists, so working copies under `.runs/` (ignored) are not found. WAY-127 and the
   invariant keep the list of paths, as the handoff asks. The paragraphs were rewrapped at 100 columns, so
   a few lines around the changed sentence moved (the diff of each file is the paragraph).
4. **Brief of a dispatched agent — fixed.** `project-level/lead/skill/SKILL.md` now says, in its paragraph
   on where the-way lies, "give the brief of an agent you dispatch for such a skill the path of that file,
   so that no personal skill of the same name stands in".
5. **Docstring and message — fixed.** The docstring of `gate/test_skills_reach_the_way_sessions.py` now says
   a skill that a human could not start under its `the-way-` name, or whose entry points would be offered to
   the model, is reported; the failure message reads "an entry point of a skill of the-way that is missing,
   differs from its copy or is not hidden from the model". `AGENTS.md`: "the gate's tests report an entry
   point that is missing, differs from its copy or lacks the field, so that a human could not start the
   skill under its `the-way-` name or the model would be offered it".
6. **WAY-127's *Scope* — fixed.** `foundation-review` and `product-guidelines` are added (part identifiers as
   `foundations/part_map.md` headings give them); `python -B elements/common/foundation_check.py` → 0,
   "0 errors", so the foundation holds the parts.

## Correction of a claim of my first report

I wrote that the failing run of the invariant test listed 46 problem lines ("46 lines ... its frontmatter
does not hold `disable-model-invocation: true`"). It listed 23. I checked it against
`reports/author-invariant-test-failing-run.txt`: 23 lines of the form
``.claude/skills/the-way-<name>/SKILL.md: its frontmatter does not hold `disable-model-invocation: true` ``
and none for `.agents/skills/`, because the test checks the two copies of a skill once (byte-identical copies
are checked as one, `seen` in `problems`). The evidence (the failing run, the failing reason) holds; only the
count was wrong.

## Checks (command → exit code)

- `python -B gate/run_tests.py gate` → 1 (the case for `eta`, before the words were added); → 0 after.
- `python -B gate/run_tests.py agent-instructions` → 1 (the generator's text test and the written-out form of
  the entry point, written first; two failures: `test_text_is_the_written_out_form` and
  `test_write_creates_both_copies_and_a_rerun_finds_them_current`); → 0 after the generator and the
  regenerated entry points, 53 tests.
- Focused runs after the last commit, each `python -B gate/run_tests.py <directory>` → 0: `agent-instructions`,
  `gate`, `elements/common`, `elements/part-map`, `instruction-files`, `product-guidelines`, `project-level`,
  `task-cycle`. `installation` was not run: nothing in it was changed and the first fix's run passed (the
  entry points of the product are written by the installer on its own).
- `python -B elements/common/foundation_check.py` → 0 ("0 errors").
- `python -B agent-instructions/skill_entry_points.py` (without `--write`) → 0, "entry points are current".
- The full gate was not run.

## Own-work check

- The requirement most likely broken by this fix: the invariant `skill-entry-points` and the test stay true
  together with the entry points after the change of the generator's text. Check: the passing run of `gate`
  with the regenerated entry points (exit 0) and the generator without `--write` (current).
- Second: the rewrap of the 15 paragraphs changed nothing but the sentence. Check: I read the diff of three
  of them (`elements/decisions/skill/SKILL.md`, `product-guidelines/coding/SKILL.md`,
  `project-level/task/skill/SKILL.md`): only the sentence and the wrap of its paragraph differ; the focused
  run of `product-guidelines`, `project-level` and `elements/common` passes. I did not read the diff of the
  other twelve line by line.

## Choices

- The qualification "Claude Code does not offer the entry points ... to the model" replaces "are hidden from
  the model" in the entry point and the 15 paragraphs, which changes the 46 entry points again (23 skills
  × 2 copies). Rejected: qualifying only `AGENTS.md`, README and WAY-127 and leaving the entry point text,
  which the finding names. Cost if wrong: one more regeneration.
- Minor 3: I kept the search as the second way, as the review says the convention exists in
  `task-cycle/skill/foundation_step.md` and `task-cycle/plan/SKILL.md`; those two files are unchanged.

## Reaches beyond the handoff

None. (Read: `task-cycle/change/fix.md`, as the handoff names it; `elements/common/foundation_check.py` was
run, not read.)

## Working copies

`.runs/author/`: logs of runs, message files of commits and a one-off script that rewrapped the paragraphs
(removed after use, never committed). One failing-run log is kept in `reports/` as
`author-fix-invariant-test-failing-run.txt`; `.runs/author/` is empty. No other copy was made.

## Unread material

- `reports/review-whole-report.md`, `review-whole-handoff.md` and `review-whole-probe-evidence.txt`: not
  read (the handoff gives the claim to correct; I checked it against my own failing-run file).
- Of the 15 skill diffs, twelve were not read line by line (see the own-work check).
- WAY-127's whole entry was re-read only where I edited it (sentence, *Scope*, *Rationale* paragraph).

## Searches not found or unclear

- None unclear. The finding 1 listed `skill_entry_points.py:211`; the sentence stood at the text of
  `entry_point_text`, not at a line of the docstring, which already said "in Claude Code".

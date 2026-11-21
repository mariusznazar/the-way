PASS f1efc257e7d2810d4072b0a82d2a98a78e889a3d

# Review of the fix — the Minor findings of the review of the whole change

Range `7d063ef278748884de28577f582b2ab0767d068d..f1efc257e7d2810d4072b0a82d2a98a78e889a3d`, three
commits (`90ac8500`, `2bd0efde`, `f1efc257`), 67 files, +227 / -192. `git rev-parse HEAD` in the
worktree gave `f1efc257e7d2810d4072b0a82d2a98a78e889a3d`, the head of the handoff. The findings file
(`reports/review-whole-findings.md`) holds six Minor findings and no blocking one, so only a new
Critical or Important finding could fail this review (WAY-162). There is none.

## Each finding of the findings file

1. **Codex claims — fixed.**
   - `AGENTS.md:12-13` now reads "which in Claude Code keeps the model from being offered a skill of
     the-way and from calling one".
   - WAY-127's sentence (`foundations/decisions.md:3342-3343`) reads "so that Claude Code offers the
     model no skill of the-way".
   - WAY-127's *Rationale* reads "removes them from what Claude Code offers the model" and "in Claude
     Code a request naming a skill without its command brings no skill".
   - The entry point text (`agent-instructions/skill_entry_points.py:211-213`), and so all 46 entry
     points, reads "since Claude Code does not offer the entry points of the-way's skills to the
     model". The 15 skill paragraphs use the same clause.
   - `README.md:161` reads "so a Claude Code session does not call a skill of the-way".

   Evidence: `git grep` of "hidden from the model" in the entry points finds nothing, and the
   generator reports "entry points are current". A search of the whole repository across line
   breaks finds one unqualified "hidden from the model" left, in `foundations/part_map.md:170-171`.
   My finding did not list that sentence, and the fix did not touch it: see new Minor note A.

2. **The invariant's test checked part of the clause — fixed.**
   - `gate/test_skills_reach_the_way_sessions.py:39` adds ``read that skill's `SKILL.md` `` to
     `REQUIRED_WORDS`.
   - The new case `eta` (lines 239-242, 263-270, 283, 335-340) builds two copies that say "do not
     call it." and do not send the session to the file, and expects exactly that finding (8 in all).
   - The failing run is kept in `reports/author-fix-invariant-test-failing-run.txt`. It fails on the
     missing `eta` finding with the seven others present, which is the expected reason.
   - It passes on the head: `python -B gate/run_tests.py gate` → 0.
   - The case fails when the behaviour breaks: drop the new word from `REQUIRED_WORDS` and the `eta`
     assertion fails. Its value comes from the invariant's sentence.

3. **Two ways to find a named skill's file — fixed.** The 15 paragraphs now give the path from "the
   list of skills in the entry point you were started with" first. The search comes second, for a
   session started without an entry point, and covers only "the files that git lists as `SKILL.md`".
   That leaves out the ignored working copies under `.runs/` that my finding named.
   - I checked the rewrap of all 15 files with a word-level diff (`git diff --word-diff=plain`). In
     each, the only changed words are "Claude Code does not offer ... to", "is" → "stands at the path
     that the list of skills in the entry point you were started with gives, or, where you were
     started without one, in", and "named" → "that git lists as". In `project-level/lead/skill/SKILL.md`
     the brief clause of finding 4 is also changed. Nothing else changed.
   - WAY-127 (`decisions.md:3346`, "each entry point giving the path of every skill") and its
     *Rationale* ("with the path from the entry point's list") now agree with the paragraphs.

4. **A dispatched agent's brief — fixed.** `project-level/lead/skill/SKILL.md:25-26` adds "give the
   brief of an agent you dispatch for such a skill the path of that file, so that no personal skill
   of the same name stands in". That covers the dispatches the finding named at lines 116 and 142.

5. **Docstring and message — fixed, with a remainder that blocks nothing** (new Minor note B).
   - The docstring (`gate/test_skills_reach_the_way_sessions.py:3-8`) now covers both a skill a human
     could not start and entry points that would be offered to the model.
   - The failure message (`:228-229`) reads "an entry point of a skill of the-way that is missing,
     differs from its copy or is not hidden from the model".
   - `AGENTS.md:19-21` reads "report an entry point that is missing, differs from its copy or lacks
     the field, so that a human could not start the skill under its `the-way-` name or the model
     would be offered it".
   - The gap the finding named, the field, is closed.

6. **WAY-127's *Scope* — fixed.** `foundations/decisions.md:3350-3352` adds `foundation-review` and
   `product-guidelines`. `python -B elements/common/foundation_check.py` → 0, "0 errors".

The author's correction of "46" to 23 in its first report agrees with what I found in the review of
the whole change.

## What the fix itself broke

No Critical or Important finding. In the fix diff, no code exists only to make a test pass. The one
code change is the text of `entry_point_text`, and its written-out form in
`agent-instructions/test_skill_entry_points.py:64-70` comes from the requirement (finding 1), not
from the code.

### New Minor notes (block nothing; for the request's list)

A. **`foundations/part_map.md:170-171`** still says "through which a human starts the-way's skills in
   sessions on it, hidden from the model". It is unqualified in the same way as finding 1, and so is
   the failure message of the invariant test at `gate/test_skills_reach_the_way_sessions.py:229`
   ("is not hidden from the model"). The part map's sentence lies outside the fix diff, and both
   texts describe the field more than they claim Codex behaviour. This is a Minor note and does not
   reopen the review.

B. **Two summaries name fewer causes than the test reports.**
   - The failure message (`gate/test_skills_reach_the_way_sessions.py:228-229`) and `AGENTS.md:19-21`
     name three causes: missing, differs from its copy, lacks the field.
   - The test also reports an entry point whose text lacks a required sentence or a line of the list
     of skills, a wrong name or description, and an orphan directory (`entry_problems` and `problems`).
   - The lines of the report that follow the message name each cause, so a reader of a failure is not
     misled. The summaries are incomplete, not wrong.

C. **Two lines of WAY-127 are now longer than the 100 columns the rest of the file keeps:**
   `foundations/decisions.md:3344` ("a human starts a skill with the command `/the-way-<name>`. In
   the-way itself a skill hands another the-way") and the line ending "which keeps the check of the
   pin (WAY-34). The skill of instruction files serves repositories outside the-way and its". It is
   form only; no check covers it.

## Declined to judge

- Whether the other skills that start agents (outside `project-level/lead/skill/SKILL.md`) need the
  brief clause of finding 4: the findings file named only lead-project's dispatches.

## Checks

- `git rev-parse HEAD` → `f1efc257...`, matches.
- `python -B agent-instructions/skill_entry_points.py` (no `--write`) → 0, "entry points are
  current".
- `python -B elements/common/foundation_check.py` → 0, "0 errors".
- `python -B gate/run_tests.py gate` → 0 (36 tests).
- `python -B gate/run_tests.py agent-instructions` → 0 (53 tests).
- `python -B gate/run_tests.py product-guidelines` → 0 (14 tests).
- Manual checks:
  - a word-level diff of the 15 skill files (above);
  - the fix diff of `AGENTS.md`, `README.md`, the generator and its test, the gate test,
    `foundations/decisions.md` and one entry point;
  - `git grep` of the hiding phrases, and a search of the foundation, instruction and test files
    across line breaks;
  - the author's failing run.
- Not run: the other focused directories, which the fix touches only in Markdown and which the
  author reports as passing. The whole gate was not run, as the handoff forbids.
- Changed invariant test: `gate/test_skills_reach_the_way_sessions.py` (invariant
  `skill-entry-points`). The change adds a required phrase and one case. It is grounded in finding 2
  and the invariant's sentence, with its failing run kept.

## Reaches beyond the dispatch

none

## Working copies

None made; `.runs/review-fix/` was not created. `git status --short` in the worktree is empty.

## Unread material

- The 46 regenerated entry points: one (`.claude/skills/the-way-critique/SKILL.md`) read in the diff.
  The generator's "entry points are current" check and the gate's invariant test stand for the rest.
- `foundations/decisions.md`: only the fix diff of WAY-127 was read. No decision beyond it was opened
  in this review.
- No guideline file was read again in this review: those of the review of the whole change
  (`guidelines/coding.md`, `guidelines/coding-generator.md`, `guidelines/testing.md`) cover the fix's
  code and tests.

## Searches not found or unclear

none

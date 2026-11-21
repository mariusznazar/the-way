# Report of the return step

**Status:** `done` — the comparison found nothing to correct; no commit.

Head compared: `f1efc257e7d2810d4072b0a82d2a98a78e889a3d`, worktree clean.

## What I compared

The foundation entries the change writes or edits, read whole from the files at the head, against the code
and the texts of the repository:

- **WAY-127** (sentence in two paragraphs, *Scope*, *Based on*, *Relations*, *Verification*, *Rationale*,
  *Rejected*) against `agent-instructions/skill_entry_points.py` (header field, text of the entry point,
  list of paths), the 46 entry points (generator without `--write`: "entry points are current"), the 15 skill
  paragraphs, `AGENTS.md` `## Skills` and `README.md` "Using the skills". They agree: the field in both
  copies; "Claude Code offers the model no skill of the-way"; the hand-over by file in the-way itself, with
  the path from the entry point's list, and by the product's own project skill with the `the-way-` prefix in
  a product; the installer unchanged.
- **Invariant `skill-entry-points`** against `gate/test_skills_reach_the_way_sessions.py`: each clause of the
  sentence (byte-identical pair, name, description start, the field, the text leading to the `SKILL.md`, the
  words "do not call it" and "read that skill's `SKILL.md`", the line with name and path for every skill, the
  directories) has its check, the invariant is cited by the test, and the test passes on the head (the focused
  run of `gate` after the fix: exit 0).
- **Environment fact `claude-code-skill-model-hiding`** against the page I read on 2026-11-21 (live raw
  Markdown and the archived copy of 2026-11-14): the sentence says no more than the quoted sentence and table
  row; WAY-127 *Based on* names it, and `foundation_check.py` finds the reference.
- **The decisions the task and my search name or touch:** WAY-127 is the only one in *Decisions in play*.
  The search of `foundations/decisions.md`, `foundations/glossary.md` and `foundations/part_map.md` for
  "project skill", "the-way-<name>", "`the-way-` prefix" and "entry point" found WAY-128 (lines of process
  skills and their entry points answer to WAY-127), the decision on the agent type copies ("a session on the-way
  itself has tracked copies as it has those entry points (WAY-127)"), the decisions on the place of the entry
  points in the part `agent-instructions`, the part map entry of `installation` (it writes its own entry points
  in a product), and a row of the withdrawn list about the installer's entry point. None says that a session
  calls a skill of the-way or that the model is offered the entry points; none needs a change.
- **The part map**, the entry of `agent-instructions` and the entry of `installation`: the first says the
  entry points are the way a human starts the skills, hidden from the model (see Minor notes below); the
  second describes the installer, which this change did not touch.
- **The glossary:** no term of this change is in it, and no word is used against its entry; no entry written
  under WAY-95.

## What I wrote

Nothing: no entry, no correction, no commit. `python -B elements/common/foundation_check.py` → 0
("0 errors"); `python -B agent-instructions/skill_entry_points.py` → 0, "entry points are current".

Where each settlement went (as the record's *Return step* asks): the two rows of *Settlements to record* went
to WAY-127 with the invariant (row 1) and to the environment fact `claude-code-skill-model-hiding` (row 2) in
the foundation step, which is in the commits `7d063ef2` and `f1efc257`; the choice of the list of paths in
the entry point is a sentence of WAY-127 and of the invariant (a clause of the author, already put before the
human as `the cycle's` in the first report); the choice that a skill paragraph falls back to a search of the
files git lists as `SKILL.md` stands in the 15 paragraphs and is a rule of skills, which no entry carries
(the question of the decisions template's "Where it goes": an instruction for how an agent works, which stands
in a skill). No choice needed an entry, and the task or its spec excludes none.

## Left for the request (not fixed here, as the handoff says)

The three Minor notes of the review of the fix stay for the request's list, and my comparison found no other
reason to change them: `foundations/part_map.md:170-171` says "hidden from the model" without limiting it to
Claude Code; the failure message of `gate/test_skills_reach_the_way_sessions.py` and its sentence in
`AGENTS.md` name only three causes; two lines of WAY-127 exceed 100 columns (lines 3344 and 3397 of
`foundations/decisions.md`, from the fix's rewrapping).

## Checks (command → exit code)

- `python -B elements/common/foundation_check.py` → 0.
- `python -B agent-instructions/skill_entry_points.py` → 0.
- Not run: the product's gate and any directory's tests (nothing changed).

## Working copies

None made; `.runs/author-return/` was not created. `.runs/author/` (first and fix stages) is empty.

## Unread material

- The task's *Context* and *Out of scope* were not re-read, only *Settlements to record* and *Decisions in
  play*, as the handoff names them.
- The element `SKILL.md` files were not read again: no entry was written.
- `reports/review-whole-report.md` and the review of the fix: not read (the handoff gives the three notes).
- Decisions found by the search were read at the lines of the match, not whole (WAY-128's lines 3070–3085
  and the agent type copies decision at lines 3620–3630 only).

## Searches not found or unclear

- None. A count of line lengths in WAY-127 (awk, bytes) gives 3344 (106) and 3397 (117) as the two lines
  clearly over 100; five more lines count 101 bytes and may hold a multi-byte character, so I did not
  count them as over 100 columns.

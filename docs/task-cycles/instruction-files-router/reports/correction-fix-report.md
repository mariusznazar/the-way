# Correction fix report — instruction-files-router, PR #49

**Status:** `done`. **Commit:** `2ba7a47` — Fix the review of 44475cf: keep WAY-133's second half and
one place for each rule (on `44475cf`). No foundation entry changed.

## I1 — the second half of WAY-133 — fixed

- `instruction-files/SKILL.md:117`, the criterion's row "every time, without exception": the note
  now reads "an instruction says what the check is for, or carries what the check cannot catch; it
  does not replace the check (WAY-133)". It held only "may explain what the check is for".
- `instruction-files/placing.md` step 2 keeps the pointer and names the note: "propose first the
  mechanism that section gives, and the instruction its note allows."
- Check: `grep -i "cannot catch\|cannot check\|cannot do" instruction-files/*.md` now finds the row
  at `SKILL.md:117`. At `44475cf` it found nothing.

## I2 — restatements between files — fixed

- WAY-130's way out: in `instruction-files/judging.md`, *When to remove a rule*, the last sentence
  now reads "A rule that carries a decision or a step leaves by the way out 'When to add a rule'
  gives it, not by this test." The way out is stated once, in `SKILL.md` "When to add a rule".
- When the main file carries a pointer: the pointer item of `instruction-files/kind_main_file.md`
  now reads "**Pointers to ways in**, where condition 1 of the criterion allows one, in the form of
  the shared layout or 'X is done by the skill `name`', with the condition worded as the criterion
  asks; …". The clause "for activities whose way in the agent will not recognise from the request
  alone" is cut; `SKILL.md`'s row for an activity and condition 1 hold it.

## The search the findings ask for, before the commit

**Rules in two files.** I ran `overlap.py` from the scratchpad again over the eight files
(`tool_loading.md` excluded). It lists sentence pairs that share four or more 4-word sequences making
up at least 40% of the shorter sentence; its positive control on `524d9b8` found the pairs R2 named.
On the worktree before the first edit of this fix it found one rule left: the check-script list in
`SKILL.md` restated the `@path` pitfall of `kind_main_file.md`.

Reading the list against the kind files showed three more items of the same kind. `CLAUDE.local.md`
restated the main file's pitfall. The subdirectory pointing line restated the layout of files loaded
with some files. The skill pointer or copy restated the layout of skills. The list now names what
each check covers instead of restating it:
- "the two pitfalls of the main file, `@path` and `CLAUDE.local.md`";
- "the pointing line the layout of files loaded with some files gives an `AGENTS.md` in a
  subdirectory";
- "the pointer or copy the layout of skills gives a skill needed in Codex".

The `.mdc` header item stays as it was: no other file of the skill states it, since
`tool_loading.md` is excluded. After the fix the search finds only the shared header rows of the four
layout tables and two lines that share a cited address — none of them a rule.

**Content a pointer leads to but its target lacks.** I checked each pointer of `changing.md`,
`placing.md`, `writing.md`, `judging.md` and the kind files against its target. I also checked each
row cut from *Mistakes this skill prevents* and each item cut from `judging.md` and the kind files in
`44475cf` against where its content now stands, and the binding sentences of WAY-128 to WAY-133 and
WAY-256 to WAY-258 against the skill's files. Besides I1, I found one gap:
- **WAY-129's "with the condition under which to read it."** The cut row "using `@path` as a pointer
  | a path in backticks, with the condition under which to read it" carried it, and so did the cut
  defect "a pointer without a condition". The shared layout's row showed the condition only in its
  example. Its *Shared carrier* now reads "a pointer as a path in backticks with the condition under
  which to read it: 'Before X, read `path`' (WAY-129)" (`SKILL.md`, "One layout for three tools").

Everything else is held where it is pointed to:
- WAY-128: the case of the reworded pointer.
- WAY-130: the threshold, the exception and naming the mistake in "When to add a rule"; the removal
  proposals in *When to remove a rule*.
- WAY-131: *In operation*.
- WAY-132: the main file's layout row; the installer note in `judging.md`, as on the base.
- WAY-133: after I1.
- WAY-256: `kind_skill.md`.
- WAY-257: the two questions in `SKILL.md`; the rows in `judging.md`.
- WAY-258: the opening of `SKILL.md`, § 2's tables, and no pointer onward from a kind file.

Not acted on: the review's Minor and out-of-scope findings.

## Checks (after the last edit, before the commit)

| Command | Exit |
|---|---|
| `python -B gate/run_tests.py instruction-files` | 0 (OK, 5 skipped) |
| `python -B elements/common/foundation_check.py` | 0 ("0 errors") |
| `python -B agent-instructions/skill_entry_points.py` | 0 ("entry points are current") |
| `python -B instruction-files/check_instructions.py . --file instruction-files/SKILL.md --file instruction-files/judging.md --file instruction-files/changing.md --file instruction-files/placing.md --file instruction-files/writing.md --file instruction-files/kind_main_file.md --file instruction-files/kind_skill.md --file instruction-files/kind_path_rule.md` | 0 — 0 errors, 5 `dead-path` warnings on the same example paths as before |
| `git diff --check` | 0 |

All four changed files stay LF. Not run: the full gate, and no push.

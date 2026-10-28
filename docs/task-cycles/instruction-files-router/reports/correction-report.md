# Correction report — instruction-files-router, PR #49

**Status:** `done`. **Commit:** `44475cf` — Correct the review remarks on PR #49: one place for each
rule of the instruction-files skill (on `f4bbf06`; the two cycle-record commits were not touched).

No foundation entry's meaning changed. In `foundations/decisions.md` only WAY-128's *Rejected* lines
were reflowed (R6). `instruction-files/check_instructions.py` changes in its module docstring only:
the lines inside `"""…"""` at the top were reflowed, and `ast.parse` passes. All files stay LF.

## Per remark

**R1 — the order of reading.** `instruction-files/SKILL.md` § 2 now reads: "Read in full the mode's
file and the file of each kind of file the mode works on — the files under judgement, the file a
rule is placed in, the files to be written — then follow the mode's file:" (the reviewer's
wording).

**R2 — no rule in two of the skill's files.** I fixed the pairs the reviewer named. Then I checked
every file of `instruction-files/` except `tool_loading.md` and removed every other restatement the
same way: the file now names the section of `SKILL.md`, or of its own file, that holds the rule.
- `placing.md` step 2 no longer lists the mechanisms and the hook qualifier. It reads: "for a rule
  that must hold every time, propose first the mechanism that section gives". Step 3 no longer
  restates "the new wording replaces it". It reads: "as 'When to add a rule' asks before adding".
- `changing.md`: "A reworded rule replaces the sentence that stands" became "a reworded rule as 'How
  to write a single rule' gives a change to a rule".
- `judging.md`:
  - The paragraph on recommending a proposal no longer restates WAY-130's threshold and exception.
    It reads: "recommended only where 'When to add a rule' lets the rule in". The repeat, in the same
    file, of the removal rules became "Removals are proposed as 'When to remove a rule' below gives".
  - The opening sentence ("A review covers together everything that loads in the same session…")
    restated `SKILL.md` step 1 and is cut. The search of records points to "the way step 1 searches
    session records" instead of restating "by pattern, reading only the hits".
  - *Typical defects* keeps only the defects no rule of the skill states — a swollen file, a file
    never updated, contradicting instructions — under "Besides a breach of a rule of this skill:".
    The four removed items each restated a rule of `SKILL.md` or `kind_main_file.md`.
  - The hook qualifier "(CI or a check of the output; a hook only against slips)" in *In operation*
    and "(a linter, CI, or a local hook only against slips)" in *When to remove* now point to the
    mechanisms "Where a rule stands" gives.
  - *Mechanisms that clean up*: the bullet on mechanical checks run by a scan is cut, because
    `SKILL.md` "What the check script settles" states it. The bullet on reviewing sessions no longer
    restates the two defects of *In operation*. The bullet on a fix keeps only its own part (name
    the sentence that becomes unnecessary) and carries the rule on changing a rule by reference.
- `kind_main_file.md`:
  - The list of files that make a main file is cut from its first sentence; `SKILL.md` § 2's table
    of kinds holds it. The sentence "A file the main file points to holds knowledge needed now and
    then" is cut; the criterion table holds it.
  - In the pointer bullet, the example "Before X, read `path`" became "in the form of the shared
    layout". "and not derivable from the repository" is cut from the rules that always apply; the
    criterion's condition 2 holds it.
  - "What the main file does not hold" lost the items for multi-step procedures and rules for one
    part of the code (both placed by the criterion) and the history of a rule ("How to write a
    single rule" states it). It now opens "Besides what the criterion places elsewhere".
- `kind_skill.md`:
  - The opening on what a skill carries and what its files carry restated the criterion's row for
    an activity. It is now "What is particular to skills — every skill, the skills of a process the
    repository works by included."
  - The sentence "What sets the place is whether a use of the skill needs the fragment at that step,
    never the count of the skill's words or lines" restated `SKILL.md`'s paragraph on length
    (WAY-256) and is cut.
- `kind_path_rule.md`: "so a rule meant for every tool takes the shared carrier below" restated the
  shared-layout sentence of `SKILL.md` and is cut.
- `writing.md`:
  - Step 1's "Nothing the README, the configuration or the manifest already says" restated
    `kind_main_file.md`'s first item of what the main file does not hold, and is cut.
  - Step 2's list of what to ask for restated the three kinds of content of `kind_main_file.md`, and
    became "the kinds of content the main file holds".
- `SKILL.md` *Mistakes this skill prevents* keeps only the two rows no other part states — saying
  from memory when a tool loads a file, and copying the user's global rules into a shared
  repository. The six cut rows each restated a rule of `SKILL.md`, `kind_main_file.md`, `writing.md`
  or `judging.md`; the `@path` row restated the pitfall in `kind_main_file.md`.

Kept on purpose:
- The list under "What the check script settles" in `SKILL.md` names what the mechanism checks. For
  instance, `@path` appears only as `@AGENTS.md`, while the rule itself stands in
  `kind_main_file.md`. It says what the mechanism is for (WAY-133); it is not a second rule for the
  agent.
- In `judging.md`, "it can be read from the repository" and "it points to a path, skill or command
  that does not exist" stay as reasons to remove a rule of any kind; nowhere else states them as
  removal reasons.
- Same-file overlaps inside `SKILL.md` stay as the base had them: the hook qualifier in the
  criterion table, in "Loaded is not yet carried out" and in the pitfalls. WAY-258 concerns two files.

How I checked: `overlap.py` in the scratchpad lists sentence pairs across the skill's eight files
(`tool_loading.md` excluded) that share four or more 4-word sequences making up at least 40% of the
shorter sentence. As a positive control I ran it on `524d9b8`: it found the pairs R2 names (the
mechanism list, the WAY-130 threshold, "with a human present or without one") and the main file's
list of files. On the head before the commit it finds no rule restated. What remains are the shared
table headers of the layout tables, two lines that share only a cited address, and the list of the
check script against the `@path` pitfall (kept, as above).

**R3 — step 1 of placing.** `placing.md` step 1 now relies on the pointer alone, as the remark
prefers: "Name what lets the rule in, as 'When to add a rule' gives it; a rule that section does not
let in is not placed." The point "with a human present or without one" left this step. "How to write
a single rule" holds it, and step 4 applies it.

**R4 — the scope of `single-rule-compliance`.** `SKILL.md` "Where a rule stands": "…in compliance
with a single trivial target annotation in Claude Code sessions (fact `single-rule-compliance`)…".

**R5 — the two makers' best-practice pages.** At `0b8c1bd`, `principles.md` named both only in its
*Sources* list, beside no principle. I read both pages on 2026-10-28 and cite each next to the
principles its text supports:
- `https://code.claude.com/docs/en/best-practices`:
  - § What you can stop doing ("piling on emphasis mostly makes Claude over-apply the rule") beside
    the emphasis rule in `SKILL.md` "How to write a single rule".
  - § What you can stop doing ("Describe your architecture and file layout in `CLAUDE.md` | Claude
    reads the repo itself") beside "Not a description of the repository" in `kind_main_file.md`.
  - § Tell Claude what it can't see ("Anything you've had to correct twice already") beside the
    repetition signal in `SKILL.md` "When to add a rule".
- `https://learn.chatgpt.com/guides/best-practices`:
  - § Make guidance reusable with AGENTS.md ("add new rules only after you notice repeated
    mistakes") beside the same repetition signal.
  - The same section ("keep the main file concise and reference task-specific markdown files")
    beside the pointers to ways in in `kind_main_file.md`.

**R6 — reflow.** WAY-128 *Rejected*: "binding the lines that stand / today — every unchanged line
would become a breach on the day of the merge." — the words are unchanged, only the line breaks
moved. `check_instructions.py` docstring lines 3–10 are rewrapped near 100 characters; no code line
changes (`git show 44475cf -- instruction-files/check_instructions.py`).

Not in this correction: whole-change review Minor 4 (WAY-256 against WAY-125), as the remarks say.

## Checks (after the last edit, before the commit)

| Command | Exit |
|---|---|
| `python -B gate/run_tests.py instruction-files` | 0 (OK, 5 skipped) |
| `python -B elements/common/foundation_check.py` | 0 ("0 errors") |
| `python -B agent-instructions/skill_entry_points.py` | 0 ("entry points are current") |
| `python -B instruction-files/check_instructions.py . --file instruction-files/SKILL.md --file instruction-files/judging.md --file instruction-files/changing.md --file instruction-files/placing.md --file instruction-files/writing.md --file instruction-files/kind_main_file.md --file instruction-files/kind_skill.md --file instruction-files/kind_path_rule.md` | 0 — 0 errors, 5 `dead-path` warnings on the same example paths as before |
| `git diff --check` | 0 |
| `python -B -c "import ast; ast.parse(open('instruction-files/check_instructions.py', encoding='utf-8').read())"` (after the docstring reflow) | 0 |

Not run: the full gate, and no push. The change touches the files of `instruction-files/` and one
decision's line breaks, so the other directories' tests do not reach it.

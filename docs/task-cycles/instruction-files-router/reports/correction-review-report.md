FAIL 44475cf

# Review of the correction after review — instruction-files-router, PR #49

Range `f4bbf06..44475cf`, one commit (`44475cf`); `git rev-parse HEAD` in the worktree is
`44475cff68036ab3250f723ce2905e5e1c59f1df`, the head given. Reviewed against the remarks R1–R6
(`correction-remarks.md`), the frozen task, WAY-128, WAY-130, WAY-133, WAY-256, WAY-257, WAY-258 and
the fact `single-rule-compliance`. Counts: 2 blocking (Important), 4 Minor, 1 out of scope.

## Remarks

| Remark | Made? | Evidence |
|---|---|---|
| R1 — order of reading | made | `instruction-files/SKILL.md:88-89` now reads the mode's file and the kind file first, "then follow the mode's file", the reviewer's wording. |
| R2 — no rule in two of the skill's files | **not made** | The named pairs are gone, but at least two restatements remain across files (finding I2), and the way two were removed dropped a rule of WAY-133 (finding I1). The report's claim "On the head before the commit it finds no rule restated" does not hold. |
| R3 — step 1 of placing | made | `instruction-files/placing.md:5-6` relies on the pointer alone; "with a human present or without one" stands in "How to write a single rule" (`SKILL.md:224-226`), which step 4 applies. |
| R4 — scope of `single-rule-compliance` | made | `SKILL.md:146-147` "…a single trivial target annotation in Claude Code sessions (fact `single-rule-compliance`)"; matches the fact's "across Claude Code CLI sessions" (`foundations/environment_facts.md:164`). |
| R5 — the two best-practice pages | made | Both addresses now stand beside principles (`SKILL.md:231-232`, `:246-249`; `kind_main_file.md:17-18`, `:21-22`). I fetched both pages: every quoted passage exists under the section named (see checks). One wording note: Minor M4. |
| R6 — reflow | made | WAY-128 *Rejected*: word sequence identical before and after, lines now 96 and 75 characters. `check_instructions.py`: docstring words identical, AST identical apart from the docstring, longest docstring line 98. |

## Findings

### Important

**I1 — the correction drops the second half of WAY-133 from the skill.** Place:
`instruction-files/placing.md:7-8` and the removed row of `SKILL.md` *Mistakes this skill prevents*.
Before the correction the skill said twice that, for a rule that must hold every time, an
instruction carries what the mechanism cannot do: `placing.md` step 2 at `f4bbf06` ("…and an
instruction only for what the mechanism cannot do") and the row "placing a rule that must hold every
time only as an instruction | a mechanism, and an instruction for the rest" (`SKILL.md:278` at
`f4bbf06`; both already stood in the base `0b8c1bd`, `SKILL.md:130` and `:159`). The correction
replaced the first with "propose first the mechanism that section gives" and cut the row as a
restatement. The section pointed to holds only "an instruction may explain what the check is for,
but does not replace it (WAY-133)" (`SKILL.md:117`) — it does not say that the instruction carries
the part the mechanism cannot check. WAY-133 says: "The instruction file then says what the
mechanism is for, or carries what the mechanism cannot check." At `44475cf`, `grep -i "cannot do\|for
the rest\|cannot check" instruction-files/*.md` finds nothing. Why it matters: an agent placing such a
rule now proposes a mechanism and has no rule telling it to keep, as an instruction, the part no
check can catch — the skill falls short of a decision in play, and the correction was to change no
meaning. The pointer is the right form; it fails only because its target lacks the content. Fix:
state the half once, in the row's *Notes* of `SKILL.md:117` (for instance "an instruction says what
the check is for, or carries what the check cannot catch; it does not replace the check (WAY-133)"),
and keep the pointer in `placing.md`.

**I2 — restatements between files remain (R2, WAY-258 "No rule stands in two of its files").**
- `SKILL.md:249-252` "a rule that carries a decision the repository records, or a step of an
  activity …, needs no repeated mistake — its reason and its way out are that decision or that
  work" and `SKILL.md:261-262` "the named mistake is later its way out", against
  `judging.md:79-81` "it was added for a mistake that can no longer be named — it is proposed for
  removal; … A rule that carries a decision or a step of an activity goes with that decision or that
  step, not by this test." The way out of a decision-carrying rule is stated in both files — the
  same rule, half of the WAY-130 pair R2 named, left in the removal list.
- `SKILL.md:116` (row "during an activity", note: "when the activity has no obvious way in, the main
  file points to it in one sentence") with condition 1 at `SKILL.md:122` ("or it points to a way in
  that would not be found otherwise"), against `kind_main_file.md:19-21` "Pointers to ways in … for
  activities whose way in the agent will not recognise from the request alone". The same rule — when
  the main file carries a pointer — in two files; the correction applied exactly this test to the
  main file's list of files and to "not derivable from the repository" and cut them, but not here.
Why it matters: the human's remark binds the correction to "no rule in two of the skill's files",
and WAY-258's rationale names the cost: "A rule kept in two files drifts." Fix the same way: the
removal bullet in `judging.md` points to the exception of "When to add a rule" (or `SKILL.md` drops
"its way out are…" and the removal list holds it alone); the pointer item of `kind_main_file.md`
says "Pointers to ways in, where condition 1 of the criterion allows one, in the form of the shared
layout…".

### Minor

**M1 — the rule on the words of a file narrows to one mode.** `SKILL.md` *Mistakes* lost the row
"headings and wording taken from the principles — surroundings, way in, route, trigger | the words
the file's readers use for the product" (in the base, `0b8c1bd` `SKILL.md:163`). What remains is
`writing.md:14-15`, which covers section names in the mode write only. In the modes place and change
a rule's wording drawn from the skill's own terms ("trigger", "way in") now meets no rule. Restoring
the point once in "How to write a single rule" would cover every mode.

**M2 — "step 1" reads two ways.** `judging.md:8-9` "the way step 1 searches session records": the
file's own numbered list under the same heading starts at line 13 ("1. The check script's errors…"),
while the target is `SKILL.md` § "1. Read". Every other pointer of the mode files names a section by
its title; "as section '1. Read' searches session records" would match them.

**M3 — `kind_skill.md:3-4` is a sentence without a verb.** "What is particular to skills — every
skill, the skills of a process the repository works by included." It still carries what To do 2
needs (every skill, process skills included), but reads as a fragment; e.g. "This file holds what
is particular to skills — …".

**M4 — the emphasis citation widens and hardens its source.** `SKILL.md:231-232`: "piled-on
emphasis makes a current model over-apply the rule". The page says (§ What you can stop doing):
"Current ones follow a plainly worded line, and piling on emphasis mostly makes Claude over-apply the
rule." The skill drops "mostly" and turns "Claude" into "a current model", in a skill that serves
three tools. "mostly makes current Claude models over-apply the rule" keeps the source's reach.

### Out of scope

**O1 — `tool_loading.md` repeats the positive control.** `tool_loading.md:185-187` "One file in every
variant must load — the positive control" and `judging.md:59` "always with a positive control, a
file that must load". The remark excludes `tool_loading.md` ("holds no rules of placement"); this is
a rule of measurement, not of placement, so it lies outside R2 as the human worded it. Noted for the
task that rebuilds the-way's skills.

## Declined to judge

- `kind_main_file.md:13-18` "Not a description of the repository …" and `:28-29` "repetitions of the
  README …" against condition 2 (`SKILL.md:123`): set aside, as the kind file's application with its
  own evidence (fact `context-file-effect`, the cited page), not a restatement of the condition.
- The list under "What the check script settles" (`SKILL.md:266-276`) against the pitfalls of
  `kind_main_file.md:45-49` and the layouts of the kind files: kept as the author argues — it names
  what the mechanism checks (WAY-133), not a second rule for the agent.
- Facts on tool loading repeated in `SKILL.md:187-190` and `kind_path_rule.md:11`: facts, not rules
  of placement.
- `kind_skill.md:8-14` (WAY-256 question) against the activity row of `SKILL.md:116`: the task's own
  design (To do 1-2, WAY-256/258), passed by both earlier reviews; not a change of this range.
- Whole-change Minor 4 (WAY-256 against WAY-125): excluded by the remarks.

## Trust boundary and irreversible operation

`instruction-files/check_instructions.py`: the change is to the module docstring only — AST of
`f4bbf06` and `44475cf` identical once the docstring is blanked, docstring words identical, no CRLF.
No operation that cannot be undone.

## Checks

| Command / method | Exit / result |
|---|---|
| `git rev-parse HEAD` | `44475cff…`, matches |
| `python -B gate/run_tests.py instruction-files` | 0 — 104 tests, OK (5 skipped) |
| `python -B elements/common/foundation_check.py` | 0 — "0 errors" |
| `python -B agent-instructions/skill_entry_points.py` | 0 — "entry points are current" |
| `python -B instruction-files/check_instructions.py . --file` each of the 8 skill files (not `tool_loading.md`) | 0 — 0 errors, 5 warnings (`dead-path` on example names, as the author reports) |
| `git diff --check f4bbf06..44475cf` | 0 |
| word-sequence diff of `foundations/decisions.md` between `f4bbf06` and `44475cf` | identical (R6) |
| Python `ast` comparison of `check_instructions.py`, docstring blanked; docstring word compare; max line length | AST equal, words equal, 98 chars |
| `git status --short` after the checks | clean — the worktree was not changed |
| Manual: read every file of `instruction-files/` at `44475cf` whole except `tool_loading.md` (its method section read), pairwise for rules stated in two files | I2, M1, O1 |
| `git grep` at `0b8c1bd`, `f4bbf06`, `44475cf` for "cannot do / for the rest / cannot check" | present at both earlier commits, absent at head (I1) |
| WebFetch `https://code.claude.com/docs/en/best-practices` (2026-10-28) | § What you can stop doing holds the emphasis row and "Describe your architecture and file layout in `CLAUDE.md` / Claude reads the repo itself"; "Anything you've had to correct twice already" stands in § Keep CLAUDE.md short under § Tell Claude what it can't see |
| WebFetch `https://learn.chatgpt.com/guides/best-practices` (2026-10-28) | § Make guidance reusable with `AGENTS.md` holds "add new rules only after you notice repeated mistakes" and "reference task-specific markdown files …" |

Not run: the full gate (`python -B gate/run_tests.py` without a directory), as the dispatch says.

## Reaches beyond the dispatch

- `instruction-files/principles.md` at `0b8c1bd` (grep for the two addresses) — to check R5's
  premise that the pages stood only in *Sources*; it holds.
- `instruction-files/SKILL.md` at `0b8c1bd` (grep) — to see whether the WAY-133 half dropped in I1
  and the row of M1 were in the base; both were.
- The two best-practice pages on the web — to verify the passages R5 cites (source fidelity).
- `instruction-files/tool_loading.md` lines 1-12 and 182-196 — to judge whether its exclusion from
  R2 hides a placement rule (O1).
- WAY-130 and WAY-133 read as quoted in the frozen task's *Decisions in play*; WAY-256 and WAY-258
  read whole in `foundations/decisions.md`.

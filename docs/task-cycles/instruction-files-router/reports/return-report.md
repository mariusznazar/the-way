# Return-step report — instruction-files-router

**Status:** `done`. **Commit:** `524d9b8` — Return step: bring the skill of instruction files in
line with WAY-256, WAY-258 and its fact (on `634fa3b`).

The first version of this report left three mismatches alone, because the return handoff said not to
act on Minor findings. The orchestrator withdrew that line: the return step corrects whatever no
longer matches the entries (WAY-11). The three are corrected below, and so is a fourth of the same
kind that I found while correcting them.

## What was compared, against which code

| Entry | Compared with | Result |
|---|---|---|
| WAY-128 (changed) | `instruction-files/SKILL.md` "Where a rule stands" (the pointer is reworded first; the rule stands whole only after a recorded miss, with WAY-130's threshold); the last sentence against `kind_skill.md` and WAY-256 | matches |
| WAY-256 (new) | `kind_skill.md`; `SKILL.md` on what is measured; how `SKILL.md` itself is laid out | **mismatch → corrected (1)** |
| WAY-257 (new) | `judging.md` output item 2; the two questions in `SKILL.md` | matches |
| WAY-258 (new) | the kind files and mode files, named directly by `SKILL.md` § 2; no rule in two files; no kind file points to another | **two mismatches → corrected (2) and (4)** |
| `claude-skill-nested-references` (new) | the citing sentence in `SKILL.md` "Ways in and routes" | matches |
| `instruction-density-accuracy` (changed) | the citing sentence in `SKILL.md` | matches |
| `single-rule-compliance` (cited by WAY-256) | the citing sentence in `SKILL.md` "Where a rule stands" | **mismatch → corrected (3)** |
| *Decisions in play*: WAY-35, WAY-127, WAY-125, WAY-129, WAY-130, WAY-133, WAY-100, WAY-09 | the files of the skill, the entry points, the docstring of `check_instructions.py` | match. WAY-09's "the principles … stand together in `instruction-files/`" still holds |
| WAY-33 findings: WAY-21, WAY-167, WAY-192, WAY-212, WAY-245 | their citations of WAY-128 and `instruction-density-accuracy` | match |
| Part map: `instruction-files`, `agent-instructions`, `product-guidelines`, `decisions`, `environment-facts` | files and responsibilities | match. `instruction-files/**` covers the new files, and the sentence still describes them |

## Corrections

1. **WAY-256 vs the Change, Place and Write procedures.** Each procedure is needed by one mode only,
   and the change reworded each of them (Place step 2 changed meaning). By WAY-256 such text stands
   in a file beside the skill that its step names. The same reading of "variant" as "mode" is the
   one this change already applied to the judge mode. They now stand in `instruction-files/changing.md`,
   `instruction-files/placing.md` and `instruction-files/writing.md`. The table of modes in
   `SKILL.md` § 2 names each mode's file directly, beside `judging.md`, and none of them points to
   another file. They name sections of `SKILL.md`, which is already read, never a file to read. The
   sentence "The table is a batch of decisions; edit nothing until it is accepted" moved from the
   former Judge section of `SKILL.md` into `judging.md`. The opening of `SKILL.md` now says that what
   only one mode needs stands in that mode's file (WAY-256, WAY-258). WAY-256's meaning is
   unchanged.
2. **WAY-258 vs `kind_skill.md`.** The clause "the step names the file directly, and that file
   points to no further file" is cut. The one-level rule stands in `SKILL.md` alone ("Ways in and
   routes", and the criterion table's "one level deep").
3. **`single-rule-compliance` in `SKILL.md`.** The sentence now reads: the four variables "produced
   no detectable contrast, after multiple-testing correction, in compliance with a single trivial
   target annotation", as the fact gives it.
4. **WAY-258 vs `placing.md` step 1** (found while making correction 1). The step restated the WAY-130
   rule that "When to add a rule" in `SKILL.md` holds: a mistake found more than once, unless the
   rule carries a decision or a step. The step now says to name what lets the rule in "as 'When to
   add a rule' gives it" — the mistake with its records, or the decision or step it carries — and
   whether a human is present. It adds that a rule with neither is not placed. The meaning is
   unchanged.

Left alone, as the orchestrator directs: Minor 3, 4 and 5. Not changed either: `judging.md`'s
paragraph on recommending a proposal. It applies WAY-130 to a judgement (proposals listed as not
recommended, with the search named) and does not repeat the rule's wording.

## What else step 11 writes

- **Sources the change rests on that the foundation lacks:** none to write. Two studies are cited
  inline without a fact: https://arxiv.org/abs/2511.12884v2 is already quoted in WAY-130's *Based on*,
  and https://arxiv.org/abs/2606.15828v5 has no decision or invariant resting on it, so it would be a
  fact with nothing to name it (WAY-73).
- **Glossary:** none. The new entries use "a file a tool adds to every session", "step" and
  "variant" in their usual meanings.
- **Settlement rows missed:** none. All seven rows are written (see `author-report.md`).
- **Choices that bind after the merge (WAY-36):** none beyond WAY-256 and WAY-258. The new mode files
  are what WAY-256 calls for.
- **Invariants:** none.

## Entries written or changed in this step

None. The corrections bring the code to the entries. The meaning sentences for the entries of
`634fa3b` stand in `author-report.md`.

## Changed files in `524d9b8` (added / removed lines)

`instruction-files/SKILL.md` +19 −60 · `instruction-files/changing.md` +7 (new) ·
`instruction-files/placing.md` +15 (new) · `instruction-files/writing.md` +18 (new) ·
`instruction-files/judging.md` +2 · `instruction-files/kind_skill.md` +1 −2.

## Checks

| Command | Exit |
|---|---|
| `python -B gate/run_tests.py instruction-files` | 0 (104 tests, OK, 5 skipped) |
| `python -B elements/common/foundation_check.py` | 0 ("0 errors") |
| `python -B agent-instructions/skill_entry_points.py` | 0 ("entry points are current") |
| `python -B instruction-files/check_instructions.py . --file` on `SKILL.md`, `judging.md`, `changing.md`, `placing.md`, `writing.md` and the three kind files | 0 — 0 errors, 5 `dead-path` warnings on the same example paths as before (`.claude/rules/`, `x/AGENTS.md`, `.the-way/instruction-files/SKILL.md`, `_zadania\` in the root `AGENTS.md`) |
| `python -B instruction-files/check_instructions.py . --file instruction-files/placing.md` (after the last edit) | 0 |
| `git diff --check` (before the commit, after the last edit) | 0 |

The test run came before the last edit, which changed only step 1 of `placing.md`; no test reads that
file. Not run: the full gate, which is the orchestrator's. Per step 11, the return step's commit
needs a review of its range (`634fa3b..524d9b8`) by a fresh reviewer.

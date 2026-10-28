PASS 524d9b8838cc0dd285fbb46630bbf7831477a356

# Review of the return step — instruction-files-router

Range `634fa3b..524d9b8` (one commit, `524d9b8`, "Return step: bring the skill of instruction files
in line with WAY-256, WAY-258 and its fact"). `git rev-parse HEAD` in the worktree is
`524d9b8838cc0dd285fbb46630bbf7831477a356`, the head given. The working tree was clean.

Counts: blocking 0 · Minor 4 · out of scope 0 (and 4 lines of Declined to judge).

## What the range does, verified

| Claim of the return report | Verified how | Result |
|---|---|---|
| Correction 1: Change, Place and Write move into `changing.md`, `placing.md`, `writing.md`, named by the table of modes (WAY-256) | removed lines of `SKILL.md` set against the three new files, line by line | the move is lossless: Change and Write are word for word; Place steps 2-5 are word for word, step 1 is reworded (correction 4); the sentence "The table is a batch of decisions; edit nothing until it is accepted" lands in `instruction-files/judging.md:30`. The table at `instruction-files/SKILL.md:81-86` names each mode's file directly. One loss in ordering: Minor 1 |
| Correction 2: the one-level clause is cut from `kind_skill.md` (WAY-258) | `instruction-files/kind_skill.md:14-15` | done; the rule stands in `SKILL.md` alone (`:118`, `:174-179`) |
| Correction 3: `single-rule-compliance` cited with its qualifiers | `instruction-files/SKILL.md:144-147` against `foundations/environment_facts.md:162-166` | "after multiple-testing correction" and "trivial target annotation" are back; one scope of the fact is still left out: Minor 4 |
| Correction 4: Place step 1 names what lets a rule in "as 'When to add a rule' gives it" (WAY-258) | `instruction-files/placing.md:5-7` against `SKILL.md:242-247` | the restatement is gone; the new wording reads ambiguously: Minor 3 |
| "WAY-258 … two mismatches → corrected", i.e. no other rule now stands in two files | reading of the three new files against `SKILL.md` | not complete: the move creates further restatements across files, of the same kind as correction 4: Minor 2 |
| "WAY-256's meaning is unchanged"; "no entries written or changed" | `git diff --stat 634fa3b..524d9b8` | only `instruction-files/` files change; no foundation file is touched |
| Trust boundary: the range does not touch `instruction-files/check_instructions.py` | `git diff --stat` | confirmed |
| Changed-files line counts | `git show --stat 524d9b8` | match (`SKILL.md` +19 −60, `changing.md` +7, `placing.md` +15, `writing.md` +18, `judging.md` +2, `kind_skill.md` +1 −2) |

No reference anywhere in the worktree (outside `.runs/`) points to the removed `SKILL.md` sections
Judge, Change, Place or Write; the four mode files are named only by `SKILL.md`.

## Findings

### Critical

None.

### Important

None.

### Minor

**Minor 1 — `instruction-files/SKILL.md:88-89`: the step now reads the kind file after the mode's
procedure is followed.** The new text: "Read the mode's file in full and follow it. Then read in
full the file of each kind of file the mode works on". On `634fa3b` the kind files were read in § 2
before any mode section, and the Judge section said "Read `judging.md` in full and judge by it,
with the file of each kind under judgement". That clause did not travel: `judging.md` names no kind
file, so taken in order, "follow it. Then read" puts the kind file — the per-fragment question of
`kind_skill.md` (WAY-256), the three conditions as applied in `kind_main_file.md` — after the
judgement it is needed for. Why it matters: the router's purpose (To do 1) is that the step judging
a kind reads that kind's rules; a literal reading judges first. An agent will most likely read both
files up front, so it does not block. Wording that keeps the order: "Read in full the mode's file and
the file of each kind of file the mode works on …, then follow the mode's file." Evidence:
`git diff 634fa3b..524d9b8 -- instruction-files/SKILL.md`, hunks at `:78` and `:93`.

**Minor 2 — the move puts rules into two files, against WAY-258, which correction 4 applied to step 1
only.** WAY-258: "No rule stands in two of its files"; its *Verification* names "the rule on
emphasis stands both in the file of skills and in the file of the main file" as a violation. Before
this range the following pairs stood in one file, `SKILL.md`; after it, in two:
- `instruction-files/placing.md:12-13` ("Search the instruction files for a rule on the same
  subject; when one stands, the new wording replaces it") and `instruction-files/SKILL.md:253-255`
  ("a check whether a rule on the same thing already stands elsewhere — then that one is replaced
  instead of a second one being added"); also `SKILL.md:236-238` ("A change to a rule replaces its
  previous wording where that wording stood") and `instruction-files/changing.md:5` ("A reworded
  rule replaces the sentence that stands");
- `instruction-files/placing.md:8-11` ("When it must happen every time, propose the mechanism first
  — a CI check, a linter, a check of a step's output, or a local git hook where the rule guards
  against slips …") and `SKILL.md:117` and `:180-182` (WAY-133, same list, same hook qualifier).

The return report also says `judging.md`'s paragraph on recommending a proposal "does not repeat the
rule's wording"; it does repeat its rule: `instruction-files/judging.md:32-35` "recommended only for
a mistake found more than once; … unless the rule carries a decision the repository records or a
step of the activity its file leads (WAY-130)" against `SKILL.md:244-247` "A rule enters only for a
mistake found more than once … The exception: a rule that carries a decision the repository
records, or a step of an activity in the file that leads that activity". That one predates the
range (it passed the whole-change review), but it is the same restatement correction 4 removed from
step 1. Why it matters: WAY-258's rationale — "A rule kept in two files drifts" — and the return
report's claim that WAY-258 now matches. Today each pair says the same, so the effect is drift
risk only, the grade the whole-change review gave the analogous restatement (its Minor 2). The fix
is the one correction 4 used: the mode file names the `SKILL.md` section ("as 'When to add a rule'
gives it", "by 'Where a rule stands'") instead of restating it.

**Minor 3 — `instruction-files/placing.md:5-7`: "A rule with neither is not placed" reads against
the wrong antecedent and drops the threshold from the step's own text.** The sentence follows
"whether the rule applies with a human present or without one", so "neither" first attaches to
that pair, which cannot be meant; the grounds it means are three (a mistake, a decision, a step),
not two. And "the mistake it removes, with the records where it was found" no longer says "more
than once"; the threshold now lives only behind "as 'When to add a rule' gives it". Meaning is
formally kept by that pointer, so it does not block. Suggested: "A rule with none of these is not
placed", and keep "found more than once" in the clause or rely on the pointer alone without listing
the grounds.

**Minor 4 — `instruction-files/SKILL.md:144-147`: the citation of `single-rule-compliance` still
leaves out the fact's scope.** The fact measured "compliance with a trivial target annotation
across Claude Code CLI sessions" (primarily Sonnet 4.6, per its source passage); the principle
draws from it that "a file has no threshold of length" for a skill that serves Claude Code, Codex
and Cursor. Correction 3 restored the two qualifiers the whole-change review named but not this
one, though the return report says the sentence now reads "as the fact gives it". Why it matters:
the same source-fidelity concern as Minor 6 of that review — a reader takes the finding as
tool-independent. Adding "in Claude Code sessions" after "target annotation" closes it.

## Declined to judge

- Minor 3, 4 and 5 of the whole-change review (`reports/review-report.md`): left on purpose by the
  orchestrator and outside this range.
- Whether `tool_loading.md`, read in full at every use (`SKILL.md:52`), should be split by WAY-256:
  untouched by the range, and the rebuild of skills is *Out of scope* of the task.
- Whether the "Mistakes this skill prevents" table (`SKILL.md:273-284`) restates rules of the body
  in the same file: WAY-258 forbids a rule in two files, not twice in one, and the table predates
  the range.
- The repetition inside `judging.md` (`:36-37` and `:85-86`, on removing a rule whose mistake can no
  longer be named): one file, and it predates the range.

## Checks run

| Command / method | Result |
|---|---|
| `git rev-parse HEAD` | `524d9b8838cc0dd285fbb46630bbf7831477a356`, the head given |
| `git diff 634fa3b..524d9b8`, `git log 634fa3b..524d9b8`, `git show --stat 524d9b8` | one commit; six files, all in `instruction-files/` |
| `python -B gate/run_tests.py instruction-files` | exit 0 — 104 tests, OK (skipped=5) |
| `python -B elements/common/foundation_check.py` | exit 0 — "0 errors" |
| `python -B agent-instructions/skill_entry_points.py` | exit 0 — "entry points are current" |
| `python -B instruction-files/check_instructions.py . --file` on `SKILL.md`, `judging.md`, `changing.md`, `placing.md`, `writing.md`, `kind_main_file.md`, `kind_skill.md`, `kind_path_rule.md` | exit 0 — 0 errors, 5 `dead-path` warnings, all on example paths (`_zadania\`, `.the-way/instruction-files/SKILL.md`, `.claude/rules/` twice, `x/AGENTS.md`), the same as before the range |
| `git diff --check 634fa3b..524d9b8` | exit 0 |
| `git ls-files --eol` on `SKILL.md` and the three new files | every file `i/lf w/lf` |
| Manual: removed `SKILL.md` lines against the new mode files | lossless move except Place step 1 (correction 4) and the "with the file of each kind" clause (Minor 1) |
| Manual: grep across the worktree (without `.runs/`, `.git/`) for the removed section names and the new file names | no dangling reference; hits in `migrate_foundation.py`, `slice_size.py` and `project-level/task/skill/SKILL.md:236` are unrelated |
| Manual: the new mode files and `judging.md` against `SKILL.md`, rule by rule, for WAY-258 | Minor 2 |
| Manual: `SKILL.md:144-147` against the fact `single-rule-compliance` | Minor 4 |

Not run: the full gate (`python -B gate/run_tests.py` without a directory) — the orchestrator's, as
the handoff says.

## Reaches beyond the dispatch

- `foundations/decisions.md` WAY-257 (read whole, beside WAY-256 and WAY-258) — the return report
  compares `judging.md` with it.
- `foundations/environment_facts.md` `claude-skill-nested-references` — the one-level rule
  correction 2 leaves in `SKILL.md` alone rests on it.
- `foundations/part_map.md` entry `instruction-files`; invariants `element-directory-contents` and
  `skill-rule-source` — to confirm that new files in `instruction-files/` break no part or
  invariant (they do not: `instruction-files/**`, and neither invariant's *Part* covers it).
- `instruction-files/check_instructions.py:1-12` and `instruction-files/test_check_instructions.py`
  (grep for `SKILL.md`, `judging`, `kind_`) — whether the script or its tests depend on the moved
  sections; they do not.
- `reports/review-report.md` — the dispatch named it as context; read for Minor 1, 2 and 6 and the
  grade of the analogous restatement.

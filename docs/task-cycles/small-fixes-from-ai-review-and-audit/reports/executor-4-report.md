# Executor report — slice 4 (the other nine skills)

**Status:** done with concerns

**Commit:** `d6ab032d` on `task/small-fixes-from-ai-review-and-audit` (base `5160a7b9`). Not pushed.

**Files changed (9, +28 / -64 in total):**
- `foundation-review/SKILL.md`
- `product-guidelines/coding/SKILL.md`
- `product-guidelines/styleguide/SKILL.md`
- `product-guidelines/testing/SKILL.md`
- `project-level/lead/skill/SKILL.md`
- `project-level/plan/skill/SKILL.md`
- `project-level/skill/SKILL.md`
- `project-level/task/skill/SKILL.md`
- `project-level/technology/SKILL.md`

Each skill's "named skill is read as a file, not called ... In a product, it is the project skill ... prefix" block became the one instruction, adapted to the skill's words ("named below", "named here", "named in this skill or in a file beside it"), in the form slice 3 used in `elements/decisions/skill/SKILL.md`. The description lines and the frontmatter are unchanged.

**Checks (worktree root, run after the commit's edits):**

| Check | Command | Exit | Result |
|---|---|---|---|
| Old sentence gone | `git grep -n "read as a file, not called"` | 0 | Only `elements/common/hand_over.md:6` among tracked files |
| Entry points | `python -B agent-instructions/skill_entry_points.py` | 0 | "entry points are current" |
| Product guidelines gate | `python -B gate/run_tests.py product-guidelines` | 0 | 14 tests, OK |
| Foundation check | `python -B elements/common/foundation_check.py` | 0 | "0 errors" |

Baseline before any edit, same commands: entry points exit 0, product-guidelines exit 0 (14 tests, OK), foundation check exit 0. The grep before the edit listed the same nine skills plus `hand_over.md`.

**Failing run first:** none. The slice changes prose only, and the checks above are the gate's existing structure checks, which passed before and after. No new test was written, so no failing run exists to report.

**Own-work check (CLAUDE/method section 3):**
- Requirement: no skill outside `elements/common/hand_over.md` keeps the hand-over sentence, and each of the nine carries the one instruction, with the rest of each paragraph untouched.
- Check: the `git grep` above, plus reading each diff. `git diff` shows only the paragraph blocks changed; no other line moved.
- Weakest point: the product sentence "never a personal copy" in `project-level/lead/skill/SKILL.md` is gone. It was part of the old product clause, and `hand_over.md` says only "the project skill of that name with the `the-way-` prefix". The lead skill keeps the-way's brief rule (give the path of the `SKILL.md` in the brief). A product session therefore no longer reads the "never a personal copy" rule in that skill. I did not restore it because the slice says to replace the sentences by the one instruction. Result: a deliberate loss that the orchestrator should decide on (see questions).
- What it showed: the grep for `personal copy` / `personal skill` in the nine skills finds only `project-level/lead/skill/SKILL.md:23`, which is the-way's brief rule, as the slice keeps it.

**Reaches beyond the handoff:**
- `elements/common/skill/SKILL.md` lines 12-26, read in part, to compare slice 3's wording of the instruction with the element skills.
- `git grep` over `AGENTS.md`, `installation/` and `agent-instructions/` for the phrases "personal copy", "the-way-` prefix" and "entry points of the-way" (search only, no reading of those files).
- The commit hook read `.ai/rules/git.md` (the git rules), as the hook asked; I followed it (English message, path-based add).

**Working copies:** I made one, `.runs/executor-4/commit_msg.txt`, to hold the commit message. Removed; the directory is gone. No other copy was made.

**Unread material:**
- `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md:40` (To do point 9) — not read.
- `foundations/decisions.md:3329-3422` (WAY-127), `:1492-1522` (WAY-35), `:3423-3538` (WAY-256) — not read.
- `foundations/part_map.md:65-81`, `:82-103`, `:117-127`, `:214-225` — not read.
- The slice's *Read* lines name these; I worked from the slice text, `task-cycle/change/SKILL.md` and `slice.md` (read whole), `elements/common/hand_over.md` (whole) and `elements/decisions/skill/SKILL.md` (whole) as the model. The nine skills were each read whole before editing.

**Searches not found or unclear:**
- A dangling pointer exists before this slice and I left it: `project-level/plan/skill/SKILL.md:85` says "Read `hand_over.md` beside this skill", and `project-level/plan/skill/assign_entries.md:15` and `existing_plan.md:14` say the same. No `hand_over.md` exists in `project-level/plan/skill/`. These are not among the nine SKILL.md files the slice names, so I did not change them. The product-guidelines gate passes with them in place.
- Other tracked text still speaks of the-way's skills' entry points: `agent-instructions/skill_entry_points.py:211` and `agent-instructions/test_skill_entry_points.py:65` (generator text, which the slice says not to change), and installer texts `installation/install.py:161, 197, 351` and `installation/test_install.py:67, 122, 275` (product-side wording of the installer). None is a hand-over sentence of a skill; I left them.

**Questions for the orchestrator:**
1. Restore the product rule "never a personal copy" in `project-level/lead/skill/SKILL.md`, by a one-clause addition to the instruction or to `elements/common/hand_over.md`? Recommended: add it to `hand_over.md`, since it then holds for every skill; this touches slice 3's file, so it is a decision for you.
2. The dangling `hand_over.md` pointers in `project-level/plan/skill/` (three places, listed above): fix in a later slice, or accept? Recommended: a small follow-up slice that points them to `elements/common/hand_over.md`, since the slice's Goal says that file is the only one that holds the sentences.

## Rename after the orchestrator's decision

**Commit:** `5bdef59f` on top of `d6ab032d`, one commit. Not pushed. Worktree clean.

**What changed:**
- `elements/common/hand_over.md` renamed to `elements/common/reaching_another_skill.md` (`git mv`); its only content change is the product paragraph, now ending "...with the `the-way-` prefix, never a personal copy of the same name".
- The path `elements/common/hand_over.md` replaced by `elements/common/reaching_another_skill.md` in 16 files: the six element skills, the nine skills, and the WAY-127 Verification line in `foundations/decisions.md` (one line each, 17 lines in total with the renamed file).
- Not touched: `project-level/plan/skill/SKILL.md:81`, `assign_entries.md:15`, `existing_plan.md:14` (`hand_over.md` beside the plan skill), and `project-level/plan/skill/hand_over.md`.
- Plan-skill sentence (`project-level/plan/skill/SKILL.md:18`) names the file by its full path only: `elements/common/reaching_another_skill.md`.

**Search (item 4):** `git grep -n "elements/common/hand_over"` (excluding `.runs/`) finds nothing; exit 1.

**Checks (item 5), each with its command and exit code:**

| Check | Command | Exit | Result |
|---|---|---|---|
| Entry points | `python -B agent-instructions/skill_entry_points.py` | 0 | "entry points are current" |
| Foundation check | `python -B elements/common/foundation_check.py` | 0 | "0 errors" |
| Product guidelines | `python -B gate/run_tests.py product-guidelines` | 0 | 14 tests, OK |
| Elements common | `python -B gate/run_tests.py elements/common` | 0 | 289 tests, OK (136 s) |

The `elements/common` run first went to the background when it passed the 120 s default timeout; I stopped that copy and reran it in the foreground with a 600 s timeout, which gave the exit code above. Only the one run counts.

**Working copies:** a commit-message file under `.runs/executor-4/`, removed together with its directory. None left.

**Unread material:** none new; the three plan-skill references were read by grep only, as the orchestrator's instruction covers them.

**Searches not found or unclear:** none.

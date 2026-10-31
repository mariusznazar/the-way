PASS 9ea5fff99e2cd1a530db2eb6689181799ce4624e

# Review of the fix of the reconciliation's findings

- Range: `c69e355..9ea5fff`, one commit, `9ea5fff docs: name the reserved rule and the task run in the skills' SKILL.md`. `git rev-parse HEAD` gives the head named.
- Read: `reports/merge-review-findings.md`, `reports/merge-fix.md`, the diff of the range.
- Bound: the findings file, and what the fix itself broke (`task-cycle/review/fix.md`).
- No invariant test changed. The range changes three `SKILL.md` files and no `.py` file.

## The three findings

| # | Finding | State | Evidence |
|---|---|---|---|
| 1 | `refine-task` does not name the reserved rule or the run's file | **fixed** | Step 3 now names `project-level/technology/reserved_choices.md` at `project-level/task/skill/SKILL.md:45`, and the section *Orchestrated mode* names `project-level/technology/task_run.md` at `:22` |
| 2 | `write-spec` does not name the reserved rule | **fixed** | Step 2 names the file in both forms at `task-cycle/spec/SKILL.md:41-42` |
| 3 | `implement-task` names the file that reads the rule, not the rule | **fixed** | `task-cycle/skill/SKILL.md:218-220` names `reserved_return.md` and `reserved_choices.md` under one condition |

None was contested. The fix took the reading to weigh on finding 3, so no ruling on it is needed.

**Finding 1.** Each `SKILL.md` condition is the step's file's condition word for word: for
`resolve_gaps.md:25-26` "needs a language, … that no decision, approved definition or accepted answer
settles", and for `orchestrated_mode.md:21-22` "whether `refine-task` starts it for a reserved choice or
the human asked for it". The form is that of step 1 of the same skill. A single path is right here:
`SKILL.md:12-13` says where the-way stands in a product, and the two step's files write the path singly.

**Finding 2.** The condition equals `design.md:18-19` word for word, and the path has the two-path form
the finding asked for, the same as `task-cycle/change/SKILL.md:101-102`.

**Finding 3.** The sentence's own condition now covers both files, and the check stays in
`reserved_return.md`, as the finding required. "Of the pinned the-way" is the wording of
`reserved_return.md:14`.

The search that showed the defect now shows each pointer named in its `SKILL.md`. The only step's file
still pointing to one of these files with no name at that step is `project-level/technology/settle.md:61`,
which is Minor finding 4 of the first review, not in the findings file.

## What the fix itself brought

### Critical

none

### Important

none

No sentence of a step's file moved, so nothing an agent has to do changed; each addition names a file and
gives no order to read it, so WAY-256's "has it read again" is not touched. The skills' descriptions are
unchanged, so no entry point changes. The added condition in `refine-task` is the condition of reading
the rule, as `resolve_gaps.md` has it, and does not restate what a reserved choice is, so it leaves
WAY-268 as it stands.

### Minor

#### 1. The new sentences' "it" can be read as something other than the step's file

- **Place:** `task-cycle/spec/SKILL.md:39-41`, "Where the design needs a language, … do not settle, it
  points to"; less so `project-level/task/skill/SKILL.md:43-45`.
- **What is wrong:** "it" means `design.md`, but the nearest noun that could take the verb is "the design".
  In `refine-task` it means `resolve_gaps.md`, across a sentence whose subject is "the task's outcome".
- **Why Minor:** the file and its condition are visible, which is what WAY-265 asks, and the order to read
  stands in the step's file, so an agent's work does not change. Naming the file instead of "it" would
  settle it.

### Not new

`task-cycle/spec/SKILL.md:42` adds a `dead-path` warning from `instruction-files/check_instructions.py`,
taking that file from 1 warn to 2. It is not a finding: `.the-way/...` exists only in a product, finding 2
asked for that form, the same warning stands at `task-cycle/plan/SKILL.md:66`,
`task-cycle/review/SKILL.md:69` and `task-cycle/change/SKILL.md:102`, and no test in `gate`, `installation`
or `agent-instructions/test_instruction_files.py` names `dead-path`.

## Findings of the first review that stand

These are not in the findings file, so they were rightly not fixed, and they go to the request's lists
from `reports/merge-review.md`:

- Minor 4, `project-level/technology/settle.md:61`;
- Minor 5, `task-cycle/skill/planning.md:12` and `task-cycle/skill/SKILL.md:218`, the second now at
  `:218-220`;
- out of scope 6, the request's description and `cycle.md:126,133`, and the three lines of its
  *Declined to judge*.

## Declined to judge

none. This review set nothing aside beyond what the first one did.

## Checks

| Check | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `9ea5fff99e2cd1a530db2eb6689181799ce4624e` |
| `git log c69e355..9ea5fff` | 0 | one commit |
| `git diff c69e355..9ea5fff`, read whole | 0 | 3 files, 14 added, 5 removed |
| `git diff --check c69e355 9ea5fff` | 0 | no whitespace error |
| `python -B <scratchpad>/check_fix.py`, the scratchpad being `C:\Users\Mariusz\AppData\Local\Temp\claude\C--Storage-repos-the-way\3f495b8a-5898-44db-bd97-8c76e67b3513\scratchpad`; line breaks ignored, on the blobs at `9ea5fff` | 0 | for each of the four pairs, the condition once in `SKILL.md` and once in the step's file, and the target file named in both; the product form once in `task-cycle/spec/SKILL.md` |
| `python -B elements/common/foundation_check.py .` | 0 | `0 errors` |
| `python -B agent-instructions/skill_entry_points.py` | 0 | `entry points are current`; run without `--write` |
| `python -B instruction-files/check_instructions.py . --file <f>` for `project-level/task/skill/SKILL.md`, `task-cycle/spec/SKILL.md`, `task-cycle/skill/SKILL.md` | 0 each | 0 errors; 1, 2 and 2 warn; of the lines naming these two files, only the warning at `task-cycle/spec/SKILL.md:42` |
| same, for `task-cycle/plan/SKILL.md`, `task-cycle/review/SKILL.md`, `task-cycle/change/SKILL.md` | 0 each | 0 errors; the same warning on the same path in each |
| `git grep -n -E 'reserved_choices\.md\|task_run\.md' 9ea5fff -- '*.md' ':!foundations'` | 0 | 19 lines, the list the paragraph above rests on |
| `git grep -n -E 'spec/SKILL\.md\|task/skill/SKILL\.md\|task-cycle/skill/SKILL\.md' HEAD -- '*.py'` | 0 | the paths appear in the installer's map, the entry-point generator and a test's control list; none reads the text the fix changed by content, as far as these lines show |
| `git grep -n -E 'dead-path' HEAD -- gate installation agent-instructions/test_instruction_files.py` | 1, no match | no test there names the warning |
| Scan of the added lines for a width over 100 | 0 | none |
| `git status --short`, before and after | 0 | empty; the worktree, index and branch are as they were |

Not run: `python -B gate/run_tests.py`, the orchestrator's run on this head. `gate/run_tests.py task-cycle`
and `gate/run_tests.py project-level` are the fix report's claims, 42 and 268 tests with exit 0, which I
did not repeat, since the gate on this head holds them.

## Reaches beyond the dispatch

- `task-cycle/spec/design.md`, `project-level/task/skill/resolve_gaps.md`, `orchestrated_mode.md` and
  `task-cycle/skill/reserved_return.md`: the step's files whose conditions the fix had to equal.
- `task-cycle/plan/SKILL.md`, `task-cycle/review/SKILL.md`, `task-cycle/change/SKILL.md`, through
  `check_instructions.py` only: to see whether the new warning was new in kind.

## Searches not found or unclear

none

# Planner report — installer root CLAUDE.md import

- Model: GPT-6; the exact deployment identifier was not exposed to this agent.
- Boundary: finished plan. No foundation entry, code, test, review, or commit was written.
- Worktree: `C:/Storage/repos/the-way-wt/installer-claude-md`.
- Base: `b8ff05bf139fc394f3f0df351e5da6c0bc0b0995` (`foundations`), as supplied by the dispatch.
- Plan: `.runs/task-cycles/installer-claude-md/plan.md`.
- Size report: `.runs/task-cycles/installer-claude-md/plan-size.md`.

## Inputs read

- Planner dispatch and the frozen task in full. The task is independent, ready for cycle, has no carried questions, and carries one accepted settlement to record as a decision.
- `agent-instructions/README.md`, the project `the-way-plan-task` entry point, and `task-cycle/plan/SKILL.md`.
- The relevant foundation: `foundations/part_map.md` for the `installation`, `instruction-files`, `agent-instructions`, and `installation-command` surfaces; WAY-34, WAY-107, WAY-132 and cycle/planning decisions in `foundations/decisions.md`; installation-related entries in `foundations/invariants.md`; `foundations/glossary.md`; and Claude Code import/loading facts in `foundations/environment_facts.md`.
- `installation/install.py`, `installation/test_install.py`, `installation/README.md`, `instruction-files/SKILL.md`, the relevant part of `instruction-files/tool_loading.md`, and `instruction-files/check_instructions.py`'s import/layout checks.
- `elements/decisions/skill/SKILL.md`, the decision guard's usage, and `task-cycle/slice_size.py`.
- The dispatch reports an installation-test baseline of 17/17 passing. I did not rerun those tests because I changed no product code or tests.

## Findings and choices

- No genuine open design choice appeared. The frozen settlement specifies the installed file, the warning, the preservation of an existing root `CLAUDE.md`, and removal of the old generated rule. Existing preflight and preview/apply structure accommodates those behaviors without choosing a new product contract. No spec is proposed.
- The foundation step has two edits in the same decision log: write settlement 1 as a new installation decision, and correct the verification examples of WAY-132 without changing its binding sentence. The product installer was deliberately outside WAY-132's binding scope. No new invariant or part-map entry follows from the task's source: the existing `installation-command` promise already allows a new file and forbids replacing an existing one.
- Two slices let separate reviewers judge installer behavior and the explanatory material. Slice 1 owns `installation/install.py` and its integration tests. Slice 2 owns `installation/README.md` and `instruction-files/SKILL.md` after the new behavior exists.
- The warning check should recognize a usable import rather than any occurrence of the text in a code example. Existing `CLAUDE.md` stays product-owned and byte-identical. The implementation agent must settle details of malformed or nonregular files safely at the trust boundary and test adversarial cases.
- The documentation should describe removal of the legacy `.claude/rules/the-way.md` only for a product moving from a pin whose installer wrote it. The current installer must neither write nor delete that file. The task excludes moving `loop2`'s pin and excludes a new `CLAUDE.local.md` warning.
- High criticality and `installation/install.py` as the trust boundary call for integration tests of preview/apply, warning order, existing-file preservation, ignored paths, code-fence decoys, malformed input and refusal/cancellation. The plan names the changed-part tests, the decision guard, and existing critical-flow tests.

## Commands and results

All repository commands below ran with the worktree as the working directory.

| Command or command group | Exit code | Result |
|---|---:|---|
| `git rev-parse --show-toplevel`; `git -C .agents/skills/the-way-plan-task rev-parse --show-superproject-working-tree`; `git ls-files --stage -- ':/.the-way'` | 0 each | Confirmed this is the top-level the-way worktree, not a product submodule. |
| `git status --short` | 0 | No tracked or untracked changes before planning. The `.runs` files are ignored by Git. |
| `rg -n` searches over `foundations/`, `installation/`, `instruction-files/`, and `task-cycle/` for the affected surfaces, decisions and paths | 0 | Located all current mentions and relevant entry ranges. |
| `Get-Content` reads of the input, skills, foundation excerpts, installer, tests, README, and instruction-files sources | 0 each | Inputs listed above were inspected. |
| `python -B task-cycle/slice_size.py .runs/task-cycles/installer-claude-md/plan.md` | 0 | Both slices fit: slice 1 reads about 134,823 estimated tokens and changes 2 files; slice 2 reads about 132,747 and changes 2 files. No unchecked paths. The final output is saved beside the plan. |

## Questions

None for the orchestrator. The migration wording and import recognition are implementation choices recorded in the plan, not open product decisions.

# Planner revision report — installer root CLAUDE.md import

- Model: Codex GPT-6; the exact deployment identifier was not exposed to this agent.
- Worktree: `C:/Storage/repos/the-way-wt/installer-claude-md`.
- Boundary: revised plan only. I changed no foundation file, code, test, or commit.
- Revised plan: `.runs/task-cycles/installer-claude-md/plan.md`.
- Revised size report: `.runs/task-cycles/installer-claude-md/plan-size.md`.

## Inputs

I read the revision dispatch, the full frozen task and current plan, the foundation author's full report, and the complete uncommitted diff of `foundations/decisions.md`, `foundations/invariants.md`, and `foundations/part_map.md`. I used the project `the-way-plan-task` skill and its `task-cycle/plan/SKILL.md`, read in the preceding planning turn. The foundation diff confirms WAY-141/1, the revised WAY-132/1 verification examples, `installation-claude-guidance/1`, and the installation failure mode. The current foundation changes are intentionally uncommitted and were left untouched.

## Revision decisions

- The *Foundation entries* table now names all four entry effects: WAY-141/1, the WAY-132/1 verification edit, `installation-claude-guidance/1`, and the `installation` part-map failure mode. It maps the new invariant and failure mode to Slice 1.
- Before Slice 1, a separate check author must write `installation/test_installed_guidance.py` from the invariant sentence and Method, cite `# invariant: installation-claude-guidance/1`, and run `python -B gate/run_tests.py installation --record .runs/installation-tests.jsonl` against the old installer to observe the expected failure. The check stays read-only for the implementation agent; a needed change returns to the foundation step. Slice 1 explicitly depends on this completed red check.
- Slice 1 still changes only `installation/install.py` and `installation/test_install.py`; additional behavior tests may be written first there. Its final check must cite and pass the new invariant. Slice 2 retains the README and instruction-files skill scope and reruns the installation check.
- The foundation-check note now includes the decisions, invariants, and part-map guards and their part tests. The plan's coverage names the independent check and the part-map edit.
- No new open design choice appeared. The original two-slice structure and the task's excluded `loop2` pin move remain appropriate.

## Commands and exit codes

All commands ran in `C:/Storage/repos/the-way-wt/installer-claude-md`.

| Command | Exit | Result |
|---|---:|---|
| `Get-Content` on the revision dispatch, plan, frozen task, and foundation-author report | 0 each | Read all requested inputs. |
| `git diff -- foundations/decisions.md foundations/invariants.md foundations/part_map.md` | 0 | Confirmed the exact uncommitted foundation edits; the diff is not copied into this report. |
| `rg -n '^## installation\|^### WAY-141\|installation-claude-guidance\|^## instruction-files' foundations/invariants.md foundations/decisions.md foundations/part_map.md` | 0 | Located the new decision at line 4274, the invariant at line 2061, and the failure mode near line 242. |
| `python -B task-cycle/slice_size.py .runs/task-cycles/installer-claude-md/plan.md` | 0 | Both slices fit; Slice 1 changes 2 files and reads about 135,928 estimated tokens, Slice 2 changes 2 files and reads about 133,655. No unchecked paths. The full output is in `plan-size.md`. |
| `git status --short` | 0 | Only the three foundation files are modified in Git; I left them untouched. Planning files are ignored under `.runs/`. |
| `git diff --stat -- foundations/decisions.md foundations/invariants.md foundations/part_map.md` | 0 | Confirmed the same three modified foundation files after planning. |
| `Get-Item` on the revised plan and size report | 0 | Both artifacts exist. |

I did not run foundation guards or installation tests in this revision. The foundation author's report records their existing results. The independent invariant check and its expected failing run remain the next step for the orchestrator.

## Questions

None.

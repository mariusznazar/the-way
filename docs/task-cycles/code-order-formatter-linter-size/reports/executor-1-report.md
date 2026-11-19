# Executor-1 report — Slice 1: formatter configuration

**Status:** done

**Commits:** `6c13454c` — Configure the Ruff formatter in ruff.toml at line width 100 and keep it off Markdown (on `task/code-order-formatter-linter-size`, after the slice base `00945f93`).

**Check result:** all focused checks pass; the one reported difference is that `ruff format` given a Markdown file by name still formats it (see weakest point). Nothing failed or was skipped.

## Files changed

- `ruff.toml`: 8 added lines, 1 removed (header comment reworded to name the formatter and WAY-382; new top-level `line-length = 100`; new `[format]` table with `exclude = ["*.md"]`, placed after `extend-exclude` because TOML top-level keys must precede tables).

No Python file was changed. No trust-boundary file was touched.

## Checks (commands run from the worktree root, exit codes)

Ruff is `the Ruff of the quality environment of the main checkout` (0.17.1).

1. Base, before the change: `ruff format --check --config ruff.toml --no-cache .` — exit 1, 79 files listed: 78 `.py` files and `installation/README.md`. The Markdown file was listed because Ruff 0.17.1 lays out the Python example in it, which is the defect this slice fixes.
2. Base lint: `ruff check --config ruff.toml --no-cache --ignore-noqa --output-format concise agent-instructions elements gate installation instruction-files process-audit product-guidelines project-level relation-model task-cycle` — exit 1, "Found 24 errors."
3. After the change: `ruff format --check --config ruff.toml --no-cache .` — exit 1, 78 files listed, all `.py`; the set equals the base's 78 `.py` files; `README.md` no longer listed. Summary: "78 files would be reformatted, 1 file already formatted" (79 tracked `.py` files, matching `git ls-files`).
4. After the change: the same lint command — exit 1, "Found 24 errors."; the sorted report lines are identical to the base's (diff empty).
5. `python -B gate/run_tests.py agent-instructions` — exit 0, "Ran 50 tests … OK (expected failures=2)". The two expected failures are the existing ones in `test_linter_invariant.py` and `test_size_invariant.py`, which slice 5 removes.

Not run, as the handoff requires: the full gate, and any test of `elements/common` (WAY-321).

No test was written first: the slice is configuration, which the cycle's test rule (`task-cycle/change/SKILL.md` section 2) gives as "write the code and the tests the behaviour needs" — the behaviour here is checked by checks 1–4.

## Own-work check (WAY-164)

- **Requirement:** the formatter is kept off `.md` files so that a run from the root reformats no Markdown file; the linter's reports stay the 24 of the base; the comment at the top names the formatter and WAY-382.
- **Check:** checks 1, 3 and 4 above, and a diff of the two format reports' file lists.
- **Result:** met for a run from the root (`.`). The `.md` file is no longer listed; the 24 lint reports are identical line for line.

## Weakest point

`[format] exclude` does not stop Ruff from formatting a Markdown file that is named explicitly on the command line: `ruff format --check --config ruff.toml installation/README.md` still reports it (exit 1). The slice's requirement is a run from the root, which is met. If the orchestrator wants the exclusion to hold for named files too, the option is top-level `force-exclude = true`. Cost: one more setting away from Ruff's default, which the decision WAY-382 text ("every other setting of the formatter at its default") does not list; I did not add it without the orchestrator's choice.

## Choices made

- The `.md` exclusion is in `[format]`, not in the top-level `extend-exclude`, so it names the formatter's own setting. Rejected: adding `*.md` to top-level `extend-exclude` — it would also hide Markdown from the linter, which checks no Markdown file now, and so changes the linter's scope without a need.
- `line-length` is top-level, because Ruff 0.17.1 accepts it only there (not under `[format]`).

## Reaches beyond the handoff

None. The handoff's own Read passages were read: `task.md` lines 29–30, 56–61, 79–83 (through the file's To do and Questions to settle sections); `foundations/decisions.md` WAY-380 and WAY-381 ranges and WAY-382; `foundations/invariants.md` `formatter-layout`; `foundations/part_map.md` `repository` part; `guidelines/coding.md` in full. `task-cycle/change/SKILL.md` and `slice.md` read whole.

## Unread material

- `task.md` — read by line ranges as the handoff gives, not whole (the handoff directs range reading).
- `foundations/decisions.md` WAY-380 and WAY-381 — read in their current ranges, 10611–10684 region, whole entries.
- No other file or entry named by the handoff was left unread.

## Searches not found or unclear

- The handoff gives the base file count as 78 `.py` files. Verified: 78 `.py` files at base, plus `installation/README.md` listed by Ruff, which the handoff's wording ("naming only `.py` files") did not anticipate — at the base the Markdown file was listed too, so the base output alone is 79 entries. Not a blocker; the slice's post-condition (no `.md` listed) holds.

## Working copies

I made no separate working copy (no worktree, clone or copy of a file). My check outputs were written to `.runs/executor-1/`; their content is summarized above, and the directory was removed after the checks. Nothing remains.

## Questions for the orchestrator

None.

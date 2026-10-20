# Final independent assessment R1 — author settlement

Status: DONE; return before affected independent code review. R1 is addressed. No further assessment, agent dispatch or human question was requested.

Worktree: `C:/Storage/repos/the-way/.runs/worktrees/s7-cycle-remarks`; branch `s7-cycle-remarks`.

Exact settlement range: `9a8bc5e7ae467a1dce81b4be830130c64337db0d..9c2a87c28ff0359bb0a48425fa23c5d8119a63a0`.

Commit: `9c2a87c28ff0359bb0a48425fa23c5d8119a63a0` — `fix: require recovery when fingerprint checks cannot run`.

Product numstat: `agent-instructions/README.md`, +3/-3. Only that explicit path was staged and committed. Tracked working tree is clean. Evidence paths named below are beside this report under `.runs/task-cycles/s7-cycle-remarks/reports/`.

## Disposition and authority

Applied the exact full replacement requested in R1 of `final-independent-assessment.md`, as accepted by `author-final-assessment-handoff.md`. The changed passage at `agent-instructions/README.md:32` now reads:

> Before the request, also run the decisions and invariants guards with
> `--merge-onto <the current foundations tip>`. Act on their relation-fingerprint findings and
> resolve any operational error that prevents those checks from running; their findings about
> copies of a version and about a placeholder request link are expected before `main`.

The frozen task's To do 5 requires that target-aware comparison. Repairing a failure that prevents it from running is a prerequisite of that authorized behavior. Complete WAY-63 and WAY-160 were reread: a Git execution error is not a valid unchecked result, and the orchestrator must receive errors as well as summaries and retain full evidence. The task-cycle verification instruction at `task-cycle/skill/SKILL.md:398` also forbids calling an unrun check passed. No new foundation meaning was introduced.

The prior blanket “act only” could suppress recovery when a target snapshot cannot be read. The correction requires recovery only when an operational error prevents the comparison. The successful path and the expected pre-main version-copy/request-link exceptions remain unchanged. Leaving the phrase would cost no edit but could leave the requested comparison unperformed; fixing it adds nine words and no normal-path command or new artifact requirement.

Used the project `the-way-maintain-instruction-files` skill's Change route, applying the accepted rewording to the existing sentence. Its principles and tool-loading source were already read whole earlier in this author session; the project entry point, complete procedure and all three mechanically reported instruction files were read again for this edit. No global skill was substituted. No production scripts, flags, tests, foundation entries, skill metadata or generated entry points changed.

## Refreshed selection and return conclusion

The actual diff changes only the repository integration instructions, owned by `agent-instructions`; the behavior it names concerns the existing decision/invariant checks and task-cycle verification. The complete part map and foundation reads from the earlier author stages remain applicable: all 210 decisions and 225 invariant sections were read, with the whole task's nine-part selection reconciled in `settlement-selection.json` at the starting HEAD. No foundation content or Scope changed in R1. The complete rereads of WAY-63 and WAY-160 confirm the existing handling of execution errors; no new dependency fingerprint or precedence relation is required.

Guideline selection was checked against `product-guidelines/reading.md` and the actual one-file diff. It remains empty: process prose only, no production code or UI, no `guidelines/` directory, and no new coding/styleguide gap. Criticality remains high because these instructions control verification before integration. The wording edit is reversible; no trust-boundary file or part-map value changes.

Return-step conclusion: a filter for expected pre-main findings cannot exempt failures that prevent the requested check from executing. This is already governed by the verification rules; the guide now expresses it. No new decision, invariant, term, environment fact, part-map change or guideline is needed. The accepted candidate-question and workspace settlements remain unchanged. No new unsettled product meaning remains with the author.

## Manual failure-path check

This is source-derived evidence, not a claim that an operational failure occurred in this cycle. The author inspected both actual failure branches and their callers:

- `elements/decisions/format_guard.py:831`: `file_at` returns a failure; the guard records a general error and returns `None`. At lines 1195–1200, fingerprint checking requires successful target resolution and a non-None merged log. Therefore that failure produces no completed fingerprint comparison.
- `elements/invariants/format_guard.py:1412`: a target decision-log read failure likewise records a general error and returns `None`. At lines 1634–1644, `check_fingerprints` runs only if merged decisions, target invariant entries and merged environment facts are all available. A missing result prevents the comparison.

Manual scenario: Git cannot read the target snapshot, so a general execution error is returned before fingerprint results exist. Under the old “act only” wording a literal reader could disregard it; under the replacement the error prevents the check and must be resolved. If both comparisons run and only the expected version-copy/placeholder findings remain, the pre-main exception still applies. A stale fingerprint remains actionable in either wording. The surrounding requirement to retain warnings and unchecked work is preserved.

No guard was patched, temporarily broken or given fabricated input. No extra failure simulation or prose-mirroring test was added. The code path, the decision rules and the new wording are the evidence for this narrow instruction correction; a live recovery workflow was not exercised.

## Focused checks and evidence

Commands ran from the worktree. Exact argument arrays, actual exits and complete stdout/stderr are recorded in `final-settlement-before.json`, `final-settlement-checks.json` and the listed files.

| Command | Result | Full output |
|---|---|---|
| `python -B instruction-files/check_instructions.py .` before edit | exit 0; 0 errors, 1 warning, 3 info | `final-settlement-instructions-before.txt` |
| Same mechanical command after edit | exit 0; 0 errors, 1 warning, 3 info | `final-settlement-instructions-after.txt` |
| `python -B gate/run_tests.py agent-instructions` | exit 0; 18 tests OK | `final-settlement-agent-instructions.txt` |
| `git diff --check` | exit 0; empty output | `final-settlement-whitespace.txt` |
| `git diff -- agent-instructions/README.md` | exit 0; complete three-line replacement | `final-settlement-diff.txt` |

The mechanical check's warning is unchanged: `AGENTS.md:20`, the relative `_zadania` folder reference does not exist in this checkout; it refers to private task notes. The check reports AGENTS at 21 lines/187 words, CLAUDE at 1 line/1 word, README at 52 lines/515 words after the edit (506 words before). No new mechanical warning or unread-file information appears.

## Retained limitations and boundary

Only affected tests and instruction checks were run here. The orchestrator owns the final required verification after review; this report does not relabel the previous 971 tests as a run on the new HEAD or claim the unavailable full gate passes. Existing foundation approval placeholders, overdue-review warnings and unchecked categories are unaffected. No foundation guard rerun is needed for this README-only settlement. The final assessment's R1 is settled within that assessment, and the author stops before the affected code review.

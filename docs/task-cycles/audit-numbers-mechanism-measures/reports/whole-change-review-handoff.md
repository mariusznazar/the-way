# Handoff — review of the whole change

Delegation: the person who requested this cycle (Mariusz) has delegated intermediate choices to the orchestrator. Your questions go to the orchestrator, never to the human; no answer of the orchestrator is the human's approval.

Worktree `the task's worktree` (read-only for you: change nothing, commit nothing). Branch `task/audit-numbers-mechanism-measures`. The-way is the top-level repository (no product, no `.the-way`).

Method: `review-change`. Read whole `task-cycle/review/SKILL.md`; the variant is the whole change, so read `task-cycle/review/whole_change.md` and follow it. You select your own foundation and guidelines by "Reading the foundation" in `elements/common/way_of_working.md` (WAY-150) and `product-guidelines/reading.md` (by WAY-328 the-way departs from the coding and testing guidelines for its own code and tests, none is missing); count the decisions read whole and read by title for your report.

Range: `2292f334d5499f45b68b00c477cd76a2effd7537..1923ef4` (`git diff` and `git log` of it, computed yourself; confirm `git rev-parse HEAD` is `1923ef4...`). The task moved no pin.

Frozen task (read whole): `.runs/task-cycles/audit-numbers-mechanism-measures/task.md`. Plan (read whole): `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md` — 8 slices, a foundation-entries agent. Spec: none.

Answers of the start of the cycle: trust boundary YES — a new script reads session records (untrusted per the part map's External context), the audit reads cycles' copies from git history, and the gate script reads the output of a gate: check crafted input at every one of these readings; irreversible operation: no. Open design choice: none. Planned route.

Slices, their ranges and whether each had a review of its own:
| Slice | Range | Review of its own |
|---|---|---|
| Foundation entries (WAY-347 to WAY-352, WAY-339 and WAY-344 changed in place, part map) | `2292f33..a030dbf` | covered by slice 1's review (range of slice 1's review started at `2292f33`) |
| 1 measures script, Claude Code | `a030dbf..f0a3829`, fix `..dae0de6` | yes: FAIL then PASS of the fix (`reports/slice-1-review-report.md`, `reports/slice-1-fix-review-report.md`) |
| 2 measures script, Codex | `dae0de6..036d24a` | yes: PASS (`reports/slice-2-review-report.md`) |
| 3 gate script | `036d24a..7916a21` | no — judged by you |
| 4 instruction and record template | `7916a21..8a8f636` | no — judged by you |
| 5 cost from either form of `stages.md` | `8a8f636..0e75a4b` | yes: PASS (`reports/slice-5-review-report.md`) |
| 6 audit reads the two files | `0e75a4b..0964b52`, fix `..9209ecb` | yes: FAIL then PASS of the fix (`reports/slice-6-review-report.md`, `reports/slice-6-fix-review-report.md`) |
| 7 series, medians, comparison | `9209ecb..49ab2fa` | yes: PASS (`reports/slice-7-review-report.md`) |
| 8 audit session instruction | `49ab2fa..1923ef4` | no — judged by you |

Reports of the executors whose slices had no review of their own (claims to verify, not evidence): `reports/slice-3-report.md`, `reports/slice-4-report.md` (the executor returned it as text; the orchestrator saved it word for word), `reports/slice-8-report.md`; the foundation-entries agent's report `reports/foundation-entries-report.md`. Mismatches the mechanical check passed on: none besides these — slice 3's report named the repository root instead of the worktree for its own path (corrected); slice 4's executor read `task-cycle/change/fix.md`-style files as the method names and wrote no report file.

The Minor and out-of-scope findings of the slice reviews are in the "Minor" and "out of scope" sections of each review report named above (slice 1: M1–M3, and the fix review's two; slice 2: three; slice 5: three and one outside the scope — `process-audit/SKILL.md:143-145` stale, which slice 8 fixed; slice 6: M1–M4; slice 7: three). They are yours to take into your own grading: list each that still holds in the final tree; those you mark within the task are fixed by the cycle after your review.

Orchestrator's choices you should judge against the task and the foundation, each in `.runs/task-cycles/audit-numbers-mechanism-measures/cycle.md` *Questions and autonomous choices* (Q3–Q24) — the file is the orchestrator's alone: do not read it, the points are here: (a) the count of other gate runs rests on empty files under `~/.the-way/gate_runs/`, a write outside the repository that WAY-140 (server, DNS, keys, external account) does not name; (b) an absent time line in `stages.md` is an earlier form, exactly one of the two is a missing field; (c) `task-cycle/gate_times.py` is not marked a trust boundary in the part map; (d) the audit shows cycle-level values only (per-agent rows stay in the file); (e) in step 2 of `task-cycle/skill/SKILL.md` the task's name is now fixed before the first gate run, step 5 keeps it; (f) the strict form on a broken first line of an unrelated Codex rollout.
The foundation check `python -B elements/common/foundation_check.py --skip-test-citations` may be run by you (read-only). The orchestrator runs the product's gate itself later: do not run it.

Return: first line `PASS <sha>` or `FAIL <sha>`, graded findings with `file:line` anchors and the slice each blocking finding comes from (or that it comes from none), the changed files with line counts, the counts of decisions read whole and by title, the checks you ran with command and exit code, **Unread material** and **Searches not found or unclear** (each `none` where none) and every reach beyond this handoff. Your report: `.runs/task-cycles/audit-numbers-mechanism-measures/reports/whole-change-review-report.md`.

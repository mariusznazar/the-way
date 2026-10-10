# Cycle record: Install the root Claude import

- Task source: `C:\Storage\The Brain\The Brain\Notes\Projects\(P) Proces pracy nad produktem\_zadania\instalator_claude_md_z_importem_agents_md.md`; ready for cycle on 2026-10-10; frozen copy: [task-frozen.md](task-frozen.md).
- Relation: independent. Product repository: `C:/Storage/repos/the-way` (isolated worktree `C:/Storage/repos/the-way-wt/installer-claude-md`).
- Process pin and target base: `foundations` at `b8ff05bf139fc394f3f0df351e5da6c0bc0b0995`. Task branch: `task/installer-claude-md`.
- Status: ready for review at [pull request 15](https://github.com/mariusznazar/the-way/pull/15). No merge was performed.
- Stage durations, models and tokens: [stages.md](stages.md). The event order below is chronological; exact individual dispatch times were not retained.

## Sharpness

| When | Criticality and touched parts | Trust boundary | Reversibility | Resulting checks |
|---|---|---|---|---|
| Start | High: installation and instruction-files each have high failure modes | `installation/install.py` | Reversible code and documentation | Real CLI integration tests, adversarial product input, changed-part gates, foundation guards and independent assessment |
| Final diff | High: the same parts and foundation entries; no new trust boundary | `installation/install.py` | Reversible; no product migration in this branch | Same checks retained; independent invariant break in a disposable copy |

## Spec and plan

The settlement in the frozen task fixed the behavior; WAY-132 leaves installer-owned files outside its binding rule. No open design choice required a spec. A fresh planner produced the two-slice [plan](plan.md); both slices fit the [size check](plan-size.md) with exit 0. There was no discarded design attempt and no slice returned too large. The planner revised the plan after the foundation author derived an invariant that needed an independent check before code.

## Events

| # | Stage | Actor and model | Input and output | Result |
|---:|---|---|---|---|
| 1 | Start and baseline | Orchestrator, gpt-6-sol | Frozen task, foundation, `agent-instructions/README.md` | Isolated worktree from `b8ff05b`; installation 17/17 and gate 98/98 passed. |
| 2 | Initial plan dispatch and handoff | `/root/planner`, gpt-6-sol | [prompt](reports/planner-prompt.md), [report](reports/planner-report.md), `plan.md`, `plan-size.md` | Two slices fit; no spec. |
| 3 | Foundation dispatch and handoff | `/root/foundation_author`, gpt-6-sol | [prompt](reports/foundation-author-prompt.md), [report](reports/foundation-author-report.md) | WAY-141, new invariant, installation failure mode and WAY-132 examples written. Whole-foundation searches and guards recorded. |
| 4 | Foundation guard rerun | Foundation author, gpt-6-sol | [report](reports/foundation-author-report.md) | Part-map guard first rejected unsupported `--merge-onto none` (exit 1); supported `--base none` run passed with 0 errors. Interrupted initial test captures were rerun to verified completion. |
| 5 | Plan revision dispatch and handoff | `/root/planner`, gpt-6-sol | [prompt](reports/planner-revision-prompt.md), [report](reports/planner-revision-report.md) | Independent invariant check and part-map dependency added; both slices still fit. |
| 6 | Independent invariant check | `/root/invariant_check`, gpt-6-sol | [prompt](reports/invariant-check-prompt.md), [report](reports/invariant-check-report.md) | Wrote `installation/test_installed_guidance.py` from the sentence and method. RED: 4 expected new failures; 17 existing tests passed. The check remained read-only during implementation. |
| 7 | Slice 1 implementation | `/root/slice1_implementer`, gpt-6.1-sol | [dispatch](reports/task-1-dispatch.md), [report](reports/task-1-report.md), commits `6ffb992`, `426d284` | TDD on CLI cases; installation 26/26 and gate 98/98 passed. The initial red test fixture cascaded once, was split, and failed cleanly before code changed. |
| 8 | Slice 1 task review | `/root/slice1_reviewer`, gpt-6.1-sol | [dispatch](reports/task-1-review-dispatch.md), [review](reports/task-1-review.md) | One Important defect: inline-code delimiter could suppress the warning. |
| 9 | Slice 1 fix and scoped re-review | Original implementer and reviewer, gpt-6.1-sol | [fix report](reports/task-1-report.md), [re-review dispatch](reports/task-1-rereview-dispatch.md), [re-review](reports/task-1-rereview.md) | Regression RED then GREEN; finding addressed, no new breakage; slice approved. |
| 10 | Slice 2 implementation | `/root/slice2_implementer`, gpt-6.1-sol | [dispatch](reports/task-2-dispatch.md), [report](reports/task-2-report.md), commit `d40e8cc` | README and instruction-files skill updated; installation 26/26, instruction-files 104 pass/5 skip, gate 98/98. |
| 11 | Slice 2 task review | `/root/slice2_reviewer`, gpt-6.1-sol | [dispatch](reports/task-2-review-dispatch.md), [review](reports/task-2-review.md) | Spec compliant, quality approved, no finding. |
| 12 | Foundation recheck and commit | Orchestrator, gpt-6-sol | [target-tip search](reports/foundation-recheck.md), original commit `c9d015f` | Target still `b8ff05b`; four explicit foundation/check paths committed. |
| 13 | Independent foundation assessment | `/root/foundation_assessor`, gpt-6-astra | [dispatch](reports/foundation-assessment-dispatch.md), [assessment](reports/foundation-assessment.md), [settlement](reports/foundation-assessment-settlement.md) | Apply, 8 observations; accepted one warning-wording correction; retained one independently authored test. Assessment and both search records entered in amended foundation commit `865cf7d`. |
| 14 | Assessment code correction | Original slice 1 implementer, gpt-6.1-sol | [dispatch](reports/assessment-code-fix-dispatch.md), [fix report](reports/task-1-report.md), commit `f3d4921` | Warning says `may miss`; focused 1/1, installation 26/26, gate 98/98 and ten cited invariant records pass. |
| 15 | Final whole-branch review | `/root/final_reviewer`, gpt-6-astra | [dispatch](reports/final-review-dispatch.md), [review](reports/final-review.md) | 0 Critical, 0 Important, 0 Minor; deliberate import break produced 3 expected failures including the independent cited test. Temporary-clone cleanup was rejected by automatic approval review as `blocked by policy`; the clone remains under ignored `.runs/`. |
| 16 | Draft request and approval-link swap | Orchestrator, gpt-6-sol | [pull request 15](https://github.com/mariusznazar/the-way/pull/15), commit `7205a82` | Draft opened against `foundations`; WAY-141 approval placeholder replaced with the request URL and pushed. Decisions guard then had 5 warnings and 5 unchecked. |

The full Superpowers task briefs and [ledger](reports/sdd-ledger.md) are retained with these reports. No Critical or Important review finding remains. No deferred minor or parked finding exists. The final target fetch still resolved to `b8ff05b`, and the branch was clean after the URL swap.

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| C1 | Existing root CLAUDE.md ownership | Inspect for import and preserve bytes | Frozen task To do 2, WAY-141 | Append import | Product guidance could be changed without its owner's choice | Slice 1 |
| C2 | Old rule in a pin move | Remove only for a product migrating from a pin that installed it | WAY-34, plan | Universal deletion | A product-owned rule could be removed, or duplicate guidance retained in an old product | Slice 2 |
| C3 | WAY-132 scope | Change its verification examples; add a separate installer decision | WAY-132 binding text | Expand its binding sentence | Unrelated instruction-file work would inherit an installer rule | Foundation step |
| C4 | Invariant verification | Write a separate level-1 invariant check before implementation | WAY-141, installation failure mode, WAY-69 | Rely only on implementation-author tests | The check could repeat the same mistaken assumption as the code | Foundation step |
| C5 | Import mentioned in code spans or fences | Treat it as ineffective; use the recorded syntax boundary | `claude-code-imports/1`, tool-loading notes and reviewed regression | Search for any substring | Silent missing guidance in an existing product file | Slice 1 |
| C6 | Nonregular or invalid UTF-8 CLAUDE.md | Refuse before writes, consistent with shared-file input checks | Existing installer behavior and CLI tests | Follow or rewrite the path | Unsafe external write or unpreserved content | Slice 1 |
| C7 | Superpowers TDD path asked by implementer | Point to installed v6.4.1 skill | Local installed plugin | Guess a version | Wrong test workflow | Slice 1 |
| C8 | Consequence wording in warning | Say Claude Code `may miss` shared guidance | [assessment](reports/foundation-assessment.md), tool-loading settings | Keep unconditional `will miss` | Warning overstates evidence in nondefault settings | `f3d4921` |
| C9 | Cut the standalone creation invariant test | Retain the separately authored direct check | WAY-69, [settlement](reports/foundation-assessment-settlement.md) | Remove duplicate run | One extra install run versus weaker independent failure signal | Foundation assessment |
| C10 | Wrapper count in README | State the actual 12 per tool, 24 total | `installation/install.py` skill map and directories | Retain old 22 count | Migration instructions misstate installed files | Slice 2 |

No provisional choice binds work after merge beyond the entries written in the foundation. There is no unresolved question for the human at this cycle boundary.

## Artifacts

| Kind | Path or commit | Author and review |
|---|---|---|
| Frozen task | [task-frozen.md](task-frozen.md) | User-approved source; no spec |
| Plan and size | [plan.md](plan.md), [plan-size.md](plan-size.md) | Planner; two slices fit |
| Foundation and independent check | `865cf7d` (content assessed at `c9d015f`) | Foundation author plus independent check author; [assessment](reports/foundation-assessment.md) and [settlement](reports/foundation-assessment-settlement.md) |
| Installer and fix | `6ffb992`, `426d284`, `f3d4921` | Slice 1 implementer; task review and final review passed |
| Documentation | `d40e8cc` | Slice 2 implementer; task review and final review passed |
| Approval URL | `7205a82` | Orchestrator; placeholder-only swap |
| Full reports, prompts and ledger | [reports/](reports/) | Review outcomes and failed attempts are linked in Events |
| Stage measurements | [stages.md](stages.md) | `task-cycle/cycle_stages.py`, session `01a12711-8f58-7e03-a25d-0c4e94684e6c`; no parser warning |

## Verification

| Check | Environment and result | Limits, warnings or unchecked |
|---|---|---|
| Baseline installation / gate | Windows worktree at `b8ff05b`: 17/17 and 98/98 pass | Before code change |
| Independent check RED | Old installer: 21 tests, 4 expected new failures and 17 existing passes; exit 1 | Cited `installation-claude-guidance/1`, no null citation |
| Slice 1 TDD RED | 24 tests: 19 failures and 1 fixture-cascade error; corrected focused RED 2 failures | Before production edit; report names cause and correction |
| Slice 1 fix RED and GREEN | One CLI regression failed before delimiter fix, then passed | Reviewed in `426d284` and scoped re-review |
| Final installation | Windows: `python -B gate/run_tests.py installation --record .runs/installation-tests.jsonl`; 26 pass, exit 0 | Ten `installation-claude-guidance/1` records pass, no fail or skip |
| Instruction-files | `python -B gate/run_tests.py instruction-files`; 104 pass, 5 skip, exit 0 | Skips reported, not called passes |
| Critical flow | `python -B gate/run_tests.py gate`; 98 pass, exit 0 | These are the current gate's critical-flow tests, not a full all-parts run |
| Foundation tests | `elements/decisions` 169; `elements/invariants` 233; `elements/part-map` 162; all exit 0 | Changed parts only |
| Foundation guards before request URL | Decisions 0 errors/6 warnings/5 unchecked; invariants 0/0/3; part map 0/0/7 | Five overdue reviews plus placeholder warning; base/merge and coverage/dependency checks unavailable |
| Decisions guard after request URL | 0 errors/5 warnings/5 unchecked, exit 0 | Five overdue reviews remain; placeholder warning cleared |
| Final review break | Disposable copy: installation exit 1, 26 tests, 3 expected failures; independent cited creation check failed on wrong import bytes | Temporary clone cleanup automatically rejected as `blocked by policy`; ignored local clone remains |
| Final diff and target | `git diff --check` exit 0; `origin/foundations=b8ff05b`; branch clean | No live Claude Code parser run; recorded import facts and CLI behavior supply the evidence |

## Return step

- Decisions: WAY-141/1 added from settlement row 1; WAY-132/1 verification examples edited with binding sentence and fingerprint unchanged.
- Invariants: `installation-claude-guidance/1` added. Its independently authored check covers the installed file, warning, preservation and absence of the old rule. No newly learned uncovered behavior requires another invariant.
- Environment facts and glossary: no new entry needed after the whole-foundation searches and final diff. Full parser equivalence remains unverified and is not claimed.
- Part map: installation gained a high failure mode for lost or duplicate Claude guidance, detected by the new invariant. Computed criticality did not fall.
- Foundation compared with touched code: `installation-command` already allows a new root file and protects existing product files; the final installer, README, skill and examples agree with WAY-141 and WAY-132.
- Projected entries: none assigned or made true beyond the task's settlement.
- Settlements to record: row 1 written whole as WAY-141/1.

## Independent assessment

- Assessed range: `b8ff05bf139fc394f3f0df351e5da6c0bc0b0995..c9d015f415fffbc84ef12bf2a9a47ede2043924f` (same foundation/test content in amended commit `865cf7d`). Filtered files: `installation/install.py`, `installation/test_install.py`, `installation/test_installed_guidance.py`, `foundations/decisions.md`, `foundations/invariants.md`, `foundations/part_map.md`.
- Full [assessment](reports/foundation-assessment.md): apply, 8 observations, no blocking issue. Full [settlement](reports/foundation-assessment-settlement.md): observation 7 changed code wording in `f3d4921`; observation 8 retained the independent check; other observations accepted as no concern or explicit evidence limits. The affected tests and final code review were repeated after the code correction. The approval URL swap changes metadata only.
- The two whole-foundation searches and assessment settlement are recorded in the message of `865cf7d`; the target-tip [recheck](reports/foundation-recheck.md) found no collision.

## Request handoff

- Request: [pull request 15](https://github.com/mariusznazar/the-way/pull/15), initially draft; target `foundations`. It will be marked ready after the record pair is pushed. Do not merge in this cycle.
- What this request settles: WAY-141/1 makes the root import the sole generated Claude route; `installation-claude-guidance/1` checks it; the installation part maps its failure; WAY-132 verification examples describe current installer files without changing its binding rule.
- Additional merge-time foundation condition: none beyond human acceptance of these new or changed entries. No invariant correction, lowered part criticality, recovered row, moved definition use or new term needs a separate merge-time decision.
- Human actions and questions: none in the frozen task or found outside the repository. `loop2` pin movement belongs to a separate product task.
- Autonomous choices: 10 rows above.
- Backlog entry: not yet changed; the private task is already in progress.
- Process remarks: none. The cleanup rejection concerns only an ignored disposable review clone and is reported above.

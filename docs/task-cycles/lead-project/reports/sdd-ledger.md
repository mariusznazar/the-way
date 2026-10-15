# SDD ledger ? plan: .runs/task-cycles/lead-project/plan.md

Base: db77ba549cb9ece7d3e62bf29e1256973f62deab. Worktree: C:/Storage/repos/the-way-wt/lead-project. Spec: .runs/task-cycles/lead-project/spec.md, reviewed without findings. Current stage: all seven slices, final review/fix, one assessment and its affected corrections complete. Both new invariant checks accepted; request19 open and archive publication pending. Full subsequent events are in cycle.md and controller-ledger.md.

## Preflight

| Slice or shared pair | Producer / consumer / internal agreement | Result |
|---|---|---|
| 1 | Reader + minimal parser fields / real Git tests and black-box invariant | Matches CLI spec; invariant check authored separately and read-only |
| 2 | Conversation/refiner/answerer / documented semantic scenarios | Same exact phrases, ownership and final acceptance; no source-string pseudo-test |
| 3 | Round orchestration / conversations and CLI; existing plan/definition/cycle skills | Explicit dependencies on 1/2, shared plan writes serialized |
| 4 | Registry and docs / installed wrappers and ordinary tests | Protected existing tests read-only; tests source committed Slice 3 |
| 5 | Ten generated foundation wrappers / produce bytes | Mechanical bounded subset, incomplete other wrappers explicit |
| 6 | Ten generated shared/cycle wrappers / produce bytes | Mechanical bounded subset, incomplete project wrappers explicit |
| 7 | Final ten wrappers / full --write and all suites | Depends on both earlier batches and final frontmatter; no stale generated output allowed |
| 1 / 3 | plan_state CLI output consumed by lead skill | Spec contract shared; no mutable plan edits by reader |
| 2 / 3 | Conversation contract and refine-task consumed by orchestrator | Exact file routing and only Status writes agree |
| 3 / 4 | New skill source consumed by install registry | Source committed before clone-based installation check |
| 3 / 5,6,7 | All stable source names/descriptions consumed by generation | Generated output not manually authored; later frontmatter changes invalidate batches |
| 5 / 6 | Same discovered inventory, disjoint outputs | No shared write, shared source must remain stable |
| 5 / 7 and 6 / 7 | Prior partial generated output consumed by whole --write | Final command only changes last ten; unexpected extra diff is finding |
| 4 / 7 | Installed source inventory / aggregate verification | Final suite requires registry update from 4 |

Ruling: Execute slices sequentially, including mechanically generated batches ? task-cycle requires each slice's fresh author/reviewer and SDD forbids parallel implementers. Independent 1/2 or 4/5/6 opportunities do not authorize shared worktree writes. Cost: more elapsed time, isolated review ranges preserved.

Ruling: task-brief script cannot parse the-way Slice headings (actual invocation failed, no matching Task 1). Preserve canonical plan; create a disposable extraction view with only Slice headings changed to Task, and use task-brief with explicit output path in this workspace. Extracted brief keeps exact slice text and links binding sources. Cost: verify extraction equality to avoid adapter drift; no product/tool changes.

Ruling: Future Read paths are added and size rechecked before their consuming slice, per planner-routing.md. Cost: measured initial report is limited to existing text; no fake files.

## Dispatches and completion

Dispatch history follows; each dependent stage waits for the preceding report and review.

Task 1: dispatch at098d7df8550d04f0fd83343013231f568ea31ba3, brief task-1-brief.md, report task-1-report.md. New source contract clarifications C11/C12 recorded in spec and cycle; no schema or behavior beyond accepted design.

Task1 author complete2233cff, full report read; review dispatch098d7df..2233cff. C13 archive-directory ruling remains independently reviewable. Acceptance0; project-level227/gate98 pass.

Task 1: complete (commits098d7df..2233cff, review clean). Invariant break detected; unbroken check passed and copy restored. Cross-slice workflow verification assigned2/3/final.
Task 2: dispatch at2233cffd031838f9e68272824fb4899c93471cc3; task-2-brief.md; allsizefits.

Task2 author complete6e8efc5; fullreport read, fourpaths checked. Review2233cff..6e8efc5 dispatch; no openauthorquestion.

Task 2: complete (commits2233cff..6e8efc5, review clean). Cross-slice integration assigned3/final; no livebehaviorclaim.
Task3 preflight: finalreader+conversation+answerer Read added/measured, allfits. Dispatch6e8efc5649044f5d79911370107b6f486068e81f, task-3-brief.md.

Final verification command detail: Slice7 project-level run must use the declared Method `python -B gate/run_tests.py project-level --record .runs/project-plan-state-evidence.jsonl`, preserving final per-invariant verdicts and superseding the pre-implementation RED record. This is the one required final suite run, not an additional duplicate. Root must inspect the18 current invariant verdicts.

Task3 authorcomplete74750b3; allfivefilesinspected, project-level227/task-cycle41 pass, gate97/98 (missing/stalewrappers, pending5-7). Review6e8efc5..74750b3 dispatch.

Task 3: complete (commits6e8efc5..74750b3, review clean). Installation/wrappers pending4-7.
OPEN root risk R1 for final review: reader exits2 on nonASCII repository path with PYTHONIOENCODING=cp1252; reproduced existing ordinary path test with only fixture output encoding changed. Evidence .runs/task-cycles/lead-project/reports/final-review-encoding-risk.txt. Not minor or dismissed; fix required before completion if confirmed. No product mutation.
Task4 dispatch74750b340769fe1c397adaff12ece77acc8350e7; futurelead Read measured, allfits; task-4-brief.md.

Task4 authorcomplete9c471a2; installation30pass, gate97/98wrapperpending. Review74750b3..9c471a2 dispatched. Generation5-7 Read now enumeratesall15sourceSKILLfiles; sizeallfits (5:110192,6:109923,7:108042estimatedtokens).

Task 4: complete (commits74750b3..9c471a2, review clean). Repo-wrapper completion required5-7.
Task5 preflight: all15sourceSKILLfiles andfrozen task inRead; allsizefits. Freshhelperbrief verified. Dispatch9c471a2a6dae5f2f53be882dbf888d499826cc28.

Slice 5 committed 6b23e0b; root verified ten generated wrapper changes and full report. Fresh review5 dispatch uses reports/review-slice5-handoff.md with exact base/head/package. Incomplete cross-batch checks remain expected; R1 remains open for final review.

Slice 5 review5 (gpt-6.1-sol): compliant/approved, no findings. Full report task-5-review.md. Root accepts remaining twenty wrappers as explicit slices 6/7 obligations, no full gate claim. Slice 6 fresh executor dispatch at 6b23e0b37a050d5fec45e948b047953d7a50baf8 using task-6-brief.md, output task-6-report.md. Foundation/source inputs unchanged since last seven-fit size result.

Slice 6 complete 0a1846b6d5f6b92806082bc9d22e66ff896a1e31. Root read full report and inspected ten-path diff; only added lead-project sibling. Clean tree. Fresh review6 (gpt-6.1-sol) dispatch reports/review-slice6-handoff.md, range 6b23e0b37a050d5fec45e948b047953d7a50baf8..0a1846b6d5f6b92806082bc9d22e66ff896a1e31, report task-6-review.md. Remaining ten wrappers and incomplete checks assigned Slice 7.

Slice 6 review6 (gpt-6.1-sol): compliant/approved, no findings; report task-6-review.md read. Root retains final ten outputs obligation. Slice 7 fresh executor dispatch at 0a1846b6d5f6b92806082bc9d22e66ff896a1e31 using task-7-brief.md, expected task-7-report.md; required full generation and all five suites, exact invariant Method record. R1 remains open for final review.

Slice 7 complete ea9a23e93958aa3e579d1846177b1d32c1d739e4. Root inspected exact ten-path diff and full report; confirmed 18 current project-plan-state-evidence/1 PASS records. All five suites passed, 414 tests. Full generator current and 15 identical pairs. Fresh review7 (gpt-6.1-sol) dispatch reports/review-slice7-handoff.md; range 0a1846b6d5f6b92806082bc9d22e66ff896a1e31..ea9a23e93958aa3e579d1846177b1d32c1d739e4, report task-7-review.md. R1 still open for final whole-branch review/fix.

Return-step candidate R2: WAY-153 leaves narrower Git-only execution at level 2; existing generic script-subprocesses allows declared non-Git commands. Root read WAY-12/22/153 and asks foundation author for source-grounded completeness ruling via reports/return-git-only-question.md, read-only report return-git-only-answer.md. No correction or additional invariant yet authorized.

Slice 7 review7 (gpt-6.1-sol) complete: compliant/approved, no findings; independent all-output/pair check and five logs/18 invariant rows verified. All seven planned slices complete. Final whole-branch dispatch waits for focused return-step R2 ruling; confirmed R1 remains assigned final fix wave.

R2 confirmed by original foundation author and root source inspection: Git-only is not covered by broad script-subprocesses or evidence sentence. Root approves separate project-plan-state-subprocesses/1 and WAY-153 Verification correction; exact existing shared Method record avoids a duplicate suite invocation. Handoff reports/return-git-only-write.md to foundation author; only two foundation files writable, separate minimal check contract required. Existing policy meaning stays unchanged.

R2 foundation 4d705b597cb4634f1c58a056558635f63f9cd407 inspected: only WAY-153 Verification and new separate sentence/Method. Fingerprint stays 33b10f25; no old check/sentence changed. Author report and isolated contract read. Guards exit 0, gate 98 and project-level 227 pass; absent new verdict explicitly unchecked. Independent check dispatch to invariant_check uses only reports/subprocess-check-handoff.md and subprocess-check-contract.md, not author reasoning.

R2 check complete 2cadf14fd3d21a82f1adee322f1022002b194385 (invariant_check, gpt-6.1-sol). Root read full report and source: project-level 229 and gate 98 PASS; 18 evidence plus 2 subprocess verdicts PASS. Existing check preserved byte-for-byte. Initial observer failures corrected and retained in report; first deliberate break remains pending post-assessment. Final whole reviewer dispatch gpt-6-astra, reports/final-review-handoff.md, BASE db77ba549cb9ece7d3e62bf29e1256973f62deab to HEAD 2cadf14fd3d21a82f1adee322f1022002b194385, transient package .superpowers/sdd/plan/review-db77ba5..2cadf14.diff. R1 OPEN.

Final whole review /root/final_review (gpt-6-astra), db77ba5..2cadf14, WITH FIXES: exactly one Important R1 ANSI output failure, independently reproduced. Root read full report and source anchors; accepts R1, no source/spec expansion. All 19 items and ten settlements covered, no other findings. Dispatch ONE final fix wave /root/final_fix (gpt-6.1-sol), reports/final-fix-handoff.md; only reader and ordinary test writable, both independent checks protected. Five final suites and real acceptance required.

Final fix /root/final_fix gpt-6.1-sol complete 84cdc87cc12ce43526cb24a61640e39cf00e950a; root read full report and exact two-file diff. ANSI regressions RED/GREEN; 231+98+41+18+30=418 PASS. Real original-plan acceptance cp1252 succeeds and source/protected hashes preserved. R1 awaits scoped verdict. Root return-step refresh confirms same target db77ba5, 88 whole Scope entries/142 headings, no new foundation meaning from output codec. Dispatch fresh final_rereview gpt-6.1-sol reports/final-rereview-handoff.md, fix range 2cadf14..84cdc87. Independent foundation assessment can run concurrently read-only on committed 84cdc87; filtered input excludes every operational artifact.

Single final scoped rereview /root/final_rereview gpt-6.1-sol complete: R1 ADDRESSED, no new breakage/out-of-scope findings. Root read full report and protected-hash evidence; accepts fix range 2cadf14..84cdc87. No additional fix wave required. Foundation assessment remains in progress; return-step check break awaits its settlements. Archive preparation detects UTF-16 PowerShell logs and transcodes by BOM; first ANSI RED log is represented by faithful UTF-8 repeated RED plus author report, no result suppressed.

Identity settlement accepted: root read foundation author's full source ruling and frozen task/entries; own synthetic reproduction confirms foreign source gets false done. Minimal existing-provenance correction preserves accepted own-cycle evidence, plan-local names and paths, needs no new human settlement. C13's basename independence retained; its path-alone sufficiency is superseded. Dispatch original foundation author via assessment-identity-foundation-write.md before independent evidence-check and separate code authors. This is explicit step11 assessment settlement with affected review, not a second final-review fix wave. No other assessment raised.

Identity foundation 9ae98fe0b8421c5b486785a462648f51f9c50f08 complete, root full report/contract/diff read: only WAY-153, evidence sentence and both incoming fingerprints; no map change needed. Existing own-task meaning explicit, /1 pre-main and no Correction. Guards0, old warnings/unchecked retained, revised invariant not yet verified. Independent check author resumes via reports/identity-check-handoff.md and isolated contract only; one protected evidence file writable, subprocess check immutable.

Independent evidence check a9e766d99672bf3c7693ebd4a5519e7fb8d30acf inspected whole diff/report by root: all18 prior methods/assertions retained;9 new identity cases,20 observedPASS/7 expectedRED; both plan/definition pairs validated4xexit0; subprocess check and imported constants unchanged. Root accepts fixture contract, not production compliance. Dispatch fresh identity_implementation gpt-6.1-sol via reports/identity-implementation-handoff.md at a9e766d; only reader/ordinary tests writable, protected checks immutable.

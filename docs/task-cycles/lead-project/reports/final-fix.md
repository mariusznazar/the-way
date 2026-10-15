# Final fix report

Status: DONE.

Base: 2cadf14fd3d21a82f1adee322f1022002b194385
Head: 84cdc87cc12ce43526cb24a61640e39cf00e950a
Commit: 84cdc87 fix: preserve Unicode plan-state evidence on ANSI stdout
Authority: final-fix-handoff.md; one R1 repair wave, no child agents, push, outside-repository writes or next-stage dispatch.

## R1 change

Confirmed inherited cp1252 stdout rejected printable Unicode from valid repository paths and diagnostic paths. The public command now configures its text stdout to UTF-8 with strict errors before parsing/reporting, preserving exact evidence in redirected output. In-memory StringIO consumers remain supported. The module docstring names the UTF-8 output convention. Only project-level/plan_state.py and project-level/test_plan_state.py changed.

Two ordinary command regressions explicitly set the child's PYTHONIOENCODING=cp1252. The successful case checks the decoded exact crafted Polish repository path, Polish archive filename, integration commit and both transitions. The diagnostic case checks exit 2, exact missing Polish path, error label, no proposal and empty stderr. Neither regression forces UTF-8 in the child fixture or hides characters. The parent test runner uses UTF-8 only to preserve its own evidence logs.

## TDD

Command (from project-level): python -B -m unittest test_plan_state.Command.test_ansi_stdout_preserves_non_ascii_paths_and_completion_evidence test_plan_state.Command.test_ansi_stdout_preserves_non_ascii_source_diagnostic

RED before implementation: exit 1, two failures. Successful command returned 2 instead of 0, with charmap encoding error for U+017C. Missing-source report substituted its encoding error for the expected exact path. Full original runner log final-fix-red.txt was captured under inherited ANSI and may render its assertion path incorrectly; the repeated RED run uses UTF-8 for the runner log only, leaves child cp1252 and also exits 1. Faithful UTF-8 log: final-fix-red-utf8-log.txt.

GREEN after implementation: exit 0, 2 tests passed; final-fix-green.txt. No code changed afterward.

## Full checks

Commands, all final code bytes (installation after the commit):

- python -B gate/run_tests.py project-level --record .runs/project-plan-state-evidence.jsonl ? exit 0, 231 tests; final-fix-project-level.txt
- python -B gate/run_tests.py gate ? exit 0, 98 tests; final-fix-gate.txt
- python -B gate/run_tests.py task-cycle ? exit 0, 41 tests; final-fix-task-cycle.txt
- python -B gate/run_tests.py agent-instructions ? exit 0, 18 tests; final-fix-agent-instructions.txt
- python -B gate/run_tests.py installation ? exit 0, 30 tests; final-fix-installation.txt

The first four commands run sequentially in one wrapper; final-fix-suite-results.json records their exact executable arguments and exits. No green suite was rerun. The installation suite uses committed HEAD. These are partial checks, never a full process gate. Generator currentness: python -B agent-instructions/skill_entry_points.py exit 0, entry points are current. No skill inventory/description changed, so no generation was needed. git diff --check exit 0. The initial log-read probes ran before suite logs existed and reported missing paths; they were observation timing errors, not test failures. One rg wildcard passed literally on Windows failed with invalid-path syntax; the authoritative acceptance report/baseline were read directly.

## Protected files

SHA-256 before and after, unchanged:

- project-level/test_plan_state_invariant.py: aac2a0e9ff64bff037d1e1f08ba0004ebb3eeb790986be85e38c5c55b2048c3c
- project-level/test_plan_state_subprocesses_invariant.py: 01e7262b943a5055e3711e689fffbb8037c0b3d68077cc9b49cb33debcb285c2

No foundation entry or invariant test changed. No protected contract change needed.

## Actual acceptance

Command: python -B project-level/plan_state.py "C:/Storage/The Brain/The Brain/Notes/Projects/(P) Loop/plan_mvp_loop2.md" .runs/task-cycles/lead-project/acceptance-loop2

Run after reading the vault rulebook, using inherited cp1252 and retaining UTF-8 raw output. Exit 0; final-fix-acceptance-output.txt. Both proposals for task 3 mag-w-lesie appear: ready for cycle -> in cycle, then in cycle -> done. Exact archive paths, commit/ref evidence and honest unchecked observations remain. final-fix-acceptance.json records the exact command, true composed_transitions, true unchanged_this_run and true matches_original_baseline. Original plan/definition hashes, original repository HEAD and empty status match the earlier baseline. Only disposable clone fetched; no original source write/fetch. Prior acceptance-reader.md and PR #12 association evidence preserved and not overwritten. No fresh PR-host claim is made by this wave.

## Choices and cost

Chosen UTF-8 at the output boundary, rather than lossy replacement/ASCII escaping or requiring callers to configure the environment. Leaving inherited ANSI fails valid input; replacement loses usable evidence; escaped path strings change the exact path a user can copy. UTF-8 preserves all required text with a four-line product change. Cost: redirected consumers must decode the explicitly documented UTF-8 stream. Existing command consumers and tests already decode UTF-8. This is an implementation choice for the settled non-ASCII/exact-evidence requirement, not an open foundation design choice. No user approval claimed.

## Self-review and limits

Read the final diff against the base: only stdout boundary/documentation and two ordinary behavioral tests; no cleanup or unrelated changes. Strict encoding avoids silent replacement. The existing control-character display behavior is retained. Public subprocess command tests cover real Git, actual process output, exits and source preservation; no mocked encoder assertions. Removing the boundary fails both regressions. Existing in-process StringIO tests remain green. Source error exit semantics remain 2.

Full process gate, actual human workflow compliance, independent assessment and scoped rereview are not performed by this executor; root owns later steps. Terminal/font rendering and downstream tools deliberately decoding UTF-8 as ANSI are outside this command's byte-preservation guarantee. No unresolved correctness concern found for R1. No upstream is configured for task/lead-project; no push occurred.

## Foundation selection refresh

Revision: base above; touched part project-level, plan_state.py trust boundary (high false-progress failure mode), project-plan-state-command pinned surface. Full part map read. All current wrapped Scope fields inspected, matching set below plus explicitly required WAY-13/48/69/125/135/136/148/149/150/153 read. Applicable invariants selected through complete Part inspection, including every and project-level, both new reader invariants and script import/subprocess restrictions. Glossary read; all-five-foundation search for encoding, Unicode, non-ASCII, stdout, UTF-8, plan state and exact evidence found the existing exact-evidence reader contract and UTF-8 fact, no conflicting output encoding mandate. No foundation change follows. decisions-found-for-change has TODO method; this selection is not a gate pass.

Scope matches: WAY-09/1, WAY-106/1, WAY-107/1, WAY-108/1, WAY-109/1, WAY-110/1, WAY-111/1, WAY-112/1, WAY-113/1, WAY-114/1, WAY-115/1, WAY-116/1, WAY-117/1, WAY-118/1, WAY-119/1, WAY-120/1, WAY-121/1, WAY-122/1, WAY-123/1, WAY-124/1, WAY-126/1, WAY-127/1, WAY-134/1, WAY-137/1, WAY-138/1, WAY-139/1, WAY-140/1, WAY-142/1, WAY-143/1, WAY-144/1, WAY-145/1, WAY-146/1, WAY-147/1, WAY-150/1, WAY-151/1, WAY-152/1, WAY-153/1, WAY-154/1, WAY-155/1, WAY-156/1.

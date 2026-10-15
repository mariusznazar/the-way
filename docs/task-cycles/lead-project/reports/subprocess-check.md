# Independent return-step subprocess check

Source revision: 4d705b597cb4634f1c58a056558635f63f9cd407.
Check author: invariant_check, distinct from foundation (sentence author) and slice1 (reader author).
New tracked file: project-level/test_plan_state_subprocesses_invariant.py.
Commit: 2cadf14fd3d21a82f1adee322f1022002b194385 — test: observe plan-state reader subprocess programs.

## Authority and separation

Read the complete subprocess-check-handoff.md and subprocess-check-contract.md, global and
worktree AGENTS.md, repository integration guide, current project-plan-state-subprocesses/1
entry and WAY-149/1. WAY-69 and TDD/testing references were read in the preceding independent
check stage. The current WAY-153 verification diff was inspected to refresh the existing
project-level foundation selection; its binding sentence and Scope are unchanged. No reader
source, ordinary reader-test oracle, return-git-only-answer.md, specification, implementation
plan or author's report was used to derive this check. No child, product change, foundation
change, old-check edit, deliberate break or independent assessment was performed.

The only property oracle is the sentence: Every subprocess the plan-state reader starts runs
Git. Inputs reuse four literal constants from the protected independent evidence test; no
expected observation or test method is reused. The check does not inspect implementation text.

## Observation and positive controls

Two citing test methods observe the reader in a separate Python interpreter executing its
public script through runpy with the original argv and script-directory import path. A Python
audit hook installed before the reader runs records actual Popen, spawn and exec events,
and records shell, file-association and fork starts as indirect starts that cannot establish
a direct Git program. The hook only records; real subprocesses run normally. It is not installed
in Git, and cannot confuse Git's own children with reader-owned starts. The wrapper's initial
Python invocation and fixture Git calls occur outside the reader interpreter and its hook.

The program is taken from an explicit executable or, when Windows supplies no separate
executable, from argv[0] of the actual command line decoded by CommandLineToArgvW. The command
arguments are recorded without environments. Each observed program must identify git or git.exe;
an indirect program start fails. Both tests require a nonempty observed trace, so no observation
cannot pass the property.

Fixtures create real disposable Git repositories and a bare remote. The successful case starts
with a stale remote-tracking ref and a newly published archive record; exit 0 and the real ref
moving to the independently observed publisher commit prove the observed starts executed. The
failure case uses an absent remote path, requires exit 2 and an unchanged remote-tracking ref,
while still requiring actual process-start observations. It catches a non-Git fallback on that
operational path. Each test names its production break and cites the invariant in its own body.

## Actual commands and outcomes

1. First declared-method execution:

   python -B gate/run_tests.py project-level --record .runs/project-plan-state-evidence.jsonl

   Exit 1: 229 tests in 48.376s, two new-check failures. These were observer errors, not evidence
   of a product violation: Windows Popen provided executable=None and a composed command line,
   while the initial check incorrectly expected a list representation. The failed-remote path
   had real Git starts but stopped on ls-remote before fetch, so a fetch-specific positive
   control was also too strong. The initial complete output is retained at
   reports/subprocess-check-initial-observer-failure.txt. Neither failure is hidden or called a
   product RED. The observer was corrected without looking at reader code or changing the property.

2. Necessary rerun after correcting those two instrument errors, same exact declared command:

   Exit 0: 229 tests in 49.293s, OK. Actual final completion output is retained in
   reports/subprocess-check-final-completion.txt (progress dots omitted). The final JSONL was
   inspected by invariant identifier: project-plan-state-subprocesses/1 has two pass rows;
   project-plan-state-evidence/1 has eighteen pass rows; the whole record has zero fail rows.
   The second execution was necessary because the first run exposed a defective observer; a
   strict one-run limit would have left the requested meaningful check unresolved.

3. python -B gate/run_tests.py gate

   Exit 0: 98 tests in 18.093s, OK. Complete output: reports/subprocess-check-gate.txt.

4. git diff --check: exit 0 before explicit-path commit.

## Protected check preservation

The SHA-256 of project-level/test_plan_state_invariant.py before and after this work is identical:

AAC2A0E9FF64BFF037D1E1F08BA0004EBB3EEB790986BE85E38C5C55B2048C3C

It was read-only. Only the new designated file was staged and committed; no amend or push.

## Coverage limits and remaining acceptance

This is a dynamic observation of successful evidence collection and an unavailable-remote path,
not a proof that every possible input follows those paths. Standard Python process-start APIs
are covered; a deliberately unaudited native process start, audit-hook evasion, or an impostor
executable named git is beyond this instrument's guarantee. The controlled fixtures demonstrate
that the ordinary observed Git calls really operate on Git repositories. Windows command-line
decoding ran here; the POSIX branch is present but not exercised on this host.

The actual current-product result is PASS for both new citing checks, and the existing eighteen
evidence checks remain PASS. This is not acceptance of the invariant, an independent assessment,
or a full gate pass. Root must obtain the one foundation/test assessment, settle remarks, and
have the separate final code reviewer derive and run the deliberate break from the sentence
under WAY-149 before acceptance. No such break was supplied or written by this author.

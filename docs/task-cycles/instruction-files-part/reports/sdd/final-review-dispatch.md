# Final whole-branch review — task `instruction-files` (cycle step 10)

You are a Senior Code Reviewer reviewing the completed work of one the-way task cycle against its
spec and plan, before the request. The orchestrator runs the cycle under the owner's delegation; you
return findings to it; nothing you approve is the owner's approval.

## What was implemented

A new part `instruction-files` of the-way (the process repository): `principles.md` (principles of
instruction files for coding agents), `tool_loading.md` (how Claude Code, Codex and Cursor load them,
with a Cursor measurement), `SKILL.md` (the skill `maintain-instruction-files`), `check_instructions.py`
(a check script that is a trust boundary — it reads files the-way does not control) and its tests; the
foundation entries that settle it (glossary term "repository instruction file", six environment facts
with watches under `probes/`, WAY-09 edited in place, WAY-127 narrowed in place, WAY-128–WAY-133 new,
*Scope* edits of WAY-27, 34, 38, 89, 120, invariants `instruction-file-imports` and
`root-claude-md-import` with seven fingerprint renewals, part map changes); two invariant checks in
`agent-instructions/test_instruction_files.py` (written by an agent that wrote neither sentences nor
code); generated entry points `the-way-maintain-instruction-files`; README lines.

## Requirements / plan

- Frozen task (Polish, binding): `C:\Storage\repos\the-way-instruction-files-part\.runs\task-cycles\instruction-files-part\frozen_task.md`
- Spec (binding, revision 3): `…\instruction-files-part\spec.md`
- Plan: `…\instruction-files-part\plan.md` (deviations P1–P10 accepted; see its end)
- Global constraints: `C:\Storage\repos\the-way-instruction-files-part\reports\sdd\global-constraints.md`
- The foundation as written on the branch (`foundations/`) is binding for the code: the code and texts
  must do what WAY-128–WAY-133 and the narrowed WAY-127 say.
- Controller rulings made during execution that changed what the plan's code did (trust boundary):
  the check script walks with its own explicit-stack `os.scandir` loop and never follows a link while
  walking; on Windows a link chain is judged with `os.readlink` only and a network-shaped path
  (`\\…`, `\??\…` after `/`→`\`) never reaches the file system; on POSIX `realpath` + `inside`; dead
  paths are judged without following links (`names_something`); tests are offline. Details: the
  ledger `C:\Storage\repos\the-way-instruction-files-part\reports\sdd\progress.md`.

## Range and package

Base 252152a (the branch's start), head c60f3ea, 21 commits. Package (commit list, stat, full diff):
`C:\Storage\repos\the-way-instruction-files-part\reports\sdd\review-252152a..c60f3ea.diff`.
Read it once; inspect files in the worktree `C:\Storage\repos\the-way-instruction-files-part` read-only.

## Deferred minors to triage

The ledger (`progress.md`) holds `minor (deferred)` and `Ruling:` lines from every task. Triage each:
which must be fixed before the request, which may stay. The orchestrator flagged three as recommended
for fixing: (1) Task 4 — `NOT_LOADED` phrases lack a closing word boundary ("is not ready" lowers a
really dead path to INFO, against task point 4); (2) Task 6 — the skill reads `.the-way/instruction-files/SKILL.md`
as checked out, not at the pinned hash, so a submodule whose HEAD differs from the pin makes the skill
follow a copy other than the pinned one (WAY-127, WAY-34); (3) Task 8 — the "Not read: … `.agents/`"
bullet beside "`.agents/skills/`: not established".

## The deliberate breaks (WAY-69, WAY-08) — you write and run them

The two invariant checks are read-only. From the two sentences in `foundations/invariants.md` only
(`instruction-file-imports/1`, `root-claude-md-import/1`), write breaks and run them in a scratch clone
so the worktree is never touched. Confirm first that `git log --oneline -- agent-instructions/test_instruction_files.py`
shows one commit (d87d74f). Run, in Git Bash:

```bash
B=/c/Users/Mariusz/AppData/Local/Temp/claude/C--Storage-repos-the-way/821bfb3e-7677-4acf-bd0e-ab8a94541c58/scratchpad/breaks
git clone -q --branch task/instruction-files-part /c/Storage/repos/the-way-instruction-files-part "$B" && cd "$B" && mkdir -p .runs
brk() { python -B gate/run_tests.py agent-instructions --record .runs/break.jsonl > /dev/null 2>&1; echo "$1 exit $?"; grep -E '"invariant": "(instruction-file-imports|root-claude-md-import)/1"' .runs/break.jsonl | grep -o '"verdict": "[a-z]*", "invariant": "[^"]*"' | sort | uniq -c; git checkout -q -- .; }
brk control
printf '\nSee @docs/x.md for the style.\n' >> AGENTS.md && brk agents
printf '\nSee @docs/x.md for the style.\n' >> agent-instructions/README.md && brk readme
{ printf '# Claude\n'; cat CLAUDE.md; } > c.tmp && mv c.tmp CLAUDE.md && brk heading
```

(If the clone directory exists, remove it first by its literal path — a hook blocks `rm -rf` on a
variable.) Expected: `control exit 0` with `pass` for both; `agents`, `readme`: exit 1 and `fail` for
`instruction-file-imports/1`; `heading`: exit 1, `fail` for `root-claude-md-import/1` (and for
`instruction-file-imports/1`, `@AGENTS.md` then standing on line 2). Add further breaks from the
sentences (a nested tracked `AGENTS.md` holding `(@./x.md)`; a tracked Markdown file the root
`CLAUDE.md` names holding `"@docs/x.md`), committed in the clone where the check needs git to track
them, each reported the same way. A break that does not fail its check is a finding against the check.

## Also check

- The foundation describes the code (WAY-01): every entry the branch writes or changes against the
  code and texts it governs (the part entry's files and failure modes; WAY-09's contents; WAY-127's
  product check and the skill; WAY-128–133 against `SKILL.md` and `principles.md`; the facts against
  what `tool_loading.md` and the decisions cite).
- The acceptance criterion: nothing in `instruction-files/` points to `.runs/` or private notes; no
  path of this machine in tracked text.
- The trust-boundary rows of spec §4.6 are each pinned by a test.

## Rules

Read-only on the worktree; scratch only under
`C:\Users\Mariusz\AppData\Local\Temp\claude\C--Storage-repos-the-way\821bfb3e-7677-4acf-bd0e-ab8a94541c58\scratchpad\final\`
(and the `breaks` clone). Do not dispatch subagents. Return the full review as the text of your final
message in this format: Strengths; Issues (Critical / Important / Minor, each with file:line, why it
matters, the fix); Deliberate breaks (each break, exit code, verdicts); Deferred minors triage (each:
fix before the request / may stay, with the reason); Declined to judge (each behaviour you set aside,
one line, with the reason); Assessment (Ready / With fixes / Not ready, with reasoning).

# Whole-change review handoff — reviewer

Worktree (read-only for you): `C:/Storage/repos/the-way-wt/agent-path-to-running-product`, branch `task/agent-path-to-running-product`.
Method: Superpowers 6.4.1 `requesting-code-review` — this is its reviewer prompt, filled; the-way's additions follow it.
Report: write your full report to `.runs/task-cycles/agent-path-to-running-product/reports/review.md`; save complete stdout+stderr of every command you run under the same `reports/` directory with prefix `review-`, and record each command and exit code.

---

You are a Senior Code Reviewer with expertise in software architecture, design patterns, and best practices. Your job is to review completed work against its plan or requirements and identify issues before they cascade.

## What Was Implemented

The-way (a process for agent-driven product work) now requires every project definition's Technology list to hold three choices of how an agent reaches the running product — its logs, its interface, its development data — each an item marked at its start by `logs:`, `interface:` or `development data:`, settled by the technology step like any other choice. The readiness check rejects a definition lacking one, before approval and on an approved definition alike, so a definition approved earlier goes back to the technology step and through the gate once its product moves its pin. New decision WAY-165 says what each choice asks and that an agent's ability to use an option is a consequence there. Commits: `596a660` decisions (author), `4c251dc` invariant sentence (sentence agent), `8720107` invariant checks and fixtures (check agent), `c657b2b` code, template and skills (author).

## Requirements / Plan

The frozen task document `.runs/task-cycles/agent-path-to-running-product/task.md` (Polish) — read it whole: To do 1–3, the answers to questions 1–6, *Settlements to record* rows 1–6, *Questions carried to cycle*, *Out of scope*. The orchestrator's rulings on carried questions and agent concerns are C6–C12 in `.runs/task-cycles/agent-path-to-running-product/cycle.md` (questions table).

## Git Range to Review

**Base:** 77c8a8bb98d4a093c9a4c9891ac4e9ad86f4f988
**Head:** c657b2b

```bash
git diff --stat 77c8a8b..c657b2b
git diff 77c8a8b..c657b2b
```

## The spec is a vision document

The spec says what the software must do. It does not enumerate every input, environment, or condition the software will meet. For behavior the spec is silent on, judge by what a reasonable person using this software would expect: a reasonable person's expectation is a requirement, and a spec's silence is not permission. Grade such findings by their effect on that person, not by whether the spec mentions the trigger.

## Declined to judge

Before your verdict, list every behavior you considered and set aside as outside the plan or spec, one line each, with the reason. The executor rules on each line; nothing you set aside is dropped silently. An empty list means you set nothing aside.

## Read-Only Review

Your review is read-only on this checkout. Do not mutate the working tree, the index, HEAD, or branch state in any way. Use tools like `git show`, `git diff`, and `git log` to inspect history. If you need a working copy of a different revision, check it out into a separate temporary directory (e.g. `git worktree add <scratch>/review-[SHA] [SHA]`) — never move HEAD on this checkout.

## You Do Not Dispatch Subagents

Do all of this review yourself. Never spawn a subagent to review part of the diff, and never spawn another reviewer for a second opinion. This process already provides every review seat the work gets; a reviewer you spawn duplicates one of them at full cost, and its verdict counts for nothing. If the diff feels too large for one pass, review it in passes yourself and say so in your report.

## What to Check

**Plan alignment:**
- Does the implementation match the plan / requirements?
- Are deviations justified improvements, or problematic departures?
- Is all planned functionality present?

**Code quality:**
- Clean separation of concerns?
- Proper error handling?
- Type safety where applicable?
- DRY without premature abstraction?
- Edge cases handled?

**Architecture:**
- Sound design decisions?
- Reasonable scalability and performance?
- Security concerns?
- Integrates cleanly with surrounding code?

**Testing:**
- Tests verify real behavior, not mocks?
- Edge cases covered?
- Integration tests where they matter?
- All tests passing?

**Production readiness:**
- Migration strategy if schema changed?
- Backward compatibility considered?
- Documentation complete?
- No obvious bugs?

## Calibration

Categorize issues by actual severity. Not everything is Critical. Acknowledge what was done well before listing issues — accurate praise helps the implementer trust the rest of the feedback.

If you find significant deviations from the plan, flag them specifically so the implementer can confirm whether the deviation was intentional. If you find issues with the plan itself rather than the implementation, say so.

## Output Format

### Strengths
### Issues
#### Critical (Must Fix)
#### Important (Should Fix)
#### Minor (Nice to Have)

For each issue: File:line reference; what's wrong; why it matters; how to fix (if not obvious).

### Recommendations
### Assessment

**Ready to merge?** [Yes | No | With fixes]

**Reasoning:** [1-2 sentence technical assessment]

## Critical Rules

DO: categorize by actual severity; be specific (file:line); explain why each issue matters; acknowledge strengths; give a clear verdict.
DON'T: say "looks good" without checking; mark nitpicks as Critical; give feedback on code you didn't read; be vague; avoid a clear verdict.

---

## The-way's additions for this review (one-author route, final review of the whole change)

1. **Coverage, order and fidelity** (this review takes over a plan review's checks): every task item To do 1–3, every row 1–6 of *Settlements to record* (state which entry carries each), source fidelity of WAY-121 and WAY-165 to the rows and answers (no meaning added or lost; read the author's wording choices in `reports/author-foundation.md` "Choices" F1–F9 if useful), and that the foundation entries (`596a660`, `4c251dc`) and invariant checks (`8720107`) precede the dependent code (`c657b2b`). To do 3 is a line of the request, not a file; check that nothing in the change contradicts it. Read `agent-instructions/README.md` for this repository's rules before `main` (decisions edited in place).
2. **Foundation consistency:** the decisions and invariant follow `elements/decisions/template.md`, `elements/invariants/template.md` and `elements/common/rules.md`; fingerprints in relations are current (recompute with `relation-model/fingerprint.py`); no other entry of `foundations/` contradicts the new text (search for overlap with WAY-108, WAY-118, WAY-122, WAY-123, WAY-137, WAY-139, WAY-140, WAY-143 and the glossary's `surface`).
3. **Sharpness:** part `project-level`, criticality high; `project-level/readiness_check.py` is a declared trust boundary — check adversarial input handling (WAY-48); no irreversible operation. Confirm or correct the author's sharpness findings in `reports/author-implementation.md`.
4. **Weakest-point check (WAY-164):** the author named To do 2 / row 5 and wrote `ApprovedBefore` tests plus a manual run; read that section of `reports/author-implementation.md` and judge whether the check would catch the miss it names.
5. **Invariant check and its deliberate break (WAY-69, WAY-08):** the invariant `project-technology-record/1` in `foundations/invariants.md` was rewritten (`4c251dc`) and its checks written (`8720107`) by two agents other than the code's author. Review the checks against the sentence (do they test what it says, and only that?). Then, **from the invariant's sentence alone**, write a deliberate break of the code it covers in a separate temporary worktree of `c657b2b` (never this checkout) — e.g. make the readiness check accept a definition lacking one of the three marks, in one of the two modes — run the method `python -B gate/run_tests.py project-level --record <scratch>/project-level-tests.jsonl` on it, and report whether the checks fail. Record the break as a patch description, command, exit code and full output path; remove the temporary worktree afterwards. An undetected break is a finding.
6. **Checks:** run in a temporary worktree or read-only here: `python -B gate/run_tests.py project-level`, `python -B gate/run_tests.py gate`, the decisions and invariants format guards on the changed files with `--base none --merge-onto none` (part-map guard with `--base none`), and `git diff --check 77c8a8b..c657b2b`. Do not write `.runs/project-level-tests.jsonl` in this checkout; point `--record` to a scratch path.
7. The author's report lists two concerns (a marked line inside a fenced block in `## Technology` counts as an item; `define-project`'s branch for a definition with no Technology section still offers "leave it"). Judge them as you would any behavior.
8. Report also: the reviewed range, changed-file list with added/removed lines, your verdict, and the *Declined to judge* list.

Return message (short): verdict, range, counts of Critical/Important/Minor with one line each, deliberate-break result, check results incl. failures/unchecked, report path.

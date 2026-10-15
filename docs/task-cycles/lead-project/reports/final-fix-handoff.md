# Final fix wave

Worktree C:/Storage/repos/the-way-wt/lead-project, branch task/lead-project. User invoked the-way implement-task and delegated intermediate choices through a reviewable PR. Root answers questions provisionally; no human approval, merge, push, outside-repository write, child agent or next-stage dispatch. This is the ONE final fix wave under Superpowers 6.4.1 subagent-driven-development. Read this full handoff first, C:/Users/Mariusz/.codex/AGENTS.md, worktree AGENTS.md and agent-instructions/README.md.

Use full Superpowers 6.4.1 implementer-prompt.md and test-driven-development/SKILL.md, including its linked writing-good-tests.md, at C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/. Follow task-cycle/skill/SKILL.md adapter boundaries. Read .runs/task-cycles/lead-project/task.md, spec.md and plan.md, then refresh foundation selection for actual fix scope using elements/common/way_of_working.md. Relevant whole entries include WAY-13/48/69/125/135/136/148/149/150/153, reader surface/boundary and both new reader invariants. Read every applicable entry whole. Protected tests project-level/test_plan_state_invariant.py and project-level/test_plan_state_subprocesses_invariant.py are read-only; preserve byte hashes and report. Do not alter foundation entries. Ask root if a fix truly needs a protected contract change; do not bypass it.

## Requirements and complete findings

Final review report and exact findings will be appended before dispatch. Report is material to validate against code; fix all confirmed findings in one wave, without unrelated cleanup. R1 must receive a real ordinary behavioral regression test under an ANSI console setting and focused RED/GREEN evidence. Do not solve it merely by forcing UTF-8 in the fixture or hiding characters. User-facing paths/evidence must remain faithful and stdout work with the platform's ordinary redirected console settings.

Use focused tests while editing. Run all five required suites once on the final code: project-level with the exact invariant record command, gate, task-cycle, agent-instructions and installation. Exact commands:

```text
python -B gate/run_tests.py project-level --record .runs/project-plan-state-evidence.jsonl
python -B gate/run_tests.py gate
python -B gate/run_tests.py task-cycle
python -B gate/run_tests.py agent-instructions
python -B gate/run_tests.py installation
```

Installer tests clone the committed source: commit fixed product files before that suite so evidence covers current HEAD. Other suites may run before commit against the identical final bytes. Do not rerun a green suite without a new change or unresolved concrete concern. Save full UTF-8 logs under the cycle reports directory as final-fix-<suite>.txt. Record all actual failures, commands and exit codes; never claim a full process gate exists. Check generator currentness and git diff --check; regenerate only if this fix changes a skill description/inventory.

Because this wave fixes visible reader output, rerun the actual acceptance command against the full original plan with the disposable clone named in reports/acceptance-reader.md, first reading the vault rulebook as instructed. Do not change the source plan, definition or source repository; the reader may fetch only its disposable clone. Save final output separately and confirm original source preservation without overwriting earlier evidence. Existing final output expects the two mag-w-lesie transitions and honest unchecked observations.

## Deliverable

Commit by explicit paths, English message, on existing branch. Read own final diff. Full sanitized report .runs/task-cycles/lead-project/reports/final-fix.md must contain exact base/head, per-finding change and evidence, TDD RED/GREEN, tests and output paths/exits, protected hashes, final acceptance, choices/options/costs, self-review and every unresolved or unchecked concern. Return DONE / DONE_WITH_CONCERNS / NEEDS_CONTEXT with commits, concise checks and full report path. Never launch a reviewer; root owns the single scoped rereview and later independent assessment.

## Final dispatch authority

BASE 2cadf14fd3d21a82f1adee322f1022002b194385. Full review: reports/final-review.md. Exactly one finding, no Critical or Minor. Root verified the report against the prior independent reproduction and accepts R1 for repair. Writable product scope: project-level/plan_state.py and project-level/test_plan_state.py only. Root will handle report/choice updates. Complete finding follows verbatim.

### R1 — valid non-ASCII paths fail on an ANSI output stream

**Thread:** new review finding confirming the already reported open R1.

**Anchor:** `C:/Storage/repos/the-way-wt/lead-project/project-level/plan_state.py:267` (same issue at the report writes on lines 264, 271–280); masking test configuration: `C:/Storage/repos/the-way-wt/lead-project/project-level/test_plan_state.py:108`.

**Do wklejenia:** Czytnik kończy poprawne wywołanie kodem 2, gdy nazwa repozytorium zawiera polskie znaki, a stdout używa kodowania cp1252: zapis nagłówka `repository:` rzuca `UnicodeEncodeError`. Test ścieżki z polskimi znakami tego nie wykrywa, ponieważ fixture wymusza UTF-8; wyjście czytnika potrzebuje jawnej, bezstratnej obsługi kodowania i regresji z wyjściem ANSI.

**Dlaczego to zgłaszam:** The command must report evidence for an explicitly supplied repository, including non-ASCII paths. `display()` escapes control characters but preserves printable Unicode. `main()` writes that string using the inherited stdout encoding; with a repository name `product zażółć & $(echo injected)` and `PYTHONIOENCODING=cp1252`, the first repository-header write fails. The catch returns exit 2 with an encoding error instead of performing the otherwise valid observation. This is a product failure, not an invalid source or failed Git operation. The same dependency affects paths, refs, source findings and evidence elsewhere in the report.

Independent reproduction used the existing ordinary command test and changed only its child environment after fixture setup. It exited 2 instead of the required 0, with `error: 'charmap' codec can't encode character '\u017c' ... character maps to <undefined>`. Full short output is `C:/Storage/repos/the-way-wt/lead-project/.runs/task-cycles/lead-project/reports/final-review-encoding-reproduction.txt`. The wrapper recorded the expected reproduction and exited 0; the reader's exit 2 is the failing observation. The existing positive test's unconditional `PYTHONIOENCODING="utf-8"` explains why a green suite did not expose it.

Fix the report boundary so correct input does not depend on the caller preconfiguring UTF-8, and retain exact usable evidence without lossy replacement. Add a command-level ordinary regression with a restricted inherited output encoding and verify decoded paths/evidence, transitions and exit status, rather than merely removing the troublesome characters or checking for absence of a traceback. Include non-ASCII diagnostics as well as a successful path. Keep protected invariant checks read-only; if their mechanics need changing, return that edit to the independent check author.

Leaving this unchanged means the advertised command fails for valid paths in the documented Windows console environment. Fixing it costs a small output-boundary change and focused regression verification; it does not require a new state format or changes to orchestration policy. The precise encoding strategy belongs to the fixer, but silently replacing characters would weaken the promised exact evidence.


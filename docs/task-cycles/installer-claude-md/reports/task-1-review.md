# Task 1 independent review

## Spec Compliance

**Verdict: Issues found.** One misunderstood requirement: effective-import detection can accept an import that is inside a Markdown code span, suppressing the required warning (installation/install.py:206). No missing delivered file and no unjustified extra feature were identified.

The review covers committed installer code and tests in b8ff05bf139fc394f3f0df351e5da6c0bc0b0995..6ffb992691d51700f3a96573b4c79ab9ce4d911a. The complete supplied diff package was read once. The frozen task, task brief, implementer report, WAY-141/1, installation-claude-guidance/1, claude-code-imports/1, tool-loading notes, installation part map, repository instructions, code-review playbook and task-reviewer rubric were read.

**Cannot verify from this committed diff:** the independent invariant test and foundation edits are outside the slice. The controller should retain their independent assessment, verify their final staged contents and run the required foundation guards at the task boundary. Frozen-task items concerning installation/README.md, instruction-files/SKILL.md and WAY-132 Verification belong to Slice 2 and require that review; their absence is not a Task 1 defect. Historical test-first ordering and the reported gate run are not established by a single final diff; the controller should retain the existing execution evidence rather than treat this review as a fresh full-gate pass.

## Blocking issues

### 1. Important ? Do not start a code-span delimiter inside a longer backtick run

**Thread:** New thread.

**Anchor:** C:/Storage/repos/the-way-wt/installer-claude-md/installation/install.py:206

**Do wklejenia:** The code-span regex can begin at the second backtick of an unmatched two-backtick run: for a line consisting of two backticks, `example `, one backtick, ` @AGENTS.md `, and one final backtick, `has_agents_import` returns true even though the import is inside the matching single-backtick code span. This suppresses the missing-import warning and leaves Claude Code without the shared instructions. Match entire backtick runs with equal-length closing runs, and add this case to the CLI warning tests.

**Dlaczego to zg?aszam:** The detector exists to decide whether the installer must warn before confirmation; after removal of the generated rule, that warning is the only signal that existing CLAUDE.md fails to load shared guidance. Its inline-code expression guards against a backtick after the opening run but has no corresponding guard before it. When the full initial two-backtick run cannot find a two-backtick closer, the unanchored search retries at its second backtick and pairs that suffix with the first later single backtick. It removes the wrong portion of the line, exposing @AGENTS.md to the whitespace-delimited import search. Markdown instead leaves the unmatched two-backtick run as text and pairs the later single-backtick runs around @AGENTS.md, so the token is code and must not count under claude-code-imports/1.

Exact focused reproduction (no checkout mutation):

    from installation.install import has_agents_import
    has_agents_import("``example ` @AGENTS.md `\n")
    # Actual: True; required: False.

This is a false negative in the installation warning, not merely a spurious advisory. warnings_for at C:/Storage/repos/the-way-wt/installer-claude-md/installation/install.py:386 uses this result to omit the warning. Preserve the whole-run delimiter boundaries when matching code spans, including at the opening delimiter, and test the adversarial line through preview and cancelled apply alongside the existing import fixtures at C:/Storage/repos/the-way-wt/installer-claude-md/installation/test_install.py:378. Leaving it unchanged permits a product with no effective import to complete installation silently; fixing it requires a local parser adjustment and one regression fixture, without changing file ownership or write behavior.

## Other issues

Critical: 0. Important: 1. Minor: 0. No additional actionable findings.

## Strengths and verified behavior

- C:/Storage/repos/the-way-wt/installer-claude-md/installation/install.py:210 makes existing CLAUDE.md KEEP after validating regular UTF-8 text, and produces exactly @AGENTS.md followed by LF for absent files. The new shared-file entry at line 308 can never request APPEND.
- C:/Storage/repos/the-way-wt/installer-claude-md/installation/install.py:305 no longer adds the legacy rule to generated files. The single source of product guidance remains the AGENTS.md block.
- C:/Storage/repos/the-way-wt/installer-claude-md/installation/install.py:450 prints warnings before the confirmation at line 460. A focused read of the unchanged run function was necessary because the supplied hunk did not include that consumer: CREATE uses exclusive creation at line 482, KEEP reaches no write branch, cancellation returns before the write loops, and ignored-path warnings receive the new shared entry.
- C:/Storage/repos/the-way-wt/installer-claude-md/installation/test_install.py:57 exercises actual preview, apply and repeated installation; the changed assertions check exact generated bytes and absence of the legacy rule. Existing-file fixtures beginning at line 378 check unchanged bytes and cancellation. Directory, invalid UTF-8 and symlink tests check rejection before unintended writes. The ignored-new-file case checks both warning timing and resulting content.
- C:/Storage/repos/the-way-wt/installer-claude-md/installation/test_installed_guidance.py:40 independently checks accepted apply with existing files, including a fenced import mention and byte preservation. This file was read as dispatched evidence, not counted as part of the reviewed committed diff.

## Verification performed

The concrete doubt was whether the inline-code regex respects complete delimiter runs. A focused, read-only Python call reproduced the false-positive detection above; no suite was rerun. Additional small helper inputs were inspected in the same call to understand delimiter behavior; only the demonstrated whole-run defect is raised.

Read C:/Storage/repos/the-way-wt/installer-claude-md/.runs/installation-tests.jsonl: all 10 records have verdict pass and cite installation-claude-guidance/1, including four independent-test records. This verifies the record contents, not the historical timing of executions. The implementer reports 26 installation tests and 98 gate tests passing; this review does not independently rerun or claim the full gate.

## Task Quality

**Verdict: Needs fixes.** The file-plan integration is small, preserves existing ownership and uses meaningful CLI tests, but the effective-import detector has a demonstrated false positive that defeats the central warning requirement. Resolve finding 1 before Task 1 is accepted.

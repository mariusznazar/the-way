# Final whole-branch review

Reviewed range: `b8ff05bf139fc394f3f0df351e5da6c0bc0b0995..f3d49213ef50bb10808d7df8fbec31e3eed101c9`.

**Ready to merge: Yes, from code review. Critical: 0. Important: 0. Minor: 0.** The implementation meets the frozen task and plan, and the independent invariant check detects a deliberate violation for the expected reason. Normal request-link completion and human acceptance still belong to the integration workflow.

## Critical findings

None.

## Important findings

None.

## Minor findings

None. No deferred finding or parked issue was present in the supplied ledger, and none is introduced by this review.

## Strengths and requirement coverage

- **Exact generated import and preservation:** [installation/install.py](C:/Storage/repos/the-way-wt/installer-claude-md/installation/install.py:41) defines the sole generated line as `@AGENTS.md\n`. `claude_change` at line 210 chooses CREATE only for an absent path and KEEP for every supported existing file. The shared-file writer at line 480 uses exclusive creation for CREATE and performs no write for KEEP. It never decodes and rewrites an existing CLAUDE.md, so existing bytes and CRLF survive.
- **Warning and cancellation integration:** [installation/install.py](C:/Storage/repos/the-way-wt/installer-claude-md/installation/install.py:378) includes the new path in Git-ignore detection and emits the missing-import warning from the existing warning loop before the confirmation at line 460. Cancellation returns before submodule and file writes. The final warning correctly says Claude Code *may* miss shared instructions; it does not claim that no alternate loading configuration exists.
- **Adversarial inputs:** [installation/install.py](C:/Storage/repos/the-way-wt/installer-claude-md/installation/install.py:189) excludes fenced code and complete matching backtick delimiter runs. The original review's unmatched-double-backtick case is addressed by the opening lookbehind and retained as a CLI fixture. Existing suffix, punctuation, code-span and fence cases exercise the warning through preview and cancelled apply. [installation/test_install.py](C:/Storage/repos/the-way-wt/installer-claude-md/installation/test_install.py:427) checks directory, malformed UTF-8 and symlink refusal before product writes; the symlink target is preserved. The generated root file has no intermediate parent path to redirect.
- **Single generated guidance route:** [installation/install.py](C:/Storage/repos/the-way-wt/installer-claude-md/installation/install.py:297) no longer adds the old rule to the file plan. Shared guidance remains in the marked AGENTS.md block. No automatic old-rule deletion, CLAUDE.local.md warning or product pin move was introduced.
- **Migration and ownership documentation:** [installation/README.md](C:/Storage/repos/the-way-wt/installer-claude-md/installation/README.md:58) describes both root files and preserves the existing-file boundary. Its pin-move instructions at line 70 recreate 24 wrappers and restrict legacy-rule cleanup to products migrating from an older pin that installed that rule. [instruction-files/SKILL.md](C:/Storage/repos/the-way-wt/installer-claude-md/instruction-files/SKILL.md:106) excludes the CLAUDE.md the installer creates, rather than every product-owned CLAUDE.md. No skill description, name or location changed, so entry-point regeneration is not triggered.
- **Foundation consistency:** [foundations/decisions.md](C:/Storage/repos/the-way-wt/installer-claude-md/foundations/decisions.md:4276) records the installer-specific choice in WAY-141. WAY-132's changed verification examples respect that boundary without changing its binding sentence. [foundations/invariants.md](C:/Storage/repos/the-way-wt/installer-claude-md/foundations/invariants.md:2061) links the executable promise to WAY-141 and the import fact. [foundations/part_map.md](C:/Storage/repos/the-way-wt/installer-claude-md/foundations/part_map.md:240) names the matching failure mode and check. The unchanged installation-command surface allows creation of an absent file and limits changes to existing files consistently with this implementation.
- **Independent behavioral checks:** [installation/test_installed_guidance.py](C:/Storage/repos/the-way-wt/installer-claude-md/installation/test_installed_guidance.py:32) calls the real CLI and checks exact filesystem bytes, no generated old rule, applied-existing-file preservation and warning order. Its oracle does not import the installer's expected-content constant or helper. The deliberate break below demonstrates that this independence is useful.

## Verification and evidence limits

Read the complete supplied range package, frozen task and plan. Reviewed code/tests and documentation/foundation wording in separate passes. Read the task reports, both task reviews, the fix re-review, ledger and independent foundation assessment. Consulted unchanged write paths for the specific preservation/cancellation risk, and the recorded import facts/loading notes for detector and warning semantics. Confirmed HEAD equals the requested head and the reviewed working tree was clean before the experiment.

The implementer reports 26 installation tests and 98 gate tests passing after the last warning change. The documentation slice reports 104 instruction-files tests with 5 skips. The foundation author reports 169 decision, 233 invariant and 162 part-map tests passing. These broad suites were not rerun merely to repeat their evidence. I read the existing installation JSONL: all ten records pass and cite installation-claude-guidance/1, including all four independent checks.

Reported foundation guard limitations remain visible: decisions have 6 warnings and 5 unchecked checks (overdue reviews, the request-link placeholder, and unavailable base/merge comparisons); invariants have 3 unchecked checks; part map has 7 unchecked checks. The pending request URL must be substituted when the request exists. These partial checks and this review are not a full-gate pass.

The permitted sources describe import behavior and specific measured punctuation cases, not a complete executable specification of Claude Code's parser. No live Claude Code loading experiment was performed. This is a source limitation, not evidence of a demonstrated defect in an additional syntax case.

## Required deliberate invariant break

Guarantee selected directly from installation-claude-guidance/1: for a product without root CLAUDE.md, the installer creates it with `@AGENTS.md` as its sole line.

Created a disposable `git clone --quiet --no-hardlinks` at `C:/Storage/repos/the-way-wt/installer-claude-md/.runs/final-review-mutant-f3d4921` and verified its HEAD was exactly `f3d49213ef50bb10808d7df8fbec31e3eed101c9`. Only the clone's `installation/install.py` was changed, using byte-preserving replacement:

```python
CLAUDE_IMPORT = "@MISSING.md\n"
```

The corresponding original value was `"@AGENTS.md\n"`. No test was modified. From that disposable clone ran:

```text
python -B gate/run_tests.py installation --record .runs/installation-break.jsonl
```

**Exit: 1. Result: 26 tests in 68.699 seconds, FAILED (failures=3).** Relevant independent-check output:

```text
FAIL: test_creates_root_claude_import_when_missing
      (test_installed_guidance.InstalledGuidanceTest.test_creates_root_claude_import_when_missing)
  installation/test_installed_guidance.py, line 38
    self.assertEqual(claude.read_bytes(), b"@AGENTS.md\n")
AssertionError: b'@MISSING.md\n' != b'@AGENTS.md\n'
```

The JSONL explicitly records that independent check as `fail` for `installation-claude-guidance/1`. The two other expected failures are the existing preview's required `+@AGENTS.md` line and the ignored-new-file test's exact-byte assertion. The seven remaining invariant records pass. This is an expected assertion failure on installed output, not a setup error or inability to invoke the installer.

**Cleanup limitation:** Automatic approval review rejected the native PowerShell `Remove-Item -LiteralPath ... -Recurse -Force` cleanup with the stated reason `blocked by policy`, even though the script first resolved and compared the exact disposable path. No alternate deletion method was attempted. That one temporary clone and its mutation record remain at the path above; no reviewed source, index, HEAD or branch was changed by the experiment. The clone must be removed through an allowed cleanup action. This operational limitation does not alter the code verdict.

## Recommendations

No source correction is requested. Complete the existing request-link and human integration steps, retain this deliberate-break result with the review evidence, and remove the disposable clone when cleanup is permitted. Keep the distinction between observed installer behavior and unmeasured Claude runtime syntax in any release or review summary.

## Declined to judge

- Moving loop2's pin and applying legacy-rule cleanup there: explicitly a separate product task; this range only supplies the migration instructions.
- Monitoring an import removed after installation by an owner or `/init`: the frozen task explicitly leaves subsequent removal unmonitored, and this installer adds no continuing monitor.
- Exhaustive equivalence with Claude Code's parser for every Markdown construction and alternate import spelling: the recorded facts and fixtures do not provide that contract or runtime evidence. The documented and tested import cases were reviewed; no additional concrete failure was established.
- Cross-platform runtime behavior on hosts other than this Windows environment: no such run was available. The existing platform-qualified README wording is retained.

No other behavior was consciously set aside as outside the plan or specification.

## Assessment

**Ready to merge: Yes, from code review.** All requested changes are present and coherent across runtime behavior, documentation and foundation entries. No Critical, Important or Minor finding remains; the required independent check fails correctly under the deliberate break. The pending integration bookkeeping and the rejected temporary-copy cleanup are explicitly recorded above.

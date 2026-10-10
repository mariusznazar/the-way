# Independent foundation assessment

Assessment verdict: **apply** (advice, not acceptance).

Assessed range: `b8ff05bf139fc394f3f0df351e5da6c0bc0b0995..c9d015f415fffbc84ef12bf2a9a47ede2043924f`.
Observations: **8**. No blocking concern established. Two optional reductions/wording improvements and one explicitly unverified boundary are recorded below.

## Scope and method

Read the supplied complete diff package, current installer, changed tests, complete affected foundation entries, installation surface and part, WAY-107, WAY-132, referenced environment facts, instruction-file loading notes and the relevant fact probes. Inspected the introduction of WAY-132 (`67d61fa`, 2026-10-08) and the installer rule history (`b7e4426`, 2026-10-01). The worktree HEAD matched the assessed head and its tracked working tree was clean when inspected. Did not read the task, spec, plan, cycle chronology, author reports or author reasoning. No subagents were used.

This was a read-only assessment of the material and code paths. Tests were inspected, not executed; this report does not claim a passing test run or a live Claude Code experiment. The only file written is this report. Paths below are relative to `C:/Storage/repos/the-way-wt/installer-claude-md`.

## 1. Beneficiary and moment of use: no concern

Anchors: `foundations/decisions.md:4276`, `foundations/decisions.md:3001`, `foundations/environment_facts.md:200`, `foundations/environment_facts.md:208`, `installation/install.py:305`.

A product owner installing the-way gets a root import that makes the whole shared instruction file available through Claude's own instruction file. WAY-107 places the backlog location outside the generated block, so importing AGENTS.md carries useful product information that a generated copy of the block cannot carry. This is a concrete mechanism supported by the recorded environment facts, not an inference about agent obedience.

Leaving the old layout keeps the extra copy and does not itself provide the product-owned instructions through that route. Applying the change costs one small root file and detection of an existing import; it removes the generated rule copy. A stronger prose instruction to read the backlog is not an equivalent cheaper mechanism. No change required.

## 2. Frequency and earlier rules: no recurrence claim established

Anchors: `foundations/decisions.md:3877`, `foundations/decisions.md:3881`, `foundations/decisions.md:3904`, `instruction-files/tool_loading.md:196`.

WAY-132 entered on 2026-10-08 and expressly excluded installer-owned product files. The installer rule existed in the 2026-10-01 history. Thus this change addresses an excluded installation surface; it does not add a second behavioral reminder for a case the existing rule already governed.

For frequency, I examined the permitted git history and the loading measurements recorded for 2026-10-07 in the loading notes. Those measurements are technical fixtures, not production incidents. Zero raw session transcripts or task run logs were examined: the dispatch excludes the cycle and author records, and supplies no independent incident corpus. Actual incident count and recurrence after WAY-132 are therefore **unverifiable**, not zero. No claim about repeated agent mistakes should be added on this evidence. No change required to the present proposal, which rests on a specific installation mechanism.

## 3. Foundation scope and links: no concern

Anchors: `foundations/decisions.md:3888`, `foundations/decisions.md:4283`, `foundations/invariants.md:2061`, `foundations/part_map.md:240`, `foundations/part_map.md:329`.

WAY-132's changed examples track the new installer-owned file without changing its binding rule. WAY-141 records the installation choice; the new invariant names that decision and the import fact, and the installation failure mode names the invariant. The existing installation surface already permits creating a missing file while limiting additions to existing files, so it does not need another exception for CLAUDE.md. The rationale's backlog statement agrees with WAY-107.

These entries have different jobs and cannot all be cut as duplication: choice, executable promise and ownership/failure mapping. No contradiction or missing necessary relation was established. The new decision's request-link placeholder remains an integration detail, not evidence that the human has already accepted this assessment. No substantive change required.

## 4. Existing product content and broad application: no concern

Anchors: `installation/install.py:179`, `installation/install.py:210`, `installation/install.py:450`, `installation/install.py:460`, `installation/install.py:480`, `installation/test_install.py:427`, `installation/test_install.py:438`, `installation/test_install.py:449`.

Existing valid files take KEEP and never enter the write branches. A missing file is created exclusively. Unsupported existing paths and invalid UTF-8 are refused before installation writes; preservation is not implemented through decode/re-encode. Warnings are emitted before the apply prompt. This is coherent with leaving product-owned instructions to their owner.

Automatically adding the import would reduce manual work but would change an existing product file outside the declared installation surface. The chosen warning leaves that work to the owner and can leave guidance unavailable until the owner acts; that is the explicit tradeoff in WAY-141, not a concealed promise of repair. No change required.

## 5. Invariant, check and code: no concern within the recorded cases

Anchors: `foundations/invariants.md:2063`, `installation/test_install.py:56`, `installation/test_install.py:380`, `installation/test_install.py:415`, `installation/test_installed_guidance.py:32`, `installation/test_installed_guidance.py:41`, `installation/test_installed_guidance.py:58`, `installation/test_installed_guidance.py:75`.

The tests exercise creation, preview, cancellation, repeated installation, byte preservation, a missing import warning before confirmation, imports mentioned in code, an effective plain import and ignored output. The integration tests inspect actual product files and command output rather than only the helper's result. The code no longer includes the old rule in its planned output. The test changes replace the old positive expectation with the new contractual behavior and add the preservation branches; they do not merely delete a failing assertion.

No coherence defect was established by inspection. Execution remains unverified by this assessor. Nothing in this observation is a claim that Claude Code itself was exercised.

## 6. Detector fidelity: boundary explicitly unverified

Anchors: `installation/install.py:189`, `installation/install.py:206`, `foundations/environment_facts.md:200`, `instruction-files/tool_loading.md:43`, `instruction-files/tool_loading.md:196`, `probes/claude-code-imports/test_claude_code_imports.py:1`.

The recorded sources support ignoring Markdown spans/fences, and the local measurements support the tested punctuation boundary. The implementation handles complete backtick delimiter runs and the shown fence cases. That is adequate evidence for the supplied fixtures.

The sources do not supply Claude's full parser or a complete conformance corpus. Equivalence for every possible Markdown construction or every other path spelling cannot be verified from the permitted material. The fact probe watches documentation passages and explicitly does not run Claude. Do not describe these tests as proof of complete parser equivalence. If that stronger claim becomes necessary, it requires runtime evidence for the disputed construction or the actual parser contract; adding speculative regex branches is not justified here. This is a limitation, not an established defect requiring rewrite.

## 7. Warning wording could be more precise: optional improvement

Anchors: `installation/install.py:389`, `instruction-files/tool_loading.md:71`.

The warning says Claude Code "will miss" the shared instructions. The loading notes document a setting that reads both instruction files. Absence of this literal root import also does not inspect other possible import routes. Therefore the warning's definite consequence is stronger than the detector establishes.

Recommended optional replacement of the complete warning text:

> CLAUDE.md has no effective @AGENTS.md import; Claude Code may miss the shared instructions in AGENTS.md. Add @AGENTS.md by hand.

Leaving the wording costs occasional misleading certainty for a product with another configured route; changing one word preserves the actionable warning at negligible maintenance cost. This does not change the decision to warn for a missing root import, and is not a blocker to the installation mechanism.

## 8. What can be cut: one redundant integration case

Anchors: `installation/test_installed_guidance.py:32`, `installation/test_install.py:56`, `installation/test_install.py:87`.

The standalone creation test duplicates the successful installation and exact CLAUDE.md/absent-rule assertions already made in the existing preview/apply/rerun integration test. Both invoke the same installation command against a temporary product. Cutting the standalone creation test would save one complete installation without removing that coverage. Keeping it offers a shorter, more focused failing test name, at the cost of duplicate setup and execution.

This is optional, not a demand to reorganize the suite. The other new applied-existing-file cases add valuable evidence beyond preview/cancel tests and should stay. No foundation entry or production branch identified above should be cut.

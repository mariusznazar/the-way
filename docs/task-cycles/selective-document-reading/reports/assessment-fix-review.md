**F1 — obsolete pending-decision marker for whole-entry/Rejected reading — ADDRESSED.** [elements/common/way_of_working.md:118](https://github.com/mariusznazar/the-way/blob/c744b15f4a48d5525e42022a5e364997e2fe1f43/elements/common/way_of_working.md#L118) now gives the settled wording in full: “Read each entry selected or found by the search whole (WAY-150): a decision's *Rejected* holds an option already weighed and refused, and nowhere else says so.” The pending parenthesis is gone. The complete WAY-150/1 entry at [foundations/decisions.md:4647](https://github.com/mariusznazar/the-way/blob/c744b15f4a48d5525e42022a5e364997e2fe1f43/foundations/decisions.md#L4647) requires whole selected entries, expanded reading and unchanged whole-search domains; its violation example expressly rejects a search hit replacing an entry. The correction implements that contract.

### New Breakage in the Fix Diff

None. The one hunk keeps the whole-foundation search beyond written links, Scope and Part at lines 116–118. Complete selected/found entries remain mandatory at lines 118–119, consistent with the selection method's all-five-element search and whole findings at lines 92–98. The correction does not require reading every foundation entry. Glossary and waiting-entry searches, disposition of every finding, repeat search and separate evidence remain unchanged. No other TODO is touched.

### Out-of-Scope Observations

None. No new independent assessment or review of the unchanged branch was performed.

### Evidence and Checks

- Exact base: `1de9e1aa8e91134131d2e5c6d07c0f0ebf359186`.
- Exact head: `c744b15f4a48d5525e42022a5e364997e2fe1f43`; checkout HEAD matched, with no tracked differences from that head.
- Read the complete assessment, author settlement and fix report, the supplied one-hunk review package once, the full current shared workflow and complete WAY-150. The package and exact-range stat both identify one changed source file, two insertions and three deletions.
- Inspected [assessment-fix-gate.txt](assessment-fix-gate.txt) and its JSONL record: captured output reports 98 tests and OK, consistent with the worker's exit-0 claim. This is supplied execution evidence, not a suite run by this reviewer or direct coverage of the prose.
- Inspected [assessment-fix-elements-common.txt](assessment-fix-elements-common.txt) and its JSONL record: zero tests, NO TESTS RAN, with a fail/no-test record. The worker correctly treats the claimed exit 1 as unchecked, not a passing suite.
- Reviewer ran exact-range `git diff --check`: exit 0. No suite rerun: source inspection raised no concrete doubt requiring one.
- Source, index, HEAD and branch were not changed; only this report was written. No subagents or push.

### Declined to Judge

- Full-branch correctness and practical savings/comprehension: outside this one-finding scoped review; no new assessment was commissioned.

### Verdict

**Fix round: All findings addressed, no new Critical/Important breakage.** No open source concern remains in scope. Remaining verification limitation: the changed-part runner has no tests and the gate suite does not directly test this prose obligation; no full-gate or observed-agent-behavior claim follows. Stop before PR.

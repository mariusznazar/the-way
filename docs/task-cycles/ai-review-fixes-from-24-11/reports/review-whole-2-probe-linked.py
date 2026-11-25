"""Probes of check_linked on the head's test fixtures. Run from the head worktree's root:

    python -B <this file> <head worktree root>
"""

import os
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(sys.argv.pop(1), "elements", "common"))

import test_foundation_check as t  # noqa: E402


class Probe(t.FoundationCheckTest):
    def test_probe_single_digit_heading_old_gap_decision_altered(self):
        # The log writes its number without a leading zero; the decision's rationale changes,
        # the invariant with the old gap does not. WAY-12: an error is due.
        log = t.DECISIONS.replace("### ABC-01 —", "### ABC-1 —").replace(
            "derives from ABC-01@0123abcd", "derives from ABC-1"
        )
        gap = self.with_new_rule().replace(
            "- **Derives from:** ABC-01\n", "- **Derives from:** ABC-1\n"
        )
        reworded = self.edit(log, "one file is easy to copy.", "one file is easy to find.")
        product = self.derived(gap, reworded, base={"decisions": log, "invariants": gap})
        print("\n--- single-digit heading, decision altered:\n" + product.check()[1])

    def test_probe_two_digit_heading_same_case(self):
        gap = self.with_new_rule()
        reworded = self.edit(t.DECISIONS, "one file is easy to copy.", "one file is easy to find.")
        product = self.derived(gap, reworded, base={"invariants": gap})
        print("\n--- two-digit heading, decision altered:\n" + product.check()[1])

    def test_probe_versioned_invariant_heading(self):
        rule = self.with_new_rule().replace("## save-keeps-name\n", "## save-keeps-name/2\n")
        product = self.derived(rule)
        print("\n--- versioned invariant heading (earlier form):\n" + product.check()[1])


if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0], "-v"])

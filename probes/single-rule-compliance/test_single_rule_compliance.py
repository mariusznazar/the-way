"""Watch of the fact `single-rule-compliance`: in McMillan's factorial study of compliance with a
trivial target annotation across Claude Code CLI sessions, none of four structural variables of the
configuration files produces a detectable contrast after multiple-testing correction, while each
additional function the agent generates within a session is associated with approximately 5.6% lower
odds of compliance per step in the session lengths tested, though the relationship is non-monotonic.

It reads arXiv's own abstract page for the paper the fact's *Source* cites — no version newer than
the one cited, and no withdrawal — and every passage of *Source*, which stands on the abstract page
of the versioned address. A revision the authors announce fails nothing until arXiv publishes it
(WAY-82). No probe of the behaviour is written: what the study measured of its models cannot be
asked here and now without a model run.
"""

import os
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fact_probes  # noqa: E402

IDENTIFIER = "single-rule-compliance"


class SingleRuleComplianceWatch(fact_probes.FactCheck):

    def test_the_paper_is_neither_revised_nor_withdrawn(self):
        # fact: single-rule-compliance/1
        self.watch_arxiv(IDENTIFIER)

    def test_the_passages_stand(self):
        # fact: single-rule-compliance/1
        self.watch_passages(IDENTIFIER)


if __name__ == "__main__":
    unittest.main()

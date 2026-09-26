"""Watch of the fact `oracle-in-loop-building`: with the hidden test oracle in their loop, the two
Copilot CLI agents the study ran reach a near-perfect score from a demo holding the tested behaviour
directly, leaving the requested library dead or absent.

It reads arXiv's own abstract page for the paper the fact's *Source* cites — no version newer than
the one cited, and no withdrawal — and every passage of *Source* at its versioned address. A
revision the authors announce fails nothing until arXiv publishes it (WAY-82). No probe of the
behaviour is written: what the study measured of its models cannot be asked here and now without a
model run.
"""

import os
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fact_probes  # noqa: E402

IDENTIFIER = "oracle-in-loop-building"


class OracleInLoopBuildingWatch(fact_probes.FactCheck):

    def test_the_paper_is_neither_revised_nor_withdrawn(self):
        # fact: oracle-in-loop-building/1
        self.watch_arxiv(IDENTIFIER)

    def test_the_passages_stand(self):
        # fact: oracle-in-loop-building/1
        self.watch_passages(IDENTIFIER)


if __name__ == "__main__":
    unittest.main()

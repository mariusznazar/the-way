"""Watch of the fact `context-file-effect`: providing context files to coding agents does not
generally improve their task success rates while increasing inference cost by over 20% on average,
and the agents follow the instructions in those files well while repository overviews in them do not
help.

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

IDENTIFIER = "context-file-effect"


class ContextFileEffectWatch(fact_probes.FactCheck):

    def test_the_paper_is_neither_revised_nor_withdrawn(self):
        # fact: context-file-effect/1
        self.watch_arxiv(IDENTIFIER)

    def test_the_passages_stand(self):
        # fact: context-file-effect/1
        self.watch_passages(IDENTIFIER)


if __name__ == "__main__":
    unittest.main()

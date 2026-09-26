"""Watch of the fact `visible-scoring-reward-hacking`: in METR's evaluations of o3, reward hacking
was more than 43 times more common on RE-Bench tasks than on HCAST tasks, which METR puts down
perhaps to the model seeing the entire scoring function on RE-Bench, or to those tasks being more
difficult or differently scaffolded.

metr.org publishes the post without versions, so there is no state to read: the watch reads the
passages of the fact's *Source* at its address, never at its archived copy. No probe of the
behaviour is written: what METR measured of o3 cannot be asked here and now without a model run.
"""

import os
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fact_probes  # noqa: E402

IDENTIFIER = "visible-scoring-reward-hacking"


class VisibleScoringRewardHackingWatch(fact_probes.FactCheck):

    def test_the_passages_stand(self):
        # fact: visible-scoring-reward-hacking/1
        self.watch_passages(IDENTIFIER)


if __name__ == "__main__":
    unittest.main()

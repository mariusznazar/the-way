"""Watch of the fact `anthropic-model-states`: Anthropic describes the lifecycle of its models by
the states Active, Legacy, Deprecated and Retired, in which an Active model is fully supported and
recommended for use and a Retired one is no longer available for use.

platform.claude.com publishes the page without versions, so there is no state to read: the watch
reads the passages of the fact's *Source* at its address, never at its archived copy. No probe of
the behaviour is written: whether a request to a retired model fails cannot be asked here and now
without credentials.
"""

import os
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fact_probes  # noqa: E402

IDENTIFIER = "anthropic-model-states"


class AnthropicModelStatesWatch(fact_probes.FactCheck):

    def test_the_passages_stand(self):
        # fact: anthropic-model-states/1
        self.watch_passages(IDENTIFIER)


if __name__ == "__main__":
    unittest.main()

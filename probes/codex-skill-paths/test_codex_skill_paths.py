"""Watch of the fact `codex-skill-paths`: Codex's initial list of skills includes each skill's file
path.

learn.chatgpt.com publishes the documentation of Codex for its current release without versions, so
there is no state to read: the watch reads the passages of the fact's *Source* at its address, never
at its archived copy. No probe of the behaviour is written: what Codex lists cannot be asked here and
now without a run of Codex, which takes credentials and a model.
"""

import os
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fact_probes  # noqa: E402

IDENTIFIER = "codex-skill-paths"


class CodexSkillPathsWatch(fact_probes.FactCheck):

    def test_the_passages_stand(self):
        # fact: codex-skill-paths/1
        self.watch_passages(IDENTIFIER)


if __name__ == "__main__":
    unittest.main()

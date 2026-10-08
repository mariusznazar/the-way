"""Watch of the fact `codex-agents-md`: when it starts, Codex builds an instruction chain from the
`AGENTS.override.md`, or else the `AGENTS.md`, of its home directory and, walking from the project
root down to its current working directory, from at most one file in each directory, and stops
searching once it reaches its current directory.

learn.chatgpt.com publishes the documentation of Codex for its current release without versions,
so there is no state to read: the watch reads the passages of the fact's *Source* at its address,
never at its archived copy. No probe of the behaviour is written: what instruction chain Codex builds
cannot be asked here and now without a run of Codex, which takes credentials and a model.
"""

import os
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fact_probes  # noqa: E402

IDENTIFIER = "codex-agents-md"


class CodexAgentsMdWatch(fact_probes.FactCheck):

    def test_the_passages_stand(self):
        # fact: codex-agents-md/1
        self.watch_passages(IDENTIFIER)


if __name__ == "__main__":
    unittest.main()

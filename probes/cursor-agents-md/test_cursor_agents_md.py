"""Watch of the fact `cursor-agents-md`: Cursor CLI reads `AGENTS.md` and `CLAUDE.md` at the project
root, where they are present, and applies them as rules alongside `.cursor/rules`.

cursor.com publishes the documentation of Cursor CLI for its current release without versions,
so there is no state to read: the watch reads the passages of the fact's *Source* at its address,
never at its archived copy. No probe of the behaviour is written: whether Cursor CLI applies these
files cannot be asked here and now without a run of Cursor CLI, which takes credentials and a model.
"""

import os
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fact_probes  # noqa: E402

IDENTIFIER = "cursor-agents-md"


class CursorAgentsMdWatch(fact_probes.FactCheck):

    def test_the_passages_stand(self):
        # fact: cursor-agents-md/1
        self.watch_passages(IDENTIFIER)


if __name__ == "__main__":
    unittest.main()

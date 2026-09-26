"""Watch of the fact `claude-code-path-rules`: Claude Code applies a rule whose frontmatter gives
`paths` only when it works with files matching those patterns.

code.claude.com publishes the documentation of Claude Code for its current release without versions,
so there is no state to read: the watch reads the passages of the fact's *Source* at its address,
never at its archived copy. No probe of the behaviour is written: whether Claude Code loads a rule
cannot be asked here and now without a run of Claude Code, which takes credentials and a model.
"""

import os
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fact_probes  # noqa: E402

IDENTIFIER = "claude-code-path-rules"


class ClaudeCodePathRulesWatch(fact_probes.FactCheck):

    def test_the_passages_stand(self):
        # fact: claude-code-path-rules/1
        self.watch_passages(IDENTIFIER)


if __name__ == "__main__":
    unittest.main()

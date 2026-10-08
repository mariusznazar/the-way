"""Watch of the fact `claude-code-agents-md`: by default, Claude Code reads `AGENTS.md` as a
repository's project instructions, on v2.1.277 or later, only when no `CLAUDE.md`,
`.claude/CLAUDE.md` or `CLAUDE.local.md` stands in its working directory or any directory above it.

code.claude.com publishes the documentation of Claude Code for its current release without versions,
so there is no state to read: the watch reads the passages of the fact's *Source* at its address,
never at its archived copy. No probe of the behaviour is written: whether Claude Code reads
`AGENTS.md` cannot be asked here and now without a run of Claude Code, which takes credentials and a
model.
"""

import os
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fact_probes  # noqa: E402

IDENTIFIER = "claude-code-agents-md"


class ClaudeCodeAgentsMdWatch(fact_probes.FactCheck):

    def test_the_passages_stand(self):
        # fact: claude-code-agents-md/1
        self.watch_passages(IDENTIFIER)


if __name__ == "__main__":
    unittest.main()

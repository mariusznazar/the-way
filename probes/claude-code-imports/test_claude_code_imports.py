"""Watch of the fact `claude-code-imports`: Claude Code expands a file that a `CLAUDE.md` imports
with `@path/to/import` syntax and loads it into context at launch alongside that `CLAUDE.md`, and
skips Markdown code spans and fenced code blocks when it parses imports.

code.claude.com publishes the documentation of Claude Code for its current release without versions,
so there is no state to read: the watch reads the passages of the fact's *Source* at its address,
never at its archived copy. No probe of the behaviour is written: whether Claude Code loads an
imported file cannot be asked here and now without a run of Claude Code, which takes credentials and
a model.
"""

import os
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fact_probes  # noqa: E402

IDENTIFIER = "claude-code-imports"


class ClaudeCodeImportsWatch(fact_probes.FactCheck):

    def test_the_passages_stand(self):
        # fact: claude-code-imports/1
        self.watch_passages(IDENTIFIER)


if __name__ == "__main__":
    unittest.main()

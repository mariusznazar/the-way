"""Watch of the fact `claude-code-nested-skills`: Claude Code loads the skills of a `.claude/skills/`
directory below the directory where it starts the first time it reads or edits a file in that
subdirectory, keeps both skills available when a nested skill's directory name matches another
skill's name, and lists the directory-qualified variants with an instruction to invoke the one whose
directory holds the files it is working on.

code.claude.com publishes the documentation of Claude Code for its current release without versions,
so there is no state to read: the watch reads the passages of the fact's *Source* at its address,
never at its archived copy. No probe of the behaviour is written: whether Claude Code loads a skill
cannot be asked here and now without a run of Claude Code, which takes credentials and a model.
"""

import os
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fact_probes  # noqa: E402

IDENTIFIER = "claude-code-nested-skills"


class ClaudeCodeNestedSkillsWatch(fact_probes.FactCheck):

    def test_the_passages_stand(self):
        # fact: claude-code-nested-skills/1
        self.watch_passages(IDENTIFIER)


if __name__ == "__main__":
    unittest.main()

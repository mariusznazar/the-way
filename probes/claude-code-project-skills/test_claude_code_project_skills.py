"""Watch of the fact `claude-code-project-skills`: Claude Code loads project skills from
`.claude/skills/` in the directory where it starts and in each parent directory up to the repository
root, only up to the worktree root in a linked git worktree, and, on v2.1.277 or later, the main
checkout's project skills when the worktree checkout has no `.claude/skills` directory at its root.

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

IDENTIFIER = "claude-code-project-skills"


class ClaudeCodeProjectSkillsWatch(fact_probes.FactCheck):

    def test_the_passages_stand(self):
        # fact: claude-code-project-skills/1
        self.watch_passages(IDENTIFIER)


if __name__ == "__main__":
    unittest.main()

"""Watch the version and quoted passages of the design-rationale overlap study."""

import os
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fact_probes  # noqa: E402

IDENTIFIER = "llm-design-rationale-expert-overlap"


class LlmDesignRationaleExpertOverlapWatch(fact_probes.FactCheck):
    def test_the_paper_is_neither_revised_nor_withdrawn(self):
        # fact: llm-design-rationale-expert-overlap/1
        self.watch_arxiv(IDENTIFIER)

    def test_the_passages_stand(self):
        # fact: llm-design-rationale-expert-overlap/1
        self.watch_passages(IDENTIFIER)


if __name__ == "__main__":
    unittest.main()

"""Watch of the fact `llm-self-preference`: in self-evaluation on two summarisation tasks, GPT-3.5
Turbo, GPT-4 and Llama 2 disproportionately favour summaries written by themselves over those by
other LLMs and by humans.

It reads arXiv's own abstract page for the paper the fact's *Source* cites — no version newer than
the one cited, and no withdrawal — and every passage of *Source* at its versioned address. A
revision the authors announce fails nothing until arXiv publishes it (WAY-82). No probe of the
behaviour is written: what the study measured of its models cannot be asked here and now without a
model run.
"""

import os
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fact_probes  # noqa: E402

IDENTIFIER = "llm-self-preference"


class LlmSelfPreferenceWatch(fact_probes.FactCheck):

    def test_the_paper_is_neither_revised_nor_withdrawn(self):
        # fact: llm-self-preference/1
        self.watch_arxiv(IDENTIFIER)

    def test_the_passages_stand(self):
        # fact: llm-self-preference/1
        self.watch_passages(IDENTIFIER)


if __name__ == "__main__":
    unittest.main()

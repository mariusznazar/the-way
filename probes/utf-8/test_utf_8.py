"""Watch of the fact `utf-8`: UTF-8 encodes every character of the range U+0000..U+10FFFF in a
sequence of one to four octets.

It reads the state the RFC Editor publishes for the RFC the fact's *Source* cites — nothing
obsoletes or updates it — and the passage of *Source* at its address. An announced revision
fails nothing (WAY-82).
"""

import os
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fact_probes  # noqa: E402

IDENTIFIER = "utf-8"


class Utf8Watch(fact_probes.FactCheck):

    def test_the_edition_is_neither_obsoleted_nor_updated(self):
        # fact: utf-8/1
        self.watch_rfc(IDENTIFIER)

    def test_the_passage_stands(self):
        # fact: utf-8/1
        self.watch_passages(IDENTIFIER)


if __name__ == "__main__":
    unittest.main()

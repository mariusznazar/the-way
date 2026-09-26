"""Watch of the fact `json-text`: a JSON text is a serialized value, in which numeric values that
the grammar cannot represent, such as Infinity and NaN, are not permitted and the names
within an object should be unique.

It reads the state the RFC Editor publishes for the RFC the fact's *Source* cites — nothing
obsoletes or updates it — and the passages of *Source* at its address. An announced revision
fails nothing (WAY-82).
"""

import os
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fact_probes  # noqa: E402

IDENTIFIER = "json-text"


class JsonTextWatch(fact_probes.FactCheck):

    def test_the_edition_is_neither_obsoleted_nor_updated(self):
        # fact: json-text/1
        self.watch_rfc(IDENTIFIER)

    def test_the_passages_stand(self):
        # fact: json-text/1
        self.watch_passages(IDENTIFIER)


if __name__ == "__main__":
    unittest.main()

"""Watch of the fact `json-lines`: a JSON Lines file holds one valid JSON value on each line, ends
each line with '\n', which admits '\r\n', and may omit the terminator after the last value.

jsonlines.org publishes no editions, so there is no state to read: the watch reads the passages of
the fact's *Source* at its address, never at its archived copy.
"""

import os
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fact_probes  # noqa: E402

IDENTIFIER = "json-lines"


class JsonLinesWatch(fact_probes.FactCheck):

    def test_the_passages_stand(self):
        # fact: json-lines/1
        self.watch_passages(IDENTIFIER)


if __name__ == "__main__":
    unittest.main()

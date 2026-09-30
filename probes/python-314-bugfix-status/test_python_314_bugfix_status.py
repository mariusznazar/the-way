"""Watch the current Python 3.14 status against its commit-pinned release metadata source."""

import os
import sys
import tomllib
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fact_probes  # noqa: E402


IDENTIFIER = "python-314-bugfix-status"


class Python314BugfixStatusWatch(fact_probes.FactCheck):
    def test_the_source_passage_stands(self):
        # fact: python-314-bugfix-status/1
        self.watch_passages(IDENTIFIER)

    def test_the_current_status_is_bugfix(self):
        # fact: python-314-bugfix-status/1
        address = fact_probes.current_raw_page(IDENTIFIER)
        _, body = fact_probes.read_page(address)
        try:
            metadata = tomllib.loads(body.decode("utf-8"))["metadata"]["3.14"]
        except (UnicodeError, tomllib.TOMLDecodeError, KeyError) as problem:
            raise fact_probes.NoVerdict("cannot read Python 3.14 metadata: %s" % problem)
        self.assertEqual(metadata.get("status"), "bugfix")


if __name__ == "__main__":
    unittest.main()

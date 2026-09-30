"""Watch the current bugfix and security binary policies against their pinned source."""

import os
import re
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fact_probes  # noqa: E402


IDENTIFIER = "python-release-binaries"


class PythonReleaseBinariesWatch(fact_probes.FactCheck):
    def test_the_source_passages_stand(self):
        # fact: python-release-binaries/1
        self.watch_passages(IDENTIFIER)

    def test_the_current_phase_policies_stand(self):
        # fact: python-release-binaries/1
        address = fact_probes.current_raw_page(IDENTIFIER)
        _, body = fact_probes.read_page(address)
        try:
            text = body.decode("utf-8")
        except UnicodeError as problem:
            raise fact_probes.NoVerdict("cannot read the current version guide: %s" % problem)
        passages = fact_probes.cited_pages(IDENTIFIER)[0].passages
        if len(passages) != 2:
            raise fact_probes.NoVerdict("the fact does not cite both phase policies")
        for phase, (_, passage) in zip(("bugfix", "security"), passages):
            section = re.search(r"^:%s:\s*(.*?)(?=^:[a-z-]+:|\Z)" % phase, text,
                                flags=re.MULTILINE | re.DOTALL)
            if section is None:
                raise fact_probes.NoVerdict("the version guide has no %s status key" % phase)
            self.assertIn(fact_probes.collapse(passage), fact_probes.collapse(section.group(1)))


if __name__ == "__main__":
    unittest.main()

"""Probe of the fact `owasp-pytm-visibility`: the repository OWASP/pytm on github.com is public.

An anonymous GET of the address the observed command of the fact's *Source* asks: 200 passes,
404 fails, and any other answer, a redirect or a limit on anonymous requests included, gives no
verdict. *Holds for* names no release of a tool, so the probe reads none (WAY-91).
"""

import os
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fact_probes  # noqa: E402

IDENTIFIER = "owasp-pytm-visibility"


class OwaspPytmVisibilityProbe(fact_probes.FactCheck):

    def test_the_repository_opens_to_a_reader_who_is_not_signed_in(self):
        # fact: owasp-pytm-visibility/1
        self.probe_visibility(IDENTIFIER)


if __name__ == "__main__":
    unittest.main()

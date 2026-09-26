"""Watch of the fact `python-stdlib-modules`: the standard library of Python 3.14 holds the modules
that `sys.stdlib_module_names` names in a Python 3.14 interpreter, which lists them the same on all
platforms, names only the main package of each package, and excludes test modules.

docs.python.org publishes the documentation of the 3.14 series with no page for each bugfix
release, so there is no state to read: the watch reads the passages of the fact's *Source* at its
address, never at its archived copy.
"""

import os
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fact_probes  # noqa: E402

IDENTIFIER = "python-stdlib-modules"


class PythonStdlibModulesWatch(fact_probes.FactCheck):

    def test_the_passages_stand(self):
        # fact: python-stdlib-modules/1
        self.watch_passages(IDENTIFIER)


if __name__ == "__main__":
    unittest.main()

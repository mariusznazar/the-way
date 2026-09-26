"""Watch of the fact `github-private-repository-response`: GitHub answers a request for a private
resource that is not properly authenticated with 404 Not Found instead of 403 Forbidden, to avoid
confirming that a private repository exists.

docs.github.com publishes the page for each version of the REST API without editions of its own, so
there is no state to read: the watch reads the passages of the fact's *Source* at its address, never
at its archived copy. No probe of the behaviour is written: an anonymous 404 cannot tell a private
repository from a missing one (WAY-84), and naming a private repository known to exist takes the
credentials of someone who can open it.

The watch of the edition reads the versions of the REST API GitHub supports, which it publishes as
data: the version *Holds for* names leaving that list is a withdrawal of the edition (WAY-82). The
address of that list is not in *Source*, so it stands here.
"""

import json
import os
import re
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fact_probes  # noqa: E402

IDENTIFIER = "github-private-repository-response"
VERSIONS = "https://api.github.com/versions"


class GithubPrivateRepositoryResponseWatch(fact_probes.FactCheck):

    def test_the_passages_stand(self):
        # fact: github-private-repository-response/1
        self.watch_passages(IDENTIFIER)

    def test_the_api_version_is_supported(self):
        # fact: github-private-repository-response/1
        named = re.search(r"\bversion (\d{4}-\d{2}-\d{2})\b",
                          fact_probes.field_value(IDENTIFIER, "Holds for"))
        if named is None:
            raise fact_probes.NoVerdict("*Holds for* names no version of the REST API")
        _, body = fact_probes.read_page(VERSIONS)
        try:
            versions = json.loads(body)
        except ValueError as problem:
            raise fact_probes.NoVerdict("%s is no JSON: %s" % (VERSIONS, problem))
        if not isinstance(versions, list):
            raise fact_probes.NoVerdict("%s is no list of versions" % VERSIONS)
        if named.group(1) not in versions:
            self.fail("%s no longer lists version %s, which *Holds for* names; it lists %s"
                      % (VERSIONS, named.group(1), ", ".join(map(str, versions))))


if __name__ == "__main__":
    unittest.main()

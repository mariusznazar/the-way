"""Probe and watch of the fact `sha-256`: the Secure Hash Standard specifies SHA-256, whose final
result is a 256-bit message digest, in its section 6.2.

The probe gives `hashlib.sha256` the example messages NIST publishes for SHA-256 and compares the
digests with NIST's. The watch reads the passage of the fact's *Source* in the FIPS 180-4 PDF, and
the state of the standard on its page at NIST's Computer Security Resource Center. The expected
values are written out (WAY-69); *Holds for* names an edition of a standard and no release of a
tool, so the probe reads no release (WAY-81).
"""

import hashlib
import os
import re
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fact_probes  # noqa: E402

IDENTIFIER = "sha-256"

# NIST's example values for SHA-256, read at NIST's own pages, never from memory:
# https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines/example-values links
# - SHA-256, https://csrc.nist.gov/CSRC/media/Projects/Cryptographic-Standards-and-Guidelines/documents/examples/SHA256.pdf
#   — "One Block Message Sample" and "Two Block Message Sample", "Message Digest is";
# - Additional, https://csrc.nist.gov/CSRC/media/Projects/Cryptographic-Standards-and-Guidelines/documents/examples/SHA2_Additional.pdf
#   — "SHA-256 Test Data" #1 to #10; #11 to #13, of 0.5 to 1.6 GB, are left out for their size.
EXAMPLES = [
    (b"abc",
     "BA7816BF 8F01CFEA 414140DE 5DAE2223 B00361A3 96177A9C B410FF61 F20015AD"),
    (b"abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq",
     "248D6A61 D20638B8 E5C02693 0C3E6039 A33CE459 64FF2167 F6ECEDD4 19DB06C1"),
    (b"\xbd",
     "68325720 aabd7c82 f30f554b 313d0570 c95accbb 7dc4b5aa e11204c0 8ffe732b"),
    (b"\xc9\x8c\x8e\x55",
     "7abc22c0 ae5af26c e93dbb94 433a0e0b 2e119d01 4f8e7f65 bd56c61c cccd9504"),
    (b"\x00" * 55,
     "02779466 cdec1638 11d07881 5c633f21 90141308 1449002f 24aa3e80 f0b88ef7"),
    (b"\x00" * 56,
     "d4817aa5 497628e7 c77e6b60 6107042b bba31308 88c5f47a 375e6179 be789fbb"),
    (b"\x00" * 57,
     "65a16cb7 861335d5 ace3c607 18b5052e 44660726 da4cd13b b745381b 235a1785"),
    (b"\x00" * 64,
     "f5a5fd42 d16a2030 2798ef6e d309979b 43003d23 20d9f0e8 ea9831a9 2759fb4b"),
    (b"\x00" * 1000,
     "541b3e9d aa09b20b f85fa273 e5cbd3e8 0185aa4e c298e765 db87742b 70138a53"),
    (b"A" * 1000,
     "c2e68682 3489ced2 017f6059 b8b23931 8b6364f6 dcd835d0 a519105a 1eadd6e4"),
    (b"U" * 1005,
     "f4d62dde c0f3dd90 ea1380fa 16a5ff8d c4c54b21 740650f2 4afc4120 903552b0"),
    (b"\x00" * 1000000,
     "d29751f2 649b32ff 572b5e0a 9f541ea6 60a50f94 ff0beedf b0b692b9 24cc8025"),
]

# The page on which NIST publishes the state of FIPS 180-4 (August 2015): a withdrawn or
# superseded publication carries its withdrawal there. The fact's *Source* cites the PDF alone,
# which carries no state, so this address is the probe's own.
STATE_PAGE = "https://csrc.nist.gov/pubs/fips/180-4/upd1/final"
# What the page shows of a publication in force, and what it shows of a withdrawn one.
IN_FORCE = 'id="pub-release-date"'
WITHDRAWN = re.compile(r'id=["\'](pub-withdrawn-message|pub-withdrawn-date|'
                       r'pub-superseded-container|pub-header-withdrawn)["\']')


class Sha256Probe(fact_probes.FactCheck):

    def test_the_digests_are_nist_s_examples(self):
        # fact: sha-256/1
        found = []
        for message, digest in EXAMPLES:
            answered = hashlib.sha256(message).digest()
            wanted = bytes.fromhex(digest)
            if answered != wanted:
                found.append("%d bytes starting %r give %s, not %s" % (
                    len(message), message[:8], answered.hex(), wanted.hex()))
            if len(answered) * 8 != 256:
                found.append("the digest is %d bits, not 256" % (len(answered) * 8))
        if found:
            self.fail("; ".join(found))


class Sha256Watch(fact_probes.FactCheck):

    def test_the_passage_stands(self):
        # fact: sha-256/1
        self.watch_passages(IDENTIFIER)

    def test_the_standard_is_neither_withdrawn_nor_superseded(self):
        # fact: sha-256/1
        _, body = fact_probes.read_page(STATE_PAGE)
        page = body.decode("utf-8", errors="replace")
        if IN_FORCE not in page:
            raise fact_probes.NoVerdict("%s shows no publication this check can read"
                                        % STATE_PAGE)
        marks = sorted(set(match.group(1) for match in WITHDRAWN.finditer(page)))
        if marks:
            self.fail("%s marks the edition withdrawn or superseded: %s"
                      % (STATE_PAGE, ", ".join(marks)))


if __name__ == "__main__":
    unittest.main()

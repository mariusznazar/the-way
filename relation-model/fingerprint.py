"""Content fingerprint of a foundation entry's binding part (WAY-02, WAY-39).

Usage as a module:  from fingerprint import fingerprint
Usage from a shell: python fingerprint.py < binding_part.txt
"""

import hashlib
import re
import sys

LENGTH = 8


def fingerprint(binding_part: str) -> str:
    """Return the fingerprint of a binding part, as WAY-39 defines it."""
    normalized = re.sub(r"[ \r\n]+", " ", binding_part).strip(" ")
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()[:LENGTH]


if __name__ == "__main__":
    print(fingerprint(sys.stdin.buffer.read().decode("utf-8")))

"""The form of an identifier and of a version, as foundation entries carry them (WAY-41, WAY-64,
WAY-75, WAY-57, WAY-79).

An identifier of an entry of the part map, the invariants or the environment facts is one or more
words in lower case joined by hyphens; a version is a number written without a leading zero; an
entry is cited at a version as `<identifier>/<version>`. The format guards and the test runner of
the gate take the form from here. Only the form lives here: how a reader finds a citation in a
file — a comment line, a `data:` line, a line of a record — stays with that reader (WAY-55).
Whether an identifier is `none`, held twice or withdrawn is a check of its element's guard.

Usage as a module:  from identifier import IDENTIFIER, VERSION, CITED
"""

import re

# One or more words of lower-case letters and digits, joined by hyphens: `relation-model`.
IDENTIFIER = r"[a-z0-9]+(?:-[a-z0-9]+)*"
# A number written without a leading zero, starting at 1.
VERSION = r"[1-9][0-9]*"
# An entry at a version: `relation-model-directory-contents/1`.
CITED = r"%s/%s" % (IDENTIFIER, VERSION)


def is_identifier(text: str) -> bool:
    """Whether the whole text has the form of an identifier."""
    return re.fullmatch(IDENTIFIER, text) is not None


def is_cited(text: str) -> bool:
    """Whether the whole text has the form of an identifier at a version."""
    return re.fullmatch(CITED, text) is not None

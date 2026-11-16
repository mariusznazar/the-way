"""One-off move of the pricing of stage rows out of process-audit/audit_count.py (WAY-365).

Run from the worktree root: python -B .runs/author-fix/move.py
Exit code 0 when the two files are written, 2 when a range is not what it should be.
"""

import sys
from pathlib import Path

SOURCE = Path("process-audit/audit_count.py")
TARGET = Path("process-audit/stage_pricing.py")

raw = SOURCE.read_bytes().decode("utf-8")
lines = raw.split("\n")


def take(first: int, last: int, starts: str) -> list[str]:
    """Lines first..last (1-based, inclusive), after checking the first line starts as expected."""
    if not lines[first - 1].startswith(starts):
        print(f"line {first} does not start with {starts!r}: {lines[first - 1]!r}")
        sys.exit(2)
    return lines[first - 1:last]


classes = take(896, 931, "@dataclass(frozen=True)")
functions = take(1371, 1462, "def is_orchestrator_row")
header = '''"""The price of the stage rows of a cycle's `stages.md`, moved out of `audit_count.py`.

The price list as numbers (`ModelPrice`, `Prices`), a row of the section of tokens by model
(`StageTokens`) and the cost in dollars of such rows at a list's prices (`priced`, `priced_older`,
`cost_at`), as `process-audit/audit_count.py` counts the cost of a cycle (WAY-337). It is imported,
never run, and runs nothing when imported. Standard library only.
"""

from dataclasses import dataclass
from decimal import Decimal

UNKNOWN = "unknown"
NO_MODEL = "—"
ORCHESTRATOR = "orchestrator"
MILLION = Decimal(1_000_000)
# A text copied from a file into a reason is cut to this many characters.
TEXT_CAP = 200


'''
body = "\n".join(classes).rstrip("\n") + "\n\n\n" + "\n".join(functions).rstrip("\n") + "\n"
TARGET.write_bytes((header + body).encode("utf-8"))

# Remove the ranges from the script, last first so the numbers stay true.
for first, last, starts in ((1918, 1919, "# A text copied"), (1371, 1464, "def is_orchestrator_row"),
                            (896, 933, "@dataclass(frozen=True)"), (408, 408, "MILLION"),
                            (389, 390, "NO_MODEL"), (348, 348, "UNKNOWN")):
    if not lines[first - 1].startswith(starts):
        print(f"range {first} does not start with {starts!r}: {lines[first - 1]!r}")
        sys.exit(2)
    del lines[first - 1:last]

text = "\n".join(lines)
text = text.replace(
    "from pathlib import Path\n",
    "from pathlib import Path\n", 1)
SOURCE.write_bytes(text.encode("utf-8"))
print("moved")
sys.exit(0)

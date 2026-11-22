"""List each invariant whose Derives from names a decision whose Verification does not name it."""

import re
import sys
from pathlib import Path

root = Path(sys.argv[1])
invariants = (root / "foundations/invariants.md").read_text(encoding="utf-8")
decisions = (root / "foundations/decisions.md").read_text(encoding="utf-8")

verification = {}
for block in re.split(r"(?m)^### ", decisions)[1:]:
    number = re.match(r"(WAY-\d+)", block)
    if not number:
        continue
    found = re.search(r"- \*\*Verification:\*\*(.*?)(?=\n- \*\*Origin)", block, re.S)
    verification[number.group(1)] = found.group(1) if found else ""

missing = 0
total = 0
for block in re.split(r"(?m)^## ", invariants)[1:]:
    name = block.split("\n", 1)[0].strip()
    derives = re.search(r"- \*\*Derives from:\*\* (.*)", block)
    if not derives:
        continue
    for number in re.findall(r"WAY-\d+", derives.group(1)):
        total += 1
        if number in verification and not re.search(
            r"\b" + re.escape(name) + r"\b", verification[number]
        ):
            missing += 1
            print(f"{name} <- {number}: not named in Verification")
print(f"{missing} of {total} links not named")

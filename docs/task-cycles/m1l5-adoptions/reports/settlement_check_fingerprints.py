"""Check every relation fingerprint the new and edited entries carry, and list every carrier of
their own fingerprints (scratch script, not committed)."""
import re
import sys

sys.path.insert(0, "relation-model")
from fingerprint import fingerprint  # noqa: E402

with open("foundations/decisions.md", encoding="utf-8") as handle:
    text = handle.read()

entries = {}
for match in re.finditer(r"^### WAY-(\d+)/\d+ — .*?\n\n(.*?)\n\n(.*?)(?=^### |\Z)", text, re.M | re.S):
    entries[int(match.group(1))] = (match.group(2), match.group(3))

checked = [124, 137, 138, 139, 140]
failures = 0
for number in checked:
    binding, rest = entries[number]
    print("WAY-%d binding %s" % (number, fingerprint(binding)))
    relations = re.search(r"\*\*Relations:\*\* (.*?)\n- \*\*", rest, re.S).group(1)
    for target, carried in re.findall(r"WAY-(\d+)@([0-9a-f]{8})", relations):
        actual = fingerprint(entries[int(target)][0])
        state = "ok" if actual == carried else "STALE (now %s)" % actual
        failures += actual != carried
        print("  carries WAY-%s@%s %s" % (target, carried, state))

for number in checked:
    own = fingerprint(entries[number][0])
    carriers = [m.start() for m in re.finditer(r"WAY-%d@" % number, text)]
    for position in carriers:
        line = text.count("\n", 0, position) + 1
        carried = text[position:position + 20].split("@")[1][:8]
        state = "ok" if carried == own else "STALE"
        failures += carried != own
        print("WAY-%d@%s carried at decisions.md:%d %s" % (number, carried, line, state))
    if not carriers:
        print("WAY-%d has no carrier in the log" % number)

print("failures: %d" % failures)
sys.exit(1 if failures else 0)

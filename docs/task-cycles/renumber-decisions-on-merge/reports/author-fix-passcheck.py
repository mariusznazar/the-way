"""Own-work check of the fix: the pass of step 2 and the count of step 3 of "The renumbering of the
task's decisions", run on an overlapping map and on a second renumbering."""
import re
from collections import Counter

REF = re.compile(r"WAY-(\d+)\b")


def apply_pass(text, mapping):
    """Step 2: the map applied once, whole numbers only."""
    return REF.sub(lambda m: "WAY-" + mapping.get(m.group(1), m.group(1)), text)


def counts(texts):
    """Steps 1 and 3: references of each whole number in the given texts."""
    c = Counter()
    for t in texts:
        c.update(REF.findall(t))
    return c


def step3_ok(mapping, before, after):
    """Each new number stands as often as the old number that became it did; an old number that is
    no new number stands no more."""
    for old, new in mapping.items():
        if after[new] != before[old]:
            return False
    news = set(mapping.values())
    return all(after[old] == 0 for old in mapping if old not in news)


# One: overlapping map 500..502 -> 502..504 (the complying example of WAY-403).
m1 = {"500": "502", "501": "503", "502": "504"}
rewritten = [
    "The spec names WAY-500, WAY-501 and WAY-502.",
    "The plan: WAY-502 twice, WAY-502, and WAY-35 stays, WAY-5020 stays.",
    "A handoff names WAY-501.",
]
stays = ["Human's remark, word for word: WAY-500 is wrong."]  # not rewritten, not counted
before = counts(rewritten)
done = [apply_pass(t, m1) for t in rewritten]
after = counts(done)
assert done[0] == "The spec names WAY-502, WAY-503 and WAY-504."
assert done[1] == "The plan: WAY-504 twice, WAY-504, and WAY-35 stays, WAY-5020 stays."
assert step3_ok(m1, before, after), "the count of step 3 fails a correct pass"
# The search the old text gave: the old number 502 stands after a correct pass (the reviewer's I-1).
assert after["502"] > 0, "old 502 is a new number: a search for it finds correct references"
# A reference the pass missed is caught by the count.
missed = [done[0], done[1], "A handoff names WAY-501."]  # the third text was not rewritten
assert not step3_ok(m1, before, counts(missed))
missed2 = [done[0], "The plan: WAY-502 twice, WAY-502 ...", done[2]]  # old 502 missed in the plan
assert not step3_ok(m1, before, counts(missed2))
# Decision by decision (the chain the step forbids) also fails the count.
chain = rewritten[:]
for old in ("500", "501", "502"):
    chain = [t.replace("WAY-" + old, "WAY-" + m1[old]) for t in chain]
assert not step3_ok(m1, before, counts(chain))

# Two: a second renumbering, the map 502..504 -> 505..507; the first row stays as it was written.
row1 = "WAY-500 -> WAY-502, WAY-501 -> WAY-503, WAY-502 -> WAY-504"
m2 = {"502": "505", "503": "506", "504": "507"}
row2 = "WAY-502 -> WAY-505, WAY-503 -> WAY-506, WAY-504 -> WAY-507"
chain_map = {}
for a, b in (("500", "502"), ("501", "503"), ("502", "504")):
    chain_map[a] = m2[b]  # first number -> present number, read through the two rows
assert chain_map == {"500": "505", "501": "506", "502": "507"}
# What the old text did ("rewritten with the rest"): the whole row under the second map.
corrupt = apply_pass(row1, m2)
assert corrupt == "WAY-500 -> WAY-505, WAY-501 -> WAY-506, WAY-505 -> WAY-507"
assert corrupt != "WAY-500 -> WAY-505, WAY-501 -> WAY-506, WAY-502 -> WAY-507"
# The new text: the row stays; a reader holding 502 as first borne takes row 1 (502 -> 504), then
# row 2 (504 -> 507), as the chain says.
assert dict(re.findall(r"WAY-(\d+) -> WAY-(\d+)", row1))["502"] == "504"
assert dict(re.findall(r"WAY-(\d+) -> WAY-(\d+)", row2))["504"] == "507"
# Step 3 of the second pass counts the texts that are rewritten, row 1 left out.
texts2 = ["The spec names WAY-502, WAY-503 and WAY-504, and WAY-504 again."]
b2 = counts(texts2)
a2 = counts([apply_pass(t, m2) for t in texts2])
assert step3_ok(m2, b2, a2)
print("ok")

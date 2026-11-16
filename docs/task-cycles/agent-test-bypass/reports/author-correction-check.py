"""Own-work check of correction 1: each rule names the other, the refinement carries the answer,
WAY-409 and WAY-410 are untouched.  Usage: python -B check.py ROOT BASEROOT"""
import re, sys
from pathlib import Path
root, base = Path(sys.argv[1]), Path(sys.argv[2])
def entry(r, n):
    t = (r / "foundations/decisions.md").read_text(encoding="utf-8")
    i = t.index(f"### WAY-{n} "); j = t.find("\n### ", i + 5)
    return t[i:j]
def flat(x): return re.sub(r"\s+", " ", x)
w100, w134 = flat(entry(root, 100)), flat(entry(root, 134))
files = {p: flat((root / p).read_text(encoding="utf-8")) for p in (
    "elements/decisions/template.md", "elements/common/skill/task_variant.md",
    "project-level/task/template.md", "project-level/task/skill/find_settlements.md")}
def near(text):
    """Text of each practice-from-outside passage and the 500 characters after it."""
    return [text[m.start():m.start() + 500] for m in re.finditer(r"practice from outside", text)]
no_wait = all(not re.search(r"wait(?:s|ing)", seg.split("WAY-134)")[0]) for f in (
    "elements/common/skill/task_variant.md", "project-level/task/skill/find_settlements.md",
    "project-level/task/template.md", "elements/common/skill/build_table.md")
    for seg in near(flat((root / f).read_text(encoding="utf-8"))))
accepted = all("`accepted`" in flat((root / f).read_text(encoding="utf-8")) for f in (
    "elements/common/skill/task_variant.md", "project-level/task/skill/find_settlements.md"))
wording = ("A row that repeats a choice the human made between ways shown enters accepted"
           in flat((root / "project-level/task/template.md").read_text(encoding="utf-8")))
checks_more = [
 ("no copy of the step makes a row that adopts an outside practice wait", no_wait),
 ("task_variant and find_settlements build such a row accepted", accepted),
 ("the task template still builds a row that repeats a choice accepted", wording),
]
checks = [
 ("WAY-100 names WAY-134", "WAY-134" in w100),
 ("WAY-134 names WAY-100", "WAY-100" in w134),
 ("WAY-134 relations: narrows WAY-100", "**Relations:** derives from WAY-33 · narrows WAY-114 · narrows WAY-100" in w134),
 ("WAY-134 says what a decision holds where the source keeps none",
  "puts no left-out part in its rejected options" in w134 and "names what it takes from the practice in its binding sentences or its *Rationale*" in w134),
 ("WAY-134 says the refinement shows the left-out parts as ways",
  "the refinement shows the human, among the ways of the question that settles it, the parts the practice leaves out" in w134),
 ("WAY-134 states the area where it prevails", "In this area this decision prevails over WAY-100" in w134),
 ("WAY-100 says WAY-134 prevails for a row", "there WAY-134 prevails" in w100),
 ("decisions template carries it", "the parts the practice leaves out are among the ways the row's source keeps" in files["elements/decisions/template.md"]),
 ("task variant (refinement, step 2) carries it", "adopts a practice from outside the product (WAY-100)" in files["elements/common/skill/task_variant.md"]),
 ("task template carries it (Source and Questions to settle)",
  files["project-level/task/template.md"].count("practice from outside the product") == 2),
 ("find_settlements carries it", "adopts a practice from outside the product (WAY-100)" in files["project-level/task/skill/find_settlements.md"]),
 ("WAY-409 unchanged since the reviewed head", entry(root, 409) == entry(base, 409)),
 ("WAY-410 unchanged since the reviewed head", entry(root, 410) == entry(base, 410)),
]
checks += checks_more
bad = 0
for n, ok in checks:
    print(("ok   " if ok else "FAIL ") + n); bad += 0 if ok else 1
print("failed:", bad); sys.exit(1 if bad else 0)

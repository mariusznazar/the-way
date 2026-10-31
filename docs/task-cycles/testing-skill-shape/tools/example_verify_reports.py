"""Check assessment.md quotes against the base, line coverage, route sums, and named paths."""
import html
import os
import re
import subprocess

REPO = "C:/Storage/repos/the-way/.runs/worktrees/styleguide-skill-shape"
BASE = "525cde1dd53c474f56ea0ece289cb60e868aa90d"
PATH = "product-guidelines/styleguide/SKILL.md"
R = f"{REPO}/.runs/task-cycles/styleguide-skill-shape/reports/"
NL = chr(10)

base = subprocess.run(["git", "-C", REPO, "show", f"{BASE}:{PATH}"], capture_output=True,
                      check=True).stdout.decode("utf-8")
lines = base.split(NL)
if lines[-1] == "":
    lines.pop()

text = open(R + "assessment.md", encoding="utf-8", newline="").read()
pat = re.compile(r"\[[^\]]+:(\d+)-(\d+)\]\(https://github.com/mariusznazar/the-way/blob/" + BASE +
                 r"/" + re.escape(PATH) + r"#L(\d+)-L(\d+)\): <code>(.*?)</code>")
ranges, bad = [], 0
for m in pat.finditer(text):
    s, e, s2, e2 = (int(m.group(i)) for i in range(1, 5))
    quote = html.unescape(m.group(5).replace("&#124;", "|")).split("<br>")
    quote = [html.unescape(q) if False else q for q in quote]
    expect = lines[s - 1:e]
    if not (s == s2 and e == e2 and quote == expect):
        bad += 1
        print("QUOTE MISMATCH", s, e)
    ranges.append((s, e))
main_rows = ranges[:-2]  # the last two quotes are the two proposals
cov = {}
for s, e in main_rows:
    for n in range(s, e + 1):
        cov[n] = cov.get(n, 0) + 1
over = [n for n, c in cov.items() if c > 1]
miss = [n for n, l in enumerate(lines, 1) if l.strip() and n not in cov]
print("quotes", len(ranges), "mismatches", bad, "overlaps", over, "missing nonblank", miss)

wc = open(R + "word-counts.md", encoding="utf-8", newline="").read().split(NL)
route = None
state = None
sections = []
cur = None
for l in wc:
    if l.startswith("## ") and l[3].isdigit():
        route = l[3:]
    elif l.startswith("### "):
        state = l[4:]
    elif (l.startswith("Read before step 4") or l.startswith("Read from step 4")) and re.search(r"(\d+) words", l):
        cur = {"route": route, "state": state, "kind": l.split(",")[0], "stated": int(re.search(r"(\d+) words", l).group(1)),
               "sum": 0}
        sections.append(cur)
    elif l.startswith("Total at the end") and cur:
        cur = None
    elif re.match(r"^  - .*: (\d+)$", l) and cur is not None:
        cur["sum"] += int(l.rsplit(": ", 1)[1])
ok = all(s["sum"] == s["stated"] for s in sections)
print("route sections", len(sections), "sums consistent", ok)

# actual word count of each file once more, directly
for name in os.listdir(f"{REPO}/product-guidelines/styleguide"):
    n = len(open(f"{REPO}/product-guidelines/styleguide/{name}", encoding="utf-8").read().split())
    print(name, n)

# every path in backticks of the rebuilt files that holds a slash exists
missing = []
for name in os.listdir(f"{REPO}/product-guidelines/styleguide"):
    t = open(f"{REPO}/product-guidelines/styleguide/{name}", encoding="utf-8").read()
    for p in re.findall(r"`([^`\s]+/[^`\s]*)`", t):
        if p.startswith(".runs/") or "<" in p or "*" in p or p.startswith("guidelines/"):
            continue
        p2 = p.replace(".the-way/", "")
        if not os.path.exists(f"{REPO}/{p2}"):
            missing.append((name, p))
    for p in re.findall(r"`([A-Za-z_]+\.md)`", t):
        if p not in ("AGENTS.md",) and not os.path.exists(f"{REPO}/product-guidelines/styleguide/{p}") \
                and not os.path.exists(f"{REPO}/{p}"):
            missing.append((name, p))
print("paths that do not exist:", missing)

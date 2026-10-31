"""Check reports/assessment.md against the base: each quote literal and whole, line ranges, coverage."""
import html
import re
import subprocess
import sys

REPO = "C:/Storage/repos/the-way/.runs/worktrees/coding-skill-shape"
BASE = "f86fd71f3cb72a9eb1620c388af44bbd1198fb4a"
PATH = "product-guidelines/coding/SKILL.md"
NL = chr(10)

base = subprocess.run(["git", "-C", REPO, "show", f"{BASE}:{PATH}"], capture_output=True,
                      check=True).stdout.decode("utf-8").split(NL)
text = open(sys.argv[1], encoding="utf-8", newline="").read()
pat = re.compile(r"\[" + re.escape(PATH) + r":(\d+)-(\d+)\]\(https://github.com/mariusznazar/the-way/blob/"
                 + BASE + "/" + re.escape(PATH) + r"#L(\d+)-L(\d+)\): <code>(.*?)</code>")
errors, covered, rows = [], {}, 0
table = text.split("## 3. The table")[1].split("## Text added")[0]
for m in pat.finditer(table):
    s, e, s2, e2 = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
    rows += 1
    if (s, e) != (s2, e2):
        errors.append(f"link range differs from the label at {s}-{e}")
    body = html.unescape(m.group(5)).split("<br>")
    if body != base[s - 1:e]:
        errors.append(f"quote of {s}-{e} is not the literal base text")
    for n in range(s, e + 1):
        if n in covered:
            errors.append(f"line {n} in two rows")
        covered[n] = True
missing = [n for n, l in enumerate(base, 1) if l.strip() and n not in covered]
if missing:
    errors.append(f"nonblank lines in no row: {missing}")
print(rows, "rows;", len(covered), "lines;", len(errors), "problems")
for e in errors:
    print("  ", e)
sys.exit(1 if errors else 0)

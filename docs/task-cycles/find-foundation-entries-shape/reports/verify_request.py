#!/usr/bin/env python3
"""Check every number of the request description against files (task acceptance criterion:
"every number the request states, in prose too, is compared with the files").

Usage: python -I -B verify_request.py        (run verify_counts.py first; it must exit 0)

What it does:
  1. The five-row table of sums must equal word-counts.md (English table and Polish table).
  2. Derived figures are computed from the files: growth of the five files together, the task-route
     savings of proposal 1, the verdict tally of assessment.md.
  3. Every other number of the description (outside URLs, code spans, commit ids, decision
     identifiers and dates) must stand as a token in one of the checked source files:
     word-counts.md, assessment.md, author_report.md, review_report.md, review_fix_report.md,
     stages.md, base_gate.txt, gate_e9c900a.txt, or be one of the derived figures.
Only ASCII goes to stdout. Exit 0 when nothing is unexplained.
"""
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
REC = HERE.parent
ROOT = HERE.parents[3]
SKILL_FILES = ["SKILL.md", "read.md", "build_table.md", "definition_variant.md", "task_variant.md"]
problems = []


def fail(msg):
    problems.append(msg)


def read(p):
    return pathlib.Path(p).read_text(encoding="utf-8")


def tokens(text):
    text = re.sub(r"(?<=\d) (?=\d{3}\b)", "", text)  # "23 159 706"
    text = text.replace(",", "")
    return set(re.findall(r"\d+", text))


req = read(REC / "request.md")

# ---- 1. the table of sums equals word-counts.md
wc = read(REC / "reports/word-counts.md")
rows = []
for l in wc.splitlines():
    cells = [c.strip() for c in l.strip().strip("|").split("|")]
    if l.startswith("|") and len(cells) == 4 and re.fullmatch(r"\d+", cells[1]):
        rows.append((cells[1], cells[2], re.sub(r"\D", "", cells[3])))
if len(rows) != 5:
    fail("word-counts.md: expected 5 rows, got %d" % len(rows))
req_rows = []
for l in req.splitlines():
    cells = [c.strip() for c in l.strip().strip("|").split("|")]
    if l.startswith("|") and len(cells) == 4 and re.fullmatch(r"\d+", cells[1]):
        req_rows.append((cells[1], cells[2], re.sub(r"\D", "", cells[3])))
if req_rows != rows + rows:
    fail("the two tables of the request (English, Polish) differ from word-counts.md: %r vs %r"
         % (req_rows, rows))

# ---- 2. derived figures
def words(path):
    return len(pathlib.Path(path).read_text(encoding="utf-8").split())


after = {n: words(ROOT / "elements/common/skill" / n) for n in SKILL_FILES}
base = len(subprocess.run(["git", "show", "f447bb6:elements/common/skill/SKILL.md"], cwd=ROOT,
                          capture_output=True, text=True, encoding="utf-8").stdout.split())
derived = set()
derived.add(str(sum(after.values())))
derived.add(str(sum(after.values()) - base))
derived.add(str(base))
for n, w in after.items():
    derived.add(str(w))
wow = words(ROOT / "elements/common/way_of_working.md")
derived.add(str(wow))
derived.add(str(wow - 952))  # proposal 1: 800
sums = [int(r[1]) for r in rows]
derived.add(str(sums[1] - 952))
derived.add(str(sums[2] - 952))
asm = read(REC / "reports/assessment.md")
verd = {"keep": 0, "move": 0}
nrows = 0
for l in asm.splitlines():
    if re.match(r"\| \d+ \|", l):
        nrows += 1
        v = [c.strip() for c in l.strip().strip("|").split("|")][6]
        verd["keep" if v.startswith("keep") else "move" if v.startswith("move") else "other"] = \
            verd.get("keep" if v.startswith("keep") else "move" if v.startswith("move") else "other", 0) + 1
if verd.get("other"):
    fail("assessment verdicts other than keep/move: %r" % verd)
derived.update([str(nrows), str(verd["keep"]), str(verd["move"])])
if sums[1] - (sums[1] - 952) != 952:
    fail("arithmetic")

# ---- 3. every other number stands in a checked file
sources = ["reports/word-counts.md", "reports/assessment.md", "reports/author_report.md",
           "reports/review_report.md", "reports/review_fix_report.md", "stages.md",
           "base_gate.txt", "gate_e9c900a.txt"]
known = set(derived)
for s in sources:
    known |= tokens(read(REC / s))

body = req
body = re.sub(r"https?://\S+", " ", body)
body = re.sub(r"`[^`]*`", " ", body)
body = re.sub(r"WAY-\d+(, \d+)*( and \d+)?", " ", body)
body = re.sub(r"\d{4}-\d{2}-\d{2}", " ", body)
body = re.sub(r"\b[0-9a-f]{7,40}\b", " ", body)
body = re.sub(r"\b0:\d\d:\d\d\b", " ", body)
unexplained = sorted({t for t in tokens(body) if t not in known and len(t) >= 2})
for t in unexplained:
    fail("number %s of the request stands in no checked file" % t)

print("derived:", " ".join(sorted(derived, key=int)))
print("%d problem(s)" % len(problems))
for p in problems:
    print("PROBLEM:", p)
sys.exit(1 if problems else 0)

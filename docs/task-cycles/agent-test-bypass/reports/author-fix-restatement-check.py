"""Fails on a restatement of WAY-410 in the files of the change that names one case only.

Usage: python -B restatement_check.py ROOT
A unit is a paragraph (blank-line separated) or a table row. A unit that describes the first case
(a test the requirement contradicts) must describe the second (a test no general code passes), and
a unit that lists the sources of an answer must list all four.
"""
import re
import sys
from pathlib import Path

root = Path(sys.argv[1])
files = ["task-cycle/skill/SKILL.md", "task-cycle/skill/request_template.md",
         "task-cycle/review/fix.md", "task-cycle/skill/correction.md", "task-cycle/change/SKILL.md"]
first = re.compile(r"(requirement contradicts|contradicts the requirement|test (and|contradicts) the requirement"
                   r"|test the requirement contradicts|a test that the requirement contradicts"
                   r"|test and the requirement contradict)", re.I)
second = re.compile(r"(general code|for every input)", re.I)
sources = re.compile(r"(the task, the spec, (a|the) decisions?|decisions? or the sentence of an invariant"
                     r"|the task, the spec, the decisions)", re.I)
four = [re.compile(w, re.I) for w in (r"\btask\b", r"\bspec\b", r"decision", r"invariant")]
bad = 0
for f in files:
    text = (root / f).read_text(encoding="utf-8")
    units = []
    for para in re.split(r"\n\s*\n", text):
        if "\n|" in para or para.startswith("|"):
            for row in para.split("\n"):
                units += row.split(" | ") if row.startswith("|") else [row]
        else:
            units.append(para)
    for u in units:
        u = re.sub(r"\s+", " ", u)
        if first.search(u) and not second.search(u):
            bad += 1
            print("ONE CASE ONLY:", f, "|", u[:110])
        if "ways open" in u and "test" in u and not re.search(r"ways open.*(no general code|cannot)", u):
            bad += 1
            print("WAYS OPEN OF ONE CASE ONLY:", f, "|", u[:110])
        if sources.search(u) and not all(p.search(u) for p in four):
            bad += 1
            print("NOT FOUR SOURCES:", f, "|", u[:110])
print("restatements failing:", bad)
sys.exit(1 if bad else 0)

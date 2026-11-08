"""Reviewer's own check: every clause of the base SKILL.md stands word for word in the rebuilt files.

Splits the base file (git show 2754675:project-level/skill/SKILL.md) into clauses at '.', ';' and
':' followed by whitespace, flattens whitespace, and looks for each clause in the flattened text of
the ten files of project-level/skill/ at the worktree. Prints only ASCII: the base line number of
each clause not found, and the counts. Exit 1 if any clause is missing, else 0.
"""
import os
import re
import subprocess
import sys

REPO = "."
SKILL_DIR = REPO + "/project-level/skill"


def flat(s):
    return re.sub(r"\s+", " ", s).strip()


def main():
    base = subprocess.run(["git", "-C", REPO, "show", "2754675:project-level/skill/SKILL.md"],
                          capture_output=True, check=True).stdout.decode("utf-8")
    lines = base.split(chr(10))
    after = ""
    for name in sorted(os.listdir(SKILL_DIR)):
        if name.endswith(".md"):
            with open(SKILL_DIR + "/" + name, encoding="utf-8") as f:
                after += " " + f.read()
    after = flat(after)
    # Map each character offset of the base to its line number.
    starts, pos = [], 0
    for ln in lines:
        starts.append(pos)
        pos += len(ln) + 1
    text = base
    clauses, missing = 0, []
    for m in re.finditer(r"[^.;:]+[.;:]?", text):
        c = flat(m.group(0))
        c = re.sub(r"^(- |\d\. |#+ |  - )", "", c).strip()
        c = c.lstrip("-").strip()
        if len(c.split()) < 3:
            continue
        clauses += 1
        if c not in after:
            line = max(i for i, s in enumerate(starts) if s <= m.start()) + 1
            missing.append((line, c))
    print("clauses:", clauses, "missing:", len(missing))
    for line, c in missing:
        print("  base line", line, ":", c.encode("ascii", "replace").decode("ascii")[:110])
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())

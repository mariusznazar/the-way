"""Compare the base SKILL.md with the rebuilt files sentence by sentence.

Both sides are whitespace-normalised, list markers dropped. A base sentence is "kept" when it
stands verbatim in the rebuilt corpus; a rebuilt sentence is "new" when it stands verbatim in the
base. The differing sentences of both sides are written to the output file (UTF-8).
"""
import re
import subprocess
import sys

REPO = "C:/Storage/repos/the-way/.runs/worktrees/coding-skill-shape"
BASE = "f86fd71f3cb72a9eb1620c388af44bbd1198fb4a"
DIR = "product-guidelines/coding/"
NEW_FILES = ["SKILL.md", "orchestrated_mode.md", "task_document.md", "recognize.md",
             "starting_set.md", "research.md", "trial_run.md", "kinds.md", "new_tools.md",
             "hand_back.md", "settle.md"]


NL = chr(10)


def headings(text):
    return [l.strip() for l in text.split(NL) if l.startswith("#")]


def norm(text):
    text = NL.join(l for l in text.split(NL) if not l.startswith("#"))
    text = re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", text, flags=re.M)
    return re.sub(r"\s+", " ", text).strip()


def sentences(text):
    # split after a sentence end or a semicolon/colon that closes a clause, before the next word
    flat = norm(text)
    parts = re.split(r"(?<=[.!?;:])\s+", flat)
    return [p for p in parts if p]


def main(out_path):
    base = subprocess.run(["git", "-C", REPO, "show", f"{BASE}:{DIR}SKILL.md"],
                          capture_output=True, check=True).stdout.decode("utf-8")
    new = {}
    for name in NEW_FILES:
        with open(f"{REPO}/{DIR}{name}", encoding="utf-8", newline="") as f:
            new[name] = f.read()
    base_n = norm(base)
    new_n = " ".join(norm(t) for t in new.values())
    lines = []
    missing = [s for s in sentences(base) if s not in new_n]
    lines.append(f"BASE sentences not verbatim in the rebuilt files: {len(missing)}")
    for s in missing:
        lines.append(f"  - {s}")
    lines.append("")
    for name, t in new.items():
        extra = [s for s in sentences(t) if s not in base_n]
        lines.append(f"{name}: sentences not verbatim in the base: {len(extra)}")
        for s in extra:
            lines.append(f"  + {s}")
    lines.append("")
    lines.append("Headings in the base: " + " | ".join(headings(base)))
    for name, t in new.items():
        lines.append(f"Headings in {name}: " + " | ".join(headings(t)))
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    print(len(missing), "base sentences differ")


if __name__ == "__main__":
    main(sys.argv[1])

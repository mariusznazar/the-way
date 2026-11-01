"""Compare the base SKILL.md of plan-project with the rebuilt files sentence by sentence.

Whitespace normalised, list markers and headings dropped. Writes UTF-8 to the output path:
base sentences not verbatim in the rebuilt corpus, and, per rebuilt file, sentences not verbatim in the base.
"""
import re
import subprocess
import sys

REPO = "C:/Storage/repos/the-way/.runs/worktrees/plan-project-skill-shape"
BASE = "2f51e6c31f5911ac8a0292a80a4f599bd4bd0092"
DIR = "project-level/plan/skill/"
NEW = ["SKILL.md", "delegated_mode.md", "existing_plan.md", "read.md", "reading_definition_and_plan.md",
       "cut_tasks.md", "guideline_tasks.md", "assign_entries.md", "place_questions.md",
       "write_and_check.md", "critique_plan.md", "hand_over.md"]
NL = chr(10)


def norm(text):
    text = NL.join(l for l in text.split(NL) if not l.startswith("#"))
    text = re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", text, flags=re.M)
    return re.sub(r"\s+", " ", text).strip()


def sentences(text):
    return [p for p in re.split(r"(?<=[.!?;:])\s+", norm(text)) if p]


def main(out):
    base = subprocess.run(["git", "-C", REPO, "show", f"{BASE}:{DIR}SKILL.md"],
                          capture_output=True, check=True).stdout.decode("utf-8")
    new = {}
    for n in NEW:
        with open(f"{REPO}/{DIR}{n}", encoding="utf-8", newline="") as f:
            new[n] = f.read()
    base_n = norm(base)
    new_n = " ".join(norm(t) for t in new.values())
    lines = []
    miss = [s for s in sentences(base) if s not in new_n]
    lines.append(f"BASE sentences not verbatim in the rebuilt files: {len(miss)}")
    lines += [f"  - {s}" for s in miss]
    for n, t in new.items():
        extra = [s for s in sentences(t) if s not in base_n]
        lines.append("")
        lines.append(f"{n}: sentences not verbatim in the base: {len(extra)}")
        lines += [f"  + {s}" for s in extra]
    with open(out, "w", encoding="utf-8", newline=NL) as f:
        f.write(NL.join(lines) + NL)
    print(len(miss), "base sentences differ")


if __name__ == "__main__":
    main(sys.argv[1])

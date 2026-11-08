"""List every unit of the base SKILL.md that does not stand word for word in the rebuilt files.

A unit is a heading (its step number dropped), or a part of a list item or paragraph between '. '
or '; ' boundaries, whitespace normalised. A unit counts as found when it occurs as a substring of
the whitespace-normalised text of SKILL.md and the files beside it in the worktree, list markers
removed. Writes the misses to compare_sentences.txt beside this script; prints only counts.
Exit code 1 when a unit of the base is missing and not listed in EXPECTED, or when an entry of
EXPECTED is found word for word after all; 0 otherwise.
"""
import glob
import os
import re
import subprocess
import sys

REPO = "."
BASE = "dfd50e513c09bebe9d09d74209cd28612565da83"
HERE = os.path.dirname(os.path.abspath(__file__))
NL = chr(10)
ITEM = re.compile(r"^\s*(?:[-*]|\d+\.)\s+")
HEADING = re.compile(r"^#+\s")

# Units of the base that the rebuild rewords on purpose; each is reported in author_report.md.
EXPECTED = {
    "When the human names an existing definition, read it whole and go on from where its status line says",
    'a working table under "Projected foundation changes" means step 5 is under way, and an item of "Technology" ending `— open` that step 6 is',
    "A finding that its fingerprint no longer matches means the definition changed after the gate, and it goes through step 7 again",
    'On reopening, add `## Technology` reading `TODO` before "Projected foundation changes", set the status line to `definition — open: Technology`, and go on at step 6 (WAY-121)',
    "Write each answer into the definition, with its status line, before the next question, so that a fresh agent reading only the file knows where the work stands (WAY-112)",
    "Three moves run through the rounds (WAY-112)",
    "what the files can answer, read yourself instead of asking",
    "The project level's directory, `project-level/`, is there, and each skill named below is the project skill of that name with the `the-way-` prefix",
}


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def units(text):
    body = text.split(NL + "---" + NL, 1)[1] if text.startswith("---" + NL) else text
    blocks, cur = [], []
    for ln in body.split(NL):
        if HEADING.match(ln):
            blocks.append(" ".join(cur))
            cur = []
            blocks.append(re.sub(r"^#+\s+(?:\d+\.\s+)?", "", ln))
        elif ITEM.match(ln) or not ln.strip():
            blocks.append(" ".join(cur))
            cur = [ITEM.sub("", ln)]
        else:
            cur.append(ln)
    blocks.append(" ".join(cur))
    out = []
    for b in blocks:
        for p in re.split(r"(?<=[.;])\s+", norm(b)):
            p = p.strip().rstrip(".;:").strip()
            if p:
                out.append(p)
    return out


def main():
    base = subprocess.run(["git", "-C", REPO, "show", BASE + ":project-level/skill/SKILL.md"],
                          capture_output=True, check=True).stdout.decode("utf-8")
    new = ""
    for path in sorted(glob.glob(REPO + "/project-level/skill/*.md")):
        with open(path, encoding="utf-8", newline="") as f:
            lines = [ITEM.sub("", ln) for ln in f.read().split(NL)]
        new += " " + norm(" ".join(lines))
    all_units = units(base)
    missing = [s for s in all_units if s not in new]
    unexpected = [s for s in missing if s not in EXPECTED]
    found_expected = sorted(EXPECTED - set(missing))
    with open(os.path.join(HERE, "compare_sentences.txt"), "w", encoding="utf-8", newline=NL) as f:
        f.write("Units of the base not found word for word in the rebuilt files:" + NL)
        for s in missing:
            f.write(("  expected: " if s in EXPECTED else "  UNEXPECTED: ") + s + NL)
        f.write("Entries of EXPECTED found word for word after all:" + NL)
        for s in found_expected:
            f.write("  " + s + NL)
    print(len(all_units), "units of the base;", len(missing), "missing;", len(unexpected),
          "unexpected;", len(found_expected), "expected but found")
    return 1 if unexpected or found_expected else 0


if __name__ == "__main__":
    sys.exit(main())

"""Check that correction 1 changed nothing but the named substitutions.

Usage: python -B check_correction.py COMMIT

For each file COMMIT changes, compares the whitespace-normalised text of COMMIT~1 with that of
COMMIT after applying, to the parent's text, the substitutions of the correction: proposal 6
("each skill named below is" -> "... or in the files beside this skill is"), proposal 4 (the uses
of "the gate" for the readiness gate), proposal 5 (the template's path) and proposal 1 (the
orchestrator's sentence removed). Line breaks are ignored, so a rewrapped paragraph passes only
if its words are the same. Exit 1 and the file names when a file differs, else 0. Prints only ASCII.
"""
import subprocess
import sys

REPO = "."
SUBS = [
    ("each skill named below is", "each skill named below or in the files beside this skill is"),
    ("after the gate", "after the readiness gate"), ("through the gate", "through the readiness gate"),
    ("blocks the gate", "blocks the readiness gate"), ("pending gate", "pending readiness gate"),
    ("that gate", "that readiness gate"), ("to the gate", "to the readiness gate"),
    ("before the gate", "before the readiness gate"),
    ("`definition_template.md`", "`project-level/definition_template.md`"),
    ("The project orchestrator may make the initial text edit only when that full text is already "
     "before it and needs no other definition-section or foundation reading; otherwise it delegates "
     "the edit. ", ""),
]


def show(rev, path):
    return subprocess.run(["git", "-C", REPO, "show", rev + ":" + path], capture_output=True,
                          check=True).stdout.decode("utf-8")


def main(commit):
    files = subprocess.run(["git", "-C", REPO, "diff", "--name-only", commit + "~1", commit],
                           capture_output=True, check=True, text=True).stdout.split()
    bad = []
    for p in files:
        a = " ".join(show(commit + "~1", p).split())
        b = " ".join(show(commit, p).split())
        for x, y in SUBS:
            a = a.replace(x, y)
        if a != b:
            bad.append(p)
    print(len(files), "files changed;", len(bad), "differ beyond the named substitutions")
    for p in bad:
        print("  ", p)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))

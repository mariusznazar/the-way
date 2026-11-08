"""Check the pointers between the files of project-level/skill/ in the worktree.

1. Every `<name>.md` a file of the skill names "beside this skill" or "beside this file" exists.
2. Every file beside SKILL.md is named in SKILL.md, under the heading of the step or section that
   EXPECTED gives it, and under no other step's heading.
3. Every file a step's file names is named in SKILL.md as well (WAY-265 for a variant's file).
4. Step 6 of SKILL.md names readiness_gate.md for a finding of the readiness check, and step 7 has it
   read unless step 6 did (finding I-1). The jumps named in criterion 5 of the task: in readiness_gate.md, the findings sent back to steps 4, 5
   and 6 name rounds.md, find_entries.md and technology.md; in existing_definition.md, the
   jumps to steps 5, 6 and 7 name their files; readiness_gate.md names delegated_mode.md with the
   condition "In a turn dispatched through a refinement conversation path".
Exit code 1 with the failures listed, else 0. Prints only ASCII.
"""
import os
import re
import sys

DIR = "project-level/skill"
NL = chr(10)
EXPECTED = {
    "delegated_mode.md": ["Delegated definition change and gate", "7. The readiness gate"],
    "existing_definition.md": ["0. Start or resume"],
    "idea.md": ["1. The idea"],
    "read_foundation.md": ["2. Read the foundation for the idea"],
    "first_write.md": ["3. The first write"],
    "rounds.md": ["4. Rounds through the sections"],
    "find_entries.md": ["5. Find the entries"],
    "technology.md": ["6. Settle the technology"],
    "readiness_gate.md": ["6. Settle the technology", "7. The readiness gate"],
}
JUMPS = {
    "SKILL.md": [r"Where the readiness check reports a finding at this step, in the run `technology\.md` gives or handed back by `settle-technology`, read `readiness_gate\.md` beside this skill: the finding goes where its 7\.1 sends it",
                 r"Read `readiness_gate\.md` beside this skill unless step 6 had you read it"],
    "readiness_gate.md": [r"step 5 \(`find_entries\.md` beside this file\)", r"step 6 \(`technology\.md` beside\s+this file\)",
                r"step 4\s+\(`rounds\.md` beside this file\)",
                r"In a turn dispatched through a refinement conversation path, `delegated_mode\.md` beside this file"],
    "existing_definition.md": [r"step 5 \(`find_entries\.md` beside this file\)",
                               r"step 6 \(`technology\.md` beside this file\) is",
                               r"step 7 \(`readiness_gate\.md` beside this file\) again",
                               r"go on at step 6\s+\(`technology\.md` beside this file\)"],
}
POINTER = re.compile(r"`([\w]+\.md)` beside this (?:skill|file)")


def text(name):
    with open(os.path.join(DIR, name), encoding="utf-8") as f:
        return f.read()


def by_heading(t):
    out, cur = {}, None
    for ln in t.split(NL):
        if ln.startswith("## "):
            cur = ln[3:].strip()
            out[cur] = ""
        elif cur:
            out[cur] += ln + NL
    return out


def main():
    errors = []
    files = sorted(f for f in os.listdir(DIR) if f.endswith(".md"))
    for f in files:
        for n in POINTER.findall(text(f)):
            if n not in files:
                errors.append("%s names %s, which does not exist" % (f, n))
    sections = by_heading(text("SKILL.md"))
    for f in files:
        if f == "SKILL.md":
            continue
        want = EXPECTED.get(f)
        if want is None:
            errors.append("%s has no expected place" % f)
            continue
        where = sorted(h for h, body in sections.items() if "`%s`" % f in body)
        if where != sorted(want):
            errors.append("%s is named under %s, expected %s" % (f, where, want))
    skill_named = set(POINTER.findall(text("SKILL.md")))
    for f in files:
        if f != "SKILL.md":
            for n in POINTER.findall(text(f)):
                if n not in skill_named:
                    errors.append("%s names %s, which SKILL.md does not name" % (f, n))
    for f, pats in JUMPS.items():
        flat = re.sub(r"\s+", " ", text(f))
        for p in pats:
            if not re.search(p.replace(r"\s+", " "), flat):
                errors.append("%s lacks %s" % (f, p))
    print(len(files), "files;", len(errors), "failures")
    for e in errors:
        print("  ", e)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

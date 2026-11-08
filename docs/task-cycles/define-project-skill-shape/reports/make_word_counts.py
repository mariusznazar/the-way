"""Write word-counts.md beside this script: the words read on the six routes of the task's question 4.

State "before" is commit dfd50e5 (the task's base); state "after" is the worktree. A file's words
are its whitespace-separated tokens, as `wc -w` counts them under a UTF-8 locale; a section is its
heading line to the line before the next heading of the same or a higher level. Prints only ASCII.
verify_counts.py, beside this script, checks the result with counting code of its own.
"""
import os
import re
import subprocess
import sys

REPO = "."
BASE = "dfd50e513c09bebe9d09d74209cd28612565da83"
HERE = os.path.dirname(os.path.abspath(__file__))
NL = chr(10)
SK = "project-level/skill/"
TEMPLATE = "project-level/definition_template.md"
ASKS = 'elements/common/way_of_working.md section "How a skill asks"'
READING = 'elements/common/way_of_working.md section "Reading the foundation"'
CONV = "project-level/lead/conversation_template.md"

ROUTES = [
    ("1. A definition from an idea, steps 0 to 7",
     ["SKILL.md", "idea.md", "read_foundation.md", "first_write.md", "rounds.md",
      "find_entries.md", "technology.md", "readiness_gate.md"],
     [TEMPLATE, ASKS, READING]),
    ("2. A definition resumed while its entries are found, steps 0, 5, 6, 7",
     ["SKILL.md", "existing_definition.md", "find_entries.md", "technology.md", "readiness_gate.md"],
     [TEMPLATE, ASKS]),
    ("3a. A turn lead-project dispatches, the agent reads the delegated mode, step 0 and step 7",
     ["SKILL.md", "delegated_mode.md", "existing_definition.md", "readiness_gate.md"],
     [TEMPLATE, ASKS, CONV]),
    ("3b. A turn lead-project dispatches, the agent reads every file of the skill",
     ["SKILL.md", "delegated_mode.md", "existing_definition.md", "idea.md", "read_foundation.md",
      "first_write.md", "rounds.md", "find_entries.md", "technology.md", "readiness_gate.md"],
     [TEMPLATE, ASKS, CONV]),
    ("4. An entry of an approved definition reopened, not dispatched, steps 0 and 7",
     ["SKILL.md", "existing_definition.md", "readiness_gate.md"],
     [TEMPLATE, ASKS]),
    ("5. A definition with no Technology section reopened, steps 0, 6, 7",
     ["SKILL.md", "existing_definition.md", "technology.md", "readiness_gate.md"],
     [TEMPLATE, ASKS]),
]


def read(path, state):
    if state == "before":
        out = subprocess.run(["git", "-C", REPO, "show", BASE + ":" + path], capture_output=True,
                             check=True).stdout
        return out.decode("utf-8")
    with open(REPO + "/" + path, encoding="utf-8", newline="") as f:
        return f.read()


def section(text, title):
    lines = text.split(NL)
    start = next(i for i, ln in enumerate(lines) if ln.strip() == "## " + title)
    end = len(lines)
    for i in range(start + 1, len(lines)):
        if re.match(r"^#{1,2} ", lines[i]):
            end = i
            break
    return NL.join(lines[start:end])


def words(name, state):
    m = re.match(r'^(.*) section "(.*)"$', name)
    if m:
        return len(section(read(m.group(1), state), m.group(2)).split())
    return len(read(name, state).split())


def c_locale_words(text):
    # coreutils 8.32 `wc -w` in the C locale: a token counts only if it holds a printable ASCII byte.
    return sum(1 for t in text.split() if any(33 <= ord(c) <= 126 for c in t))


def pct(a, b):
    return "%+.1f%%" % (100.0 * (b - a) / a)


def main():
    out = []
    w = out.append
    base_skill = read(SK + "SKILL.md", "before")
    base_lines = base_skill.split(NL)
    total_files = {}
    w("# Word counts of the six routes")
    w("")
    w("Words are counted as `wc -w` counts them under a UTF-8 locale (`LC_ALL=C.UTF-8 wc -w`): the "
      "whitespace-separated tokens of a file, Markdown and frontmatter included. Of a file read by "
      "sections, the sections read count, each from its heading to the line before the next heading "
      "of the same or a higher level. The state \"before\" is commit dfd50e5, where "
      "`project-level/skill/SKILL.md` is the only file of the skill; the state \"after\" is the "
      "worktree after the last change of a counted file. Every file read beside the skill is the "
      "same in both states. `verify_counts.py` beside this file recounts every figure below and in "
      "the other reports with counting code of its own.")
    w("")
    w("Rules of the count:")
    w("")
    w("- Skill text is `SKILL.md` and the files beside it that the route reads. Read beside the skill "
      "is what question 4 lists: `project-level/definition_template.md` whole (step 0, every route), "
      "the section \"How a skill asks\" of `elements/common/way_of_working.md` (step 0, every route), "
      "its section \"Reading the foundation\" (step 2, route 1 only) and "
      "`project-level/lead/conversation_template.md` (routes 3a and 3b). The files of the skills the "
      "route calls, the definition and the product's files are outside the count.")
    w("- The state \"before\" has one file for the skill, read whole on every route, so its skill "
      "text is the same on every route.")
    w("- Route 3a counts `existing_definition.md`: a dispatched turn always works on a definition its "
      "conversation file names, and step 0 has that case read the file. The edit itself is counted "
      "as question 4 gives route 3a, with no file of another step.")
    w("- Route 1 reads neither `existing_definition.md` (no definition is named) nor "
      "`delegated_mode.md` (no turn is dispatched).")
    w("- Routes 2, 4 and 5 read `existing_definition.md` at step 0 and then the files of the steps "
      "they go on to: route 2 steps 5, 6 and 7; route 4 step 7; route 5 steps 6 and 7.")
    w("- `readiness_gate.md` counts once on every route. On routes 1, 2 and 5, which pass step 6, a finding of "
      "the readiness check at step 6 has it read there, and step 7 does not read it again; without "
      "a finding it is read at step 7. Either way the route reads it once.")
    w("")
    w("## The count of the base, and the task's figure")
    w("")
    utf = len(base_skill.split())
    c = c_locale_words(base_skill)
    tmpl = read(TEMPLATE, "before")
    w("- `project-level/skill/SKILL.md` on the base: %d words under a UTF-8 locale, %d words with "
      "`wc -w` in the C locale, which the Git Bash of this cycle uses while `LANG` is unset. The task's "
      "figure is the first. The %d words between them are standalone em dashes: coreutils 8.32 in "
      "the C locale counts no token without a printable ASCII byte, and the file holds %d em dashes, "
      "%d of them standing alone." % (utf, c, utf - c, base_skill.count(chr(8212)),
                                      sum(1 for t in base_skill.split() if t == chr(8212))))
    w("- `project-level/definition_template.md`: %d words under a UTF-8 locale (the task's figure), "
      "%d in the C locale." % (len(tmpl.split()), c_locale_words(tmpl)))
    w("- The fragments the task's Need names, on the base:")
    for a, b in [(25, 51), (73, 125), (145, 183)]:
        w("  - lines %d-%d: %d" % (a, b, len(NL.join(base_lines[a - 1:b]).split())))
    w("- Quoted in the proposals of `assessment.md` (proposal 1, removed from `delegated_mode.md` by "
      "correction 1):")
    p1 = ("The project orchestrator may make the initial text edit only when that full text is "
          "already before it and needs no other definition-section or foundation reading; otherwise "
          "it delegates the edit.")
    assert p1 in " ".join(read(SK + "SKILL.md", "before").split())
    assert p1 not in " ".join(read(SK + "delegated_mode.md", "after").split())
    w('  - in %s before: "%s": %d' % (SK + "SKILL.md", p1, len(p1.split())))
    w("")
    w("## The files")
    w("")
    w("### Before")
    w("")
    w("  - %s: %d" % (SK + "SKILL.md", words(SK + "SKILL.md", "before")))
    w("")
    w("### After")
    w("")
    names = ["SKILL.md", "delegated_mode.md", "existing_definition.md", "idea.md", "read_foundation.md",
             "first_write.md", "rounds.md", "find_entries.md", "technology.md", "readiness_gate.md"]
    for n in names:
        w("  - %s: %d" % (SK + n, words(SK + n, "after")))
    all_after = sum(words(SK + n, "after") for n in names)
    w("")
    w("All ten files of the skill after: %d words." % all_after)
    w("")
    w("### Read beside the skill, the same in both states")
    w("")
    for n in [TEMPLATE, ASKS, READING, CONV]:
        w("  - %s: %d" % (n, words(n, "before")))
        assert words(n, "before") == words(n, "after"), n
    w("")
    summary = []
    for title, files, beside in ROUTES:
        w("## " + title)
        w("")
        for state in ("before", "after"):
            w("### " + state.capitalize())
            w("")
            sk = [SK + "SKILL.md"] if state == "before" else [SK + f for f in files]
            ns = sum(words(f, state) for f in sk)
            w("Skill text, %d words:" % ns)
            w("")
            for f in sk:
                w("  - %s: %d" % (f, words(f, state)))
            w("")
            nb = sum(words(f, state) for f in beside)
            w("Read beside the skill, %d words:" % nb)
            w("")
            for f in beside:
                w("  - %s: %d" % (f, words(f, state)))
            w("")
            w("Total of the route: %d words." % (ns + nb))
            w("")
            total_files[(title, state)] = (ns, ns + nb)
        b, a = total_files[(title, "before")], total_files[(title, "after")]
        summary.append("| %s | %d | %d | %d | %d | %s | %s |" % (
            title.split(" ", 1)[0].rstrip("."), b[0], b[1], a[0], a[1], pct(b[0], a[0]), pct(b[1], a[1])))
    w("## Summary")
    w("")
    w("| Route | Skill text before | Total before | Skill text after | Total after | Change of the skill text | Change of the total |")
    w("|---|---|---|---|---|---|---|")
    for row in summary:
        w(row)
    w("")
    w("## The six recorded runs")
    w("")
    w("The task's Context records six runs of the skill: one definition from an idea (route 1), four "
      "turns lead-project dispatched (route 3a or 3b) and one entry of an approved definition reopened "
      "(route 4). Summed over the six, each dispatched turn counted once by route 3a and once by 3b:")
    w("")
    w("| Reading of the dispatched turns | Skill text before | Total before | Skill text after | Total after | Change of the skill text | Change of the total |")
    w("|---|---|---|---|---|---|---|")
    r1 = ROUTES[0][0]
    r4 = ROUTES[4][0]
    for key in ("3a", "3b"):
        rk = next(t for t, _, _ in ROUTES if t.startswith(key + "."))
        sb = total_files[(r1, "before")][0] + 4 * total_files[(rk, "before")][0] + total_files[(r4, "before")][0]
        tb = total_files[(r1, "before")][1] + 4 * total_files[(rk, "before")][1] + total_files[(r4, "before")][1]
        sa = total_files[(r1, "after")][0] + 4 * total_files[(rk, "after")][0] + total_files[(r4, "after")][0]
        ta = total_files[(r1, "after")][1] + 4 * total_files[(rk, "after")][1] + total_files[(r4, "after")][1]
        w("| %s | %d | %d | %d | %d | %s | %s |" % (key, sb, tb, sa, ta, pct(sb, sa), pct(tb, ta)))
    w("")
    w("## Against the task's estimates")
    w("")
    sk_after = words(SK + "SKILL.md", "after")
    w("The task's question 1 estimated the rebuilt skill text by route. Counted, against those "
      "estimates (quoted in brackets, not recounted):")
    w("")
    w("- `SKILL.md` alone: %d words [task: 500-600 words]." % sk_after)
    w("- Route 3a, a dispatched turn reading its own steps: %d words [task: 1550-1750 words]."
      % total_files[(ROUTES[2][0], "after")][0])
    w("- Route 4, an approved definition reopened: %d words [task: 1250-1400 words]."
      % total_files[(ROUTES[4][0], "after")][0])
    w("- Route 1, a definition from an idea: %d words [task: 2350-2550 words]. Only this figure falls "
      "outside its estimate, which matches no route counted here, and route 3b, every file of "
      "the skill, gives %d words." % (total_files[(ROUTES[0][0], "after")][0],
                                      total_files[(ROUTES[3][0], "after")][0]))
    w("")
    with open(os.path.join(HERE, "word-counts.md"), "w", encoding="utf-8", newline=NL) as f:
        f.write(NL.join(out))
    print("written")
    return 0


if __name__ == "__main__":
    sys.exit(main())

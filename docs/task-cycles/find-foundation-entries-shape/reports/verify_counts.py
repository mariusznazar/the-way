#!/usr/bin/env python3
"""Counts and checks for the find-foundation-entries rebuild (task To do 3-5, question 4).

Usage, from anywhere:

    python -I -B verify_counts.py --write   # write word-counts.md from the files as they stand
    python -I -B verify_counts.py           # check every number and the assessment table

Words are counted as `wc -w` counts them: runs of non-blank characters. The "before" state is read
from git at BASE (the file is identical at dfd50e5, the task's base; the check proves it), the
"after" state from the working tree, which must be committed and clean in elements/common/skill/.

The check compares with the files every number the request will state:
  - word-counts.md must equal what this script renders;
  - the counts block between the markers in author.md must equal the rendered block;
  - each number-bearing sentence of the proposals in assessment.md (render_proposals) must stand
    in assessment.md verbatim;
  - the numbers the task states (1584, 1752, 424, 674, 419) must equal the computed ones;
  - assessment.md: every nonblank line of the base file lies in exactly one row, each quoted
    fragment equals its lines joined by one space, each Words cell equals the count of its quote,
    the words of the rows add up to the whole base file, and each place after exists.
Exit code 0 when everything holds, 1 otherwise. Only ASCII goes to stdout.
"""
import pathlib
import re
import shutil
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BASE = "f447bb6"
TASK_BASE = "dfd50e5"
SKILL_DIR = "elements/common/skill"
SKILL_FILES = ["SKILL.md", "read.md", "build_table.md", "definition_variant.md", "task_variant.md"]
BASE_SKILL = SKILL_DIR + "/SKILL.md"
WOW = "elements/common/way_of_working.md"
PROJECTED = "elements/common/projected_mode.md"
DEF_TEMPLATE = "project-level/definition_template.md"
TASK_TEMPLATE = "project-level/task/template.md"
COUNTED_UNCHANGED = [WOW, PROJECTED, DEF_TEMPLATE, TASK_TEMPLATE]
TASK_STATED = 424
MARK_BEGIN ="<!-- counts:begin -->"
MARK_END = "<!-- counts:end -->"


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT)] + list(args), check=True,
                          capture_output=True).stdout


def base_text(path):
    return git("show", BASE + ":" + path).decode("utf8")


def tree_text(path):
    return (ROOT / path).read_bytes().decode("utf8")


def wc(text):
    return len(text.split())


def wc_tool(text):
    """`wc -w` itself, when the tool exists; None otherwise."""
    exe = shutil.which("wc")
    if not exe:
        return None
    out = subprocess.run([exe, "-w"], input=text.encode("utf8"), capture_output=True).stdout
    return int(out.split()[0])


def section(text, heading):
    """A `## heading` section: the heading line to the line before the next `## `."""
    lines = text.split("\n")
    start = None
    for i, line in enumerate(lines):
        if line.strip() == "## " + heading:
            start = i
        elif start is not None and line.startswith("## "):
            return "\n".join(lines[start:i])
    if start is None:
        raise SystemExit("FAIL no section " + heading)
    return "\n".join(lines[start:])


def task_template_section(text):
    """The section "Settlements to record" and its rule under "What each section carries"."""
    sec = section(text, "Settlements to record")
    lines = text.split("\n")
    start = next(i for i, l in enumerate(lines) if l.startswith("- **Settlements to record:**"))
    end = next(i for i in range(start + 1, len(lines)) if lines[i].startswith("- **Out of scope:**"))
    return sec + "\n" + "\n".join(lines[start:end])


def definition_template_section(text):
    """`## Projected foundation changes` as the task gives it: lines 260-348."""
    lines = text.split("\n")
    assert lines[259] == "## Projected foundation changes", lines[259]
    assert lines[348] == "## Gate record", lines[348]
    return "\n".join(lines[259:348])


def compute():
    d = {}
    base_skill = base_text(BASE_SKILL)
    wow = base_text(WOW)
    d["base_skill"] = wc(base_skill)
    d["wow"] = wc(wow)
    d["projected"] = wc(base_text(PROJECTED))
    d["def_section"] = wc(definition_template_section(base_text(DEF_TEMPLATE)))
    d["task_section"] = wc(task_template_section(base_text(TASK_TEMPLATE)))
    d["task_range_181_208"] = wc("\n".join(base_text(TASK_TEMPLATE).split("\n")[180:208]))
    d["task_section_heading"] = wc(section(base_text(TASK_TEMPLATE), "Settlements to record"))
    d["wow_ask"] = wc(section(wow, "How a skill asks"))
    d["wow_read"] = wc(section(wow, "Reading the foundation"))
    d["wow_critique"] = wc(section(wow, "Critique before collective review"))
    d["wow_three"] = d["wow_ask"] + d["wow_read"] + d["wow_critique"]
    for f in SKILL_FILES:
        d["after_" + f] = wc(tree_text(SKILL_DIR + "/" + f))
    a = d
    d["after_total"] = sum(a["after_" + f] for f in SKILL_FILES)
    # the skill text read on each route
    common = a["after_SKILL.md"] + a["after_read.md"] + a["after_build_table.md"]
    d["task_after_1"] = common + a["after_task_variant.md"]
    d["def_after_1"] = common + a["after_definition_variant.md"]
    d["task_after_2"] = d["task_after_1"] + d["wow"] + d["task_section"]
    d["def_after_2"] = d["def_after_1"] + d["wow"] + d["def_section"] + d["projected"]
    d["task_after_3"] = d["task_after_1"] + d["wow"] - d["wow_ask"] - d["wow_read"]
    d["task_before_1"] = d["base_skill"]
    d["def_before_1"] = d["base_skill"]
    d["task_before_2"] = d["base_skill"] + d["wow"] + d["task_section"]
    d["def_before_2"] = d["base_skill"] + d["wow"] + d["def_section"] + d["projected"]
    d["task_before_3"] = d["base_skill"] + d["wow"] - d["wow_ask"] - d["wow_read"]
    # the sentence of the intro that names future callers (proposal 3)
    m = re.search(r"This skill\nserves a project definition.*?\(WAY-115, WAY-134\)\.", base_skill, re.S)
    d["future_sentence"] = wc(m.group(0))
    # proposal 1: three sections of way_of_working.md instead of the whole file
    d["p1_task_2"] = d["task_after_1"] + d["wow_three"] + d["task_section"]
    d["p1_task_3"] = d["task_after_1"] + d["wow_critique"]
    d["p1_saved_2"] = d["task_after_2"] - d["p1_task_2"]
    d["p1_saved_3"] = d["task_after_3"] - d["p1_task_3"]
    return d


def pct(after, before):
    p = round((after - before) * 100.0 / before)
    return ("+" if p > 0 else "-" if p < 0 else "") + str(abs(p)) + "%"


def render_counts(d):
    L = []
    L.append("| Route and sum | Before (base) | After | Change |")
    L.append("|---|---|---|---|")
    rows = [
        ("Task mode, sum 1: the skill's own text read on the route", "task_before_1", "task_after_1"),
        ("Task mode, sum 2: sum 1 with the files read beside it (`way_of_working.md`, the task template section)", "task_before_2", "task_after_2"),
        ("Task mode, sum 3: sum 2 without what step 1 of `refine-task` read earlier (the whole task template, \"How a skill asks\", \"Reading the foundation\")", "task_before_3", "task_after_3"),
        ("Project definition, sum 1: the skill's own text read on the route", "def_before_1", "def_after_1"),
        ("Project definition, sum 2: sum 1 with the files read beside it (`way_of_working.md`, the definition template section, `projected_mode.md`)", "def_before_2", "def_after_2"),
    ]
    for label, b, a in rows:
        L.append("| %s | %d | %d | %s |" % (label, d[b], d[a], pct(d[a], d[b])))
    L.append("")
    L.append("Files after the rebuild: " + ", ".join(
        "`%s` %d" % (f, d["after_" + f]) for f in SKILL_FILES) + "; together %d words (base `SKILL.md`: %d)."
        % (d["after_total"], d["base_skill"]))
    L.append("")
    L.append("Files read beside the skill, unchanged: `way_of_working.md` %d; its sections \"How a skill asks\" %d "
             "and \"Reading the foundation\" %d; the task template section \"Settlements to record\" with its rule %d; "
             "the definition template section \"Projected foundation changes\" %d; `projected_mode.md` %d."
             % (d["wow"], d["wow_ask"], d["wow_read"], d["task_section"], d["def_section"], d["projected"]))
    return "\n".join(L)


def render_proposals(d):
    return {
        "p1": ("Reading only the three sections would cost %d words of `way_of_working.md` instead of %d "
               "(\"Critique before collective review\" %d, \"How a skill asks\" %d, \"Reading the foundation\" %d). "
               "On task-mode sum 2 that is %d fewer words (%d instead of %d); on sum 3, where the sections \"How a skill asks\" "
               "and \"Reading the foundation\" are already excluded, %d fewer (%d instead of %d)."
               % (d["wow_three"], d["wow"], d["wow_critique"], d["wow_ask"], d["wow_read"],
                  d["p1_saved_2"], d["p1_task_2"], d["task_after_2"],
                  d["p1_saved_3"], d["p1_task_3"], d["task_after_3"])),
        "p3": ("The sentence has %d words, carried on every route of both variants." % d["future_sentence"]),
        "p4": ("In the rare run in which the human accepts no row, `projected_mode.md` would not be read at all, "
               "%d words saved; in every other run of the definition variant it is read once, as now." % d["projected"]),
    }


def render_wordcounts(d):
    head = ["# Word counts - find-foundation-entries rebuild", "",
            "Made by `verify_counts.py --write` from the files at commit %s of the task branch, counted as `wc -w`. "
            "Before: the base %s (the file is identical at %s). The counts hold only for those files; "
            "`verify_counts.py` without an argument checks every number the request states." % (last_commit(), BASE, TASK_BASE),
            ""]
    note = ["", "The task document states %d words for the task template's section \"Settlements to record\" with its rule. "
            "Counted by what an agent reads - the section's own lines 80-87 (%d words) and the rule's bullet under "
            "\"What each section carries\" - the sum is %d. The task's figure equals lines 181-208 of "
            "`project-level/task/template.md` (%d words): the rule's bullet, the bullet \"Out of scope\" and the paragraph "
            "below it, without the section's own lines. This report uses %d."
            % (TASK_STATED, d["task_section_heading"], d["task_section"], d["task_range_181_208"], d["task_section"])]
    return "\n".join(head) + "\n" + render_counts(d) + "\n" + "\n".join(note) + "\n"


def last_commit():
    return git("log", "-1", "--format=%h", "--", SKILL_DIR).decode().strip()


def parse_assessment(text):
    rows = []
    for line in text.split("\n"):
        if not re.match(r"^\| \d+ \| L\d", line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
        rows.append(cells)
    return rows


def check_assessment(path, fail):
    text = path.read_text(encoding="utf8")
    base = base_text(BASE_SKILL).split("\n")
    nonblank = {i + 1 for i, l in enumerate(base) if l.strip()}
    seen = {}
    rows = parse_assessment(text)
    if not rows:
        fail("assessment.md holds no row")
        return
    total = 0
    for cells in rows:
        if len(cells) != 9:
            fail("row %s has %d cells" % (cells[0], len(cells)))
            continue
        n, rng, quote, words, _when, _rec, _verdict, _reason, place = cells
        m = re.match(r"^L(\d+)(?:-(\d+))?$", rng)
        if not m:
            fail("row %s: lines %r" % (n, rng))
            continue
        a, b = int(m.group(1)), int(m.group(2) or m.group(1))
        lines = [base[i - 1].strip() for i in range(a, b + 1) if base[i - 1].strip()]
        want = " ".join(lines)
        if quote != want:
            fail("row %s: the quoted fragment is not lines %d-%d of the base" % (n, a, b))
        if int(words) != wc(want):
            fail("row %s: Words %s, the quote has %d" % (n, words, wc(want)))
        total += wc(want)
        for i in range(a, b + 1):
            if base[i - 1].strip():
                seen[i] = seen.get(i, 0) + 1
        for f, h in re.findall(r"`([^`]+)` § \"([^\"]+)\"", place):
            p = ROOT / SKILL_DIR / f
            if not p.exists():
                fail("row %s: place %s does not exist" % (n, f))
            elif h != "front matter" and not re.search(r"^#+ " + re.escape(h) + r"\s*$", p.read_text(encoding="utf8"), re.M):
                fail("row %s: no heading %r in %s" % (n, h, f))
        if "§" not in place:
            fail("row %s: no place after" % n)
    for i in sorted(nonblank):
        if seen.get(i, 0) != 1:
            fail("base line %d lies in %d rows" % (i, seen.get(i, 0)))
    if total != wc("\n".join(base)):
        fail("the rows hold %d words, the base file %d" % (total, wc("\n".join(base))))
    return text


def main():
    problems = []

    def fail(msg):
        problems.append(msg)
        print("FAIL " + msg)

    d = compute()
    if "--write" in sys.argv:
        (HERE / "word-counts.md").write_bytes(render_wordcounts(d).encode("utf8"))
        print("written word-counts.md; commit " + last_commit())
        return 0
    # the base is the task's base
    paths = [BASE_SKILL, WOW, PROJECTED, DEF_TEMPLATE, TASK_TEMPLATE]
    r = subprocess.run(["git", "-C", str(ROOT), "diff", "--quiet", TASK_BASE, BASE, "--"] + paths)
    if r.returncode != 0:
        fail("the counted files differ between %s and %s" % (TASK_BASE, BASE))
    # the counted files are committed
    st = git("status", "--porcelain", "--", SKILL_DIR).decode().strip()
    if st:
        fail("elements/common/skill/ is not clean: " + st.replace("\n", "; "))
    for p in COUNTED_UNCHANGED:
        if base_text(p) != tree_text(p):
            fail(p + " changed since the base")
    # python split against wc -w
    for f in SKILL_FILES:
        t = tree_text(SKILL_DIR + "/" + f)
        w = wc_tool(t)
        if w is not None and w != wc(t):
            fail("wc -w and split differ for " + f)
    if wc_tool("a b") is None:
        print("note: wc not found; counted by whitespace split, which is what wc -w does")
    # the numbers the task states
    if d["task_section"] != TASK_STATED:
        if d["task_range_181_208"] == TASK_STATED:
            print("note: the task states 424 for the task template section; that is lines 181-208, the report counts %d"
                  % d["task_section"])
        else:
            fail("task states 424 for the task template section; computed %d, lines 181-208 %d"
                 % (d["task_section"], d["task_range_181_208"]))
    for key, stated in (("base_skill", 1584), ("wow", 1752), ("def_section", 674), ("projected", 419)):
        if d[key] != stated:
            fail("task states %d for %s, computed %d" % (stated, key, d[key]))
    # word-counts.md
    wcp = HERE / "word-counts.md"
    if not wcp.exists() or wcp.read_bytes().decode("utf8") != render_wordcounts(d):
        fail("word-counts.md differs from what the files give")
    # author.md block
    ap = HERE / "author_report.md"
    if ap.exists():
        t = ap.read_text(encoding="utf8")
        if MARK_BEGIN not in t or MARK_END not in t:
            fail("author.md has no counts block")
        else:
            block = t.split(MARK_BEGIN, 1)[1].split(MARK_END, 1)[0].strip("\n")
            if block != render_counts(d):
                fail("the counts block of author.md differs from what the files give")
    else:
        fail("author.md missing")
    # assessment.md
    asp = HERE / "assessment.md"
    if not asp.exists():
        fail("assessment.md missing")
    else:
        text = check_assessment(asp, fail)
        if text is not None:
            for k, s in render_proposals(d).items():
                if s not in text:
                    fail("assessment.md lacks the number sentence of proposal " + k)
    print("%d problem(s)" % len(problems))
    if not problems:
        print("task route %d / %d / %d words; definition route %d / %d words; files after: %d"
              % (d["task_after_1"], d["task_after_2"], d["task_after_3"], d["def_after_1"], d["def_after_2"], d["after_total"]))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())

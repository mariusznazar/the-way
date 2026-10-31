"""Count the words of the seven routes of the task, before and after the rebuild.

Words are whitespace-separated, Markdown and frontmatter included; of a file read by sections,
the sections read (heading to the line before the next heading of the same or a higher level).
Writes the report as UTF-8 Markdown to the path given.
"""
import subprocess
import sys

REPO = "C:/Storage/repos/the-way/.runs/worktrees/testing-skill-shape"
BASE = "00c0a747272a9a179b7a855f256daff985ea2ee1"
SG = "product-guidelines/styleguide/"
NL = chr(10)


def read_worktree(path):
    with open(f"{REPO}/{path}", encoding="utf-8", newline="") as f:
        return f.read()


def read_base(path):
    return subprocess.run(["git", "-C", REPO, "show", f"{BASE}:{path}"],
                          capture_output=True, check=True).stdout.decode("utf-8")


def words(text):
    return len(text.split())


def section(text, heading):
    lines = text.split(NL)
    start = next(i for i, l in enumerate(lines) if l.strip() == heading)
    level = len(heading) - len(heading.lstrip("#"))
    end = len(lines)
    for j in range(start + 1, len(lines)):
        l = lines[j]
        if l.startswith("#") and len(l) - len(l.lstrip("#")) <= level:
            end = j
            break
    return NL.join(lines[start:end])


WOW = "elements/common/way_of_working.md"
CRIT = "elements/common/critique/"


def count(entry, state):
    kind, path = entry[0], entry[1]
    reader = read_base if state == "before" else read_worktree
    if path == SG + "SKILL.md":
        text = reader(path)
    else:
        text = read_worktree(path)
    if kind == "section":
        text = section(text, entry[2])
        return f"{path} section \"{entry[2].lstrip('# ')}\"", words(text)
    return path, words(text)


def F(path):
    return ("file", path)


HAAS = ("section", WOW, "## How a skill asks")
CBCR = ("section", WOW, "## Critique before collective review")
RTF = ("section", WOW, "## Reading the foundation")
FIRST_READS = [F("project-level/task/skill/SKILL.md"), F("project-level/task/template.md"), HAAS,
               RTF]
CRIT_BESIDE = [F(CRIT + "prepare.md"), F(CRIT + "check.md"), F(CRIT + "settle.md")]
CRIT_SKILL = F(CRIT + "SKILL.md")

STEP0 = [F(SG + "template.md"), F("product-guidelines/template.md"),
         F("project-level/task/skill/SKILL.md"), F("project-level/task/template.md"),
         HAAS, RTF, CBCR, CRIT_SKILL]

# Each route: (title, note, before_to_step4, before_total_extra, after_to_step4, after_total_extra)
ROUTES = {}


def before(research, ends_at_1=False):
    to4 = FIRST_READS + [F(SG + "SKILL.md")] + STEP0
    extra = []
    if ends_at_1:
        return to4, extra
    if research:
        to4 = to4 + CRIT_BESIDE
    else:
        extra = CRIT_BESIDE
    return to4, extra


def after(research, audit, orchestrated=False, ends_at_1=False):
    to4 = FIRST_READS + [F(SG + "SKILL.md")]
    if orchestrated:
        to4 = to4 + [F(SG + "orchestrated_mode.md")]
    to4 = to4 + [F(SG + "recognize.md")]
    if ends_at_1:
        return to4, []
    to4 = to4 + [F(SG + "template.md"), F(SG + "starting_rules.md")]
    extra = []
    if research:
        to4 = to4 + [F(SG + "research.md"), CRIT_SKILL] + CRIT_BESIDE
    if audit:
        to4 = to4 + [F(SG + "audit.md")]
    extra = [F("product-guidelines/template.md"), F(SG + "settle.md"), F(SG + "task_document.md"),
             CBCR]
    if not research:
        extra = extra + [CRIT_SKILL] + CRIT_BESIDE
    extra = extra + [F(SG + "hand_back.md")]
    return to4, extra


ROUTE_DEFS = [
    ("1. First styleguide, no screens, human without a preference",
     "research runs, no audit", dict(research=True, audit=False)),
    ("2. First styleguide, no screens, human with a preference",
     "no research, no audit", dict(research=False, audit=False)),
    ("3. First styleguide, there are screens",
     "counted with a human without a preference, so research and audit both run",
     dict(research=True, audit=True)),
    ("4. Refresh, screens unchanged",
     "no research (a refresh), no audit (screens unchanged)", dict(research=False, audit=False)),
    ("5. Extension, screens changed",
     "research runs (every extension), audit runs", dict(research=True, audit=True)),
    ("6. Orchestrated mode on route 1",
     "route 1 with the orchestrated mode; the refiner requests research and critiques from the "
     "orchestrator, and the files it reads are counted as on route 1",
     dict(research=True, audit=False, orchestrated=True)),
    ("7. Product without a user interface, ends at step 1",
     "nothing after step 1 is read", dict(research=False, audit=False, ends_at_1=True)),
]


def table(entries, state):
    rows, total = [], 0
    for e in entries:
        name, n = count(e, state)
        rows.append((name, n))
        total += n
    return rows, total


def fmt_rows(rows):
    return NL.join(f"  - {name}: {n}" for name, n in rows)


def main(out):
    out_lines = []
    summary = []
    first_reads_n = {s: sum(count(e, s)[1] for e in FIRST_READS) for s in ("before", "after")}
    for title, note, kw in ROUTE_DEFS:
        ends = kw.get("ends_at_1", False)
        b4, bx = before(kw["research"], ends)
        a4, ax = after(kw["research"], kw["audit"], kw.get("orchestrated", False), ends)
        res = {}
        for state, to4, extra in (("before", b4, bx), ("after", a4, ax)):
            r4, t4 = table(to4, state)
            rx, tx = table(extra, state)
            res[state] = (r4, t4, rx, t4 + tx)
        fr = first_reads_n["before"]  # the first reads are the same files in both states
        out_lines.append(f"## {title}")
        out_lines.append("")
        out_lines.append(f"Route: {note}.")
        out_lines.append("")
        for state in ("before", "after"):
            r4, t4, rx, tot = res[state]
            out_lines.append(f"### {state.capitalize()}")
            out_lines.append("")
            out_lines.append(f"Read before step 4 (files in the order read), {t4} words:")
            out_lines.append("")
            out_lines.append(fmt_rows(r4))
            out_lines.append("")
            if rx:
                out_lines.append(f"Read from step 4 to the end, {tot - t4} words:")
                out_lines.append("")
                out_lines.append(fmt_rows(rx))
                out_lines.append("")
            elif not ends:
                out_lines.append("Read from step 4 to the end: nothing beyond the files above.")
                out_lines.append("")
            out_lines.append(f"Total at the end of the run: {tot} words. Without the first reads "
                             f"of refine-task ({fr} words): before step 4 {t4 - fr}, total {tot - fr}.")
            out_lines.append("")
        summary.append((title, res, fr))
    head = []
    head.append("# Word counts of the seven routes")
    head.append("")
    head.append("Method. Words are whitespace-separated, Markdown and frontmatter included; of a "
                "file read by sections, the sections read. Figures are from the worktree "
                "(after) and from commit 525cde1 for the base `SKILL.md` (before).")
    head.append("")
    head.append("Rules of the count:")
    head.append("")
    head.append("- Every read of the route counts, in both states. The first reads of refine-task "
                "are the first reading of the files that the base skill's step 0 makes the "
                "session read again: `project-level/task/skill/SKILL.md`, "
                "`project-level/task/template.md` and the sections \"How a skill asks\" and "
                "\"Reading the foundation\" of "
                f"`elements/common/way_of_working.md` ({first_reads_n['before']} words together). They count in "
                "both states; in the before state the second reading counts again (a file read "
                "twice counts twice, task question 3); in the after state the second reading is "
                "gone. The last column of the summary leaves the first reads out, for comparison "
                "with the task's estimate (about 8850 before and 5900 after, which counted "
                "`SKILL.md` and the files of step 0 only, and not the section \"Reading the "
                "foundation\" of `way_of_working.md` that step 0 reads a second time: this is why "
                "the before figure stands about 490 words above the estimate).")
    head.append("- Other files refine-task reads (`read_sources.md`, `draft.md`, "
                "`product-guidelines/reading.md` and so on) are the same in both states and are "
                "left out; this is the cycle's rule: the files refine-task sends the session to are "
                "equal in both states and stay out of the counts. Where the session started on route 6, refine-task's own "
                "`orchestrated_mode.md` and `project_plan_task.md` are likewise equal in both "
                "states and left out.")
    head.append("- A file a counted file sends the session to on the route counts in both "
                "states: the files beside `elements/common/critique/SKILL.md` (`prepare.md`, "
                "`check.md`, `settle.md`), read once on the route by the author who runs and "
                "settles the critique, at the first critique (step 2 where research ran, else "
                "step 4); a later critique of the same session does not read them again. The "
                "critic's own reading is another agent's context and is not counted.")
    head.append("- \"Before step 4\" is the text read before step 4 begins; \"total\" is the sum at "
                "the end of the run. In the before state step 0 reads everything at the start, "
                "also on route 7, where the run ends at step 1.")
    head.append("- Route 3 is counted with a human without a preference, so research and audit "
                "both run. Route 5 is an extension with changed screens, so research and audit "
                "both run; its figures equal route 3.")
    head.append("- The product's own files (its root `AGENTS.md`, `guidelines/`) and the entries "
                "of its foundation differ by product and are left out of both states. Conditional "
                "files read only on a condition the routes do not name — `new_tools.md` (a new "
                "tool left as a technology question) and `staged_cleaning.md` (the human chooses "
                "to clean the screens as tasks touch their styles) — are not read on any route "
                "here; their words come on top where the condition holds.")
    head.append("")
    head.append("## Summary")
    head.append("")
    head.append("| Route | Before: to step 4 | Before: total | After: to step 4 | After: total | "
                "Before without first reads (to 4 / total) | After without first reads (to 4 / total) |")
    head.append("|---|---|---|---|---|---|---|")
    for title, res, fr in summary:
        b, a = res["before"], res["after"]
        head.append(f"| {title} | {b[1]} | {b[3]} | {a[1]} | {a[3]} | {b[1]-fr} / {b[3]-fr} | "
                    f"{a[1]-fr} / {a[3]-fr} |")
    head.append("")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(NL.join(head + out_lines) + NL)
    for title, res, fr in summary:
        print(title[:2], res["before"][1], res["before"][3], res["after"][1], res["after"][3],
              res["before"][1] - fr, res["after"][1] - fr)


if __name__ == "__main__":
    main(sys.argv[1])

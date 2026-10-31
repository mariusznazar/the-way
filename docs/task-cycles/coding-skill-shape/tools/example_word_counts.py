"""Count the words of the six routes of the task, before and after the rebuild.

Words are whitespace-separated (as wc -w), Markdown and frontmatter included; of a file read by
sections, the sections read. The state "before" is commit 00c0a74 for product-guidelines/testing/
SKILL.md; every other file counted is the same in both states except the new files beside the skill.
Writes the report as UTF-8 Markdown to the path given.
"""
import subprocess
import sys

REPO = "C:/Storage/repos/the-way/.runs/worktrees/testing-skill-shape"
BASE = "00c0a747272a9a179b7a855f256daff985ea2ee1"
T = "product-guidelines/testing/"
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


def count(entry, state):
    kind, path = entry[0], entry[1]
    if path == T + "SKILL.md" and state == "before":
        text = read_base(path)
    else:
        text = read_worktree(path)
    if kind == "section":
        text = section(text, entry[2])
        return f"{path} section \"{entry[2].lstrip('# ')}\"", words(text)
    return path, words(text)


def F(path):
    return ("file", path)


WOW = "elements/common/way_of_working.md"
CRIT = "elements/common/critique/"
HAAS = ("section", WOW, "## How a skill asks")
CBCR = ("section", WOW, "## Critique before collective review")
RTF = ("section", WOW, "## Reading the foundation")
FIRST_READS = [F("project-level/task/skill/SKILL.md"), F("project-level/task/template.md"), HAAS, RTF]
CRIT_BESIDE = [F(CRIT + "prepare.md"), F(CRIT + "check.md"), F(CRIT + "settle.md")]
CRIT_SKILL = F(CRIT + "SKILL.md")
GEN_TEMPLATE = F("product-guidelines/template.md")
TEST_TEMPLATE = F(T + "template.md")

# Step 0 of the base skill reads, at the start of every run:
STEP0 = [GEN_TEMPLATE, TEST_TEMPLATE, F("project-level/task/skill/SKILL.md"),
         F("project-level/task/template.md"), HAAS, RTF, CBCR, CRIT_SKILL]


def before(research):
    to4 = FIRST_READS + [F(T + "SKILL.md")] + STEP0
    extra = []
    if research:
        to4 = to4 + CRIT_BESIDE
    else:
        extra = CRIT_BESIDE
    return to4, extra


def after(research, audit, new_level, orchestrated=False, step2=True):
    to4 = FIRST_READS + [F(T + "SKILL.md")]
    if orchestrated:
        to4 = to4 + [F(T + "orchestrated_mode.md")]
    to4 = to4 + [F(T + "recognize.md")]
    template_read = False
    if step2:
        to4 = to4 + [TEST_TEMPLATE, F(T + "starting_set.md")]
        template_read = True
        if research:
            to4 = to4 + [F(T + "research.md"), CRIT_SKILL] + CRIT_BESIDE
    if audit or new_level:
        if not template_read:
            to4 = to4 + [TEST_TEMPLATE]
        if audit:
            to4 = to4 + [F(T + "audit.md")]
        if new_level:
            to4 = to4 + [F(T + "new_level.md")]
    extra = [GEN_TEMPLATE, F(T + "settle.md"), F(T + "task_document.md"), CBCR]
    if not research:
        extra = extra + [CRIT_SKILL] + CRIT_BESIDE
    extra = extra + [F(T + "hand_back.md")]
    return to4, extra


ROUTE_DEFS = [
    ("1. First guidelines, no tests, human without a preference",
     "steps 0-2, 4, 5 run; step 2 runs research and the critique of its reports; no step 3 (no tests, "
     "no new level); the critique of step 4 runs",
     dict(research=True, audit=False, new_level=False)),
    ("2. First guidelines, no tests, human with a preference",
     "steps 0-2, 4, 5 run; step 2 runs no research (the human has a preference); no step 3; the "
     "critique of step 4 runs, and it is the first critique of the session",
     dict(research=False, audit=False, new_level=False)),
    ("3. Tests and no guidelines, no preference; also an extension",
     "steps 0-5 run; step 2 runs research and the critique of its reports (no preference, or every "
     "extension); the audit of step 3 runs (the product has tests); no new level; the critique of "
     "step 4 runs",
     dict(research=True, audit=True, new_level=False)),
    ("4. Refresh",
     "steps 0-5 run; step 2 runs no research (a refresh); the audit of step 3 runs (it audits each "
     "level again); no new level; the critique of step 4 runs, and it is the first critique of the "
     "session",
     dict(research=False, audit=True, new_level=False)),
    ("5. \"A new level\", recipe already standing, no step 2",
     "steps 0, 1, 3 (the new-level case only, no audit), 4, 5 run; no step 2, so no research; the "
     "critique of step 4 runs, and it is the first critique of the session",
     dict(research=False, audit=False, new_level=True, step2=False)),
    ("6. Orchestrated mode on route 1",
     "route 1 with orchestrated mode: the refiner reads orchestrated_mode.md and requests research "
     "and critiques from the orchestrator; the files it reads are counted as on route 1 plus "
     "orchestrated_mode.md",
     dict(research=True, audit=False, new_level=False, orchestrated=True)),
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
    out_lines, summary = [], []
    fr = sum(count(e, "before")[1] for e in FIRST_READS)
    for title, note, kw in ROUTE_DEFS:
        b4, bx = before(kw["research"])
        a4, ax = after(**kw)
        res = {}
        for state, to4, extra in (("before", b4, bx), ("after", a4, ax)):
            r4, t4 = table(to4, state)
            rx, tx = table(extra, state)
            res[state] = (r4, t4, rx, t4 + tx, tx)
        out_lines += [f"## {title}", "", f"Reading counted: {note}.", ""]
        for state in ("before", "after"):
            r4, t4, rx, tot, tx = res[state]
            out_lines += [f"### {state.capitalize()}", "",
                          f"Read before step 4 (files in the order read), {t4} words:", "",
                          fmt_rows(r4), ""]
            if rx:
                out_lines += [f"Read from step 4 to the end, {tx} words:", "", fmt_rows(rx), ""]
            out_lines += [f"Total at the end of the run: {tot} words. Without the first reading in "
                          f"`refine-task` ({fr} words): before step 4 {t4 - fr}, total {tot - fr}.", ""]
        summary.append((title, res))
    head = ["# Word counts of the six routes", "",
            "Words are counted as `wc -w` counts them (whitespace-separated), Markdown and "
            "frontmatter included; of a file read by sections, the sections read (heading to the "
            "line before the next heading of the same or a higher level). Figures come from the "
            "worktree (state \"after\") and from commit 00c0a74 for `product-guidelines/testing/"
            "SKILL.md` (state \"before\"); every other file counted is identical in both states, "
            "except the files new beside the skill.", "",
            "Rules of the count:", "",
            f"- The first reading in `refine-task` is the files that step 0 of the base skill makes "
            f"the session read a second time: `project-level/task/skill/SKILL.md`, "
            f"`project-level/task/template.md`, and the sections \"How a skill asks\" and \"Reading "
            f"the foundation\" of `{WOW}` ({fr} words together; the task's figure of 2835 words is "
            f"the same). They count in both states; in state \"before\" the second reading counts "
            f"again (a file read twice counts twice); in state \"after\" it is gone.",
            "- Other files `refine-task` reads (`read_sources.md`, `draft.md`, "
            "`product-guidelines/reading.md`, and so on) are the same in both states and stay out; "
            "where the session starts on route 6, `refine-task`'s own `orchestrated_mode.md` is "
            "equally the same in both and stays out.",
            "- A file a counted file sends the session to on the route counts in both states: the "
            "files beside `elements/common/critique/SKILL.md` (`prepare.md`, `check.md`, "
            "`settle.md`; 509 words) are read once, at the first critique of the session (step 2 "
            "where research ran, else step 4); a later critique does not read them again. The "
            "critic's own reading is another agent's context and is not counted.",
            "- \"Before step 4\" is the text read before step 4 begins; the total is the sum at the "
            "end of the run, the file of the last step included.",
            "- The product's own files (its root `AGENTS.md`, `guidelines/`) and the entries of "
            "its foundation differ by product and stay out of both states. The conditional files "
            "`new_tools.md` (a new tool left as a technology question) are read on none of these "
            "routes, and their words come on top where the condition holds.",
            "- In state \"before\", step 0 reads at the start of every run, whatever the route: "
            "both templates, the task skill and template, the two sections of the way of working "
            "and `critique/SKILL.md`.",
            "- Route 3 counts a human without a preference (research runs); an extension also runs "
            "research and the audit, so its figures equal route 3.", "",
            "## Summary", "",
            "| Route | Before: to step 4 | Before: total | After: to step 4 | After: total | "
            "Before without the first reading (to step 4 / total) | After without the first reading "
            "(to step 4 / total) | Change of the total |",
            "|---|---|---|---|---|---|---|---|"]
    for title, res in summary:
        b, a = res["before"], res["after"]
        head.append(f"| {title} | {b[1]} | {b[3]} | {a[1]} | {a[3]} | {b[1]-fr} / {b[3]-fr} | "
                    f"{a[1]-fr} / {a[3]-fr} | {100*(a[3]-b[3])/b[3]:.1f}% |")
    head.append("")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(NL.join(head + out_lines) + NL)
    for title, res in summary:
        print(title[:2], res["before"][1], res["before"][3], res["after"][1], res["after"][3])


if __name__ == "__main__":
    main(sys.argv[1])

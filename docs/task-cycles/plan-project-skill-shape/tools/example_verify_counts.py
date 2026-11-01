"""Compare every figure stated in reports/word-counts.md with the files.

Per file: each "  - <name>: <n>" line is recounted from the file (state "before" reads
product-guidelines/coding/SKILL.md from commit f86fd71, otherwise the worktree; a name of the form
<path> section "<title>" is recounted by the section). Per sum: "Read before step 4 ..., N words",
"Read from step 4 to the end, N words", "Total ... N words" and the "without the first reading"
figures are recomputed from the recounted lines; the summary table is compared with the blocks
and its percentage with the totals. Exit code 1 and a list of the differences if any figure is
off; 0 otherwise.
"""
import re
import sys

sys.path.insert(0, "C:/Storage/repos/the-way/.runs/task-cycles/coding-skill-shape/tools")
import word_counts as wc  # noqa: E402

NL = chr(10)


def recount(name, state):
    m = re.match(r'^(.*) section "(.*)"$', name)
    if m:
        path, title = m.group(1), m.group(2)
        entry = ("section", path, "## " + title)
    else:
        entry = ("file", name)
    return wc.count(entry, state)[1]


def main(path):
    text = open(path, encoding="utf-8", newline="").read()
    lines = text.split(NL)
    errors, checked = [], 0
    route, state, block = None, None, None
    sums = {}  # (route, state) -> dict(to4, extra, total)
    first = None
    fr = sum(wc.count(e, "before")[1] for e in wc.FIRST_READS)
    cur = {}
    for ln in lines:
        if ln.startswith("## ") and not ln.startswith("## Summary"):
            route = ln[3:]
        elif ln.startswith("### "):
            state = ln[4:].lower()
            cur = sums.setdefault((route, state), {"to4": 0, "extra": 0})
        m = re.match(r"^  - (.*): (\d+)$", ln)
        if m and route and state:
            n = recount(m.group(1), state)
            checked += 1
            if n != int(m.group(2)):
                errors.append(f"{route} {state} {m.group(1)}: stated {m.group(2)}, file {n}")
            cur.setdefault("lines", []).append((block, n))
            cur["to4" if block == "to4" else "extra"] += n
        m = re.match(r"^Read before step 4 .*, (\d+) words:$", ln)
        if m:
            block = "to4"
            cur["stated_to4"] = int(m.group(1))
        m = re.match(r"^Read from step 4 to the end, (\d+) words:$", ln)
        if m:
            block = "extra"
            cur["stated_extra"] = int(m.group(1))
        m = re.match(r"^Total at the end of the run: (\d+) words\. Without the first reading in "
                     r"`refine-task` \((\d+) words\): before step 4 (\d+), total (\d+)\.$", ln)
        if m:
            cur["stated_total"] = int(m.group(1))
            cur["stated_fr"] = int(m.group(2))
            cur["stated_to4_nofr"] = int(m.group(3))
            cur["stated_total_nofr"] = int(m.group(4))
    for (r, s), c in sums.items():
        checked += 4
        if c["to4"] != c.get("stated_to4"):
            errors.append(f"{r} {s}: sum before step 4 {c['to4']} vs stated {c.get('stated_to4')}")
        if c["extra"] != c.get("stated_extra", 0):
            errors.append(f"{r} {s}: sum from step 4 {c['extra']} vs stated {c.get('stated_extra', 0)}")
        total = c["to4"] + c["extra"]
        if total != c.get("stated_total"):
            errors.append(f"{r} {s}: total {total} vs stated {c.get('stated_total')}")
        if c.get("stated_fr") != fr:
            errors.append(f"{r} {s}: first reading stated {c.get('stated_fr')}, files {fr}")
        if c["to4"] - fr != c.get("stated_to4_nofr") or total - fr != c.get("stated_total_nofr"):
            errors.append(f"{r} {s}: figures without the first reading are off")
    # summary table
    for ln in lines:
        if ln.startswith("| ") and ln.count("|") >= 9 and not ln.startswith("| Route") and "---" not in ln:
            cells = [c.strip() for c in ln.strip("|").split("|")]
            r = cells[0]
            b, a = sums[(r, "before")], sums[(r, "after")]
            bt, at = b["to4"] + b["extra"], a["to4"] + a["extra"]
            want = [str(b["to4"]), str(bt), str(a["to4"]), str(at),
                    f"{b['to4'] - fr} / {bt - fr}", f"{a['to4'] - fr} / {at - fr}",
                    f"{100 * (at - bt) / bt:.1f}%"]
            checked += len(want)
            for w, g in zip(want, cells[1:]):
                if w != g:
                    errors.append(f"summary {r}: stated {g}, computed {w}")
    # the text that quotes fixed figures
    for needle, entries, label in (("3391 words", wc.FIRST_READS, "first reading"),
                                   ("509 words", wc.CRIT_BESIDE, "files beside the critique")):
        total = sum(wc.count(e, "after")[1] for e in entries)
        want = int(needle.split()[0])
        checked += 1
        if total != want:
            errors.append(f"{label}: stated {want}, files {total}")
    new_tools = wc.count(("file", wc.T + "new_tools.md"), "after")[1]
    checked += 1
    if f"({new_tools}) come on top" not in text:
        errors.append(f"new_tools.md words stated differently from {new_tools}")
    print(f"{checked} figures compared, {len(errors)} differ")
    for e in errors:
        print("  ", e)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))

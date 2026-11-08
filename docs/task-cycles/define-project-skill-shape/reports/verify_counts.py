"""Compare every word figure the reports state with the files.

Usage: python -B verify_counts.py WORD_COUNTS [PROSE_FILE ...]

From WORD_COUNTS (word-counts.md):
- each "  - <path>: <n>" line, or "  - <path> section "<title>": <n>", under a "### Before" or
  "### After" heading or a route's block, is recounted from the file in that state (before: commit
  dfd50e5; after: the worktree);
- each "  - lines <a>-<b>: <n>" is recounted from the base SKILL.md;
- each '  - in <path> <state>: "<text>": <n>' checks that the text stands in that file and
  recounts it;
- each "Skill text, N words:", "Read beside the skill, N words:" and "Total of the route: N words."
  is recomputed from the lines of its block; "All ten files of the skill after: N words." from
  the files; the two tables and their percentages from the blocks; the figures of the first
  section (UTF-8 and C-locale counts, em dashes) from the files.
From WORD_COUNTS and every PROSE_FILE: every "<n> words" and every signed percentage in the text,
outside brackets that begin "[task:" (a figure of the task, quoted) or "[example:" (a
figure made up to show the script failing), must be one of the figures this script computed.

When `wc` is on PATH, each whole file counted is also given to `wc -w` under LC_ALL=C.UTF-8 and
LC_ALL=C, and the results are compared with this script's own counts.
Exit code 1 and a list of differences when a figure is off, else 0. Prints only ASCII.
Independent of make_word_counts.py: it imports nothing from it and counts with its own code.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

REPO = "."
BASE = "dfd50e513c09bebe9d09d74209cd28612565da83"
NL = chr(10)
DASH = chr(8212)


def read(path, state):
    if state == "before":
        return subprocess.run(["git", "-C", REPO, "show", BASE + ":" + path],
                              capture_output=True, check=True).stdout.decode("utf-8")
    with open(os.path.join(REPO, path), "rb") as f:
        return f.read().decode("utf-8")


def tokens(text):
    return re.findall(r"\S+", text)


def section_text(text, title):
    lines = text.split(NL)
    idx = [k for k, ln in enumerate(lines) if ln.rstrip() == "## " + title]
    if len(idx) != 1:
        raise ValueError("section %r found %d times" % (title, len(idx)))
    out = []
    for ln in lines[idx[0] + 1:]:
        if ln.startswith("# ") or ln.startswith("## "):
            break
        out.append(ln)
    return NL.join([lines[idx[0]]] + out)


def count(name, state):
    m = re.fullmatch(r'(.*) section "(.*)"', name)
    if m:
        return len(tokens(section_text(read(m.group(1), state), m.group(2))))
    return len(tokens(read(name, state)))


def c_count(text):
    return len([t for t in tokens(text) if re.search(r"[!-~]", t)])


def pct(a, b):
    return "%+.1f%%" % (100.0 * (b - a) / a)


def wc_check(names, errors, notes):
    wc = shutil.which("wc")
    if not wc:
        notes.append("wc not on PATH: the cross-check with wc -w did not run")
        return
    tmp = tempfile.mkdtemp()
    for name, state in names:
        data = read(name, state).encode("utf-8")
        path = os.path.join(tmp, "f.txt")
        with open(path, "wb") as f:
            f.write(data)
        mine = {"C.UTF-8": len(tokens(data.decode("utf-8"))), "C": c_count(data.decode("utf-8"))}
        for loc, want in mine.items():
            env = dict(os.environ, LC_ALL=loc)
            got = int(subprocess.run([wc, "-w", path], capture_output=True, env=env,
                                     check=True).stdout.split()[0])
            if got != want:
                errors.append("wc -w LC_ALL=%s %s %s: wc %d, this script %d" % (loc, state, name, got, want))
    notes.append("wc -w cross-check ran on %d files in two locales" % len(names))


def main(argv):
    wcpath = argv[1]
    prose = argv[2:]
    text = open(wcpath, encoding="utf-8").read()
    lines = text.split(NL)
    errors, notes = [], []
    figures = set()
    checked = 0
    whole_files = set()
    blocks = {}
    route = state = block = None
    base_skill = read("project-level/skill/SKILL.md", "before")
    base_lines = base_skill.split(NL)
    for ln in lines:
        if ln.startswith("## "):
            route, state, block = ln[3:], None, None
            continue
        if ln.startswith("### "):
            state = ln[4:].strip().lower()
            block = None
            continue
        m = re.fullmatch(r"Skill text, (\d+) words:", ln)
        if m:
            block = "skill"
            blocks.setdefault((route, state), {})["stated_skill"] = int(m.group(1))
            continue
        m = re.fullmatch(r"Read beside the skill, (\d+) words:", ln)
        if m:
            block = "beside"
            blocks.setdefault((route, state), {})["stated_beside"] = int(m.group(1))
            continue
        m = re.fullmatch(r"Total of the route: (\d+) words\.", ln)
        if m:
            blocks.setdefault((route, state), {})["stated_total"] = int(m.group(1))
            continue
        m = re.fullmatch(r"  - lines (\d+)-(\d+): (\d+)", ln)
        if m:
            a, b, n = int(m.group(1)), int(m.group(2)), int(m.group(3))
            got = len(tokens(NL.join(base_lines[a - 1:b])))
            figures.add(got)
            checked += 1
            if got != n:
                errors.append("lines %d-%d: stated %d, counted %d" % (a, b, n, got))
            continue
        m = re.fullmatch(r'  - in (\S+) (before|after): "(.*)": (\d+)', ln)
        if m:
            path, st, quote, n = m.group(1), m.group(2), m.group(3), int(m.group(4))
            checked += 1
            if " ".join(quote.split()) not in " ".join(read(path, st).split()):
                errors.append("quoted text not in %s %s: %s" % (st, path, quote[:50]))
            got = len(tokens(quote))
            figures.add(got)
            if got != n:
                errors.append("quoted text in %s: stated %d, counted %d" % (path, n, got))
            continue
        m = re.fullmatch(r"  - (.+): (\d+)", ln)
        if m:
            name, n = m.group(1), int(m.group(2))
            st = state if state in ("before", "after") else "before"
            got = count(name, st)
            if state not in ("before", "after") and count(name, "after") != got:
                errors.append("%s differs between the states" % name)
            figures.add(got)
            checked += 1
            if " section " not in name:
                whole_files.add((name, st))
            if got != n:
                errors.append("%s %s %s: stated %d, counted %d" % (route, st, name, n, got))
            if block:
                d = blocks.setdefault((route, state), {})
                d[block] = d.get(block, 0) + got
    m = re.search(r"All ten files of the skill after: (\d+) words\.", text)
    skill_dir = os.path.join(REPO, "project-level", "skill")
    names = sorted(f for f in os.listdir(skill_dir) if f.endswith(".md"))
    all_after = sum(count("project-level/skill/" + f, "after") for f in names)
    figures.add(all_after)
    checked += 1
    if len(names) != 10 or not m or int(m.group(1)) != all_after:
        errors.append("all files after: %d files, %d words, stated %s" % (len(names), all_after, m and m.group(1)))
    sums = {}
    for (r, s), d in blocks.items():
        if "stated_total" not in d:
            continue
        sk, bs = d.get("skill", 0), d.get("beside", 0)
        sums[(r.split(" ", 1)[0].rstrip("."), s)] = (sk, sk + bs)
        figures.update([sk, bs, sk + bs])
        checked += 3
        for key, want in (("stated_skill", sk), ("stated_beside", bs), ("stated_total", sk + bs)):
            if d.get(key) != want:
                errors.append("%s %s %s: stated %s, computed %d" % (r, s, key, d.get(key), want))
    for (r, s), (sk, tot) in list(sums.items()):
        if s == "after":
            b = sums[(r, "before")]
            figures.update([pct(b[0], sk), pct(b[1], tot), abs(b[0] - sk), abs(b[1] - tot)])
    in_six = False
    for ln in lines:
        if ln.startswith("## "):
            in_six = ln.startswith("## The six")
        if not ln.startswith("| ") or ln.startswith("| Route") or ln.startswith("| Reading") or "---" in ln:
            continue
        c = [x.strip() for x in ln.strip().strip("|").split("|")]
        if in_six:
            k = c[0]
            sb = sums[("1", "before")][0] + 4 * sums[(k, "before")][0] + sums[("4", "before")][0]
            tb = sums[("1", "before")][1] + 4 * sums[(k, "before")][1] + sums[("4", "before")][1]
            sa = sums[("1", "after")][0] + 4 * sums[(k, "after")][0] + sums[("4", "after")][0]
            ta = sums[("1", "after")][1] + 4 * sums[(k, "after")][1] + sums[("4", "after")][1]
            want = [str(sb), str(tb), str(sa), str(ta), pct(sb, sa), pct(tb, ta)]
        else:
            b, a = sums[(c[0], "before")], sums[(c[0], "after")]
            want = [str(b[0]), str(b[1]), str(a[0]), str(a[1]), pct(b[0], a[0]), pct(b[1], a[1])]
        figures.update(want)
        for w_, g in zip(want, c[1:]):
            checked += 1
            if w_ != g:
                errors.append("table row %s: stated %s, computed %s" % (c[0], g, w_))
    utf, cl = len(tokens(base_skill)), c_count(base_skill)
    tmpl = read("project-level/definition_template.md", "before")
    first = {"utf": utf, "c": cl, "diff": utf - cl, "dashes": base_skill.count(DASH),
             "alone": len([t for t in tokens(base_skill) if t == DASH]),
             "tutf": len(tokens(tmpl)), "tc": c_count(tmpl)}
    figures.update(first.values())
    m = re.search(r"on the base: (\d+) words under a UTF-8 locale, (\d+) words with .*?The (\d+) words "
                  r"between them .*?holds (\d+) em dashes, (\d+) of them", text, re.S)
    m2 = re.search(r"definition_template.md`: (\d+) words under a UTF-8 locale \(the task's figure\), (\d+) in", text)
    stated = [int(x) for x in (m.groups() if m else ())] + [int(x) for x in (m2.groups() if m2 else ())]
    want = [first[k] for k in ("utf", "c", "diff", "dashes", "alone", "tutf", "tc")]
    checked += len(want)
    if stated != want:
        errors.append("first section: stated %s, computed %s" % (stated, want))
    for f in [wcpath] + prose:
        body = open(f, encoding="utf-8").read()
        body = re.sub(r"\[(?:task|example):[^\]]*\]", "", body)
        for n in re.findall(r"(?<![\w.+-])(\d+) words\b", body):
            checked += 1
            if int(n) not in figures:
                errors.append("%s: '%s words' is no figure this script computed" % (os.path.basename(f), n))
        for p in re.findall(r"(?<![\w.])([+-]\d+\.\d%)", body):
            checked += 1
            if p not in figures:
                errors.append("%s: '%s' is no percentage this script computed" % (os.path.basename(f), p))
    wc_check(sorted(whole_files), errors, notes)
    print("%d figures compared, %d differ" % (checked, len(errors)))
    for n_ in notes:
        print("  note:", n_)
    for e in errors:
        print("  ", e.encode("ascii", "replace").decode("ascii"))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

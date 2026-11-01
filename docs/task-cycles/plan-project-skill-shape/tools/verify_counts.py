"""Compare every figure stated in reports/word-counts.md with the files.

Per file: each "  - <name>: <n>" line is recounted from the file (state "before" from commit 2f51e6c,
state "after" from the worktree; a name of the form <path> section "<title>" is recounted by the
section). Per sum: "Skill text, N words", "Read beside the skill, N words" and "Total ... N words" are
recomputed from the recounted lines; the summary table is compared with the blocks, its percentages
with the totals. Exit code 1 and the list of differences if any figure is off, else 0.
Independent of word_counts.py (own counting code).
"""
import re
import subprocess
import sys

REPO = "C:/Storage/repos/the-way/.runs/worktrees/plan-project-skill-shape"
BASE = "2f51e6c31f5911ac8a0292a80a4f599bd4bd0092"
NL = chr(10)


def read(path, state):
    if state == "before":
        return subprocess.run(["git", "-C", REPO, "show", f"{BASE}:{path}"], capture_output=True,
                              check=True).stdout.decode("utf-8")
    return open(f"{REPO}/{path}", encoding="utf-8", newline="").read()


def words_of_section(text, title):
    lines = text.split(NL)
    heading = "## " + title
    i = next(k for k, l in enumerate(lines) if l.strip() == heading)
    j = len(lines)
    for k in range(i + 1, len(lines)):
        if re.match(r"^#{1,2} ", lines[k]):
            j = k
            break
    return len(NL.join(lines[i:j]).split())


def recount(name, state):
    m = re.match(r'^(.*) section "(.*)"$', name)
    if m:
        return words_of_section(read(m.group(1), state), m.group(2))
    return len(read(name, state).split())


def main(path):
    lines = open(path, encoding="utf-8", newline="").read().split(NL)
    errors, checked = [], 0
    route = state = block = None
    data = {}
    for ln in lines:
        if ln.startswith("## ") and not ln.startswith("## Summary"):
            route = ln[3:]
        elif ln.startswith("### "):
            state = ln[4:].lower()
            data[(route, state)] = {"skill": 0, "beside": 0}
        m = re.match(r"^Skill text, (\d+) words:$", ln)
        if m:
            block = "skill"
            data[(route, state)]["s_skill"] = int(m.group(1))
        m = re.match(r"^Read beside the skill, (\d+) words:$", ln)
        if m:
            block = "beside"
            data[(route, state)]["s_beside"] = int(m.group(1))
        m = re.match(r"^Total at the end of the run: (\d+) words\.$", ln)
        if m:
            data[(route, state)]["s_total"] = int(m.group(1))
        m = re.match(r"^  - (.*): (\d+)$", ln)
        if m and route and state:
            n = recount(m.group(1), state)
            checked += 1
            if n != int(m.group(2)):
                errors.append(f"{route} {state} {m.group(1)}: stated {m.group(2)}, file {n}")
            data[(route, state)][block] += n
    for (r, s), d in data.items():
        checked += 3
        if d["skill"] != d.get("s_skill"):
            errors.append(f"{r} {s}: skill sum {d['skill']} vs stated {d.get('s_skill')}")
        if d["beside"] != d.get("s_beside"):
            errors.append(f"{r} {s}: beside sum {d['beside']} vs stated {d.get('s_beside')}")
        if d["skill"] + d["beside"] != d.get("s_total"):
            errors.append(f"{r} {s}: total {d['skill'] + d['beside']} vs stated {d.get('s_total')}")
    for ln in lines:
        if ln.startswith("| ") and not ln.startswith("| Route") and "---" not in ln:
            c = [x.strip() for x in ln.strip("|").split("|")]
            b, a = data[(c[0], "before")], data[(c[0], "after")]
            bt, at = b["skill"] + b["beside"], a["skill"] + a["beside"]
            want = [str(b["skill"]), str(bt), str(a["skill"]), str(at),
                    f"{100 * (a['skill'] - b['skill']) / b['skill']:+.1f}%", f"{100 * (at - bt) / bt:+.1f}%"]
            checked += len(want)
            for w, g in zip(want, c[1:]):
                if w != g:
                    errors.append(f"summary {c[0]}: stated {g}, computed {w}")
    print(f"{checked} figures compared, {len(errors)} differ")
    for e in errors:
        print("  ", e)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))

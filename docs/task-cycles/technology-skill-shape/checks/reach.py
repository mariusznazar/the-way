"""Reach check: for each of the five routes, the files that route reads (as the pointers of SKILL.md
give them) must hold the fragments the acceptance criteria name. Prints PASS/FAIL lines to argv[1]."""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
D = ROOT / "project-level/technology"


def norm(t):
    return re.sub(r"\s+", " ", t)


text = {p.name: norm(p.read_text(encoding="utf-8")) for p in D.glob("*.md")}

routes = {
    "A leader, new list, no open choice": ["SKILL.md", "start.md", "list.md", "running_product.md", "close.md"],
    "B leader, new list, open choices": ["SKILL.md", "start.md", "list.md", "running_product.md", "settle.md", "close.md"],
    "C leader, resuming, open choices": ["SKILL.md", "start.md", "running_product.md", "settle.md", "close.md"],
    "D leader, resuming, no open choice": ["SKILL.md", "start.md", "running_product.md", "close.md"],
    "E research agent": ["research.md"],
}

results = []


def check(route, label, needle, files=None, absent=False):
    files = files or routes[route]
    hit = [f for f in files if needle in text[f]]
    ok = (not hit) if absent else bool(hit)
    results.append((ok, f"{route} | {label} | {'in ' + ', '.join(hit) if hit else 'nowhere in the route'}"))


LOOK = "look at the three matters of an agent's way to the running product — its logs, its interface and its development data"
NAME = "`.runs/technology/<choice>.md`, the choice's name in lower case with hyphens for spaces, which the product's Git ignores"
FOUND = "The step writes into the definition only, never into the product's foundation (WAY-106)"
CRIT = "elements/common/critique/SKILL.md"

for r in list(routes)[:4]:
    check(r, "foundation rule", FOUND)
    check(r, "report name rule", NAME)
    check(r, "location paragraph (the-way, prefix)", "each skill named in this skill or in a file beside it")
for r in ("A leader, new list, no open choice", "B leader, new list, open choices"):
    check(r, "the look (text)", LOOK)
    check(r, "pointer to the look from the listing", "running_product.md")
for r in ("C leader, resuming, open choices", "D leader, resuming, no open choice"):
    check(r, "the look (text)", LOOK)
    check(r, "resume bullet takes the look", "first take the look at the logs, the interface and the development data that `running_product.md`", ["start.md"])
    check(r, "step 0 pointer of SKILL.md reaches running_product.md", "Where the Technology section holds a list, read `running_product.md`", ["SKILL.md"])
for r in ("B leader, new list, open choices", "C leader, resuming, open choices"):
    check(r, "critique instruction read at the steps that use it", CRIT, ["SKILL.md", "settle.md"])
    check(r, "path of research.md reaches the agent's list", "and the path of the file `research.md`", ["settle.md"])
    check(r, "risks written to the choice's report", "Write the risks the tests give into the choice's report, `.runs/technology/<choice>.md`", ["settle.md"])
for r in ("A leader, new list, no open choice", "D leader, resuming, no open choice"):
    check(r, "critique instruction not read", CRIT, ["start.md", "list.md", "running_product.md", "close.md"], absent=True)
check("C leader, resuming, open choices", "reuse rule names the report directory", "a report of an open choice under `.runs/technology/` that reads `critique: passed` is reused", ["start.md"])

# Finding 1: a human who adds or changes an item at the resume question reaches list.md.
C = "C leader, resuming, open choices"
check(C, "finding 1: step 0 pointer names the human's change", "when the look it gives adds an item to the list or the human adds or changes one", ["SKILL.md"])
check(C, "finding 1: resume bullet sends the human's change to list.md", "where the human adds or changes an item, follow the step \"List the choices\" (`list.md` beside this file)", ["start.md"])
# Finding 2: the resuming leader with open choices ends in the step Close.
check(C, "finding 2: close.md is read on this route", "Return to `define-project`, which sets the status line to `ready for gate`")
check(C, "finding 2: SKILL.md points to close.md", "read `close.md` beside this skill", ["SKILL.md"])

# Route E: what the agent needs, from its file alone.
E = "E research agent"
check(E, "foundation rule", FOUND)
check(E, "report name rule", NAME)
check(E, "where the-way lies", "This file lies in `project-level/technology/` of the-way")
check(E, "where the template lies", "`definition_template.md` lies in `project-level/`")
check(E, "what the leader gives", "The leader gives you the definition, the choice and the preferences under it, the template's Technology section")
for word in ("wave", "critique:", "`critique`", "SKILL.md", "list.md", "settle.md", "start.md", "close.md",
             "running_product.md", "step 1", "step 2", "step 3", "open choice", "recommend"):
    check(E, f"no unexplained term {word!r}", word, absent=True)

# Pointers: every file named in backticks as *.md beside the skill exists; every file is named by SKILL.md.
named = set()
for f, t in text.items():
    for m in re.findall(r"`([a-z_]+\.md)`", t):
        if m == "definition_template.md":  # lies in project-level/, not beside the skill
            continue
        named.add(m)
        results.append(((D / m).exists(), f"pointer | {f} names {m} | {'exists' if (D / m).exists() else 'MISSING'}"))
for p in D.glob("*.md"):
    if p.name != "SKILL.md":
        ok = f"`{p.name}`" in text["SKILL.md"]
        results.append((ok, f"SKILL.md names {p.name} | {'yes' if ok else 'NO'}"))

# Bare step numbers in the files beside the skill (review by hand).
notes = []
for f, t in text.items():
    if f == "SKILL.md":
        continue
    for m in re.finditer(r".{30}\b[Ss]tep \d[.\d]*.{20}", t):
        notes.append(f"step number in {f}: ...{m.group(0)}...")

fails = [r for r in results if not r[0]]
out = [("PASS " if ok else "FAIL ") + msg for ok, msg in results] + notes
out.append(f"total={len(results)} failed={len(fails)}")
pathlib.Path(sys.argv[1]).write_text("\n".join(out) + "\n", encoding="utf-8")
print(out[-1])
sys.exit(1 if fails else 0)

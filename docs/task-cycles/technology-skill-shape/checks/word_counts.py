"""Words read on the five routes of the task, before (commit 525cde1) and after (the worktree).

Words are whitespace-separated tokens of a whole file: len(text.split()). A section's bounds: from its
heading line, included, up to the line before the next line that begins with '## ' (second-level
heading), or the end of the file. Writes a Markdown fragment to argv[1]."""
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
BASE = "525cde1dd53c474f56ea0ece289cb60e868aa90d"
TECH = "project-level/technology/"


def old(path):
    return subprocess.run(["git", "-C", str(ROOT), "show", f"{BASE}:{path}"], capture_output=True,
                          text=True, encoding="utf-8", check=True).stdout


def new(path):
    return (ROOT / path).read_text(encoding="utf-8")


def words(text):
    return len(text.split())


def section(text, heading):
    # The heading must stand outside every code fence: a template shows its headings in fenced
    # examples too.
    lines = text.split("\n")
    fenced = False
    outside = []
    for i, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            fenced = not fenced
        elif not fenced:
            outside.append(i)
    starts = [i for i in outside if lines[i] == heading]
    assert len(starts) == 1, (heading, starts)
    start = starts[0]
    end = next((i for i in outside if i > start and lines[i].startswith("## ")), len(lines))
    return "\n".join(lines[start:end])


WOW = "elements/common/way_of_working.md"
TEMPLATE = "project-level/definition_template.md"
CRIT = ["elements/common/critique/" + n for n in ("SKILL.md", "prepare.md", "check.md", "settle.md")]

# Fixed addition of the leader routes: counted once, the same before and after.
fixed = {
    TEMPLATE + " (whole)": words(new(TEMPLATE)),
    WOW + ' section "How a skill asks"': words(section(new(WOW), "## How a skill asks")),
    WOW + ' section "Reading the foundation"': words(section(new(WOW), "## Reading the foundation")),
}
assert fixed[TEMPLATE + " (whole)"] == words(old(TEMPLATE))
assert words(section(old(WOW), "## How a skill asks")) == fixed[WOW + ' section "How a skill asks"']
assert words(section(old(WOW), "## Reading the foundation")) == fixed[WOW + ' section "Reading the foundation"']
fixed_sum = sum(fixed.values())
crit_words = {p: words(new(p)) for p in CRIT}
for p in CRIT:
    assert words(old(p)) == crit_words[p]
crit_sum = sum(crit_words.values())
tech_section = words(section(new(TEMPLATE), "## Technology"))
assert words(section(old(TEMPLATE), "## Technology")) == tech_section

old_skill = words(old(TECH + "SKILL.md"))
files = {f: words(new(TECH + f)) for f in
         ("SKILL.md", "start.md", "list.md", "running_product.md", "settle.md", "research.md", "close.md")}

routes = {
    "leader, new list, no open choice": ["SKILL.md", "start.md", "list.md", "running_product.md", "close.md"],
    "leader, new list, open choices": ["SKILL.md", "start.md", "list.md", "running_product.md", "settle.md", "close.md"],
    "leader, resuming, open choices": ["SKILL.md", "start.md", "running_product.md", "settle.md", "close.md"],
    "leader, resuming, no open choice": ["SKILL.md", "start.md", "running_product.md", "close.md"],
}
crit_on = {"leader, new list, open choices", "leader, resuming, open choices"}

rows = []
for name, fl in routes.items():
    before = old_skill + fixed_sum + crit_sum
    after = sum(files[f] for f in fl) + fixed_sum + (crit_sum if name in crit_on else 0)
    rows.append((name, before, after))
rows.append(("research agent", old_skill + tech_section, files["research.md"] + tech_section))

out = []
out.append("| Route | Before | After | After minus before |")
out.append("|---|---:|---:|---:|")
for name, b, a in rows:
    out.append(f"| {name} | {b} | {a} | {a - b:+d} |")
out.append("")
out.append("Files of the skill, words each:")
out.append("")
out.append("| File | Words |")
out.append("|---|---:|")
out.append(f"| {TECH}SKILL.md at {BASE[:7]} | {old_skill} |")
for f, w in files.items():
    out.append(f"| {TECH}{f} | {w} |")
out.append(f"| sum of the seven files after | {sum(files.values())} |")
out.append("")
out.append("Fixed addition of the leader routes, once:")
out.append("")
out.append("| Part | Words |")
out.append("|---|---:|")
for k, v in fixed.items():
    out.append(f"| {k} | {v} |")
out.append(f"| sum | {fixed_sum} |")
out.append("")
out.append("Critique instruction:")
out.append("")
out.append("| File | Words |")
out.append("|---|---:|")
for k, v in crit_words.items():
    out.append(f"| {k} | {v} |")
out.append(f"| sum | {crit_sum} |")
out.append("")
out.append(f"Fixed addition of the research agent: section \"Technology\" of {TEMPLATE}: {tech_section} words.")
out.append("")
extra = {"list.md if the look adds an item or the human adds or changes one (resuming routes)": files["list.md"]}
for k, v in extra.items():
    out.append(f"Conditional, not in the rows above: {k}: +{v} words.")
pathlib.Path(sys.argv[1]).write_text("\n".join(out) + "\n", encoding="utf-8")
print("ok", [(n, b, a) for n, b, a in rows])

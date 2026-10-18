"""Slice 1 weakest-point check (WAY-164).

Requirement: the skeletons of the two templates are the form the F4 fixtures follow, so that a form
check reading them holds the valid fixtures to exactly what those fixtures contain; and every rule
of the templates cites a decision of the-way.

Method: read the first fenced block under `## Required form` of each template; take its header
lines, `## ` sections and non-placeholder `### ` headings; check that the F4 fixtures STYLEGUIDE
(styleguide merged form) and TESTING (common form alone) hold them in that order. Then list every
list item of both templates outside fenced code that names no `WAY-` number.

Usage: python -B weakest_point.py <the-way worktree>
"""
import importlib.util
import os
import re
import sys

root = sys.argv[1]


def skeleton(path):
    text = open(os.path.join(root, path), encoding="utf-8").read()
    section = text.split("## Required form", 1)[1]
    block = re.search(r"^```markdown\n(.*?)^```$", section, re.S | re.M).group(1)
    items = []
    for line in block.splitlines():
        if line.startswith("- **"):
            items.append(("header", line.split(":**")[0] + ":**"))
        elif line.startswith("## "):
            items.append(("section", line))
        elif line.startswith("### ") and "<" not in line:
            items.append(("heading", line))
    return items


def in_order(text, items, name):
    lines = text.splitlines()
    position, ok = 0, True
    for kind, item in items:
        found = next((i for i in range(position, len(lines))
                      if lines[i] == item or (kind == "header" and lines[i].startswith(item))), None)
        if found is None:
            print("MISSING or out of order in %s: %r" % (name, item))
            ok = False
        else:
            position = found + 1
    return ok


spec = importlib.util.spec_from_file_location(
    "f4", os.path.join(root, "product-guidelines", "test_form_check_invariants.py"))
f4 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(f4)

common = skeleton("product-guidelines/template.md")
merged = skeleton("product-guidelines/styleguide/template.md")
print("common form:", common)
print("merged form:", merged)
common_sections = [i for i in common if i[0] == "section"]
merged_sections = [i for i in merged if i[0] == "section"]
print("merged sections = common sections with Roles after When to read:",
      merged_sections == common_sections[:1] + [("section", "## Roles")] + common_sections[1:])
ok1 = in_order(f4.TESTING, common, "TESTING")
merged_rest = [i for i in merged if i[0] != "header" or "Discipline" in i[1] or "Applies" in i[1]]
ok2 = in_order(f4.STYLEGUIDE, merged_rest, "STYLEGUIDE")
print("TESTING follows the common form:", ok1)
print("STYLEGUIDE follows the merged form:", ok2)
print("Roles table header in fixture:",
      "| Role | Kind | Meaning for the user | Text on it | Decision |" in f4.STYLEGUIDE)

uncited = 0
for path in ("product-guidelines/template.md", "product-guidelines/styleguide/template.md"):
    text = open(os.path.join(root, path), encoding="utf-8").read()
    inside, item, start = False, [], 0
    lines = text.splitlines() + [""]
    for number, line in enumerate(lines, 1):
        if line.startswith("```"):
            inside = not inside
            continue
        if inside:
            continue
        if re.match(r"^\s*- ", line) or not line.strip() or line.startswith("#"):
            if item and not re.search(r"WAY-\d+", " ".join(item)):
                print("NO DECISION CITED: %s:%d: %s" % (path, start, " ".join(item)[:90]))
                uncited += 1
            item, start = ([line.strip()], number) if re.match(r"^\s*- ", line) else ([], 0)
        elif item:
            item.append(line.strip())
print("list items naming no decision:", uncited)
sys.exit(0 if ok1 and ok2 else 1)

from pathlib import Path
import re

parts = {"task-cycle", "project-level", "product-guidelines", "instruction-files", "agent-instructions"}
extra = {2, 4, 5, 7, 8, 12, 14, 17, 18, 19, 20, 22, 29, 31, 35, 40, 41, 49, 52, 53, 54, 56, 60, 64, 71, 72, 85, 86, 95, 97, 104}
terms = re.compile(r"guideline|exemplar|screenshot|visual|styleguide|applies to|when to read|interface|render|appearance", re.I)
for name, heading, field in [
    ("decisions.md", r"^### (WAY-\d+/\d+)", "Scope"),
    ("invariants.md", r"^## ([^\n]+/\d+)", "Part"),
]:
    path = Path("foundations") / name
    content = path.read_text(encoding="utf-8")
    headers = list(re.finditer(heading, content, re.M))
    selected = []
    linked = []
    search = []
    for index, match in enumerate(headers):
        block = content[match.start():headers[index + 1].start() if index + 1 < len(headers) else len(content)]
        location = f"{path.as_posix()}:{content.count(chr(10), 0, match.start()) + 1}"
        label = f"{match.group(1)} | {location}"
        scope = re.search(r"(?ms)^- \*\*" + field + r":\*\* (.*?)(?=^- \*\*|\n\n|\Z)", block)
        assert scope, label
        words = set(re.findall(r"[a-z]+(?:-[a-z]+)*", scope.group(1)))
        if words & parts or "every" in words:
            selected.append(label)
        elif name == "decisions.md" and int(match.group(1).split("-")[1].split("/")[0]) in extra:
            linked.append(label)
        if terms.search(block):
            search.append(label)
    print(f"{name}: population={len(headers)} selected={len(selected)}")
    print("Scope/Part selections (read whole by design agent; lines at source base):")
    print("\n".join(selected))
    print(f"Additional whole-entry reads through links/search: {len(linked)}")
    print("\n".join(linked) or "none")
    print(f"Semantic-search hits: {len(search)}")
    print("\n".join(search))
    print()
print("Inventory generation completed; stdout is metadata only; stderr empty on success.")

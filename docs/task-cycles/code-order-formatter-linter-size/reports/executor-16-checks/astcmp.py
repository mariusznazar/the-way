import ast, pathlib, subprocess
BASE = "95316c256de20d7e7a272a27246ecd244e14c4d5"
base_src = subprocess.run(["git", "show", f"{BASE}:process-audit/audit_count.py"], capture_output=True, check=True).stdout.decode("utf-8")
def top(src):
    out = {}
    for node in ast.parse(src).body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            out[node.name] = ast.dump(node)
        elif isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            out[node.targets[0].id] = ast.dump(node)
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            out[node.target.id] = ast.dump(node)
    return out
old = top(base_src)
new = {}
where = {}
for name in ("audit_count", "version_analysis", "audit_report"):
    for k, v in top(pathlib.Path(f"process-audit/{name}.py").read_text(encoding="utf-8")).items():
        assert k not in new or k in ("display", "__all__"), (k, where.get(k), name)
        new[k] = v
        where[k] = name
same = [k for k in old if k in new and old[k] == new[k]]
diff = [k for k in old if k in new and old[k] != new[k]]
gone = [k for k in old if k not in new]
added = [k for k in new if k not in old]
print("identical:", len(same), "moved-or-kept")
print("changed:", diff)
print("missing from the new modules:", gone)
print("added:", added)
import collections
print(collections.Counter(where[k] for k in same))

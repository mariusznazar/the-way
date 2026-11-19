import ast, subprocess, sys
old = ast.parse(subprocess.run(["git", "show", "d0a861d9:process-audit/record_reading.py"], capture_output=True, check=True).stdout.decode("utf-8"))
new = ast.parse(open("process-audit/audit_shared.py", encoding="utf-8").read())
def top(tree):
    out = {}
    for n in tree.body:
        if isinstance(n, (ast.FunctionDef, ast.ClassDef)):
            out[n.name] = ast.dump(n)
        elif isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name):
            out[n.targets[0].id] = ast.dump(n)
    return out
o, n = top(old), top(new)
for name in ["AuditCountError", "GitError", "Git", "table_cells", "is_separator", "THE_WAY", "MAX_BYTES", "GIT_TIMEOUT", "display"]:
    print(name, "identical" if o.get(name) == n.get(name) else f"DIFFERENT old={name in o} new={name in n}")
rr = top(ast.parse(open("process-audit/record_reading.py", encoding="utf-8").read()))
print("removed from record_reading:", sorted(set(o) - set(rr)))
print("changed in record_reading:", sorted(k for k in rr if k in o and o[k] != rr[k]))
print("added in record_reading:", sorted(set(rr) - set(o)))

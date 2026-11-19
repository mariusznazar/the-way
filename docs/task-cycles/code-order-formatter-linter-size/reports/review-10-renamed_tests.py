import ast, subprocess, sys
def tests(src):
    t = ast.parse(src); lines = src.splitlines(); out = []
    for n in ast.walk(t):
        if isinstance(n, ast.FunctionDef) and n.name.startswith("test_"):
            body = "\n".join(lines[n.lineno-1:n.end_lineno])
            out.append((n.lineno, n.name, "decision:" in body or "invariant:" in body))
    return sorted(out)
old = subprocess.run(["git","show","0ccdc807:process-audit/test_record_items.py"],capture_output=True,text=True,encoding="utf-8",cwd="wt").stdout
new = open("wt/process-audit/test_record_items.py",encoding="utf-8").read()
o = tests(old); n = tests(new)
print(len(o), len(n))
renamed = [(a[1], b[1], b[2]) for a,b in zip(o,n) if a[1]!=b[1]]
print("renamed", len(renamed), "with decision/invariant line", sum(r[2] for r in renamed))
for r in renamed: print(r[2], r[1])

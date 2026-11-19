import ast, sys
root = "process-audit/"


def key_of(n):
    if isinstance(n, (ast.FunctionDef, ast.ClassDef)):
        return n.name
    if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
        return n.targets[0].id
    if isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name):
        return n.target.id
    return None


old = ast.parse(open(".runs/review-15/old/audit_count.py", encoding="utf-8").read())
new = {}
for f in ("audit_count", "problem_register", "record_reading"):
    t = ast.parse(open(root + f + ".py", encoding="utf-8").read())
    for n in t.body:
        k = key_of(n)
        if k:
            new.setdefault(k, []).append((f, ast.dump(n)))
missing = []
diff = []
where = {}
oldkeys = set()
for n in old.body:
    k = key_of(n)
    if not k:
        continue
    oldkeys.add(k)
    d = ast.dump(n)
    cands = new.get(k, [])
    m = [f for f, dd in cands if dd == d]
    if not cands:
        missing.append(k)
    elif not m:
        diff.append((k, [f for f, _ in cands]))
    else:
        where.setdefault(m[0], []).append(k)
print("missing", missing)
print("diff", diff)
print({k: len(v) for k, v in where.items()})
print("new only", [k for k in new if k not in oldkeys])
for k, v in new.items():
    if len(v) > 1:
        print("defined in several files", k, [f for f, _ in v])

import ast, sys
root = ""
def names(node):
    if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)):
        return [node.name]
    if isinstance(node, ast.Assign):
        return [t.id for t in node.targets if isinstance(t, ast.Name)] or [ast.dump(node)[:60]]
    if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
        return [node.target.id]
    return None
def load(p):
    src = open(p, encoding="utf-8").read()
    return ast.parse(src), src
base, bsrc = load(root + ".runs/review-16/base_audit_count.py")
new = {}
for f in ["audit_count", "version_analysis", "audit_report"]:
    t, s = load(root + f"process-audit/{f}.py")
    for n in t.body:
        nm = names(n)
        if nm:
            for x in nm:
                new.setdefault(x, []).append((f, ast.dump(n), n))
other_base = []
for n in base.body:
    nm = names(n)
    if not nm:
        other_base.append(n)
        continue
    for x in nm:
        if x not in new:
            print("MISSING", x); continue
        d = ast.dump(n)
        if any(d == dd for _, dd, _ in new[x]):
            pass
        else:
            print("DIFF", x, [f for f, _, _ in new[x]])
print("non-named base nodes:")
for n in other_base:
    print(type(n).__name__, getattr(n, "lineno", None), ast.get_source_segment(bsrc, n)[:80].replace("\n", "|"))
bnames = set(x for n in base.body for x in (names(n) or []))
print("NEW names:", sorted(k for k in new if k not in bnames))
print("DUP:", [k for k, v in new.items() if len(v) > 1])

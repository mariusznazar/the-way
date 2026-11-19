import ast, sys
def top(path):
    tree = ast.parse(open(path, encoding='utf-8').read())
    out = {}
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            out[node.name] = ast.dump(node)
        elif isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name):
                    out[t.id] = ast.dump(node.value)
    return out
old = top('.runs/executor-15/old/audit_count.py')
new = {}
for f in ('audit_count', 'problem_register', 'record_reading'):
    t = top(f'process-audit/{f}.py')
    for k, v in t.items():
        new.setdefault(k, []).append((f, v))
for k, lst in new.items():
    if k not in old:
        print('NEW', k, [f for f, _ in lst]); continue
    for f, v in lst:
        if v != old[k]:
            print('CHANGED', k, f)
for k in old:
    if k not in new:
        print('GONE', k)
for k, lst in new.items():
    if len(lst) > 1:
        print('DUP', k, [f for f, _ in lst])

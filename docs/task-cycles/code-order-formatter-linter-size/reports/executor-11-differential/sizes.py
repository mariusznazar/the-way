import ast, sys
for p in sys.argv[1:]:
    t = ast.parse(open(p, encoding="utf-8").read())
    for n in ast.walk(t):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            s = n.end_lineno - n.lineno + 1
            if s > 80: print(p, n.name, n.lineno, s)

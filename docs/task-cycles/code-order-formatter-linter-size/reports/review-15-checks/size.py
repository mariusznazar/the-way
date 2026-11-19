import sys
sys.path.insert(0, "agent-instructions")
sys.dont_write_bytecode = True
from test_size_invariant import function_sizes, file_lines
for p in ("problem_register", "record_reading", "audit_count"):
    s = open(f"process-audit/{p}.py", encoding="utf-8").read()
    fs = function_sizes(s)
    over = [f for f in fs if f[2] > 110]
    top = sorted(fs, key=lambda f: -f[2])[:3]
    print(p, "lines", file_lines(s), "functions over 110:", over, "top3", top)

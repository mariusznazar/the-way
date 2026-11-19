import pathlib, sys
sys.path.insert(0, "agent-instructions")
from test_size_invariant import file_lines, function_sizes
names = ["audit_count", "version_analysis", "audit_report", "record_reading", "problem_register", "stage_pricing", "record_items"]
bad = 0
for n in names:
    path = pathlib.Path("process-audit") / (n + ".py")
    src = path.read_text(encoding="utf-8")
    sizes = function_sizes(src)
    biggest = max(sizes, key=lambda s: s[2])
    over = [s for s in sizes if s[2] > 110]
    lines = file_lines(src)
    print(f"{n}: {lines} lines, largest function {biggest[0]} {biggest[2]}, over110={over}, file_over_1200={lines > 1200}")
    bad += len(over) + (lines > 1200)
print("violations", bad)

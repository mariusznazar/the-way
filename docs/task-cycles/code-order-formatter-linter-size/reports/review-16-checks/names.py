import re, sys
sys.path.insert(0, "process-audit"); sys.dont_write_bytecode = True
import audit_count
src = open("process-audit/test_audit_count.py", encoding="utf-8").read()
names = sorted(set(re.findall(r"audit_count\.([A-Za-z_][A-Za-z_0-9]*)", src)))
print(len(names))
for n in names:
    if not hasattr(audit_count, n): print("MISSING", n)
# names reachable but not defined in audit_count module itself and not in __all__
for n in names:
    o = getattr(audit_count, n, None)
    mod = getattr(o, "__module__", None)
    if mod and mod != "audit_count" and n not in audit_count.__all__:
        print("via import (not in __all__):", n, mod)

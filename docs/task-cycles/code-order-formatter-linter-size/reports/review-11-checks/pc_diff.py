import sys, json, random
root = sys.argv[1]
sys.path.insert(0, root + "/project-level")
sys.path.insert(0, root + "/elements/common")
sys.path.insert(0, root)
import plan_check
sys.path.insert(0, ".runs/review-11/wt/project-level")
import importlib.util
spec = importlib.util.spec_from_file_location("tpc", root + "/project-level/test_plan_check.py")
tpc = importlib.util.module_from_spec(spec); spec.loader.exec_module(tpc)
plan, dfn, fp = tpc.PLAN, tpc.DEFINITION, tpc.FINGERPRINT
rnd = random.Random(7)
cases = [(plan, dfn, None), (plan, None, "gone"), (plan, None, None), ("", dfn, None)]
lines = plan.splitlines(keepends=True)
for i in range(len(lines)):
    cases.append(("".join(lines[:i] + lines[i+1:]), dfn, None))
    cases.append(("".join(lines[:i] + [lines[i]] + lines[i:]), dfn, None))
for s in ["Status: draft", "Status: handed over 2026-02-30", "Status: handed over 2026-10-04", "Status: bogus", "Status: handed over 2026-10-04 "]:
    cases.append(("\n".join(s if l.startswith("Status:") else l for l in plan.split("\n")), dfn, None))
cases.append((plan.replace(fp, "deadbeef"), dfn, None))
cases.append((plan, dfn.replace("- Definition fingerprint: " + fp, ""), None))
cases.append((plan, dfn.replace("- Definition fingerprint: " + fp, "- Definition fingerprint: 00000000"), None))
cases.append((plan, dfn + "\nextra", None))
dl = dfn.splitlines(keepends=True)
for i in range(len(dl)):
    cases.append((plan, "".join(dl[:i] + dl[i+1:]), None))
for _ in range(600):
    t = list(plan); 
    for _ in range(rnd.randint(1,3)):
        p = rnd.randrange(len(t)); t[p] = rnd.choice("abc# |-:\n0é")
    cases.append(("".join(t), dfn, None))
out = [[str(f) for f in plan_check.check(*c)] for c in cases]
json.dump(out, open(sys.argv[2], "w"))
print(len(cases), len({json.dumps(o) for o in out}))

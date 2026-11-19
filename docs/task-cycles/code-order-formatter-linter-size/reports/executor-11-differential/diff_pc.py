import importlib.util, sys, random
from pathlib import Path
old_dir = Path(".runs/executor-11/old/project-level").resolve()
new_dir = Path("project-level").resolve()
def load(name, d):
    sys.path.insert(0, str(d))
    spec = importlib.util.spec_from_file_location(name, d / "plan_check.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    sys.path.pop(0)
    return m
old = load("pc_old", old_dir); new = load("pc_new", new_dir)
sys.path.insert(0, str(new_dir))
import test_plan_check as t
def run(mod, plan, definition, err=None):
    return [str(f) for f in mod.check(plan, definition, err)]
cases = 0; diffs = 0; nonempty = set()
def compare(plan, definition, err=None):
    global cases, diffs
    cases += 1
    a, b = run(old, plan, definition, err), run(new, plan, definition, err)
    if a:
        nonempty.add(tuple(a))
    if a != b:
        diffs += 1; print("DIFF", a, b)
compare(t.PLAN, t.DEFINITION)
compare(t.PLAN, None, "no such file"); compare(t.PLAN, None)
rng = random.Random(7)
plines = t.PLAN.split("\n"); dlines = t.DEFINITION.split("\n")
for i in range(len(plines)):
    compare("\n".join(plines[:i] + plines[i+1:]), t.DEFINITION)
    compare("\n".join(plines[:i] + [plines[i]] + plines[i:]), t.DEFINITION)
for i in range(len(dlines)):
    compare(t.PLAN, "\n".join(dlines[:i] + dlines[i+1:]))
    compare(t.PLAN, "\n".join(dlines[:i] + [dlines[i]] + dlines[i:]))
# header variants
head_variants = ["Status: draft", "Status: handed over 2026-02-30", "Status: handed over 2026-10-02", "Status: nonsense", "", "Status:  draft"]
for v in head_variants:
    for i, l in enumerate(plines):
        if l.startswith("Status:"):
            compare("\n".join(plines[:i] + ([v] if v else []) + plines[i+1:]), t.DEFINITION)
for fp in (t.FINGERPRINT, t.OTHER_FINGERPRINT, "XYZ", "0" * 8):
    for i, l in enumerate(plines):
        if l.startswith("Definition:"):
            compare("\n".join(plines[:i] + [l.replace(t.FINGERPRINT, fp)] + plines[i+1:]), t.DEFINITION)
for fp in (t.FINGERPRINT, t.OTHER_FINGERPRINT):
    compare(t.PLAN, t.definition(approval_fingerprint=fp)); compare(t.PLAN, t.definition(status="Status: draft"))
# random char mutations in header region of plan and definition
for _ in range(1500):
    p = list(t.PLAN); d = list(t.DEFINITION)
    for _ in range(rng.randint(1, 3)):
        tgt = p if rng.random() < .5 else d
        n = min(len(tgt), 900) if tgt is p else len(tgt)
        k = rng.randrange(n) if rng.random() < .8 else rng.randrange(len(tgt))
        op = rng.random()
        if op < .4: del tgt[k]
        elif op < .8: tgt[k] = rng.choice("0123456789abcdefXYZ-|—\n :#`")
        else: tgt.insert(k, rng.choice("\n 9a—"))
    compare("".join(p), "".join(d))
print("cases", cases, "diffs", diffs, "distinct nonempty outputs", len(nonempty))

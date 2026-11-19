import importlib.util, random, sys
sys.dont_write_bytecode = True
def load(name, path, dirs):
    for d in dirs:
        sys.path.insert(0, d)
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    for d in dirs:
        sys.path.remove(d)
    return m
old = load("old_ac", ".runs/review-15/oldroot/process-audit/audit_count.py", [".runs/review-15/oldroot/process-audit"])
for k in [k for k in sys.modules if k in ("stage_pricing", "record_items", "remarks_check")]:
    pass
for k in ("stage_pricing", "record_items", "remarks_check"):
    sys.modules.pop(k, None)
new = load("new_ac", "process-audit/audit_count.py", ["process-audit"])
rr = sys.modules["record_reading"]
cols = ["Started (UTC)", "Exit code", "Total seconds", "Other gate runs at the same time", "Directory", "Directory seconds"]
rnd = random.Random(15)
def cellfor(c):
    r = rnd.random()
    if c == "Started (UTC)":
        return rnd.choice(["2026-01-02 03:04:05.678", "bad", "unknown", "2026-01-02 03:04:05.678"])
    if c == "Exit code": return rnd.choice(["0", "1", "x", "unknown", "0"])
    if c == "Total seconds": return rnd.choice(["12.345", "1.5", "z", "unknown"])
    if c.startswith("Other"): return rnd.choice(["0", "1", "q"])
    if c == "Directory": return rnd.choice(["gate", "a", "a", "b", "—", "x"*300, "c"])
    return rnd.choice(["1.000", "2.5", "nan", "—", "unknown"])
def gen():
    cs = list(cols)
    if rnd.random() < 0.15: cs.remove(rnd.choice(cs))
    if rnd.random() < 0.1: rnd.shuffle(cs)
    lines = []
    if rnd.random() < 0.1: lines.append("```")
    if rnd.random() < 0.8:
        lines.append("| " + " | ".join(cs) + " |")
        lines.append("|" + "---|" * len(cs))
    n = rnd.choice([0, 1, 3, 10, 60, 520]) if rnd.random() < 0.3 else rnd.randint(0, 12)
    base = [cellfor(c) for c in cs]
    for i in range(n):
        if rnd.random() < 0.5: base = [cellfor(c) for c in cs]
        row = list(base)
        row[cs.index("Directory")] if "Directory" in cs else None
        if "Directory" in cs: row[cs.index("Directory")] = rnd.choice(["a", "b", "a", "—", "d%d" % i])
        if rnd.random() < 0.08: row = row + ["extra"]
        lines.append("| " + " | ".join(row) + " |")
        if rnd.random() < 0.03: lines.append("text")
    if rnd.random() < 0.1: lines.append("```")
    if rnd.random() < 0.15: lines.append("| late | row |")
    return "\n".join(lines) + ("\n" if rnd.random() < .8 else "")
def mk(mod, text, reason):
    C = mod.Cycle if hasattr(mod, "Cycle") else rr.Cycle
    c = C("r", "f", "abc", "unknown")
    mod.read_gate(c, text, reason)
    return (c.unknown, c.missing, c.missing_in, c.gate_runs, [(g.others, g.total, g.code, g.directories) for g in c.gate_timed])
bad = 0
N = 4000
for i in range(N):
    t = gen()
    if i % 50 == 0: t = None
    a = mk(old, t, "no file"); b = mk(rr, t, "no file")
    if a != b:
        bad += 1
print("cases", N, "different", bad)
rnd = random.Random(15)
st = {"runs": 0, "missing": 0, "cut": 0, "late": 0, "wide": 0}
for i in range(N):
    r = mk(rr, gen(), "x")
    if r[3]: st["runs"] += 1
    if r[2]: st["missing"] += 1
    if any("more than" in b for a, b in r[0]): st["cut"] += 1
    if any("after a line" in b for a, b in r[0]): st["late"] += 1
    if any("cells, not" in b for a, b in r[0]): st["wide"] += 1
print(st)
hdr = "| " + " | ".join(cols) + " |\n|---|---|---|---|---|---|\n"
t1 = hdr + "".join(f"| 2026-01-02 03:04:05.{i%1000:03d} | 0 | 1.000 | 0 | gate | 1.000 |\n" for i in range(530))
t2 = hdr + "".join(f"| 2026-01-02 03:04:05.678 | 0 | 1.000 | 0 | d{i} | 1.000 |\n" for i in range(70))
t3 = hdr + "".join(f"| 2026-01-02 03:04:05.678 | 0 | 1.000 | 0 | d{i%3} | 1.000 |\n" for i in range(10)) + "x\n| 2026 | 0 |\n"
for t in (t1, t2, t3):
    a = mk(old, t, "x"); b = mk(rr, t, "x")
    print(a == b, [x for x in b[0]][:3])

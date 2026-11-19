import importlib.util, random, sys
sys.dont_write_bytecode = True
def load(name, path, extra):
    sys.path.insert(0, extra)
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    sys.path.remove(extra)
    return mod
old = load('old_ac', '.runs/executor-15/old/audit_count.py', '.runs/executor-15/old')
# the new modules need their own siblings: process-audit
for n in ('stage_pricing', 'record_items', 'remarks_check'):
    sys.modules.pop(n, None)
new = load('record_reading', 'process-audit/record_reading.py', 'process-audit')

COLS = ["Started (UTC)", "Exit code", "Total seconds", "Other gate runs at the same time", "Directory", "Directory seconds"]
random.seed(7)
def row(cells): return "| " + " | ".join(cells) + " |"
def make():
    cols = COLS[:]
    if random.random() < 0.15:
        cols.remove(random.choice(cols))
    if random.random() < 0.1:
        cols.reverse()
    lines = ["# Gate times", ""]
    if random.random() < 0.05:
        return "\n".join(lines) + "\nno table\n"
    if random.random() < 0.1:
        lines += ["```", row(cols), "```"]
    lines += [row(cols), row(["---"] * len(cols))]
    n = random.choice([0, 1, 2, 3, 5, 520])
    for i in range(n):
        key = [random.choice(["2026-01-02 03:04:05.678", "bad", "unknown"]), random.choice(["0", "1", "x", "unknown"]),
               random.choice(["12.345", "1.2", "unknown"]), random.choice(["0", "2", "z"])]
        for d in range(random.choice([0, 1, 2, 3, 55])):
            dirn = random.choice(["gate/a", "gate/b", "—", "x" * 300])
            secs = random.choice(["1.5", "—", "bad", "unknown", "7"])
            cells = key + [dirn, secs]
            if random.random() < 0.05: cells = cells[:-1]
            if len(cols) != len(COLS):
                cells = cells[:len(cols)]
            lines.append(row(cells))
        if random.random() < 0.05:
            lines.append(row(["a", "b"]))
    if random.random() < 0.2:
        lines += ["", "A note.", row(["a"] * len(cols))]
    return "\n".join(lines) + "\n"
count = 0
for i in range(3000):
    text = make()
    for t, why in ((text, None), (None, "no file because test")):
        a = old.Cycle("r", "f", "c", "2026-01-01")
        b = new.Cycle("r", "f", "c", "2026-01-01")
        old.read_gate(a, t, why); new.read_gate(b, t, why)
        fa = (a.unknown, a.missing, a.missing_in, a.gate_runs, [(g.others, g.total, g.directories, g.code) for g in a.gate_timed])
        fb = (b.unknown, b.missing, b.missing_in, b.gate_runs, [(g.others, g.total, g.directories, g.code) for g in b.gate_timed])
        assert fa == fb, (text, fa, fb)
        count += 1
print("compared", count, "gate texts: identical")

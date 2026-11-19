import os, re, shutil, subprocess, sys, time
from pathlib import Path

root = Path(sys.argv[1])
old = sys.argv[2]
new = sys.argv[3]
DAY = 86400000


def make(reg, now):
    reg.mkdir(parents=True)
    names = [
        f"{now-1000}_{now+3*DAY}_badend.run",
        f"{now+3*DAY}_running_badstart.run",
        f"{now-1000}_{now-5000}_endbeforestart.run",
        f"{now-2*DAY}_{now-2*DAY+1000}_old.run",
        f"{now-1000}_running_valid.run",
        f"{now-90000}_{now+30000}_near.run",
        "junk.txt",
        f"{now-7*DAY}_running_stale.run",
        "12_x.run",
    ]
    for n in names:
        (reg / n).touch()


def norm(text):
    return re.sub(r"\d{10,}", "T", text)


def run(script, case, cmd, now):
    d = root / case
    shutil.rmtree(d, ignore_errors=True)
    reg = d / "reg"
    make(reg, now)
    out = d / "rec.md"
    p = subprocess.run(
        [sys.executable, "-B", script, "--output", str(out), "--registry", str(reg), "--", *cmd],
        capture_output=True, text=True, cwd=str(d.parent),
    )
    rec = norm(out.read_text(encoding="utf-8")) if out.exists() else None
    rows = None
    if rec:
        rows = [l for l in rec.splitlines() if l.startswith("|")]
        rows = [re.sub(r"\d+\.\d{3}", "S", r) for r in rows]
    files = sorted(norm(n) for n in os.listdir(reg))
    return p.returncode, norm(p.stdout), norm(p.stderr), rows, files


ok = ["python", "-c", "print('== a'); print('Ran 1 test in 0.1s')"]
bad = ["python", "-c", "import sys; print('== a'); print('Ran 1 test in 0.1s'); sys.exit(3)"]
missing = ["definitely-not-a-command-xyz"]
mism = 0
for case, cmd in (("ok", ok), ("bad", bad), ("missing", missing)):
    now = int(time.time() * 1000)
    a = run(old, case + "_old", cmd, now)
    b = run(new, case + "_new", cmd, now)
    same = a == b
    print(case, "SAME" if same else "DIFF", a[0], b[0])
    if not same:
        mism += 1
        print(a)
        print(b)
print("mismatches", mism)

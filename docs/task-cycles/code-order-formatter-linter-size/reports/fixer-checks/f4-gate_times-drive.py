import subprocess, sys, time, os, shutil
from pathlib import Path
base = Path(sys.argv[1]); script = Path(sys.argv[2]); tag = sys.argv[3]
reg = base / ("reg_" + tag); shutil.rmtree(reg, ignore_errors=True); reg.mkdir()
now = int(time.time() * 1000)
H = 3600 * 1000
names = [
    f"{now-5000}_running_aaaa.run",            # running, counts
    f"{now-3000}_{now+30000}_bbbb.run",        # ended after this run started, counts
    f"{now-3*H}_{now-2*H}_cccc.run",           # ended long before, does not count, kept
    f"{now-30*H}_{now-29*H}_dddd.run",         # over a day old, deleted
    f"{now-7*H}_running_eeee.run",             # running over six hours, deleted
    f"{now-1000}_{now-5000}_ffff.run",         # end before start, deleted
    f"{now+10*60*1000}_running_gggg.run",      # start in the future, deleted
    "notes.txt",                               # another form, left alone
    "123_456_xx.run",                          # old ended, deleted
]
for n in names: (reg / n).write_bytes(b"")
out = base / ("record_" + tag + ".md")
if out.exists(): out.unlink()
out.write_bytes(b"")
p = subprocess.run([sys.executable, "-B", str(script), "--output", str(out), "--registry", str(reg), "--", sys.executable, "-c", "print('== dir1'); print('Ran 3 tests in 0.5s'); raise SystemExit(3)"], capture_output=True)
print(tag, "exit", p.returncode, "stdout", p.stdout.decode().split())
print("stderr", p.stderr.decode())
print("registry left", sorted(x for x in os.listdir(reg) if "running" not in x or x.endswith("aaaa.run")))
rows = [l for l in out.read_text(encoding="utf-8").splitlines() if l.startswith("| 20")]
print("others/code cells", [r.split("|")[2:5] + r.split("|")[5:6] for r in rows])

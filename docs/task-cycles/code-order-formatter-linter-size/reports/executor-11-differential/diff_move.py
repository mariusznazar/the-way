import os, stat, shutil, subprocess, sys
from pathlib import Path
exec(open(".runs/executor-11/diff_install.py", encoding="utf-8").read().split("scenarios = {")[0])
res = {}
for script in ("install_old.py", "install.py"):
    p = base / ("move_" + script.replace(".py", "")) / "product"
    product(p, s_fresh)
    seq = [run(script, p, ["--apply"], "y\n")]
    git(p, "add", "-A"); git(p, "commit", "-qm", "installed")
    older = git(wt, "rev-parse", "HEAD~1").strip()
    git(p / ".the-way", "fetch", "-q", "origin", older) if False else None
    git(p / ".the-way", "checkout", "-q", "--detach", older)
    git(p, "add", ".the-way"); git(p, "commit", "-qm", "pin older")
    (p / ".the-way" / "scratch.txt").write_text("untracked\n")
    seq += [run(script, p, [], ""), tree(p), run(script, p, ["--apply"], "y\n"), tree(p)]
    res[script] = seq
print("same" if res["install_old.py"] == res["install.py"] else "DIFF")
for r in res["install.py"][1::2][:1]: pass
print(res["install.py"][1][1][:400])

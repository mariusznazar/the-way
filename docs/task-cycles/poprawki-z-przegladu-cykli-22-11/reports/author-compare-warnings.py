import subprocess, sys, re, collections
repos = sys.argv[1:]
for repo in repos:
    out = {}
    for name, script in (("base", ".runs/author/base_ci.py"), ("head", "instruction-files/check_instructions.py")):
        r = subprocess.run([sys.executable, "-B", script, repo], capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=300)
        out[name] = [l for l in r.stdout.splitlines() if l.startswith(("WARN", "ERROR", "INFO  dead", "INFO  read"))]
    bw = [l for l in out["base"] if l.startswith("WARN")]
    hw = [l for l in out["head"] if l.startswith("WARN")]
    newwarn = [l for l in hw if l not in bw]
    # info lines new on head
    binfo = set(out["base"]); newinfo = [l for l in out["head"] if l not in binfo and l.startswith("INFO")]
    kinds = collections.Counter(re.sub(r"^INFO\s+dead-path\s+\S+\s+", "", l).split("` ", 1)[-1][:60] for l in newinfo)
    print(repo.split("\\")[-1].split("/")[-1], "base warn", len(bw), "head warn", len(hw), "new warn", len(newwarn), "new info", len(newinfo), dict(kinds))
    for l in newwarn[:3]: print("   NEWWARN", l[:150])

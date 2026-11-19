import os, stat, shutil, subprocess, sys, hashlib
from pathlib import Path
wt = Path(".").resolve()
base = wt / ".runs/executor-11/inst"
env = dict(os.environ, GIT_CONFIG_NOSYSTEM="1", GIT_TERMINAL_PROMPT="0", GIT_AUTHOR_NAME="F", GIT_AUTHOR_EMAIL="f@example.invalid", GIT_COMMITTER_NAME="F", GIT_COMMITTER_EMAIL="f@example.invalid", PYTHONIOENCODING="utf-8")
def git(d, *a):
    r = subprocess.run(["git", "-C", str(d), *a], env=env, capture_output=True, text=True, encoding="utf-8")
    assert r.returncode == 0, r.stderr
    return r.stdout
def tree(d):
    out = {}
    for p in sorted(Path(d).rglob("*")):
        if ".git" in p.relative_to(d).parts or p.is_dir(): continue
        rel = p.relative_to(d).as_posix()
        if rel.startswith(".the-way/"): continue
        out[rel] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out
def product(where, setup):
    def force(f, path, exc):
        os.chmod(path, stat.S_IWRITE); f(path)
    shutil.rmtree(where, onerror=force) if where.exists() else None
    where.mkdir(parents=True)
    git(where, "init", "-q", "--initial-branch=main")
    (where / "README.md").write_text("x\n")
    setup(where)
    git(where, "add", "-A"); git(where, "commit", "-qm", "init")
def run(script, product_dir, args, stdin):
    r = subprocess.run([sys.executable, "-B", str(wt / "installation" / script), str(product_dir), "--url", str(wt), *args], env=env, input=stdin, capture_output=True, text=True, encoding="utf-8")
    norm = lambda t: t.replace(str(product_dir), "P").replace("\\", "/").replace(str(product_dir).replace("\\", "/"), "P")
    return r.returncode, norm(r.stdout), norm(r.stderr)
def s_fresh(w): pass
def s_agents(w): (w / "AGENTS.md").write_text("# mine\r\nline\r\n"); (w / ".gitignore").write_bytes(b"node_modules\r\n"); (w / "CLAUDE.md").write_text("no import\n")
def s_ignored(w): (w / ".gitignore").write_text(".claude/\n.the-way\n")
def s_stale(w):
    d = w / ".claude/skills/the-way-gone"; d.mkdir(parents=True)
    (d / "SKILL.md").write_text("---\nname: the-way-gone\ndescription: x Use this product's pinned the-way commit.\n---\n\nThe process for this repository is pinned as the Git submodule `.the-way`, at the commit its gitlink records.\n")
    a = w / ".claude/agents"; a.mkdir(parents=True)
    (a / "the-way-old.md").write_text("---\nname: the-way-old\ndescription: x Dispatched only by the task cycle of the-way.\n---\nbody\n")
    (w / "AGENTS.override.md").write_text("o\n")
def s_marker_bad(w): (w / "AGENTS.md").write_text("<!-- the-way:begin -->\nx\n")
scenarios = {"fresh": s_fresh, "agents": s_agents, "ignored": s_ignored, "stale": s_stale, "markerbad": s_marker_bad}
diffs = 0; n = 0
for name, setup in scenarios.items():
    results = {}
    for script in ("install_old.py", "install.py"):
        p = base / script.replace(".py", "") / "product"
        product(p, setup)
        seq = []
        for args, stdin in (([], ""), (["--apply"], "n\n"), (["--apply"], "y\n"), (["--apply"], "y\n"), ([], "")):
            seq.append(run(script, p, args, stdin))
            seq.append(tree(p))
        results[script] = seq
    n += 1
    if results["install_old.py"] != results["install.py"]:
        diffs += 1; print("DIFF in", name)
        for a, b in zip(results["install_old.py"], results["install.py"]):
            if a != b: print(a, b); break
    else:
        print(name, "same; exit codes", [r[0] for r in results["install.py"][::2]], "files", len(results["install.py"][5]))
# error paths
for label, args in (("notdir", [str(base / "nonexistent")]), ):
    outs = [subprocess.run([sys.executable, "-B", str(wt / "installation" / s), *args], env=env, capture_output=True, text=True) for s in ("install_old.py", "install.py")]
    same = (outs[0].returncode, outs[0].stdout, outs[0].stderr) == (outs[1].returncode, outs[1].stdout, outs[1].stderr)
    print(label, same, outs[1].returncode); n += 1; diffs += not same
p = base / "cred" / "product"; product(p, s_fresh)
outs = [subprocess.run([sys.executable, "-B", str(wt / "installation" / s), str(p), "--url", "https://user:pw@example.invalid/x.git"], env=env, capture_output=True, text=True) for s in ("install_old.py", "install.py")]
same = [(o.returncode, o.stdout, o.stderr) for o in outs[:1]] == [(o.returncode, o.stdout, o.stderr) for o in outs[1:]]
print("credentials", same, outs[1].returncode); n += 1; diffs += not same
print("scenarios", n, "diffs", diffs)

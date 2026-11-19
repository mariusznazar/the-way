"""usage: run_cases.py <tag> <code root>; runs the cases of the audit command; saves stdout, stderr, exit, results."""
import json, pathlib, shutil, subprocess, sys
base = pathlib.Path(__file__).resolve().parent
tag, code = sys.argv[1], pathlib.Path(sys.argv[2]).resolve()
out = base / f"cases-{tag}"
shutil.rmtree(out, ignore_errors=True); out.mkdir()
def locations(name, register, results):
    p = base / f"loc-{tag}-{name}.json"
    p.write_text(json.dumps({"the-way": {"repository": (base / "clone").as_posix(),
        "problem_register": register.as_posix(), "audit_results": results.as_posix()}}), encoding="utf-8")
    return p
def run(name, loc, repo="the-way"):
    p = subprocess.run([sys.executable, "-B", str(code / "process-audit/audit_count.py"), "--locations", str(loc),
                        "--repository", repo, "--today", "2026-11-19"], capture_output=True, cwd=str(code))
    (out / f"{name}.out").write_bytes(p.stdout.replace(str(code).encode(), b"<CODE>"))
    (out / f"{name}.err").write_bytes(p.stderr.replace(str(code).encode(), b"<CODE>"))
    (out / f"{name}.exit").write_text(str(p.returncode))
for name, register in (("template", base / "clone/process-audit/problem_register.md"), ("crafted", base / "register-crafted.md")):
    if not register.exists():
        continue
    res = out / f"results-{name}"; res.mkdir()
    run(name, locations(name, register, res))
    for f in res.iterdir():
        shutil.copy(f, out / f"{name}-{f.name}")
blocked = out / "results-blocked"; (blocked / ".count-2026-11-19.md.tmp").mkdir(parents=True)
run("blocked", locations("blocked", base / "clone/process-audit/problem_register.md", blocked))
run("nokey", locations("nokey", base / "clone/process-audit/problem_register.md", out / "results-nokey"), repo="nosuch")

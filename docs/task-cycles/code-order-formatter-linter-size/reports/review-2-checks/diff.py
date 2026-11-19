import subprocess, sys, os, re, json
HERE = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
BASE = HERE + "/base"; HEAD = HERE + "/head"; IN = HERE + "/inputs"
tmp = HERE + "/outputs"; os.makedirs(tmp, exist_ok=True)
cases = {
 "gate_times": [
  ["task-cycle/gate_times.py"],
  ["task-cycle/gate_times.py", "--output", tmp + "/gt1.tsv", "--"],
  ["task-cycle/gate_times.py", "--output", IN, "--", "python", "-c", "print(1)"],
  ["task-cycle/gate_times.py", "--output", tmp + "/gt2.tsv", "--registry", IN + "/bad.json", "--", "python", "-c", "import sys; sys.exit(3)"],
  ["task-cycle/gate_times.py", "--output", tmp + "/gt3.tsv", "--registry", IN + "/garbage.md", "--", "python", "-c", "print('ok')"],
  ["task-cycle/gate_times.py", "--bogus", "--", "x"],
 ],
 "check_instructions": [
  ["instruction-files/check_instructions.py", IN + "/repo"],
  ["instruction-files/check_instructions.py", IN + "/nonexistent"],
  ["instruction-files/check_instructions.py", "//server/share/x"],
  ["instruction-files/check_instructions.py", "--file", IN + "/garbage.md"],
  ["instruction-files/check_instructions.py", "--file", IN + "/crlf.md", "--file", IN + "/long.md"],
  ["instruction-files/check_instructions.py", "--file", "//server/share/f.md"],
 ],
 "readiness_check": [],
 "plan_check": [],
 "plan_state": [],
 "cycle": [],
 "audit_count": [
  ["process-audit/audit_count.py", "--locations", IN + "/bad.json", "--prices", IN + "/bad.json"],
  ["process-audit/audit_count.py", "--locations", IN + "/missing.json"],
  ["process-audit/audit_count.py", "--locations", IN + "/garbage.md"],
  ["process-audit/audit_count.py", "--today", "2026-13-45"],
  ["process-audit/audit_count.py", "--locations", IN + "/empty.md"],
 ],
 "install": [
  ["installation/install.py", IN + "/nonexistent"],
  ["installation/install.py", IN + "/home"],
  ["installation/install.py", IN + "/gitrepo", "--url", "ext::sh -c id"],
  ["installation/install.py", IN + "/gitrepo", "--url", "file:///x"],
 ],
}
for f in ["empty.md", "garbage.md", "crlf.md", "long.md", "seven.md", "bad.json"]:
    for mode in [[], ["--before-approval"], ["--fingerprint"]]:
        cases["readiness_check"].append(["project-level/readiness_check.py", IN + "/" + f] + mode)
    cases["plan_check"].append(["project-level/plan_check.py", IN + "/" + f])
    cases["plan_state"].append(["project-level/plan_state.py", IN + "/" + f, IN + "/gitrepo"])
cases["plan_check"].append(["project-level/plan_check.py", IN + "/nonexistent.md"])
cases["plan_state"].append(["project-level/plan_state.py", IN + "/crlf.md", IN + "/nonexistent"])
cases["plan_state"].append(["project-level/plan_state.py", IN + "/crlf.md", IN + "/home"])
for script in ["cycle_stages", "cycle_measures"]:
    for extra in [[IN + "/bad.jsonl"], [IN + "/empty.jsonl"], [IN + "/nonexistent.jsonl"], ["--output", tmp + "/x.md", IN + "/bad.jsonl"], ["../../etc/passwd"], [IN + "/garbage.md"]]:
        cases["cycle"].append(["task-cycle/%s.py" % script, "--codex-home", IN + "/home", "--claude-home", IN + "/home"] + extra)
def run(root, cmd):
    cmd = [cmd[0].replace(cmd[0], root + "/" + cmd[0])] + cmd[1:]
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONIOENCODING="utf-8", HOME=IN + "/home", USERPROFILE=IN + "/home", CLAUDE_CONFIG_DIR=IN + "/home", CODEX_HOME=IN + "/home")
    p = subprocess.run([sys.executable, "-B"] + cmd, capture_output=True, cwd=IN + "/home", env=env, timeout=120)
    norm = lambda b: b.decode("utf-8", "replace").replace(root, "<ROOT>").replace(root.replace("/", "\\"), "<ROOT>")
    # line numbers inside tracebacks are expected to differ; none expected
    sha = lambda s: re.sub(r"(6c13454c|015ce05c)[0-9a-f]*", "<SHA>", s)
    return p.returncode, sha(norm(p.stdout)), sha(norm(p.stderr))
total = diffs = 0
log = []
for name, lst in cases.items():
    for cmd in lst:
        a = run(BASE, cmd); b = run(HEAD, cmd)
        total += 1
        tb = "Traceback" in a[2] or "Traceback" in b[2]
        same = a == b
        if not same: diffs += 1
        log.append({"cmd": " ".join(cmd).replace(IN, "<IN>").replace(tmp, "<OUT>"), "exit": [a[0], b[0]], "same": same, "traceback": tb, "stderr0": a[2][:160]})
        if not same:
            print("DIFF", log[-1]["cmd"]); print(a); print(b)
open(HERE + "/diff-log.json", "w", encoding="utf-8").write(json.dumps(log, indent=1))
print("cases", total, "diffs", diffs)

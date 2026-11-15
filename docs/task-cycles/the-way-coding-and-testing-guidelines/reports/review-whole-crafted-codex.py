import json, os, subprocess, sys, shutil
ROOT = os.path.abspath(".runs/review-whole-2/crafted")
SCRIPT = os.path.abspath("task-cycle/cycle_stages.py")
def run(name, lines, raw=False):
    home = os.path.join(ROOT, "home_" + name)
    shutil.rmtree(home, ignore_errors=True)
    d = os.path.join(home, "sessions", "2026", "10", "06")
    os.makedirs(d)
    path = os.path.join(d, "rollout-2026-10-06T10-00-00-orchf.jsonl")
    with open(path, "wb") as h:
        for l in lines:
            h.write((l if isinstance(l,str) else json.dumps(l)).encode("utf-8") + b"\n")
    out = os.path.join(ROOT, "out_" + name + ".md")
    p = subprocess.run([sys.executable, "-B", SCRIPT, "orchf", "--codex-home", home, "--claude-home", os.path.join(ROOT, "noclaude"), "--output", out], capture_output=True, text=True)
    print(name, "exit", p.returncode, "| stderr:", p.stderr.strip().splitlines()[-1] if p.stderr.strip() else "", "| out exists:", os.path.exists(out))
meta = {"timestamp": "2026-10-06T10:00:00Z", "type": "session_meta", "payload": {"id": "orchf"}}
ok_tokens = {"timestamp": "2026-10-06T10:00:30Z", "type": "token_usage_record", "payload": {"thread_id": "orchf", "turn_id": "o1", "usage": {"input_tokens": 1, "cached_input_tokens": 0, "output_tokens": 1}}}
run("list_first", [ [1,2]])
run("number_first", [5])
run("null_first", [None])
run("string_first", ["x"])
run("list_later", [meta, [1]])
run("string_later", [meta, "abc"])
run("null_payload", [meta, {"timestamp": "2026-10-06T10:00:10Z", "payload": None}])
run("deep", [meta, "[" * 100000 + "]" * 100000], raw=True)
run("bighex", [meta, '{"timestamp": "2026-10-06T10:00:10Z", "payload": {"x": ' + "9" * 5000 + '}}'], raw=True)
run("nan", [meta, '{"timestamp": "2026-10-06T10:00:10Z", "payload": {"x": NaN}}'], raw=True)
run("tskind", [meta, {"timestamp": {"a":1}, "payload": {}}])
run("ts_naive_mix", [meta, dict(ok_tokens, timestamp="2026-10-06T10:00:30")])
run("ts_zsep", [meta, dict(ok_tokens, timestamp="2026-10-06Z10:00:30")])
run("turn_list", [meta, dict(ok_tokens, payload=dict(ok_tokens["payload"], turn_id=["a"]))])
run("good", [meta, ok_tokens])

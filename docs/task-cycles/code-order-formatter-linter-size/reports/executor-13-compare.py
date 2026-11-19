"""Runs the old and the new cycle_stages.py on crafted transcripts and compares exit code, stdout and
stderr. The old script is the one at the slice's base; the new one is the worktree's."""

import copy
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path("the worktree's root")
WORK = ROOT / ".runs/executor-13/inputs"
OLD = ROOT / ".runs/executor-13/old/cycle_stages.py"
NEW = ROOT / "task-cycle/cycle_stages.py"


def at(clock):
    return f"2026-10-06T{clock}.000Z"


def write(path, entries):
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(entries, str):
        path.write_text(entries, encoding="utf-8", newline="")
    else:
        path.write_text("".join(json.dumps(e) + "\n" for e in entries), encoding="utf-8")
    return path


def user(clock, text, **extra):
    return {"type": "user", "timestamp": at(clock), "message": {"role": "user", "content": text}, **extra}


def assistant(clock, ident, content=None, usage=None, model="claude-x", stop="end_turn"):
    if usage is None:
        usage = {
            "input_tokens": 3,
            "cache_creation_input_tokens": 5,
            "cache_read_input_tokens": 7,
            "output_tokens": 11,
            "cache_creation": {"ephemeral_5m_input_tokens": 2, "ephemeral_1h_input_tokens": 3},
        }
    return {
        "type": "assistant",
        "timestamp": at(clock),
        "uuid": ident + "u",
        "message": {
            "id": ident,
            "model": model,
            "content": content if content is not None else [{"type": "text", "text": "hi"}],
            "usage": usage,
            "stop_reason": stop,
        },
    }


def claude_good():
    return [
        user("10:00:00", "go: see reports/a_findings.md and reports/../evil.md and reports/x|y.md."),
        assistant(
            "10:00:10",
            "m1",
            [{"type": "tool_use", "id": "t1", "name": "Bash"}, {"type": "tool_use", "id": "t2", "name": "Agent"}],
            stop="tool_use",
        ),
        {
            "type": "user",
            "timestamp": at("10:00:20"),
            "message": {"role": "user", "content": [{"type": "tool_result", "tool_use_id": "t1"}]},
        },
        assistant("10:00:30", "m2", [{"type": "server_tool_use", "name": "web"}]),
    ]


def codex_meta_line(ident, clock, parent=None, path=None):
    payload = {"id": ident, "timestamp": at(clock)}
    if parent:
        payload.update(parent_thread_id=parent, agent_path=path)
    return {"timestamp": at(clock), "type": "session_meta", "payload": payload}


def ev(clock, kind, turn, **extra):
    return {"timestamp": at(clock), "type": "event_msg", "payload": {"type": kind, "turn_id": turn, **extra}}


def tok(clock, thread, turn, usage=None):
    if usage is None:
        usage = {"input_tokens": 100, "cached_input_tokens": 40, "output_tokens": 9}
    return {
        "timestamp": at(clock),
        "type": "token_usage_record",
        "payload": {"thread_id": thread, "turn_id": turn, "usage": usage},
    }


def item(clock, **payload):
    return {"timestamp": at(clock), "type": "response_item", "payload": payload}


def codex_orchestrator():
    return [
        codex_meta_line("orch", "11:00:00"),
        ev("11:00:01", "task_started", "o1"),
        ev("11:00:02", "user_message", "o1", message="hello"),
        {"timestamp": at("11:00:03"), "type": "turn_context", "payload": {"turn_id": "o1", "model": "gpt-x"}},
        item("11:00:04", type="function_call", name="exec", call_id="c1", input="tools.spawn_agent(1)"),
        item("11:00:05", type="function_call", name="shell", call_id="c2"),
        item("11:00:06", type="function_call_output", call_id="c2"),
        item("11:00:07", type="function_call", name="shell", call_id="c3"),
        item("11:00:08", type="web_search_call"),
        tok("11:00:09", "orch", "o1"),
        ev("11:00:10", "task_complete", "o1"),
    ]


def codex_sub(parent_id="orch"):
    return [
        codex_meta_line("sub", "11:01:00", parent_id, "/root/sub"),
        ev("11:01:01", "task_started", "s1"),
        item("11:01:02", type="message", role="user", content=[{"type": "input_text", "text": "see reports/s_findings.md. and reports/q.md"}]),
        {"timestamp": at("11:01:03"), "type": "turn_context", "payload": {"turn_id": "s1", "model": "gpt-y"}},
        item("11:01:04", type="custom_tool_call", name="apply_patch", call_id="d1"),
        item("11:01:05", type="custom_tool_call_output", call_id="d1"),
        tok("11:01:06", "sub", "s1"),
        tok("11:01:07", "parent-other", "zz", {"input_tokens": "bad"}),
        ev("11:01:08", "task_complete", "s1"),
        ev("11:01:09", "task_started", "s2"),
        item("11:01:10", type="agent_message", recipient="/root/sub", content=[{"type": "encrypted_content"}]),
        tok("11:01:11", "sub", "s2"),
    ]


def mutate(entries, index, fn):
    entries = copy.deepcopy(entries)
    fn(entries[index])
    return entries


CASES = []


def case(name, claude=None, codex=None, extra=None, args=None):
    CASES.append((name, claude, codex, extra, args))


def build():
    base = WORK
    for name in ("cl_good",):
        pass
    # Claude cases: each gets its own claude home with one transcript (plus a subagent for the good one)
    def claude_case(name, entries, sub=None, meta=None):
        home = base / name / "claude"
        t = write(home / "projects/p/sess.jsonl", entries)
        if sub is not None:
            write(home / "projects/p/sess/subagents/agent-a1.jsonl", sub)
            if meta is not None:
                write(home / "projects/p/sess/subagents/agent-a1.meta.json", meta)
        return [str(t), "--codex-home", str(base / name / "codex"), "--claude-home", str(home)]

    def codex_case(name, orch, sub=None):
        home = base / name / "codex"
        t = write(home / "sessions/2026/10/06/rollout-x-orch.jsonl", orch)
        if sub is not None:
            write(home / "sessions/2026/10/06/rollout-x-sub.jsonl", sub)
        return [str(t), "--codex-home", str(home), "--claude-home", str(base / name / "claude")]

    out = {}
    good = claude_good()
    out["claude_good_sub"] = claude_case(
        "claude_good_sub",
        good,
        sub=[user("10:00:05", "work on reports/r1.md"), assistant("10:00:15", "s1")],
        meta='{"description": "d | x", "agentType": "exec"}',
    )
    out["claude_good_nometa"] = claude_case("claude_good_nometa", good, sub=[user("10:00:05", "x"), assistant("10:00:15", "s1")])
    out["claude_bad_meta"] = claude_case("claude_bad_meta", good, sub=[user("10:00:05", "x"), assistant("10:00:15", "s1")], meta="{not json")
    out["claude_no_usage"] = claude_case("claude_no_usage", mutate(good, 1, lambda e: e["message"].pop("usage")))
    out["claude_no_cc"] = claude_case("claude_no_cc", mutate(good, 1, lambda e: e["message"]["usage"].pop("cache_creation")))
    out["claude_no_1h"] = claude_case("claude_no_1h", mutate(good, 1, lambda e: e["message"]["usage"]["cache_creation"].pop("ephemeral_1h_input_tokens")))
    out["claude_null_count"] = claude_case("claude_null_count", mutate(good, 1, lambda e: e["message"]["usage"].__setitem__("input_tokens", None)))
    out["claude_float_count"] = claude_case("claude_float_count", mutate(good, 1, lambda e: e["message"]["usage"].__setitem__("output_tokens", 1.5)))
    out["claude_big_count"] = claude_case("claude_big_count", mutate(good, 1, lambda e: e["message"]["usage"].__setitem__("output_tokens", 10**15)))
    out["claude_neg_count"] = claude_case("claude_neg_count", mutate(good, 1, lambda e: e["message"]["usage"].__setitem__("cache_read_input_tokens", -1)))
    out["claude_bool_count"] = claude_case("claude_bool_count", mutate(good, 1, lambda e: e["message"]["usage"].__setitem__("cache_read_input_tokens", True)))
    out["claude_bad_time"] = claude_case("claude_bad_time", mutate(good, 0, lambda e: e.__setitem__("timestamp", "yesterday")))
    out["claude_time_int"] = claude_case("claude_time_int", mutate(good, 0, lambda e: e.__setitem__("timestamp", 5)))
    out["claude_no_message"] = claude_case("claude_no_message", mutate(good, 0, lambda e: e.pop("message")))
    out["claude_no_content"] = claude_case("claude_no_content", mutate(good, 0, lambda e: e["message"].pop("content")))
    out["claude_synthetic"] = claude_case("claude_synthetic", mutate(good, 1, lambda e: (e["message"].__setitem__("model", "<synthetic>"), e["message"].pop("usage"))))
    out["claude_model_null"] = claude_case("claude_model_null", mutate(good, 3, lambda e: e["message"].__setitem__("model", None)))
    out["claude_split_mismatch"] = claude_case("claude_split_mismatch", mutate(good, 3, lambda e: e["message"]["usage"]["cache_creation"].__setitem__("ephemeral_1h_input_tokens", 99)))
    out["claude_not_json"] = claude_case("claude_not_json", '{"type":"user"}\nnot json\n')
    out["claude_deep"] = claude_case("claude_deep", '{"type":"user","timestamp":"2026-10-06T10:00:00Z","message":{"content":' + "[" * 100000 + "]" * 100000 + "}}\n")
    out["claude_empty"] = claude_case("claude_empty", "")
    out["claude_unknown_first"] = claude_case("claude_unknown_first", [ [1, 2] ])
    out["claude_non_dict_line"] = claude_case("claude_non_dict_line", [good[0], [1], "x", good[1]])
    out["claude_bad_utf8"] = None
    p = base / "claude_bad_utf8" / "claude/projects/p/sess.jsonl"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(b'{"type":"user","timestamp":"2026-10-06T10:00:00Z","message":{"content":"\xff"}}\n')
    out["claude_bad_utf8"] = [str(p), "--codex-home", str(base / "x"), "--claude-home", str(base / "x")]
    out["claude_surrogate"] = claude_case("claude_surrogate", '{"type":"user","timestamp":"2026-10-06T10:00:00Z","message":{"content":"a\\ud800 reports/s\\ud800.md reports/ok.md"}}\n' + json.dumps(good[1]) + "\n")

    # Codex cases
    orch, sub = codex_orchestrator(), codex_sub()
    out["codex_good"] = codex_case("codex_good", orch, sub)
    out["codex_no_sub"] = codex_case("codex_no_sub", orch)
    out["codex_no_id"] = codex_case("codex_no_id", mutate(orch, 0, lambda e: e["payload"].pop("id")), sub)
    out["codex_empty_id"] = codex_case("codex_empty_id", mutate(orch, 0, lambda e: e["payload"].__setitem__("id", "")), sub)
    out["codex_bad_time"] = codex_case("codex_bad_time", mutate(orch, 2, lambda e: e.__setitem__("timestamp", "nope")), sub)
    out["codex_no_time"] = codex_case("codex_no_time", mutate(orch, 2, lambda e: e.pop("timestamp")), sub)
    out["codex_tok_no_thread"] = codex_case("codex_tok_no_thread", mutate(orch, 9, lambda e: e["payload"].pop("thread_id")), sub)
    out["codex_tok_no_turn"] = codex_case("codex_tok_no_turn", mutate(orch, 9, lambda e: e["payload"].pop("turn_id")), sub)
    out["codex_tok_no_usage"] = codex_case("codex_tok_no_usage", mutate(orch, 9, lambda e: e["payload"].pop("usage")), sub)
    out["codex_tok_bad_count"] = codex_case("codex_tok_bad_count", mutate(orch, 9, lambda e: e["payload"]["usage"].__setitem__("cached_input_tokens", "3")), sub)
    out["codex_tok_no_out"] = codex_case("codex_tok_no_out", mutate(orch, 9, lambda e: e["payload"]["usage"].pop("output_tokens")), sub)
    out["codex_sub_bad_other"] = codex_case("codex_sub_bad_other", orch, mutate(sub, 6, lambda e: e["payload"]["usage"].__setitem__("input_tokens", None)))
    out["codex_sub_nonobject_payload"] = codex_case("codex_sub_nonobject_payload", orch, mutate(sub, 2, lambda e: e.__setitem__("payload", "text")))
    out["codex_line_list"] = codex_case("codex_line_list", orch[:3] + [ [1] ] + orch[3:], sub)
    out["codex_not_json"] = codex_case("codex_not_json", '{"type":"session_meta","payload":{"id":"orch"}}\nnope\n')
    out["codex_sub_as_orch"] = codex_case("codex_sub_as_orch", sub, None)
    out["codex_first_not_meta"] = codex_case("codex_first_not_meta", orch[1:], sub)
    out["codex_sub_empty"] = codex_case("codex_sub_empty", orch, "")
    out["codex_sub_nometa"] = codex_case("codex_sub_nometa", orch, sub[1:])
    out["codex_sub_open_turn"] = codex_case("codex_sub_open_turn", orch, sub[:5] + sub[6:7])
    out["codex_many_files"] = codex_case(
        "codex_many_files",
        orch,
        mutate(sub, 2, lambda e: e["payload"]["content"][0].__setitem__("text", " ".join(f"reports/r{n}.md" for n in range(30)))),
    )
    out["codex_two_orch"] = [out["codex_good"][0], str(WORK / "codex_no_sub" / "codex/sessions/2026/10/06/rollout-x-orch.jsonl"), "--codex-home", str(WORK / "codex_good" / "codex"), "--claude-home", str(WORK / "x")]
    out["mixed"] = [out["codex_good"][0], out["claude_good_sub"][0], "--codex-home", str(WORK / "codex_good" / "codex"), "--claude-home", str(WORK / "claude_good_sub" / "claude")]
    out["missing_session"] = ["nosuchid", "--codex-home", str(WORK / "x"), "--claude-home", str(WORK / "x")]
    out["by_id"] = ["orch", "--codex-home", str(WORK / "codex_good" / "codex"), "--claude-home", str(WORK / "x")]
    out["no_args"] = ["--codex-home", str(WORK / "x"), "--claude-home", str(WORK / "x")]
    return out


def run(script, args, env):
    done = subprocess.run([sys.executable, "-B", str(script), *args], capture_output=True, env=env, cwd=str(ROOT))
    return done.returncode, done.stdout, done.stderr


def main():
    import os

    if WORK.exists():
        import shutil

        shutil.rmtree(WORK)
    cases = build()
    env = {k: v for k, v in os.environ.items() if k not in ("CODEX_SESSION_ID", "CLAUDE_CODE_SESSION_ID")}
    bad = 0
    codes = {}
    for name, args in cases.items():
        o = run(OLD, args, env)
        n = run(NEW, args, env)
        # paths of the script itself do not appear in the output; compare all of it
        same = o == n
        codes[name] = o[0]
        if not same:
            bad += 1
        print(f"{'same' if same else 'DIFF'} {name} exit={o[0]}/{n[0]} out={len(o[1])}/{len(n[1])} err={len(o[2])}/{len(n[2])}")
    print("cases", len(cases), "different", bad)
    print("exit codes seen", sorted(set(codes.values())))
    # an output file too
    args = cases["claude_good_sub"] + ["--output", str(WORK / "out_old.md")]
    run(OLD, args, env)
    args = cases["claude_good_sub"] + ["--output", str(WORK / "out_new.md")]
    run(NEW, args, env)
    print("output file bytes equal", (WORK / "out_old.md").read_bytes() == (WORK / "out_new.md").read_bytes())
    # error messages, to see that the cases reach the intended branch
    for name in ("claude_no_cc", "claude_null_count", "codex_tok_bad_count", "codex_no_id", "codex_tok_no_turn", "claude_not_json"):
        code, out, err = run(NEW, cases[name], env)
        print(name, code, err.decode("utf-8", "replace").strip()[-160:].replace(str(WORK), "<W>"))


main()

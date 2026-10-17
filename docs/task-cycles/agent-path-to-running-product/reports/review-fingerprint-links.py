"""Recompute fingerprints of decisions and invariants; check every Name@fp link in the repo."""
import re, sys, subprocess, os
root = sys.argv[1]
sys.path.insert(0, os.path.join(root, "relation-model"))
from fingerprint import fingerprint

def binding(path, heading_re):
    text = open(os.path.join(root, path), encoding="utf-8", newline="").read()
    lines = text.splitlines()
    out = {}
    for i, line in enumerate(lines):
        m = re.match(heading_re, line)
        if not m:
            continue
        j = i + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        para = []
        while j < len(lines) and lines[j].strip():
            para.append(lines[j]); j += 1
        out[m.group(1)] = fingerprint("\n".join(para))
    return out

dec = binding("foundations/decisions.md", r"^### (WAY-\d+)/\d+ — ")
inv = binding("foundations/invariants.md", r"^## ([a-z0-9-]+)/\d+\s*$")
print("decisions", len(dec), "invariants", len(inv))
for k in ("WAY-121", "WAY-165", "WAY-118", "WAY-100", "WAY-106", "WAY-116", "WAY-123", "WAY-137", "WAY-122"):
    print(k, dec.get(k))
print("project-technology-record", inv.get("project-technology-record"))
files = subprocess.run(["git", "-C", root, "ls-files"], capture_output=True, text=True).stdout.split()
stale = total = 0
for f in files:
    if f.startswith(".runs") or not f.endswith((".md", ".py")):
        continue
    try:
        text = open(os.path.join(root, f), encoding="utf-8").read()
    except Exception:
        continue
    for n, line in enumerate(text.splitlines(), 1):
        for m in re.finditer(r"\b(WAY-\d+)@([0-9a-f]{8})\b", line):
            total += 1
            cur = dec.get(m.group(1))
            if cur != m.group(2):
                stale += 1
                print("STALE %s:%d %s@%s current %s" % (f, n, m.group(1), m.group(2), cur))
        for m in re.finditer(r"\b([a-z][a-z0-9-]+)@([0-9a-f]{8})\b", line):
            if m.group(1) in inv:
                total += 1
                if inv[m.group(1)] != m.group(2):
                    stale += 1
                    print("STALE-INV %s:%d %s@%s current %s" % (f, n, m.group(1), m.group(2), inv[m.group(1)]))
print("links", total, "stale", stale)

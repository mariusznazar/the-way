"""Weakest-point check: runs of N words the skill shares with the templates of guidelines and with
the binding sentences of WAY-193..WAY-212 (a restated rule shows as a long shared run)."""
import re, sys
from pathlib import Path
R = Path("/home/user/the-way")
N = int(sys.argv[1]) if len(sys.argv) > 1 else 8
def words(t): return re.findall(r"[A-Za-z0-9`'<>\-]+", t.lower())
def shingles(ws): return {tuple(ws[i:i+N]) for i in range(len(ws)-N+1)}
skill = (R/"product-guidelines/coding/SKILL.md").read_text(encoding="utf-8")
sw = words(skill)
dec = (R/"foundations/decisions.md").read_text(encoding="utf-8")
binding = []
for m in re.finditer(r"^### (WAY-(\d+))/1 — .*?\n\n(.*?)\n\n- \*\*Change", dec, re.S | re.M):
    if 193 <= int(m.group(2)) <= 212: binding.append((m.group(1), m.group(3)))
sources = [("coding/template.md", (R/"product-guidelines/coding/template.md").read_text(encoding="utf-8")),
           ("template.md", (R/"product-guidelines/template.md").read_text(encoding="utf-8"))] + binding
for name, text in sources:
    common = shingles(sw) & shingles(words(text))
    if not common: continue
    # merge into maximal runs in the skill
    runs, i = [], 0
    while i <= len(sw)-N:
        if tuple(sw[i:i+N]) in common:
            j = i
            while j+1 <= len(sw)-N and tuple(sw[j+1:j+1+N]) in common: j += 1
            runs.append(" ".join(sw[i:j+N])); i = j+N
        else: i += 1
    print(f"== {name}: {len(runs)} shared run(s) of >= {N} words")
    for r in runs: print("   -", r)

import importlib.util, random, shutil, subprocess, sys
from pathlib import Path
base = Path(".runs/executor-11").resolve()
def load(name, p):
    spec = importlib.util.spec_from_file_location(name, p)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
old = load("ci_old", base / "old/instruction-files/check_instructions.py")
new = load("ci_new", Path("instruction-files/check_instructions.py").resolve())
root = base / "ci_root"
shutil.rmtree(root, ignore_errors=True)
seeds = [
 "See `docs/real.md` and `docs/missing.md:12` and `//host/share/x.md` and `" + chr(92) * 2 + "srv" + chr(92) + "a.md`.\n",
 "The file `old/gone.md` does not exist anymore. Also `other/gone2.md` is not read; `~/nope.md` here.\n",
 "@docs/real.md\n@docs/missing.md\n@docs/real.md, and @ghost.md. @//host/s/a.md @AGENTS.md\n",
 "IMPORTANT: a\nYOU MUST b\n\n```\nCRITICAL: in fence `bad/path.md`\n```\nNEVER EVER c\n",
 "`name.md` `src/x.py` `a.b.c/d.md` `https://x.y/z.md` `/park` `*.md` `C:" + chr(92) + "Users" + chr(92) + "f.md`\n",
 "# Title\n- `dir/file.txt`\n| `a/b.json` |\n1. `c/d.ts` does not load\n",
 "Nie istnieje `pl/plik.md`, a `pl/inny.md` nie jest wczytywany.\n",
]
rng = random.Random(3)
cases = diffs = 0
def compare(r, extra=()):
    global cases, diffs
    cases += 1
    a = [str(f) for f in old.check(str(r), extra)]; b = [str(f) for f in new.check(str(r), extra)]
    if a != b: diffs += 1; print("DIFF", a[:3], b[:3])
    return a
nonempty = 0
for case in range(400):
    shutil.rmtree(root, ignore_errors=True)
    (root / "docs").mkdir(parents=True); (root / "docs/real.md").write_text("x")
    (root / "sub").mkdir(); (root / ".claude/skills/s1").mkdir(parents=True); (root / ".agents/skills/s2").mkdir(parents=True)
    (root / ".cursor/rules").mkdir(parents=True)
    def text():
        return "".join(rng.choice(seeds) for _ in range(rng.randint(1, 5)))
    (root / "AGENTS.md").write_text(text(), encoding="utf-8")
    if rng.random() < .8: (root / "CLAUDE.md").write_text(rng.choice(["@AGENTS.md\n", "x\n@AGENTS.md\n", text()]), encoding="utf-8")
    if rng.random() < .5: (root / "sub/AGENTS.md").write_text(text(), encoding="utf-8"); (root / "sub/CLAUDE.md").write_text(text(), encoding="utf-8")
    (root / ".claude/skills/s1/SKILL.md").write_text(text(), encoding="utf-8")
    (root / ".agents/skills/s2/SKILL.md").write_text(text(), encoding="utf-8")
    (root / ".cursor/rules/a.mdc").write_text(rng.choice(["---\nx: 1\n---\n", ""]) + text(), encoding="utf-8")
    (root / ".cursor/rules/b.md").write_text(text(), encoding="utf-8")
    if rng.random() < .3: (root / "CLAUDE.local.md").write_text("x")
    if rng.random() < .3: (root / "pointed.md").write_text(text(), encoding="utf-8"); (root / "AGENTS.md").write_text("see `pointed.md`\n" + text(), encoding="utf-8")
    ex = base / "extra.md"; ex.write_text(text(), encoding="utf-8")
    out = compare(root, [str(ex)] if rng.random() < .5 else ())
    nonempty += bool(out)
print(compare(None, [str(ex)]) and "none-root ok")
# BOM / invalid / big files
shutil.rmtree(root, ignore_errors=True); root.mkdir()
(root / "AGENTS.md").write_bytes(b"\xff\xfe\x00bad"); (root / "CLAUDE.md").write_bytes(b"\xef\xbb\xbf@AGENTS.md\n`x/y.md`")
compare(root)
(root / "AGENTS.md").write_bytes(b"`a/b.md` " * 200000); compare(root)
for r in (".", "../../.."):
    compare(Path(r).resolve())
# CLI: exit code and output
for args in ([str(root)], [str(base / "nonexistent")], ["--file", str(ex)], ["//host/x"], []):
    outs = []
    for script in (base / "old/instruction-files/check_instructions.py", Path("instruction-files/check_instructions.py").resolve()):
        r = subprocess.run([sys.executable, "-B", str(script), *args], capture_output=True, text=True, encoding="utf-8", cwd=str(base))
        outs.append((r.returncode, r.stdout, r.stderr))
    cases += 1
    if outs[0] != outs[1]: diffs += 1; print("CLI DIFF", args)
print("cases", cases, "diffs", diffs, "nonempty", nonempty)
shutil.rmtree(root, ignore_errors=True)

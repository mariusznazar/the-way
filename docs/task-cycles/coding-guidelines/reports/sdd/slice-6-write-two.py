"""Write only the two entry points of maintain-coding-guidelines with the generator's own
discover and produce, in process; then verify their bytes equal produce(discover(ROOT))."""
import importlib.util, sys
from pathlib import Path
ROOT = Path("/home/user/the-way")
spec = importlib.util.spec_from_file_location("sep", ROOT / "agent-instructions/skill_entry_points.py")
sep = importlib.util.module_from_spec(spec); sys.modules["sep"] = sep; spec.loader.exec_module(sep)
assert sep.ROOT == ROOT, sep.ROOT
mode = sys.argv[1]
produced = sep.produce(sep.discover(sep.ROOT))
paths = [".claude/skills/the-way-maintain-coding-guidelines/SKILL.md",
         ".agents/skills/the-way-maintain-coding-guidelines/SKILL.md"]
for p in paths:
    data = produced[p].encode("utf-8")
    target = ROOT / p
    if mode == "write":
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        print("wrote", p, len(data), "bytes")
    else:
        print(p, "equal" if target.read_bytes() == data else "DIFFERENT")

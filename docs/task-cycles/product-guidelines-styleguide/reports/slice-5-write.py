import sys
sys.path.insert(0, "agent-instructions")
import skill_entry_points as m
out = m.produce(m.discover(m.ROOT))
names = ["critique", "define-project", "find-foundation-entries", "implement-task", "lead-project"]
n = 0
for nm in names:
    for d in m.ENTRY_DIRECTORIES:
        p = f"{d}/the-way-{nm}/SKILL.md"
        assert p in out, p
        (m.ROOT / p).write_bytes(out[p].encode("utf-8"))
        n += 1
print("written", n)

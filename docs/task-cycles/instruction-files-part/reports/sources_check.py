"""Lists every bullet of a Markdown file that carries no source: a fact, an address, a
measurement, or the words saying none is established. Usage: python -B sources_check.py FILE"""
import re
import sys

text = open(sys.argv[1], encoding="utf-8").read()
bullets = re.findall(r"^- .*?(?=^- |^#|^\s*$|\Z)", text, re.M | re.S)
marks = ("(fact `", "(http", "measured", "not established", "neither documented nor measured")
missing = [bullet.splitlines()[0] for bullet in bullets if not any(m in bullet for m in marks)]
print("\n".join(missing))
print(f"{len(bullets)} bullets, {len(missing)} without a source")
sys.exit(1 if missing else 0)

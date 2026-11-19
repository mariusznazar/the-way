import pathlib, re, subprocess, sys
base = pathlib.Path(__file__).resolve().parent
root = base / "clone"
text = (root / "process-audit/problem_register.md").read_text(encoding="utf-8")
# the cycles' records: taken from a first run of the base code over the real history
count = (base / "seed" / "count-latest.md").read_text(encoding="utf-8")
section = count.split("## Cycles")[1].split("## Cost")[0]
rows = [r.strip("| ").split(" | ") for r in section.splitlines() if r.startswith("| the-way")]
records = [r[1] for r in rows]
pins = [r[5] for r in rows if r[5] != "unknown"]
assert len(records) > 10
fix_holds = pins[3]
head = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
issues = [
    ("open-one", "open", "none"), ("open-two", "open", "none"), ("open-empty", "open", "none"),
    ("open-unread", "open", "none"), ("open-refused", "open", "none"),
    ("fixed-real", "fixed", fix_holds), ("fixed-missing", "fixed", "1234567890abcdef1234567890abcdef12345678"),
    ("fixed-short", "fixed", head[:9]), ("dropped-one", "dropped", "none"),
]
def prob(repo, rec, issue, cls="process-remark", weight="Minor", cost="nothing"):
    return f"| {repo} | {rec} | author | a lapse | {cls} | {weight} | {cost} | {issue} |"
problems = [
    prob("the-way", records[0], "open-one"),
    prob("the-way", records[0], "open-one", weight="Critical", cost="human"),
    prob("the-way", records[5], "open-one", cls="confirmation", weight="no problem"),
    prob("the-way", records[7], "open-two", cls="foundation-gap", weight="Important", cost="round"),
    prob("the-way", records[9], "fixed-real", weight="Important", cost="stage"),
    prob("the-way", records[-1], "fixed-real"),
    prob("the-way", records[-2], "fixed-real"),
    prob("the-way", records[3], "fixed-missing"),
    prob("the-way", records[4], "fixed-short", cost="steps"),
    prob("the-way", records[6], "dropped-one"),
    prob("the-way", "f" * 40, "open-unread"),
    prob("other", "e" * 40, "open-unread"),
    prob("the-way", records[2], "open-refused", cls="no-such-class"),
    prob("the-way", records[2], "open-refused"),
    prob("the-way", records[8], "no-such-issue"),
    prob("the-way", records[1], "dropped-one", weight="bad-weight"),
]
iss_rows = "".join(f"| {n} | the matter | {f} | {x} |\n" for n, f, x in issues)
header_i = "| Issue | What | Fate | Fix |\n|---|---|---|---|\n"
header_p = ("| Repository | Record | Stages | What | Class | Weight | Cost of an occurrence "
            "| Issue |\n|---|---|---|---|---|---|---|---|\n")
cls = "| Class | Meaning | Added | Withdrawn |\n|---|---|---|---|\n"
assert text.count(header_i) == 1 and text.count(header_p) == 1 and text.count(cls) == 1
text = text.replace(header_i, header_i + iss_rows).replace(header_p, header_p + "".join(p + "\n" for p in problems))
text = text.replace(cls, cls + "| late-class | later | 2026-10-20 | none |\n")
(base / "register-crafted.md").write_text(text, encoding="utf-8", newline="\n")

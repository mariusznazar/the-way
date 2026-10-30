"""Rule preservation check: every sentence-sized piece of the old SKILL.md must stand in the new
files word for word, or be listed in CHANGES with its exact new wording (which must stand there)."""
import re, subprocess, sys, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[4]
BASE = "525cde1dd53c474f56ea0ece289cb60e868aa90d"
NEW_FILES = ["SKILL.md", "start.md", "list.md", "running_product.md", "settle.md", "research.md", "close.md"]


def norm(text):
    text = re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", text, flags=re.M)  # list markers
    return re.sub(r"\s+", " ", text).strip()


def pieces(text):
    body = text.split("---", 2)[2]
    body = re.sub(r"^#{1,6} .*$", "", body, flags=re.M)  # headings are rows of their own
    body = norm(body)
    parts = re.split(r"(?<=[.;:?!])\s+(?=[A-Z`\"*(])", body)
    return [p.strip() for p in parts if p.strip()]


def main():
    old = subprocess.run(["git", "-C", str(ROOT), "show", f"{BASE}:project-level/technology/SKILL.md"],
                         capture_output=True, text=True, encoding="utf-8", check=True).stdout
    new = {f: (ROOT / "project-level/technology" / f).read_text(encoding="utf-8") for f in NEW_FILES}
    joined = norm("\n".join(new.values()))
    changes_path = pathlib.Path(__file__).with_name("changes.json")
    changes = json.loads(changes_path.read_text(encoding="utf-8")) if changes_path.exists() else {}
    exact = 0
    listed = 0
    bad = []
    for p in pieces(old):
        if p in joined:
            exact += 1
        elif any(p.startswith(k) for k in changes):
            key = next(k for k in changes if p.startswith(k))
            if all(norm(n) in joined for n in changes[key]):
                listed += 1
            else:
                bad.append(("listed new wording not found", p, changes[key]))
        else:
            bad.append(("unmatched", p, None))
    out = [f"pieces exact={exact} listed={listed} problems={len(bad)}"]
    for kind, p, n in bad:
        out.append(f"{kind}: {p}")
    pathlib.Path(sys.argv[1]).write_text("\n".join(out), encoding="utf-8")
    print(out[0])
    return 1 if bad else 0


sys.exit(main())

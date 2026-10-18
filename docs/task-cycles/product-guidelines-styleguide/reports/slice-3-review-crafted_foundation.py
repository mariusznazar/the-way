"""Time the form check on a product whose decision log and invariants file hold long crafted lines
(WAY-48: the borrowed parsers now read a product's untrusted foundation)."""
import importlib.util, os, subprocess, sys, time
the_way, root = sys.argv[1], sys.argv[2]
spec = importlib.util.spec_from_file_location("t", os.path.join(the_way, "product-guidelines", "test_form_check.py"))
t = importlib.util.module_from_spec(spec); spec.loader.exec_module(t)
n = 95000
log_extra = "\n".join([
    "- **" + ":*" * n,                      # bold field, lazy name with no closing :**
    "### ABC-" + "0" * (2 * n) + "x",        # version heading, long digit run
    "## " + "/1" * n + "x",                  # heading with many /digits
    "*" + ":" * (2 * n),                     # prose field
    "A" * (2 * n) + "-",                     # prefix-like run
])
inv_extra = "\n".join([
    "## " + "a/1" * n + "x",
    "## " + "/" + "1" * (2 * n) + "x",
    "- **" + "a:*" * n,
    "| " + "a|" * n,
])
files = dict(t.FOUNDATION, **{"guidelines/testing.md": t.TESTING})
files["foundations/decisions.md"] = t.LOG + "\n" + log_extra + "\n"
files["foundations/invariants.md"] = t.INVARIANTS.replace("## Withdrawn", inv_extra + "\n\n## Withdrawn")
for path, text in files.items():
    full = os.path.join(root, *path.split("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as h:
        h.write(text)
print("sizes", os.path.getsize(os.path.join(root, "foundations", "decisions.md")),
      os.path.getsize(os.path.join(root, "foundations", "invariants.md")))
g = ["git", "-c", "user.name=Gate", "-c", "user.email=gate@example.com", "-c", "core.autocrlf=false"]
subprocess.run(g + ["init", "-q", "-b", "main"], cwd=root, check=True)
subprocess.run(g + ["add", "-A"], cwd=root, check=True)
subprocess.run(g + ["commit", "-q", "-m", "p"], cwd=root, check=True)
for options in (["--merge-onto", "none"], ["--merge-onto", "HEAD"]):
    start = time.monotonic()
    r = subprocess.run([sys.executable, "-B", os.path.join(the_way, "product-guidelines", "form_check.py"), root] + options,
                       capture_output=True, env=dict(os.environ, PYTHONIOENCODING="utf-8"))
    print(options, "exit", r.returncode, "seconds %.1f" % (time.monotonic() - start))
    print(r.stdout.decode("utf-8")[-1500:])

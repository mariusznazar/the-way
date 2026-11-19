import io, subprocess, tokenize
base, head = "6c13454c", "015ce05c"
files = subprocess.run(["git","diff","--name-only",base+".."+head],capture_output=True,text=True,check=True,cwd="..\..").stdout.split()
def comments(rev, f):
    src = subprocess.run(["git","show",rev+":"+f],capture_output=True,check=True,cwd="..\..").stdout.decode("utf-8")
    return [t.string.rstrip() for t in tokenize.generate_tokens(io.StringIO(src).readline) if t.type == tokenize.COMMENT]
bad = 0
for f in files:
    a, b = comments(base, f), comments(head, f)
    if a != b:
        bad += 1; print("COMMENTS DIFFER", f, len(a), len(b))
print("files", len(files), "comment-differ", bad)

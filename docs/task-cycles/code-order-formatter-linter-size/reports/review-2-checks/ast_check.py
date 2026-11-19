import ast, subprocess, sys
base, head = "6c13454c", "015ce05c"
files = subprocess.run(["git","diff","--name-only",base+".."+head],capture_output=True,text=True,check=True).stdout.split()
same = differ = 0
for f in files:
    a = subprocess.run(["git","show",base+":"+f],capture_output=True,check=True).stdout
    b = subprocess.run(["git","show",head+":"+f],capture_output=True,check=True).stdout
    ta = ast.dump(ast.parse(a), include_attributes=False)
    tb = ast.dump(ast.parse(b), include_attributes=False)
    if ta == tb: same += 1
    else:
        differ += 1; print("DIFF", f)
print("files", len(files), "same", same, "differ", differ)

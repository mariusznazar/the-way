import re
m={str(n):str(n+5) for n in range(355,361)}
text="WAY-355 and WAY-360 and WAY-35 and WAY-3550 and WAY-359."
out=re.sub(r"WAY-(\d+)\b",lambda x:"WAY-"+m.get(x.group(1),x.group(1)),text)
print(out)
assert out=="WAY-360 and WAY-365 and WAY-35 and WAY-3550 and WAY-364."

import ast,sys
def top(path):
    t=ast.parse(open(path,encoding='utf-8').read())
    d={}
    for n in t.body:
        if isinstance(n,(ast.FunctionDef,ast.ClassDef)): k=n.name
        elif isinstance(n,ast.Assign): k=ast.unparse(n.targets[0])
        elif isinstance(n,ast.AnnAssign): k=ast.unparse(n.target)
        else: continue
        d[k]=ast.dump(n)
    return d
old=top('.runs/review-13/old.py'); a=top('task-cycle/cycle_stages.py'); b=top('task-cycle/stage_transcripts.py')
new={**a,**b}
print("dup",set(a)&set(b))
for k in old:
    if k not in new: print("MISSING",k)
    elif old[k]!=new[k]: print("DIFF",k)
for k in new:
    if k not in old: print("NEW",k)

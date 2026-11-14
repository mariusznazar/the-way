import re, sys
text = open('foundations/decisions.md', encoding='utf-8', newline='').read().split('\n')
def span(n):
    pat = re.compile(r'^### WAY-%s — ' % n)
    for i, l in enumerate(text):
        if pat.match(l):
            j = i + 1
            while j < len(text) and not text[j].startswith('### ') and not text[j].startswith('## '):
                j += 1
            return i + 1, j
    return None
out = []
for n in sys.argv[2:]:
    s, e = span(n)
    out.append('<<<< WAY-%s lines %d-%d' % (n, s, e))
    out.extend(text[s-1:e])
open(sys.argv[1], 'w', encoding='utf-8', newline='\n').write('\n'.join(out))

from pathlib import Path
import re
import textwrap

root = Path('C:/Storage/repos/the-way-wt/guidelines-research')
for kind in ('coding', 'styleguide', 'testing'):
    path = root / f'product-guidelines/{kind}/SKILL.md'
    raw = path.read_bytes().decode('utf-8')
    newline = '\r\n' if '\r\n' in raw else '\n'
    text = raw.replace('\r\n', '\n')
    text = re.sub(r'(?<=\S) {2,}', ' ', text)
    text = text.replace('in this task\n  (WAY-', 'in this task (WAY-')
    # Reflow affected top-level bullets only, leaving sublists unchanged.
    pattern = r'^- (?:\*Context\*|Ask, as one question|For the first|Where research ran|\*\*Trial run\*\*|Hand back to).*?(?=^\S|\n\n|\Z)'
    def reflow(match):
        value = match.group().rstrip()
        joined = ' '.join(value.split())
        return textwrap.fill(joined, width=98, subsequent_indent='  ', break_long_words=False, break_on_hyphens=False) + ('\n' if match.group().endswith('\n') else '')
    text = re.sub(pattern, reflow, text, flags=re.M | re.S)
    if not text.endswith('\n'):
        text += '\n'
    path.write_bytes(text.replace('\n', newline).encode('utf-8'))
print('Formatted affected bullets')
